# Nothing tells the party that falsifies an acceptance condition to go and look for it

Type: grilling
Status: resolved

Blocked by: none

## Question

*Surfaced by [node 252](252-may-an-unclaimed-nodes-acceptance-condition-be-amended.md)'s worker, and pasted as it
wrote it.*

> Node 252 gives the party that establishes a falsifying fact the pen to repair the clause, and creates no duty to
> go looking for one. So the permission fires only where somebody notices by accident. Node 112's worker found node
> 111's condition, `verbatim`, *"by luck rather than by instruction"*, and named the cheap form the duty would take:
> *"before refusing a word, grep the open nodes' `## Acceptance condition` sections for it."* Nodes 152 and 203 were
> found by node 252's worker on a search nobody asked for, and nobody had found node 203's at all. What this decides:
> whether the duty exists; whose it is — the falsifying node's worker, or the manager at the moment it resolves that
> node; how wide it reaches, since a word is greppable and *"node 188 moved a section"* is not; and whether it ships
> or binds this effort only. **Adjacent and deliberately not merged:** the shipped manager contract's own open
> question 5, *"Does anything tell a worker to go and look at the record when it reports what its work invalidates?
> Nothing does"*, is the same hole one level up — this is its sharpest instance and is worth deciding on its own,
> because a condition on an unclaimed node blocks work where a stale decision merely misleads.

**Blockers, in the worker's words:** *"none. Node 252 is resolved and is its only input."*

## The manager's note at filing

*Not a change to anything above.*

**This is the residual node 252's own answer names**, and its author wrote it as such rather than as a defect found
elsewhere: the permission is granted and nothing makes anybody look. **Two of the four instances node 252 reaches
were found by an unasked-for search**, and one of them — node 203's — nobody had found at all in the time it had
been wrong.

**The manager holds one thing bearing on the "how wide" fork and offers it as material rather than as a position**:
of the four instances, exactly one is greppable. Node 111's turns on a refused word. The other three turn on a
*decision* — a section moved, a demand sharpened, a banking route reversed — and no string search finds those.

***Annotated by the manager after the worker reported.*** **The paragraph above is wrong, and the worker measured
it.** It is greppable for all four — not by the refused *word*, but by the **path each change touches**. The
manager reasoned from one handle where there are two.

## Interview

### Attempt 1 — the question put to the human

*Pasted as the worker wrote it. **No answer has arrived** and the payload had not reached the human when this was
written — [node 265](265-should-the-worktree-route-drop-enterworktree-for-git.md)'s question is the older of the
two waiting. Banked here so that a death leaves the worker's work on disk.*

**ABOUT:** You agreed today that whoever establishes a fact which makes an unclaimed node's acceptance condition
wrong may repair that clause themselves. Nothing makes anybody *look*, so that permission only fires when someone
trips over the damage by accident. This decides whether a duty to look exists, whose it is, and how far it reaches.

**SO FAR:**

**What is broken today.** Four acceptance conditions on the graph are currently wrong. One was found by luck. Two
were found by a search nobody had asked for. The fourth — node 203's — nobody found at all in the time it had been
wrong; it surfaced only because someone was hunting for something else.

**The worry, and why it looked expensive.** Only one of the four is findable by searching for a *word* (node 111's,
where a word was banned outright). The other three were broken by decisions — a section moved to another file, a
demand sharpened, a filing route reversed — and the assumption has been that catching those means *reading* every
open condition. I measured that corpus: 81 open nodes carry an acceptance condition, 2,424 lines, ~31,000 words. As
a duty to read, that is genuinely expensive, and nobody had priced it.

**I measured the alternative, and the assumption is wrong.** Each of the four was catchable by a search — not for a
*word*, but for **the thing the change names**. The banned word for the first; for the other three, the file path
each change touched (`map-implementation-rules.md`, `decisions.md`, `map-history.md`). Searching all 81 open
conditions for those four handles finds every one of the four damaged conditions. The reading it costs, per handle:
**4, 14, 27 and 38 matching lines** — against 2,424 lines for the corpus. The worst of the four is 38 lines.

**Why that is not luck.** A condition is a demand written in words. A later fact can only falsify it by changing
something the condition *names*, and a condition names things by word or by path. The party that made the change is
holding that word or that path already. Nothing has to be remembered or reconstructed.

**One thing I found that nothing has connected.** The general version of this question is already an open node on
your graph — **node 37, "Nothing tells a worker to hold its work against the record"**, open since early on, whose
text reads *"Nothing tells a worker to go and look."* One worker's count puts *"eighteen twenty-eighths of this
effort's propagation traffic"* on it. It is also open question 5 in the shipped manager contract. I am not answering
it, and I say under the last alternative why I think the two come apart.

**Two things I settled myself rather than asking.** I priced the duty as a *search* rather than a *read*, because
the measurement says a search reaches every known instance — so the expensive option is costed and rejected on
evidence rather than left unexamined. And I have not tried to catch the case where a condition describes a thing in
different words from the ones the change uses; that residual is stated in the recommendation rather than engineered
away.

**ASK:** When a worker or the manager establishes a fact that makes some other node's acceptance condition wrong,
must it go and look for that condition — and if so, who looks, how far, and does it bind the shipped workflow or
only this effort?

**RECOMMENDED:** **Yes — a duty to *search*, in the same hand that already holds the pen.** Four parts, offered as
one package, because parts two, three and four only mean anything if part one is yes.

**One. The duty exists, and it is a search rather than a read.** Before handing back, the party searches the open
nodes' `## Acceptance condition` sections for the handles its own work fixes — a word it refuses, a path it changes
or moves something out of, a phrase it supersedes — and reads only what matches. Measured on all four known
instances: 4, 14, 27 and 38 lines, against 2,424 to read the corpus.

**Two. Whose: the same split node 252 already drew for the pen.** The party that established the falsifying fact
searches; where no such party exists, the manager does. That makes this one rule with a trigger rather than two
rules, and it puts the looking in the same context as the fact and the repair. Node 95 is the evidence for not
routing it through the manager instead: it carries a repair the manager has been cleanly licensed to make for weeks
and has not made.

**Three. How wide: every open node's condition, claimed or not, and the handles get listed.** The search covers
claimed nodes too — a live worker being judged against a wrong standard is the worst case, not an excluded one —
though what is *done* about a claimed node stays the manager's, since your existing raise rule governs there. And
the party names, on its handover, which handles it searched. That is what makes the duty checkable by someone else
rather than a claim to have been careful.

**The residual, stated rather than solved.** A condition that describes a thing in different words from the ones
the change uses will not match, and no handle search catches it. All four known instances matched; I cannot promise
the fifth will.

**Four. It ships, on whatever carries node 252's permission.** A permission that ships without its trigger ships
broken, and node 95 measures what an untriggered permission does. This adds no new question about *which* carrier —
the manager already has that one waiting for you from node 252.

What this rests on: four damaged conditions, all four reachable by the cheap route; node 203, wrong for days with
nobody looking; and the fact that the party holding the fact is already the party holding the pen, so this hands the
duty to the only context where doing it is free.

**ALTERNATIVES:**

- **Put the duty on the manager at the moment it resolves the falsifying node.** One party, no contract change to
  five worker files. But it spends the manager's context, which this effort has measured as the thing that actually
  fails, and node 95 shows repairs stall in exactly that hand.
- **The narrow duty only: before refusing a word, search the conditions for it.** Node 112's worker's own phrasing —
  cheap, checkable, and provably correct. It reaches one of the four instances.
- **Build an index of every live acceptance condition instead of a duty.** One file to consult rather than a search
  to remember. The manager has already named a version of this for you. It costs upkeep at every mint and every
  amendment, and an index that falls out of date fails silently, where a search cannot.
- **Change nothing.** Node 252's permission stays armed but untriggered, and every falsified condition waits for
  someone to trip over it. That is today, and node 203 is what it costs.
- **Decide this together with node 37 rather than now.** Defensible, and I recommend against it. Node 37 asks how
  much of the whole record a worker must hold its work against — an unbounded corpus with no index of the thing being
  searched. Acceptance conditions are bounded, live in one named section, and are already enumerable: 81 of them.
  Deciding this one now gives node 37 a worked, measured instance to reason from instead of an argument.

#### The human's answer

*Their reply on 2026-09-19, `verbatim`:*

> it seems ok, there was also the idea of the cascade agent that is relevant (but there was no progress done)

**The option it takes**, quoted so the reply is attributable to exactly one thing. It is **the worker's
`RECOMMENDED`**, written by the worker and not by the manager — the four-part package, taken whole:

> **Yes — a duty to *search*, in the same hand that already holds the pen.** Four parts, offered as one package,
> because parts two, three and four only mean anything if part one is yes.
>
> **One. The duty exists, and it is a search rather than a read.** Before handing back, the party searches the open
> nodes' `## Acceptance condition` sections for the handles its own work fixes — a word it refuses, a path it
> changes or moves something out of, a phrase it supersedes — and reads only what matches.
>
> **Two. Whose: the same split node 252 already drew for the pen.** The party that established the falsifying fact
> searches; where no such party exists, the manager does.
>
> **Three. How wide: every open node's condition, claimed or not, and the handles get listed.** The search covers
> claimed nodes too, though what is *done* about a claimed node stays the manager's. The party names, on its
> handover, which handles it searched.
>
> **Four. It ships, on whatever carries node 252's permission.**

**No divergence**: the answer agrees with the recommendation.

**The rider is not a qualification of the answer — it is a second thing they hold**, and it is passed to the worker
as theirs rather than read by the manager. **`cascade`** is a defined word in the shipped manager contract's
glossary: *"an AFK pass that propagates a known revision outward over the graph's edges and over landed code,
queueing graph edits rather than interrupting the human."* Their note that **no progress has been done on it** is a
fact about the effort that the worker did not have and that bears on where this duty belongs.

***The manager's own note, beside their words and not part of them.*** The manager did not ask which option
*"it seems ok"* pointed at, on the same ground as at nodes 252 and 265: **only one of the five is an assent**, and
each `ALTERNATIVE` is a named refusal of it. The worker was resumed in the same turn carrying both their words and
this reading, and told to correct the reading if it takes the answer somewhere it did not offer. **It did not correct
it.**

## Answer

*Written by this node's worker and pasted as it wrote it.*

> **The duty exists, it is a search rather than a read, and it belongs in the same hand that already holds the pen.**
> The human's words, `verbatim`: *"it seems ok, there was also the idea of the cascade agent that is relevant (but
> there was no progress done)"*. The first clause takes this node's `RECOMMENDED` whole — the four-part package,
> unamended. Not a divergence. The second clause is a fact of theirs and not a qualification; it is discharged under
> *How this divides with the cascade* below.
>
> ### The duty: search the handles, do not read the corpus
>
> Before handing back, the party that established a fact searches the open nodes' `## Acceptance condition` sections
> for the **handles its own work fixes** — a word it refuses, a path it changes or moves something out of, a phrase
> it supersedes — and reads only what matches.
>
> **This was the fork the node was minted on, and it was decided by measurement rather than by argument.** The
> premise it was minted with — that one of the four known instances is greppable and the other three would need a
> duty to read — is false, and the numbers are these. The corpus is **81 open nodes carrying a condition, 2,424
> lines, ~30,800 words**. Searching it for the handle each of the four falsifying changes actually held returns every
> one of the four damaged conditions, at a cost of **4, 14, 27 and 38 matching lines** respectively:
>
> | damaged node | the handle the falsifying party held | matching lines across all 81 |
> | --- | --- | --- |
> | [111](111-write-the-starting-an-effort-section.md) | the refused word `charting` | 4 |
> | [152](152-where-the-harness-worktree-instruction-lives.md) | the path `map-implementation-rules.md`, which node 188 moved a section out of | 14 |
> | [156](156-four-resolved-nodes-have-no-index-line.md) | the path `decisions.md`, whose entry semantics node 241 settled | 27 |
> | [203](203-node-155s-condition-preserves-a-contradiction.md) | the path `map-history.md`, whose banking route node 199 reversed | 38 |
>
> **Why the handle always exists, so this is a construction rather than four lucky cases.** A condition is a demand
> written in words. A later fact can only falsify it by changing something the condition **names**, and a condition
> names things by word or by path. The party that made the change is already holding that word or that path. Nothing
> has to be remembered, reconstructed, or searched for.
>
> ### Whose: the split node 252 already drew for the pen
>
> The party that **established the falsifying fact** searches. Where no such party exists — the clause was falsified
> by landed code, or noticed later by somebody else — **the manager searches**. That is [node
> 252](252-may-an-unclaimed-nodes-acceptance-condition-be-amended.md)'s own split for the pen, reused rather than
> restated, so the looking and the repairing are one rule with one trigger and land in one context.
>
> **Why not the manager at resolution instead.** [Node 95](95-carry-the-widening-rule-into-the-shipped-files.md)
> carries a repair [node 82](82-amending-a-condition-whose-scope-was-too-narrow.md) licenses cleanly, found weeks ago
> and still unperformed: the manager's own hand is measurably where these stall. And this effort's standing
> preference is that context lives in the workers rather than the manager, whose context is the thing that has
> actually failed.
>
> ### How wide: every open node's condition, claimed or not, with the handles named
>
> The search covers **claimed** nodes too. **This is wider than node 252's permission, deliberately**: that
> permission reaches unclaimed nodes only, because amending under a live worker is a different act. Looking is not. A
> worker being judged right now against a standard known to be wrong is the worst case on the graph, not an excluded
> one — and what is *done* about a claimed node stays the manager's, the standing raise rule governing there.
>
> The party **names on its handover which handles it searched**. That is what makes the duty checkable by somebody
> else rather than a claim to have been careful, and it costs one line.
>
> ### The residual, stated rather than solved
>
> A condition that describes a thing in **different words** from the ones the change uses will not match, and no
> handle search catches it. All four known instances matched; the fifth is not promised. This is the honest limit of
> what was approved, and it is the case an edge-walking pass would catch — see below.
>
> ### How this divides with the cascade
>
> *This section answers the human's second clause, which supplied a fact this node did not hold: that no progress
> has been made on the cascade.*
>
> [Node 15](15-cascade-pass-mechanics.md) split the cascade into three parties by what the change lands on, and
> **this node lands squarely inside the one that was parked**:
>
> 1. **Resolved-node targets ride the resolving worker's handover.** Push at establishment, in the party's hand, no
>    pass. [Node 43](43-widen-the-invalidation-channel.md) carries it and is open.
> 2. **Open-node targets were parked.** Node 15, `verbatim`: *"Open-node targets are not settled, and stay where they
>    are"*, on the stated ground that *"no index reaches an open node — an open node's one-line summary is its
>    title"*. And, parked with it: *"one duty waits with it: sharpening an unstarted node's acceptance condition,
>    which [node 07] gave this pass, is an open-node edit and therefore stays with the manager for now."*
> 3. **Landed code is the spawned pass.** [Node 44](44-cascade-worker-contract.md) and [node
>    87](87-managers-cascade-duties-have-no-contract.md), both open, both unbuilt. Their conditions are scoped to a
>    landed-code inventory and reach no open node's condition — so **this answer does not touch either, and the pass
>    as specified is untouched.**
>
> **So this answer takes the acceptance-condition slice out of part 2 and gives it part 1's mechanism.** It does not
> make a cascade smaller or unnecessary; it resolves one named class that the cascade's own answer deferred, by the
> route that answer had already chosen for the class where the party holds the fact.
>
> **And it falsifies part 2's stated ground for this slice.** An index *does* reach an open node's acceptance
> condition: `## Acceptance condition` is a named section in a fixed place in every node file, enumerable at 81 and
> searchable at 4 to 38 lines. Node 15 was right that an open node's *summary* is its title; it did not notice that
> the condition is its own index. **What that does to the rest of part 2 — open nodes' questions, blockers and
> annotations, which have no such named section — is not settled here and is reported as a node**, and it is where
> the residual above belongs: a pass over edges catches the synonym case a handle search cannot.
>
> ### This node ran its own duty on itself
>
> Searching the 81 open conditions for this work's own handles — `cascade`, `acceptance condition`, `INVALIDATIONS`
> — returned hits in about twenty nodes and **one live finding**: [node
> 95](95-carry-the-widening-rule-into-the-shipped-files.md)'s clause 1 requires `graph-conventions.md`'s
> `### Acceptance condition` to state *who may change a condition*, and that sentence now also needs a *trigger*.
> Node 252 already recorded that node 95's condition is short in two ways; **this is the third**. Node 44 was
> inspected and is not touched. The search cost under thirty lines of reading.
>
> ### Where it ships
>
> **It ships**, on whatever node carries node 252's permission. A permission that ships without its trigger ships
> broken, and node 95 is the measurement of what an untriggered permission does. This adds no second question about
> *which* carrier — that one is already in front of the human from node 252 — but two open nodes are the standing
> candidates and each already touches the ground: **node 95**, whose condition names `graph-conventions.md`'s
> `### Acceptance condition` and `SKILL.md`'s `## Acceptance conditions`, and **node 43**, which already rewords the
> `INVALIDATIONS` line in the same five worker contracts this duty attaches beside.
>
> ### Node 37 stays separate
>
> [Node 37](37-invalidations-is-not-a-check.md), *"Nothing tells a worker to hold its work against the record"*, is
> open and is the general version of this question — it is also open question 5 in the shipped manager contract, and
> **nothing on the graph connects the two**. It is not merged, and the cascade fact sharpens rather than weakens the
> ground:
>
> - **Different corpus, differently indexed.** Node 37's targets are resolved nodes, for which `decisions.md`
>   already is *"one capped line per resolved node and therefore the index of the whole decision record"*, read whole
>   by every worker. This node's targets are open nodes' conditions, for which no index was thought to exist and one
>   turns out to.
> - **Node 15 part 1 has already reshaped node 37's territory** by widening the channel's word, which node 37's own
>   text predates. Merging would fold a partly-answered question into a fully-answered one.
> - **Different consequence.** A wrong condition blocks or misdirects work; a stale decision misleads.
>
> What this node gives node 37 is a worked, measured instance and a mechanism to test against, rather than an
> answer.

**The index line the worker wrote:**

> A duty to search exists: the party establishing a falsifying fact searches the open nodes' acceptance conditions
> for the handles its own work fixes, else the manager does.

## Flags

`263.1` `ASSUMPTION` **· settled** — *The worker's own text, pasted.*

> **I priced the duty as a search rather than a read, and the number that decided the node was one I made myself.**
> The node was minted on the premise that one of four instances is greppable and that reaching the other three *"is a
> duty to read, and nobody has costed it"*. I costed it, and then tested whether a read was needed at all: I measured
> the corpus (81 open conditions, 2,424 lines, ~30,800 words) and then ran, against all 81, the handle each of the
> four falsifying parties actually held. All four matched, at 4, 14, 27 and 38 lines. I offered only the search, with
> the read named and priced as the rejected option, and both numbers were in the payload's `SO FAR` before the human
> assented — so the pricing was visible rather than silent. What I accepted: the whole recommendation rests on a
> generalisation from four cases, that a clause can only be falsified by a change to something it names in words. I
> believe it is a construction rather than an induction, and I have stated the one case it does not reach.

`263.2` `ASSUMPTION` **· settled** — *The worker's own text, pasted.*

> **I widened the duty to claimed nodes, where node 252's permission stops at unclaimed ones.** Node 252 confined its
> pen to unclaimed nodes, on the ground that amending under a live worker is a different act. I extended the duty to
> **look** across every open node's condition regardless of claim status, and left what is **done** about a claimed
> one with the manager under the standing raise rule. My ground is that a live worker being judged against a
> known-wrong standard is the worst case rather than an excluded one, and that excluding claimed nodes makes the
> search no cheaper — there is one claimed node with a condition today. It was stated in the payload and assented to.
> What I accepted: a later reader meets two rules about acceptance conditions with different scopes, and nothing but
> this paragraph explains why they differ.

`263.3` `ASSUMPTION` **· settled** — *The worker's own text, pasted.*

> **I judged how this duty divides with the cascade without putting the division back to the human.** The human's
> answer added, in their own words, that *"there was also the idea of the cascade agent that is relevant (but there
> was no progress done)"* — a fact I did not hold and could not have inferred. I read node 15, node 44 and node 87
> rather than a paraphrase, found that node 15's part 2 parks exactly this class on a ground my measurement
> falsifies, and wrote the division into the answer rather than asking them which of the three readings they meant.
> My ground for not asking: node 15's own answer already chose push-at-establishment for the class where the party
> holds the fact, so giving this slice that mechanism is applying their decision rather than making a new one. What I
> accepted: if they meant that this duty should have been written as part of the cascade rather than beside it, the
> answer as written puts it in the wrong file, and the node I reported is where that would surface.

`263.4` `MANAGER-WRONG` **· settled** — ***Filed by the manager against itself.*** **The manager's note at filing, and the spawn
that carried it, asserted a false fact as the sharpest fork of this node's question**: *"of the four instances,
exactly one is greppable. Node 111's turns on a refused word. The other three turn on a decision … and no string
search finds those."* **All four are reachable by search**, by the path the falsifying change touched rather than by
a refused word, measured at 4, 14, 27 and 38 lines. The manager marked it *"as material rather than as a position"*
and the worker reports that **the marking did not prevent it hardening** — it framed the worker's first hour, and
what saved it was a different sentence in the same paragraph saying nobody had costed the alternative, which read as
an invitation to test. The manager had reasoned from one handle where there are two. **The worker's generalisation
is carried here because it is the repair**: an assertion about the shape of an answer should be marked *untested*
rather than merely *non-binding*, and a spawn that can name a cheap test for it should name the test. This is the
shipped contract's open question 9 occurring live.

## Nodes surfaced

*One, with the worker's own question. **The manager has minted its node file** — [node
272](272-the-cascades-open-node-half-is-parked-on-a-ground-that-turns-out-to-be-false.md).*

## Invalidations

*The worker's own text, pasted.*

> **[Node 15](15-cascade-pass-mechanics.md) — its part 2 is invalidated for one class, and the ground it was parked
> on is false for that class.** Node 15 wrote *"Open-node targets are not settled, and stay where they are"*, on the
> ground that *"no index reaches an open node — an open node's one-line summary is its title."* An open node's
> `## Acceptance condition` is a named section at a fixed place in every node file: 81 of them on this graph, 2,424
> lines, searchable by handle at 4 to 38 lines. For that class the index exists, and node 263 gives the class part
> 1's own mechanism — push at establishment, in the hand of the party holding the fact. Node 15's parts 1 and 3 are
> untouched, and the duty node 15 parked alongside — *"sharpening an unstarted node's acceptance condition … stays
> with the manager for now"* — is moved only as to **finding**, not as to **sharpening**. Reported as a node.
>
> **[Node 252](252-may-an-unclaimed-nodes-acceptance-condition-be-amended.md) — one sentence of its answer is
> superseded.** Its `### What that does not fix, and it is the residual` says *"This answer gives the permission and
> creates no such duty — a duty to go looking is a new demand and was not put to the human."* The demand has now been
> put and taken. The rest of node 252 stands whole: node 263 supplies its trigger and changes nothing about its test,
> its pen, or its guards. Node 263's duty is **wider in one respect only** — it reaches claimed nodes, where node
> 252's permission does not.
>
> **[Node 95](95-carry-the-widening-rule-into-the-shipped-files.md)'s acceptance condition is now short in a third
> way.** It is open and unclaimed. Its clause 1 requires `graph-conventions.md`'s `### Acceptance condition` to state
> *who may change a condition after it is written*; that sentence must now also state the **trigger** — who searches,
> for what, and how far. Node 252 recorded the first two shortfalls and neither has been repaired. All three are
> amendable under node 252, whose pen here is the manager's. **Found by running this node's own duty on this node's
> own work**, which is the first exercise of the rule and is recorded as such.
>
> **Untouched, and stated so they are not read as moved.** Node 44 and node 87 — both are scoped to a landed-code
> inventory and reach no open node's condition; the pass as specified is unchanged. Node 37 — open, the general
> question, deliberately not merged. [Node 43](43-widen-the-invalidation-channel.md) — open; it rewords the
> `INVALIDATIONS` line in the five contracts this duty attaches beside, and is a carrier candidate rather than
> something this answer changes. Node 82 and node 39 — a duty to look touches neither authorship nor scope.

## Retrospective

*The worker's own text, pasted.*

> **1. What I had to hunt for.**
>
> - *That node 37 exists.* My spawn and my node file both framed the general version of this question as the shipped
>   manager contract's **open question 5**, with no node behind it. There is a node, open since early, whose text
>   reads *"Nothing tells a worker to go and look."* — near-identical to my own node's title. I found it by grepping
>   the node files for `go and look` on a hunch. **Nothing on the graph connects them**, and both my node's author
>   and the manager wrote as though nothing did.
> - *That the cascade's own answer had already parked this exact class.* I would not have looked at all without the
>   human's second clause. Node 15's part 2 is the ground under my whole answer and nothing pointed at it; node 15
>   does not appear in my node file, my spawn, or node 252.
> - *The corpus measurement.* Nothing in the record states how many open nodes carry a condition, how large they are,
>   or that the section heading is uniform. Deriving 81 / 2,424 lines / ~30,800 words took two shell commands and was
>   the single most valuable thing I did.
> - *Whether nodes 44 and 87 were falsified by my answer.* Their titles say "cascade" and my answer moves cascade
>   territory. Only reading node 44's condition showed it scoped to landed code. Cheap, but nothing let me skip it.
>
> **2. What arrived in my context that this node did not need.**
>
> - *From the mandatory reads, `map.md`:* I used four of roughly twenty-five `## Notes` items. The worktree rules,
>   the gate-diff rule, the spent moved-standard licence, the resume rule, the plugin direction, the checker-rules
>   direction and the retrospective's own full statement bore on nothing. **This is at least the seventh report of
>   this item**; node 246 holds it.
> - *Where a scoped pointer worked, as the positive datum:* my spawn told me to grep `decisions.md` for `condition`
>   rather than read it. 148 lines became 21, of which I used one. **Second consecutive node on which that
>   instruction paid**; node 165 should have both measurements.
> - *Whole files taken for one fact:* node 252 (511 lines) — paid, it is the node's only real input. Node 155 (72
>   lines) **did not pay**: I opened it to check whether its search-the-record instruction was already my duty, and
>   its clause 1d rules it out in one line. Node 07 was grepped rather than read, correctly.
> - *Duplicated instruction:* the retrospective's four questions arrived in my spawn and again, at greater length, in
>   `map.md`. **Same finding as node 252's worker, one node later.**
>
> **3. What would have made this node easier.**
>
> - ***My spawn asserted a false fact and it was load-bearing.*** It stated, as the sharpest fork of the question,
>   that *"of the four instances, exactly one is greppable"* — and my node file repeats it. It is wrong. The manager
>   correctly marked it *"as material rather than as a position"*, and it still framed my first hour: I built the
>   fork around it and tested it only because the same paragraph said *"nobody has costed it"*, which read as an
>   invitation. **The marking did not prevent the hardening; the invitation is what saved it.** This is the manager
>   contract's open question 9 occurring live, and it is worth recording that a "this is material, not a position"
>   disclaimer was not sufficient. The generalisable form: **an assertion about the shape of the answer should be
>   marked as untested, not merely as non-binding, and a spawn that can name a cheap test for it should name the
>   test.**
> - *In the node file:* it framed the adjacency as an open question in a shipped file when it is an open **node**,
>   37, whose question overlaps mine almost word for word. A worker told to judge separability should be told what it
>   is separating from.
> - *In the record:* nothing links the four damaged conditions, node 37, node 15's part 2, and node 252. **Five
>   records of one hole**, each findable only by guessing the words the others used. Node 252's worker reported the
>   same absence one node earlier.
> - *In the contract:* nothing. The rule forcing dependent questions out of a shared payload is what collapsed five
>   candidate questions into one package.
>
> **4. What I read that was stale, wrong, or contradicted something else.**
>
> - **My own spawn's greppability claim**, above. The most consequential stale fact I met, and it was written this
>   session.
> - **Node 15's part 2 ground** — *"no index reaches an open node"* — false for the acceptance-condition class.
> - **Node 252's residual sentence** — *"This answer … creates no such duty"* — superseded by this node.
> - **Node 95's condition, short in a third way.** Found by running this node's own duty.
> - **Node 37's text predates node 15 part 1**, which has since answered the mechanism for half its territory, and
>   node 37 records none of it. Not minted — node 37 is open and whoever claims it will meet node 15 — but nothing on
>   node 37 says so.

## The manager's disposal of the retrospective's record items

*Not the worker's text.*

- **The spawn's false greppability claim** → **filed as `263.4` against the manager**, carrying the worker's
  generalisation as the repair rather than only the correction.
- **Nothing on the graph connects node 37 to this node**, and both the node's author and the manager wrote as though
  nothing did → **not minted**, node 37 being open and its claimant meeting this answer. **Named for the human**, and
  it is the same shape as the worker's next item.
- **Five records of one hole, each findable only by guessing the others' words** — the four damaged conditions, node
  37, node 15's part 2, node 252 → **not minted, and this is the second consecutive worker to report it.** The
  manager has already named *"there is no index of conditions known to be wrong"* for the human at node 252's
  disposal; this widens it from conditions to the whole hole. **Named for the human, second report.**
- **`map.md`'s `## Notes`, seventh report** → node 246 holds it. Not minted.
- **The retrospective's four questions arriving twice**, second consecutive report → **still not minted**: removing
  the duplicate is a `Change the map` on a paragraph the human's own standing instruction owns.
- **The scoped `decisions.md` grep paying a second consecutive time** → **carried to [node
  165](165-measure-whether-a-fed-file-earns-its-place.md)**, now three measurements.
- **Node 95's condition short in a third way** → **the manager has not amended it**, and that is now the third
  shortfall recorded and the third time it has not been repaired. Node 95 is the standing evidence in two separate
  answers that a permission can be granted and never exercised, and **the manager is the hand it keeps stalling
  in.** Named for the human as a judgement they may want to take off the manager.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
