# Form bank

Every application form asks the same forty things. Years of experience in each
named skill, work authorization, notice period, earliest start date, desired
compensation, relocation, remote preference, references, the demographic
selections, and three or four short free-text boxes. None of it is hard. All of
it gets retyped from memory.

Retyping from memory has one specific failure, and it is not the lost time. Two
applications to the same company, six weeks apart, carry different answers. Four
years of a skill in March and seven in May. A notice period that moved for no
reason. A number that dropped for no reason either.
Both records sit in the same applicant tracking system, and a recruiter who opens
both sees somebody who does not know their own history.

So the answers get decided once, written down, and copied.

## The line this does not cross

This file is something the person copies from. It is never something an assistant
types into a form.

- No filling a field. No selecting an option. No uploading the résumé. No
  clicking submit.
- No answering a screening question inside a form, including the ones that look
  like a formality.
- No browser automation pointed at an application. Not with a driver, not with an
  extension, and not by describing the clicks to something else that does them.

What is allowed, and useful: reading this file, telling the person which of these
fields this particular form is going to want, naming the ones still empty,
trimming an answer to the box's limit, and handing the finished text over for them
to paste.

The person applies. When they ask for the automated version the answer is no, and
the reason is that they are the one who has to defend every answer in the room.

**What this is, said plainly.** These are instructions, not a technical control.
Nothing here can stop software that decides to ignore them, and a package that
implied otherwise would be selling a guarantee it does not have. What it does is
make the line unambiguous, so crossing it is a choice somebody made rather than a
default nobody noticed.

**Nothing gets invented to fill a row.** A field this file cannot answer is a
question for the person, not a gap to close with a reasonable guess.

## Two files, and what each one holds

`forms.md` lives in the person's job-hunt folder next to `profile.md`. It holds
field-shaped facts: a date, a number, one of three options. It gets scanned in
five seconds with a form open in the other window, and copied verbatim.

**Say where that folder can and cannot go, once, at the moment they create the
file.** The rest of this package recommends keeping the job-hunt folder in a git
repository, which is good advice for a profile and a résumé. This file holds a
legal name, a phone number, a home city, and whatever the person chose to write in
the four rows further down. A private repository is fine. A public one is not, a
work-owned laptop or a synced company drive is not, and a repository that might
one day be made public is the one that catches people. If any of that is in
doubt, the file belongs outside the repo, and a `forms.md` line in `.gitignore`
costs nothing.

`answers.md`, from `references/answer-bank.md`, holds what the person says and
writes: the stories, the term-to-defence chains, the free-text form answers, in
two registers. Prose, rewritten as they get better at telling it.

**Every free-text box on a form is `answers.md`'s job, not this file's.** That
file holds the list and the rule that matters most about them, which is that a
stored paragraph pasted into forty forms describes none of them. Naming those
boxes again here would be the second copy this paragraph exists to prevent: a
rule stated in two files gets updated in one, and a list stated in two files has
already drifted by the time anybody checks.

Keeping the two apart is not tidiness. A file holding both becomes prose, and
prose is useless when the form is open and the answer needed is a date.

Markdown, not structured data. The format is the guardrail: a schema invites a
filler, and a table shaped for a person to read gives a machine no reason to
parse it. It also renders in every editor and on a phone, and needs nothing
installed.

## Day one: what the intake asks

An intake that asks forty questions before the first search gets abandoned, and
an abandoned intake produces no search. So most of this is not asked on day one,
and some of it is never asked.

**Derived from the profile, asked nowhere.** The intake already established
country and city, citizenship, permits, which markets need sponsorship, the
invoicing entity, timezone, relocation, hours available, employment versus
contract, and the floor and target. Those are the facts the form wants, already
stated in prose. Restate them in field shape and confirm the restatement.

**Extracted from the CV, read back for correction.** The identity block, and
eight to twelve rows of years per named skill. Draft both from the document, show
them, and let the person fix the wrong rows. Correcting ten rows takes a minute.
Answering ten questions takes ten.

**Actually asked on day one, and only this:**

1. The name as it appears on official documents, where the CV shows a different
   one. Forms ask for a legal name and a CV often carries a working name.
2. A real earliest start date. A date, not "two weeks", because "two weeks" on a
   form filled in three weeks ago is wrong.
3. A phone number with country code, where the CV omits it.
4. Whatever they want changed on the skill-years draft.

Everything else stays empty until a real form asks for it. An empty row is not a
gap. It is a row nobody has needed yet.

## What accumulates

After every application, one pass, three minutes, while the form is still open:

- Any field the form demanded that this file did not have gets added, in the
  form's own wording, with the answer the person actually gave.
- Any answer the person changed on the fly gets corrected here, or the next form
  gets the old one.
- The log gets a line: date, company, role, which fields were new.

The log is not a second pipeline. `pipeline.json` tracks status. This log tracks
what was said, so a discrepancy is traceable to the form that caused it.

By the sixth application the pass is usually empty.

## Years by named skill

The field that gets guessed most, and the one where a guess becomes a
contradiction across two applications. `answer-bank.md` and `SKILL.md` both state
the rule; this is where the number lives.

- Count calendar years from first professional or shipped use until now. Do not
  sum months across overlapping roles, and do not count a course.
- One number per skill, everywhere. The number here is the number on the résumé.
- Write `none` rather than leaving a row blank. A blank row is what becomes an
  improvised number at 11pm.
- The honest bounded number, always. The longer career does its work in prose,
  not in a number field.

## Compensation stores no number

The number lives in `profile.md`, put there by `references/compensation.md`, with
its band, its source and the date it was researched. This file stores the date and
a pointer, because a second copy of a number is how a résumé, a form and an
interview end up disagreeing.

Re-derive when the profile's research date is more than about three months old, or
when the target level changes.

## The demographic questions

US forms often end with four selections: race and ethnicity, gender, veteran
status, and disability status, under an equal opportunity or voluntary
self-identification heading. Outside the US they mostly do not appear, and where
they do they are different questions with different wording.

The handling is deliberate and it is narrow.

**Nothing in this package asks them.** Not at intake, not later, not as an
optional extra, not as a helpful offer once the person has answered nine other
things.

**Nothing in this package fills them, proposes a value, or infers one.** Not from
a name, not from a photo, not from the CV, not from a country of residence, not
from a pattern in earlier answers.

**Nothing in this package nudges.** No note that answering helps. No note that
declining helps. Both of those are somebody's position dressed as advice, and
nobody asked for one.

**Nothing in this package reads those four rows, for any purpose, ever.** Not into
a score. Not into a verdict. Not into a cover letter brief. Not into the fit
review's comparison against the likely pool, which is the place it would be
easiest to justify and the place it would do the most damage. Not summarized back
in conversation, not repeated in a status line, and not copied into anything under
`applications/`. A row the person filled in is theirs to paste into a form and
nothing else's to look at. Where a form's fields are being listed for them, these
four are named as fields, never as values.

The template ships those four rows filled with `my call, at the form`, and they
stay that way unless the person writes something else in themselves.

Why the rows exist at all, given that: a person who has decided is entitled to
write their decision down, for the same reason as the rest of the file. Two forms
at the same company carrying different self-identifications are a discrepancy in a
record the person cannot see and cannot correct. If they want that answer stable,
this is where it goes, in their words, typed by them.

**Either decision is a whole answer.** Every one of these fields offers a decline
option, so "decline to self-identify" fills a row exactly as completely as naming
something does. Both get written the same way, by the person, and neither gets a
comment.

## What stays out of the file entirely

Criminal history, background check consent, credit history, immigration document
numbers, date of birth, national identification numbers, driver's licence number,
bank account or direct-deposit details, an emergency contact's name and number,
and salary history where a form still asks for it.

These get answered live, by the person, on the form, every time. The reason is not
squeamishness. The wording, the jurisdiction and the lawful scope of these
questions all vary by state and by country, so a stored answer goes stale without
looking stale, and a stale wrong answer on a background-check field is a withdrawn
offer. Retyping it is cheap by comparison.

The last three are on the list for a different reason: they are the fields a
thief wants. A licence number is state-issued, so "national identification
numbers" does not reach it, and driving roles ask for it on the application
itself rather than at onboarding. Direct-deposit details belong to a payroll form
after an offer and never to an application. And an emergency contact is somebody
else's phone number, which is not the person's to store on their behalf.

**Anything that would be identity-theft material if this folder leaked stays out,
whether it is listed here or not.** The list is what has come up, not the limit.

## References

Not a day-one question, because it is not the person's question to answer alone.
Three other people have to agree first, and asking for that on the day somebody
starts a search stalls the search. So the file holds the state, not the contacts,
until permission exists.

Ask before the first form that demands references, not after. Tell each person
which role it is, every time, before their name goes in a box: somebody calling
out of nowhere about a job they never heard of is how a reference stops being a
reference. Most forms take "available on request", so a form that hard-requires
three contacts is the one to fill in last.

**Their contact details are not the person's to store.** Agreeing to be a
reference is not agreeing to have a mobile number sitting in somebody else's
folder, which may be a git repository. So the table holds initials, the role and
where the number can be found ("in my phone", "the 2019 thread"), and the number
itself gets fetched at the form that demands it. When the search ends, those rows
come out.

## The file

Copy this into the job-hunt folder as `forms.md`. Fill the rows a real form has
actually asked for, and leave the rest.

```markdown
# Form answers

Last updated: YYYY-MM-DD

I copy out of this file. Nobody types out of it into a form except me.

## Identity

| Field | Answer |
|---|---|
| Full legal name | |
| Preferred name | |
| Email | |
| Phone, with country code | |
| City, country | |
| LinkedIn URL | |
| Portfolio or site | |
| Repo host profile | |
| Which résumé file to attach | |

## Authorization

From the location and authorization block in `profile.md`. Where that block
records uncertainty, this one records the same uncertainty. It does not get
resolved here.

| Field | Answer |
|---|---|
| Authorized without sponsorship in | |
| Sponsorship required for | |
| Permit or visa held, and what it authorizes | |
| Can invoice as a business, registered in | |

## Availability

| Field | Answer |
|---|---|
| Currently employed | |
| Notice period | |
| Earliest start date | |
| Hours per week available | |
| Employment, contract, or both | |
| Remote, hybrid, or onsite | |
| Willing to relocate, and where | |
| Willing to travel, how much | |
| Timezone, and overlap hours | |

## Compensation

| Field | Answer |
|---|---|
| Desired compensation | read from `profile.md`, never copied here |
| Band researched on | YYYY-MM-DD |
| Re-derive when | that date is over three months old, or the target level changes |

## Years by named skill

One row per skill that has appeared on a form or in a target posting. Eight to
twelve rows. This is not a skills inventory.

| Skill, in the words forms use | Years | Since | What the count covers |
|---|---|---|---|
| | | | |

## Equal opportunity and self-identification

My call, at the form. Nothing and nobody fills these in for me.

| Field | Answer |
|---|---|
| Race and ethnicity | my call, at the form |
| Gender | my call, at the form |
| Veteran status | my call, at the form |
| Disability status | my call, at the form |

## Answered live, never stored

Criminal history, background check consent, credit history, immigration document
numbers, date of birth, national ID numbers, driver's licence number, bank account
or direct-deposit details, an emergency contact's name and number, salary history.
The wording and the lawful scope of these change by jurisdiction, so a stored
answer goes stale without looking stale, and the last three are simply what a
thief would want out of this file. Anything else that would be identity-theft
material if this folder leaked belongs here too.

## References

State, not contacts, until each person has agreed.

| Initials | Role | Relationship | Where their number is | Asked, on |
|---|---|---|---|---|
| | | | | |

## Free text

Lives in `answers.md`, not here.

## Form log

| Date | Company | Role | Fields that were new |
|---|---|---|---|
| | | | |
```
