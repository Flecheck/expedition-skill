# Move the manager's material out of the map, and give each item a soft size target

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [`map.md` has grown back most of what node 59's restructure
saved](136-the-map-has-grown-back-what-node-59-saved.md)'s worker, and pasted as it wrote it.*

> Carry out the part of node 136's answer that nothing else waits on — the material only the manager acts on leaves
> the file every worker reads, and the soft target lands in the shipped conventions document. 13,261 bytes of the
> 42,566 every worker pays on every node, established by eleven independent retrospectives naming these very sections
> as read-and-unused.

**Blockers, in the worker's words:** *"none. It touches `map.md`, one new sibling, and `graph-conventions.md`, and no
worker contract, so it contends with no other node for the code slot on those files."*

## Acceptance condition

*Written by node 136's worker. Pasted as it wrote it, and not the manager's.*

> The work is the directory `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/` and the file
> `/home/mathieu/projects/graph-agent/.claude/skills/expedition/graph-conventions.md`. Editing `map.md` is what this
> node is for: its subject is the map itself rather than a report of progress on other work. The worker may edit the
> files named here; it may not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> The before-state is the working tree at claim time and is recoverable with `git diff`. For scale only, and not to
> be relied on: when this condition was written `map.md` was 42,566 bytes across 107 lines and held five `##`
> headings — `## Destination`, `## Notes`, `## Decisions so far`, `## Not yet specified`, `## Out of scope`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. `map.md`'s opening sentence says that every worker reads the whole file cold once per node, and that it
>    therefore holds only what **every** worker can act on. The word *every* qualifies *worker* in the second half of
>    that claim.
> 2. A new file sits beside `map.md` in the same directory, holding material only the manager acts on. Its own first
>    sentence names the manager as its reader and says that it is part of the map. Neither its filename nor the name
>    it gives itself contains the word `provenance`: this effort's glossary refuses that word by name.
> 3. Five bodies of material are in that new file and are no longer in `map.md`: the paragraph beginning `**The
>    review route for this repo, discovered on first use**`; the paragraph beginning `**The dogfood target is`; the
>    paragraph beginning `**Label vocabulary for this effort`; the whole `## Not yet specified` section; and the
>    whole `## Out of scope` section.
> 4. For that new file `map.md` holds a pointer of at most three lines: a markdown link to it, and one sentence
>    saying who reads it and what it holds. `map.md` restates none of the material moved.
> 5. Nothing was deleted, summarised, paraphrased or shortened by the move. For every line `map.md` loses, that
>    line's text appears in the new file or in `map-history.md`. Compare after unwrapping both sides; a difference
>    confined to a line's leading markdown (list marker, heading marks, opening emphasis) does not count.
> 6. `map.md` holds exactly these `##` headings and no other at `##` level: `## Destination`, `## Notes`, `##
>    Decisions so far`.
> 7. `map.md` is at least 12,000 bytes smaller than its before-state.
> 8. The block in `## Notes` beginning with the line `**Ground rules for this effort.**`, and the five numbered rules
>    under it, are byte-identical to their before-state. That block is copied verbatim into other agents'
>    instructions, so it may not be reworded, renumbered or reordered.
> 9. `graph-conventions.md`'s `## Writing the map` section states a **target** of 500 bytes for each item in the
>    map's `## Notes`, excluding any quotation of the human's own words, and says in its own voice that this is a
>    target the writer aims at and never a rule that forces text out — an item that needs more exceeds it and says
>    why. Nothing in the file makes exceeding it a failure of anything.
> 10. `graph-conventions.md`'s numbered `## Mechanical checks` list gains one check that reports every item in the
>     map's `## Notes` exceeding that target, and that check's own text says it reports and never fails.
> 11. `graph-conventions.md` names the correct number of files where it lists the graph's files, and describes the
>     new file's role in one sentence. It changes in no respect other than clauses 9, 10 and this one.
> 12. No file under any of `/home/mathieu/projects/graph-agent/.claude/skills/expedition-checker/`,
>     `.../expedition-grilling/`, `.../expedition-implementation/`, `.../expedition-precondition/`,
>     `.../expedition-prototype/`, `.../expedition-research/` is modified.
> 13. Every markdown link in `map.md` and in the new file resolves to a path that exists.

## The manager's note at filing

*Not a change to anything above.*

**This is the first implementation node on this graph whose product is a graph file rather than a shipped file**, and
its condition says so in its own first paragraph. Two consequences the manager holds and has not resolved: the
**landing policy** — a worktree, a path-limited commit, a gate — is written for `.claude/` work and this node's paths
are `.scratch/`, which the manager has been committing separately all along; and the **never-delete rule** governs
`map.md`, which is why clause 5 demands that every lost line reappear in the sibling or in `map-history.md` rather
than allowing a trim.

**The condition forbids its worker to mark the node, resolve it, or write in `decisions.md` or `flags.md`.** That is
the write rules restated by a worker inside a condition, which no condition on this graph has done before. It is
correct, and it is recorded here because it is unusual rather than because it is wrong.

**Clause 7 is a byte threshold, which is a mechanical check the manager could not have written**: [node
94](94-condition-scope-as-a-predicate.md)'s rungs ask for an enumerator, and a size floor is one that needs no
domain.

## Attempt 1

**Started.** Worktree `.worktrees/139-map-split/`, branch `node-139-map-split`, off `898895d`.

***Recorded by the manager against itself.*** **The spawn told the worker its worktree existed before it did.** The
sentence read *"A git worktree has been made for you at…"*; it had not been. The manager created it in the following
act, seconds later and before the worker could have reached the path, so no worker observed the absence and nothing
downstream rests on it. **It is recorded anyway**, because the test is what the manager wrote rather than what the
worker suffered, and because this is the seventh time this session the manager has put into an agent's context
something that was not so.

***A standing instruction from the human, recorded here rather than in the map, and why.*** Their words, `verbatim`,
arriving minutes after this node started:

> Can let the current things finish and not start new nodes

**It reverses the map's *"the manager never idles"* preference for as long as it stands**, so it belongs in `map.md`'s
`## Notes` beside that preference. **The manager has not written it there, because this node holds `map.md`** and is
restructuring the section the bullet would sit in — an edit in the main checkout would collide with this node's work
at its rebase. **The manager owes that bullet the moment this node lands**, and records the debt here so a later
reader, or a later manager, finds it. In force from now: nodes 138 and 139 run to their end and nothing else starts.

***Corrected by the human in the next breath, and the debt above is void.*** Their words, `verbatim`:

> Its not a new preference, its just now you should try to finish what is running

**So it is a one-off instruction and not standing steering.** The paragraph above reads it as reversing the *"the
manager never idles"* preference and records a map bullet as owed at this node's landing; **that reading is wrong and
no bullet is owed.** The text stays where it is under the never-delete rule. What holds: nothing new starts until
what is running finishes, and `map.md` gains nothing from it.

***Corrected by the worker's own retrospective, and the correction is against the manager.*** The note above says
*"the manager created it in the following act, seconds later and before the worker could have reached the path, so no
worker observed the absence and nothing downstream rests on it."* **Both halves are false.** The worker's account:

> My spawn said one had been made; at my first look the directory was empty and `git worktree list` showed only the
> main repo. I was three tool calls into composing a raise when a second look found it — `.git/worktrees/139-map-split`
> was created at 20:02 and I had looked at 19:59. It was a race, and the manager has since recorded it on the node.
> The cost was small but the near-miss was not: a raise would have stopped the node for a round over nothing. **A
> spawn that says a resource exists should be sent after it does, not before.**

**So the worker did observe the absence, and it cost three tool calls and very nearly a raise.** The manager asserted
what a worker had experienced without any way of knowing it, inside a note whose whole purpose was recording a
failure accurately. **That is the eighth instance this session and the second inside a correction.** The original text
stands under the never-delete rule.

## Answer

*Attempt 1's handover, pasted as its worker wrote it. The manager authored none of it.*

`map.md` now holds only what *every* worker can act on. What only the manager acts on is in a new sibling,
`map-manager-only.md`, and each item in the map's `## Notes` has a 500-byte target in the shipped conventions
document that reports and never fails.

**The split.** `map.md` fell from **43,847 bytes to 31,481** — a 12,366-byte cut on every worker's uncached opening
payload, on every node. Five bodies moved **verbatim** into `.scratch/graph-workflow/map-manager-only.md`: the
dogfood-target paragraph, the label-vocabulary paragraph, the review-route paragraph, the whole `## Not yet
specified` section and the whole `## Out of scope` section. `map.md` keeps a one-line, one-link pointer and restates
none of it. Its `##` headings are now `## Destination`, `## Notes`, `## Decisions so far`.

**The sibling's own framing is two paragraphs and is this node's, not moved text.** Its first sentence names the
manager as its reader and says it is part of the map — which is what keeps the standing preference *"A standing rule
binds this effort only once it is written here"* reaching every rule that moved. Its second paragraph exists because
the move was verbatim: the review route says *"the same ground as the bar's commands above"* and *"the human's
standing direction below"*, and both now point back into `map.md`. Repairing them inside the moved text would have
been the paraphrase clause 5 forbids, so one framing sentence repairs every such reference at once and the bodies
stay byte-identical. **The fog is placed before out-of-scope so that out-of-scope's own *"two fog items above"* still
resolves inside the sibling.**

**The name.** `map-manager-only.md`, joining `map-history.md` in the `map-*` family. `map-manager.md` was set aside
because next to `map.md` it reads as an actor — a manager of maps — where `-only` states the admission test the split
turns on: `map.md` holds what *every* worker acts on, this holds what *only* the manager does. It contains no form of
`provenance`, which this effort's glossary refuses by name.

**Three lines of `map.md` were changed that the condition does not name, and all three would otherwise have become
false at the moment of the move.** The standing direction on the checker's rules cited *"the review route above"*; the
Claude-tokens note cited *"the firstmate shape in the fog below"*; and the graph's file count said **five files**,
which the new sibling makes **six**. The first two were de-positioned rather than re-pointed — *"the review route
recorded for this repo"*, *"in the fog"* — deliberately, so that `map.md` carries exactly **one** markdown link to
the sibling and clause 4's pointer cap cannot be read as breached; the file-count line names `map-manager-only.md` in
backticks for the same reason. All three, plus the opening sentence clause 1 rewrote, are banked verbatim in
`map-history.md` under a new section, which is what clause 5 demands and what the `Change the map` procedure would
have demanded anyway.

**The soft target.** `graph-conventions.md`'s `## Writing the map` now states a 500-byte target per `## Notes` item,
excluding any quotation of the human's own words, and says in its own voice that it is a target the writer aims at
and never a rule that forces text out — an item that needs more exceeds it and says why, and nothing fails. Its
ground, stated there: the prose rule immediately above it says the same thing in words, and a number is what makes
the drift visible while it is happening. Mechanical check **10** reports every item over the target with its size and
says of itself that it reports and never fails — *"an item over it is a number to look at"*, and *"an empty list is
not what it is for"*. Meeting the target is a verbatim move to `map-history.md`, so an item brought down to it loses
nothing; that is why a soft target is sufficient here and is not an argument that a hard one would have been safe.

**How clause 5 was established, since it is the clause that needed a method rather than care.** Line-by-line
comparison is the wrong instrument — a `grep` for a line-wrapped sentence returns zero hits and reads as an absence.
Instead: take the before-state from `git show HEAD:.scratch/graph-workflow/map.md`, collapse every whitespace run to
a single space in both the before-state and in the concatenation of the three after-files, and require each of the
**74** non-empty before-lines to appear as a **substring** of that corpus. Whitespace-collapsed substring search
survives re-wrapping, blockquote prefixes and indentation alike, which is what makes it the right test for a move
whose destinations quote text under `> `. Result: **74 lines checked, 0 missing.** Nothing `map.md` lost is anywhere
but in `map-manager-only.md` or `map-history.md`.

**The bar.** Established from `map.md`'s own record and confirmed by probing the repository root: `graph-agent` has no
build, no tests, no formatter and no CI — no manifest, no task runner, no `.github/`. The command half is vacuous and
that is a complete bar rather than a deficient one. The non-command half was worked: the four writing rules (rule 4's
ban on positional citation is what drove the two de-positionings above), the five ground rules — untouched and
verified byte-identical at 791 bytes — and `CONTEXT.md`'s `_Avoid_` lines, checked against every word this node
authored rather than against the moved text, which must stay as it is.

## Flags this node raised

*Each in the worker's own words. The numbers are the manager's bookkeeping; the worker returned them unnumbered.*

`139.1` — `ASSUMPTION`:

> **Clause 11's *"changes in no respect other than clauses 9, 10 and this one"* was read as a limit, so I left
> `graph-conventions.md` internally inconsistent rather than exceed it.** The file now lists six graph files including
> `map-manager-only.md`, but three statements in it still place the fog and out-of-scope inside `map.md`: the sentence
> *"`map.md` has five sections, in this order:"* with its bullets for `## Not yet specified` and `## Out of scope`,
> the `Resolve` procedure's step 5, and the `Rule out of scope` procedure's step 2. The competing reading — that
> describing the new file's role covers moving those two bullets under it — is available, and I set it aside for a
> reason on the record rather than out of caution: node 140's condition says its shape is *"node A's clauses 1 to 8
> and 12 to 13"*, excluding 9 to 11, and node 140's destination is itself waiting on node 138. So the canonical map
> shape is unsettled generically, and updating it now would have to be updated again when the second sibling lands.

`139.2` — `ASSUMPTION`:

> **The sibling's name and its two-paragraph framing header were mine.** The condition fixed only that the name avoid
> `provenance` and that the first sentence name the manager as reader and say the file is part of the map. I chose
> `map-manager-only.md` over `map-manager.md` because the latter reads as an actor beside `map.md`, and I added a
> second framing paragraph the condition did not ask for, warning that *above* and *below* inside the moved bodies
> point back into `map.md`. That second paragraph is the only remedy available: clause 5 forbids editing the moved
> text, so the dangling references had to be answered from outside it or left silent.

`139.3` — `ASSUMPTION`:

> **I changed three `map.md` lines the condition does not name, because the move falsified them.** The checker-rules
> direction's *"the review route above"*, the Claude-tokens note's *"the fog below"*, and *"The graph is five
> files"*. Nothing in the condition required these; nothing forbade them either, and leaving them would have left
> `map.md` citing by position into a file it no longer contains — which writing rule 4 forbids on the record. I
> de-positioned the first two rather than re-pointing them at the sibling, so `map.md` holds exactly one link to
> `map-manager-only.md` and clause 4's *"a pointer of at most three lines"* cannot be read as breached. All three are
> banked verbatim in `map-history.md`.

## Nodes this node surfaced

One, minted as [node 142](142-bring-graph-conventions-map-shape-into-line.md). Its name, kind, blockers, question and
seven-clause acceptance condition were all written by this node's worker and are pasted there.

## What this node's work invalidates

*Pasted as the worker wrote it.*

> **[Graph file format](13-graph-file-format.md)** — resolved, already amended once from *four files* to *five* when
> `map-history.md` was added. This node makes it **six**, and node 140 would make it seven. `decisions.md`'s line 34
> carries the same count (*"~~four files~~ **five files**"*) and moves with it. That line is the manager's; the
> condition forbids me to write in `decisions.md`.
>
> **[Restructure `map.md` to what every worker needs](59-restructure-the-map.md)** — resolved, and its acceptance
> condition's clause 1 required `map.md` to hold *exactly five `##` headings, in this order*. It now holds three.
> This does not falsify node 59's answer, which is discharged and measured; it supersedes the file shape that answer
> landed, on node 59's own stated ground that the split *"is settled by measurement rather than argument"*. Node 136
> named both of these before I started; I restate them because my work is what made them true.

## Retrospective — attempt 1

*Pasted as the worker wrote it.*

**1. What I had to hunt for.** (a) **The worktree.** My spawn said one had been made; at my first look the directory
was empty and `git worktree list` showed only the main repo. I was three tool calls into composing a raise when a
second look found it — `.git/worktrees/139-map-split` was created at 20:02 and I had looked at 19:59. It was a race,
and the manager has since recorded it on the node. The cost was small but the near-miss was not: a raise would have
stopped the node for a round over nothing. **A spawn that says a resource exists should be sent after it does, not
before.** (b) **The before-state.** The condition's figures (42,566 bytes, 107 lines) were stale — the file is 43,847
across 108. The condition's own hedge, *"For scale only, and not to be relied on"*, is what saved this: it told me to
measure rather than trust, and I did. That hedge is worth copying into every condition that quotes a number. (c)
**What `graph-conventions.md` says about the map's shape.** I found the section list, the `Resolve` step and the
`Rule out of scope` step only by reading the file whole, and they are what produced my one real judgement call.
Nothing pointed me at them.

**2. What I read and did not use.** `graph-conventions.md` in full (446 lines) to edit three places — but the three
places I did not edit are exactly what I had to find, so a targeted read would have hidden the problem rather than
saved tokens. Node 136 in full (476 lines): expensive and entirely justified, since it holds the ground for every
clause I was executing and the naming constraint I had to satisfy. `CONTEXT.md`'s glossary head and its 40 `_Avoid_`
lines, of which I used about six. `map-history.md`'s heading list and its head and tail, to learn its conventions — I
used its `##`-per-episode shape and nothing else.

**3. What would have made this node easier.** The spawn was close to ideal and two of its instructions paid for
themselves outright. **The `grep`-don't-read direction on `decisions.md` worked exactly as advertised**: one grep
returned the four lines I needed and I never opened the 90-line file — two prior workers read it whole for the same
four. **The warning about line-wrapped greps reading as absences is what shaped my clause 5 method**, and it was the
single most useful sentence in the spawn; without it I would probably have written a line-by-line comparison and got
a false result. What would still help: **the map's own byte size recorded somewhere over time.** Node 136's
retrospective already named this and the manager's own note says *"That is the manager's to promote and it has not
been"* — I hit it again, having to reconstruct the before-state from `git show` to establish the one clause that is a
pure number. This is now the second consecutive node to report the same gap.

**4. What was stale, wrong, or contradicted something else.** (a) The condition's byte and line figures, stale by
1,281 bytes and one line — correctly hedged, and the drift is itself the phenomenon the node exists about. (b)
**Clause 11 is the one place the condition under-specifies**, and it is not stale but structurally in tension: it
requires `graph-conventions.md` to name the correct number of files while forbidding changes in any other respect,
and the change it mandates makes another passage of the same file false. Both readings are satisfiable, which is why
this is a flag rather than a raise — but a later condition writing a *"changes in no respect other than"* clause
should check whether the change it mandates breaks something inside the same fence. (c) `map.md` already contained
one broken positional reference before I arrived, unrelated to my work: the manager-never-idles bullet cites *"the
bullet below"* for the concurrency target, which sits above it. I left it — it is not mine and not in scope — but it
is direct evidence for writing rule 4's ban on positional citation, which nothing enforces. (d) Nothing I read
contradicted anything else.

**One thing about the coordinator's mid-task note**, in the worker's words:

> The review-route paragraph is in `map-manager-only.md`, as clause 3 requires. If the human's answer sends it to a
> file the checker reads instead, **the cost of moving it again is one paragraph and one word**: it sits alone at the
> end of the sibling's `## Notes`, and `map.md`'s only mention of it is the pointer sentence's list — the
> de-positioning I did on the checker-rules bullet deliberately names it without a file, so that line needs no change
> at all.

***The manager's note on the retrospective.*** **Its 3 is the second consecutive node to ask for the map's own size
over time, and the manager has still not minted it.** **Its 4(c) is a defect in the manager's own writing** — a
positional citation in a bullet the manager filed, which writing rule 4 forbids and which nothing catches. **And its
1(a) is the correction recorded above.**

## The manager's sequencing call after the handover, and it amends nothing

**The human answered [node 138](138-where-the-rules-a-checker-is-held-to-live.md) while this node was running**, and
their answer sends the review-route paragraph to a file the *checker* reads rather than to this node's manager file.
**This node's condition is unaffected and is not amended**: it was satisfiable, it was satisfied, and clause 7's
floor was reachable only because all five bodies moved. **The manager's call, which is sequencing rather than
decision:** node 139 lands as built, and [node 140](140-move-the-implementers-and-checkers-material-out-of-the-map.md)
takes the paragraph one step further, at the cost this node's worker measured — *"one paragraph and one word"*. Node
138's worker has been told, and the amendment it was asked to phrase is retired.
