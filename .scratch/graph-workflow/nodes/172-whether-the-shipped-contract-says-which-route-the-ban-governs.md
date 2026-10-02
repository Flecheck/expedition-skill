# Whether the shipped checker contract says which route "open no other file beside it" governs

Type: grilling
Status: claimed

Blocked by: 334

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
