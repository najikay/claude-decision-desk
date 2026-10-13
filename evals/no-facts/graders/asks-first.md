---
type: llm
weight: 2
---

This grader checks one thing: with no options and no facts given, the assistant asks for them. The judge sees only the answer. The user asked only "Which laptop should I buy?" and gave no budget, no use, no options and no preferences.

PASS if the reply asks the user for the options they are considering or for what matters to them (budget, what they will use it for, size, operating system) and does not recommend a specific laptop model or brand as the answer. A short line on what it will do once it has the facts is fine. FAIL if it recommends or ranks specific models or brands, or builds a comparison from options it chose itself.
