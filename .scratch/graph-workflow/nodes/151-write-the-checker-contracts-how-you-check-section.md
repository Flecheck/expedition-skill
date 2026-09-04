# Write the checker contract's `## How you check` section

Type: implementation
Status: open

Blocked by: 143

## Question

*Surfaced by [Whether the workflow ships its own reviewing discipline, now that a checker may not find
one](145-whether-the-workflow-ships-its-own-reviewing-discipline.md)'s worker, and pasted as it wrote it.*

> Node 143 removes the checker's discovery apparatus and leaves it with sources and no discipline for working against
> them, and it deletes the one sentence routing a standards breach to `FAIL: the bar`. Write the method the human
> elected — a short shipped section in the checker's contract, carrying the four moves and that routing.

**Blockers, in the worker's words:** *"143. Node 143 rewrites what the checker is given and deletes the section this
one replaces; writing this first would build a method section around apparatus about to be removed, and both edit the
same file."*

## Acceptance condition

*Written by node 145's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.claude/skills/expedition-checker/SKILL.md`, relative to the repository root. The worker may edit that
> file and no other, and may not write any file under `.scratch/`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. The file contains a section headed exactly `## How you check`, placed after the section headed `## Hard rules`
>    and before the section headed `## What you hand back`.
> 2. That section's body — from its heading to the next line beginning `## ` — is at most 2,000 bytes.
> 3. It states that the checker splits the acceptance condition into its parts before it reads the work, because its
>    `PASS` owes one line per part.
> 4. It states that three things are kept separate and are never merged with one another or ranked against one
>    another — the acceptance condition, the bar, and the standards the spawn gives the checker — and that passing on
>    one of the three never excuses or masks failing on another.
> 5. It states that the standards report under the bar, so that work breaching a standard is `FAIL: the bar` and
>    never `FAIL: acceptance condition`.
> 6. It states that the checker establishes each part of the condition by a search it can name and hands that search
>    back, rather than by reading the work through.
> 7. It states that the checker says plainly what it did not check.
> 8. It states that an effort's own rules may add method specific to that effort on top of this section, and that
>    this section's demands still hold where they do.
> 9. The section contains no instruction to search for, look for, discover, or otherwise go and find the standards
>    the checker holds work against.
> 10. Where the section refers to a shape the file defines elsewhere, it uses that file's own name for it — `PASS`,
>     `FAIL: acceptance condition`, `FAIL: the bar`, `NOT COVERED` — and defines no second version of any of them.
> 11. The section names no skill and no plugin, assumes no particular repository, machine or toolchain, and requires
>     nothing to be invocable.
> 12. No text outside the new section is deleted or reworded, with one exception: a sentence elsewhere in the file
>     stating clause 5's routing, which the new section now carries, may be removed as a duplicate.
> 13. No file other than the one named above is modified.
> 14. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Its paths are repo-relative**, unlike [node 149](149-state-the-prose-standards-demands-in-the-rules-file.md)'s,
which is flagged at `149.1`. The spawn asked for that explicitly after node 149's condition recurred the defect [node
147](147-graph-records-name-absolute-paths-on-a-machine.md) had just repaired.

**Its author asks for it to run immediately after [node 143](143-rules-arrive-by-the-spawn-never-by-a-search.md), and
says why**, at flag `145.3`: between node 143 landing and this node landing, the shipped checker contract states its
standards as a given and nowhere says which of its two verdicts they report under. **That is a sequencing request on
the manager rather than an edge**, and the manager has recorded it rather than acted on it.
