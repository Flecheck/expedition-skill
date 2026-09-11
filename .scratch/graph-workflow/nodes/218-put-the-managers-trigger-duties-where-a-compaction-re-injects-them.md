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

## Flags

*The worker's own text, pasted. The ids are the manager's bookkeeping and nothing else. Outstanding — this node has
not reached its gate.*

`218.1` `ASSUMPTION` — **The effort's map is named by path as `.scratch/<effort>/map.md` rather than by this
effort's literal path.** Clause 3 requires the map named by path and clause 4 forbids naming any effort; an effort's
name is its own directory's, so the literal path cannot satisfy both. Settled on `CONTEXT.md`'s **Effort** entry,
which states that an effort's files live in `.scratch/<effort>/` — so the placeholder is this repo's authoritative
notation for an effort path and not a workaround — and on the fact that a checker already reads `CONTEXT.md` among
its standards, so this form discloses nothing new to it while the literal path would hand every checker the
record's location. Not raised because neither clause is left unsatisfied: the departure is from a strict reading of
"by path" that the glossary itself does not use.

`218.2` `ASSUMPTION` — **One sentence was added that the acceptance condition did not ask for**, scoping the four
duties to a manager: *"Every duty here is a manager's own, and a worker reading them acts on none of them."* The
file is loaded by the harness into every agent in this repository, so the trigger about something going in front of
the human, read cold by a worker, is an instruction to address the human — which ground rule 3 forbids anything in
the files from giving. Settled on that ground rule, and on the reading that naming whose the duties are scopes them
rather than adding another, so the condition's "nothing else as a duty" is not breached.

### The manager's note beside these flags

*Not a change to either.*

**Flag `218.1` is the collision the manager warned this node's worker about, and the manager was wrong about who
could resolve it.** The spawn said that if clause 3 and clause 4 could not both be satisfied it was the manager's to
repair and the worker should raise. The worker did not need to: it found that `CONTEXT.md` — a file the manager did
not think of as a source of notation — already fixes how this repo writes an effort's path. **The collision was
real and the repo had already solved it.** Its retrospective says the fact *"arrived by accident"*, reached only
because `CONTEXT.md` was on its vocabulary list, and that nothing anywhere points a worker at it for a path
convention.

## Review

### Checker run 1 — `PASS`

*Pasted as the checker wrote it. Every sentence is the checker's. It handed back **no `NOT COVERED` and no
question**. Its first attempt died on a session limit before establishing anything and was resumed rather than
replaced; this is that run's outcome.*

> **How I established each part of the amended condition.**
>
> - *Scope preamble — one new file, no other file edited; no marking, resolving, or line in `decisions.md`/`flags.md`.* `git status --untracked-files=all --ignored --porcelain` in the worktree returns exactly one line, `?? .claude/rules/expedition-triggers.md`, and nothing ignored. `git diff --stat HEAD` is empty, so no tracked file is modified. Decisively: `find . -path ./.git -prune -o -type f -print` differenced against `git ls-files` yields exactly one path, the work itself. `.scratch/` is tracked here (232 of the 243 tracked files sit under it), so `decisions.md`, `flags.md` and the node files are all inside git's view and none moved.
> - *1 — exists, at most 2,000 bytes.* `wc -c` gives **1057**.
> - *2 — the four triggers, moment then duty, and nothing else as a duty.* (a), (b) and (d) appear as the condition's own words. (c) appears as "An agent hands something back for the human, so it goes in front of them as soon as nothing else is" — the same moment and the same duty, with *payload* replaced. That replacement keeps the work inside `CONTEXT.md`, whose **Handover** entry refuses `report, return, payload, deliverable` for precisely the thing a worker hands back; clause 2 asks the trigger to be *stated*, not quoted, so the paraphrase satisfies it and avoids the collision. For *nothing else as a duty* I took every remaining sentence one at a time: the heading, "Four moments, each with the one duty it fires", the two sentences under `## Where every other rule lives` (both demanded by clause 3), and the two under `## What this file is` (demanded by clause 5). None states a moment with a duty. The one borderline sentence is "a worker reading them acts on none of them" — I read it as the negative scope of the four already stated rather than a fifth, and it is load-bearing for ground rule 3: without it a worker reading "so it goes in front of them" could take that duty as its own, which ground rule 3 forbids.
> - *3 — names the map by path, triggers only, overrides nothing.* "Every other rule an effort works under is in its map — `.scratch/<effort>/map.md` and the files beside it. **This file holds triggers only, and overrides nothing there.**" The `<effort>` placeholder is the notation `graph-conventions.md` uses for the same layout, and it is what clause 4's ban on naming an effort forces. "The files beside it" is accurate: the implementation-rules file states that it is itself part of the map.
> - *4 — safe for every agent, checker included.* A grep over the **unwrapped** text for `node[ -][0-9]+`, `flag [0-9]`, `graph-workflow`, `attempt`, `expedition` and `[0-9]+` returns nothing at all — the file contains no digit. No effort is named, no failure narrated. I can attest to the clause directly rather than only by search: **the harness injected this file into my own context partway through this check, and it told me nothing whatever about the work under check.** On the clause's first sentence ("every line is a standing constraint") I applied the clause's own gloss — "a line that would tell a checker something about a particular piece of work fails this clause" — because reading the first sentence literally would forbid the mechanism line that clause 5 demands, making the condition self-contradicting.
> - *5 — one harness's mechanism and this effort's own practice.* "That is **one harness's mechanism, and this effort's own practice**: nothing the workflow ships may assume this file exists."
> - *6 — nothing else under `.claude/`, nothing under `.scratch/`, no hook.* Same evidence as the preamble. For the hook: `.claude/` in this tree holds only `rules/` and `skills/`; `.claude/hooks`, `.claude/settings.json`, `.claude/settings.local.json` and `.claude/settings.json.d` all do not exist, and since the tree holds no untracked file besides the work, none was created and then ignored.
> - *7 — the bar.* Below.
>
> **The bar, discovered from the repo rather than taken on trust.** The 243 tracked files are 242 `.md` files plus `.gitignore` — no manifest, no task runner, no CI directory, no formatter config, nothing to invoke. So there is no build, no test suite and no formatter to run, and the bar here is entirely its non-command half. That matches what the implementation-rules file records, so record and repo agree.
>
> **Standards I read, and which bore on the work.** I resolved the implementation-rules file by one listing of `.scratch/` and took the standards from it; I derived no statement of intent about this node from it, and the work under check is not a record file, so its record-as-work rule did not fire. Which bore:
>
> - **`/writing-for-agents`** — the one that bites hardest, since this file is always-loaded and so "earns even harder pruning than the body". Three headings, one section each, the four triggers first. No sprawl, no no-ops. On **negation**: three negatives, two of them the condition's own dictated content ((d) and clause 5); the worker's own negative is paired with its positive ahead of it ("Every duty here is a manager's own", *then* "a worker acts on none of them"), which is exactly the pairing the standard prescribes.
> - **`CONTEXT.md`'s `_Avoid_` lines** — checked by hand, not by grep, per the measured trap. The distinctive refusals are all absent. `question` appears, in "A landing is not a question", but it is refused only as a name for the **grilling** node kind; the file uses it in the ordinary sense `CONTEXT.md` itself uses under **Park** and **Raise**. Read positively as well as negatively, the file uses `resolve`, `frontier`, `manager`, `worker`, `effort`, `map` and `landing` in their fixed senses.
> - **`graph-conventions.md`** — its never-delete and map-writing rules reach the graph's seven files only, and it says so ("every file the effort ships [is] edited plainly"); the work is neither, so those rules do not bind it. Its `<effort>` path notation matches the file's.
> - **Ground rules** — 1 holds: the file assumes a harness in one sentence and *declares* that assumption in the next, placing itself outside what the workflow ships. 3 holds, and the added scope sentence is what makes it hold. 4 and 5 hold. 2 is about worker contracts and does not reach this file.
> - **The four standing rules for writing** — 1, 3 and 4 hold plainly. On **rule 2**, its second half ("cites the nodes that shaped it") and clause 4's ban on node numbers cannot both be satisfied here. I did not treat that as a defect: clause 4 states its own reason for overriding the citation half for this one file (it is read by a blind checker, and a node number is exactly what would leak), and the file satisfies rule 2's first half in full. No defect results from complying, so this is not a question under my contract — I record it so the manager knows I met it and how I read it.
> - **`/coding-principles`** — altitude only: the four triggers, the file's whole point, come first; scoping and mechanism follow. One subject per file.
> - **`/naming`** — "Triggers a manager acts on" and `expedition-triggers.md` both round-trip to what the file holds, and claim no property it lacks.
>
> **Reviewing skill.** The standards state that none is named for this repo and that a checker does not go looking for one, so I ran none and delegated nothing.
>
> **Enumerator.** The condition records no search command, so there was none to re-run.
>
> No `NOT COVERED:` parts and no `QUESTIONS:`.

### The manager's note beside this run

*Not a change to anything the checker wrote.*

**One sentence in it is evidence rather than a check, and it is the first direct observation this effort has of the
mechanism the human chose:** *"the harness injected this file into my own context partway through this check."* The
checker was not looking for that and had no reason to say it. **It establishes that the harness loads
`.claude/rules/*.md` into an agent without any spawn or hook carrying it** — which is what node 217's answer could
only infer from the `InstructionsLoaded` event's documented trigger.

**It does not establish the thing the human's condition turns on.** *"If the rules don't work"* is about surviving a
**compaction**, and no compaction happened during that check. That observation is still owed and is the manager's to
make from its own context.
