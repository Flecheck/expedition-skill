# Check that a node's condition is still current before claiming it

Type: grilling
Status: resolved
Blocked by: none

## Answer

Before claiming an implementation node, the manager reads the node's annotations and notes and searches the tree for each passage its condition quotes, then amends or asks before claiming. Ships in SKILL.md.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The human took all three recommendations. The node it surfaced is [node 373](373-ship-the-check-before-a-claim.md). Flags 365.1, 365.2, 365.3 settle at the node closing report.

## Question

Four implementation nodes claimed on 2026-09-27 and 2026-09-28 (226, 236, 186, 234) stopped on a raise because their acceptance condition quoted text that later landed work had already removed or moved; node 186 already carried two annotations saying so. The frontier lists a node as startable from its status and blockers alone. What does a check before a claim cover (the node's annotations, whether each passage its condition quotes still exists, whether a later node changed the route it assumes), who runs it, and does it ship in the manager's skill or stay in this effort's map?

*Filed by the manager from its own retrospective, 2026-09-28. The human's words on it, `verbatim`: "1 ok, we might want to change the skill".*

## Interview

#### Questions 1 to 3, relayed 2026-09-29

*Pasted as the worker handed it back.*

```
NODE:          Check that a node's condition is still current before claiming it (365)
ABOUT:         This node decides what the manager checks on an implementation node before claiming it, so that a claim stops failing on a condition that later work has already made wrong. It is being decided now because four claims in two days (226, 236, 186, 234) each ended in a raise and a round trip to you for this reason.
SO FAR:        I read the node, map.md, decisions.md, the four nodes' raises, the claim rules in `expedition/SKILL.md` and `graph-conventions.md`, and node 366's first payload.
               - What went wrong in each of the four:
                 - 236: the phrase its condition quoted had already been removed and banked by node 268.
                 - 234: the "two sentences" its condition quoted had been banked by node 229, 14 minutes before node 234 was minted.
                 - 186: it already carried two annotations saying its condition was broken. The manager claimed it without reading them. The manager's own note on the node says so.
                 - 226: an annotation and a 2026-09-25 manager note were already on the node. Its clause was also false about the tree in a way no quote check would catch: it said "exactly one file names the path", and about 33 files did.
               - Result: reading the node's annotations and notes, plus one search per quoted passage, would have caught all four before the claim.
               - The problem is not rare. Node 366's worker found six more unclaimed implementation nodes whose conditions quote text that has moved: 80, 88, 149, 219, 220 and 284.
               - What the shipped files already say:
                 - `SKILL.md` already has a claim-time duty of the same shape: "Re-derive an enumerated scope before the node is claimed."
                 - It already lets the manager amend an unclaimed node's condition without asking you, where every word of the replacement is already fixed.
                 - The implementation contract already makes a worker raise a condition "already known to be false". That rule is the backstop that fired four times.
                 - Nothing tells anyone to check a condition's quoted text or annotations before the claim. The frontier script reads only the header fields.
               - Settled on my own authority:
                 - Where the check finds something, the manager uses the amendment rules that already exist, or puts the node to you and does not claim it. No new route.
                 - The check is not recorded on the node when it finds nothing. An amendment it causes is recorded anyway, under the existing rules.
                 - The check covers implementation nodes only, because only those carry a condition.

Q1. What the check covers
ASK:           Does the check before a claim cover the node's annotations and notes, plus a search for each passage its condition quotes or names by heading, and nothing more?
RECOMMENDED:   Yes, those two. Together they would have caught all four stopped claims, and each is cheap: one read of the node file you already open, and one search per quote. A check of "whether a later node changed the route the condition assumes" has no fixed extent. Doing it means judging every decision made since the node was filed. That is the worker's reading of the tree, and the existing raise already backs it up.
ALTERNATIVES:  - Also check for route changes, by reading the decisions.md lines added since the node was filed. It would catch more, but it is open-ended and is roughly a worker's job done twice.
               - Annotations only. This catches 186 and 226, and misses 236 and 234.
               - Also check grilling and research nodes' questions. Those carry no condition, and their worker reads the tree anyway.

---

Q2. Who runs it
ASK:           Does the manager run the check itself, as part of claiming, rather than leaving it to the worker's first step?
RECOMMENDED:   The manager. Claiming is the manager's act, and the only fix for a stale condition that avoids you is an amendment, which only the manager may make before the claim. Once a worker holds the node, the condition can only be raised to you. That is exactly the round trip the four nodes cost, and each one also used up a spawn and a code slot.
ALTERNATIVES:  - The worker, as its first step. This is today's backstop. It finds the problem, but only after the claim, so every find becomes a raise to you.
               - The frontier script. Pulling quotes out of prose is fuzzy, and it would add machinery to a read-only script that reads only header fields.
               - A separate agent before each claim. It costs a spawn per claim for two searches.

---

Q3. Where the rule lives
ASK:           Does the rule ship in the manager's skill, as about 65 words in `.claude/skills/expedition/SKILL.md` next to the existing "Re-derive an enumerated scope before the node is claimed", rather than stay in this effort's map?
RECOMMENDED:   Ship it, in about these words: "Before you claim an implementation node, read everything written on its file after its condition, meaning annotations, amendments and your own notes. Then search the tree for each passage the condition quotes or names by heading. Where a passage is gone, or an annotation says the condition is wrong, amend the condition under the rules above or put it to the human, and claim the node only once its condition holds." Any effort that lives long enough goes stale this way, not just this one. Your words on the node were "we might want to change the skill". The cost is about 400 bytes on a 50,232-byte file. It sits next to its sibling duty, and it adds no heading and no procedure.
ALTERNATIVES:  - Map-only. It costs nothing in the skill, but the next effort starts without the rule and pays the same four raises.
               - Put it as a step in `graph-conventions.md`'s `### Claim` procedure. That procedure is written for whoever claims, and the amendment rules the check relies on are in `SKILL.md`, so the rule would have to point back there.
               - Ship it and also have the implementation contract say the worker checks first. That adds size and restates a duty the raise already covers.

RETROSPECTIVE (partial; the full one comes with the handover)
1. What I had to hunt for: what actually stopped each of the four nodes. It is in each node's `## Interview` raise, and neither the node nor the spawn says so.
2. What arrived that this node did not need: most of decisions.md (about 29k tokens). Only the lines for nodes 82, 252, 263 and 366, and the claim-related lines, mattered. Most of map.md's `## Notes` also bore on nothing here.
3. What would have made this easier: the node's question naming the heading of each of the four raises.
4. What was stale, wrong or contradictory: nothing found yet. The node's claim that "node 186 already carried two annotations saying so" checks out.
```

#### The human's answer to questions 1 to 3, 2026-09-29

`verbatim`: *"ok"*

The manager had put the questions with the line "Please answer Q1 to Q3. "ok for recommended" takes all three." So the reply takes the worker's `RECOMMENDED` on all three: the check covers the node's annotations and notes plus a search for each passage its condition quotes or names by heading; the manager runs it as part of claiming; the rule ships in `.claude/skills/expedition/SKILL.md`, next to "Re-derive an enumerated scope before the node is claimed".

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      Check that a node's condition is still current before claiming it (365)

ANSWER:        Before the manager claims an implementation node, it checks that the node's acceptance condition is still current. The human took all three recommendations, `verbatim` "ok".
               - What the check covers (Q1). Two things and nothing more. First, everything written on the node file after its condition: annotations, amendments and the manager's own notes. Second, a search of the working tree for each passage the condition quotes or names by heading. Together these would have caught all four claims that stopped on a raise on 2026-09-27 and 2026-09-28. Nodes 186 and 226 already carried annotations or notes saying their conditions were wrong. Nodes 236 and 234 quoted text that nodes 268 and 229 had already removed and banked. The check does not judge whether a later node changed the route a condition assumes, because that has no fixed extent. The worker's reading of the tree, backed by its existing duty to raise a condition already known to be false, covers that case.
               - Who runs it (Q2). The manager, as part of claiming. Only the manager may amend a condition without the human, and only while nobody holds the node. Once a worker holds it, a stale condition can only be raised to the human, which costs a spawn, a code slot and a round trip.
               - What a finding leads to. The manager uses the routes that already exist: it amends the condition under `SKILL.md`'s `### Changing one after it is written`, or it puts the node to the human and does not claim it.
               - Where the rule lives (Q3). It ships in `.claude/skills/expedition/SKILL.md`, as one paragraph of about 65 words placed right after "Re-derive an enumerated scope before the node is claimed", which is its sibling duty at the same moment. It adds no heading and no procedure. Until that node lands, the manager keeps the check as the practice it already follows.

INDEX LINE:    Before claiming an implementation node, the manager reads the node's annotations and notes and searches the tree for each passage its condition quotes, then amends or asks before claiming. Ships in SKILL.md.

FLAGS:
               ASSUMPTION, on the node: Where the check finds a defect, the manager uses the routes that already exist: an amendment under `### Changing one after it is written` where every word of the replacement is already fixed, otherwise a question to the human, with no claim meanwhile. I settled this myself because the shipped amendment rules already cover the case, and a new route would add size the human wants cut.
               Index: A failed claim-time check uses the existing amendment rules or goes to the human; it opens no new route.

               ASSUMPTION, on the node: A check that finds nothing is not recorded on the node. An amendment the check causes is recorded anyway, under the existing five duties that come with every amendment. I settled this myself because recording a clean check would add bookkeeping to every claim and protect nothing.
               Index: A claim-time check that finds nothing leaves no record on the node.

               ASSUMPTION, on the node: The check covers implementation nodes only, because only they carry an acceptance condition. A grilling or research worker reads the tree itself. I settled this myself from the node's own question, which speaks of a node's condition.
               Index: The claim-time check applies only to implementation nodes, the only kind with a condition.

NEW NODES:
               Name: Ship the check before a claim into the manager's contract
               Kind: implementation
               Question: Add to the manager's contract the paragraph that makes the manager check an implementation node's condition is still current before claiming it.
               Blockers: none. Node 368 (claimed) edits other passages of the same file, `## Acceptance conditions` first paragraph and constraint 2. So this is a new node rather than clauses joined to 368, and the two may meet at integration.
               Acceptance condition:
               > 1. `.claude/skills/expedition/SKILL.md`, under `### Changing one after it is written`, gains one new paragraph immediately after the paragraph that begins "Re-derive an enumerated scope before the node is claimed."
               > 2. The new paragraph tells the manager that, before it claims an implementation node, it does two things. First, it reads everything written on the node's file after its acceptance condition, meaning its annotations, its amendments and the manager's own notes. Second, it searches the working tree for each passage the condition quotes or names by heading.
               > 3. The new paragraph says that where a quoted or named passage is gone, or where an annotation or note says the condition is wrong, the manager either amends the condition under the rules of that same section or puts the node to the human, and claims the node only once neither is true.
               > 4. The new paragraph adds no new route for a defective condition. It names no procedure beyond the rules of the section it sits in and the human.
               > 5. The new paragraph is at most 80 words. It is written in plain English, one idea per sentence. It uses no figure of speech and no term that `.claude/skills/expedition/glossary.md` does not define, other than plain words.
               > 6. No heading in any file under `.claude/skills/` is added, removed or renamed. No other paragraph of `SKILL.md` changes, and no other file changes.
               > 7. Scope came from no search: the work adds one paragraph at the one place named.

INVALIDATIONS: none. The answer adds a duty beside node 82's re-derivation duty and changes no resolved node's answer. Node 366's triage (resolved) and node 372's condition clause 3, which reports kept conditions that quote text no longer present, are the whole-backlog counterpart and agree with this answer.

CONDITIONS:    I searched the `## Acceptance condition` and `## Question` sections of every open or claimed node for "before the node is claimed", "Re-derive an enumerated scope", "### Claim", "before you claim", "claim time", "claim-time", "## Acceptance conditions`" and "stale".
               - Node 368 (claimed) matched on the first, third and seventh phrases. Its clauses edit other passages of `SKILL.md` and stay correct; nothing here makes them wrong.
               - Node 372 matched in substance, its clause 3. It is consistent with this answer and needs no change.
               - Node 41 matched "claim time" in a filing note about its own condition's audit, not in its condition or question.
               - The "stale" matches (nodes 211, 220, 78, 13, 80, 284, 367) concern other subjects.
               No replacement clauses. No open node's question changes.

MISSING FROM MAP: none. What stopped each of the four nodes came from their `## Interview` raises, not from the map. That is node-specific, not map material.

RETROSPECTIVE
1. What I had to hunt for: why each of the four claims stopped. It is in each node's `## Interview` raise, and neither my node nor the spawn pointed there. I also had to find where a claim-time duty already lives: `SKILL.md`'s "Re-derive an enumerated scope before the node is claimed", under `### Changing one after it is written`, not under `## Acceptance conditions`' opening or `### Claim`.
2. What arrived that this node did not need: nearly all of decisions.md (about 29k tokens). Only the lines for nodes 82, 252, 263 and the claim-adjacent entries bore on this node. Most of map.md's `## Notes` also bore on nothing here. The manager's note that node 366 overlapped only in noticing stale nodes was accurate and useful.
3. What would have made this easier: the node's question citing the four raises by heading (`#### Raise 1` in each node's `## Interview`). The spawn pointing at the `SKILL.md` paragraph holding the sibling re-derivation duty.
4. What was stale, wrong or contradictory: the resume message speaks of "your Q5 context". This node's payload had only Q1 to Q3. The Q5 was node 366's. Otherwise nothing found stale. The question's claim that node 186 already carried two annotations checks out.
No method skill was invoked, so no part of one was skipped.
`````

## Flags

`365.1` `ASSUMPTION` **· settled** — A failed claim-time check uses the existing amendment rules or goes to the human; it opens no new route. *(The worker's full text is under its handover's `FLAGS`.)*

`365.2` `ASSUMPTION` **· settled** — A claim-time check that finds nothing leaves no record on the node. *(The worker's full text is under its handover's `FLAGS`.)*

`365.3` `ASSUMPTION` **· settled** — The claim-time check applies only to implementation nodes, the only kind with a condition. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-09-29:* flags 365.1, 365.2, 365.3 settle at the node closing report that closes this node.
