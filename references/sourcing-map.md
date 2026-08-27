# Sourcing map

Where to look, in priority order, and the rule for each channel.

The principle behind the order: **go as close to the employer as you can get.**
Every layer between the person and the hiring company adds staleness, strips the
employer's name, or adds a toll. Aggregators are useful for discovery and poor
for application.

Fan out across angles rather than running one query deeper. Ten channels at one
page each returns more real roles than one channel at ten pages, because the
tenth page of any job board is the same roles the first page had.

## Tier 1: the employer's own posting

**Company career pages and ATS boards.** Greenhouse, Ashby, Lever, Workday,
Rippling, SmartRecruiters, Workable. These are the freshest listings that exist,
they name the real employer by definition, and the apply link is the real one.

Build a target company list during the intake and keep it in the profile: the
twenty to forty companies the person would actually take a job at. Check them
directly. This is the highest-yield channel and almost nobody does it, because it
is the only one that requires a list instead of a search box.

Greenhouse exposes a public JSON API, no key required, which returns every
posting for a company including the compensation string where one is published:

```
https://boards-api.greenhouse.io/v1/boards/<company>/jobs?content=true
```

That call is also the compensation research tool in
`compensation.md`.

**Warm network.** Companies where the person knows someone, has worked with the
team, or has a public connection to the work. Check their careers page whether or
not they appear in any search. A warm application to a mediocre-fit role beats a
cold application to a perfect-fit one.

## Tier 2: talent and contract platforms

Braintrust, Toptal, Gun.io, Contra, Wellfound, Arc.dev, and the equivalents in
the person's field. These pay well and skip the résumé pile, and most of them
gate their listings behind an account.

Two things to know. Several require an approved profile before anything is
visible, so treat setup as a one-time task worth flagging rather than something
to do mid-run. And the profile's exclusion list applies here permanently: a
platform someone has ruled out stays out.

**Recruiting and staffing firms** belong in this tier, and they are two leads in
one: their current openings, and the recruiter as an ongoing contact who will
keep sending roles for years. Specialist firms in the person's field beat
generalists.

## Tier 3: niche boards

Boards scoped to one field or one way of working return a higher hit rate than
the giants, because the filtering already happened.

**aijobs.net** (run by Foorilla) is the reference example for AI, ML and data
roles: free to browse and apply, roughly fifty thousand listings, filters for
remote and for contract type, and an "include agencies" toggle that maps directly
onto the employer-versus-intermediary rule below. It exports a filtered search as
**CSV or JSON**, which makes it the cheapest bulk input in this whole map: filter
once, export, score the export against the profile, verify the survivors.

Foorilla also publishes an **AI/ML and Big Data salary dataset** on GitHub under
CC0, a weekly snapshot of survey responses from 2021 onward, at
`https://raw.githubusercontent.com/foorilla/ai-jobs-net-salaries/main/salaries.csv`.
Public domain, no key, useful as a comp benchmark by title, level, location and
remote ratio.

They also sell API access to the same listings, behind a paid subscription. It is
optional, it is not part of the loop, and the free export above is enough.
Where someone already pays for it, `keyed-sources.md` covers how the key is
supplied and how any keyed source has to behave.

Find the equivalent board for the person's field and add it to the profile.
RemoteOK and the remote-first boards fill the same slot for location rather than
discipline.

## Tier 4: aggregators and alerts

Indeed, and whatever else surfaces volume. Also job-alert emails, which are an
underrated channel because someone already ran the search: LinkedIn job alerts,
board digests, newsletter listings, and roles a friend forwarded.

A job-board MCP connector, when one is available, sits here. It is **one input
among many**, never the search itself. Its coverage is one index; the point of
this map is that no single index is enough.

Local and regional boards matter when the person can work in that market. They
are ignored by everyone optimizing for the US remote market, which is exactly why
they are worth checking.

## Rules that apply everywhere

**`company` is the hiring employer.** Never the aggregator, the alert service,
the staffing firm, or the talent platform the lead arrived through. When a lead
comes in through an intermediary, dig one layer further; the intermediary's own
listing nearly always names the employer. Recording the intermediary instead
produces postings with nothing to research and nothing to search for, and it
defeats deduplication when the same role arrives twice through two different
platforms.

**Paid job-seeker paywalls: resolve or drop.** Any board that charges to view or
apply gets traced to the employer's own posting. When it cannot be traced, the
lead is dropped rather than surfaced. A free login is a different thing: keep it
and note the login in the verdict.

**Prefer the employer's link, keep the board link when that is all there is.**
Search `<company> careers <title>` before settling. `sourceType: "company-site"`
when confirmed there, `"job-board"` when only the board has it, `"alert-only"`
when it cannot be confirmed anywhere but came from a real alert. Freshness counts
at least as much as provenance.

**Stay inside terms of service.** LinkedIn specifically: its job-alert emails are
the supported path, and scraping the site risks the account that carries the
person's professional network. No lead is worth that.

**Verify before it ships.** Every posting gets fetched and confirmed open. See
the search loop in `SKILL.md`, step 4.

## Login-gated sources

Wellfound, Otta, Hired, YC's Work at a Startup, and most talent-platform
dashboards need a real logged-in session. Two honest options: the person sets up
the account once and the search uses a browser tool against their session, or the
channel stays out of the loop. Guessing at what is behind a login wastes the run.

Flag the setup when a gated source is worth it for their field. Do it once,
between runs, rather than blocking a search on it.
