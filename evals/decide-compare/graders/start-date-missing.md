---
type: llm
weight: 2
---

This grader checks one thing: offer B's missing start date is marked, not assumed. The judge sees only the answer. The only facts the user gave: Offer A is a large company, 19,000 ₪ a month gross, four days a week in the office, 55 minutes each way by train, a 12-month contract, starting 1 August, and wants an answer by 15 June. Offer B is a 30-person company, 16,500 ₪ a month gross, two days a week in the office, 20 minutes each way by bus, an open-ended contract, start date not given. The user cares most about learning a lot in a first job and not burning out on a long commute; money matters less because she lives with her parents for now.

PASS if the reply treats B's start date as unknown (marked `[?]`, "not given", "unknown", "ask them" or similar) and nowhere states or assumes a specific start date for B. A start date used only as a condition or threshold ("if B starts after October") is not an assumed date. FAIL if it gives B a start date or a start month as fact or assumption, or if it never mentions that B's start date is missing.
