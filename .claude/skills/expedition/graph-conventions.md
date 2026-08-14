# Graph conventions

How an effort's graph is written and changed. Read this before touching any of an effort's files.

Terms are used exactly as the glossary (`CONTEXT.md`) defines them.

A repo whose tracker doc already documents a different local-markdown scheme: see
`wayfinder-divergences.md`.

**The manager is the graph's only writer.** A worker returns text; the manager writes it. No procedure
below is ever performed by a worker.

**No edit deletes.** When any graph file changes, text that no longer holds is struck through or
marked in place and the new text is added around it. Text leaves a file only when it is wrong or the
human asks for it gone.

## The four files

```
.scratch/<effort>/
  map.md                 The whole effort at low resolution. Read once per session.
  decisions.md           One capped line per resolved node. Append-only.
  flags.md               One capped line per flag, with its state. Append-only.
  nodes/NN-<name>.md     One file per node. All detail.
```

`map.md` has four sections, in this order:

- `## Destination` — what reaching the end of the effort looks like.
- `## Notes` — the domain, the skills every session consults, and standing preferences for this
  effort. Also the two things the manager maintains here: the **declared label vocabulary**, and the
  bar's commands once they have been discovered for this repo.
- `## Not yet specified` — the fog.
- `## Out of scope` — one line per node ruled beyond the destination, and per area consciously ruled
  out.

`decisions.md` holds one line per resolved node: one sentence, about 25 words. Enough to judge
relevance, never a restatement. Grouped under the declared labels where a vocabulary exists, flat
where it does not.

`flags.md` holds one line per flag, in this form:

```
- [ ] ASSUMPTION · [<node name>](nodes/NN-<name>.md) — <one line>
```

`- [ ]` is outstanding, `- [x]` is settled by the human. **The checkbox lives only in `flags.md`.** The
flag's node is the **first** link on the line; the text after the dash may contain others.

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
starts. Its worker may raise a `CONDITION-WRONG` flag against it and may not rewrite it.

### `## Flags`

One entry per flag, free prose, each prefixed with one of three markers:

- `ASSUMPTION` — the worker decided a small ambiguity itself.
- `CONDITION-WRONG` — the worker judged its acceptance condition wrong.
- `DELEGATED` — the human said "you decide" and the worker answered.

No checkbox here.

### `## Review`

Everything that happened after the code landed, appended per round: the checker's outcome, and the
human's corrections at the gate. Rounds accumulate in this one node.

### `## Interview`

One block per attempt: the attempt's routing key, then each relayed question and each human answer.
An answer is marked `verbatim` or `paraphrase`. An answer that contradicts the recommendation the
worker gave is additionally marked `DIVERGENCE`. A dead attempt is marked in its own heading.

**Ordering requirement: write the human's answer into `## Interview` at relay time** — the moment the
human gives it, before the manager attempts to resume the worker.

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

1. `nodes/NN-<name>.md`: append the flag under `## Flags`, prefixed with its marker.
2. `flags.md`: append one unchecked line naming the same marker and linking the node.

The flag's text is written before its line.

### Settle a flag

1. `flags.md`: change that flag's `- [ ]` to `- [x]`.

No other file changes, and the node file is not touched. A flag the human turns into a node is
checked the same way; the node itself is created by the ordinary add-a-node step.

## Mechanical checks

Every one of these is decidable by reading the files.

1. Every `Blocked by:` target exists, and is not `superseded` or `out-of-scope`.
2. Every `Superseded by:` has a matching `Supersedes:`, both directions present.
3. No `NN` used twice, and no gap that indicates a reused number.
4. Every `Labels:` entry appears in the map's declared vocabulary.
5. Every `resolved` node has an `## Answer` and exactly one line in `decisions.md`.
6. Every `## Flags` entry has a line in `flags.md`, and none the other way.
7. Every `implementation` node has an `## Acceptance condition` before it is `claimed`.
8. No node has more than three `## Interview` attempt blocks.
