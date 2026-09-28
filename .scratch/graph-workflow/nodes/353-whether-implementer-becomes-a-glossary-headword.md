# Whether `implementer` becomes a glossary headword or leaves the shipped files

Type: grilling
Status: resolved
Blocked by: 56

## Answer

`implementer` leaves the shipped files, reworded to "the worker" at 9 sites; flag markers are format tokens the glossary's completeness rule does not cover, so they get no entries.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The node it surfaced is [node 357](357-reword-implementer-to-the-worker-in-the-shipped-files.md). Flag 353.1 settles at the node closing report.

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

## Handover, attempt 1

*Pasted as the worker handed it back.*

````
HANDOVER:      Whether `implementer` becomes a glossary headword or leaves the shipped files

ANSWER:        The word `implementer` leaves the shipped files, and the glossary gains no headword for it. Its 9 uses are reworded to "the worker" or "a worker". Where a sentence needs to say which worker, they become "the implementation worker", which uses only words the glossary already defines. The 9 uses are: the glossary's Checker entry (line 134), the checker contract `.claude/skills/expedition-checker/SKILL.md` (lines 79, 88, 208, 209, 210, 215, 250), and the manager contract `.claude/skills/expedition/SKILL.md` (line 830). The node's question counted 6 and missed the manager contract. `implementer` names no party that **Worker** does not already name. A headword costs every reader of the glossary on every read, while a rename is a one-off edit. This follows node 305's ruling that a name the glossary lacks is said in plain words rather than added. The question's alternative, "the worker holding the code", is set aside: the phrase no longer appears anywhere under `.claude/skills`.

               The flag markers `ASSUMPTION`, `CONDITION-WRONG` and `DELEGATED` get no glossary entries, and the glossary's text is not changed for them. They are backticked format tokens with a fixed shape. Each is defined in full where its shape is defined: `.claude/skills/expedition/graph-conventions.md`'s `## Flags` section, and each worker contract's "markers are yours" line. That is how `PASS`/`FAIL` and the handover field names are already treated. The glossary's completeness paragraph covers "a term those files use in this vocabulary", and this node reads that as covering terms and not format tokens (markers, outcomes, handover field names). A future marker, such as `FRICTION` or `LICENCE`, likewise owes no glossary entry.

               The human's answer, verbatim: *"ok"*, a bare assent that settles both recommendations of the one payload (Q1 rename to "the worker" with no headword; Q2 no entries for the markers and no glossary change).

INDEX LINE:    `implementer` leaves the shipped files, reworded to "the worker" at 9 sites; flag markers are format tokens the glossary's completeness rule does not cover, so they get no entries.

FLAGS:         ASSUMPTION: The acceptance condition I wrote for the rename node does not require the checker contract's `## Words used exactly` to gain a `worker` entry. That contract already uses "worker" undefined, in its own `manager` definition, and the glossary defines it. Adding an entry would lengthen a contract the human asked to have compacted, for no gain in meaning. The condition's scope comes from a grep over the working tree that excludes `.scratch/` and `.git`. So record-side uses of "implementer", such as in `map.md`, `map-implementation-rules.md`, node titles and conditions, are deliberately left alone as record text.
               Index: The `implementer` rename condition adds no `worker` entry to the checker contract's word list and leaves record-side uses of the word alone.

NEW NODES:     - Name: Reword `implementer` to "the worker" in the shipped files
                 Kind: implementation
                 Question: Carry node 353's answer into the shipped files: the 9 uses of `implementer` become "the worker"/"a worker" (or "the implementation worker" where a sentence needs it), with no glossary headword.
                 Blockers: none
                 Acceptance condition:
                 Done when all of the following hold.
                 1. Running `grep -rn -i "implementer" --exclude-dir=.scratch --exclude-dir=.git .` from the repository root returns nothing. Run over the working tree when this condition was written, it returned exactly these 9 lines, which are the whole scope of the work:
                      `.claude/skills/expedition/glossary.md:134` — "The manager starts it, and the implementer never does, because whoever spawns it"
                      `.claude/skills/expedition/SKILL.md:830` — "3. What does an implementer do with a finding it believes is false? It has no route except fixing it."
                      `.claude/skills/expedition-checker/SKILL.md:79` — "5. Your outcome goes to the manager, which sends it to the implementer."
                      `.claude/skills/expedition-checker/SKILL.md:88` — "The implementer works from the same file, so the two of you"
                      `.claude/skills/expedition-checker/SKILL.md:208` — "over the part of the work the implementer may edit."
                      `.claude/skills/expedition-checker/SKILL.md:209` — "command whose hits are mostly text the implementer may not touch"
                      `.claude/skills/expedition-checker/SKILL.md:210` — "command to text the implementer may edit is part of supplying one."
                      `.claude/skills/expedition-checker/SKILL.md:215` — "The extent lets the implementer repair every instance"
                      `.claude/skills/expedition-checker/SKILL.md:250` — "A `FAIL` sends the work back to an implementer who met the scope as written"
                    An instance the grep reaches outside this list is reported and not edited.
                 2. At each of the 9 sites, the party is now named "the worker" or "a worker", with the article adjusted to the sentence. "The implementation worker" is allowed instead where the sentence would otherwise not say which worker. No other word or coined phrase names this party at these sites.
                 3. Apart from the rename and the article changes it forces, the sentences at these sites say what they said before. No rule is added, removed or narrowed, and lines are re-wrapped only as far as the rename requires.
                 4. `.claude/skills/expedition/glossary.md` gains no headword and no `_Avoid_` line, and its entry and `_Avoid_` counts are unchanged by this work.
                 5. No file other than `.claude/skills/expedition/glossary.md`, `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition-checker/SKILL.md` is changed, and nothing under `.scratch/` is changed.
                 6. The working tree meets the bar.

INVALIDATIONS: - Node 56 (resolved): the open question in its `## Annotation` on `implementer` is now answered: the word leaves the shipped files. Its ASSUMPTION 56.4 listed the markers as possible gaps. This answer narrows how its completeness paragraph is read, not the text itself: backticked format tokens (flag markers, checker outcomes, handover field names) are outside "this vocabulary" and are not defects for lacking an entry.
               - Node 29 (resolved), which designed the completeness rule: narrowed the same way. The rule reaches terms, not format tokens.
               - Node 305 (resolved): extended. Its plain-words ruling is applied to a word that is already in use (`implementer`), not only to names coined in a single file.

CONDITIONS:    Searched the open nodes' `## Acceptance condition` and `## Question` sections (65 open or claimed nodes, claimed or not) for: `implementer`, "holding the code", `CONDITION-WRONG`, the markers, "glossary.md", `expedition-checker/SKILL.md`, "Checker entry", `SKILL.md:830`, "finding it believes is false", "the implementer may edit". I read only the matches.
               - Node 41 (open, implementation): the question changes, but no clause does. The manager's 2026-09-27 note, relaying node 56's worker, says the `FRICTION` entry its worker owes "now goes in `.claude/skills/expedition/glossary.md`". Under this answer, `FRICTION` is a flag marker and owes no glossary entry. So that obligation, and the manager's filing note that `UPSTREAM` belongs in the glossary as its refused alternative, no longer hold. The marker is defined where its shape is defined, which clauses 1 and 7 already require. Its condition does not mention the glossary, so no replacement clause is needed. Clause 8 ("the checker contract is not changed by this work") limits that node's own work and does not conflict with the new rename node, which changes that file.
               - Node 170 (open, implementation, no condition yet): the question is partly answered. Whichever repair the human picks for a licence, a new marker such as `LICENCE` owes no glossary entry. Whoever writes its condition must not demand one.
               - Node 34 (open, grilling): a term is renamed in its title, "What an implementer does with a checker finding it believes is false". Its body already says "implementation worker". The shipped line it concerns (`.claude/skills/expedition/SKILL.md:830`) will read "a worker" or "the implementation worker" once the rename node lands. The title is record text and stays as it is under never-delete.
               - Nodes 32, 149, 152, 214 use "implementer" in their record-side prose or conditions, but none of them names a shipped site of the word. No change.
               - No open implementation node's condition covers the same file and the same concern as the rename, so it is minted rather than joined.

MISSING FROM MAP: none

RETROSPECTIVE:
1. What I had to hunt for: the actual list of sites (the node said 6; there are 9, including one in the manager contract), whether "the worker holding the code" still exists (it does not), and where the markers are defined (`graph-conventions.md` `## Flags`). Node 305's precedent turned up only through the decisions.md grep.
2. What arrived that this node did not need: most of map.md (worktree, landing, and termination notes); nothing in the spawn itself.
3. What would have made this easier: the node file giving a grep command rather than a hand count, and linking node 305 as the precedent for "plain words or glossary". The manager's note about compaction was useful and belongs in the spawn as it was.
4. What was stale, wrong or contradictory: the node's count ("five places" in the checker contract; it is seven) and its omission of `.claude/skills/expedition/SKILL.md:830`. The node says the implementation contract names the party "the worker holding the code"; that phrase is gone. Node 41's manager note (relaying node 56's worker), which assumes `FRICTION` owes a glossary entry, is now contradicted by this answer.
````

## Flags

`353.1` `ASSUMPTION` **· settled** — The acceptance condition I wrote for the rename node does not require the checker contract's `## Words used exactly` to gain a `worker` entry, and record-side uses of the word are left alone. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-09-28:* flag 353.1 settles at the node closing report that closes this node.
