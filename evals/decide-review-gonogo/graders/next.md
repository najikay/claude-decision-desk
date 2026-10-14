---
type: llm
weight: 1
---

This grader checks one thing: the reply's last line is a "Next:" line that names words to type. The judge sees only the answer. The skill tells the assistant to end every reply with one line that starts with "Next:" (bold or plain) and gives the user the words to type, or the thing to paste, for the next step, often with a skill name in brackets. The line may offer an alternative ("..., or say *rescore* (decide-compare)") or a short sequence ("do the cheapest test, then paste this record and say *rescore this*"); that is still one Next line.

PASS if the last line of the reply, ignoring blank lines and closing code fences, starts with "Next:" and names a phrase for the user to type or something to paste. FAIL if there is no such line, or if other text follows it.
