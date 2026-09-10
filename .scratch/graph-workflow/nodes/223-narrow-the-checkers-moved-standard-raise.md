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
