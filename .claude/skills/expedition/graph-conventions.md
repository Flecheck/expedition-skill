# Graph conventions

This document says how an effort's graph is written and changed. Read it before touching any of an
effort's files.

Terms are used exactly as the glossary (`glossary.md`, beside this file) defines them.

If a repo's tracker doc already documents a different local-markdown scheme, see
`wayfinder-divergences.md`.

`## Writing the graph` in `SKILL.md`, the file beside this one, says who writes the graph's record and
how the manager pastes what a worker hands it.

No edit deletes. When a graph file changes, strike through or mark in place the text that no longer
holds, and add the new text around it. Remove text from a file only when it is wrong or the human asks
for it gone. The never-delete rule covers only the graph's own files, listed under `## The seven files`
below. Edit the product the effort changes, and every file the effort ships, plainly: remove superseded
wording, and move nothing to a history file. The never-delete rule also does not reach a removal made by
an act that is invoked and whose declared purpose is removal. The rule guards against deletion that is
unannounced, and being invoked for that purpose is the announcement. Such an act leaves an entry in
place of what it removed. The entry names what was removed and records that the text remains recoverable
from the effort's version control history.

Inside the graph's files, two separate questions settle what happens to superseded text. The first is
what the text is, and this test answers it: *"text is rule-stating if an agent could act differently
because of it today; it is record-stating if it only tells you what was already decided or done."*
What a text is settles that a superseded version of it must never be left readable as though it still
binds. Where the superseded text goes is a second and separate question.

Where superseded text goes is settled by whether the file holding it already archives its own subject.
A node file does: it holds every superseded thing about its one node, so superseded text in a node file
stays in it, marked superseded where it stands. `map.md`, and every sibling of it that states rules
that currently bind, does not. So a superseded item in one of them is replaced by its current form, and
its superseded text is appended verbatim to `map-history.md`. `## Writing the map` below describes
how. Text that records what happened, such as a line in `decisions.md` or an entry in `flags.md`, is
marked superseded in place and never removed. `map-history.md` holds superseded text only, and is never
rewritten.

An implementation node's acceptance condition is rule-stating while its node is live. A superseded
clause of one stays in the node file and is never appended to `map-history.md`. The clause is marked
superseded where the clause itself stands, rather than only recorded elsewhere in the node file. The
reason is that the checker is handed the condition as text and does not read the node.

## The seven files

```
.scratch/<effort>/
  map.md                 The whole effort at low resolution. Every worker reads it once per node.
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
  path-limited commit of that node's paths takes, what happens to the worker's tree on each of the
  gate's three outcomes, and what happens when integrating the node's work conflicts. Landing is the
  manager's, so neither a worker nor its checker reads this section.

`map-manager-only.md` also holds the declared label vocabulary, where the effort declares one.

`map-implementation-rules.md` holds the bar's commands and the standards an implementation node's work
is held against. Its readers are that node's worker and its checker, rather than every worker. What the
file admits is under `## Writing the map` below.

`map.md` has three sections, in this order:

- `## Destination` — what reaching the end of the effort looks like. The section also says, in one
  line, whether the effort is expected to reach the destination. Where the effort is not expected to,
  this line is where a manager reads that a non-empty frontier is that effort's steady state rather
  than a defect.
- `## Notes` — the domain, the skills every session consults, and the standing preferences for this
  effort. Two further blocks are optional prose, written where the effort has them. Each lives here
  and in no sibling file of the map. The first is the effort's ground rules. The second declares, by
  path and glob, which sources are authoritative, which are evidence only, and which hold statements
  known to be false. Absent any declaration, every source a worker is pointed at is authoritative.
- `## Decisions so far` — a pointer to `decisions.md`. The section holds no decision.

`decisions.md` holds one line per resolved node: one sentence of about 25 words, enough to judge
relevance and never a restatement. The lines are grouped under the declared labels where a vocabulary
exists, and flat where it does not.

`flags.md` is the graph's capped index of every judgement an agent made on its own. It holds one line
per flag, one sentence long, written as a report. `## Flags` in `SKILL.md` says whose text the line is,
and `## Closing an effort` there says what the effort closing report takes from this file. The line's
form:

```
- [ ] NN.k ASSUMPTION · [<node name>](nodes/NN-<name>.md) — <one line>
```

A `FRICTION` flag uses this same form. Its marker stands where `ASSUMPTION` stands above, as every
other marker does.

Every flag carries an id, `NN.k`, made of its node's number and then a sequence number within that node,
allocated in write order and never reused. In `flags.md` the id sits between the checkbox and the
marker. On the node's `## Flags` entry it sits in front of the marker.

`- [ ]` means outstanding. `- [x]` means the human has dealt with the flag, which does not mean they
agreed with it. The node holds the same state, marking a settled flag `settled`, so the node and
`flags.md` can disagree. Where they disagree, `flags.md` wins, because the sweep and the effort closing
report are built from it. The flag's node is the first link on the line. The text after the dash may
contain other links.

## Writing the map

This section covers `map.md` and every sibling of it that states rules that currently bind, including a
file the map later splits into, from the day it is written. None of these files archives its own
subject, so their superseded text goes to `map-history.md`, as the paragraphs above `## The seven files`
state.

Each file of the map declares its reader: one kind of worker, or the manager alone. The file admits a
line only where that reader would do something differently for having read it while working a node.
Whoever is already editing a passage applies that test to that passage. No pass over a whole file is owed
under the test, and one is allowed. How a rule was learned fails the test: how many attempts it took and
what they cost, who was wrong, and what the file said before. Move that material to `map-history.md`, and
leave in its place the markdown link to the node that shaped the line. A trigger is part of a rule and
stays. A trigger is an error string, a symptom, or the condition under which a rule fires.

Every note and standing preference in `map.md`'s `## Notes`, and every fog item in
`map-manager-only.md`'s `## Not yet specified`, is a current statement: it says what holds now.
It cites by markdown link the nodes that shaped it, without restating what those nodes hold. The account
behind an item is how it came to say what it says, what was measured, and what it used to say. That
account belongs in `map-history.md`, under a heading mirroring the map section the item came from. So a
map file is rewritten as it changes, rather than grown by appending. The text that replaces an item
stands alone. Every worker reads all of `map.md` once per node, so its size is a cost paid once per
node.

Moving the superseded text out deletes nothing. Text moved to `map-history.md` is moved verbatim,
without summarising, paraphrasing or shortening it. Text already struck through moves struck through. An
item carrying no account beyond its current statement moves nothing.

Each item in the `## Notes` of `map.md`, and of any sibling of it that has one, targets 500 bytes,
counting the item's own prose and not any quotation of the human's own words. The target never forces
text out: an item that needs more exceeds it and says why. No check below treats a breach as a defect.
To bring an item down to the target, use the `Change the map` procedure below.

## Adding a node

Allocate the next unused `NN`. A node keeps its number forever. A number is never reused.

`NN` is the node's identity. The name is free-form. It carries a foreign label when the effort was
adopted from a tracker that had one. For example, a node imported as `AUTH-2` is named
`nodes/24-auth-2-token-refresh.md`. The foreign label resolves to the node by glob.

Create the file with its mandatory fields and its `## Question`. When you create several nodes at once,
write every file first, then fill in `Blocked by:` in a second pass.

1. Whoever adds the node runs checks 1, 3 and 4 under `## Mechanical checks` itself, as part of adding
   it, over the material this addition touched: each new node's number, `Blocked by:` and `Labels:`.

## The node file

Fields are bare `Key: value` lines. They live only in the header block, which is everything above the
first `##` heading.

The name, `Type:` and `Status:` are mandatory. Every other field appears only when it has a value. Write
the fields in the order shown below.

```markdown
# <free-form name — carries a foreign label when one exists>

Type: grilling | prototype | precondition | implementation
Status: open | claimed | resolved | superseded | out-of-scope
Labels: EFF, REG
Blocked by: 31, 47
Supersedes: 12
Superseded by: 88

## Question
## Acceptance condition     <- implementation only; written by the agent or manager that created the node
## Answer                   <- appended on resolution
## Flags
## Review
## Interview
## Annotation               <- written by the manager; one section per annotation, in the order written
```

Sections appear in the order shown, and only when they have content.

### `## Acceptance condition`

The condition states what done means for this implementation node. `## Acceptance conditions` in
`SKILL.md` says who writes it and who may change it after it is written. `### Amend an acceptance
condition` under `## Procedures` says how a change is recorded on the node.

A condition is self-contained text. Everything needed to judge whether the work is done is in the
condition, so its reader never goes anywhere else to find out what it demands. That reader is the
checker, which is handed the condition as text and has not read the node.

So the condition states what must be true, in its own words. A path may say where: the work must touch
that file, produce it, or leave it in a stated state. Such a path is written relative to the repository
root, because an absolute path names a machine, and the worker and the checker that read the condition
may not be on it. The demand itself stays in the text, and never behind a pointer such as *as decided at
node NN*. Where a condition depends on material held elsewhere, whoever writes the condition copies that
material into it. The bar is the one thing a condition need not copy, and only because the bar reaches
the checker by its own route.

A demand about the record as a whole belongs on the handover and in no condition, whatever its wording.
Such a demand holds the work against every decision the effort has recorded: that the work contradicts
none of them, or that everything in it traces back to one. Such a demand goes in the handover's
`INVALIDATIONS` part, which names every resolved node whose answer the work changes, and how it changes
what that answer says: a rename, an extension, a narrowing or a contradiction. A demand about what
changed in the tree, such as *no file under `.scratch/` changes*, is permitted.

Where a condition's scope was derived from a search, the condition states that search. The list of
files stays, and so does the clause that excludes every other file. The search is written beside the
list, as what produced it, and never in place of it. The condition's author owes exactly one of the
three below. A condition addressing a defect with instances that carries none of the three is
malformed.

1. An **enumerator**: the command, and what it returned when it was run.
2. Where no command fits, a **bounding set**: the smallest set that provably contains every instance,
   and how that set was computed.
3. An explicit statement that the scope came from no search, because the work creates a file, or
   because the named places are the work rather than instances of a defect.

An enumerator searches the working tree and never the effort's record. A search over the effort's own
node files or its indexes quantifies over the record, which a condition may not do, and no copy
repairs it.

An instance the search reaches outside the condition's list is reported and not edited. A worker whose
search matches a place the list does not name gains a duty to report it, and never a permission to edit
it. A false positive costs one line in a handover.

A condition's scope is a finding stated in advance. Its readers, the checker and the worker before it,
cannot go and look at how the scope was found, so a condition owes them the same extent that a
checker's finding owes.

An effort whose product is not the expedition skill files never fixes those files. So on such an effort,
no acceptance condition, and no condition for closing the effort, may be made to depend on a change to
them. A defect found in them is recorded as a `FRICTION` flag, which `### Settle a flag` under
`## Procedures` covers.

`## The checker` in `SKILL.md` says how the manager hands a condition to the checker, and what it does
with a condition that leaves part of its demand in another file.

### `## Flags`

The section holds one entry per flag, in free prose. Each entry holds the full account of what produced
its flag, as `### Raise a flag` under `## Procedures` states. Each entry starts with the flag's id and
then its marker, one word saying which kind of flag it is. There are five markers:

- `ASSUMPTION` — the worker decided a small ambiguity itself.
- `CONDITION-WRONG` — filed by the manager, after a worker raised its acceptance condition as wrong and
  the human answered *ship it anyway*.
- `DELEGATED` — the human said "you decide" and the worker answered.
- `FRICTION` — a defect the agent noticed in the expedition workflow itself while using it, rather than
  a judgement about the work in front of it.
- `PERMISSION` — a permission the human granted for one attempt, past a contract clause that blocked
  the node.

A settled flag's entry takes this form:

```
`NN.k` `ASSUMPTION` **· settled** — <the judgement, in the worker's own prose>
```

The word for a flag is `settled`, and `resolved` is kept for a node. Only the line in `flags.md` carries
a checkbox.

### Recording the human's words

The rules in this section cover `## Interview` and `## Review`, the two sections that hold the human's
words. `### The human's words` in `SKILL.md` says when and how the manager records an answer.

Every recorded answer carries one of three markers: `verbatim`, `paraphrase` or `standing yes`. A reply
pasted as the human wrote it is marked `verbatim`. That mark says the answer is the human's own words
rather than the manager's rendering of them. Where the reply takes an option or an outcome it was
offered, the manager quotes that option in the same entry. The quote is attributed to whoever wrote it,
usually the worker.

An entry marked `standing yes` records an item the manager took under a standing yes, as the skill
`expedition-standing-yes` describes. It quotes the scope text of that standing yes word for word, says
which standing yes was applied, and quotes what was taken: the worker's `RECOMMENDED`, or the checker's
`PASS`. The scope text is not the human's words about that item, so such an entry is never marked
`verbatim`. Under `## Review`, such an entry is the gate's outcome, an approval.

### `## Review`

The section records everything that happened after the code was written, appended round by round on this
one node. It holds three kinds of entry and nothing else:

1. One entry per checker run, giving its outcome: `PASS`, or `FAIL` and whether the acceptance condition
   or the bar was not met. A checker may raise instead of judging. Its entry then gives no verdict and
   says what it raised.
2. Each correction round, numbered, with the human's words and what the worker changed. The human's
   words are recorded as `### The human's words` in `SKILL.md` says. For a round the manager starts
   when integrating the node's work conflicts, the entry records the paths of the conflicted files in
   place of the human's words.
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
agreement and resolve as though its recommendation had been taken. A node holds at most three attempt
blocks.

`## When an agent dies or is stopped` and `## Stopping a running worker` in `SKILL.md` say when an
attempt is resumed, replaced or stopped. An attempt's block records what happened to it this way:

- An attempt whose agent died and did not continue is marked `dead` in its own heading. Its block
  carries the dead agent's transcript record count, and its cause of death as the harness stated it.
- An attempt whose agent died and was resumed is the same attempt continuing, and is not a new attempt
  block. Its block carries the same two facts about the death. So no resume counts toward the limit of
  three attempt blocks.
- An attempt the human said is final is marked `final stop` in its own heading, beside where a dead
  attempt is marked `dead`. No manager resumes an attempt so marked.

### `## Annotation`

An annotation records what a later piece of work changed about this node's answer. The manager writes
one onto a node whose answer a later node has changed the meaning of. An annotation is the manager's to
write and never a worker's, because `## Writing the graph` in `SKILL.md` makes the manager the only
writer of the graph's record. A worker whose work changes another node's answer reports that change in
its handover, and the manager writes the annotation from that report.

Where a reporting agent supplied the text, the annotation is that agent's own words, pasted as
`### You write as a scribe` in `SKILL.md` says. Anything the manager adds stands beside those words as
its own marked note.

An annotation is added to the node. It replaces nothing the node already holds.

Each annotation is its own section. Annotations come after every other section, in the order they were
written, as the block under `## The node file` above shows. The heading is `## Annotation`, and it may
name what the annotation records after a colon:

```
## Annotation: <what this annotation records>
```

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

- A node uses only labels declared in the effort's label vocabulary, which `map-manager-only.md` holds.
- A label is only a filter. Order comes from `Blocked by:` edges and never from a label.
- A node's identity is its `NN` and never a label.
- An effort that declares no vocabulary has no labels on any node.

## Reading the graph

The frontier is every node that is `open`, unblocked and unclaimed. A node is unblocked when every `NN`
in its `Blocked by:` is `resolved`. This document sets no order within the frontier. `Labels:` can
narrow it to one area.

A node file's body and its fenced blocks can hold lines that look like fields, and a field can hold
text that is not a value. So anything that scans these files follows these rules:

1. Read fields only from the header block, which is everything above the first `##` heading.
2. Skip fenced code blocks.
3. Take node numbers from a `Blocked by:` field by this rule. The field is written under the
   never-delete rule, so a blocker that has been satisfied is struck through in place rather than
   removed. The field may also hold markdown links to node files, explanatory prose, and commit hashes
   inside code spans. So take a node number from the field only where the number lies outside every
   backtick-delimited code span, outside every `~~...~~` strikethrough, and outside the parenthesised
   target of every markdown link. For example:
   - ``Blocked by: ~~31~~`` gives nothing, because its one blocker is struck through.
   - ``Blocked by: [95](95-carry-the-widening-rule-into-the-shipped-files.md),
     [103](103-carry-the-pick-report-settling-moment.md)`` gives 95 and 103, from the link texts, and
     nothing from the link targets.
   - ``Blocked by: none — [node 139](139-move-the-managers-material-out-of-the-map.md)
     landed as `4e38c11` `` gives 139, from the link text. It gives nothing from the link target, and
     nothing from the digits of the commit hash inside the code span.
   - ``Blocked by: ~~277~~ **none — node 277 resolved and landed at `b94104a`.**`` gives 277, from the
     prose "node 277", and nothing from the struck blocker or the commit hash. Node 277 is resolved, so
     the number the prose repeats blocks nothing.

## Procedures

Each procedure lists every file it changes, in the order the changes are made.

### Start an effort

Use this to create an effort's files. `## Starting an effort` in `SKILL.md` says what the act
establishes and who performs it.

1. `map.md`: write its three sections, as `## The seven files` above describes them. Its
   `## Destination` says both what reaching the end of the effort looks like and whether the effort is
   expected to reach it.
2. `map-history.md`: create it, holding no text yet.
3. `map-manager-only.md`: create it, holding the declared label vocabulary, or a line saying that the
   effort declares none.
4. `map-implementation-rules.md`: create it.
5. `decisions.md`: create it, holding no line yet.
6. `flags.md`: create it, holding no line yet.
7. `nodes/`: create the directory.
8. `nodes/NN-<name>.md`: create each of the effort's first nodes by the steps under `## Adding a node`.
9. Whoever starts the effort, which is the manager, runs checks 1, 3 and 4 under `## Mechanical checks`
   itself, as part of this act, over the material it touched: each first node's number, `Blocked by:`
   and `Labels:`, and the declared label vocabulary.

### Claim

1. `nodes/NN-<name>.md`: set `Status: claimed`.

Save the file before any work starts. Claim an `implementation` node only once it has an
`## Acceptance condition`.

2. Whoever claims the node runs check 7 under `## Mechanical checks` itself, as part of this claim, over
   the material this claim touched: the claimed node.

### Resolve

1. `nodes/NN-<name>.md`: append the `## Answer`.
2. `nodes/NN-<name>.md`: set `Status: resolved`.
3. `decisions.md`: append one capped line, under the node's label group where a vocabulary exists.
4. `map-history.md`: where the answer has made a fog item specific enough that it now exists as its own
   node, append that item's text verbatim.
5. `map-manager-only.md`: remove that item from `## Not yet specified`. Step 4 has already appended it
   verbatim, so the text is removed rather than struck in place.
6. Whoever resolves the node runs checks 5 and 9 below itself, as part of this resolve, over the
   material this resolve touched: the resolved node and its line in `decisions.md`. Where steps 4 and 5
   moved a fog item, it also runs check 11 over `map-history.md` and `map-manager-only.md`.

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

6. Whoever supersedes the node runs checks 1 and 2 below itself, as part of this supersession, over the
   material it touched: the superseded node, each replacement, and every node whose `Blocked by:` step
   4 changed.

### Rule out of scope

1. `nodes/NN-<name>.md`: set `Status: out-of-scope`.
2. `map-manager-only.md`: append one line to `## Out of scope`, giving the gist, why it is out of scope,
   and a link to the node.

Every node that lists `NN` in `Blocked by:` now holds an edge that nothing satisfies. Rule each such
node out of scope too, or correct its `Blocked by:`. Until then, check 1 below reports it.

3. Whoever rules the node out of scope runs check 1 below itself, as part of this ruling, over the
   material it touched: the node ruled out and every node that lists it in `Blocked by:`.

### Park

1. Tell the worker to store its progress and stop. The worker hands back its progress and writes
   nothing.
2. `nodes/NN-<name>.md`: append that progress to `## Interview`, under the current attempt. Include
   every question already answered, with the human's words verbatim and not summarised.
3. `nodes/NN-<name>.md`: set `Status: open`.

Answers already relayed are already on the node, because `### The human's words` in `SKILL.md` has the
manager write each one there as it is given.

4. Whoever parks the node runs check 8 below itself, as part of parking it, over the material this act
   touched: the node's `## Interview`.

### Record a question or an answer

Use this when a relayed question, or the human's answer to one, is written onto its node.

1. `nodes/NN-<name>.md`: append the question or the answer to `## Interview`, under the current
   attempt, in the form that the `## Interview` subsection of `## The node file` above gives. An answer
   carries the marker that `### Recording the human's words` above requires.
2. Whoever appends it runs check 8 below itself, as part of this append, over the material it touched:
   the node's `## Interview`.

### Record a checker's run

Use this when a checker hands back its outcome, or hands back a raise instead of an outcome.

1. `nodes/NN-<name>.md`: append the run's entry to `## Review`, in the form that the `## Review`
   subsection of `## The node file` above gives.
2. Whoever appends it runs check 9 below itself, as part of this append, over the material it touched:
   the entry just appended.

### Amend an acceptance condition

Use this when a node's acceptance condition is changed after it is written. `### Changing one after it
is written` in `SKILL.md` says who may change it and what the change may cover.

1. `nodes/NN-<name>.md`: under `## Acceptance condition`, mark each clause the amendment replaces as
   superseded where the clause stands. Append the amendment after the text of the condition's author,
   marked as its own author's, beside the search or the fact that justified it.
2. `nodes/NN-<name>.md` and `flags.md`: raise the amendment's flag by the steps under
   `### Raise a flag`.
3. Whoever amends the condition runs check 6 below itself, as part of this amendment, over the material
   it touched: the flag's entry on its node and its line in `flags.md`.

### Raise a flag

1. `nodes/NN-<name>.md`: append the flag under `## Flags`, starting with its id and its marker. The id's
   `k` is the next unused one for that node.
2. `flags.md`: append one unchecked line with the same id and marker, linking the node.

Both writes are part of raising the flag, and are never left to a tidy-up afterwards.

The flag's entry under `## Flags` holds the full account of what produced the flag, on every kind of
node. For a flag from a worker's own unprompted judgement, that account is what the worker actually did,
told in the worker's words. The entry holds the account whether or not the node has an `## Interview`
attempt or a round in `## Review`. A worker hands the account back as part of its handover's `FLAGS`
part, which is filed under `## Flags`.

3. Whoever raises the flag runs check 6 below itself, as part of raising it, over the material it
   touched: the flag's entry on its node and its line in `flags.md`.

### Settle a flag

1. `flags.md`: change that flag's `- [ ]` to `- [x]`.
2. `nodes/NN-<name>.md`: mark that flag `settled` under `## Flags`.

`## Flags` in `SKILL.md` says when a node's flags settle, and which flags reach the effort closing
report.

A flag the human turns into a node is settled the same way. The new node is created by the steps under
`## Adding a node`.

A `FRICTION` flag raised on an effort whose product is not the expedition skill files has exactly two
dispositions, and being settled as fixed is not one of them:

- declined — the human judges the flag not worth carrying. Settle it in place by steps 1 and 2, and
  record the human's reason on its entry under `## Flags`.
- outstanding — its line stays unchecked, which means the flag is carried. The effort closing report of
  that effort carries it again.

No agent may mark such a flag settled as fixed, because the fix lands only in the repository holding the
expedition skill files, and no agent crosses a repository boundary. Once the human knows the fix landed,
they may check the flag's line by hand, and mark its entry settled.

This changes, for such a flag, two rules under `## Flags` in `SKILL.md`:

- the rule that a node's flags settle at its gate or at its node closing report. Such a flag stays
  outstanding past both, until the human declines it or checks it by hand.
- the rule on which flags reach the effort closing report. Such a flag reaches that report while it is
  outstanding, whatever that rule says of other flags.

3. Whoever settles the flag runs check 6 below itself, as part of settling it, over the material it
   touched: the flag's entry on its node and its line in `flags.md`.

### Change the map

Use this when a note or standing preference in `map.md`, or a fog item in `map-manager-only.md`, no
longer says what holds. Use it too when a rule in a sibling of `map.md` that states rules that currently
bind no longer holds. A new item is written straight into its file, with no other change.

`## Writing the graph` in `SKILL.md` says who runs this procedure.

1. `map-history.md`: append the item's existing text verbatim, under the heading mirroring the map
   section it came from. Struck-through text stays struck through.
2. `map.md`, or the sibling the item came from: replace the item with its new current statement, citing
   by markdown link the nodes that shaped it.

`## Writing the map` above says why a map file holds the current statement and not the account.

3. Whoever changes the map runs checks 4, 10 and 11 below itself, as part of this change, over the
   material it touched: the map file it changed and `map-history.md`. Check 11 is what establishes that
   step 1 was carried out.

## Mechanical checks

Each of these is decidable by reading the files.

1. Every `Blocked by:` target exists and is `open`, `claimed` or `resolved`.
2. Every `Superseded by:` has a matching `Supersedes:`, and every `Supersedes:` has a matching
   `Superseded by:`.
3. Every `NN` is used once, and there is no gap that indicates a reused number.
4. Every `Labels:` entry appears in the map's declared vocabulary.
5. Every `resolved` node has an `## Answer` and exactly one line in `decisions.md` that is not struck
   through. It may have any number of struck-through lines there.
6. Every `## Flags` entry has a line in `flags.md` with the same id, and every line there has an entry.
   The two agree on state: a flag that is `- [x]` in `flags.md` is marked `settled` on its node, and a
   flag marked `settled` on its node is `- [x]`. A settled flag whose index line has been removed is not
   a mismatch. An outstanding flag missing its index line still is one.
7. Every `implementation` node has an `## Acceptance condition` before it is `claimed`.
8. Every node has at most three `## Interview` attempt blocks.
9. Every item under a `NOT COVERED:` label in a `## Review` opens with `OWED` or with `ESTABLISHED BY`.
   Every such item on a `resolved` node opens with `ESTABLISHED BY`.
10. The check lists every item in the `## Notes` of `map.md`, and of any sibling of it that has one,
    that is over the 500-byte target set under `## Writing the map` above, with its size. It reports and
    never fails.
11. Every change to a map file, meaning `map.md` or a sibling of it that states rules that currently
    bind, keeps everything it takes out in `map-history.md`. This has two halves. First,
    `map-history.md`'s content before the change is a byte-exact prefix of its content after the
    change, so the file gained text and lost none. Second, every passage the change removed from a map
    file appears byte-identically inside the text the change appended to `map-history.md`. The check
    is decided by comparing the two states of the files character by character, and not by reading
    them for sense, so it too is decidable by reading the files. It fails where either half does not
    hold.

### Who runs a check, and when

Every check is run by whoever performs an act that can make it false, at that act, over the material
that act touched. So each procedure under `## Procedures`, and `## Adding a node`, ends with a step
naming the checks its writes can make false. No schedule, no periodic pass and no separately spawned
agent runs any of them, with one exception. The sweep runs every check over the whole graph at an empty
frontier, and `## Closing an effort` in `SKILL.md` says who runs it.

### What a failure produces

A failed check produces one of two things, and neither raises a flag.

- Where what failed is that act's own bookkeeping, such as a missing index line, a missing edge or a
  flag left unmarked, whoever performs the act repairs it inside the same act and reports nothing.
- Where the repair would change something the human decided, would rewrite or remove text already
  recorded, or would reverse a status, whoever performs the act puts it to the human instead.

### How a check reads the files

A check reads the files by these rules.

- `## Reading the graph` above holds three of them: fields are read only from the header block, fenced
  code blocks are skipped, and node numbers are taken from a `Blocked by:` field by the rule stated
  there.
- Text is unwrapped into unbroken lines before any phrase is matched, because a phrase that wraps is
  invisible to a search over lines.
- In `flags.md`, a flag's node is the first link on the line.
- In `decisions.md`, a resolved node's entry is identified by the first link on its line. So an entry
  whose text cites another node is not counted as an entry for that node.
- A `## Flags` entry is line-anchored: it begins at the start of a line with the flag's id. So a flag
  id that appears mid-sentence inside another entry's prose is not itself an entry.
- A flag counts as settled on its node only where the marker `**· settled**` stands in one of two
  positions: directly after the entry's kind marker, as the settled form under `## The node file` shows,
  or directly after its id. The bare word `settled` in an entry's prose does not settle it.
- A number for which no node file has ever existed is a skipped number. It is not a gap that indicates a
  reused number, and check 3 does not fail on it.
- A heading that begins `## Acceptance condition` and continues with further words counts as the node's
  `## Acceptance condition`.
- A `NOT COVERED:` label inside a blockquote is quoted text. Check 9 does not read it as a label.

## Work that changes a file other nodes are written against

An implementation node that changes a file which other nodes of the same effort are written against
must, at its gate, name which files it moved and which existing files are left in the older form.

## What a hard rule in a worker contract is

A hard rule in a worker contract binds by being read by the agent the contract was given to. No
mechanism in the shipped workflow enforces one.

A contract says what a worker may do. What a worker can do is a property of the harness that ran it,
such as which tools the harness gave it. A clause about what a worker may do survives a change of
harness. A clause about what a worker can do does not, because the next harness may allow what the last
one prevented.

So whoever writes or edits a contract writes each rule as what a worker may do. A rule that would be
false on a harness unable to enforce it does not belong in a shipped file. Where agents keep reading a
rule as demanding less than it says, the remedy is a better-written rule or an exception granted to that
rule, and never an assumed capability.
