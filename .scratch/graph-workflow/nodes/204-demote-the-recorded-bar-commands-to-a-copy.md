# Demote the recorded bar commands to a copy confirmed against the repo, in the implementer's and the manager's contracts

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [Which statement of the bar's commands wins where a recorded copy and the repo's own
instructions disagree](174-which-statement-of-the-bars-commands-wins.md)'s worker, and pasted as it wrote it.*

> The implementer's contract tells its worker to use whatever the implementation-rules
> file records for this repo and to discover the commands only where that file records none, so the
> recorded copy is authoritative for it. The checker discovers from the repo. The manager's contract
> states the trusted-copy model twice more and still offers the bar's commands as something a checker's
> spawn may carry. Bring all four sites onto the one rule: the repo's own statement wins, the record is
> confirmed against it before use, and a difference is reported rather than charged against the work.

**Blockers, in the worker's words:**

> none. Fifteen open nodes target `.claude/skills/expedition/SKILL.md`; each one's
> acceptance condition was read and none claims the passages this changes, so any order works and the
> manager holds the sequencing — flagged above. Running after
> [node 173](173-stop-the-checkers-spawn-carrying-the-bars-commands.md) is the tidier order, that node
> repairing the checker's own copy of the given this changes in the manager's mirror of it, so the two
> wordings can be made to match.

## Acceptance condition

*Written by node 174's worker. Pasted as it wrote it, and not the manager's.*

> The work is two files, relative to the repository root:
> `.claude/skills/expedition-implementation/SKILL.md` and `.claude/skills/expedition/SKILL.md`. The
> worker may edit those two and no other, and may not write any file under `.scratch/`.
>
> **The rule the work states, and against which every clause below is measured:**
>
> > A repo's own live statement of its build, test and format commands is authoritative. Where an
> > effort's implementation-rules file records those commands, that record is a copy of an earlier
> > discovery: an agent confirms it against what the repo itself says before using it, rather than
> > trusting it. Where the two differ the repo's statement wins, the agent runs the repo's commands,
> > and it reports the difference so the record can be repaired; the difference is never a reason to
> > judge the work defective. Where the repo states no commands of its own, the record is the only
> > statement there is and stands as it is, unconfirmed.
>
> Done means every one of the following is true of the finished tree.
>
> 1. In `.claude/skills/expedition-implementation/SKILL.md`, the section headed `## The bar` no longer
>    tells its reader to use whatever an implementation-rules file records for this repo, and no
>    longer conditions discovery from the repo on that file recording nothing.
> 2. That same section states the rule quoted above in full: that the repo's own statement is
>    authoritative; that a recorded copy is confirmed against the repo before use rather than trusted;
>    that the repo's statement wins where the two differ; that the difference is reported and never
>    counts against the work; and that an absent repo statement leaves the record standing unconfirmed.
> 3. That section keeps its statement of the bar's properties — the work builds, it warns about
>    nothing, it is formatted, the tests relevant to the change pass, and whatever else the repo itself
>    demands is satisfied — and keeps its statement that a repo with no build, no tests and no
>    formatter meets the bar on its remaining half, that being a complete bar and not a deficient one.
> 4. In `.claude/skills/expedition/SKILL.md`, no sentence states that the bar's commands live in the
>    effort's map, live in any one file and nowhere else, or are written once into the effort's map.
>    Where that file says what the effort's map holds in relation to the bar's commands, it says the
>    map holds a record of them that is confirmed against the repo before use.
> 5. In `.claude/skills/expedition/SKILL.md`, the list of what a checker's spawn receives no longer
>    offers the bar's commands as something that spawn may carry, and no item in that list is
>    conditioned on the effort's map recording commands for the repo. That list states instead that
>    the checker discovers the commands from the repo itself, and states the bar's properties as what
>    the spawn conveys.
> 6. Where either file refers to the file in which a repo states its own commands to an agent, it
>    names that file by role and position only. No particular filename for such a file appears
>    anywhere in either finished file.
> 7. Neither finished file states or implies that an implementation worker and its checker take the
>    bar's commands from different places, or from different files.
> 8. Any sentence in either file that introduces a list by stating how many items it holds states a
>    count arithmetically correct for the items that list then holds.
> 9. No text in either file outside the passages clauses 1 to 8 reach is deleted or reworded.
> 10. Neither finished file names a plugin, requires any skill to be invocable, or assumes a
>     particular repository, machine or toolchain.
> 11. No file other than the two named above is modified, and no file under `.scratch/` is modified.
> 12. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This is one node over two shipped files, and its author said why.** In its own words at filing, the repair *"covers all four sites in one node, on the ground that the defect being fixed **is** an inconsistency between shipped files and landing half of it would recreate one."* That call is flag `174.4`.

**Its own author read fifteen open conditions on `.claude/skills/expedition/SKILL.md` to establish that no blocking edge is owed**, and named the order it would prefer without demanding it: after [node 173](173-stop-the-checkers-spawn-carrying-the-bars-commands.md), so the checker's own copy and the manager's mirror of it can be made to agree. **The manager holds the sequencing on that file and this node states no edge.**
