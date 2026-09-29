# Check that a node's condition is still current before claiming it

Type: grilling
Status: claimed
Blocked by: none

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
