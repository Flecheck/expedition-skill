# Take a pause under a standing yes

Type: implementation
Status: resolved
Blocked by: ~~14~~

## Question

This lets a manager holding a standing yes take a worker's raise that recommends a pause, and carry out every step a pause needs. Today `expedition-standing-yes` only says to resume the worker with the `STANDING YES` line.

*Manager's note:* minted by the worker of [node 14](14-ship-the-rule-for-widening-scope.md) on its `NEW NODES` part, with the question and condition below as it wrote them.

## Acceptance condition

Scope: the named place is the work, and the scope came from no search. The file this work may change is `.claude/skills/expedition-standing-yes/SKILL.md`. Any other instance is edited only on the three grounds the implementation contract states, with a flag naming the place and the reason; any other is reported and not edited.

1. Under `## Taking a covered item`, the file says that where a covered raise's `RECOMMENDED` is a pause, the manager also carries out the steps under `## A paused implementation node` in the skill `expedition`. The file points to that heading and does not restate its steps.

*Manager's note, before the claim:* nothing is written after the condition. `## Taking a covered item` in `.claude/skills/expedition-standing-yes/SKILL.md` and `## A paused implementation node` in `.claude/skills/expedition/SKILL.md` are present at `47beb1c218`. Its scope came from no search. Node 14 resolved, so the blocker is struck.

## Answer

`.claude/skills/expedition-standing-yes/SKILL.md`, `## Taking a covered item`, step 2 (the step for a question or a raise) gains a paragraph after the `DIVERGENCE` sentence: "Where a covered raise's `RECOMMENDED` is a pause, also carry out the steps under `## A paused implementation node` in the `expedition` skill's `SKILL.md`. The worker reads the `STANDING YES` line as the pause." The paragraph points to the heading and does not restate its steps. It sits inside step 2 rather than as a new numbered step, so steps 3 to 5 keep their numbers. The second sentence tells the manager that the `STANDING YES` resume is still sent on a pause. This matches the implementation contract's `### The raise`, which reads that line as the pause where the `RECOMMENDED` was the pause.

*Manager's note:* landed as `b9b1d69809` on `master` by fast-forward, after the human's approval; the worktree and branch are removed.

## Flags

`18.1` `ASSUMPTION` **· settled** — Beyond clause 1, inside the listed file, I added one sentence: "The worker reads the `STANDING YES` line as the pause." It tells the manager that the resume in step 2 is still sent on a pause, and that the worker does not take it as "continue". The fact is already fixed by the implementation contract's `### The raise`, which node 14 shipped. Without the sentence, a manager could read the pause steps as replacing the resume.

## Review

### Checker run 1 — `PASS`

The checker's entry, as it wrote it:

PASS
- Scope: `git status --short` in the worktree shows exactly one modified path, `.claude/skills/expedition-standing-yes/SKILL.md`, which is the file the condition lists. No edit sits outside the list. The condition records no search, so I had no command to re-run.
- Clause 1 is met. `git diff` shows a paragraph added inside step 2 of `## Taking a covered item`. It reads: "Where a covered raise's `RECOMMENDED` is a pause, also carry out the steps under `## A paused implementation node` in the `expedition` skill's `SKILL.md`." The heading resolves: `grep -n "^## A paused implementation node" .claude/skills/expedition/SKILL.md` hits once. I compared the paragraph with that heading's six steps (mint the enabling node, `Blocked by:`, leave it `claimed`, the slot count, the rebase, "continue"). The paragraph restates none of them.
- Bar: the root `CLAUDE.md` `## Commands` says there is no build, no tests, no formatter and no CI. The repository bears that out, so there is no command to run. I ran `git diff --check`, which was clean.
- Standards: I read only the standards in `.scratch/rename-split-upgrade/map-implementation-rules.md`. Two of them bore on this work:
  - The glossary `_Avoid_` lines. "pause" is used here in its glossary sense under **Pause**, and the refusal at line 265 is aimed at another concept, so the use is correct. No other added word hits an `_Avoid_` line.
  - The writing rules in the root `CLAUDE.md`, especially rule 6. The pointer names the heading and says in one clause what the reader goes there for. The manager is already told to read `expedition/SKILL.md` as its contract. The sentences are plain, with one idea each and no line-number citations.
- The trigger-file standard does not apply, because the work does not touch `expedition/SKILL.md`.
- I ran no reviewing skill, because the standards name none that can run. I checked `/writing-for-agents`, `/coding-principles` and `/naming` by hand, and they apply only to the prose here.

Flags: 18.1 is true of the work. The added sentence "The worker reads the `STANDING YES` line as the pause." is in the file. `expedition-implementation/SKILL.md` already says the same in "Where your `RECOMMENDED` was the pause, read it as the pause." (the `STANDING YES` resume passage), so the two are consistent.

### Gate outcome — approve

The human's words, `verbatim`:

> approve
