---
type: llm
weight: 2
---

This grader checks one thing: the user's numbers survive exactly. The judge sees only the answer. The user wrote in Hebrew, asking for help choosing between two flats. Flat A (in Hebrew "דירה א"): 4,200 ₪ a month, 10 minutes' walk from campus, fourth floor with no lift, one-year lease. Flat B ("דירה ב"): 3,600 ₪ a month, 35 minutes by bus from campus, with a flatmate, two-year lease. What matters most: quiet for studying and a short journey, and the budget is limited. The user must answer flat A's landlord by Thursday.

PASS if the reply gives flat A's rent as 4,200 ₪ (or 4200) and flat B's rent as 3,600 ₪ (or 3600), and every journey time it states is the one given (10 minutes for A, 35 minutes for B). FAIL if a rent or journey time is rounded, converted, changed, or replaced with a different number, or if either rent is missing.
