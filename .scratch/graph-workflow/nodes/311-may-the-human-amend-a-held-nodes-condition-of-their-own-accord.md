# May the human amend a held node's condition of their own accord?

Type: grilling
Status: resolved
Supersedes: 279

## Question

The manager contract says "The human may also amend a condition of their own accord at any time." `graph-conventions.md` `### Acceptance condition` limits the human, the party and the manager to "a condition on a node nobody holds yet", and says a condition under a live worker reaches the human "by that worker's raise, and by no other route". The same contradiction was already in `graph-conventions.md` at `4068519`, so node 299 did not introduce it. Which holds?

*Reported by [node 297](297-rewrite-the-manager-contract-part-2.md)'s worker. The manager's note: on this effort the human did amend held nodes 296 and 299 of their own accord, recorded on those nodes.*

## Answer

The human may change any acceptance condition at any time, held node or not; only the fact-establishing party and the manager are limited to nodes nobody holds.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The human's `"ok"` is under `## Interview`. The fix is [node 321](321-remove-graph-conventions-limit-on-the-human-amending-a-held-nodes-condition.md).

## Interview

### Attempt 1

**Q1, from the worker**, pasted as it wrote it, 2026-09-25. **Held, not yet put to the human**: it arrived while [node 315](315-the-manager-contract-forbids-rendering-a-reply-while-graph-conventions-permits-a-paraphrase.md)'s question was in front of the human.

```
NODE:          May the human amend a held node's condition of their own accord
ABOUT:         The two shipped files contradict each other on whether you may change the acceptance condition of an implementation node that a worker is already working on. This node settles which file is right, so that an implementation node can then fix the wrong one.
SO FAR:        I read both files as they stand on master, and the record behind them.
                - `expedition/SKILL.md`, `### Changing one after it is written`, says: "The human may also amend a condition of their own accord at any time." Two other passages in the same file take this for granted. One says "Where the human amends a condition while a check is live, tell the checker." The other has the manager raise, itself, a defective condition it finds before the check ("Where you find such a condition before the check, you raise it"), and says "What to do about a claimed node stays yours".
                - `graph-conventions.md`, `### Acceptance condition`, says: "The human changes only a condition on a node nobody holds yet. A condition under a live worker reaches the human by that worker's raise, and by no other route." That sentence is also inconsistent with itself: the worker's raise brings the condition to you, yet the same passage forbids you to change it.
                - Where it came from: both sentences were written by commit `b095bb6` (node 95). Node 95's worker added the unclaimed-only limit on its own authority (flag 95.3), taking it from node 252's answer. What node 252 limited was the new permission it gave to agents: the party that established a fact, and the manager, may amend only a condition on a node nobody holds yet. Its words: "it reaches an unclaimed node only; once a worker holds it, your raise rule governs and nothing changes". It put no limit on you. Node 252's own record cites node 166, where you changed a live node's condition at its gate, as "that route exists and works".
                - What you have actually done: you changed held nodes' conditions three times. At node 166 you did it twice, both times at a gate and in your own words. At nodes 296 and 299 you did it with "ok" to wording the manager proposed while those workers were in correction rounds. So 296 and 299 were at the manager's proposal rather than purely on your own initiative. Each time, the manager passed the new text to the worker and the checker, and the work went on.
                Nothing yet settled on my own authority.
ASK:           When a worker already holds an implementation node, may you change its acceptance condition, whether on your own initiative or when the manager proposes it? That is, does `SKILL.md` hold, with `graph-conventions.md`'s two sentences corrected?
RECOMMENDED:   Yes, `SKILL.md` holds. You may change any condition at any time, whether or not a worker holds the node. The limit to nodes nobody holds applies only to the two agents who may amend without you: the party that established the fact, and the manager. "By no other route" is also wrong, because the manager may raise a held node's condition to you. It rests on five things. `SKILL.md` states this in three places. The limit on you was never decided: it was a worker's assumption that stretched node 252 beyond what it said. You have used this route three times without harm. `graph-conventions.md`'s sentence does not even hold together. And you are the authority the whole amendment scheme falls back on. The fix would be one implementation node on `graph-conventions.md` `### Acceptance condition`. It would say that the party and the manager change only a condition on a node nobody holds yet. It would say that you may change any condition at any time. And it would say that an amended condition on a held node goes to its live worker and to any live checker. `SKILL.md` today names only the checker, though the manager has passed the new text to the worker each time.
ALTERNATIVES:  `graph-conventions.md` holds: you change only conditions on nodes nobody holds, and a held node's condition reaches you only through its own worker's raise. `SKILL.md` drops "of their own accord" and the checker-notice line, and your amendments at nodes 166, 296 and 299 become out of rule after the fact.
                A middle rule: you may change a held node's condition only when answering a raise (the worker's or the manager's), never unprompted. This keeps nodes 296 and 299, but leaves node 166 outside the rule.
```

*The manager: put to the human on 2026-09-25, once node 315's question was answered.*

**A1, the human**, `verbatim`, 2026-09-25: *"ok"*

This takes the option the worker offered as `RECOMMENDED`, in the worker's words: *"Yes, `SKILL.md` holds. You may change any condition at any time, whether or not a worker holds the node. The limit to nodes nobody holds applies only to the two agents who may amend without you: the party that established the fact, and the manager. "By no other route" is also wrong, because the manager may raise a held node's condition to you."* The reply came while the manager's last message ended on this question, with the recommendation restated as *"It recommends yes: the limit to unheld nodes should bind only the two agents who may change a condition without you."* Node 316's question had not yet been put to the human.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted. The worker's session then stopped on a usage limit; the handover had already arrived whole.*

HANDOVER:      May the human amend a held node's condition of their own accord

ANSWER:
**`SKILL.md` holds.** The human may change any acceptance condition at any time, whether or not a worker holds the node, on their own initiative or at the manager's proposal. The human's words, `verbatim`, assenting to the recommendation: *"ok"*.

The limit to "a node nobody holds yet" binds only the two agents who may amend without the human: the party that established a fact which makes a clause wrong, and the manager. It never bound the human. `graph-conventions.md` `### \`## Acceptance condition\`` says "The human changes only a condition on a node nobody holds yet. A condition under a live worker reaches the human by that worker's raise, and by no other route." Both sentences are wrong. The first restricts the human. The second leaves out the manager's own raise of a held node's condition, which `SKILL.md` gives it ("Where you find such a condition before the check, you raise it"; "What to do about a claimed node stays yours").

Where the two sentences came from: commit `b095bb6` (node 95). Node 95's worker added the unclaimed-only boundary on its own authority (flag 95.3), taking it from node 252. Node 252 limited only the new permission it gave to agents ("it reaches an unclaimed node only; once a worker holds it, your raise rule governs and nothing changes"). It put no limit on the human, and its own record cites node 166's live-gate amendment by the human as "that route exists and works". The practice agrees: the human amended held conditions twice at node 166's gates, in their own words, and once more with "ok" to the manager's proposed wording, filed on both 296 and 299. Each time the manager passed the amended text to the worker and to the checker.

When the human amends the condition of a node a worker holds, the amended text goes to that worker and to any live checker, and is then the whole condition. `SKILL.md` today names only the checker.

The fix is [the new implementation node below]. It removes the two sentences from `graph-conventions.md`, which already points at `SKILL.md` for who may change a condition, and makes `SKILL.md`'s notice line name the worker as well as the checker.

INDEX LINE:    The human may change any acceptance condition at any time, held node or not; only the fact-establishing party and the manager are limited to nodes nobody holds.

FLAGS:
ASSUMPTION — Where the fix goes. My recommendation described the fix as one implementation node on `graph-conventions.md` `### \`## Acceptance condition\``, stating there who is limited and that an amended condition goes to the worker and the checker. The human's "ok" settled the substance. Placement I settled myself under node 312's resolved split, which the human approved: rules about who may change a condition live in `SKILL.md`, and `graph-conventions.md` keeps a pointer to them. So the new node removes the two wrong sentences from `graph-conventions.md` rather than restating the rule there. It carries the worker notice into `SKILL.md`, extending the existing sentence "Where the human amends a condition while a check is live, tell the checker." If the human wanted the rule stated in `graph-conventions.md` itself, the node's clauses 1 and 2 move there, and node 312's split is broken for this one rule. No round was run on this: I decided it from node 312's answer and the files on master at `4cc74de`.
Index sentence: The fix for the human's right to amend a held condition removes graph-conventions.md's wrong limit and extends SKILL.md, rather than restating the rule in graph-conventions.md, keeping node 312's one-home split.

NEW NODES:
Name:      Remove graph-conventions.md's limit on the human amending a held node's condition
Kind:      implementation
Question:  Carry node 311's answer into the shipped files: the human may change any acceptance condition at any time, and an amended condition on a held node reaches its worker and any live checker.
Blockers:  none. It edits the same two files as two other nodes, in different sections. Node 318 (open) edits `graph-conventions.md`'s node-file template code block under `## The node file`. Node 319 (claimed) edits `graph-conventions.md` `### Recording the human's words` and `SKILL.md` `### The human's words`. This node touches only `graph-conventions.md` `### \`## Acceptance condition\`` and `SKILL.md` `## The checker`, and reads `SKILL.md` `### Changing one after it is written`.
Acceptance condition:
1. In `.claude/skills/expedition/graph-conventions.md`, under the heading `### \`## Acceptance condition\``, the two sentences "The human changes only a condition on a node nobody holds yet." and "A condition under a live worker reaches the human by that worker's raise, and by no other route." are removed. Nothing is written in their place that says or implies that the human may change only a condition on a node nobody holds yet, or that a held node's condition reaches the human only by its worker's raise. The sentence before them, "`## Acceptance conditions` in `SKILL.md` says who writes it and who may change it after it is written.", stays as it is. `grep -niE "nobody holds|no other route|live worker" .claude/skills/expedition/graph-conventions.md` returns nothing.
2. In `.claude/skills/expedition/SKILL.md`, under the heading `## The checker`, the two sentences "Where the human amends a condition while a check is live, tell the checker. The amended text is then the whole condition." are replaced where they stand. The replacement, addressed to the manager as *you* like the rest of the file, says three things. Where the human amends the condition of a node a worker already holds, you pass the amended text to that worker. Where a check is also live, you pass it to the checker too. The amended text is then the whole condition. The replacement is stated once, and the rule is not restated anywhere else in the file.
3. In `.claude/skills/expedition/SKILL.md`, under `### Changing one after it is written`, the sentences "The amendments in this section, by the party that established a fact and by you, apply only to a node nobody holds yet." and "The human may also amend a condition of their own accord at any time." are unchanged.
4. No other text in either file changes, no heading in either file changes, and no other path changes.

INVALIDATIONS:
Node 95 (resolved, "Carry node 82's widening rule into the two shipped files that state the old one"): its flag 95.3 recorded adding "node 252's unclaimed-only boundary to both files", and in `graph-conventions.md` it applied that boundary to the human as well as to the two agents. This answer contradicts that part of node 95's landed work. The boundary holds for the party that established the fact and for the manager, and not for the human. Node 95's other content stands. Node 252 is not contradicted: its limit was on the agents' permission only. Node 312 is not contradicted: its flag 312.3 left this contradiction to this node on purpose. No open node's acceptance condition quotes either sentence being removed. I searched every node file for "nobody holds yet", "no other route" and "own accord": the only matches are this node and resolved or superseded nodes 95, 250, 297, 299 and 312.

RETROSPECTIVE:
(1) What I had to hunt for. First, where the contradiction came from. I found it with `git log -S"own accord"` and `-S"no other route"`, which both pointed to `b095bb6`. Then node 95's flag 95.3 and node 252's answer gave the reason. I looked first at the 4068519 version the node file names, which only shows the contradiction was older. Second, whether `SKILL.md` gives the manager a route of its own to the human for a held node's condition. It does, at lines 224–225 and 419–420. Nothing in the spawn or the node pointed there, and I found it by grepping `SKILL.md` for "condition". Third, how 296 and 299 were really amended. Their `## Amendment by the human` sections say "approved the manager's proposal", which is not "of their own accord" as the node's manager note says.
(2) What arrived that this node did not need. Almost all of `map.md` (about 48 KB when printed): only the "decision of the human's own may be proposed for change" bullet and node 312's split bore on this node. The `decisions.md` grep for "condition" returned about 25 lines, of which 3 bore on it (252, 95, 82). Searching for "amend" alone would have been enough. Node 109, as the spawn itself said. Its record did not match the spawn's description (see 4). A narrower spawn pointer would have helped: "`decisions.md`: nodes 95, 252, 312".
(3) What would have made it easier. The node file could name `b095bb6`, node 95's flag 95.3 and node 252 as the origin. The spawn could name node 312's split rule, because it decides where the fix goes, and I found it only by chance through the search results. The spawn could also say which open nodes are editing the same files. It came in the mid-task message for 319, but 318 I had to find myself.
(4) Stale, wrong or contradicting. The spawn says "On node 109 the human amended the condition of an open, unheld node at the manager's proposal". Node 109's amendments were written by the workers of nodes 290, 294 and 291 and filed by the manager, under the rule for a party that established a fact. None was the human's. The node file's manager note says the human amended 296 and 299 "of their own accord". Both nodes record it as the human's "ok" to a proposal the manager drafted. `graph-conventions.md`'s own passage contradicts itself: it sends a held condition to the human by raise but forbids the human to change it. Master moved from the snapshot's `02bdd3b` to `4cc74de` during the node. The two passages I quote are unchanged at `4cc74de`.

*The manager's note:* the worker's item 4 corrects two statements of mine. On node 109 I misdescribed the amendments: they were filed from other nodes' re-pointing lists, and the human's own amendment there was of clause 5 alone. On nodes 296 and 299, the human's amendments were an "ok" to my proposed wording, not of their own accord.

## Flags

`311.1` **· settled** `ASSUMPTION` — Where the fix goes. My recommendation described the fix as one implementation node on `graph-conventions.md` `### \`## Acceptance condition\``, stating there who is limited and that an amended condition goes to the worker and the checker. The human's "ok" settled the substance. Placement I settled myself under node 312's resolved split, which the human approved: rules about who may change a condition live in `SKILL.md`, and `graph-conventions.md` keeps a pointer to them. So the new node removes the two wrong sentences from `graph-conventions.md` rather than restating the rule there. It carries the worker notice into `SKILL.md`, extending the existing sentence "Where the human amends a condition while a check is live, tell the checker." If the human wanted the rule stated in `graph-conventions.md` itself, the node's clauses 1 and 2 move there, and node 312's split is broken for this one rule. No round was run on this: I decided it from node 312's answer and the files on master at `4cc74de`.
