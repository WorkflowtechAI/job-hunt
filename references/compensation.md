# Compensation research

Do this before filling any salary field and before quoting any contract rate. Ten
minutes, and the number comes from data instead of nerve.

Used by the apply pack for application forms, and by the contract track for rate
ladders. The output goes in the profile so the next one is a lookup.

## 1. Find the published band

Pay transparency laws in several US states and a growing number of other
jurisdictions force employers to publish ranges. The range therefore often exists
somewhere even when this particular posting omits it.

Greenhouse exposes a public JSON API, no key required, returning every posting for
a company with its compensation string:

```
https://boards-api.greenhouse.io/v1/boards/<company>/jobs?content=true
```

Check the same company's postings in transparency jurisdictions even when the
target req is elsewhere. The band travels between locations more than the
posting suggests.

Where the company is not on Greenhouse, the same trick works on the other ATS
platforms with public boards, and failing that, the company's own careers page
for a sibling role.

## 2. Identify the department

Identical work pays differently depending on whether the req is banded against
engineering or against general and administrative. It shows in the posting
metadata and in the API response.

This is the single largest unexplained variance between two apparently equivalent
roles, and it is invisible unless you look for it.

## 3. Benchmark against real data

For AI, ML and data roles, Foorilla publishes a CC0 salary dataset, a weekly
snapshot of survey responses from 2021 onward:

```
https://raw.githubusercontent.com/foorilla/ai-jobs-net-salaries/main/salaries.csv
```

Public domain, no key, with title, level, location, remote ratio and company
size. Every field has an equivalent; find the person's, record it in the profile,
and prefer a real dataset to a salary-estimator widget.

## 4. Adjust for geography, in both directions

Where the person is outside the employer's home market, the market discount is
real and published nearshore rates show its size. So is the premium for a scarce
specialization, and so is the difference between contractor and employee.

Apply all three. Applying only the one that flatters produces a number that gets
withdrawn in the second conversation.

## 5. Quote contract and employment as a calibrated pair

Where both are possible, work out the two numbers that leave the person
indifferent, and present them together.

They can differ by tens of percent and still net out the same, because
employer-side burden, statutory contributions, benefits and employer-of-record
fees sit on one side while self-employment tax and unpaid time off sit on the
other. Run the arithmetic rather than estimating it.

Presenting both, calibrated, gives the employer a real choice and often makes the
contract option genuinely cheaper for them. That is a considerably stronger
position than one number defended down.

## 6. Cross-border, before quoting

Where the person lives in one country and bills into another:

- Is there a tax treaty, and is there a totalization agreement? They are separate
  instruments and the second is the one people forget.
- What is the tax residency threshold in days, and where does the person sit
  against it?
- Which exclusions cover income tax while leaving self-employment or social
  contributions in place?

Gross up for whatever survives. State plainly that these figures want
confirmation from a cross-border accountant, and never let a quote imply
professional tax advice.

## Record it

Write the result into the profile: the band found, the source, the date, and the
number the person decided on. A researched number that has to be re-derived every
application is half a method.
