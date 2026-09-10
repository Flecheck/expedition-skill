# Move the landing section out of the file an implementation worker reads

Type: implementation
Status: resolved

Blocked by: none

## Question

*Minted by the manager under the map's rule that a standing retrospective item reported a second time becomes a node.
**This is its sixth report**, and the manager missed the first five.*

`map-implementation-rules.md`'s opening paragraph declares its readers to be **an implementation node's worker and its
checker**, and says it exists so that *"no other worker pays to read it"*. Roughly 125 of its ~185 lines are
`## Landing an implementation node's work` — worktree creation, base checks, rebase forensics, sandbox mounts, merge
and cleanup. **None of it is anything a worker or a checker does.** It is the manager's lifecycle material, and
[node 139](139-move-the-managers-material-out-of-the-map.md) built `map-manager-only.md` for exactly this class.

**The reports, all in workers' own words:**

- [node 144](144-make-the-rules-file-stand-alone.md): *"it is the manager's material sitting in the worker's file, and
  it survived node 140's move because node 140 moved by source rather than by reader."*
- [node 163](163-a-condition-demands-facts-the-checker-does-not-read.md): *"a spawn pointer to `## What the work is
  held against` would have avoided it."*
- [node 167](167-the-checkers-bar-commands-route.md): *"Roughly sixty lines of git diagnostics bearing on nothing a
  grilling worker does."*
- [node 171](171-carry-the-record-node-reading-rule-into-the-rules-file.md): *"nothing in this file says which
  paragraphs a checker holds work against and which are the manager's lifecycle instructions."*
- [node 126](126-carry-question-batching-into-the-grilling-contract.md): *"My spawn warned me and I still took it
  whole, because `Read` on a file is whole-file: **the warning cannot fix this, and the arrangement can.**"*
- [node 177](177-carry-question-batching-into-the-glossarys-grilling-entry.md): *"on the same counting this is at
  least the fourth. The fix has not changed."*

**What is open** is only the shape of the move, the destination being named by the reports themselves.

## Acceptance condition

*The manager's own. Marked as the manager's, and read back against the two rules that bind every condition before this
node may be claimed: it is self-contained text, and it quantifies over no part of the record — every demand below
names a file, a heading or a string.*

> The work is `.scratch/graph-workflow/map-implementation-rules.md` and
> `.scratch/graph-workflow/map-manager-only.md`. No other file may be edited. The worker may not mark this node,
> resolve it, or write a line in `decisions.md` or in `flags.md`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. The whole of the section headed `## Landing an implementation node's work`, from that heading to the line before
>    the next `##` heading, is in `map-manager-only.md` and no longer in `map-implementation-rules.md`. Its text is
>    byte-identical to what `map-implementation-rules.md` held: no paragraph, bullet or struck passage is reworded,
>    renumbered, reordered or unstruck.
> 2. `map-implementation-rules.md` holds, in place of that section, a pointer of at most three lines naming
>    `map-manager-only.md`, saying that it holds how an implementation node's work is landed, and saying that landing
>    is the manager's and bears on neither a worker nor a checker. It restates no part of the moved section.
> 3. `map-implementation-rules.md`'s opening paragraph states that everything remaining in the file is held against a
>    worker's work, so that a reader who has read the file has read only what binds them.
> 4. No text is deleted from either file: the moved section is deleted from its origin only in the sense that it is
>    present, byte-identical, in its destination.
> 5. Nothing under the heading `## What the work is held against` changes, and no numbered rule in either of the two
>    blocks that heading holds — the five ground rules, and the four standing rules for writing — is reworded,
>    renumbered or reordered.
> 6. Every markdown link in both files resolves to a path that exists. Links inside the moved section resolve from
>    its new location.
> 7. No file outside `.scratch/graph-workflow/` is modified.

## The manager's note at filing

*Not a change to anything above.*

**The condition above is the manager's own**, this node having been minted by the manager rather than by an agent.
What it demands is a byte-identical move plus a pointer; it decides nothing that is open, and it deliberately does
**not** say where in `map-manager-only.md` the section goes, that being the worker's to place.

**The manager's own conduct is part of the subject.** The map's rule is that the second report of a standing item
mints a node. Six reports arrived and the manager minted nothing until now, which is the same failure [node
183](183-nothing-measures-the-record-about-itself.md) records against four reports of a different item. **Two
independent standing items have now each been missed five or more times**, which is evidence about the rule rather
than about either item.

## Review

### Checker run 1 — `PASS`

*Pasted as the checker wrote it, in its own order. Every sentence is the checker's.*

> I have everything. Here is my outcome.
>
> ---
>
> **Settled first, per my contract's *"Where the work moved one of them"* branch.** `map-implementation-rules.md` is both a path under check and the file my contract sends me to for standards, and this work removes 128 lines from it. I read my standards from the unmodified copy at `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md`, outside the worktree, and compared the operative sets element by element on both sides.
>
> **The sets are identical, so the check proceeded.** Ground: every standard the file states — the bar's commands (none for this repo, a complete bar), the bar's non-command list, the review route's standards list, the record-under-check rule, the five ground rules, the four standing rules for writing — lives under `## What the work is held against`, and that heading onward is byte-identical across the change (`sha256 7a2a3364930339a791da6ae6903c6b66659341376efbab63f5cab846510a657d` on both sides, `cmp` clean). What the work removed, `## Landing an implementation node's work`, requires and refuses nothing of an implementation node's deliverable — it states the manager's worktree/commit/rebase/merge procedure and that procedure's sandbox costs — and is not among the standards the file's own `## What the work is held against` enumerates. What the work added (one sentence of file scope, one 3-line pointer) adds no element either. So no operative element was added, removed or altered, and reading the standards from either side would have yielded the same set. No raise.
>
> ```
> PASS
> ```
>
> **I read the changed paths as the work under check, under the record-under-check rule** in `## What the work is held against` ("An implementation node's work on this effort may be the effort's own record"). I derived no statement of intent from their content; the acceptance condition as given was my only statement of intent.
>
> **Scope, before the clauses.** `git status --porcelain` in the worktree returns exactly ` M .scratch/graph-workflow/map-implementation-rules.md` and ` M .scratch/graph-workflow/map-manager-only.md`; `--untracked-files=all` returns nothing. `decisions.md`, `flags.md`, `map.md` and every file under `nodes/` — including `nodes/188-move-the-landing-section-out-of-the-workers-file.md` — are unmodified. So "no other file may be edited" and the bar on marking/resolving/writing `decisions.md` or `flags.md` both hold.
>
> **Clause by clause:**
>
> 1. **Met.** `## Landing an implementation node's work` is absent from `map-implementation-rules.md` (`grep -n '^## '` returns only `## What the work is held against`) and present in `map-manager-only.md`. Extracted the section from `git show HEAD:` origin (lines 28–155, to the line before `## What the work is held against`) and from the worktree destination (lines 46–173, to the line before `## Not yet specified`): 128 lines and 16619 bytes each, `sha256 a1bac90236c5656cc0c9a50385369d0cb84fcfac0be54a4a82a9299a5dc838e5` on both, `cmp` reports no difference. Byte-identity settles reworded/renumbered/reordered/unstruck mechanically.
> 2. **Met.** The pointer is 3 lines, names `map-manager-only.md` as a resolving link, says it holds how an implementation node's work is landed, and says landing is the manager's and bears on neither a worker nor a checker. It sits where the section was, immediately before `## What the work is held against`. Its only addition beyond the clause is a citation to node 188 — no part of the moved section is restated.
> 3. **Met.** The opening paragraph now carries "**Everything remaining in this file is held against a worker's work**, so a reader who has read the file has read only what binds them."
> 4. **Met, and established as insertion-only rather than by eye.** For `map-manager-only.md`, `diff -u` of the HEAD version against the new version with the inserted section excised shows additions only — one provenance paragraph before `## Notes` — and no deletion. For `map-implementation-rules.md`, `diff -u` of the HEAD version with the section excised against the new file shows two additions and one changed line; a character-level `difflib` opcode dump of that line reports a single `insert` at offset 410 and no `delete` or `replace`, so no old text was dropped. The section's deletion from origin is discharged by the byte-identity in clause 1.
> 5. **Met.** `## What the work is held against` onward is byte-identical (`cmp` clean, hash above), which covers the five ground rules and the four standing rules for writing inside it.
> 6. **Met.** Extracted every `](...)` target from both files after unwrapping with `tr '\n' ' '`, so targets split across a line break would surface as misses; 18 distinct targets in `map-implementation-rules.md` and 46 in `map-manager-only.md`, all resolving to existing paths, none missing. The moved section's links resolve from the new location because both files sit in `.scratch/graph-workflow/`, confirmed by resolving them from there. I also checked the section's six internal `*above*`/`*below*` references and all six resolve inside the section itself, so the destination's claim about them is accurate and the placement between `## Notes` and `## Not yet specified` breaks nothing the clauses reach.
> 7. **Met.** Only the two `.scratch/graph-workflow/` paths are modified, per the status above.
>
> **The bar.** Confirmed against the repo rather than taken from the spawn. `git ls-tree --name-only HEAD` returns only `.claude`, `.gitignore`, `.scratch`, `CONTEXT.md`. A `git ls-files` sweep for manifests, lockfiles, task runners, formatter configs and CI (`package.json`, `Cargo.toml`, `pyproject.toml`, `Makefile`, `justfile`, `Taskfile`, `flake.nix`, `.pre-commit-config.yaml`, `.prettierrc*`, `.editorconfig`, `rustfmt.toml`, `.markdownlint*`, `.github/*`, and others) printed `(no manifest, task runner, formatter config or lockfile tracked)` and `(no CI config tracked)`; a test-path sweep printed `(no test files tracked)`. The one ignore file, `.gitignore`, ignores `.worktrees/` and `.claude/worktrees/` and invokes nothing. So there is no command to run, and under the *"if relevant"* clause that is a complete bar on its remaining half. `git diff --check` prints nothing.
>
> Non-command half, held against the authored delta — three short passages, the rest being byte-identical moved text the standard does not bite on. `CONTEXT.md`'s `_Avoid_` lines: checked the distinctive refusals by hand as the standards' recorded trap directs, no hit; the ordinary-English third I did not grep. `/writing-for-agents`: read it and applied it myself — the change is a textbook progressive-disclosure move, the pointer front-loads its leading words, states what the material is and encodes the condition for reaching it, and restates no part of the target; the negations present ("bears on neither a worker nor a checker", "not into `map.md`") are paired with the positive target and are the condition's own words. Four standing rules for writing: all four met — the why is compressed and no shape is, both pointers state current form and cite node 188 without restating it, the moved section keeps its own heading in the destination, and no citation added anywhere uses a line number. Ground rules 3, 4 and 5 met; ground rules 1 and 2 do not bite, both being about shipped files where these two paths are `.scratch/` record files. `/coding-principles` and `/naming` do not bite: no code and no new identifier. `graph-conventions.md` bites and produced the question below. **No reviewing skill is named for this repo** — the standards say so in as many words — so I ran none, went looking for none, and spawned no agent, which means the limit on what a skill delegates never engaged.
>
> ```
> QUESTIONS:
> - Complying with clause 1 and clause 7 together makes two statements outside `.scratch/graph-workflow/`
>   false, and the worker could repair neither, the condition saying "No other file may be edited".
>   `.claude/skills/expedition/graph-conventions.md` — itself named among the standards — states that
>   `map-implementation-rules.md` "holds the rules an implementation node's work is held to — the landing
>   policy, the bar's commands and the standards work is held against"; the landing policy is no longer
>   there. And `.gitignore`'s comment reads "See .scratch/graph-workflow/map-implementation-rules.md,
>   \"How the worktree is made\"" — a citation in exactly the by-quoted-phrase form standing rule 4
>   prescribes, whose phrase now resolves to nothing in the file it names and appears once in
>   `map-manager-only.md`. Where the section now sits is right by `graph-conventions.md`'s own account of
>   `map-manager-only.md` ("the part of the map that only the manager acts on"), so what has gone stale is
>   the origin's description rather than the destination's. Both wordings are the condition's own scope and
>   so were not the worker's to depart from, which is why this is a question and not a `FAIL`: I considered
>   `FAIL: the bar` on `graph-conventions.md` and set it aside on my contract's routing — the work complies,
>   and complying is what produced the defect.
>     Form, as a predicate: a file outside `.scratch/graph-workflow/` that cites
>   `map-implementation-rules.md` for content the move relocated, whether by quoted phrase or by describing
>   what that file holds.
>     Extent, as a bounding set, since no enumerator over the implementer's editable region can reach it —
>   the implementer may edit only the two files under check and neither holds an instance. I ran
>   `git ls-files -- . ':!:.scratch' | xargs -r grep -ln 'map-implementation-rules'` in the worktree, which
>   returned four files, and read the citing passage in all four. Two are instances, as above. Two are not:
>   `.claude/skills/expedition-checker/SKILL.md` and `.claude/skills/expedition-implementation/SKILL.md`
>   cite the file by path and by role only, naming no relocated content. That set is provably complete for
>   files outside `.scratch/`. It does not cover citations from inside `.scratch/graph-workflow/`, which is
>   the record I am blind to and did not sweep — so the two instances are what resolve to nothing in the
>   files I hold, and whoever holds the record settles whether more exist there.
> ```
>
> Nothing in the condition went uncovered — I am filing no `NOT COVERED` entry.
>
> Two observations that are not findings and do not bear on the outcome, offered because you asked me not to read the condition charitably on your behalf. Clause 2 bounds the pointer by "at most three lines", and this file mixes one-long-line paragraphs with paragraphs wrapped near 120 columns, so the same bound admits a pointer roughly a hundred words long or one roughly four hundred depending on wrapping style; it is checkable, so I checked it as written, and the pointer is short by either measure. Separately, clause 1's boundary — "to the line before the next `##` heading" — captured the two blank lines that stood before `## What the work is held against`, so the destination now carries two blank lines before `## Not yet specified`; that is compliance with the boundary as the condition drew it, not a defect. I also satisfied myself that the rules file's own `How a rule in this file is superseded` procedure does not fire here and demands no `map-history.md` append: this section still holds and merely changed file, which is not supersession.

*No `NOT COVERED`. One question, carried to the human with the gate.*

### Gate — `approve`

**The human's word, `verbatim`.**

> approve

**What it decided.** The gate asked for `approve`, `correct` or `reject` on a `PASS`ing tree. `approve` lands the
work as it stands: the byte-identical move, the three-line pointer, the added scope sentence, and the unrequested
provenance paragraph flag `188.2` discloses — that paragraph was named in the payload as cheap to remove, and the
approval keeps it.

**What it did not decide, and the manager is not treating as decided.** Two things travelled with the payload and
neither is answered by a word about the work.

- **The checker's question** — that complying with clauses 1 and 7 together made `graph-conventions.md`'s gloss and
  `.gitignore`'s quoted-phrase citation false, with no route for this node's worker to repair either. It needed no
  answer to land the work and it is held elsewhere: it is filed verbatim on [node
  198](198-two-files-describe-the-rules-file-by-contents-node-188-removes.md), whose subject it is, and which this
  node's resolution unblocks.
- **The grilling node this node's worker surfaced** — whether `map-manager-only.md` gets an admission test now that
  it holds the landing section's history. Minted at [node
  225](225-whether-map-manager-only-gets-an-admission-test.md) and unclaimed; it is the human's question to answer
  when it reaches them, and the approval of a move is not an answer to it.

*Both of the worker's flags are settled by the approval — the placement it chose and the provenance paragraph it
added were the two things the payload put in front of the human, and both stand.*

## Flags

*Both are the worker's own text, pasted. The ids and the settlement are the manager's bookkeeping and nothing else.*

`188.1` **· settled** `ASSUMPTION` — **Where in `map-manager-only.md` the section sits.** The condition deliberately
left the placement to me and I chose immediately after `## Notes`, before `## Not yet specified`, as its own `##`
section. The ground is that the destination file runs settled material first and unsettled material (fog, then out
of scope) after, and landing is settled operative procedure; a top-level heading also keeps standing rule 3's
navigate-by-heading property that the section had in its origin. The alternatives were before `## Notes` — rejected
because the file's opening says *"Everything below binds this effort exactly as it did in `map.md`"* and reads as an
introduction to the Notes — and at the end of the file, rejected because it buries a procedure the manager runs
behind two sections of things nobody acts on.

`188.2` **· settled** `ASSUMPTION` — **A provenance paragraph was added to `map-manager-only.md` that the condition
did not ask for.** The condition demanded a pointer in the origin and said nothing about the destination. I added
one paragraph to the destination's opening block recording where the section came from, that it is byte-identical,
why it moved, and that its relative words resolve inside itself. The ground is standing rule 2 — an item cites the
nodes that shaped it — and the precedent of nodes 139 and 140, which both left exactly such an account in the
destination's opening; without it the largest section of a manager-only file has no citation and a reader cannot
tell it was moved rather than written there. It is three sentences and deletes nothing, so it is cheap to remove if
unwanted.

## Answer

*Pasted as the worker wrote it.*

The whole of `## Landing an implementation node's work` — 128 lines, 16,619 bytes — now lives in
`map-manager-only.md` and is gone from `map-implementation-rules.md`. Three lines stand where it was, and the rules
file fell from 197 lines / 28,590 bytes to 73 lines / 12,370 bytes: **a 56.7% cut to what every implementation
worker and every checker reads**, on the file whose own opening declares those two its only readers.
`map-manager-only.md` rose 17,162 → 34,160 bytes, paid by the one reader who acts on the material. (Derivation, run
in the worktree: `wc -l -c` on both files, against `git show HEAD:<path> | wc -l -c`.)

**Where it went, which the condition left to me.** Immediately after `## Notes` and before `## Not yet specified`,
as its own `##` section at destination lines 46–173. The ground is that `map-manager-only.md` runs
settled-then-unsettled — `## Notes` holds standing material the manager acts on, and `## Not yet specified` and
`## Out of scope` hold fog and exclusions. Landing is settled operative procedure, so it joins the settled half
rather than sitting behind the fog; keeping it a top-level heading satisfies standing rule 3, a long answer being
navigable by heading. Nothing was placed before `## Notes`, so the out-of-scope line's *"The Notes above"* — which
that file's own opening warns points into `map.md` — is untouched.

**Byte-identity was discharged by diff, not by reading.** `sed -n '46,173p' map-manager-only.md | diff -
<extracted section>` returns zero differences; the extract came from `sed -n '28,155p'` of the file at `HEAD`. The
section's two trailing blank lines travelled with it, the section being defined as the heading through the line
before the next `##`.

**The pointer carries no heading of its own.** Clause 1 moved the heading out, so the three lines sit as a pointer
paragraph among the file's other opening paragraphs — the same shape `map.md` uses for its own four pointers. It
reads: *"**How an implementation node's work is landed is in [map-manager-only.md](map-manager-only.md)**: landing
is the manager's, and it bears on neither a worker nor a checker. Moved there by [node 188](…)."* It names no
worktree, no rebase and no sandbox, so it restates no part of the moved section.

**Clause 3 was added, not substituted.** One sentence went into the opening paragraph — *"**Everything remaining in
this file is held against a worker's work**, so a reader who has read the file has read only what binds them."* —
leaving every prior word of that paragraph in place. That matters under node 189: had it *replaced* a live rule
statement, the superseded text would owe a verbatim append to `map-history.md`, and this condition permits no third
file. Nothing in the old sentence became false, so nothing was owed.

**One addition the condition neither demanded nor forbade**, flagged below: a provenance paragraph at
`map-manager-only.md` line 11, in the opening block where that file already keeps its account of itself. It says
where the section came from, that it is byte-identical, that landing is the manager's rather than a worker's or a
checker's, and that its own *above* and *below* words resolve inside the section rather than into `map.md`. The
ground is standing rule 2 and the precedent of nodes 139 and 140, both of which left the destination-side account in
the destination's opening.

**Held against `/writing-for-agents`, which cost two prunes.** The first drafts of the pointer and the provenance
paragraph each carried a clause the other already held — *"the part of the map no worker reads"* beside *"bears on
neither a worker nor a checker"*, and a restated reason in the destination. Both went, on the single-source-of-truth
rule and the no-op test. What survives is a mirrored pair stating the same split from each reader's side, which is
what lines 3 of the two files already do.

**Relative words, checked in both directions and none broken.** Inside the moved section every *above* / *below*
resolves within the section, including line 105's *"Two earlier accounts of it in this file were wrong and are
struck below"* — those two struck accounts travelled with it, so *"in this file"* now truthfully names
`map-manager-only.md`. In the rules file all ten survivors still resolve: the opening's *"The struck rule statements
below"* still has referents (three struck passages remain, in the bar and review-route paragraphs), and node 200's
paragraph names two instances that both survive with their targets unmoved.

**The bar, confirmed against the repo rather than trusted.** The record's claim holds exactly: no manifest, no task
runner, no CI, no `CLAUDE.md` or `AGENTS.md` anywhere in the tree, and `.gitignore` is the one ignore file, carrying
both `.worktrees/` and `.claude/worktrees/` and invoking nothing. The command half is empty and the record needs no
repair. The non-command half was applied: `/writing-for-agents` (above), `CONTEXT.md`'s `_Avoid_` lines checked by
hand against my ~5 new sentences, the five ground rules (this is record rather than a shipped file, so 1, 2 and 5 do
not reach it), and the four standing rules for writing. All 96 markdown links in the two files resolve to paths that
exist.

**What the worker reported its work invalidates**, pasted as it wrote it:

No resolved node is contradicted. Three **open** nodes' acceptance conditions are now unsatisfiable or wrong as
written, because each anchors on text that was in `map-implementation-rules.md` and is now in
`map-manager-only.md`. None was mine to repair — a condition is not the worker's to rewrite, and all three sit
outside my own condition's two-file scope.

- **Node 152** (*Where the harness worktree instruction lives*) — **unsatisfiable as written.** It requires the
  `**A worktree is created by the harness, never by hand.**` paragraph to land in `map-implementation-rules.md` *"in
  the section holding the paragraph beginning `**Landing policy**`, and immediately after it"*, and it permits
  editing only `map.md` and `map-implementation-rules.md`. That section is now in a third file its worker may not
  touch. Its clause that *"the landing policy's own phrase `see the standing instruction immediately below` resolves
  to that paragraph's new position"* names a phrase that also moved. The natural repair points the whole node at
  `map-manager-only.md`, which is a change of place rather than an addition, so it likely exceeds node 82's
  manager-amendment authority.
- **Node 160** (*Carry the integration-conflict rule into the map*) — **satisfiable after a smaller repair.** Its
  clause 1 names *"In `map-implementation-rules.md`, inside the paragraph beginning `**Landing policy**`"* and its
  clause 7 names *"The sentence in `map-implementation-rules.md` reading `The graph's own files are *not* committed
  per node…`"*. Both sentences are now in `map-manager-only.md` — which that node's file list already permits, its
  clause 6 making a demand of it. Only the two file names in clauses 1 and 7 are wrong.
- **Node 186** (*An implementation worker tests its worktree*) — **its anchor is gone, not its destination.** It
  requires a bullet in `map-implementation-rules.md` *"placed in the same list that already holds that file's
  sandbox material"*, and that *"No file other than `.scratch/graph-workflow/map-implementation-rules.md`
  changes."* After the move there is **no sandbox material left in that file at all** (`grep -in 'sandbox'
  map-implementation-rules.md` returns only the `.worktrees/` mention inside the bar paragraph). The destination is
  still right — node 186's bullet instructs the *worker*, so the admission test puts it in the rules file — but it
  now has no list to join and needs a new anchor.

**Already held, and now unblocked.** **Node 198** exists for the two stale descriptions and is blocked by this
node. Its author could not name the destination and left clause 2 without one; it is **`map-manager-only.md`**. Its
two targets are confirmed still stale: `map.md` line 7 glosses the rules file as holding *"the landing policy, the
code-slot count, the bar's commands and the standards work is held against"*, and `graph-conventions.md`'s
`## The seven files` says *"the landing policy, the bar's commands and the standards work is held against"*. **Two
sites its clause 1 may not literally reach**, worth adding when it is claimed: `map.md` line 36 states that the
code-slot count *"lives in [map-implementation-rules.md](map-implementation-rules.md)"*, which is now false and is
buried mid-sentence in a long `## Notes` bullet about question batching; and `map.md` line 5 describes
`map-manager-only.md` as holding *"the dogfood target, the label vocabulary, the fog, and what is out of scope"*,
which is now incomplete. Clause 1 speaks of *"naming a section that file no longer holds"*, and the code-slot count
is a paragraph rather than a section.

**Checked and clean:** the checker's contract names only the standards in the rules file; the implementation
contract names only the standards and the bar's commands; the manager's contract says landing is *"recorded in its
map"*, which stays true. None needs repair.

*The manager has filed the three invalidations onto nodes 152, 160 and 186 themselves, and the two extra sites onto
node 198.*

## Retrospective

*Filed by the manager in the same edit that resolves the node, the duty the human settled at [node
212](212-the-mint-on-second-report-rule-is-defeated.md). Pasted as the worker wrote it.*

Each item names the standing item it reports and how many times that name appears in the record (`grep -rio <name>
--include='*.md' .scratch/graph-workflow`, run today).

1. **Standing item: *the manager's material in the worker's file*** — 21 hits across 12 files. This node is that
   item's sixth report and its first repair, and the repair took one `sed`, one `diff` and three authored lines. The
   item was correctly diagnosed by node 144's worker on the first report, in words the node file quotes: *"it
   survived node 140's move because node 140 moved by source rather than by reader."* Nothing was ever unclear; what
   was missing was a node. The generalisable finding is not about landing but about **moving by source**: node 139
   and node 140 both split the map by *where text came from*, and both left material sitting in front of the wrong
   reader. Any future split should be checked by asking, of each block, which declared reader acts on it.

2. **Standing item: *went to a file for one fact and took the whole file*** — 13 hits across 9 files for *"for one
   fact"*, 38 across 28 for *"whole file"*. This node is the arrangement fix that node 126's worker said was the
   only fix — *"the warning cannot fix this, and the arrangement can"* — and it worked: a worker claiming node 186
   or node 205 tomorrow reads 12,370 bytes where it would have read 28,590. My own instance of the item is
   `decisions.md`: my spawn pointed me at it unscoped, this effort declaring no label vocabulary, so I read all 131
   lines to use six (nodes 139, 140, 144, 189, 191, 198). The arrangement that would have avoided it is a per-node
   pointer naming the relevant lines, which the spawn is already the right place for — the spawn named four other
   files precisely.

3. **Standing item: *a byte-identity clause is discharged by diff*** — the demand is named 134 times across 45
   files as *"byte-identical"*, but the cheap discharge is named only 6 times across 5 files as *"by diff"*. That
   ratio is the finding. My spawn carried the technique as a manager's note and it cost me nothing: `sed | diff -q`
   on a 128-line block, versus reading 16,619 bytes twice. Given how often the corpus demands byte-identity and how
   rarely it says how to check it, the technique belongs in `map-implementation-rules.md` as a one-line rule for
   both a worker and a checker, which is exactly what that file's admission test admits — a line its reader acts on
   differently.

4. **Standing item: *a condition fences out the neighbouring repair*** — 73 hits across 26 files for *"fence"*, and
   node 198's own filing calls it *"the pathology this effort has now recorded four times"*. This node is a clean
   fifth instance, and an instructive one, because the fencing was **right**: clause 1 demanded byte-identity, so a
   worker free to edit `map.md` would have been a worker free to break the thing being moved. The cost is real
   anyway — three open conditions now hold wrong file names, and node 198 must run behind me — but it is the cost of
   a correct boundary rather than a defect. What would have made it cheaper is not a wider scope but a **clause that
   obliges the worker to enumerate what its move falsifies**, which I did on `INVALIDATIONS` because the contract
   asks for it, not because the condition did. The contract's `INVALIDATIONS` part is doing the work here; the
   finding is that a moving node should be spawned knowing that, which mine was not.

5. **Nothing read was stale, wrong, or self-contradicting.** The bar's record matched the repo exactly, all 96 links
   resolved, and node 200's freshly-landed paragraph about relative words was accurate about both instances it
   names. One thing arrived and bore on nothing: the map's `## Destination` and the whole of `## Decisions so far`,
   plus `map.md`'s twenty standing preferences, of which two reached my work (never-delete, and the retrospective
   rule). That is the cost of `map.md` being read whole by every worker, which is a settled trade rather than a
   defect.
