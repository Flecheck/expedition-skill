# The manager's own uncommitted record edits collide with a landing branch

Type: grilling
Status: resolved

Blocked by: none

## Question

*The manager's own, minted after the collision below. Marked as the manager's.*

**The landing policy has no procedure for the case where the manager's own uncommitted edits sit on the files a
landing branch changes.** It met that case at [node 144](144-make-the-rules-file-stand-alone.md): the branch changed
`map.md` and `map-implementation-rules.md`, and the main checkout held uncommitted manager edits to both — two count
settings written there minutes earlier. `git merge --ff-only` cannot write a file with local modifications, so an
approved node could not land.

**Why the case is structural rather than unlucky.** The policy says the graph's own files *"are **not** committed per
node; they are committed periodically by the human"*. So the record accumulates uncommitted edits for long stretches
by design — while implementation nodes whose work **is** the record land by fast-forwarding over those same files.
The two rules guarantee the collision; nothing in the policy names it.

**What makes it worse than an ordinary conflict:** the manager's edits exist in no commit anywhere. A wrong move
loses the human's own recorded words, which is the one thing the never-delete rule exists to protect.

**What is open:**

1. Does the manager commit the record before a landing, and if so does that survive the human's standing instruction
   that they review a diff before a commit is made?
2. Or does the manager stash and restore, accepting a window where the edits live only in a stash?
3. Or does the record stop being edited at all while a record-editing node is in flight — which serialises the
   manager against its own workers?
4. Is this the same question as [node 115](115-two-writers-edit-the-map-at-once.md)'s, or a different one? Node 115
   is a *worker's* map change against the manager's; this is the manager against itself, and its open carriers are
   [node 160](160-carry-the-integration-conflict-rule-into-the-map.md) and [node
   162](162-how-much-of-the-integration-rule-ships.md).

## The manager's note at filing

*Not a change to anything above.*

**The manager has taken no route.** The collision is live and unresolved at this node's filing: node 144's work is
committed on its branch and not merged, and the manager put the sequence to the human rather than running it.

**The human's words that prompted it**, `verbatim`: *"we should make it so that there isn't issues like that later"*.

**Not started, and the reason is a count rather than a judgement.** This effort runs two nodes needing the human at
once, and both places are held by [node 165](165-measure-whether-a-fed-file-earns-its-place.md) and [node
50](50-shared-blocks-stay-duplicated.md), each holding a banked question.

## Interview

### Attempt 1

*The attempt's routing key does not survive the manager's session, so it is not recorded here.*

**The worker's payload carried two questions**, numbered `Q1` and `Q2` under the batching rule [node
126](126-carry-question-batching-into-the-grilling-contract.md) landed as `8cc9b79`. This is the first payload on this
effort to use it.

**The human's reply, `verbatim`.**

> Q1 ok Q2 does it happen only because the change do change the map whereas in a regular effort it shouldn't be the case so it isn't nessesary ?

**What `Q1 ok` takes**, quoted from the worker's own text and attributed to the worker:

> **Q1 ASK:** The moment you approve a node's work, should the manager commit its own outstanding record edits as
> **step one** of the landing sequence — path-limited to the effort's record directory, with the message reported to
> you afterwards but **no diff put in front of you first** — and only then rebase, re-run the bar, and fast-forward?
>
> **RECOMMENDED:** Yes.

***The manager's note on Q1.*** **Settled, and not a divergence** — the reply names `Q1` and assents to its
recommendation. It takes none of Q1's five alternatives. **It narrows a standing habit of the human's** and the
worker said so in as many words when it recommended it, so the narrowing is on the record as deliberate rather than
inferred: the manager commits the effort's record, path-limited, as step one of a landing, after approval and without
a diff being put in front of them first.

***The manager's note on Q2.*** **This is a question back, not an answer**, and it went to the worker rather than
being read as taking any option. The manager has not treated it as a `no`, nor as the `map only` alternative, nor as
assent. **Q2 stays unsettled and its number is fixed** — a re-ask uses `Q2` again, per the rule the same node landed.

***The manager's note on the reply's form.*** **It is `Q1 ok Q2 …`, which is exactly the shape [flag
`126.2`](126-carry-question-batching-into-the-grilling-contract.md) chose the glyphs for** — its worker took `Q1.`
over a markdown heading on the stated ground that the human's own predicted reply form was *"Q1 ok Q2 ok Q3 .."* and
that the number they type should be the number the payload shows. The manager records that the prediction held on its
first use.

**The worker's re-ask of `Q2`, pasted as it wrote it. Its number is unchanged, per the rule node 126 landed.**

> **Your premise holds, and I went and measured it rather than reasoning about it.**
>
> **Why a regular effort does not meet this.** Git refuses the merge only where a file the manager left dirty is one the branch *also* changes. The manager's only uncommitted files are the effort's record; a branch only touches the record if that node's work *is* the record. On an ordinary effort — implementation nodes editing product code — the two sets never intersect, and the merge is never blocked. The disjointness is not luck: this effort's own rules already forbid a worker to touch `decisions.md`, `flags.md` or its node's status line, and the checker `FAIL`s if one appears in the work.
>
> **How much of this effort is the exception.** Of the **17 node landings since the worktree-and-fast-forward policy came in, 7 changed files in the effort's own record, and 4 of those changed nothing else.** That is a large fraction, and it is large for exactly the reason you name: this effort's subject *is* the workflow, so restructuring the map is implementation work here and would be nothing on a normal effort.
>
> **The one thing I found that cuts against shipping harder than your question did.** The general form of this hazard — foreign uncommitted work sitting in the tree at landing time — is *already* settled in the shipped design, and settled differently. Node 11's rule: where the tree holds uncommitted work the node did not write, *"the manager stops and says so rather than committing someone else's work under a node's name."* So a new shipped sentence would not fill a gap; it would add a **second, contradictory** disposition — commit it — for a case a regular effort never reaches, and sit next to a rule that says stop.
>
> **Q2 ASK:** Given that the collision only fires when an implementation node's work is the effort's own record, does anything reach the shipped manager contract, or does this stay in this effort's map alone?
>
> **RECOMMENDED:** **Nothing ships — map only.** This reverses what I recommended last time, and your question is why. I had argued a regular effort meets this hazard; it does not, and the shipped contract already answers the general form of it with the opposite instruction.
>
> **ALTERNATIVES:** One sentence anyway, on the ground that the workflow is meant to be dogfooded and every future effort that improves the workflow itself meets this — set aside because that is a known special case, and the map is where a special case belongs until a second effort actually hits it. Hand it to node 162 — set aside, different step.

**The human's reply, `verbatim`.**

> stays in the map

**The option it takes**, quoted from the worker's own re-asked `Q2` and attributed to the worker:

> **RECOMMENDED:** **Nothing ships — map only.**

***The manager's note.*** **Not a divergence** — the reply names the re-asked recommendation and takes neither
alternative. **Both questions of this payload are now settled**, `Q1` at the first relay and `Q2` at the second, and
the worker reversed its own `Q2` recommendation between them because the human's question falsified its premise.

## Answer

*Pasted as the worker wrote it.*

> ### The rule
>
> When the human approves an implementation node at its gate, the landing sequence gains one step before every step it already had: **the manager commits its own outstanding edits to the effort's record**, path-limited to the record directory, with no diff put in front of the human first and the commit reported afterwards. Only then does the manager rebase the node's branch, re-run the bar, and `git merge --ff-only`.
>
> The human assented to that sequence as recommended, taking none of the five alternatives offered. It does not breach the shipped contract's *"approval before any commit"* — the record commit happens after the gate approves.
>
> ### Why that moment, and not the one the record currently names
>
> Three facts, measured in a scratch repository rather than reasoned about:
>
> - `git merge --ff-only` refuses **only** where a file the manager has left dirty is one the branch also changes. Unrelated dirty files merge without complaint.
> - Committing the record and then merging **without** rebasing fails outright — `fatal: Not possible to fast-forward`. So the record commit must come **before the rebase**, never between the rebase and the merge.
> - After that commit the rebase can conflict on the record files, both sides having appended. Node 115 already makes that conflict the manager's own to resolve by keeping both sides.
>
> **The moment the record currently names is the wrong one.** Node 115's answer says the manager's graph state *"must be committed before a worktree is cut"*. A worktree is cut when a node is claimed, and the manager writes the record continuously for the whole of that node's life. At node 144 the two colliding edits were written minutes before the landing; they landed as `9a252c9`, whose two paths are the same two paths as node 144's own commit `37a3d28`. Committing at the cut is still worth doing, because it keeps the worker's base current — it does not prevent this failure.
>
> ### A read-only trial runs before anything is touched
>
> `git merge-tree --write-tree` says in advance whether the rebase will conflict on the record files. It writes nothing, costs one call, and turns the union case from a surprise into a plan.
>
> ### The rule stays in this effort's map, and nothing ships
>
> The human's word, `verbatim`: *"stays in the map"*.
>
> The collision fires only where an implementation node's work **is** the effort's own record. On an ordinary effort the two sets never intersect — disjointness that is already guaranteed rather than hoped for, a worker touching `decisions.md`, `flags.md` or its node's status line being a checker `FAIL`. Measured: of the **17 node landings since the worktree-and-fast-forward policy came in, 7 changed files in the effort's own record and 4 of those changed nothing else.** Large, and large for the one reason that does not generalise.
>
> **The shipped contract already answers the general form of this hazard, and answers it the other way.** Node 11's rule is that where the tree holds uncommitted work the node did not write, the manager *"stops and says so rather than committing someone else's work under a node's name."* A shipped sentence saying *commit it* would put two contradictory dispositions in one file, for a case a regular effort never reaches.
>
> ### This is not node 115's question
>
> Node 115 is a **worker's** record edits meeting the manager's, resolved by unioning at integration. This is the **manager's own** edits meeting the merge step, and no union resolves it, because there is nothing to merge — the edits sit in no commit anywhere.
>
> ### What the map has to be made to say
>
> 1. The sentence *"The graph's own files are **not** committed per node; they are committed periodically by the human"* is struck. Node 160's clause 7 already demands exactly this.
> 2. New text beside it states the sequence and gives the moment as **before the rebase, at landing**. Node 160's clause 7 says *"before a worktree is cut"*, which this node establishes to be insufficient — so that clause wants a second half rather than a replacement.

## Flags

*All four are the worker's own text, pasted.*

`176.1` `ASSUMPTION` **· settled** — **The commit's scope and its message, which the human's assent did not reach.** My question said "path-limited to the effort's record directory" and said nothing about the message or a trailer. I settled both: the commit takes the record directory as a whole rather than the paths the branch happens to intersect, because computing that intersection is fiddly at the tensest moment of the sequence; and it carries **no** `Node: <effort>/<NN>` trailer, because node 11 fixes that trailer as the join key for a node's *code* commit and record bookkeeping is not that node's work.

`176.2` `ASSUMPTION` **· settled** — **The human's own hand-edits in the record directory are committed by step one rather than stopping the landing.** Node 11 tells the manager to stop where the tree holds uncommitted work the node did not write, and step one now sweeps whatever sits in the record directory. I settled that it commits rather than stops: node 11's ground is *attribution* — "committing someone else's work under a node's name" — and the record commit names no node; the record is append-only under the never-delete rule; and nothing is ever pushed.

`176.3` `ASSUMPTION` **· settled** — **The read-only trial merge is part of the rule.** `git merge-tree --write-tree` appeared in my payload's `SO FAR` as a measured fact but not in the question the human answered, so their assent does not reach it. I put it in the answer on my own authority.

`176.4` `ASSUMPTION` **· settled** — **I did not invoke the `/grilling` method skill.** The map names it among the skills every session should consult; my contract states that its own discipline and shapes are "the whole of what binds you, and they bind whether or not any such skill is invoked". I worked from the contract alone.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
