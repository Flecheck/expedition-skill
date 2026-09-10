# Put the manager's trigger-duties where a compaction re-injects them

Type: implementation
Status: claimed

Blocked by: none

## Question

*Minted by the manager from [node 217](217-whether-a-hook-can-hold-the-managers-standing-duties.md)'s answer, which
the human's own question asked for.*

The manager has missed three standing duties that fire at moments nothing marks — filing a retrospective, putting a
banked payload in front of the human, and topping up a slot when a node finishes. The human asked whether a hook
can keep the effort's instructions in front of it. **Node 217 established that it can, badly, and that a file on
disk does it better**: a `SessionStart` hook with the `compact` matcher injects text once per compaction and the
text is then lost to the next one, while an instruction file is re-read from disk each time context is rebuilt.
**This repository has neither** — no instruction file at its root, no `.claude/rules/`.

What is open is what that file holds. **Not the map**: the map is 33 KB and its whole point is that a worker reads
it once per node. What belongs here is the short list of the manager's **triggers** — the moments at which a duty
fires — pointing at the map for everything else.

## Acceptance condition

*The manager's own, this node having been minted by the manager rather than by an agent. Marked as the manager's,
and read back against the two rules that bind every condition: it is self-contained text, and it quantifies over no
part of the record — every demand below names a file, a heading or a string.*

> ~~The work is one new file at the repository root, `CLAUDE.md`, and no other file may be edited.~~ **The work is
> one new file, `.claude/rules/expedition-triggers.md`, and no other file may be edited** — amended by the manager
> on the human's answer, below. The worker may not mark this node, resolve it, or write a line in `decisions.md` or
> `flags.md`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. ~~`CLAUDE.md` exists at the repository root and~~ **`.claude/rules/expedition-triggers.md` exists and** is **at
>    most 2,000 bytes**.
> 2. It states each of the following as a trigger — the moment, then the duty — and nothing else as a duty:
>    (a) a node resolves, so its retrospective is filed in the same edit that writes its answer;
>    (b) a node finishes, so the frontier is looked at and a replacement is started before anything else continues;
>    (c) an agent hands back a payload for the human, so it goes in front of them as soon as nothing else is;
>    (d) a landing is not a question, so it never occupies the one channel the human has.
> 3. It names the effort's map by path as where every other rule lives, and states that this file holds triggers
>    only and overrides nothing there.
> 4. **It is written to be safe for every agent in this repository to read, a checker included.** It contains no
>    account of what happened — no node number, no flag id, no count of attempts, no story of a failure, no name of
>    any effort — and every line in it is a standing constraint true of any node's work. A line that would tell a
>    checker something about a particular piece of work fails this clause.
> 5. It states that it is one harness's mechanism and this effort's own practice, and that nothing the workflow
>    ships may assume it exists.
> 6. ~~No file under `.claude/` and no file under `.scratch/` is modified, and no hook is configured anywhere.~~
>    **No file under `.claude/` other than the one named above is created or modified**, no file under `.scratch/` is
>    modified, and **no hook is configured** — amended by the manager on the human's answer, below, which put the
>    file inside `.claude/` and parked the hook rather than refusing it.
> 7. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Clause 4 is the one that could go wrong invisibly, and it is why this node is not simply a copy of the map's
manager section.** A file at the repository root is read by **every** agent this workflow spawns in this repo, and
one of them is a checker that is deliberately blind to the effort's record. So this file is governed by exactly the
test [node 42](42-checker-spawn-carries-ground-rules.md) shipped for what may travel to a blind checker: a standing
constraint true of any node's work, never an account of what happened. **The manager's triggers pass that test; the
manager's failures do not.**

**Clause 6 refuses the hook.** Node 217's answer establishes that a hook's injection is lost at the next
compaction, so the hook buys a worse version of what the file gives for nothing, and configuring one would also put
harness configuration in a repository whose ground rule 1 refuses toolchain assumptions in anything shipped. A
later node may add one; this one does not.

**What this cannot repair.** Two of the three duties are decisions the manager makes at a moment, not facts it
lacks — a file in front of it does not make it act. [Node 212](212-the-mint-on-second-report-rule-is-defeated.md)'s
`Q3.` answer repairs the retrospective by removing the separate later act altogether, which is the stronger shape,
and this node is the weaker mechanism applied to the two duties that have no such shape yet.

## Held: clause 6 rests on a finding now under challenge

*Filed by the manager. **Do not claim this node until this is lifted.***

Clause 6 refuses to configure any hook, and its ground is [node
217](217-whether-a-hook-can-hold-the-managers-standing-duties.md)'s finding that `PreCompact` cannot inject context
and that a `SessionStart` injection is lost to the next compaction. **The human has contradicted the first half**,
`verbatim`: *"It seems that PreCompact works for the hook"*. Node 217's worker is resumed to establish it.

**If `PreCompact` can inject text that reaches the rebuilt context, clause 6 is wrong and this condition is the
manager's to revise before the node is worked** — it is the manager's own condition, so revising it costs nothing
but must happen before a worker holds it, not after.

## Interview

### Attempt 0 — the manager's own question, and the human's reply

*No worker has held this node. The question was the manager's, on the hold above, and the reply is written here at
the moment they spoke.*

**The manager asked** whether to settle `PreCompact` by observation — configuring a hook that echoes one marker, so
the next compaction answers it — or to drop the question and take node 217's established route, a file on disk
re-read every time context is rebuilt, revising clause 6 to permit a hook without requiring one.

**Their reply, `verbatim`.**

> We can try with the rules

**Recorded as ambiguous by the manager, and not resolved by it.** It takes neither option as offered, and *the
rules* has two live referents in this effort's own recent exchanges:

- **`.claude/rules/`**, the directory node 217's answer names alongside a root `CLAUDE.md` as what
  `InstructionsLoaded`'s `compact` matcher fires on — a mechanism that reloads without a hook being configured, and
  which **this repository does not have**. On that reading the reply changes this node's destination file and drops
  the hook.
- **the map's rules**, their own phrase from the exchange that produced node 217 — *"is there a way of adding a hook
  to keep the map instructions ?"* — where *the rules* means the three duties this node is about. On that reading
  the reply takes the experiment.

**Which matters, because the two readings pull this node's condition in opposite directions**, and both clauses they
reach are the manager's own: clause 1 names `CLAUDE.md` **at the repository root**, and clause 6 forbids modifying
**any file under `.claude/`** — which `.claude/rules/` is. The manager has amended neither and asked which.

### The answer, and what it amended

**Their reply, `verbatim`.**

> .claude/rules , we postpone PreCompact if the rules don't work

**Which reading it took: the first.** *The rules* is `.claude/rules/`, the directory, and not the map's rules. It
also settles the second half without being asked: `PreCompact` is **deferred against a condition** rather than
dropped — it comes back if the directory mechanism does not hold the instructions across a compaction.

**A vocabulary note, and it is the manager's rather than a correction of theirs.** `CONTEXT.md` refuses *postpone*
by name; this effort's word for a deferral is **park**. Their word is recorded above as they wrote it, and the
record uses `park` beside it.

**What the manager amended, both clauses being its own and no worker holding this node.** Marked in place above
rather than rewritten silently, on [node 160](160-carry-the-integration-conflict-rule-into-the-map.md)'s precedent
for an amended clause.

- **The scope line and clause 1**: the file moves from `CLAUDE.md` at the repository root to
  `.claude/rules/expedition-triggers.md`. The 2,000-byte cap is unchanged.
- **Clause 6**: it forbade modifying any file under `.claude/`, which is now where the work goes. It now forbids
  every file under `.claude/` **other than the one the scope line names**, keeps `.scratch/` closed, and keeps the
  hook out — but as a park rather than a refusal.

**Three clauses the amendment does not touch, and one of them matters more now than it did.** Clauses 2, 3 and 5
stand as written. **Clause 4 matters more**: it demands the file be safe for every agent in this repository to read,
a checker included, and a file under `.claude/rules/` is loaded into an agent's context by the harness rather than
by a spawn the manager controls — so the manager cannot choose who sees it. The clause was written for that risk at
a root `CLAUDE.md` and it reaches this destination unchanged.

**What the manager will observe rather than assert.** Whether the directory mechanism holds is checkable from the
manager's own context after the next compaction: if the file's text is present without anything having read it
aloud, the mechanism works. **The manager reports what it sees rather than judging it**, and the human's condition —
*"if the rules don't work"* — is what decides whether `PreCompact` comes back. No node is minted for the fallback
yet, the observation not having happened.

## The hold is lifted

*Filed by the manager. **This node may be claimed.***

The hold said `do not claim until clause 6's ground is settled`. It is settled by the human's own direction rather
than by establishing the `PreCompact` fact: the route is now `.claude/rules/`, which needs no hook, so **clause 6 no
longer rests on the contested finding at all.** The `PreCompact` question stays open and unowned — parked against
the condition the human set — and nothing in this node turns on it.

**It is not claimed yet for a different reason: both code slots are full**, held by nodes 223 and 224, each at its
gate with a live worktree. This node is on the frontier and takes the first slot that frees.
