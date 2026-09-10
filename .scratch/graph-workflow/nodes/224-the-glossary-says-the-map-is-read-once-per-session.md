# The glossary's `Map` entry says the map is read once per session, where one of its files is read by no worker

Type: implementation
Status: resolved

Blocked by: none

## Question

*Surfaced by [The manager's contract defines the map as one
file](215-the-managers-contract-defines-the-map-as-one-file.md)'s worker, and pasted as it wrote it.*

> `CONTEXT.md`'s entry for **Map** reads *"The whole effort at low resolution, read once per session: the destination, the standing notes, the fog, and what is out of scope. It indexes decisions and never restates one."* The *"read once per session"* clause attaches a whole-map read to the term, and that is false of a map that is more than one file: the file holding the manager's own material is read by no worker at all, and the file holding an implementation node's rules is read only by that node's worker and its checker. This is the same defect node 215 removed from the manager's contract's `map` entry, and it survives on the very ground node 194 used to narrow the identical claim one file over — that node deliberately made *"Every worker reads `map.md` whole and cold"* precise in `graph-conventions.md` rather than widening it to *"the whole map"*, saying in its answer that *"the sibling holding the manager's material is read by no worker at all, so a widened 'the whole map' would have been false"* — and node 194 never reached `CONTEXT.md`. No open node covers this entry. The condition below deliberately scopes its arithmetic clause to counts the file states of its own contents rather than to every counted list in the file, because that is the cheap half and it is the half a glossary can get wrong; the expensive whole-file form is the standing item this node's own retrospective reports below.

**Blockers, in the worker's words:** none

## Acceptance condition

*Written by node 215's worker. Pasted as it wrote it, and not the manager's.*

> The work is one file, relative to the repository root: `CONTEXT.md`. The worker may edit that one and no other, and may not write any file under `.scratch/`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. That file's entry for the term **Map** no longer states or implies that the map is read once per session, and no longer states or implies that any reader reads the whole of it. Where the entry says what is read once per session, it says that what is read that way is a part of the map rather than the whole of it.
> 2. That entry keeps its statement of what the map is — the whole effort at low resolution, holding the destination, the standing notes, the fog, and what is out of scope — and keeps its statement that it indexes decisions and never restates one.
> 3. The entry names no particular filename. Where it says where the map's material sits, it says so by role and position only.
> 4. That entry's `_Avoid_` line is unchanged, character for character.
> 5. No entry for any term other than **Map** is added, removed or reworded, and no text outside the **Map** entry is deleted or reworded.
> 6. Any count the finished file states of its own contents — of its term entries, of its `_Avoid_` lines, or of anything else it enumerates about itself — is arithmetically correct for the finished file.
> 7. The finished file names no plugin, requires no skill to be invocable, and assumes no particular repository, machine or toolchain.
> 8. No file other than the one named above is modified, and no file under `.scratch/` is modified.
> 9. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Its author's own work is what made this reachable, and its author said why the defect survived so long.** Node
194 met the identical claim one file over and deliberately narrowed *"Every worker reads `map.md` whole and cold"*
rather than widening it to *"the whole map"* — recording that *"the sibling holding the manager's material is read by
no worker at all, so a widened 'the whole map' would have been false"* — and **node 194 never reached
`CONTEXT.md`**.

**Its clause 6 is deliberately narrower than its sibling nodes' arithmetic clauses**, and its author explained the
choice: it scopes the count check to *"counts the file states of its own contents"* rather than to every counted
list in the file, *"because that is the cheap half and it is the half a glossary can get wrong"*. **The expensive
whole-file form is the standing item its own retrospective names** — `nothing indexes counted lists`, which node
204's worker and this node's both paid for by hand.

**It is disjoint from [node 222](222-the-conventions-file-says-a-worker-reads-the-whole-map.md)**, which carries the
same defect in `graph-conventions.md`. Three files stated the map as one thing: the manager's contract, now
repaired; `CONTEXT.md`, this node; and the conventions document, node 222.

## Flags

*The worker's own text, pasted. The id is the manager's bookkeeping and nothing else. **Settled by the approval**,
the flag having been named in the payload the human answered.*

`224.1` **· settled** `ASSUMPTION` — The condition's clause 1 left the unit of the once-read open — it forbids saying the map is
read once per session, and where the entry keeps saying what *is* read that way it requires only that the thing read
be a part rather than the whole. I wrote *"read cold once per node"* rather than keeping *"once per session"* scoped
to a part. Ground: node 215's landed wording in the manager's contract says *"reads cold once per node"* for the
identical claim, so the two files now say one thing; the glossary's own **Node** entry defines a node as sized to
one agent session, making *per node* the file's own unit; and *session* is the reading under which the original claim
was false, the manager's session spanning many nodes. Decided rather than raised because the condition is
satisfiable either way and nothing outside this entry turns on the choice — but a checker reading clause 1's third
sentence as a requirement to *retain* a "once per session" statement, rather than as a condition on one, would find
that phrase absent, so it is flagged rather than left silent.

## Review

### Checker run 1 — `PASS`

*Pasted as the checker wrote it, in its own order. Every sentence is the checker's.*

> PASS
>
> **Read as the work.** The changed paths I established myself, not from the spawn: `git status --porcelain --untracked-files=all --ignored=matching` and `git diff --name-status HEAD` in `/home/mathieu/projects/graph-agent/.claude/worktrees/224-the-glossary-says-the-map-is-read-once` both return exactly ` M CONTEXT.md` — no untracked file, no ignored-but-modified file, nothing staged. `.scratch/` is tracked in this repo (232 files under `git ls-files .scratch`) and none of it is modified. The changed path is not one of the effort's record files, so the implementation-rules file's record-as-work rule does not fire; I read `CONTEXT.md` as the work under check and derived no statement of intent from it.
>
> **The moved standard, settled first.** `CONTEXT.md` is both the file under check and one of the standards the bar names, so I split the standard before checking anything else. Taking the standard's operative content as the set of things it requires or refuses — the bar names it as "`CONTEXT.md`'s `_Avoid_` lines" — the two sides are element-identical: 41 `_Avoid_` lines before and after, and every byte of the file outside the **Map** entry is unchanged (established by extracting `git show HEAD:CONTEXT.md`, replacing the Map block in each side with a sentinel, and comparing both the raw bytes and the paragraph-unwrapped text: identical, 62 paragraphs each). What moved inside the entry is the definitional prose of one term, not any refusal. On that reading the check survives and I carried on. Disclosing the reading, per the licence carried into my spawn ("Q1 ok Q2 ok"): **my outcome was reached on the reading that `CONTEXT.md`-as-standard's operative content is its `_Avoid_` refusals and its set of defined terms, both unmoved, and that the revised wording of one term's definition is not operative content of the standard.** On the wider reading — that a glossary's operative content includes each term's meaning — the operative content did move and my contract's branch would send me to a raise; the licence is what let me proceed instead.
>
> **One line per part of the condition:**
>
> 1. **Met.** The entry now reads, unwrapped: *"The whole effort at low resolution: the destination, the standing notes, the fog, and what is out of scope. It is more than one file and no reader reads all of it — the part every worker reads cold once per node holds what every worker can act on, and material only one kind of reader acts on sits in a sibling of that part. It indexes decisions and never restates one."* The word `session` does not occur in the entry; the once-reading is attributed to *"the part every worker reads cold once per node"*, explicitly a part, and *"no reader reads all of it"* is stated outright. The clause's second sentence I read two ways and it is met on both: vacuously, the entry no longer says "once per session" at all; substantively, what it says is read that way is a part rather than the whole.
> 2. **Met.** *"The whole effort at low resolution"* survives with all four items (destination, standing notes, fog, out of scope), and the final sentence *"It indexes decisions and never restates one."* is byte-identical to HEAD's.
> 3. **Met.** The entry contains no backticked token and no filename (checked against a grep for backticked spans, whose ten hits all sit outside the entry). Where it says where material sits it says *"the part every worker reads cold once per node"* (role) and *"a sibling of that part"* (position). Both are accurate against `graph-conventions.md`'s `## The seven files` and against the implementation-rules file's own opening.
> 4. **Met.** `_Avoid_: index, plan, README` — compared as `repr()` on both sides, byte-for-byte identical, no trailing-whitespace difference.
> 5. **Met.** Everything outside the Map entry is byte-identical (above), so no other entry was added, removed or reworded and no text outside the entry was deleted or reworded. The changed block contains the Map entry and nothing else. The entry's continued use of *"indexes"* is the pre-existing final sentence, unchanged, and the Map `_Avoid_` refuses `index` as a name for the map rather than the verb — checked by hand rather than by grep, per the measured trap.
> 6. **Met.** The finished file states no total of its term entries (51) or of its `_Avoid_` lines (41). The counts it does state of its own contents are `## The five kinds of node`, which holds exactly five entries (grilling, research, prototype, implementation, precondition), and *"three of them name a skill the worker invokes"*, which is three of those five. Both correct; the Map entry adds no count, *"more than one file"* being a claim about the map rather than a count of this file's contents.
> 7. **Met, on a stated reading.** The finished file names no plugin (a case-insensitive grep for `plugin` and `mattpocock` returns nothing), names no toolchain and no machine, and instructs no reader to invoke anything. The new text names no skill, no plugin, no path. Two pre-existing mentions sit outside the entry, where condition 5 forbade the worker to touch them: `/wayfinder` and `/expedition`, each naming the workflow being defined rather than requiring one to be invocable, and `.scratch/graph-workflow/nodes/`, a relative effort directory rather than a particular repository. I read 7 as satisfied on those; had I read them as breaches, the route would be a question rather than a `FAIL`, since the worker was forbidden to edit them.
> 8. **Met.** Established from the diff and from the full status, above.
> 9. **Met.** See the bar below.
>
> **What I ran for the bar, and what it printed.** I discovered the commands from the repo rather than taking the record's copy: the worktree root holds only `.claude/`, `CONTEXT.md`, `.gitignore` and `.scratch/`; a filter for `package.json`, `Cargo*`, `pyproject`, `Makefile`, `justfile`, `flake*`, `go.mod`, `.pre-commit*`, `tox*`, `setup*`, `requirements*`, `pom*`, `build.*`, `gradle*`, `.editorconfig`, `treefmt`, `biome`, `eslint`, `prettier` and `rustfmt` printed `NONE`; `ls .github` printed `No such file or directory`; `.claude/` holds seven skill directories and no `*.json`, so no settings and no hooks; `.gitignore` ignores `.worktrees/` and `.claude/worktrees/` and invokes nothing. There is no build, no test runner, no formatter and no CI, so there is nothing to run and the bar here is entirely its non-command half. This matches what the implementation-rules file records, so there is no repo/record difference to report.
>
> **Standards read, and which bore.** I read the implementation-rules file in the worktree for the standards and opened no other file beside it. It names: `/coding-principles`, `/naming`, `CONTEXT.md`'s `_Avoid_` lines, the effort's ground rules and its four standing rules for writing, `graph-conventions.md`, `/writing-for-agents`, and the acceptance condition. It names **no reviewing skill**, so I ran no reviewing skill and went looking for none; nothing was delegated to a subagent, so the blindness constraint on delegated parts never arose. What bore: `CONTEXT.md`'s `_Avoid_` lines (no refused word enters the new text — `session`, `run`, `plan`, `item`, `report`, `question` all absent, and `index` only as the unchanged verb); `graph-conventions.md`, against which the entry's role-and-position description of where the map's material sits is accurate; `/writing-for-agents`, which the entry meets — the added text is shape rather than explanation, it duplicates no neighbouring file's content, and it restates no environment lookup; and the four standing rules, of which rule 1 (never compress the shapes) and rule 4 (no line numbers) bear and hold. What did not bear: `/coding-principles` and `/naming`, the change being three sentences of prose introducing no identifier and no code.
>
> **The acceptance condition records no enumerator**, so there was no command of its own to run as written.
>
> ```
> QUESTIONS:
> - A file beside the one the condition names still carries the wording the condition removed, and the
>   worker could not touch it: `.claude/skills/expedition/graph-conventions.md`, under `## The seven
>   files`, describes `map.md` as *"The whole effort at low resolution. Read once per session."* — the
>   glossary's superseded phrasing, in a shipped standard whose own opening says *"Terms are used exactly
>   as the glossary (`CONTEXT.md`) defines them."* It is not false of `map.md`, but the two documents now
>   differ in vocabulary for the same read (`per session` there, `per node` in the revised entry and in
>   the implementation-rules file's *"read whole, cold, once per node by every worker"*), and `session` is
>   a word `CONTEXT.md` refuses on both its **Effort** and **Attempt** entries. Condition 8 confined the
>   work to `CONTEXT.md`, so this was the condition's own scope and not the worker's to depart from;
>   whether the shipped conventions document should follow is for the human.
> ```

*No `NOT COVERED`. One question, and it lands on [node
222](222-the-conventions-file-says-a-worker-reads-the-whole-map.md), which already holds
`graph-conventions.md`'s statement that a worker reads the whole map — the manager has filed it there.*

### Gate — `approve`

**The human's word, `verbatim`.**

> approve

**What it decided.** `approve` on a `PASS`ing tree lands the work as it stands, including flag `224.1`'s choice of
*once per node* over the condition's permitted *once per session scoped to a part*. **The flag is settled by the
approval.**

**What travelled with the payload and is not decided by a word about the work.** The checker's one question — that
`graph-conventions.md` still describes `map.md` as *"Read once per session"* in a shipped standard whose own opening
says terms are used exactly as this glossary defines them — is filed on [node
222](222-the-conventions-file-says-a-worker-reads-the-whole-map.md), which already holds that file's account of how
the map is read. It needed no answer to land this work.

**One thing the manager repaired in the record at this landing, on this node's worker's finding rather than its
work.** `map.md` stated that `CONTEXT.md` holds *"50 term entries and 40 `_Avoid_` lines"*, measured at node 29. The
true figures are **51 and 41**, established twice here — by this node's worker and independently by its checker —
and **wrong before this node's own edit**, which added neither an entry nor an `_Avoid_` line. Struck in place with
the corrected figures, dated, and marked non-authoritative under node 183's rule. The worker's own observation on
why its condition could not catch this is in its retrospective: the wrong count was one file away, in `map.md`, and
outside every clause it was given.

## Answer

*Pasted as the worker wrote it.*

`CONTEXT.md`'s entry for **Map** no longer attaches a whole-map read to the term. The clause *"read once per
session"* is gone from the entry's opening sentence, and in its place the entry states that the map is more than one
file, that no reader reads all of it, and that what is read cold once per node is *the part every worker reads* —
leaving the sibling holding one kind of reader's material outside that read. The entry keeps, unchanged in
substance, its statement of what the map is (the whole effort at low resolution: the destination, the standing
notes, the fog, and what is out of scope) and its statement that it indexes decisions and never restates one. Its
`_Avoid_` line is untouched, character for character.

The entry's new wording is:

> The whole effort at low resolution: the destination, the standing notes, the fog, and what is out of scope. It is
> more than one file and no reader reads all of it — the part every worker reads cold once per node holds what every
> worker can act on, and material only one kind of reader acts on sits in a sibling of that part. It indexes
> decisions and never restates one.

Three calls inside it a later reader would otherwise re-derive.

1. **"once per node", not "once per session".** The condition's clause 1 permits the entry to keep saying what is
   read once per session so long as what is said to be read that way is a part rather than the whole. It was
   sharpened instead to *once per node*, on three grounds: node 215's landed repair of the manager's contract's
   `map` entry says *"The one every worker reads cold once per node is a part of it"*, and this entry is the same
   claim in the glossary; the glossary's own **Node** entry already fixes a node as *"sized to one agent session"*,
   so *per node* is the file's own unit and *per session* is the looser paraphrase of it; and *session* is the
   reading under which the original claim was false in the first place, the manager's session spanning many nodes
   and taking in the sibling no worker reads. This is the `ASSUMPTION` flag above.
2. **Position by role, never by filename.** Clause 3 forbids naming a file, so the entry locates material as *"the
   part every worker reads cold once per node"* and *"a sibling of that part"* — the same two role-and-position
   phrases node 215 used, which keeps the glossary and the manager's contract saying one thing in one vocabulary.
3. **No node citation was added inside the entry.** The four standing rules for writing ask an item to cite the
   nodes that shaped it, but no entry in this glossary cites one: the file's own header states that *"the reasoning
   behind each one lives in the node that settled it"*, and a citation would be a link to a filename, which clause 3
   forbids. The rule is satisfied at the file's level rather than the entry's, and this is deliberate rather than an
   omission.

Clause 6 raised no collision with clause 5. The only count `CONTEXT.md` states of its own contents is the heading
`## The five kinds of node`, and five kind entries sit under it in the finished file. The file states no count of
its term entries or of its `_Avoid_` lines, so nothing outside the **Map** entry needed rewording to keep an
arithmetic claim true, and nothing outside it was touched. Measured for the record: the finished file holds **51
term entries and 41 `_Avoid_` lines** — `map.md` says 50 and 40, a stale record outside this node's scope and
reported below.

The bar's non-command half was confirmed against the repo rather than trusted from the record: no manifest, no task
runner, no CI directory, no formatter config, and the one ignore file, `.gitignore`, holds exactly the two entries
the record describes (`.worktrees/` and `.claude/worktrees/`) and invokes nothing. The record and the repo agree;
there is no difference to repair.

**What the worker reported its work invalidates:** `none`.

**What the worker surfaced as new nodes:** `none`.

## Retrospective

*Filed by the manager in the same edit that resolves the node, the duty the human settled at [node
212](212-the-mint-on-second-report-rule-is-defeated.md). Pasted as the worker wrote it.*

1. **What I had to hunt for.** Node 215's landed wording — the thing this node most needed, since its whole job is
   to say in the glossary what 215 already said in the manager's contract. Nothing pointed at it. The node file and
   the spawn both cite node 215 as the *author* of my condition and as having *removed the same defect*, but neither
   quotes the replacement text, so I grepped `.claude/skills/` for `once per node` and found it at `SKILL.md`'s
   `map` entry. I looked first at `decisions.md`'s line for 215, which says the shape of the repair (*"the cold-read
   file becomes a part of it, named by role and never by filename"*) but not the sentences, so it cost a read
   without answering. Second, the bar's commands: `map-implementation-rules.md` records them, and the contract
   requires confirming the record against the repo, which took one directory listing plus the ignore file — cheap
   and correctly placed. Nothing else was hunted.

2. **What arrived in my context that this node did not need.** `map.md`, read whole and cold, is where the weight
   is. This node is a four-line prose edit to one glossary entry, and of that file's ~45 standing preferences and
   notes exactly two bore on the work: the note that `CONTEXT.md` is the glossary whose `_Avoid_` lines bind, and
   the retrospective rule that produced this section. The long items on resumption, on flag settlement, on the
   one-question-at-a-time rule, on the human being the scarce resource, on token priority, on the manager never
   idling, and the whole `Notes` account of what the manager must carry are addressed to the manager and reach no
   worker's decision — they are the same class of material as the manager-only sibling that node 139 already moved
   out, and the honest arrangement would be a second cut of `map.md` along the same line 139 used: what a *worker*
   acts on against what the *manager* acts on. One heading would have saved most of it.
   `map-implementation-rules.md`, by contrast, was almost entirely load-bearing after its 56.7% cut; the one part I
   did not need was the checker-facing rule on reading changed paths as the work, which binds the checker and not
   me. From my spawn, the pointer to decisions 142 and 204 fed nothing: 142 is `graph-conventions.md`'s map shape
   (node 222's file, which I must not touch) and 204 is the bar-commands demotion, which my contract already states
   in full. And I went to `decisions.md` for four lines and took the file.

3. **What would have made this node easier.** Two things, both small. The node file quotes the defective sentence in
   full — which is why I never had to guess what I was repairing — and it should have quoted the *repaired* sibling
   sentence beside it, since the condition demands consistency with a wording it does not contain. One line in the
   spawn (`node 215 landed: "It is more than one file. The one every worker reads cold once per node is a part of
   it…"`) would have removed the only hunt this node had. Second, the condition's clause 1 mixes a prohibition with
   a conditional permission about the same phrase, and the flag above exists only because of that seam: had it said
   *"the entry may say that a part is read once per node or once per session, and must not say the map is"*, there
   would be nothing to flag.

4. **What I read that was stale, wrong, or contradicted something else.** One item, and it names the record.
   `map.md` states that *"`CONTEXT.md` holds 50 term entries and 40 `_Avoid_` lines"*, measured at node 29. The file
   holds **51 and 41** — and held those before my change, which added no entry and no `_Avoid_` line. This is the
   standing item `nothing indexes counted lists` landing for at least the third time on this effort, node 204's
   worker and this node's author having both paid for it by hand; under the map's own rule that the second report of
   the same standing item mints a node, it is past due. Note also the pleasing near-miss: my condition's clause 6
   was written narrowly, to counts a file states *of its own contents*, and it caught nothing, because the wrong
   count about `CONTEXT.md` is not in `CONTEXT.md` — it is in `map.md`, one file away and outside every clause I was
   given. The cheap half is cheap because it checks the file that rarely lies about itself.
