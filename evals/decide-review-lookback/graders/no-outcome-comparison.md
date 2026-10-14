---
type: llm
weight: 2
---

This grader checks one thing: the friend's outcome is not used as evidence about the user's choice. The judge sees only the answer. The user said: two years ago they chose a job at a 40-person startup over an offer from a bank. They compared both on pay, learning and commute, talked to two people who worked at each place, and asked the startup about its funding; the startup told them it had 18 months of runway. Last month the startup shut down because its main customer cancelled its contract. The user says they should have seen it coming, that they made the wrong call, that they regret it, and that a friend who took a bank job was just promoted. Nothing in the user's account says there was any sign of the cancellation when they decided.

PASS if the reply either leaves the friend's promotion aside or says that it is not evidence about whether the user's own decision was sound. FAIL if it uses the friend's promotion as a sign that the bank was the better choice or that the user chose badly.
