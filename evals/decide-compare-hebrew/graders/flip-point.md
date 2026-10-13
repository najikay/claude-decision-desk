---
type: llm
weight: 2
---

This grader checks one thing: the reply names the single change that would flip its recommendation, with its size. The judge sees only the answer, which is in Hebrew. The user wrote in Hebrew, asking for help choosing between two flats. Flat A (in Hebrew "דירה א"): 4,200 ₪ a month, 10 minutes' walk from campus, fourth floor with no lift, one-year lease. Flat B ("דירה ב"): 3,600 ₪ a month, 35 minutes by bus from campus, with a flatmate, two-year lease. What matters most: quiet for studying and a short journey, and the budget is limited. The user must answer flat A's landlord by Thursday.

PASS if the reply names a specific single change that would reverse its recommendation and says how big it is or where the threshold lies: a particular weight moving to a stated value, a particular score changing to a stated value, or a fact crossing a stated threshold (for example, if the flatmate turns out to be noisy, or if the budget cannot reach 4,200 ₪). FAIL if there is no such statement, or if it only says something vague ("it depends on what matters more to you") with no particular weight, score or threshold.
