# A periodic review with nothing named to review

Type: grilling
Status: open

## Question

Every pass this workflow has is **triggered by something and pointed at something**. A cascade knows what changed
and propagates it. A sweep looks for revisions nobody propagated. A checker holds one node's work against one
acceptance condition. `INVALIDATIONS` asks a worker what its own work contradicted. In every case something names
the target.

**Nothing ever stands back and looks at the whole of what has been built to ask whether it is any good.** The
human's idea, in their own words: *"a periodic review of the state of the changes, to find improvement to
architecture and other. A bit like the cascade worker but with no specific thing to review."*

So: **should an expedition run an untriggered, periodic, open-ended review of its own accumulated work — and if so,
what is it held against, what does it return, and what fires it?**

### The obstacle, which is on the record and is not small

[Done-ness and termination](10-done-ness.md) already ruled on the nearest thing to this and ruled against it, under
its own heading *"Does anything check the cascade did not miss a node"*:

> The answer is **no audit agent** — a second agent judging the first is the same judgement risk restated, with no
> ground truth to appeal to.

It named three backstops instead — the standing bar, the mechanical check, and the human reading the changes — and
accepted a **named residual risk**: *"a semantic miss, in code that builds cleanly, in a file the human did not
happen to read. Nothing here catches that."*

**This node cannot be answered without meeting that ruling.** Either it is distinguished or it is overruled, and
saying which is most of the work.

### The distinction that might do it, and it is not obviously sound

Node 10's ground was **no ground truth to appeal to**. That bites hardest on *did agent A miss something*, where
the only yardstick is another agent's judgement of the same material. It bites less where the pass holds the work
against **something outside the work**, and this effort has run that shape twice and both times it paid:

- [Review every shipped file against `/writing-great-skills`](47-review-shipped-skills.md) — six findings, six
  places the files already met the standard, and it **falsified a measurement the manager had written into its own
  node**.
- [Re-review the shipped files against `/writing-for-agents`](54-review-against-writing-for-agents.md) — ten of
  node 47's twelve findings still stood, and the new text's one sharp sentence priced a quarter of the corpus as
  read by nobody.

**But both of those had a document to hold the work against, and this idea explicitly does not** — *"no specific
thing to review"* is the whole of what makes it new. So the precedent does not transfer for free, and whether
*architecture* is a yardstick or a preference is the question underneath the question.

### What the answer has to fix, whichever way it goes

- **What fires it.** *Periodic* is not yet a trigger. Candidates already visible: every N resolved nodes, every N
  landed commits, at each compaction of the manager's thread, or on the human's word alone.
- **What it is held against.** The shipped standards, the map's own destination and standing preferences, the
  glossary — or nothing but the reviewing agent's judgement, which is what node 10 refused.
- **What it returns, and to whom.** Proposed nodes are the obvious shape, and the obvious failure with it: a pass
  that can always find *something* mints work forever. Whether it is allowed to return *nothing* and have that be
  a result matters more than what it returns when it finds something.
- **Whether it is a new mechanism at all.** [Done-ness and termination](10-done-ness.md) already requires a
  **whole-graph sweep that produces nothing new** as one of four termination conditions. This may be that sweep
  run early and often rather than a second thing — in which case the answer is a trigger and a scope widening, not
  a contract. The glossary's `Sweep` entry is narrower than that reading needs: *"a pass looking for revisions
  nobody propagated"*, which is missed propagation and not architecture.
- **What it costs.** An open-ended pass over accumulated work is the most expensive shape of agent this design has,
  because nothing bounds what it reads. That has to be priced before it is scheduled, not after.

### Related, and none of them is this

- [Cascade pass mechanics](15-cascade-pass-mechanics.md) and [Write the cascade pass's worker
  contract](44-cascade-worker-contract.md) — the triggered version, which the human's phrasing points at as the
  shape to borrow.
- [Workflow self-improvement during use](19-workflow-self-improvement.md) — friction, raised where noticed. Same
  spirit, opposite discipline: opportunistic and never scheduled.
- [Nothing tells a worker to hold its work against the record](37-invalidations-is-not-a-check.md) — the same
  gap seen from inside a single node rather than over the whole effort, and open.
- The map's fog item **Nothing watches a standard that lives outside this repository** — an external yardstick
  moving under a resolved node, which is a trigger this node's answer might absorb.

## Priority

**Low, at the human's word.** It is not token-use work, so it does not ride [What the manager works on
next](16-human-steering.md)'s standing bump; and it is not blocking anything, since every mechanism it would
review works without it.

## Where it came from

The human's own idea, unprompted, `verbatim`: *"I had the idea of having a periodic review of the state of the
changes, to find improvement to architecture and other. A bit like the cascade worker but with no specific thing
to review. Add a node with low priority"*.
