# Fix the upgrade skill's citations of its own subsection

Type: implementation
Status: resolved
Labels: UPGRADE

## Question

This makes the steps of `/expedition-upgrade` point to headings that exist, so a manager following step 3 or step 6 finds the passage it is sent to. Steps 3 and 6 under `## Your steps, in order` in `.claude/skills/expedition-upgrade/SKILL.md` cite `## A branch that already exists`, but that heading is `### A branch that already exists`, under `## Work already done or under way`.

*Manager's note:* minted by the worker of [node 11](11-ship-the-local-merge-of-a-deliverable.md) on its `NEW NODES` part, with the question and condition below as it wrote them.

## Acceptance condition

In `.claude/skills/expedition-upgrade/SKILL.md`, every citation of the heading "A branch that already exists" gives it as `### A branch that already exists`. Scope: on 2026-10-12, in the worktree of node 11, cut from `a40f9008e8`, `grep -n "## A branch that already exists" .claude/skills/expedition-upgrade/SKILL.md` returned 3 lines: steps 3 and 6, and the heading itself. That count is for scale only and is not authoritative. An instance the search finds outside this file is reported, not edited.

*Manager's note:* the worker of [node 09](09-an-implementation-node-may-widen-its-own-scope.md) wrote a replacement for this condition's last sentence, to be filed only once node 14 has landed and if this node is still unclaimed then. As it wrote it: "An instance the search finds outside this file is edited only on the three grounds for widening that `.claude/skills/expedition-implementation/SKILL.md` states, with a flag naming the place and the reason; any other instance is reported, not edited." Its words are fixed by node 09's answer and by the shipped implementation contract.

*Manager's note, before the claim:* re-ran the recorded search at `cf5984eadc`; it returned the same 3 lines (steps 3 and 6, and the heading itself), so the scope has not grown. The replacement clause node 09's worker wrote is not filed, because node 14 has not landed.

## Answer

Steps 3 and 6 under `## Your steps, in order` in `.claude/skills/expedition-upgrade/SKILL.md` now cite `### A branch that already exists`, matching the heading's real level under `## Work already done or under way`. Nothing else changed. A search over the worktree's `.claude/` and root `CLAUDE.md` for "A branch that already exists" finds only steps 3 and 6, the heading itself, and the first sentence of its body. No instance exists outside this file, so nothing was reported. The bar: the worktree's root `CLAUDE.md`, under `## Commands`, states there is no build, no tests, no formatter and no CI. That matches `map-implementation-rules.md`, so the bar is the standards plus the condition.

*Manager's note:* landed as `872398c449` on `master` by fast-forward, after the human's approval; the worktree and branch are removed.

## Review

### Checker run 1 — `PASS`

The checker's entry, as it wrote it:

PASS

Acceptance condition, by part:
- "every citation of the heading 'A branch that already exists' gives it as `### A branch that already exists`": met. In the worktree, I unwrapped `.claude/skills/expedition-upgrade/SKILL.md` into one line with `tr '\n' ' ' | tr -s ' '` and searched it for `branch that already exists`. It has two citations, in step 3 and step 6, and both now read `` `### A branch that already exists` ``. The other two hits are the heading itself (`### A branch that already exists`, nested under `## Work already done or under way`) and ordinary prose ("take a branch that already exists"), which is not a citation. No citation of the heading wraps across lines.
- "An instance the search finds outside this file is reported, not edited": I ran the same unwrapped search over every file under `.claude/` and over the root `CLAUDE.md`. The phrase "A branch that already exists" turns up in no other file I hold, so there is nothing to report. `git diff --stat` shows that only `.claude/skills/expedition-upgrade/SKILL.md` changed, with 2 insertions and 2 deletions, both of them `##` to `###` in the citations at steps 3 and 6.
- The recorded search: I ran `grep -n "## A branch that already exists" .claude/skills/expedition-upgrade/SKILL.md` as written, in the worktree. It returned 3 lines: 42 (step 3), 46 (step 6) and 92 (the heading). That matches the recorded return of 3 lines for steps 3 and 6 and the heading. There is no mismatch.

The bar:
- The root `CLAUDE.md`, under `## Commands`, says the repository has no build, no tests, no formatter and no CI. I confirmed this: the worktree root holds only `.claude`, `CLAUDE.md`, `CONTEXT-MAP.md`, `CONTEXT.md`, `.gitignore` and `.scratch`, with no build manifest and no `.github`. Building, warnings, formatting and tests therefore have no commands to run. `git diff --check` printed nothing, so the change adds no whitespace errors.
- Standards: I read only the standards in `.scratch/rename-split-upgrade/map-implementation-rules.md`. These are `/coding-principles`, `/naming`, the glossary's `_Avoid_` lines, `graph-conventions.md`, `/writing-for-agents`, the root `CLAUDE.md` `## Rules for the files under .claude/skills/`, and the trigger-file rule.
  - Writing rule 6 of the root `CLAUDE.md` (citing a heading by its exact text) is the one that bore on this work, and the change brings both citations into line with the heading's actual level.
  - The change adds no words, so the `_Avoid_` lines and the rest of the writing rules are not engaged.
  - The trigger-file rule is not engaged, because `.claude/skills/expedition/SKILL.md` is unchanged.
  - The standards name no reviewing skill, so I ran none.

The node holds no flags. I left nothing written and created no temporary files.

### Gate outcome — approve

The human's words, `verbatim`:

> approve
