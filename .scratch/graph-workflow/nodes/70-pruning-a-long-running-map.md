# Pruning a long-running effort's map

Type: grilling
Status: resolved

## Question

[Restructure `map.md` to what every worker needs](59-restructure-the-map.md) moved the map's append history into
`map-history.md` and cut every worker's map read by 71%. **It fixed the file workers read and created a file that
grows without bound.** `map-history.md` is already 87,768 bytes at 67 nodes; the dogfood target is 179.

### The human's instruction, `verbatim`

> *"We should add a node for cleanup of old data in the map for long running efforts"*

### Why node 59 does not already answer this, and why the answer cannot simply be "move it again"

Node 59 worked because there were **two readers with different needs** — a worker who must act, and a reader who
wants the account — so the split fell on a real seam. There is no third reader behind `map-history.md`. Anything
moved out of it is moved out of the effort's working files entirely, and that is a different act with a different
rule governing it.

**The rule is the never-delete preference**, and it is the oldest standing constraint in this effort: *when any file
in the graph is edited, nothing is deleted; the old text is marked in place and the new text is added around it.*
Node 59 satisfied it by moving text **verbatim** — the discharge was that all 106 before-state lines still existed
somewhere a reader could reach. **Pruning cannot make that claim**, so this node has to confront the rule rather
than route around it.

### The observation that probably decides it, offered as the manager's own and not as a finding

**Every graph file is committed, so nothing in them has ever been deletable in the sense the rule fears.** The
human commits the tracker periodically — `7d29001 periodic save of map` landed during node 59's run — so the
account of any line is in git whether or not it is in a working file. If the never-delete rule exists to keep the
record recoverable, **git already discharges it**, and the rule's real subject is what a *reader* meets in a file
rather than what exists at all.

If that reading holds, pruning is not deletion but **a change of where history is looked up**, and the question
becomes which material earns its place in a working file versus in `git log`. If it does not hold — because the rule
is also about not making a reader run git to understand a line — then pruning needs a destination and this is a
much larger node.

## What has to be decided

1. **What "old" means.** Node count, age, or the state of the thing described. The strongest candidate is
   **discharge**: an account of a preference that has since been superseded, or a fog item long since spent, has a
   different claim on a working file than a live item's history does. Node 59 already met this — it moved two
   **spent** fog items and flagged the judgement as `59.2`.
2. **Whether the never-delete rule reaches a file's own history file at all**, or is scoped to what a reader meets
   in `map.md` and the node files. Node 59's own fog item on this was narrowed to *"a node file's reader, not this
   map's"*, so the scope is already known to be narrower than it was written.
3. **Where pruned material goes**, if anywhere: git alone, a dated file, or out.
4. **Who runs it and when.** A sweep at close is the obvious hook and the wrong one for a *long-running* effort,
   which is the case the human named. A periodic manager pass is the alternative, and the manager is the party with
   the least context to spare.
5. **Whether the node files need the same treatment.** They are the larger corpus and nothing has measured them —
   this node should measure before assuming the map is where the growth is. Node 13's split was justified on a
   growth rate that turned out to be wrong, which is the cautionary case and is annotated there.

## What is already known, and worth not re-deriving

- **The growth is words per item, not items.** Measured at node 53 and annotated on [Graph file
  format](13-graph-file-format.md): `map.md` reached 92,113 characters while `decisions.md` stayed at one capped
  line per node. **A cap per item is what has actually held**, twice — `decisions.md`'s and node 59's 900-character
  fog items — and neither needed pruning to stay small.
- **That suggests the cheaper answer may not be pruning at all**, but a cap on `map-history.md`'s entries of the
  kind that has already worked twice in this effort. The human asked for cleanup; the manager notes the alternative
  because the two have very different costs and only one of them touches the never-delete rule.

## Where it came from

The human's own instruction, unprompted, alongside [Run an implementation node's work in a
worktree](68-implementation-in-a-worktree.md) and [Whether the workflow ships explicit subagent
definitions](69-explicit-subagent-definitions.md).

## Interview

### Attempt 1

**The worker's first payload carried two questions**, `Q1` and `Q2`, under the batching rule node 126 landed. Its
`SO FAR` reported measurements against this node's own premise, which the manager relayed in full.

**The human's first reply, `verbatim`.**

> I wasn't the one making the no delete rule, it was done by you but it's not a bad idea, which is why I approved it. It seems to be causing some issues ? With line count ? What do you think about it. For the action of doing the cleanup I would see like the stop skill, a cleanup skill. For the cleanup skill, it is designed to delete things so it should be fine.

***The manager's note.*** **Not an answer to either question**, and the manager did not read *"it's not a bad
idea"* as taking `Q1`. It carried three things: a **correction of attribution** — the never-delete rule is the
workflow's own and not the human's, recorded as an annotation on [node
189](189-where-the-never-delete-rule-stops.md); **a question back** to the manager about line count, which the
manager answered from measurements already in the record; and **a mechanism neither question offered**, cleanup as
an invoked skill on the model of [node 166](166-ship-an-expedition-stop-skill.md)'s stop skill.

**The worker withdrew `Q1` rather than re-asking it**, in its words: *"I put Q1 to you as 'your oldest standing
rule'. That was wrong and you were right to say so. I have now checked it myself: twelve of the standing
preferences in `map.md` carry your words marked `verbatim`, and the never-delete bullet carries none and cites no
node. It is the workflow's own rule. I withdraw Q1 — not because you refused it, but because it was built on that
premise."*

**It answered the human's question back with a measurement**, in its words: *"**No, and the number is not close.**
I measured every struck-through passage in the entire record: **6,252 bytes out of 3,600,256 — 0.17%.** In `map.md`
itself it is 1.13%. Across all 193 node files, 0.07%."*

**The human's second reply, `verbatim`.**

> Q3 ok. Q2. I see the cleanup more as a logical cleanup than just a text cleanup. In the idea, either the user choose or the skill finds part of the graph that is considered "done" and then if the effort needs to work on it again it is like the work that was already done was already shipped. For example in Lang, if after a while, the parser is considered done, we can remove the completed issues regarding the parser and if we later need to modify the parser we look at the code instead of looking at all the previous issues. The main source of truth at this point would be the code and documentation instead of using the map. In this idea then all files can be cleanup.

**What `Q3 ok` takes**, quoted from the worker's own re-asked payload and attributed to the worker:

> **RECOMMENDED:** It ships. *"Without it, every future effort's cleanup skill contradicts the rule stated two files
> away, and the manager or a worker re-derives the exemption each time. That is the identical defect node 189 was
> minted for."*

***The manager's note on `Q3`.*** **Not a divergence**, and it takes neither alternative — neither *stays in this
effort's map only*, nor *ships written as a property of the cleanup skill rather than as an exemption to the
never-delete rule*. **It is the second time in this session the human has shipped a boundary against the map's own
standing default** that a rule reaches a shipped file only where they say so, the first being node 189's `Q3`.

***The manager's note on `Q2`.*** **A reframing, not a choice among the three offered**, and it went back to the
worker rather than being read as taking any of them. **All three of the worker's candidates were classes of
text** — struck-through passages, spent fog, settled flag entries. **The human's unit is a subject area of the work
whose output has shipped**, and it cuts across every file at once: their words, *"either the user choose or the
skill finds part of the graph that is considered 'done'"*, and *"In this idea then all files can be cleanup."*
**It also asserts something about what the record is for**, which no question put to them: *"The main source of
truth at this point would be the code and documentation instead of using the map."* `Q2` stays unsettled and its
number is fixed.

**The worker's second re-ask carried `Q2` and a new `Q4`.** `Q2` kept its number per the rule node 126 landed. Its
`SO FAR` established that the human had already invented the unit their reframing needs — the `Labels:` field they
proposed unprompted at [node 13](13-graph-file-format.md), *"so that it is then possible to label all nodes that
are about a specific part of the problem"* — and that it is applied to **1 node out of 193**. It also measured that
**no severable region exists on this effort**: of 102 resolved nodes, exactly 3 are cited by neither a live rule
file nor an open node, and those 3 carry 1, 44 and 20 inbound links from nodes that would remain.

**The human's third reply, `verbatim`.**

> Q2. I don't plan on using it here, for the label, I think it is a way of doing it, I don't know if it will be always the case, for example, I don't think there are a lot of labels right now. So I expect it to be a bit more free-hand Q4. do cleanup flags

**What `Q4` takes**, quoted from the worker's own payload and attributed to the worker:

> **RECOMMENDED:** It carries it, as a second operation named separately in the skill. … It is the only cleanup I
> measured that has a real reader — `flags.md` is the one file your close-out sweep must read whole, and its own
> header says the report *is* the unchecked lines, so 68% of it contributes nothing to the only job it has.

***The manager's note on `Q4`.*** **Not a divergence**, and it takes none of the three alternatives — not a separate
skill, not a move to a sibling file, and not leaving `flags.md` alone. **It carries a reversal of [node
27](27-does-flags-file-survive.md), which the worker named before the human's standing direction on reversals had
arrived**, and which that direction now makes ordinary rather than exceptional.

***The manager's note on `Q2`.*** **It confirms the second half of the recommendation and does not take the first
half as written.** *"I don't plan on using it here"* settles that the skill does not run on this effort, which is
what the worker recommended. On the unit, their words are a direction rather than a selection: the label is *"a way
of doing it"* rather than the way, they are unsure *"if it will be always the case"*, they note there are few
labels today, and they expect it *"a bit more free-hand"*. **The manager has not read that as taking the first
alternative** — *you name the region free-hand each time and the skill does not try to find it* — because *"a bit
more free-hand"* is not the same as abandoning the finding half, and picking between them is the worker's. It went
back to the worker with that stated.

## Answer

*Pasted as the worker wrote it.*

> Cleanup is an **invoked act with two named operations**, not a standing practice, not a sweep, and not a rule
> about age. The human's words that fixed it: *"For the action of doing the cleanup I would see like the stop skill,
> a cleanup skill. For the cleanup skill, it is designed to delete things so it should be fine."*
>
> **Nothing is pruned from `map-history.md` as a class, and the never-delete rule was never the problem.** Measured
> across the whole record: struck-through text is **6,252 bytes of 3,600,256 — 0.17%**; 1.13% of `map.md`, 0.07%
> across the 193 node files. The rule this node was minted to confront costs a sixth of one percent. What made the
> map expensive was live prose accumulating in the one file every worker re-reads, and that has been repaired three
> times by *moving* text rather than deleting it — `map.md` went 92,113 → 26,971 → 43,847 → 28,964 and is 29,782
> today.
>
> **This node's own premise was falsified before it could be worked.** It was filed on *"87,768 bytes at 67 nodes;
> the dogfood target is 179"*. That rate extrapolates to ~253,000 bytes by now; the file is 110,517. **78% of it is
> a single frozen deposit from node 59 that has grown 1.7% in 126 nodes**, and real growth is 184 bytes per node.
> The 179 is also not this effort's node count — `map-manager-only.md` defines it as 179 gap labels in Lang. This
> effort passed it and the file did not blow up. This is node 13's cautionary case repeating, which this node's own
> item 5 had named.
>
> **`map-history.md` has no reader to save.** It appears on none of the five worker contracts' read lists; the
> shipped `graph-conventions.md` states its access mode outright — *"Read for history, not to work a node"*; and
> real reads occur in **10 of 193 nodes**, every one a node about the record's own structure. Cost is size ×
> re-reads: `map.md` is 29,782 × 193; `map-history.md` is 110,517 × ~10. **Node 189 therefore improves this rather
> than worsening it** — sending superseded rule text there moves it off the file read 193 times onto the file read
> ten times. Its growth is the mechanism keeping `map.md` flat.
>
> **The cap alternative this node proposed is dead, on four measured precedents.** A per-item cap bounds words per
> item and never bounds a file. `flags.md`'s one-sentence cap holds exactly (333 entries, average 319 bytes, largest
> 505) and the file is 108,900 bytes. `decisions.md`'s one-line cap holds and the file is 33,422, and node 129
> proved that cap lossy. Node 59's hard 900-byte cap was breached later and nothing caught it. Node 136's soft
> 500-byte target on `map.md`'s `## Notes` is missed by **18 of 30 items — 60%**, average 900, largest 3,541.
>
> **Item 5 is answered by measurement and needed no human.** The node files need nothing: 193 files, 3,273,210
> bytes, average 16,959. The last measurement (54 files) averaged 18,190 — **per-file size fell 8%.** Each is read
> by its own worker, so the corpus grows in count, which is the effort making progress, not bloat.
>
> ### The unit of a cleanup
>
> The human reframed cleanup from a class of text to **a subject area whose work has shipped**: *"either the user
> choose or the skill finds part of the graph that is considered 'done' ... if we later need to modify the parser we
> look at the code instead of looking at all the previous issues. The main source of truth at this point would be
> the code and documentation instead of using the map. In this idea then all files can be cleanup."*
>
> **They had already invented the mechanism for it.** At node 13 they proposed `Labels:` unprompted: *"so that it is
> then possible to label all nodes that are about a specific part of the problem"* — the same unit, two months
> earlier. **It is used on 1 node of 193**, which they observed back to the manager: *"I don't think there are a lot
> of labels right now. So I expect it to be a bit more free-hand"*.
>
> **So the two halves of their proposal do not share a unit, and that is the settlement.** A human naming a region
> needs no declared vocabulary; a skill *finding* one does. The unit is therefore **the region as the human names
> it, in their own words**, with the skill proposing the set of nodes it reads that to mean and the human confirming
> or amending it before anything goes. A label accelerates the proposal where one exists and is never required. This
> keeps the finding half useful today and lets it strengthen if labels are ever applied.
>
> **What does not loosen is the safety, because it is a property of the set rather than of how the set was chosen.**
> Three conditions, all mechanically checkable: every node in the set is resolved; nothing outside the set refers
> into it; and the human has confirmed it.
>
> **A region reaches every file of the record**, per their *"all files can be cleanup"* — including the part of
> `map-history.md` attributable to that region. This is the answer flag `189.3` left open: what may leave
> `map-history.md` is not a class of text and not the old, but **the share belonging to a region being removed**.
>
> **Node 189 is what makes this safe, and it landed a day before it was needed.** Its cut moved text stating a rule
> that currently binds out of the nodes and into the rule files. So a subject region now holds accounts and no live
> rules, and the failure this node feared — deleting the parser's nodes and losing a rule that bound the whole
> effort — is closed by construction rather than by care.
>
> **It does not run on this effort, on the human's word — *"I don't plan on using it here"* — and the measurement
> agrees.** 148 of 193 nodes are cited by a live rule file or a still-open node. Of the 102 resolved nodes, **3**
> are cited by neither, and those three carry 1, 44 and 20 inbound links from node files that would remain. There is
> no severable region in this graph: 1,280 node-to-node links, 111 of 193 nodes cited five or more times, and the
> most-cited are the oldest — nodes 10, 12, 8 and 13 at 82, 76, 73 and 70 citations, exactly the ones that would
> look finished first. **Lang is the better case and still not clean:** it has the 13 declared families, but 38 of
> its 179 gaps are cross-cutting `X-*`, a fifth of the corpus belonging to two areas at once.
>
> **On their claim that the code becomes the source of truth**, weighed rather than assumed: it holds for the
> artifact and is weakest for **measurements**. Node 129 recorded a fact three separate workers went looking for
> after its node had resolved, which survived only because that node's text was still there — an account, not a
> rule, so node 189 does not cover it. What makes this safe to get wrong is that every graph file is committed, so
> an announced removal that records where the text went is recoverable. That is the git observation this node was
> handed, and it belongs here — not as a licence to delete quietly, but as the reason judging "done" too early is
> cheap rather than fatal.
>
> ### The second operation
>
> **Settled flag entries are removed from the index, and this is orthogonal to regions.** Flags settle when their
> node closes, so `flags.md`'s **230 settled entries — 73,994 bytes, 68% of the file** — are spread across every
> region including live ones; a region cleanup would never reach them. It is the one cleanup measured on this effort
> with a real reader: `flags.md` is the file the close-out sweep must read whole, and its own header says the report
> *is* the unchecked lines. **Nothing is lost**, because the human ordered the duplicate themselves at node 22's
> gate — a settled flag is marked settled on its node too, *"so someone reading a node can see which of its
> judgements are still live without opening this file"*. Their word: *"do cleanup flags"*.
>
> ### What this node does not do
>
> No sweep, no schedule, no age criterion, no cap. **"Old" dissolves as a criterion**: on this record nothing is old
> enough for its removal to buy anything, and discharge-by-age would have selected the 0.17%. Node 191 reached the
> same shape independently and an hour earlier — repairs ride invoked work, never a sweep.

**What the worker reported its work invalidates**, pasted as it wrote it:

> **Node 27** — *"Whether flags.md survives the settle-at-close practice"*. It settled that `flags.md` *"stays: not
> a queue but the capped index of every agent judgement"*. The settled-flag cleanup reverses the permanent-index
> half: 230 of 333 entries become removable. The queue reading it rejected is what the file becomes. The human took
> this knowingly, under their own standing direction that discovery may make an earlier decision wrong. **What
> survives**: its other half, that the flag index is the counterpart to the decisions index, and that check 6
> compares both states — that comparison is amended rather than dropped.
>
> **`flags.md`'s own header** — it states *"**Append-only.** A settled flag is checked, never removed."* That is now
> false and is the operative text a reader meets. It is a rule statement in a graph file, so under node 189 it is
> replaced rather than struck, its old text banked to `map-history.md`.
>
> **This node's own file** — its `## What is already known` section states *"A cap per item is what has actually
> held, twice"*. Measured, two of the four caps have not held: node 59's 900-byte cap was breached at 1,343
> uncaught, and node 136's 500-byte target is missed by 60% of items. Its `## Question` states *"the dogfood target
> is 179"* as this effort's node count; it is 179 gap labels in Lang.
>
> **Not invalidated, and worth saying so.** Node 189 is confirmed and extended rather than contradicted: its flag
> `189.3` deliberately left this node the question of what leaves `map-history.md`, and its rule/account cut is what
> makes region removal safe. Node 191 is agreed with independently — no sweep.

## Flags

*All five are the worker's own text, pasted. The ids are the manager's bookkeeping and nothing else.*

`70.1` **· settled** `ASSUMPTION` — **I settled the unit rather than asking a fourth time.** The human said the
label was *"a way of doing it"*, that they did not know *"if it will be always the case"*, and that they expected it
*"a bit more free-hand"*. I read that as loosening how a region is *selected* and not how it is *checked*, and split
their own *"either the user choose or the skill finds"* into two halves needing different units — free-hand naming
for the choosing half, a declared label only for the finding half. Ground: my own measurement that labels are on 1
node of 193 makes a label-only rule one that cannot fire, and they stated that same fact back at me. What I did not
put to them is whether a propose-and-confirm step is more machinery than they want; it is one message at
invocation, and it is what makes the three safety conditions enforceable at all.

`70.2` **· settled** `ASSUMPTION` — **I read "all files can be cleanup" as reaching `map-history.md` region by
region, and it is the answer to flag `189.3`.** That flag left "what may leave that file at all" to this node. I
answered: nothing as a class — not by age, not by struck-ness, not by discharge — but the share attributable to a
region leaves with its region. Ground: any other reading either exempts one file from a rule the human said reaches
all of them, or licenses a class-based prune the measurement says is worth 0.17%.

`70.3` **· settled** `ASSUMPTION` — **I withdrew my own Q1 rather than re-asking it.** It asked whether `git log`
discharges the never-delete rule, and it was built on the premise that the rule was the human's, which they
corrected. I withdrew it on two grounds: their cleanup-skill proposal reframes the question from *whether the text
still exists* to *whether the removal was announced*, which is what the rule's own text names as its harm; and my
measurement of 0.17% means there is no saving to buy with a relaxation. The recoverability half survives inside the
answer as what makes an announced removal safe.

`70.4` **· settled** `ASSUMPTION` — **I answered the node's item 5 by measurement instead of putting it to the
human.** It asked whether the node files need the same treatment and recorded that nothing had measured them. They
are 193 files at 3,273,210 bytes, averaging 16,959 against 18,190 at the last measurement — per-file size is
falling, and each file is read once by its own worker. Ground: the node asked for a measurement, not a preference.

`70.5` **· settled** `ASSUMPTION` — **I blocked the cleanup skill node on the conventions node.** The settled-flag
operation makes the graph fail the shipped mechanical check that joins a node's flag entry to its index line, so
shipping the skill first would produce a graph failing a check the same workflow ships. Ground: that is the defect
node 189 was minted for. The cost is a longer chain (142 → 194 → conventions → skill) and the manager may judge the
sequencing differently.

***The manager's note.*** **All five are settled by the human's answers at this node's own interview**, that being
the first human moment this node's close reached. **Four of the five are the worker declining to spend a human
question**, three of them on grounds it measured rather than argued.
