# Whether the shipped checker contract says which route "open no other file beside it" governs

Type: grilling
Status: resolved

Blocked by: 334

## Answer

The shipped checker contract gains one sentence under `## What you are given`: a path handed over as the work is read as the work, even inside the effort's directory.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The human took the recommendation. The node it surfaced is [node 378](378-a-path-given-as-the-work-is-read-as-the-work.md). Flags 172.1 settle at the node closing report.

## Question

*Surfaced by [An acceptance condition demands facts about files the checker is told it does not read](163-a-condition-demands-facts-the-checker-does-not-read.md)'s worker, and pasted as it wrote it.*

> Node 143 landed, inside `## The standards you hold the work against`, the
> sentences *"The implementation-rules file is the single exception, and only for the
> standards in it"* and *"read nothing else in the effort's directory … open no other
> file beside it"*. A checker whose changed paths all sit in the effort's directory
> cannot tell from that section whether those sentences reach the paths it was handed as
> the work. This effort settles it in its own map. **This node does not reopen that
> decision** — it asks only whether the shipped sentence should say which of the two
> routes it governs, for an effort in another repo that will have no such map rule and
> whose first record-editing node's checker will meet the same ambiguity with nothing to
> resolve it.

**Blockers, in the worker's words:** *"node 164, which is open and edits the same section of the same shipped file."*

## The manager's note at filing

*Not a change to anything above.*

**This node's subject is [flag `163.2`](163-a-condition-demands-facts-the-checker-does-not-read.md)** — its author's
own reading of the shipped sentence as bounded by its section, which it recorded as a belief it had not put to the
human. The flag and this node are two halves of one thing.

**The human has already decided the effort-local half**, `verbatim`: *"I would say add it to the rules in the map
somewhere, not the skill at it is relevant only for this project"*. This node asks about the shipped file only, which
is the half that direction did not reach.

*The manager's note, 2026-09-26:* node 164 was superseded by [node 334](334-land-the-open-repairs-to-the-checker-contract-in-one-change.md), so this node's blocker is re-pointed to 334.

## Interview

#### Question 1, relayed 2026-10-02

*Pasted as the worker handed it back.*

```
NODE:          Whether the shipped checker contract says which route "open no other file beside it" governs (node 172)
ABOUT:         This node decides whether the shipped checker contract should say that its ban on reading the record leaves alone the changed paths the checker is handed as the work. It is being asked now because node 334, its blocker, has resolved and landed its changes to that file.
SO FAR:        I read the node, map.md, the decisions.md lines for nodes 143, 163 and 334, the shipped `.claude/skills/expedition-checker/SKILL.md` as it stands (24,280 bytes), and this effort's rule in `map-implementation-rules.md`.
               - The sentences the node quotes have moved. The ban now appears twice in the shipped file. Under `## What you are given`: "Leave the record unread, and do not go looking for it. The one exception is `map-implementation-rules.md`, and only for the standards in it." Under `## The standards you hold the work against`: "Read only the standards in it, and open no other file in the effort's directory." Given 3 separately hands the checker "the paths that changed". Neither passage says what happens when a changed path is a record file. The first passage is the broader ban, so it is where any fix belongs.
               - The ambiguity is not specific to this project. The shipped implementation contract's hard rule 1 says "Write a graph file only where your node's own work is a change to that file". The manager's skill also allows a node whose own work is a change to a graph file. So in any repo, an implementation node can hand its checker changed paths inside `.scratch/<effort>/`, and that checker has nothing that tells it whether it may read them.
               - This effort already settles the question locally, in `map-implementation-rules.md`: the instruction "governs the route by which standards reach the checker, and not the changed paths it was given as the work". That rule also carries project-specific material: changes to a node's status line, `decisions.md` or `flags.md` are manager bookkeeping and are a FAIL, and the checker must say it read the changed paths under that rule. You placed that rule locally, in your words: "I would say add it to the rules in the map somewhere, not the skill at it is relevant only for this project". This node does not reopen that decision.
               - Settled on my own authority: the fix would be one sentence in the `## What you are given` paragraph, which covers both passages because it states how the work reaches the checker. It ships none of the bookkeeping material. No open node's condition or question depends on the ban's wording. Node 214 (open) edits the same file, but a different table, so the two nodes would only need separate turns at the file.
ASK:           Should the shipped checker contract gain one sentence saying that a changed path handed over as the work is read as the work, even when it sits in the effort's directory, or should the shipped file stay silent and leave each effort to settle it?
RECOMMENDED:   Ship it. Add after "The one exception is `map-implementation-rules.md`, and only for the standards in it." the sentence: "A path you were given as the work is the work wherever it sits, and you read it." It adds about 85 bytes, roughly 0.35% of the file. This is the general half that your earlier answer did not cover: the shipped contracts themselves allow record-editing work in any repo, so a checker elsewhere will hit the same ambiguity with no local rule to settle it. A checker that reads the ban broadly cannot check that work at all and would have to raise. The project-specific half (the bookkeeping FAIL and the say-so) stays in `map-implementation-rules.md`. As a follow-up, that file's own restatement of the disambiguation could then shrink to a pointer at the shipped sentence.
ALTERNATIVES:  - Leave the shipped file silent. This saves the bytes and reads your earlier answer as covering the whole question, but a checker in another repo meets a record-editing node with nothing to resolve the ambiguity.
               - Ship the full local rule, including the bookkeeping FAIL and the say-so. This contradicts your placement of that material as specific to this project, and adds several hundred bytes.
               - Narrow the second passage instead ("open no other file in the effort's directory beyond the paths given as the work"). The broader "Leave the record unread" ban in `## What you are given` would stay ambiguous.

RETROSPECTIVE:
1. What I had to hunt for: where the quoted sentences went (your notes said they had moved, and I found the second occurrence in `## What you are given` by reading the file), and whether the shipped contracts actually allow record-editing implementation work in other repos (found in hard rule 1 of the implementation contract).
2. What arrived that this node did not need: the full map.md (about 48KB), of which only the writing rules and the pointer to the implementation-rules file mattered. Nothing in the spawn was surplus.
3. What would have made this easier: being told that the ban appears in two places in the shipped file, and the location of this effort's map rule (which file and heading). I found it by searching for "record file".
4. What was stale, wrong or contradictory: the node's `## Question` quotes sentences no longer in the shipped file ("The implementation-rules file is the single exception, and only for the standards in it"; "open no other file beside it"). Its stated blocker, node 164, is superseded; the manager's note already re-points it to node 334. The human's verbatim "relevant only for this project" sits in tension with the fact that the shipped implementation contract permits graph-file work in any repo. That tension is why I am asking this question.
```

#### The human's answer to question 1, 2026-10-02

`verbatim`: *"ok"*

The manager had put the question with the line "Please answer node 172: "ok for recommended" adds to the checker contract "A path you were given as the work is the work wherever it sits, and you read it."; or name an alternative." So the reply takes the worker's `RECOMMENDED`: that one sentence ships in `.claude/skills/expedition-checker/SKILL.md` after "The one exception is `map-implementation-rules.md`, and only for the standards in it.", and the project-specific part stays in `map-implementation-rules.md`.

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      Whether the shipped checker contract says which route "open no other file beside it" governs (node 172)

ANSWER:        Yes. The shipped checker contract says it in one sentence. In `.claude/skills/expedition-checker/SKILL.md`, under `## What you are given`, the sentence "A path you were given as the work is the work wherever it sits, and you read it." follows the sentence "The one exception is `map-implementation-rules.md`, and only for the standards in it."

The ban is not specific to this effort. The shipped implementation contract permits work that changes a graph file ("Write a graph file only where your node's own work is a change to that file"), so a checker in any repo can be handed changed paths inside `.scratch/<effort>/`. Before this change, the shipped file did not say whether the record ban reached those paths. The ban appears twice: "Leave the record unread, and do not go looking for it" under `## What you are given`, and "open no other file in the effort's directory" under `## The standards you hold the work against`. The sentence sits beside the broader of the two. Because it states how the work reaches the checker, it settles both passages, so the second passage keeps its words.

Only the general half ships. This effort's project-specific rule stays in `map-implementation-rules.md`, as the human placed it at node 163: a change to a node's status line, `decisions.md` or `flags.md` is manager bookkeeping and a `FAIL`, and the checker says it read the changed paths as the work under that rule. The sentence adds about 85 bytes to a file of about 24 KB. That cost was weighed against the human's wish to compact the skills.

The human's reply, `verbatim`, to a question that recommended this sentence at this place: *"ok"*. The manager's prompt to the human had stated that this reply takes the recommendation.

INDEX LINE:    The shipped checker contract gains one sentence under `## What you are given`: a path handed over as the work is read as the work, even inside the effort's directory.

FLAGS:         ASSUMPTION: I judged that one sentence in `## What you are given` settles both statements of the ban, so the sentence under `## The standards you hold the work against` ("open no other file in the effort's directory") keeps its words. The new sentence states how the work reaches the checker, so the second passage reads as being about the standards route only. A second edit would have added bytes the human wants kept out. The recommendation the human assented to included this judgement, but they were not asked about it as a separate question.
               Index: Node 172 added its work-path sentence only under `## What you are given` and left the standards section's "open no other file" wording alone, judging that one sentence settles both statements of the ban.

NEW NODES:     Name: Say in the shipped checker contract that a path given as the work is read as the work
               Kind: implementation
               Question: Add the one sentence node 172 decided to `.claude/skills/expedition-checker/SKILL.md`.
               Blockers: none. It shares `.claude/skills/expedition-checker/SKILL.md` with node 214 (open), whose condition concerns the table under `### When what you check against is itself the problem` and limits only that node's own changes. That is a scheduling clash over one file for the manager, not a defect to join.
               Acceptance condition:
                 1. In `.claude/skills/expedition-checker/SKILL.md`, under the heading `## What you are given`, the sentence "A path you were given as the work is the work wherever it sits, and you read it." appears word for word. It comes immediately after the sentence "The one exception is `map-implementation-rules.md`, and only for the standards in it." and before the sentence "The acceptance condition as given to you is the only statement of intent you get." Compare on the text with its line breaks joined into single spaces. Before this work, both of those neighbouring sentences are present in that paragraph, and the new sentence appears nowhere in the file.
                 2. No other sentence of `.claude/skills/expedition-checker/SKILL.md` changes, and no heading in it is renamed. Re-wrapping the lines of the one paragraph that holds the new sentence is allowed, provided that paragraph's words are otherwise unchanged when compared with line breaks joined into single spaces.
                 3. No file other than `.claude/skills/expedition-checker/SKILL.md` changes.
                 Scope: this came from no search. The named sentence and file are the work, not instances of a defect.

INVALIDATIONS: Node 163 is extended, not contradicted. Its index line says "the rule goes in this effort's implementation-rules file, not the shipped contract". That still holds for the rule it wrote (the bookkeeping `FAIL` and the say-so), but the general half, that a changed path is read as the work, now also ships. The rule in `map-implementation-rules.md` that the instruction "governs the route by which standards reach the checker, and not the changed paths it was given as the work" becomes a restatement of shipped text once the new node lands. It stays correct, and no node is proposed to shrink it. That is the manager's call under the compaction wish.
               Node 143 is extended. Its exception, that the checker reads `map-implementation-rules.md` for the standards only, gains a sibling sentence carving the work's own paths out of the record ban.
               Flag `163.2` (the worker's reading of the shipped sentence as limited to the standards route) is confirmed in shipped text by this answer.

CONDITIONS:    Searched the open nodes' `## Acceptance condition` and `## Question` sections (every open node, claimed or not) for "leave the record unread", "one exception", "wherever it sits", "paths that changed", "read as the work", "What you are given", "open no other file", "standards you hold the work against" and `expedition-checker/SKILL.md`. Matches were nodes 214, 41, 30 and node 172 itself. Node 214's clauses concern the table under `### When what you check against is itself the problem`, and its clause 3 limits only its own work. Node 41's clause 8 says the checker file is not changed by its own work. Node 30's question names the checker file as where a flag check would land. None is made wrong by this answer, and no replacement clause is written. Node 376 landed after my question (35ce19d1) and touched hard rule 1 only. I checked the tree as it stands: on unwrapped text, the anchor sentence occurs once and "wherever it sits" occurs nowhere under `.claude/skills`.

MISSING FROM MAP: Which file and heading hold this effort's rule on record paths as work. map.md says only that the implementation-rules file holds "the standards work is held against". I found the rule by searching `map-implementation-rules.md` for "record file". I also had to find for myself that the shipped ban appears twice in the checker file; I got that by reading the file.

RETROSPECTIVE:
1. What I had to hunt for: where the quoted sentences moved to, where the effort-local rule sits, and that the implementation contract allows graph-file work in any repo (hard rule 1).
2. What arrived that this node did not need: most of map.md (about 48 KB). Only the writing rules and the pointer to the implementation-rules file bore on this node.
3. What would have made this easier: a spawn note that the ban appears twice in the checker file. The resume note about node 376's landing was useful, because it confirmed that the paragraph this node's condition anchors on was unmoved.
4. What was stale, wrong or contradictory: the node's `## Question` quotes sentences that are no longer in the shipped file, and its in-text blocker is node 164, which is superseded; the manager's note re-points it. The human's earlier "relevant only for this project" sat in tension with the implementation contract's permission for graph-file work in any repo. This answer settles that tension for the general half only.
`````

## Flags

`172.1` `ASSUMPTION` **· settled** — Node 172 added its work-path sentence only under `## What you are given` and left the standards section's "open no other file" wording alone, judging that one sentence settles both statements of the ban. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-10-02:* flags 172.1 settle at the node closing report that closes this node.
