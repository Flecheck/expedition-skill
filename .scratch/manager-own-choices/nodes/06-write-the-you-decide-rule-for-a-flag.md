# Write the "you decide" rule for a flag into the manager contract

Type: implementation
Status: resolved
Deliverable: you-decide-on-a-flag
Blocked by: ~~01~~ ~~08~~

## Question

*Proposed by the worker of [node 02](02-you-decide-on-a-flag-at-the-gate.md), as it wrote it:* This lets the human answer "you decide" to a flag in a gate payload or a node closing report without the manager sending it back to a worker that has already chosen. Today `### Two things the human can say that are not answers` in `.claude/skills/expedition/SKILL.md` sends every "you decide" back to the worker. This node adds the rule for a flag to that section.

*Manager's note:* blocked on [node 01](01-what-the-manager-settles-on-its-own.md), because node 02's worker found that node 01's answer may add a flag marker this rule must name, which would replace clause 1's sentence.

## Acceptance condition

*Written by the worker of node 02, filed by the manager:*

1. ~~*(superseded by amendment 1 below)*~~ In `.claude/skills/expedition/SKILL.md`, the section headed `### Two things the human can say that are not answers` contains a new paragraph made of these two sentences, word for word. The only permitted difference is setting *"you decide"* in italics, as the rest of that section sets it:
   "A *"you decide"* on a flag that records a choice an agent made, an `ASSUMPTION` or a `DELEGATED` flag, keeps that choice and settles the flag. Nothing is sent back. On any other flag there is no choice to hand over. Say so to the human, and ask what they meant."
2. The new paragraph stands directly after the section's first paragraph. That first paragraph begins "Send a *"you decide"* back to the worker holding the node." and ends "removes the human from a node without anyone noticing." It is left word for word as it was. The section's second paragraph, which begins "Send a reframing of the question mid-interview", is also left word for word as it was.
3. The section's heading is unchanged.
4. No other part of `.claude/skills/expedition/SKILL.md` changes, and no other file under `.claude/` changes. In particular, `.claude/rules/expedition-triggers.md` and `.claude/skills/expedition/graph-conventions.md` are unchanged.

Scope: this scope came from no search. The named section is the work itself, not one instance of a defect.

### Amendment 1 — by the worker of node 01, filed by the manager

What fixed the words: [node 01](01-what-the-manager-settles-on-its-own.md)'s answer, resolved on 2026-11-12, where the human took payload 3's Q6: `AMENDMENT` is a sixth marker, and it joins `ASSUMPTION` and `DELEGATED` under node 02's rule. Clause 1 is superseded and now reads, as that worker wrote it:

1. In `.claude/skills/expedition/SKILL.md`, the section headed `### Two things the human can say that are not answers` contains a new paragraph made of ~~these two sentences~~ these sentences *(amendment 2)*, word for word. The only permitted difference is setting *"you decide"* in italics, as the rest of that section sets it:
   "A *"you decide"* on a flag that records a choice an agent made, an `ASSUMPTION`, a `DELEGATED` or an `AMENDMENT` flag, keeps that choice and settles the flag. Nothing is sent back. On any other flag there is no choice to hand over. Say so to the human, and ask what they meant."

*Manager's note:* node 06 is now blocked on [node 08](08-add-the-amendment-flag-marker.md), as node 01's worker asked, so the marker exists before this rule names it. Node 01's worker also noted that clause 1 says "these two sentences" over a quote of four sentences, and left it, because nothing its work fixes reaches it.

### Amendment 2 — by the manager

What fixed the words: the quote in amendment 1's clause 1 holds four sentences, as node 01's worker noted, so "these two sentences" miscounts them. Clause 1 now says "these sentences". Nothing else changes. The fix is fixed by the text of the clause itself, and decides nothing.

## Answer

The worker's answer, as it wrote it (in full under `## Handover, attempt 1`): In `.claude/skills/expedition/SKILL.md`, the section `### Two things the human can say that are not answers` has a new paragraph, directly after the section's first paragraph: "A *"you decide"* on a flag that records a choice an agent made, an `ASSUMPTION`, a `DELEGATED` or an `AMENDMENT` flag, keeps that choice and settles the flag. Nothing is sent back. On any other flag there is no choice to hand over. Say so to the human, and ask what they meant." Nothing else changed.

*Manager's note:* landed on the deliverable branch `you-decide-on-a-flag`, the gate taken under standing yes 1. The branch is not pushed.

## Flags

`06.1` `ASSUMPTION` **· settled** — Amendment 1 to clause 1, written by node 01's worker and filed by the manager after node 01 resolved. The worker handed no flag sentence for the amendment itself. *Manager's note: `ASSUMPTION` is used because no `AMENDMENT` marker exists yet. Node 08 adds it.*

`06.2` `ASSUMPTION` **· settled** — *Manager's own flag:* the manager amended clause 1's "these two sentences" to "these sentences", because the quoted paragraph holds four sentences. The condition was written by node 02's worker. The node was unclaimed, and the replacement's words are fixed by the clause itself.

## Handover, attempt 1

The worker's handover, as it wrote it:

```
ANSWER:        In `.claude/skills/expedition/SKILL.md`, the section `### Two things the human can say that are not answers` has a new paragraph. It stands directly after the section's first paragraph, which sends a *"you decide"* back to the worker. The new paragraph reads, word for word as clause 1 (as amended) requires:
               "A *"you decide"* on a flag that records a choice an agent made, an `ASSUMPTION`, a `DELEGATED` or an `AMENDMENT` flag, keeps that choice and settles the flag. Nothing is sent back. On any other flag there is no choice to hand over. Say so to the human, and ask what they meant."
               Nothing else changed. The section's heading, its first paragraph and its reframing paragraph are unchanged. No other file was touched. `.claude/rules/expedition-triggers.md` was left alone because it holds no copy of this rule: it contains no "decide" at all, and this section is not the governing statement of any trigger-duty or of the priority. The three markers the rule names all exist on the deliverable's base. `ASSUMPTION` and `DELEGATED` are in `graph-conventions.md`'s marker list, and `AMENDMENT` was added there by node 08, at `2f0a2a9`. The specific rule and the general one sit next to each other in the same section, so the specific rule needs no pointer back to the general one.

INDEX LINE:    Added to SKILL.md's "Two things the human can say" section: a "you decide" on an ASSUMPTION, DELEGATED or AMENDMENT flag keeps the choice; on any other flag the manager asks what was meant.

FLAGS:         none

NEW NODES:     none

INVALIDATIONS: none. Node 02's answer says "Two of the five markers". Node 02's own annotation already extends that to three of six, so this work changes nothing further in it. Nodes 07 (clause 12) and 08 (clause 4) say this section is "unchanged", but those clauses judge their own diffs on `own-choices`. They stay true of that work.

CONDITIONS:    I searched the `## Question` and `## Acceptance condition` sections of every open and claimed node (05, 09), and the `## Answer` and `## Acceptance condition` sections of the resolved nodes (01, 02, 03, 07, 08). The terms were `you decide`, `Two things the human can say`, `not answers`, `DELEGATED` and `AMENDMENT`.
               - Node 05: no match.
               - Node 09 (claimed, deliverable `explain-a-relayed-question`), clause 4: it requires `### Two things the human can say that are not answers` to be unchanged. That clause judges node 09's own diff on its own branch, so it stays true and needs no replacement. The manager should still expect both deliverables to sit near this section when they are integrated. This work's hunk is inside the section, after its first paragraph. Node 09 places its subsection after `### The last line of a report`, so the two should not edit the same lines.
               - Node 03's answer: its reasoning that the heading's "Two" stays correct still holds. The new paragraph adds a case to "you decide", not a third thing.
               No clause needs replacing. No open node's question changes.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings: none yet.
               Paths touched: `.claude/skills/expedition/SKILL.md`, in the worktree `/home/ten/Projects/expedition-skill/.scratch/manager-own-choices/worktrees/06-you-decide-rule`. That is 4 lines added and nothing removed.
               Bar: I confirmed against the repository that there is no build, no tests, no formatter and no CI. The root `CLAUDE.md` `## Commands` says so, and the tree has no build or CI files. This matches `map-implementation-rules.md`. The remaining half of the bar is the standards and the acceptance condition, and both are met by text copied word for word from the condition. The new lines wrap at the same width as the section around them.
               Files other nodes are written against: `SKILL.md`'s `### Two things the human can say that are not answers` gains one paragraph. Nodes 07 and 08 are written against the older form of that section, and so is node 09's clause 4.
               Proposed commit message:
                 Manager contract: a "you decide" on a flag keeps the agent's choice

                 Node: manager-own-choices/06
```

## Review

### Checker run 1 — `PASS`

The checker's entry, as it wrote it:

```
PASS

Clause 1 holds: the new paragraph appears word for word, and *"you decide"* is in italics. I unwrapped each paragraph of the post-change `.claude/skills/expedition/SKILL.md` into one line with `awk 'BEGIN{RS=""}{gsub(/\n/," ");print}'`. Then `grep -nxF "<the four quoted sentences>"` matched exactly one whole paragraph, and the backticked flag names match the condition's text. `grep -cF 'keeps that choice and settles the flag'` gives 1.

Clause 2 holds: the new paragraph is placed directly after the section's first paragraph, and both neighbouring paragraphs are unchanged. I unwrapped `git show 2f0a2a9:<file>` the same way and diffed it against the unwrapped working file. The diff is a single added paragraph (`40a41`), between the paragraph beginning "Send a *"you decide"* back to the worker holding the node." and the one beginning "Send a reframing of the question mid-interview". Neither of those two paragraphs moved.

Clause 3 holds: the heading is unchanged. `### Two things the human can say that are not answers` is present and identical on both sides of that same diff.

Clause 4 holds: nothing else changed. `git status --short --untracked-files=all` lists only ` M .claude/skills/expedition/SKILL.md`. `git diff 2f0a2a9 --stat -- .claude` gives one file with 4 insertions, so `expedition-triggers.md` and `graph-conventions.md` are unchanged.

The bar has no commands to run here. The root `CLAUDE.md` `## Commands` section says the repository has no build, no tests, no formatter and no CI. I confirmed that against the repository: a listing of the worktree root shows only `.claude`, `.claude-plugin`, `CLAUDE.md`, `CONTEXT*.md`, `README.md`, `.gitignore` and `.scratch`, with no build, test or formatter configuration. The rest of the bar is covered by the standards below.

Standards:
- I read only the standards in `.scratch/manager-own-choices/map-implementation-rules.md`, under `## What the work is held against`.
- These bore on the work:
  - Glossary `_Avoid_` lines. I checked all of them by hand. The only possible hit is "ask what they meant", which is the manager asking the human in the ordinary sense. It does not name a raise, so the "ask" refusal under **Raise** does not apply. The wording is also the condition's own.
  - `graph-conventions.md`. The markers `ASSUMPTION`, `DELEGATED` and `AMENDMENT` exist under those exact names, and "settles the flag" uses that file's word *settled*.
  - The rules for writing in the root `CLAUDE.md`. No breach.
  - The trigger-file rule. It does not apply. The section sits under `## Writing the graph`, and it is not the governing statement of a trigger-duty or of the priority. `expedition-triggers.md` has nothing about *"you decide"*, so leaving it unedited is correct.
- These did not apply: `/coding-principles` and `/naming` (the work names nothing and contains no code), and `/writing-for-agents`. I checked the added paragraph against the root `CLAUDE.md` writing rules by hand. I did not invoke `/writing-for-agents` or any other reviewing skill, because the standards file names none to run.

Flags:
- `06.1` and `06.2` describe amendments to the condition. Neither claims anything about the work, so neither is true or false of it.
- The condition as given to me says "these sentences", which matches what `06.2` describes.
- No flag is false.

I wrote no files apart from a temporary unwrap in `$TMPDIR`, which I have removed.
```

### Gate 1 — approve, `standing yes`

Taken under standing yes 1, whose scope text is, word for word: "commits on feature branches dedicated to deliverables, in the current effort". What was taken: checker run 1's `PASS`. Committed on the node's branch, and the deliverable branch `you-decide-on-a-flag` is fast-forwarded to it.
