# Jev-scored skill selection

Optional. The search scores every posting by the rubric without any of this,
and nothing here is a default.

## What it is

A second reading of a posting, by a model that answers one typed yes/no
question at a time with a number from 0 to 1. Jev, TypeSafe's System One API,
calls that question a noul. There is no prose to parse and no prompt to tune.
The question is fixed, the answer is a number, and the number is evidence.

The question, asked once per skill in the table, held or not:

> Does this posting call for "<skill>", either by name or by describing work
> that requires it?

With two criteria attached. True: the posting asks for it or for work that
needs it. False: the posting does not need it. Questions go in batches of 60.

The point is the second half of the question. A keyword filter sees
"Microsoft 365" only when the posting spells it that way. This sees it when
the posting says "M365", and sees PowerShell when the posting asks for
"scripting against our tenant". Its reach has a limit the question itself
sets: it asks whether the work requires the skill, not whether the work
resembles it. A posting that wants infrastructure as code without naming a
tool scored Terraform at about 0.40 in a test written to catch exactly that,
below the line. Read a miss on an unnamed tool as "not established", not as
"not wanted".

## When it runs

Only with the person's own TypeSafe key. `keyed-sources.md` says where the key
lives and how a keyed source behaves, and the rule that matters most is the
first one: the key is mentioned once, at intake, alongside the other keyed
sources, and never again. Without a key the script prints one line on stderr
(`no TYPESAFE_API_KEY; score by the rubric as usual`), exits 0, writes nothing,
and the posting is scored by the rubric exactly as before.

```
python <skill folder>/scripts/jev_match.py applications/<dir>/posting.md [--skills FILE] [--top N] [--repeat N] [--out FILE] [--json]
```

The script lives where the skill is installed (`~/.claude/skills/job-hunt/`
in the setup steps), not in your job-hunt folder, and runs from any folder.
The posting's path is what matters: the script looks beside the posting and
in every folder above it, so a posting under `applications/` in your job-hunt
folder finds that folder's `forms.md` and `.env` on its own.

The skill list comes from `--skills FILE`, or by default from the "Years by
named skill" table in `forms.md`, found beside the posting or above it, then
in the current folder: column one is the skill, column two the years. A
plain text file with one skill per line, such as `skills.txt`, also works,
and a line may carry `skill | years`. That table is the only part of
`forms.md` the script reads. `--top N` limits the printed rows (30 by
default; the file always holds every row), and `--json` prints the same
result as JSON instead of the table.

## What leaves the machine

Two things. The posting text, up to 12,000 characters. And the skill names, one
per question. That is the whole request.

Not sent: anything from `profile.md`, the résumé, the years column, the run
file, and the four self-identification rows of `forms.md`, which the script
never reads. The key goes in an `Authorization: Bearer` header on a request to
`https://api.typesafe.ai/v1/systemone`. It is read from `TYPESAFE_API_KEY` in
the shell environment; failing that, from the file named by `TYPESAFE_ENV`;
failing that, from a `.env` beside the posting or in any folder above it,
which is how the `.env` next to `profile.md` is found; and last from `.env` in
the current folder or `~/job-hunt/.env`. The model is `jev-latest`;
`JEV_MODEL` in the environment overrides it.

`scripts/jev_match.py`, with `scripts/jev_client.py` beside it, is the only
code in the package that sends anything off your machine. Read it before
trusting it. It is short.

## What comes back

`jev-match.json`, written beside the posting, or wherever `--out` points. One
row per skill: `skill`, `wants` (0 to 1), `years` from the table, blank where
the list carried none, and `spread` under `--repeat`. Sorted by `wants`,
highest first.

Beneath the rows, a **"wanted, and not yet held"** list: every skill with
`wants` at or above 0.60 whose `years` is blank, `none`, `0`, a dash, `n/a`
or `no`. That list is the posting's gaps, in the posting's own order of
priority.

The file also records the posting's file name, the name of the skill list it
read (never its path), how many skills were `asked` and `answered`, how many
`batches` there were and how many `batches_failed`, the `seconds` taken and
the `tokens` used. Read `answered` against `asked` before trusting an empty
gaps list: a thin result and a clean one look the same in the rows.

Exit codes. 0: written, or no key and nothing written. 1: every batch failed,
nothing written, each failure named on stderr. 2: no such posting, or no
skill list, nothing written. A batch that fails while others succeed is named
on stderr, counted in `batches_failed`, and skipped. No skill is ever written
as 0 because a request failed. A missing row means not asked, the same way a
null score means not read.

## How the rubric consumes it

`wants` is evidence for two of the six dimensions in `scoring-rubric.md`:
**Craft match (35)** and **Domain and stack (15)**. The assistant still reads
the posting and still writes the score. Level fit, location and authorization,
compensation and reachability do not see it. Pay still ranks and never gates.

A high `wants` on a skill the person holds supports the craft or domain score
already being written. A high `wants` on a skill they lack is a domain bullet
they cannot touch, and the rubric's four-bullet rule applies as before.

A Jev failure is at most a `scoreNote`. It is never a number, never a null
score, and never a reason to drop the posting. The run-file shape and
`dashboard.html` do not change.

## Two other readers

**`apply-pack.md`, lens 2.** The keyword filter marks each named term present,
present in other words, or absent. `wants` is the semantic side of that table:
the terms the posting asks for by describing the work rather than naming it.
"Add only what is true" still decides what goes on the résumé.

**`interview-prep.md`, section 2.** The requirement list as a question bank.
The "wanted, and not yet held" list ranks first, because those are the
questions with no experience behind the answer, and section 7 of that file is
where each one gets its honest line.

## Working rules, from measurement

**Send the whole posting.** The state is the posting text, not a summary of
it. In measurement, a 700-character headline in place of the full posting moved
11 of 30 answers by 0.20 or more.

**Repeat near the line.** Identical runs differ. In a 25-question measurement
the mean spread was 0.015 and the largest 0.040; a later run saw 0.05, so
treat those as typical, not as a ceiling. `--repeat 3` asks three times and
prints the spread. A skill at 0.58 or 0.62 deserves it. A skill at 0.20 or
0.90 does not.

**Read 0.60 as yes.** A noul is bimodal: most answers land well above or well
below the line, and the line is 0.60. Do not read 0.45 as "somewhat wanted".

**It demotes. It has not rescued.** In measurement a semantic layer has only
moved postings down, by finding wanted skills the person lacks. It has not
moved one up by finding a match the keyword pass missed. So a wanted skill the
person lacks is a gap to name, not a bullet to write, and nothing here adds
anything to a résumé.

## The measurement

The benchmark: https://iambraun.com/jevreports/skill-selection/, 17 September
2026, jev-1.13.0. Five arms, 743 skills against 12 postings, 8,916 decisions
per arm.

240 of the hardest skill-to-posting pairs were adjudicated twice; on the 215
where both passes agreed, Jev's AUC is 0.793, against 0.732 for GLM-5.3-flash
and 0.384 for Haiku 4.5. On the 95 unambiguous rows Jev reaches 0.937. Each
decision takes 11.7 ms. All 8,916 decisions cost $0.0328, against $0.0429 for
GLM and $0.5504 for Haiku. Jev lost no answers. Haiku lost 572.

Every limit the report states, so the numbers are not read as more than they
are:

- Twelve postings, from one candidate, in one month, skewed to pre-sales and
  MSP (managed service provider) roles. A different field may land differently.
- The adjudicators are Claude-family models, not humans.
- The 240 adjudicated pairs are the hardest ones, so that AUC is a floor, not
  an average.
- Against a free substring match, Jev is ahead but not statistically separated
  (p = 0.146).
- On a coarser domain-label metric, GLM leads: 0.681 against 0.614, p = 0.0063.
- The cost counts input tokens only. Charging output at the same rate would
  make it $0.0395.
- GLM's numbers depend on its `reasoning_effort` being pinned.

The harness that produced the report is available from the author on request.
It is not in this package.
