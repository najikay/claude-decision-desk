"""The promises Decision Desk makes, checked as the exact sentences that carry them.

Each check reads the body of a skill (the text after the frontmatter) for the sentence that does the
work. Deleting or weakening a rule makes a test fail; a looser check ("the word 'invented' appears
somewhere") would pass with the rule gone.
"""

import os
import unittest
from pathlib import Path

ROOT = Path(os.environ.get("PLUGIN_ROOT") or Path(__file__).resolve().parents[1])
SKILLS = sorted((ROOT / "skills").glob("*/SKILL.md"))
NAMES = ("decide-frame", "decide-compare", "decide-gonogo", "decide-premortem", "decide-review")

RULE = (
    "**No fact about your options is invented, the weights are yours to change, and what would flip the answer is always named.** "
    "Every fact about an option (a salary, a commute, a price, a date, what a place or a company is like) comes from the user; "
    "where one is needed and missing, mark it `[?]` or say `guess` beside the score, never fill it in. "
    "General knowledge may be used only when labelled as general and not as a fact about this option. "
    "Propose criteria and weights from what the user said, say they are the user's to change and that you will rescore. "
    "Always include *wait* or *do nothing* among the options when that is honest. "
    "Say in plain words what single change would flip the result. "
    "Give a recommendation; the decision stays the user's: never write `chosen:` for them. "
    "Write in the language the user writes in; keep names, numbers and currency exactly as given; "
    "keep tables on their own lines so right-to-left text does not reorder them. "
    "If the user gives no options and no facts, say so and ask for them."
)

CARE = (
    "- **Medical, legal, tax, investment and insurance decisions.** Not decided here. Frame the question and the facts to bring to the professional, and say so once.\n"
    "- **Someone under strain.** A decision made in panic, grief or a crisis: say it plainly, name the smallest reversible step, and the option to wait; do not push toward a verdict.\n"
    "- **Other people's lives.** Do not weigh a decision that is someone else's to make (a partner, a child, an employee) as if the user owned it; frame the conversation instead.\n"
    "- **\"Just tell me what to do.\"** Give the recommendation and the flip point; say the decision is theirs; do not refuse and do not pretend certainty.\n"
    "- **Between conversations** nothing is kept; the decision record is what the user keeps.\n"
    "- **Never put the user's situation into a web search.**\n"
)

RECORD = (
    "```\n"
    "Decision record\n"
    "decision: <one line>\n"
    "deadline: <date or [not set]>\n"
    "options: A: ... | B: ... | wait: ...\n"
    "dealbreakers: ...\n"
    "criteria and weights (yours to change): <criterion> <w> | ...\n"
    "scores: A <total> | B <total>   (arithmetic shown above)\n"
    "flips if: <the single change that reverses it>\n"
    "recommendation: <option> because <one line>\n"
    "first step (reversible): ...\n"
    "chosen: [you fill this]\n"
    "revisit: <date the user gave, or [when you will know more]>\n"
    "```\n"
)


def body(name: str) -> str:
    return (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8").split("---\n", 2)[2]


class Rules(unittest.TestCase):
    def test_the_rule_of_the_desk_is_in_every_skill_word_for_word(self):
        for name in NAMES:
            self.assertIn(RULE, body(name), f"{name}: the shared rule block differs")

    def test_the_care_block_is_in_every_skill_word_for_word(self):
        for name in NAMES:
            self.assertIn(CARE, body(name), f"{name}: the Care block differs")

    def test_the_decision_record_is_in_every_skill(self):
        for name in NAMES:
            text = body(name)
            self.assertIn(RECORD, text, f"{name}: the decision record differs")
            self.assertIn("decide-gonogo writes `options: yes | no | wait` and `conditions: yes if ... | no if ...`", text, name)
            self.assertIn("`chosen:` always stays `[you fill this]` unless the user filled it.", text, name)

    def test_every_skill_ends_with_a_next_line_naming_a_skill(self):
        for name in NAMES:
            last = body(name).rstrip().splitlines()[-1]
            self.assertIn("**Next:**", last, f"{name}: the output does not end with a Next line")
            self.assertRegex(last, r"\((decide-[a-z]+)\)", f"{name}: the Next line names no skill")
            self.assertIn(
                "**Ending.** End the reply with one line starting **Next:**, giving the words the user can type to take the next step, with the skill in brackets.",
                body(name),
                name,
            )

    def test_dates_and_other_people_stay_the_users(self):
        for name in NAMES:
            text = body(name)
            for sentence in (
                "do not add a year, a weekday or a calendar date they did not give",
                "How another person will act (an employer, a landlord, a seller, a partner) is never a fact",
            ):
                self.assertIn(sentence, text, f"{name}: missing {sentence!r}")

    def test_each_skill_keeps_its_own_load_bearing_rule(self):
        for name, sentences in {
            "decide-compare": [
                "A fact a criterion needs and the user did not give is `[?]` in the table, never a likely value.",
                "Do not add anything about an option the user did not say",
                "**Dealbreakers apart from weights.**",
                "these weights are yours to change; tell me any new weight and I will rescore",
                "its source: `you said` (with the fact) or `guess`",
                "A cell whose fact is `[?]` gets a neutral 3 marked `[?]`",
                "Check every product and sum before you write it.",
                "Find the single change that reverses the top two",
                "**What would flip it**",
                "*rescore this* (decide-review)",
            ],
            "decide-frame": [
                "If not, write `[not set]` and ask by when they have to answer",
                "Never assume a date.",
                "then *wait* (ask for more time, defer) and *do nothing* when honest",
                "each marked `(suggestion)`",
                "each with the cheapest way to find it out",
                "**Does it need a matrix?**",
                "*compare A and B* with the facts (decide-compare)",
            ],
            "decide-gonogo": [
                "no market price, resale value, depreciation, insurance, running cost, interest rate, salary range, \"prices will drop\", \"most people regret it\"",
                "**Can it be undone, and at what cost?**",
                "**The cheapest test first.**",
                "**Yes if, no if.**",
                "the smallest safe step is to talk to the prescriber (or a pharmacist) before changing anything",
                "`gain` · `lose` · `reversible?` · `cost of waiting` · `cheapest test` · `yes if` · `no if` · `first step`",
                "*rescore this* (decide-review)",
            ],
            "decide-premortem": [
                "**Do not re-argue the decision.**",
                "A cause that rests on something the user did not say is marked `assumption`",
                "A cause that fits any plan of this kind and uses none of the user's facts does not go in.",
                "**Nothing invented about the place, the company, the course or the people.**",
                "**One kill criterion**",
                "It must be something the user can check, not a feeling.",
                "*rescore this* (decide-review)",
            ],
            "decide-review": [
                "do not re-judge cells the new information does not touch, and do not change a weight the user did not ask to change",
                "**What moved**: a table `item` · `was` · `now` · `why`",
                "if it was `[you fill this]`, it stays `[you fill this]`",
                "**Separate the decision from the outcome.**",
                "Mark each later fact `not knowable then`.",
                "Never say \"you should have known\" about something that was not knowable.",
                "**Do not call the decision wrong because the outcome was bad**",
                "**One thing to keep and one to change next time**",
                "*help me think this through* (decide-frame)",
            ],
        }.items():
            for s in sentences:
                self.assertIn(s, body(name), f"{name}: missing {s!r}")

    def test_no_skill_scrapes_or_needs_a_tool(self):
        for f in SKILLS:
            text = f.read_text(encoding="utf-8").lower()
            for word in ("scrape", "selenium", "playwright", "mcp__", "allowed-tools"):
                self.assertNotIn(word, text, f"{f}: {word!r}")

    def test_every_skill_is_present(self):
        self.assertEqual(sorted(p.parent.name for p in SKILLS), sorted(NAMES))


if __name__ == "__main__":
    unittest.main()
