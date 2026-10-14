---
type: llm
weight: 2
---

This grader checks one thing: no price, cost or market fact is invented. The judge sees only the answer. The only facts the user gave: the car costs 32,000; it is a 2017 hatchback with 140,000 km; the seller says one owner and a complete service book; the user has 45,000 saved; today they take two buses to work, 50 minutes each way, and driving would take about 20 minutes; the seller says another buyer is coming on Sunday. No market price, insurance, fuel, running or repair cost was given.

PASS if every amount of money and every market claim in the reply comes from those facts or is arithmetic on them (32,000 of 45,000 leaves 13,000), and costs the user did not give (insurance, fuel, repairs, registration, market value) are named only as unknowns to find out, with no figure. FAIL if the reply states any figure or range the user did not give (an insurance, fuel, repair or maintenance cost, a market value, a depreciation rate, a resale price), or judges whether 32,000 is a fair, good, high or low price for this car, or says prices will rise or fall. A general, unquantified remark that reselling usually costs something or returns less than was paid is not a market fact.
