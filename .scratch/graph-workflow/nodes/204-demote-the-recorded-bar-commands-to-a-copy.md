# Demote the recorded bar commands to a copy confirmed against the repo, in the implementer's and the manager's contracts

Type: implementation
Status: resolved

Blocked by: none

## Question

*Surfaced by [Which statement of the bar's commands wins where a recorded copy and the repo's own
instructions disagree](174-which-statement-of-the-bars-commands-wins.md)'s worker, and pasted as it wrote it.*

> The implementer's contract tells its worker to use whatever the implementation-rules
> file records for this repo and to discover the commands only where that file records none, so the
> recorded copy is authoritative for it. The checker discovers from the repo. The manager's contract
> states the trusted-copy model twice more and still offers the bar's commands as something a checker's
> spawn may carry. Bring all four sites onto the one rule: the repo's own statement wins, the record is
> confirmed against it before use, and a difference is reported rather than charged against the work.

**Blockers, in the worker's words:**

> none. Fifteen open nodes target `.claude/skills/expedition/SKILL.md`; each one's
> acceptance condition was read and none claims the passages this changes, so any order works and the
> manager holds the sequencing — flagged above. Running after
> [node 173](173-stop-the-checkers-spawn-carrying-the-bars-commands.md) is the tidier order, that node
> repairing the checker's own copy of the given this changes in the manager's mirror of it, so the two
> wordings can be made to match.

## Acceptance condition

*Written by node 174's worker. Pasted as it wrote it, and not the manager's.*

> The work is two files, relative to the repository root:
> `.claude/skills/expedition-implementation/SKILL.md` and `.claude/skills/expedition/SKILL.md`. The
> worker may edit those two and no other, and may not write any file under `.scratch/`.
>
> **The rule the work states, and against which every clause below is measured:**
>
> > A repo's own live statement of its build, test and format commands is authoritative. Where an
> > effort's implementation-rules file records those commands, that record is a copy of an earlier
> > discovery: an agent confirms it against what the repo itself says before using it, rather than
> > trusting it. Where the two differ the repo's statement wins, the agent runs the repo's commands,
> > and it reports the difference so the record can be repaired; the difference is never a reason to
> > judge the work defective. Where the repo states no commands of its own, the record is the only
> > statement there is and stands as it is, unconfirmed.
>
> Done means every one of the following is true of the finished tree.
>
> 1. In `.claude/skills/expedition-implementation/SKILL.md`, the section headed `## The bar` no longer
>    tells its reader to use whatever an implementation-rules file records for this repo, and no
>    longer conditions discovery from the repo on that file recording nothing.
> 2. That same section states the rule quoted above in full: that the repo's own statement is
>    authoritative; that a recorded copy is confirmed against the repo before use rather than trusted;
>    that the repo's statement wins where the two differ; that the difference is reported and never
>    counts against the work; and that an absent repo statement leaves the record standing unconfirmed.
> 3. That section keeps its statement of the bar's properties — the work builds, it warns about
>    nothing, it is formatted, the tests relevant to the change pass, and whatever else the repo itself
>    demands is satisfied — and keeps its statement that a repo with no build, no tests and no
>    formatter meets the bar on its remaining half, that being a complete bar and not a deficient one.
> 4. In `.claude/skills/expedition/SKILL.md`, no sentence states that the bar's commands live in the
>    effort's map, live in any one file and nowhere else, or are written once into the effort's map.
>    Where that file says what the effort's map holds in relation to the bar's commands, it says the
>    map holds a record of them that is confirmed against the repo before use.
> 5. In `.claude/skills/expedition/SKILL.md`, the list of what a checker's spawn receives no longer
>    offers the bar's commands as something that spawn may carry, and no item in that list is
>    conditioned on the effort's map recording commands for the repo. That list states instead that
>    the checker discovers the commands from the repo itself, and states the bar's properties as what
>    the spawn conveys.
> 6. Where either file refers to the file in which a repo states its own commands to an agent, it
>    names that file by role and position only. No particular filename for such a file appears
>    anywhere in either finished file.
> 7. Neither finished file states or implies that an implementation worker and its checker take the
>    bar's commands from different places, or from different files.
> 8. Any sentence in either file that introduces a list by stating how many items it holds states a
>    count arithmetically correct for the items that list then holds.
> 9. No text in either file outside the passages clauses 1 to 8 reach is deleted or reworded.
> 10. Neither finished file names a plugin, requires any skill to be invocable, or assumes a
>     particular repository, machine or toolchain.
> 11. No file other than the two named above is modified, and no file under `.scratch/` is modified.
> 12. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This is one node over two shipped files, and its author said why.** In its own words at filing, the repair *"covers all four sites in one node, on the ground that the defect being fixed **is** an inconsistency between shipped files and landing half of it would recreate one."* That call is flag `174.4`.

**Its own author read fifteen open conditions on `.claude/skills/expedition/SKILL.md` to establish that no blocking edge is owed**, and named the order it would prefer without demanding it: after [node 173](173-stop-the-checkers-spawn-carrying-the-bars-commands.md), so the checker's own copy and the manager's mirror of it can be made to agree. **The manager holds the sequencing on that file and this node states no edge.**

## Flags

*All three are the worker's own text, pasted. The ids are the manager's bookkeeping and nothing else.*

`204.1` **· settled** `ASSUMPTION` — **I settled that clause 7 does not reach the two passages that still route an implementer to the record, and stated the sameness in the checker's item instead of rewording them.** `expedition/SKILL.md`'s implementation-spawn bullet says the spawn carries *"the bar by way of the map"*, and the implementer's read-list says the implementation-rules file holds *"the bar's commands where the effort has recorded them"*. Read literally against clause 7 — nothing may state or imply that an implementer and its checker take the commands from different places — either could be argued to imply it, since the checker's item now says *from the repo itself*. I judged they do not: both name the route by which the *record* travels, neither claims the record is authoritative, and the rewritten `## The bar` sends the implementer to the repo. Clause 9 protects both passages, so rewording them to be safe would have risked the opposite violation. What I did instead was add *"exactly as the implementation worker does"* to the checker's item, which denies the difference in the same file at the cost of five words.

`204.2` **· settled** `ASSUMPTION` — **I settled that the ban on naming the file a repo states its commands in does not reach the effort's own implementation-rules file, and used role-only phrasing where I had a choice.** Clause 6 says no particular filename for such a file may appear anywhere in either finished file, and flag `167.1` with ground rule 1 behind it bar a shipped contract from naming one harness's convention. The effort's record file is a different object — the rule I am shipping distinguishes them in its own first two sentences — and its filename already stands in two passages clause 9 protects, so a reading that swept it in would put clauses 6 and 9 in irreparable conflict. I took the role reading, and in the passage I rewrote I still wrote *"the effort's implementation-rules file"* rather than the filename, so the section names no file at all.

`204.3` **· settled** `ASSUMPTION` — **I settled that `## Where two of these pull against each other` states no list count, and left it out of the arithmetic audit.** The condition required every sentence introducing a list by stating its size to be arithmetically correct, and that heading sits above three bullets. Each bullet is explicitly one duty set against another — the scribe rule against the fuller form of a flag, supplying what a condition omits against authoring one, arrival order against the cost of a waiting gate — so *"two of these"* counts the duties in each collision rather than the collisions in the list; node 76's own index line calls them *"the three that pull against each other"*. Editing the heading to say *three* would have reworded protected text on a misreading.

## Review

### Checker run 1 — `PASS`

*Pasted as the checker wrote it, in its own order. Every sentence is the checker's.*

> All checks are complete. Assembling the outcome.
>
> **Settled first, before checking anything else — the contract's *"Where the work moved one of them"* branch.** My standards come from `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md`. That file is untouched (`git status --porcelain -- .scratch/` returns nothing). Of the standards it names — `/coding-principles`, `/naming`, `CONTEXT.md`'s `_Avoid_` lines, the effort's ground rules, the four standing rules for writing, `.claude/skills/expedition/graph-conventions.md`, `/writing-for-agents`, and the node's acceptance condition — **not one is a changed path**. `graph-conventions.md` sits in the same directory as one of the changed files but is itself unmodified. So no standard I hold the work against moved, in operative content or in rationale, and the branch does not fire. The changed files are shipped worker contracts, one of them my own sibling contract, but a sibling contract is not among my standards — my standards reach me only from the implementation-rules file. Check proceeds normally.
>
> ```
> PASS
>
> STANDARDS READ: /home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md.
>   Bore on this work: the effort's ground rules (1-5); the four standing rules for writing;
>   CONTEXT.md's _Avoid_ lines; graph-conventions.md; /writing-for-agents; /naming;
>   /coding-principles. No reviewing skill is named for this repo — the rules file says so in as
>   many words — so I ran no reviewing skill and went looking for none. I read /writing-for-agents,
>   /naming and /coding-principles into my own context as standards; nothing was delegated, so no
>   agent was handed less than I was.
> CHANGED-PATHS RULE: the rules file's "work may be the effort's own record" rule did not fire —
>   neither changed path is in the effort's record directory. I confirmed no node status line, no
>   decisions.md and no flags.md appears among the work (git status --porcelain shows exactly two
>   entries, both under .claude/skills/).
> ENUMERATOR: the condition records none, so there was no command to run as written.
>
> 1. MET. `## The bar` no longer says "use whatever `map-implementation-rules.md` records for this
>    repo", and no longer says "Where it records none, discover them from the repo". Discovery is
>    now unconditional and first: "discover them from the repo, and hand what you found back in
>    your handover". Read from the finished file and from the hunk's deleted lines.
> 2. MET. All five elements of the quoted rule are present, in order: authority ("a repo's own live
>    statement of its build, test and format commands is authoritative"); confirmation rather than
>    trust ("that record is a copy of an earlier discovery — you confirm it against what the repo
>    itself says before using it, rather than trusting it"); the repo wins ("Where the two differ
>    the repo's statement wins, you run the repo's commands"); reported and never counted against
>    ("you report the difference so the record can be repaired; the difference is never a reason to
>    judge the work defective"); absent repo statement ("Where the repo states no commands of its
>    own, the record is the only statement there is and stands as it is, unconfirmed").
> 3. MET. The properties survive verbatim ("it builds, it warns about nothing, it is formatted, the
>    tests that are relevant to your change pass, and whatever else the repo itself demands is
>    satisfied"), and so does the complete-bar sentence ("A repo with no build, no tests and no
>    formatter meets the bar on its remaining half; that is a complete bar and not a deficient
>    one") — carried over word for word from the deleted text.
> 4. MET. I swept every sentence of expedition/SKILL.md mentioning "bar" or "command" over
>    unwrapped text (a line-based search would have missed the wrapped ones). "written once into
>    the effort's map" is gone; the map bullet's "nowhere else" list no longer holds the commands.
>    Both sentences that say what the map holds in relation to the bar's commands say it the
>    prescribed way: "It also holds a record of the bar's commands once discovered for this repo,
>    which an agent confirms against the repo before using", and "the record of them in the
>    effort's map is confirmed against the repo before use".
> 5. MET. The checker's spawn list no longer offers the commands: "the bar — its properties, which
>    are the whole of what the spawn conveys of it: the commands the checker discovers from the
>    repo itself, exactly as the implementation worker does". No item in that list is conditioned
>    on the map recording commands (the one surviving condition, "Where the effort declares none,
>    that given is absent", is on the effort declaring ground rules).
> 6. MET, on a reading I had to settle — see the note below this block. No filename appears in
>    either finished file that is a file in which a repo states its own build/test/format commands
>    to an agent. The complete set of filename tokens in the two finished files is: expedition —
>    decisions.md, graph-conventions.md; expedition-implementation — decisions.md, flags.md,
>    map.md, map-implementation-rules.md. Neither file refers to a repo's own command-stating file
>    by any name at all; it says "the repo", "what the repo itself says", "its own".
> 7. MET. The checker's item asserts sameness outright — "exactly as the implementation worker
>    does" — and both files route the commands to the repo. The spawn line "the bar by way of the
>    map" survives (clause 9 forbade touching it) and states how the bar travels in a spawn rather
>    than where the commands come from, so it neither states nor implies two places.
> 8. MET, checked over both whole files rather than the hunks. I extracted every paragraph carrying
>    a count word from unwrapped text and counted the items each introduces. 32 counted lists in
>    expedition/SKILL.md and 17 in expedition-implementation/SKILL.md all come out arithmetically
>    correct. The one the work changed: "two things live there and nowhere else: the effort's
>    ground rules, and the standing steering the human has given" = 2. Two I checked with care:
>    "Six parts, every time" against a seven-line template — correct, `HANDOVER:` carries the
>    node's name and is the label, not a part, which the manager contract confirms ("Five parts …
>    An implementation worker returns a sixth, the gate payload"); and the heading "Where two of
>    these pull against each other" over three bullets — not a count of the list's items but of the
>    rules in each collision, so outside clause 8's predicate.
> 9. MET. Exactly four hunks (git diff -U0 | grep -c '^@@' = 4), 17 insertions and 10 deletions,
>    and `git diff -w --stat` is byte-identical to `git diff --stat`, so nothing changed by
>    whitespace or reflow either. I read all ten deleted lines: each falls inside the passages
>    clauses 1-5 and 8 reach, and every phrase clause 3 protects reappears verbatim.
> 10. MET. No plugin is named in either finished file. No manifest, task runner, formatter, test
>     framework, machine path or repository name appears. The only skill either file mentions is
>     "a method skill", conditionally ("Where a method skill's instructions … conflict"), which
>     requires nothing to be invocable; it is pre-existing and unchanged. The changed text itself
>     names only "the repo", which is the ground-rule-1 direction of travel.
> 11. MET. `git status --porcelain --untracked-files=all` returns exactly two lines, both ` M` on
>     the two named paths. Nothing untracked, and `git status --porcelain -- .scratch/` is empty.
> 12. MET — the bar holds, and its command half is confirmed against the repo rather than taken
>     from the spawn. See the bar block below.
>
> BAR — what I ran and what it printed
>   Command half, confirmed against the repo itself (which is the rule this work ships, so I ran
>   the confirmation rather than trusting the record):
>     - `ls -a` at the worktree root prints only `.claude  CONTEXT.md  .git  .gitignore  .scratch`.
>     - `git ls-files` filtered for package.json, Cargo.toml, pyproject.toml, setup.py, go.mod,
>       Makefile, justfile, Taskfile, .pre-commit, Gemfile, pom.xml, build.gradle, CMakeLists,
>       any .nix, .editorconfig, tsconfig, eslint, prettier, ruff, biome, .tool-versions and
>       requirements*.txt → "(none)".
>     - `ls -a .github` → "(no .github)".
>     - `cat .gitignore` → two entries, `.worktrees/` and `.claude/worktrees/`, both comments and
>       paths, invoking nothing.
>     So: no build, no tests, no formatter, no CI, nothing to invoke. Nothing to run, and nothing
>     printed because there was no command to print anything. This matches the record in the
>     implementation-rules file exactly, so there is no difference to report.
>     Under the "if relevant" clause that is a COMPLETE bar on its remaining half, not a deficient
>     one.
>   Non-command half:
>     - /writing-for-agents (read as a standard). The change moves the files toward its
>       single-source-of-truth and cache levers — "the environment is a source of truth too … a
>       document that restates it is a cache", which is the work's own thesis. Prohibitions are
>       paired with positive targets, the "why" is compressed to one clause ("a copy of an earlier
>       discovery"), and the five added sentences each change behaviour against the default, so no
>       no-ops and no sprawl. Co-location holds: the rule sits under `## The bar` beside the
>       properties, and in the manager contract beside the existing `map` and `the bar` bullets.
>     - /naming: no identifier introduced. "the effort's implementation-rules file" is a role name
>       already used by the standards file and the checker contract. "a record of the bar's
>       commands" claims no property the value lacks — a record rather than a statement — which is
>       the skill's own claim-no-property rule and is the point of the change.
>     - /coding-principles: prose-only diff, no code, no types, no error handling; nothing hoisted.
>       Nothing to fault.
>     - CONTEXT.md `_Avoid_` lines: checked the distinctive refusals by hand rather than by grep, as
>       the rules file directs. None appears in the changed text — no "quality bar", no "CI", no
>       "default checks", no reviewer/verifier/auditor/reject, no issue/ticket/card/item/gap/task,
>       no spec/criteria/definition of done. The only hits a grep list would return are "report the
>       difference" and "you run the repo's commands", both ordinary-English verbs and exactly the
>       false-positive class the rules file warns about; "where" is refused by no _Avoid_ line.
>       CONTEXT.md's own `The bar` entry already says "the commands are discovered per repo", so the
>       change agrees with the glossary rather than contradicting it.
>     - graph-conventions.md (a standard, unmodified): still says the map's `## Notes` holds "the
>       bar's commands once they have been discovered for this repo". That stays true of the
>       finished tree — the change is to the record's standing, not its location — so no conflict,
>       and clause 11 forbade touching it anyway.
>     - Ground rules 1-5: all held. Rule 1 is the change's direction of travel. Rule 2 holds —
>       `## The bar` states the rule in full without needing any skill to be invocable. Rule 3
>       holds — "you report the difference" is routed through the handover, named in the sentence
>       before it, and addresses no human. Rules 4 and 5 hold: six lines of prose, no new
>       mechanism, no new file, no new section.
>     - Four standing rules for writing: the "why" is compressed and the shapes are not (1); no node
>       citations were added, which is correct for a shipped file under ground rule 1 (2); the rule
>       is reachable by one heading, `## The bar` (3); no line number is cited anywhere in the
>       change (4).
>     - Formatted: changed lines wrap at 82-107 characters, inside both files' existing convention
>       (bodies run 99-108). No trailing whitespace and no tabs in any added line.
>     - The acceptance condition: covered clause by clause above.
> ```
>
> **The one reading I had to settle, stated so you can correct me.** Clause 6 refuses a filename for *"the file in which a repo states its own commands to an agent."* I read that as the **repo's own** command-stating file — an agent-instructions file or a manifest — and not as the effort's implementation-rules file. My grounds are the condition's own vocabulary: its quoted rule sets *"a repo's own live statement"* against *"the effort's implementation-rules file records those commands"*, and clause 6's subject is *"a repo"* with the possessive *"its own"*, which is the first term and not the second. The implementation-rules file belongs to an effort, and the whole thesis of this work is that its record is precisely *not* the repo's own statement.
>
> Under the other reading, **the work would FAIL clause 6**: `map-implementation-rules.md` still appears by filename twice in the finished implementation contract, under `## What you read` ("`map-implementation-rules.md`, beside it — the standards your work is held to, and the bar's commands where the effort has recorded them") and under `## The standards your work is held to` ("It is `map-implementation-rules.md`, the sibling of the effort's map"). I did not fault those, because on my reading clause 6 does not reach them and clause 9 then forbids touching them. What made me look twice is that the worker replaced that filename with the role phrase inside `## The bar` — but clause 2 dictates that phrasing directly, so the worker was following clause 2's words rather than clause 6's.
>
> **QUESTIONS:** none.
> **NOT COVERED:** none — every clause was establishable from the two changed paths, the diff, the working tree and the repo itself.
>
> One observation carrying no finding, for whoever holds the record: `expedition/SKILL.md` still tells a spawn to carry "the bar by way of the map" for an implementation node, while the checker's item four sections later says the commands are discovered from the repo "exactly as the implementation worker does". Both remain true under the new rule, and clause 9 put the first sentence out of the work's reach, so it is not a defect — but the first now conveys less than it did before this change.

*No `NOT COVERED`. No questions raised — in its words: “every clause was establishable from the two changed paths, the diff, the working tree and the repo itself.”*

### Gate — `approve`

**The human's word, `verbatim`.**

> approve

*One checker run, `PASS`, with no questions and nothing uncovered. No correction round. All three flags are settled by the approval — including `204.2`, which the checker independently reached the same way while stating that the other reading would have made the work `FAIL` clause 6.*

## Answer

*Pasted as the worker wrote it.*

> **Four sites across two shipped contracts now state one rule: a repo's own live statement of its build, test and format commands is authoritative, and a recorded copy is confirmed against it before use rather than trusted.** The implementer's contract was the outlier node 174 named — it told its worker to *"use whatever `map-implementation-rules.md` records for this repo"* and to discover from the repo only *"where it records none"* — and the manager's contract held the same trusted-copy model in two glossary entries and offered the commands as something a checker's spawn may carry.
>
> **What changed, by site.**
>
> - **`.claude/skills/expedition-implementation/SKILL.md`, `## The bar` (lines 91-99).** The second paragraph is replaced. It now leads with the repo's statement being authoritative, tells the worker to discover the commands from the repo and hand them back, demotes the effort's implementation-rules record to *"a copy of an earlier discovery"* the worker *"confirm[s] against what the repo itself says before using it, rather than trusting it"*, gives the repo the win where the two differ, requires the difference reported so the record can be repaired, states that the difference *"is never a reason to judge the work defective"*, and closes the remaining branch: where the repo states no commands of its own the record *"is the only statement there is and stands as it is, unconfirmed"*. The first paragraph's five properties and the *"complete bar and not a deficient one"* sentence are untouched.
> - **`.claude/skills/expedition/SKILL.md`, the `map` glossary entry.** The bar's commands leave the *"live there and nowhere else"* list, which falls from three items to **two** — the ground rules and the standing steering. A new clause says the map *"also holds a record of the bar's commands once discovered for this repo, which an agent confirms against the repo before using"*.
> - **`.claude/skills/expedition/SKILL.md`, the `the bar` glossary entry.** *"the commands are discovered per repo and written once into the effort's map"* becomes *"a repo's own live statement of its commands is authoritative, and the record of them in the effort's map is confirmed against the repo before use"*. `CONTEXT.md`'s own entry — *"Properties rather than commands: the commands are discovered per repo"* — needed no change and got none.
> - **`.claude/skills/expedition/SKILL.md`, what a checker's spawn receives.** *"the bar — its commands where the effort's map records them for this repo, its properties otherwise"* becomes *"the bar — its properties, which are the whole of what the spawn conveys of it: the commands the checker discovers from the repo itself, exactly as the implementation worker does"*. This is stated from the rule rather than matched against a landed wording, node 173 being open and unclaimed.
>
> **Three calls a later reader would otherwise re-derive.**
>
> 1. **The two passages that still route an implementer to the record were left standing, and the sameness was stated positively instead.** `expedition/SKILL.md`'s implementation-spawn bullet still reads *"the bar by way of the map"*, and the implementer's own read-list still says the implementation-rules file holds *"the bar's commands where the effort has recorded them"*. Neither claims authority and neither names a place the checker is shut out of: both describe the route by which the *record* arrives, and the reader then confirms it against the repo. Rather than reword text the condition's clause 9 protects, the checker's own item carries the denial — *"exactly as the implementation worker does"* — so the file says on its face that the two agents end at the same place.
> 2. **The record's location is named by role in the passage that was rewritten**, as *"the effort's implementation-rules file"*, and the filename survives only in the two protected passages that already carried it. Measured on the finished pair: the only filenames anywhere in either file are `graph-conventions.md`, `decisions.md`, `flags.md`, `map-implementation-rules.md` and `map.md` — every one a file of the effort's own record, and none a file in which a repo states its commands to an agent. No `CLAUDE.md`, no `AGENTS.md`, no manifest, no task runner, no absolute path.
> 3. **Every counted list in both finished files was enumerated, not trusted.** Twenty sentences introduce a list by stating its size across the two files; nineteen were already correct and the twentieth is the one this work changed (three → two). The audit is worth recording because nothing indexes counted lists: the correct ones are the five node kinds, five handover parts, two things travelling in a spawn, two things always both, two such things, two things staying out, three gate outcomes, one-of-three places, four constraints, two rules binding every condition, three tier-1 kinds, three non-claimants, two counts, two forms of steering, three invisible states, first-two-and-the-third, three raise triggers, three colliding method-skill instructions, six handover parts, two flag places under two caps, and the four self-containment tests. The heading `## Where two of these pull against each other` was read as naming a pair per collision rather than the list's length, and left alone.
>
> **The bar's own record was confirmed against the repo rather than trusted, which is the rule this work ships.** The repo root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`; a search outside `.git` and `.scratch` finds no `package.json`, `Cargo.toml`, `pyproject.toml`, `Makefile`, `justfile`, `Taskfile`, `*.nix`, `.pre-commit-config.yaml`, `CLAUDE.md` or `AGENTS.md`, and no CI directory. `.gitignore` ignores `.worktrees/` and `.claude/worktrees/` and invokes nothing. **No difference to report**: the record's claim of no build, no tests, no formatter and no CI holds, and because the repo states no commands of its own the record stands as the only statement there is — unconfirmed in exactly the sense the new wording describes. **The rule is inert on this effort and its first real use is the confirmation costing one `find`.**
>
> **The bar's non-command half.** No trailing whitespace, no tabs, no CRLF; the four hunks wrap at 107 and 104 columns against each file's existing prose maximum of 108. Three of the added words land on `CONTEXT.md`'s refused list and each is accounted for: *complete* only inside the preserved *"a complete bar"* sentence, which the condition's clause 3 requires kept and which the rules file's own bar paragraph phrases the same way; *run* as the verb for executing a command, refused only as a name for an effort or an attempt, and already standing in the checker's *"Run the repo's own commands"*; and *where*, which the rules file records as a false positive of that grep list and which `CONTEXT.md` confirms is ordinary English inside another `_Avoid_` line's prose. Held against `/writing-for-agents`, the change moves **toward** that standard rather than away: its own discipline is that a document restating the environment is a copy of a lookup, earning its load only where the lookup is expensive, and *"leave the one-file, one-command lookups to the environment, where they cannot go stale"* is this rule in the standard's own words. That standard's term for the object is *cache*; flag `174.2` refuses the word for this effort, so the shipped text says *a copy … confirmed against the repo before use*.

**What the worker reported its work invalidates**, pasted as it wrote it:

**[Node 10](nodes/10-done-ness.md) — *Done-ness and termination* — has one clause of its `## Answer` contradicted by shipped text as of this work**, and the contradiction was already reported by node 174's worker rather than found here. Node 10 wrote that the commands are *"discovered per repo on first use, and then **written once into the map's Notes**"*. `written once` is now false on both counts — on location since node 140 moved the record to the implementation-rules file, and on standing since *once* has become *once, and confirmed against the repo on each use*. What node 204 adds is that the phrase `written once into the effort's map` no longer appears in any shipped file: it was the manager contract's `the bar` glossary entry, and it is gone. Node 10's other three clauses stand — *discovered per repo on first use* is the ground this work rests on, *so the next node does not re-derive them* is narrowed rather than reversed and holds exactly as written on a repo that states no commands of its own, and *so the human can see and edit what is actually being run* is now the record's main job.

**Nothing else resolved is contradicted.** [Node 143](nodes/143-rules-arrive-by-the-spawn-never-by-a-search.md) is untouched: the *standards* still arrive in one known file that both agents read, and only the bar's *commands* were split out of it, by node 167 and then node 174. [Node 167](nodes/167-the-checkers-bar-commands-route.md) is completed rather than contradicted — its answer already had the checker's spawn stop carrying the commands, and this work carries that shape into the manager's mirror of the same given. [Node 173](nodes/173-stop-the-checkers-spawn-carrying-the-bars-commands.md) is untouched and still owed: it repairs the checker's own contract, whose `## What you are given` still offers *"either its commands for this repo, or the properties alone"*. **One known inconsistency is deliberately left standing and is not mine**: `graph-conventions.md`'s `## Notes` bullet still names `map.md` as the home of the bar's commands, which is [node 153](nodes/153-graph-conventions-notes-bullet-is-false.md)'s and which flag `174.3` reserved to it; clause 11 forbade me the file.

## Annotation: the retrospective

*Filed by the manager, pasted as the worker wrote it. Filed with the node rather than after it, which is what [node 212](212-the-mint-on-second-report-rule-is-defeated.md)'s `Q3.` asks be made the rule.*

**RETROSPECTIVE** — the seventh part, on this effort's standing instruction:

1. **What I had to hunt for.** *Whether any open node already covers the `map`-is-one-file defect* — found by grepping the sixteen open nodes on `expedition/SKILL.md` for the entry's own phrasing; I looked first at `decisions.md`, which showed node 142 repairing `graph-conventions.md` and nothing for the manager's contract. **Nothing indexes which open acceptance conditions touch which passages of a shipped file**, which is the item flag `174.4` reported and whose retrospective called it the third report; this is the fourth. *Whether `where` is refused* — the rules file already carried the correction and `CONTEXT.md` line 217 confirmed it in one grep, so the trigger did its job. *The size of every counted list in both files* — nothing indexes them, so twenty lists were enumerated by hand after grepping number words.
2. **What arrived that this node did not need.** The biggest item is inside a mandatory read: `map-implementation-rules.md` declares its readers to be an implementation worker and its checker, but roughly two-thirds of it — the whole landing section, sandbox mount tables, the rebase-repair pass, the `EnterWorktree` routes and the base check — is addressed to the **manager**, who creates the worktree and lands the work. I read it and acted on none of it. A split by reader, or a heading a worker can stop at, would let the file's declared reader stop reading where its own material ends. Second, `decisions.md` was read whole, 129 lines, for about seven that bore on the bar's commands; the spawn's instruction to read it unscoped and filter myself is the declared arrangement absent a label vocabulary, but a grep for `bar` and `command` would have returned those seven, and choosing the whole read was mine rather than the record's. Third, from the spawn, manager note 4 warned that a sandbox may refuse a write under `.claude/skills/`; one `Edit` was refused once and then succeeded on a plain retry with no sandbox error in sight, so the note primed a diagnosis that was not the cause — though it earned its place by stopping me escalating to an unsandboxed write on the first refusal.
3. **What would have made this node easier.** The condition's arithmetic clause quantifies over both whole files, which turns a four-hunk edit into a twenty-list audit; it is the right demand, but **nothing in the record indexes counted lists**, so every worker meeting a clause of that shape pays the same enumeration. One convention — a counted list is audited when that list is edited — would let the next worker check only what it touched, which is what the rules file's own *"whoever is already editing a passage applies this to that passage"* does for a different rule. Manager note 1 was the note that paid for itself: knowing node 173 was open and unclaimed told me clause 5 was mine to state from the rule rather than to match, and saved reading that node.
4. **What I read that was stale, wrong, or contradictory.** One finding, reported as the node above: the manager contract's `map` entry against `graph-conventions.md`'s four-file listing and `CONTEXT.md`'s filename-free definition. Nothing else read stale — the rules file's `where` correction and its warning that the refused words are unusable as a grep list both held and both saved time. One friction that is not the record's fault: the spawn named the worktree's base as `master` at `7343289` while my session's opening status showed `master` at `8340e18`, and both are true of two different repositories, which cost one check to establish.
