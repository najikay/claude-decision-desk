---
type: llm
weight: 2
---

This grader checks one thing: the deadline is asked for or marked as not set. The judge sees only the answer. The user said only: they are finishing their degree, they have a job offer from a big company, and they have a place in the master's program at their university; they are confused and keep going back and forth. They gave no deadline, no salary or terms, no cost or funding for the master's, and did not say whether the place can be deferred.

PASS if the reply asks by when the user has to decide or answer (the offer's reply date, the master's confirmation date), or marks the deadline as not set or unknown (`[not set]`, `[?]`). FAIL if it assumes a specific date, or never raises the question of a deadline.
