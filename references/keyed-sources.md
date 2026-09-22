# Keyed sources

Optional. The search runs fully without any of this, and nothing here is a
default.

Some sources have a paid tier that returns listings programmatically instead of
a page at a time. Where someone already pays for one, the search should use it.
Where they do not, the search should never bring it up again.

## Foorilla

Runs `aijobs.net` (AI, ML and data roles), which is free to browse, free to
apply through, and exports a filtered search as CSV or JSON with no account.
**That free path is the one in `sourcing-map.md`, and it is enough.**

Their API is the keyed version of the same data.

| | |
|---|---|
| What the key buys | Programmatic access to listings, salary data, and the other foorilla spaces, instead of exporting a filtered page |
| Cost | API access requires an active PRO+ subscription, **$64/month** as of 2026-08-27. PRO first, then upgrade to PRO+ |
| Base URL | `https://foorilla.com/api/v1/` |
| Docs | `https://foorilla.com/api/v1/docs` |
| Auth | Header `Api-Key: <key>`, or `?api_key=<key>`. Prefer the header |
| Rate limits | 600 requests per minute, 5 per second |
| Paging | `page`, and `page_size` from 1 to 1000 |
| No key needed | `/core/metadata/`, which returns field labels |
| Data licence | **CC BY-SA 4.0.** Credit foorilla, link the licence, and note changes anywhere their data is republished. A private shortlist is not publishing; a blog post or a product is |

Their separate **jobdata API** at `jobdataapi.com` is a different, much larger
product, priced from $345/month. It is out of scope here.

Also free and unkeyed, and already in `sourcing-map.md`: their CC0 salary
dataset at
`https://raw.githubusercontent.com/foorilla/ai-jobs-net-salaries/main/salaries.csv`.

## TypeSafe (Jev)

Jev is TypeSafe's System One API: one typed yes/no question in, one number
from 0 to 1 out. In this package it does one job, the semantic skill match in
`scripts/jev_match.py`, which asks it, per skill in `forms.md`, whether a
posting calls for that skill. `jev-selection.md` says how the score uses the
answer and what the measurement behind it shows. Nothing else in the package
touches it, and the search scores every posting by the rubric without it.

| | |
|---|---|
| What the key buys | A `wants` number per skill per posting, as evidence for the Craft and Domain and stack dimensions of the score. Never the score itself |
| Cost | **$0.042 per million input tokens** as of 2026-09-17. The twelve-posting benchmark run, 8,916 decisions, cost $0.0328 |
| Base URL | `https://api.typesafe.ai/v1/systemone` |
| Auth | Header `Authorization: Bearer <key>` |
| Model | `jev-latest`. `JEV_MODEL` in the environment overrides it |
| What it sends | The posting text, up to 12,000 characters, and the skill names, one question each. Nothing from `profile.md`, and never the four self-identification rows |
| What it writes | `jev-match.json` beside the posting: one row per skill with `wants` and years, plus how many skills were asked and answered, how many batches failed, seconds and tokens, so a thin result shows. The key is never in it, and no path is |

The four behaviour rules below apply unchanged. In this script's terms: no key
is one line on stderr, exit 0, and nothing written; a failed batch is named on
stderr and skipped, never written as 0; and the answer is one input to two
dimensions of the score, never the score and never a gate.

## Where the key lives

An environment variable, read at run time:

```
FOORILLA_API_KEY
TYPESAFE_API_KEY
```

From the shell environment, or from `.env` in your job-hunt folder: the script finds it beside the posting or in any folder above it, then in the current folder, then at `~/job-hunt/.env`; `TYPESAFE_ENV` can name the file outright.
That file is gitignored:

```
# ~/job-hunt/.gitignore
.env
```

The README tells people to keep the working folder in a private git repo, so
this matters even when the repo is private. Private is not the same as intended
for version control.

### Three places a key never goes

- **`profile.md`.** It is a file destined for version control.
- **The run JSON, and `jev-match.json`.** Those get pasted into the dashboard,
  dropped into chats, and kept as history.
- **`dashboard.html` and `resume.html`.** Neither has network code, and
  `resume.html` carries a content-security-policy header that would block a
  request anyway. Adding network code to either would break the one claim about
  them that is unambiguously true.

A name with nothing after the equals sign is not a key. The lookup treats
`TYPESAFE_API_KEY=`, `TYPESAFE_API_KEY=""` and a whitespace-only value as
absent, and goes on to the next file rather than taking the next line. That
reads like pedantry and is not: an env file holds more than one secret, and a
lookup that can slide off its own line forwards whichever one sits below it to
whoever the key was for.

Never print, echo, or return the value either. When the variable is missing, the
whole of the correct response is: *set `FOORILLA_API_KEY` or `TYPESAFE_API_KEY`
in your job-hunt env file.* Do not go looking for it, do not read it back to
confirm it, and do not suggest pasting it into the chat.

## How a keyed source behaves

Four rules, and the first is the one that matters.

**An absent key degrades silently to the free channels.** Mention it once, during
the intake, and never again. A skill that nags about a paid upgrade every Monday
gets uninstalled, and it would be nagging on behalf of someone else's business.

**A keyed source is still one input among many.** Same rule the job-board
connector gets in `sourcing-map.md`. Paying for an index does not make it the
search, and a run that leans on it stops finding what it does not carry.

**Provenance is judged on the record, not the price.** A listing from an
ATS-sourced API gets `sourceType: "company-site"` only where the record actually
carries the employer's own posting URL. Where it hands back an aggregator link,
it is `"job-board"`, key or no key. An expensive API is not evidence about where
a link points.

**Every other rule still applies.** Confirm each posting is live. Record the
hiring employer in `company`, never the intermediary. Score against the profile
like anything else.

## Adding another one

Copy the Foorilla row shape: what the key buys, the cost with the date it was
checked, base URL, auth header, limits, licence, and the environment variable
name. Then the same four behaviour rules, unchanged, because they are what keep
an optional paid source from quietly becoming a requirement.
