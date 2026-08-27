# Scoring rubric

Every posting gets a score from 0 to 100 and a one-line verdict. The score exists
to order the list, so it has to spread. A run where everything lands between 70
and 85 has ranked nothing.

## Drop before scoring

Only four things remove a posting from the list entirely:

1. **Below the profile's compensation floor.** One hard line, stated once in the
   profile.
2. **On the exclusion list.** Company, platform, or work type the person ruled
   out.
3. **Confirmed dead.** Expired, closed, removed, 404. Set `live: false`; the
   dashboard drops it. Unconfirmed is not dead, see `SKILL.md` step 4.
4. **Behind a paid job-seeker paywall with no traceable original.**

Everything else gets scored and stays visible. A posting the person can see and
reject in two seconds costs them nothing. A posting that never reached them
because a rubric decided on their behalf can cost them the job.

## The six dimensions

| Dimension | Points | What earns them |
|---|---|---|
| Craft match | 35 | Does the day-to-day work match what this person actually does well |
| Domain and stack | 15 | Named tools, sector, product type they already know |
| Level fit | 10 | Scope and seniority land where they are, neither a demotion nor a stretch they cannot defend |
| Location and authorization | 15 | How workable this is given the profile's location block |
| Compensation | 15 | Position against the profile's target, not its floor |
| Reachability | 10 | Fresh, direct apply link, employer's own posting, warm connection |

Craft carries the most weight on purpose. Domain is learnable in a quarter;
craft is what took a career.

### Craft match, 35

Read the posting's responsibilities, not its requirements list. Requirements are
written by HR from a template. Responsibilities are written by the hiring manager
describing their actual problem.

Full marks when the person has done this exact work and can point at where. Half
when they have done its neighbor. Low when the posting describes a trade they
have not practiced, however impressive the résumé looks next to it.

### Domain and stack, 15

Named tools, industry, and product shape. Split the requirement list into **craft
bullets** and **domain bullets**. Most strong candidates clear craft nearly
everywhere and lose on domain. Score domain honestly and let craft carry the
posting; four or more domain bullets they cannot touch is where the seat is the
domain itself, and the score should say so.

### Level fit, 10

A staff role for someone at senior scores below a senior role, and so does a
mid-level seat. Years requirements are the softest signal in any posting: read
"7+ years" in a field younger than seven years as the word "senior" and score
accordingly.

### Location and authorization, 15

Set `locationFit` and score from the profile's location block:

- **`global`**: hires from anywhere, or the person can bill it through their own
  entity. Full marks.
- **`us-remote`**: remote, but likely requires residence in a specific country.
  Partial. A posting that says "remote (US)" usually means remote from inside the
  US. Treating that as location-agnostic is the most common scoring error there
  is. Keep these, flag the requirement, and note the contractor path when the
  person has an entity to bill through.
- **`onsite`**: requires relocation. Low, unless the profile says relocation is
  on the table.

Where the profile records no authorization barrier, do not invent one. A false
"needs sponsorship" flag buries roles the person can take today.

### Compensation, 15

More pay scores higher, the same way a closer role match scores higher. **Pay
ranks, it never gates above the floor.**

Say the range plainly and never editorialize. Calling a role "underpaid" and
burying it substitutes a judgment for the person's own, and a role at the low end
is a real lead in a thin month. Where a posting states no salary, do not infer
one and do not penalize the omission; score the midpoint of the dimension and
move on.

### Reachability, 10

Posted in the last week, on the employer's own ATS, with a direct apply link, and
someone in the network works there: full marks. Sixty days old, three
intermediaries deep, alert-only: near zero. This dimension is the tiebreaker
between two equally good matches, and it is usually right.

## Calibration

| Band | Meaning | What to do with it |
|---|---|---|
| 85-100 | Rare. Written for this person | Apply today, tailor properly |
| 70-84 | Strong. Real gaps, none disqualifying | Apply this week |
| 55-69 | Plausible. Worth an application when the week has room | Batch these |
| 40-54 | Weak. One thing is genuinely off | Visible, not recommended |
| under 40 | Poor fit | Stays on the list, sorted to the bottom |

Expect two or three in the top band per good run, and zero in a thin week. **Zero
is a valid result and it gets reported as zero.** A padded top band trains the
person to stop trusting the ordering, and once that trust is gone the whole
shortlist is decoration.

## Strengths, gaps, verdict

**`strengths`**, two or three. What in the posting matches something specific in
the profile. Not "strong technical background".

**`gaps`**, one to three. Named honestly. The gaps field is what makes the score
believable and what the cover letter has to answer. A posting with no gaps listed
was not read carefully.

**`verdict`**, one line, plain language, no jargon. It answers "should I care
about this and why" for someone reading twenty of them over coffee.

Good: "Strong match. They want the discovery-to-rollout work you already do, and
they name your stack. They also want Kubernetes depth you do not have."

Bad: "High alignment across core competency vectors with moderate stack
divergence."

The verdict is the only part of the run most people read closely. Write it like a
colleague who read the posting so they did not have to.
