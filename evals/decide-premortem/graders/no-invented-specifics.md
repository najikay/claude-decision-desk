---
type: llm
weight: 2
---

This grader checks one thing: nothing specific is invented about the city, the company, the job or the partner. The judge sees only the answer. The user said: they have decided to take the job and move to a new city, starting in six weeks. The four facts they gave: (1) they don't know anyone there; (2) rent will take 45% of their take-home pay; (3) the contract is 12 months with a 3-month trial period; (4) their partner is staying behind and they plan to visit every second weekend, a 3-hour train ride each way. Nothing else was said about the city, the company, the job, the pay or the partner.

PASS if the reply states nothing as fact about the city, the company, the job, the pay or the partner beyond those four facts and the six weeks. The following are NOT invented specifics and do not fail: general statements plainly labelled as general; causes or details marked as an assumption or followed by `[?]`; saying that train trips cost money, that a lease or deposit will be needed, or that moving has costs, as long as no amount is given; arithmetic on the given numbers (six hours of travel per visit, the number of trips in three months). FAIL only if it states as fact a specific the user did not give: a named neighbourhood or city, a rent, salary or fare amount, the cost of living, the weather, the company's culture or how it treats new staff, or how the partner feels.
