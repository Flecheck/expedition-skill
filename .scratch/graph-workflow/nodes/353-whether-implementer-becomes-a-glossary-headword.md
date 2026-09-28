# Whether `implementer` becomes a glossary headword or leaves the shipped files

Type: grilling
Status: claimed
Blocked by: 56

## Question

`implementer` has no headword in `.claude/skills/expedition/glossary.md`. It is used in the glossary's own Checker entry ("the implementer never does") and in `.claude/skills/expedition-checker/SKILL.md` (five places, e.g. "the part of the work the implementer may edit"). The implementation contract names the same party "the worker holding the code". Node 56's completeness paragraph now makes a term used with no entry a defect. Should the glossary gain `implementer` as a headword, with an `_Avoid_` line if needed, or should every use become "the worker holding the code" (or "the worker") so the word leaves the shipped files? Also: are the flag markers `ASSUMPTION` and `CONDITION-WRONG` terms the glossary owes entries for?

*Reported by [node 56](56-ship-the-glossary-into-the-skill-set.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Interview

#### Questions 1 and 2, relayed 2026-09-27

*Pasted as the worker handed it back.*

```
NODE:          Whether `implementer` becomes a glossary headword or leaves the shipped files (353)
ABOUT:         Node 56 made the glossary say that any term the skill files use needs an entry, and that a term used without one is a defect. `implementer` is used but has no entry, and the flag markers may be in the same position. This node decides whether to add entries or reword the files.
SO FAR:        I read the node, map.md, the glossary/naming lines of decisions.md, node 56's `implementer` annotation and handover, and node 305's answer, then searched `.claude/`.
               - `implementer` appears 9 times in shipped files, not the 6 the node states: once in the glossary's Checker entry ("the implementer never does"), 7 times in `.claude/skills/expedition-checker/SKILL.md` (lines 79, 88, 208, 209, 210, 215, 250), and once in the manager contract `.claude/skills/expedition/SKILL.md:830` ("What does an implementer do with a finding it believes is false?"). The node misses the last one.
               - The node says the implementation contract calls this party "the worker holding the code". That is stale: the phrase no longer appears anywhere under `.claude/skills`. The implementation contract calls its reader "you", and the glossary's party is **Worker**.
               - Precedent: node 305 had the same question about "standing over sources" (glossary term, or plain words everywhere?). The human chose plain words everywhere, with nothing added to the glossary.
               - Markers: `ASSUMPTION`, `CONDITION-WRONG` and `DELEGATED` are defined once in `.claude/skills/expedition/graph-conventions.md` `### ## Flags` ("There are three markers: ..."). Each worker contract defines the ones it uses under "Two markers are yours: ...". The glossary already writes `CONDITION-WRONG` inside its Acceptance condition entry. None of the three is a headword, and neither are the checker's `PASS`/`FAIL` outcomes or the handover field names. The glossary's completeness paragraph covers "a term those files use in this vocabulary". That wording leaves open whether format tokens count.
               - The two questions below are independent of each other.

Q1. `implementer`: headword or rename
ASK:           Should `implementer` get a glossary headword, or should all 9 uses be reworded so the word leaves the shipped files?
RECOMMENDED:   Reword all 9, with no headword. The plain replacement is "the worker", which the glossary already defines. For example: "sends it to the worker", "the part of the work the worker may edit", "the worker never does" (Checker entry), and "What does a worker do with a finding it believes is false?" (manager contract). A checker only ever deals with one worker, the implementation node's, so "the worker" is unambiguous there. Where a sentence needs it, "the implementation worker" also uses only defined words. Reasons: it follows node 305's plain-words ruling; a headword costs every reader of the glossary on every read, while a rename is a one-off edit in two files you asked to have compacted; and `implementer` names no party that Worker doesn't already name. This becomes one implementation node against the checker contract, the glossary's Checker entry and one line of the manager contract.
ALTERNATIVES:  - Add an `Implementer` headword with an `_Avoid_` line. This keeps the wording but adds a synonym for Worker, which the glossary's `_Avoid_` lines normally refuse.
               - Add the headword and also put `implementer` on Worker's `_Avoid_` line. This contradicts itself.
               - Reword to "the worker holding the code". That phrase is gone from the tree, and it is longer.

---

Q2. Flag markers: entries or not
ASK:           Does the glossary owe entries for the flag markers `ASSUMPTION`, `CONDITION-WRONG` (and by the same reasoning `DELEGATED`), or are they format tokens outside its vocabulary?
RECOMMENDED:   No entries, and no change to the glossary text. They are literal tokens with a set shape, defined in full where that shape is defined (`graph-conventions.md` `## Flags`, and each contract's "markers are yours" line). That is the same treatment `PASS`/`FAIL` and the handover field names already get without anyone calling it a defect. The Flag entry already defines the concept the markers classify. This node's answer records the ruling that the completeness paragraph's "this vocabulary" covers terms, not backticked format tokens. Recording it there rather than adding a sentence to the glossary keeps the glossary from growing.
ALTERNATIVES:  - Add one sentence to the Flag entry naming the three markers and pointing to graph-conventions.md. This costs about two lines per glossary read and removes the ambiguity from the glossary itself.
               - Give each of the three markers its own headword. That is three entries for words already defined in full, twice over.
               - Add a clause to the completeness paragraph saying that format tokens (markers, outcomes, field names) are out of scope. This settles the question for every token, not just these, at the cost of one line.
```

#### The human's answer to questions 1 and 2, 2026-09-28

The human, `verbatim`: *"ok"*. It takes the worker's recommendation on both: Q1 "Reword all 9, with no headword."; Q2 "No entries, and no change to the glossary text."
