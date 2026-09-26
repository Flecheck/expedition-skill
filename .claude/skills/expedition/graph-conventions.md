# Graph conventions

This document says how an effort's graph is written and changed. Read it before touching any of an
effort's files.

Terms are used exactly as the glossary (`CONTEXT.md`) defines them.

If a repo's tracker doc already documents a different local-markdown scheme, see
`wayfinder-divergences.md`.

`## Writing the graph` in `SKILL.md`, the file beside this one, says who writes the graph's record and
how the manager pastes what a worker hands it.

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
- `## Landing an implementation node's work` — the landing policy: where a node's worker works, what one
  path-limited commit of that node's paths takes, and what happens to the worker's tree on each of the
  gate's three outcomes. Landing is the manager's, so neither a worker nor its checker reads this
  section.

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
per flag, one sentence long, written as a report. `## Flags` in `SKILL.md` says whose text the line is,
and `## Closing an effort` there says what the closing report takes from this file. The line's form:

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

The condition states what done means for this implementation node. `## Acceptance conditions` in
`SKILL.md` says who writes it and who may change it after it is written. The human changes only a
condition on a node nobody holds yet. A condition under a live worker reaches the human by that
worker's raise, and by no other route.

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
none of them, or that everything in it traces back to one. Such a demand goes in the handover's
`INVALIDATIONS` part, which names which resolved node the work contradicts and how. A demand about what
changed in the tree, such as *no file under `.scratch/` changes*, is permitted.

`## The checker` in `SKILL.md` says how the manager hands a condition to the checker, and what it does
with a condition that leaves part of its demand in another file.

### `## Flags`

The section holds one entry per flag, in free prose. Each entry starts with the flag's id and then its
marker, one word saying which kind of judgement the flag records. There are three markers:

- `ASSUMPTION` — the worker decided a small ambiguity itself.
- `CONDITION-WRONG` — filed by the manager, after a worker raised its acceptance condition as wrong and
  the human answered *ship it anyway*.
- `DELEGATED` — the human said "you decide" and the worker answered.

A settled flag's entry takes this form:

```
`NN.k` **· settled** `ASSUMPTION` — <the judgement, in the worker's own prose>
```

The word for a flag is `settled`, and `resolved` is kept for a node. Only the line in `flags.md` carries
a checkbox.

### Recording the human's words

The rules in this section cover `## Interview` and `## Review`, the two sections that hold the human's
words. `### The human's words` in `SKILL.md` says when the manager records an answer, what it pastes,
when it marks an answer `paraphrase`, and what it does with a terse reply whose option is unclear.

Every recorded answer carries one of two markers, `verbatim` or `paraphrase`. A reply pasted as the
human wrote it is marked `verbatim`. That mark says the answer is the human's own words rather than the
manager's rendering of them. Where the reply takes an option or an outcome it was offered, the manager
quotes that option in the same entry. The quote is attributed to whoever wrote it, usually the worker.

### `## Review`

The section records everything that happened after the code was written, appended round by round on this
one node. It holds three kinds of entry and nothing else:

1. One entry per checker run, giving its outcome: `PASS`, or `FAIL` and whether the acceptance condition
   or the bar was not met. A checker may raise instead of judging. Its entry then gives no verdict and
   says what it raised.
2. Each correction round, numbered, with the human's words and what the worker changed. The human's
   words are recorded as `### The human's words` in `SKILL.md` says.
3. The gate's outcome: approve, correct or reject. For a reject, the entry also records what
   implementing the node surfaced, and which of the three routes under `### What reject means` in
   `SKILL.md` the node then took.

A checker that gives a `PASS` or `FAIL` may also name a part of the acceptance condition that it could
not establish, for lack of material it was not given. The run's entry lists such parts under a
`NOT COVERED:` label, one item per part, each quoting the part as the checker wrote it. The outcome on
that entry covers the rest of the condition and nothing more.

Every item opens with its state, which is either `OWED` or `ESTABLISHED BY`. Establishing a part
rewrites that opening and nothing else:

```
NOT COVERED:
- OWED — "<the part, as the checker wrote it>"
- ESTABLISHED BY <who> · <what they read or ran> — "<the part, as the checker wrote it>"
```

Whether a part has been established is read from the item's first word alone, and never from the prose
after it. One item holds one part, so parts are counted by items and never by sentences. The
`NOT COVERED:` label stands alone on its own line, so prose that mentions the words names no part. The
state is the manager's bookkeeping, as a flag's state is. The part is the checker's own text, pasted.

A part stays owed until someone establishes it. `### The payload` in `SKILL.md` says who establishes
it, and by when.

Who established the part, and what they read or ran, is recorded on the part's own item, and not where
the establishing happened. A part nobody established stays visible as an item opening `OWED`, which
check 9 below reads. The `NOT COVERED:` list is part of the run's entry, the first kind above.

An entry for a run that covered the whole condition has no `NOT COVERED:` label, no item and no marker.

### `## Interview`

The section holds one block per attempt. A block gives the attempt's routing key, then each relayed
question and each of the human's answers. The manager also marks `DIVERGENCE` on an answer that
contradicts the recommendation the worker gave, so the worker does not read an unmarked answer as
agreement and resolve as though its recommendation had been taken. A dead attempt is marked in its own
heading. A node holds at most three attempt blocks.

## Statuses

- `open` — can be taken once it is unblocked and unclaimed.
- `claimed` — a worker holds it. The claim belongs to the node, so a worker that dies does not release
  it. A node whose code is under check is `claimed`.
- `resolved` — carries an `## Answer`. It is the only status that satisfies a `Blocked by:` edge.
- `superseded` — replaced by other nodes, or made unnecessary by them.
- `out-of-scope` — ruled beyond the destination. Carries no `## Answer`.

No status marks a node as parked, under check or carrying flags. A parked node is `open` with a
non-empty `## Interview`.

## Edges

There are three kinds of edge, and `Blocked by:` is the only one that orders nodes.

- `Blocked by: NN, NN` on the dependent node.
- `Superseded by: NN, NN` on the old node, present from the moment it becomes `superseded`.
- `Supersedes: NN[, NN]` on the replacement, carrying the number of every node it supersedes.

An edge exists only where one of these fields states it. No field records which code a node touches.

## Labels

A label names the family or part a node belongs to, for example `CLASS` rather than `CLASS-1`. Labels
are optional, and a node may carry several.

- A node uses only labels declared in the map's `## Notes`.
- A label is only a filter. Order comes from `Blocked by:` edges and never from a label.
- A node's identity is its `NN` and never a label.
- An effort that declares no vocabulary has no labels on any node.

## Reading the graph

The frontier is every node that is `open`, unblocked and unclaimed. A node is unblocked when every `NN`
in its `Blocked by:` is `resolved`. This document sets no order within the frontier. `Labels:` can
narrow it to one area.

A node file's body and its fenced blocks can hold lines that look like fields, so anything that scans
these files follows two rules:

1. Read fields only from the header block, which is everything above the first `##` heading.
2. Skip fenced code blocks.

## Procedures

Each procedure lists every file it changes, in the order the changes are made.

### Claim

1. `nodes/NN-<name>.md`: set `Status: claimed`.

Save the file before any work starts. Claim an `implementation` node only once it has an
`## Acceptance condition`.

### Resolve

1. `nodes/NN-<name>.md`: append the `## Answer`.
2. `nodes/NN-<name>.md`: set `Status: resolved`.
3. `decisions.md`: append one capped line, under the node's label group where a vocabulary exists.
4. `map-history.md`: where the answer has made a fog item specific enough that it now exists as its own
   node, append that item's text verbatim.
5. `map-manager-only.md`: remove that item from `## Not yet specified`. Step 4 has already appended it
   verbatim, so the text is removed rather than struck in place.

### Supersede

Use this when another node replaces the node, or when another node's answer or landed work means the
node no longer needs doing. A node whose question has only changed, and which is `open`, unclaimed and
holds no work, still needs to exist. Update it in place instead, marking the old wording.

1. `nodes/MM-<name>.md`: each replacement node carries `NN` in its `Supersedes:`. A replacement is
   either created now or an existing node named as the replacement.
2. `nodes/NN-<name>.md`: mark the superseded text in place.
3. `nodes/NN-<name>.md`: add `Superseded by: MM[, MM]`, then set `Status: superseded`.
4. Every node listing `NN` in `Blocked by:`: replace `NN` with the number of every replacement.
5. `decisions.md`: strike through the old node's line in place. A node that never resolved has no line
   there, and nothing is written there for it. Each replacement gets its own line when it resolves.

Step 1 needs only the replacement nodes to exist. Their own work need not have landed.

### Rule out of scope

1. `nodes/NN-<name>.md`: set `Status: out-of-scope`.
2. `map-manager-only.md`: append one line to `## Out of scope`, giving the gist, why it is out of scope,
   and a link to the node.

Every node that lists `NN` in `Blocked by:` now holds an edge that nothing satisfies. Rule each such
node out of scope too, or correct its `Blocked by:`. Until then, check 1 below reports it.

### Park

1. Tell the worker to store its progress and stop. The worker hands back its progress and writes
   nothing.
2. `nodes/NN-<name>.md`: append that progress to `## Interview`, under the current attempt. Include
   every question already answered, with the human's words verbatim and not summarised.
3. `nodes/NN-<name>.md`: set `Status: open`.

Answers already relayed are already on the node, because `### The human's words` in `SKILL.md` has the
manager write each one there as it is given.

### Raise a flag

1. `nodes/NN-<name>.md`: append the flag under `## Flags`, starting with its id and its marker. The id's
   `k` is the next unused one for that node.
2. `flags.md`: append one unchecked line with the same id and marker, linking the node.

Both writes are part of raising the flag, and are never left to a tidy-up afterwards.

The round that raised the flag, an `## Interview` attempt or a round in `## Review`, says what produced
it. For a flag from a worker's own unprompted judgement, what produced it is what the worker actually
did, told in the worker's words. A one-line summary is enough under `## Flags`. The round needs the full
account. Where a node has no round at all, as with a `research` node or an AFK `precondition` node, the
`## Flags` entry carries that account itself.

### Settle a flag

1. `flags.md`: change that flag's `- [ ]` to `- [x]`.
2. `nodes/NN-<name>.md`: mark that flag `settled` under `## Flags`.

`## Flags` in `SKILL.md` says when a node's flags settle, and which flags reach the closing report.

A flag the human turns into a node is settled the same way. The new node is created by the steps under
`## Adding a node`.

### Change the map

Use this when a note, standing preference or fog item in `map.md` no longer says what holds. Use it too
when a rule in a sibling of `map.md` that states rules that currently bind no longer holds. A new item
is written straight into its file, with no other change.

1. `map-history.md`: append the item's existing text verbatim, under the heading mirroring the map
   section it came from. Struck-through text stays struck through.
2. `map.md`, or the sibling the item came from: replace the item with its new current statement, citing
   by markdown link the nodes that shaped it.

`## Writing the map` above says why a map file holds the current statement and not the account.

## Mechanical checks

Each of these is decidable by reading the files.

1. Every `Blocked by:` target exists and is `open`, `claimed` or `resolved`.
2. Every `Superseded by:` has a matching `Supersedes:`, and every `Supersedes:` has a matching
   `Superseded by:`.
3. Every `NN` is used once, and there is no gap that indicates a reused number.
4. Every `Labels:` entry appears in the map's declared vocabulary.
5. Every `resolved` node has an `## Answer` and exactly one line in `decisions.md`.
6. Every `## Flags` entry has a line in `flags.md` with the same id, and every line there has an entry.
   The two agree on state: a flag that is `- [x]` in `flags.md` is marked `settled` on its node, and a
   flag marked `settled` on its node is `- [x]`.
7. Every `implementation` node has an `## Acceptance condition` before it is `claimed`.
8. Every node has at most three `## Interview` attempt blocks.
9. Every item under a `NOT COVERED:` label in a `## Review` opens with `OWED` or with `ESTABLISHED BY`.
   Every such item on a `resolved` node opens with `ESTABLISHED BY`.
10. The check lists every item in the map's `## Notes` that is over the 500-byte target set under
    `## Writing the map` above, with its size. It reports and never fails.
