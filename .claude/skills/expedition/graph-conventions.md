# Graph conventions

This document says how an effort's graph is written and changed. Read it before touching any of an
effort's files.

Terms are used exactly as the glossary (`CONTEXT.md`) defines them.

If a repo's tracker doc already documents a different local-markdown scheme, see
`wayfinder-divergences.md`.

The manager is the only writer of the graph's record. It writes as a scribe. A worker returns text. The
manager pastes each part of it under the right heading without re-authoring, shortening, re-ordering or
re-rendering it. Anything of the manager's own goes beside that text as its own marked note.

A worker whose node's own work is a change to a graph file makes that change itself, as it would any
other work. The recording stays the manager's: the answer, the status, the `decisions.md` line, the
flags, and every procedure below.

No edit deletes. When a graph file changes, strike through or mark in place the text that no longer
holds, and add the new text around it. Remove text from a file only when it is wrong or the human asks
for it gone. The never-delete rule covers only the graph's own files, listed under `## The seven files`
below. Edit the product the effort changes, and every file the effort ships, plainly: remove superseded
wording, and move nothing to a history file.

Inside the graph's files, what happens to superseded text depends on the text's job, whichever file
holds it. Text that records what happened, such as a node's `## Answer`, a line in `decisions.md` or an
entry in `flags.md`, is marked superseded in place and never removed. Text that states a rule that
currently binds is replaced by its current form, with its superseded text appended verbatim to
`map-history.md`. `map-history.md` holds superseded text only, and is never rewritten. `map.md` is
written this way, and so is every sibling of it that states rules that currently bind.
`## Writing the map` below describes how.

## The seven files

```
.scratch/<effort>/
  map.md                 The whole effort at low resolution. Read once per session.
  map-history.md         The account behind the map's lines. Read for history, not to work a node.
  map-manager-only.md    The part of the map only the manager acts on. No worker reads it.
  map-implementation-rules.md  The rules an implementation node's work is held to.
  decisions.md           One capped line per resolved node. Append-only.
  flags.md               One capped line per flag, with its state. Append-only.
  nodes/NN-<name>.md     One file per node. All detail.
```

`map-manager-only.md` and `map-implementation-rules.md` are part of the map. A rule written in either
binds exactly as one written in `map.md` does.

Among what `map-manager-only.md` holds are three of the map's sections:

- `## Not yet specified` — the fog.
- `## Out of scope` — one line per node ruled beyond the destination, and one per area consciously ruled
  out.
- `## Landing an implementation node's work` — the landing policy: where a node's worker works, and what
  happens to that work between the gate and the repository. Landing is the manager's, so neither a
  worker nor its checker reads this section.

`map-implementation-rules.md` holds the bar's commands and the standards an implementation node's work
is held against. Its readers are that node's worker and its checker, rather than every worker. What the
file admits is under `## Writing the map` below.

`map.md` has three sections, in this order:

- `## Destination` — what reaching the end of the effort looks like.
- `## Notes` — the domain, the skills every session consults, and the standing preferences for this
  effort. The manager also maintains two things here: the declared label vocabulary, and the bar's
  commands once they have been discovered for this repo. Two further blocks are optional prose, written
  where the effort has them. The first is the effort's ground rules. The second declares, by path and
  glob, which sources are authoritative, which are evidence only, and which hold statements known to be
  false. Absent any declaration, every source a worker is pointed at is authoritative.
- `## Decisions so far` — a pointer to `decisions.md`. The section holds no decision.

`decisions.md` holds one line per resolved node: one sentence of about 25 words, enough to judge
relevance and never a restatement. The lines are grouped under the declared labels where a vocabulary
exists, and flat where it does not.

`flags.md` is the graph's capped index of every judgement an agent made on its own. It holds one line
per flag, one sentence long. Whoever holds the context writes that line as a report when the flag is
raised. Nobody reconstructs it later. The closing report's outstanding flags are the unchecked lines of
`flags.md`. The line's form:

```
- [ ] NN.k ASSUMPTION · [<node name>](nodes/NN-<name>.md) — <one line>
```

Every flag carries an id, `NN.k`, made of its node's number and then a sequence number within that node,
allocated in write order and never reused. In `flags.md` the id sits between the checkbox and the
marker. On the node's `## Flags` entry it sits in front of the marker.

`- [ ]` means outstanding. `- [x]` means the human has dealt with the flag, which does not mean they
agreed with it. The node holds the same state, marking a settled flag `settled`, so the node and
`flags.md` can disagree. Where they disagree, `flags.md` wins, because the sweep and the closing report
are built from it. The flag's node is the first link on the line. The text after the dash may contain
other links.

## Writing the map

This section covers `map.md` and every sibling of it that states rules that currently bind, including a
file the map later splits into, from the day it is written. The graph's other files record what
happened: `decisions.md`, `flags.md`, the node files, and `map-history.md`, which holds superseded text
only. Superseded text in those files stays where it is.

Each file of the map declares its reader: one kind of worker, or the manager alone. The file admits a
line only where that reader would do something differently for having read it while working a node.
Whoever is already editing a passage applies that test to that passage. The test requires no sweep of a
file, and permits none. How a rule was learned fails the test: how many attempts it took and what they
cost, who was wrong, and what the file said before. Move that material to `map-history.md`, and leave in
its place the markdown link to the node that shaped the line. A trigger is part of a rule and stays. A
trigger is an error string, a symptom, or the condition under which a rule fires.

Every note, standing preference and fog item in `map.md` is a current statement: it says what holds now.
It cites by markdown link the nodes that shaped it, without restating what those nodes hold. The account
behind an item is how it came to say what it says, what was measured, and what it used to say. That
account belongs in `map-history.md`, under a heading mirroring the map section the item came from. So a
map file is rewritten as it changes, rather than grown by appending. The text that replaces an item
stands alone. Every worker reads all of `map.md` once per node, so its size is a cost paid once per
node.

Moving the superseded text out deletes nothing. Text moved to `map-history.md` is moved verbatim,
without summarising, paraphrasing or shortening it. Text already struck through moves struck through. An
item carrying no account beyond its current statement moves nothing.

Each item in `## Notes` targets 500 bytes, counting the item's own prose and not any quotation of the
human's own words. The target never forces text out: an item that needs more exceeds it and says why. No
check below treats a breach as a defect. To bring an item down to the target, use the `Change the map`
procedure below.

## Adding a node

Allocate the next unused `NN`. A node keeps its number forever. A number is never reused.

`NN` is the node's identity. The name is free-form. It carries a foreign label when the effort was
adopted from a tracker that had one. For example, a node imported as `AUTH-2` is named
`nodes/24-auth-2-token-refresh.md`. The foreign label resolves to the node by glob.

Create the file with its mandatory fields and its `## Question`. When you create several nodes at once,
write every file first, then fill in `Blocked by:` in a second pass.

## The node file

Fields are bare `Key: value` lines. They live only in the header block, which is everything above the
first `##` heading.

The name, `Type:` and `Status:` are mandatory. Every other field appears only when it has a value. Write
the fields in the order shown below.

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

Sections appear in the order shown, and only when they have content.

### `## Acceptance condition`

The condition states what done means for this implementation node. It is written by the node that
spawned this node, before any work starts. Its worker may not rewrite it. A worker that judges the
condition wrong raises it.

A condition is self-contained text. Everything needed to judge whether the work is done is in the
condition, so its reader never goes anywhere else to find out what it demands. That reader is the
checker, which is handed the condition as text and has not read the node.

So the condition states what must be true, in its own words. A path may say where: the work must touch
that file, produce it, or leave it in a stated state. The demand itself stays in the text, and never
behind a pointer such as *as decided at node NN*. Where a condition depends on material held elsewhere,
whoever writes the condition copies that material into it. The bar is the one thing a condition need not
copy, and only because the bar reaches the checker by its own route.

A demand about the record as a whole belongs on the handover and in no condition, whatever its wording.
Such a demand holds the work against every decision the effort has recorded: that the work contradicts
none of them, or that everything in it traces back to one. Every worker returns `INVALIDATIONS` on its
handover instead, naming which resolved node its work contradicts and how. A demand about what changed
in the tree, such as *no file under `.scratch/` changes*, is permitted.

The manager hands a condition that points anyway to the checker as written, and supplies nothing it
omits. Where the missing part is what the check depends on, the condition goes to the human instead. The
manager raises such a condition where it meets one before the check. The checker raises one it cannot
check.

Four parties may change a condition after it is written:

- The condition's own worker, which may not rewrite it and raises instead, as above.
- The party that established a fact which falsified a clause of an unclaimed node's condition, because a
  node resolved or work landed. That party writes the replacement as text on its handover. The manager
  files it. Two provisos apply. Every word of the replacement is already fixed by a resolved node, by
  work landed in the tree, by the glossary or by the shipped files. The amendment names which of these
  fixed it.
- The manager, under the same two provisos, where no such party exists. Separately, the manager may
  extend a condition's scope to further instances of a defect the condition already describes, provided
  the amendment writes no requirement that was not already fixed.
- The human, who receives everything else.

The last three change only a condition on a node nobody holds yet. A condition under a live worker
reaches the human by that worker's raise, and by no other route.

An amendment only transcribes words already fixed elsewhere. Writing a whole condition for a node that
an agent created is a different act. That act is not the manager's.

An amendment by the party that established the fact, or by the manager, can reach none of the following
three things:

- A new demand at any place.
- An ambiguous demand at a place the condition already lists. While the ambiguity is open, the worker
  decides it and flags it, or raises it. Once a resolved node has settled the ambiguity, the clause can
  be amended to that node's reading.
- A defect the condition does not describe. Reaching one takes a new node, whatever file the defect
  lives in.

Before handing back, the party that established a fact must search for the conditions that fact
falsifies. It searches the open nodes' `## Acceptance condition` sections for what its own work fixes:
each word it refuses, each path it changes or moves something out of, and each phrase it supersedes. It
reads only what matches. Where no such party exists, the manager searches. The search covers every open
node's condition, claimed or not. What to do about a claimed node stays the manager's, under the raise
above. The party names on its handover what it searched for.

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
gate at the latest, the gate being the last point at which the human can act on it rather than the
point at which the node resolves.

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
- `superseded` — replaced **or made unnecessary** by other nodes. Does not satisfy an edge.
- `out-of-scope` — ruled beyond the destination. Does not satisfy an edge. Carries no `## Answer`.

There is no status for a parked node, a node under check, or a node carrying flags. A **parked** node
is `open` with a non-empty `## Interview`.

## Edges

Three kinds, and `Blocked by:` is the only ordering truth.

- `Blocked by: NN, NN` on the dependent. Satisfied only by `resolved`.
- `Superseded by: NN, NN` on the old node. Mandatory the moment it becomes `superseded`.
- `Supersedes: NN[, NN]` on the replacement — the number of every node it supersedes. Where one node
  is superseded by several replacements, each carries that node's number; where one replacement
  retires several nodes, it carries all of theirs.

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
4. `map-history.md`: where the answer has made a fog item specifiable, so that it now exists as its
   own node instead, append that item's text there verbatim.
5. `map-manager-only.md`: remove that item from `## Not yet specified`. The text moves rather than
   being struck in place, step 4 having already appended it verbatim.

The answer is written before the status changes.

### Supersede

Use when the node is no longer the place its work happens — because another node replaces it, or
because another node's answer or landing means it no longer needs doing. A node whose question merely
changed, and which is `open`, unclaimed and holds no work, still needs to exist and is updated in
place instead, with the old wording marked.

1. `nodes/MM-<name>.md`: the replacement node or nodes — created now, or an existing node named as
   the replacement — each carrying `NN` in its `Supersedes:`.
2. `nodes/NN-<name>.md`: mark the superseded text in place.
3. `nodes/NN-<name>.md`: add `Superseded by: MM[, MM]`, then set `Status: superseded`.
4. Every node listing `NN` in `Blocked by:`: replace `NN` with the replacement's number. Where there
   are several replacements, list all of them.
5. `decisions.md`: strike through the old node's line in place. A node that never resolved has no
   line there to strike, and nothing is written there for it. Each replacement gets its own line when
   it resolves.

The replacements exist before the old node is marked `superseded`: what must exist is the replacement
**node**, and its own work need not have landed.

### Rule out of scope

1. `nodes/NN-<name>.md`: set `Status: out-of-scope`.
2. `map-manager-only.md`: append one line to `## Out of scope` — the gist, why it is out of scope, and
   a link to the node.

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

**The norm is settling a node's flags at the first human moment its close reaches** — an
implementation node's gate where it has one, and otherwise the **pick report** that closes it — while
the work is still there and judging one is cheap. No kind of node is exempt. The pick report awaits no
answer, so the settlement rides whatever the human says next, and the manager never settles a flag on
its own judgement or on the passage of time.

The closing report is the exception path rather than the ordinary destination, and it carries two
populations: flags raised before this practice existed, on nodes already resolved; and flags whose
pick report the human never answered, because they never spoke again.

A flag the human turns into a node is settled the same way; the node itself is created by the ordinary
add-a-node step.

### Change the map

Use when a note, a standing preference or a fog item in `map.md` no longer says what holds, or when a
rule in a sibling of it that states rules that currently bind no longer holds. A new item is written
straight into that file and changes nothing else.

1. `map-history.md`: append that item's existing text, verbatim, under the heading mirroring the map
   section it came from. Struck-through text stays struck through.
2. `map.md`, or the sibling the item came from: replace it with the item's new current statement,
   citing by markdown link the nodes that shaped it.

The account is written before the item is changed, so a run that dies leaves it banked rather than
lost. See `## Writing the map` above for why a map file carries the statement and not the account.

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
10. Every item in the map's `## Notes` over the 500-byte target of `## Writing the map` above, with its
    size, counting the item's own prose and not any quotation of the human's own words. **This one
    reports and never fails.** A target is not a threshold: an item over it is a number to look at, and
    the check exists so that the map's growth is seen rather than caught. It is the one check here whose
    output is a list rather than a verdict, and an empty list is not what it is for.
