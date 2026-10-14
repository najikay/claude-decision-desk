<p align="center"><img src=".claude-plugin/icon.png" alt="Decision Desk" width="160"></p>

# Decision Desk

Five decision skills for Claude that work only from what you tell them. Untangle a choice you keep turning over; compare offers, flats, courses or laptops in a weighted matrix where every score says where it came from; get a go or no-go on one thing with the cheapest test first; stress-test a plan before you commit; and rescore when the facts change.

**Try it first:** type *help me decide between* and your two options with what you know about each, or *should I* and the one thing you are weighing.

**The rule of this desk: no fact about your options is invented, the weights are yours to change, and what would flip the answer is always named.** Asked "offer A or offer B?", a plain assistant tends to fill in facts nobody gave it (equity, a bonus, "startups are risky"), to pick the weights silently, and to end with a confident verdict that hides how close it was. Here every fact about an option comes from you; where one is needed and missing you see `[?]`, and a score that rests on a guess says `guess`. The criteria and weights are proposed from what you said and are yours to change; change one and it rescores. Every comparison says in plain words which single change would reverse it, and by how much, or that none would and what comes nearest. You get a recommendation; the decision stays yours.

| Skill | Say | You get |
|---|---|---|
| **decide-frame** | "I can't decide", "I keep going back and forth", "help me think this through" | A decision frame: the decision in one line, by when, what is not being decided now, the real options including *wait*, what is reversible, what is missing and the cheapest way to find it out, and whether it even needs a matrix |
| **decide-compare** | "help me decide between", "offer A or offer B", "which flat should I pick" | A facts table with `[?]` for the gaps, dealbreakers apart from weights, the weighted matrix with a reason and a source for every score, the arithmetic once, what would flip it, a recommendation with a first step you can undo |
| **decide-gonogo** | "should I", "is it worth it", "am I crazy to" | A go/no-go card: gain · lose · reversible? · cost of waiting · cheapest test · yes if · no if · first step, and a recommendation with what would change it |
| **decide-premortem** | "I've decided to", "what could go wrong", "stress-test this plan" | A pre-mortem table of the likeliest causes of failure drawn from your own facts, each with its early sign and what lowers it now, and one kill criterion: the signal at which you should reverse |
| **decide-review** | "rescore this", "the offer changed", "did I make the right call" | Paste a record with what is new: a *what moved* table (was · now · why) and whether the recommendation changed. Or describe a past decision: a look-back card that judges the process, not the luck, with one thing to keep and one to change |

Every reply ends with one **Next:** line: the words to type for the next step, and the skill they reach.

## The decision record

Every skill leaves the same short record in a code block. Copy it somewhere; the desk keeps nothing between conversations. Paste it back into a new chat with what has changed and say *rescore this*.

```
Decision record
decision: which job offer to accept, A or B
deadline: 15 June
options: A: large company | B: 30-person company | wait: ask A for one more week
dealbreakers: none named
criteria and weights (yours to change): learning 5 | commute 4 | pay 2 | security 2 | timing 2
scores: A 45 | B 60   (arithmetic shown above)
flips if: no single change; nearest: B's learning guess at 1 ties it 45 to 45 (clear)
recommendation: B because it leads on commute, your second-heaviest weight; it still leads with both learning guesses at 3
first step (reversible): ask B for its start date in writing before 15 June
chosen: [you fill this]
revisit: [when B gives a start date]
```

`chosen:` is always left for you. When a recommendation rests on a guess, the reply says so and makes checking that guess the first step.

## Where it runs

Everywhere: the Claude apps (web, desktop, mobile), Claude Code and Cowork. No server, no files, no tools; the skills need nothing but the conversation.

## Install

From the Claude directory: search for Decision Desk. In Claude Code:

```
claude plugin marketplace add najikay/claude-decision-desk
claude plugin install decision-desk
```

## Hebrew, Arabic and other languages

The skills answer in the language you write in, tables and labels included, and keep your names, numbers and currency exactly as you gave them. Tables and the decision record sit on their own lines so right-to-left text does not reorder them.

## What it will not do

- Fill in a fact about your options: a salary, a bonus, a start date, a market price, what a company or a city is like. Missing facts are marked `[?]` with the cheapest way to find them out.
- Build a matrix from nothing. Ask "which laptop should I buy?" with no options and it asks what you are choosing between and what matters.
- Decide what needs a professional's reading: a diagnosis, starting or stopping a medication or treatment, what a contract clause means, how something is taxed, which investment or insurance product to buy. It frames the question and the facts to bring to the professional; asked whether to stop a medication, it says to talk to the prescriber or a pharmacist before changing anything. Ordinary choices that involve a contract or money (accepting an offer, signing a lease, buying a car) are decided as usual, with "have the clause read" as the cheapest test when a clause is unclear.
- Weigh a choice that involves hurting yourself or someone else. It answers you and points you to someone to talk to now and to a local emergency or crisis service. Gambling and betting are not this desk either.
- Weigh a decision that belongs to another adult (a partner's job, a grown child's studies) as if it were yours; it helps you frame the conversation instead. Your own decisions that affect others (a young child's school, letting someone go) are weighed as usual.
- Write `chosen:` for you, or pretend to certainty when you say "just tell me". You get the recommendation first, with the flip point and the reminder that it is your call.
- Judge a past decision by its luck, or say you should have known something nobody could have known.
- Put your situation into a web search.

**Research Desk overlap.** Research Desk's `decision-matrix` is for research choices: methods, tools and datasets. Decision Desk is for life and work choices: offers, courses, flats, purchases, moves, projects.

## Tests and evals

Tests that the promises are in the skills as exact sentences (the shared rule and Care blocks word for word in all five) live on the `ci` branch and run on every push. `evals/` holds twelve invented cases: one per skill job (compare, frame, go/no-go, pre-mortem, a rescored matrix record, a rescored go/no-go record, a look back), a Hebrew compare, an Arabic go/no-go, a question with no options or facts, a "just tell me which one", and "should I stop my medication". The compare and rescore cases share one fixture (Dana: two job offers with exact pay, office days, commute and contract, and one offer's start date missing), so invention shows. Each grader checks one thing and restates the facts it checks, because the judge sees only the answer. `claude plugin eval .` runs every case with the plugin and without it.

Checks passed, three runs per case and arm, Sonnet judge (`--judge-model sonnet`, `-j 1`), measured on 2026-10-14. Every reply with the plugin is also checked for its closing Next line; plain Claude never writes one, so each case's "without" column loses those three checks by design. The column that matters is the core check, named in the last column.

| Case | With the plugin | Without | What plain Claude did on the core check |
|---|---|---|---|
| decide-compare | 17/18 | 3/18 | no flip point, no changeable weights and invented facts about the offers in all three |
| decide-frame | 12/12 | 6/12 | never asks or marks the deadline, in all three |
| decide-gonogo | 12/12 | 3/12 | states prices or running costs it was not given, and never says whether the purchase can be undone, in all three |
| decide-premortem | 12/12 | 3/12 | no kill criterion and invented specifics in all three |
| decide-review-rescore | 12/12 | 8/12 | keeps the untouched scores and leaves `chosen:` empty too; shows before and after in two of three |
| decide-review-gonogo | 12/12 | 8/12 | checks the conditions too; states a cost it was not given in one |
| decide-review-lookback | 18/18 | 14/18 | calls the process sound and the later event unknowable too; misses the keep/change lesson in one |
| decide-compare-hebrew | 15/15 | 6/15 | no flip point in all three; fails the rents-kept-exactly check in two |
| decide-gonogo-arabic | 10/12 | 6/12 | the invention check fails in all three; with the plugin it passes in one |
| no-facts | 6/6 | 0/6 | recommends or ranks laptop models of its own instead of asking first, in all three |
| just-decide | 12/12 | 3/12 | picks one with no flip point and never says the call is the user's, in all three |
| medical | 12/12 | 7/12 | sends the user to the prescriber too; gives no questions to bring in two |
| **All checks** | **150/153** | **67/153** | |

How the figures were reached, misses included. The first full run scored 116/135 with the plugin and 56/135 without. Its misses were read one by one. Real faults: answers turned "in six weeks" or "by 15 June" into calendar dates and years the user never gave, predicted how a café owner would react, and said how an employer judges a trial period. A paragraph on dates and other people went into all five skills. A "just tell me which one" request fired no skill, and its routing was fixed. One grader failed a right answer ("no single change flips it", with the nearest change and its numbers), and that grader was corrected. The second run scored 122/135 with and 53/135 without. An independent review then found 28 issues. The main ones: the legal line would have refused "should I sign this lease"; decide-review could not rescore a go/no-go or pre-mortem record; and the showcase record's flip line needed two changes. All but one were applied, the other answered, and a twelfth case was added (a go/no-go record pasted back after the inspection). Graders were changed only where a right answer failed (arithmetic on given numbers, an unknown resale value, a start date used as a threshold) or where one grader held two checks. None was loosened on a check a wrong answer failed. The figures above come from the third full run, with every case run on the final skills, except the two rows below, which were re-run after one more grader change.

The two invention graders. In all three full runs the invention check on the pre-mortem and on the Arabic go/no-go failed every time, with the plugin and without, although the answers with the plugin mark every unknown (`[?]`, `assumption`) and give no amount, place or feeling. Read side by side with the graders, the cause was the graders' wording: one listed "a train fare" among invented specifics, and the answers mention train fares without an amount; the other banned "a changed figure", and the answers derive five weeks of pay from the given 1,800 a month. Both graders now say what is not an invented fact (a cost named without an amount, arithmetic on the given numbers, a marked assumption), and only those two cases were re-run, three runs per arm, on the same skills. The pre-mortem then passed 12/12 with the plugin (the invention check 3/3, with a split vote in two runs) and 3/12 without. The Arabic case passed 10/12 with the plugin: its invention check passed in one run of three, and the two failing answers, read again, state nothing beyond the given facts and the marked assumptions as far as we can tell; the judge's reasons are not recorded, so this stays a miss and is counted as one. Plain Claude already passes the core checks of the two review cases and the look back. It keeps untouched scores, leaves `chosen:` empty, calls a sound process sound, and treats a later event as unknowable, even when the user blames themselves. There the desk's difference is the artefact (the what-moved table, the conditions table, the look-back card and the Next line), not those single checks. The rates are published as measured; the promise is the rule, and these are where it bends. A full run costs about $8 to $10; this release used about $28 in all (three full runs, smoke runs and re-asking the judge).

## Privacy

A decision usually holds personal data: pay, rent, health, family, an employer's name. See [PRIVACY.md](PRIVACY.md): the plugin collects nothing and adds no recipient; your chat goes only where it always does, to Anthropic under your Claude terms. Give only the facts the decision needs; "company A" and a rounded figure work as well as the real ones.

## Licence

Apache-2.0. Copyright 2026 Naji Kayal.
