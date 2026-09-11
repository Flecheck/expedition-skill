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
> 4. ~~**It is written to be safe for every agent in this repository to read, a checker included.**~~ **Narrowed on
>    the human's answer: clause 8 below is what keeps the file away from other agents, and this clause now stands on
>    its own second half alone.** It contains no account of what happened — no node number, no flag id, no count of
>    attempts, no story of a failure, no name of any effort — and every line in it is a standing constraint true of
>    any node's work. A line that would tell a checker something about a particular piece of work fails this clause.
>    **This clause holds whether or not clause 8 proves possible.**
> 5. ~~It states that it is one harness's mechanism and this effort's own practice, and that nothing the workflow
>    ships may assume it exists.~~ **Struck on the human's answer**, `verbatim`: *"I don't think the "What this file
>    is" should be here"*. A manager reading that statement acts no differently for having read it, so it is a
>    history in a file of triggers. **The statement is owed by the record instead**, where [node
>    226](226-nothing-in-the-record-says-the-auto-loaded-trigger-file-exists.md)'s clause 1 already demands it. **The
>    finished file states nothing about what it is** — no section of that kind, under any heading.
> 6. ~~No file under `.claude/` and no file under `.scratch/` is modified, and no hook is configured anywhere.~~
>    **No file under `.claude/` other than the one named above is created or modified**, no file under `.scratch/` is
>    modified, and **no hook is configured** — amended by the manager on the human's answer, below, which put the
>    file inside `.claude/` and parked the hook rather than refusing it.
> 7. The working tree meets the bar.
> 8. **Added on the human's answer**, `verbatim`: *"shouldn't we add a path constraint on the manager map, so that
>    the rules are only loaded by the manager when running an expedition ?"* — **The file declares a constraint that
>    keeps the harness from loading it into an agent whose work does not touch an effort's record.** The property is
>    what this clause demands; the mechanism is whatever the harness provides, discovered from the harness rather
>    than assumed, per ground rule 1. The worker establishes what the mechanism is and states in its handover what
>    it read to establish it. **If the harness provides no such mechanism, that is a raise and not a workaround** —
>    do not approximate the constraint by writing the file somewhere the harness does not load, and do not configure
>    a hook, which clause 6 still forbids.

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

### Gate — `correct`, on two points

**The human's words, `verbatim`.**

> shouldn't we add a path constraint on the manager map, so that the rules are only loaded by the manager when running an expedition ? Also I don't think the "What this file is" should be here ?

**Recorded at the moment they spoke, before anything was changed.** Neither point is a `reject` and neither asks
for different triggers; both are about the file's reach and its contents, and **both land on clauses the manager
wrote itself.**

**How the manager reads each, stated so a wrong reading is visible rather than silent.**

- **The path constraint.** The file today is loaded by the harness into **every agent in this repository** — this
  node's own checker observed it arriving in its context mid-check. The human asks whether it can instead be
  constrained to load only for the manager, while an expedition is being run. That is a **new demand**, and it
  removes the pressure that produced clause 4 and flag `218.2`: if a worker and a checker never see the file, the
  file need not be written for them.
- **`## What this file is`.** That section exists because **clause 5 demanded it** — *"It states that it is one
  harness's mechanism and this effort's own practice, and that nothing the workflow ships may assume it exists."*
  The manager reads the objection as the effort's own admission test applied to the manager's own clause: **a
  manager reading that sentence acts no differently for having read it**, so it is a history rather than a trigger,
  and the file the human chose is a file of triggers. The statement is still true and still worth recording — in the
  record, where [node 226](226-nothing-in-the-record-says-the-auto-loaded-trigger-file-exists.md) already demands
  it — rather than in the file.

**What the manager has amended, both clauses being its own.** Marked in place in the condition above.

- **Clause 5 is struck**, and its content is not lost: node 226's clause 1 already requires the record to state that
  the harness loads this file, and node 226's condition is its author's rather than the manager's.
- **A new clause 8 demands the path constraint**, stated as a property rather than as a mechanism — ground rule 1
  prefers what is discovered over what is declared, and the manager has not established what the harness offers.
- **Clause 4 is narrowed rather than dropped.** If clause 8 holds, no checker ever reads the file, so the clause's
  reason is gone — but the manager is keeping its ban on accounts of what happened, because the reason for *that*
  half is the manager's own context rather than a checker's blindness, and because clause 8's mechanism is not yet
  established. **If clause 8 turns out to be impossible, clause 4 is the only thing standing between a blind checker
  and this file.**

**Where the work goes.** Back to its worker for a correction round, then to a fresh check — **the condition itself
changed**, so the shipped rule that the acceptance condition is re-checked only where the correction touches it is
satisfied trivially: it touches it everywhere. Then back to this gate.

### The correction round — what changed, and what the worker read to establish clause 8

*Pasted as the worker wrote it. The manager's own words are marked where they appear.*

**The mechanism, established from two independent sources that agree**, and this is the worker's account of clause
8:

> The first source is **the harness's own binary**. It is a 339 MB compiled executable, and it embeds its own
> strings: `grep -a` reads them, and `grep -a -b -o` gives byte offsets that `tail -c +N | head -c M` turns into
> readable regions. Three findings, each quoted from the binary:
>
> - its own guidance text states *"a `.claude/rules/*.md` file with `paths` frontmatter (or a nested-directory
>   CLAUDE.md) loads only when Claude works with matching files, while LOCAL files are always in context"* — the
>   property clause 8 demands, named as a `paths` frontmatter field;
> - the rules loader filters a directory of rules files with `h.push(...x.filter((I)=>o?I.globs:!I.globs))` under a
>   parameter it calls `conditionalRule`, so a rules file either carries globs and is conditional, or carries none
>   and loads unconditionally. **That is the mechanism in the implementation rather than in prose**, and it is why
>   the constraint is a property of the file itself and needs no hook and no settings change;
> - the load-reason enumeration is `session_start`, `nested_traversal`, `path_glob_match`, `include`, `compact` —
>   `path_glob_match` being the reason a glob-scoped file loads, and `compact` being the reason it loads when a
>   context is rebuilt.
>
> The second source is **the official documentation**, read to confirm the YAML shape rather than the mechanism:
> the field is `paths`, its value is a YAML list of glob strings, every documented example is repository-relative,
> no frontmatter field is required alongside it, and *"rules with `paths:` frontmatter reload as Claude reads files
> they apply to"*.

**The glob and why it is that glob:**

> **The glob is `.scratch/**`, and it is the effort record's location rather than any effort's name.** `CONTEXT.md`'s
> **Effort** entry states that an effort's files live in `.scratch/<effort>/`, so `.scratch/**` is exactly "an
> effort's record", covers every effort this repo hosts, and names none — which is what lets clause 8 and clause 4's
> surviving half both hold. Clause 8's own sharp question resolves here rather than colliding: the constraint is
> expressible one directory level above the segment clause 4 forbids.

**The finding that matters most, and it is the worker contradicting the manager's own framing of the amendment:**

> **Clause 8 narrows the exposure and does not close it, which is why clause 4's surviving half is still
> load-bearing.** `map-implementation-rules.md` establishes that an implementation node's work on this effort may be
> the effort's own record, and that where it is, the checker reads the changed paths it was given as the work. Such
> a checker is working under `.scratch/` and the glob will load this file into it. So the class of agent that
> reaches this file is narrowed from every agent in the repository to agents touching a record, and a blind checker
> remains inside that class whenever the work under check is a record file. The file therefore still carries no
> account of anything.

***The manager's note.*** **The manager told this worker that clause 8 "removes the pressure that produced clause 4
and flag `218.2`". That was wrong, and the worker established why.** A checker whose work under check *is* a record
file sits inside `.scratch/**` and still receives this file — which is not a rare case on this effort but the
ordinary one, three of today's four checks having been on record files. Clause 4's surviving half and the scoping
sentence are both still doing work, and the manager kept clause 4 for a weaker reason than the real one.

**What changed in the file:** the `## What this file is` section removed in full under struck clause 5; the YAML
frontmatter block added under clause 8. *"Nothing else changed. The title, the framing sentence, the four triggers
and the `## Where every other rule lives` section are byte-identical to the version that passed its check."* Size
**1,057 → 812 bytes**, against a cap of 2,000.

## Flags — after the correction round

*The worker's own text, pasted. `218.1` and `218.2` were raised in the first round and are restated here by the
worker; **`218.2`'s ground has changed** and the new ground is recorded rather than the old one being overwritten.
`218.3` is new to this round.*

`218.3` `ASSUMPTION` — **The path constraint is `paths: [".scratch/**"]` and was shipped without the load being
observed.** Clause 8 asks for a property and sends the worker to the harness for the mechanism; the mechanism was
established from the harness binary's own embedded loader and guidance text and confirmed against the official
memory documentation, but no compaction or spawn was put through the finished file to watch it load or decline to
load. Settled on two sources agreeing rather than on observation, because observing it means a fresh agent working
outside `.scratch/`, which is not something this node can arrange from inside its own worktree. The check that would
settle it is the one that already produced evidence for the unconstrained case: a checker working on paths outside
`.scratch/` should no longer find this file in its context.

**`218.2`'s new ground, in the worker's words** — the flag itself is unchanged, the sentence is still kept, and only
what justifies it has moved: *"Its original ground — clause 4's demand that the file be safe for every agent — is
struck. It is kept on a narrower one: a checker or an implementation worker whose work under check is a record file
is inside the `.scratch/**` glob, so trigger (c) still reaches an agent that must not act on it, and ground rule 3
forbids anything in the files from telling an agent to address the human."*

**`218.1` is restated unchanged**, and the worker adds that the frontmatter glob *"had to be written one level above
the same segment for the same reason"* — so the same collision between clause 3 and clause 4 was resolved twice, by
the same `CONTEXT.md` entry, in two different places in the file.

### Checker run 2 — `PASS` on clauses 1–7 and the declaration half of clause 8

*A second, independent checker, spawned fresh against the amended condition and told that the first run's outcome is
not evidence for it. Pasted as it wrote it. Its own closing line: **"My PASS covers clauses 1-7 and the declaration
half of clause 8, and no more."***

> **Scope — one new file and nothing else.** `git status --ignored --untracked-files=all --porcelain` in the worktree returns exactly `?? .claude/rules/expedition-triggers.md`; `git diff HEAD --name-status` is empty. `find .claude -type f` returns that file plus the nine pre-existing `expedition*` skill files, untouched. Nothing in `decisions.md` or `flags.md` moved, and no node file moved — the worktree's whole `.scratch/` tree is tracked and clean.
>
> 1. Exists, and is 812 bytes (`wc -c`) against a 2,000-byte ceiling.
> 2. Four bullets, each written moment-then-duty, matching (a)-(d) one for one. Nothing else in the file is shaped as a trigger. One judgement I am naming rather than burying: the opening line "Every duty here is a manager's own, and a worker reading them acts on none of them" is an attribution of those four duties and not a fifth, so I read it as within "nothing else as a duty".
> 3. "Every other rule an effort works under is in its map — `.scratch/<effort>/map.md` and the files beside it" names the map by path; "This file holds triggers only, and overrides nothing there" is the second half, stated in as many words.
> 4. No account. A grep over the file unwrapped into one line for node references, flag ids, digits, attempt counts, failure words and effort names returns nothing; `<effort>` is a placeholder, not a name. Every line is a standing constraint true of any node's work.
> 5. Nothing in the finished file states what it is — no statement of harness mechanism, of the effort's own practice, or of what the workflow may assume, under any heading or in the frontmatter. I read clause 5 as forbidding statements of the struck kind rather than as contradicting clause 3; under the other reading the condition would be self-contradicting, and my contract forbids me to check work against my own repair of one.
> 6. No other file under `.claude/` and no file under `.scratch/` is created or modified, per the status and diff above. No hook is configured: a search for `settings*.json` over the worktree returns nothing, and the repo has no `.claude/settings.json` at all. The one hook on this machine is in the human's own home directory — a `PreToolUse` Bash gate whose command is a `/nix/store` path, with zero occurrences of `expedition-triggers`. It predates this work and is not configured by it.
> 7. The bar holds, and I discovered its commands from the repo rather than taking the record's copy: the worktree's whole contents are `.claude`, `.gitignore`, `.scratch`, `CONTEXT.md`. A recursive hunt for `package.json`, `Cargo.toml`, `pyproject.toml`, `Makefile`, `justfile`, `*.toml`, `*.yml`, `*.yaml`, `*.cfg`, `flake.nix` returns nothing, and there is no `.github`. No build, no tests, no formatter, no CI — the bar's command half is empty, which is a complete bar and not a deficient one, and it agrees with what the implementation-rules file records. Its non-command half holds:
>    - `CONTEXT.md`'s `_Avoid_` lines, checked by hand rather than by grep, per the measured trap. Two near-misses, both clean. "payload" is refused under **Handover** and the file writes "hands something back" where the condition's own paraphrase said payload. "finished" is refused under **Closed**, for an effort being over; the file writes "A node finishes", and `_Avoid_` under **Resolve** does not list it while `CONTEXT.md` itself writes "when it has finished" of a worker. "landing" is refused only as the compound "landing commit". Every other term — node, resolve, frontier, manager, worker, agent, effort, map, trigger — is used as the glossary and `graph-conventions.md` fix it.
>    - Ground rule 1: the body assumes no repo, machine or toolchain. Ground rule 3: the one trigger that mentions the human makes it a manager's duty to put something in front of them, and tells no spawned agent to address them. Ground rule 4: 812 bytes of plain prose.
>    - The four standing rules for writing: no why-prose to compress and the four shapes stated whole; one heading for the one section beyond the list; no line-number citation, the map cited by path. Standing rule 2's "cites the nodes that shaped it" binds an item of the map, and this is not a map file — the never-delete rule in `graph-conventions.md` draws that same line at the graph's own files — so it does not collide with clause 4's ban on node numbers. I considered handing that back as a question and judged there is no collision to report.
>    - `/writing-for-agents`: no sprawl, no duplication, no no-op line, and the one prohibition is paired with its positive.
> 8. Established in part, and the rest is under `NOT COVERED:` below. What I established: the file's frontmatter is a well-formed YAML block, `paths:` carrying a one-element list `".scratch/**"`, and `paths` is the key the harness itself documents for exactly this property. I read the harness's own memory documentation directly, under "Organize rules with `.claude/rules/`": *"Rules without `paths` frontmatter are loaded at launch with the same priority as `.claude/CLAUDE.md`"*, and under "Path-specific rules": *"Rules can be scoped to specific files using YAML frontmatter with the `paths` field. These conditional rules only apply when Claude is working with files matching the specified patterns"*, and *"Path-scoped rules trigger when Claude reads files matching the pattern, not on every tool use."* The harness on this machine is above every version caveat that page attaches to `paths`. The glob's domain is right: `graph-conventions.md`'s "The seven files" puts every file of an effort's record under `.scratch/<effort>/`, so `.scratch/**` is the record and nothing else. So the declaration is correctly formed, uses the mechanism the harness provides rather than an approximation, and is not a file written somewhere the harness does not load.
>
>    One observation, not a finding, since no stated property is breached: the docs' own table gives `src/**/*` for "all files under a directory" and never shows a bare trailing `**`. **If `.scratch/**` matches more narrowly than intended under whatever glob library the harness uses, the rule loads less often rather than more**, which still satisfies what clause 8 demands.
>
>    The observation the spawn invited: **this file is not in my context. That is not evidence about the gate.** The main repo has no `.claude/rules/` directory at all, my cwd is the main repo rather than the worktree, and I reached the file with `Read` against an absolute worktree path. Its absence is explained by location, so I can draw nothing from it either way.
>
> ```
> NOT COVERED:
> - "The file declares a constraint that keeps the harness from loading it into an agent whose work does not
>   touch an effort's record." I establish the declaration and not the behaviour. Observing that the harness
>   withholds this file would mean launching harness sessions against the worktree with and without a
>   `.scratch/` read and inspecting what loaded, which is neither read-only nor something I can do from
>   where I stand. What I hold is the harness's documentation of `paths`, the file's conformance to it, and
>   a running version above every caveat that documentation attaches. Whoever can run the harness against
>   the tree, or read `/context` in a session launched there, is the party that can settle the rest.
> - "The worker establishes what the mechanism is and states in its handover what it read to establish it."
>   The handover is outside the paths I was given, and I was given nothing from the effort's record. I
>   cannot establish what the worker read or what it stated. The manager holds the handover and is the only
>   party that can settle this.
>
> QUESTIONS:
> - A disclosure rather than a question, and it needs no answer. I spawned one helper agent to establish the
>   harness's rules-loading mechanism. It went beyond the documentation and cited the effort's own record by
>   node number. I discarded every record-derived part of what it returned, re-established the mechanism
>   myself by reading the harness documentation directly, and every fact in clause 8 above rests on that
>   direct read. Flagging it because a spawn of mine touched material I am kept blind to, which the manager
>   should know happened even though nothing from it reached my outcome.
> ```

### The two `NOT COVERED` parts — one settled, one still owed

*The checker named for each who could settle it.*

**Settled: what the worker read to establish the mechanism.** The manager holds the handover and it does state it,
at length and with sources: the harness's own compiled binary, read with `grep -a` for its embedded strings, giving
the guidance text naming `paths` frontmatter, the loader's own `conditionalRule` filter, and the load-reason
enumeration including `path_glob_match` and `compact`; and the official memory documentation, read to confirm the
YAML shape rather than the mechanism. **Two independent sources, and the checker reached the second of them by
itself and agrees with it.**

**Still owed: that the harness actually withholds the file.** Nobody has observed it. The checker is right that it
cannot, and right about who can — *"whoever can run the harness against the tree, or read `/context` in a session
launched there"*. **That is the manager, and only after this work lands**, since the file exists solely in an
uncommitted worktree today. **The manager's session works under `.scratch/` continuously, so it is inside the glob
rather than outside it** — what it can observe is the positive case, and the negative one needs an agent working
outside `.scratch/`. This is also exactly what the human's own condition on the mechanism —
*"if the rules don't work"* — leaves to observation, and flag `218.3` is the worker's own disclosure of the same
gap.

### Flag `218.4` — the checker's own disclosure, filed by the manager

*The checker offered it as needing no answer. The manager files it as a flag because it is a judgement an agent made
on its own, and because its subject is the checker contract rather than this work.*

`218.4` `ASSUMPTION` — **A checker's helper agent reached the effort's record, which the checker is kept blind to.**
In the checker's own words: *"I spawned one helper agent to establish the harness's rules-loading mechanism. It went
beyond the documentation and cited the effort's own record by node number. I discarded every record-derived part of
what it returned, re-established the mechanism myself by reading the harness documentation directly, and every fact
in clause 8 above rests on that direct read."* **The blindness held because the checker noticed and repaired it**,
not because anything stopped the helper. The checker disclosed it unprompted and its outcome rests on its own
direct read.
