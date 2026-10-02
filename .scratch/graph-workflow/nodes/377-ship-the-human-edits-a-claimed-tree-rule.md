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

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-10-02. A fresh checker; the condition reached it as a verbatim copy in `$TMPDIR/c377.md`.*

> PASS
>
> Worktree: /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/377-human-edits. Base is 0f4c45044. Changed paths: .claude/skills/expedition-implementation/SKILL.md and .claude/skills/expedition/SKILL.md, both uncommitted. `git status --porcelain --untracked-files=all` shows only these two files, so no other path is touched.
>
> 1. Sentence replaced. `grep -rn "yours alone" .claude/skills` returns one line, `expedition-implementation/SKILL.md:18`. The diff replaces "The tree your spawn names is yours alone for the whole node." with three sentences, in this order: "The tree your spawn names is yours alone among the agents for the whole node." / "The human may also edit it." / "Edit only files inside it." The third is kept unchanged. Met.
>
> 2. Correction-round bullet. In `git diff`, the list under "In a correction round:" gains one bullet: "Where the human has edited your tree, keep what they wrote. Where their text conflicts with the acceptance condition or with something the checker found, raise it. Leave that text unchanged." Both demanded things are present, in order. The bullet uses `raise`, which the contract defines in `## Words used exactly` as the kind of raise that stops work. Met.
>
> 3. Manager rule. `grep -n "^### "` places the addition under `### Three outcomes, and no fourth`, directly after the line "...touched something the condition names." It is two sentences: "Where the human says they edited a claimed node's tree, pass their words to that node's worker when you next resume it." / "Ask the human nothing about what changed." Both demanded things are present. Met.
>
> 4. Checker contract untouched. `git diff --quiet 0f4c45044 -- .claude/skills/expedition-checker/SKILL.md` exits 0 (unchanged). Met.
>
> 5. Scope search. I ran `grep -rn "yours alone" .claude/skills` as written over the worktree. It returned exactly one line, `.claude/skills/expedition-implementation/SKILL.md:18`, which matches the recorded return. No instance falls outside the named files.
>
> 6. Writing rules and size.
>    - Writing rules: I held each added sentence against the six standing writing rules received in the ground-rules text, which the rules file says are the rules in `map.md`'s `## Notes`. Every added sentence carries one idea and is stated as what to do. The condition's "does not change that text" became the positive "Leave that text unchanged." There are no figures of speech, coined phrases or slogan contrasts, and nothing new is bolded.
>    - Size, measured with `wc -l` at the base and in the worktree: implementation 338 -> 341 and expedition 824 -> 826, so a net gain of 5 lines. The diff shows 6 `+` lines and 1 `-` line, because the replaced sentence was rewrapped from one line into two. I read "adds no more than five lines" as the net gain, which is 5. Met under that reading.
>
> 7. The bar.
>    - The rules file records that this repo has no build, no tests, no formatter and no CI. The command half of the bar is therefore empty, and that is a complete bar.
>    - I confirmed the worktree has no CLAUDE.md or AGENTS.md at its root.
>    - `git diff --check` printed nothing, so there are no whitespace errors.
>    - All added lines are at most 102 characters wide.
>    - The non-command half is the standards (below). Met.
>
> Standards: I read only the standards in .scratch/graph-workflow/map-implementation-rules.md, and opened no other file in the effort's directory.
> - The list is: /coding-principles and /naming; the glossary's `_Avoid_` lines; the ground rules; the six writing rules; graph-conventions.md; /writing-for-agents.
> - These bore on the work:
>   - Glossary `_Avoid_` lines. "tree" is refused only as a name for the graph, and here it means the working tree. No other added word appears in an `_Avoid_` line.
>   - The writing rules (see part 6).
>   - Ground rule 3. No added text has an agent address the human. The manager rule tells the manager to ask the human nothing.
>   - /writing-for-agents. I read it from the mattpocock-skills plugin (nix store, skills/productivity/writing-for-agents/SKILL.md). The additions state the positive target, and they duplicate no meaning held elsewhere.
> - The rules file's co-edit rule for .claude/rules/expedition-triggers.md does not apply. The addition sits under `## The gate`, not under `## The order you act in` or `## What is in front of the human, and when`.
> - /coding-principles, /naming and graph-conventions.md did not bear on this prose-only change.
>
> Review route: the rules file names no reviewing skill, so I ran none. Ground rule 5 makes /writing-for-agents a standard, so I held the work against it by hand. I ran no subagent.
>
> I read the changed paths as the work under check. Neither is a record file, and no bookkeeping paths appear. I wrote no files and made no temporary directory.

### Gate — approve, `standing yes`, 2026-10-02

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and left no part of the condition uncovered. This settles none of the node's flags; they settle at the node closing report.

## Flags

`377.1` `ASSUMPTION` — *The worker's own text.* Clause 6 says the change "adds no more than five lines across the two files". I read that as the net growth in line count, which is five here. Rewrapping the replaced sentence also rewrites one existing line, so `git diff --numstat` reports 6 insertions and 1 deletion. Making the insertion count five as well would have meant one manager-skill line far past the file's wrap width of about 105 characters, or cutting words the condition requires. No exchange with the human took place. I made the edits, measured the diff, and chose the net reading.
