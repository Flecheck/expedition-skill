# Whether the five standing rules for writing reach a worker that is not an implementation worker

Type: grilling
Status: claimed
Blocked by: 348

## Question

This effort's five standing rules for writing are held against every prose deliverable. They sit in `map-implementation-rules.md`, which only an implementation worker and a checker read. Grilling, research, prototype and precondition workers also write prose that the manager pastes onto the graph unaltered. Must those rules reach those workers, and if so, by moving them into `map.md`, by a pointer in those contracts, or by some other route?

*Reported by [node 168](168-where-a-non-implementation-worker-gets-the-ground-rules.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Interview

#### Question 1, relayed 2026-09-27

*Pasted as the worker handed it back.*

```
NODE:          349, Whether the five standing rules for writing reach a worker that is not an implementation worker
ABOUT:         This effort has five standing rules for writing: compress the explanation of why but never the shapes; state an item's current form and cite the nodes behind it; make a long answer navigable by heading; cite by heading or quoted phrase, never by line number; write plain English. `map.md` says they are "held against every prose deliverable", but they sit only in `map-implementation-rules.md`, which only an implementation worker and a checker read. This node decides whether grilling, research, prototype and precondition workers must have them, and by what route. It comes up now because node 348 landed today and put the ground rules back in `map.md` for the same reason, and left these five rules behind.
SO FAR:        I read the following: the grilling contract, `map.md`, `map-implementation-rules.md`, the `decisions.md` lines about the ground rules and the rules file, node 168's interview and handover, node 190's condition, and the checker-spawn section of the manager contract and the checker contract.
               What the files say today:
               - `map.md` ends its `## Notes` with a one-line pointer: the five rules "are in map-implementation-rules.md, held against every prose deliverable".
               - The four non-implementation contracts list only the node file, `map.md` and `decisions.md` as reading. They also say "you never go looking for a standard you are judged against". So a grilling or research worker sees the pointer but may not follow it. The claim that the rules cover every prose deliverable is therefore not true for those four workers.
               - Those workers do write prose that the rules are aimed at. The manager pastes a grilling worker's ANSWER onto the node unaltered, and rules 2 to 4 are about that kind of record text. The human reads the question payloads directly, and rule 5 (plain English) is about exactly that.
               - The checker gets its standards by reading `map-implementation-rules.md` itself. The ground rules are the exception: the manager copies "the block of ground rules" into every checker spawn as text (manager contract, node 42).
               - No shipped file mentions the five rules. They belong to this effort alone, so any answer here changes only this effort's map, unless you say otherwise.
               - The block is 1,412 bytes. `map.md` is 22,838 bytes.
               - Node 190 (open) is NOT independent of this node, which is different from what the manager believed. Two of its clauses assume the five rules stay in the rules file. Clause 4 says: "No numbered rule in the file's block of five standing rules for writing is reworded". Node 348's amendment to clause 1 says: "five standing rules for writing, stated as held in this file". If the block moves, both clauses must be rewritten, and node 190 should not be claimed until this node has resolved.
               Settled on my own authority: I treat "reach" as meaning the worker has the rules in a file its contract tells it to read. Whether anyone checks a grilling worker's prose against them is a separate matter, because no checker looks at non-implementation work.
ASK:           Must the five standing rules for writing reach the grilling, research, prototype and precondition workers, and if so, by which route?
RECOMMENDED:   Yes. Move the five rules verbatim from `map-implementation-rules.md` into `map.md`'s `## Notes`, as a second numbered list inside the "Ground rules for this effort" block. The rules file then says that `map.md` holds them, in the same way it already does for the ground rules. This rests on four points:
               (a) It is the same reasoning you accepted at node 168: a block that binds every worker belongs in the one map file every worker reads.
               (b) Putting the rules inside the ground-rules block means the checker keeps receiving them with no change to any shipped file. The manager already copies that block into every checker spawn as text, and the rules file already says the five rules pass node 42's test for what may be copied there. If they sat in `map.md` as a separate block, the checker would lose them, because it does not read `map.md`.
               (c) Keeping the ground rules as "rules of scope" and these as "rules of writing" does little work. Ground rule 5 (`/writing-for-agents`) is itself a rule of writing.
               (d) The cost is 1.4 KB more in `map.md` for every worker, and the rules file shrinks by the same amount.
               I would file this as one implementation node for the move, plus replacement text for node 190's clauses 1 and 4.
ALTERNATIVES:  - Move the rules to `map.md` as their own block, separate from the ground rules. The checker then loses them unless the manager contract (a shipped file) copies a second block, or the rules file keeps a duplicate that can drift.
               - Keep them in the rules file and add that file to the four contracts' reading lists. You rejected this for the ground rules at node 168: those workers would read the bar commands, the worktree route and the review route, which they never use.
               - Keep a copy in both files. That makes two places to supersede and lets them drift apart.
               - Have the manager copy them into every worker's spawn. This changes every spawn and breaks the rule that a spawn points rather than summarises.
               - Say they bind implementation work only, and narrow `map.md`'s "every prose deliverable" to match. This is the cheapest option, but it leaves the answers pasted onto nodes and the payloads you read outside rules that were written for them.
```

#### The human's answer to question 1, 2026-09-27

The human, `verbatim`: *"ok"*. It takes the worker's recommendation: "Yes. Move the five rules verbatim from `map-implementation-rules.md` into `map.md`'s `## Notes`, as a second numbered list inside the "Ground rules for this effort" block. The rules file then says that `map.md` holds them, in the same way it already does for the ground rules."
