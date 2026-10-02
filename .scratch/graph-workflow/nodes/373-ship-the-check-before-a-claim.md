# Ship the check before a claim into the manager's contract

Type: implementation
Status: claimed
Blocked by: none

## Question

Add to the manager's contract the paragraph that makes the manager check an implementation node's condition is still current before claiming it.

*Reported by [node 365](365-check-a-nodes-condition-is-still-current-before-claiming-it.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none. Node 368 (claimed) edits other passages of the same file, `## Acceptance conditions` first paragraph and constraint 2. So this is a new node rather than clauses joined to 368, and the two may meet at integration."*

## Acceptance condition

*Authored by node 365's worker and filed by the manager.*

> 1. `.claude/skills/expedition/SKILL.md`, under `### Changing one after it is written`, gains one new paragraph immediately after the paragraph that begins "Re-derive an enumerated scope before the node is claimed."
> 2. The new paragraph tells the manager that, before it claims an implementation node, it does two things. First, it reads everything written on the node's file after its acceptance condition, meaning its annotations, its amendments and the manager's own notes. Second, it searches the working tree for each passage the condition quotes or names by heading.
> 3. The new paragraph says that where a quoted or named passage is gone, or where an annotation or note says the condition is wrong, the manager either amends the condition under the rules of that same section or puts the node to the human, and claims the node only once neither is true.
> 4. The new paragraph adds no new route for a defective condition. It names no procedure beyond the rules of the section it sits in and the human.
> 5. The new paragraph is at most 80 words. It is written in plain English, one idea per sentence. It uses no figure of speech and no term that `.claude/skills/expedition/glossary.md` does not define, other than plain words.
> 6. No heading in any file under `.claude/skills/` is added, removed or renamed. No other paragraph of `SKILL.md` changes, and no other file changes.
> 7. Scope came from no search: the work adds one paragraph at the one place named.

## Handover, attempt 1

*The worker's own text, pasted, 2026-10-02.*

````
HANDOVER:      Ship the check before a claim into the manager's contract
ANSWER:        `.claude/skills/expedition/SKILL.md`, under `### Changing one after it is written`, gains one paragraph of 77 words. It sits immediately after the paragraph beginning "Re-derive an enumerated scope before the node is claimed." It reads:
               "Before you claim an implementation node, read everything written on its file after its acceptance condition: its annotations, its amendments and your own notes. Then search the working tree for each passage the condition quotes or names by heading. Where such a passage is gone, or an annotation or note says the condition is wrong, amend the condition under this section's rules or put the node to the human. Claim the node only once neither is true."
               The paragraph addresses the manager as "you", as the rest of SKILL.md does. "This section's rules" points at the rules of `### Changing one after it is written` and names no other procedure. The two things the manager does are marked by "read" and "Then search" rather than by "First"/"Second", which saved words. No heading was added, removed or renamed, and no other paragraph or file changed. `.claude/rules/expedition-triggers.md` is not affected, because this paragraph is neither a trigger-duty nor the priority.
INDEX LINE:    SKILL.md's `### Changing one after it is written` now tells the manager to read a node's annotations, amendments and notes and search for each quoted passage before claiming it.
FLAGS:         ASSUMPTION: Clause 2 asks for "the manager's own notes". The glossary's **Manager note** means the manager's annotation on a relayed question, which is a narrower thing. I wrote "your own notes" as plain words for any note the manager wrote on the node, and did not use the glossary term. Index: Node 373's paragraph says "your own notes" in plain words for the manager's notes on a node, not the glossary's narrower **Manager note** on a relayed question.
NEW NODES:     none
INVALIDATIONS: none. This carries out node 365's answer (Q3), as written.
CONDITIONS:    I searched every open and claimed node file (34 of them) for "Changing one after it is written", "Re-derive an enumerated scope", "before it claim" / "before you claim", "check before a claim" and the path `.claude/skills/expedition/SKILL.md`. The only match on the first four was node 373 itself. Nodes 317, 375, 370, 87 and 85 matched on the path. Node 375 (open) edits other sections, and nothing in it conflicts with this work. Node 370 (claimed) has clause 16: "`.claude/skills/expedition/SKILL.md` changes only as clause 14 says". That holds for 370's own diff, but when both branches are merged SKILL.md will have this paragraph too. This is an integration matter, and no clause needs replacing. I wrote no replacements and changed no open node's question.
MISSING FROM MAP: none
GATE PAYLOAD:  No checker findings yet. Path touched: .claude/skills/expedition/SKILL.md (worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/373-claim-check). Bar: I checked the repo and found no build, tests, formatter or CI files, which matches map-implementation-rules.md. So the bar is its non-command half. The new lines are at most 103 characters, in line with the file's wrapping. Words: 77 (limit 80).
               Proposed commit message:
               Tell the manager to check a node's condition is still current before claiming it

               Node: graph-workflow/373

RETROSPECTIVE:
1. What I had to hunt for: whether "annotation", "amendment" and "notes" are glossary terms. Only "Manager note" is, and it means something narrower. "Annotation" is a section in graph-conventions.md, not a glossary entry.
2. What arrived that this node did not need: most of map.md, and nearly all of map-implementation-rules.md beyond the line that says there are no commands.
3. What would have made this easier: if the condition had said whether "the manager's own notes" means the glossary's Manager note or plain notes.
4. What was stale, wrong or contradictory: node 365's draft of "about 65 words" came out at about 75 words, so the label in its answer was low. Nothing else.
````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-10-02. A fresh checker; the condition reached it as a verbatim copy in `$TMPDIR/c373.md`.*

> PASS
>
> Context. The work is one uncommitted path in worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/373-claim-check (HEAD 5c858081): .claude/skills/expedition/SKILL.md, with 6 added lines and 0 removed. I read the changed path as the work. I read only the standards in .scratch/graph-workflow/map-implementation-rules.md and opened no other file in the effort's directory. I did not read the node file.
>
> Parts of the acceptance condition:
> 1. Placement. The diff has one hunk, under `### Changing one after it is written`. It inserts one paragraph directly after the paragraph that begins "Re-derive an enumerated scope before the node is claimed." and before "Every amendment, whoever wrote it, comes with five things." Established by `git -C <wt> diff` and `awk '/^### Changing one after it is written/,/^## /' SKILL.md`.
> 2. The two acts before a claim. The added text, unwrapped (`git diff -U0 | grep '^+[^+]' | tr '\n' ' '`), reads: "Before you claim an implementation node, read everything written on its file after its acceptance condition: its annotations, its amendments and your own notes. Then search the working tree for each passage the condition quotes or names by heading." Both acts are present, in that order.
> 3. When to amend or put the node to the human. The text says: "Where such a passage is gone, or an annotation or note says the condition is wrong, amend the condition under this section's rules or put the node to the human. Claim the node only once neither is true." This matches the part.
> 4. No new route. The only routes named are "this section's rules" and the human. Established from the same unwrapped text.
> 5. Length, plain English and terms. `wc -w` gives 77 words, so it is within 80. There are four sentences, each with one idea, and no figure of speech. "claim", "implementation node", "acceptance condition" and "annotation" are glossary terms or are defined in graph-conventions.md `### ## Annotation`. "amendments", "notes", "passage", "working tree" and "heading" are plain words. "put ... to the human" is phrasing used elsewhere in the shipped files. I checked the `_Avoid_` lines (`grep -n "_Avoid_" glossary.md`) by hand against the 77 words, and no refused word appears.
> 6. Nothing else changed. `git status --porcelain --untracked-files=all` lists only SKILL.md. `git diff --stat` shows 1 file, 6 insertions, and the count of '-' lines is 0. So no heading was added, removed or renamed, no other paragraph changed, and no other file changed.
> 7. The condition records no command, so there was nothing to re-run. The diff confirms the work adds one paragraph at the one place named.
>
> The bar. map-implementation-rules.md records that this repo has no build, no tests, no formatter and no CI. The worktree root holds only .claude, CONTEXT.md, CONTEXT-MAP.md, .gitignore and .scratch. There is no agent-instruction file and nothing to invoke, so I ran no commands. The bar is therefore its non-command half, all checked by hand:
> - The ground rules and the six standing rules for writing hold. The text cites no line numbers, assumes no toolchain, has no agent address the human, and is plain English.
> - The glossary `_Avoid_` lines hold, with no hits.
> - graph-conventions.md holds. "annotations" uses that file's meaning.
> - /writing-for-agents holds. The text is short, direct and in imperative form, and wraps at the width of the surrounding text.
> - /coding-principles and /naming do not apply, since the work is prose only.
> - The trigger-file rule (edit .claude/rules/expedition-triggers.md together with `## The order you act in` / `## What is in front of the human, and when`) does not apply. The paragraph sits under `## Acceptance conditions`, and the trigger file has no claim duty (`grep -i claim` returned nothing).
>
> The standards say no reviewing skill is named for this repo, so I ran none.

### Gate — approve, `standing yes`, 2026-10-02

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and left no part of the condition uncovered. This settles none of the node's flags; they settle at the node closing report.

## Flags

`373.1` `ASSUMPTION` — *The worker's own text.* Clause 2 asks for "the manager's own notes". The glossary's **Manager note** means the manager's annotation on a relayed question, which is a narrower thing. I wrote "your own notes" as plain words for any note the manager wrote on the node, and did not use the glossary term.
