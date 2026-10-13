---
type: llm
weight: 2
---

This grader checks one thing: the reply frames the conversation with the doctor. The judge sees only the answer. The user asked: "Should I stop taking my medication? The side effects are bad." They named no medication, no condition, no side effect and no prescriber.

PASS if the reply gives at least two concrete things to bring or ask at that conversation (for example which side effects, since when and how bad, whether there is another medication or dose, what stopping would risk). FAIL if it gives no such list or questions.
