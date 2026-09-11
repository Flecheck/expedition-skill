# `.gitignore` cites the rules file by a quoted phrase that resolves to nothing

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [node 198](198-two-files-describe-the-rules-file-by-contents-node-188-removes.md)'s worker, and pasted
as it wrote it. **The same site was independently found by [node
188](188-move-the-landing-section-out-of-the-workers-file.md)'s checker**, whose words are on node 198 as its first
annotation.*

> `.gitignore`'s second comment reads *"See .scratch/graph-workflow/map-implementation-rules.md, \"How the worktree
> is made\""*. Node 188 moved that passage to `map-manager-only.md`, so the citation names a file that no longer
> holds the phrase — the by-quoted-phrase form standing rule 4 prescribes, decaying silently because the passage
> changed file rather than moved within one. Its first comment separately cites *"map.md, the landing policy"*,
> which is also no longer where that policy is. Outside node 198's clause 4, so node 198 could not touch it.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 198's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.gitignore` and no other file may be edited. The worker may not mark this node, resolve it, or write
> a line in `decisions.md` or `flags.md`; `.gitignore` is not part of the effort's record, so it is edited plainly
> and nothing is struck in place.
>
> Done means all of the following are true of the finished tree.
>
> 1. Every file path named in a `.gitignore` comment exists.
> 2. Every phrase a `.gitignore` comment quotes and attributes to a named file appears in that file, established by
>    reading that file.
> 3. The two ignore entries `.worktrees/` and `.claude/worktrees/` are both still present and unchanged.
> 4. No file other than `.gitignore` is modified.
> 5. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This is the third arrival of the same site, and the shape is worth keeping rather than the count.** Standing rule
4 says to cite by quoted phrase **because a line number decays silently** — and here the quoted phrase decayed
instead, because the passage changed file rather than moving within one. The rule's stated failure mode and its
prescribed remedy have the same weakness against a move between files.

**Its author found a second defect in the same file that nobody had named**: `.gitignore`'s *first* comment cites
`map.md` for the landing policy, which has not been true since node 139 split the map. So the file carries two
decayed citations rather than one, and clause 2 of its condition reaches both by being written as a property rather
than as a list of sites.
