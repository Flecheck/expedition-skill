# Workflow self-improvement during use

Type: grilling
Status: open

## Question

When using the workflow reveals that the **workflow itself** is wrong, where does that go?

Surfaced by [Dogfood target](09-dogfood-target.md). The human's expectation is explicit: *"The workflow is bound to evolve and improve anyway as I find new things by using it"*. So this is not an edge case to handle once — it is the expected steady state, and the dogfood run's most valuable output is the friction it exposes. Without a place to put that, it evaporates into a transcript.

The awkwardness is that the friction is discovered on one graph and has to be fixed on another:

- A subagent grilling a Lang spec gap notices the relay payload is missing something. That is not a Lang node — Lang's graph is about a programming language. Does it become a node on **this** map, which may by then be closed? A node on Lang's graph tagged as not-about-Lang? A separate log?
- **Who is allowed to notice?** Subagents are read-only and stay off the graph, per [Relay protocol](08-relay-protocol.md). If only the manager may record friction, everything a subagent noticed has to survive its return value. If subagents may record it, the single-writer rule needs an exception.
- **What granularity?** A one-line "this was annoying" is cheap and gets written; a properly-framed node is useful and does not get written. These may want to be two different things, with a promotion step.
- Does friction **interrupt** the run or queue? [Revision semantics](06-revision-semantics.md) chose queued graph edits over human interrupts for cascades; the same reasoning may apply, but a workflow bug can also be blocking the very run that found it — the workflow cannot always defer fixing itself the way it can defer a decision.
- **When may the workflow be changed mid-run?** Editing the skill files while a graph is live means later nodes ran under different rules than earlier ones, so the dogfood stops being one experiment. Freezing until the run ends is cleaner but wastes what was just learned. Is there a distinction between a fix that unblocks the run and an improvement that can wait?
- Does this map's own destination move? The destination is *dogfooded once*. If a friction fix is required to *finish* the dogfood, the map has to accept new implementation nodes after it thought it was nearly done — which is [Done-ness](10-done-ness.md)'s oscillation question wearing a different hat.

Added by [Done-ness and termination](10-done-ness.md), which widens where friction comes from and answers the last bullet:

- **Some of it will be found on machines and repositories this graph can never see.** The human will also run the workflow on work projects elsewhere — and those are the runs *most* likely to break the design, because a bounded effort that actually terminates exercises the parts Lang never will. A channel that works only by an agent reading files in this repo misses exactly those.
- So friction from there arrives as **the human's own words to the manager** — a third possible noticer alongside the manager and the subagent, and the one the *who is allowed to notice* bullet did not consider. It also puts a floor under the granularity question: whatever the mechanism is, the human has to be able to dictate a one-liner from memory, days later, about a repository that is not even open.
- **The destination bullet above now has a mechanical answer.** Done-ness settled that only the human closes an effort, and that a fix landing as a new node simply keeps the frontier non-empty. So this map's destination does not need to move: the map cannot close while friction nodes are open, and the human decides when to stop accepting them.

- **How a self-edit lands is settled, and it is not special.** [Git and code-landing policy](11-git-and-code-landing.md) rules that an effort's graph lives in the repo the effort changes and that each repo's effort follows the same policy — so a friction fix to the skill files is an implementation node on *this* map, landing in `graph-agent` by the same gate as anything else: reviewer, human approval, one path-limited commit. Nothing cross-repo is coordinated. What stays this node's question is **when** the workflow may edit itself — mid-run, between efforts, or only when the human says so — not how the edit lands.
- One consequence worth noticing: a self-edit during the dogfood takes the **exclusive code slot in `graph-agent`** while Lang's own implementation nodes hold Lang's. Two independent slots in two repositories is not something the concurrency model has been asked about, and it is the first case where the workflow improving itself competes with the workflow doing its job.

Not blocked: answerable now, and worth answering before the dogfood starts rather than during it, since the run is where the friction arrives.

## Annotation

Added by [Naming](14-naming.md).

- **The promotion step this node asked for exists, and it is called `promote`.** Derived for flags in [Done-ness](10-done-ness.md), it is the same act: turn a one-line note of friction, or a flag, into a node. So the granularity question keeps both levels — a cheap line that actually gets written, and a node it can be promoted into — under one verb.
- **A vocabulary change is a self-edit like any other, and the worst-behaved one.** [`CONTEXT.md`](../../../CONTEXT.md) is a product-tree file in `graph-agent`, so changing a settled term lands through the gate here like anything else. But it is the one kind of self-edit that makes earlier and later nodes of a live effort read differently, which is this node's *may the workflow change mid-run* question at its highest stakes.
