# Whether a pointer that summarises its target restates it

Type: grilling
Status: resolved
Blocked by: none

## Answer

A pointer that lists or summarises its target heading restates it under rule 6; a pointer names the heading and, in one clause at most, what the reader goes there for.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The nodes it surfaced are [node 367](367-say-in-rule-6-what-a-pointer-may-hold.md) and [node 368](368-cut-the-pointers-that-list-their-target-to-one-clause.md). Flags 361.1 settle at the node closing report.

## Question

Under standing rule for writing 6, does a pointer that names a heading and then summarises what that heading holds count as restating it? Examples: `SKILL.md` `## Acceptance conditions`' three-sentence first paragraph, `SKILL.md` `### The human's words`' last paragraph, and `graph-conventions.md` `### Recording the human's words`' first paragraph. If it does, should every such pointer be one sentence? This decides about 330 words (node 355, Tier 2).

*Reported by [node 355](355-where-the-manager-read-shipped-files-restate-one-another.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Interview

#### Question 1, relayed 2026-09-28

*Pasted as the worker handed it back.*

```
NODE:          Whether a pointer that summarises its target restates it

ABOUT:         Standing rule for writing 6 says to point at a heading of a file the reader already reads, not restate it. Some pointers name the heading and then list what it holds. This node decides whether that list counts as restating. It is decided now because it controls about 330 words of the compaction you asked for (node 355, Tier 2).

SO FAR:        I read rule 6 in map.md, node 253's answer, node 355's Tier 2, node 312's pointer clause, and the four example passages in the tree. What I found:
               - The manager is told to read both `expedition/SKILL.md` and `graph-conventions.md` (SKILL.md, the paragraph after the opening). So rule 6's first sentence applies to every example: the reader will open the target anyway. Your node 253 carve-out (duplicate when the target "would not be read" and is mostly useless) does not apply to any of them.
               - Node 312 already expected pointers of "one sentence" and wrote them that way. Its clause 2: "that passage points at the other file's heading in one sentence."
               - The examples say more than a pointer needs to, in two ways:
                 (a) Some list the target's contents item by item. `SKILL.md` `### The human's words` ends with a 57-word pointer that names "the three marks `verbatim`, `paraphrase` and `standing yes`, the quoted option, and whether an entry goes under `## Interview` or `## Review`". `graph-conventions.md` `### Recording the human's words` opens with a 53-word pointer back the other way, listing four things SKILL.md says.
                 (b) Some state part of the rule itself. `SKILL.md` `## Acceptance conditions` spends 86 words over three sentences pointing at `graph-conventions.md`, and it says what the one irreparable demand is ("a demand about the record as a whole"). `SKILL.md` `### The four constraints on a condition you write yourself` item 2 names the three rules a condition is read back against.
               - For contrast, here is a pointer that is already short. `graph-conventions.md` `` ### `## Acceptance condition` `` opens with "`## Acceptance conditions` in `SKILL.md` says who writes it and who may change it after it is written." That is one sentence with one clause about what the reader goes there for.
               Settled on my own authority: none yet.

ASK:           Under rule 6, what may a pointer to a heading say beyond naming it? Does listing or summarising what that heading holds count as restating it?

RECOMMENDED:   Yes, it counts as restating. A pointer names the heading and, in one clause at most, what the reader goes there for. It lists none of the target's items and states none of its rules. That makes "one sentence per pointer" true as a result, but the rule tests what the pointer says, not how many sentences it has. A sentence cap alone can be met with one long sentence that still lists everything. The "who writes it and who may change it" pointer above is the model. Two reasons:
               - The reader reads the target anyway, so the list is paid for twice.
               - A copied list has to be kept in step with its target. Until the list is rewritten, a change to the target makes the list wrong.
               If you agree, I would hand back two things:
               - a rewording of rule 6 in map.md, so the rule still binds this effort only
               - an implementation node that cuts the four passages above to this form (about 110 words saved)
               The other Tier 2 items are restatements outside a pointer. The rule you choose here does not decide them, and I would list them for node 355's follow-up.

ALTERNATIVES:  - Only stating a rule's content counts as restating. A list of the target's topics stays allowed as a routing aid. This cuts (b) but keeps (a), saving roughly half as much.
               - A plain one-sentence cap per pointer, with no test on what the sentence says. It is easy to check, but a long sentence can still carry the whole list.
               - A summary is not restating. The four passages stay as they are, and Tier 2's pointer items are dropped.
```

#### The human's answer to question 1, 2026-09-28

The human, `verbatim`: *"361 ok"*. It takes the worker's recommendation: "Yes, it counts as restating. A pointer names the heading and, in one clause at most, what the reader goes there for. It lists none of the target's items and states none of its rules."

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      Whether a pointer that summarises its target restates it

ANSWER:
**Yes. Under standing rule for writing 6, a pointer that lists or summarises what its target heading holds restates it.** A pointer names the heading and says, in one clause at most, what the reader goes there for. It lists none of the items that heading holds and states none of its rules. So each pointer comes out as one sentence. The test is what the pointer says, though, and not how many sentences it has, because one long sentence can still carry the whole list. The model is the opening of `graph-conventions.md` `` ### `## Acceptance condition` ``: "`## Acceptance conditions` in `SKILL.md` says who writes it and who may change it after it is written."

Grounds: every example's reader is the manager, which is told to read both `expedition/SKILL.md` and `graph-conventions.md`. So a list in the pointer is read twice, and it goes wrong when the target changes. Node 253's carve-out (restate where the target would not otherwise be read and is mostly text the reader does not need) does not apply to these pointers. Node 312 already wrote its pointers as one sentence each.

This binds this effort only, as rule 6 does. It is written into rule 6 in `map.md` and into no shipped file.

How it was reached. One question was put: what may a pointer say beyond naming its heading, and does a summary count as restating? The recommendation was "yes, heading plus one clause, no list, no rule content". The options set aside were: only rule content counts, so topic lists stay; a plain one-sentence cap; summaries are not restating. The human's reply, `verbatim`: *"361 ok"*. That is assent to the recommendation.

The passages this reaches are the four pointer items of node 355's Tier 2 item 13: `SKILL.md` `### The human's words`' last paragraph, `graph-conventions.md` `### Recording the human's words`' first paragraph, `SKILL.md` `## Acceptance conditions`' first paragraph, and `SKILL.md` `### The four constraints on a condition you write yourself` item 2. Together they save about 110 words. Tier 2 items 14 to 19 are restatements outside a pointer, and this answer does not decide them.

INDEX LINE:    A pointer that lists or summarises its target heading restates it under rule 6; a pointer names the heading and, in one clause at most, what the reader goes there for.

FLAGS:
- ASSUMPTION: The human's "361 ok" assented to a recommendation that said the answer would reach no shipped file except through an implementation node, and would be written into rule 6 as effort-only text. I took the rule change to be effort-only because the map's rule applies where the human names no scope. Node 253 made rule 6 itself effort-only. What I did: I wrote the rule-6 wording and the cut of the four passages as two separate implementation nodes.
  Index: Took the pointer rule as effort-only, like rule 6, and split the map change from the shipped-file cuts into two nodes.

NEW NODES:

1. Name: Say in rule 6 what a pointer may hold
   Kind: implementation
   Blocked by: none (node 361 resolves with this handover)
   Question: Can standing rule for writing 6 in `map.md` say that a pointer names the heading and, in one clause at most, what the reader goes there for, listing none of the target's items and stating none of its rules?
   Acceptance condition:
   > The work is `.scratch/graph-workflow/map.md` and `.scratch/graph-workflow/map-history.md`, and no other file may be edited. The worker may not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`. The scope came from no search: the named place is the work.
   >
   > Done means all of the following are true of the finished tree.
   > 1. In `map.md`'s `## Notes`, rule 6 of the numbered list of this effort's standing rules for writing keeps its four existing sentences word for word. Directly after its first sentence ("**Point at a heading of another shipped file instead of restating what it holds, where the reader is already told to read that file.**") it gains these two sentences, word for word: "A pointer names the heading and says, in one clause at most, what the reader goes there for. It lists none of the items that heading holds and states none of its rules."
   > 2. Rules 1 to 5 are not reworded, renumbered or reordered.
   > 3. The list's bold lead-in names `nodes/361-whether-a-pointer-that-summarises-its-target-restates-it.md` as a markdown link, as a node that shaped the sixth rule.
   > 4. The text rule 6 held before this change is appended verbatim to `map-history.md`, under a heading that mirrors the section it came from. `map-history.md` gains text and loses none.
   > 5. Every markdown link in the two files resolves to a path that exists.

2. Name: Cut the pointers that list their target to one clause
   Kind: implementation
   Blocked by: none
   Question: Can the four pointers node 355 found listing or summarising their target heading be cut to the heading and one clause about what the reader goes there for?
   Note for the manager: this concerns the same two files as node 359 (`SKILL.md`, `graph-conventions.md`), but different passages. Node 359 is claimed, so under the contract these would be filed as a new node. If 359 is unclaimed when you file this, the clauses below may join its condition instead.
   Acceptance condition:
   > The work is `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition/graph-conventions.md`, and no other file may be edited. Scope: the scope came from no search command. The places are the four passages listed below, which node 355's worker found by reading both files in full. If you find another pointer in any file under `.claude/skills/` that lists the items its target heading holds or states that heading's rules, report it and do not edit it.
   >
   > A **pointer** here means text that names a heading of another file so that the reader goes there. In the finished form, each pointer names the heading and says, in one clause at most, what the reader goes there for. It lists none of the items that heading holds and states none of its rules. Example of the finished form, already in `graph-conventions.md`: "`## Acceptance conditions` in `SKILL.md` says who writes it and who may change it after it is written."
   >
   > Done means all of the following are true of the finished tree.
   > 1. `.claude/skills/expedition/SKILL.md`, `### The human's words`, last paragraph: the pointer to `### Recording the human's words` in `graph-conventions.md` is in the finished form. The paragraph no longer names the three marks `verbatim`, `paraphrase` and `standing yes`, the quoted option, or `## Interview` and `## Review` as where an entry goes. The pointer to where `graph-conventions.md` states the rule for the `DIVERGENCE` mark stays, in the finished form.
   > 2. `.claude/skills/expedition/graph-conventions.md`, `### Recording the human's words`, first paragraph: the pointer to `### The human's words` in `SKILL.md` is in the finished form. It no longer lists when the manager records an answer, what it pastes, when it marks an answer `paraphrase`, and what it does with a terse reply. The sentence saying that the section's rules cover `## Interview` and `## Review` stays.
   > 3. `.claude/skills/expedition/SKILL.md`, `## Acceptance conditions`, first paragraph: it points at `graph-conventions.md` in the finished form, in one sentence or in one sentence per heading it names. It no longer states the self-contained rule, the demand about the record as a whole, or what a condition owes about the search that produced its scope. The second paragraph ("Where an agent minted the node, …") is unchanged.
   > 4. `.claude/skills/expedition/SKILL.md`, `### The four constraints on a condition you write yourself`, item 2: the item still says to read the condition back before the node is claimed and to record that reading on the node. It no longer names the three rules one by one. Instead it points, in the finished form, at the heading of `graph-conventions.md` that holds them.
   > 5. Each statement that clauses 1 to 4 remove is still stated at the heading the pointer names. No rule is lost.
   > 6. No heading in any file under `.claude/skills/` is renamed. Every heading a changed pointer cites exists in the named file with exactly the cited text.

INVALIDATIONS: Node 253: an extension. Its rule 6 said to point instead of restating and did not say what a pointer may hold. This answer adds that a summary or a list of the target's contents counts as restating. Node 355: a narrowing of its Tier 2. Item 13's four pointer passages move from borderline to clear instances. Items 14 to 19 stay borderline, because they are restatements outside a pointer. Node 312: no change. Its one-sentence pointers already meet the test.

CONDITIONS:    I searched the `## Acceptance condition` and `## Question` sections of the 65 open nodes, claimed or not, for "one-sentence", "one sentence", "rule 6", "rule for writing 6", "The human's words", "Recording the human's words", "## Acceptance conditions" and "The four constraints on a condition". The matches that are not about pointers: 210, 149, 363, 156, 13, 271, 214, 190, 234. None of them states a pointer form this answer makes wrong. Node 359 (claimed) clause 5 cites `### Recording the human's words` as a heading to point at, which this answer does not change. I wrote no replacement clause. Node 360 (open): its question is unchanged. Where it chooses to cut a contract passage to a pointer at a glossary entry, this answer sets that pointer's form. So one part of how its answer is carried out is fixed, and its question is not answered.

MISSING FROM MAP: The map does not say that the manager is told to read both `expedition/SKILL.md` and `graph-conventions.md`. Rule 6 turns on that fact. I got it from the paragraph of `SKILL.md` that begins "`graph-conventions.md`, beside this file, holds".

RETROSPECTIVE
1. What I had to hunt for: node 253's actual rule and grounds. Its `## Answer` is only the index line, and the substance is under `## Handover, attempt 1`. The decisions.md lines needed a search by node path, because "node 253" as text did not match. I also had to find the passages' text in the tree, and which files the manager is told to read.
2. What arrived that this node did not need: the notes on node 362 (restating within `expedition/SKILL.md`). The map's bulk beyond the writing rules, as usual.
3. What would have made this easier: a spawn line saying that node 253's `## Answer` points at its handover, and that decisions.md entries are found by node path. Also, if node 355's Tier 2 had quoted the four passages in full, I would not have needed to open the shipped files.
4. What was stale, wrong or contradictory: nothing I found wrong. The node's question lists three examples, while node 355's item 13 has four (item 2 of the four constraints). I included all four.
`````

## Flags

`361.1` `ASSUMPTION` **· settled** — Took the pointer rule as effort-only, like rule 6, and split the map change from the shipped-file cuts into two nodes. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-09-28:* flags 361.1 settle at the node closing report that closes this node.
