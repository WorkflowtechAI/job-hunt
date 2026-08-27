# The master résumé

A tailored résumé that arrives as text in a chat window gets retyped into a
document. That retyping is the largest cost per application in the whole loop,
and it is also where invention gets in, because somebody retyping a bullet
improves it and the improvement is not always true.

So the résumé is a file. One master, tailored copies beside it, and a printable
page that comes out of a browser.

## The master is markdown

One file, `resume/master.md`, in the person's job-hunt folder. It holds
everything: every role, every bullet, the long version. No posting sees all of
it.

Why markdown, against the alternatives:

**Against JSON Resume, or any schema.** A schema makes the file machine-readable
and makes the person a data entry clerk. Nobody hand-edits their own career in
JSON, so the file stops getting corrected, and a stale master is worse than an
awkward one. A schema also has no clean place for the section it did not
anticipate, forces ISO dates on people who remember a year, and needs a theme
package installed before it renders at all. Markdown loses none of the structure
that tailoring actually uses, because tailoring works on sections, entries and
bullets, and headings plus list items name all three.

**Against markdown plus pandoc.** Markdown yes, pandoc not as the engine.
Pandoc's own docs are clear that PDF output goes through a separate program
(`pdflatex`, `xelatex`, `weasyprint`, `typst` and others), and that is a large
install to make a two-page document. A browser already prints to PDF on every
operating system. Pandoc stays useful for one job, below, which is `.docx`.

**What markdown buys that matters most:** a tailored copy and the master are the
same kind of file, so the difference between them is a diff. That is the whole
no-fabrication check, further down.

## The shape

Fixed, because `resume.html` renders it and the tailoring reads it.

```markdown
# Full Name

One line saying what you are

City or timezone · email · [site](https://example.com/you)

## Summary

Two or three sentences. Plain prose.

## Experience

### Job Title

**Employer** · Location · 2022 to present

- What you did, with the number
- Another one

### Earlier Job Title

**Employer** · Location · 2016 to 2022

- What you did

## Skills

**Languages** · one, two, three
**Platforms** · one, two, three

## Credentials

- Credential, issuer, year · [verify](https://example.com/verify/x)

## Education

### Degree

**Institution** · 2012 to 2016
```

Five conventions, and the renderer depends on all five:

1. `#` appears once, and it is the person's name.
2. Under the name: the first text line is the headline, and the lines after it are
   contact details.
3. `##` is a section. `###` is one entry inside it, and the text line under a
   `###` is the employer and dates line.
4. `- ` is a bullet.
5. Date ranges read `2022 to present`, not with a dash. A dash between two years
   is the one character that gets mangled by every export path this file will
   pass through.

Inline, only three things work: `**bold**`, `*italic*`, and
`[text](https://url)`. Tables, images and footnotes do not, on purpose. A résumé
that needs a table needs its own document, which is the case covered below.

## When somebody arrives with a .docx

They will. Read the file, do not ask them to paste their own résumé into a chat
window a section at a time.

A `.docx` is a zip archive with the text in one XML file, so nothing needs to be
installed:

```bash
unzip -p resume.docx word/document.xml | sed -e 's|</w:p>|\n|g' -e 's|<[^>]*>||g' \
  -e 's|&lt;|<|g' -e 's|&gt;|>|g' -e 's|&quot;|"|g' -e "s|&apos;|'|g" \
  -e "s|&#39;|'|g" -e 's|&amp;|\&|g'
```

```powershell
Copy-Item resume.docx resume-copy.zip
Expand-Archive resume-copy.zip -DestinationPath docx-out -Force
(Get-Content docx-out/word/document.xml -Raw) -replace '</w:p>', "`n" -replace '<[^>]*>', '' `
  -replace '&lt;', '<' -replace '&gt;', '>' -replace '&quot;', '"' -replace '&apos;', "'" `
  -replace '&#39;', "'" -replace '&amp;', '&'
```

All formatting is lost, which is the point. The text is what tailoring works on.

The entity decoding at the end is not optional, and `&amp;` has to be decoded
last or it re-creates the others. Word writes `&amp;` for an ampersand, and an
employer called Smith & Co otherwise reaches `master.md` as `Smith &amp; Co`,
where the renderer escapes the ampersand again and prints `Smith &amp;amp; Co`.

Those five are all the entities XML predefines, so nothing else is named here.
Anything else arrives either as the character itself, which is why a curly quote
or a dash comes through fine, or as a numeric reference like `&#8217;` from a
generator that chose to write one. Read the punctuation in `master.md` once, not
just the structure: a stray `&#8217;` prints literally on the finished page.

A PDF or a plain text file: read it directly. A `resume.json` from JSON Resume:
read it and write the markdown from it. Nothing else works: ask them to paste
the text, or to save as plain text from whatever holds it.

**Keep the original.** Copy it to `resume/original.<ext>` and never delete it.
It is the fallback for the case in the next section, and it is the document they
have already sent to people.

Then write `resume/master.md`, show it to them, and ask what is wrong with it.
Something is always wrong with it, usually a date or a job title, and it is
faster to correct a draft than to dictate one.

## When this is the wrong choice for someone

A generic layout is a downgrade for some people, and pretending otherwise is how
a feature gets abandoned in week two. Four questions:

1. Is the look of the résumé part of what is being sold? A designer, an art
   director, anyone whose document is a work sample.
2. Is it an academic CV, with publications, grants and a citation format?
3. Does it need a photo, a personal-details block, or a signature, because of the
   country it goes to?
4. Is it set in a script or typeface the layout here does not handle?

Any yes, and the rendered page is not for them. **The rest still is.** Keep
`resume/master.md` as the content master, keep their own document as the one that
gets sent, and let the apply pack hand over `changes.md` alone: a labeled list of
what to move, reword and cut. They apply it to their own file in about ten
minutes, and they keep their formatting.

Say this out loud the first time, rather than rendering a page they did not want
and letting them discover it looks worse than the one they had.

One case runs the other way. Where an employer's application form parses an
uploaded file, a plain single-column page reads more reliably than a two-column
design, and the "Copy as plain text" button in `resume.html` fills a paste box
without the layout garbage a PDF copy produces. Worth saying to someone whose
designed résumé keeps coming back parsed wrong.

## Rendering

Nothing to install. `resume.html` sits in the job-hunt folder next to
`dashboard.html`, opens as a local file, and has no network code in it.

1. Open `resume.html` in a browser.
2. Drop `resume/master.md`, or a tailored copy, onto it.
3. Set density and paper. The dashed lines are where the paper runs out.
4. Print. Save as PDF. In the dialog: headers and footers off, because the footer
   prints your own file path into a document an employer reads. Margins default,
   scale 100%. Save into the application's folder as `resume.pdf`.

The lines are a floor, not the break. Print keeps each entry whole rather than
splitting a role across pages, so the real break can land above a line and the
page count can come out higher, never lower. A résumé whose last entry touches
the second line is already over.

The lines assume 96dpi, which is what print CSS assumes. Changing the print
dialog's scale moves the real break and the lines will not follow it, so leave
scale alone.

**No browser at all**, on a headless box: there is no render, and the markdown is
the deliverable. Say that plainly instead of producing nothing. Most forms take
pasted text, and the file is already readable.

## Optional, only if the person already has it

Neither is a default, neither gets suggested twice, and the loop is complete
without both.

| Tool | For | Command | Note |
|---|---|---|---|
| `pandoc` | A `.docx`, where an employer demands one | `pandoc resume.md -o resume.docx` | GPL. Two things. Its PDF output needs a separate engine installed, so do not route the PDF through it. And pandoc reads a bare newline inside a paragraph as a space, so put a backslash at the end of the headline, each contact line and each Skills row in the copy you convert, or they run together on one line |
| `resumed` | Someone who already keeps a `resume.json` | `resumed render resume.json` | MIT, npm. Needs a theme package installed first, which is a network install, which is why it is not the path here |

A number that belongs on a résumé goes into `resume/master.md` first, sourced
from the numbers table in `profile.md`. A tailored copy draws only from the
master. That is what makes the number check below mean anything.

## Where a tailored copy lives

Never in the master. Never only in a chat window.

```
~/job-hunt/
  resume/
    master.md            everything, never tailored, never edited for a posting
    original.docx        what they arrived with
  applications/
    2026-08-27-northwind-fde/
      posting.md
      review.md
      resume.md          the tailored copy
      resume.pdf         saved out of the browser
      letter-brief.md
      changes.md
```

The folder name is `<date>-<company>-<role>`, lowercase, hyphens, no spaces. The
date is the day the pack was built.

That naming is doing three jobs. It sorts chronologically, so the recent
applications are the ones at the bottom. It greps by company, which is what
happens six weeks later when a recruiter calls about a role the person half
remembers. And it keeps twenty applications as twenty readable records instead of
twenty files called `resume-final-2.md`.

## Proving the tailored copy added nothing

Tailoring may reorder, reword and cut. It may not add a fact. Four checks. Three
are pass or fail, one is for reading, and the section ends by naming what none of
them catch, because a check whose limits are not written down gets trusted past
them.

Run all four from the job-hunt folder and paste the output at the bottom of
`changes.md`, including when it is empty. A check whose result nobody wrote down
did not run.

**Read the diff.** Works whether or not the folder is a git repo:

```bash
git diff --no-index --word-diff resume/master.md applications/<folder>/resume.md
```

Every `{+added+}` is a claim to justify. The limit: a moved block reads as
removed in one place and added in another, so a reordered résumé produces a
large diff. This one is for reading, not for passing.

**Check the numbers.** Order-blind, which is why it survives reordering.
Tailoring never needs a number the master does not have:

```bash
nums() { grep -oE '[0-9]+([.,][0-9]+)*%?' "$1" | tr -d ',' | sort -u; }
comm -13 <(nums resume/master.md) <(nums applications/<folder>/resume.md)
```

**Check the titles and employers.** Cutting a role is allowed. Retitling one is
not, and title inflation is the fabrication people talk themselves into. This
reads the file's own convention: an entry heading, then the bold employer name on
the line under it.

```bash
heads() { awk '/^###[[:space:]]/{print;h=1;next} /^[[:space:]]*$/{next} h&&/^\*\*/{if(match($0,/\*\*[^*]+\*\*/))print substr($0,RSTART,RLENGTH);h=0;next} {h=0}' "$1" | sort -u; }
comm -13 <(heads resume/master.md) <(heads applications/<folder>/resume.md)
```

It reads only the bold name, not the location and dates after it, so shortening
`**Employer** · Oslo · 2016 to 2022` to `**Employer** · 2016 to 2022` is not a
finding. And it ignores the Skills rows, which use the same `**` shape, because
cutting a skill is a sanctioned CUT and a check that fires on the commonest
honest edit is a check nobody runs twice.

**Check the credentials and the sections.** The cheapest real catch in the set. A
certification, a clearance, a licence or a degree is the highest-stakes thing a
tailored copy can invent, and none of the checks above sees any of it: a
fabricated certification dated in a year the master already mentions passes the
number check, and a fabricated `## Clearance` section passes both.

```bash
hard() { grep -inE 'certif|clearance|licen[cs]e|diploma|degree|accredit|authoriz|^## ' "$1" | cut -d: -f2- | sed 's/^ *//' | sort -u; }
comm -13 <(hard resume/master.md) <(hard applications/<folder>/resume.md)
```

Empty output is a pass on all three. Every line printed is a number, an entry
heading, an employer, a credential line or a whole section that is in the
tailored copy and not in the master. Each one is either a fabrication or a
rewording that changed the characters; both need looking at, and the second gets
fixed by keeping the master's wording.

Windows, same three checks:

```powershell
function Nums($p) {
  (Select-String -Path $p -Pattern '[0-9]+([.,][0-9]+)*%?' -AllMatches).Matches.Value |
    ForEach-Object { $_ -replace ',', '' } | Sort-Object -Unique
}
function Heads($p) {
  $h = $false
  Get-Content $p | ForEach-Object {
    if ($_ -match '^###\s') { $_; $h = $true }
    elseif ($_ -match '^\s*$') { }
    elseif ($h -and $_ -match '(\*\*[^*]+\*\*)') { $Matches[1]; $h = $false }
    else { $h = $false }
  } | Sort-Object -Unique
}
function Hard($p) {
  Select-String -Path $p -Pattern 'certif|clearance|licen[cs]e|diploma|degree|accredit|authoriz|^## ' |
    ForEach-Object { $_.Line.Trim() } | Sort-Object -Unique
}
function Added($a, $b) {
  Compare-Object $a $b | Where-Object SideIndicator -eq '=>' | ForEach-Object InputObject
}
$m = 'resume/master.md'; $t = 'applications/<folder>/resume.md'
Added (Nums $m) (Nums $t); Added (Heads $m) (Heads $t); Added (Hard $m) (Hard $t)
```

### Record the master's fingerprint

One more line at the bottom of `changes.md`, from `sha256sum resume/master.md`
(or `Get-FileHash resume/master.md -Algorithm SHA256`).

All four checks compare the tailored copy against the master, so they are
worthless if the master itself was edited to suit the posting. That is the one
failure that passes everything by construction, and it then persists into every
later application, each of which also passes. The fingerprint does not prevent
it. It makes it findable afterwards with one grep across the application folders,
which is enough, because the person only needs to catch it once.

### What none of this catches

A tailored copy that keeps the title, keeps the numbers, and inflates a bullet
from "contributed to" to "owned". Nothing mechanical sees that. `9 weeks`
reworded to `9 months` also passes, because `9` is in the master.

The mechanical guarantee covers numbers, entry headings, employer names,
credential lines and section headings. Everything past that rests on the labeled
`changes.md` and on lens 3, the hostile hiring manager. Say that plainly rather
than letting an empty check output read as a clean bill of health.
