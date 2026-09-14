---
name: expedition-stop
description: Close a management session in an expedition's manager thread — start no new node, finish the work in flight, report, and stop. Invoke when the session is ending.
---

# Closing a management session

You are the **manager** of an **expedition**, and this session — your own thread's life, not the
effort — is ending. The effort is not being closed: only the human closes one, and nothing here does
that.

Three things happen, in order. You start nothing new, you finish what is already in flight, and you
report.

## Start no new node

From here you **claim nothing, and spawn no worker for a node that is not already under way**. A node
finishing normally has you top up to the effort's counts; now it does not, and a slot a finishing node
leaves empty stays empty. The frontier is left exactly where it is.

## Finish the work in flight

Two cases, split on whether the human is needed.

**Work you can carry through alone, you carry through**: a handover that has arrived is filed, the node
it answers is resolved on it, finished work gets its checker spawned, and work the human has already
approved is landed.

**Work that cannot move without the human goes in front of them before the session ends**, rather than
being left standing: every node waiting at a gate, and every worker holding a question they have not
answered. Both are already tier 1 claimants in your contract's `What is in front of the human, and
when`; that section, `What is never yours` and `Three outcomes, and no fourth` govern how they travel
and what an answer does, unchanged. All a session ending adds is that none of them is left over.

The session ends once they are answered and whatever they unblock is carried through under the first
case above. **What is still unanswered when the human stops answering is left where it stands** —
recorded, and named in the closing report below.

## Write no handoff document

The record already carries what a fresh manager needs, so a handoff document would only copy it. The
three states that read as an ordinary node are each derivable from the node's own file:

- **waiting at a gate** — `claimed`, with a checker's outcome recorded and no gate outcome under it;
- **a worker holding an unanswered question** — `claimed`, with a question recorded and no answer under
  it;
- **parked** — `open`, with a non-empty interview.

A live worktree is discovered from the version control system rather than recorded, so it needs no
handoff either.

## What does not survive, and why it costs nothing

Whatever routes you to your running agents dies with this session, so every attempt still running is
unresumable to the next manager. **That costs nothing**: it is the ordinary replacement case rather
than a loss, and a fresh manager replaces such an attempt by the ordinary route of your contract's
`When an agent dies or is stopped` — everything the human has already said on that node replayed and
marked settled, so they are never asked twice.

## The session's closing report

The last thing you write — this session's, not the effort's. It carries:

- **what landed**;
- **what resolved**;
- **what is in flight**, each named with which of the two cases above it sits in;
- **what is outstanding for the human** — every gate, every unanswered question, every unsettled flag.

Then stop.
