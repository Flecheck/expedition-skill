# Whether a pointer that summarises its target restates it

Type: grilling
Status: claimed
Blocked by: none

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
