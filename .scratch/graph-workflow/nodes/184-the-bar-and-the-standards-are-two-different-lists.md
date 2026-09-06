# The bar's project criteria and the review route's standards are still two different lists

Type: implementation
Status: resolved

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
>
>    **Amended, and the amendment is the manager's, carrying the human's instruction. This clause is reversed rather
>    than supplemented.** Their words, `verbatim`: *"I don't think there should a be a never delete rule on the rules.
>    They can change."* So in `map-implementation-rules.md` a superseded **rule statement** is **replaced** and not
>    struck: the strike markers this node's work added are removed along with the text they mark, and the paragraph is
>    left stating its current form only. **What is not touched by this** is any struck text this node's work did not
>    itself add — that is other nodes' material and other conditions' subject, and node 190 holds the paragraph's
>    remaining shape.
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

`184.3` `CONDITION-WRONG` — **The manager's own, and not the worker's.** Clause 2 of this node's condition imposed
the never-delete rule on a file of rules, and the human has directed that it does not belong there. The manager
amended the clause rather than putting the amendment to them as a question, on the ground that their instruction
names this file and this rule and needs no inference to reach the clause — *"I don't think there should a be a never
delete rule on the rules. They can change."* **The judgement that their words reach clause 2 is the manager's**, and
this flag is where it is recorded. The amendment's scope — 184's own strike markers and no other node's — is also
the manager's and was not stated by them.

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

### Correction round 1 — from the human at the gate, not from a checker

***The manager's note.*** **The check had passed and the human did not approve.** They read the file at the gate and
directed two changes, and the second of them reversed clause 2 of this node's own condition — amended by the manager
on their instruction and recorded as flag `184.3` above. Their words in full are on [node
191](191-the-rules-file-carries-accounts-rather-than-rules.md), which their objection minted; what reached the
worker was the two corrections and their verbatim words for each.

**What the worker changed, pasted as it wrote it.**

> *Correction 2 (clause 2 reversed).* The strike my change introduced — ``~~`CONTEXT.md`'s `_Avoid_` lines, and the
> node's acceptance condition.~~`` — is gone along with the text it marked, and the enumeration now states its
> current form only. The two strikes surviving in that paragraph are node 158's on the ignore file and node 169's on
> the standing preferences; I removed neither, per the manager's scope limit.
>
> *Correction 1 (rules, not an account).* Four pieces of narrative are gone: the sentence beginning *"The divergence
> was a defect and not a split…"*; the reasoning about `/writing-for-agents` being reachable through ground rule 5
> and `graph-conventions.md` not; the account half of the node 184 citation, *"which found this enumeration and the
> review route's below disagreeing about exactly those two"*; and *"Found at node 169, whose condition forbade its
> worker the repair."* The bare citation of node 184 stays.
>
> *The judgement you left to me on the "which reader each is for" material.* I applied one test: does the sentence
> tell a reader what binds them now, or what a node discovered? I kept the first and cut the second, which trimmed
> that material by about half. What stands is:
>
> > **The two enumerations in this section are one set of standards and not two**: this half is what an
> > implementation node's worker writes to, and the review route's *"standards to hold work against"* below is what
> > its checker holds the finished work against. The *"human's global coding principles"* here is `/coding-principles`
> > there, and the one this half adds is the **node's acceptance condition**, which reaches a checker by its own
> > route.
>
> I cut the `**Which reader each is for:**` label into the sentence, compressed the list comparison to *"the one this
> half adds"*, and dropped the verbatim *"The rules should also be used by the implementer"* — `map.md` holds that
> direction, and restating it here is the fourth standing rule's *restating what they hold*. What survives is
> operative: without it a reader meets two enumerations and no statement of which one binds them, and reads the
> `/coding-principles` naming difference as a third divergence.

**What it reports the paragraph now carries, and hands to [node 190](190-the-rules-file-states-one-list-twice.md)
rather than repairing**, in its words:

> **A convention now stands mixed in that one paragraph**, and it is node 190's: under the amended clause 2 a
> superseded rule statement is replaced rather than struck, but node 158's and node 169's strikes remain in place
> beside my clean replacement. The paragraph therefore carries both conventions at once. I left it that way because
> the scope limit was explicit, and I record it so node 190 does not have to rediscover it.

**The correction of detail to its own flag `184.2`**, in its words:

> My second flag's parenthetical said *"my condition did not force the choice: clause 2 would have permitted a
> strike-and-replace."* Clause 2 is now reversed, so that reads wrong; the accurate form is that the amended clause
> would permit a plain replacement. The flag's conclusion is untouched … Nothing in the amended clause 2 reaches it:
> `criteria` is not a strike my change added.

**What it reported about the condition it had been working to**, pasted from its retrospective and left here because
it is a finding about how this node came to need a correction round at all:

> My condition's clause 2 encoded a never-delete rule over the rules file that the human turned out not to hold, and
> I complied with it exactly. The condition was written by node 169's worker, so a worker generalised the map's
> never-delete rule onto a file the human reads as rules that can change — and the cost landed on the gate rather
> than on the node that wrote it. **A condition author writing a convention into a condition is asserting the
> human's practice from the record, which is the one thing a worker cannot check.**

***The manager's note on that.*** **It is the first report of this item and no node is minted for it**, the map's
rule minting on the second. Recorded here so the second report has something to be the second of.

**And the worker connected it to its own earlier retrospective**, in its words: *"I reported that roughly 60% of my
own work file — the `## Landing an implementation node's work` section — bore on nothing for a worker and that five
workers had said so. The human's objection at the gate is the same class of material seen from their side, and it is
now node 191. The two findings are one finding from two directions."*

### Checker run 2 — `PASS`

*Resumed rather than respawned, per the standing instruction. It was given the amended clause 2 as the whole of that
clause and told the work had changed. It was told nothing of the human's other correction and nothing of node 191 —
the condition is the only statement of intent it has. Pasted as it wrote it; every sentence is the checker's.*

> **Nothing inherited from run 1.** Clause 2 was amended and the work moved, both inside the same paragraph, so I
> re-established all five clauses and re-ran the bar against the tree as it now stands.
>
> **Clause 2, against the amended words — the inverted property.** I reconstructed the run-1 intermediate state from
> a snapshot I took that round, so I know exactly which strikes this node's work introduced rather than inferring
> it. Struck spans in `HEAD` line 137: ``~~ignores `.worktrees/`~~`` and `~~this map's own standing preferences~~`.
> Struck spans in the run-1 state: those two, **plus** ``~~`CONTEXT.md`'s `_Avoid_` lines, and the node's acceptance
> condition.~~`` — exactly one pair introduced by this node's work. Struck spans **now**: the two `HEAD` pairs,
> byte-identical, and nothing else. So the strike this node's work added is gone, **and the text it marked is gone
> with it**: `grep` for `lines, and the node's acceptance condition` over the whole file returns 0.
>
> **The scope limit holds in both directions.** A per-line `~~` marker census over the whole file matches `HEAD`
> line for line, and since line 137 is the only line differing from `HEAD` at all, every other node's struck
> material is byte-identical. Neither of the two strikes this work did not introduce was touched.
>
> **One thing worth stating plainly:** the amended clause reads like a departure from `graph-conventions.md`'s
> *"This deletes nothing"*, and on this change it is not. A word-level diff of line 137, `HEAD` versus now, has
> exactly **one** token on the deletion side — `condition.`, whose sentence-ending period moved when the enumeration
> was extended. Everything the work removed this round was text the work had itself written in an unlanded,
> uncommitted state. **Nothing that ever landed was deleted, so there was nothing to bank in `map-history.md`.**
>
> **Clause 1.** Both paragraphs name the two standards — the first branch — and the paragraph also carries the
> second branch's material. I verified that claim against both live enumerations and it is accurate. **Clause 3.**
> Lines 161–177 diff clean against `HEAD`; both blocks identical, in place and in order. **Clause 4.** 40 `](`
> occurrences, all matched, every distinct target exists on disk. The count fell from 41 to 40 because the run-1
> link to node 169 went out with that round's text; `HEAD` did not cite node 169 in this file either, so this is not
> a regression against what landed. **Clause 5.** One entry, the work's own path; nothing staged.
>
> **The bar, re-run in full.** Command half re-verified from the tree rather than assumed: no manifest, task runner,
> Makefile, justfile, flake or pre-commit config at root, and no `.github/workflows`. Non-command half holds. Of the
> words this change adds against `HEAD`, only `finished` and `review` appear on any `_Avoid_` line, and both are the
> false-positive class the file itself warns about. The four standing rules hold: the shape is uncompressed and the
> explanatory prose was tightened this round.

**Its two questions, pasted as it wrote them. Neither is a `FAIL` and it said so.**

> **Carried forward from run 1, still live.** The file now says in its own words *"The two enumerations in this
> section are one set of standards and not two"* — a documented duplication: the next change to the standards must
> be made in two places … The duplication is the condition's wording rather than the worker's choice, so the work is
> not failed for it. Whether one paragraph should instead point at the other is for whoever owns the condition.

> **New this round, and it turns on the amendment.** The enumeration now ends ``… `/writing-for-agents`, and the
> node's acceptance condition — the last two added at [node 184](…).`` Read against the four-item list it follows,
> *"the last two"* points at `/writing-for-agents` and the acceptance condition; what node 184 actually added is
> `graph-conventions.md` and `/writing-for-agents`, the middle two … Read instead as *"the two added last"* the
> phrase is true. Both parses are live. **In the previous iteration a following clause resolved it; complying with
> the amended clause 2 deleted the struck before-state that clause leant on**, and the paragraph now offers a reader
> no anchor for which two are meant. I am not calling this a breach: the ambiguity is confined to a provenance note,
> the enumeration itself is unambiguous and correct, and standing rule 1 asks for exactly the compression that
> produced it — so failing the work on it would be checking against my own preference. Naming the two items outright
> would close it.

*No `NOT COVERED`.*

***The manager's note.*** **The second question is a cost of the manager's own amendment and the checker traced it
there without being told the amendment's history.** The struck before-state was what disambiguated *"the last two"*;
removing it, which is what the amended clause 2 demanded, took the anchor with it. **The manager did not foresee
that** and records it against itself rather than against the worker or the clause.

### Gate — `approve`

**The human's word, `verbatim`.**

> approve

***The manager's note.*** **It declines the correction round the manager recommended.** The manager put two options
at the gate — approve as it stands, or one more round naming the two items outright to close the *"the last two"*
ambiguity — and recommended the correction. `approve` is one of the gate's three words and takes the first. **So the
ambiguous provenance note lands**, and it is [node 190](190-the-rules-file-states-one-list-twice.md)'s to reach,
that node already owning this paragraph's remaining shape.

*Two checker runs, both `PASS`; the correction round between them came from the human and not from a checker. All
three flags are settled by the approval.*

## Answer

*Pasted as the worker wrote it after the correction round.*

> `map-implementation-rules.md`'s bar paragraph now names, in its non-command half: the project criteria (the human's
> global coding principles and `/naming`), this effort's ground rules and its four standing rules for writing,
> `CONTEXT.md`'s `_Avoid_` lines, `graph-conventions.md`, `/writing-for-agents`, and the node's acceptance condition.
> Clause 1 is met by its first branch — both paragraphs name the two standards — and the paragraph additionally
> states which reader each enumeration serves and that the two are one set.
>
> The finding behind the repair, which the human directed out of the rules file and which is recorded here instead:
> **the divergence was a defect and not a deliberate split between the bar and the standards.** `/writing-for-agents`
> was already reachable from the bar through ground rule 5, which the bar's enumeration names as part of *"this
> effort's ground rules"*, so its absence from the enumeration was an omission. `graph-conventions.md` was reachable
> by no path at all. A deliberate split would not have left one of the two reachable twice. That asymmetry, together
> with `map.md`'s standing direction that the rules the checker holds work against are the implementer's too, is
> what settled it.
>
> **The chain that produced this node ends here.** Node 144's condition fenced off the bar paragraph and made node
> 169; node 169's fenced off the review-route paragraph and made this node. Mine fenced off no paragraph, so I could
> touch both, and complying with it produced no fourth node of that kind.
>
> **A convention now stands mixed in that one paragraph**, and it is node 190's: under the amended clause 2 a
> superseded rule statement is replaced rather than struck, but node 158's and node 169's strikes remain in place
> beside my clean replacement. The paragraph therefore carries both conventions at once. I left it that way because
> the scope limit was explicit, and I record it so node 190 does not have to rediscover it.

**What the worker reported its work invalidates:** `none`.

***The manager's note on that last paragraph.*** **It became more than a tidiness question while this node sat at
its gate.** [Node 189](189-where-the-never-delete-rule-stops.md) settled, at the human's word, that a superseded
**rule statement** is replaced and its old text moved verbatim to `map-history.md`. Node 158's and node 169's
surviving strikes in this paragraph are superseded rule statements, so they are now wrong where they stand rather
than merely inconsistent. Node 190 inherits that.
