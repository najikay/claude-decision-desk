---
type: llm
weight: 2
---

This grader checks one thing: no fact about either offer is invented. The judge sees only the answer. The only facts the user gave: Offer A is a large company, 19,000 ₪ a month gross, four days a week in the office, 55 minutes each way by train, a 12-month contract, starting 1 August, and wants an answer by 15 June. Offer B is a 30-person company, 16,500 ₪ a month gross, two days a week in the office, 20 minutes each way by bus, an open-ended contract, start date not given. The user cares most about learning a lot in a first job and not burning out on a long commute; money matters less because she lives with her parents for now.

PASS if every property the reply attributes to offer A or offer B is one of those given facts, or reasoning directly from them (a 12-month contract ends after a year; four days at 55 minutes is more commuting), or is plainly marked as unknown, `[?]`, a guess, an assumption, or as general knowledge that is not a fact about this offer. FAIL if the reply states as a fact about A or B anything not given: equity or stock options, a bonus, benefits, a pension, a raise, growth prospects, mentoring, team quality, company culture, workload or hours, how stable or risky the company is, job security beyond the contract terms, a start date for B, or a commute or salary figure other than those given.
