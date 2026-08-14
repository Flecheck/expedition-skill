# Expedition

Expedition is a workflow for taking a loose idea all the way to finished code. One manager thread
owns a graph of nodes and spawns one worker per node; the human talks only to the manager. Its
ancestor is Matt Pocock's `/wayfinder`, which it supersedes for efforts it is run on, and it borrows
its one-liaison-behind-a-crew shape from [firstmate](https://github.com/kunchenguid/firstmate).

This glossary is the vocabulary the skill files are written in. It grows only as terms are actually
resolved, and the reasoning behind each one lives in the node that settled it, under
`.scratch/graph-workflow/nodes/`.

## The effort and its graph

**Expedition**:
The workflow itself, invoked as `/expedition`. Where its ancestor charts the way, an expedition
travels it — implementation lives inside the graph rather than downstream of it.
_Avoid_: graph-agent (the repository's name, not the workflow's), wayfinder

**Effort**:
One expedition's worth of work: a single graph, from loose idea to the human closing it. Its files
live in `.scratch/<effort>/`, and its name is that directory's.
_Avoid_: project, run, epic, session

**Graph**:
An effort's nodes and the blocking edges between them.
_Avoid_: plan, backlog, tree

**Node**:
One element of the graph: a single question to decide or a single piece of work to do, sized to one
agent session. Its identity is a sequential `NN` that never changes; its name is free-form.
_Avoid_: issue, ticket, card, item (each names something in a hosted tracker, and a repo may hold
real ones), gap, task

**Map**:
The whole effort at low resolution, read once per session: the destination, the standing notes, the
fog, and what is out of scope. It indexes decisions and never restates one.
_Avoid_: index, plan, README

**Destination**:
What reaching the end of an effort looks like. It fixes the scope, which is what makes work beyond it
out of scope rather than fog.
_Avoid_: goal, objective, definition of done

**Frontier**:
The nodes that are open, unblocked and unclaimed — the work takeable right now.
_Avoid_: backlog, queue, ready

**Fog**:
In-scope work you can tell is coming but cannot yet phrase as a question. Sharpness, not scope, keeps
something here.
_Avoid_: unknowns, TBD, icebox

**Out of scope**:
Work consciously ruled beyond the destination. Both a node status and a section of the map, and it
never graduates into fog.
_Avoid_: retired (that is supersession, a different thing), wontfix, cancelled

**Labels**:
The family or part a node belongs to, so work can be scoped to one area of a large graph. A filter
and never structure: no order may be inferred from a label, and a label is never a node's identity.
_Avoid_: tags, categories

## The actors

**Manager**:
The single long-lived thread that owns the graph: it picks what to work on, spawns one worker per
node, is the only writer of the graph's files, and is the only thing the human ever talks to. It
never answers a question on the human's behalf.
_Avoid_: orchestrator, first mate, coordinator, main thread

**Worker**:
An agent spawned to work exactly one node. It reads the repo, writes no graph file, and never
addresses the human directly. Named for its role rather than for the harness, because the harness is
replaceable.
_Avoid_: subagent, crewmate, subtask (which names the work, not the worker)

**AFK / HITL**:
Whether a node needs the human in order to be worked. An AFK worker needs no live answer to proceed, though
it may still raise a broken premise; a HITL worker cannot finish without the human's own words. Both are
properties of the node's kind rather than of the harness running it.
_Avoid_: autonomous, unattended, automatic, interactive

**Attempt**:
One worker instance on one node. A node outlives its attempts: a dead worker is replaced, and the
replacement is a new attempt.
_Avoid_: retry, run, session

**Checker**:
The second, independent, read-only agent that checks a landed implementation against its acceptance
condition and the bar before the human sees it. It checks against something stated, so it is not a
second opinion. Started by the manager and never by the implementer, because whoever spawns it chooses
what it sees. Its outcomes are `PASS` and `FAIL`, and a `FAIL` names which of the two was not met. It may
instead raise, in which case it issues no verdict at all — its characteristic case is an acceptance
condition that is incoherent or unmeasurable, which it alone ever reads cold.
_Avoid_: reviewer, verifier, auditor — reviewing is the human's; reject — that is the human's word at
the gate

## The five kinds of node

Each names what its worker does, and three of them name a skill the worker invokes.

**grilling**:
A decision only the human can make, reached by interviewing them one question at a time.
_Avoid_: decision, question, interview

**research**:
A fact from outside the working directory, read and reported. Never involves the human.

**prototype**:
A probe built to be reacted to and then discarded. Need not be code, and lives outside the product
tree.

**implementation**:
Product code that lands in the repo and has to be correct. Its worker needs no live answer in order to
proceed and raises only when its premise is broken, and the node ends at the gate.

**precondition**:
Work that must happen before something else can be decided. It decides nothing, probes nothing, and
produces no product code.
_Avoid_: task (every node is a task in ordinary English, and it collides with the word for a worker),
chore, setup

## Working a node

**Claim**:
Taking a node off the frontier before any work starts, so that a concurrent session skips it.

**Handover**:
What a worker returns when it has finished: its node's answer written as the node will hold it, the
index line, its flags, and the nodes it surfaced or invalidated. The manager files it unaltered.
_Avoid_: report (the closing report owns that word), return, payload, deliverable

**Resolve**:
Answering a node's question and writing that answer onto it. The only outcome that satisfies an edge.
_Avoid_: close, done, complete

**Supersede**:
Retiring a node that already holds work by writing a replacement node with a forward pointer to it. A
superseded node does not satisfy an edge, so everything blocked on it stays blocked.
_Avoid_: revise, obsolete, rewrite

**Revision**:
An already-settled node turning out wrong. Handled in place while the node is unstarted, and by
supersession once it holds work.
_Avoid_: correction (a correction round is a different thing), change request

**Cascade**:
An AFK pass that propagates a known revision outward over edges and code, queueing graph edits rather
than interrupting the human.

**Sweep**:
A pass looking for revisions nobody propagated. The same work as a cascade in the opposite direction:
a cascade knows what changed, and a sweep is looking.
_Avoid_: audit, full cascade

**Flag**:
A note a worker leaves recording a judgement the human may want to revisit. It costs nothing until
the effort closes.
_Avoid_: TODO, warning

**Promote**:
Turning a flag, or a one-line note of friction, into a node.
_Avoid_: postpone, defer (both blur into park)

**Acceptance condition**:
What done means for one implementation node, written by the node that spawned it, before any work
starts. Its worker may flag the condition wrong but may not rewrite it.
_Avoid_: definition of done, criteria, spec

**The bar**:
The standing quality properties every implementation must leave the tree meeting — builds, no
warnings, formatted, tests pass where relevant, plus whatever the repo itself demands. Properties
rather than commands: the commands are discovered per repo.
_Avoid_: quality bar, default checks, CI

**Code slot**:
The right to modify product code, held by one worker at a time. Occupancy is discovered from the
working tree rather than recorded, so a dying worker leaves nothing behind to clean up.
_Avoid_: write lock, code lock — there is no lock

## Talking to the human

**Relay**:
The channel and the payload carrying a worker's question to the human and the answer back. The
manager passes both along unaltered and answers nothing itself.
_Note_: firstmate's Relay means external channels like X and Discord, which this workflow rules out
of scope.

**Raise**:
Bringing something to the human that stops work until they act. The gate is the scheduled kind, on a
finished diff. A worker raises an unscheduled one when its premise is broken — the thing that is wrong is
not the worker's to change, the decision changes a lot, or the choice is genuinely too hard to make alone.
Below that line it decides and leaves a flag instead. A raise blocks while keeping the code slot, it
pre-empts grilling work in the manager's queue, and its answer either continues that worker or stops it.
_Avoid_: escalate, interrupt; and *ask*, since a HITL worker's ordinary relayed question is not a raise

**Manager note**:
The manager's own annotation on a relayed question, drawn only from context it already holds.

**Verbatim / paraphrase**:
The two ways a recorded answer can stand — the human's own words, or the manager's rendering of them.
_Avoid_: provenance (an abstraction over a two-valued label)

**Divergence**:
A marker on a recorded answer noting that the human contradicted the recommendation they were given.

**Park**:
The human deferring a live question. The node stores its progress and returns to open, and the
answers it already holds stay banked.
_Avoid_: pause, snooze, postpone

**Banked answer**:
An answer the human has already given, held on a parked node and waiting for a fresh worker. Paid for
once.
_Avoid_: cached, saved

**Interview**:
The record of a HITL exchange on a node — its attempts, and the human's answers with their
verbatim-or-paraphrase standing.
_Avoid_: comments, discussion, log

## Landing code

**Gate**:
The one point on the code path where work stops until the human acts: the manager raises a checked
diff, and nothing is committed until it is approved. It has exactly three outcomes — approval, a
correction round, or a reject — and the manager assembles what it raises out of text others wrote,
never rendering the diff into the conversation.
_Avoid_: review (that is what the human does at the gate), sign-off, PR

**Approval**:
The human's yes at the gate. The only thing that permits a code commit.

**Reject**:
The human's finding at the gate that implementing the node surfaced something meaning its code should
not exist. Not a verdict on quality — a node whose code is merely wrong takes a correction round — so
the node does not resolve, the working tree is cleaned, and what survives is the discovery. The word is
the human's alone; the checker's outcomes are `PASS` and `FAIL`.
_Avoid_: refuse, discard, abandon (which names losing the code, not learning why)

**Salvage**:
The unfinished work saved off a stopped attempt before the working tree is cleaned: a path-limited diff the
manager writes without reading it, kept out of the product tree and linked from whichever node inherits the
work. Saved and never finished — nothing is tidied, made to build, or brought to the bar on its way out.
_Avoid_: stash, WIP, draft, backup

**Correction round**:
One cycle of the human saying what is wrong and the worker fixing it, while the node stays claimed.
Uncapped, and neither a revision nor a check.
_Avoid_: review round, iteration, revision

**Code commit**:
One commit holding only the code a single implementation node produced, limited to that node's paths
and made by the manager on approval.
_Avoid_: landing commit

**Graph commit**:
A commit of an effort's own markdown files, made by the human whenever they like. It passes through
no gate and names no node.
_Avoid_: bookkeeping commit

**Node trailer**:
`Node: <effort>/<NN>` in a code commit's body — the join key between git history and the graph. It
carries the effort because `NN` restarts at `01` for every new effort a repo hosts.

## Closing an effort

**Closed**:
The human's declaration that an effort is over. Only the human closes one; the manager reports that
the conditions hold and nothing more. Most efforts are never closed, and that is a legitimate steady
state.
_Avoid_: done, finished, complete

**Closing report**:
What the manager hands the human once the frontier empties: what was decided, what landed, and every
flag still outstanding.
_Avoid_: completion report, summary
