# An implementation worker tests the worktree it was handed before it starts work

Type: implementation
Status: open

Blocked by: none

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
