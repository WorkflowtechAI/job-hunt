# Intake

Runs once, produces `profile.md`, `resume/master.md` and `forms.md`, takes about
fifteen minutes plus the résumé conversion in section 8. Re-run any part of it
whenever something changes.

The output is what every search, score and cover letter reads. A vague profile
returns the same generic shortlist the person could have gotten from a job board
on their own, so the time spent here pays back more than any other time in the
whole skill.

## How to run it

**Read their CV or résumé first.** Ask for it before asking anything else: a
file, a LinkedIn export, a personal site, a portfolio, whatever exists. Then ask
only what the document cannot tell you, and confirm what you extracted rather
than making them retype it.

Nobody enjoys answering ten questions from someone holding their résumé.

A `.docx` is a zip file, so reading one needs nothing installed:
`references/resume-master.md` has the command. Read the document out. Do not
ask somebody to paste their own résumé into a chat window a section at a time.

**One question at a time.** A form with fifteen fields is a form. Ask, listen,
follow up where the answer opens something, move on.

**Real examples in the prompt, not placeholders.** "Something like: senior
support engineer who moved into automation, now building AI systems" teaches the
shape. "`<your background here>`" teaches nothing.

**Block on very little.** Sections 1, 2 and 3 gate the first search. Section 8
and most of section 9 gate the first application rather than the search, so they
can wait until a role is picked; section 9's four questions are quick enough to
ask while the résumé is being converted, and the rest of that file stays empty
until a real form asks. Everything else can be filled in over the first couple of
runs. Say so, so nobody feels they are failing an exam.

**Two of these questions are uncomfortable.** The salary floor, and the honest
account of what they have actually shipped. Ask them plainly and without
flinching, because a profile that is polite about both produces a search that
wastes their time. Say why you are asking.

## The nine areas

### 1. Who you are, honestly

One paragraph. The trajectory, not the job titles: where they started, what they
do now, and what makes the combination unusual.

Most people describe themselves as the role they last held. The useful version is
the intersection nobody else has. Ask "what do you know that the other people
applying to these jobs do not", and follow up until there is a specific answer.

Extract the first draft from the CV, then read it back and ask what is wrong with
it. Correcting a draft is far easier than writing one.

### 2. What you want, in fit order

Three to five target roles, ranked, with a sentence each on why it fits.

Then the one people skip: **what to stop chasing.** Roles their résumé
superficially matches and their career has moved past, work they are done doing,
seats they would resent inside a month. Ask directly: "what would you turn down
even if it paid well?"

The stop list prevents more wasted applications than the target list generates
good ones.

### 3. Where you can work, and what you are allowed to do

The block that decides which entire categories of role are real. Get it exact.

- Country and city they live in.
- Citizenship and any residence permits or visas, with what each authorizes.
- Which markets they can work in without sponsorship, and which need it.
- Whether they can invoice as a business, and where that business is registered.
- Timezone, and the hours they can actually overlap with.
- Whether relocation is on the table, and where to.

Write the conclusions as plainly as the facts: which categories are fully open,
which are a longshot worth pitching anyway, which are closed.

Two failure modes, both expensive. Inventing a barrier that does not exist buries
good roles under a false flag. Ignoring one that does exist fills the shortlist
with jobs they cannot take. Where the person is unsure of their own status, say
so in the profile rather than guessing on their behalf.

### 4. What you will take

- **The floor.** Below this number, the role gets dropped. One hard line, stated
  once. Explain why you are asking: everything above the floor stays visible and
  gets ranked, so a low floor does not mean low-paying jobs crowd the list; it
  means a real job never gets hidden from them during a thin month.
- **The target.** What a good outcome looks like. This ranks, it does not filter.
- **Employment, contract, or both**, and whether that preference is strong.
- **Hours available**, and whether part-time or fractional counts.
- **Notice period or start date.**

When someone hesitates on the floor, the useful framing is not "what are you
worth" but "what number would make you say no to work you can do".

### 5. Proof

What they can put in front of an employer, and defend three levels down.

- Systems shipped, with what each one does and who uses it.
- Numbers they can recount cold: scale, cuts, throughput, headcount, revenue.
- Certifications and credentials, held rather than in progress, with verification
  links where they exist.
- Public artifacts: repos, writing, talks, a portfolio site.
- Languages, and the honest level of each.

**Only what is earned goes in.** Something in progress is recorded as in
progress. A number they cannot source is left out. This section becomes claims in
cover letters and answers in interviews, so an inflation here surfaces at the
worst possible moment.

Ask for the numbers explicitly, one at a time, because people leave their best
ones out. "How many clients?" "How much did that cut?" "How big was the team?"

### 6. Limits

- Companies and platforms excluded, and whether the exclusion is permanent.
- Industries or work they will not do.
- Anything that must stay out of a public application.

Record these once so no future run re-litigates them.

### 7. Cadence

- Hours per week available for the search.
- Weekly application target, set from those hours rather than from ambition.
- Whether contract outreach runs alongside, and at what volume.
- Which day the weekly review happens.
- Whether they already pay for a job-data source that has an API. **This is the
  one and only time to ask.** Yes: `keyed-sources.md` says where the key goes.
  No, or unsure: move on and never raise it again. The search runs on free
  channels, and a paid source is nobody's default.

Fifteen tailored applications beat forty pasted ones, and take less time, because
the forty produce forty rejections to read.

### 8. Your résumé, as a file

The first output that is not part of `profile.md`. Write `resume/master.md` from
the document they handed over, in the shape `references/resume-master.md` fixes,
and copy the original to `resume/original.<ext>` without deleting it.

This is a conversion, not an interview. Everything needed is in the document
already, so the only questions worth asking are about what the document got
wrong: a stale title, a role with no dates, a number they can no longer source.

Show them the result and ask what is wrong with it. Something always is, and
correcting a draft takes a minute where dictating one takes an hour.

**Two things to say out loud, once.** The master holds everything, including the
material a given application will cut, so it is longer than a résumé they would
send. And where the look of their résumé is part of what they are selling, the
rendered page is not for them: `resume-master.md` names those cases and says
what they get instead. Better said now than discovered after a render they did
not want.

**No document at all.** Some people arrive with nothing, usually early career.
Write `resume/master.md` for them from sections 1, 2 and 5 plus the role dates,
in the same fixed shape, and hand it back labeled as a draft to correct rather
than as a conversion to check. It is a worse master than a converted one and it
is a great deal better than the apply pack having no input.

### 9. The fields every form asks for

The second output that is not part of `profile.md`. Write `forms.md` from
`references/form-bank.md`, which holds the template and the rules.

Almost none of this is a question. Authorization, availability, hours, employment
versus contract and the compensation dates all come from sections 3 and 4,
already stated in prose; restate them in field shape and confirm the restatement.
Asking a second time is how an intake earns a reputation. The identity block and
eight to twelve rows of years-per-skill come out of the CV as a draft they
correct.

**Four questions, and only these.** The name as it appears on official documents,
where the CV shows a different one. A real earliest start date, as a date rather
than "two weeks", because "two weeks" written three weeks ago is wrong. A phone
number with country code, where the CV omits it. And whatever they want changed
on the skill-years draft.

**Do not ask the demographic questions.** Not here, not later, not as an optional
extra. `form-bank.md` says why, ships those rows reading "my call, at the form",
and that is where they stay unless the person writes something else in
themselves. Do not infer a value from a name, a document or a country, and do not
offer an opinion on whether answering helps.

References are not a day-one question either. Three other people have to agree
first, and asking for that on day one stalls the search.

## When an answer is too vague to use

Four answers are load-bearing enough that a soft version poisons every later run:
the rare thing in section 1, the target roles in section 2, the floor in section
4, and the numbers in section 5. Everything else can be approximate on the first
pass.

For those four, push once. "What specifically" is usually enough, and the second
answer is nearly always better than the first, because the first is the one
people have said out loud before.

Stop pushing when the answer contains a specific noun and, where the question
admits one, a number. That is the bar, and it is reachable in two exchanges.

**Where the person has the `grilling` skill installed**, this is exactly what it
is for: hand it the draft profile and let it interrogate the assumptions in
dependency order before the file gets written. Worth doing when the person is
mid-career-change, when the target roles and the proof do not obviously line up,
or when they say some version of "I am not sure what I am actually going for".

**Without it**, run the light version inline. Three questions, asked in this
order because each one depends on the last:

1. Who is the other person applying to this role, and what do they have?
2. What does this person have that that person does not?
3. What is the evidence for that, that a stranger could check?

An answer that survives all three is a profile. An answer that does not is a
job title.

Do not turn this into an interrogation. One pass, on the four answers that
matter, then move on. The profile improves every week from real runs, and a
perfect intake is not a prerequisite for a useful first search.

## Before writing the file

Show the person a summary of what you understood, in their own terms, and let
them correct it. One screen. This catches the misreading that would otherwise
shape every search for a month.

Then write `profile.md` from `references/profile-template.md`, `resume/master.md`
per section 8, and `forms.md` per section 9. Tell them where all three are and
that they can edit them directly. They are their files, in plain markdown, and
none of them should ever feel like a black box.

## Keeping it current

Re-open the profile when any of these happen: a certification lands, a system
ships, a role starts or ends, the floor moves, a target role type stops feeling
right, an exclusion gets added after a bad experience, or a run surfaces a
question the profile could not answer.

That last one is the important one. Every time a search has to guess, the guess
gets confirmed with the person and then written back into the profile, so the
same question is never asked twice.
