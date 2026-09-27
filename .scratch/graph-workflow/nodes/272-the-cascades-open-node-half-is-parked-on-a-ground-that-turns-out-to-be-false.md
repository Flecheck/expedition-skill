# The cascade's open-node half is parked on a ground that turns out to be false

Type: grilling
Status: resolved

Blocked by: none

## Answer

Part 2 of the cascade gets no pass: every party's pre-handover search covers open nodes' questions as well as conditions and reports the questions it changes; the manager updates them in place.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The nodes it surfaced are [node 350](350-carry-the-open-question-search-into-the-shipped-contracts.md) and [node 351](351-the-cascades-per-candidate-agent-does-not-join-a-defect-to-an-open-node.md); its replacement duty for node 87 is filed there. Flags 272.1 and 272.2 settle at the node closing report.

## Question

*Surfaced by [node 263](263-nothing-tells-the-falsifying-party-to-go-and-look.md)'s worker, and pasted as it wrote
it.*

> [Node 15](15-cascade-pass-mechanics.md) split the cascade three ways and parked the open-node half — *"Open-node
> targets are not settled, and stay where they are"* — on one stated ground: *"no index reaches an open node — an
> open node's one-line summary is its title."* [Node
> 263](263-nothing-tells-the-falsifying-party-to-go-and-look.md) falsifies that ground for one class, and only one:
> an open node's `## Acceptance condition` is a named section in a fixed place, enumerable at 81 across this graph
> and searchable for a handle at 4 to 38 lines of reading. Node 263 takes that class and gives it part 1's
> mechanism. **What this decides is what happens to the rest of part 2** — an open node's question, its blockers,
> its annotations, which have no such named section and for which node 15's ground may still hold. Three things ride
> on it. First, node 15 parked a second duty alongside: *"sharpening an unstarted node's acceptance condition, which
> [node 07] gave this pass, is an open-node edit and therefore stays with the manager for now"* — node 263 moved the
> *finding*, and whether the *sharpening* moves with it is unsettled. Second, node 263's own stated residual lands
> here: a condition that names a thing in different words from the ones the change uses is invisible to a handle
> search, and an edge-walking pass is what would catch it. Third, the human's own fact, `verbatim`, is that on the
> cascade *"there was no progress done"* — [node 44](44-cascade-worker-contract.md) and [node
> 87](87-managers-cascade-duties-have-no-contract.md) are open and both scoped to part 3, landed code, so part 2 has
> no node at all and this is it. **Adjacent and not merged:** [node 37](37-invalidations-is-not-a-check.md) holds
> the resolved-node record, which is indexed by `decisions.md` and which part 1 has already reshaped.

**Blockers, in the worker's words:** *"none. Nodes 15 and 263 are resolved and are its inputs; nodes 44 and 87 are
open, are scoped to part 3, and neither blocks nor is blocked by this."*

## The manager's note at filing

*Not a change to anything above.*

**The human's own fact is what produced this node**, and the manager did not hold it: *"there was also the idea of
the cascade agent that is relevant (but there was no progress done)"*. Node 263's worker had finished its
recommendation before that reached it, went and read nodes 15, 44 and 87 rather than a paraphrase, and found that
the cascade's own answer had already parked precisely the class it was answering.

**The manager is offering no position on any of the three forks**, and says why rather than leaving it blank: it has
already been wrong once on this node's parent about which things are findable by search — flag `263.4` — and the
whole of this question turns on that same judgement applied to a different corpus.

**One thing the manager holds that the question does not name.** The pattern node 263 used is not specific to
acceptance conditions: *a later fact can only falsify a demand by changing something the demand names, and the party
that made the change is already holding that word or path*. Whether that reaches an open node's **question** — which
is prose rather than a demand, and names things far more loosely — is exactly what this node has to settle, and it
is the difference between the two halves of part 2.

## Interview

### Attempt 1

*The worker stopped once on the session's usage limit and was resumed in place.*

#### Question 1, relayed 2026-09-27

*The worker's payload, pasted as handed back.*

```
NODE:          The cascade's open-node half is parked on a ground that turns out to be false (272)
ABOUT:         Node 15 split the cascade three ways and parked part 2, changes that land on open nodes, on the ground that "no index reaches an open node". Node 263 showed that ground is false for acceptance conditions. This node decides what happens to the rest of part 2: an open node's question, its blockers and its annotations. It is decided now because node 44's cascade contract (part 3, landed code only) is written and awaiting its check, and node 87 is about to ship "open-node targets stay manual" as a manager duty.
SO FAR:        I read node 15's answer, node 263's answer, node 87 and its condition, node 44's draft contract in its worktree, the shipped manager contract's amendment rules and graph-conventions.md's Supersede and Annotation rules. Then I measured.
               - **Node 15's ground is false for questions too, and in the same way.** `## Question` is also a named section in a fixed place. Across the 75 open or claimed nodes the question sections total 1,764 lines (~20,600 words). Searching them for handles costs little: `map-history.md` 2 matching lines, `map-implementation-rules.md` 10, `INVALIDATIONS` 9, `code slot` 9, `cascade` 21. That is the same range as node 263's 4 to 38 lines over conditions. So the real difference between the two halves is not findability. A question is looser prose than a demand, so a handle search catches renames and moved paths in it but misses "your question is now partly answered" when that is said in other words. That is the synonym gap node 263 already named.
               - **Settled on my own authority, from the shipped files (you are not asked these):**
                 (a) Sharpening an unstarted node's condition has already moved out of part 2. The shipped manager contract now has the party that established the fact write the replacement clause and the manager file it. Node 327 added "a same-file, same-concern defect joins the open node". So node 15's "stays with the manager for now" is spent.
                 (b) Blockers are covered already. graph-conventions.md's Supersede procedure makes the manager repoint inbound edges.
                 (c) Annotations do not arise. An annotation records a change to a node's *answer*, and an open node has none. An open node's question changing is an in-place update with the old wording marked.
                 So what is left of part 2 is exactly one thing: an open node's `## Question`.
               - **I will report one side finding on the handover (you need not answer it).** Node 44's draft per-candidate role reports new nodes with no join-to-open-node rule. A cascade-found defect in the same file and on the same concern as an open node would therefore become a new node, against node 327's rule.
ASK:           How should an open node's `## Question` be kept current when another node's work changes it (renames a term in it, answers part of it, or makes it unnecessary)?
RECOMMENDED:   Give it part 1's mechanism. No pass of its own. Every worker already searches the open nodes' `## Acceptance condition` sections for the handles its work fixes. That same search also covers their `## Question` sections. Any open node whose question the work changes is reported on the handover, and the manager updates an unclaimed node in place under the existing Supersede/update rule. For a claimed node the manager decides, as it does for conditions. The synonym gap stays stated rather than solved, as at node 263. This rests on three things. The measured cost is a few to about twenty lines per handle. It puts the context in the worker that already holds the handle, per your standing preference. And a separate pass for this half would spend a spawn per resolution to re-derive what the resolving worker had in hand, which node 15 already rejected as the cost of a cascade agent per resolution. It changes one line in the five worker contracts, plus node 87's "open-node targets stay manual" duty, which I would replace in its condition.
ALTERNATIVES:  - Keep it manual (status quo): the manager reads its own answers and updates open questions by hand, and node 87 ships "stay manual" as written. This keeps the duty in the manager's hand, which is where node 263 measured such repairs stalling (node 95).
               - Pull at claim time: the worker claiming a node checks its own question against the decisions resolved since the node was filed. This catches the synonym case a handle search cannot, but it costs every claim a read and finds the change only when the node is picked up, not when it happens.
               - A spawned edge-walking pass over open nodes' questions at each resolution: this catches the synonym case at the time it happens, but it is a new agent per resolution, for a gap with no recorded miss yet.
               - Push plus pull together: the fullest coverage, at the cost of both.
```

#### The human's answer to question 1, 2026-09-27

The human, `verbatim`: *"ok"*. The manager reads it as taking the recommendation, the one option the question marked recommended: "Give it part 1's mechanism. No pass of its own. Every worker already searches the open nodes' `## Acceptance condition` sections for the handles its work fixes. That same search also covers their `## Question` sections."

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      The cascade's open-node half is parked on a ground that turns out to be false (272)

ANSWER:
**Part 2 of the cascade gets part 1's mechanism, and no pass of its own.** The human's reply, `verbatim`: *"ok"*, a bare assent to the one recommendation offered. So the recommendation is theirs.

**What was left of part 2 is one thing: an open node's `## Question`.** Node 15 parked part 2 (changes that land on open nodes) on the ground that *"no index reaches an open node"*. Node 263 showed that ground false for acceptance conditions. The rest of part 2 was an open node's question, its blockers and its annotations, and three of those were already settled by the shipped files:
- **Sharpening an unstarted node's condition has already left part 2.** The shipped manager contract (`.claude/skills/expedition/SKILL.md`) has the party that established a fact write the replacement clause, with the manager filing it. Node 327 (`eef448a`) added the rule that a same-file, same-concern defect joins the open node. So node 15's *"stays with the manager for now"* is spent.
- **Blockers need nothing new.** `graph-conventions.md`'s Supersede procedure already has the manager repoint inbound edges.
- **Annotations do not arise.** An annotation records a change to a node's *answer*, and an open node has none. A change to an open node's question is an in-place update with the old wording marked, under the same Supersede section.

**Node 15's ground is false for questions too, and in the same way.** `## Question` is a named section in a fixed place. Across the 75 open or claimed nodes, measured 2026-09-27, the question sections total 1,764 lines (~20,600 words). Handles match cheaply:

| handle | matching lines |
| --- | --- |
| `map-history.md` | 2 |
| `map-implementation-rules.md` | 10 |
| `INVALIDATIONS` | 9 |
| `code slot` | 9 |
| `cascade` | 21 |

That is the same range as node 263's 4 to 38 lines over conditions. So the difference between the two halves was never whether they can be found. The difference is that a question is looser prose than a demand.

**The rule.**
- The search every party already runs before handing back a fact covers the open nodes' `## Question` sections as well as their `## Acceptance condition` sections. It uses the same handles: each word the work refuses, each path it changes or moves something out of, and each phrase it supersedes. It covers every open node, claimed or not, and reads only what matches.
- The party reports each open node whose question its work changes: a renamed term, a part answered, or the node made unnecessary.
- The manager updates an unclaimed node's question in place, old wording marked, under graph-conventions.md's rule for a node whose question has only changed. What to do about a claimed node stays the manager's, as for conditions.
- Where no such party exists, the manager searches.
- No agent is spawned for this half, and there is no pull at claim time.

**The residual, stated and not solved.** A question that names a thing in different words from the ones the change uses will not match a handle search. The most likely miss is "your question is now partly answered", said in other words. This is the same limit node 263 accepted. An edge-walking pass or a claim-time check would catch it, and both were set aside for now because no miss of this kind is recorded.

**What was set aside:**
- keeping it manual, which leaves the duty where node 263 measured such repairs stalling (node 95);
- pulling at claim time;
- a spawned edge-walking pass per resolution;
- push plus pull together.

**What it means for node 87.** Node 87's fourth duty, *"open-node targets stay manual"*, is superseded by this answer and is replaced below under CONDITIONS.

INDEX LINE:    Part 2 of the cascade gets no pass: every party's pre-handover search covers open nodes' questions as well as conditions and reports the questions it changes; the manager updates them in place.

FLAGS:
ASSUMPTION: This node's own prose: I settled three of the four sub-items of part 2 myself, from the shipped files, and did not put them to the human. Sharpening a condition has already moved: the manager contract's amendment rules and node 327 both ship it. Blockers are covered by graph-conventions.md's Supersede step that repoints inbound edges. Annotations do not arise, because graph-conventions.md defines an annotation as a change to a node's answer and an open node has none. Only the `## Question` half went to the human. Index sentence: Node 272 settled that condition-sharpening, blockers and annotations needed no new part-2 mechanism, reading the shipped files, and asked the human only about open nodes' questions.

ASSUMPTION: This node's own prose: I read *"the manager updates a claimed node's question as it decides"* as the same split the shipped manager contract already draws for conditions, where what to do about a claimed node stays the manager's. It is not a new permission to edit a question under a live worker. Index sentence: Node 272 read a claimed node's changed question as the manager's to handle under the existing claimed-node split, granting no new permission to edit it under a live worker.

NEW NODES:
1. **Name:** Carry the open-question search into the shipped contracts
   **Kind:** implementation
   **Question:** Node 272 decided that the search every party runs before handing back a fact covers the open nodes' `## Question` sections as well as their `## Acceptance condition` sections. The party reports each open node whose question its work changes, and the manager updates it in place. The shipped files state the search over conditions only.
   **Blocked by:** none
   **Acceptance condition:**
   The files in scope are these six. The five worker contracts are `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md` and `.claude/skills/expedition-implementation/SKILL.md`. The sixth is the manager's contract, `.claude/skills/expedition/SKILL.md`.
   The scope came from a search. `grep -n -F "search the open nodes' \`## Acceptance condition\` sections for what your" .claude/skills/*/SKILL.md` returned exactly the five worker contracts, and `grep -n -F "It searches the open nodes' \`## Acceptance condition\` sections" .claude/skills/expedition/SKILL.md` returned the manager's contract. An instance the same searches reach outside these six files is reported and not edited.
   After this work:
   - (a) In each of the five worker contracts, the paragraph beginning "Before you write your handover, search the open nodes' `## Acceptance condition` sections" also tells the worker to search the open nodes' `## Question` sections. It uses the same handles: each word its work refuses, each path it changes or moves something out of, and each phrase it supersedes. It covers every open node, claimed or not, and the worker reads only what matches.
   - (b) In each of those five contracts, the handover's `CONDITIONS` part, or a part placed beside it, asks the worker to name the open nodes whose `## Question` its work changes (a renamed term, a part answered, or the node made unnecessary) and to say how.
   - (c) In `.claude/skills/expedition/SKILL.md`, the paragraph beginning "Before a party hands back a fact it established" says three things. The search also covers the open nodes' `## Question` sections. The manager updates an unclaimed node's question in place with the old wording marked, per graph-conventions.md's rule for an open, unclaimed node whose question has only changed. Where no party established the fact, the manager does that search.
   - (d) Each of the six files states that a question naming a thing in different words from the change's will not match, and that this is accepted.
   - (e) No file under `.scratch/` is changed.
   - (f) Every heading in each of the six files, as listed by `grep -n '^#\{1,6\} '` before the work, is still present afterwards, in the same order.

2. **Name:** The cascade's per-candidate agent does not join a defect to an open node
   **Kind:** implementation
   **Question:** The cascade contract that landed as `c64a0e3` has its per-candidate agent report a new node for every departure it finds. It carries no rule that a defect in the same file and on the same concern as an open node joins that node. The five worker contracts carry that rule, since node 327. A cascade-found defect would therefore be minted as a new node, against the effort's standing rule that a related defect goes into a node that already exists.
   **Blocked by:** none
   **Acceptance condition:**
   `.claude/skills/expedition-cascade/SKILL.md` is changed. Scope came from no search: the named file is the work.
   After this work:
   - (a) The per-candidate role tells the agent this: before reporting a node, search the open nodes' `## Acceptance condition` sections for the path the defect is in, and read only what matches. Where the defect concerns the same file and the same concern as an open implementation node, name that node and give the clauses to add to its acceptance condition, instead of reporting a new node.
   - (b) The per-candidate handover's shape has a place for that joined node and its clauses.
   - (c) Those clauses are held to the same points the file already states for a condition under `### The acceptance condition you write`.
   - (d) No file under `.scratch/` is changed.
   - (e) Every heading in the file, as listed by `grep -n '^#\{1,6\} '` before the work, is still present afterwards, in the same order.

INVALIDATIONS:
- **Node 15 (Cascade pass mechanics): extension and narrowing.**
  - Part 2's *"Open-node targets are not settled, and stay where they are"* is now settled. Open nodes' conditions get part 1's mechanism by node 263, and their questions by this node.
  - Its ground, *"no index reaches an open node"*, is false for both conditions and questions.
  - Its *"sharpening an unstarted node's acceptance condition … stays with the manager for now"* is spent. The shipped manager contract's amendment rules and node 327 moved it.
- **Node 263: extension.** Its handle search now also runs over `## Question` sections. Its residual, the synonym case, is inherited here unchanged and still unsolved.
- **Node 87 (open): its fourth duty is superseded.** See CONDITIONS.

CONDITIONS:
**What I searched for.** I searched every open or claimed node's `## Acceptance condition` section for these handles: `stay manual`, `open-node`, `Open-node`, `## Question`, `search the open nodes`, `what your own work fixes`, `` Acceptance condition` sections ``, `CONDITIONS`. None matched. I also searched for the paths the new nodes touch: `expedition-cascade` (no match), `expedition-grilling/SKILL.md` and `expedition-research/SKILL.md` (node 41, the friction flag, a different concern), and `expedition/SKILL.md` (node 89, the worktree lifecycle, a different concern). So no join applies.

**Replacement for node 87 (open, unclaimed).** Node 87's condition requires *"each of the five duties above"*, a pointer into its own `## Question`. The fourth of those duties is now wrong. Its replacement, to stand in node 87's question and be copied as text into its condition:
> "Open-node targets need no pass. Before a party hands back a fact it established, it searches the open nodes' `## Acceptance condition` and `## Question` sections for what its own work fixes, and reports the conditions and questions that fact makes wrong. The manager files the replacement conditions and updates an unclaimed node's question in place, old wording marked. Where no such party exists, the manager does the search."

What fixed its words: the conditions half is fixed by the shipped `.claude/skills/expedition/SKILL.md` (the paragraph beginning "Before a party hands back a fact it established") and node 263. The questions half is fixed by this node, 272. "Update in place, old wording marked" is fixed by the shipped `graph-conventions.md`'s Supersede section.

A side remark, not a replacement: node 87's condition points at its own question for the five duties rather than copying them, which the self-containment rule forbids. It already says it is incomplete, pending the human's choice of file.

MISSING FROM MAP: none

RETROSPECTIVE:
1. **What I had to hunt for.**
   - Whether "annotations" on open nodes were a real thing. They are not: graph-conventions.md's `### ## Annotation` defines one as a change to an answer. I found that by grepping the shipped files, after the node's question listed annotations as a live class.
   - Where the shipped search duty sits in each contract. I found it with a grep for the sentence.
   - Whether node 44's landed file carries the join rule. It does not; I grepped for "join" and "open node".
2. **What arrived that this node did not need.**
   - Most of `map.md`: the worktree, landing, retrospective history and glossary-count paragraphs bore on nothing here. Only the "nodes are grouped by file" bullet and the standing preferences mattered.
   - Node 263's answer read whole, where the "How this divides with the cascade" subsection would have done.
   - The first read of `map.md` spilled to a file at 46KB because I combined it with the decisions grep. Reading `map.md` alone, then narrowing the grep, avoided that.
3. **What would have made this easier.**
   - The node file could have said that condition-sharpening had already been shipped since node 15 (by the manager contract's amendment rules and node 327). That would have saved deriving it.
   - The spawn's note that node 87's condition quotes "open-node targets stay manual" was the most useful pointer. A pointer to the exact shipped paragraph ("Before a party hands back a fact it established", in `expedition/SKILL.md`) would have saved a search.
4. **What was stale, wrong or contradictory.**
   - The node's question treats annotations as an open-node class, which graph-conventions.md contradicts.
   - Node 15's "sharpening stays with the manager for now" is stale against the shipped manager contract.
   - Node 87's question still lists "open-node targets stay manual" as a settled duty.
   - The spawn said node 44 was uncommitted in a worktree. It had since landed as `c64a0e3`, which the manager corrected in its resume note.
   - One slip of my own: I wrote two scratch files for the measurement into `$TMPDIR` (`/tmp/claude-1000/q.txt` and `c.txt`), which is outside what this contract allows (it says write no file).

## Flags

`272.1` `ASSUMPTION` **· settled** — I settled three of the four sub-items of part 2 myself, from the shipped files, and did not put them to the human. Sharpening a condition has already moved: the manager contract's amendment rules and node 327 both ship it. Blockers are covered by graph-conventions.md's Supersede step that repoints inbound edges. Annotations do not arise, because graph-conventions.md defines an annotation as a change to a node's answer and an open node has none. Only the `## Question` half went to the human. — Node 272 settled that condition-sharpening, blockers and annotations needed no new part-2 mechanism, reading the shipped files, and asked the human only about open nodes' questions.

`272.2` `ASSUMPTION` **· settled** — I read *"the manager updates a claimed node's question as it decides"* as the same split the shipped manager contract already draws for conditions, where what to do about a claimed node stays the manager's. It is not a new permission to edit a question under a live worker. — Node 272 read a claimed node's changed question as the manager's to handle under the existing claimed-node split, granting no new permission to edit it under a live worker.

*The manager's note, 2026-09-27:* flags 272.1 and 272.2 settle at the node closing report that closes this node. The worker's own scratch files in `$TMPDIR`, which it reported, touched nothing in the record.
