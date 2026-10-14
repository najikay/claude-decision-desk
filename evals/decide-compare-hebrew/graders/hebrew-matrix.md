---
type: llm
weight: 2
---

This grader checks one thing: the comparison table is in Hebrew. The judge sees only the answer. The user wrote in Hebrew, asking for help choosing between two flats. Flat A (in Hebrew "דירה א"): 4,200 ₪ a month, 10 minutes' walk from campus, fourth floor with no lift, one-year lease. Flat B ("דירה ב"): 3,600 ₪ a month, 35 minutes by bus from campus, with a flatmate, two-year lease. What matters most: quiet for studying and a short journey, and the budget is limited. The user must answer flat A's landlord by Thursday.

PASS if the reply contains a comparison table or matrix of the two flats whose criteria and reasons are written in Hebrew (the expected labels may be in Hebrew, such as "שקט" for quiet, "זמן נסיעה" for journey time, "מחיר" for price, "משקל" for weight; numbers, the ₪ sign and symbols such as `[?]` may stay as they are). FAIL if there is no table, or if the table's criteria and reasons are in English.
