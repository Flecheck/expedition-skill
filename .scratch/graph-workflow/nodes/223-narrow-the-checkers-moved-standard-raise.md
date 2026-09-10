# Narrow the checker's moved-standard raise to where nothing unmoved survives

Type: implementation
Status: resolved

Blocked by: none

## Question

*Surfaced by [Whether adding a standard is a case of `### Where the work moved one of
them`](178-whether-adding-a-standard-is-a-moved-standard.md)'s worker, and pasted as it wrote it.*

> Carry node 178's answer into the shipped checker contract, replacing the branch that raises on any added, removed or altered element with one that raises only where an element that moved is one this work must be held against and no unmoved statement of it survives.

**The file it edits, in the worker's words:** `.claude/skills/expedition-checker/SKILL.md` — and no other. Disjoint from node 222 (`graph-conventions.md`), node 215 and node 213.

**Blockers, in the worker's words:** none. **Must not run in parallel with node 214**, which edits the same clause.

**Ground for the three-site requirement in the condition below**, since it looks like belt-and-braces and is not: *"one rule stated at several sites, so a repair to one leaves the file self-contradicting"* is a standing item with **eight prior reports** (nodes 46, 102, 116, 117, 126, 144, 163, 175), and the node it is biting right now is 222.

**Acceptance condition:**

> **Scope.** The only file this work may create, edit or delete is `.claude/skills/expedition-checker/SKILL.md`. Editing any other file is a `FAIL` on this condition.
>
> **What that file states now.** It tells a checker how to proceed when the work under check has edited a document holding a standard the work is measured against, and it states one rule at three sites:
>
> 1. a bullet under the heading `### Where the work moved one of them`, reading: *"**An element was added, removed or altered.** The operative standard has itself moved, you have nothing unmoved left to hold the rest of the work against, and no reading of the work can produce an outcome. Raise it."*
> 2. a row of the table under the heading `### When what you check against is itself the problem`, reading: *"the work moved the operative content of a standard the bar carries | a raise, and no outcome"*
> 3. a paragraph under the heading `### raise — nothing left to check against`, beginning *"**A standard the work moved.**"* and reading: *"Where the work changed the operative content of a standard the bar carries, you have nothing unmoved to hold the rest of the work against, as above."*
>
> **Done means** all three sites state the narrower rule below instead, and the finished file states the old rule at no site.
>
> The narrower rule, which the file must carry in substance — the wording is the worker's, and these are not sentences to paste:
>
> **(a)** A standard is not the file that holds it. An edit to a file containing a standard reaches that standard only where it changes what the standard itself requires or refuses; an edit elsewhere in the same file does not reach it. The comparison the section prescribes runs over what the standard requires or refuses, never over the file's text.
>
> **(b)** An element the work itself added is part of the work, and not a standard the work is held against. Adding an element leaves every pre-existing element of that standard unmoved, so a check remains possible and a purely additive edit is never on its own a reason to raise. The added element is held against the acceptance condition as work, like any other changed text, and the checker does not hold the work against an element that same work introduced.
>
> **(c)** A removed or altered element is handled one element at a time. The elements that did not move still bind and the work is held against them. The checker raises only where an element that moved is one this work must be held against and no unmoved statement of it survives. Where that reaches only part of what the checker must establish and the rest stands, the file's existing `NOT COVERED:` route applies instead of a raise.
>
> **(d)** The ground is stated together with the rule at the section named in item 1, so that a checker decides between raising and proceeding by asking whether anything unmoved is left to hold the work against, rather than by asking whether the file changed.
>
> **Three further properties of the finished file.**
>
> - The three sites agree with one another: no site states or implies that a purely additive edit requires a raise, and no site contradicts another about when a raise is required.
> - The old text is **replaced**, not struck through, and no superseded-text history file is appended to. This file is one the workflow ships, and the effort's never-delete rule governs the effort's own record rather than shipped files.
> - The section named in item 1 keeps prescribing an element-by-element comparison over a standard's operative content, keeps the operative-content-versus-rationale distinction, keeps the identical-sets case, and keeps the instruction to unwrap both sides first. This work narrows when a raise is required; it removes none of those.
>
> **Also out of scope, and editing either is a `FAIL`:** `.claude/skills/expedition-implementation/SKILL.md`, and every file in the effort's record directory. A rule making a condition that cannot be honoured alongside a standard into a raise is a different repair to the same section and is not this work's.
>
> The bar applies as it reaches you.

**On node 214: separate edits to the same clause, sequenced, and this one first.** Four reasons. This answer is settled and node 214's is not — its own file says the trigger must be stated *"precisely enough that it does not fire on every hard clause"* and it carries no acceptance condition, which the human or whoever they send still owes. Node 214 also reaches `.claude/skills/expedition-implementation/SKILL.md`, and I verified the moved-standard branch appears in no file but the checker contract, so this repair cannot touch that file. They must not be parallelised, both editing `.claude/skills/expedition-checker/SKILL.md`, and two worktrees over one shipped file is what the rules file tells the manager to avoid. And the order is not arbitrary: node 214 adds a raise ground to a list whose neighbouring ground this repair narrows, so a worker on 214 that reads the narrowed text writes a consistent list, where one that goes first writes against text about to change — which is the moved-standard situation itself. **One test governs both** — is anything unmoved left to hold the work against — and node 31's answer already says that test governs the contract's other raise grounds too, so the two repairs compose rather than conflict.

**One node I considered and did not mint.** An implementer-side statement of parts (a) and (b) in `.claude/skills/expedition-implementation/SKILL.md`. I dropped it: that contract carries no moved-standard text, and node 171's worker — the one implementer that met this — was reasoning about its *checker's* contract and said so (*"I hold no authority over the checker's contract and did not touch it"*). An implementer produces work rather than an outcome about work, and its acceptance condition already tells it what to write, so there is no circularity to resolve on that side.

**Its author's ground for one clause of the condition, pasted, because the clause looks redundant and is not:**

**Ground for the three-site requirement in the condition below**, since it looks like belt-and-braces and is not: *"one rule stated at several sites, so a repair to one leaves the file self-contradicting"* is a standing item with **eight prior reports** (nodes 46, 102, 116, 117, 126, 144, 163, 175), and the node it is biting right now is 222.

## Acceptance condition

*Written by node 178's worker. Pasted as it wrote it, and not the manager's.*

> **Scope.** The only file this work may create, edit or delete is `.claude/skills/expedition-checker/SKILL.md`. Editing any other file is a `FAIL` on this condition.
>
> **What that file states now.** It tells a checker how to proceed when the work under check has edited a document holding a standard the work is measured against, and it states one rule at three sites:
>
> 1. a bullet under the heading `### Where the work moved one of them`, reading: *"**An element was added, removed or altered.** The operative standard has itself moved, you have nothing unmoved left to hold the rest of the work against, and no reading of the work can produce an outcome. Raise it."*
> 2. a row of the table under the heading `### When what you check against is itself the problem`, reading: *"the work moved the operative content of a standard the bar carries | a raise, and no outcome"*
> 3. a paragraph under the heading `### raise — nothing left to check against`, beginning *"**A standard the work moved.**"* and reading: *"Where the work changed the operative content of a standard the bar carries, you have nothing unmoved to hold the rest of the work against, as above."*
>
> **Done means** all three sites state the narrower rule below instead, and the finished file states the old rule at no site.
>
> The narrower rule, which the file must carry in substance — the wording is the worker's, and these are not sentences to paste:
>
> **(a)** A standard is not the file that holds it. An edit to a file containing a standard reaches that standard only where it changes what the standard itself requires or refuses; an edit elsewhere in the same file does not reach it. The comparison the section prescribes runs over what the standard requires or refuses, never over the file's text.
>
> **(b)** An element the work itself added is part of the work, and not a standard the work is held against. Adding an element leaves every pre-existing element of that standard unmoved, so a check remains possible and a purely additive edit is never on its own a reason to raise. The added element is held against the acceptance condition as work, like any other changed text, and the checker does not hold the work against an element that same work introduced.
>
> **(c)** A removed or altered element is handled one element at a time. The elements that did not move still bind and the work is held against them. The checker raises only where an element that moved is one this work must be held against and no unmoved statement of it survives. Where that reaches only part of what the checker must establish and the rest stands, the file's existing `NOT COVERED:` route applies instead of a raise.
>
> **(d)** The ground is stated together with the rule at the section named in item 1, so that a checker decides between raising and proceeding by asking whether anything unmoved is left to hold the work against, rather than by asking whether the file changed.
>
> **Three further properties of the finished file.**
>
> - The three sites agree with one another: no site states or implies that a purely additive edit requires a raise, and no site contradicts another about when a raise is required.
> - The old text is **replaced**, not struck through, and no superseded-text history file is appended to. This file is one the workflow ships, and the effort's never-delete rule governs the effort's own record rather than shipped files.
> - The section named in item 1 keeps prescribing an element-by-element comparison over a standard's operative content, keeps the operative-content-versus-rationale distinction, keeps the identical-sets case, and keeps the instruction to unwrap both sides first. This work narrows when a raise is required; it removes none of those.
>
> **Also out of scope, and editing either is a `FAIL`:** `.claude/skills/expedition-implementation/SKILL.md`, and every file in the effort's record directory. A rule making a condition that cannot be honoured alongside a standard into a raise is a different repair to the same section and is not this work's.
>
> The bar applies as it reaches you.

## Its author on sequencing against node 214

*Pasted as it wrote it. The manager schedules and has added no edge, this node's `Blocked by:` being `none`; what
follows is the worker's reasoning and it binds the manager's scheduling rather than the graph.*

**On node 214: separate edits to the same clause, sequenced, and this one first.** Four reasons. This answer is settled and node 214's is not — its own file says the trigger must be stated *"precisely enough that it does not fire on every hard clause"* and it carries no acceptance condition, which the human or whoever they send still owes. Node 214 also reaches `.claude/skills/expedition-implementation/SKILL.md`, and I verified the moved-standard branch appears in no file but the checker contract, so this repair cannot touch that file. They must not be parallelised, both editing `.claude/skills/expedition-checker/SKILL.md`, and two worktrees over one shipped file is what the rules file tells the manager to avoid. And the order is not arbitrary: node 214 adds a raise ground to a list whose neighbouring ground this repair narrows, so a worker on 214 that reads the narrowed text writes a consistent list, where one that goes first writes against text about to change — which is the moved-standard situation itself. **One test governs both** — is anything unmoved left to hold the work against — and node 31's answer already says that test governs the contract's other raise grounds too, so the two repairs compose rather than conflict.

**One node I considered and did not mint.** An implementer-side statement of parts (a) and (b) in `.claude/skills/expedition-implementation/SKILL.md`. I dropped it: that contract carries no moved-standard text, and node 171's worker — the one implementer that met this — was reasoning about its *checker's* contract and said so (*"I hold no authority over the checker's contract and did not touch it"*). An implementer produces work rather than an outcome about work, and its acceptance condition already tells it what to write, so there is no circularity to resolve on that side.

## The manager's note at filing

*Not a change to anything above.*

**This node ends a licence when it lands.** Until it does, a checker meeting the branch carries on and discloses,
which the human granted at node 178 as standing steering and which `map.md` now carries in their words. **The
narrowed branch is what the licence stood in for**, so whoever lands this should expect the map's licence item to be
retired in the same breath — by the manager, in the record, not by this node's worker.

**Two workers may not hold `.claude/skills/expedition-checker/SKILL.md` at once.** This node and [node
214](214-a-condition-that-contradicts-a-standard-is-a-raise.md) both edit it, and node 214 still has no acceptance
condition. Its author's reasoning above puts this node first; **the manager holds that sequencing and has written no
blocking edge**, since neither node needs what the other produces.

## Flags

*The worker's own text, pasted. The id is the manager's bookkeeping and nothing else. **Settled by the approval**,
the flag having been the substance of what the gate put in front of the human.*

`223.1` **· settled** `ASSUMPTION` — **Two edits outside the three enumerated sites, in the `NOT COVERED:` route the narrower rule
sends work to.** Part (c) of my acceptance condition routes a partially-reaching moved standard to *"the file's
existing `NOT COVERED:` route"*. That route's own section states its cause as the checker's blindness alone —
*"something observable that is not observable **by you**"*, *"anything outside the paths you were given"* — and its
output template asked the checker to say *"why establishing it is outside what you were given"*. The moved-standard
case is neither: the part is observable and what has gone is the thing to hold it against. Left alone, site 1 would
have pointed a checker at a section whose stated cause excluded its case, which is the same one-rule-at-several-sites
defect this node exists to avoid. I decided rather than raised: the file is wholly inside my scope clause, the change
removes no demand the section already made, and I hold a recommendation I believe. I added one paragraph naming the
second cause and pointing back at `### Where the work moved one of them`, and widened the template's placeholder to
cover both causes. The alternative I set aside was leaving the route untouched and letting each checker reconcile it,
which is what produced the arrivals node 178 counted.

## Review

### Checker run 1 — `PASS`

*Pasted as the checker wrote it, in its own order. Every sentence is the checker's. It handed back **no question and
no `NOT COVERED`**.*

> ```
> PASS
> ```
>
> **Scope — only `.claude/skills/expedition-checker/SKILL.md` created, edited or deleted.** `git status --porcelain=v1` in the tree I was given returns exactly one line, ` M .claude/skills/expedition-checker/SKILL.md`; nothing staged, nothing untracked, no deletions. `git diff --stat` confirms one file, 49 insertions, 15 deletions. The two named out-of-scope targets are clean in that tree: `.claude/skills/expedition-implementation/SKILL.md` is untouched, and the effort's record directory is tracked and present in the worktree (`git ls-files .scratch` returns its files) and appears in no diff. Bounded to the tree I was given — anything done outside it is outside the paths I hold.
>
> **All three sites state the narrower rule, and the old rule stands at no site.** I split the file into paragraphs, unwrapped each into unbroken text, and searched that for `operative`, `moved` and `unmoved`. Site 1 (`### Where the work moved one of them`) now runs four paragraphs and four bullets; site 2 is the table row under `### When what you check against is itself the problem` plus a following note; site 3 is the `**A standard the work moved, where nothing unmoved survives.**` paragraph under `### raise — nothing left to check against`. The three old texts resolve to nothing in the file: no bullet reading *"An element was added, removed or altered"*, no row reading *"the work moved the operative content of a standard the bar carries"*, no paragraph opening *"**A standard the work moved.**"* plain.
>
> **(a) A standard is not the file that holds it.** Site 1's first paragraph states it in those words and adds *"an edit reaches a standard only where it changes what that standard itself requires or refuses, and an edit elsewhere in the same file leaves the standard untouched however large that edit is."* The prescribed comparison still runs over operative content — *"settle it on the operative content alone: take the set of things the standard requires or refuses … compare the sets rather than the prose around them"* — and the file's text is expressly excluded as the test: *"and* did the file change *never does."*
>
> **(b) An added element is work, not a standard.** Site 1's second bullet carries all four clauses: the element is part of the work; every pre-existing element is unmoved so a check remains possible; *"Hold the added element against the acceptance condition, as work, like any other changed text"*; and *"hold the work against no element that same work introduced."* It closes *"A purely additive edit is never on its own a reason to raise."*
>
> **(c) One element at a time, unmoved elements still bind, raise only where nothing unmoved survives, partial reaches `NOT COVERED:`.** Site 1 adds *"Then take the elements one at a time: every element that did not move still binds, and the work is held against it,"* then a removed-or-altered bullet that asks of that element alone whether this work must be held against it and whether an unmoved statement survives elsewhere, then a fourth bullet routing the whole-of-what-you-must-establish case to a raise and the partial case to `NOT COVERED:`. That route is wired at the receiving end too: the `### A part you could not establish` section gained a paragraph admitting this second, non-blindness cause, and the `NOT COVERED:` template's *why* clause was widened to *"outside what you were given, or nothing unmoved left to hold it against."*
>
> **(d) The ground is stated with the rule at the section in item 1.** Site 1's second paragraph: *"whether it did is the one question this section turns on:* **is anything unmoved left to hold this work against?** *That question decides between raising and carrying on, and* did the file change *never does."*
>
> **The three sites agree, and none states or implies that a purely additive edit requires a raise.** Site 1 forecloses it categorically; site 2's note says *"An element the work itself added is in none of these rows"*; site 3 names *"an element this work added"* among the edits that are not that ground. All three split the same way — raise where the loss is the whole of what must be established, `NOT COVERED:` where it reaches only part — so no site contradicts another. One thing I weighed and did not treat as a defect: site 1's fourth bullet heads with *"An element this work must be held against moved"* where site 3 says *"removed or altered"*. Read alone that bullet's *moved* could be stretched to cover an addition, but it is the negative tail of the bullet immediately above it and sits two bullets below a categorical statement that additive is never on its own a reason to raise, so the property holds as written.
>
> **Replaced, not struck through, and no history file appended to.** `~~` resolves to nothing in the file, as do `<del>`, `<s>` and `<strike>`. The diff shows the old text removed rather than marked. No second file changed, so `map-history.md` was not appended to. This agrees with the standard rather than departing from it: `graph-conventions.md` states that the never-delete rule *"reaches the graph's own files … and nothing outside them. The product the effort changes, and every file the effort ships, are edited plainly."*
>
> **The section keeps its four retained properties.** Element-by-element comparison over operative content: kept, and extended by the one-at-a-time paragraph. The operative-content-versus-rationale split: kept verbatim in substance, with *"destroys it"* softened to *"can take away what you would have held the work against"*. The identical-sets bullet: unchanged, character for character. *"Unwrap both sides first"*: unchanged. Nothing about the section's machinery was removed.
>
> **Nothing out of scope was added.** The added text says nothing about a condition that cannot be honoured alongside a standard; that repair is absent, as the condition requires.
>
> **The condition records no enumerator**, so there was no command of that kind to run.
>
> **The bar.** Its commands I discovered from the repo rather than taking the recorded copy: no `package.json`, `Makefile`, `justfile`, `Cargo.toml`, `pyproject.toml` or `.github` anywhere in the tree; the one ignore file, `.gitignore`, ignores `.worktrees/` and `.claude/worktrees/` and invokes nothing. So there is no build, no test, no formatter and no CI to run, and the bar here is entirely its non-command half — a complete bar, not a deficient one. The implementation-rules file's recorded copy says the same; no difference to report.
>
> **Standards read, and which bore.** I read them from the one known file my contract names, `.scratch/graph-workflow/map-implementation-rules.md`, resolved by a single listing of `.scratch/`, and read nothing else beside it. They are `/coding-principles` and `/naming`; `CONTEXT.md`'s `_Avoid_` lines; the effort's five ground rules; its four standing rules for writing; `graph-conventions.md`; and `/writing-for-agents`. Those that bore:
>
> - **`/writing-for-agents`** bore hardest, this being a prose deliverable. I invoked it and held the added prose against it by hand. Its **negation** lever is satisfied: each prohibition is paired with the positive target ahead of it. Its **single source of truth** lever is the live tension, the condition itself mandating one rule at three sites; the work discharges it by naming the authoritative site at both derivative ones (*"`### Where the work moved one of them` … carries the whole of this"*), so the duplication is marked rather than silent. *Unmoved* is used as a repeated **leading word** and the decision collapses to one binary question, which is a sharpening over the old wording.
> - **`CONTEXT.md`'s `_Avoid_` lines** — I scanned the added text for the refused words and then checked the distinctive refusals by hand rather than trusting the scan, the trap being measured. The scan's only hits were `question` twice, one of the seven ordinary-English words refused for a single concept (the **grilling** node), used here for *"the one question this section turns on"*; not the refused sense. Also by hand: *ask*, refused as a worker's mode of putting things to the human, appears twice in the added text in a reflexive sense (*"Ask of that element alone whether…"*) and never as a channel to the human. No `reviewer`/`verifier`/`auditor`/`reject`/`review`, no `criteria`/`spec`/`definition of done`, no `quality bar`/`CI`, no `report`.
> - **Ground rules** — nothing added assumes this repo, machine or toolchain (1); the added text cross-references only headings inside its own file and depends on no skill being invocable (2); the raise and the `NOT COVERED:` handback both still travel through the manager, and nothing tells an agent to address the human (3); the growth is four real branches rather than machinery for predicted needs, and the condition mandates all three sites (4); the deliverable was held against `/writing-for-agents` (5).
> - **Four standing rules for writing** — rule 4 is notably honoured: all three cross-references cite by heading, never by line number. Rule 1 holds (the *why* compressed, the shapes intact); rule 3 holds (each site is reachable by its own heading). Rule 2 is a rule for the map's items and does not reach a shipped file, which carries no node citations by ground rules 1 and 2.
> - **`graph-conventions.md`** bore on the replace-versus-strike question, as above, and its `## Review` `NOT COVERED:` item shape is unaffected by the widened *why* clause in the contract's own template.
> - **`/coding-principles` and `/naming`** touch nothing here; the change is prose with no code and no new identifiers.
>
> **No reviewing skill.** The standards name none for this repo and I went looking for none, so no part of one was run, left unrun, or delegated. `/writing-for-agents` I read as a standard in my own context, so nothing ran in an agent handed less than I was.
>
> **Not the record.** The changed path is a shipped skill file, so the implementation-rules file's rule about work that is the effort's own record does not fire; I read the one changed path I was given as the work.
>
> **Which reading the moved-standard branch was settled on, as the manager's licence requires me to disclose.** My primary reading is that the branch never fires here: `.claude/skills/expedition-checker/SKILL.md` is not among the standards enumerated in the implementation-rules file, so the work moved my *instructions*, not a standard I hold the work against, and every one of the seven standards I did hold it against is unmoved. Belt and braces, both other readings land in the same place. Under the pre-repair wording I read on disk in the main checkout — the version this work replaces — treating my contract as a standard the bar carries would demand a raise on the bare fact that an element was altered, which is the defect this work exists to repair, and I carried on and disclosed under the human's standing licence, `verbatim` *"Q1 ok Q2 ok"*. Under the repaired wording in the work itself, the altered elements are not ones this work must be held against, so no raise is owed either. All three readings permit an outcome, and my `PASS` is the same on each.

*No `NOT COVERED`, and no question. The manager's note: this is the first checker on this effort to reach the
moved-standard branch and settle it on the ground that a shipped contract is not among the enumerated standards —
three readings, one outcome, all disclosed.*

### Gate — `approve`

**The human's word, `verbatim`.**

> approve

**What it decided.** The gate offered `approve`, `correct` or `reject` on a `PASS`ing tree whose checker asked
nothing. `approve` lands the work as it stands — including flag `223.1`'s two edits outside the three sites the
condition enumerated, which the payload named as the one thing the worker decided rather than raised. **That flag is
settled by the approval.**

**What it also does, and the manager states it because it is a consequence rather than a choice.** `map.md`'s
moved-standard licence said in its own text that it **expires when the branch is repaired**. This is that repair, so
the licence is spent by its own terms. The manager has banked the item verbatim in `map-history.md` and replaced it,
and **no longer carries the licence in a checker's spawn.** Nothing about that was the human's to decide again.

## Answer

*Pasted as the worker wrote it.*

The shipped checker contract's moved-standard branch now fires only where nothing unmoved is left to hold the work
against. All three sites the acceptance condition enumerates state the narrower rule, and the old rule survives at
no site. The only file created, edited or deleted is `.claude/skills/expedition-checker/SKILL.md`.

**Site 1 — `### Where the work moved one of them`.** The one bullet reading *"An element was added, removed or
altered … Raise it."* is replaced by three, and the section's opening prose is rewritten around them.

- Part (a) is now the section's first move rather than something a reader must infer from the comparison method:
  *"A standard is not the file that holds it"*, an edit reaching a standard only where it changes what that standard
  requires or refuses. This is stated up front because three independent readers described the trigger as *a file
  that is also a standard*, which is wider than the text ever said.
- Part (d) is carried by naming the question the section turns on, in the paragraph that keeps the
  operative-content-versus-rationale split: *"is anything unmoved left to hold this work against?"*, followed by the
  statement that this question decides between raising and carrying on and *did the file change* never does. The
  negative is paired with the positive deliberately.
- The bullets are now four, one per case: identical sets (unchanged, original wording); **an element was added** (it
  is work, every pre-existing element is unmoved, hold it against the acceptance condition, and a purely additive
  edit is never on its own a reason to raise); **an element was removed or altered** (asked of that element alone —
  does it reach this work, and does an unmoved statement of it survive elsewhere in that standard or in another
  standard read); and the raise case, **an element this work must be held against moved and no unmoved statement
  survives**, which raises where it is the whole of what must be established and routes to `NOT COVERED:` where it
  reaches only part. A one-line lead-in before the bullets carries part (c)'s element-at-a-time discipline: *"every
  element that did not move still binds, and the work is held against it."*
- Everything the condition's third property protects is intact: the element-by-element set comparison over
  operative content, the operative-content-versus-rationale distinction, the identical-sets case (kept in its
  original words), and the instruction to unwrap both sides first.

**Site 2 — the table under `### When what you check against is itself the problem`.** The row `the work moved the
operative content of a standard the bar carries | a raise, and no outcome` becomes two rows: the whole-of-it case
routing to a raise, and *"the same, reaching only part of what you must establish"* routing to the
outcome-plus-not-covered cell the table already used one row above. One sentence follows the table stating that an
element the work itself added is in none of the rows, and pointing at site 1 as carrying the whole of it.

**Site 3 — the paragraph in `### raise — nothing left to check against`.** Now *"A standard the work moved, where
nothing unmoved survives."* It states the removed-or-altered trigger, the survival test, and then enumerates
positively the three edits that are **not** this ground — a rationale reworded, an element this work added, an
element that moved but is not one this work is held against — followed by the partial case routing to not-covered.
It points at site 1 too.

**The call a later reader would otherwise re-derive: two edits outside the three enumerated sites, in `### A part
you could not establish, alongside a PASS or a FAIL`.** Part (c) sends a partially-reaching moved standard to *"the
file's existing `NOT COVERED:` route"*, but that route stated its cause exclusively as the checker's own blindness —
*"not observable **by you**"*, *"anything outside the paths you were given"* — and its template line asked for *"why
establishing it is outside what you were given"*. A checker arriving from part (c) has a case that is observable and
whose cause is that the yardstick moved, so the route as written did not admit it and the file would have pointed at
a section that denied the case. I added one short paragraph naming that second cause, saying it is not blindness,
pointing back at site 1, and stating that everything below applies to it unchanged; and I widened the template
placeholder to *"why you could not establish it: outside what you were given, or nothing unmoved left to hold it
against"*. Nothing the section already demanded was removed or weakened. This is flag `223.1` above.

**One fact for whoever writes node 214's acceptance condition.** `### raise — nothing left to check against` opens
*"Two things do that"* and then names the acceptance condition and the moved standard; the *"fifth ground beside
those four"* inside it counts ways a **condition** can be uncheckable, not raise grounds, so the two counts are
consistent as they stand. Node 214 adds a raise ground to that section, so its work makes *"Two things"* read three.
I left it, the count being correct today and the sentence not one of my three sites.

**The bar, discovered from the repo rather than taken from the record.** `graph-agent` has no manifest, no task
runner, no CI directory and no formatter config: no `package.json`, `Cargo.toml`, `pyproject.toml`, `Makefile`,
`justfile`, `flake.nix`, `.pre-commit-config.yaml`, no `.github/`. The one ignore file, `.gitignore`, ignores
`.worktrees/` and `.claude/worktrees/` and invokes nothing. So there is no build, no test and no format command to
run, and the bar holds on its non-command half alone. **This matches the record's copy in
`map-implementation-rules.md` exactly** — no difference to report and nothing to repair there. Held against the
non-command half: the effort's five ground rules, the four standing rules for writing, `CONTEXT.md`'s `_Avoid_`
lines (no refused word is introduced), `/writing-for-agents`, `/coding-principles` and `/naming`, and the acceptance
condition. `graph-conventions.md` is a standard the bar names but it governs the effort's seven record files and the
node file format, so it bears on nothing in a shipped skill file.

**No superseded-text history file was appended to**, the old text being replaced in place as the condition requires
for a file the workflow ships. `map.md` was not touched.

**What the worker reported its work invalidates**, pasted as it wrote it:

- **Node 31's `## Answer`** holds the rule this work replaces — the added-removed-or-altered threshold its checker
  guessed at mid-check — and is contradicted on that point alone by the file as it now stands. Its method survives
  untouched. **This was already reported by node 178's worker** and is recorded in node 178's answer, so it is named
  here for completeness rather than as a fresh finding; the manager should not double-file it.
- **`map.md`'s licence item is not contradicted, it is triggered.** The item states in the human's own terms that
  the licence *"expires when the branch is repaired"*. This work is that repair, so landing it satisfies the item's
  own stated expiry rather than falsifying it. Its retirement is the manager's to write.

*The manager did not double-file node 31, on the worker's own instruction. It performed the licence retirement at
this landing, as the worker said was the manager's.*

## Retrospective

*Filed by the manager in the same edit that resolves the node, the duty the human settled at [node
212](212-the-mint-on-second-report-rule-is-defeated.md). Pasted as the worker wrote it.*

**(1) What I had to hunt for.** Almost nothing, and that is unusual for this effort. The one fact I went and got
myself was the bar's commands, which my contract requires me to confirm against the repo rather than trust — one
`ls` over manifests, task runners and `.github/`, plus `.gitignore`. I also grepped the repo for the moved-standard
branch to confirm my node file's author's claim that it appears in no file but the checker contract; that claim held
exactly, and the grep cost one command. The one thing I reached for that was not pointed at was
`/writing-for-agents`, located by `find` over the nix store because ground rule 5 names it by plugin name rather
than by path — a deliberate property of that rule, but it is a search every implementation worker on this effort
pays for again. A path in the rules file beside the name would end it, at the cost of the rule's stated
repo-independence.

**(2) What arrived that this node did not need.** Judged backwards from the finished work:

- **`map.md`, read whole for four items.** This is the effort's largest standing item, reported at least
  twenty-seven times before mine. Of roughly thirty standing items I used four: the never-delete rule's boundary
  (which my condition already restated), the retrospective's four questions, the licence item on my own branch, and
  the node-files-are-for-agents preference. The worktree material, `EnterWorktree`, the concurrency counts, the
  resume rule, the token-priority rule, the one-question-at-a-time rule and the manager's-report rule bore on
  nothing a worker does. The arrangement that would have avoided it is the one the map already applied twice — a
  sibling file holding what only an implementation worker acts on — but `map.md` is read whole *by contract*, so no
  heading inside it can help. What would help is my contract naming which of the map's blocks bind a worker.
- **`map-implementation-rules.md`, read whole for two sections.** I needed `## What the work is held against` and
  the two rule blocks. The file's first 30 lines are its own admission policy and supersession procedure, addressed
  to whoever edits it; the record-node reading rule is addressed to a checker. Roughly a third of the file bore on
  nothing I did.
- **My spawn's pointer to four decisions entries.** Nodes 178 and 46 were useful — 178 as the source of my
  condition, 46 only as the index line naming the several-sites item. Nodes 31 and 214 resolved to nothing usable in
  `decisions.md`: node 31's line is one sentence naming five things the contract gained, which told me nothing about
  the threshold, and **node 214 has no entry in `decisions.md` at all**, being unresolved, so a worker pointed at it
  there finds nothing and does not know whether it looked wrong.
- **Node 178's file, 275 lines, read whole for its part-(a)-to-(c) reasoning.** Nearly all of it is the arrival
  count, its four wrong statements, and the manager's corrections of itself — history I did not need, since my
  condition carries the rule in substance. I read it because the manager named it and because I wanted the author's
  reading of the `NOT COVERED:` sentence. That single sentence, at line 196, is what I went for. It is also the one
  place the record states what I most needed, so I do not regret the read; a link from my node file to node 178's
  *answer section* rather than to the node would have halved it.
- **My node file states the ground for the three-site requirement twice, verbatim**, at lines 19 and 59, the second
  under a heading announcing it is pasted because it looks redundant. Reading the same paragraph twice cost little
  but made me check whether the two differed.

**(3) What would have made this node easier.** In the node file: nothing on the substance — this is the
best-specified condition I could ask for, and the enumeration of three sites with their exact current text meant I
never had to establish the scope myself. Two smaller things: the duplicated ground paragraph, and a link to node
178's `## Answer` rather than to the whole node. In the record: something stating that `### A part you could not
establish` is the route two different causes now reach, which is the one judgement my condition left me to make; my
condition's part (c) named the route as existing but nobody had checked that the route's own section admitted the
case. In the contract: nothing. In the spawn: the note pointing at exactly that `NOT COVERED:` question, with *"I
have no view on the answer"*, was the highest-value line I received — it named the one real decision in the node
before I had read the file, and it did so without pre-deciding it.

**(4) What I read that was stale, wrong, or contradicted something else.** Nothing stale on the substance, and two
things worth naming. First, the record's copy of the bar's commands in `map-implementation-rules.md` **matched the
repo exactly**, which is the outcome that rule wants and is worth recording as a non-finding, since the demotion of
that copy at node 204 exists to catch the other case. Second, my node file says the implementation-rules file *"was
cut by 56.7% an hour ago and everything left in it binds you"* — the file as I read it is 74 lines and still carries
its own editing policy, its supersession procedure, a *"Nothing below was reworded on the way here"* note about
stale *above*/*below* references, and a record-node rule addressed to a checker, none of which is held against a
worker's work. The claim that everything remaining binds a worker is the file's own first paragraph and it is not
quite true of the file's own first thirty lines. That is the same class of defect as the *above*/*below* note it
already carries about itself.
