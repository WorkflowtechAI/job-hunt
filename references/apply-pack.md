# The apply pack

Per role, on request, after the person picks roles off the shortlist. Never
automatically for a whole run: this is expensive work and most postings do not
earn it.

Three outputs, in this order:

1. **An adversarial fit review.** Five hostile readers, before anything is
   written.
2. **A tailored résumé** for this posting, built from their real one.
3. **A cover letter brief.** The points to hit, in order, with the evidence
   attached. **Not the letter.**

The last one is a deliberate line. A drafted letter needs the person's voice, and
a voice that is not theirs is worse than a plain one, because it gets read aloud
in an interview by someone who did not write it. The brief carries everything a
letter needs except the sentences. They write the sentences, or hand the brief to
whatever writing tooling already sounds like them.

## Inputs

The posting (full text, not the summary), `resume/master.md`, `profile.md`, and
`answers.md` if it exists. No master yet: build it first, from
`references/resume-master.md`. It is one pass over whatever résumé they already
have, and every later pack reuses it. Where the posting is thin, read the
company's other postings for the same team; they leak what this one omitted.

## 1. Adversarial fit review

Run all five lenses. Each one is a different reader with a different reason to
say no. Report what each finds, plainly, before proposing any changes.

The point of doing this first is that two of the five regularly end with "do not
apply, or apply to something else there", and that answer is worth finding before
an afternoon goes into a tailored résumé.

### Lens 1: the six-second screen

A recruiter with ninety résumés scans the top third for four things: title
proximity, obvious keyword hits, tenure pattern, location. Nothing else is read.

Does the top third of the résumé pass? Name what is missing from it. Most
résumés bury their best match on page two, which is the same as not having it.

### Lens 2: the keyword filter

List every concrete term the posting names: tools, methods, certifications,
domains, scale figures. Mark each present in the résumé, present in a different
word, or absent.

Add only what is true. A term the person cannot defend three levels down (see
`answer-bank.md`) gets left out no matter how well it would match, because
passing a filter into an interview that exposes it is a worse outcome than not
passing the filter.

Where the résumé says the same thing in different words, use the posting's words.
That is not gaming anything; it is speaking their language.

### Lens 3: the hostile hiring manager

Read every bullet looking for inflation. For each claim, ask "how?" and "by how
much?" and mark the ones with no answer. Then ask which bullets describe
participation rather than ownership, because "was involved in" is where a strong
CV goes soft.

Flag anything that would collapse under one follow-up question. This is the lens
that saves interviews.

### Lens 4: the comparison

Against the likely pool for this posting, what is genuinely rare here, and what
is on everyone's résumé? Lead with the rare thing, and be honest that the rare
thing changes per posting: the long operational record is rare in a specialist
pool, and the specialist work is rare in a generalist pool.

Name the generic material too, since that is what gets cut for space.

### Lens 5: the gap hunter

What will they notice and ask about? The employment gap, the short stint, the
career pivot, the missing credential, the seniority mismatch, the location.

For each: is it addressed on the résumé, in the letter brief, or left for the
interview? All three are valid choices. Leaving it unconsidered is not.

### The verdict

Close the review with a call: apply, apply to a different role at this company,
or skip. Say which of the five lenses drove it. When the answer is skip, say so
plainly and do not build the rest of the pack; a review that always concludes
"apply" is a review that is not being run.

## 2. The tailored résumé

Built from the master, per posting. Rules, in force order:

**Reorder before rewriting.** Most of the gain is in what appears in the top
third. Move the matching experience up, move the matching bullets to the top of
their role, and lead the summary line with what this posting asked for.

**Mirror their language where it is true.** Same concept, their word.

**Quantify what can be quantified.** Numbers route through the master. The
numbers table in `profile.md` is where a number is established and sourced;
`resume/master.md` is where it enters the résumé; a tailored copy draws only
from the master. Any number matches every other place it appears.

A number this posting wants and the master does not have goes into the master
first, from the profile table. Putting it straight into the tailored copy
bypasses the number check in `references/resume-master.md`, which is the only
thing standing between a rounded-up figure and an employer.

**Cut what this posting does not want.** A résumé aimed at everything aims at
nothing. Two pages maximum for most people, one for early career. Cutting real
experience because this posting does not need it is correct.

**Invent nothing.** No new employers, no adjusted dates, no borrowed projects, no
title upgrades. Reordering, rewording and cutting are the only operations
available. This is not a style preference; a fabricated résumé is fraud and it
surfaces in reference checks.

**Keep the master intact.** Never edit `resume/master.md` for a posting. The
master accumulates everything and each posting gets a subset, written to its own
file. A pack that tailors the master in place destroys the only copy holding the
material it cut, and the next posting needs that material.

### The output is a file

One folder per application, named `<date>-<company>-<role>`, lowercase and
hyphenated:

```
applications/2026-08-27-northwind-fde/
  posting.md        the posting text as it read on the day
  review.md         the five lenses and the call
  resume.md         the tailored copy
  letter-brief.md   output 3, below
  changes.md        every change, labeled, and the check output
```

A sixth file, `resume.pdf`, appears when the person prints `resume.md` through
`resume.html`. Tell them that step exists; do not do it for them, because the
print dialog is theirs.

The format of `resume.md`, the render, and the folder convention are all in
`references/resume-master.md`.

### changes.md, and why it has only three labels

One line per change, each one carrying a label:

```
MOVED     Northwind bullet 3 to the top of the role. The posting leads on rollout.
REWORDED  "integration work" to "systems integration". Their words, same claim.
CUT       The 2013 support role. Two pages, and this posting does not want it.
```

**There is no ADDED label.** A change that cannot be labeled MOVED, REWORDED or
CUT is a fabrication, and the fix is to revert it rather than to justify it in
prose. Because both files are markdown, part of that rule is machine-checkable:
`references/resume-master.md` has the commands and says which part.

Then run the checks in `references/resume-master.md` and paste their output at
the bottom of `changes.md`, including when it is empty, along with the master's
fingerprint. A check whose result nobody wrote down did not run.

Read the last part of that section too, the one naming what the checks do not
catch. An empty output is not a clean bill of health, and lens 3 is still the
thing that catches an inflated bullet.

Where the person's own résumé formatting is the thing being sold, per the same
file, `changes.md` is the entire deliverable and there is no render. They apply
the labeled list to their own document in about ten minutes.

## 3. The cover letter brief

Not a letter. A brief the person writes from, in their own voice.

Format:

```
OPENING ANGLE
  The one true thing that makes this posting and this person worth
  each other's time. One sentence. Where the match is partial, name
  the part that matches rather than claiming the whole.

HIT, IN ORDER
  1. <point>  evidence: <specific thing, with its number>
  2. <point>  evidence: <...>
  3. <point>  evidence: <...>
  Three to five. Ordered by what is rarest in this pool, per lens 4.

ADDRESS DIRECTLY
  The gap or mismatch from lens 5 that is better named than discovered,
  with the nearest real thing they do have.

LEAVE OUT
  What the master résumé carries that this letter should not:
  the accomplishments that dilute, the terms that invite a question
  nobody can answer, anything that reads as apology.

MIRROR
  Words and phrases from the posting worth echoing, because they are
  the words the reader chose.

CLOSE
  What the invitation should offer.
```

Two standing rules for whatever gets written from it. Every claim that can carry
a number carries one. And compensation, engagement structure and availability
terms stay out of the letter entirely; those go in the application's salary field
and the first call. Research that number with `compensation.md` rather than
improvising into a box.

## From the dashboard

Each card has an **Apply pack** button that puts a prompt on the clipboard.
Paste it into an assistant that has this skill installed and the pack starts:
the phrase "apply pack" is what triggers the skill, and the skill is where the
five lenses and the rest of this file come from. The prompt itself is short on
purpose, but it carries what the card already knows and the assistant would
otherwise re-derive from the posting alone: the score this run gave, the
verdict, the gaps already found, the comp and location as listed. It also names
the inputs and the output folder, because a session that has the skill but not
the folder will invent a résumé rather than tailor the real one, and will hand
it back as chat text rather than as a file.

Two things it cannot carry. The posting's full text stays behind the link, so an
assistant with no way to read the page needs it pasted. And it cannot make the
inputs exist: run the paste from the folder holding `profile.md` and the master
résumé, or hand them over when asked.
