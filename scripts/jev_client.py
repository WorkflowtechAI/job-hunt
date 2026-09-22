"""The one place that talks to Jev: the key, the endpoint, the call.

Jev is TypeSafe's System One API. You send one state (here, a job posting)
and many typed questions about it; you get typed numbers back, so there is
nothing to parse and nothing to retry. Three question types:

    noul    is this true?                 answered as a 0 to 1 confidence
    score   where on this ladder?         an ordered set of levels
    choice  which of these?               one of a fixed set

This module never prints or returns the key. `ask` takes the questions and
returns the answers; the credential does not leave here, and no error string
carries the header.

The key comes from, in order:

    1. TYPESAFE_API_KEY in the shell environment
    2. the file named by TYPESAFE_ENV, if that variable is set
    3. .env in the current folder, then ~/job-hunt/.env

The .env file is the same one keyed-sources.md documents for the other
optional key. One line: TYPESAFE_API_KEY=...
"""
import io
import json
import os
import re
import time
import urllib.error
import urllib.request

ENDPOINT = "https://api.typesafe.ai/v1/systemone"
MODEL = os.environ.get("JEV_MODEL", "jev-latest")

def key_files():
    """Where a key file may sit, resolved at call time so a caller that sets
    TYPESAFE_ENV after import (jev_match.py does, once it knows where the
    posting lives) is honoured."""
    return [os.environ.get("TYPESAFE_ENV") or "",
            os.path.join(os.getcwd(), ".env"),
            os.path.join(os.path.expanduser("~"), "job-hunt", ".env")]


def have_key():
    """True when a key is readable, without handing it to the caller.

    Agrees with `ask()` by construction: both treat an empty value as no key,
    because `_key()` returns None rather than "" for one.
    """
    return _key() is not None


# HORIZONTAL WHITESPACE ONLY, and a value that cannot be empty. The obvious
# r"KEY\s*=\s*(.+?)\s*$" is wrong in a way that leaks: \s matches newlines, so
# against a line reading "TYPESAFE_API_KEY=" with nothing after the equals, the
# match walks on to the NEXT line of the file and returns it whole. Measured
# against "TYPESAFE_API_KEY=\nOTHER_SECRET=hunter2": it returned
# 'OTHER_SECRET=hunter2', which ask() would then put in the Authorization
# header and send. An .env holds more than one secret, and that is the point of
# the bug rather than a detail of it. [ \t] cannot cross a line and . never
# matches a newline, so the value is always the one on the key's own line.
_KEY_LINE = re.compile(
    r"^[ \t]*(?:export[ \t]+)?TYPESAFE_API_KEY[ \t]*=[ \t]*(.*)$", re.M)


def _from_text(text):
    """The first line that names the key AND carries a value, or None.

    Every match, not just the first: an env file edited by hand often keeps an
    old `TYPESAFE_API_KEY=` above the real one. Stopping at the first match
    would report no key at all while a working one sat two lines below, which
    is a confusing failure rather than a dangerous one, and still worth not
    having.
    """
    for m in _KEY_LINE.finditer(text):
        value = m.group(1).strip().strip('"').strip("'").strip()
        if value:
            return value
    return None


def _key():
    env = os.environ.get("TYPESAFE_API_KEY", "").strip()
    if env:
        return env
    for path in key_files():
        if not path:
            continue
        try:
            with io.open(path, encoding="utf-8-sig") as fh:
                text = fh.read()
        except OSError:
            continue
        except ValueError:
            # A file that is not UTF-8 raises UnicodeDecodeError, which is a
            # ValueError and is not caught by OSError. Letting it out would
            # break the promise every caller relies on: degrade, never raise.
            # A file that cannot be read is a file without the key in it.
            continue
        found = _from_text(text)
        if found:
            return found
    return None


def ask(state, questions, timeout=120, model=None):
    """One call, many questions, all evaluated against the same state.

    Returns (answers, usage, error). `error` is None on success and a short
    string otherwise, never an exception: every caller degrades rather than
    dies, and the string never carries the key.
    """
    key = _key()
    if not key:
        return {}, {}, "no TYPESAFE_API_KEY"
    if not questions:
        return {}, {}, None

    body = json.dumps({"state": state, "model": model or MODEL,
                       "questions": questions}).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=body,
        headers={"Authorization": "Bearer " + key,
                 "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            payload = json.load(r)
    except urllib.error.HTTPError as e:
        return {}, {}, "HTTP %d: %s" % (e.code, e.read().decode("utf-8", "replace")[:300])
    except Exception as e:                                  # noqa: BLE001
        return {}, {}, "%s: %s" % (type(e).__name__, e)

    return payload.get("answers") or {}, payload.get("usage") or {}, None


def nouls(answers):
    """The numeric answers, skipping anything malformed."""
    out = {}
    for name, a in answers.items():
        if isinstance(a, dict) and isinstance(a.get("noul"), (int, float)):
            out[name] = float(a["noul"])
    return out


# STATE SIZE. Send the whole posting. The API docs advise trimming state to
# what the questions need, and that is right when the state is a haystack (a
# long history, of which any one question touches a sliver). A job posting is
# the subject of every question asked about it, so trimming deletes evidence:
# measured against one posting, cutting it to a 700-character headline moved
# 11 of 30 answers by 0.20 or more and produced confident wrong answers.
# references/jev-selection.md carries the numbers.

def score(criteria, instructions):
    """A rating on an ordered ladder. 2 to 10 levels, low to high."""
    return {"type": "score", "instructions": instructions, "criteria": criteria}


def noul(instructions, when_true="", when_false=""):
    """Is this true? Answered as a 0 to 1 confidence."""
    q = {"type": "noul", "instructions": instructions}
    if when_true or when_false:
        q["criteria"] = {"true": when_true, "false": when_false}
    return q


def choice(options, instructions):
    """Pick one of a fixed set."""
    return {"type": "choice", "instructions": instructions, "criteria": options}


def normalize(answer):
    """A score as 0 to 1: the level divided by the top level of its ladder."""
    legend = answer.get("legend") or {}
    top = max((int(k) for k in legend), default=0)
    return (answer.get("score", 0) / top) if top else 0.0


def ask_stable(state, questions, repeat=3, pause=0.15, timeout=120, model=None):
    """Average several calls, for any number a threshold will act on.

    Jev is not deterministic. Measured: the same 25 questions against the
    same state returned identical answers 4 times out of 25, mean spread
    0.015, largest 0.040. Harmless until a cutoff decides something, where a
    value a few hundredths from the line joins or leaves a list between runs
    with no input change. Averaging makes that visible instead of silent.

    Returns (answers, usage, error, spread). The spread is the largest range
    seen on any answer, so a number sitting on a boundary shows up as one.
    """
    runs, usage, last_err = [], {}, None
    for i in range(max(1, repeat)):
        answers, u, err = ask(state, questions, timeout, model)
        if err:
            last_err = err
            continue
        runs.append(answers)
        usage = u
        if i + 1 < repeat:
            time.sleep(pause)
    if not runs:
        return {}, {}, last_err or "no successful call", 0.0

    out, worst = {}, 0.0
    for name, first in runs[0].items():
        merged = dict(first)
        field = "score" if "score" in first else "noul"
        vals = [r[name].get(field) for r in runs
                if name in r and isinstance(r[name].get(field), (int, float))]
        if vals:
            spread = max(vals) - min(vals)
            worst = max(worst, spread)
            merged[field] = sum(vals) / len(vals)
            merged["spread"] = round(spread, 3)
            merged["runs"] = len(vals)
        out[name] = merged
    return out, usage, None, round(worst, 3)
