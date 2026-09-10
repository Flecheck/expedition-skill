# The manager's contract defines the map as one file, where the workflow ships four map files

Type: implementation
Status: resolved

Blocked by: 204

## Question

*Surfaced by [Demote the recorded bar commands to a copy confirmed against the
repo](204-demote-the-recorded-bar-commands-to-a-copy.md)'s worker, and pasted as it wrote it.*

> `.claude/skills/expedition/SKILL.md`'s glossary entry for **map** says the map is "the
>            effort's whole shape at low resolution, in the one file every worker reads cold once per
>            node", equating the map with a single file. The rest of the shipped set does not:
>            `graph-conventions.md`, beside it, lists `map.md`, `map-history.md`, `map-manager-only.md`
>            and `map-implementation-rules.md` as an effort's map files; the implementation contract
>            calls the rules file "the sibling of the effort's map"; the checker's contract names its
>            path; and `CONTEXT.md`, the glossary this effort declares authoritative, defines Map with
>            no filename and no one-file claim at all. So the manager's contract is the single outlier,
>            the same shape node 174 found for the implementer's contract. This node's own work
>            sharpened it: the entry now also says the map "holds a record of the bar's commands", and
>            on this effort that record sits in a sibling rather than in the file a worker reads cold.

**Blockers, in the worker's words:** node 204, whose work puts the wording clause 2 below requires kept into that entry.

## Acceptance condition

*Written by node 204's worker. Pasted as it wrote it, and not the manager's.*

> The work is one file, relative to the repository root: `.claude/skills/expedition/SKILL.md`. The worker may edit that one and no other, and may not write any file under `.scratch/`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. That file's glossary entry for **map** no longer states that the effort's map is one file, and no longer states or implies that everything the map holds sits in the one file a worker reads cold once per node. Where the entry says what a worker reads cold once per node, it says that file is a part of the map rather than the whole of it.
> 2. That entry keeps its statement of what the map is — the effort's whole shape at low resolution, holding the destination, the standing preferences, the fog as in-scope work that can be told is coming but cannot yet be phrased as a question, and what is ruled out of scope — and keeps all four of its remaining statements: that the map indexes decisions and never restates one; that the manager owns it; that two things live there and nowhere else, those being the effort's ground rules and the standing steering the human has given; and that it holds a record of the bar's commands once discovered for this repo, which an agent confirms against the repo before using.
> 3. The entry names no particular filename. Where it says where the map's material sits, it says so by role and position only.
> 4. No sentence anywhere in the finished file states or implies that a worker reads the whole of the map, or that the map is a single file.
> 5. Any sentence in the finished file that introduces a list by stating how many items it holds states a count arithmetically correct for the items that list then holds.
> 6. No text outside the passages clauses 1 to 5 reach is deleted or reworded.
> 7. The finished file names no plugin, requires no skill to be invocable, and assumes no particular repository, machine or toolchain.
> 8. No file other than the one named above is modified, and no file under `.scratch/` is modified.
> 9. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Its blocking edge is already satisfied.** Node 204 landed with the wording its clause 2 requires kept, so this
node is takeable now.

**It is the same shape as its own parent, one file over.** Node 174 found the implementer's contract to be the
outlier on where the bar's commands live; this is the manager's contract as the outlier on what the map is. **Its
author's own work sharpened the defect it reports** — node 204 added *"holds a record of the bar's commands"* to
that entry, and on this effort that record sits in a sibling rather than in the file a worker reads cold.

**Its clause 5 carries the arithmetic audit forward**, which on node 204 meant enumerating 49 counted lists across
two files to satisfy one clause. ~~**Nothing indexes counted lists** — the item node 204's retrospective reports for
the fourth time.~~ **Struck by the manager, and this is the corrected version.** Nothing indexes counted lists, and
node 204's retrospective reports that item **with no count at all**; its *"this is the fourth"* attaches to a
different item — that nothing indexes which open acceptance conditions touch which passages of a shipped file.
**This node's own worker caught the error**, named the shape as the manager contract's own ninth unsettled question
— *"An unestablished inference of yours, written into a node's question or into a spawn, arrives at the worker as
settled fact and hardens there"* — and acted on neither claim, auditing the file itself. It is flagged at `215.3`.

## Review

### Checker run 1 — `FAIL`, on the acceptance condition

*Pasted as the checker wrote it, in its own order. Every sentence is the checker's.*

> ```
> FAIL: acceptance condition
> ```
>
> **Base, verified myself rather than taken from the spawn.** The worktree's `HEAD` is `1773ea2`; `git merge-base HEAD master` is `1773ea2`, so the tree is an ancestor of `master` with no divergence of its own. `git diff --name-only HEAD master` returns eleven paths, every one under `.scratch/`, and `git diff master HEAD -- .claude/skills/expedition/SKILL.md .claude/skills/expedition/graph-conventions.md` is empty — the shipped file in this tree is current and the divergence is record-only. The base claim holds this time.
>
> **The standards I read.** `.scratch/graph-workflow/map-implementation-rules.md`, and nothing else beside it. What bore on this work: the review route's *"standards to hold work against"* (`/coding-principles`, `/naming`, `CONTEXT.md`'s `_Avoid_` lines, this effort's ground rules and its four standing rules for writing, `graph-conventions.md`, `/writing-for-agents`); its statement that **no reviewing skill is named for this repo**, so I ran none and went looking for none; and its rule that an implementation node's work may be the effort's own record. **I read the changed path I was given as the work under that rule** — here it is a shipped file rather than a record file, and no change to a node status line, to `decisions.md` or to `flags.md` appears among the work. I read `/writing-for-agents` by name from the `mattpocock-skills` plugin and held the changed prose against it.
>
> **The bar.** Its command half is empty, confirmed against the repo rather than taken from the spawn: the root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`; `git ls-files` matched no manifest, task runner, CI file, YAML, formatter config or hook config anywhere in the tree; there is no `.github`; `.gitignore` ignores `.worktrees/` and `.claude/worktrees/` and invokes nothing. Under the *"if relevant"* clause that is a complete bar. **The bar holds** — nothing I ran, and nothing in the non-command half, faults the changed text. The failure below is on the condition, not on the bar.
>
> ---
>
> ### The finding — clause 4
>
> **The instance.** In `.claude/skills/expedition/SKILL.md`, under `## Spawning a worker`, the spawn's third item:
>
> > **the pointers the worker reads** — its own node file, the effort's map, and the effort's index of decisions scoped by label where a vocabulary exists.
>
> This sentence says a worker reads *the effort's map*, unqualified. The finished file's own amended glossary now says the map **is more than one file**, and that *"The one every worker reads cold once per node is a **part** of it"* — so pointing a worker at "the effort's map" is pointing it at the whole. Either reading of the phrase trips clause 4: if *"the effort's map"* denotes the map as the glossary now defines it, the sentence states that a worker reads the whole of the map; if it denotes one file identified as the effort's map — which is how a pointer in a list of pointers reads — it implies the map is a single file. Clause 4 forbids both.
>
> The file's own sibling standard confirms which way the design runs: `graph-conventions.md`'s file table says of `map-manager-only.md`, *"The part of the map only the manager acts on. **No worker reads it.**"* So the unqualified pointer now sends every worker at material the shipped conventions say no worker reads. The passage was reachable: clause 4 quantifies over the whole finished file, and clause 6 leaves any passage clauses 1 to 5 reach open to edit.
>
> **The form, as a predicate.** A sentence in `.claude/skills/expedition/SKILL.md` that says an agent the manager spawns — a *worker*, as the glossary distinguishes it from the manager — reads, or is pointed at, *the map* or *the effort's map* without naming which part of it; or that treats the map as one file or one path.
>
> **The extent — an enumerator** over the whole of what the implementer may edit, which is one file:
>
> ```
> grep -n 'map' /home/mathieu/projects/graph-agent/.claude/worktrees/215-map-as-one-file/.claude/skills/expedition/SKILL.md
> ```
>
> Nine hits. I unwrapped the file into unbroken lines before applying the predicate, so a sentence spanning a line break is not invisible to it. Applied by hand: **one instance**, the spawn item quoted above. Seven hits are the manager recording or writing to the map, or the map holding a setting, and none say a worker reads it. The ninth — the per-kind addition *"for `implementation`, its acceptance condition, **the bar by way of the map**"* — is the same pointer seen from the implementation branch; I judged it **not** an instance, since it says where the bar reaches the worker from and not that the worker reads the whole, and I name it here because whoever repairs the instance is standing next to it.
>
> ---
>
> ### What the other clauses came to
>
> - **Clause 1 — met.** The entry no longer says the map is one file; it says *"It is more than one file"*, and names the file a worker reads cold once per node as *"a part of it"*.
> - **Clause 2 — met.** *"the effort's whole shape at low resolution"* survives, with the destination, the standing preferences, the fog in its own words, and what is ruled out of scope. All four remaining statements are present and unreworded: indexes decisions and never restates one; *"You own it"*; two things live there and nowhere else, being the ground rules and the standing steering; and the record of the bar's commands, confirmed against the repo before use.
> - **Clause 3 — met.** The entry names no filename. Its two placements are by role (*"what every worker can act on"*, *"material only one kind of reader acts on"*) and by position (*"a part of it"*, *"a sibling of that part"*).
> - **Clause 5 — met.** I enumerated every sentence and heading in the finished file that introduces a list with a count and counted the items each list then holds: five node kinds, five handover parts (with the sixth named separately for an implementation worker), four constraints on a condition, three tier-1 kinds, three outcomes, three places a rejected node goes, three non-claimants, three states nothing shows, two counts, two tiers, two forms of steering, two writes to raise and two to settle a flag, two rules binding every condition, two things a spawn carries that are not yours, two the human can say that are not answers, two the scribe rule protects, two handed back alongside an outcome, two that stay out of a payload, two things a licence produces. Every one is arithmetically correct. `## Where two of these pull against each other` heads three bullets, but its *"two"* counts the rules in tension inside each bullet rather than the bullets, so it is not a count of the list's items.
> - **Clause 6 — met.** `git diff` is one hunk, wholly inside the **map** entry. No other text is deleted or reworded, and no other passage is reflowed.
> - **Clause 7 — met.** `grep -i -E 'plugin|skill|mattpocock|/writing-for-agents|/coding-principles|/naming'` over the finished file returns nothing. It names no plugin, requires no skill to be invocable — `graph-conventions.md` is a sibling file read by path, not a skill invoked — and names no repo, machine or toolchain.
> - **Clause 8 — met.** `git status --porcelain -uall` shows exactly one entry, `M .claude/skills/expedition/SKILL.md`. No untracked file, and nothing under `.scratch/` touched.
> - **Clause 9 — met.** As above.
>
> **Nothing is left uncovered.** Every clause was establishable from the tree and the standards file; no part of the condition demands material outside what I was given, so there is no `NOT COVERED` entry.
>
> ```
> QUESTIONS:
> - The condition's clauses 1 to 4 are right for the file they name and leave the shipped file beside it saying the opposite, and clause 8 forbids the worker from touching it. `.claude/skills/expedition/graph-conventions.md`, under `## Writing the map`, states: "every worker reads the whole map cold, so an item's size is paid once per node". That sentence says exactly what clause 4 forbids the manager contract to say, and it contradicts that same file's own table entry for `map-manager-only.md` — "The part of the map only the manager acts on. No worker reads it." — so the inconsistency predates this work rather than being made by it. Its neighbour two paragraphs earlier, "Every worker reads `map.md` whole and cold", is consistent with the amended glossary and needs nothing. This is not a departure the worker made and not a defect in the wording the condition dictates; it is a second shipped file the same correction has not reached, and it needs a node rather than a correction round here.
> ```

### The disagreement, and why the manager has not resolved it

*The manager's own note. It decides nothing.*

**The worker flagged this exact passage and reached the opposite conclusion.** Its flag, in its words: *"the spawn
section's map pointer was read as outside clause 4… I left it unreworded: it names a pointer rather than a file, the
glossary entry two hundred lines above it now states the map's file count outright, and clause 6 forbids rewording
text the earlier clauses do not reach. The alternative was to widen the pointer to name the map's files, which would
have put filenames into the contract that ground rule 1 keeps out."*

**So this is a worker against its checker on one judgement, and that disagreement has one referee.** The manager
may not order a correction round here, because ordering one is choosing the checker: the repair the `FAIL` implies
is a rewording of the spawn's pointer bullet, and the worker's ground for leaving it is that clause 4 does not reach
it and clause 6 therefore forbids touching it. **Both read the same two clauses and split.** It goes to the human
with both readings and the manager takes no side.

**What is not in dispute.** Every other clause is met, on both parties' accounts — the entry itself, clause 5's
arithmetic over the whole file, and the bar. The checker says so explicitly: *"The failure below is on the
condition, not on the bar."*

### Gate — `approve`, over a `FAIL`

**The human's word, `verbatim`.**

> approve

**What it decided.** The gate offered three routes: the checker is right and the work takes a correction round; the
worker is right and the work lands on its reading; or the condition is wrong and the human amends it. **`approve`
takes the second** — the work lands as it stands, so the human refereed the disagreement in the worker's favour and
the checker's `FAIL` is overridden rather than answered.

**What that settles, precisely, and it is worth stating because it is a precedent.** The passage the checker failed
the work on — the spawn's *"the pointers the worker reads — its own node file, the effort's map, and the effort's
index of decisions"* — **stays as it is**, on the worker's reading that clause 4 does not reach a pointer and that
clause 6 therefore forbids touching it. **Nothing about the checker's reading is recorded as wrong**: it read the
same two clauses and split, which is the case the referee exists for.

**What it does not settle.** Whether that pointer bullet should say which part of the map a worker reads is now
nobody's node. The manager notes it and mints nothing: the human has just declined the repair, and minting a node
for the thing they declined would be the manager overriding the referee by another route. **If it wants doing, it
is theirs to ask for.**

*Both of the worker's flags are settled by the approval. The manager's own flag `215.3` below is not — it is about
the manager rather than the work.*

### Flag `215.3` — the manager's own, against itself

*Filed by the manager. Outstanding.*

**Two statements of the manager's, both false, both handed to this node's worker as fact.** Its own node file said
the counted-list item was *"the item node 204's retrospective reports for the fourth time"* — node 204's
retrospective states that item with **no count at all**, its *"fourth"* attaching to a different item. And this
node's spawn said that item *"is minted as a node"*; **no such node existed**, which the worker established by
checking every node from 211 to 221 and grepping every open node.

**The worker named the shape better than the manager can**, quoting the manager's own contract's ninth unsettled
question: *"An unestablished inference of yours, written into a node's question or into a spawn, arrives at the
worker as settled fact and hardens there."* **It acted on neither claim**, audited the file itself, and minted no
duplicate — so the cost was its checking time and nothing worse.

## Flags

*Both are the worker's own text, pasted. The ids are the manager's bookkeeping and nothing else. Both are settled
by the approval; the manager's own `215.3` above is not.*

`215.1` **· settled** `ASSUMPTION` — **`ASSUMPTION` — the spawn section's map pointer was read as outside clause 4.** Clause 4 forbids any sentence in the finished file stating or implying that the map is a single file. The spawn section lists *"the pointers the worker reads — its own node file, the effort's map, and the effort's index of decisions"*, placing the map between two things that are single files, which can be read as implying it is one too. I left it unreworded: it names a pointer rather than a file, the glossary entry two hundred lines above it now states the map's file count outright, and clause 6 forbids rewording text the earlier clauses do not reach. The alternative was to widen the pointer to name the map's files, which would have put filenames into the contract that ground rule 1 keeps out.

`215.2` **· settled** `ASSUMPTION` — **`ASSUMPTION` — one clause was added that the minimum fix did not require.** The entry now ends its file-count passage with *"material only one kind of reader acts on sits in a sibling of that part"*. Nothing in the condition demanded it; clause 1 demanded only that the cold-read file be called a part. I added it because an entry that calls the file a part and never says where the remainder is tells its reader less than the false version did, and because clause 3 governs *how* the entry may say where material sits — by role and position — which reads as anticipating that it does. The wording is `graph-conventions.md`'s own so the two files state one concept.

## Answer

*Pasted as the worker wrote it.*

The manager's contract's `map` glossary entry no longer equates the map with one file. Its opening clause *"in the one file every worker reads cold once per node"* is gone; in its place the entry states **"It is more than one file."** and then says the file every worker reads cold once per node **is a part of it, holding what every worker can act on**, with material only one kind of reader acts on sitting in a sibling of that part. One hunk, eight lines for six, in `.claude/skills/expedition/SKILL.md` and nowhere else.

**Every statement the condition required kept is kept, word for word**: the effort's whole shape at low resolution; the destination, the standing preferences, the fog with its gloss, and what is ruled out of scope; that it indexes decisions and never restates one; that the manager owns it; that two things live there and nowhere else, the ground rules and the standing steering; and that it holds a record of the bar's commands once discovered for this repo, which an agent confirms against the repo before using — the clause node 204 landed shortly before this node started. Nothing in the entry beyond the opening clause was reworded.

**No filename entered the entry.** Where the entry now says where the map's material sits it says so by role and by position only: *"the one every worker reads cold once per node"*, *"holding what every worker can act on"*, *"a sibling of that part"*. A filename would have assumed this effort's own file names, which ground rule 1 forbids and which `graph-conventions.md` — where an effort's file names belong — already carries.

**The sibling clause is an addition, and this is why it is there.** Telling a reader the cold-read file is a *part* and never telling them where the rest of the map is leaves the entry less useful than the false version it replaces. The condition's third clause anticipates the entry saying where the map's material sits, so saying it by role was the licensed route rather than an extra. Its wording tracks `graph-conventions.md`'s own — *"Each file of the map declares who reads it"*, and *"the part of the map that only the manager acts on"* — so a reader meets one concept across the two files rather than two wordings.

**The audit for the single-file claim reached the whole finished file.** Every occurrence of `map` was read. Eight sit outside the entry and none states or implies a whole-map read or a single file: two route the bar's commands and the code-slot count to *"the effort's map"*, one carries it as a spawn pointer, one as *"the bar by way of the map"*, one as the landing policy's home, two as the two counts' home, and one as standing steering's *"only durable home"*. The one judgement call in that audit is flagged below.

**The arithmetic audit, likewise over the whole finished file.** Thirty-four sentences carry a count. **Twenty-three introduce a list by stating how many items it holds, and every one is arithmetically correct** for the items its list then holds: *"there are five"* (the five kinds) = 5; *"two things live there and nowhere else"* = 2; *"Five parts, every time"* = 5 with *"a sixth, the gate payload"* = 6; *"Two things this protects."* = 2; *"Two things the human can say that are not answers"* = 2; *"Two things that travel in a spawn and are not yours"* = 2; *"two things, always both"* = 2; *"there are two such things"* = 2; *"Two things stay out"* = 2; *"Three outcomes, and no fourth"* = 3; *"exactly one of three places"* = 3; *"Raising a flag is two writes, in order"* = 2; *"Settling a flag is two writes too"* = 2; *"The four constraints on a condition you write yourself"* = 4; *"the two rules that bind every condition"* = 2; *"The queue has two tiers"* = 2; *"Tier 1 holds exactly three kinds of thing"* = 3; *"Three things are not claimants at all"* = 3; *"Two counts bound how much you start"* = 2; *"Steering from the human takes two forms"* = 2; *"Three states nothing in the files shows"* = 3; *"The first two you volunteer. The third you answer on request."* = 3; *"One limit of this contract"* = 1.

Eleven more count-bearing sentences were inspected and are outside the clause's predicate, being back-references or counts of something other than a list's length; each is nonetheless correct: *"which of the two was not met"*, *"Both are properties of the node's kind"*, *"the one word fixing how a piece of the record stands"*, *"the two markers"*, *"One of the human's two interfaces"*, *"each of the three outcomes"*, *"both procedures"*, *"tier 1 stays at three"*, *"neither of the agent's two entries"*, *"After two replacements, a third failure"*, and the heading *"Where two of these pull against each other"* — which sits over three bullets and counts the rules in each collision rather than the list's items, each bullet naming exactly two. That is the reading node 204's worker and its checker both took, and it is unchanged here. Six lists in the file state no count at all and so fall outside the predicate: the `What is never yours` table, the spawn's `It carries:`, the checker's `What it receives:`, the gate payload's bullets, the closing report's `It carries:`, and the nine items of `## What nothing here settles`.

**The work changed no count.** The entry's only counted list is *"two things live there and nowhere else"*, at two before the edit and two after. Node 204's checker reported 32 counted lists in this file against this pass's 34 count-bearing sentences and 23 in-predicate; the difference is what each pass called a counted list, not a disagreement about any arithmetic — no count in the file is wrong on either reading.

**The bar's command half was confirmed against the repo rather than trusted.** The repository root holds `.claude`, `.scratch`, `CONTEXT.md` and `.gitignore` and nothing else: no manifest, no task runner, no `.github`, no formatter configuration, no `CLAUDE.md` or `AGENTS.md` at the root or under `.claude`. So the repo states no commands of its own, and the rules file's record — no build, no tests, no formatter, no CI, one ignore file naming `.worktrees/` and `.claude/worktrees/` and invoking nothing — is accurate as written, with no difference to report and nothing for the repo's statement to win over. The bar is met on its non-command half: `/coding-principles` and `/naming`, the ground rules, the four standing rules for writing, `CONTEXT.md`'s `_Avoid_` lines (the `Map` entry refuses *index*, *plan* and *README*; the entry's kept *"indexes decisions"* is the verb and pre-existing), `graph-conventions.md`, `/writing-for-agents`, and the acceptance condition.

**No file under `.scratch/` was written and no second file was touched.** The sandbox did not refuse the write; the one edit under `.claude/skills/` went through sandboxed on the first attempt, and no override was needed on this node.

**What the worker reported its work invalidates**, pasted as it wrote it:

`none`. Node 204's four kept statements all survive verbatim, and node 76, which wrote this contract, is extended rather than contradicted.

**One tension I am reporting rather than calling an invalidation.** `graph-conventions.md`'s 500-byte paragraph still says *"every worker reads the whole map cold"*, which now reads oddly beside the manager contract's *"It is more than one file."* Node 194's worker met that exact sentence and left it deliberately, recording that the paragraph keeps *"its `map.md`-only scope and its 'the whole map', both correct there and both referenced by a mechanical check"*. On that scoping there is no contradiction, so I minted nothing and touched nothing: challenging it is a resolved node's business, not mine.

## Retrospective

*Filed by the manager in the same edit that resolves the node. Pasted as the worker wrote it — the first
retrospective on this effort whose items carry named standing items, the duty the human settled at node 212.*

Each item names the standing item it reports and how many times that name appears in the record, counted over `.scratch/graph-workflow` with `grep -ro`.

**1. What I had to hunt for.**

- *The size of every counted list in the finished file.* Standing item: **nothing indexes counted lists** — 1 occurrence of that exact name, 8 of *"counted list"*, all confined to nodes 204 and 215. I looked first at `decisions.md`, which indexes nothing of the kind. The fact came from grepping every number word and digit over 626 lines and then reading each of the ~90 hits by hand to sort 23 in-predicate lists from 11 back-references and the rest of the noise. Two tool calls and the single largest block of reading on this node, for a clause my four-line edit could not violate. Reporting the cost rather than absorbing it, as the spawn asked.
- *Whether any node already carries that item.* Same standing item, **nothing indexes counted lists**. I listed `nodes/`, read the heads of nodes 211 to 221, and grepped every open node for *counted* and *arithmetic*. None carries it.

**2. What arrived in my context that this node did not need.**

- *`map.md`, read whole.* Standing item: **read-and-unused** — 27 occurrences. I acted on three things in it: that a file the workflow ships is edited plainly rather than under never-delete, the standing preference narrowing density by document class, and that this effort declares ground rules. The worktree and sandbox history, the concurrency counts, the resume rule, the flag-settlement rule and the dogfood target bore on nothing for a one-entry glossary edit. What would have avoided it: `map.md` is already split by *reader* into two siblings, and the residue is still organised by *how a rule arose* rather than by what a worker acts on — a heading separating what binds a worker editing a shipped file from what binds the manager's own procedure would let a worker read one section. Node 141 already settles that no sweep is built and that the manager owes a disposition when this arrives.
- *`decisions.md`, read whole at 133 lines.* Same standing item, **read-and-unused**. I used four lines — nodes 204, 200, 194 and 142 — of which two mattered, and the other ~129 bore on nothing. The question I actually needed answered was *is there an open node on this passage*, which an index of **resolved** nodes cannot answer by construction; I answered it by grepping the open node files instead.
- *The contract's `### The raise` block and `## If you are a replacement attempt`.* Unused, and I would keep both: a worker cannot know it will not raise until it has finished.

**3. What would have made this node easier.**

- *In the spawn.* Note 2 was **the note that paid for itself** — 1 occurrence of that name. Telling me clause 5 reached the whole finished file *before* I opened the file meant I audited once instead of discovering the scope halfway and auditing twice. Note 1 did the same for the entry's current wording, and note 3 removed a decision by establishing the other three sites already agree. Keep this practice.
- *In the record.* Standing item: **nothing indexes counted lists**, and this is its second statement as a proposal. One convention retires the audit — a counted list is audited when that list is edited — which is exactly what `map-implementation-rules.md` already does for its own admission test with *"whoever is already editing a passage applies this to that passage"*. Node 204's worker proposed the same convention from the same clause shape.
- *In the node file.* Nothing missing. The condition was precise, satisfiable, and needed no raise.

**4. What I read that was stale, wrong, or contradicted something else.**

- Standing item: **unestablished inference** — 2 occurrences, both in the manager's own contract's ninth unsettled question, which names this exact shape: *"An unestablished inference of yours, written into a node's question or into a spawn, arrives at the worker as settled fact and hardens there."* Two instances arrived on this node. My node file's manager note says *"Nothing indexes counted lists — the item node 204's retrospective reports for the fourth time"*, but node 204's retrospective attaches *"this is the fourth"* to a **different** item, *"nothing indexes which open acceptance conditions touch which passages of a shipped file"*, and states the counted-list item with no count at all. And the spawn's note 2 says the counted-list cost *"is minted as a node"*; no node in the record carries it — I checked every node from 211 to 221 and grepped every open node. I acted on neither claim: I audited the file myself and minted no duplicate, leaving the disposition to whoever owns nodes 219 and 220.
- The spawn says the worktree *"sits at master (`1773ea2`)"*. `master` is at `54d03b3`. Record-only, so nothing in my work depends on it, but the landing policy's base check turns on exactly this comparison.
- `graph-conventions.md`'s *"every worker reads the whole map cold"* now reads oddly beside the entry I just corrected. Node 194 settled it as correct in its own scope; named under `INVALIDATIONS` above, not acted on.
