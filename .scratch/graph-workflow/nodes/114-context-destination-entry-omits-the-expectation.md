# `CONTEXT.md`'s `Destination` entry does not say the destination states whether the effort is expected to end

Type: implementation
Status: resolved

## Question

*Reported as an invalidation by [Whether charting an effort establishes and records that it is expected to
end](91-charting-records-whether-an-effort-ends.md)'s worker, and pasted as it wrote it. Minted by the manager
because no node reached it.*

> `CONTEXT.md`'s `Destination` entry reads *"What reaching the end of an effort looks like. It fixes the scope, which
> is what makes work beyond it out of scope rather than fog."* It is now short by this answer: the destination also
> states whether the effort is expected to reach it. Contradicted by omission rather than by statement, so the
> disposition is an extension of the entry, not a replacement. **No open node reaches it** — nodes 90, 106 and 107
> each repair a different `CONTEXT.md` entry (`Closed`, `Closing report`, the reservation of the word `report`), and
> none touches `Destination`.

**Blockers:** none.

## Acceptance condition

***Written by the manager, for a node the manager minted itself*** because the node that found the defect surfaced it
as an invalidation rather than as a node, and no other node reaches the entry. Marked as the manager's own under
[Who writes the acceptance condition for an implementation node the manager mints
itself](39-condition-for-a-manager-minted-node.md), whose constraint 1 confines it to what is already fixed. **What
is fixed is node 91's resolved answer**; the entry's wording and the shape of the addition are not, so this condition
states the property and leaves the form.

> **Scope, and the search that produced it**, under [node 94](94-condition-scope-as-a-predicate.md)'s rung 1.
> `CONTEXT.md` is edited and no other file is.
>
> ~~The enumerator, run while this condition was written: `grep -rn "Destination" CONTEXT.md` returns two lines — the
> entry's own heading `**Destination**:` and the `_Avoid_` line of another entry that refuses the word — and
> `grep -rln "Destination" .claude/skills` returns no file, so the term is stated in the glossary and nowhere in the
> shipped skills.~~
>
> **Struck and replaced. Both recorded returns were false when the manager wrote them**, found by [Whether the
> checker re-runs a condition's own enumerator](110-does-the-checker-rerun-the-enumerator.md)'s worker and re-run by
> the manager before this correction. What the commands actually return:
>
> - `grep -rn "Destination" CONTEXT.md` returns **one** line, `CONTEXT.md:39:**Destination**:`. The command is
>   case-sensitive and the `_Avoid_` line the manager had in mind is lowercase, so it never matched.
> - `grep -rln "Destination" .claude/skills` returns **one** file, `.claude/skills/expedition/graph-conventions.md`.
>   That hit is the description of `map.md`'s `## Destination` section under `## The five files` — **the exact line
>   [node 111](111-write-the-starting-an-effort-section.md)'s clause 10 is open to edit**. So this node stays out of
>   it, and the two conditions do not collide: node 111 edits that line, this node edits `CONTEXT.md`'s entry.
>
> A place this work finds stating what the destination holds, outside `CONTEXT.md`, is **reported and not edited**;
> reporting it is the whole of what this condition asks for it.
>
> 1. `CONTEXT.md`'s **Destination** entry states that the destination also says, in one line, whether the effort is
>    expected to reach it.
> 2. It states that where the effort is not expected to reach it, this is where a manager reads that a non-empty
>    frontier is that effort's steady state rather than a defect.
> 3. The entry's existing two sentences are kept, the addition being an extension rather than a replacement, and its
>    `_Avoid_` line is unchanged.
> 4. The entry states nothing, in any wording, about how often efforts end or fail to end.
> 5. No other entry in `CONTEXT.md` changes. In particular the **Closed**, **Closing report**, **Flag** and
>    **Handover** entries are untouched, those being nodes 90, 106, 103 and 107's work.
> 6. No file under `.claude/skills/` changes and no file under `.scratch/` changes.
> 7. The working tree meets the bar.

### The manager's read-back, recorded before any claim

*[Node 39](39-condition-for-a-manager-minted-node.md)'s constraint 2 requires the condition to be read back against
the two rules that bind every condition, and that reading recorded on the node.*

- **Self-contained text.** It passes. Each demanded property is written out here rather than pointed at; the file is
  named by path and the checker has the repo; the enumerator is a command the checker can run.
- **It does not quantify over the record.** It passes. Every clause is a demand about the state of one file, and the
  enumerator's domain is the tree rather than `nodes/` — which is what flag `94.2` requires.

## The manager's note at filing

*Not a change to anything above.*

**Node 111 could not absorb this**, its own clause 12 confining it to `.claude/skills/expedition/`. That is why this
is a node rather than a widening.

## Annotation: the condition's enumerator was corrected in place before any claim

*Filed by the manager against its own text. The node is open and holds no work, so [Revision
semantics](06-revision-semantics.md)'s in-place route applies rather than supersession.*

**What was wrong and who found it.** Both recorded returns in the scope clause were false at the moment the manager
wrote them — not stale, false. Node 110's worker ran the two commands as part of its own node and reported them; the
manager re-ran both before correcting, and both of the worker's findings hold exactly. The struck text and its
replacement are in the condition above.

**Why this matters beyond one node.** The manager wrote the first condition on this graph to carry an enumerator
under [node 94](94-condition-scope-as-a-predicate.md)'s rung 1, and got the enumerator wrong — which is the precise
failure node 110 is asking whether the checker should catch. **The instance is the manager's own and is recorded as
evidence for that node rather than as an argument in it.** Node 110's worker put it more sharply than the manager
would: on the two live false instances, *"the author is the manager."*

## Answer

*Node 114's worker's `ANSWER`, pasted as it wrote it. **The node is not resolved by this section**: the work is
uncommitted and its check is running.*

> `CONTEXT.md`'s `Destination` entry now states the expectation. It gained two sentences and kept both of its own;
> the `_Avoid_` line is untouched. The entry in full:
>
> > **Destination**:
> > What reaching the end of an effort looks like. It fixes the scope, which is what makes work beyond it out of
> > scope rather than fog. **It also says, in one line, whether the effort is expected to reach it. Where an effort
> > is not expected to reach it, that line is where a manager reads that a non-empty frontier is that effort's
> > steady state rather than a defect.**
> > _Avoid_: goal, objective, definition of done
>
> **The calls inside it.**
>
> - **An extension, appended inside the entry, not a restructure.** No heading, no sub-bullet, no new entry. Node
>   91's answer fixes that the fact rides the destination's existing text, and the glossary's every other entry is
>   unbroken prose; a `Destination` entry that alone carried structure would announce a distinction the answer does
>   not make.
> - **"in one line" is stated as the destination's form**, which is unusual for a glossary that otherwise states
>   meaning. Clause 1 demands it, and it is load-bearing: it is what tells a reader the expectation is a sentence in
>   an existing section rather than a field, a section, or a per-effort setting — the four things node 91 explicitly
>   refused to create.
> - **Only the non-expected side of the consequence landed.** Node 91's answer is a symmetric pair: an empty
>   frontier is a **milestone** where the effort is expected to end, and a **surprise** where it is not. Clause 2
>   demands only the second. The first is not here, deliberately — flagged below.
> - **No frequency claim, in any wording.** Clause 4 forbids one, and node 86 withdrew every frequency claim from
>   the workflow. What the entry records is that one effort's own expectation is written down, never how often
>   efforts end. The conditional *"where an effort is not expected to reach it"* is a branch, not a rate.
> - **"steady state" is the condition's own word**, and it already appears in the `Closed` entry attached to the
>   rejected frequency claim node 90 is repairing. Reused here without the frequency, and it is not a defined term,
>   so node 90's repair cannot orphan it.
>
> **The residual clause, discharged.** Clause 6's residual asks that a place stating what the destination holds,
> outside `CONTEXT.md`, be reported and never edited. One instance, and it is the one the condition predicted:
>
> - `.claude/skills/expedition/graph-conventions.md`, under `## The five files`: `` `## Destination` — what reaching
>   the end of the effort looks like. `` This is the shipped statement of the destination's contents, and it is now
>   short by the same line `CONTEXT.md` just gained. It is **node 111's clause 10** to edit. **Not edited.**
>
> Three uses of the word were checked and **ruled out** as instances: `SKILL.md`'s *"beyond the destination → the
> node is ruled out of scope"* uses the term without stating its contents; the five worker contracts' *"`map.md` —
> the destination, the standing preferences, the fog"* is a pointer to the map's sections; and
> `graph-conventions.md`'s *"The closing report is the exception path rather than the ordinary destination"* uses
> *destination* in its ordinary-English sense, about where a flag settles. That last one is reported below anyway as
> a possible collision with node 91.
>
> **The condition's enumerator was re-run before any edit, and both corrected returns hold exactly:** `grep -rn
> "Destination" CONTEXT.md` → one line, `CONTEXT.md:39:**Destination**:`; `grep -rln "Destination" .claude/skills` →
> one file, `.claude/skills/expedition/graph-conventions.md`. Re-run after the edit with the same two returns. Cost:
> one command, seconds.

## Index line

*The worker's, pasted.*

> `CONTEXT.md`'s `Destination` entry now says the destination states in one line whether the effort is expected to
> reach it, and what a non-empty frontier then reads as.

## Flags

`114.1` `ASSUMPTION` **settled** — **Only the non-expected half of node 91's milestone/surprise pair is in the entry.** Node 91's
`### What turns on it` settles a symmetric pair: an empty frontier is a **milestone** where the effort is expected to
end, and a **surprise** where it is not; likewise the closing report is a destination on one and an exception path on
the other. My clause 2 demands only the not-expected side, so that is what I wrote, and I did not add the milestone
side on my own authority. The ground: clause 1 caps the addition at one line's worth of property, the glossary entry
is four sentences and a second symmetric clause would roughly double it, and the manager's reading of an empty
frontier as a milestone is procedure rather than vocabulary — it belongs in the starting-an-effort procedure node 111
is writing, where the map's own `## Destination` line already states it for this effort. What I accepted: a reader of
the glossary alone now learns what a non-empty frontier means on an open-ended effort and is told nothing about what
an empty one means on a bounded one, and if node 111 does not carry the milestone side, no shipped file states it.

## New nodes

*The worker's, pasted.*

> none.
>
> *Nothing I found needs a node.* The four staleness findings below are either already owned (the
> `graph-conventions.md` destination line by node 111, the `grilling` entry by node 113's report, the `Closed` entry
> by node 90) or are two-word `map.md` corrections the `Change the map` procedure covers, which node 91's flag `91.1`
> established as the ordinary route for a map edit.

## Invalidations

*The worker's, pasted.*

> none. My work contradicts no resolved node.
>
> *One thing adjacent to an invalidation, reported rather than claimed as one.* `graph-conventions.md`'s `### Settle
> a flag` says *"The closing report is the exception path rather than the ordinary destination"*, unconditionally.
> Node 91 conditionalised exactly that sentence's vocabulary — *"a destination on an effort expected to end, an
> exception path on one that is not."* Read in place the line is about **where a flag settles** and is correct, so I
> am not calling it an invalidation; read cold it is the general claim node 91 split in two, in node 91's own words.
> I did not edit it (clause 6 forbids it) and I am reporting it for the manager to judge.

***The manager's judgement on that, since the worker asked for one and it is the manager's to give.*** **It is not an
invalidation and it is not left alone either.** The sentence is correct where it sits and would be wrong if lifted,
which is a property of the sentence rather than a defect in it — and node 107's answer is about to rename the very
term in it, so whoever performs that rename will be editing this line anyway. **The manager has recorded it against
node 107's repair rather than minting a node**, and has not edited it: the file is shipped and the manager writes no
shipped file.

## Gate payload, as the worker handed it back

*The worker's, pasted. Its first line was true when written; the check is now running.*

> *What the checker found, and what I changed:* none — no checker run has reached me.
>
> *Paths I touched:* `/home/mathieu/projects/graph-agent/.worktrees/114-destination-entry/CONTEXT.md`, and nothing
> else. `git status --porcelain` in the worktree returns exactly ` M CONTEXT.md`. Nothing under `.claude/skills/` or
> `.scratch/` changed (`git diff --name-only -- .claude/skills .scratch` returns zero paths), and no other entry's
> `**Term**:` heading or body appears in the diff.
>
> *One thing the diff shows that clause 3 might look violated by:* the hunk touches the line ending `out of scope
> rather than fog.` because the new prose was appended to it. **Both existing sentences are byte-identical as
> sentences**; only the line they wrap onto grew.
>
> *The bar.* This repository has no build, no tests, no formatter and no CI, which the map records and which I
> confirmed independently in the worktree: the whole top level is `.claude`, `CONTEXT.md`, `.gitignore`, `.scratch`;
> a `find` for `package.json`, `Cargo.toml`, `pyproject.toml`, `Makefile`, `justfile`, `*.nix`, `.editorconfig` and
> `.prettierrc*` returns nothing, and there is no `.github`. So the bar's command half is empty and it is met on its
> non-command half: `/naming` and `/coding-principles` invoked, `/writing-for-agents` invoked as ground rule 5
> requires for a prose deliverable, `CONTEXT.md`'s `_Avoid_` lines checked against the new prose (it uses none of
> `goal`, `objective`, `definition of done`, nor any other entry's refusals), the four standing writing rules held
> (no line-number citation; the entry states its current form and restates no node; the glossary cites no node
> per-entry by its own preamble's design), and the entry wrapped at the file's ~100-column convention.
>
> *Proposed commit message:*
>
> ```
> Say in the glossary that the destination records the expectation of ending
>
> `CONTEXT.md`'s `Destination` entry said what reaching the end of an effort
> looks like and that it fixes the scope. It was short by node 91's answer: the
> destination also states, in one line, whether the effort is expected to reach
> it, which is the only place a manager can read that per-effort fact.
>
> The entry gains two sentences and keeps both of its own. It now says the
> destination states in one line whether the effort is expected to reach it,
> and that where an effort is not, that line is where a manager reads that a
> non-empty frontier is that effort's steady state rather than a defect.
>
> Only the not-expected side of node 91's milestone/surprise pair is stated;
> the milestone side is procedure and belongs with the starting-an-effort
> section. No claim is made about how often efforts end or fail to end, node 86
> having withdrawn every frequency claim: what is recorded is one effort's own
> expectation.
>
> Node: graph-workflow/114
> ```

## Retrospective

*The worker's, pasted. Handed back as text on this effort only, and never filed by the worker. **Its fourth staleness
finding is corrected by the manager below**, being the one place it stated more than the facts support.*

> *What I had to hunt for.* Four things, all cheap individually and all re-derived per node:
>
> - **The commit trailer's effort string and the message style.** The spawn named the worktree, the branch and the
>   base commit but not `graph-workflow/114`; I derived the effort from the `.scratch/graph-workflow/` path and
>   confirmed the trailer format and the imperative-subject-plus-prose-body style from `git log`. The map's landing
>   policy already holds every other commit mechanic — that the commit is path-limited, that it carries the trailer,
>   that it is never pushed — so one line there naming the effort string and pointing at the style would retire a
>   `git log` read on every implementation node.
> - **`CONTEXT.md`'s wrap width.** Measured with `awk` (max 107, the entry's own lines at ~100). No convention states
>   it, and a prose deliverable whose diff is one of the human's two interfaces is worth wrapping consistently.
> - **Whether `where` is actually a refused word.** See the stale findings below; I grepped the `_Avoid_` lines to
>   check, because the map told me it was.
> - **Whether the bar's "no build, no tests" still held.** The map states it and the spawn told me to discover it
>   from the map rather than take the spawn's word, so I did both and then confirmed with a `find`. That third step
>   was mine, not asked for, and it is what surfaced the stale `.gitignore` detail — so I would keep it, but the
>   spawn's framing ("discover that from the map rather than taking my word for it") sets the map against the spawn
>   when the useful check is the map against the repo.
>
> *What I read and did not use.*
>
> - **`decisions.md` in full, 90 lines, to use four.** The spawn scoped it *"by the labels bearing on done-ness,
>   termination and the glossary — a filter instruction, not an extract."* **The filter is unexecutable as written**:
>   the map declares *"Label vocabulary for this effort: none declared"*, so the file is flat and has no labels to
>   filter by. I read all of it to find nodes 10, 86, 91 and 94. On a flat index the honest instruction is either the
>   four node numbers or nothing.
> - **`/coding-principles`, invoked because the contract mandates it, with nothing operative for a four-sentence
>   glossary entry.** Its content is code altitude, silent failure and illegal states; what reached my output was its
>   pointer to `/naming` and its grouping point, which `/writing-for-agents` states better for prose. The contract's
>   *"invoke if present"* is unconditional, so I ran it rather than judging it inapplicable — but a prose-only node
>   pays ~1.5k tokens for it every time.
> - **Most of `map.md`.** I acted on the bar line, the four standing writing rules, the ground rules and the
>   `## Destination` section. The landing policy, the concurrency counts, the dogfood target, the token findings, the
>   seven fog items and the out-of-scope section did not bear on a glossary sentence. That is the file's known cost
>   rather than a defect in this spawn.
> - **Node 91's three flags, its `## Interview` and its retrospective pointer.** I needed `### What is recorded, and
>   where` and `### What turns on it`. The rest is the account of how the answer was reached, and standing writing
>   rule 3 (navigable by heading) worked — I could see which sections to read.
> - **`graph-conventions.md`'s five-files list and flag-settling section**, read to discharge the residual clause and
>   to rule out three non-instances. Read to rule out rather than to use, which is the residual clause working as
>   designed, not waste.
>
> *What would have made this node easier.* Not much — this spawn was unusually well-built, and two of its
> pre-emptions saved real work: naming node 107's live rename and its exact reserved entries meant I never had to
> discover a collision, and naming node 113's stale `grilling` entry with an explicit *leave it* meant I did not
> spend a round deciding whether to report something already reported. **The instruction to re-run the corrected
> enumerator was the highest-value line in the spawn**: it cost one command and seconds, and it is the difference
> between beginning on a verified premise and beginning on a premise that had already been false once on this very
> node. Two smaller things: clauses 1 and 2 are nearly the entry's finished text, so the writing was minutes and the
> **verification** was the bulk of the node — which suggests the effort's cost on this kind of node sits in proving
> compliance, not in producing prose. And the spawn's *"seventh part"* against the map's *"sixth handover part"* is
> an off-by-one worth settling (below).
>
> *What I found stale, wrong, or contradicting something else.* Five, none of which I edited.
>
> 1. **`map.md`'s review route lists `where` among `CONTEXT.md`'s refused ordinary-English words. It is not
>    refused.** No `_Avoid_` entry in `CONTEXT.md` lists it; the only `_Avoid_` line containing the word uses it as a
>    conjunction, in the `Raise` entry's *"...the ordinary mode of a worker built to question the human, where a raise
>    is..."*. The map presents that list as *"measured"*, and a checker taking it literally greps for a non-refusal in
>    a file where `where` appears constantly. The other seven — `report`, `run`, `session`, `index`, `plan`, `item`,
>    `question` — are genuine.
> 2. **`map.md`'s bar line says the repository has *"no ignore file"*.** A `.gitignore` now exists at the root, added
>    by the worktree landing policy to ignore `.worktrees/`. The bar's conclusion is untouched, a `.gitignore` being
>    nothing to invoke, but the parenthetical is false and it is one of the two clauses a later node would check
>    first.
> 3. **`graph-conventions.md`'s *"The closing report is the exception path rather than the ordinary destination"*** —
>    reported above under `INVALIDATIONS` as adjacent rather than an invalidation. Correct in place, and node 91's own
>    vocabulary read cold.
> 4. **The retrospective's part number disagrees across two sources.** `map.md` calls it *"a sixth handover part"*;
>    the spawn calls it a seventh. The contract says *"Six parts, every time"* and its block carries seven labels, of
>    which `HANDOVER:` is the name line — so six parts, and the retrospective is the seventh. The spawn is right and
>    the map's *"sixth"* is off by one.
> 5. **The `graph-conventions.md` destination line and the `grilling` entry**, both already owned (nodes 111 and 113
>    respectively) and both left alone.

***The manager's corrections to that retrospective, all three verified before acting rather than taken from the
report.***

**Findings 1 and 2 hold exactly and the map is corrected.** `where` is refused by no `_Avoid_` line — exactly one
`_Avoid_` line contains the word, the `Raise` entry's, where it is a conjunction. And `.gitignore` exists, is
tracked, and is 223 bytes. Both map lines were archived verbatim to `map-history.md` and then changed, under the
map's own procedure.

**Finding 4 is stated more strongly than the facts support, and the correction is narrower than the report.** The
worker says the map is *"off by one"*. It is off by one **only for an implementation node**.
`expedition-grilling/SKILL.md` says *"Five parts, every time"*; `expedition-implementation/SKILL.md` says *"Six parts,
every time"*, the sixth being the gate payload. So the retrospective is the **sixth** part on the four kinds whose
handover has five and the **seventh** on an implementation node. **The worker read the implementation contract, which
is the one case where its claim held.** The map now states both, and the superseded wording is archived.

**One thing in the retrospective the manager owes and has not done.** Its first bullet asks that the map's landing
policy name the effort string for the commit trailer and point at the message style, so no implementation worker
re-derives it from `git log`. That is a map edit the manager can make and **has not made**, and it is recorded here
rather than performed, because it is a change to the landing policy rather than a correction of a false statement.

## The checker

*One attempt, killed mid-run by the harness's session limit and **resumed rather than replaced**, under the rule
standing in the map. The manager spawned it; the worker that wrote the code did not.*

### Attempt 1 — killed at 35 records, resumed, returned `PASS`

**The death, read from the transcript rather than from the harness's summary line**, as node 119's answer requires:
**35 records, 124,667 bytes**, last record *"You've hit your session limit · resets 2:20pm (Europe/Paris)"*, and its
`.meta.json` carries no `stoppedByUser` key — so it was the harness's kill and not the human's, and resumable. Its
own last line before stopping was *"Paragraph-level unwrapped diff shows exactly one paragraph moved. Now the
standards, and clause 6's scope."*

**What the resume carried, and what it was required to re-run.** The manager told it what had changed under it while
it was stopped — the two map corrections — and required, under flag `119.4`, that it **re-run the bar's command half
rather than carry it over** and **re-establish that no standard moved**, `CONTEXT.md` being both the file under
change and the source of the `_Avoid_` lines. It did both. **This is the first resumed check on this effort under
that rule.**

*Pasted as the checker wrote it. **The manager authored none of it.***

> ## PASS
>
> **Acceptance condition — every clause established.** Method note: the diff over lines is misleading here, so I
> unwrapped both sides into unbroken paragraphs (`perl` split on blank lines, whitespace collapsed) and compared
> those. The file has 62 paragraphs; exactly one differs.
>
> | # | Clause | How established |
> |---|---|---|
> | 1 | Entry states the destination says, in one line, whether the effort is expected to reach it | Added sentence 1 is verbatim that. `"in one line"` grammatically modifies what *the destination* says, not the entry — clause 2's back-reference `"that line"` confirms it. Met. |
> | 2 | States that where not expected to reach it, this is where a manager reads a non-empty frontier is the steady state rather than a defect | Added sentence 2, verbatim bar `"that line is where"` for `"this is where"` — which pins it to clause 1's line rather than loosening it. Met. |
> | 3 | Existing two sentences kept, addition an extension not a replacement, `_Avoid_` unchanged | **Worker's declaration one confirmed.** Prefix test: `index(wt_body, base_body) == 0` → pure append. `_Avoid_: goal, objective, definition of done` byte-identical. Only the wrap grew. Met. |
> | 4 | Nothing, in any wording, about how often efforts end or fail to end | Scanned added text against 17 frequency terms (`most, many, often, rarely, usually, always, never, typically, majority, …`) → zero hits. Met. |
> | 5 | No other entry changes; **Closed**, **Closing report**, **Flag**, **Handover** untouched | Whole-file unwrapped paragraph diff: 62/62, one changed. Those four compared individually and byte-identical (254 / 182 / 482 / 293 bytes). Met. |
> | 6 | Nothing under `.claude/skills/` or `.scratch/` changes | `git status --porcelain -uall --ignored=matching -- .claude .scratch` → empty. 133 tracked files under `.scratch`, 9 under `.claude`; `.gitignore` ignores only `.worktrees/`, so an added file there would surface as `??`. **Established from git metadata alone — I read nothing under `.scratch/`.** Met. |
> | 7 | Working tree meets the bar | Below. Met. |
>
> Scope: `git diff --name-only` → `CONTEXT.md`, nothing staged. No file outside the condition's list was edited.
>
> **The recorded enumerator, re-run as written — both match.** `grep -rn "Destination" CONTEXT.md` → the single line
> `CONTEXT.md:39:**Destination**:`; `grep -rln "Destination" .claude/skills` → the single file
> `.claude/skills/expedition/graph-conventions.md`. No discrepancy to hand back. The corrected returns hold, and note
> enum 1 still returns line 39 post-change because the append landed below the heading and added no new occurrence.
>
> Discharging the residual clause, I swept case-insensitively over `.claude` and `CONTEXT.md` (bounded away from
> `.scratch/`). Exactly one place outside `CONTEXT.md` states what the destination *holds*: `graph-conventions.md`,
> the line `` `## Destination` — what reaching the end of the effort looks like. `` under `## The five files` — the
> line the condition names, unedited. The other twelve hits name the destination without stating its content (six
> instances of `` `map.md` — the destination, the standing preferences, the fog ``, and four `"beyond the
> destination"` out-of-scope uses). **Reported, not edited.**
>
> **The bar.** Command half established empty rather than assumed: the tracked tree is 143 `.md` files plus
> `.gitignore` and nothing else — no manifest (probed `package.json`, `Cargo.toml`, `pyproject.toml`, `Makefile`,
> `justfile`, `flake.nix`, `CMakeLists.txt`, `build.zig`, and 12 more), no CI config, no formatter config, no
> extensionless file. Nothing to invoke. Hygiene: no CRLF, no tabs, no trailing whitespace, final newline present;
> added lines are 100/96/60 chars against a file median of 60 and max of 107, so the ~100-col wrap convention holds.
>
> Standards found and used: `/coding-principles` and `/naming` (`~/dotfiles/programs/claude/skills/`),
> `mattpocock-skills:writing-for-agents`, and `CONTEXT.md`'s own `_Avoid_` lines. No `CODING_STANDARDS.md` or
> `CONTRIBUTING.md` exists. I extracted all 107 refused tokens from all 41 `_Avoid_` lines programmatically and
> scanned the added text: **zero hits**, then hand-checked the distinctive refusals (`report, run, session, index,
> plan, item, question`) — none present. I independently confirmed both map corrections: `.gitignore` is tracked at
> 223 bytes, and **`where` is refused by no `_Avoid_` line** (it appears only inside the *explanatory prose* of the
> `Raise` entry's `_Avoid_`, which is the likely source of the map's error).
>
> **`mattpocock-skills:code-review` — which parts ran.** Standards axis: **run**, in a sub-agent handed the diff, the
> unwrapped before/after, all four standards, the smell baseline pasted in full, the ground rules and the four
> writing rules, and a hard prohibition on reading `.scratch/` or seeking the change's origin — so it held strictly
> less than nothing I hold, and more than a bare spawn would. Spec axis: **left unrun**, per my contract (a reviewing
> skill is for standards, never intent) and because its step-2 search targets `docs/`, `specs/`, `.scratch/`. Its
> `docs/agents/issue-tracker.md` step likewise unrun. The acceptance condition was my only statement of intent.
>
> **I did not adopt either of the axis's two claimed hard violations.** Both fail on inspection:
>
> 1. *Duplication with the **Closed** entry.* It argued `"never closed"` ≡ `"frontier never empties"`. The file's own
>    entries refute that: **Closing report** is what the manager hands over *"once the frontier empties"*, while
>    **Closed** is *"the human's declaration that an effort is over."* An empty frontier triggers the report; the
>    human then declares or does not — which is precisely why *"most efforts are never closed"* can be true. Distinct
>    facts. Clause 4 was the condition's own anti-duplication guard and the work is on the right side of it. The
>    shared token `steady state` is repetition of a *token*, which `writing-for-agents` explicitly endorses — the
>    axis conceded this in its own non-findings, contradicting its finding.
> 2. *Writing rule 1, "no shape / near no-op".* Sentence 2 does carry a shape: which line a manager reads a specific
>    meaning from. It beats the default, since the default reading of a non-empty frontier is unfinished work. And
>    decisively — it is verbatim what clause 2 dictates, so it was never the worker's to depart from; even had I
>    judged it a defect, the route would be a question, never a `FAIL`.
>
> **On the worker's declaration two, the half-written pair — I judge clause 2 met and raise no question.** Clause 2
> demands only the not-expected side, and the restraint was right for a stronger reason than the worker gave: the
> milestone side's mechanism is *already in the file*, under the entry that owns it — **Closing report**, keyed on
> the frontier emptying. Writing it under **Destination** too would have created the duplication claim 1 wrongly
> alleged. Only the not-expected side lacked a home, and that is the half written.
>
> No `QUESTIONS:` and no `NOT COVERED:` — every clause was establishable from the working tree and the standards.
>
> One observation that is *not* a finding (it touches neither the condition nor the bar, and is pre-existing text
> this node did not touch): `graph-conventions.md` uses "destination" in a plain-English sense in *"The closing
> report is the exception path rather than the ordinary destination"*, colliding with the defined term. Possibly of
> interest since node 111 is editing that file; discard if not.

**The manager's note beside it, and not the checker's. Three things worth the record.**

**It is the second consecutive check to cover a condition whole** — no `QUESTIONS:`, no `NOT COVERED:` — and the
second whose condition names one readable file with no clause reaching `.scratch/`. Node 116's was the first. That is
now a pattern in conditions rather than in checkers.

**It rejected its own sub-agent's two hard findings and showed its work on both**, one of them by catching the
sub-agent contradicting itself between its findings and its non-findings.

**It reached the same conclusion as node 114's worker on the half-written pair, on a different and better ground.**
The worker's ground was that the milestone side is procedure rather than vocabulary. The checker's is that the
milestone side's mechanism **is already in the file**, under `Closing report`, keyed on the frontier emptying — so
writing it under `Destination` too would have created real duplication. **Flag `114.1` stands as the worker wrote
it**; this is recorded beside it, not merged into it.

**And it independently confirmed both of the manager's map corrections**, including locating the likely source of the
`where` error: the word appears inside the *explanatory prose* of the `Raise` entry's `_Avoid_` line rather than in
its list of refused words.

## Interview

### The gate — approved

**The human's word, `verbatim`**, written at the moment they spoke:

> 114 approve

**What it settles.** Node 114's one outstanding flag, `114.1`, is settled by this approval. **The reply names the
node**, which is the sixth recorded instance of the human volunteering a scope where a bare assent would have been
ambiguous — and here it was: node 113's second payload was queued behind this gate when they wrote it.
