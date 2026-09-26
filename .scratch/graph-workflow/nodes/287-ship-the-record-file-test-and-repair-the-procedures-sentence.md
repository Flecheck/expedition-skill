# Ship the record-file test into the manager's contract and repair the procedures sentence

Type: implementation
Status: superseded
Superseded by: 337

Blocked by: none

## Question

*Surfaced by [node 283](283-what-makes-a-change-to-a-record-file-a-node-rather-than-bookkeeping.md)'s worker, and
pasted as it wrote it.*

> `SKILL.md`'s `## Writing the graph` names two sides — the manager as the record's only writer, and a worker whose
> node's own work is a change to a graph file — and gives no test for which side a change is on. The same passage
> also states that every procedure in `graph-conventions.md` is the manager's and that no worker performs one, while
> `Change the map` has been handed to workers by **seven** acceptance conditions. Write the test in, and repair the
> sentence.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 283's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition/graph-conventions.md`, and no
> other file may be edited. The worker may not mark this node, resolve it, or write a line in `decisions.md` or
> `flags.md`. Done means all of the following are true of the finished tree.
>
> **1.** `SKILL.md`'s `## Writing the graph` section states a test, **decidable by looking at which file a change
> touches and taking no account of the change's content**, with these three branches and no fourth:
>
> - a change to a file the workflow ships — its skill files, its rules files, and its glossary — is a node's work,
>   always, whoever noticed that the file needed changing;
> - a change confined to the files of an effort's own record — its map, the siblings of its map, its history file,
>   its decisions index, its flags index, and its node files — is the manager's own, made with no node, no
>   acceptance condition, no worker, no checker and no gate;
> - where a node of the first kind would otherwise leave the record contradicting what that node ships, the same
>   node's worker makes the record change too, inside that node, named in that node's acceptance condition, so that
>   both land together.
>
> **2.** That section states that **the reverse of the third branch does not hold**: noticing that a record file is
> wrong never makes a shipped-file node, and a defect confined to the record falls in the second branch whatever
> produced it.
>
> **3.** That section **no longer states without qualification** that every procedure in `graph-conventions.md`
> belongs to the manager and that no worker performs one. What stands in its place says that the procedures are the
> manager's **except the one that changes a map file**, which a worker performs in the third branch above and the
> manager performs otherwise.
>
> **4.** The section's existing statement that the manager's sole authorship is about recording rather than about
> files, and that a worker whose node's own work is a change to a graph file makes that change itself, is still
> present, and nothing clauses 1 to 3 add contradicts it.
>
> **5.** `graph-conventions.md`'s `### Change the map` procedure states who runs it, in the same two cases as clause
> 3. Its numbered steps are otherwise unchanged.
>
> **6.** Neither file states how many attempts this took, what it cost, who was wrong, or what the file said before.
> A trigger by which a reader knows a rule applies is not such a statement and stays.
>
> **7.** Only the two named paths are edited. No node file, no status line, and nothing in `decisions.md` or
> `flags.md`.

## The manager's note at filing

*Not a change to anything above.*

**This node is the shipped half of node 283's own carriage, and its author decided that split rather than leaving it
to the manager.** The `map.md` half of that answer is the manager's under the test's own branch 2, and **is not
done** — it is named in the session's closing report as owed.

**The sentence clause 3 repairs was contradicted by seven acceptance conditions at the time it was written**, its
author measured. Whoever claims this should read that as a warning about the shape rather than a curiosity: **a
statement in a shipped file that the workflow's own practice has never matched survived unremarked until a worker
was asked a question that happened to cross it.**

**`graph-conventions.md` is the most contended file on this effort.** One worker measured nineteen open nodes
editing it, another twenty-seven conditions naming it, and several demand it change in no other respect. **Two
workers must not hold it at once**, and [node 288](288-nothing-mechanically-verifies-the-never-delete-bank.md), this
node's sibling, edits it too.

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 337](337-carry-the-record-file-test-the-home-of-a-standing.md), the merge [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole.
