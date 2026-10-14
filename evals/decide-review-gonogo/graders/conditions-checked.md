---
type: llm
weight: 2
---

This grader checks one thing: the record's conditions are checked against the new facts. The judge sees only the answer. The user pasted a go/no-go record for buying a 2017 hatchback with 140,000 km for 32,000, with 45,000 saved. Its conditions: yes if the inspection finds no major repair due and insurance plus running costs fit the monthly budget; no if a major repair is due or the costs do not fit. Recommendation: not yet, test first. chosen: [you fill this]. The new facts: the seller allowed the inspection; the mechanic found the clutch will need replacing within about a year, quoted at 4,500; nothing else major was found; the insurance quote is 3,800 a year; the user can spare 600 a month for the car. No fuel, parking or other running cost was given.

PASS if the reply takes the record's conditions (the repair condition and the costs-fit-the-budget condition) and says for each whether it is now met, not met, or still unknown, using the new facts (the clutch at 4,500 within about a year; insurance 3,800 a year against 600 a month; fuel and other running costs not given). FAIL if it gives a new verdict without going through the conditions, or ignores one of them.
