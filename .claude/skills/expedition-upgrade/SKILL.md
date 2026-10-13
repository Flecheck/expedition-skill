---
name: expedition-upgrade
description: Upgrade a conversation into an expedition. The human invokes it, with a request, in a conversation that was not started as an expedition, to turn that conversation into an expedition whose manager is the conversation's own thread.
---

# Upgrading a conversation into an expedition

The human has invoked this skill, with a request, in a conversation that was not started as an
expedition. This conversation's own thread becomes the manager of an effort.

Read the manager contract now. It is the `SKILL.md` of the skill `expedition`. Act as the manager from
then on. From the upgrade on, do no node's work yourself. The work this conversation began goes on as
nodes, with one worker spawned for each node.

This file holds only the steps an upgrade adds to the manager contract. Terms are used exactly as the
glossary, `glossary.md` beside the manager contract, defines them.

## What the request names

The request names three things:

- the destination;
- the deliverables;
- the effort, either a new effort or an existing effort named by its name.

Where the request leaves the destination unstated, ask the human for it. Do the same where it leaves
unstated whether the effort is expected to reach its destination, or which deliverables there are.
Write none of these three yourself.

## Your steps, in order

1. **Let running agents finish.** Background agents still running in the conversation finish before
   the upgrade starts. What they return counts as part of the conversation.
2. **Start the effort, or add to an existing one.**
   - For a new effort, start it as the manager contract's `## Starting an effort` describes, with the
     conversation as its starting point.
   - For an existing effort, add the deliverables and the nodes to that effort. Each new node takes the
     next unused node number. Only one thread manages an effort at a time. So before invoking the
     upgrade, the human ends the management session of any other thread managing that effort, with
     `/expedition-stop`.
3. **Declare the deliverables**, as `### Declaring a deliverable` in the manager contract says, and as
   `### A branch that already exists` below changes it.
4. **Carry the conversation into the record**, as `## What is carried into the record` below says.
5. **Carry the work already done or under way**, as `## Work already done or under way` below says.
6. **Check each existing branch declared as a deliverable's branch**, as
   `### A branch that already exists` below says.

Write the record so that the effort needs nothing from the conversation once the upgrade is done. A
later compaction of this thread's context, or the end of its management session, then loses nothing
the effort needs.

## What is carried into the record

- **Decisions already made.** They go into one `grilling` node, written as resolved. Where the
  conversation did several unrelated things, they go into a few such nodes instead, one for each
  thing. The human's words are the node's answer. Where the human assented to a recommendation of
  yours, keep the recommendation beside the assent, marked as yours.
- **Questions still open.** They become open `grilling` nodes, grouped as grilling nodes usually are. A
  node may hold more than one question.
- **Choices you made without the human's agreement.** Each becomes an `ASSUMPTION` flag on the node
  whose decision it bears on. Record it as your own choice, and never as the human's decision.
- **Findings that took real effort.** A finding that exists only in the conversation and took real
  effort to obtain, such as a benchmark result, goes into one file in the effort's directory. Link that
  file from the map's `## Notes`, and mark it there as your own work.

Leave out the conversation's chronology. Leave out facts that can be read again from the working tree.

How the rest of the work splits into nodes is yours to read from the conversation.

### The human's words, where the conversation was compacted

Check whether the environment keeps a full transcript of the conversation. Do not assume that it does.

Where a transcript exists, mint a `precondition` node whose work is to read it. Its worker reads the
transcript, and you do not. The worker takes out of it the human's words and the decisions already
made, and marks each `verbatim`, with the transcript cited as its source. Write the nodes of decisions
already made from what that worker hands back.

This changes, for an upgrade, the rule in `### The human's words` in the manager contract. That rule
marks a reply `paraphrase` whenever the human's words are no longer in your context. In an upgrade
with a transcript, words that are no longer in your context are taken from the transcript, and are
marked `verbatim`.

Where no transcript exists, `### The human's words` applies unchanged.

## Work already done or under way

### Commits made before the upgrade

They stay as they are. No node is linked to them.

### A branch that already exists

A branch that already exists may be declared as a deliverable's branch. It then takes the place of a
branch created from the deliverable's base. The deliverable's entry still names a base, in any of
the three forms `## The graph's files` in `graph-conventions.md` gives.

This changes, for an upgrade, the rule in `### Declaring a deliverable` in the manager contract. That
rule creates every deliverable's branch from the current tip of its base. In an upgrade, a deliverable
may instead take a branch that already exists, and no branch is created for it.

Once the rest of the upgrade is done, check the following about each such branch:

- For a deliverable that lands by pull request, the branch holds no commit of the effort's own record.
  A commit of the record would otherwise reach the pull request.
- For every such branch, the main checkout does not have it checked out. The main checkout's graph
  commits would otherwise land on it.

Where a check does not hold, ask the human what to do. Change neither the branch nor the checkout
yourself.

### Uncommitted changes

Uncommitted changes in the conversation's working tree, outside the effort's own record, move into the
worktree of a new `implementation` node. Once they are in that worktree, the conversation's working
tree no longer holds them.

That node names one deliverable: the one the request ties this work to. Where the request leaves it
unclear, ask the human which deliverable it is.

Write the node's acceptance condition yourself, as the manager contract's `## Acceptance conditions`
says for a node you minted. The condition covers the whole change, including the part written before
the upgrade. The change then goes through the checker and the gate like the work of any other
implementation node.

### Planned work

Work that was planned in the conversation and not started becomes open nodes.
