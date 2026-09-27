# The cascade's per-candidate agent does not join a defect to an open node

Type: implementation
Status: resolved
Blocked by: none

## Question

The cascade contract that landed as `c64a0e3` has its per-candidate agent report a new node for every departure it finds. It carries no rule that a defect in the same file and on the same concern as an open node joins that node. The five worker contracts carry that rule, since node 327. A cascade-found defect would therefore be minted as a new node, against the effort's standing rule that a related defect goes into a node that already exists.

*Reported by [node 272](272-the-cascades-open-node-half-is-parked-on-a-ground-that-turns-out-to-be-false.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Acceptance condition

*Authored by node 272's worker and filed by the manager.*

> `.claude/skills/expedition-cascade/SKILL.md` is changed. Scope came from no search: the named file is the work.
> After this work:
> - (a) The per-candidate role tells the agent this: before reporting a node, search the open nodes' `## Acceptance condition` sections for the path the defect is in, and read only what matches. Where the defect concerns the same file and the same concern as an open implementation node, name that node and give the clauses to add to its acceptance condition, instead of reporting a new node.
> - (b) The per-candidate handover's shape has a place for that joined node and its clauses.
> - (c) Those clauses are held to the same points the file already states for a condition under `### The acceptance condition you write`.
> - (d) No file under `.scratch/` is changed.
> - (e) Every heading in the file, as listed by `grep -n '^#\{1,6\} '` before the work, is still present afterwards, in the same order.

## Answer

The cascade's per-candidate agent now searches open nodes' acceptance conditions for a departure's path, and joins a same-file, same-concern departure to that node as clauses instead of reporting a new node.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `4c7f6a7`. Flags 351.1, 351.2 settle at the node closing report.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      The cascade's per-candidate agent does not join a defect to an open node

ANSWER:        `.claude/skills/expedition-cascade/SKILL.md` now gives the per-candidate role the join rule that node 327 shipped in the five worker contracts. There are three changes.
               (1) Under `## Per-candidate` / `### What you are given`, a new paragraph says the agent is also given the place that holds the effort's node files. It says those files are record rather than product code, and that the agent reads them only to search them. This is how the agent reaches the open nodes' `## Acceptance condition` sections. The spawn points at the files, so the contract names no path and no command (ground rules 1 and 2). Reading the node files is consistent with hard rule 2 (write no file). The code-slot rule is untouched: it governs product code only. When a slot is occupied, the agent hands back nothing but `CANNOT JUDGE`, so it never reaches the join search.
               (2) Under `### What you do`, a new paragraph sets out the rule. Before reporting a node, the agent searches the open nodes' `## Acceptance condition` sections for the path the departure is in, and reads only what matches. It searches only the node files the spawn points at and reads nothing else of the record. An open node is one that has not been resolved, superseded or put out of scope, whether or not a worker holds it. This matches the manager contract's "claimed or not" and the status values `open` and `claimed`. Where the departure concerns the same file and the same concern as an open implementation node, the agent joins it to that node instead of reporting a new node. It names the node and gives the clauses to add, written to the five points under `### The acceptance condition you write`. The manager adds the clauses where nobody holds the node, and files them as a new node where somebody does. This last sentence copies the five contracts' own wording. The existing sentence that pointed at "the block" now says "the first block".
               (3) Under `### What you hand back`, the `NEW NODES` line now reads "in one of the two shapes under `### A node you report`". A second block shape is added under that heading: `JOINS:` (number and name of the open implementation node), `DEPARTURE:` (the departure the clauses repair) and `CLAUSES:` (written to `### The acceptance condition you write`).
               The search is stated as a property, and the file still names no `git` command. No heading was added, removed or reordered. Every line is within 105 columns.

INDEX LINE:    The cascade's per-candidate agent now searches open nodes' acceptance conditions for a departure's path, and joins a same-file, same-concern departure to that node as clauses instead of reporting a new node.

FLAGS:         ASSUMPTION: The acceptance condition says "defect", but the cascade contract calls the thing a per-candidate agent finds a "departure" throughout (`DEPARTURES`, "repair the departure"). I kept "departure" in the new text so the file uses one word for one thing, and did not bring in "defect" beside it.
               Index sentence: The cascade contract's join rule says "departure", not the five contracts' "defect", to keep the file's own word for what a per-candidate agent finds.
               ASSUMPTION: The acceptance condition does not say how the agent reaches the open nodes. I made it an input: the spawn gives the place holding the node files. The agent then searches those files and reads only what matches. The alternative was to have the manager paste every open node's condition into the spawn, which would put that cost on the manager's side. This choice means the manager's cascade spawn must carry that location. No manager-side text describes the cascade spawn today: a search for "cascade" under `.claude/skills/expedition/` returns nothing, so there was nothing to change there.
               Index sentence: The cascade per-candidate agent reaches open nodes' conditions by searching the node files its spawn points at, so the cascade spawn must carry their location.

NEW NODES:     none

INVALIDATIONS: This extends node 327: its join rule now reaches the cascade contract as well as the five worker contracts. It extends the landed cascade contract (`c64a0e3`) with a new input and a second report shape. It contradicts nothing.

CONDITIONS:    I searched the `## Acceptance condition` sections of every open or claimed node file under `.scratch/graph-workflow/nodes/` for `expedition-cascade` and `per-candidate`. The only match was node 351 itself. No replacement clauses.

MISSING FROM MAP: `map.md` does not say where the cascade's spawn is described on the manager's side, or whether it is described at all. I searched `.claude/skills/expedition/` for "cascade" and found nothing. I went on by making the node-file location an input the per-candidate agent is given, stated in the cascade contract alone.

GATE PAYLOAD:  Checker findings: none yet.
               Bar: the rules file records that the repo has no build, no tests, no formatter and no CI. Confirmed: the repo has no manifest or task runner. So the bar is the non-command half: the standards, the ground rules, the five writing rules, the `CONTEXT.md` `_Avoid_` lines, `graph-conventions.md`, `/writing-for-agents` and the acceptance condition.
               Checks run:
               - (e) headings: I captured the `grep -n '^#\{1,6\} '` output before editing and compared the heading text afterwards. Identical and in the same order; only line numbers moved.
               - Line width: no line is over 105 columns.
               - `git status` in the worktree shows only `.claude/skills/expedition-cascade/SKILL.md` modified, so nothing under `.scratch/` changed (d).
               - No `git` command appears in the file.
               - I checked the new text by hand against the `_Avoid_` lines: none of the refused words are used.
               Paths touched: `.claude/skills/expedition-cascade/SKILL.md`, in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/351-join`. I also wrote a scratch heading list to `$TMPDIR/h351-before.txt`, which is outside the repo.
               Proposed commit message:
                 Join a cascade-found departure to an open node

                 The per-candidate agent searches the open nodes' acceptance conditions
                 for the path a departure is in. It joins a same-file, same-concern
                 departure to that implementation node as clauses, instead of reporting
                 a new node.

                 Node: graph-workflow/351

RETROSPECTIVE
1. What I had to hunt for: whether any manager-side text describes the cascade spawn. There is none, so nothing tells the manager to pass the node-file location. I also had to find the effort's meaning of "open node" (claimed or not, from the manager contract's related-defect passage) and the status values (in `graph-conventions.md`).
2. What arrived that this node did not need: most of `map.md`'s standing preferences, and the rules file's paragraphs on worktree removal and on record files as the work.
3. What would have made this easier: the spawn or node saying whether the manager's cascade spawn text exists anywhere, or is still to be written. The acceptance condition naming the word to use ("defect" or "departure") would have removed one flag.
4. What was stale, wrong or contradictory: the acceptance condition says "defect", but the file it changes says "departure". Nothing else was wrong. The manager's notes matched the file on disk.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 347's check; the condition reached it as a verbatim copy in `$TMPDIR/c351.md`.*

> PASS
>
> This is the check of node 351, "The cascade's per-candidate agent does not join a defect to an open node". The work is the uncommitted diff to `.claude/skills/expedition-cascade/SKILL.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/351-join`, on base 4b538be. I read the whole condition in `/tmp/claude-1000/c351.md`.
>
> **Parts of the condition**
>
> - **Scope (the named file is the work, and no search was used):** met. `git status --short --untracked-files=all` shows only `M .claude/skills/expedition-cascade/SKILL.md`.
> - **(a):** met. `### What you do` under `## Per-candidate` gains this text: "Before you report a node, search the open nodes' `## Acceptance condition` sections for the path the departure is in, and read only what matches. … Where the departure concerns the same file and the same concern as an open implementation node, join it to that node instead of reporting a new node. Name that node and give the clauses to add to its acceptance condition". `### What you are given` also gains the place holding the node files, marked as the record, and read only to search it.
> - **(b):** met. `### A node you report` gains a second block, "For a departure that joins an open implementation node". Its fields are `JOINS:`, `DEPARTURE:` and `CLAUSES:`. The `NEW NODES:` line of the handover now reads "in one of the two shapes under `### A node you report`".
> - **(c):** met. The added text says "Write those clauses to the five points under `### The acceptance condition you write`". The `CLAUSES:` field repeats that.
> - **(d):** met. No `.scratch/` path appears in the status.
> - **(e):** met. `diff` of `grep '^#\{1,6\} '` at HEAD against the working file prints nothing. Every heading is present, in the same order.
>
> **The bar**
>
> - The repo has no build, tests, formatter or CI, so there are no commands to run.
> - `git diff --check` is clean (exit 0).
> - No added line exceeds 105 characters, and there is no trailing whitespace.
> - No `git` command was reintroduced: `grep -nE '`git [a-z]'` finds nothing.
>
> **Standards:** as in my earlier checks, I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`.
>
> - These bore on the work, and I found nothing against them:
>   - Ground rules 1–3. The contract still stands alone, names no tool, and reaches the human only through the manager.
>   - `CONTEXT.md`'s `_Avoid_` lines.
>   - The writing rules. Citations are by heading, and there is no added bold.
>   - `/writing-for-agents`.
> - The added text also agrees with the five worker contracts' rule on joining a related defect, and with the manager contract's rule for filing one.
> - `/coding-principles` and `/naming` did not bear on the work.
> - No reviewing skill is named, so I ran none.
>
> NOT COVERED:
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The condition covers `.scratch/`, and the worktree shows no change there. What the main tree's record holds is outside what I was given.

### Gate — approve, `standing yes`, 2026-09-27

Taken under the standing yes recorded in `map.md`'s `## Notes` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and its one NOT COVERED item is the worker's bookkeeping. This settles none of the node's flags; they settle at the node closing report.

## Flags

`351.1` `ASSUMPTION` **· settled** — The acceptance condition says "defect", but the cascade contract calls the thing a per-candidate agent finds a "departure" throughout (`DEPARTURES`, "repair the departure"). I kept "departure" in the new text so the file uses one word for one thing, and did not bring in "defect" beside it. — The cascade contract's join rule says "departure", not the five contracts' "defect", to keep the file's own word for what a per-candidate agent finds.

`351.2` `ASSUMPTION` **· settled** — The acceptance condition does not say how the agent reaches the open nodes. I made it an input: the spawn gives the place holding the node files. The agent then searches those files and reads only what matches. The alternative was to have the manager paste every open node's condition into the spawn, which would put that cost on the manager's side. This choice means the manager's cascade spawn must carry that location. No manager-side text describes the cascade spawn today: a search for "cascade" under `.claude/skills/expedition/` returns nothing, so there was nothing to change there. — The cascade per-candidate agent reaches open nodes' conditions by searching the node files its spawn points at, so the cascade spawn must carry their location.

*The manager's note, 2026-09-27:* flags 351.1, 351.2 settle at the node closing report that closes this node, which names its gate as taken under the standing yes.
