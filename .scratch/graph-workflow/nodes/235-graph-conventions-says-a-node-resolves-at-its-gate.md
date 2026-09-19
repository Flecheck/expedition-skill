# `graph-conventions.md` says a node resolves at its gate, and it does not

Type: implementation
Status: resolved

Blocked by: none

## Question

*Surfaced by [node 216](216-what-a-correction-round-after-a-rebase-conflict-owes.md)'s worker, and pasted as it
wrote it.*

> `.claude/skills/expedition/graph-conventions.md`, on when an owed `NOT COVERED` part is established, says it
> happens *"by the gate at the latest, the node resolving there with nothing after it to establish anything."* The
> node does not resolve there: the landing policy resolves it after the commit, rebase, bar re-run and merge, and
> node 68 already named the consequence — *"the human's approval is no longer the last thing that can fail."* This
> node's answer widens the gap, a second approval now being reachable after the first. **The false clause is the
> reason given for a rule, so a reader who checks the reason finds it does not hold.**

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 216's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.claude/skills/expedition/graph-conventions.md`. The worker may edit that file and no other; it may
> not mark this node, resolve it, or write a line in `.scratch/graph-workflow/decisions.md` or
> `.scratch/graph-workflow/flags.md`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. The clause asserting that the node resolves at its gate, with nothing after it able to establish anything, no
>    longer appears in the file. The surrounding rule — that an owed `NOT COVERED` part is established by the gate
>    at the latest — is unchanged in what it demands.
> 2. Whatever reason stands in its place is true of the lifecycle the file describes: that the gate is the last
>    point at which the human can act on it, rather than the point at which the node resolves.
> 3. No other rule in the file changes what it demands, and no rule is added.
> 4. The file's existing section order and heading names are unchanged.
> 5. Every markdown link in the file resolves to a path that exists, except a link to a path outside this
>    repository, which is out of scope.
> 6. No file outside `.claude/skills/expedition/` is modified.
> 7. The standing quality bar for this repository holds of the finished tree.

## The manager's note at filing

*Not a change to anything above.*

**Two `NOT COVERED` parts were settled after their gate on this effort today**, which is the clause's falsity
demonstrated rather than argued: node 198's two, settled by the manager at its landing, and node 229's one, settled
by the manager at its gate. In all three the establishing happened at or after the moment the clause says nothing
can follow.

**Four open nodes now edit `graph-conventions.md`** — this one, [node
222](222-the-conventions-file-says-a-worker-reads-the-whole-map.md), [node
228](228-graph-conventions-says-map-notes-holds-three-things-kept-elsewhere.md) and [node
233](233-ship-the-two-never-delete-tests-into-the-conventions-document.md). **Two workers must not hold that file at
once.** The manager holds the sequencing and has written no blocking edge, none of the four needing what another
produces.

## Flags

`235.1` **· settled** `ASSUMPTION` — I wrote the replacement reason in the acceptance condition's own words and did not qualify it
for the case node 216 opened, where content authored during a post-approval rebase returns to the checker and the
gate, so a second approval is reachable after the first. My ground: clause 2 of the condition scopes the reason to
"the lifecycle the file describes", and `graph-conventions.md` describes one gate; and on the wider lifecycle the
claim still holds, because whichever gate is the node's last, a gate is the only point at which the human acts on
the work. A qualification would have put landing-policy material, which no worker reads, into a shipped file.

`235.2` **· settled** `ASSUMPTION` — Clause 5 of the condition demands that every markdown link in the file resolve to a path that
exists. The file holds exactly one `](` occurrence: `[<node name>](nodes/NN-<name>.md)`, inside the fenced block
showing `flags.md`'s line form. I read the clause as not reaching it and left it untouched. My ground: it is a
template with metavariables in both halves rather than a link to any path, the file's own scanning rules tell a
reader to skip fenced code blocks, and repairing it would have changed a documented shape, which clause 3 forbids.
No other markdown link exists in the file, so clause 5 is otherwise vacuously met.

`235.3` **· settled** `ASSUMPTION` — ***Filed by the manager***, this being a departure the worker reported in its retrospective
rather than as a flag of its own. The worker did not read `decisions.md` whole. Its words, `verbatim`: *"My spawn
named no sections of it, and my contract says I read 'the sections the spawn names'. I did not read its 147 lines
whole; I grepped it for `gate`, `NOT COVERED` and `resolve` and read the fourteen matching lines, which gave me node
216's line — the one that bears on flag 235.1 — and confirmed nothing else touched the clause. If that is short of
the contract, the contract's wording is what made it look permitted."* The manager's own note beside it: the spawn
named no sections because this effort declares no label vocabulary and the spawn said the index was unscoped, which
is the manager's wording rather than the worker's.

## Retrospective

*This effort's own standing instruction, carried in the spawn and shipped nowhere. Pasted as the worker wrote it.*

1. **What I had to hunt for.**
   - *Who wrote the removed clause.* I needed it for `INVALIDATIONS`, which nothing in my spawn or
     node file supplied. One `grep -rln` over `.scratch/graph-workflow/` for the clause's own
     words found node 38 (author) and node 75 (restatement) in one shot. Cheap, but it is the
     one thing a node of this shape always needs and never gets: **a node whose work is "remove
     this false sentence" could carry, in the node file, where else that sentence appears in the
     record.** The surfacing worker at node 216 had just done that search to find it at all.
   - *Whether my two side-findings were already nodes.* The `.gitignore` comment cites
     `map-implementation-rules.md`, *"How the worktree is made"*, a heading that now lives in
     `map-manager-only.md`; and `CONTEXT.md` says the node ends at the gate. Two greps over
     `nodes/` settled it: the first is already [node
     227](227-gitignore-cites-a-quoted-phrase-that-resolves-to-nothing.md), the second is
     nobody's. Both greps were guesses at wording — `grep -rln "gitignore"`, then `grep -rln "ends
     at the gate"` — and a wording-blind way to ask *is this already a node* would have been
     surer, not just cheaper.
   - *Where I actually work.* `EnterWorktree` with the path my spawn gave refused: *"the current
     working directory /home/mathieu/projects/graph-agent is the repository root, not an isolated
     worktree — switching is only available to sessions whose working directory is inside a
     worktree of this repository."* The tool's own description says the opposite for a first entry
     from the launch directory. I confirmed the worktree exists in `git worktree list` and then
     worked by absolute path into it, which cost two calls and a decision I should not have had to
     make. **Every edit is in the worktree; my shell's cwd is not.** Worth knowing whether the
     concurrent worker hit the same wall — if it did, the spawn should stop naming `EnterWorktree`
     for a worktree the manager already created and say *edit by absolute path* instead.

2. **What arrived that this node did not need.**
   - *From the spawn.* The retrospective's four questions arrive twice: in full in my spawn, and
     again in `map.md`'s `## Notes`, where the superseded wording sits beside the current one. I
     read both. One of them is enough, and the spawn's copy is the one that must stay.
   - *From `map.md`, read whole as required.* For a two-clause prose edit, the items that bore on
     nothing were the human-queue count and the one-question rule, the payload trigger, the
     no-diff-command rule, the manager-never-idles rule, the resume rule, the spent moved-standard
     licence, and the heterogeneous-harness note. That is most of `## Notes`. It is not a defect of
     any item — every one binds *some* worker — but it is the cost the file's own design accepts.
     The arrangement that would cut it for my kind of node already exists and is one step short:
     `map-implementation-rules.md` proves a per-reader sibling works. **Several of those items are
     addressed to the manager alone** (the queue count, the payload trigger, the diff command, the
     never-idle rule, the resume rule) **and would sit in `map-manager-only.md` without a worker
     losing anything.**
   - *From `map-implementation-rules.md`.* The review-route paragraph is the longest thing in the
     file and is the checker's; the `CONTEXT.md`-as-a-grep-list trap inside it is the checker's
     too. A worker needs the bar's commands, the ground rules, the four writing rules, and the
     record-as-work rule. A heading split inside that one file — what the worker writes to, what
     the checker holds it against — would let each read its half, and it is the file's own
     principle applied once more.
   - *Whole file taken for one fact.* `CONTEXT.md`: I went for the senses of `gate`, `resolve` and
     `node` and took 303 lines. **Here the surplus paid** — the `implementation` entry's false
     clause is the new node above, and I would not have seen it from a targeted grep. Reported as
     the counter-example the question asks for: reading it whole is right for a node editing
     shipped prose.
   - *`decisions.md`, and a departure I am flagging rather than hiding.* My spawn named no sections
     of it, and my contract says I read "the sections the spawn names". I did not read its 147
     lines whole; I grepped it for `gate`, `NOT COVERED` and `resolve` and read the fourteen
     matching lines, which gave me node 216's line — the one that bears on flag 235.1 — and
     confirmed nothing else touched the clause. If that is short of the contract, the contract's
     wording is what made it look permitted.

3. **What would have made this node easier.**
   - *In the node file.* A pointer to where else the removed clause lives in the record (see 1).
     The manager's note already did the equivalent for file contention — naming the three other
     open nodes on `graph-conventions.md` and saying I hold it alone — and that note was the single
     most useful non-mandatory thing I read. The same note shape applied to the text being removed
     would have saved the only real search I ran.
   - *In the spawn.* Say what to do when `EnterWorktree` refuses, or drop it (see 1).
   - *In the record.* Nothing. The condition was measurable clause by clause and I never had to
     guess at what it wanted; clause 2 handing me the replacement reason almost verbatim is why
     this node has two flags instead of a raise.

4. **What was stale, wrong, or contradictory.**
   - *The thing this node existed to fix*, in `graph-conventions.md`. Fixed.
   - *`CONTEXT.md`'s `implementation` entry*, *"the node ends at the gate"* — the same falsity in
     the glossary the shipped files declare authoritative. New node above.
   - *Node 38's answer and node 75's duty 61*, both carrying the removed clause. On
     `INVALIDATIONS`.
   - *`.gitignore`'s comment*, citing `map-implementation-rules.md`, *"How the worktree is made"* —
     that heading is in `map-manager-only.md`. Already [node
     227](227-gitignore-cites-a-quoted-phrase-that-resolves-to-nothing.md); no new node.
   - *The `EnterWorktree` tool description* contradicts the tool's behaviour for a first entry from
     the launch directory. Not this repo's file, so nothing to file against it — recorded here
     because the spawn tells every implementation worker to call it.

## Review

### Run 1 — `PASS`

*The checker's own text, pasted. It was spawned by the manager, was given the acceptance condition as extracted
text, the bar as properties, the changed paths, and this effort's ground rules and four standing rules for writing
copied as text, and was given nothing from this node or from the effort's record.*

PASS

**Standards read.** `.scratch/graph-workflow/map-implementation-rules.md` (the effort's implementation-rules file; resolved by a single listing of `.scratch/`, which holds one directory, `graph-workflow`). The standards it states are: `/coding-principles` and `/naming`; `CONTEXT.md`'s `_Avoid_` lines; this effort's ground rules and its four standing rules for writing (both held in that file); `.claude/skills/expedition/graph-conventions.md`; and `/writing-for-agents`. It names **no reviewing skill** for this repo and says a checker does not go looking for one, so I ran none and delegated nothing. Bearing on this work: `/writing-for-agents`, the four standing rules for writing, `CONTEXT.md`'s `_Avoid_` lines, and `graph-conventions.md` itself. Not bearing: `/coding-principles`, `/naming` (no code, no identifiers), and the file's rule about work that is the effort's own record (the changed path is a shipped skill file, not a record file).

**A standard moved under the check, and I settled that first.** `graph-conventions.md` is both a named standard and the one changed path. Comparing operative content element by element on unwrapped text: the edit touches one sentence's trailing clause only, and the operative demand in that sentence — *"It happens by the gate at the latest"* — is byte-identical on both sides. The sets of things the standard requires or refuses are identical; only the wording explaining one of them changed. Nothing was added or removed. So the standard still stands and the check remained possible throughout.

**How I established each part of the condition** (diff: `git -C /home/mathieu/projects/graph-agent/.claude/worktrees/235-graph-conventions-node-resolves-at-gate diff` — one hunk, 2 insertions, 1 deletion; `git log 70ac77c..HEAD` is empty, so the working tree is the whole of the work):

1. Met. The removed clause was `the node resolving there with nothing after it to establish anything`. I searched the whole file unwrapped (`\s+`→space, then substring search for `nothing after it`, `node resolving`, `resolving there`, `resolves there`) — no occurrence anywhere in the finished file. The surrounding rule `It happens by the gate at the latest,` survives verbatim, so what it demands is unchanged.
2. Met. The replacement reads `the gate being the last point at which the human can act on it rather than the point at which the node resolves`, and that is true of the lifecycle this file describes. `### ## Review` names the gate's three outcomes approve / correct / reject, and a reject routes the node to `out-of-scope`, `superseded`, or back to `open` — so the node does not resolve at the gate. `### Resolve` is a separate manager procedure, and mechanical check 9 (`no resolved node still carries one opening with OWED`) puts the deadline before resolution, not at it. The file describes no human act on the node after its gate. (`CONTEXT.md`'s glossary corroborates: *Gate* — "the one point on the code path where work stops until the human acts"; *Reject* — "the node does not resolve".)
3. Met. The diff is a single hunk inside one paragraph; no other rule's text moved and no rule was added.
4. Met. No `#` or `##` or `###` line appears in the diff on either side; section order and heading names are byte-identical to `70ac77c`.
5. Met, with one thing worth stating plainly. Searching the file unwrapped for `[...](...)`, autolinks and reference-style definitions returns exactly one link-shaped string: `[<node name>](nodes/NN-<name>.md)`, and it sits **inside a fenced code block** as the template form of a `flags.md` line. Fenced content is literal text rather than markdown, so the file renders zero markdown links and the condition holds vacuously. Under the other reading — counting the fenced placeholder as a link — its target is a template (`NN`, `<name>`) that resolves to no path; that text is pre-existing, untouched by this work, and a `FAIL` on it would fail the work for something it did not write. I record both readings so the manager can settle which it meant. Enumerator over the file the worker may edit: `python3 -c "import re,sys;print(re.findall(r'\[[^\]]*\]\([^)]*\)',re.sub(r'\s+',' ',open(sys.argv[1]).read())))" .claude/skills/expedition/graph-conventions.md`.
6. Met. `git status --porcelain --untracked-files=all` returns exactly one line, ` M .claude/skills/expedition/graph-conventions.md`. No untracked files, no other modifications, and `decisions.md`, `flags.md` and the node file are all unmodified.
7. Met — see below.

**The bar, discovered from the repository itself.** The repo root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. A `find` to depth 3 for `package.json`, `Cargo.toml`, `pyproject.toml`, `Makefile`, `justfile`, `flake.nix`, `.pre-commit-config.yaml` and any `*.yml`/`*.yaml` returns nothing; there is no `.github`. The one ignore file, `.gitignore`, lists `.worktrees/` and `.claude/worktrees/` and invokes nothing. So there is **no build, no tests, no formatter and no CI to run** — printing nothing because there was nothing to run, which is a complete bar on its command half rather than a deficient one, and it matches what the implementation-rules file records.

The bar's remaining half is the standards. Held by hand against the two changed lines: no `CONTEXT.md` `_Avoid_` word appears in the new wording (`gate`, `human`, `act`, `node`, `resolves` are all the approved terms; the refused `review`, `reject`, `done`, `complete` do not occur in it). Against `/writing-for-agents`: the sentence is not a no-op — it replaces a false reason with the reason a reader needs in order to know why the deadline sits where it does — it is co-located with the rule it explains, and the positive is stated before the contrast. Against the four standing rules for writing: this is prose explaining why and stays one clause; no shape, no heading and no citation moved, and nothing is cited by line number. Against the ground rules: the edit assumes no repo, machine or toolchain, adds no dependency on a skill being invocable, and tells no agent to address the human.

**What this run handed back alongside its outcome.** One question, which travels to the human inside the gate payload and queued on nothing of its own: which reading of clause 5 the manager meant, the checker having recorded both and failed the work on neither. **No part of the condition was left uncovered.**

### Gate — `approve`

**The human's answer**, `verbatim`: *"approve"*

Landed under the effort's landing policy: one path-limited commit of `.claude/skills/expedition/graph-conventions.md`
in the node's worktree, no rebase needed (the worktree's base and the manager's `HEAD` were both `70ac77c`), the
bar's command half empty so nothing to re-run, `git merge --ff-only` onto `master`, worktree removed and branch
deleted. Commit `23eb355`, carrying the trailer `Node: graph-workflow/235`.

**The three flags this node held are settled by this approval**, under the human's standing instruction that
approving a node's end settles its flags.

**The checker's question travelled with this gate and the human did not answer it separately.** It asked which
reading of clause 5 the manager meant — whether the every-link-resolves demand reaches the metavariable placeholder
inside a fenced block. The approval settles the work rather than the reading, and the manager has not settled the
reading on its own judgement.

## Answer

*The worker's own text, pasted.*

The false clause is gone from `.claude/skills/expedition/graph-conventions.md`, and the rule it
was the reason for is untouched. Under `## Review`, the paragraph on establishing a part a
checker did not cover read:

> It happens by the gate at the latest, the node resolving there with nothing after it to
> establish anything.

and now reads:

> It happens by the gate at the latest, the gate being the last point at which the human can act
> on it rather than the point at which the node resolves.

**The demand is unchanged** — establishing still happens by the gate at the latest — and only its
stated ground changed. What was false was the ground: the node does not resolve at its gate, the
landing policy resolving it after the commit, rebase, bar re-run and merge, so a reader who
checked the reason found it did not hold.

**The replacement is written in the acceptance condition's own words**, near-verbatim from its
clause 2, rather than in a wording of the worker's own. Two calls sit behind that. First, the
reason is true of the lifecycle *this file* describes, which is the scope clause 2 sets: this file
knows one gate, with outcomes approve / correct / reject, and it knows that something happens
"between the gate and the repository" (its description of the landing policy in
`map-manager-only.md`). Second, it is not qualified for the case [node
216](216-what-a-correction-round-after-a-rebase-conflict-owes.md) opened, where a second
approval is reachable after the first: whichever gate is the node's last, the human acts at a gate
and nowhere else, so "by the gate at the latest" still names the deadline. That call is flag 235.1
above.

**A two-sentence version was written first and collapsed to one.** The discarded second sentence
("The node does not resolve there: work carries on between the gate and the repository") was
dropped against the `/writing-for-agents` standard's no-op test — it paid load to restate the
correction the first sentence already carries — and against standing writing rule 1, the prose
that explains why being the part that compresses.

**The same false claim survives in one other shipped file and in two resolved nodes.** `CONTEXT.md`'s
`implementation` entry ends *"the node ends at the gate"*; clause 6 of the condition put it out of
reach, so it is reported as a new node below. Node 38's `## Answer` states the removed clause as
"one addition no clause asked for", and node 75's duty 61 restates it verbatim — both on
`INVALIDATIONS`. No other file under `.claude/skills/` carries it: searched for `nothing after
it`, `resolving there`, `resolves there` and `node ends at the gate` across `.claude/skills/` and
`CONTEXT.md`.
