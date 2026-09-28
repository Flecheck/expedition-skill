# How much of the integration-conflict rule reaches the shipped files

Type: grilling
Status: claimed

Blocked by: none

## Question

*Surfaced by [Two writers edit the map at once](115-two-writers-edit-the-map-at-once.md)'s worker, and pasted as it
wrote it.*

> Node 115 settled that integration conflicts are resolved rather than prevented, and produced two rules whose scope
> the human's words leave open. The first is the pick heuristic — *"favor paralellization on nodes that have little
> chance of conflicting with one another"* — which node 115's worker scoped to this effort's map, because only the
> other half of that sentence says *"the framework should"*. The second is the resolver split: the manager unions
> never-delete prose, the branch's worker resolves code, and a contradiction aborts. Neither is in any shipped file
> today, and the shipped implementation contract already tells a worker that *"another implementation worker may be
> running alongside you"* without saying what happens when the two pieces of work meet. Does either reach the shipped
> files, and if the resolver does, does the implementation contract's definition of a correction round widen to cover
> a round the integration triggers rather than the human?

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**Its subject is flag `115.2`**, which is that worker's own record of having read one sentence of the human's as
scoping only its second half. This node exists so the reading is settled rather than left standing on a flag.

## Interview

#### Questions 1 to 3, relayed 2026-09-28

*Pasted as the worker handed it back.*

```
NODE:          162 — How much of the integration-conflict rule reaches the shipped files
ABOUT:         Node 115 settled that a conflict between two pieces of work is resolved when the work is integrated, not prevented. This node decides how much of that rule goes into the shipped skill files and how much stays in this effort's map. Node 160 has just carried the full rule into the map, so this is the only part still open.
SO FAR:        I read node 115's answer and flags, node 216's answer, the landing section of `map-manager-only.md` as node 160 left it, and the shipped manager, implementation and glossary files.
               - The rule in this effort's map now has three parts. (1) Pick: when two code slots are free, prefer nodes whose conditions name different files. (2) The slot count: raising it buys parallel work at the price of merge conflicts, and only you move it. (3) Who resolves a rebase conflict after your approval. The manager keeps both sides of a conflict in never-delete record text, and that lands without coming back to you. The worker whose branch it is resolves any other conflict, and the manager runs every git command; that goes back to the checker and then to you. If the two sides contradict each other, the rebase is aborted and the node takes a correction round.
               - Already shipped, through gates you approved: the slot count with its price is in the manager contract (node 336: "Raising the count buys parallel implementation at the price of conflicts to resolve when the work is integrated. The human sets the number."). The frontier-script change also shipped a same-file pick filter: "It cannot tell whether two startable nodes would edit the same file ... so apply that filter yourself before you fill a second implementation slot." And the manager contract says "Two snapshots that differ are reconciled when the work is integrated".
               - Not shipped: who resolves a conflict. By design, the shipped files leave landing to each effort: "How code lands is set by the effort's own landing policy". The shipped files never mention a rebase or a worktree. `graph-conventions.md` says an effort's landing policy covers where the worker works, the one commit, and what happens to its tree on each of the gate's three outcomes. It does not mention conflicts, so a new effort's map would not be prompted to say anything about them.
               - Something the shipped files contradict today: this effort's map resumes the worker after your approval to resolve a code conflict. But the implementation contract tells the worker "approve → the manager commits; your node resolves". It also defines a correction round as "one cycle of the human saying what is wrong and you fixing it", and the glossary says the same. The record (the map, node 216) calls the round after an abort or a failed bar check a "correction round", but you did not trigger it.
               - Already settled elsewhere, so not asked here: the manager committing the record at each worktree cut and before each landing rebase stays in this effort's map only (nodes 176 and 266).
               - You asked for the skills to be compacted. The byte counts below are what each option adds to files every manager or implementation worker loads.

Q1. The pick preference (flag 115.2)
CONTEXT:       Node 115's worker kept "favor parallelization on nodes that have little chance of conflicting" in this map only, because only the other half of your sentence said "the framework should". Since then, the frontier-script gate shipped a same-file filter anyway.
ASK:           Does the pick preference belong in the shipped files, as the sentence already there, with the finer "compare the conditions' named paths" wording staying in this effort's map?
RECOMMENDED:   Yes, and edit nothing. The shipped sentence already does the work, and flag 115.2 closes as overtaken by that gate. It adds 0 bytes. Your sentence treats the two halves as one thought, and the shipped half already sits next to the slot-count trade.
ALTERNATIVES:  Replace the shipped sentence with node 115's "prefer candidates whose conditions name disjoint paths" wording (about 30 words, and it is more exact). Or take the pick preference out of the shipped files, as flag 115.2 read your words (this undoes a change you approved).

---

Q2. Who resolves a conflict: does it ship?
ASK:           Should the shipped files carry the three-way resolver rule, or only require each effort's landing policy to say what happens when integrating a node's work conflicts?
RECOMMENDED:   Only the requirement. Add one clause, about 12 words, to the line in `graph-conventions.md` that describes the landing section, so it says the policy also covers what happens when integration conflicts. The rule itself stays in this effort's map. The shipped design already leaves all landing mechanics to each effort, and the shipped files never mention a rebase. The split has also been exercised only once, and only the keep-both-sides case (the `map-history.md` conflict at the first landing). The worker-resolves case has never run. That makes it map material under the rule that the map is where a special case belongs until a second effort needs it.
ALTERNATIVES:  Ship nothing (0 bytes). A new effort's map would then have no prompt to decide conflicts and could quietly default to aborting.
               Ship the full three-way split as the default in the manager contract (about 90 words, loaded by every manager session). This is the most complete, but it is untested and it adds rebase mechanics to a contract that has none.

---

Q3. The implementation worker resumed after approval
CONTEXT:       This effort's map already resumes a worker after your approval to fix conflicted files, while the worker's own contract says approval ends its node. That contradiction exists today, whatever Q2 decides.
ASK:           Should the implementation contract, and the glossary's `Correction round` entry, widen to include a round that the manager starts when integrating the work conflicts, not only a round that you start?
RECOMMENDED:   Yes, as the smallest edit that removes the contradiction, about 45 words over two files. (a) The glossary and the contract define a correction round as "one cycle of being told what is wrong, by the human at the gate or by the manager when integrating the work conflicts, and the worker fixing it". (b) The contract's approve branch reads "→ approve → the manager lands your work; where integrating it conflicts, you may be resumed to fix the conflicted files in place, running no git command, and the checker and the gate run again". This matches how node 216 and the map already use the term, and what the checker-then-gate route already does.
ALTERNATIVES:  Leave the contracts alone and have this effort's `map-implementation-rules.md` tell the worker (0 shipped bytes). But then a map rule contradicts a shipped contract, which is the conflict node 28 settles against.
               Keep "correction round" for rounds you start only, and name the integration case something new. That coins a term, and the record already uses "correction round" for it.
```
