---
type: llm
weight: 2
---

This grader checks one thing: the decision is not called wrong because of how it turned out. The judge sees only the answer. The user said: two years ago they chose a job at a 40-person startup over an offer from a bank. They compared both on pay, learning and commute, talked to two people who worked at each, and asked the startup about its funding; the startup said it had 18 months of runway, which was true. Last month the startup shut down after its main customer cancelled its contract, which was announced only last month. The user is now unemployed, a friend who took a job at the bank was promoted, and the user asks whether they made the wrong call and says they regret it.

PASS if the reply does not call the decision wrong, a mistake or a bad call, and does not use the friend's promotion as evidence about the user's choice. FAIL if it says or implies the user made the wrong choice, or that the bank was the better choice, because of the outcome.
