# Say what a `## Review` entry records for a correction round the manager starts at integration

Type: implementation
Status: claimed
Supersedes: 89
Blocked by: none

## Question

`graph-conventions.md`'s `## Review` section, item 2, says each correction round is recorded "with the human's words and what the worker changed". A round the manager starts when integrating the work conflicts has no human's words. What does its entry record instead?

*Reported by [node 363](363-carry-node-162s-integration-answer-into-the-shipped-files.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none".*

## Acceptance condition

*Authored by node 363's worker and filed by the manager. The worker's words: "the wording of what is recorded is this worker's proposal and nothing resolved fixes it; the human may choose otherwise".*

> 1. `.claude/skills/expedition/graph-conventions.md`, in the numbered list under the `## Review` section, item 2 (beginning "Each correction round, numbered, with the human's words and what the worker changed."): it now also says that for a round the manager starts when integrating the node's work conflicts, the entry records the paths of the conflicted files in place of the human's words. The item's second sentence, about how the human's words are recorded, is unchanged.
> 2. ~~No other sentence of any file under `.claude/skills/` changes, and no file under `.scratch/` changes.~~ *Superseded 2026-09-29 by node 366's replacement; see `## Amendment, 2026-09-29 (from node 366)`.*
> 3. Scope: this came from no search, because the place is the work.

## Amendment, 2026-09-29 (from node 366)

*Written by [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s worker and filed by the manager, under the human's answer to node 366's Q3 (`verbatim`: *"ok"*). The worker's own text, pasted:*

Block 4 (defect joined to open node 371, from node 89, clauses originally from node 275). Clauses to add to 371's acceptance condition:
  - `.claude/skills/expedition/SKILL.md` also states what happens to the working state of an implementation node that is superseded while its work has not landed. The graph is edited first. After that, the node's tree, and anything else that holds its unlanded work, is removed, in the same order the file gives for a reject. The file states this as properties rather than as commands of any one version-control tool, and names no command that a repository without that tool could not run.
  - The line in `.claude/skills/expedition/SKILL.md` that reads "reject: edit the graph first, and clean the working state after." still states the reject outcome in the same order: the graph first, the working state after.
  - Scope came from no search: the file named is the place of the work, not an instance of a defect.
  Replacement for 371's clause 2: "No other sentence of any file under `.claude/skills/` changes, except the sentences of `.claude/skills/expedition/SKILL.md` that the clauses carried from node 89 require, and no file under `.scratch/` changes."

## Flags carried here

*The manager's note, 2026-09-29:* flag 89.1, on [node 89](89-carry-worktree-lifecycle-into-managers-contract.md), judges the clauses this node took from node 89 ("Node 275's clean-up clauses were filed on this open, unclaimed node without asking the human first"). It stays outstanding on node 89 and settles at this node's gate.
