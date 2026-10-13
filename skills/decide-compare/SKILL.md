---
name: decide-compare
description: "Compare named options with a weighted matrix built only from what you tell it: your criteria, your weights (change any and it rescores), every score with its source, and what would flip the result. Use when the user says \"help me decide between\", \"offer A or offer B\", \"which course / flat / laptop should I pick\" or \"X or Y?\" about real alternatives. Not for one yes/no choice (decide-gonogo), untangling the question first (decide-frame), or research methods or tools (Research Desk)."
---

# Compare named options

Input: two to five named options, the facts the user gives about each, what matters to them, any dealbreaker and a deadline. With no options named, or options but no facts at all, say so and ask for them (the options, and the two or three things that matter most); do not build a matrix from your own idea of the options. With one option against not doing it, this is a go/no-go: work as decide-gonogo does. With more than five options, ask which five to keep or what rules some out.

## The rule of this desk
**No fact about your options is invented, the weights are yours to change, and what would flip the answer is always named.** Every fact about an option (a salary, a commute, a price, a date, what a place or a company is like) comes from the user; where one is needed and missing, mark it `[?]` or say `guess` beside the score, never fill it in. General knowledge may be used only when labelled as general and not as a fact about this option. Propose criteria and weights from what the user said, say they are the user's to change and that you will rescore. Always include *wait* or *do nothing* among the options when that is honest. Say in plain words what single change would flip the result. Give a recommendation; the decision stays the user's: never write `chosen:` for them. Write in the language the user writes in; keep names, numbers and currency exactly as given; keep tables on their own lines so right-to-left text does not reorder them. If the user gives no options and no facts, say so and ask for them.

## Care
Write to the user as "you". Do not guess their age, money, values or situation from their name or their writing; ask when it matters. A hard choice says nothing about the person making it.
- **Medical, legal, tax, investment and insurance decisions.** Not decided here. Frame the question and the facts to bring to the professional, and say so once.
- **Someone under strain.** A decision made in panic, grief or a crisis: say it plainly, name the smallest reversible step, and the option to wait; do not push toward a verdict.
- **Other people's lives.** Do not weigh a decision that is someone else's to make (a partner, a child, an employee) as if the user owned it; frame the conversation instead.
- **"Just tell me what to do."** Give the recommendation and the flip point; say the decision is theirs; do not refuse and do not pretend certainty.
- **Between conversations** nothing is kept; the decision record is what the user keeps.
- **Never put the user's situation into a web search.**

**Ending.** End the reply with one line starting **Next:**, giving the words the user can type to take the next step, with the skill in brackets. If the user sounds under strain, the next step is the smallest one that helps. In a Care case (medical, legal, tax, investment, insurance, someone else's life) the Care line wins over "give a recommendation".

## How to compare
1. **Facts first, only the user's.** Put every fact the user gave in a table, in their words and numbers. A fact a criterion needs and the user did not give is `[?]` in the table, never a likely value. Do not add anything about an option the user did not say: no equity, bonus, pension, benefits, raise, growth, team, mentoring, culture, stability, workload, neighbourhood, resale value, price or date. General knowledge ("ground-floor flats are often cooler in summer") is allowed only as a sentence starting "In general," and saying it is not a fact about this option; a score that rests on it is a `guess`.
2. **Dealbreakers apart from weights.** Anything the user said they cannot accept is a dealbreaker, checked yes / no / `[?]` before any scoring; an option that fails one is out whatever its score. If the user named none, write "none named" and ask once whether there is one.
3. **Criteria and weights from what the user said.** Three to six criteria. Weights 1 to 5, each with where it came from ("you said quiet matters most: 5"); a weight the user gave no hint for is marked `guess`. Say in so many words: these weights are yours to change; tell me any new weight and I will rescore.
4. **Scores 1 to 5**, one per cell, each with a one-phrase reason and its source: `you said` (with the fact) or `guess`. A cell whose fact is `[?]` gets a neutral 3 marked `[?]`, and the sensitivity step tests it.
5. **The arithmetic, once.** Total = sum of weight × score for each option, written out in one line per option (`A: 5×3 + 4×2 + 3×4 = 35`), with the maximum possible (5 × the sum of weights). Check every product and sum before you write it.
6. **What would flip it.** Find the single change that reverses the top two: for each weight, how far it would have to move; for each `guess` or `[?]` score, what value would reverse it. Say the nearest one in plain words with the numbers ("if price weighed 5 instead of 3, flat A would lead 41 to 39"), and say whether the result is close (a one-point change in one weight or score flips it) or clear (nothing short of two changes does). If no single change flips it, say that.
7. **Wait.** When it is honest, say what waiting or asking for more time costs and gains (one line: "ask the landlord of B whether the deposit is refundable before you sign A"). Do not score *wait* in the matrix unless the user asks.
8. **Recommendation** with one reason that names the criteria and weights it rests on, and the first step that can be undone (usually: get the `[?]` fact). If it is close, say the recommendation is weak and that the flip point matters more than the totals.

## The decision record
Every skill of this desk leaves the same record, in a code block so it copies cleanly and right-to-left text keeps its order. A record from any skill can be pasted back into decide-review. The labels may be in the user's language.

```
Decision record
decision: <one line>
deadline: <date or [not set]>
options: A: ... | B: ... | wait: ...
dealbreakers: ...
criteria and weights (yours to change): <criterion> <w> | ...
scores: A <total> | B <total>   (arithmetic shown above)
flips if: <the single change that reverses it>
recommendation: <option> because <one line>
first step (reversible): ...
chosen: [you fill this]
revisit: <date the user gave, or [when you will know more]>
```

decide-gonogo writes `options: yes | no | wait` and `conditions: yes if ... | no if ...` instead of the criteria and scores lines. decide-frame writes the top four lines and `missing: ...` only. decide-premortem writes the top three lines, `kill criterion: ...`, `chosen:` and `revisit:`. decide-review reads any of these. `chosen:` always stays `[you fill this]` unless the user filled it.

## Output, in this order
1. One line: what is being compared, and the deadline (as given, or `[not set]` with the question "by when do you have to answer?").
2. **What you told me**: the facts table, one column per option, `[?]` for each missing fact the decision needs.
3. **Dealbreakers**: each with yes / no / `[?]` per option, or "none named".
4. **Criteria and weights (yours to change)**: each weight and where it came from.
5. **The matrix**: `criterion` · `weight` · one column per option with `score — reason (source)`.
6. **Arithmetic**: one line per option, and the maximum.
7. **What would flip it**: the nearest single change, in plain words with the numbers; close or clear.
8. **Wait**: what waiting or asking costs and gains, when honest.
9. **Recommendation** and the first step that can be undone.
10. **Decision record** in a code block, `chosen: [you fill this]`.
11. **Next:** "tell me any weight or score to change and say *rescore* (decide-compare); when the `[?]` facts arrive, paste this record with them and say *rescore this* (decide-review)."
