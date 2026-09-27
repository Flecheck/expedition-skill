# A shipped file points at a sibling shipped file rather than restating it, and nothing says so

Type: grilling
Status: claimed

Blocked by: none

## Question

*Minted by the manager under this effort's rule that a retrospective item naming the record is disposed of in the
report that closes its node. The question is the manager's; the finding and its ground are [node
166](166-ship-an-expedition-stop-skill.md)'s worker's.*

**The human corrected the same thing twice by hand, on one node, and no rule in this effort states it.**

At node 166's second gate they pointed at a paragraph of the new `expedition-stop` skill and said, `verbatim`:

> I think it is duplicated from the normal way the manager works, maybe try to refer to the normal way of proceding
> in the skill as to not duplicate the instructions

The worker then applied the same ground a second time, at a passage the human had not pointed at, and **declined to
apply it a third time** where a contract rule was restated in order to be overridden — all on its own judgement,
recorded as flag `166.5`.

**Node 166's worker's own statement of the gap**, `verbatim`:

> the human's correction is a rule about how a skill refers to a sibling skill, and nothing in this effort's record
> states it. The four standing rules for writing cover compression, citation and navigability;
> `/writing-for-agents` states single-source-of-truth for a document against itself. Neither says *a shipped file
> points at a sibling shipped file's heading rather than restating its content* — which is exactly what the human
> asked for twice now, first as a gate correction and now as a general instinct I was told to apply at my own
> judgement. It would be worth a standing rule, because the next shipped file will face the same choice with nobody
> to correct it.

**What is actually unsettled, and it is more than whether to write the rule down.**

- **Where the boundary sits.** The worker found one case where the ground does *not* apply: a passage that restates
  a contract rule **in order to suspend it**, which is unreadable without the rule being named. Any rule written
  here has to carry that exception or it will be applied wrongly.
- **What a pointer may name.** The worker pointed at **headings** of the manager's own contract rather than at a
  path, on the ground that its reader already holds that contract — and the checker accepted that as satisfying the
  effort's ground rule 2, which requires each shipped contract to stand alone rather than depend on a skill being
  invocable. Whether a heading citation is always safe, and what happens when the pointed-at heading is renamed, is
  not settled: node 166's file now depends on four headings' wording in a file four other open nodes edit.
- **Whether it binds this effort only, or ships.** Under the map's rule a standing rule binds this effort once
  written in the map, and reaches a shipped file only where the human says so. This one is *about* the shipped
  files, which makes the distinction load-bearing rather than formal.

## The manager's note at filing

*Not a change to anything above.*

**The manager has not written the rule and is not proposing wording.** It records only what it holds: it carried the
human's ground into the correction-round spawn as *"the same instinct may apply elsewhere in the file … but that is
your judgement and a flag if you take it"*, which is what produced flag `166.5` — so the one piece of evidence about
where the boundary sits exists because the manager declined to draw it.

**Two shipped files already point at each other today**, and neither does it under a rule: `expedition-stop`'s four
citations of the manager's contract, landed at `f22dd5c`, and the worker contracts' existing instruction to read
`graph-conventions.md`. Whatever is decided here reaches both.

## Interview

#### Questions 1 to 3, relayed 2026-09-27

*Pasted as the worker handed it back.*

```
NODE:          A shipped file points at a sibling shipped file rather than restating it, and nothing says so (253)
ABOUT:         This node decides whether "point at the other file's heading, don't repeat what it says" becomes a written rule, where the rule stops, and whom it binds. It comes up now because you gave token use priority and asked for the skills to be compacted, and this rule is what makes files shorter without losing anything.
SO FAR:        I read the node, map.md, the decisions.md lines on the topic, nodes 50, 312 and 166 (flag 166.5), flag 289.4, the five writing rules in map-implementation-rules.md, and the shipped tree as it stands on master.
               - What the rule is about. At node 166's gate you told its worker to point at the manager's normal procedure rather than repeat it. The worker then did the same once more on its own judgement. It declined a third time, at a sentence that repeats the manager's top-up rule in order to switch it off, because that sentence cannot be read without the rule it switches off. No written rule covers this. Writing rule 2 is about record items citing nodes, and rule 4 is about citing by heading rather than by line number.
               - What already happens, with no rule behind it. Pointing happens only between files the manager reads. Node 312 split the rules shared by expedition/SKILL.md and graph-conventions.md into one file each, with one-line pointers to headings, and you approved it. expedition-stop, expedition-standing-yes and expedition-cleanup point at headings of the manager's contract or of graph-conventions.md.
               - Worker contracts point at nothing. They repeat shared blocks on purpose: at node 50 you said "keep them duplicated", on the ground that each worker reads only one contract, so the repeated text never costs any single reader anything. So a pointer only saves tokens when the reader already reads the file it points at, which lines up with ground rule 2 (each worker contract stands alone). I do not propose reopening node 50. Removing repeats across the worker contracts would make no worker's read shorter.
               - The node file is out of date on one point. It says the worker contracts "instruct to read graph-conventions.md". None does today (grep: 0 hits in all six worker contracts).
               - Renamed headings. Pass 289 guarded against them only as its own worker's assumption (flag 289.4): a heading whose exact text appears in another shipped file or in the live map files keeps that text. Node 313's script checks this, but only for the rewrite nodes. Nothing standing covers it. Node 29 part 3 ("ok for 29") already refused new mechanical checks.

Q1. What the rule says, and where it stops
ASK:           Should the rule be: a shipped file points at a heading of another shipped file wherever its reader already reads that file, and restates otherwise, with the exception for a passage that switches a rule off for its own case?
RECOMMENDED:   Yes, in this wording: "Where a shipped file's reader is already told to read another shipped file, point at that file's heading instead of restating what it holds. A worker contract restates what it needs, because its reader reads no other shipped file. A passage that changes a rule for its own case names the rule by heading and states the change in its own words." This matches all three cases on record: node 312's split, expedition-stop's pointers, and node 50's duplication. It also covers the case the 166 worker declined, since expedition-stop can now say "the top-up rule under <heading> does not apply; leave the counts below" and no longer repeats the rule.
ALTERNATIVES:  - Point everywhere, worker contracts included. This reopens node 50, conflicts with ground rule 2, and saves no reader any tokens.
               - Write no rule and leave it to each worker's judgement plus correction at the gate. Nothing stops the next file from repeating content.
               - Point only by path, never by heading. The reader then opens a whole file for one rule.

---

Q2. Whom it binds
ASK:           Should the rule bind this effort only, as a sixth writing rule in map-implementation-rules.md, rather than being written into a shipped file?
RECOMMENDED:   This effort only. The rule governs how the workflow's own files are written, and on any other effort those files are never edited, so a shipped copy would never be used there. The writing rules file is read by exactly the implementers and checkers who edit shipped files. It sits beside rule 4 (cite by heading), which it builds on.
ALTERNATIVES:  - Ship it in the manager contract, so any effort that edits the skills gets it. That is extra prose in every manager's read for a case only this effort has.
               - Put it in map.md's standing preferences. Every worker would read it, but only implementers act on it.

---

Q3. When a heading that another file points at is renamed
ASK:           Should the rule also say that a heading another shipped file points at may be renamed only in the same change that updates every citation of it, found by searching the shipped files for the heading's exact text?
RECOMMENDED:   Yes, as one more sentence of the same rule. It turns pass 289's assumption into a standing rule at the cost of one sentence. It adds no mechanical check, so it stays within node 29 part 3. It also protects expedition-stop, whose four heading citations point into a file other open nodes edit.
ALTERNATIVES:  - Freeze cited headings, so they are never renamed. This blocks legitimate rewrites.
               - Add a mechanical check. You refused that at node 29 part 3.
               - Say nothing, leave broken pointers for the checker to catch, and accept that a rename passes silently.
```

*The manager's note, 2026-09-27:* Q2 recommends a sixth writing rule in `map-implementation-rules.md`. [Node 349](349-whether-the-five-standing-rules-for-writing-reach-other-workers.md)'s question, which is in front of the human first, is whether the five writing rules move from that file to `map.md`. Its answer may change where Q2's rule would go.
