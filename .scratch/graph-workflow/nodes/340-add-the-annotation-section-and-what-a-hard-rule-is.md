# Add the annotation section and what a hard rule is to graph-conventions.md

Type: implementation
Status: open
Supersedes: 73, 79
Blocked by: none

## Question

Nodes 73 and 79 each add one passage to `graph-conventions.md`: 73 what kind of thing a hard rule in a worker contract is, and 79 a section for the annotation the manager writes onto a node whose answer a later node changed. Make both in one piece of work.

*Proposed by [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker and filed by the manager, on the human's "ok" to node 330's merge and its conflicts' recommendations. The worker wrote each condition to the recommended option of every conflict.*

*The worker's blockers:* none

## Acceptance condition

*Written by node 330's worker.*

> The work is `.claude/skills/expedition/graph-conventions.md`. No file outside `.claude/skills/expedition/` changes. No file under `.claude/skills/expedition-checker/`, `expedition-grilling/`, `expedition-implementation/`, `expedition-precondition/`, `expedition-prototype/` or `expedition-research/` changes, so `git diff` over those six directories comes back empty. No file under `.scratch/` changes. The file is one the workflow ships, so it is edited plainly. The places named below are the work itself, so this scope came from no search.
>
> Done means every one of the following is true of the finished tree. Each clause names, in brackets, the node its demand comes from.
>
> 1. (79) The section that documents a node file's sections, `## The node file`, gains a statement of one more kind of section a node may carry: an annotation, written by the manager onto a node whose answer a later node has changed the meaning of. It states three things:
>    - an annotation records what a later piece of work changed about this node's answer;
>    - its text is the reporting agent's own words where a reporting agent supplied them;
>    - it is added rather than replacing anything the node already holds.
> 2. (79) It states where an annotation sits relative to the six sections already listed there (`## Question`, `## Acceptance condition`, `## Answer`, `## Flags`, `## Review`, `## Interview`). So the file's rule that sections appear in the order shown, and only when they have content, is true of a node carrying one. Whether the annotation is one section or several, and where in the order it falls, is the worker's to choose and to state.
> 3. (79) It states that an annotation may carry a heading naming what it records, and gives the form of that heading.
> 4. (79) It states that an annotation is the manager's to write and never a worker's. This is consistent with `SKILL.md`'s `## Writing the graph`, which makes the manager the only writer of the graph's record.
> 5. (79) Whatever the file already fixes about a node file is still present afterwards and has lost nothing it required: the mandatory fields, the rule that fields live in the header block and nowhere else, the six section names, and the statement that sections appear in the order shown and only when they have content.
> 6. (73) The file gains one new section, under a heading of the worker's choosing and at most 200 words long, holding all three of the following:
>    - It states that a hard rule in a worker contract binds by being read by the agent the contract was given to, and that no mechanism in the shipped workflow enforces one.
>    - It states the distinction in both directions. A contract says what a worker **may** do, and what a worker **can** do is a property of the harness that ran it. A clause of the first kind survives a change of harness, and one of the second kind does not.
>    - It states the consequence for anyone writing or editing a contract. A rule that would be false on a harness unable to enforce it does not belong in a shipped file. The remedy for a rule agents read down is a better-written rule or a granted exception, never an assumed capability.
> 7. (73, 79) The file's existing headings, listed by `grep -n '^#\{1,6\} '`, are all still present afterwards and in the same order, with the new material added rather than replacing any of them. No existing text is deleted or reworded, except where clause 2 needs the statement of section order to include the annotation.
> 8. The working tree meets the bar.
