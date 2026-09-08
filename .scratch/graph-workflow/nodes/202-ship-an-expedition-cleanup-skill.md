# Ship an `expedition-cleanup` skill

Type: implementation
Status: open

Blocked by: 201

## Question

*Surfaced by [Pruning a long-running effort's map](70-pruning-a-long-running-map.md)'s worker, and pasted as it
wrote it.*

> The human asked for cleanup to be an invoked skill on the model of `expedition-stop`, with two operations:
> removing a finished subject region the human names, and removing settled entries from the flag index. Ship it.

**Blockers, in the worker's words:** *"new node 1 above"* — which is [node
201](201-ship-the-cleanup-exemption-and-the-flag-check.md). Its ground is flag `70.5`: the settled-flag operation
makes the graph fail a mechanical check the same workflow ships, so the check is amended before the skill that
breaches it exists.

**The human's own words that fixed the shape**, `verbatim`, at node 70's interview:

> For the action of doing the cleanup I would see like the stop skill, a cleanup skill. For the cleanup skill, it is
> designed to delete things so it should be fine.

And, settling the second operation, `verbatim`: *"do cleanup flags"*.

## Acceptance condition

*Written by node 70's worker. Pasted as it wrote it, and not the manager's.*

> The work is a new skill under `.claude/skills/expedition-cleanup/`. Done means every one of the following is true
> of the finished tree.
>
> 1. A file `.claude/skills/expedition-cleanup/SKILL.md` exists, with the frontmatter shape the sibling
>    `expedition-*` skills use, and a description saying it is invoked in an expedition's manager thread to remove
>    record that a finished part of the effort no longer needs.
> 2. It states the standing rule it is an exception to, in its own words — that an edit to a file of the effort's
>    record never deletes, superseded text being marked and left where it is — and states that the rule guards
>    against removal that is unannounced, so an invoked act whose declared purpose is removal falls outside it.
> 3. It describes **two operations**, each given a distinct name, and states that each is invoked separately and
>    that neither implies the other.
> 4. For the first operation, removing a finished region, it states all of the following:
>    a. the region is named by the human in their own words, describing a part of the effort's subject matter whose
>       work is finished, and the skill never judges on its own that a region is finished;
>    b. the skill proposes the set of nodes it reads that naming to mean and presents that set for the human's
>       confirmation or amendment, and removes nothing before that confirmation;
>    c. three conditions the proposed set must meet, with the skill removing nothing from a set failing any of them:
>       every node in the set is resolved; nothing outside the set — no remaining node, and no other file of the
>       record — refers to any node in it; and the human has confirmed the set;
>    d. where a declared grouping field is present on nodes it may be used to propose the set faster, and that it is
>       never required, most efforts having few or none;
>    e. the operation reaches every file of the effort's record, removing the part of each attributable to the
>       region, and is not confined to the node files;
>    f. what is removed is each node's account of what happened, and what is left in its place is a single entry
>       naming the region as the human named it, the identifiers of the nodes removed, and the fact that the removed
>       text remains recoverable from the effort's version control history;
>    g. text stating a rule that currently binds is never removed by this operation, and the reason as a property:
>       such text is held in the effort's rule files rather than on a node, so it is not in a region to begin with.
> 5. For the second operation, removing settled flag entries, it states all of the following:
>    a. the effort's flag index carries one line per flag with its state, and the report built from it is the lines
>       not yet settled;
>    b. the operation removes the lines whose flag is settled and leaves the lines whose flag is outstanding;
>    c. nothing is lost, because a flag's prose and its settled marking both live on the node that raised it, and
>       the operation does not modify that node;
>    d. removing a settled line is not a mismatch against the mechanical check joining a node's flag entry to its
>       index line.
> 6. It states that the skill removes nothing on a criterion of age, of how long a file has grown, or of text having
>    been marked superseded — the two operations above are the whole of what it does.
> 7. **It assumes no particular repository, machine, or toolchain**, names no plugin, requires no skill to be
>    invocable, and names no command. Where it must refer to a commit, to version control, or to searching the
>    record, it states the property and not the command.
> 8. It addresses the manager throughout. Where an operation requires the human's confirmation it directs the
>    manager to obtain it, and it instructs no agent other than the manager to address the human.
> 9. It is at most 5,000 bytes.
> 10. No file outside `.claude/skills/expedition-cleanup/` is created or modified.
> 11. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This is the second file the workflow has not written yet to reach the frontier**, the other being [node
166](166-ship-an-expedition-stop-skill.md)'s stop skill, which the human named as this one's model and which is
still open. Under the priority order they approved, *the files the workflow has not written yet* is the only group
that moves toward the destination — so this node sits in that group rather than in the shipping backlog.

**Its clause 4(g) is what [node 189](189-where-the-never-delete-rule-stops.md) bought.** Before that node resolved,
a region's nodes could hold text stating a rule that bound the whole effort, and removing the region would have
taken it. Node 189's cut moved such text off the nodes and into the rule files, so the guarantee is structural
rather than a caution the skill has to enforce. Its author put it as *"closed by construction rather than by
care"*.

**Its clause 9's 5,000-byte cap is the author's own** and is not drawn from any rule of this effort's. The manager
records that it was chosen rather than derived, so a worker that finds it binding has somewhere to point.
