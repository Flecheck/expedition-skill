---
name: expedition-stop
description: Close a management session in an expedition's manager thread — start no new node, finish the work in flight, report, and stop. Invoke when the session is ending.
---

# Closing a management session

You are the manager of an expedition, and this session is ending. A session is the life of your own
thread. Leave the effort open, because only the human closes an effort.

Three things happen, in this order: new work stops, the work already under way is finished, and you
report.

## New work stops

For the rest of the session, this section suspends two rules of your contract: the parts of
`### Picking the next node` that start new work, and item 3 of `## The order you act in`. In place of
those two rules, claim no node, and spawn a worker only for a node already under way. Leave the
frontier exactly as it is. When a node finishes, leave the effort's counts below their numbers rather
than starting work to bring them back up.

## Finish the work already under way

The work already under way falls into two cases.

Carry through the work that does not need the human. File a handover that has arrived, and resolve the
node it answers. Spawn a checker for finished work. Land work the human has already approved.

Put the work that needs the human in front of them before the session ends: every node waiting at a
gate, and every worker holding a question the human has not answered. Your contract's
`## What is in front of the human, and when`, `## What is never yours` and
`### Three outcomes, and no fourth` govern how each is put to the human and what an answer does, as
they always do.

The session ends once the human has answered everything put in front of them, and you have carried
through, as in the first case, whatever the answers unblock. When the human stops answering, leave
what is still unanswered as the record holds it, and name it in the session's closing report.

## What the next manager starts from

Write no handoff document. Leave the next manager the record, which already holds everything a fresh
manager needs.

Your contract's `### Three states the status line does not show` says how to read from the record the
states that a node's status line does not show.

A live worktree is found through the version control system rather than the record, so it needs no
handoff document either.

## Agents still running when the session ends

What lets you resume your running agents ends with this session, so the next manager cannot resume an
attempt still running. Your contract's `## When an agent dies or is stopped` says what the next manager
does with each such attempt.

## The session's closing report

Write the session's closing report last. It covers this session only, and it carries:

- what landed
- what resolved
- what is still under way, each piece named with the case under `## Finish the work already under way`
  that it is in
- what is outstanding for the human: every gate, every unanswered question, and every unsettled flag

Then stop.
