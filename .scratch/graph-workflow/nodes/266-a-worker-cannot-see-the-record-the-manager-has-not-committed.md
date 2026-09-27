# A worker's worktree cannot see the record the manager has not committed

Type: grilling
Status: resolved

Blocked by: none

## Answer

The manager commits the record itself, path-limited and without a diff, before cutting every worktree and again at landing. Workers work the record in their worktree. This effort's map only.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. Its clauses 11 to 13 are filed on [node 160](160-carry-the-integration-conflict-rule-into-the-map.md) as an amendment. The manager applies the rule from now on, ahead of node 160 landing, on the human's answer recorded under `## Interview`. Flags 266.1 and 266.2 settle at the node closing report.

## Question

*Surfaced by [node 260](260-never-ask-which-is-stated-for-nodes-not-for-what-waits.md)'s worker, and pasted as it
wrote it.*

> An implementation node whose work *is* a change to the effort's record is handed a worktree reset to committed
> `master`, while the record it must edit lives partly uncommitted in the manager's main tree. Node 260 hit this
> exactly: its condition named a `map.md` paragraph that existed only in the manager's working copy, and the node
> file it had to link to was untracked. The worker could produce the right end state, but landing has to reconcile
> two divergent copies of `map.md` by hand, and a worker with less context would have silently written against a
> stale map or reported the condition broken. Which fix does the human want — the manager commits the record before
> resetting a worktree for any node that touches it; record-file nodes are worked in the main tree rather than a
> worktree; or the manager states the discrepancy in the spawn and owns the reconciliation as it does today? Each
> has a different cost and one of them changes the landing policy in `map-manager-only.md`.

**Blockers, in the worker's words:** *"none"*

## The manager's note at filing

*Not a change to anything above.*

**This is a defect in the manager's landing policy and the manager found none of it.** The policy resets every
worktree to the manager's committed `HEAD`, and says nothing about the manager's own **working tree**, which on this
effort is never clean: the graph's record is written continuously and committed in batches.

**The concrete cost, measured on node 260 rather than argued**: ~8k tokens and two minutes of a worker's context
establishing that a paragraph its condition quoted was not in its tree, and a landing that now cannot fast-forward
without a hand reconciliation of `map.md`.

**One consequence the question does not name, and it reaches every record node, not only this one.** A node file
minted during the session is **untracked** in every worktree cut before the commit that adds it. So any link a
worker writes to a node it must cite — which the effort's second standing writing rule requires — dangles in the
tree the checker reads, and resolves only after landing. Node 260's worker took that trade knowingly. **A checker
is blind and will read it as a broken link**, so the cost is paid again at every check.

**The manager offers no position between the three options**, having caused the problem, and notes only that the
first and second both change `map-manager-only.md`'s landing policy while the third leaves it as it is and makes
the manager's spawn carry the discrepancy every time.

## Interview

### Attempt 1

#### Questions 1 and 2, relayed 2026-09-27

*The worker's payload, pasted as handed back.*

```
NODE:          266 — A worker's worktree cannot see the record the manager has not committed
ABOUT:         Decides how an implementation worker, whose tree is cut from committed `master`, gets the effort's live record, which the manager writes continuously and leaves uncommitted. It is decided now because today about 25 nodes landed on top of a record last committed at `084aae9`. Three workers (346, 347, 348) and node 285's script test all had to work around it by editing or reading the main checkout directly.
SO FAR:        I read the node, `map.md`, the worktree, landing and commit lines of `decisions.md`, nodes 115, 176 and 160, the landing policy in `map-manager-only.md`, and the manager's shipped contract. Four findings:
               (1) **You have already decided most of this, and it was never carried out.** Node 115 established that the record "must be committed before a worktree is cut". Node 176, where you assented to the recommendation and said *"stays in the map"*, added a second moment: at landing, the manager commits its own record edits as the first step, path-limited, shows no diff and reports the commit afterwards. Both moments are clause 7 of **node 160**, an implementation node that is open, unblocked (its blocker 144 is resolved) and unclaimed. So the live landing policy in `map-manager-only.md` still says *"The graph's own files are not committed per node; they are committed periodically by the human"*. That is why the manager believes it commits the record only when you ask. Node 176's rule is not being applied either.
               (2) **The effort used to work the other way.** `git log -- .scratch/graph-workflow` shows a run of `Graph state:` commits, several per node, up to `084aae9`. Then they stopped. The stale worktree is a symptom of that gap, not of a missing design.
               (3) **Committing at the cut also fixes node 260's dangling links.** A node file minted before the cut becomes tracked, so a link to it resolves in the tree the checker reads. Working in the main checkout would fix this too. Stating the discrepancy in the spawn would not.
               (4) **The shipped manager contract fixes "approval before any commit".** A commit at landing comes after approval, which is why node 176 did not breach it. A commit at the cut comes before any gate. So the manager needs your standing authority to make record commits on its own, without a diff and without being asked. That is the part no record can give me.
               Settled on my own authority: grilling, research and precondition workers read the main checkout already, so only implementation workers are affected.

Q1. Where the fix lives: commit more often, or read from somewhere else
CONTEXT:       This is the manager's sharpest question. It is also the choice node 266's question offers.
ASK:           Should the manager commit the record itself, path-limited to `.scratch/graph-workflow/`, with no diff shown and the commit reported afterwards, immediately before it cuts every implementation worktree (in addition to node 176's commit at landing)? Or should workers whose node touches the record work in the main checkout instead?
RECOMMENDED:   Commit before every cut, on the manager's own authority. It is what node 115 derived, what node 160's clause 7 already demands, and what this effort did until `084aae9`. It costs one commit per node. The worktree then equals the tree the manager stands on, links to newly minted nodes resolve for the checker, and the gate still shows all of a node's work in one worktree diff. Committing at every cut, rather than only for nodes whose condition names a record path, means no judgement call at claim time. A code-only worker also reads its own node file and the rules file, so it gains from the current copy too. Carrying this out means landing node 160 (its clause 7 already has the words), not minting a new node.
ALTERNATIVES:  - Nodes that touch the record work in the main checkout: the manager's own edits mix into the node's diff, the second code slot can no longer run a record node beside another one, and the checker reads a record that keeps moving.
               - Split nodes: the shipped file is edited in the worktree and the record files in the main checkout (today's practice for 346-348): two places to check and no single diff at the gate.
               - The spawn states the discrepancy and the manager reconciles at landing: this costs every worker the ~8k tokens node 260 spent, and it leaves the dangling links.
               - Commit at the cut only for nodes whose condition names a record path: saves a few commits, and adds a judgement the manager can get wrong.
               - The human keeps committing the record on request: this is the current practice that produced the 25-node gap.

---

Q2. Map only, or shipped
CONTEXT:       Whichever fix Q1 takes, it has to live somewhere. Node 176 put its rule in this effort's map only.
ASK:           Does the fix stay in this effort's map, like node 176's rule, or does it go into the shipped manager contract?
RECOMMENDED:   It stays in the map. Node 176's ground still holds: the problem bites only where an implementation node's work *is* the effort's own record, and on an ordinary effort a worker's paths never intersect the record. There is one residual cost. On an ordinary effort a worktree cut from a stale commit would still hold a stale copy of the worker's own node file, so the manager's spawn should point workers at the node file's main-checkout path. That already happens and needs no new rule.
ALTERNATIVES:  - Ship "commit the record before cutting a worktree" in `.claude/skills/expedition/SKILL.md`: this puts a record-commit exception beside "approval before any commit" for a case most efforts never reach.
               - Ship only a sentence saying the worker reads its node file from the main checkout: this is already the practice and adds nothing.
```

#### The human's answer to questions 1 and 2, 2026-09-27

The human, `verbatim`: *"ok for recommended"*. It takes the worker's recommendation on both: Q1 "Commit before every cut, on the manager's own authority."; Q2 "It stays in the map."

## Handover, attempt 1

*Pasted as the worker handed it back.*

````
HANDOVER:      266 — A worker's worktree cannot see the record the manager has not committed

ANSWER:
> ### The rule
>
> **Immediately before it cuts any implementation node's worktree, the manager commits the effort's record itself**: path-limited to `.scratch/graph-workflow/`, with no diff put in front of the human, and the commit reported afterwards. It does this before every cut, not only for nodes whose condition names a record path. This is **in addition to** node 176's commit, the first step of landing, made after approval and before the rebase. Committing at the cut keeps the worker's base current, and committing at landing unblocks the merge. Neither replaces the other. A worker does **not** read or edit the record in the main checkout: its whole node, record files included, is worked and checked in its own worktree.
>
> The human's answer, `verbatim`: *"ok for recommended"*. It assented to both of the questions they were asked.
>
> ### What this node found, and why the fix is carriage rather than design
>
> - **The rule was already derived, and it had never landed.** Node 115 established that the record "must be committed before a worktree is cut", and node 176 added the commit at landing. Both sit in clause 7 of [node 160](160-carry-the-integration-conflict-rule-into-the-map.md), which is open and unblocked. So `map-manager-only.md`'s landing policy still says *"The graph's own files are not committed per node; they are committed periodically by the human"*. The manager, reading that, committed the record only when asked. Between `084aae9` and the time of this node, about 25 nodes landed on an uncommitted record.
> - **The effort used to do this.** `git log -- .scratch/graph-workflow` shows several `Graph state:` commits per node up to `084aae9`. The gap is a lapse in practice that the stale sentence permits.
> - **Committing at the cut also fixes the dangling-link cost** named at filing. A node file minted before the cut is tracked in the worktree, so a link to it resolves in the tree the checker reads.
> - **Why the human's authority was needed.** The shipped manager contract fixes *"approval before any commit"*. Node 176's commit comes after a gate approval. A commit at the cut comes before any gate, so it needed the human's standing permission for record commits the manager makes on its own. That permission is this answer.
>
> ### Options set aside
>
> - Record nodes worked in the main checkout: the manager's edits mix into the node's diff, the second code slot can no longer take a record node beside another one, and the checker reads a moving record.
> - Split nodes (shipped file in the worktree, record files in the main checkout), today's practice for nodes 346 to 348: two places to check and no single diff at the gate.
> - The spawn states the discrepancy and the manager reconciles at landing: costs each worker what node 260 spent (about 8k tokens) and leaves the dangling links.
> - A commit at the cut only for nodes whose condition names a record path: saves a few commits and adds a judgement the manager can get wrong.
> - The human commits on request: the practice that produced the gap.
>
> ### Scope: this effort's map only
>
> The rule stays in this effort's map and ships nowhere. Node 176's ground holds: the problem bites only where an implementation node's work *is* the effort's own record, and on an ordinary effort a worker's paths never intersect the record. A code-only worker on an ordinary effort reads its node file from the main-checkout path the spawn gives it, which is already the practice.
>
> ### How it is carried
>
> It is carried by landing node 160, whose clause 7 already demands both commit moments. Clauses are added to it (below) so it also states the manager's own authority, "every cut", and where the worker works. No new node is minted.

INDEX LINE:    The manager commits the record itself, path-limited and without a diff, before cutting every worktree and again at landing. Workers work the record in their worktree. This effort's map only.

FLAGS:
ASSUMPTION — **The routine record commits need no human-facing message beyond the report.** Neither question named a commit message or trailer. I follow node 176's flag `176.1`: the commit takes the whole record directory and carries no `Node: <effort>/<NN>` trailer, because that trailer is the join key for a node's code commit and record bookkeeping is not that node's work.
Index: The pre-cut record commit takes the whole record directory and carries no node trailer, following node 176's rule for the landing commit.

ASSUMPTION — **The two scope points were folded into Q1, not asked separately.** My Q1 asked about "before every cut" and "workers do not work in the main checkout" together, with "only record-touching nodes" and the split practice listed as alternatives. The human's bare assent covers them as recommended. I asked them in one question because each only makes sense given the commit-at-cut choice.
Index: "Commit before every cut" and "no record edits in the main checkout" were settled inside the assented question, not asked separately.

NEW NODES:
Joins open node **160** (*Carry the integration-conflict rule into the map*), which is unclaimed and concerns the same file and the same concern: the landing policy in `.scratch/graph-workflow/map-manager-only.md`. Clauses to add to its acceptance condition:
> 11. The new text that clause 7 demands states that the manager makes the commit before a worktree is cut **before every implementation worktree it cuts**, whatever paths that node's condition names. It also states that the manager makes both of clause 7's commits on its own authority, path-limited to `.scratch/graph-workflow/`, with no diff shown to the human first and each commit reported to the human afterwards.
> 12. The same new text states that an implementation worker reads and edits the effort's record files in its own worktree, and never in the main checkout.
> 13. The sentence clause 7 quotes is looked for in `.scratch/graph-workflow/map-manager-only.md`, which is where it now stands. Scope search: `grep -rn -l 'committed periodically' --include=*.md .` run from the repository root returned `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md`, with the `nodes/` directory excluded. The `map-history.md` hit is banked history and is not edited. Any instance the search reaches outside these two files is reported, not edited.
No other new node.

INVALIDATIONS:
- **Node 11** (*Git and code-landing policy*) and the landing-policy sentence it produced, *"The graph's own files are not committed per node; they are committed periodically by the human"*: contradicted. The manager commits the record at every cut and at every landing. Node 176 already contradicted this sentence for landing; this node extends that to the cut and makes the manager's authority explicit.
- **Node 115**: extended. Its "committed before a worktree is cut" was a worker's derivation. It now carries the human's assent and applies to every cut.
- **Node 176**: extended, not changed. Its landing commit stands, and a second moment with the same shape (path-limited, no diff, reported afterwards) is added before it. Its "stays in the map" scope is reaffirmed.
- **Nodes 346, 347 and 348** (and node 285's test against the live graph): their practice of working the record in the main checkout is set aside for future nodes. Their landed work is not affected.

CONDITIONS:    I searched every open and claimed node's `## Acceptance condition` for `committed periodically`, `worktree is cut`, `record edits` and `commit(s|ted) the (record|graph)`. Only node 160 matched, on clause 7. Clause 7 is not made wrong by this node, only incomplete, so I wrote no replacement and gave additions instead, under NEW NODES. Separately, node 160's own annotation already records that clause 7 names `map-implementation-rules.md` where the sentence now stands in `map-manager-only.md`. My clause 13 addresses this. The file name comes from the landed tree, where I confirmed the sentence at `map-manager-only.md` line 98.

MISSING FROM MAP: `map.md` does not say that the record is committed, who commits it, or when. The only statement is the stale sentence in `map-manager-only.md`'s landing policy, which I found by search. Nodes 115 and 176, which had already answered the question, turned up only through the `decisions.md` search the spawn named, and node 160's open clause 7 only by opening node 176. `map.md` also gives no pointer from a node's question to open implementation nodes that already carry its answer.

Method skill: none invoked. I worked from the contract alone.

RETROSPECTIVE
1. **What I had to hunt for:** that nodes 115 and 176 had already answered the question, and that the answer was stuck in open node 160's clause 7. Finding that took four searches, and it was the central fact. I also had to find the shipped contract's "approval before any commit", which is what turned the question into one about authority.
2. **What arrived that this node did not need:** most of `map.md`. Only the landing-adjacent pointers mattered. The `decisions.md` worktree lines on harness routes, `EnterWorktree` and the sandbox (lines 100 to 170) were irrelevant.
3. **What would have made this easier:** a spawn line saying *"nodes 115, 176 and open node 160 already address committing the record"*. The manager's note framed the problem as undesigned when the design existed. A node file for a defect in the manager's own policy could also name the policy's current sentence and the nodes that last changed it.
4. **What was stale, wrong or contradictory:** the landing policy's *"committed periodically by the human"* contradicts resolved node 176 and has done so since it resolved. The manager acted on the stale sentence ("the human commits the record on request"). Node 160's clause 7 names the wrong file for that sentence, which is already annotated but not repaired. Node 266's own filing note says the manager "offers no position" and calls it a defect "the manager found none of"; both are true, but they miss that the manager's earlier nodes had already settled it.
````

## Flags

`266.1` `ASSUMPTION` **· settled** — The routine record commits need no human-facing message beyond the report. *(The worker's full text is under its handover's `FLAGS`.)*

`266.2` `ASSUMPTION` **· settled** — The two scope points were folded into Q1, not asked separately. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-09-27:* flags 266.1 and 266.2 settle at the node closing report that closes this node.
