# Move the landing section out of the file an implementation worker reads

Type: implementation
Status: claimed

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
