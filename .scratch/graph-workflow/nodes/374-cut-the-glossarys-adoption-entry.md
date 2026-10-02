# Cut the glossary's Adoption entry to its meaning

Type: implementation
Status: claimed
Blocked by: none

## Question

Can the glossary's **Adoption** entry lose its sentence listing adoption's steps, now that `adoption.md` states those steps and the kind of the import nodes?

*Reported by [node 370](370-cut-the-glossary-entries-that-restate-a-shipped-sections-rule.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none"*

## Acceptance condition

*Authored by node 370's worker and filed by the manager.*

> The work is `.claude/skills/expedition/glossary.md`, and no other file may be edited. Scope: no search produced it. The one place named is the work itself, not an instance of a defect.
> 1. In `.claude/skills/expedition/glossary.md`, the text between the line `**Adoption**:` and its `_Avoid_` line is exactly: "Starting an effort from a directory of work that already exists. It is a way of starting an effort, not a kind of node." The bold term line and the `_Avoid_` line stay word for word.
> 2. No rule is lost. Every part of the removed sentence ("It carries steps that starting from a conversation does not: taking the effort's name from the directory that already exists, resolving any reserved graph name the directory already uses for something else, deriving the map from the record the effort already wrote rather than from a conversation, declaring the label vocabulary from the foreign label families, and minting the bulk import as `precondition` nodes.") is stated in `.claude/skills/expedition/adoption.md`, read as a whole: its opening paragraphs, `## Your steps, in order` and `## The bulk import`. Where a part is stated nowhere in that file, the sentence stays and the worker reports it.
> 3. No other glossary entry, `_Avoid_` line or heading in any file under `.claude/skills/` changes.

## Handover, attempt 1

*The worker's own text, pasted, 2026-10-02.*

````
HANDOVER:      Cut the glossary's Adoption entry to its meaning
ANSWER:        The glossary's **Adoption** entry in `.claude/skills/expedition/glossary.md` now reads only "Starting an effort from a directory of work that already exists. It is a way of starting an effort, not a kind of node." The bold term line and the `_Avoid_` line are unchanged. The sentence listing adoption's steps was removed because `.claude/skills/expedition/adoption.md`, read as a whole, states every part of it:
                - taking the effort's name from the directory: `## Your steps, in order`, step 1;
                - resolving a reserved graph name the directory already uses: step 2, plus `## A reserved name already in use`;
                - deriving the map from the record the effort already wrote rather than from a conversation: step 3 ("Take its content from what the effort already wrote, and invent none of it", and ask the human where the foreign record states nothing);
                - declaring the label vocabulary from the foreign label families: step 4;
                - minting the bulk import as `precondition` nodes: the opening paragraphs ("Your part ends when you mint the bulk import as the graph's first nodes. Their kind is `precondition`."), and `## The bulk import` ("The import runs in two passes, each on `precondition` nodes.");
                - "steps that starting from a conversation does not": the first paragraph ("This file holds only the steps adoption adds to them").
                No part was missing, so the sentence was removed in full. No other entry, `_Avoid_` line or heading changed.
INDEX LINE:    The glossary's Adoption entry is cut to its meaning, because adoption.md's opening, its steps and its bulk-import section state every step and the import nodes' `precondition` kind.
FLAGS:         none
NEW NODES:     none
INVALIDATIONS: Node 370: an extension. Its answer kept Adoption whole because `## Your steps, in order` alone omits `precondition`. With `adoption.md` read as a whole, which is what this node's clause 2 asks for, that reason no longer holds, and Adoption is now cut like the other entries. Node 360's rule (the section keeps the rule and the entry keeps the meaning) is now applied to this entry too. It is not contradicted.
CONDITIONS:    I searched every open and claimed node file except 374, case-insensitively, for `Adoption**`, `Adoption entry`, `label families`, `reserved graph name`, `starting from a conversation` and "as `precondition` nodes". Nothing matched. A wider search for `adoption` and `glossary` matched only text unrelated to this entry. One hit was node 375's clause 7, which says the glossary is not changed by node 375's own work. That clause limits node 375 and does not conflict with this work. I write no replacement clauses, and no open node's question changes.
MISSING FROM MAP: none
GATE PAYLOAD:  Checker findings: none yet.
               Paths touched: .claude/skills/expedition/glossary.md (in worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/374-adoption, uncommitted).
               Bar: the repo has no build, tests, formatter or CI. map-implementation-rules.md records the same, and nothing in the worktree contradicts it. The edited entry keeps the glossary's line wrapping.
               Proposed commit message:
                 Cut the glossary's Adoption entry to its meaning

                 adoption.md's opening, its steps and its bulk-import section state
                 every step the entry listed, including the import nodes' kind.

                 Node: graph-workflow/374

RETROSPECTIVE
1. What I had to hunt for: nothing much. Finding node 360's and 370's lines in decisions.md took one targeted grep.
2. What arrived that this node did not need: most of map.md and map-implementation-rules.md (worktree, landing, review-route and trigger-file paragraphs). The full implementation contract's sections on writing new-node conditions also went unused.
3. What would have made this easier: nothing material. The condition quoted the removed sentence and named the sections to check, so the work took one pass.
4. What was stale, wrong or contradictory: nothing found. map.md's glossary count ("58 term entries and 45 `_Avoid_` lines") is dated and marked non-authoritative. This edit does not change either count.
````
