# Narrow the checker's moved-standard raise to where nothing unmoved survives

Type: implementation
Status: claimed

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

*The worker's own text, pasted. The id is the manager's bookkeeping and nothing else. Outstanding — this node has
not reached its gate.*

`223.1` `ASSUMPTION` — **Two edits outside the three enumerated sites, in the `NOT COVERED:` route the narrower rule
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
