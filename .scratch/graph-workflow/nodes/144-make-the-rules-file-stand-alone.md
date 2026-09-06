# Make the rules file stand alone for a reader that does not read `map.md`

Type: implementation
Status: resolved

Blocked by: 140, 143

## Question

*Surfaced by [Where the rules a checker is held to live](138-where-the-rules-a-checker-is-held-to-live.md)'s worker,
and pasted as it wrote it.*

> The standards list names *"this map's standing preferences, ground rules and four standing rules"*, which resolve
> to nothing for a checker that reads the rules file and not the map. Two of the three can move; the third cannot and
> has been unsafe as a checker standard since node 42 fixed the test for what may reach a blind checker.

## Acceptance condition

*Written by node 138's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/`. The worker may edit `map.md` and the
> sibling file holding the implementer's and checker's rules, and no other file; it may not mark this node, resolve
> it, or write a line in `decisions.md` or `flags.md`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. The block beginning with the line `**Ground rules for this effort.**` and the numbered rules under it, and the
>    block beginning `**Four standing rules for writing anything in this effort**` and the numbered rules under it,
>    are in the rules file and no longer in `map.md`. Their text is byte-identical to what `map.md` held: no rule is
>    reworded, renumbered or reordered.
> 2. For each of the two, `map.md` holds a pointer of at most two lines naming the rules file and saying what it
>    holds. `map.md` restates neither block.
> 3. The sentence in the rules file naming `this map's standing preferences, ground rules and four standing rules` as
>    standards is replaced by a statement that resolves inside the rules file itself: it names the two blocks now
>    held there, and it states that the map's standing preferences as a whole are not among the standards work is
>    held against.
> 4. That statement gives the reason in one sentence: a standing preference may be an account of what happened or a
>    steer about what gets worked, and only a standing constraint true of any node's work may be held against a piece
>    of work by a reader blind to the record.
> 5. No other paragraph of the rules file changes, and no heading named `## Notes` is added to it.
> 6. Every markdown link in `map.md` and in the rules file resolves to a path that exists.
> 7. No file outside `.scratch/graph-workflow/` is modified.

## The manager's note at filing

*Not a change to anything above.*

**Its clause 1 moves the ground-rules block out of `map.md`, which [node
139](139-move-the-managers-material-out-of-the-map.md)'s clause 8 held byte-identical *inside* `map.md`, and which
[node 140](140-move-the-implementers-and-checkers-material-out-of-the-map.md)'s clause 11 holds there too.** Those
are not in conflict: each condition binds its own node's finished tree, and this node runs after both. The manager
records it because a reader meeting the three clauses together will otherwise think one contradicts another.

**Its subject is a defect that predates the split.** In its author's words, the reference to the standing preferences
*"has been wrong as a checker standard since node 42 fixed that test"*, and the move exposes it rather than creating
it. That is [flag `138.4`](138-where-the-rules-a-checker-is-held-to-live.md).

**Why it waits on [node 143](143-rules-arrive-by-the-spawn-never-by-a-search.md) as well as node 140.** Node 143
rewrites what the checker's contract says it is given; this node rewrites what the given itself contains. Doing this
first would edit a standard the contract still describes as discovered.

## Flags

*All four are the worker's own text, pasted. The ids and the links are the manager's bookkeeping and nothing else.
The account of what produced them is the worker's handover, which reached the manager as one document; each entry
below carries that account in the worker's words.*

`144.1` **· settled** `ASSUMPTION` — The paragraph `Every rule above is drawn from a standing preference …` was moved into the rules
file with the ground-rules block, on the reading that clause 1's "the block beginning with the line
`**Ground rules for this effort.**`" runs to the end of that passage rather than stopping at the last
numbered rule. The condition is silent on it. Left in `map.md` it would have read `Every rule above` with
no rules above it; moved, its trailing `the rest of this file` points at `map.md`, which the rules file's
own second paragraph already warns is true of moved text. The dangling reference in the file every worker
reads cold was judged the worse of the two.

`144.2` **· settled** `ASSUMPTION` — The wrong phrase in the standards sentence was struck through rather than deleted, and the
replacement placed beside it. Clause 3 says "replaced"; the map's never-delete standing preference says
superseded text is marked and left where it is, and that preference is part of the bar this node is held
to. Strikethrough is also this file's established idiom.

`144.3` **· settled** `ASSUMPTION` — The rules file's bar paragraph still names `this map's own standing preferences` among the
project criteria, contradicting the new statement two paragraphs below it. It was left untouched because
clause 5 forbids changing any other paragraph of that file, and it is not the sentence clause 3 names. The
contradiction is now visible to any checker reading the file cold.

`144.4` **· settled** `ASSUMPTION` — The first pointer was placed exactly where the ground-rules block stood, so that `map.md`'s
preceding paragraph — "The manager copies the block below as text into every checker spawn" — resolves
through the pointer instead of dangling. That paragraph was not edited, on the same minimality ground.

`144.5` **· settled** `LICENCE` — **The manager's, recording a licence the human granted in answer to the manager's own raise.**
This node's two changed paths, `map.md` and `map-implementation-rules.md`, both sit in the effort's own directory,
which the shipped checker contract tells a checker to leave unread — *"Read that file for its standards and read
nothing else in the effort's directory … open no other file beside it"* — while its given 3 hands it *"the paths that
changed."* The manager raised the collision rather than improvising past it for a third time, having already
improvised it at [node 147](147-graph-records-name-absolute-paths-on-a-machine.md) and [node
140](140-move-the-implementers-and-checkers-material-out-of-the-map.md) and flagged itself at `147.3` and `140.9`
both times. The human granted a licence for this one check. **It binds this attempt only and changes nothing on
disk**; the permanent fix is [node 163](163-a-condition-demands-facts-the-checker-does-not-read.md), which is claimed
and holds a banked question on exactly this.

***The manager's note on this flag's marker.*** `graph-conventions.md` defines three markers — `ASSUMPTION`,
`CONDITION-WRONG` and `DELEGATED` — and **none of them is a licence**, which the manager's contract nonetheless
requires be recorded as a flag. `LICENCE` is written here because writing one of the three would be false. That hole
is [node 170](170-a-licence-has-no-flag-marker.md) rather than something settled in the moment.

## Interview

### The manager's raise, and the human's answer

*Not a worker's interview. The manager raised a clause of the shipped checker contract as blocking this node's
check, under the rule that it may not depart from a worker contract on its own authority.*

**What the manager put to the human:** whether to grant a licence, for this one check only, to instruct the checker
that it reads the two changed paths as *the work under check* and takes no statement of intent from them — the
alternative being that the node goes to the gate with no check at all, and the human's diff read is the check.

**The human's reply, `verbatim`.**

> for 144, give the licence

*Takes the manager's `RECOMMENDED` route. Not a divergence.*

## Review

### Checker run 1 — `PASS`

*Pasted as the checker wrote it. It was spawned under the human's licence, flag `144.5`, and says so in its outcome.*

> Checked under the human's one-time licence: I read `.scratch/graph-workflow/map.md` and `.scratch/graph-workflow/map-implementation-rules.md` as the bytes under check only, taking no statement of intent from either. I read no node file, no `decisions.md`, no `flags.md`.
>
> ### Settled first: the work moved standards under the check
>
> Per `### Where the work moved one of them`, before checking anything else I split the moved standards into operative content and rationale and compared the sets element by element, unwrapped.
>
> - **The two relocated blocks** (clause 1) are **byte-identical**. I extracted the range from `git show HEAD:.scratch/graph-workflow/map.md` between `**Ground rules for this effort.**` and `## Decisions so far`, and the tail of the new rules file, and diffed: the sole difference is the blank separator line that preceded `## Decisions so far`. 2013 vs 2012 bytes. The sets are identical, so it does not matter which side I read them from, and the check survives.
> - **The standards list** (clause 3) lost one entry: `this map's standing preferences`. Read narrowly — "a standard the bar carries" being one of the standards named, not the list itself — **no standard's operative content moved**: each named standard is either untouched or relocated byte-identically. Read broadly, an element of the list was removed. I proceeded rather than raised, on three grounds: the contract's own stated reason for raising ("nothing unmoved left to hold the rest of the work against") plainly does not obtain, since seven of eight elements are unmoved and two of them reached me as text in the spawn; the removed element is one the human's licence had **already** put out of my reach for this check, so its removal changes nothing about what I could hold this work against; and a raise is reserved for where no reading of the work could produce an outcome, which is not this case. **This is a judgement at the edge of the contract's binary, and it is question 1 below.**
>
> ### The condition, clause by clause
>
> 1. **Met.** Both blocks are in the rules file (lines 108–123), byte-identical as above; no rule reworded, renumbered or reordered. `grep -cF` over the ten rule texts and the block's trailing paragraph returns **0** in `map.md`.
> 2. **Met.** `map.md:62` and `map.md:64`, one source line each (312 and 304 bytes), each naming `map-implementation-rules.md` by name and by resolving link and saying what it holds. No restatement, per the greps above.
> 3. **Met.** The sentence is superseded by strikethrough with the bolded replacement beside it — the file's own established convention, used twice in the very same section (`~~ignores `.worktrees/`~~ **ignores …**`) and in `map.md` (`~~six~~ seven`). The replacement resolves in-file (`both of which this file holds below`; the blocks are indeed below at 108+), and the exclusion is stated: `**map.md's standing preferences are not among the standards, as a whole.**`
> 4. **Met.** The reason is one sentence and matches the condition's wording. The sentence after it is node citation, which standing rule 2 requires.
> 5. **Met.** A paragraph-level compare with whitespace normalised (16 paragraphs before, 21 after) shows **exactly one** pre-existing paragraph changed — the review route — and five added. Heading list is byte-identical before and after; `grep -c '^## Notes'` on the rules file returns **0**. No whitespace anomalies introduced; both files end with a newline.
> 6. **Met.** All markdown links extracted from unwrapped text and existence-tested: `map.md` 61 links / 36 distinct targets, `map-implementation-rules.md` 24 links / 17 distinct targets, **0 missing**, 1 external URL.
> 7. **Met.** `git status --porcelain -uall` lists only the two permitted paths. `decisions.md`, `flags.md` and `nodes/144-…md` are untouched, so the node was not marked or resolved.
>
> ### The bar
>
> Discovered rather than assumed, per ground rule 1: no `package.json`, `Cargo.toml`, `pyproject.toml`, `Makefile`, `justfile`, `Taskfile.yml`, `go.mod` or `.pre-commit-config.yaml`; no `.github/workflows`. The repository root holds only `CONTEXT.md`, `.gitignore`, `.claude/` and `.scratch/`. `.gitignore` ignores `.worktrees/` and `.claude/worktrees/` and invokes nothing — matching the claim the rules file records. **Nothing to invoke; the command half is empty and the bar is complete on its remaining half.**
>
> Standards read, from `map-implementation-rules.md` under `## What the work is held against`, and which bore:
>
> - `/coding-principles`, `/naming` — **no bite**. The diff is entirely markdown prose and introduces no code and no identifier.
> - `CONTEXT.md`'s `_Avoid_` lines — **checked by hand**, per the file's own recorded trap about greppability. I isolated the genuinely new prose (3020 bytes) by subtracting the verbatim-moved blocks from the diff's added lines, then scanned it against ~60 distinctive refusals. Two hit classes, **neither a finding**: `refused` (three, all pre-existing text inside the rewritten paragraph, and in the sense of "CONTEXT.md refuses this word", not the node-outcome sense the `_Avoid_` line covers) and `deliverable` (one pre-existing, one new at `map.md:64` — but ground rule 5 as handed to me in the spawn and standing rule text both use "prose deliverable", so refusing the work a word its own standards use would be checking against my preference).
> - The effort's **ground rules** and **four standing rules** — hold. The change is a textbook progressive-disclosure move: material out of the file every worker reads cold, behind two front-loaded pointers, co-located under the heading that names it, with node citations and no restatement.
> - `graph-conventions.md` — read `## The seven files`, `## Writing the map`, `### Change the map`, `## Mechanical checks`. The rules file is "part of the map", so the never-delete rule is satisfied by a verbatim in-map relocation rather than exempted; `Change the map`'s trigger ("no longer says what holds") is not met, since the blocks still say exactly what holds. Both pointers are well under the 500-byte `## Notes` target, which reports and never fails.
> - `/writing-for-agents` — invoked by name from `mattpocock-skills` and applied by hand; it spawns nothing, so no blind-delegation question arose. The one negation (`are not among the standards`) is paired with the positive enumeration immediately preceding it, which is what the standard asks. No reviewing skill was run: the standards state none is named for this repo.

```
NOT COVERED:
- ESTABLISHED BY the human, at the gate · read the part as the gate presented it — as owed,
  unestablished, and named as the one thing neither the checker nor the manager could reach —
  and approved the node with it in front of them. Their word, `verbatim`: "approve".
  — "this map's own standing preferences", named by the bar paragraph of
  map-implementation-rules.md as part of the bar's non-command half. The human's licence
  gives me map.md as bytes under check and no statement of intent from it, and standing
  preferences are statements of intent, so I could not apply this element of the bar. It
  is also the element question 2 is about.
```

***The manager's note on the owed part.*** It is `OWED` and the manager has **not** established it. What would
establish it is a reading of `map.md`'s standing preferences against this work — which is the one thing the licence
put out of the checker's reach and which the manager cannot do without becoming the author of the standard. It
therefore reaches the human at the gate as an owed part rather than an established one, and this is the case
`graph-conventions.md` names when it says a part may be established by the human at the gate reading it themselves.

**The questions it raised alongside its outcome, pasted as it wrote them.** They issue no verdict and did not stop it
passing; they travel to the human in the gate payload.

> - The checker contract's rule for a moved standard is a bright line: "An element was added, removed or altered ... Raise it." This work removes one element from the standards list (map.md's standing preferences) while leaving every other standard unmoved or relocated byte-identically, so the rule fires but its own stated reason ("nothing unmoved left to hold the rest of the work against") does not. I proceeded and reported rather than raised. Does the contract want a middle branch for a list that loses an entry, as against a standard whose content changed?
> - The condition is met, and complying is what produced two defects the worker could not repair. (a) map-implementation-rules.md now states, two paragraphs apart, that map.md's standing preferences ARE part of the bar's non-command half (the unchanged bar paragraph) and are NOT among the standards, while also saying "The standards above are the whole of what work is held against". Clause 5 forbade touching the bar paragraph. (b) The moved sentence "That test is what keeps the rest of this file out of the block" meant the map's other notes when it sat in map.md; in map-implementation-rules.md "the rest of this file" now reads as the landing policy, the bar's commands and the review route. Clause 1's byte-identical requirement forbade rewording it. Both wordings are the condition's own and so were not the worker's to depart from. (b) also sits against the stated purpose the pointer gives — "so that file stands alone for a reader who does not read this map" — since the moved paragraph still refers outward to standing preferences held in map.md.
> - Minor, and it did not bear on my outcome: `Change the map` step 1 sends an item's superseded text to map-history.md verbatim, and the condition forbade editing that file. I judged the procedure's trigger unmet, so no finding — but whoever holds the record may want the relocation noted there anyway.

### Gate — `approve`

**The human's word, `verbatim`.**

> approve

**Landed as `37a3d28`**, rebased onto `9a252c9` and fast-forwarded onto `master`; the worktree was removed and its
branch deleted. **The landing did not go as the policy describes it**, and the account is on [node
176](176-the-managers-record-edits-collide-with-a-landing.md): the manager's own uncommitted record edits sat on both
of this node's two paths, so `git merge --ff-only` was refused, and the sandbox had gone read-only over the whole
effort directory, which is [node 175](175-what-the-worktree-cycle-does-to-the-sandbox.md). The edits were committed
first, at the human's approval, as `9a252c9`. **A read-only trial merge established before anything ran that the two
changes could not conflict** — `git merge-tree --write-tree` returning `Auto-merging` on both files — and the rebase
then went through without a conflict.

*No correction round was taken; checker run 1's `PASS` stands as the only run. The five flags this node holds are
settled by the approval, under the human's standing instruction that approving a node's end settles its flags. The
checker's three questions were in the payload and the human answered none of them; that is their choice rather than an
omission, and the manager records the questions rather than reading approval as an answer to them. **Question 1 — the
bright line for a moved standard that is a list losing an entry — is minted as its own node.**

## Answer

*Pasted as the worker wrote it.*

> The two blocks a checker was previously sent to `map.md` for now live in
> `map-implementation-rules.md`, and the standards sentence that pointed at the map resolves inside the
> rules file.
>
> **What moved, byte-identical.** The `**Ground rules for this effort.**` block with its five numbered
> rules, and the `**Four standing rules for writing anything in this effort**` block with its four, are
> appended to `map-implementation-rules.md` at the end of `## What the work is held against`, in map order.
> Nothing was reworded, renumbered or reordered; verified by string-matching the moved text against
> `HEAD:.scratch/graph-workflow/map.md`. They sit under that heading rather than a new one because they are
> literally what the work is held against, and because clause 5 forbids a `## Notes` heading here.
>
> **The closing paragraph of the ground-rules block moved with the block.** `Every rule above is drawn from
> a standing preference …` states the block's membership test and ends `the block is appended to like any
> other part of this map`. Clause 1 names *the block beginning with* that line, and this paragraph is inside
> it on that reading. Left behind, it would have dangled in `map.md` — `Every rule above` with no rules above
> it, in the one file every worker reads cold. Moved, its `the rest of this file` now means `map.md`, which is
> the exact hazard the rules file's second paragraph already declares (*"a paragraph that says above or below
> may be pointing at something in `map.md`"*). Flagged.
>
> **What `map.md` holds instead.** One single-line pointer per block, in the blocks' original positions, each
> naming `map-implementation-rules.md` and saying what it holds. Neither restates a rule. The first pointer
> sits exactly where the ground-rules block was so that the paragraph above it — *"The manager copies the
> block below as text into every checker spawn"* — still resolves in one hop.
>
> **The standards sentence.** In the review-route paragraph, `this map's standing preferences, ground rules
> and four standing rules` is struck and replaced by `this effort's ground rules and its four standing rules
> for writing, both of which this file holds below`, followed by a statement that the map's standing
> preferences are not among the standards as a whole, with the reason in one sentence: a standing preference
> may be an account of what happened or a steer about what gets worked, and only a standing constraint true
> of any node's work may be held against a piece of work by a reader blind to the record. The old wording is
> struck rather than deleted, honouring the never-delete standing preference, which is itself part of the bar
> this node is held to. No other paragraph of the rules file changed — its first 105 lines are byte-identical
> to `HEAD`.
>
> **Links.** Every markdown link in both files resolves: 61 in `map.md`, 24 in the rules file, checked
> against the filesystem. Both files sit in the same directory, so the `nodes/…` and `../../` links inside
> the moved text resolve unchanged.
>
> **The consequence this move has outside the two files, and it is the finding worth carrying.** This
> effort's ground rules are no longer in `map.md`'s `## Notes`. Five shipped worker contracts —
> `expedition-research`, `expedition-grilling`, `expedition-prototype`, `expedition-precondition`,
> `expedition-implementation` — and `graph-conventions.md` all tell a worker that *the map's `## Notes` may
> declare the effort's ground rules*, and only implementation workers and checkers are given the rules file.
> So a research or grilling worker on this effort now meets a pointer where it was told to find the block.
> The checker is unaffected: it receives the block as text from the manager, per node 42, and that route
> still works. Reported as a new node.
>
> **One contradiction left standing inside the rules file, because clause 5 forbids repairing it.** The
> bar paragraph in the same section still lists `this map's own standing preferences` among the project
> criteria, two paragraphs above the new statement that they are not among the standards. Different sentence,
> different string, not the one clause 3 names. Reported as a new node.

**What the worker reported its work invalidates, pasted as it wrote it.**

> [Subagent context contract](12-subagent-context-contract.md), whose answer fixes that the map's
> `## Notes` carries the effort's ground rules block, and which `map.md` still records in the paragraph
> above the new pointer. After this node the block is not in that section; the section holds a pointer to
> `map-implementation-rules.md`. The declaration itself survives — this effort still declares a ground-rules
> block and no source hierarchy — but its location does not, and the shipped contracts that repeat node 12's
> sentence are listed in the first new node above. Nodes 139 and 140, whose conditions held this block
> byte-identical inside `map.md`, are not contradicted: each binds its own finished tree, as the manager's
> note at filing records.

## Retrospective

*Pasted as the worker wrote it. Filed by the manager as an annotation.*

**(1) What I had to hunt for.** Three things. The exact byte boundaries of the two blocks — found by reading `map.md` with a byte dump, after the line-numbered read, because "byte-identical" cannot be trusted to a rendered view; that was necessary work, not a shortfall. Whether `this map's standing preferences` appears anywhere in the rules file besides the sentence clause 3 names — found by reading the file, and it does, in the bar paragraph, which clause 5 then forbade me to touch. That one I looked for late, on a hunch, after I had already made the edit; nothing pointed me at it. And who else depends on the ground rules being in `map.md`'s `## Notes` — found by one grep across `.claude/skills`, and it turned up six files. That grep is the highest-value thing I did on this node and nothing asked for it.

**(2) What arrived that this node did not need.** From the spawn: the paragraph on how the retrospective is filed and by whom is fully restated in my spawn and again in `map.md`'s standing preference on retrospectives, which I read cold; I needed the four questions, not the account of who files them. The manager's second note — that clauses 3 and 4 are the ones needing judgement — was accurate but did not change what I did, since I had to satisfy all seven anyway; the first note, about 139 and 140, did do work and stopped me re-deriving a contradiction. From the mandatory reads: `map.md`'s `## Notes` is about 5,000 words of which I acted on four items — never-delete, the four standing rules, the ground rules, and the retrospective questions — while the standing preferences on concurrency, model heterogeneity, resume, token priority, worktree creation and one-question-at-a-time bore on nothing here; that is the same observation the node I just worked on is about, since those preferences are precisely the material that cannot be held against a piece of work. `map-implementation-rules.md`'s `## Landing an implementation node's work` is now roughly half that file — sandbox measurements, rebase repair, base verification — and none of it reaches a worker who never rebases or merges; it is the manager's material sitting in the worker's file, and it survived node 140's move because node 140 moved by source rather than by reader. A section heading separating what the *manager* does with an implementation node's work from what the *worker and checker* are held against would let a worker stop reading at the second heading. From `SKILL.md`: the whole `## If you are a replacement attempt` and most of `## Flag, or raise`'s raise machinery bore on nothing, but I would not remove them — a contract read once per node cannot be conditional on which branch you turn out to need. Where I went for one fact and took a file: I read the implementation contract whole for the standards rule and the handover shape, which is the intended use, so nothing to report there.

**(3) What would have made this node easier.** In the record: nothing states, in either file, which paragraphs of `map-implementation-rules.md` a checker holds work against and which are the manager's lifecycle instructions. My node's condition protects "no other paragraph" of a file whose paragraphs serve two different readers, and I had to work out the distinction myself to know that the bar paragraph mattered and the rebase paragraph did not. In the node file: the condition names one sentence by quoting a phrase, which is exactly right, but nothing told me whether the phrase occurs elsewhere in the file — and it does, in a near-identical form. A condition that quotes a phrase would be safer if it said how many times that phrase occurs, or said plainly that other occurrences are out of scope. In the spawn: nothing missing that I noticed; the paths, the tree, the base commit and the uncommitted-changes instruction were all there.

**(4) What was stale, wrong, or contradictory.** Two things, both now reported. The rules file's bar paragraph naming `this map's own standing preferences` contradicts the statement my own clauses 3 and 4 required me to write, and I could not repair it. And five shipped worker contracts plus `graph-conventions.md` say the effort's ground rules may be declared in the map's `## Notes`, which this node makes false for this effort's map. One near-miss worth recording: the rules file's second paragraph says *"Nothing below was reworded on the way here"*, which was true of node 140's move and is now slightly less true — the moved blocks are still verbatim, but the statement I added to the review-route paragraph was written here, not moved. Clause 5 forbade me to adjust that paragraph, and it is a small enough drift that I did not mint a node for it.
