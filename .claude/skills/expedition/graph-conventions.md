# Graph conventions

How an effort's graph is written and changed. Read this before touching any of an effort's files.

Terms are used exactly as the glossary (`CONTEXT.md`) defines them.

A repo whose tracker doc already documents a different local-markdown scheme: see
`wayfinder-divergences.md`.

**The manager is the graph's only writer, and it writes as a scribe.** A worker returns text; the
manager pastes each part of it under the right heading and never re-authors, shortens, re-orders or
re-renders it. What the manager has of its own goes in beside that text as its own marked note. No
procedure below is ever performed by a worker.

**No edit deletes.** When any graph file changes, text that no longer holds is struck through or
marked in place and the new text is added around it. Text leaves a file only when it is wrong or the
human asks for it gone.

## The five files

```
.scratch/<effort>/
  map.md                 The whole effort at low resolution. Read once per session.
  map-history.md         The account behind the map's lines. Read for history, not to work a node.
  decisions.md           One capped line per resolved node. Append-only.
  flags.md               One capped line per flag, with its state. Append-only.
  nodes/NN-<name>.md     One file per node. All detail.
```

`map-history.md` holds, verbatim, whatever the map has appended in place and no longer needs to
carry: every worker reads the map cold once per node, so the account of how a note reached its
current form moves here while the map keeps the note.

`map.md` has four sections, in this order:

- `## Destination` — what reaching the end of the effort looks like.
- `## Notes` — the domain, the skills every session consults, and standing preferences for this
  effort. Also the two things the manager maintains here: the **declared label vocabulary**, and the
  bar's commands once they have been discovered for this repo. Two further blocks are optional prose,
  written where the effort has them: its **ground rules**, and a **standing over sources** declared by
  path and glob — which sources are authoritative, which are evidence only, and which hold statements
  known to be false. Absent any declaration, every source a worker is pointed at is authoritative.
  Both live here because the map is a pointer every worker already receives.
- `## Not yet specified` — the fog.
- `## Out of scope` — one line per node ruled beyond the destination, and per area consciously ruled
  out.

`decisions.md` holds one line per resolved node: one sentence, about 25 words. Enough to judge
relevance, never a restatement. Grouped under the declared labels where a vocabulary exists, flat
where it does not.

`flags.md` is the graph's **capped index of every judgement an agent made on its own** — the flag
counterpart to `decisions.md`, standing to a node's `## Flags` as `decisions.md` stands to its
`## Answer`. One line per flag, one sentence, written report-shaped at raise time by whoever holds the
context and never reconstructed later. The closing report's outstanding flags are this file's unchecked
lines, and they are readable only because each was written to be read.

The form:

```
- [ ] NN.k ASSUMPTION · [<node name>](nodes/NN-<name>.md) — <one line>
```

Every flag carries an **id**, `NN.k` — its node's number, then a sequence within that node, allocated
in write order and never reused. It sits between the checkbox and the marker here, and in front of the
marker on the node's `## Flags` entry. Without it a flag can only be pointed at by its position in a
list.

`- [ ]` is outstanding; `- [x]` is the human having dealt with the flag, which is not the same as
having agreed with it. The same state is on the node, where a settled flag is marked `settled`, so the
two can genuinely disagree. **Where they disagree `flags.md` wins, because the sweep and the closing
report are built from it.** The flag's node is the **first** link on the line; the text after the dash
may contain others.

## Adding a node

Allocate the next unused `NN`. Numbers are never reused, and a node keeps its number forever.

`NN` is the node's identity. The name is free-form, and carries a foreign label when the effort was
adopted from a tracker that had one: a node imported as `AUTH-2` is named
`nodes/24-auth-2-token-refresh.md`, and the foreign label resolves to the node by glob.

Create the file with its mandatory fields and its `## Question`. When several nodes are created at
once, write every file first and wire `Blocked by:` in a second pass.

## The node file

Fields are bare `Key: value` lines. **Fields live in the header block — everything above the first
`##` heading — and nowhere else.**

Mandatory: the name, `Type:`, `Status:`. Every other field appears only when it has a value. Write the
fields in the order shown below.

```markdown
# <free-form name — carries a foreign label when one exists>

Type: grilling | research | prototype | precondition | implementation
Status: open | claimed | resolved | superseded | out-of-scope
Labels: EFF, REG
Blocked by: 31, 47
Supersedes: 12
Superseded by: 88

## Question
## Acceptance condition     <- implementation only; written by the spawning node
## Answer                   <- appended on resolution
## Flags
## Review
## Interview
```

Sections appear in that order and only when they have content.

### `## Acceptance condition`

What done means for this implementation node. Written by the node that spawned it, before any work
starts, and its worker may not rewrite it. A worker that judges the condition wrong **raises** rather
than shipping quietly past it, because a broken condition is not the worker's to fix. The
`CONDITION-WRONG` flag is the manager's to file afterwards, and only where the human's answer was
*carry on, ship it anyway*.

**A condition is self-contained text.** Everything needed to judge whether the work is done is in the
condition, and its reader never goes anywhere else to find out what it demands. That reader is the
**checker**: it is handed the condition as text and has not read the node, so a condition pointing at
something it was not given cannot be checked at all — and the manager, supplying what the condition
left out, becomes the author of the standard the work is judged against.

So the condition states **what must be true** in its own words. A **path** may say where — the work must
touch that file, produce it, or leave it in a stated state — because the checker has the repo. What may
never sit outside the text is the demand itself: *as decided at node NN*, *the section agreed in the
interview*, *the wording the human chose* — each sends its reader away to learn what is being required
of them. Where a condition genuinely depends on material held elsewhere, whoever writes one **copies
that material into it**. The bar is the one thing it need not copy, and only because that reaches the
checker by its own route.

**One demand no copy repairs: the record as a whole.** A condition may not hold the work against every
decision the effort has recorded — that the work contradicts none of them, or that everything in it
traces back to one. Copying reaches a demand that **names** material held elsewhere; it cannot reach one
that **quantifies over the record**, where there is no bounded material to bring inside the text and
what there is grows every time a node resolves. Any wording of that shape is the same demand — *no
decision on any resolved node changes*, *every rule here traces to a resolved node*, *the work is
consistent with every decision so far* — and each leaves its reader no standard to hold the work
against. A demand about **what changed in the tree** is a different thing and stays permitted: *no file
under `.scratch/` changes* is answerable from the diff, whatever those files decided.

**The duty behind it is real, and it is owed on the handover instead.** Every worker returns
`INVALIDATIONS` — which resolved node its work contradicts, and how — answered by the party that built
the work and may read the record to see what it touches. The checker is in neither position: it holds
the condition as text, has not read the node, and does not read the record at all. So the demand belongs
on the handover and in no condition.

**A condition that points anyway is not repaired on the way to the checker.** The manager hands it over
as written and supplies nothing it omits. Where what is missing is what the check turns on, it goes to
the human instead — raised by the manager where it meets one before the check, or by the checker on a
condition it cannot check.

### `## Flags`

One entry per flag, free prose, each prefixed with the flag's id and then one of three markers:

- `ASSUMPTION` — the worker decided a small ambiguity itself.
- `CONDITION-WRONG` — the manager's, filed after a worker raised its acceptance condition as wrong and
  the human answered *ship it anyway*.
- `DELEGATED` — the human said "you decide" and the worker answered.

A flag the human has confirmed is marked `settled` here as well as checked in `flags.md`, so a reader
of the node can tell which of its judgements are still live without opening a second file:

```
`NN.k` **· settled** `ASSUMPTION` — <the judgement, in the worker's own prose>
```

The word is `settled` rather than `resolved`: a node resolves, a flag settles. No checkbox here — the
checkbox is `flags.md`'s.

### The human's words, in either log

`## Interview` and `## Review` are the two sections that hold them, and these rules cover both.

**Ordering: the graph is written the moment the human speaks.** Their answer goes into its section at
relay time. Resuming a worker is a background send and does not block, so the manager issues the resume
and the write in one turn rather than one after the other. What the ordering protects is that the answer
reaches disk before the worker can return, so a worker that dies still leaves the human's words banked.

Every recorded answer carries one of two markers, `verbatim` or `paraphrase`. **The manager pastes the
reply as they wrote it, however terse, and marks it `verbatim`.** *"ok for recommended"* is a complete
answer and is recorded as one. Where the reply takes an option or an outcome it was offered, that option
is quoted in the same entry and attributed to whoever wrote it — usually the worker — because the reply
is unreadable without it and it is not the human's prose.

**Nothing is rendered, so nothing on either log is marked `paraphrase`** unless the manager genuinely
could not avoid rendering it. Copying is the manager's cheapest act and it yields `verbatim` every
time, which is what stops the marker from needing a judgement.

Where a terse reply does not make clear which option it points at, the manager records the reply and
asks which.

### `## Review`

Everything that happened after the code was written, appended per round; rounds accumulate in this one
node. Three things, and nothing beyond them:

1. **the checker's chronology, one entry per run.** A run either names `PASS`, or names `FAIL` and
   which of the two it failed — the acceptance condition or the bar — or **raised instead of judging**,
   in which case it issued no verdict at all and the entry says what it raised. A run may additionally
   name a part of the acceptance condition it did **not cover**, and its entry then carries that part
   and, later, who established it — below.
2. **each correction round, numbered**, with the human's words verbatim and what the worker changed.
3. **the gate's outcome, named as one of approve / correct / reject.** A reject also records what
   implementing the node surfaced, and which of the three routes the node then took: `out-of-scope`,
   `superseded` by a replacement, or back to `open` behind a new `Blocked by:` edge.

**A part a run did not cover.** A checker's `PASS` or `FAIL` may name a part of the acceptance condition
its outcome does not reach: a part it could not establish, because establishing it needs material the
checker was not given. The run's entry carries those parts under a `NOT COVERED:` label, one item per
part, each quoting the part as the checker wrote it — and the outcome on that entry covers the rest of
the condition and no more. So the entry says both halves — the parts named are what the run left, and the
rest of the condition is what it covered.

The part is still owed, and **establishing it is recorded on that same item**: who established it, and
what they read or ran. Usually that is the manager, which holds the handover the checker does not; it may
instead be the human at the gate reading it themselves, or a later run of the check. It happens by the
gate at the latest, the node resolving there with nothing after it to establish anything.

**Every item opens with its state**, and establishing a part rewrites that opening and nothing else:

```
NOT COVERED:
- OWED — "<the part, as the checker wrote it>"
- ESTABLISHED BY <who> · <what they read or ran> — "<the part, as the checker wrote it>"
```

`OWED` and `ESTABLISHED BY` are the only two openings an item may take, so whether a part has an
establisher is read off the item's first word and never judged from the prose after it. The marker opens
the **item**, so a quote that wraps over several lines cannot carry it away, and one item is one part, so
parts are counted by items and never by sentences. The label stands alone on its own line, so prose that
mentions the words names no part at all. The state is the manager's bookkeeping, as a flag's state is;
the part is the checker's own text, pasted.

**An entry for a run that covered the whole condition carries none of this** — no `NOT COVERED:` label,
no item and no marker, and the entry reads exactly as it did before. A condition whose every demand lands
in a file gives a checker nothing to name here, which is what `## Acceptance condition` above already
asks of one.

Both halves sit on the entry that named the part, rather than being recorded where the establishing
happens, because the part is an obligation left **open** and what a later reader needs is whether it
still is. Recorded where the establishing happens, the record moves with whoever acted — three parties,
each writing somewhere else — so there is no one place to look; and a part nobody ever established writes
nothing anywhere, which is the case the record exists for. Keyed to the entry that named it there is one
place whatever happened, and a part nobody has established is legible there as an item still opening
`OWED`, which is what check 9 below reads. **This is not a fourth thing on the log**: it is entry kind 1
carrying what its run handed back.

### `## Interview`

One block per attempt: the attempt's routing key, then each relayed question and each human answer. An
answer that contradicts the recommendation the worker gave is additionally marked `DIVERGENCE`. A dead
attempt is marked in its own heading.

At most three attempt blocks per node.

## Statuses

- `open` — takeable once unblocked and unclaimed.
- `claimed` — a worker holds it. The claim belongs to the node, not to the worker: a worker that dies
  does not release it. A node whose code is under check is `claimed`.
- `resolved` — carries an `## Answer`. **The only status that satisfies a `Blocked by:` edge.**
- `superseded` — replaced by other nodes. Does not satisfy an edge.
- `out-of-scope` — ruled beyond the destination. Does not satisfy an edge. Carries no `## Answer`.

There is no status for a parked node, a node under check, or a node carrying flags. A **parked** node
is `open` with a non-empty `## Interview`.

## Edges

Three kinds, and `Blocked by:` is the only ordering truth.

- `Blocked by: NN, NN` on the dependent. Satisfied only by `resolved`.
- `Superseded by: NN, NN` on the old node. Mandatory the moment it becomes `superseded`.
- `Supersedes: NN` on the replacement — one number. Where a node is superseded by several, each
  replacement carries the same `Supersedes: NN`.

No edge is inferred from anything else, and no field records which code a node touches.

## Labels

Optional and multi-valued: the family or part a node belongs to — `CLASS`, not `CLASS-1`.

- A node may only use a label declared in the map's `## Notes`.
- Labels are a filter and never structure. No order may be inferred from a label, and a label is
  never a node's identity.
- Absent by default. An effort that declares no vocabulary has no labels on any node.

## Reading the graph

The **frontier** is every node that is `open`, unblocked and unclaimed. Unblocked means every `NN` in
`Blocked by:` is `resolved`. This document fixes no order within the frontier; `Labels:` scopes it to
one area.

A node file's body carries lines in field form, and its fenced blocks carry field lines, status values
and placeholder paths. So two rules bind anything that scans these files:

1. **Read fields only from the header block** — everything above the first `##` heading.
2. **Skip fenced code blocks.**

## Procedures

Each lists every file that changes, in order.

### Claim

1. `nodes/NN-<name>.md`: set `Status: claimed`.

Save before any work starts. An `implementation` node may not be claimed until it has an
`## Acceptance condition`.

### Resolve

1. `nodes/NN-<name>.md`: append the `## Answer`.
2. `nodes/NN-<name>.md`: set `Status: resolved`.
3. `decisions.md`: append one capped line, under the node's label group where a vocabulary exists.
4. `map.md`: remove from `## Not yet specified` any fog the answer has made specifiable, which now
   exists as its own node instead. Mark, never delete.

The answer is written before the status changes.

### Supersede

Use when the node holds work — an answer, an interview, or landed code. A node that is `open`,
unclaimed and holds none of those is updated in place instead, with the old wording marked.

1. `nodes/MM-<name>.md`: create the replacement node or nodes, each carrying `Supersedes: NN`.
2. `nodes/NN-<name>.md`: mark the superseded text in place.
3. `nodes/NN-<name>.md`: add `Superseded by: MM[, MM]`, then set `Status: superseded`.
4. Every node listing `NN` in `Blocked by:`: replace `NN` with the replacement's number. Where there
   are several replacements, list all of them.
5. `decisions.md`: strike through the old node's line in place. Each replacement gets its own line
   when it resolves.

The replacements exist before the old node is marked `superseded`.

### Rule out of scope

1. `nodes/NN-<name>.md`: set `Status: out-of-scope`.
2. `map.md`: append one line to `## Out of scope` — the gist, why it is out of scope, and a link to
   the node.

Nothing is written to `decisions.md`.

Every node that lists `NN` in `Blocked by:` now holds an edge that nothing satisfies. Each one must be
ruled out of scope too, or have its `Blocked by:` corrected. Until then check 1 below reports it and
the frontier stays non-empty.

### Park

1. Instruct the worker to store its progress and stop. It returns the progress and writes nothing.
2. `nodes/NN-<name>.md`: append the returned progress to `## Interview`, under the current attempt.
   Every question already answered, and the human's words verbatim rather than summarized.
3. `nodes/NN-<name>.md`: set `Status: open`.

The progress is written before the status changes. Answers already relayed are already on the node.

### Raise a flag

1. `nodes/NN-<name>.md`: append the flag under `## Flags`, prefixed with its id — the next unused `k`
   for that node — and its marker.
2. `flags.md`: append one unchecked line carrying the same id and marker, and linking the node.

The flag's text is written before its line. Both writes belong to the act of raising the flag and never
to a tidy-up afterwards: a `## Flags` section assembled once does not stay assembled.

The round that raised the flag — an `## Interview` attempt or a `## Review` round — says **what produced
it**, and for a flag written from a worker's own unprompted judgement that means what the worker
actually did, in its words. A one-line summary is enough under `## Flags`; it is not enough in the round
that created it. Where there is no round at all — a `research` node, an AFK `precondition` node — the
`## Flags` entry carries that account itself.

### Settle a flag

1. `flags.md`: change that flag's `- [ ]` to `- [x]`.
2. `nodes/NN-<name>.md`: mark that flag `settled` under `## Flags`.

**The norm is settling a node's flags at the human moment that ends it** — a grilling node's last
answer, an implementation node's gate — while the work is still there and judging one is cheap. The
closing report is the exception path rather than the ordinary destination: it carries the flags that
never had a human moment at all, those raised before this practice existed and those on the kinds of
node that never end in front of the human, `research` and an AFK `precondition`.

A flag the human turns into a node is settled the same way; the node itself is created by the ordinary
add-a-node step.

## Mechanical checks

Every one of these is decidable by reading the files.

1. Every `Blocked by:` target exists, and is not `superseded` or `out-of-scope`.
2. Every `Superseded by:` has a matching `Supersedes:`, both directions present.
3. No `NN` used twice, and no gap that indicates a reused number.
4. Every `Labels:` entry appears in the map's declared vocabulary.
5. Every `resolved` node has an `## Answer` and exactly one line in `decisions.md`.
6. Every `## Flags` entry has a line in `flags.md` carrying the same id, and none the other way — and
   the two agree on state: a flag `- [x]` in `flags.md` is marked `settled` on its node, and one marked
   `settled` on its node is `- [x]`.
7. Every `implementation` node has an `## Acceptance condition` before it is `claimed`.
8. No node has more than three `## Interview` attempt blocks.
9. Every item under a `NOT COVERED:` label in a `## Review` opens with `OWED` or with `ESTABLISHED BY`,
   and no `resolved` node still carries one opening with `OWED`.
