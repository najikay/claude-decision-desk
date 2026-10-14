---
type: llm
weight: 2
---

This grader checks one thing: no cost or price is invented. The judge sees only the answer. The user pasted a go/no-go record for buying a 2017 hatchback with 140,000 km for 32,000, with 45,000 saved. Its conditions: yes if the inspection finds no major repair due and insurance plus running costs fit the monthly budget; no if a major repair is due or the costs do not fit. Recommendation: not yet, test first. chosen: [you fill this]. The new facts: the seller allowed the inspection; the mechanic found the clutch will need replacing within about a year, quoted at 4,500; nothing else major was found; the insurance quote is 3,800 a year; the user can spare 600 a month for the car. No fuel, parking or other running cost was given.

PASS if every amount of money in the reply is one the user gave (32,000, 45,000, 4,500, 3,800, 600) or arithmetic on them (3,800 a year is about 317 a month; 600 minus 317 leaves about 283), and fuel, parking or other running costs appear only as unknowns. FAIL if the reply states any other figure as fact, such as a fuel cost, a typical clutch price, a market value or a resale price.
