# Ship the human-edits-a-claimed-tree rule

Type: implementation
Status: claimed
Blocked by: none

## Question

Carry node 85's answer into the implementation contract and the manager's skill.

*Reported by [node 85](85-human-edits-a-claimed-tree.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none".*

## Acceptance condition

*Authored by node 85's worker and filed by the manager.*

>  Done when all of the following hold.
>
> 1. In `.claude/skills/expedition-implementation/SKILL.md`, the sentence "The tree your spawn names is yours alone for the whole node." is replaced. The new text states three things, in this order: the tree the spawn names is the worker's alone among the agents for the whole node; the human may also edit it; and "Edit only files inside it." stays.
> 2. In the same file, the bulleted list that follows the line "In a correction round:" gains one bullet. The bullet states two things. First, where the human has edited the worker's tree, the worker keeps what the human wrote. Second, where the human's text conflicts with the acceptance condition or with something the checker found, the worker raises it and does not change that text.
> 3. In `.claude/skills/expedition/SKILL.md`, the section headed `### Three outcomes, and no fourth`, or the text directly under it, gains at most two sentences. They state that where the human says they edited a claimed node's tree, the manager passes the human's words to that node's worker at the worker's next resume, and asks the human nothing about what changed.
> 4. `.claude/skills/expedition-checker/SKILL.md` is not changed by this work.
> 5. Scope search: `grep -rn "yours alone" .claude/skills` was run over the working tree on 2026-10-02. It returned exactly one line: `.claude/skills/expedition-implementation/SKILL.md:18`. An instance the same search reaches outside the files this condition names is reported and not edited.
> 6. Each added passage follows the writing rules in `map.md`'s `## Notes`: plain English, one idea per sentence, stated as what to do. The whole change adds no more than five lines across the two files.
> 7. The working tree meets the bar.

## Handover, attempt 1

*The worker's own text, pasted, 2026-10-02.*

````
HANDOVER:      Ship the human-edits-a-claimed-tree rule

ANSWER:        Node 85's answer is now in the two shipped files. The change adds five lines net.
                - `.claude/skills/expedition-implementation/SKILL.md`, in the code-slot paragraph near the top: "The tree your spawn names is yours alone for the whole node." is replaced by "The tree your spawn names is yours alone among the agents for the whole node. The human may also edit it." "Edit only files inside it." stays and follows those sentences. The paragraph is rewrapped over one extra line.
                - Same file, in the list under "In a correction round:": a new bullet comes after the flag bullet and before the "Every round" bullet. It reads: "Where the human has edited your tree, keep what they wrote. Where their text conflicts with the acceptance condition or with something the checker found, raise it. Leave that text unchanged." The raise and the no-change instruction are two separate sentences, so each sentence holds one idea.
                - `.claude/skills/expedition/SKILL.md`, under `### Three outcomes, and no fourth`: two sentences are added at the end of the paragraph "The bar is re-checked in every correction round...". They read: "Where the human says they edited a claimed node's tree, pass their words to that node's worker when you next resume it. Ask the human nothing about what changed." They continue the existing paragraph with no blank line between, which keeps the change to two lines.
                - `.claude/skills/expedition-checker/SKILL.md` is unchanged.
                - Scope search: before the edit, `grep -rn "yours alone" .claude/skills` over the worktree returned only `.claude/skills/expedition-implementation/SKILL.md:18`. After the edit it returns the same file and line, which now reads "yours alone among the agents". A wider search, `grep -rni "tree.*alone|alone.*tree|human.*edit.*tree"` over `.claude/skills` and `.claude/rules`, found no other statement about the tree that this change makes stale.
                - Bar: the repo has no build, no tests and no formatter. That matches `map-implementation-rules.md`, which says `graph-agent` has nothing to invoke and `.gitignore` invokes nothing. So the bar is its non-command half: the standards and the acceptance condition.

INDEX LINE:    The implementation contract now says the tree is the worker's alone among the agents and the human may edit it. The worker keeps human text and raises conflicts. The manager passes the human's words on at the next resume.

FLAGS:         ASSUMPTION: Clause 6 says the change "adds no more than five lines across the two files". I read that as the net growth in line count, which is five here. Rewrapping the replaced sentence also rewrites one existing line, so `git diff --numstat` reports 6 insertions and 1 deletion. Making the insertion count five as well would have meant one manager-skill line far past the file's wrap width of about 105 characters, or cutting words the condition requires. No exchange with the human took place. I made the edits, measured the diff, and chose the net reading.
               Index sentence: Node 377 read "adds no more than five lines" as net line growth (five), since rewrapping the replaced sentence makes git count 6 insertions and 1 deletion.

NEW NODES:     none

INVALIDATIONS: none. This carries out node 85's answer and contradicts no resolved node. The sentence node 85's question quotes ("yours alone for the whole of the node") was already reworded before this node. This node replaces its current form.

CONDITIONS:    I searched the conditions and questions of all 38 nodes whose status is not resolved, superseded, dropped, moot or merged. The search terms were "yours alone", "Three outcomes, and no fourth", "In a correction round", "human edit", "edited the", "human may also edit" and "among the agents". Only node 377 matched. I also searched those nodes for the two changed paths: nodes 41, 317, 32 and 87 matched. None of their clauses is made wrong by this work, so I wrote no replacement. One side note: node 32's `## Question` cites `expedition-implementation/SKILL.md` "line 54" for the line "Leave `flags.md` unread". That was already stale before this change (line 65 at 0f4c45044), and the extra line this change adds makes it line 66. Node 32's meaning is unaffected. The question cites by line number, which writing rule 4 forbids.

MISSING FROM MAP: none

GATE PAYLOAD:  No checker findings yet.
               Paths touched:
                 .claude/skills/expedition-implementation/SKILL.md
                 .claude/skills/expedition/SKILL.md
               Worktree: /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/377-human-edits (branch worktree-377-human-edits), uncommitted.
               No method skill was invoked, so nothing was skipped.
               Proposed commit message:
                 Let the human edit a claimed node's tree

                 The implementation contract now says the tree is the worker's alone
                 among the agents and that the human may also edit it. A new
                 correction-round bullet tells the worker to keep the human's text and
                 to raise any conflict with the condition or a checker finding. The
                 manager's skill, under "Three outcomes, and no fourth", passes the
                 human's words to the worker at its next resume and asks nothing about
                 what changed.

                 Node: graph-workflow/377

RETROSPECTIVE
1. What I had to hunt for: the effort name for the `Node:` trailer, which I took from `git log`. Also how to count "five lines" in clause 6, and whether an appended paragraph counts as "the text directly under" the heading.
2. What arrived that this node did not need: most of `map.md`, about 38KB. Only the writing rules in `## Notes` bore on this work. Of `map-implementation-rules.md`, only the bar paragraph applied.
3. What would have made this easier: a condition that defines "lines added", as net growth or as diff insertions, and that names where in the section the new sentences go.
4. What was stale, wrong or contradictory: node 32's question cites a contract line by number ("line 54"), and that number was already wrong. The quote in node 85's question ("yours alone for the whole of the node, and every file you edit is inside it") no longer matched the shipped wording. Both manager claims checked out: one grep hit at line 18, and both anchors exist.
````

## Flags

`377.1` `ASSUMPTION` — *The worker's own text.* Clause 6 says the change "adds no more than five lines across the two files". I read that as the net growth in line count, which is five here. Rewrapping the replaced sentence also rewrites one existing line, so `git diff --numstat` reports 6 insertions and 1 deletion. Making the insertion count five as well would have meant one manager-skill line far past the file's wrap width of about 105 characters, or cutting words the condition requires. No exchange with the human took place. I made the edits, measured the diff, and chose the net reading.
