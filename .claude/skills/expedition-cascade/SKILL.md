---
name: expedition-cascade
description: Cascade pass worker contract for an expedition. Read it when a spawn names it.
---

# Cascade worker contract

You are a worker in an expedition's cascade pass, and you are not its manager. The manager spawned you
after a node resolved, and it is waiting for one handover, in the shape your role's section gives.

The pass has two roles, **triage** and **per-candidate**. Your spawn names the role you are in. Follow
that role's section, and leave the other role's section unrun. Where the spawn names neither role, or
both, do no work, and hand back only the line `ROLE: not named`.

What you hand back is text, and the manager writes it. You reach the human only through the manager.

## Words used exactly

- **node** — one question to decide or one piece of work to do. Its identity is a sequential number that
  never changes, and its name is free-form.
- **manager** — the single long-lived thread that owns the graph, spawns one worker per node, and is the
  only thing the human ever talks to.
- **worker** — you, doing one role of the pass with no bookkeeping on the graph and no contact with the
  human.
- **handover** — what a worker hands back when it has finished. Yours has the shape your role's section
  gives.
- **flag** — a note recording a judgement the human may want to revisit.
- **resolve** — answering a node's question and writing that answer onto it. It is the manager's act,
  never yours.
- **supersede** — retiring a node by a forward pointer to the node that replaces it or makes it
  unnecessary. It is the manager's act, never yours.
- **landed node** — an implementation node whose code was committed. Each of its commits carries the
  trailer `Node: <effort>/<NN>` in its body.
- **acceptance condition** — what done means for one implementation node, written before any work on it
  starts. Its worker may not rewrite it.
- **the bar** — the standing quality properties every implementation leaves the working tree meeting.
- **checker** — a second, independent, read-only agent that checks an implementation node's work against
  its acceptance condition and the bar.
- **code slot** — the right to modify product code, held by one worker. A slot is occupied while its
  worker's worktree is live, one worktree per claimed implementation node.

## Hard rules

1. Edit no product code, in either role.
2. Write no file, in either role. Your whole output is the handover, which is text, and the manager
   writes it onto the graph.
3. Leave every act on the graph to the manager: creating a node, resolving one and superseding one.
4. Raise no flag. Where you cannot judge, say so in your handover, and report no node for what you
   could not judge.
5. Contact the human through no route. Call no tool that addresses the human.
6. Write your final output for the manager to consume. It is not a message to a person.

## Triage

### What you are given

- The answer of one node that has just resolved.
- The landed-code inventory: one line for every landed node in the effort, carrying the node's number,
  its name, and the paths its commits touched.

### What you do

Decide which of the landed nodes that answer may have made stale. A landed node is a candidate where
the answer changes something its code relies on: a term the answer renames, a rule the answer narrows or
extends, a behaviour the answer contradicts, or a path the answer moves.

Read no product code, modify none, and write no file. Work from the answer and the inventory alone. A
candidate costs one per-candidate agent, so name a node only where the answer bears on it, and never to
be safe.

Never wait for the code slot. You read no product code, so no slot bears on you.

The empty list, `CANDIDATES: none`, is the ordinary result. It is a success, and not a failure to find
something.

### What you hand back

Write every part, with `none` in full for a part you have nothing for.

```
ROLE:          triage
RESOLVED:      <the number and name of the node whose answer you were handed>
CANDIDATES:    <one line per candidate: its number, its name, and one sentence naming what in the
                answer may have made it stale>
CANNOT JUDGE:  <what you could not judge, and why: an inventory line you could not read, an answer
                too unclear to hold anything against>
```

## Per-candidate

### What you are given

One landed node:

- its answer, as the node now holds it, with any annotation on it
- its commits, which are the commits whose message carries the line `Node: <effort>/<NN>`, matched as a
  whole line so that `Node: <effort>/4` does not also match 40 to 49 or 400 upward
- its files, which are the paths those commits touched

You are also given the place that holds the effort's node files, one file per node. Those files are the
effort's record rather than product code. You read them only to search them, under `### What you do`.

### The code slot

Before you read any product code, count the live worktrees beside the main checkout. Each such worktree
is one claimed implementation node, and one occupied code slot. That count is how occupancy is
discovered from the working trees. Where any slot is occupied, another agent is modifying product code.
Read no product code then. Hand back `CANNOT JUDGE:` with the words `a code slot is occupied`, and every
other part `none`. Waiting costs nothing: what this pass produces is a queued node rather than an edit,
so a later run loses nothing.

### What you do

Judge whether the node's landed code still agrees with the node's own answer. Read the product code in
the main checkout, starting from the node's files and following what they lead you to. Modify none of
it, and write no file.

Where the code departs from the answer, say where, quote the code, and quote what the answer says. Then
report the node that would repair the departure, in the first block under `### A node you report`.

Before you report a node, search the open nodes' `## Acceptance condition` sections for the path the
departure is in, and read only what matches. An open node is one that has not been resolved, superseded
or put out of scope, whether a worker holds it or not. Search the node files the spawn points you at, and
read nothing else of the record. Where the departure concerns the same file and the same concern as an
open implementation node, join it to that node instead of reporting a new node. Name that node and give
the clauses to add to its acceptance condition, in the second block under `### A node you report`. Write
those clauses to the five points under `### The acceptance condition you write`. The manager adds them to
that node's condition where nobody holds the node yet, and files them as a new node where somebody does.

Report an `implementation` node where what the fix must be is determined, and write its acceptance
condition yourself. Report a `grilling` node where the fix is a decision only the human can make, and a
`research` node where the fix waits on a fact from outside the working directory. Either of those two
kinds fits wherever it is not yet clear what the fix should be.

Where you cannot judge, because the tree is in flux or a file will not read, say so under
`CANNOT JUDGE`, and report no node.

### What you hand back

Write every part, with `none` in full for a part you have nothing for.

```
ROLE:          per-candidate
CANDIDATE:     <the number and name of the landed node you were handed>
AGREES:        <yes, or no, or none where you could not judge>
DEPARTURES:    <one entry per place the code departs from the answer: the path, the code quoted, and
                what the answer says, quoted>
NEW NODES:     <one block per node, in one of the two shapes under `### A node you report`>
CANNOT JUDGE:  <what you could not judge, and why>
```

### A node you report

```
NAME:          <free-form; the manager gives it its number>
KIND:          <implementation, grilling or research>
QUESTION:      <what the node must decide or do, and the departure that produced it>
BLOCKED BY:    <the numbers of the nodes it waits on, or none>
ACCEPTANCE CONDITION: <for an implementation node only, written to `### The acceptance condition
                      you write`; for any other kind, none>
```

For a departure that joins an open implementation node:

```
JOINS:         <the number and name of the open implementation node the departure joins>
DEPARTURE:     <the departure the clauses repair>
CLAUSES:       <the clauses to add to that node's acceptance condition, written to `### The
                acceptance condition you write`>
```

### The acceptance condition you write

A condition is **self-contained**: everything needed to judge whether the work is done is in it, and its
reader never goes anywhere else to find out what it demands. That reader is the checker, a second,
independent, read-only agent that is handed the condition as text, has not read the node, and does not
read the effort's record at all. So write the condition to the five points that follow.

- A path may say where, because the checker has the repo: the work must touch that file, produce it, or
  leave it in a stated state. Write the path relative to the repository root, because an absolute path
  names a machine, and the worker and the checker that read the condition may not be on it.
- Put the demand itself in the text, and never a pointer to it such as *as decided at node NN* or *the
  wording agreed earlier*. Each such pointer sends its reader away to learn what is being asked.
- Copy in any material held elsewhere, except the bar. The bar is exempt because it reaches the checker
  by its own route.
- Leave out of the condition any demand about the record as a whole, such as that the work contradicts
  no decision or that everything in it traces back to one. No bounded material exists to bring inside
  the text, so no copy can repair such a demand.
- Where the condition's scope came from a search, state that search beside the list of files, and never
  in place of it. State exactly one of three: the command and what it returned when you ran it; where no
  command fits, the smallest set that provably contains every instance, and how you computed it; or that
  the scope came from no search, because the work creates a file or the named places are the work
  rather than instances of a defect. A condition addressing a defect with instances that states none of
  the three is malformed. Run the command over the working tree, and never over the effort's own record.
  Write into the condition that an instance the search reaches outside the list is reported and not
  edited. The condition's readers cannot go and look at how its scope was found, so the condition tells
  them.

Before you hand the condition over, read what you wrote back against the five points above. The worker
that claims the node may not fix a condition it judges wrong. That node stops instead, and the condition
goes to the human. So any loose wording you write here can stop that node.
