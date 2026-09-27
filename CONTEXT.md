# Expedition

Expedition is a workflow that takes a loose idea all the way to finished code. One manager thread
owns a graph of nodes and spawns one worker per node. The human talks only to the manager.
Its ancestor is Matt Pocock's `/wayfinder`, and Expedition replaces `/wayfinder` on the efforts
Expedition is run on. From [firstmate](https://github.com/kunchenguid/firstmate) it takes this design:
one agent talks to the human on behalf of a crew of agents.

This glossary defines the words the skill files are written in. A term is added only when the node
that settles it resolves. The reasoning behind each term is in the node that settled it, under
`.scratch/graph-workflow/nodes/`.

## The effort and its graph

**Expedition**:
The workflow itself, invoked as `/expedition`. Its ancestor works out what the work is, and leaves the
implementation to follow afterwards. An expedition also implements the work, as nodes inside its own
graph.
_Avoid_: graph-agent (the repository's name, not the workflow's), wayfinder

**Effort**:
One expedition's work: a single graph, from a loose idea until the human closes the effort. Its files
are in `.scratch/<effort>/`, and the effort's name is the name of that directory.
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
An outline of the whole effort: the destination, the standing notes, the fog, and what is out of
scope. It is more than one file, and no reader reads all of it. Every worker reads one part of it
once per node, and that part holds what every worker can act on. Material that only one kind of
reader acts on is kept in another file beside that part. The map points to decisions and does not
restate them.
_Avoid_: index, plan, README

**Destination**:
What the end of an effort looks like. It fixes the scope, so work beyond the destination is out of
scope and is not fog. It also says, in one line, whether the effort is expected to reach its
destination. Where the effort is not expected to reach it, that line tells a manager that a frontier
that is not empty is the effort's steady state and not a defect.
_Avoid_: goal, objective, definition of done

**Frontier**:
The nodes that are open, unblocked and unclaimed: the work that can be taken now.
_Avoid_: backlog, queue, ready

**Fog**:
In-scope work that is known to be coming but cannot yet be phrased as a question. Work stays in the
fog until it can be phrased as one.
_Avoid_: unknowns, TBD, icebox

**Out of scope**:
Work deliberately ruled to lie beyond the destination. It is both a node status and a section of the
map. Work that is out of scope stays out of the fog.
_Avoid_: retired (that is supersession, a different thing), wontfix, cancelled

**Labels**:
The family or part a node belongs to, so that work can be limited to one area of a large graph. A
label only filters nodes. No order may be inferred from a label, and a label is never a node's
identity.
_Avoid_: tags, categories

## The actors

**Manager**:
The single long-lived thread that owns the graph. It picks what to work on, spawns one worker per
node, is the only writer of the graph's record, and is the only thing the human ever talks to. A
question put to the human is the human's to answer, and the manager never answers one on the human's
behalf. The record is every answer, status, index line and flag, and the manager alone writes it.
Other text in the graph's files is not part of the record.
_Avoid_: orchestrator, first mate, coordinator, main thread

**Scribe**:
How the manager writes. It pastes what an agent handed back under the right heading, as it was
handed back. It never re-authors, shortens, re-orders or re-renders that text. Anything of its own
goes beside that text, as its own marked note. The manager may assemble pasted pieces: put them in
order, join them into one continuous text, and extract a block of text to hand to somebody else. It
may not rewrite the pieces into a gloss.
_Avoid_: editor, curator, secretary

**Worker**:
An agent spawned to work exactly one node. It reads the repo, does none of the graph's bookkeeping,
and never addresses the human directly. Anything it has for the human goes through the manager.
Where its own node's work is a change to a graph file, the worker makes that change itself, and the
recording stays the manager's. It is named for its role, not for the harness, because the harness can
be replaced.
_Avoid_: subagent, crewmate, subtask (which names the work, not the worker)

**AFK / HITL**:
Whether a node needs the human in order to be worked. An AFK worker needs no live answer to proceed,
though it may still raise a broken premise. A HITL worker cannot finish without the human's own
words. Both are properties of the node's kind, not of the harness that runs it.
_Avoid_: autonomous, unattended, automatic, interactive

**Attempt**:
One worker instance on one node. A node lasts longer than any of its attempts: a worker that dies is
replaced, and the replacement is a new attempt.
_Avoid_: retry, run, session

**Checker**:
The second, independent, read-only agent that checks a finished implementation against its acceptance
condition and the bar before the human sees it. It checks against something stated, so it is not a
second opinion. The manager starts it, and the implementer never does, because whoever spawns it
chooses what it sees. Its outcomes are `PASS` and `FAIL`, and a `FAIL` names which of the two was
not met. It may raise instead, and then it gives no outcome at all. The typical reason it raises is an
acceptance condition that is incoherent or unmeasurable. The checker is the only agent that reads the
condition without having read the node.
_Avoid_: reviewer, verifier, auditor (reviewing is the human's), reject (the human's word at the
gate)

## The five kinds of node

Each kind names what its worker does.

**grilling**:
A decision only the human can make, reached by interviewing them. Its worker may put several of its
own questions in one payload. Two questions share a payload only where neither's answer depends on the
other's. A question whose answer depends on another question in that payload is held for a later
payload.
_Avoid_: decision, question, interview

**research**:
A fact from outside the working directory, read and reported. Its ordinary work is done without the
human. Its worker may raise where the node's premise is broken.

**prototype**:
A probe built to be reacted to and then discarded. It need not be code. It is kept outside the
product tree.

**implementation**:
Product code that lands in the repo and has to be correct. Its worker needs no live answer in order to
proceed, and raises only when its premise is broken. Its gate is the last point at which the human can
act on it. The node continues after its gate: after approval the manager commits the work and lands
it, and the node resolves after that.

**precondition**:
Work that must happen before something else can be decided. It does only that work: it decides
nothing, probes nothing, and produces no product code.
_Avoid_: task (every node is a task in ordinary English, and it is too close to the words used for a
worker), chore, setup

## Working a node

**Claim**:
Taking a node off the frontier before any work starts, so that a concurrent session skips it.

**Handover**:
What a worker returns when it has finished, in seven parts: its node's answer written as the node
will hold it, the index line, its flags, the new nodes it found, which resolved node its work changes,
the open conditions it searched and any replacement clauses it wrote, and what `map.md` did not tell
it. An implementation worker returns an eighth part, the gate payload. The manager files it unaltered.
_Avoid_: report (the closing report uses that word), return, payload, deliverable

**Resolve**:
Answering a node's question and writing that answer onto it. The only outcome that satisfies an edge.
_Avoid_: close, done, complete

**Supersede**:
Retiring a node by a forward pointer to the node that replaces it or makes it unnecessary. A
superseded node does not satisfy an edge, so everything blocked on it stays blocked.
_Avoid_: revise, obsolete, rewrite

**Revision**:
An already-settled node that turns out to be wrong. It is handled in place where the node still needs
to exist, and by supersession where it does not.
_Avoid_: correction (a correction round is a different thing), change request

**Cascade**:
An AFK pass that propagates a known revision outward along edges and into code. It queues graph
edits and does not interrupt the human.

**Sweep**:
A pass that looks for revisions nobody propagated. It is the same work as a cascade, done in the
opposite direction: a cascade starts from a known change, and a sweep searches for changes.
_Avoid_: audit, full cascade

**Flag**:
A note recording a judgement that an agent made on its own and that the human may want to revisit.
The agent is usually a worker, and it is the manager where a judgement of the manager's own went into
the graph. Raising a flag blocks nothing. A flag is settled at the first moment, after its node's
worker has handed back, at which the node is put in front of the human. That moment is an
implementation node's gate where the node has one, and otherwise the pick report that closes the
node. A flag goes into the closing report only where the human never spoke again.
_Avoid_: TODO, warning

**Promote**:
Turning a flag, or a one-line note of a difficulty met while working, into a node.
_Avoid_: postpone, defer (both are too close in meaning to park)

**Acceptance condition**:
What done means for one implementation node, written before any work starts. Its worker leaves it as
written, and may not rewrite it. Where an agent created the node, that agent writes the condition.
Where the manager created the node, the manager writes it. Where the worker judges the condition
wrong, the worker raises the matter, and does not raise a flag of its own. The `CONDITION-WRONG`
flag is the manager's to file, and only where the human answered that raise by saying to carry on and
ship anyway.
_Avoid_: definition of done, criteria, spec

**The bar**:
The standing quality properties that every implementation must leave the tree meeting: it builds, it
has no warnings, it is formatted, the relevant tests pass, and whatever else the repo itself demands
is met. The bar is a list of properties. The commands that check them are discovered in each repo.
_Avoid_: quality bar, default checks, CI

**Code slot**:
The right to modify product code. How many code slots an effort runs is that effort's own setting, one
worker to a slot, and the number may be more than one. A slot's occupancy is discovered by counting
the live worktrees, one per claimed implementation node, rather than by inspecting the working tree
for uncommitted changes.
_Avoid_: write lock, code lock — there is no lock

## Talking to the human

**Relay**:
The channel and the payload that carry a worker's questions to the human and the answers back. One
payload holds one or several of that worker's questions, and it is one thing in front of the human
either way. A payload carries the questions of one worker only. The manager passes the questions and
the answers along unaltered, and answers nothing itself.
_Note_: firstmate's Relay means external channels like X and Discord, which this workflow rules out
of scope.

**Raise**:
An agent putting something to the human. Whether a raise waits depends on its channel. A worker's
raise stops its work until the human acts. A checker's question, handed back alongside its outcome,
does not wait for the human. A flag waits for the moment that closes its node: an
implementation node's gate, or the pick report. The gate is the scheduled form of a blocking raise,
made on a finished diff. A worker opens an unscheduled blocking raise when its premise is broken: the
thing that is wrong is not the worker's to change, the decision changes a lot, or the choice is
genuinely too hard to make alone. Where none of these holds, the worker decides and leaves a flag
instead. A blocking raise holds the code slot while it waits, and is put ahead of grilling work in the
manager's queue. Its answer either continues that worker or stops it.
_Avoid_: escalate, interrupt, and *ask* (asking is the ordinary work of a worker built to question the
human, and a raise is what a worker meant to work mostly by itself does when it needs input it does
not have)

**Manager note**:
The manager's own annotation on a relayed question, drawn only from context it already holds.

**Verbatim / paraphrase**:
The two forms a recorded answer can take: the human's own words, or the manager's rendering of them.
_Avoid_: provenance (an abstraction over a two-valued label)

**Divergence**:
A marker on a recorded answer noting that the human contradicted the recommendation they were given.

**Park**:
The human deferring a live question. The node stores its progress and returns to open, and it keeps
the answers it already holds as banked answers.
_Avoid_: pause, snooze, postpone

**Banked answer**:
An answer the human has already given, held on a parked node and waiting for a fresh worker. The human
is not asked for it a second time.
_Avoid_: cached, saved

**Interview**:
The record of a HITL exchange on a node: its attempts, and the human's answers, each marked verbatim
or paraphrase.
_Avoid_: comments, discussion, log

## Landing code

**Gate**:
The one point on the code path where work stops until the human acts. The manager raises a checked
diff, and nothing is committed until the diff is approved. The gate has exactly three outcomes:
approval, a correction round, or a reject. The manager assembles what it raises out of text others
wrote, and does not render the diff into the conversation.
_Avoid_: review (that is what the human does at the gate), sign-off, PR

**Approval**:
The human's yes at the gate. The only thing that permits a code commit.

**Reject**:
The human's finding at the gate that implementing the node revealed that its code should not exist.
A reject is not a verdict on quality: a node whose code is merely wrong takes a correction round. On a
reject the node does not resolve, and the manager removes that node's worktree and deletes its branch.
Where the human asks for the work to be kept, it is committed onto that branch before the directory is
removed. What is kept is the discovery. The word is the human's alone; the checker's outcomes are
`PASS` and `FAIL`.
_Avoid_: refuse, discard, abandon (which names losing the code, not learning why)

**Salvage**:
The unfinished work saved from a stopped attempt before the working tree is cleaned. It is a
path-limited diff that the manager writes without reading. It is kept out of the product tree, and
linked from the node that takes over the work. It is saved and never finished: nothing in it is
tidied, made to build, or brought to the bar when it is saved.
_Avoid_: stash, WIP, draft, backup

**Correction round**:
One cycle of the human saying what is wrong and the worker fixing it, while the node stays claimed.
The number of rounds has no limit. A correction round is not a revision, and it is not a check.
_Avoid_: review round, iteration, revision

**Code commit**:
One commit holding only the code a single implementation node produced, limited to that node's paths
and made by the manager on approval.
_Avoid_: landing commit

**Graph commit**:
A commit of an effort's own markdown files, made by the human whenever they like. No gate applies to
it, and it names no node.
_Avoid_: bookkeeping commit

**Node trailer**:
`Node: <effort>/<NN>` in a code commit's body. It is the key that joins git history to the graph. It
carries the effort because `NN` restarts at `01` for every new effort a repo hosts.

## Starting an effort

**Starting an effort**:
The act that creates an effort. The manager performs it, and it happens before the graph exists. It
produces the effort's files and its first nodes. It has two inputs: a conversation with the human, or
a directory of work that already exists. The input is the only thing the two ways of starting differ
in.
_Avoid_: charting (this workflow's cartographic metaphor stops at the map, and every act beneath it is
described plainly; and the word names what the workflow's ancestor does when it "works out what the
work is", rather than anything this workflow performs), kickoff, onboarding, bootstrap, setup, init

**Adoption**:
Starting an effort from a directory of work that already exists. It is a way of starting an effort,
not a kind of node. It carries steps that starting from a conversation does not: taking the effort's
name from the directory that already exists, resolving any reserved graph name the directory already
uses for something else, deriving the map from the record the effort already wrote rather than from a
conversation, declaring the label vocabulary from the foreign label families, and minting the bulk
import as `precondition` nodes.
_Avoid_: migration (which names moving data, not taking on an effort), import (importing is one step
inside adoption, not the act itself), onboarding, port

## Closing an effort

**Closed**:
The human's declaration that an effort is over. Only the human closes one; the manager reports that
the conditions hold and nothing more. An effort whose destination says it is not expected to end, and
whose frontier never empties, is in a legitimate steady state rather than a stalled one, and is not to
be treated as a defect.
_Avoid_: done, finished, complete

**Closing report**:
What the manager hands the human once the frontier empties. It covers only what the human has not
already seen. It carries what landed, the supersession chains, the state of the bar, every flag still
outstanding, what the sweep found, and every sweep round.
_Avoid_: completion report, summary
