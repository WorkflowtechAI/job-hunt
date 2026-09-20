"""Which of your skills does this posting actually call for?

    python <skill folder>/scripts/jev_match.py applications/<dir>/posting.md
    python <skill folder>/scripts/jev_match.py posting.md --skills skills.txt --top 40
    python <skill folder>/scripts/jev_match.py posting.md --repeat 3

Run from any folder. The posting's path is what matters: the script looks
for forms.md, skills.txt and .env beside the posting and in every folder
above it, so a posting under applications/ inside your job-hunt folder finds
that folder's files on its own.

Optional, and key-gated. With no TYPESAFE_API_KEY this prints one line and
exits 0; the skill scores by the rubric exactly as it would without this
file. With a key it asks Jev one yes/no question per skill, with the posting
as the only state:

    Does this posting call for "<skill>", either by name or by describing
    work that requires it?

What leaves your machine: the posting text (up to 12,000 characters) and the
skill names. Nothing from profile.md. From forms.md, only the first two
columns of the "Years by named skill" table; the self-identification rows
are never read.

The skill list, in order of preference:

    --skills FILE        a forms.md (its years table), or a plain text file
                         with one skill per line, optionally "skill | years"
    forms.md             beside the posting or above it, then in the cwd
    skills.txt           the same places, one skill per line

Output: jev-match.json beside the posting (or --out), rows of skill, wants
(0 to 1) and years, sorted by wants, plus a "wanted, and not yet held" list:
wants of 0.60 or more where years is blank, none, 0, a dash, n/a or no. The
file also records how many skills were asked and answered, how many batches
failed, the seconds taken and the tokens used, so a thin result can be told
from a clean one. It never writes a score; the assistant still does that.

Exit codes: 0 written (or no key, nothing written); 1 every batch failed,
nothing written; 2 no posting or no skill list, nothing written. A failed
batch is named on stderr. No skill is ever recorded as 0 because a call
failed: an unanswered question is absent, not a zero.
"""
import argparse
import io
import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev_client as jev                                       # noqa: E402

BATCH = 60
WANTED = 0.60
MAX_STATE = 12000
QUESTION = ('Does this posting call for "%s", either by name or by '
            'describing work that requires it?')
WHEN_TRUE = "The posting asks for it or for work that needs it"
WHEN_FALSE = "The posting does not need it"
NOT_HELD = ("", "none", "0", "-", "n/a", "no")


def read_table(text):
    """(skill, years) rows from the 'Years by named skill' table of a forms.md.

    Reads the first two columns of the first table under that heading and
    nothing else in the file. Rows with an empty skill cell are skipped.
    """
    head = re.search(r"^##\s+Years by named skill\s*$", text, re.M | re.I)
    if not head:
        return []
    body = text[head.end():]
    nxt = re.search(r"^##\s", body, re.M)
    if nxt:
        body = body[:nxt.start()]
    rows, seen_header = [], False
    for line in body.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not seen_header:
            seen_header = True                  # the header row
            continue
        if all(re.fullmatch(r":?-+:?", c or "-") for c in cells):
            continue                             # the separator row
        if not cells or not cells[0]:
            continue
        years = cells[1] if len(cells) > 1 else ""
        rows.append((cells[0], years))
    return rows


def read_lines(text):
    """(skill, years) rows from a plain list: one per line, 'skill | years' allowed."""
    rows = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        parts = [p.strip() for p in s.split("|")]
        rows.append((parts[0], parts[1] if len(parts) > 1 else ""))
    return rows


def folders_near(posting):
    """The posting's folder and every folder above it, then the cwd."""
    out, p = [], posting.resolve().parent
    while True:
        out.append(p)
        if p.parent == p:
            break
        p = p.parent
    cwd = Path.cwd().resolve()
    if cwd not in out:
        out.append(cwd)
    return out


def load_skills(path, posting):
    """Rows from an explicit file, or from forms.md / skills.txt near the posting."""
    if path:
        candidates = [Path(path)]
    else:
        candidates = [d / name for d in folders_near(posting)
                      for name in ("forms.md", "skills.txt")]
    for p in candidates:
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        rows = read_table(text) if p.suffix.lower() == ".md" else read_lines(text)
        if rows:
            return rows, p
        if path:
            break
    return [], None


def point_at_env(posting):
    """Let the client find a .env beside the posting or above it.

    The client reads TYPESAFE_API_KEY from the environment, then TYPESAFE_ENV,
    then .env in the cwd and ~/job-hunt/.env. A job-hunt folder that is none
    of those still holds its .env next to profile.md, so this walks up from
    the posting and names the first .env that carries the key.
    """
    if os.environ.get("TYPESAFE_API_KEY") or os.environ.get("TYPESAFE_ENV"):
        return
    for d in folders_near(posting):
        f = d / ".env"
        try:
            text = io.open(f, encoding="utf-8-sig").read()
        except OSError:
            continue
        if re.search(r"^\s*(?:export\s+)?TYPESAFE_API_KEY\s*=", text, re.M):
            os.environ["TYPESAFE_ENV"] = str(f)
            return


def held(years):
    """True when the years cell says the skill is actually held."""
    return (years or "").strip().lower() not in NOT_HELD


def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")

    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("posting", help="the posting, as saved by the apply pack")
    ap.add_argument("--skills", default="", help="forms.md or a one-per-line list")
    ap.add_argument("--top", type=int, default=30, help="rows to print (the file holds all)")
    ap.add_argument("--repeat", type=int, default=1,
                    help="ask this many times and report the spread")
    ap.add_argument("--out", default="", help="default: jev-match.json beside the posting")
    ap.add_argument("--json", action="store_true", help="print the result as JSON")
    a = ap.parse_args()

    posting = Path(a.posting)
    if posting.exists():
        point_at_env(posting)
    if not jev.have_key():
        print("no TYPESAFE_API_KEY; score by the rubric as usual", file=sys.stderr)
        return 0
    if not posting.exists():
        print("no such posting: %s" % posting, file=sys.stderr)
        return 2
    skills, source = load_skills(a.skills, posting)
    if not skills:
        print("no skill list: pass --skills, or keep a 'Years by named skill' "
              "table in forms.md or one skill per line in skills.txt beside "
              "the posting or above it", file=sys.stderr)
        return 2

    state = {"job_posting": posting.read_text(encoding="utf-8",
                                              errors="replace")[:MAX_STATE]}
    years_of = {s: y for s, y in skills}
    names = list(years_of)
    batches = (len(names) + BATCH - 1) // BATCH

    t0 = time.time()
    wants, spreads, failed = {}, {}, 0
    tokens = {"input": 0, "output": 0}
    for i in range(0, len(names), BATCH):
        chunk = names[i:i + BATCH]
        qs = {"q%d" % n: jev.noul(QUESTION % s, WHEN_TRUE, WHEN_FALSE)
              for n, s in enumerate(chunk)}
        if a.repeat > 1:
            ans, usage, err, _worst = jev.ask_stable(state, qs, repeat=a.repeat)
        else:
            ans, usage, err = jev.ask(state, qs)
        if err:
            failed += 1
            print("  batch %d of %d failed, skipped: %s"
                  % (i // BATCH + 1, batches, err), file=sys.stderr)
            continue
        for k in ("input", "output"):
            v = (usage or {}).get(k + "_tokens")
            if isinstance(v, (int, float)):
                tokens[k] += int(v)
        for n, s in enumerate(chunk):
            v = ans.get("q%d" % n) or {}
            if isinstance(v.get("noul"), (int, float)):
                wants[s] = float(v["noul"])
                if "spread" in v:
                    spreads[s] = v["spread"]
    dt = time.time() - t0

    if not wants:
        print("every batch failed (%d of %d); nothing written" % (failed, batches),
              file=sys.stderr)
        return 1

    rows = [{"skill": s, "wants": round(w, 3), "years": years_of.get(s, ""),
             **({"spread": spreads[s]} if s in spreads else {})}
            for s, w in wants.items()]
    rows.sort(key=lambda r: -r["wants"])
    gaps = [r for r in rows if r["wants"] >= WANTED and not held(r["years"])]
    result = {
        "posting": posting.name, "skills_from": source.name,
        "asked": len(names), "answered": len(rows),
        "batches": batches, "batches_failed": failed,
        "seconds": round(dt, 2), "tokens": tokens,
        "wanted_floor": WANTED,
        "matches": rows, "wanted_not_held": gaps,
    }

    out = Path(a.out) if a.out else posting.with_name("jev-match.json")
    out.write_text(json.dumps(result, indent=1, ensure_ascii=False) + "\n",
                   encoding="utf-8")

    if a.json:
        print(json.dumps(result, indent=1, ensure_ascii=False))
        return 0

    print("asked about %d skills, %d answered, %.1fs, %d tokens in, %d out%s"
          % (len(names), len(rows), dt, tokens["input"], tokens["output"],
             ("  (%d of %d batches failed)" % (failed, batches)) if failed else ""))
    print("  wants  years  skill")
    for r in rows[:a.top]:
        print("  %.2f   %-5s  %s%s" % (r["wants"], (r["years"] or "-")[:5],
                                       r["skill"][:44],
                                       ("  (spread %.2f)" % r["spread"])
                                       if "spread" in r else ""))
    if gaps:
        print("\n  wanted, and not yet held:")
        for r in gaps[:12]:
            print("    %.2f  %s" % (r["wants"], r["skill"]))
    print("\nwrote %s" % out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
