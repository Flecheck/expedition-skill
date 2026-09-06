# The bar's project criteria and the review route's standards are still two different lists

Type: implementation
Status: claimed

Blocked by: 169

## Question

*Surfaced by [The rules file's bar paragraph still names the map's standing preferences as project criteria](169-rules-file-bar-paragraph-names-the-maps-standing-preferences.md)'s worker, and pasted as it wrote it.*

> `map-implementation-rules.md`'s `## What the work is held against` holds two enumerations of what work is held to,
> and after this node they still differ. The bar paragraph's non-command half reads *"the project criteria (the
> human's global coding principles and `/naming`), [the ground rules and the four standing rules], `CONTEXT.md`'s
> `_Avoid_` lines, and the node's acceptance condition"*. The review-route paragraph's **standards to hold work
> against** reads *"`/coding-principles` and `/naming`; `CONTEXT.md`'s `_Avoid_` lines; [the ground rules and the four
> standing rules]; `graph-conventions.md`; and `/writing-for-agents`"*. So `graph-conventions.md` and
> `/writing-for-agents` are in the checker's list and absent from the implementer's, and `/writing-for-agents` is the
> standard ground rule 5 says every prose deliverable on this effort is held against. The human's standing direction
> at `map.md` is that *"The rules should also be used by the implementer"* — one set of rules, not two — and node 143
> landed the implementer and the checker reading the same file for that reason. Whether the divergence is a defect or
> a deliberate split between *the bar* and *the standards* is what this node settles; I could not repair it, my
> condition's clause 3 forbidding any change to another paragraph of that file.

**Blockers, in the worker's words:** *"169."*

## Acceptance condition

*Written by node 169's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map-implementation-rules.md`, and no other file may be edited. The worker may
> not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> Done means all of the following are true of the finished tree.
> 1. The paragraph beginning `**The bar's commands for this repo, discovered on first use**` and the paragraph
>    beginning `**The review route for this repo, discovered on first use**` no longer disagree about whether
>    `graph-conventions.md` and `/writing-for-agents` are held against an implementation node's work. Either both
>    paragraphs name them, or one paragraph states in its own text that it enumerates something different from the
>    other and says what — for instance that the bar's project criteria are a subset, and which reader each
>    enumeration is for.
> 2. Nothing is deleted: any superseded wording remains in the file, marked struck, and the replacement is added
>    around it.
> 3. No numbered rule in the file's two blocks — the five ground rules, and the four standing rules for writing — is
>    reworded, renumbered or reordered.
> 4. Every markdown link in the file resolves to a path that exists.
> 5. No file outside `.scratch/graph-workflow/` is modified.

## The manager's note at filing

*Not a change to anything above.*

**Its author found this while forbidden to fix it**, by the same clause that produced this node's own parent: node
144's condition stopped its worker touching the bar paragraph, which became node 169; node 169's condition stops its
worker touching the review-route paragraph, which becomes this. **Three nodes in a chain, each created by the
condition of the last.** The manager records the shape and takes no view on whether the conditions were wrong to be
narrow.

## Flags

*Both are the worker's own text, pasted. The ids and links are the manager's bookkeeping and nothing else.*

`184.1` `ASSUMPTION` — I judged the divergence a defect rather than a deliberate split between the bar and the standards, and repaired it by widening the bar's enumeration to match the review route's. The judgement rests on two things rather than on preference: the human's standing direction that the rules the checker holds work against are the implementer's too, and the measured asymmetry that `/writing-for-agents` was already reachable from the bar via ground rule 5 while `graph-conventions.md` was reachable by no path at all. A deliberate split would not have left one of the two reachable twice. Below all three raise triggers: the repair was mine to make, it reaches no file but this one, and I hold a recommendation I believe.

`184.2` `ASSUMPTION` — I left the pre-existing phrase *"the project criteria"* untouched. `criteria` appears on a `CONTEXT.md` `_Avoid_` line, but that line belongs to the **acceptance condition** entry, refusing `criteria` as a name for an acceptance condition — and the bar paragraph names the project criteria and the node's acceptance condition as two separate things in the same sentence, so it is not using the refused sense. This is exactly the false-positive shape the review-route paragraph documents. So I read it as a false positive rather than as a defect I declined to fix, and my condition did not force the choice. Node 189's question of where the never-delete rule stops does not bite here, there being nothing I judged wrong to remove.

## Review

***The manager's note before the first check, and it is against the manager.*** **Two statements in this node's spawn
were false, and its worker checked both rather than taking them.** The manager said the main checkout carried
uncommitted edits in the Landing section — `diff` shows the two copies byte-identical, so those edits landed in
`c8e2c69`. And the manager said a worktree cut from a commit contains no node files — false here, `.scratch/` being
committed periodically, with node files through 185 present in that tree. **The second of those the manager had
written into three spawns as a correction to an earlier defect**, and it was itself wrong.

### Checker run 1 — `PASS`

*Pasted as the checker wrote it, ordered under its own headings; every sentence is the checker's.*

> **Settled first: the work moved a standard-bearing file.** The one changed path is the implementation-rules file my contract sends me to. I split it as the contract requires. The only changed line is line 137, the bar's-commands paragraph. The review route's `**The standards to hold work against:**` enumeration — the one my contract points a checker at — is byte-identical on both sides. Comparing the operative sets element by element (unwrapped to words, strike markers stripped): the set of things this file requires of an implementation node's work is **identical** before and after. **What moved is *which of the two paragraphs names them*, not the set.** Only wording moved, so the check stands and I ran it.
>
> **I read the changed path as the work under the rule at `An implementation node's work on this effort may be the effort's own record`**, deriving no statement of intent from its content.
>
> **No reviewing skill is named for this repo, so I ran none and went looking for none.** I loaded `/writing-for-agents` for its text only; it spawned nothing, so the delegation limit did not arise.
>
> 1. **The two paragraphs no longer disagree.** Stripping struck spans from line 137, its live text names `graph-conventions.md` and `/writing-for-agents`. The review route names both. Both paragraphs now name them — the condition's first branch. The work additionally supplies the second branch's material.
> 2. **Nothing deleted.** Splitting both revisions into words and stripping `~~` from both sides, **the deletion side of the diff is empty** — no word was removed. Line 137 carries 6 `~~` markers, an even count, so every strike closes.
> 3. **No numbered rule touched.** `diff` over numbered lines reports exactly `137c137`. The five ground rules and the four standing rules are unchanged, in place and in order.
> 4. **Every markdown link resolves.** 41 occurrences, 26 distinct targets, all exist on disk, including the two newly added.
> 5. **Nothing outside `.scratch/graph-workflow/`.** One entry, nothing staged; the node's file, `decisions.md` and `flags.md` all untouched, so the worker neither marked nor resolved the node.
>
> **The bar.** Command half empty, as given. Non-command half holds. `CONTEXT.md`'s `_Avoid_` lines: of the words this change adds, only `decision` and `review` appear on any `_Avoid_` line, and **both are the false-positive class the file itself warns about** — `decision` is refused as the name for a grilling node and is used here as ordinary English, and `review` is refused as the name for the gate while *"the review route"* is this file's own pre-existing term. `graph-conventions.md`'s `## Writing the map` scopes itself to `map.md`, so it does not reach this file; strike-in-place is this file's established practice in ten other places.

**The question it raised alongside its outcome, pasted as it wrote it.**

> Complying with the condition's first branch leaves the same set of standards enumerated **twice** in one section, and the work says so in its own text: *"The two enumerations in this section are one list."* `/writing-for-agents` — a standard this very file names — refuses that: *"Keep each meaning in a single source of truth… Duplication… costs maintenance and tokens."* The next change to the standards must now be made in two places, which is the shape of the divergence this node was minted to repair. The condition's second branch was not available honestly, since the work's finding is that the two enumerate the *same* thing and not different things; and merging them into one list would mean removing an enumeration, which the condition's clause 2 forbids. **So the duplication is the condition's own wording rather than the worker's choice**, the worker was not free to depart from it, and the work is not failed for it. Whether the file should instead carry one enumeration with the other paragraph pointing at it is a question for whoever owns the condition.

*No `NOT COVERED`.*

***The manager's note.*** **The checker reached [node 190](190-the-rules-file-states-one-list-twice.md)'s subject
independently, from behind the blindfold.** This node's own worker minted node 190 for exactly the duplication the
question names, in the same handover; the checker had not read that node file, that handover, or any part of the
record. **Two agents, neither able to see the other, converged on the same defect and on the same remedy** — one
enumeration with the other paragraph pointing at it. The manager records the convergence and settles nothing on it.

**It also names the condition rather than the work as the cause**, which is the same finding node 184's worker made
about the chain 144 → 169 → 184: a narrow condition producing the defect its own node was minted to repair.
