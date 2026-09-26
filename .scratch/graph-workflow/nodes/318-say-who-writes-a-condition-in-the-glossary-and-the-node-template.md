# Say who writes a condition in the glossary and the node-file template

Type: implementation
Status: resolved
Supersedes: 55
Blocked by: 302

## Question

Two places still say an acceptance condition is written by the node that spawned it, without the case where the manager minted the node. `CONTEXT.md`'s `**Acceptance condition**:` entry reads "What done means for one implementation node, written by the node that spawned it, before any work". The node-file template's code block in `.claude/skills/expedition/graph-conventions.md` reads "`## Acceptance condition     <- implementation only; written by the spawning node`". Make both agree with `.claude/skills/expedition/SKILL.md`'s `## Acceptance conditions`: "Where an agent minted the node, that agent wrote the condition before any work on the node started, and you file it. Where you minted the node, you write the condition."

*Manager's note: minted by the manager to replace [node 55](55-who-writes-a-condition-with-no-spawning-node.md), on the human's "ok for supersede". Blocked by node 302, which rewrites `CONTEXT.md`.*

## Acceptance condition

*Written by the manager, which minted this node. Every demand in it is fixed by `expedition/SKILL.md`'s `## Acceptance conditions` as landed at `e64b3de`, or by the state of the files.*

1. `CONTEXT.md`'s entry headed `**Acceptance condition**:` no longer says without qualification that a condition is written by the node that spawned it. It says that where an agent minted the node, that agent writes the condition, and that where the manager minted the node, the manager writes it. Its `_Avoid_` line is unchanged, and no other glossary entry is edited.
2. In `.claude/skills/expedition/graph-conventions.md`, the node-file template's annotation on the `## Acceptance condition` line no longer says only "written by the spawning node". It still says the section is for implementation nodes only, and it states or points at the same two cases as clause 1.
3. No other text in either file changes, and no other path changes.
4. The working tree meets the bar.

## The manager's reading of this condition, 2026-09-25

*The manager's own note.* Read back against the two rules that bind every condition. **Self-contained:** every demand is written out, and the rule the two places must agree with is quoted in `## Question`. Nothing sends the checker to the record. **No demand over the record:** every clause is about the two files and the tree.

## Answer

The glossary's acceptance-condition entry and the node-file template now say the agent that created a node writes its condition, or the manager where the manager created it.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The human approved. The work landed as commit `3529bec`. The node the worker surfaced is [node 325](325-say-who-writes-a-condition-in-the-implementation-contracts-words-list.md).

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted. The flag is raised under `## Flags` at the gate.*

HANDOVER:      Say who writes a condition in the glossary and the node-file template

ANSWER:        Both places now state who writes the condition in the two cases that `expedition/SKILL.md`'s `## Acceptance conditions` gives.

               - `CONTEXT.md`, the `**Acceptance condition**:` entry. The first sentence now reads "What done means for one implementation node, written before any work starts." The unchanged sentence "Its worker leaves it as written, and may not rewrite it." follows it. Two new sentences come next: "Where an agent created the node, that agent writes the condition. Where the manager created the node, the manager writes it." The rest of the entry and its `_Avoid_` line are unchanged. Only the lines the change touched were rewrapped.
               - `.claude/skills/expedition/graph-conventions.md`, the node-file template under `## The node file`. The annotation now reads "`## Acceptance condition     <- implementation only; written by the agent or manager that created the node`". The alignment of the `<-` column is kept. The line is 105 columns, one more than the file's previous longest line, and it is inside a code fence.

               Choices a later reader would otherwise have to work out again:
               - I wrote "created" rather than SKILL.md's "minted". "Mint" is not a term defined in `CONTEXT.md` and is a figure of speech, and standing writing rule 5 asks for plain words. I kept "an agent" so the wording matches clause 1 and SKILL.md.
               - The two new sentences come after "Its worker leaves it as written…" rather than before it. Placed before it, "Its worker" would directly follow "the manager writes it", and "Its" could then be read as the manager's worker.
               - I kept "before any work starts" word for word, so the only text changed is the who-writes wording that clauses 1 and 2 demand.

               The repo has no build, no tests, no formatter and no CI. `map-implementation-rules.md` records the same, and I found no manifest or task runner that says otherwise. The bar here is therefore its non-command half. I checked the new text against the `_Avoid_` lines: "created", "agent" and "writes" are refused by none. I also checked it against standing writing rule 5: one idea per sentence, one clear referent for each pronoun, and no undefined coined term.

               Re-pointing search, run from the repo root:
               - `python3 .scratch/graph-workflow/scripts/search-conditions.py 318 ed4ed20:CONTEXT.md .scratch/graph-workflow/worktrees/318-who-writes-a-condition/CONTEXT.md --phrases $TMPDIR/p318.txt`
               - The same command for `.claude/skills/expedition/graph-conventions.md`.
               - The phrases file held: "written by the node that spawned it", "written by the spawning node", "the node that spawned it", "the spawning node", "written by the node that spawned".
               - Both runs printed `# Gone items: 0 (quotes 0, n-gram runs 0, protected headings 0)` and no phrase hits. The node-81 n-gram runs on `CONTEXT.md` all appear as KEPT, so the expected false result did not show up as gone.
               - I also grepped every open or claimed node file for "spawned it", "spawning node", "who writes a/the condition" and "written by the node". None of the hits is in an open condition that quotes the removed text:
                 - node 13 is resolved; the grep matched the `Status: open | …` line in its template;
                 - node 32's hits are in an annotation that records history;
                 - node 79's hit is a link to node 55 in its `## Question`, and its condition does not quote the template.
               - No replacement clause or supersede proposal is owed.
               - Node 307's condition says "No other entry in `CONTEXT.md` changes". That clause is about 307's own diff, and I did not touch the `**Checker**:` entry, so the two nodes do not conflict.

INDEX LINE:    The glossary's acceptance-condition entry and the node-file template now say the agent that created a node writes its condition, or the manager where the manager created it.

FLAGS:         ASSUMPTION: I wrote "created" where `expedition/SKILL.md` and this node's condition say "minted". "Mint" is not defined in `CONTEXT.md` and is a figure of speech, and standing writing rule 5 asks for plain words. The meaning is the same, and the human may prefer the shipped term for consistency with SKILL.md. I made no exchange with the human; I made the two edits, ran the search, and settled this myself.
               Index sentence: At node 318 the worker wrote "created" rather than SKILL.md's undefined "minted" for who writes a condition, as plain English.

NEW NODES:     Name: Say who writes a condition in the implementation contract's words list
               Kind: implementation
               Question: `.claude/skills/expedition-implementation/SKILL.md`, under `## Words used exactly`, defines **acceptance condition** as "what done means for your node, written by the node that spawned yours before you started". A node the manager created has no spawning node, and this node, 318, is one. So the definition is false for every manager-created node. The same phrase in the five contracts' `## When a node you report is an implementation node` sections is correct in place, because there the reporting worker's node is the spawning node.
               Blockers: none
               Acceptance condition:
               1. In `.claude/skills/expedition-implementation/SKILL.md`, the `**acceptance condition**` bullet under `## Words used exactly` no longer says without qualification that the condition was written by the node that spawned yours. It says that the agent that created your node wrote the condition, or the manager where the manager created your node, before you started. It still says the worker leaves the condition as written and may not rewrite it.
               2. No other text in that file changes, and no other path changes.
               3. The working tree meets the bar.

INVALIDATIONS: none

GATE PAYLOAD:  No checker findings yet.
               Paths touched, both in the worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/318-who-writes-a-condition`:
               - `CONTEXT.md`
               - `.claude/skills/expedition/graph-conventions.md`
               The only file written outside the worktree is the scratch phrases file `$TMPDIR/p318.txt`.
               Proposed commit message:
                 Say who writes a condition in the glossary and the node-file template

                 Node: graph-workflow/318

RETROSPECTIVE:
(1) What I had to hunt for:
    - Whether "mint" is a defined term. I looked in `CONTEXT.md` first, found nothing, then grepped the shipped skills. SKILL.md uses the word four times and never defines it.
    - Whether any open condition quotes the template line. The script answered that, but my first grep for open nodes, `^Status: (open|claimed)`, also matched node 13's template body. Anchoring the pattern with `$` fixed it.
(2) What arrived that this node did not need:
    - Most of `map-implementation-rules.md`: the history paragraphs, the record-as-work rule and the supersede procedure. The bar paragraph and the writing rules were enough.
    - The script's many KEPT lines.
    - A spawn could quote just the bar paragraph and the two rule blocks, and the script could offer a gone-only mode.
(3) What would have made this node easier:
    - Clause 3, "No other text … changes", could say whether rewrapping lines counts as a change. I assumed it does not.
    - The node's `## Question` could have named the implementation contract's own `## Words used exactly` line. It has the same defect and sits outside this node's paths, which I report above as a new node.
(4) What was stale, wrong or contradictory:
    - The spawn warned of a known false n-gram run for node 81 on `CONTEXT.md`. With the current script it shows as KEPT, not gone, so the warning looks stale, perhaps after node 324's change.
    - `expedition-implementation/SKILL.md`'s definition of acceptance condition, "written by the node that spawned yours", contradicts `expedition/SKILL.md`'s `## Acceptance conditions` for manager-created nodes, this node included.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-26. The checker was resumed from node 307's check.*

> PASS
>
> Node 318, "Say who writes a condition in the glossary and the node-file template", meets all four parts of its acceptance condition, and the bar holds. The work is one rewritten passage in the glossary's **Acceptance condition** entry and one changed template line in `graph-conventions.md`, and nothing else changed.
>
> My contract is the main-tree checker contract, unchanged since my last check: its last commit is `76e66e3` and it has no uncommitted edits. The work is in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/318-who-writes-a-condition`, on branch `worktree-318-who-writes-a-condition`, based on `ed4ed20`. I read the changed paths only as the work. No list of rule changes was asked for this node, so none is given.
>
> `CONTEXT.md`'s `_Avoid_` lines are one of the standards this work is held against. The edit does not touch any `_Avoid_` line, so no standard moved.
>
> **Part by part**
> 1. **The glossary entry names both writers: met.**
>    - In `CONTEXT.md`'s `**Acceptance condition**:` entry, "written by the node that spawned it, before any work starts" became "written before any work starts".
>    - Two sentences were added: "Where an agent created the node, that agent writes the condition. Where the manager created the node, the manager writes it." These state the two cases the condition requires. The condition says "minted" and the text says "created", which is the same meaning in plain words.
>    - The entry's `_Avoid_` line, "definition of done, criteria, spec", is unchanged.
>    - No other glossary entry is edited.
> 2. **The template annotation no longer says only "written by the spawning node": met.**
>    - In `graph-conventions.md`'s node-file template, the annotation went from "`<- implementation only; written by the spawning node`" to "`<- implementation only; written by the agent or manager that created the node`".
>    - It still says "implementation only", and it states the same two cases as part 1.
> 3. **No other text or path changes: met.**
>    - `git diff` touches only the Acceptance condition entry in `CONTEXT.md` and the single template line in `graph-conventions.md`.
>    - `git status --porcelain --untracked-files=all` shows only those two files modified.
>    - I searched both files unwrapped for "spawning node", "node that spawned" and "spawned it", and nothing remains.
> 4. **The working tree meets the bar: met**, as below.
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, in the same state as at my last check: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:**
>   - Standing rule 5 (plain English): the new sentences are plain and each states one case.
>   - `CONTEXT.md`'s `_Avoid_` lines: none is changed, and no refused word is introduced.
>   - `graph-conventions.md`, which is itself part of the work.
>   - All five ground rules, which are met.
> - No reviewing skill is named, so I ran none.

### Gate — approve, 2026-09-26

The human, `verbatim`: *"approve"*

## Flags

`318.1` **· settled** `ASSUMPTION` — I wrote "created" where `expedition/SKILL.md` and this node's condition say "minted". "Mint" is not defined in `CONTEXT.md` and is a figure of speech, and standing writing rule 5 asks for plain words. The meaning is the same, and the human may prefer the shipped term for consistency with SKILL.md. I made no exchange with the human; I made the two edits, ran the search, and settled this myself.
