# How much of the integration-conflict rule reaches the shipped files

Type: grilling
Status: resolved

Blocked by: none

## Answer

The pick filter and slot price already ship. The resolver split stays in the map, `graph-conventions.md` requires each landing policy to cover conflicts, and a correction round can be integration-started.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The node it surfaced is [node 363](363-carry-node-162s-integration-answer-into-the-shipped-files.md). Flags 162.1 and 162.2 settle at the node closing report; flag 115.2 settles on this answer too.

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

#### The human's answer to questions 1 to 3, 2026-09-28

The human, `verbatim`: *"ok"*. It takes the worker's recommendation on all three: Q1 "Yes, and edit nothing."; Q2 "Only the requirement."; Q3 "Yes, as the smallest edit that removes the contradiction".

## Handover, attempt 1

*Pasted as the worker handed it back.*

````
HANDOVER:      162 — How much of the integration-conflict rule reaches the shipped files

ANSWER:        **Of node 115's rule, the shipped files carry the pick preference and the slot count's price, both already shipped. They also carry a requirement that each effort's landing policy says what happens on a conflict, and a correction round that the integration can start. The three-way resolver split stays in this effort's map.** The human's word to all three recommendations, `verbatim`: *"ok"*.

### 1. The pick preference ships, in the form already shipped
The manager contract already says, from the frontier-script change: *"It cannot tell whether two startable nodes would edit the same file ... so apply that filter yourself before you fill a second implementation slot."* That sentence is the shipped form of *"favor paralellization on nodes that have little chance of conflicting with one another"*. It stays as written, and 0 bytes are added. The more exact wording, that the manager prefers candidates whose acceptance conditions name disjoint paths, stays in this effort's `map-manager-only.md`. Flag `115.2` scoped the preference to this effort only. A gate the human approved overtook that reading, and the human has now agreed to it. The two halves of their sentence ship together.

### 2. The slot count and its price are already shipped, with no change
Node 336 put into the manager contract that raising the count buys parallel implementation at the price of conflicts to resolve when the work is integrated, and that the human sets the number. Nothing is added.

### 3. Who resolves a conflict stays with each effort; the shipped files only require the policy to say it
The shipped design leaves landing to each effort's own policy (*"How code lands is set by the effort's own landing policy"*), and no shipped file mentions a rebase. So the three-way split does not ship. The split is: the manager keeps both sides in never-delete text, the branch's own worker resolves everything else, and a contradiction aborts into a correction round. What ships is one clause in `graph-conventions.md`'s description of the `## Landing an implementation node's work` section: the landing policy also covers what happens when integrating a node's work conflicts. Without that clause, a new effort's map is never prompted to decide the question. The ground is that the split has been used once, and only its keep-both-sides branch (the `map-history.md` conflict at the first landing under node 160). A special case stays in the map until a second effort needs it.

### 4. A correction round widens to include one the integration starts
The implementation contract and the glossary's `Correction round` entry now define it as a round started by the human at the gate, or by the manager when integrating the work conflicts. The contract's approve branch no longer says the node resolves at approval. It says the manager lands the work, and where integrating the work conflicts, the worker may be resumed to fix the conflicted files in place, running no git command, and the checker and the gate then run again. That is the route node 216 already settled for content authored after approval, and it matches how this effort's map and node 216 already use the term. Without this change, this effort's own landing policy resumes a worker after approval, while that worker's shipped contract tells it that approval ends its node.

### 5. What stays in this effort's map
The three-way resolver split, the disjoint-paths wording of the pick preference, and the manager's record commits at every worktree cut and before every landing rebase. The record commits were already settled as this effort's own at nodes 176 and 266.

### 6. Skipped from any method skill
No method skill was invoked, so nothing was skipped.

INDEX LINE:    The pick filter and slot price already ship. The resolver split stays in the map, `graph-conventions.md` requires each landing policy to cover conflicts, and a correction round can be integration-started.

FLAGS:         ASSUMPTION — **The bare "ok" is read as assent to all three recommendations.** The reply named no question, so under the contract it settles every question's recommendation in that payload and nothing else.
               Index: A bare "ok" at node 162 was read as assent to all three recommendations: the pick filter already ships, conflicts stay per-effort, and the correction round is widened.

               ASSUMPTION — **The new node's condition covers two contract sentences beyond the two edits the human approved.** Line 16 says the worker holds a code slot "until the human has approved your work". The correction-round bullet says "You receive the human's words exactly as they said them". Both still say the worker's part ends at approval, or that only the human starts a round. Leaving them would keep the contradiction the approved edit exists to remove. The payload quoted about 45 words; these add about 30 more. The gate is where the human can cut them.
               Index: Node 162 widened its approved contract edit to two more implementation-contract sentences that still say a worker's part ends at approval.

NEW NODES:     **Carry node 162's integration answer into the shipped files**
               Kind: implementation
               Question: Carry node 162's answer into the shipped files. Each landing policy must state what happens when integration conflicts, and a correction round may be started by the manager at integration.
               Blockers: none
               Acceptance condition:
               1. `.claude/skills/expedition/graph-conventions.md`: the bullet that begins `` - `## Landing an implementation node's work` — the landing policy: `` also says that the policy covers what happens when integrating a node's work conflicts. It becomes: "where a node's worker works, what one path-limited commit of that node's paths takes, what happens to the worker's tree on each of the gate's three outcomes, and what happens when integrating the node's work conflicts." The bullet's closing sentence, "Landing is the manager's, so neither a worker nor its checker reads this section.", is unchanged. No other sentence of the file changes, and the file names no version-control command it did not name before.
               2. `.claude/skills/expedition-implementation/SKILL.md`, under `## Words used exactly`: the entry `- **correction round** — one cycle of the human saying what is wrong and you fixing it.` becomes `- **correction round** — one cycle of being told what is wrong, by the human at the gate or by the manager when integrating your work conflicts, and you fixing it.`
               3. The same file, in the code block under `## After the code is written`: the line `→ approve → the manager commits; your node resolves` becomes a branch saying, in these words: `→ approve → the manager lands your work; where integrating it conflicts, you may be resumed to fix the conflicted files in place, running no git command, and the checker and the gate run again`. It may wrap over indented continuation lines inside the block. The `correct` and `reject` lines are unchanged.
               4. The same file, near the top: the sentence `You hold a code slot from your first edit until the human has approved your work.` becomes `You hold a code slot from your first edit until your work has landed or been rejected.`
               5. The same file, under the `In a correction round:` list: the bullet beginning `You receive the human's words exactly as they said them.` keeps its existing text and gains one sentence, `In a round the manager starts when integrating your work conflicts, you receive the conflicted files instead, and you fix them in place.`
               6. `.claude/skills/expedition/glossary.md`, entry `**Correction round**:`: its first sentence, `One cycle of the human saying what is wrong and the worker fixing it, while the node stays claimed.`, becomes `One cycle of being told what is wrong, by the human at the gate or by the manager when integrating the work conflicts, and the worker fixing it, while the node stays claimed.` The entry's other sentences and its `_Avoid_` line are unchanged.
               7. No other file under `.claude/skills/` changes, and no file under `.scratch/` changes.
               8. Scope. The command `grep -rn -E 'saying what is wrong|your node resolves|until the human has approved your work|You receive the human.s words exactly' .claude/skills/`, run over the working tree before this node, returned exactly five lines: `expedition-implementation/SKILL.md` for the code-slot sentence, the correction-round entry, the approve line and the correction-round bullet, and `glossary.md` for the `Correction round` entry. Clauses 2 to 6 cover all five. The `graph-conventions.md` clause came from no search, because the place is the work. After the work, the same command returns no line saying that only the human starts a correction round or that the node resolves at approval. An instance the command reaches outside this list is reported and not edited.

INVALIDATIONS: **Node 115** is narrowed and extended, not contradicted. Flag `115.2`'s reading, that the pick preference is this effort's alone, is overtaken: the preference ships in the shipped sentence's form. The flag can settle on this answer. The resolver split's scope is now fixed: it stays in this effort's map.
               **Node 160** is extended. Its code-slot paragraph in `map-manager-only.md` says how much of the rule ships "is still open at node 162". That is no longer true. The binding text is replaced by the `Change the map` procedure, with the old sentence banked verbatim in `map-history.md`.
               **The glossary's `Correction round` term**, and every resolved node quoting the implementation contract's approve line, are extended: a round may now be started at integration, and approval no longer resolves the node in the worker's contract.
               **Node 216** is unchanged. This answer carries its checker-then-gate route into the worker's contract.

CONDITIONS:    Searched every open node's `## Acceptance condition` and `## Question` for these phrases: `correction round`, `approve → the manager commits`, `your node resolves`, `what happens to the worker's tree`, `115.2`, `same file`, `landing policy`, and the paths `graph-conventions.md`, `expedition-implementation/SKILL.md` and `glossary.md` among open implementation nodes. No unclaimed node's condition clause is made wrong, so no replacement is written.
               **Node 34** (open, grilling) quotes the implementation contract's diagram, including `→ approve → the manager commits; your node resolves`, under "What is shipped today". Once the new node lands, that quotation is out of date. Its question, about a finding the implementer believes is false, is unchanged in substance.
               **Node 89** (open, implementation, "Carry the worktree lifecycle into the manager's contract") asks whether the worktree lifecycle is a rule of the workflow or a practice of one effort. This answer settles the conflict-handling part of that question as per-effort: the shipped files only require the policy to state it. The rest of node 89's question stays open.
               **Node 234** (claimed) quotes the landing policy's conflict sentences. Being claimed, it is named but not amended.
               Open implementation nodes on the same three files (32, 41, 190, 208, 284, 359 and others) concern different things, so the defect joins none of them.

MISSING FROM MAP: `map.md` does not say that the landing policy, and the pick and slot rules, now sit in `map-manager-only.md`. It says only that the landing section moved there. I found what that section holds by listing its headings. `map.md` also does not name which shipped sentences already carry part of node 115's rule. I found them by searching the shipped files.

RETROSPECTIVE:
1. What I had to hunt for: which parts of node 115's rule had already shipped. The same-file pick filter came in through the frontier-script commit (`353689f`), and the slot price through node 336. Neither the node file nor the spawn mentioned them, and they changed the answer to Q1 from a decision into a confirmation. I also had to hunt for the exact shipped sentences that say a worker's part ends at approval.
2. What arrived that this node did not need: most of `map.md`, and most of the `decisions.md` search results (glossary grouping, checker repairs, gate ordering). Of `map-manager-only.md`, only the three paragraphs of the landing section were needed, not the worktree mechanics bullets.
3. What would have made this easier: a note in the spawn that nodes 336 and the frontier-script change had already shipped parts of the rule, and a pointer to node 216 as the other half of the correction-round question. In the node file, a line recording that node 176 and node 266 had already scoped the record commits to this effort.
4. What was stale, wrong or contradictory: the node's question says neither rule "is in any shipped file today", but the pick filter and the slot price both had since shipped. The shipped implementation contract and glossary define a correction round as started only by the human, while the map and node 216 use the term for rounds the integration starts. The implementation contract's approve line says the node resolves at approval, which node 242 already found false for the glossary.
````

## Flags

`162.1` `ASSUMPTION` **· settled** — The bare "ok" is read as assent to all three recommendations. *(The worker's full text is under its handover's `FLAGS`.)*

`162.2` `ASSUMPTION` **· settled** — The new node's condition covers two contract sentences beyond the two edits the human approved. *(The worker's full text is under its handover's `FLAGS`.)*
