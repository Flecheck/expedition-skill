# Carry the integration-conflict rule into the map

Type: implementation
Status: resolved

Blocked by: 144

## Question

*Surfaced by [Two writers edit the map at once](115-two-writers-edit-the-map-at-once.md)'s worker, and pasted as it
wrote it.*

> Carry node 115's answer into the map: a rebase conflict is resolved rather than aborted, the resolver depends on
> what conflicted, the slot count is a dial with a stated price, and the manager's pick prefers candidates whose
> conditions name disjoint paths.

**Blockers, in the worker's words:** *"node 144, whose condition clause 5 demands that no other paragraph of
`map-implementation-rules.md` changes — a direct contradiction rather than a merge conflict. Node 152 edits the same
section and will merely conflict, which this node's own answer says is acceptable."*

## Acceptance condition

*Written by node 115's worker. Pasted as it wrote it, and not the manager's.*

~~**Two clauses of this condition have been amended, and clause 7 is not marked where it stands.** The amendments are
held in the two `## Annotation` sections at the end of this file. **Read those before holding any work against this
condition.** *Pointer added by the manager as a safety repair; it changes no clause's text. [Node
199](199-is-an-acceptance-condition-a-rule-or-a-record.md)'s worker established that a condition amended elsewhere,
with nothing pointing at it from the condition block, is read as live by a checker handed the node cold — the
failure node 143's checker caught. **Which form an amendment should take is node 199's open question, and the
manager has not pre-empted it.***~~

**Struck by the manager, on the same day it was written, because its central claim is false.** Clause 7 **is**
marked where it stands: the paragraph beginning `**Amended, and the amendment is the manager's, made with the
human's approval.**` sits **inside the condition block**, as a continuation of clause 7 itself, so a checker
handed this condition as text sees the clause and sees that it has been added to, in the same reading. **This
node was never in the unsafe shape**, and the pointer above was added on a false premise.

**Where the false premise came from, and it is the manager's to own.** [Node
199](199-is-an-acceptance-condition-a-rule-or-a-record.md)'s worker classified this node with nodes 200 and 140 as
*"the clause untouched with the amendment in a following paragraph plus a separate annotation section"*. The
second half of that is right — there is a separate annotation section — and the first half is wrong. **The manager
did not check the clause before repeating the claim**, put it to the human as established, and wrote the pointer
on it. Flag `160.2` records it.

**What this node's shape actually is, under the rule the human approved at node 199's `Q4.`**: the amendment is
adjacent to the clause and inside the block, which is what that rule demands. **Nothing here needs repairing.**

> The work is `.scratch/graph-workflow/`. The worker may edit `map-implementation-rules.md`, `map-manager-only.md`
> and `map-history.md`, and no other file; it may not mark this node, resolve it, or write a line in `decisions.md`
> or `flags.md`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. In `map-implementation-rules.md`, inside the paragraph beginning `**Landing policy**`, the sentence `**A rebase
>    conflict is resolved by nobody in the moment**: the manager runs `git rebase --abort` and the node takes a
>    correction round with the worker respawned.` is struck through in place with `~~`, and its text is otherwise
>    unchanged. It is not deleted and not moved.
> 2. That struck sentence's full text, unaltered, also appears in `map-history.md` under the heading mirroring the
>    section it came from, appended rather than replacing anything.
> 3. New text sits immediately after the struck sentence, stating all four of these and nothing that contradicts
>    them: that a rebase conflict is resolved rather than aborted; that a conflict in text held under the
>    never-delete rule is resolved by the manager by keeping both sides, which is assembly rather than authoring, and
>    is reported without the work returning to the checker or the gate; that any other conflict, product code
>    included, is resolved by the worker whose branch is being rebased, which the manager resumes to edit the
>    conflicted files in place while the manager itself runs every git command, and that this resolution returns to
>    the checker and to the gate; and that where the two sides contradict each other so that keeping both would make
>    the file assert two incompatible things, the manager runs `git rebase --abort` and the node takes a correction
>    round.
> 4. In the paragraph beginning `**How many implementation workers run at once`, new text states that raising the
>    count buys parallel implementation at the price of integration conflicts, that the human sets it, and that the
>    manager neither raises it on its own judgement nor treats the effort's current value as a ceiling. The existing
>    text of that paragraph is unchanged.
> 5. That new text quotes, marked `verbatim`, the words `but the framework should allow user to tell the manager to
>    increase parallelization, at the expanse of odds of having to resolve merge conflicts`.
> 6. `map-manager-only.md` states that when more than one code slot is free the manager prefers candidates whose
>    acceptance conditions name disjoint sets of paths, and gives the reason in one sentence: a condition already
>    lists its paths, so conflict likelihood is readable before either node starts.
> 7. The sentence in `map-implementation-rules.md` reading `The graph's own files are *not* committed per node; they
>    are committed periodically by the human, which is safe only because node files are append-only.` is struck
>    through in place with `~~`, its text otherwise unchanged, with its full text appended to `map-history.md` as in
>    clause 2, and new text beside it stating that the manager commits the graph's own files itself, before a
>    worktree is cut, so that the tree a worker is given equals the tree the manager is standing on.
>
>    **Amended, and the amendment is the manager's, made with the human's approval.** *The clause above stands
>    unchanged and this is added to it, both moments being wanted.* The new text also states that when the human
>    approves a node at its gate, the manager commits its own outstanding record edits, path-limited to the record
>    directory, as the **first step of landing and before the rebase** — because `git merge --ff-only` is refused
>    where a dirty file is one the branch also changes, and because a record commit made after the rebase leaves the
>    branch unable to fast-forward. Committing at the cut keeps the worker's base current; committing before the
>    rebase is what unblocks the merge, and neither substitutes for the other.
> 8. No heading named `## Notes` is added to any file this node edits.
> 9. Every markdown link in the files this node edits resolves to a path that exists, except any link to a path
>    outside this repository, which is out of scope.
> 10. No file outside `.scratch/graph-workflow/` is modified.

## Annotation: why clause 7 was amended, and by whom

*Filed by the manager.*

**The defect and its wording are [node 176](176-the-managers-record-edits-collide-with-a-landing.md)'s worker's, not
the manager's.** It established, by running git in a scratch repository rather than reasoning about it, that
committing the record *before a worktree is cut* does not prevent the collision the clause exists to prevent: the cut
happens when a node is claimed, the manager writes the record continuously for that node's whole life, and node 144's
colliding edits were written minutes before its landing. It said in as many words that *"amending a live condition is
the manager's act with the human, not a worker's"*, and supplied the text the amendment needed to demand.

**The manager put it to the human rather than amending on its own authority**, under the rule that rewriting an
acceptance condition is never the manager's. Their word, `verbatim`:

> ok

**What was done and what was not.** The original clause is left standing and unchanged; the amendment is added
beneath it, because the finding is that the clause is *insufficient* rather than wrong. This node is open and
unclaimed, so no worker was mid-flight when it changed.

## Annotation: this node's clause 7 inherited an error from a resolved node

*Filed by the manager from node 176's handover, and pasted as that worker wrote it.*

> **Node 115 (resolved) — its section 5 states a remedy that does not fix the failure it names.** Its words: *"an
> uncommitted graph edit blocks the landing step even when the rebase is clean. It is why the manager's graph state
> must be committed before a worktree is cut."* **The *"It is why"* does not follow.** The block occurs at the merge,
> at the end of the node; committing at the cut, at the start, leaves every edit the manager makes in between — which
> is several commits' worth, and was the whole of node 144's collision.

***The manager's note.*** **Node 115 is resolved and its section 5 is uncorrected there.** The manager has recorded
the finding here, on the node that inherited it, rather than editing a resolved node's answer. Whether an annotation
onto an already-resolved node has a home in the graph's format at all is one of the manager contract's own declared
unsettled questions.

## Annotation: node 188 has landed, and two of this condition's file names are now wrong

*Filed by the manager from [node 188](188-move-the-landing-section-out-of-the-workers-file.md)'s worker, in its own
words. Nothing above is changed, and **the condition is not amended.***

> **Node 160** (*Carry the integration-conflict rule into the map*) — **satisfiable after a smaller repair.** Its
> clause 1 names *"In `map-implementation-rules.md`, inside the paragraph beginning `**Landing policy**`"* and its
> clause 7 names *"The sentence in `map-implementation-rules.md` reading `The graph's own files are *not* committed
> per node…`"*. Both sentences are now in `map-manager-only.md` — which that node's file list already permits, its
> clause 6 making a demand of it. Only the two file names in clauses 1 and 7 are wrong.

**Why the manager has not repaired it even though it looks like bookkeeping.** The file this condition would now
name is already in its own permitted list, so the fix is two words — but rewriting a condition is not the manager's,
and *"only the two file names are wrong"* is itself a judgement of the worker's that whoever claims this node should
confirm against the tree rather than inherit.

## Amendment, 2026-09-27 (from node 266)

*Written by [node 266](266-a-worker-cannot-see-the-record-the-manager-has-not-committed.md)'s worker under its `NEW NODES`, which joined it to this node, and filed by the manager. Clauses to add to this node's acceptance condition, pasted as it wrote them:*

> 11. The new text that clause 7 demands states that the manager makes the commit before a worktree is cut **before every implementation worktree it cuts**, whatever paths that node's condition names. It also states that the manager makes both of clause 7's commits on its own authority, path-limited to `.scratch/graph-workflow/`, with no diff shown to the human first and each commit reported to the human afterwards.
> 12. The same new text states that an implementation worker reads and edits the effort's record files in its own worktree, and never in the main checkout.
> 13. The sentence clause 7 quotes is looked for in `.scratch/graph-workflow/map-manager-only.md`, which is where it now stands. Scope search: `grep -rn -l 'committed periodically' --include=*.md .` run from the repository root returned `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md`, with the `nodes/` directory excluded. The `map-history.md` hit is banked history and is not edited. Any instance the search reaches outside these two files is reported, not edited.

## Amendment by the human, 2026-09-27 (from raise 1)

*The worker's recommended wording, taken by the human's "ok" to raise 1 and "ok" to the manager's follow-up, both recorded under `## Interview`. Filed by the manager.*

- **Clause 1** reads: "In `map-manager-only.md`, inside the paragraph beginning `**Landing policy**`, the sentence `<quoted>` is removed, and the new text clause 3 demands stands where it stood."
- **Clause 7**, amended in the same way: remove the sentence, with the new text standing in its place.
- **Clause 2, and clause 7's history half**, stay as written: each removed sentence is appended verbatim to `map-history.md` under a heading mirroring `## Landing an implementation node's work`.
- **Clause 4** also lets "still open at node 160" be replaced by the same route.

## Interview

#### Raise 1, relayed 2026-09-27

*Pasted as the worker handed it back. The worker is stopped until the human answers.*

```
NODE:          Carry the integration-conflict rule into the map (160)
ABOUT:         Writes node 115's integration-conflict rule and node 176's and node 266's record-commit rule into the landing section of `.scratch/graph-workflow/map-manager-only.md`. Clauses 4, 5 and 6 are written. The new text for clauses 3, 7, 11 and 12 is also written. I stopped at clauses 1, 2 and 7, which say how the two superseded sentences are handled.
SO FAR:        I read the contract, the node file (condition, the node-188 annotation, and the node-266 amendment with clauses 11 to 13), map.md, map-implementation-rules.md, map-manager-only.md, the decisions.md lines on landing, conflicts and record commits, and `.claude/skills/expedition/graph-conventions.md` (about superseded text and `## Changing the map`). All edits are in the worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/160-record-commits`, in `.scratch/graph-workflow/map-manager-only.md` only. Nothing is committed.
               Clause 1's file name is wrong, as the manager suspected. The `**Landing policy**` paragraph and the sentence `**A rebase conflict is resolved by nobody in the moment**: …` are in `map-manager-only.md` under `## Landing an implementation node's work`, and not in `map-implementation-rules.md`. That file now has only a three-line pointer ("How an implementation node's work is landed is in map-manager-only.md"). Clause 13 fixes clause 7's file name, and nothing fixes clause 1's. Both quoted sentences still match the file byte for byte. `grep -rln` finds the rebase sentence only in `map-manager-only.md` and `map-history.md` (map-history holds the older landing-policy text), and finds `committed periodically` in the same two files, which agrees with clause 13's search.
               Written so far:
               (a) Clause 3's new text is placed right after the rebase-conflict sentence. It states the four required points and cites node 115.
               (b) The new text for clauses 7, 11 and 12 is placed right after the "committed periodically" sentence. It states the commit before every worktree cut, whatever paths the node names, so the worker's tree equals the manager's. It states the commit at approval as the first step of landing, before the rebase, with both reasons. It states that the two commits do not replace each other. It states that both are made on the manager's own authority, path-limited to `.scratch/graph-workflow/`, with no diff shown first and each reported afterwards. It states that a worker reads and edits the record in its own worktree and never in the main checkout. It cites nodes 115, 176 and 266.
               (c) Clauses 4 and 5: sentences are appended to the end of the `**How many implementation workers run at once` paragraph, with the human's words marked `verbatim`. I checked those words against node 115's `## Answer`. The paragraph's existing text is unchanged.
               (d) Clause 6: a new paragraph right after that one states the disjoint-paths preference and the one-sentence reason.
               The two old sentences are still in the file, unstruck. So for now the file states both the old rule and the new one, and it stays that way until you answer. Nothing has been appended to `map-history.md` yet, because the heading and framing depend on the route you choose.
               The contradiction: clause 1 requires the rebase sentence to be "struck through in place with `~~` … not deleted and not moved". Clause 7 requires the same for the "committed periodically" sentence. Both sentences state landing rules that bind now. The rule settled at node 189 says the opposite for rule text in a map file. `graph-conventions.md`, which is one of the standards this work is held to, says: "`map.md`, and every sibling of it that states rules that currently bind, does not [archive its own subject]. So a superseded item in one of them is replaced by its current form, and its superseded text is appended verbatim to `map-history.md`." map.md's standing preference says the same: "Text whose job is to state a rule that currently binds is not struck in place". The rules file adds: "The struck rule statements below predate this and are not licence to add another." Clauses 1 and 7 were written before node 189 settled this. Node 200 hit the same kind of collision, and its worker settled it with a flag. At node 200's gate the human said a raise was expected. map.md records that as a standing rule: a condition that forces a contradiction with a standard is raised. That is why I am raising.
               A smaller point that the same answer could cover: clause 4 keeps the code-slot paragraph's existing text unchanged. That text says the integration-conflict question is "still open at node 160 and node 162", which stops being true for node 160 once this node lands.
ASK:           Should clauses 1 and 7 be amended so that each superseded sentence is replaced rather than struck in place? The amended clauses would also name `map-manager-only.md` in clause 1.
RECOMMENDED:   Yes, replace. Amend clause 1 to read: "In `map-manager-only.md`, inside the paragraph beginning `**Landing policy**`, the sentence `<quoted>` is removed, and the new text clause 3 demands stands where it stood." Amend clause 7 in the same way: remove the sentence, with the new text standing in its place. Clause 2, and clause 7's history half, stay as written: each removed sentence is appended verbatim to `map-history.md` under a heading mirroring `## Landing an implementation node's work`. That meets `graph-conventions.md`'s check 11 and loses nothing. This rests on graph-conventions.md's supersession rule, map.md's node-189 preference, and the node-200 precedent. The change is mechanical: the new text is already written in position. Optionally, clause 4 could also let "still open at node 160" be replaced by the same route.
ALTERNATIVES:  Strike in place as written, reading clause 1's file as `map-manager-only.md`. This meets the condition but breaks graph-conventions.md's supersession rule and adds struck rule statements to a map file, which the rules file forbids.
               Strike in place and also bank each sentence verbatim in map-history. This meets the condition's letter, but it still leaves struck rule text in a live map file, so it has the same breach.

RETROSPECTIVE (this raise, not a handover)
1. What I had to hunt for: whether node 189's replace rule reaches `map-manager-only.md`. The rules file's statement is scoped to "a rule in this file". I found the binding statement in `graph-conventions.md` (the "every sibling of it that states rules that currently bind" paragraph). The node-200 precedent I found by grepping decisions.md and node 200 for "raise" and "strike".
2. What arrived that this node did not need: most of `map.md` (destination, token and v2 notes, vocabulary). Most of `map-manager-only.md` beyond the landing section (steering order, plain-English pass, fog, out of scope). I read the whole file because the condition names it. The node file's struck pointer paragraph about node 199 and flag 160.2 (about 20 lines) bore on nothing.
3. What would have made this easier: the spawn or the node file noting that the condition predates node 189 and requires strike-in-place for live rules, which is a known collision class (node 200). Also, the node-188 annotation's point about clause 1 being filed as an amendment, as clause 13 was for clause 7, rather than left as an annotation.
4. Stale, wrong or contradictory: clause 1 names the wrong file, and nothing amends it. Clauses 1 and 7 contradict node 189 and graph-conventions.md. The code-slot paragraph's "still open at node 160" will be stale once this lands, and clause 4 freezes it. map.md's opening pointer to map-implementation-rules.md is correct.
```

#### The human's answer to raise 1, 2026-09-27

The human, `verbatim`: *"ok"*. It takes the worker's recommendation: "Yes, replace. Amend clause 1 to read: "In `map-manager-only.md`, inside the paragraph beginning `**Landing policy**`, the sentence `<quoted>` is removed, and the new text clause 3 demands stands where it stood." Amend clause 7 in the same way: remove the sentence, with the new text standing in its place. Clause 2, and clause 7's history half, stay as written".

*The manager's note:* the manager had also asked whether the answer takes the worker's optional point, "Optionally, clause 4 could also let "still open at node 160" be replaced by the same route." The bare "ok" does not say, so the manager asks which before resuming the worker.

#### The human's answer to the manager's follow-up on raise 1, 2026-09-27

The manager asked: "Should clause 4 also let that phrase be replaced the same way, with the old text moved to `map-history.md`?", recommending yes. The human, `verbatim`: *"ok"*. It takes the worker's optional point: "Optionally, clause 4 could also let "still open at node 160" be replaced by the same route."

## Answer

The landing policy now resolves rebase conflicts instead of aborting them. The manager commits the record at every worktree cut and before every landing rebase. The slot count is the human's dial.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `ed54b9b`. Flags 160.3, 160.4, 160.5 settle at the node closing report.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

````
HANDOVER:      Carry the integration-conflict rule into the map (160)

ANSWER:        Node 115's integration-conflict rule, and the record commits from nodes 176 and 266, are now in `.scratch/graph-workflow/map-manager-only.md` under `## Landing an implementation node's work`. The old text was replaced and kept, not struck in place. That follows the human's "ok" to raise 1: the condition's strike-in-place wording in clauses 1 and 7 contradicted node 189's rule and `graph-conventions.md`, which say a map file's live rule is replaced and its old text moved to `map-history.md`. The human's second "ok" also let the code-slot paragraph's "still open at node 160" be replaced in the same way.
               - **Where the text is.** Clause 1's file name was wrong. The `**Landing policy**` paragraph moved to `map-manager-only.md` at node 188. `map-implementation-rules.md` keeps only a pointer to it and was not edited.
               - **Rebase conflicts (clause 3).** In the `**Landing policy**` paragraph, the sentence beginning "A rebase conflict is resolved by nobody in the moment" is replaced by new text in the same place. It says a rebase conflict is resolved and the rebase is not aborted. A conflict in text held under the never-delete rule is resolved by the manager keeping both sides. That is assembly, not authoring, so it is reported and does not return to the checker or the gate. Any other conflict, product code included, is resolved by the worker whose branch is being rebased. The manager resumes that worker to edit the conflicted files in place and runs every git command itself. That resolution returns to the checker and the gate. Where the two sides contradict each other, the manager runs `git rebase --abort` and the node takes a correction round.
               - **Record commits (clauses 7, 11, 12).** The sentence "The graph's own files are *not* committed per node; they are committed periodically by the human…" is replaced in the same way. The manager commits the record itself at two moments. The first is before every implementation worktree it cuts, whatever paths the node names, so the worker's tree equals the manager's. The second is the first step of landing on approval, before the rebase. The reason: `git merge --ff-only` is refused where a dirty file is one the branch also changes, and a record commit made after the rebase leaves the branch unable to fast-forward. Neither commit replaces the other. Both are made on the manager's own authority, path-limited to `.scratch/graph-workflow/`, with no diff shown first and each reported afterwards. An implementation worker reads and edits the record in its own worktree, never in the main checkout.
               - **Code-slot count (clauses 4, 5).** The paragraph beginning `**How many implementation workers run at once` gains new sentences. Raising the count buys parallel implementation at the price of integration conflicts. The human sets the count. The manager does not raise it on its own judgement and does not treat the current value as a ceiling. The human's words from node 115 are quoted and marked `verbatim`. That paragraph's "still open at node 160 and node 162" clause is replaced: the conflicts are resolved as the landing policy states, the rule was settled at node 115 and carried in at node 160, and how much of it ships is still open at node 162.
               - **Disjoint paths (clause 6).** A new paragraph after it says that when more than one code slot is free, the manager prefers candidates whose conditions name disjoint sets of paths. The reason given is that a condition already lists its paths, so how likely two nodes are to conflict can be read before either starts.
               - **History.** The three replaced passages are appended word for word to `.scratch/graph-workflow/map-history.md` under a new heading, "Superseded from `map-manager-only.md` at node 160 — …", with one sub-heading each named after the section they came from. For the third passage, the whole sentence containing the replaced clause is kept. The history file was only appended to, so its earlier content is an unchanged prefix. Every removed passage appears byte for byte in the appended text, which meets `graph-conventions.md` check 11.

INDEX LINE:    The landing policy now resolves rebase conflicts instead of aborting them. The manager commits the record at every worktree cut and before every landing rebase. The slot count is the human's dial.

FLAGS:         ASSUMPTION: The new rebase-conflict text keeps the condition's words "text held under the never-delete rule" for the manager's keep-both-sides case. Since node 189, that rule no longer covers rule text in map files, which is replaced instead. So the words cover a conflict in record text (node files, `decisions.md`, `flags.md`), and a conflict between two edits to a map file's live rules falls to the worker, or to the abort where the two sides contradict. I kept the condition's wording rather than narrowing or widening it, because clause 3 fixes the four things the text must state.
               Index sentence: node 160 kept "text held under the never-delete rule" as the manager's keep-both-sides case, so since node 189 conflicts in a map file's live rules go to the worker, not to the manager.
               ASSUMPTION: For the stale "still open at node 160" clause in the code-slot paragraph, I replaced only that clause of the sentence and moved the whole sentence to `map-history.md`. The rest of the paragraph's text is unchanged.
               Index sentence: node 160 replaced only the "still open at node 160" clause of the code-slot paragraph and banked the whole sentence it sat in.

NEW NODES:     none

INVALIDATIONS: Node 68 (*Run an implementation node's work in a worktree*): contradicted. Its "a conflict aborts into a correction round" now holds only where the two sides contradict each other. Otherwise the conflict is resolved.
               Node 11 (*Git and code-landing policy*): contradicted on the record being "committed periodically by the human". The manager now commits it at every cut and at landing. Node 266 already reported this, and node 160 carries it out.
               Node 115: extended. Its section 5 remedy, commit before a worktree is cut, is now joined by node 176's commit before the rebase.
               Node 188: narrowed. The landing section is no longer byte-identical to what it moved.

CONDITIONS:    I searched the `## Acceptance condition` of every open and claimed node for: `resolved by nobody`, `rebase --abort`, `committed periodically`, `still open at`, `second slot`, `Landing policy` and `map-manager-only`. Matches were in nodes 152, 149, 234, 230, 236, 254, 276, 284 and 352, plus this node's own condition. After reading what matched, only node 234 (open, unclaimed) has a clause my work makes wrong.
               Node 234, clause 4, second sentence. Current text: "The sentence beginning `**A rebase conflict is resolved by nobody in the moment**` is not edited, struck, moved or deleted by this node." That sentence no longer exists, so the clause is vacuously true and no longer protects anything. Replacement: "The text in that paragraph beginning `A rebase conflict is resolved, and the rebase is not aborted.` and ending `the manager runs `git rebase --abort` and the node takes a correction round.` is not edited, struck, moved or deleted by this node." What fixes these words: this node's work, once landed in the tree.
               Clause 4's first sentence, "The paragraph beginning `**Landing policy**` is byte-identical to its state at `HEAD`", still holds against whatever HEAD is when node 234 runs.

MISSING FROM MAP: `map.md` does not say that conditions written before node 189 may still require strike-in-place for live rules, a known kind of clash (node 200). I found it through `graph-conventions.md` and by searching node 200.
               Clause 12 puts a rule for workers ("a worker reads and edits the record in its own worktree") into `map-manager-only.md`, which no worker reads. I wrote it where the condition demands. A worker learns it from its spawn.

GATE PAYLOAD:  Checker findings: none yet (no checker has run).
               Raise 1 is answered ("ok", and "ok" to the optional clause-4 point). Both old sentences are now replaced rather than struck, and they are banked in `map-history.md`. The code-slot paragraph's "still open at node 160" clause is replaced and its sentence banked.
               Bar: the repo has no build, tests, formatter or CI. The worktree root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`, with no manifest, which matches the rules file's record. Both edited files are markdown.
               Checks run: every relative markdown link in both edited files resolves (clause 9). No `## Notes` heading was added (clause 8). `git status` shows only the two files below (clause 10).
               Paths touched (worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/160-record-commits`):
               - `.scratch/graph-workflow/map-manager-only.md`
               - `.scratch/graph-workflow/map-history.md`
               Proposed commit message:
                 Carry the integration-conflict rule and the record commits into the map

                 The landing policy in map-manager-only.md now resolves a rebase conflict
                 instead of aborting it, and says who resolves it depending on what
                 conflicted. The manager commits the record before every worktree cut and
                 as the first step of landing. The code-slot count is the human's dial,
                 with its price stated, and the pick prefers nodes whose paths are
                 disjoint. The replaced sentences are banked in map-history.md.

                 Node: graph-workflow/160

RETROSPECTIVE
1. What I had to hunt for: where the clause-1 sentence now stands (found by grep, in `map-manager-only.md`). Whether node 189's replace rule reaches that file (`graph-conventions.md`, the paragraph on "every sibling of it that states rules that currently bind"). The node-200 precedent (by searching decisions.md and node 200).
2. What arrived that this node did not need: most of `map.md` (destination, the v2/token notes, the vocabulary note). Most of `map-manager-only.md` outside the landing section, read whole because the condition names the file. The node file's struck pointer paragraph and flag 160.2.
3. What would have made this easier: a note on the node that its condition predates node 189 and requires strike-in-place for live rules. Clause 1's file name filed as an amendment, as clause 13 did for clause 7, rather than left in an annotation. The resume pointing at the answered `## Interview` in the main checkout did help.
4. Stale, wrong or contradictory: clause 1 names the wrong file. Clauses 1 and 7 contradicted node 189 and `graph-conventions.md`, which the raise settled. Node 234's clause 4 now points at a sentence that is gone (replacement given above). The rules file's own supersession paragraph is scoped to "a rule in this file", although the same rule binds the other map files through `graph-conventions.md`.
````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 56's check; the condition reached it as a verbatim copy in `$TMPDIR/c160.md`.*

> PASS
>
> This is the check of node 160, "Carry the integration-conflict rule into the map". The work is the uncommitted diff to the record files `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/160-record-commits`, on base 7bfa1e8. I read those two files as the work, under the rules file.
>
> I read the whole of `/tmp/claude-1000/c160.md`. That includes node 266's clauses 11 to 13 and the human's amendment of 2026-09-27. Under that amendment, clauses 1 and 7 read as removing the sentence and banking it verbatim, clause 1 names `map-manager-only.md`, and clause 4's "still open at node 160" may be replaced the same way. The struck manager note at the top of the file sits outside the quoted condition, so I did not hold the work to it.
>
> **Parts of the condition**
>
> - **Scope, and clause 10:** met. `git status --short --untracked-files=all` shows only `map-manager-only.md` and `map-history.md`. The diff contains no node file, no `decisions.md` and no `flags.md`.
> - **Clause 1 (amended):** met. In the `**Landing policy**` paragraph of `map-manager-only.md`, the sentence "**A rebase conflict is resolved by nobody in the moment**: … with the worker respawned." is gone, and clause 3's text now stands in its place.
> - **Clause 2:** met. That sentence appears verbatim in `map-history.md` under `### From *Landing an implementation node's work* — the landing policy's sentence on a rebase conflict`. The text is identical: `grep -F` finds it in HEAD's `map-manager-only.md`. The history diff removes 0 lines.
> - **Clause 3:** met. The new text states all four points, and nothing else in the paragraph contradicts them:
>   - "A rebase conflict is resolved, and the rebase is not aborted";
>   - for a conflict in never-delete text, the manager keeps both sides, "assembly rather than authoring", reports it, and "the work does not return to the checker or to the gate";
>   - for any other conflict, product code included, the manager resumes the worker to edit in place while "the manager itself runs every git command", and "That resolution returns to the checker and to the gate";
>   - where keeping both sides would make the file assert two incompatible things, the manager runs `git rebase --abort` and the node takes a correction round.
>   - The next sentence, "A post-rebase bar failure likewise takes a correction round", agrees with these.
> - **Clause 4 (amended):** met.
>   - The sentence naming node 160 as open now reads "resolved as the landing policy above states, settled at node 115 and carried here at node 160, and how much of that rule ships is still open at node 162". The old sentence is banked verbatim (`grep -F` finds it in HEAD).
>   - New text is appended at the end of the paragraph: "Raising the count buys parallel implementation at the price of integration conflicts. The human sets the count. The manager does not raise it on its own judgement, and does not treat the effort's current value as a ceiling."
>   - Apart from those, the paragraph's text is unchanged.
> - **Clause 5:** met. The paragraph carries the quotation marked `verbatim`, word for word: *"but the framework should allow user to tell the manager to increase parallelization, at the expanse of odds of having to resolve merge conflicts"*.
> - **Clause 6:** met. A new paragraph reads "When more than one code slot is free, the manager prefers candidates whose acceptance conditions name disjoint sets of paths." Its one-sentence reason is "A condition already lists its paths, so how likely two nodes are to conflict can be read before either node starts."
> - **Clause 7 (amended), with clause 11:** met.
>   - The sentence "The graph's own files are *not* committed per node; …" is removed. It is banked verbatim under a heading mirroring `## Landing an implementation node's work`.
>   - The text in its place states the commit "before it cuts every implementation worktree, whatever paths that node's condition names, so that the tree a worker is given equals the tree the manager is standing on".
>   - It states the commit on approval "as the first step of landing, before the rebase", with both reasons: `--ff-only` is refused over a dirty file, and a record commit made after the rebase blocks the fast-forward.
>   - It says "neither one replaces the other".
>   - Clause 11: "The manager makes both commits on its own authority, path-limited to `.scratch/graph-workflow/`. It shows the human no diff before either commit, and reports each commit to the human afterwards."
> - **Clause 12:** met. "An implementation worker reads and edits the effort's record files in its own worktree, and never in the main checkout."
> - **Clause 13:** met. The recorded search matches its recorded return. I ran `git grep -l 'committed periodically' HEAD -- '*.md' ':!*/nodes/*'`, and it returns `map-manager-only.md` and `map-history.md`. On the worked tree, `grep -rn -l … --exclude-dir=nodes --exclude-dir=worktrees` returns only `map-history.md`, which is banked history. No instance lies outside the two files.
> - **Clause 8:** met. `grep -c '^## Notes'` in `map-manager-only.md` gives 1 both before and after, so no heading was added. The diff adds no heading to `map-history.md`.
> - **Clause 9:** met. Every `](path)` target outside fences in the two files exists relative to `.scratch/graph-workflow/`, except `/home/mathieu/projects/Lang`. That path is outside this repository, which the clause excludes. It also predates this work: it is not in the diff.
>
> **The bar**
>
> - The worktree's `map-implementation-rules.md` records no build, tests, formatter or CI. The repo confirms this: there is no manifest.
> - `git diff --check` is clean (exit 0).
>
> **Standards.** As in my earlier checks, I read only the standards in `map-implementation-rules.md`, together with the ground rules given as text.
>
> - These bore on the work, and I found nothing against them:
>   - `graph-conventions.md`'s `### Change the map`: each replaced sentence is banked verbatim under a mirroring heading, and the new statements cite nodes 115, 176 and 266 by link;
>   - `## Writing the map`;
>   - the `CONTEXT.md` `_Avoid_` lines;
>   - the writing rules;
>   - `/writing-for-agents`;
>   - the ground rules. These are record files, not shipped files, so the git commands named in them are the effort's own practice.
> - `/coding-principles` and `/naming` did not bear on the work.
> - No reviewing skill is named, so I ran none.
>
> NOT COVERED:
> - None of the condition's parts is uncovered. Clause 10 and the scope sentence's ban on node, `decisions.md` and `flags.md` writes are established from the worktree diff. What the main checkout's record holds is outside what I was given.

### Gate — approve, `standing yes`, 2026-09-27

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and its one NOT COVERED item is the worker's bookkeeping. This settles none of the node's flags; they settle at the node closing report.

## Flags

`160.2` `MANAGER-WRONG` **· settled** — **The manager reported this node to the human as carrying an unsafe amendment shape, and
it does not.** Node 199's worker classified node 160 alongside nodes 200 and 140 as a condition whose amendment sits
only in a separate section. **The manager repeated that without opening the clause**, told the human that node 160
was *"open and unclaimed, and its clause 7 sits unmarked"*, and added a pointer at the top of the condition as a
safety repair. Clause 7 carries its amendment inside the condition block, immediately beneath it. **The pointer was
unnecessary and its premise was false**; it is struck above rather than deleted, and no clause of this condition was
ever changed by it. **The cost was a false statement to the human and a paragraph of noise at the head of a
condition a worker will read cold.**

`160.3` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment from node 266 above.* Node 266's clauses 11 to 13 were filed on this open, unclaimed node without asking the human first.

`160.4` `ASSUMPTION` **· settled** — The new rebase-conflict text keeps the condition's words "text held under the never-delete rule" for the manager's keep-both-sides case. Since node 189, that rule no longer covers rule text in map files, which is replaced instead. So the words cover a conflict in record text (node files, `decisions.md`, `flags.md`), and a conflict between two edits to a map file's live rules falls to the worker, or to the abort where the two sides contradict. I kept the condition's wording rather than narrowing or widening it, because clause 3 fixes the four things the text must state.

`160.5` `ASSUMPTION` **· settled** — For the stale "still open at node 160" clause in the code-slot paragraph, I replaced only that clause of the sentence and moved the whole sentence to `map-history.md`. The rest of the paragraph's text is unchanged.

*The manager's note, 2026-09-27:* flags 160.3, 160.4, 160.5 settle at the node closing report that closes this node, which names its gate as taken under the standing yes.

*The manager's note, 2026-09-27:* the landing rebase conflicted in `map-history.md`, where the manager's own appended block (node 56's glossary location) and this node's appended block met at the end of the file. The manager kept both sides, the manager's block first. That is the keep-both-sides case this node's rule gives the manager, and the resolved diff against `master` removes no line.
