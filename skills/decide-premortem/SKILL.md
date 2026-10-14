---
name: decide-premortem
description: "Before you commit, imagine it failed and work out why: the likeliest causes ranked, the early warning sign of each, what lowers each now, and the signal at which you should reverse. Use when the user says \"I've decided to\", \"what could go wrong with my plan\", \"am I missing something about this plan\" or \"stress-test this plan\". Not for making the decision (decide-compare, decide-gonogo), code or document review, or generic risk lists with nothing of the user's situation in them."
---

# Pre-mortem a decision

Input: a decision the user has made or is about to make, and the facts they give about it (dates, money, people, terms). With a decision but no facts about the situation, say so and ask for the three or four that matter (when it starts, what it costs, who is affected, what is fixed in a contract); a pre-mortem built from nothing is a generic risk list.

## The rule of this desk
**No fact about your options is invented, the weights are yours to change, and what would flip the answer is always named.** Every fact about an option (a salary, a commute, a price, a date, what a place or a company is like) comes from the user; where one is needed and missing, mark it `[?]` or say `guess` beside the score, never fill it in. General knowledge may be used only when labelled as general and not as a fact about this option. Propose criteria and weights from what the user said, say they are the user's to change and that you will rescore. Always include *wait* or *do nothing* among the options when that is honest. Say in plain words what single change would flip the result. Give a recommendation where the skill makes one; the decision stays the user's: never write `chosen:` for them. Write in the language the user writes in; keep names, numbers and currency exactly as given; keep tables on their own lines so right-to-left text does not reorder them. If the user gives no options and no facts, say so and ask for them.

## Care
Write to the user as "you". Do not guess their age, money, values or situation from their name or their writing; ask when it matters. A hard choice says nothing about the person making it.
- **Medical, legal, tax, investment and insurance questions.** What needs a professional's reading is not decided here: a diagnosis, whether to start, stop or change a medication or treatment, what a contract clause means or whether a contract can be enforced or broken, liability, how something is taxed, and which investment or insurance product to buy. Frame the question and the facts to bring to the professional, and say so once. For a medication or treatment, the smallest safe step is to talk to the prescriber or a pharmacist before changing anything, and to get help at once if a side effect is severe; in the record write `recommendation: [the professional's call]`. An ordinary choice that involves a contract, money or health (accepting an offer at a given salary, signing a lease, buying a car) is decided here as usual; if a clause is unclear, "have the clause read" is the cheapest test.
- **Someone under strain.** A decision made in panic, grief or a crisis: say it plainly, name the smallest reversible step, and the option to wait. Strain changes the size of the step, not whether a recommendation is given: asked for one, give it.
- **Harm to yourself or someone else.** If a choice involves hurting yourself or another person, do not weigh it as a decision: answer the person, say to talk to someone now and to contact a local emergency or crisis service. Do not invent a phone number.
- **Gambling and betting.** Not this desk: say so once, and do not score a bet.
- **Other people's lives.** A decision that belongs to another adult (a partner's job, a grown child's studies, a friend's relationship) is not weighed as if the user owned it; frame the conversation instead. A decision the user owns that affects others (a young child's school, letting an employee go) is weighed as usual, with the other person's view written as a question `[?]`.
- **"Just tell me what to do."** Put the recommendation, its one reason, the flip point and "the decision is yours" in the first lines; the rest can follow below. Do not refuse and do not pretend certainty.
- **Between conversations** nothing is kept; the decision record is what the user keeps.
- **Never put the user's situation into a web search.**

**Ending.** End the reply with one line starting **Next:**, giving the words the user can type to take the next step, with the skill in brackets. If the user sounds under strain, the next step is the smallest one that helps. In a Care case (a question for a professional, harm, gambling, another adult's decision) the Care line wins over giving a recommendation.

**Dates and other people.** Keep every date and time in the user's own terms: do not add a year, a weekday or a calendar date they did not give, and do not turn "in two months" or "by Friday" into a date; if the year or the date matters and is unclear, write `[?]` and ask. How another person will act (an employer, a landlord, a seller, a partner) is never a fact: write it as a question to ask, with `[?]` ("would the landlord accept a shorter lease? `[?]`"). A claim about the user's own life or about how a place or a company works that the user did not make ("the deposit comes back", "new staff are watched closely") is a guess: mark it `assumption` or leave it out.

## How to run it
1. **Do not re-argue the decision.** The user has decided or nearly; your job is to make it more likely to work. If one of their facts makes the plan look unworkable, say so once, plainly, as one cause in the table, and go on.
2. **Set the scene in one line**: "It is [a date or a point the user gave, such as the end of the trial period], and this did not work. Why?"
3. **Causes from the user's situation.** Three to six causes. Each cause opens with the user's own fact it rests on, quoted ("you said: ..."); anything in the cause beyond that fact is marked `assumption` in the same cell. The things that slip in unmarked: a home shared with a partner, who pays for travel, that there is a lease and what it says, moving or setting-up costs and when they fall, how an employer runs a trial, what a partner feels or plans, the user's savings. Each cause is tied to a fact the user gave, quoted or named ("the course fee is due in full before the first week, so one late payment ..."). Rank them by how likely they are, judged from what the user said, and say what the rank rests on. A cause that rests on something the user did not say is marked `assumption` with what you assumed. A cause that fits any plan of this kind and uses none of the user's facts does not go in.
4. **Nothing invented about the place, the company, the course or the people.** No neighbourhoods, prices, rents, climate, culture, how a company treats new staff, how hard a course is, unless the user said it. General knowledge ("in general, the first months in a new city are the loneliest") only as a sentence starting "In general," and only to explain a cause the user's facts already raise.
5. **For each cause**: the early sign the user could notice (concrete and observable, with when to look), and what they can do now, before it starts, to lower it (cheap and specific to their facts).
6. **One kill criterion**: the signal, with a point in time in the user's terms or a number, at which the user should reverse or change the plan ("if by the end of the second term you have failed more than one module, switch to part-time"). It must be something the user can check, not a feeling. Add when to check it, in the user's terms (the end of the trial period, the first rent day).
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
5. **Decision record** in a code block: `decision`, `deadline`, `options`, `kill criterion`, `chosen: [you fill this]`, `revisit` (when to check the kill criterion, in the user's terms).
6. **Next:** "put the check date in your calendar; on that date, paste this record with what happened and say *rescore this* (decide-review)."
