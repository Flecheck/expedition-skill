# A related defect joins an open node instead of becoming a new one

Type: implementation
Status: resolved
Blocked by: none

## Question

Workers report every defect they find as its own new node, and nearly every condition fences its node to a few lines ("no other entry changes", "no other path changes"). So the graph fills with nodes that change a few lines each and pay a full spawn, check and gate apiece. The human's instruction, `verbatim`: *"To avoid the issue, maybe we can make so that if it is related, put the defect in an already existing node ?"* Ship that rule into the contracts.

*Minted by the manager from the human's instruction, recorded in the map under `## Notes`.*

## Acceptance condition

*Written by the manager, which minted this node.*

1. In each of the five worker contracts (`.claude/skills/expedition-grilling/SKILL.md`, `expedition-implementation`, `expedition-precondition`, `expedition-prototype` and `expedition-research`), the instructions for the handover's new-nodes part say: where a defect the worker would report concerns the same file and the same concern as an open node the worker found, the worker names that node and gives the clauses to add to its acceptance condition, instead of proposing a new node.
2. `.claude/skills/expedition/SKILL.md` says the manager files such a report as an amendment to the named node's condition when that node is open and unclaimed, and as a new node when it is not.
3. `.claude/skills/expedition/SKILL.md` says the manager may amend the acceptance condition of a node that is open and unclaimed without first asking the human, recording the amendment on the node with a flag of its own that settles at the node's gate, and that the condition of a claimed node stays as written. The human's words behind this clause, `verbatim`: *"I think we shouldn't be too afraid of updating a node before it is started"*.
4. `.claude/skills/expedition/graph-conventions.md` says how the amendment is recorded on the node, or points at the rule it already has for recording an amendment.
5. No other rule in those files changes, and no other path changes.
6. The working tree meets the bar.

## Answer

A worker joins a same-file, same-concern defect to an open implementation node by giving clauses to add to its condition. The manager files them as an amendment or, if the node is held, as a new node, and graph-conventions gains an amendment procedure.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `eef448a`. Flags 327.1 to 327.5 go to the human in the pick report that closes this node.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      A related defect joins an open node instead of becoming a new one

ANSWER:        The rule is now in the shipped files. Seven files changed in the worktree `.scratch/graph-workflow/worktrees/327-related`. Nothing is committed.

- **Five worker contracts** (`.claude/skills/expedition-{grilling,implementation,precondition,prototype,research}/SKILL.md`). The same text went into all five, byte for byte.
  - A new last paragraph in `## When a node you report is an implementation node` says: where a defect the worker would report concerns the same file and the same concern as an open implementation node, the worker joins the defect to that node instead of proposing a new node. It finds such a node by searching the open nodes' `## Acceptance condition` sections for the path the defect is in, reading only what matches. In `NEW NODES` it names that node and gives the clauses to add to its acceptance condition, written "to the same points as a condition". It is also told what the manager does with them.
  - The `NEW NODES:` placeholder in the handover template gains a third line: "for a defect that joins an open node, that node and the clauses to add to its condition".
  - The paragraph says "the same points" rather than "the four points" on purpose. Node 109 will add a fifth point to that section, and a written count would then be wrong.
- **`.claude/skills/expedition/SKILL.md`, `### Changing one after it is written`**
  - Clause 3 was already partly true there. The existing paragraph limited amendments to a node nobody holds yet and said a held node's condition is handed over as written. The five-things list already recorded the amendment on the node and carried it as a flag. I built on that and restated nothing.
  - Added to that paragraph: the worker reporting a related defect is one of the amending parties, and "You make or file each of them without first asking the human."
  - The parties list now reads "Five parties" and gains "A worker that reports a related defect, described below."
  - The cannot-cover list is narrowed. "A new demand" and "A defect the condition does not describe" each gain the exception "except … a related defect, below". The second bullet keeps "Any other defect takes a new node, whatever file the defect is in."
  - A new paragraph defines a related defect: same file and same concern as an open node, named on `NEW NODES` with clauses. The manager files the clauses as an amendment when the node is open and nobody holds it. Otherwise it files them as a new implementation node whose acceptance condition is those clauses, writing the node's name and question itself, marked as its own.
  - Five-things item 4 now reads "It is carried as a flag of its own, which settles at that node's gate under `## Flags`." The lead-in to the list points at the new graph-conventions procedure.
  - The `## What is never yours` row on rewriting an acceptance condition (node 337's wording) now says "the one exception, amending the condition of a node nobody holds yet". Before, it said "the one narrow exception, amending a clause of the condition". An amendment can now add clauses, so the old wording understated it.
  - Kept on purpose: the manager's amendments stay limited to what is already fixed. "Where any part of the replacement needs a judgement nobody has made, it goes to the human" stands unchanged.
- **`.claude/skills/expedition/graph-conventions.md`**
  - It had no rule for recording an amendment, so I added a new procedure, `### Amend an acceptance condition`, placed before `### Raise a flag`. Step 1: mark each replaced clause superseded where it stands, and append the amendment after the condition author's text, marked as its author's, beside the search or fact that justified it. Step 2: raise the amendment's flag by `### Raise a flag`. Step 3: the check step, running check 6 over the flag's entry and its `flags.md` line. Node 339's rule is met, and no other check can be made false by these writes.
  - The `### \`## Acceptance condition\`` description gains one sentence pointing at the procedure.

INDEX LINE:    A worker joins a same-file, same-concern defect to an open implementation node by giving clauses to add to its condition. The manager files them as an amendment or, if the node is held, as a new node, and graph-conventions gains an amendment procedure.

FLAGS:
ASSUMPTION: Clause 5 says "no other rule changes". I still narrowed two bullets of `SKILL.md`'s cannot-cover list ("A new demand", "A defect the condition does not describe … whatever file the defect is in") and changed "Four parties" to "Five". Left as written, those lines contradict clause 2. I read them as part of the rule clauses 2 and 3 demand, not as "other" rules. — Index: Node 327's worker narrowed SKILL.md's "cannot cover" list and its parties count to make room for the related-defect route, reading them as part of the demanded rule rather than as other rules.
ASSUMPTION: I also reworded the `## What is never yours` row from "the one narrow exception, amending a clause of the condition" to "the one exception, amending the condition". An amendment can now add clauses, and the old wording would understate it. — Index: Node 327's worker reworded the never-yours row's exception to "amending the condition", since a related defect adds clauses rather than amending one.
ASSUMPTION: Clause 3 says the manager "may amend … without first asking the human". I kept the existing limit that the manager's own amendments demand only what is fixed, with anything needing a judgement going to the human. The human's words ("not be too afraid of updating a node before it is started") are about asking first, not about the manager deciding things. — Index: Node 327's worker kept the rule that an amendment the manager writes needs no new judgement, reading the human's instruction as dropping the question first and not the manager's limits.
ASSUMPTION: When the named node is no longer open and unclaimed, the manager files the clauses as a new implementation node and writes its name and question itself, marked as its own. The clauses are written to the condition points, so they can stand as that node's condition. I did not ask the worker for a full new-node block as well, because clause 1 says "instead of proposing a new node". — Index: Node 327's worker had the manager write the name and question of a fallback new node itself, the worker supplying only the clauses.
ASSUMPTION: The amendment's flag gets no new marker. The record's amendment flags already use `ASSUMPTION` (for example 81.1, 103.1), and adding a marker would be another rule. — Index: Node 327's worker added no marker for an amendment's flag, the record already carrying such flags as ASSUMPTION.

NEW NODES:     none

INVALIDATIONS:
- [How a condition's scope is amended](nodes/82) and [May an unclaimed node's acceptance condition be amended, and by whom](nodes/252): extension. A third route now exists: a worker's related-defect clauses may add a new demand, and a defect the condition does not describe, to an unclaimed node's condition. Both nodes had forbidden that. Node 252's "the pen is the falsifying party's, else the manager's" gains a third holder: the reporting worker.
- [An acceptance condition is self-contained text](nodes/33): extension. The self-containment points now bind the clauses a worker gives for a related defect, not only whole conditions.
- The decisions line for [node 86](nodes/86) and flag 86.2 ("amending another worker's condition is the defect node 82 exists to fix"), and flags 191.4 and 212.5 (minting rather than amending an open condition): their ground is contradicted for a same-file, same-concern defect from now on.

CONDITIONS:
- Searched every open or claimed node's `## Acceptance condition` (81 nodes) for: "four parties", "whatever file", "does not describe", "carried as a flag", "narrow exception", "amending a clause", "its acceptance condition too", "a new demand", "Changing one after", "When a node you report", "NEW NODES", "Amend an acceptance", "related defect". Nothing matched.
- Then listed the conditions naming `SKILL.md`, `graph-conventions` or "amend": 109, 137, 160, 190, 202, 230, 284, 285, 41, 56, 44, 80, 97, 89. I read the clauses that matched "amend", "NEW NODES", "Acceptance conditions", "Procedures", "worker contract" or "five".
- None is made wrong, so I wrote no replacement.
- Node 109 clause 6 adds a fifth point to the section I appended to. My paragraph deliberately says "the same points" with no count, so it stays true after 109.
- Node 109 clause 5 targets `SKILL.md`'s `## Acceptance conditions` and graph-conventions' `### Acceptance condition`. My changes sit beside what it will add and contradict none of its clauses.

MISSING FROM MAP: none

GATE PAYLOAD:
- Checker findings: none yet (no checker run).
- Bar: the repo states no build, test or format command. The worktree has no manifest, task runner or CI, which matches `map-implementation-rules.md`. So the bar is its non-command half.
  - I confirmed the wrap width stays at 105 in every prose line I added.
  - `git diff --check` is clean.
  - The shared section and the `NEW NODES` template are byte-identical across the five contracts. `expedition-research` differs only because the section ends the file there.
  - The new words were checked against `CONTEXT.md`'s `_Avoid_` lines. "report" appears only as a verb, as the contracts already use it.
  - Method skills: none were invoked, so no part was skipped.
- Paths touched (worktree `.scratch/graph-workflow/worktrees/327-related`, branch `worktree-327-related`):
  - `.claude/skills/expedition-grilling/SKILL.md`
  - `.claude/skills/expedition-implementation/SKILL.md`
  - `.claude/skills/expedition-precondition/SKILL.md`
  - `.claude/skills/expedition-prototype/SKILL.md`
  - `.claude/skills/expedition-research/SKILL.md`
  - `.claude/skills/expedition/SKILL.md`
  - `.claude/skills/expedition/graph-conventions.md`
- Node 137: none of my text touches "pick report" or "closing report". Five-things item 5 still says "pick report" and is unchanged, so 137 can rename it.
- Proposed commit message:

  Let a related defect join an open node's condition instead of minting a new node

  The five worker contracts name an open implementation node and give clauses for a same-file,
  same-concern defect. The manager files them as an amendment to an unclaimed node, or as a new
  node otherwise, without asking the human first. graph-conventions.md gains the procedure that
  records an amendment.

  Node: graph-workflow/327

RETROSPECTIVE
1. What I had to hunt for: which marker an amendment's flag carries. Neither shipped file says, and I found it by grepping `flags.md` for "amend" (ASSUMPTION is the practice). I also had to confirm graph-conventions has no amendment-recording rule, by grepping its headings and "condition".
2. What arrived that this node did not need: nearly all of `map.md` (about 58KB read whole). Only the `## Notes` bullet on grouping by file (the node-327 bullet) bore on this node. Most of `map-implementation-rules.md` is accounts; I used only the "no build, no tests, no formatter" fact and the five writing rules. A narrower decisions grep would have done: my "new node|amend|acceptance condition" pattern pulled in wide lines like node 10's.
3. What would have made this easier: the node's condition could say outright that `SKILL.md`'s "cannot cover" list (new demand, undescribed defect "whatever file the defect is in") has to be narrowed. Without that, clause 5 reads as forbidding exactly that edit. The spawn's note on node 337 was the most useful single item. It would also help if the spawn named the marker convention for an amendment flag.
4. What was stale, wrong or contradictory: clause 5 ("no other rule changes") sits in tension with clauses 2 and 3, which need the "cannot cover" list and the parties count changed. Node 109's condition clause 6 quotes the contracts as saying "against those four", but they now say "against the four points above", so that quote is already stale. The never-yours row's "amending a clause" wording came from node 337 and was made inaccurate by this node.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 342's check; the condition reached it as a verbatim copy in `$TMPDIR/c327.md`.*

> PASS
>
> This is the check of node 327, "A related defect joins an open node instead of becoming a new one". The work is the uncommitted diff in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/327-related`, on base eb3b217. I read the condition in full from `/tmp/claude-1000/c327.md`.
>
> **Clause 1.** Met in all five worker contracts (grilling, implementation, precondition, prototype, research).
> - The `NEW NODES` line of each handover block gains "; for a defect that joins an open node, that node and the clauses to add to its condition".
> - Each contract adds the same paragraph after its section on writing a condition: "Where a defect you would report concerns the same file and the same concern as an open implementation node, join the defect to that node instead of proposing a new node… In `NEW NODES`, name that node and give the clauses to add to its acceptance condition."
> - "Implementation node" narrows "open node" only to the nodes that have an acceptance condition to add clauses to.
>
> **Clause 2.** Met. `### Changing one after it is written` in `SKILL.md` gains: "File those clauses as an amendment to that node's condition when the node is open and nobody holds it. When it is not, file them as a new implementation node whose acceptance condition is those clauses, and write that node's name and question yourself, marked as your own."
>
> **Clause 3.** Met.
> - "The amendments in this section, by the party that established a fact, by a worker reporting a related defect and by you, apply only to a node nobody holds yet. You make or file each of them without first asking the human."
> - "Where a worker already holds the node, its condition is handed over as written" is kept.
> - Item 4 of the five things every amendment carries now reads "It is carried as a flag of its own, which settles at that node's gate under `## Flags`."
>
> **Clause 4.** Met.
> - `graph-conventions.md` gains a procedure, `### Amend an acceptance condition`, under `## Procedures`. Step 1 marks each replaced clause as superseded where it stands and appends the amendment, marked as its author's. Step 2 raises the flag by `### Raise a flag`. Step 3 runs check 6.
> - `` ### `## Acceptance condition` `` points to the new procedure.
> - `SKILL.md`'s list of the five things names the procedure by its heading. Both cited headings exist: `grep -n '^### '` finds them in graph-conventions.md at lines 508 and 521.
>
> **Clause 5.** Met.
> - `git status --short --untracked-files=all` shows exactly the 7 named paths.
> - Every rule the diff touches besides the clauses above is a direct consequence of them:
>   - "Four parties" becomes "Five parties", with the related-defect worker added as the fifth.
>   - The two limits "A new demand…" and "A defect the condition does not describe…" gain a "except a related defect, below" exception. Without it they would forbid what clause 2 demands.
>   - The `## What is never yours` table cell "the one narrow exception, amending a clause of the condition…" becomes "the one exception, amending the condition…", to match.
>   - The workers' paragraph adds how to find the node: search the open nodes' `## Acceptance condition` sections for the defect's path.
>   - The manager writes the name and question of the fallback new node. Clause 2 requires a new node, and the worker supplies only clauses.
> - No other rule's text changes.
> - `grep -noiE 'four parties|narrow exception'` over the skills and `CONTEXT.md` finds no stale wording left behind.
>
> **Clause 6.** Met: see the bar below.
>
> **The bar**
> - The repo has no build, tests, formatter or CI, so there are no commands to run.
> - `git diff --check` is clean (exit 0).
> - The only added line wider than the file's wrap width is the table row. The table's other rows are equally wide.
>
> **Standards.** As in my earlier checks, I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`.
> - `CONTEXT.md` `_Avoid_` lines: checked by hand against the added text. Nothing found.
> - Writing rules: citations are by heading and no bold was added.
> - `/writing-for-agents`: nothing found.
> - Ground rules:
>   - Each worker contract carries the rule in its own text.
>   - Nothing tells a spawned agent to address the human.
>   - Nothing assumes a repo, machine or toolchain.
> - graph-conventions.md: the new procedure ends with a check step that names check 6. That meets the file's own rule that each procedure names the checks its writes can make false, which I held the work against. The new procedure moves no element of that standard.
> - `/coding-principles` and `/naming` did not bear on the work, since it is prose.
> - No reviewing skill is named, so I ran none.
>
> The condition records no search command.
>
> NOT COVERED:
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The condition does not demand this; the rules file makes it a bookkeeping rule. The worktree diff contains no such write, and what the main tree's record holds is outside what I was given.

### Gate — approve, `standing yes`, 2026-09-27

Taken under the standing yes recorded in `map.md`'s `## Notes` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and its one NOT COVERED item is the worker's bookkeeping, which the diff shows was not written. This settles none of the node's flags; they settle at the pick report that closes the node.

## Flags

`327.1` `ASSUMPTION` **· settled** — Clause 5 says "no other rule changes". I still narrowed two bullets of `SKILL.md`'s cannot-cover list ("A new demand", "A defect the condition does not describe … whatever file the defect is in") and changed "Four parties" to "Five". Left as written, those lines contradict clause 2. I read them as part of the rule clauses 2 and 3 demand, not as "other" rules. — Node 327's worker narrowed SKILL.md's "cannot cover" list and its parties count to make room for the related-defect route, reading them as part of the demanded rule rather than as other rules.

`327.2` `ASSUMPTION` **· settled** — I also reworded the `## What is never yours` row from "the one narrow exception, amending a clause of the condition" to "the one exception, amending the condition". An amendment can now add clauses, and the old wording would understate it. — Node 327's worker reworded the never-yours row's exception to "amending the condition", since a related defect adds clauses rather than amending one.

`327.3` `ASSUMPTION` **· settled** — Clause 3 says the manager "may amend … without first asking the human". I kept the existing limit that the manager's own amendments demand only what is fixed, with anything needing a judgement going to the human. The human's words ("not be too afraid of updating a node before it is started") are about asking first, not about the manager deciding things. — Node 327's worker kept the rule that an amendment the manager writes needs no new judgement, reading the human's instruction as dropping the question first and not the manager's limits.

`327.4` `ASSUMPTION` **· settled** — When the named node is no longer open and unclaimed, the manager files the clauses as a new implementation node and writes its name and question itself, marked as its own. The clauses are written to the condition points, so they can stand as that node's condition. I did not ask the worker for a full new-node block as well, because clause 1 says "instead of proposing a new node". — Node 327's worker had the manager write the name and question of a fallback new node itself, the worker supplying only the clauses.

`327.5` `ASSUMPTION` **· settled** — The amendment's flag gets no new marker. The record's amendment flags already use `ASSUMPTION` (for example 81.1, 103.1), and adding a marker would be another rule. — Node 327's worker added no marker for an amendment's flag, the record already carrying such flags as ASSUMPTION.

*The manager's note, 2026-09-27:* flags 327.1 to 327.5 settle at the pick report that closes this node, sent to the human with its gate named as taken under the standing yes.
