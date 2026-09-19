# Nothing tells the party that falsifies an acceptance condition to go and look for it

Type: grilling
Status: claimed

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
