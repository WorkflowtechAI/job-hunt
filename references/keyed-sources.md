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

## Where the key lives

An environment variable, read at run time:

```
FOORILLA_API_KEY
```

From the shell environment, or from `~/job-hunt/.env` in the working folder.
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
- **The run JSON.** Those get pasted into the dashboard, dropped into chats, and
  kept as history.
- **`dashboard.html`.** It has no network code, and adding any would break the
  one claim about it that is unambiguously true.

Never print, echo, or return the value either. When the variable is missing, the
whole of the correct response is: *set `FOORILLA_API_KEY` in your job-hunt env
file.* Do not go looking for it, do not read it back to confirm it, and do not
suggest pasting it into the chat.

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
