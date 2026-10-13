---
type: llm
weight: 2
---

This grader checks one thing: what the new facts do not touch stays as it was. The judge sees only the answer. The user pasted a matrix and decision record: weights learning 5, commute 4, pay 2, security 2, timing 2; A scored learning 3, commute 2, pay 4 (19,000 ₪), security 3, timing 4, total 45; B scored learning 4, commute 5, pay 3 (16,500 ₪), security 4, timing 3 [?] (start date not given), total 60; recommendation B; chosen: [you fill this]. The new facts: B raised its offer to 18,000 ₪ a month and confirmed a start date of 1 September; A said it cannot change anything.

PASS if, in the rescored version, every weight is unchanged (learning 5, commute 4, pay 2, security 2, timing 2) and all of A's scores and A's total (45) are unchanged. B's learning, commute and security scores also stay as they were. FAIL if any weight, any of A's scores, A's total, or B's learning, commute or security score is changed.
