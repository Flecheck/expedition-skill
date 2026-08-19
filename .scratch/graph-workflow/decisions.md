# Decisions so far

The index — one line per resolved node: enough to judge relevance, then open the node for the
detail it holds. A decision lives in exactly one place, its node; this file never restates one.

**Append-only.** A superseded node's line is struck through in place and its replacement gets a
new line of its own. Nothing is ever deleted or rewritten.

**New entries are capped at one line, one sentence, ~25 words.** Grouped by label where the effort
declares a label vocabulary; flat where it does not. Split out of `map.md` and capped by
[Graph file format](nodes/13-graph-file-format.md).

> The ten entries below are **pre-cap**: they were written into the map body before the cap existed
> and were moved here verbatim rather than shortened, per the standing rule that an in-place update
> never deletes.

- [Destination of this effort](nodes/01-destination.md) — a working workflow in place, dogfooded once; not a spec. This map carries execution.
- [Runtime that hosts the manager and its subagents](nodes/02-runtime-host.md) — Claude Code skills plus built-in subagents; question round-trips via pause-and-resume. Flagged provisional by the user: "might be a bit too simple."
- [How much of the lifecycle the workflow owns](nodes/03-lifecycle-scope.md) — one graph from idea to perfect code; supersedes wayfinder rather than sitting downstream of it, because implementation can only reshape decisions that are still live.
- [Concurrency model](nodes/04-concurrency-model.md) — ~2 HITL grilling subagents in flight to keep the human's queue full; exactly one code-modifying subagent at a time, so v1 needs no worktrees. Later: worktrees plus `git merge --ff-only`.
- [How the graph's bookkeeping is kept straight](nodes/05-graph-state-mechanism.md) — markdown files and prose rules, not a CLI, because a CLI's command surface would prejudge the still-open revision semantics. Skills *can* ship executables; a read-only `check`/`frontier` command is the first thing to extract if drift appears.
- [Revision semantics](nodes/06-revision-semantics.md) — unstarted nodes are updated in place; nodes holding work are superseded by replacement nodes of any shape, with a mandatory forward pointer. Fan-out is an aggressive AFK cascade whose scope is agent judgement over both edges and code, and whose output is queued graph edits rather than human interrupts. Code revisions jump the exclusive code slot; decision revisions queue normally.

- [Node type taxonomy](nodes/07-node-type-taxonomy.md) — five types: research, prototype, grilling, task, implementation. Implementation and prototype split on whether the artifact is the deliverable; `task` stays for preconditions. Verification is an obligation on every implementation node discharged by an independent reviewer, not a type. Implementation is AFK and never asks live: small ambiguities are decided and flagged, genuine forks become grilling nodes. Acceptance conditions are written by the spawning node.

- [Relay protocol](nodes/08-relay-protocol.md) — prototyped live with two HITL subagents. Routing turned out nearly free; the **payload** is the hard part. A relayed question carries the node's name, what the node is about, a digest of the thread so far, the question verbatim, and optional manager notes drawn only from context the manager already holds. Answers go back **verbatim** with provenance and an explicit divergence marker. Death is detected lazily by a failed resume, recovered by replaying an at-relay-time log on the node file, capped at two respawns. All four human redirects are supported; "you decide" is answered by the subagent, "ask me later" stores progress and returns the node to `open` with its answers banked. The manager never answers anything.

- [Dogfood target](nodes/09-dogfood-target.md) — **[Lang](/home/mathieu/projects/Lang)**, and specifically a **migration** of its live `.scratch/spec-completion/` effort rather than a fresh one: Lang is where the idea came from, its ~130 labelled gaps are already a graph written in prose, its compiler is explicitly disposable, and its ground rules ("docs win over code", "no invented semantics", "facts are the agent's job, decisions are the author's") restate this effort's own principles. Success is **coverage, not completion** — every mechanism this map decides gets run once on a real effort. Seven things the manager can schedule must happen; four (supersession, cascade, death-recovery, termination) must not be faked, and "not yet observed" is a legitimate result. The run's second output is a record of the friction found while using it. *(Corrected by [Graph file format](nodes/13-graph-file-format.md): the corpus is **179** distinct gap labels, not ~130.)*

- [Done-ness and termination](nodes/10-done-ness.md) — done is a **fixed point the human declares**, never the manager: an empty frontier (where `superseded` ≠ `resolved`, and a parked node is `open`, so "ask me later" postpones *done* and not just the question), a tree meeting the standing bar, a whole-graph **sweep** that produces nothing new, and the human having read the **completion report**. The bar ships as default *properties* — builds, no warnings, formatted, tests pass where relevant, plus project criteria, plus the acceptance condition — with commands **discovered per repo**, since the workflow will run on repos this machine has never seen; the independent reviewer checks it at every implementation node, so "landed" means "landed green". Flags cost nothing until the report, where the human settles them or **postpones** one, which creates a node. No audit agent for cascade misses: the bar, the mechanical edge check, and the human's own reading of the changes are the backstops, and a semantic miss in code that builds cleanly is the named residual risk. **Most efforts never terminate at all, and that is a legitimate steady state.**

<!-- capped entries from here on -->

- [Graph file format](nodes/13-graph-file-format.md) — four files, `NN` identity with foreign labels in the free-form name, optional `Labels:` as a subset selector, and a fifth status `out-of-scope`.
- [Git and code-landing policy](nodes/11-git-and-code-landing.md) — the manager commits one path-limited commit per implementation node, after the human approves it; no branches, no push, no history rewrite.
- [Naming the workflow and its vocabulary](nodes/14-naming.md) — the workflow is `/expedition`, an element is a `node`, and forty terms are fixed in [CONTEXT.md](../../CONTEXT.md) with their rejected synonyms attached.
- [Write the graph conventions document](nodes/21-conventions-document.md) — the format and its seven procedures ship at `.claude/skills/expedition/`, instructions only, wayfinder differences in a sibling file. Commit `92407d4`.
- [Subagent context contract](nodes/12-subagent-context-contract.md) — the spawn dispatches to a contract skill over three pointers; the worker returns a **handover** the manager pastes unaltered; the checker is blind.
- [Human review of landed code](nodes/20-human-code-review.md) — the gate has three outcomes, approve / correct / reject; the manager assembles the payload from others' text and never renders the diff.
- [Friction from running this map by hand](nodes/24-self-hosted-friction.md) — fourteen findings; the constraint that actually failed every session is the manager's context, not the human's attention.
- [When an AFK worker cannot proceed](nodes/23-worker-cannot-proceed.md) — three triggers open a blocking raise; the human's answer continues or stops the worker, and a stop salvages the work first.
- [Write the worker contract skills](nodes/22-worker-contract-skills.md) — six standalone skills, one per node kind plus the checker, each carrying its own vocabulary and every return variant. Commit `e72f444`.
- [Off-contract subagent output](nodes/17-off-contract-output.md) — on-contract means the manager can file it, however far it departs; departures become flags, and only an unfileable return is re-prompted, once.
- [What is recorded when the human takes an option as offered](nodes/25-recording-an-option-taken.md) — the manager pastes the human's reply as written, marked `verbatim`, with the option quoted beside it and attributed to the worker.
- [Whether flags.md survives the settle-at-close practice](nodes/27-does-flags-file-survive.md) — it stays: not a queue but the capped index of every agent judgement, the flag counterpart to this file, and check 6 now compares both states.
- [Carry the recorded deltas into the shipped skill files](nodes/26-carry-deltas-into-shipped-files.md) — nine deltas and node 27's five items land, two contracts gain a carve-out, and the glossary follows on three entries. Commit `0cec4e7`.
- [Whether a spawn may override a shipped worker contract](nodes/28-spawn-overriding-a-contract.md) — a spawn may not depart on the manager's authority; the manager raises instead, and the answer licenses one attempt while the repair becomes a node.
