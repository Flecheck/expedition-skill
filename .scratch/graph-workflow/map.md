# Map: a graph workflow that ends in finished code

Label: wayfinder:map

## Destination

A working, dogfooded workflow living in this repo: skill files, plus any harness they need, that take a loose idea all the way to a state where the code is finished and correct — driven by a manager thread that owns a graph of issues and spawns one subagent per issue, where implementation issues are first-class and revisable.

Reached when the workflow has been run end to end on at least one real effort.

## Notes

**This map carries execution.** Wayfinder is normally plan-don't-do; this effort overrides that, as the skill's Notes block permits. Implementation is in scope, and the destination is working files rather than a spec. Reason: the deliverable is mostly prose instructions, so a spec precise enough to build from would be the same document written twice — and designing an implementation-first workflow via spec-then-build would contradict the thing being designed.

**Domain.** Agent workflow design. The artifact is skill files (markdown), possibly with bundled `scripts/`. Direct ancestor is Matt Pocock's `/wayfinder`, which this supersedes for efforts it is run on; the orchestration shape is borrowed from [firstmate](https://github.com/kunchenguid/firstmate) (one liaison, a crew behind it).

**Skills every session should consult:** `/grilling` and `/domain-modeling` by default, `/naming` for terminology, `/coding-principles` before writing code, `/prototype` for prototype nodes.

**Standing preferences for this effort:**

- Prefer short, simple prose and code that can be changed later over machinery built for predicted needs. Reserve heavy design for the hard-to-reverse core — the graph structure and revision semantics.
- **The human is the scarce resource.** Parallelism exists to saturate the human, not the machine.
- The human only ever talks to the manager thread. A subagent never answers its own HITL question.
- **An in-place update never deletes.** When any file in the graph is edited — a node or this map — superseded text is marked as superseded and left where it is, and new text is added around it. Information leaves a file only when it is clearly wrong or the human asks for it gone. Quiet deletion is most damaging and least visible in the map itself.
- Tracker is local markdown (no issue tracker configured): this map and its nodes are the files in this directory.

**Known prerequisite:** this directory is not yet a git repository, and the design already assumes git (`--ff-only` landing). `git init` must happen before any implementation node runs.

## Decisions so far

- [Destination of this effort](issues/01-destination.md) — a working workflow in place, dogfooded once; not a spec. This map carries execution.
- [Runtime that hosts the manager and its subagents](issues/02-runtime-host.md) — Claude Code skills plus built-in subagents; question round-trips via pause-and-resume. Flagged provisional by the user: "might be a bit too simple."
- [How much of the lifecycle the workflow owns](issues/03-lifecycle-scope.md) — one graph from idea to perfect code; supersedes wayfinder rather than sitting downstream of it, because implementation can only reshape decisions that are still live.
- [Concurrency model](issues/04-concurrency-model.md) — ~2 HITL grilling subagents in flight to keep the human's queue full; exactly one code-modifying subagent at a time, so v1 needs no worktrees. Later: worktrees plus `git merge --ff-only`.
- [How the graph's bookkeeping is kept straight](issues/05-graph-state-mechanism.md) — markdown files and prose rules, not a CLI, because a CLI's command surface would prejudge the still-open revision semantics. Skills *can* ship executables; a read-only `check`/`frontier` command is the first thing to extract if drift appears.
- [Revision semantics](issues/06-revision-semantics.md) — unstarted nodes are updated in place; nodes holding work are superseded by replacement nodes of any shape, with a mandatory forward pointer. Fan-out is an aggressive AFK cascade whose scope is agent judgement over both edges and code, and whose output is queued graph edits rather than human interrupts. Code revisions jump the exclusive code slot; decision revisions queue normally.

- [Node type taxonomy](issues/07-node-type-taxonomy.md) — five types: research, prototype, grilling, task, implementation. Implementation and prototype split on whether the artifact is the deliverable; `task` stays for preconditions. Verification is an obligation on every implementation node discharged by an independent reviewer, not a type. Implementation is AFK and never asks live: small ambiguities are decided and flagged, genuine forks become grilling nodes. Acceptance conditions are written by the spawning node.

- [Relay protocol](issues/08-relay-protocol.md) — prototyped live with two HITL subagents. Routing turned out nearly free; the **payload** is the hard part. A relayed question carries the node's name, what the node is about, a digest of the thread so far, the question verbatim, and optional manager notes drawn only from context the manager already holds. Answers go back **verbatim** with provenance and an explicit divergence marker. Death is detected lazily by a failed resume, recovered by replaying an at-relay-time log on the node file, capped at two respawns. All four human redirects are supported; "you decide" is answered by the subagent, "ask me later" stores progress and returns the node to `open` with its answers banked. The manager never answers anything.

## Not yet specified

- **The implementation nodes that write the actual skill files** — the manager's skill, the issue-subagent prompt templates, the invocation surface. Cannot be sized until the taxonomy, relay and file format land. This is where most of the remaining work lives. The taxonomy has now landed, so the remaining blockers to sizing are the relay and the file format — and it is now known that each of these nodes will carry a spawner-written acceptance condition and an independent review before it can resolve.
- **Whether the Claude Code subagent runtime proves too simple**, and the upgrade path to a firstmate shape (real sessions, worktrees, file mailboxes) if so. Only judgeable after a dogfood run. The taxonomy raised the load: every implementation node now spends a second AFK agent on independent review, and the HITL budget is disjoint from the code slot, so more agents run concurrently than first assumed.
- **Resume and recovery** — what happens when the manager's context compacts or its session dies mid-graph. Firstmate's answer is that all state lives on disk and the next session reconciles; whether prose rules are enough to make that work here is unknown. [Relay protocol](issues/08-relay-protocol.md) supplied the first real mechanism: routing keys and the interview log are durable on disk per attempt, so a fresh manager can re-adopt interviews that are still live. What is still unknown is everything the manager holds that is *not* an interview — chiefly the node-name-to-routing-key mapping as a whole, and whatever it knew about why it chose the nodes it chose.
- ~~**Failure handling** — a subagent that dies mid-question, returns garbage, or exceeds its context before answering.~~ **Graduated** by [Relay protocol](issues/08-relay-protocol.md), which split it in two and answered one half. The **death and context-exhaustion** half is answered there: lazy detection by failed resume, replay from the node's at-relay-time log, two-respawn cap, then escalation as a node-too-coarse decision. The **garbage** half is now [Off-contract subagent output](issues/17-off-contract-output.md), because a live-but-off-contract agent shares no remedy with a dead one. Kept here, struck through, per the standing rule that nothing is deleted.
- **How the human sees graph progress** — whether anything renders the graph, or reading the files is enough. Sharpened by the revision decision: supersession chains are the record of where the graph keeps rubbing, and a cascade that supersedes eleven nodes without saying so is a surprise waiting for the next human read. Both only pay off if something surfaces them. Sharpened again by [Relay protocol](issues/08-relay-protocol.md): a **parked** node is back to `open` while holding answers the human already paid for, so a graph read must make half-interviewed nodes distinguishable from never-started ones — otherwise a deferral becomes invisible debt. This is now the presentation counterpart to [Human-initiated steering](issues/16-human-steering.md), which is the control side of the same problem; steering is useless without a view to steer from.
- **Extraction of a graph tool**, per the revisit trigger in the graph-state decision. The revision decision moved this closer: there is now a status that does not satisfy an edge, two edge directions to keep consistent, and repointing work for the cascade — all currently prose.
- **Whether a research node is warranted** — none exists yet, because every open question is a design decision rather than an external fact. The trigger written here was "if revision semantics stalls"; it did not stall, so that trigger is spent, and no research node is outstanding on this account.

## Out of scope

- **Multi-repo and remote fleets** — firstmate's secondmates, SSH-reachable homes, cross-machine dispatch. Beyond a single-repo workflow.
- **Non-Claude-Code harness support** — Codex, Grok, OpenCode. The runtime decision picked one harness deliberately; portability is a different effort.
- **External channels** — firstmate's Relay (X, Discord). The destination names one human on one channel.
- **Cost and token accounting**, dashboards, fleet telemetry.
