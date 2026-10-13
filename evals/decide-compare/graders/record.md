---
type: llm
weight: 1
---

This grader checks one thing: the reply leaves a decision record the user can keep. The judge sees only the answer.

PASS if the reply contains a block headed "Decision record" (or plainly the same thing) with separate lines for at least the decision, the options, the recommendation and a "chosen" line. FAIL if there is no such block.
