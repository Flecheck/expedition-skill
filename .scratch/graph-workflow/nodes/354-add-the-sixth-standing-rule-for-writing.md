# Add the sixth standing rule for writing: point at a heading of a file the reader already reads

Type: implementation
Status: open
Blocked by: 352

## Question

Write node 253's rule as the sixth standing rule for writing, in the list that holds the other five.

*Reported by [node 253](253-a-shipped-file-points-at-a-sibling-rather-than-restating-it.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Acceptance condition

*Authored by node 253's worker and filed by the manager.*

> The work is `.scratch/graph-workflow/map.md`, `.scratch/graph-workflow/map-implementation-rules.md` and `.scratch/graph-workflow/map-history.md`, and no other file may be edited. The worker may not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> Done means all of the following are true of the finished tree.
> 1. In `map.md`'s `## Notes`, the numbered list of this effort's standing rules for writing, inside the block that begins with the bold line "**Ground rules for this effort.**", ends with a sixth rule, word for word as below. Rules 1 to 5 of that list are not reworded, renumbered or reordered.
>    6. **Point at a heading of another shipped file instead of restating what it holds, where the reader is already told to read that file.** Where the reader is not, restate what the reader needs when the file pointed at is mostly text that reader does not need, so the reader is not sent to read it. A passage that changes a rule for its own case names that rule by heading and states the change in its own words. Rename a heading that another shipped file cites only in the change that updates every citation of it, found by searching the shipped files for the heading's exact text.
> 2. The list's bold lead-in links `nodes/253-a-shipped-file-points-at-a-sibling-rather-than-restating-it.md` as the node that fixed the sixth rule. Wherever the lead-in gives the number of rules, it says six.
> 3. No sentence in `map.md`, `map-implementation-rules.md` or `map-manager-only.md` gives the number of this effort's standing rules for writing as four or five.
> 4. Every text this work removes from `map.md` or `map-implementation-rules.md` is appended verbatim to `map-history.md`, under a heading that mirrors the section it came from, with struck-through text staying struck through. `map-history.md` gains text and loses none.
> 5. Every markdown link in the three files resolves to a path that exists.
>
> Scope search for clause 3: `grep -rn -i "rules for writing" .scratch/graph-workflow/map.md .scratch/graph-workflow/map-implementation-rules.md .scratch/graph-workflow/map-manager-only.md .claude/skills`. Run over the working tree on 2026-09-27, before node 352 landed, it returned 1 line in `map.md` (the paragraph beginning "The five standing rules for writing anything in this effort") and 3 matches in `map-implementation-rules.md` (the bar paragraph, and the review route paragraph twice). It returned none in `map-manager-only.md` or `.claude/skills`. Node 352 moves these lines, so the worker re-runs the command on the tree it starts from and edits every match in the three editable files. A match the search reaches in any other file is reported, not edited.
