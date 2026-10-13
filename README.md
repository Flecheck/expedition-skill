# expedition-skill

`/expedition` is a Claude Code workflow that takes a loose idea all the way to finished, reviewed code.
One long-lived **manager** thread owns a graph of **nodes**. It spawns one **worker** agent per node,
and it is the only agent you ever talk to.

This README describes what the skill files say today. The skill files are authoritative. The two closed
efforts under `.scratch/` are their history: many of their earlier nodes describe rules that have
since changed. [History](#history) lists the main ones.

## Why it exists

### The first use case: work too big for one context

Some work is too big for one conversation. It holds many open questions, many decisions that depend on
each other, and code that has to follow from them. Run in one conversation, it fills the context
window, and each compaction loses information. Run across many conversations, it needs someone to
split it, track what was decided and why, and write the notes the next conversation resumes from.

The workflow's design descends from Matt Pocock's `/wayfinder` skill. `/wayfinder` works out the whole
plan first, and leaves the implementation to follow afterwards. `/expedition` works incrementally
instead: decisions, prototypes and implementation are all nodes of one graph, worked as they become
startable. Implementing early often shows that an earlier decision was wrong, so a settled node can be
revised. The aims:

- **Implementation is part of the graph.** An implementation node is first-class, and its code goes
  through an independent checker and a human gate before it lands.
- **The human is the scarce resource.** Workers run in parallel so that there is always one thing
  waiting for the human. The human never has to manage the agents.
- **The manager's context is the first thing to run out.** So most of the context lives in the
  workers, and the manager points at files rather than holding their content. A node that ends with
  the manager knowing everything the worker knew counts as a failure, even if the node resolved.
- **You work from the manager's chat and from code review.** The node files are written for agents.
- **It must work on repositories this machine has never seen.** Nothing assumes a toolchain. The bar's
  commands (build, lint, format, tests) are discovered in each repository rather than declared.

The orchestration shape, one agent talking to the human on behalf of a crew, is borrowed from
[firstmate](https://github.com/kunchenguid/firstmate).

### The second use case: several small things at once on one repository

The second effort (`rename-split-upgrade`) came from a different kind of work. The request that
started it described a feature that led to benchmarking, benchmarks that led to optimisation, an
optimisation that needed a package upgrade, and bugs found along the way. Those tasks were split by
hand, and some conversations grew past the context window and had to be compacted, losing
information.

That effort added two things:

- **Deliverables.** One effort can hold several mostly independent pieces of work. Each piece lands on
  its own branch, as its own pull request or by a local merge. Once a piece has merged, the record it
  no longer needs is cleaned up. This may become the main way of working: one long-running effort that
  small tasks keep being added to, and cleaned out of once merged.
- **Upgrading a conversation.** When an ordinary conversation turns out to be too complex, or to be
  several tasks, you can turn it into an expedition and split the work into nodes.

## The skills

There are three groups. You invoke six of the skills yourself. The manager spawns the five worker
contracts. `repo-docs` stands on its own.

### Skills you invoke

| skill | when to invoke it |
| --- | --- |
| `/expedition` | To start an effort from a conversation, or to manage an existing one in a new session. The conversation's thread becomes the manager. |
| `/expedition-upgrade <request>` | In an ordinary conversation that has grown into an effort. The request names the destination, the deliverables, and a new or existing effort. |
| `/expedition-standing-yes <scope>` | To let the manager take the worker's recommendation, or the checker's `PASS` at a gate, as your answer on items inside a scope you describe in your own words. It can also cover pushing a deliverable's branch or merging a deliverable locally. |
| `/expedition-triage` | When open nodes may have gone stale. The manager checks every open node against the current tree and proposes, in one payload, which are moot, dropped, merged or kept, and which flags to settle. |
| `/expedition-cleanup` | To remove the record of a finished part of the effort (a region cleanup). The manager also proposes one by itself when a deliverable has merged. |
| `/expedition-stop` | When the management session is ending. The manager starts no new node, finishes the work in flight, puts anything waiting in front of you, reports, and stops. The effort stays open. |

### Worker contracts the manager spawns

You never invoke these. Each one is a standalone file that a worker reads when its spawn names it. There
is one per kind of node, plus one for the checker.

| skill | who reads it | what that agent does |
| --- | --- | --- |
| `expedition-grilling` | a grilling worker | Interviews you, through the manager, on a decision only you can make. It writes no file. |
| `expedition-precondition` | a precondition worker | Does work that must happen before something can be decided, such as establishing a fact. It decides nothing and writes no product code. |
| `expedition-prototype` | a prototype worker | Builds a throwaway probe, kept outside the product tree, for you to react to. |
| `expedition-implementation` | an implementation worker | Writes product code in its own git worktree against a written acceptance condition and the bar. It raises only when its premise is broken. |
| `expedition-checker` | the checker | Independently checks finished code against the acceptance condition and the bar. It returns `PASS` or `FAIL`, and it is read-only. |

### `repo-docs`

A standalone skill that keeps a repository's glossary and decision records true as the code changes.
It replaces the dependency on `/domain-modeling`. No expedition file depends on it.

### Supporting files inside `expedition/`

- `glossary.md`: the vocabulary every other file is written in. Its `_Avoid_` lines list the refused
  synonyms.
- `graph-conventions.md`: the format of an effort's files, the statuses and edges, the procedures for
  writing the graph, and the mechanical checks.
- `adoption.md`: how to start an effort from a directory of work that already exists.
- `wayfinder-divergences.md`: what to append to a repository whose tracker doc already describes the
  `/wayfinder` scheme.
- `scripts/frontier.sh`: reads an effort's graph and prints the startable nodes and the slot counts.
  It writes nothing.

`.claude/rules/expedition-triggers.md` is not a skill. The harness loads it automatically when an
agent reads a file matching its `paths:` frontmatter. It holds the manager's trigger-duties and their
priority, so that they survive a compaction of the manager's context.

## How an effort runs

### Starting one

There are three ways in:

- **From a conversation.** Invoke `/expedition` and describe the idea. The manager establishes the
  effort's name, its destination and whether it is expected to reach it, the map's standing
  preferences and ground rules, the label vocabulary, and the first nodes. It asks you for whatever it
  cannot take from what you said.
- **From a conversation already under way.** Invoke `/expedition-upgrade` with a request. Decisions
  already made become resolved grilling nodes, open questions become open nodes, and uncommitted
  changes move into the worktree of a gated implementation node.
- **From existing work (adoption).** Point the manager at a directory of work that already exists,
  such as a `/wayfinder` effort. The effort takes the directory's name. Its questions and decisions are
  imported as nodes by precondition workers, under `adoption.md`.

### The effort's files

Each effort lives in `.scratch/<effort>/`:

```
map.md                       destination, notes, ground rules; every worker reads it
map-manager-only.md          fog, out of scope, landing policy, deliverables, counts
map-implementation-rules.md  the bar's commands and the standards code is held to
map-history.md               superseded map text, kept verbatim
decisions.md                 one short line per resolved node
nodes/NN-<name>.md           one file per node, holding all the detail
```

The manager is the only writer of the record. Nothing in these files is deleted silently: superseded
text is struck through in place, or moved verbatim to `map-history.md`. Graph commits (commits of
these markdown files) are yours to make whenever you like.

### What you do during an effort

The manager keeps exactly one thing awaiting your reply in front of you whenever something is waiting.
Every message it sends ends with a short line saying what is expected of you.

- **Answer the question.** A worker's question arrives with options and a recommendation. A reply such
  as *"ok for recommended"* is a complete answer. *"You decide"* sends that one question back to the
  worker. Deferring a question parks the node, and it keeps the answers you already gave.
- **Judge a gate.** When an implementation node's checker passes, the manager raises a gate pointing at
  the worktree. It does not render the diff in the chat. You answer with one of three outcomes:
  approve (the manager commits with a `Node: <effort>/<NN>` trailer, and the node resolves), correct
  (the worker fixes the work, with no limit on rounds), or reject (implementing the node showed this
  code should not exist).
- **Redirect, if you want.** The manager picks the next node itself and reports it as already started.
  Name a different node in one line to redirect it. Standing steering (a scope or an emphasis) is
  written into the map and binds until you change it.
- **Stop a worker.** Ask in words, naming the node. The manager stops it with `TaskStop`. A worker
  stopped from the task UI is marked as stopped by you, and the manager can no longer resume it.
- **Set the counts.** Two nodes that need you run at once, and two code slots (implementation nodes
  running at once). Either can be changed for an effort. More code slots buy parallel work at the
  price of more merge conflicts.
- **Close the effort.** When the frontier empties, the manager runs a sweep and sends the effort
  closing report. Only you close an effort.

### Deliverables

An effort can declare deliverables in `map-manager-only.md`. Each deliverable has a branch and a base:

- `base: upstream <branch>`: lands by pull request. The manager pushes only on your yes, and you
  create the pull request.
- `base: local <branch>`: lands by a local merge, on your yes. By default it is a rebase and then a
  fast-forward.
- `base: deliverable <name>`: stacked on another deliverable, and lands the way that one lands.

Each implementation node names one deliverable, and its worktree is cut from that deliverable's branch.
Once a deliverable has merged, the manager proposes a region cleanup of its nodes.

## Working on this repository

The root `CLAUDE.md` holds the standards that changes to the skill files are held to: the ground rules,
the rules for writing, and the duty to keep `.claude/rules/expedition-triggers.md` in step with
`expedition/SKILL.md`. Improvements to the workflow are themselves run as expeditions in `.scratch/`.
