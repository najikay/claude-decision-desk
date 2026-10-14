---
type: llm
weight: 2
---

This grader checks one thing: the reply names the single change that would flip its recommendation, with its size. The judge sees only the answer. The only facts the user gave: Offer A is a large company, 19,000 ₪ a month gross, four days a week in the office, 55 minutes each way by train, a 12-month contract, starting 1 August, and wants an answer by 15 June. Offer B is a 30-person company, 16,500 ₪ a month gross, two days a week in the office, 20 minutes each way by bus, an open-ended contract, start date not given. The user cares most about learning a lot in a first job and not burning out on a long commute; money matters less because she lives with her parents for now.

PASS if the reply names a specific single change that would reverse its recommendation and says how big it is or where the threshold lies: a particular weight moving to a stated value ("if pay weighed 5 instead of 2, A would win"), a particular score changing to a stated value, or a fact crossing a stated threshold ("if B cannot start before October"). Also PASS if the reply says plainly that no single change reverses it and gives, with numbers, the nearest change or pair of changes that would (for example "no single change flips it; the nearest is B's learning guess at 1, which ties 45 to 45"). FAIL if there is no such statement, or if it only says something vague ("if money matters more to you, A could make sense", "it depends on your priorities") with no particular weight, score or threshold.
