# An implementation worker tests the worktree it was handed before it starts work

Type: implementation
Status: resolved

Blocked by: none

## Answer

Dropped with no edit, per the human: the plain-git worktree route puts every tree inside the already-writable repository, so the silent unwritable-tree case this probe guarded no longer arises.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`, together with its agreement with the drop and its one caveat. No work landed and no gate was held. Its worktree and branch were removed with nothing on them. The node raised no flags.

## Question

*Surfaced by [The manager sees its own writable region](179-the-manager-sees-its-own-writable-region.md)'s worker, and pasted as it wrote it.*

> A worker can be handed a worktree its session cannot write. Node 175 measured exactly that, and the file-editing
> tools keep succeeding throughout, so the failure stays invisible until the worker's first git write — after the
> node's work is done. The manager cannot pre-empt it, the harness cutting the tree at the spawn itself. One shell
> write at the start, by the party that owns the tree, converts a whole node lost at its end into a raise at its start.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 179's worker. Pasted as it wrote it, and not the manager's.*

> `.scratch/graph-workflow/map-implementation-rules.md` gains one bullet, placed in the same list that already holds
> that file's sandbox material, stating all four of the following in the file's own voice:
>
> 1. Before doing any work, an implementation worker writes one throwaway file at the root of the worktree it was
>    given and deletes it — for example `touch <worktree>/.probe && rm <worktree>/.probe`.
> 2. That write is made with a **shell command** and never with a file-editing tool. The file-editing tools succeed in
>    directories where no shell command can write, so a probe made with one detects nothing.
> 3. Where the write fails with `Read-only file system`, the worker has been handed a tree it cannot write. It does no
>    work, and raises immediately, naming the path that failed. It does not retry with the sandbox off and does not
>    work around it.
> 4. The reason, stated so a reader need not be told it elsewhere: a worker's file edits go on appearing to succeed
>    for the whole node, and the first thing that fails is a git write at the end, so an untested tree costs the
>    node's entire work.
>
> The file's existing sandbox bullets are neither deleted nor reworded — new text is added alongside them. No file
> other than `.scratch/graph-workflow/map-implementation-rules.md` changes.

## The manager's note at filing

*Not a change to anything above.*

**This is the half [node 179](179-the-manager-sees-its-own-writable-region.md) explicitly did not close**, and its
worker's own honest caveat: the human's *"no schedule"* settles what the **manager** does, and leaves the silent case
uncaught until this lands.

**Four nodes now queue on `map-implementation-rules.md`** — this one, [node
184](184-the-bar-and-the-standards-are-two-different-lists.md) which is claimed, [node
149](149-state-the-prose-standards-demands-in-the-rules-file.md) and [node
160](160-carry-the-integration-conflict-rule-into-the-map.md). The manager holds that ordering and has written no
edges between them.

## Annotation: the probe produced a false positive on its first use, before this node was claimed

*Filed by the manager from [node 184](184-the-bar-and-the-standards-are-two-different-lists.md)'s retrospective, and
pasted as that worker wrote it. **This bears directly on the acceptance condition above**, which as written would land
an instruction whose first real use was wrong.*

> **the probe instruction produced a false positive.** `touch` on my worktree failed with `Read-only file system`, and
> the tree was fully writable — the same `touch` succeeded with the sandbox off. The cause is that my sandbox's write
> allow-set names node *169's* worktree and not mine, so it was a sandbox denial rather than a property of the tree.
> Followed literally, the instruction would have cost this whole node to a raise on a good tree — the exact failure
> node 175 measured, in the opposite direction. **The probe must be run with the sandbox off, or its failure must be
> distinguished from a sandbox denial before it is read as a verdict**; the rules file's own sandbox subsection
> already contains the material to make that distinction.

***The manager's note.*** **The manager carried this instruction into two implementation spawns before it was a
rule**, on the ground that node 175 had measured a worker losing a whole node to an unwritable tree. **It fired
falsely on the first of the two.** Clause 3 of the condition above — *"it does no work, and raises immediately… It
does not retry with the sandbox off"* — is the clause the finding lands on, and it is [node
179](179-the-manager-sees-its-own-writable-region.md)'s worker's text, not the manager's. **The manager has not
amended it**; a condition is not the manager's to rewrite, and this node is not claimed, so the amendment is the
human's or a fresh writer's.

**The manager has stopped carrying the instruction in spawns** until the condition is repaired, which is a change to
what the manager does rather than to anything on disk.

## Annotation: node 188 has landed, and this condition's anchor no longer exists

*Filed by the manager from [node 188](188-move-the-landing-section-out-of-the-workers-file.md)'s worker, in its own
words. Nothing above is changed, and **the condition is not amended** — it was already unrepaired for the reason the
annotation above records, and this adds a second defect rather than replacing the first.*

> **Node 186** (*An implementation worker tests its worktree*) — **its anchor is gone, not its destination.** It
> requires a bullet in `map-implementation-rules.md` *"placed in the same list that already holds that file's
> sandbox material"*, and that *"No file other than `.scratch/graph-workflow/map-implementation-rules.md`
> changes."* After the move there is **no sandbox material left in that file at all** (`grep -in 'sandbox'
> map-implementation-rules.md` returns only the `.worktrees/` mention inside the bar paragraph). The destination is
> still right — node 186's bullet instructs the *worker*, so the admission test puts it in the rules file — but it
> now has no list to join and needs a new anchor.

## Interview

#### Raise 1, relayed 2026-09-28

*Pasted as the worker handed it back. The worker is stopped until the human answers.*

```
RAISE (trigger 1: the acceptance condition is not mine to change, and as written it cannot be met and part of it is already known to be false). I made no edits. The worktree is untouched and the code slot is held.

NODE:          An implementation worker tests the worktree it was handed before it starts work (186)
ABOUT:         Would add one bullet to `.scratch/graph-workflow/map-implementation-rules.md` telling an implementation worker to write-probe its worktree with a shell command before starting, and to raise if the probe fails. I stopped at the manager's "check first" step, before any edit.
SO FAR:        I read the contract, the node file (it has no `## Amendment` section) and the rules file in the worktree. I searched `decisions.md` for the worktree lines. What I found:
               (a) **The anchor is gone.** The condition says the bullet goes "in the same list that already holds that file's sandbox material". `grep -in 'sandbox' map-implementation-rules.md` finds no such list. The file is now prose paragraphs plus one `## What the work is held against` section. The only sandbox mentions are inside the worktree-route paragraph ("need no harness tool call and no sandbox override", and "the removal ... runs with the sandbox off"). Node 188 moved the old sandbox material out, which the node's own second annotation already records.
               (b) **Clause 3 is known to give a false alarm.** Clause 3 says: raise on `Read-only file system` and never retry with the sandbox off. The node's first annotation (from node 184's retrospective) says this probe fired falsely on a writable tree. The cause was that worker's sandbox allow-set naming another node's worktree. So a failed probe can be a sandbox denial and not an unwritable tree, and clause 3 as written tells the worker to throw the node away on a good tree.
               (c) **The premise has partly changed.** The Question rests on "the harness cutting the tree at the spawn itself". Since nodes 265 and 268, the manager cuts the tree with plain `git worktree add` at `.scratch/graph-workflow/worktrees/<NN>-<name>`. The worker "writes that tree by absolute path, calls no tool to reach or leave it ... there is no first act to get wrong". Creating and writing the tree "need no ... sandbox override". The underlying risk still exists (node 175: file-editing tools keep succeeding where the shell cannot write, and the first failure is a git write at the end). The harness-cut case the Question names no longer happens.
               (d) For what it is worth, the probe the condition describes, `touch <worktree>/.probe && rm <worktree>/.probe`, succeeded here with the sandbox on. So this tree is writable and nothing about my own environment is blocking.
               On my own authority I settled only this: I would not repair the condition quietly, and I would not choose an anchor or reword clause 3 myself.
ASK:           How should node 186's acceptance condition be repaired, or should the node be dropped?
RECOMMENDED:   Rewrite the condition and keep the node, because the silent-loss risk node 175 measured is still real under the plain-git route. The rewrite has three parts: (1) anchor the new text right after the paragraph **"An implementation node's worktree is made with plain git, and a worker reaches it by path."** in `map-implementation-rules.md`, as a new paragraph and not a bullet in a list; (2) keep clauses 1, 2 and 4 as they stand; (3) replace clause 3 with: "Where the shell write fails with `Read-only file system`, the worker reruns the same probe once with the sandbox off. If it then succeeds, the failure was a sandbox denial and not a property of the tree: the worker carries on and flags it, naming the path. If it fails again, the tree is unwritable: the worker does no work and raises immediately, naming the path." Also change "No file other than ... changes" so it allows nothing beyond that same file. This rests on annotation 1's measured false alarm, on node 188's removal of the old anchor, and on the route text now in force.
ALTERNATIVES:  - Drop node 186 on the grounds that the plain-git route ("no first act to get wrong") removed the case it guards. I set this aside because the route text says nothing about a worker's allow-set failing to cover its tree, which is exactly the failure node 184 hit.
               - Keep clause 3 as written and only change the anchor. I set this aside because it would land a rule whose only real use so far was wrong.
               - Put the probe in the manager's spawn rather than in the worker's rules file. I set this aside because the harness gives the manager no view of the worker's sandbox region (node 179), and the manager has already stopped carrying the instruction.

Notes for the manager: I did not append to `map-history.md`. No files were touched.

RETROSPECTIVE
1. What I had to hunt for: only whether an `## Amendment` existed and whether the rules file still held any sandbox list. One grep answered each.
2. What arrived that this node did not need: the reading list's `decisions.md` worktree lines were mostly struck history (nodes 150 and 243). Only the node 265, 277 and 281 lines mattered.
3. What would have made this easier: the node already carried two annotations saying the condition is broken and unamended. The spawn could have said "this node's condition is known defective (see its two annotations); confirm and raise, or claim it only once amended". Better still, the condition could have been repaired before the node was claimed.
4. What was stale, wrong or contradictory: the condition's anchor (gone since node 188), its clause 3 (a known false alarm, annotation 1), and the Question's "harness cutting the tree at the spawn" (superseded by node 265's plain-git route).
```

*The manager's note:* the node's two annotations already said its condition was broken and unamended; the manager claimed it without reading them. That is the manager's defect, and the same one as nodes 226 and 236.

#### The human's answer to raise 1, 2026-09-28 — a divergence

The human, `verbatim`: *"I kinda feel like the way the worktree work now, there are no issues anymore no ? I would say maybe drop the node ? Do say if you disagree"*. **This is a divergence**: the worker recommended "Rewrite the condition and keep the node"; the human's answer takes the alternative the worker set aside, "Drop node 186 on the grounds that the plain-git route ("no first act to get wrong") removed the case it guards."

*The manager's note:* the human asked the manager to say if it disagreed. The manager answered that it agrees, on context it already held: every worktree this session was cut with plain `git worktree add` inside the repository, every worker wrote its tree with no failure, node 186's own probe succeeded with the sandbox on, and node 184's false alarm came from a sandbox naming another node's worktree under the old route. The manager relays the human's answer with no further word from itself.

## Handover, attempt 1

*Pasted as the worker handed it back.*

````
HANDOVER:      An implementation worker tests the worktree it was handed before it starts work
ANSWER:        Dropped with no edit, per the human. The node guarded against a worker being handed a worktree its shell cannot write while its file-editing tools keep succeeding, so the loss shows up only at the node's closing git write (measured at node 175). Both measured cases came from routes that no longer exist: a harness-cut tree (node 175), and a sandbox allow-set naming a different harness worktree, which made the probe fire falsely on a writable tree (node 184's retrospective). Under the plain-git route of nodes 265 and 268, the tree is at `.scratch/graph-workflow/worktrees/<NN>-<name>`, inside the repository directory the session can already write. There the case does not come up, and a shell `touch`/`rm` probe on node 186's own tree succeeded with the sandbox on. The condition was also unmeetable as written: its anchor, a list of sandbox material in `map-implementation-rules.md`, had been removed by node 188, and its clause 3 had already given a false alarm. Reopen only if a worktree route again puts the tree outside the repository directory.
INDEX LINE:    Dropped with no edit, per the human: the plain-git worktree route puts every tree inside the already-writable repository, so the silent unwritable-tree case this probe guarded no longer arises.
FLAGS:         none
NEW NODES:     none
INVALIDATIONS: none
CONDITIONS:    Searched the open nodes' conditions and questions for `probe`, `Read-only file system` and `tests the worktree`. Neither the conditions nor the questions depend on node 186, and dropping it changes no open node's question.
MISSING FROM MAP: none
GATE PAYLOAD:  Nothing found by a checker (none ran). Paths touched: none. No commit, because nothing lands; the manager removes worktree `.scratch/graph-workflow/worktrees/186-worktree-tests` and branch `worktree-186-worktree-tests`.

RETROSPECTIVE
1. What I had to hunt for: only whether an `## Amendment` existed and whether the rules file still held any sandbox list. One grep answered each.
2. What arrived that this node did not need: most of the `decisions.md` worktree lines were struck history (nodes 150 and 243). Only the node 265, 277 and 281 lines mattered.
3. What would have made this easier: the node already had two annotations saying its condition was broken. Checking whether the plain-git route had made the node unnecessary before claiming it would have saved the spawn.
4. What was stale, wrong or contradictory: the condition's anchor (gone since node 188), its clause 3 (a known false alarm), and the Question's premise that the harness cuts the tree at spawn (superseded by node 265).
````
