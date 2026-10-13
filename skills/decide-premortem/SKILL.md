---
name: decide-premortem
description: "Before you commit, imagine it failed and work out why: the likeliest causes ranked, the early warning sign of each, what lowers each now, and the signal at which you should reverse. Use when the user says \"I've decided to\", \"what could go wrong\", \"am I missing something\" or \"stress-test this plan\". Not for making the decision (decide-compare, decide-gonogo), or for generic risk lists with nothing of the user's situation in them."
---

# Pre-mortem a decision

Input: a decision the user has made or is about to make, and the facts they give about it (dates, money, people, terms). With a decision but no facts about the situation, say so and ask for the three or four that matter (when it starts, what it costs, who is affected, what is fixed in a contract); a pre-mortem built from nothing is a generic risk list.

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

## How to run it
1. **Do not re-argue the decision.** The user has decided or nearly; your job is to make it more likely to work. If one of their facts makes the plan look unworkable, say so once, plainly, as one cause in the table, and go on.
2. **Set the scene in one line**: "It is [a date or a point the user gave, such as the end of the trial period], and this did not work. Why?"
3. **Causes from the user's situation.** Three to six causes, each tied to a fact the user gave, quoted or named ("the course fee is due in full before the first week, so one late payment ..."). Rank them by how likely they are, judged from what the user said, and say what the rank rests on. A cause that rests on something the user did not say is marked `assumption` with what you assumed. A cause that fits any plan of this kind and uses none of the user's facts does not go in.
4. **Nothing invented about the place, the company, the course or the people.** No neighbourhoods, prices, rents, climate, culture, how a company treats new staff, how hard a course is, unless the user said it. General knowledge ("in general, the first months in a new city are the loneliest") only as a sentence starting "In general," and only to explain a cause the user's facts already raise.
5. **For each cause**: the early sign the user could notice (concrete and observable, with when to look), and what they can do now, before it starts, to lower it (cheap and specific to their facts).
6. **One kill criterion**: the signal, with a date or a number, at which the user should reverse or change the plan ("if by the end of the second term you have failed more than one module, switch to part-time"). It must be something the user can check, not a feeling. Add the date to check it.
7. **What would change the picture**: the one fact, if it turned out differently, that would move the top cause down the list or off it.

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
1. One line: the decision, as the user stated it, and the point in time the pre-mortem looks back from.
2. **Pre-mortem table**: `#` · `cause (from what you said)` · `early sign` · `lower it now` · `how likely, from what you said`, ranked, with `assumption` marked where it applies.
3. **Kill criterion**: one line, with the date or number and when to check it.
4. **What would change the picture**: one line.
5. **Decision record** in a code block: `decision`, `deadline`, `options`, `kill criterion`, `chosen: [you fill this]`, `revisit` (the kill-criterion check date).
6. **Next:** "put the check date in your calendar; on that date, paste this record with what happened and say *rescore this* (decide-review)."
