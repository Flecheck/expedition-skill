# Nothing bounds what a spawn may assert about the answer its node is meant to reach

Type: grilling
Status: resolved

## Answer

A worker checks each claim of fact in the manager's notes and in its node's `## Question` before relying on it; the manager contract's existing ban on stating the answer is unchanged.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. It surfaced [node 380](380-ship-the-check-on-a-spawns-claims.md), which ships the answer. Its `INVALIDATIONS` extend node 8 and narrow node 47's annotation; the manager notes them here and edits neither. Flags 78.1, 78.2, 78.3 settle at the node closing report.

## Question

A manager note is capped at **context the manager already holds** ([Relay protocol](08-relay-protocol.md)'s `F9`),
which bounds where the material comes from and **not what it may claim.**

**Measured twice, both against the manager.** [How an agent workflow and its skills reduce their own token
cost](52-token-cost-of-a-workflow.md)'s annotation records the manager writing an unestablished inference into node
68's `## Question` and into two spawns *"in each case as settled fact"*. [Review every shipped file against
`/writing-great-skills`](47-review-shipped-skills.md)'s annotation records four manager pointers travelling into
node 54's spawn and **all four coming back falsified.**

**And the two workers said the same thing independently, in their own retrospectives.** Node 69's: *"A spawn that
hands a worker the conclusion it is meant to test costs the worker the work of unpicking it."* Node 68's: *"A spawn
that asserts findings rather than pointing at sources costs a correction round when the assertion is stale."*

The manager's remedy in the node 54 case — instructing the worker to **treat manager material as evidence rather
than argument** — is its own invention and is written nowhere.

## What has to be decided

1. **Must a spawn mark what the manager asserts as evidence rather than as a settled fact?**
2. **Does the same bound reach a node's `## Question`**, which the manager also writes and which a worker reads as
   the frame for its own work? Node 52's annotation records an inference landing there as well as in the spawns.
3. **Is there anything a spawn may never assert at all — the conclusion the node exists to test?**

**Blockers: none.**

Reported by node 75's worker as item 177 of §Q2, *practice the manager adopted on its own authority*.

## Interview

#### Questions 1 and 2, relayed 2026-10-02

*Pasted as the worker handed it back.*

```
NODE:          What a spawn may assert (node 78)
ABOUT:         This node decides what limits a manager's spawn on what it may claim. Today the limit covers only where a note's material may come from, not whether its claims are true. It is being decided now because the manager's claims keep arriving wrong, and the manager has started improvising a "treat these as claims to check" line in its spawns.
SO FAR:        I read the node, map.md, the grilling contract, the manager contract's `## Spawning a worker` as it stands, the annotations on nodes 47, 52 and 69, and the evidence in nodes 66 and 67. Node 211 has no decisions.md line yet because it is still open.
               - The shipped manager contract says: "Write a note only from context you already hold. Do not read code, or go and find things out, in order to write one. A note may name the one of a worker's questions you believe is sharpest. It may not say what you think the answer is." So the third question this node asks ("may a spawn assert the conclusion?") is already settled for notes. That sentence has been there since the contract was first written (commit 4f9781b00, 2026-08-29).
               - Both of the node's original cases came before that contract existed. Node 68 was created on 2026-08-22 and node 54 on 2026-08-26.
               - The cases after the contract shipped are claims of fact, not claims about the answer. The cap does not reach them. One: the manager's spawn for node 66 called node 367 an instance, and node 66's worker found it was not. Two: this very spawn says node 67's handover called node 214 "claimed" and node 375 "open". The handover actually says 214 claimed and 375 claimed. At that commit (9213ad95a), 214 was open and 375 was resolved. So the worker was wrong, and the manager's retelling of the worker's error was also wrong.
               - What failed each time was a false or stale fact the manager honestly held. A limit on where a note's material comes from cannot catch that, and the manager cannot mark claims it does not know are wrong. The worker reading the note is the one party that can check.
               - Nothing in any worker contract says how to treat manager notes. Five contracts (grilling, research, prototype, precondition, implementation) share the sentence "Read each of the following. Do not trust any summary of them." That sentence covers the files the worker is told to read, not the notes.
               - Settled on my own authority (it will come back as an ASSUMPTION flag): the third question needs no new rule, because the shipped "It may not say what you think the answer is" already answers it for notes. The question of whether the same limit reaches a node's `## Question` is Q2 below.
               - Settled on my own authority: whatever rule ships covers only the manager's own material. A direction from the human, a permission the human granted, and an acceptance condition stay authoritative, because the manager contract already sets them apart from notes.

Q1. Whose job it is to catch a wrong claim
CONTEXT:       The node asks whether a spawn must mark what the manager asserts as evidence rather than settled fact. The recorded failures suggest the check works better on the reading side.
ASK:           Should the fix be a rule for the worker reading the spawn (check each claim in the manager's notes before relying on it), rather than a rule that the manager mark its claims?
RECOMMENDED:   Yes, a reader-side rule. Ship it by rewording the existing sentence in the five worker contracts, for example: "Read each of the following rather than any summary of them, and check each claim of fact in the manager's notes before you rely on it." That adds about 15 words per contract, with no new section and nothing added to the manager contract. It rests on the finding above: the manager cannot mark claims it does not know are wrong, and the worker can check them cheaply. This spawn's opening line already does this by hand, and it caught a wrong claim this time. Implementation spawns that carry "confirmed at <commit>" notes stay cheap to check, because the commit is given.
ALTERNATIVES:  Writer-side: the manager labels every assertion as a claim and gives its source. This costs more in every spawn, and it fails exactly when the manager believes the wrong claim.
               Both rules together: more text, and the writer-side half adds nothing the reader-side half does not already catch.
               No rule: the manager keeps improvising the line, and a spawn that leaves it out goes unchecked.

---

Q2. Does the same check reach a node's `## Question`
CONTEXT:       Node 52 records the manager writing an inference into node 68's `## Question` as settled fact. A worker reads its question as the frame for all its work, and nothing tells it to check the premises in that frame.
ASK:           Should the worker also check the claims of fact in its own node's `## Question` before relying on them, apart from text marked as the human's own words?
RECOMMENDED:   Yes, in the same sentence as Q1: "check each claim of fact in your node's `## Question` and in the manager's notes before you rely on it". It costs about six more words per contract. It rests on the node 68 case. A wrong premise in the question shapes every turn of the attempt, so it costs more than a wrong note. A question pasted from another worker's NEW NODES is the same kind of unverified claim.
ALTERNATIVES:  Notes only: the cheapest option, but it leaves out the recorded node 68 case.
               A writer-side rule in the manager contract against stating an inference as fact when it writes a question. This has the same weakness as Q1's writer-side option, because the manager does not know which of its inferences are wrong.

RETROSPECTIVE
1. What I had to hunt for: whether the shipped cap already answers the third question (it does, and I found that with git log -S). I also had to find the dates of the node 54 and 68 spawns to see whether the cap was in force then (it was not). And I had to find which worker contracts share the sentence a rule would edit.
2. What arrived that this node did not need: the decisions.md line for node 8. Its content is the same as the cap in the shipped manager contract. Node 211 has no decisions.md line, because it is open, so pointing me at its "line" sent me to the node file, which I needed only to see that it is a sibling rule.
3. What would have made this easier: the node's `## Question` saying that "It may not say what you think the answer is" already ships. That would have answered half the node before I started.
4. What was stale, wrong or contradictory: the manager's note says node 67's worker called node 375 "open". The handover says "node 375 (claimed)". At that commit, 214 was open and 375 was resolved. The node's Question cites the cap as "capped at context the manager already holds (node 8's F9)". The shipped wording is now "Write a note only from context you already hold", as the manager predicted.
```

*The manager's note:* the worker is right that the manager's spawn misquoted node 67's handover: it said node 375 "open" where the handover says "claimed".

#### The human's answer to questions 1 and 2, 2026-10-02

`verbatim`: *"ok"*

The manager had closed the payload with "Please answer Q1 and Q2. "ok for recommended" takes both." The reply "ok" names no alternative, so it takes the worker's `RECOMMENDED` on both. Q1, the worker's: "Yes, a reader-side rule. Ship it by rewording the existing sentence in the five worker contracts, for example: "Read each of the following rather than any summary of them, and check each claim of fact in the manager's notes before you rely on it."" Q2, the worker's: "Yes, in the same sentence as Q1: "check each claim of fact in your node's `## Question` and in the manager's notes before you rely on it"."

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      What a spawn may assert

ANSWER:        **The worker checks the spawn's claims, rather than the manager marking them.** The human's reply to both questions was `verbatim`: *"ok"*, which takes the worker's recommendation on each.

               **1. Must a spawn mark what the manager asserts as evidence rather than settled fact? No. The worker reading the spawn checks it.** Each of the five worker contracts that take a spawn (grilling, research, prototype, precondition, implementation) rewords its sentence "Read each of the following. Do not trust any summary of them." It becomes a sentence that also tells the worker to check each claim of fact in the manager's notes before relying on it. A rule for the writer was set aside for two reasons. First, the manager cannot mark a claim it does not know is wrong. Second, every case recorded since the manager contract shipped was a wrong fact the manager believed, not a stated answer: node 66's spawn named node 367 as an instance, and node 66's worker found it was not. The cap on a note ("Write a note only from context you already hold") limits where a note's material comes from, and so cannot catch such a fact. The manager contract does not change. The improvised line "these are the manager's own claims, so treat them as claims to check" that spawns have been carrying becomes unnecessary once this ships.

               **2. Does the same limit reach a node's `## Question`? Yes, in the same sentence.** The worker also checks each claim of fact in its own node's `## Question` before relying on it. Text marked as the human's own words is left out. The ground is node 68: the manager wrote an inference into that node's `## Question` as settled fact (recorded in node 52's annotation), and a wrong premise in the frame shapes every turn of the attempt.

               **3. Is there anything a spawn may never assert? Already answered for notes, and nothing new is added.** The manager contract's `## Spawning a worker` has said since it was first written (commit 4f9781b00, 2026-08-29) that a note "may name the one of a worker's questions you believe is sharpest. It may not say what you think the answer is." Both of this node's original cases, the spawns for node 54 (created 2026-08-26) and node 68 (created 2026-08-22), came before that sentence existed.

               **What the check covers is only the manager's own material.** A direction from the human carried in their words, a permission the human granted, and an implementation node's acceptance condition stay authoritative. The manager contract's `### Two things that travel in a spawn and are not yours` already sets the first two apart from notes, and a worker may not fix the third.

               The cost is about twenty words per contract, by rewording an existing sentence, with no new section. This was weighed against the human's wish to compact the skills.

INDEX LINE:    A worker checks each claim of fact in the manager's notes and in its node's `## Question` before relying on it; the manager contract's existing ban on stating the answer is unchanged.

FLAGS:         ASSUMPTION: The node's third question was not put to the human, because the shipped manager contract already answers it for notes: a note "may not say what you think the answer is", in place since commit 4f9781b00. Both original cases came before that sentence, and the cases since were wrong facts rather than stated answers, so no further ban was proposed.
               Index: Node 78 added no ban on what a spawn asserts, because the manager contract already forbids a note to state the answer and no case since has broken that.

               ASSUMPTION: The check covers only the manager's own material: its notes, and the node's `## Question` outside the human's quoted words. A human direction, a permission the human granted, and an acceptance condition stay authoritative, because the manager contract already sets the first two apart from notes and a worker may not fix a condition.
               Index: Node 78's check-before-relying rule covers the manager's notes and a node's question, never a human direction, a permission or an acceptance condition.

               ASSUMPTION: The rule goes into the five contracts that share the sentence "Read each of the following. Do not trust any summary of them.", and not into the checker or cascade contracts. The checker's spawn carries the ground rules and nothing of the manager's own. The cascade contract has no such reading sentence. Whether a cascade worker needs the rule was left unexamined.
               Index: Node 78's rule ships in the five contracts that read a spawn's pointers, leaving the checker and cascade contracts unchanged and the cascade case unexamined.

NEW NODES:     Name:     Ship the check on a spawn's claims into the five worker contracts
               Kind:     implementation
               Question: Write node 78's answer into the worker contracts. A worker checks each claim of fact in the manager's notes, and in its own node's `## Question` outside the human's quoted words, before relying on it. The rule goes into the existing sentence each contract uses to tell the worker to read its sources rather than summaries of them.
               Blockers: none. It shares the `## What you read` section of the same five files with open node 32 (the `flags.md` sentence) and edits the same files as open node 41 (FRICTION). The concerns differ, so this is code-slot scheduling, not a defect to join.
               Acceptance condition:
                 The work is these five files:
                   `.claude/skills/expedition-grilling/SKILL.md`
                   `.claude/skills/expedition-research/SKILL.md`
                   `.claude/skills/expedition-prototype/SKILL.md`
                   `.claude/skills/expedition-precondition/SKILL.md`
                   `.claude/skills/expedition-implementation/SKILL.md`
                 Scope came from a search over the working tree: `grep -n 'Do not trust any summary of them' .claude/skills/*/SKILL.md`, which on 2026-10-02 returned exactly one line in each of the five files above and in no other file. If the search reaches an instance outside this list when the work is done, report it and do not edit it.

                 Done means every one of the following is true of the finished tree.
                 1. In each of the five files, the sentence "Read each of the following. Do not trust any summary of them." is gone. In its place, at the same spot, the text states all three of the following:
                    (a) the worker reads each listed source itself rather than a summary of it;
                    (b) the worker checks each claim of fact in the manager's notes in its spawn before relying on it;
                    (c) the worker checks each claim of fact in its own node's `## Question` before relying on it, except text marked there as the human's own words.
                 2. The replacement text says (a) to (c) as what to do, with no prohibition. It adds no heading and adds at most 40 words to each file compared with the removed sentence. An example of wording that meets clauses 1 and 2: "Read each of the following rather than any summary of them. Before you rely on a claim of fact in the manager's notes, or in your node's `## Question` outside the human's quoted words, check it."
                 3. The replacement text is the same in all five files.
                 4. Nothing in the replacement tells the worker to check, doubt or re-derive a direction from the human, a permission the human granted, or an acceptance condition.
                 5. No other sentence of the five files changes.
                 6. No other file changes. That includes `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition-checker/SKILL.md`, `.claude/skills/expedition-cascade/SKILL.md` and every file under `.scratch/graph-workflow/`.
                 7. The tree meets the bar.

INVALIDATIONS: Node 8 (Relay protocol), F9, which caps a manager note at context the manager already holds: extended, not contradicted. The cap still governs where a note's material comes from, and a reader-side check now governs whether its claims are relied on.
               Node 47's annotation, which calls the instruction to node 54's worker to "treat manager material as evidence rather than argument" "the spawn rule working": narrowed in standing. That instruction was the manager's own invention when it was given, and from the new node's landing it is shipped contract text rather than an improvised spawn line.
               No other resolved node changes.

CONDITIONS:    I searched every open and claimed node's `## Acceptance condition` and `## Question` for these terms: "Do not trust any summary", "summary of them", "manager's notes", "MANAGER NOTES", "a note may", "context you already hold", "evidence rather than", "What you read", and the five contract paths.
               - Node 41 (open), condition clause 7, names the same five paths. It concerns the FRICTION marker, and nothing in it conflicts. No replacement.
               - Node 32 (open), question, names the same five files by line number, about the `flags.md` sentence in the same section. A different concern, so no replacement. Its line numbers may shift when either node lands, which writing rule 4 already warns about.
               - Node 130's question uses "evidence rather than as a specification" about a different subject, so it does not match in substance.
               - Node 211 (open) is a sibling rule: a number handed onward carries its date and its reader re-derives it. A number in a manager note is now also a claim to check under this answer. That is consistent with node 211, so its question and condition are unchanged.
               I wrote no replacement clause and changed no open node's question.

MISSING FROM MAP: The map does not say that the manager contract already forbids a note to state the answer, so the node's third question looked open until I checked the shipped file and its history with `git log -S`. The map also has no line for the practice of treating spawn claims as claims to check, which spawns have been carrying. I learned of it from this spawn.

RETROSPECTIVE
1. What I had to hunt for: whether the shipped cap already answers the third question (it does, found with `git log -S`). The dates of the node 54 and 68 spawns compared with the contract's first commit. Which worker contracts share the sentence to edit. Whether an open node already owns that sentence (none does; node 32 is a neighbour in the same section). At the resume, the commit and the recorded reply, both of which I checked.
2. What arrived that this node did not need: the decisions.md line for node 8, which only repeats the cap in the manager contract. And the pointer to node 211's "line": node 211 is open, so it has no decisions.md line, and its node file mattered only as a sibling rule.
3. What would have made this easier: the node's `## Question` noting that "It may not say what you think the answer is" already ships. That would have answered a third of the node before I started.
4. What was stale, wrong or contradictory: the spawn's note said node 67's worker called node 375 "open". The handover actually says "node 375 (claimed)", and at commit 9213ad95a node 214 was open and node 375 was resolved, so the worker's claim and the manager's retelling of it were both wrong. The node's `## Question` quotes the cap as "capped at context the manager already holds", but the shipped wording is now "Write a note only from context you already hold", as the manager's note predicted. The claims in the resume all checked out.
`````

## Flags

`78.1` `ASSUMPTION` **· settled** — The node's third question was not put to the human, because the shipped manager contract already answers it for notes. *(The worker's full text is under its handover's `FLAGS`.)*

`78.2` `ASSUMPTION` **· settled** — The check covers only the manager's own material, never a human direction, a permission or an acceptance condition. *(The worker's full text is under its handover's `FLAGS`.)*

`78.3` `ASSUMPTION` **· settled** — The rule goes into the five contracts that share the reading sentence, not the checker or cascade contracts; the cascade case is unexamined. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-10-02:* flags 78.1, 78.2, 78.3 settle at the node closing report that closes this node.
