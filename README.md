# Job Hunt

A job and contract search you run as a loop instead of a panic. It is a skill for
an AI coding assistant plus a local HTML dashboard. Nothing to sign up for, no
server, no subscription, no third-party job-search service. Your files stay in
your folder, and your CV goes to whatever assistant you install this into, the
same as anything else you hand it.

Open `index.html` for the same thing as a page you can read in a browser.

## What it does

You bring your CV and fifteen minutes. It builds a candidate profile, and then
each run:

- sources roles across employer career pages, ATS boards, talent platforms, niche
  boards, aggregators, and your own job-alert emails
- scores every posting 0 to 100 against your profile, with a plain-English verdict
- opens each posting to confirm it is still live, and labels the ones it could
  not confirm rather than dropping them silently
- writes a run file the dashboard reads

For each role you pick off that shortlist, the **apply pack** runs five hostile
readers at your résumé against the job description (the six-second screen, the
keyword filter, the hostile hiring manager, the comparison against the likely
pool, the gap hunter), then builds a tailored résumé from your real one and a
brief of what your cover letter has to hit. It ends with a call, and *skip this
one* is a real answer.

The brief is deliberately not a letter. It carries the opening angle, the points
in order with evidence attached, what to address head-on and what to leave out.
You write the sentences, because a letter in a borrowed voice gets read back to
you in the interview.

It also builds a reusable interview answer bank, preps you for a specific
interview, researches real salary bands, and drafts contract outreach for your
review.

Two tracks run at once off the same profile: **employment** applications, and
**contract** engagements proposed to companies that never posted a job. Most
people run only the first and wonder why the pipeline is thin.

## Setup

**1. Install the skill.** Clone it straight into your assistant's skills
directory. For Claude Code:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/WorkflowtechAI/job-hunt.git ~/.claude/skills/job-hunt
```
```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
git clone https://github.com/WorkflowtechAI/job-hunt.git "$HOME\.claude\skills\job-hunt"
```

`git pull` in that folder later picks up changes. No git: download the ZIP from
GitHub and unpack it so that `~/.claude/skills/job-hunt/SKILL.md` exists. Watch
that step, because unpacking one level off is the one install mistake that fails
silently.

Restart the session and ask what skills it has. Other assistants that read a
skills or instructions folder work the same way; point yours at `SKILL.md`.

**2. Make your folder.** This is where your search lives, separate from the
skill.

```bash
mkdir -p ~/job-hunt/runs
cp ~/.claude/skills/job-hunt/dashboard.html ~/job-hunt/
```

Anywhere works. A private git repo is a good home: your whole search, versioned
and portable.

**3. Run the intake.** Point the assistant at your CV and say *"run the job-hunt
intake"*. It writes `~/job-hunt/profile.md`, which is plain markdown you can edit.

**4. First search.** Say *"refresh my jobs"*. It takes a while, because the
sourcing is wide and every posting gets checked. Then open `dashboard.html` and
drop the run file on it.

## Week to week

| Say this | You get |
|---|---|
| "refresh my jobs" | A full search run and a new shortlist |
| "am I a fit for this?" + url | One posting scored, with the gaps named |
| "apply pack for the Northwind role" | Adversarial review, tailored résumé, cover letter brief |
| "prep me for Thursday's interview" | A prep document and a one-page sheet |
| "draft openers for this week" | Contract outreach, for your review, unsent |
| "weekly scoreboard" | Applications, replies, interviews, and what to change |

## Your folder

```
~/job-hunt/
  profile.md          the intake output, edit it any time
  runs/2026-08-27.json  one search run
  pipeline.json       application status, exported from the dashboard
  dashboard.html      opens in a browser, no server
```

## What is in this package

| File | What it does |
|---|---|
| `SKILL.md` | The doctrine: search loop, run format, link hygiene, guardrails |
| `dashboard.html` | Shortlist and application pipeline, local only |
| `index.html` | This page, in a browser |
| `example-run.json` | A run file to look at, and to test the dashboard with |
| `references/intake.md` | The guided intake |
| `references/profile-template.md` | The profile it fills in |
| `references/sourcing-map.md` | Where to look, and the rule for each channel |
| `references/scoring-rubric.md` | Six dimensions, calibration bands, what never gets filtered |
| `references/apply-pack.md` | Adversarial fit review, tailored résumé, cover letter brief |
| `references/compensation.md` | How to research a real salary band before answering |
| `references/answer-bank.md` | Reusable interview and application answers |
| `references/interview-prep.md` | Per-interview prep and the one-pager |
| `references/contract-track.md` | Contract outreach |

## What it will not do

- **Never applies for you.** A run produces a shortlist and stops. You click every
  apply link and send every message. That is the design, not a limitation.
- **Never invents a claim.** No borrowed projects, no rounded-up numbers, no
  credential-in-progress described as held.
- **Never ships your data anywhere of its own.** Profile, CV, runs and pipeline
  are files in your folder, and the dashboard uses browser local storage with no
  network code in it. Your assistant still sends what it reads to its model
  provider, so install this into one you would trust with a résumé.
- **Never links a job you have to pay to read.** Job-seeker paywalls get traced to
  the employer's posting, or dropped.
- **Never quietly bins a role.** Unconfirmed postings are labeled unconfirmed.

## The honest part

This is a search that works, not a machine that gets you hired. A good run
surfaces two or three roles genuinely worth an application; a thin week surfaces
none, and it says so rather than padding the list. You still do the interviews,
the follow-ups, the decisions, and about ten minutes of tailoring per
application.

## Where this came from

Built by [David Braun](https://workflowtech.ai) for a real job and contract
search, then generalized so it does not need to be his. The rules that look
oddly specific are the ones that came from a run that failed: an employer's name
replaced by an aggregator's, a shortlist of dead links, a good role buried by a
scoring rule that was trying to help.

Everything in here is doctrine plus one HTML file. The dashboard has no
dependencies, no build step, and no network calls. It is one file; read it
before you trust it with anything.

Issues and pull requests are welcome, particularly a sourcing map for a field
this one does not cover well.

## License

MIT. See [LICENSE](LICENSE).
