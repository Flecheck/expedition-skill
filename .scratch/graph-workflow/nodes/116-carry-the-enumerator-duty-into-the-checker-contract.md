# Carry the checker's enumerator duty into the checker's contract

Type: implementation
Status: claimed

## Question

*Surfaced by [Whether the checker re-runs a condition's own enumerator](110-does-the-checker-rerun-the-enumerator.md)'s
worker, and pasted as it wrote it.*

> Make the checker's contract state that where an acceptance condition records the search that produced its scope,
> the checker runs that command as written, reports what it returned against what the condition records, and never
> `FAIL`s the work on that comparison alone. Nothing states this today: `scope` appears in that file zero times, and
> node 109 ships node 94's rule into seven files that do not include it.

**Blockers, in the worker's words:** *"none. Node 110 resolves with this handover, node 94 is resolved, and this node
shares no file with nodes 95, 103, 109, 111 or 114."*

## Acceptance condition

*Written by node 110's worker. Pasted as it wrote it, and not the manager's. It carries its scope's enumerator under
[node 94](94-condition-scope-as-a-predicate.md)'s rung 1.*

> **Scope, and the search that produced it.** `.claude/skills/expedition-checker/SKILL.md` is edited and no other
> file is.
>
> **The enumerator, run while this condition was written.** `grep -rln "enumerator" --include="*.md" .claude/
> CONTEXT.md` returns exactly that one path, and `grep -rln "extent" --include="*.md" .claude/ CONTEXT.md` returns
> exactly that same one path — so that file is the only shipped file naming either, and it names them only about the
> checker's own findings. Beside them, `grep -c "scope" .claude/skills/expedition-checker/SKILL.md` returns **0**:
> the contract does not use the word at all, so this work adds a duty rather than repairing instances of a defect
> spread across the tree. **A place this work finds stating what a checker establishes about a condition's scope,
> outside the file above, is reported and not edited**; reporting it is the whole of what this condition asks for it.
>
> **One expected movement in that enumerator, stated so it is not read as a discrepancy.** [Node
> 109](109-carry-the-extent-rule-into-the-shipped-files.md) is open and will add the word *enumerator* to seven other
> shipped files. Where it has landed before this node is checked, the first command above returns eight paths rather
> than one, and the seven additions are node 109's work and not this node's scope.
>
> 1. **The duty, copied here in full rather than pointed at.** The contract states that where the acceptance
>    condition records the search that produced its scope, the checker **runs that command as written** and states in
>    its outcome what the command returned and whether that matches the return the condition records.
>
> 2. **What the comparison is against.** The contract states that the comparison is against the **return the
>    condition records**, and not against the condition's list of places. It states that the two may legitimately
>    differ — a condition may exclude part of its scope from the enumerator's domain and say so — and that where the
>    condition states the reason, the difference is not a discrepancy.
>
> 3. **What the comparison is not.** The contract states that the checker is not asked whether the scope has grown
>    since the condition was written, and cannot establish it: it holds no before-state, the work has moved the
>    listed files under it, and other work may have landed in them. What it establishes is whether a recorded claim
>    is false.
>
> 4. **The outcome.** The contract states that a mismatch, or a return reaching a place the condition's list does not
>    name, is handed back **alongside** the outcome and is **never on its own a `FAIL`**. It states all three
>    reasons: a property nobody demanded of the work is not a finding, the enumerator being a statement of how the
>    list was got rather than a demand on the work; a `FAIL` sends the work back to a worker who met the scope as
>    written and whom this contract forbids to repair a condition; and the condition's own residual clause already
>    routes an out-of-list instance to being reported and not edited.
>
> 5. **What stays a `FAIL`.** The contract states that the work editing a file outside the condition's list remains a
>    `FAIL` on the condition, established from the diff and not from the enumerator.
>
> 6. **A record-reaching domain.** The contract states that where the recorded command's domain reaches the effort's
>    record rather than the working tree, the checker runs it as written, reports that the condition's enumerator
>    reaches material the checker is blind to, and does **not** silently narrow the command to the tree.
>
> 7. **Authorship is not a factor.** The contract states that this duty holds whoever wrote the enumerator, and that
>    the checker is not told and does not ask.
>
> 8. **The surplus travels as a finding.** The contract states that what is handed back under clause 4 is a finding,
>    so it carries the three things `### What every finding carries` already requires of one — the instances, the
>    form as a predicate, and one of the three extents.
>
> 9. **Nothing already in the file is removed, renumbered, or changed in meaning** beyond what clauses 1 to 8 name.
>    In particular hard rules 1 to 6, `### What every finding carries`, `### What you can establish, and what you
>    cannot`, the `PASS`, `FAIL` and raise shapes, the `QUESTIONS:` and `NOT COVERED:` routes, and the five raise
>    grounds all stand exactly as they stand today. **Where in the file the new material goes is not dictated**, that
>    being a form the worker settles.
>
> 10. **`CONTEXT.md` is changed only if a term genuinely moves**, and where one does, it is reported in the handover
>     rather than assumed to travel. No file under `.scratch/` is changed.
>
> 11. **The bar.** The standing bar applies: the tree builds, warns about nothing, is formatted, and passes the tests
>     relevant to the change. This repository has no build, no tests and no formatter, which is a complete bar on its
>     remaining half rather than a deficient one — so what remains is `/coding-principles`, `/naming`, and the file's
>     own form: it addresses the checker as *you*, states rules rather than explaining them, and a new rule joins an
>     existing section rather than sitting beside it.

## The manager's note at filing

*Not a change to anything above.*

**This is the first node whose acceptance condition anticipates its own enumerator moving**, in the paragraph headed
*"One expected movement"*. Node 110's answer makes a checker compare the recorded return against what the command
returns now; this condition pre-empts the false positive that node 109 landing first would otherwise produce. Whether
that is a shape other conditions should copy is nobody's node yet.

## Answer

*Node 116's worker's `ANSWER`, pasted as it wrote it. **The node is not resolved by this section**: the work sits
uncommitted and its check is running.*

> **Node 110's rule is now stated in `.claude/skills/expedition-checker/SKILL.md`, as one new `###` section, `### The
> enumerator a condition records`.** Before this change the word `scope` appeared in that file zero times; it now
> appears four, all inside the new section. Nothing else in the file moved: 36 insertions, 0 deletions, one file.
>
> **Where it went, and why there.** The section sits inside `## What you hand back`, between `### What you can
> establish, and what you cannot` and `### PASS`. The condition left the placement to the worker and clause 11
> required that a new rule *join an existing section rather than sit beside it*, which I read as forbidding a new
> top-level `##` peer rather than a `###` inside one. Three things fix that position:
>
> - `### What every finding carries` is already read by then, so the closing sentence's citation of it points
>   backwards rather than forwards;
> - `### What you can establish, and what you cannot` is the file's existing statement of the checker's epistemic
>   limits, which is exactly what clause 3 adds one more of — the two now read as one movement;
> - `### PASS` and `### FAIL` come after, so *never on its own a `FAIL`* is read before the `FAIL` shape it
>   qualifies.
>
> The `PASS` and `FAIL` code blocks were deliberately left untouched, clause 9 requiring them to stand exactly as
> they stand; clause 1's demand that the outcome state the return is carried in the section's prose instead.
>
> **One wording call inside clause 3, and it is the only place my text is not the condition's own words.** The
> condition's ground reads *"it holds no before-state"*. I wrote **"You were given no before-state"**. The bald
> version would contradict the same file's given 3 — *"The work — the paths that changed, in the working tree holding
> them. Produce a diff yourself if you want one"* — which presupposes the checker can reach a before-state, and it
> was falsified in practice an hour before this node was claimed: node 103's checker attempt 2 ran `git grep -ln
> "closing report" 47703bb` and used the baseline productively. The scoped version is true of the five givens, is the
> file's own idiom (*"Your blindness is a property of what you were given, not of what you are"*), keeps the
> condition's ground rather than replacing it, and leaves the baseline move available. Flagged below.
>
> **The condition's residual clause returned nothing.** *"A place this work finds stating what a checker establishes
> about a condition's scope, outside the file above, is reported and not edited."* Searched over every tracked file
> under `.claude/` plus `CONTEXT.md`, unwrapped into unbroken text, for *checker*/*check* within 80 characters of
> *scope* in both orders. One hit, `graph-conventions.md`'s *"must be ruled out of scope too"* — the mechanical check
> on unsatisfiable `Blocked by:` edges, not a statement about a condition's scope. **No place outside the checker
> contract was found, so nothing was owed here.**
>
> **`CONTEXT.md` is unchanged, and no term moved.** *enumerator*, *extent* and *scope* carry no entry there; the new
> section coins nothing and reuses the file's own `enumerator`, defined one section above as extent rung 1. The
> `Acceptance condition` and `Checker` entries both stand true after the change.
>
> **The condition's own enumerator, re-run before any edit, was exact in all three halves.** `grep -rln "enumerator"
> --include="*.md" .claude/ CONTEXT.md` → one path, the checker contract. Same command over `extent` → the same one
> path. `grep -c "scope" .claude/skills/expedition-checker/SKILL.md` → **0**. Node 109 has not landed, so the
> one-path return stands and the eight-path movement the condition anticipates did not occur.
>
> **The bar.** No build, no tests, no formatter, as the map records. `/coding-principles` and `/naming` were invoked;
> `/writing-for-agents` was read as ground rule 5 requires. The section is second person, states rules rather than
> explaining them, and its one prohibition (*never quietly narrow the command to the tree*) is paired with the
> positive that precedes it, per that skill's negation lever. Its name was derived by the naming method from *"the
> search an acceptance condition records as having produced its scope"*, stripped of what the file and the section
> already carry.

**The manager's note beside it**, and not the worker's. **This is the first node on this graph whose worker re-ran
its own condition's enumerator before touching anything**, and it reports the cost as seconds. The rule node 110
wrote for the checker turns out to be worth something one step earlier, to the worker, as a check that its premise
holds before it works. Nobody asked for that and no node covers it.

## Index line

*The worker's, pasted.*

> The checker contract gains one section stating that it runs a condition's recorded enumerator, compares against the
> recorded return, and never `FAIL`s the work on that comparison alone.

## Flags

`116.1` `ASSUMPTION` — **Clause 3's first ground is stated as a limit on what the checker was given, not on what it
can reach.** The condition's words are *"it holds no before-state"*; I wrote *"You were given no before-state"*. I did
not raise, because the condition is satisfiable, measurable and coherent, and its demand — that the contract state
the checker is not asked about scope growth, with those three grounds — is met in full. I settled the wording rather
than the substance, on two things I could check: the bald sentence would contradict `## What you are given`'s third
given in the same file, which tells the checker to produce a diff itself and so presupposes a before-state; and node
103's checker attempt 2 reached one an hour before this node was claimed, re-running the condition's enumerator
against commit `47703bb`, confirming the recorded four exactly, and correctly diagnosing the 4→3 divergence as the
work having repaired the fourth file — the single most useful thing either of that node's two checkers did with the
rule.

**On whether clauses 2 and 3 conflict with that practice, which I was asked to judge: they do not, and one ground
under clause 3 is weaker than the evidence.** Clause 2 says what to compare against and forbids no further
diagnostic; attempt 2 compared against the recorded return and satisfied it before doing anything else. Clause 3 says
the checker is *not asked* — which my text states, and which forbids nothing — and *cannot establish* scope growth.
That conclusion survives on a ground the condition does not state: the checker does not know which commit the
condition was written against, that being in the record it is blind to, and a branch's fork point is not necessarily
that commit. I did not add that ground, an unrequested reason being a repair of the condition rather than a rendering
of it. **The risk I accepted:** a checker reading *"you cannot establish it"* may take the baseline re-run to be
outside its remit and hand back a bare mismatch where attempt 2 handed back a diagnosis. That is the new node below.

## Invalidations

*The worker's, pasted.*

> none.

## Gate payload, as the worker handed it back

*The worker's, pasted. Its first line was true when written; the check is now running.*

> No checker has run yet, so nothing was found and nothing was changed in response.
>
> *Paths touched, all inside the worktree `/home/mathieu/projects/graph-agent/.worktrees/116-checker-enumerator-duty/`:*
> - `.claude/skills/expedition-checker/SKILL.md` — 36 insertions, 0 deletions, one new `###` section.
>
> `CONTEXT.md` was read and deliberately not changed: no term moved. No file under `.scratch/` was touched. `git
> status --porcelain` in the worktree shows exactly one modified path and no untracked file.
>
> *Diff:* `git -C /home/mathieu/projects/graph-agent/.worktrees/116-checker-enumerator-duty diff`
>
> *What the human is being asked to look at, beyond the diff:* one judgement call. The condition's clause 3 mandates
> the ground *"it holds no before-state"*; I wrote *"you were given no before-state"* instead, because the bald form
> contradicts the same file's own instruction to the checker to produce a diff itself, and because a real checker
> reached a before-state an hour ago and used it well. The substance of the clause is unchanged and all three grounds
> are stated. Everything else in the section is the condition's own words.
>
> *Proposed commit message:*
>
> ```
> State the checker's duty to re-run a condition's recorded enumerator
>
> An acceptance condition may record the search that produced its scope. Four
> recorded enumerators exist on this graph and two were false as recorded, with
> nothing having re-run any of them until node 110 did.
>
> The checker contract now states the duty: run the recorded command as written,
> say in the outcome what it returned and whether that matches the return the
> condition records, and compare against that recorded return rather than the
> condition's list of places. A mismatch, or a return reaching an unlisted place,
> travels alongside the outcome as a finding and is never on its own a FAIL. What
> stays a FAIL is the work editing a file outside the list, established from the
> diff. An enumerator whose domain reaches the effort's record is run as written
> and reported, never quietly narrowed to the tree.
>
> The rule holds whoever wrote the enumerator, and the checker is not told.
>
> Node: graph-workflow/116
> ```

## Retrospective

*The worker's, pasted. Handed back as text on this effort only, and never filed by the worker.*

> **What I had to hunt for.** Two things, and both were in the record rather than in my node.
>
> The first is the one that decided my only judgement call: **what a checker actually does with a recorded enumerator
> in practice.** My spawn named node 103's `## The checker` and that pointer was worth more than anything else I was
> given — but it named the section, not the fact, so I read both attempts end to end to find the four lines that
> mattered (`git grep -ln "closing report" 47703bb`, and the sentence concluding the divergence was the work
> repairing the fourth file). The fact I needed was *which commit* the baseline was and *how the checker got it*,
> because that is what tells you whether clause 3's ground is false or merely narrow. A spawn line reading *"attempt
> 2 reached a baseline at `47703bb` by its own hand, not by being given one"* would have replaced that read.
>
> The second: **whether `## What you are given` presupposes a before-state.** Nothing pointed at it. I found it
> because I read the target file whole before editing, which was right, but the collision between given 3 (*"Produce
> a diff yourself if you want one"*) and clause 3 (*"it holds no before-state"*) is the load-bearing fact of this
> node and it is invisible from either document alone. It is the same shape node 110's worker reported: absence, and
> now contradiction, does not announce itself.
>
> **What I read and did not use.** `map.md` in full, the largest single read of the node: destination, dogfood
> target, landing policy, the code-slot count, the label vocabulary, out of scope, and eight fog items. Six lines
> bore on the work — the bar's commands, the review route, ground rules 1-5, standing writing rules 1-4, and the
> retrospective instruction. `decisions.md` scoped by grep to checker and condition lines, ~20 of 88; I opened three
> of those nodes and used two. Node 110 in full, of which I used `### The rule`, `### What the comparison is against`
> and `### Why not a FAIL`; its evidence table, its three flags and its retrospective were confirmation I did not
> draw on, though its retrospective's third point predicted my own first hunt exactly. Node 94's `## Answer` in full
> for one thing — the residual clause's exact wording, *"it is reported and not edited"*, which my clause 4 bullet
> had to be faithful to. Node 103's checker section in full, of which about fifteen lines mattered.
> `/coding-principles` and `/naming`, invoked as the contract requires and honestly thin on a prose deliverable: the
> altitude rule shaped the ordering inside the section, the naming method produced the heading, and the rest — silent
> fail, illegal states, struct naming — has no purchase on markdown. `/writing-for-agents` earned its read on exactly
> one lever, negation, which changed one sentence.
>
> **What would have made this node easier.**
>
> First, **the condition's enumerator was the cheapest and most valuable thing in my payload and it is three
> commands.** Running them was my first act after reading the contract and it took seconds. That is the rule working:
> I began knowing the premise held rather than assuming it. Nothing to improve — recorded because it is the first
> node whose worker verified its own condition's enumerator before touching anything, and it cost nothing.
>
> Second, and it is the same structural point node 110's and node 94's retrospectives both made, hit a third time:
> **what I needed from node 103 was an artifact, not a decision.** Its index line in `decisions.md` does not mention
> enumerators, baselines or checkers re-running anything; the fact I needed lives in a quoted checker outcome inside
> the node file. My spawn carried the pointer by hand, which is the manager compensating for a graph that indexes
> decisions and not artifacts. Three workers have now reported this and none of us has a fix. What I can add from my
> side: **the artifact I needed was a checker's outcome text**, and those are accumulating on node files with no
> index at all — the graph indexes what was decided and what was flagged, and never what was *run*.
>
> Third, my spawn's manager notes were correctly marked as context rather than steer, and the sentence *"Whether
> those conflict is yours to judge and, if you judge they do, to report rather than resolve silently"* is the reason
> this handover contains a judgement instead of a raise. It named the choice, named that it was mine, and took no
> position. The one thing it could not give me, and which I had to derive, was whether the conflict was severe enough
> to be a raise — that turned on the target file's own text, which the manager had correctly not read.
>
> **What I found stale, wrong, or contradicting something else.**
>
> - **Clause 3 of my own acceptance condition states a ground that is false of a checker in a git repository**, and
>   false in a way its own target file already contradicts: `## What you are given`'s third given tells the checker
>   to produce a diff itself, which requires a before-state. The condition was written before node 103's checker
>   demonstrated the capability, so this is the condition aging by one hour rather than an error at writing time.
>   **This is now the third consecutive node whose node file is an instance of its own finding** — node 94's and node
>   110's retrospectives each recorded one, and mine is that a condition's recorded claim went stale under it, which
>   is precisely the class the condition exists to make checkable.
> - **`CONTEXT.md`'s `Code slot` entry is stale against `map.md`.** It reads *"Occupancy is discovered from the
>   working tree rather than recorded"*; the map now says occupancy *"is discovered by counting the live worktrees
>   ... rather than by inspecting the working tree for uncommitted changes, so the human's own edits no longer read
>   as an occupied slot"*, set at node 68. The glossary states the superseded mechanism, and the map's own line names
>   the reason it was superseded. Outside my condition's scope, so reported and not edited.
> - **The map's `## Notes` line naming `/grilling` and `/domain-modeling` as skills every session should consult is
>   still contradicted by practice**, and node 110's retrospective already reported it three-for-three on grilling
>   nodes. I add the implementation side: `/coding-principles` and `/naming` were invocable and I ran them, and on a
>   pure-prose deliverable they returned almost nothing usable, while `/writing-for-agents` — which the map reaches
>   only through ground rule 5, not through that Notes line — was the skill that changed the text. Node 113 exists
>   for this; recorded as its evidence rather than as a new report.

## The checker

*One attempt. The manager spawned it; the worker that wrote the code did not.*

### Attempt 1 — `PASS`

*Pasted as the checker wrote it. **The manager authored none of it** and took no view on any of it; its five questions
travel to the human inside the gate payload.*

> **Settled first: the work moved a file, and that file is my own contract.**
> `.claude/skills/expedition-checker/SKILL.md` is not among the standards the bar carries here (those are
> `/coding-principles`, `/naming`, `/writing-for-agents` and `CONTEXT.md`), so the raise ground *a standard the work
> moved* does not fire. What I hold the work against — the acceptance condition and the bar — is unmoved. I also did
> not have to choose which version of my contract binds me: the copy I loaded is the pre-change one (the main repo's
> copy is unmodified; the work is uncommitted in the worktree), and I discharged the added duty anyway by running all
> three recorded commands, so this check satisfies both versions.
>
> **Scope, from the diff.** `git status --porcelain` and `git diff --numstat` in the worktree: exactly one file
> modified, `.claude/skills/expedition-checker/SKILL.md`, **36 insertions, 0 deletions**, no staged changes, no
> untracked files. `.gitignore` ignores only `.worktrees/`, and `git status --porcelain --ignored=matching` surfaces
> nothing further, so git's account is complete. Matches the reported paths exactly. No file outside the condition's
> list is edited — clause 5's `FAIL` does not fire.
>
> **The recorded enumerators, run as written.**
>
> | recorded command | condition records | returned | verdict |
> | --- | --- | --- | --- |
> | `grep -rln "enumerator" --include="*.md" .claude/ CONTEXT.md` | exactly one path | `.claude/skills/expedition-checker/SKILL.md` — one path | matches |
> | `grep -rln "extent" --include="*.md" .claude/ CONTEXT.md` | exactly that same one path | same single path | matches |
> | `grep -c "scope" .claude/skills/expedition-checker/SKILL.md` | **0** | **4** | mismatch, explained below — not a discrepancy |
>
> The `scope` mismatch resolves against the condition's own framing, *"run while this condition was written"*. I
> established the recorded `0` was true pre-work: `git show HEAD:.claude/skills/expedition-checker/SKILL.md | grep -c
> "scope"` returns **0**, and `git diff | grep -c "^+.*scope"` returns **4** — all four occurrences are inside the
> added block. The word entered the file only as the work's own new text, which is the word the condition asked the
> work to use. The purpose the condition gave for recording `0` — *"so this work adds a duty rather than repairing
> instances of a defect spread across the tree"* — is confirmed rather than contradicted. Per clause 2, a difference
> whose reason the condition states is not a discrepancy.
>
> **Node 109's expected movement has not landed.** The first command returns one path, not eight.
>
> **The residual clause has nothing to report.** Searching the whole shipped tree bounded to `.claude/` and
> `CONTEXT.md`, no file outside the checker contract mentions an enumerator, a recorded search, or a grep, and none
> states what a checker establishes about a condition's scope. Bounded to the files I hold; I cannot establish it of
> the effort.
>
> **Clauses 1 to 8** are each stated in the new `### The enumerator a condition records` section: the duty to run as
> written and state the return against the recorded one (1); comparison against the recorded return and never the
> list of places, with a stated exclusion not a discrepancy (2); the not-asked-and-cannot-establish limit with three
> grounds (3, see below); alongside-the-outcome and never on its own a `FAIL`, with all three named reasons (4);
> editing outside the list stays a `FAIL` from the diff (5); the record-reaching domain run as written, reported,
> never narrowed (6); the duty holding whoever wrote it, not told and not asked (7); and the hand-back carrying the
> three things `### What every finding carries` requires, cited by heading rather than line number (8).
>
> **Clause 9 is established mechanically.** `diff <(git show HEAD:…SKILL.md) <(sed '200,235d' …SKILL.md)` is empty —
> deleting the inserted block reproduces `HEAD` byte for byte. Every pre-existing line is present, in order,
> unchanged; the heading list is identical modulo the single insertion; the new content is bulleted, so no numbered
> list could have been renumbered. Hard rules 1-6, both cited neighbours, the `PASS`/`FAIL`/raise shapes, the
> `QUESTIONS:` and `NOT COVERED:` routes and all five raise grounds stand untouched. Placement was undictated; a new
> `###` inside the existing `## What you hand back` joins a section rather than sitting beside it.
>
> **Clause 10.** `CONTEXT.md` has no diff. `.scratch/` is **tracked, not ignored** (`git ls-files .scratch` returns
> files), so a change under it would appear in `git status` — none does, and I established this without reading
> anything under it. On whether a term genuinely moved: I find none. `enumerator` and `extent` were already in the
> contract and already absent from the glossary, and `scope` is used in the ordinary sense `CONTEXT.md` itself uses
> for it (**Labels**: *"so work can be scoped to one area of a large graph"*). The worker's judgement reached me via
> the spawn as clause 10 requires, rather than being assumed.
>
> **Clause 11, the bar.** I established the empty command half rather than assuming it: the entire tracked tree is 11
> files — nine markdown skill files, `.gitignore`, `CONTEXT.md`. No `package.json`, `Cargo.toml`, `Makefile`,
> `justfile`, `pyproject`, `go.mod`, no formatter or linter config, no `.github/`. There is nothing to invoke, and
> that is a complete bar on its command half. On the remaining half: the section addresses the checker as *you*
> throughout, leads every paragraph with a bolded rule, and pairs each prohibition with its positive target. My
> hand-check of the refused vocabulary over the added lines found **none** of the distinctive refusals (`reviewer`,
> `verifier`, `auditor`, `reject`, `task`, `escalate`, `criteria`, `spec`, `definition of done`, `quality bar`, `CI`,
> `item`); the only hits were `run` and `report` in their ordinary senses, both already the file's established usage.
>
> **Clause 3's declared departure — I judge it satisfies clause 3.** Two grounds. First, the condition specifies
> content, not wording: every clause is framed *"The contract states that…"*, none says *in these words*, and clause 9
> shows the condition marking off what it leaves to the worker. Clause 1's heading *"copied here in full rather than
> pointed at"* describes the condition's own drafting — it copied the duty into itself instead of citing a node —
> rather than imposing transcription. Clause 9's *"changed in meaning"* is scoped to *"Nothing already in the file"*,
> which I established is untouched. Second, the substance holds: all three grounds are present and the conclusion
> still follows, carried mainly by the second and third. And the worker's reason is correct on the facts — the bald
> *"it holds no before-state"* would have contradicted given 3 of the same file, *"Produce a diff yourself if you want
> one"*. I exercised that given myself: `git show HEAD:` gave me a before-state and I used it to establish the `scope`
> count. The mandated wording would have shipped a self-contradiction; the scoped form is narrower and true, and still
> supports *cannot establish it*, since even holding a before-state the checker cannot know the tree as it stood when
> the condition was written — node 109 is open and may land in between.
>
> **The reviewing skill.** `mattpocock-skills:code-review`. I ran its **Standards axis only**, in an agent supplied
> with every given I hold — the condition's mandated constraints, the paths, the diff command, the standards by name,
> the house and ground rules, the wrapped-line warning — and bounded away from `.scratch/`, the record, and `git log`.
> Its **Spec axis I left unrun**: it searches `docs/`, `specs/` and `.scratch/` for a requirements document,
> `.scratch/` is off limits to me, and the acceptance condition was my only statement of intent. Of the agent's
> deviations I discarded most as not mine to hand back: the three-reason list, the enumerated finding shape, the
> record-reaching branch, `residual clause`, `the command's domain` and the `scope` sense are all **dictated by the
> condition word for word**; adding a row to `### When what you check against is itself the problem` is what clause 9
> forbids; its "nine subsections" point misreads *"the three"* (`PASS`, `FAIL`, raise, not a subsection count); and
> its claim that only extent 3 can apply is wrong, since extent 2 fits — the returned paths minus the condition's list
> is a computable bounding set. Its unrunnable-command gap I also judged not a finding: the section names no tool and
> defers wholly to what the condition recorded, and clause 1 already makes an error a return to be stated.
>
> ```
> QUESTIONS:
> - The condition's clause 6 tells the checker, where a recorded command's domain reaches the effort's
>   record, to "run it as written" and "Never quietly narrow the command to the tree". The same file
>   states "You do not read it, and you do not go looking for it" and "Where a skill's procedure and
>   your blindness conflict, blindness wins" — and .claude/skills/expedition/SKILL.md names "it may not
>   quantify over the record" as one of the two rules binding every condition. So the new branch
>   handles a condition the workflow declares unwritable, reverses the file's blindness precedent
>   without saying so, and closes off the one mitigation. The wording is the condition's own and so was
>   not the worker's to depart from. Does clause 6 want the checker to enter the record here, or should
>   such a condition route to the raise the file already has for a broken premise?
> - Clause 8 makes the hand-back a finding carrying instances, form and extent, but every other
>   hand-back route in that part of the file ships a fenced block and this one gets none — and neither
>   QUESTIONS: (this is not a question) nor NOT COVERED: (the checker did establish it) fits. A checker
>   handing an enumerator mismatch back alongside a PASS has no shape to put it in; the PASS block has
>   no slot for one. The condition never asked for a new block and clause 9 forbade touching the
>   existing shapes, so the work complied — but the route ships without a shape.
> - "enumerator" now names two objects in one file. `### What every finding carries` defines it as the
>   command the *checker* supplies with a finding, "over the part of the work the implementer may
>   edit"; the new section uses it for the command the *condition's author* ran. Clause 8 makes the
>   collision load-bearing, requiring a finding *about* an enumerator to carry an extent whose first
>   option is an enumerator. The term is the condition's own throughout. Should the file distinguish
>   the two senses, perhaps in `## Words used exactly`?
> - "the condition's own residual clause" (clause 4's phrase, verbatim) is a coined term used once and
>   defined in no shipped file, and nothing in the shipped set requires a condition to carry either a
>   residual clause or a list of places, though both rules dereference them. The name does not
>   round-trip — a reader cannot tell what shape to look for.
> - Clause 3's mandated wording "it holds no before-state" would, taken literally, have contradicted
>   the same file's given 3, "Produce a diff yourself if you want one" — which I exercised myself in
>   this very check. I judged the worker's scoped substitution to satisfy clause 3, but the departure
>   is from a condition's dictated text, so the human may want to ratify it rather than have it stand
>   on my judgement alone.
> ```
>
> My `PASS` covers the whole condition; nothing went back as not covered. Clause 10's *"reported in the handover"* I
> established from what the spawn relayed rather than from the tree, the handover not being something I hold.

**The manager's note beside it, and not the checker's.** **Nothing came back under `NOT COVERED:`** — the first check
on this effort to cover a condition whole, and the reason is in the condition rather than in the checker: node 116's
scope is one file the checker can read, with no place under `.scratch/` and no clause quantifying over the record.
Every earlier check left parts owed because its condition named the effort's own files.

**The gate is ready and is queued.** Node 107's question was live when this outcome arrived, and a live question is
never displaced, so the gate waits behind it rather than in front of it.
