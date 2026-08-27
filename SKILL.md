---
name: job-hunt
description: "Run a job and contract search as a repeatable loop. A one-time guided intake builds a candidate profile from the person's CV, then each run sources across job boards, ATS pages and talent platforms, scores every posting 0-100 against that profile, verifies each link is live, and writes a run file the local HTML dashboard reads. Per role, an apply pack runs an adversarial five-reader review of their résumé against the job description, produces a tailored résumé, and briefs what the cover letter must hit without drafting it. Also covers an interview answer bank, per-company interview prep, salary bands, contract outreach, and a weekly scoreboard. Two tracks: employment applications and contract engagements. Trigger on 'job search', 'find me jobs', 'refresh my jobs', 'run a search', 'rank these postings', 'am I a fit for this', 'review my resume', 'tailor my CV', 'apply pack', 'cover letter', 'application pipeline', 'render my resume', 'interview prep', 'what does this role pay', or 'contract work'."
---

# Job Hunt

A search loop you can run every week. The person owns the decisions; this skill
does the sourcing, the honest scoring, and the paperwork.

Two tracks run at the same time off one identity:

- **Track A, employment.** Applications to jobs someone posted.
- **Track B, contract.** Engagements you propose to a company that never posted
  anything.

Most people run only Track A and wonder why the pipeline is thin. The same
profile sells both ways.

## What this runs on

A folder of plain files. Default `~/job-hunt/`, anywhere works.

| File | What it is | Written by |
|---|---|---|
| `profile.md` | The candidate profile: identity, target roles, hard limits, honest claims | The intake, once. Edited whenever reality changes |
| `resume/master.md` | The master résumé as markdown: everything, in one file | The intake, once. Edited when a role or a number changes |
| `runs/<date>.json` | One search run: the scored shortlist | Each search |
| `applications/<date>-<company>-<role>/` | One application: the posting, the review, the tailored résumé, the letter brief, the change log | Each apply pack |
| `pipeline.json` | Application status per posting | Exported from the dashboard |

`dashboard.html` opens in a browser with no server and no install. Drop a run
file on it to see the shortlist; it tracks status per posting from there.

`resume.html` is its sibling. Drop `resume/master.md` or a tailored copy on it
and it renders the page, and the browser's own print dialog saves the PDF. No
install, no build step, no service. `references/resume-master.md` holds the
master résumé format and says why the render path is a browser rather than a
toolchain.

No account, no database, and no key required. Where the person already pays for
a source that has an API, the search uses it: `references/keyed-sources.md`,
which is optional and never a default. If the folder is in a private git repo,
the whole search is versioned and portable.

## First run: the intake

If `profile.md` does not exist, run the intake in `references/intake.md` before
searching. It asks questions one at a time and writes the profile at the end.

Read their CV or résumé first if they have one, then ask only what the CV cannot
tell you. Ten questions to someone who already handed you a document is how an
intake earns a reputation.

The profile is the whole game. A search against a thin profile returns the jobs
everyone else is also seeing, so when an answer comes back vague on something
load-bearing, push on it before moving on. The intake says where and how.

## The search loop

Run this end to end each time. It takes real work; a search that skips the
verification step produces a shortlist of dead links, which is worse than no
shortlist.

### 1. Anchor on the profile

Load `profile.md`. Every score in the run traces back to something in it. Where
the profile is silent, ask rather than assume, then write the answer back into
the profile so the next run knows.

Pay attention to the profile's **location and work authorization** block. It
decides which whole categories of role are even real. Getting this wrong in
either direction wastes the run: flagging an authorization barrier that does not
exist buries good roles, and ignoring one that does exist fills the shortlist
with jobs they cannot take.

### 2. Source wide

Full channel list and the rules for each: `references/sourcing-map.md`.

The short version: company career pages and ATS boards first, then talent and
contract platforms, then aggregators, then whatever job-alert email lands in
their inbox. A job-board MCP connector, when one is available, is **one input
among many**, never the search itself.

Fan out across angles rather than running one query deeper. Ten sources at one
page each beats one source at ten pages.

### 3. Score honestly

Rubric: `references/scoring-rubric.md`. Score 0-100 and write a one-line plain
verdict for each posting. No jargon in the verdict; it gets read at breakfast.

The rubric's core rule: **pay ranks, it does not gate.** Above the profile's
stated floor, every role is takeable, so compensation contributes to the score
the same way a closer role match does and never removes a posting from the list.
A ranker that hides the best thing currently available has failed rather than
protected anyone.

### 4. Verify every link

Fetch each posting before it goes in the run.

- Still open: keep it, set `live: true`, and set `postedDaysAgo` when the page
  shows a date.
- Expired, closed, removed, 404: set `live: false`. The dashboard drops these,
  so the shortlist never shows a dead job.
- Could not confirm it either way: that is `sourceType: "alert-only"`, **not**
  `live: false`. Those two are different facts and confusing them deletes real
  jobs. Surface it with the verdict saying it is unconfirmed.

Never silently bin a named role. A role you dropped without saying so is
indistinguishable, to the person reading, from a role that never existed.

### 5. Write the run file

```json
{
  "date": "2026-08-27",
  "track": "both",
  "focus": "optional one-line note on what this run went after",
  "postings": [
    {
      "title": "Forward Deployed Engineer",
      "company": "Actual Hiring Employer Inc",
      "url": "https://jobs.example.com/fde",
      "location": "Remote (US)",
      "salary": "$150,000 - $190,000",
      "jobType": "Full-time",
      "employmentType": "w2",
      "score": 84,
      "verdict": "Strong match. They want the discovery-to-rollout work you already do, and they name your stack.",
      "strengths": ["Owns POC through production", "Names MCP and evals"],
      "gaps": ["Wants Kubernetes depth you do not have"],
      "locationFit": "us-remote",
      "sourceType": "company-site",
      "postedAt": "2026-08-22",
      "postedDaysAgo": 5,
      "live": true
    }
  ]
}
```

`employmentType`: `w2` | `contract` | `unknown`.
`locationFit`: `global` (hires anywhere, or billable from anywhere) | `us-remote`
(remote but likely requires residence in the country) | `onsite` (relocation).
`sourceType`: `company-site` | `job-board` | `alert-only`.

A "remote US" posting usually means remote from inside the US. Treating it as
location-agnostic is the single most common scoring error.

Save to `runs/<date>.json`. Each run replaces the shortlist rather than adding to
a growing pile, so the dashboard shows the current search. Application status
already tracked in `pipeline.json` survives, keyed on the posting URL (or on
title + company + location when a posting has no usable link).

### 6. Hand it over

Open `dashboard.html`, drop the run file on it, and say what changed in one
paragraph: how many roles, the top three, and anything the person needs to decide.

## Per role: the apply pack

`references/apply-pack.md`, on request, for roles the person picks off the
shortlist. Never automatically for a whole run. Three outputs:

1. **An adversarial fit review.** Five hostile readers before anything is
   written: the six-second screen, the keyword filter, the hostile hiring
   manager, the comparison against the likely pool, and the gap hunter. It ends
   with a call, and "skip this one" is a real answer.
2. **A tailored résumé,** built from `resume/master.md` by reordering, rewording
   and cutting. Never by inventing. It lands as a file in the application's own
   folder, beside a change log that labels every edit, and renders to a PDF
   through `resume.html`. Chat text made the person retype it, and retyping is
   where invention gets in.
3. **A cover letter brief.** The points to hit, in order, with the evidence
   attached, what to address directly, and what to leave out.

**The brief is not the letter.** Writing the prose needs the person's own voice,
and a letter in a borrowed voice gets read back to them in an interview. Hand
over the brief and let them write from it, or let them pass it to whatever
writing tooling already sounds like them.

## Link hygiene

These rules are not fussiness. Each one comes from a run that failed.

**`company` is the hiring employer, always.** Never the aggregator, the alert
service, the staffing firm, or the talent platform the lead arrived through. A
run that writes the aggregator's name into `company` ships postings with no
traceable employer: nothing to search for, nothing to research before the
interview, and duplicate rows when the same role arrives through two
aggregators. When a lead comes through an intermediary, dig one layer further.
The intermediary's own listing almost always names the real employer. Name the
intermediary only when the employer truly cannot be determined, and treat that
as a sign to search harder rather than as an acceptable default.

**Paid job-seeker paywalls: drop the link.** Any board that gates viewing or
applying behind a subscription gets resolved to the employer's own posting, or
the lead gets dropped. Nobody should pay a toll to read about a job. A free
login is different: surface it and note the login in the verdict so the person
decides.

**Prefer the employer's own posting, keep the board listing when that is all
there is.** Search `<company> careers <title>` and link the ATS page when it
exists, with `sourceType: "company-site"`. When only the board has it, keep it,
link the board, and set `sourceType: "job-board"`. Freshness counts at least as
much as provenance. A live board listing today beats a company page found next
week.

**Respect the profile's exclusion list.** Companies, platforms and role types the
person has ruled out stay out, permanently, without re-litigation each run.

**Scraping stays inside the terms of service.** LinkedIn in particular: use its
job-alert emails rather than scraping the site. An account ban costs more than
any single lead is worth.

## Track A: employment

Target roles come from the profile, in fit order, with a matching **stop chasing**
list. The stop list does more work than the target list. It keeps the search from
drifting back toward the roles the person's résumé superficially matches and their
career has moved past.

**Requirement triage.** Split every posting into craft bullets and domain bullets.
Craft is the thing they do regardless of industry. Domain is the specific stack,
sector or product. Most people clear craft nearly everywhere and lose on domain.
Skip when the domain is the seat itself, roughly four or more domain bullets they
cannot touch. Apply when the domain gaps are learnable and the craft is a match.

**Years fields get the honest bounded number.** Where a form asks years of
experience in a thing, answer for that thing, and let the longer career do its
work in prose. Seniority inflation in postings ("7+ years of LLM experience" in a
field that age) is a template artifact, not a gate. Read it as "senior" and apply.

**Application and interview answers:** `references/answer-bank.md` builds the
person's reusable answers once, every one of them citing the numbers table in
`profile.md` as the single source of truth. `references/interview-prep.md` is
the per-company prep pattern for a specific scheduled interview.
`references/compensation.md` is how the salary field gets a researched number
instead of a guess.

Weekly target lives in the profile. Set it from time available, honestly. Fifteen
tailored applications beat forty pasted ones, and the pasted forty take longer.

## Track B: contract

`references/contract-track.md`. Prospects in nearness-to-revenue order, starting
with people who already know the person's work. Openers are personal, specific,
and short.

A company hiring for the work the person does is also a prospect for that work
delivered as a contract. Capture the company name from Track A sourcing even when
the posted role is a poor fit.

## Guardrails

1. **Never auto-apply.** A run produces a shortlist and stops. A human sends
   every application and every message. No exceptions, no "it was obviously a
   yes."
2. **Honest claims only.** No invented projects, no borrowed client stories, no
   inflated numbers, no credentials in progress described as held. Every claim
   has to survive the interview it gets the person into.
3. **Personal data stays local.** The profile, the CV, and the pipeline live in
   the person's folder. Do not post them anywhere.
4. **Never print, echo or return an API key.** Keys live in the environment, per
   `references/keyed-sources.md`, and never in `profile.md`, a run file, or the
   dashboard. When one is missing, the whole answer is "set `FOORILLA_API_KEY`
   in your job-hunt env file", not a hunt for it. An absent key degrades to the
   free channels silently.
5. **Plain language.** In anything the person reads: "searching", "found",
   "strong match", "apply". Jargon in a verdict is a small failure of respect.
6. **Say when the search came up short.** Three real roles is a result. Twenty
   padded ones is a waste of their week.

## Weekly scoreboard

Review every Friday. Track A: applications sent, responses, interviews. Track B:
openers sent, replies, calls, proposals. Both: offers.

When response rates undershoot by week three, change the message or change the
targets. Adding volume to a message that is not landing produces more silence.
