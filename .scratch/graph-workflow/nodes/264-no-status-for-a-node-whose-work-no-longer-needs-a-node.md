# The graph has no status for a node whose work no longer needs a node

Type: grilling
Status: resolved

Blocked by: none

## Question

*Surfaced by [node 252](252-may-an-unclaimed-nodes-acceptance-condition-be-amended.md)'s worker, and pasted as it
wrote it.*

> Nodes 203 and 245 exist only to amend another unclaimed node's acceptance condition, which node 252 now permits
> directly. Neither should be worked, and neither has a status that says so. `out-of-scope` means the work is beyond
> the destination, which is false — the work is wanted and is simply no longer a node's worth of it. `superseded`
> requires the node to hold work and requires a replacement node to point at, and these hold none and have none.
> Leaving them `open` leaves two nodes on the frontier that nobody should take. What this decides: whether a sixth
> status exists, or whether such a node is disposed of some other way, and what happens to anything listing it in
> `Blocked by:`. Small and low-priority; it has two live instances and no more.

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**The two instances are live on the frontier right now**, [node
203](203-node-155s-condition-preserves-a-contradiction.md) and [node
245](245-node-156s-condition-re-derives-a-weaker-property.md), and the manager has not touched either. Standing them
down is the manager's by node 252's own words, and the manager is not inventing a status in order to do it.

**One thing the manager holds that the question does not name**: node 203's own acceptance condition is *itself*
falsified, by node 199, which is the fact node 252's worker found. So node 203 is simultaneously an instrument that
is no longer needed and an instance of the disease it was built to cure. Whichever disposal this node settles has to
be right for a node in that state.

## Interview

### Attempt 1 — the question put to the human

*Pasted as the worker wrote it. **No answer has arrived** when this was written. Banked here so that a death leaves
the worker's work on disk.*

**ABOUT:** Five nodes on the graph should never be worked, and no status says so — so they sit on the frontier where
anyone may take them, and an effort is only done when its frontier empties. This decides whether a sixth status is
invented, or the supersession the graph already has is widened to cover them.

**SO FAR:** I read the node, `map.md`, `graph-conventions.md`'s statuses/edges/procedures/checks, `SKILL.md`'s word
list, grepped `decisions.md`, then each of the five instances and the two nodes that killed them.

Two facts decided the shape, and I went looking for both: **every one of the five has a live node to point at** (203
→ 252, 245 → 252, and 261/262/250 → node 268, which is claimed and under work right now), and **no node anywhere
lists any of the five in `Blocked by:`**.

**The five are one shape with four different causes.** Each must leave the frontier, satisfy no edge, and tell its
reader where to go instead:

- **203** and **245** — the work is still wanted; under node 252 the manager now does it directly, with no node at
  all.
- **261** — its subject, the `EnterWorktree` call, left the route at node 265. Nobody does that work anywhere.
- **262** — its condition demands that no two sentences in one file collide over a worker's "first act". Node 268
  deletes one of the two, so the condition goes vacuously true and nothing is left to do. (What survives is a wish —
  that the remaining sentence say what it is first *relative to* — which nobody ever fixed as a demand. I'd record
  that on the supersession so it isn't lost.)
- **250** — different: finished, checked twice, committed to branch `worktree-250-worker-reaches-its-worktree`,
  parked by you at its gate. Its subject is the worker's half of the route node 265 replaced.

Settled on my own authority: that these are one question rather than several; and that my answer **does** reach node
250 — it is the one of the five that already qualifies under the rule as written, holding an interview, two review
runs and a commit.

**ASK:** Should the graph gain a sixth status for a node that should not be worked — or should `superseded` be
widened to cover it, dropping its requirement that the node hold work, so the discriminator becomes *does this node
still need to exist?* rather than *has anyone started it?*

**RECOMMENDED:** Widen `superseded`. Invent no status.

- The status reads: *replaced **or made unnecessary** by other nodes. Does not satisfy an edge.*
- The `Supersede` procedure opens: *use when the node is no longer the place its work happens — because another node
  replaces it, or because another node's answer or landing means it no longer needs doing.* The in-place branch
  keeps the case it was written for: a node whose **question** changed but which still needs to exist.
- Two consequences I'd rather state than have you find. `Supersedes:` must become multi-valued (`Supersedes: NN[,
  NN]`) — the spec says "one number" today, and node 268 would supersede three at once. And standing node 250 down
  **reverses your park of it**, which is why it is in front of you rather than simply done.

What it rests on: the `Blocked by:` half is the part of my node's question with teeth, and only supersession answers
it — step 4 of the existing procedure already repoints a dependent at the replacement, and mechanical check 1
already catches a missed one. A new status would need every bit of that written from scratch. Meanwhile the one
thing a new status could carry that `superseded` cannot — *nothing replaces this* — has **zero instances** across
all five. Inventing it is machinery for a predicted need, which this map's standing preference refuses by name; if a
pointerless instance ever turns up, minting the status then costs exactly what minting it now costs.

**ALTERNATIVES:**

- **A sixth status** (`withdrawn`, `dropped`): honest, but buys a distinction with no instances, and leaves the
  `Blocked by:` consequence unwritten — a status is not an edge, so a dependent has nothing to be repointed at.
- **Reuse `out-of-scope`**: its mechanics fit exactly, but its procedure files the node under
  `map-manager-only.md`'s `## Out of scope`, which states what this effort *declines* — and it declines none of
  these five. A manager reading that list later would be misled; against your own preference for an honest empty
  word over a rich misleading one.
- **Leave them `open` with the question amended to say "do not take this"**: they stay on the frontier, so it never
  empties and the effort can never reach done under node 10.
- **Delete the node files**: refused by never-delete, which names `nodes/` explicitly, and the gap would surface in
  mechanical check 3.

#### The human's answer

*Their reply on 2026-09-19, `verbatim`:*

> ok

**The option it takes**, quoted so the reply is attributable to exactly one thing. It is **the worker's
`RECOMMENDED`**, written by the worker and not by the manager:

> **Widen `superseded`. Invent no status.** The status reads: *replaced **or made unnecessary** by other nodes. Does
> not satisfy an edge.* The `Supersede` procedure opens: *use when the node is no longer the place its work happens
> — because another node replaces it, or because another node's answer or landing means it no longer needs doing.*
> The in-place branch keeps the case it was written for: a node whose **question** changed but which still needs to
> exist.

**No divergence**: the answer agrees with the recommendation.

***The manager's own note, beside their words and not part of them.*** **The answer carries a reversal of the
human's own act and the worker put it in front of them rather than in a footnote**: standing node 250 down reverses
the park they made at its gate earlier today. Their assent reaches it because the worker said so in the same
payload — *"which is why it is in front of you rather than simply done"* — and because the worker had already
settled, and stated, that its answer reaches node 250. **The manager has not stood any node down**; that is work,
and the worker was resumed to write the answer and hand back what it needs.

The manager did not ask which option *"ok"* pointed at, on the same ground as at nodes 252, 263 and 265: **only one
of the five is an assent**, and each `ALTERNATIVE` is a named refusal of it.

## Answer

*Written by this node's worker and pasted as it wrote it.*

> **No sixth status. `superseded` is widened to reach a node that should not be worked: its "holds work" gate is
> dropped, and the discriminator becomes whether the node still needs to exist rather than whether anyone started
> it.** The human's words settling it, `verbatim`: *"ok"*, taking the recommendation whole against four named
> alternatives, each of which refused it. Not a divergence.
>
> ### The rule
>
> Three statements change. Nothing else in the revision semantics moves.
>
> - **The status.** `superseded` — *replaced **or made unnecessary** by other nodes. Does not satisfy an edge.*
> - **The procedure's trigger.** `Supersede` is used when the node is no longer the place its work happens — because
>   another node replaces it, or because another node's answer or landing means it no longer needs doing. The
>   in-place branch keeps the case it was written for: a node whose **question** changed but which still needs to
>   exist.
> - **The edge's arity.** `Supersedes: NN[, NN]` on the replacement, matching `Superseded by:`. **This is a change to
>   the graph's file format and not to a status definition**, and it is here because the format cannot otherwise
>   express what the rule needs: node 268 supersedes three nodes at once and node 252 supersedes two, while [node
>   13](13-graph-file-format.md) fixed `Supersedes:` at one number. The one-number form was written for
>   one-old-to-many-new and never contemplated many-old-to-one-new.
>
> ### Why no new status: every instance has somewhere to point
>
> The thing a sixth status would carry that `superseded` cannot is *nothing replaces this*. **It has no instances.**
> All five nodes this was minted over have a live node to point at:
>
> | node | superseded by | why it no longer needs a node |
> |---|---|---|
> | 203 | 252 | the work is still wanted; under node 252 the manager does it directly with no node, and node 252's own answer table already accounts for node 155's clause 4 |
> | 245 | 252 | the same, for node 156's clause 5 |
> | 261 | 268 | its subject, the `EnterWorktree` call, left the route at node 265; nobody does that work anywhere |
> | 262 | 268 | its condition demands clarification only where two sentences collide over a worker's *"first act"*; node 268 deletes one of the two, so the condition goes vacuously true |
> | 250 | 268 | finished, checked twice, committed and unlanded; its subject is the worker's half of the route node 265 replaced |
>
> **The precedent is the graph's own.** Node 13's naming annotation already considered a retirement status — Lang's
> hand-written `RETIRED` — and refused it: *"the two are different concepts, and this design already has
> `superseded` for the second."* `superseded` has been the graph's retirement mechanism since the format was fixed.
> This answer removes the gate that kept it from reaching cases it was already meant for.
>
> ### The `Blocked by:` half was already answered, and nothing new is owed
>
> **Two existing statements answer it and neither changes.** The `Supersede` procedure's step 4 repoints every
> dependent at the replacement, listing all of them where there are several; [node
> 06](06-revision-semantics.md) states the same and adds that *"a `Blocked by` pointing at a superseded node is an
> **error, not a satisfied edge**"*, which mechanical check 1 already catches. The glossary's *"everything blocked on
> it stays blocked"* also stays true: a dependent repointed at an unresolved replacement is still blocked, correctly,
> until that replacement resolves.
>
> **Today there is nothing to repoint.** No node in the graph lists 203, 245, 250, 261 or 262 in `Blocked by:` —
> searched across every node file.
>
> ### A node may be superseded on a replacement that exists and has not landed
>
> Node 268 is claimed and unlanded; node 250's own work is committed to a branch and not on `master`. **The existing
> rule already decides this, and decides it correctly**: the procedure requires that *"the replacements exist before
> the old node is marked `superseded`"* — the replacement **node**, not its landed work. Waiting for the landing
> would leave 250, 261 and 262 takeable on the frontier for the whole duration of node 268, which is the exact harm
> this node exists to stop.
>
> The bookkeeping is already right for an unlanded replacement: a dependent repointed at it stays blocked until it
> resolves. And the move is cheap to undo if node 268 is rejected — a superseded node's text stays where it is under
> never-delete, so re-minting from it costs one new node and nothing else.
>
> ### Node 250: the supersession came second, and on the human's word
>
> Node 250 was **parked by the human at its gate on 2026-09-19**, and is superseded later the same day on their
> *"ok"* to a payload that named the reversal of that park as a consequence of the recommendation. **The reversal is
> theirs, taken knowingly, and is not the manager's act.** A reader meeting a park and a supersession on one node
> reads them in that order.
>
> It is also the one of the five that qualified under the rule **as written**, holding an `## Interview`, two
> `## Review` runs and a commit — work by any of the three tests. What the widened rule adds for it is only the
> reason: it is superseded because the route it documented was replaced, not because it asked the wrong question.
> **What is not settled here is the branch**, which is reported as a node.
>
> ### What node 262 loses, measured rather than assumed
>
> Node 262's condition goes vacuously true once node 268 lands. What it asked for beyond that is one phrase: that the
> surviving `map-manager-only.md` fog item saying *"a worker's first act is to read its own node"* state what it is
> first relative to.
>
> **That residue does not warrant a node, and the measurement is the reason.** `grep -rn "first act\|first thing"
> .claude/skills/expedition*/ .scratch/graph-workflow/map-manager-only.md` returns **exactly one line** — that fog
> item. No shipped worker contract uses the phrase at all, so the third and fourth claimants node 262's question
> named are the manager's spawn text, which lives in no file. One uncontested phrase, used as a premise inside a fog
> item rather than as a binding rule, harms nothing. Minting a node for it would be machinery for a predicted need,
> which is the argument this answer is built on. It is recorded here so that it is not lost.
>
> ### Who performs this
>
> - **The manager's bookkeeping**, needing no node: superseding the five per the procedure — `Supersedes:` on 252
>   and 268, `Superseded by:` on each of the five, `Status: superseded`. Nothing is written to `decisions.md`; none
>   of the five ever resolved, so none has a line to strike.
> - **One implementation node**, because **six statements in three shipped files** carry the gate this answer drops
>   and no worker may edit them by hand: `graph-conventions.md`'s `## Statuses` entry, its `## Edges` arity and its
>   `### Supersede` trigger; `SKILL.md`'s word-list entries for **supersede** and **revision**; and `CONTEXT.md`'s
>   **Supersede** and **Revision** entries.

**The index line the worker wrote:**

> No sixth status: `superseded` widens to a node made unnecessary rather than replaced, its holds-work gate dropped
> and `Supersedes:` made multi-valued; five nodes stand down.

## Flags

*All four are the worker's own text, pasted.*

`264.1` `ASSUMPTION` **· settled** — Read the five instances as one question rather than several, without asking. The spawn made
establishing this part of the work and offered no default. They have four different causes — work migrated to the
manager (203, 245), subject removed from the route (261), condition gone vacuously true (262), and finished work
obsoleted before landing (250) — but one consequence each: leave the frontier, satisfy no edge, carry no answer,
point somewhere. I decided that the consequence is what a status names and the cause is not, so one rule covers all
five. **If the completed-and-obsoleted case was to be held separate, this is where it was merged.**

`264.2` `ASSUMPTION` **· settled** — Decided that this answer reaches node 250, which the spawn left to me and asked me to state
either way. Ground: node 250 already qualified for `superseded` under the rule as written, holding an interview, two
review runs and a commit, so excluding it would have made this answer narrower than the rule it widens. What I did
not decide is the fate of its branch.

`264.3` `ASSUMPTION` **· settled** — Held the node-250 branch question out of the payload rather than numbering it as a second
question. The contract permits a payload to carry several independent questions and this one was independent;
`map.md`'s standing preference that exactly one question is in front of the human, and the human's two recorded
corrections about stacked questions, decided it the other way. **The cost is that the branch's disposal waits for a
fresh node rather than riding this exchange.**

`264.4` `ASSUMPTION` **· settled** — Discharged node 263's duty by searching the open and claimed nodes' `## Acceptance condition`
sections for the handles this work changes, and chose the handle list myself: `superseded`, `Supersedes:`,
`out-of-scope`/`out of scope`, plus `statuses`/`five status`, `Blocked by` and `graph-conventions`. **Result: nothing
breaks.** Almost every hit uses *superseded* in the never-delete sense — text marked superseded in place — which this
answer does not touch. Two conditions enumerate headings rather than text and both survive, this work adding and
removing none: node 79's clause 8 and node 111's clause 13. **The residue is file-exclusivity sequencing, not
breakage**: nodes 41, 43, 49, 55, 73, 79, 109, 111, 120, 146, 148, 153, 190, 195, 201, 206, 228, 230 and 233 all
edit `graph-conventions.md`, and several demand it change *in no other respect*, so two workers must not hold it at
once.

## Invalidations

*The worker's own text, pasted.*

> - **[Node 06](06-revision-semantics.md) — Revision semantics.** Its first branch reads *"Not yet started — open,
>   unclaimed, no answer, no landed code → **update in place.** … Supersession exists to preserve work; where there
>   is none, a replacement node is pure noise."* **Narrowed rather than reversed.** Its ground holds where a
>   replacement would have to be **minted**, and is false where one already exists — which is every one of the five
>   instances here, none of which minted anything. Supersession also exists to *point*, and pointing is worth most
>   exactly where there is no work to preserve. Its second branch widens to cover a node that is neither. Node 06 is
>   `resolved` and holds work, so whether this is an annotation or a supersession is the manager's call; the change
>   is narrow enough that I would annotate.
> - **[Node 13](13-graph-file-format.md) — Graph file format.** Its answer states *"`Supersedes: NN` on the
>   replacement (so 'is this a revision?' is a local read)"* as a single number. It is now `Supersedes: NN[, NN]`.
>   The stated purpose survives untouched — the read stays local. Node 13 is `resolved`; its annotation also lists
>   `Supersedes:` among the names confirmed unchanged, which remains true of the name and not of its arity.

## Retrospective

*The worker's own text, pasted. Condensed by the worker itself; nothing of its four sections is omitted here.*

> **1. What I had to hunt for.** **Whether every instance has a node to point at** — the fact the whole answer turns
> on. Nothing in the spawn or the node file had it. I looked first in node 265's `## Answer`, which was the wrong
> place; it is in its `## Nodes surfaced`, which says node files were minted for none of the three. **That is
> false**, so I then listed the directory and read the headers of nodes 266–272 to find node 268 `claimed`. A
> one-line annotation on node 265 saying which numbers its three surfaced nodes became would have removed the
> largest single hunt in this node. **Whether anything lists the five in `Blocked by:`** — one grep; the spawn called
> this *"the part with a consequence"* without telling me it has zero live instances, which is the cheapest possible
> fact to have included. **The `Supersedes:` arity** — found only by reading `## Edges` after I had settled my
> recommendation; had I written the answer from the `### Supersede` procedure alone, **I would have shipped a rule
> the file format cannot express.** **The `RETIRED` precedent** at node 13, the strongest single support for the
> recommendation, found incidentally.
>
> **2. What arrived and this node did not need.** **`map.md` in full** — a seventh worker reporting it; I used two
> items of roughly thirty. The retrospective item itself runs ~1,500 words to deliver four questions the spawn
> already restates; **everything before *"The four questions, as the spawn puts them"* is account rather than rule
> and belongs in `map-history.md`.** `graph-conventions.md` lines 330–500 — grepping headings first bounded it to
> one read, which is the right arrangement. **Node 252's answer at full length** — I needed two facts and both are
> in the table at its end. **The spawn's framing of node 262 as *"shrunk rather than dead"*** — a reasonable read
> that was wrong, and I spent effort reconciling it before concluding the condition goes vacuously true. The spawn
> marked it as material rather than instruction, which is what let me discard it; **a spawn that says *check this*
> costs less than one that says *this is the shape*.**
>
> **3. What would have made this easier.** In the spawn: **naming node 268.** The manager minted it this session and
> it is the replacement for three of the five. In the record, and it is the real finding: **supersession is stated
> in six places across three shipped files and not one of them says the other five exist.** Bounding this node's
> implementation scope meant finding all six by hand. This is the same complaint nodes 190 and 233 are already
> about, now with a seventh instance. In the contract: nothing.
>
> **4. What was stale, wrong, or contradicted something else.** **Node 265's `## Nodes surfaced` states *"The
> manager has minted node files for none of them yet"*. All three are minted** — 268, 269, 270 — and this cost me
> the hunt in (1). **`CONTEXT.md`'s Revision entry and `SKILL.md`'s state two different tests, and always have**:
> the glossary says *"Handled in place while the node is **unstarted**"*, `SKILL.md` says *"while the node **holds
> no work**"*. Those are different sets, and nothing recorded the divergence; the glossary's own entry is
> internally mismatched too. This answer removes both formulations, so it stops mattering. **Node 203's annotation
> ends *"this node and node 245 are its two live instances"*. There are five** — a record of what was true when
> written, so not a defect, but a reader lands on a count out by three.
>
> One contract note, outside the six parts: **I did not invoke `mattpocock-skills:grilling`**, which `map.md` lists
> as a default consult. Nothing in it was needed — the discipline, the payload shape and the reply-reading rules are
> all in my contract, and the map's own standing direction is that shipped files should not depend on that plugin.

## The manager's disposal

*Not the worker's text.*

- **Node 265's `## Nodes surfaced` saying no node files were minted** → **the manager's own stale text, and it cost
  this worker its largest hunt.** It was true when written and false within the hour. **Annotated on node 265**
  rather than left, because the worker's evidence is that a reader goes there for exactly this.
- **The two implementation/grilling nodes the worker surfaced** → **minted** as [node
  274](274-carry-the-widened-supersession-into-the-shipped-files.md) and [node
  275](275-node-250s-finished-work-is-on-a-branch-nothing-will-land.md), each carrying its author's own text.
- **Superseding the five is the manager's bookkeeping and is NOT yet done.** It waits on nothing, and the manager is
  recording that it is owed rather than doing it silently at the next convenient moment.
- **Supersession stated in six places across three shipped files, none naming the others** → nodes 190 and 233 hold
  the general complaint; this is the seventh instance. **Named for the human.**
- **`map.md`'s retrospective item being ~1,500 words of account for four questions** → **not minted**: it is a
  `Change the map` on a paragraph the human's own standing instruction owns. Third report.
- **The spawn asserting node 262 was *"shrunk rather than dead"*** → the manager's own framing, wrong, and marked as
  material which is what let the worker discard it. **Not filed as a flag**: the worker reports the marking worked
  here, where at `263.4` it did not. That difference is worth the human's eye and is named for them.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
