# Re-derive a deliverable node's scope against its deliverable's branch

Type: implementation
Status: resolved
Labels: SPLIT

## Question

This lets the manager re-derive and check an acceptance condition against the code a node will actually change. That code may sit only on a deliverable's branch, which the main checkout does not receive until the deliverable lands. Today `### Changing one after it is written` in `.claude/skills/expedition/SKILL.md` tells the manager to re-run a condition's recorded search, and to "search the working tree for each passage the condition quotes or names by heading". It says nothing about a node that names a deliverable, so the manager searches the main checkout. This gap predates node 10, and an implementation node naming a deliverable from node 05 already had it.

*Manager's note:* minted by the worker of [node 10](10-ship-deliverable-on-every-node-kind.md) on its `NEW NODES` part, with the question and condition below as it wrote them. It gave the blockers as "none (node 11 also edits `.claude/skills/expedition/SKILL.md`, in different sections; the manager may order them)".

## Acceptance condition

Scope: the named place is the work, and the scope came from no search. `.claude/skills/expedition/SKILL.md`, `### Changing one after it is written`: the passage beginning "Re-derive an enumerated scope before the node is claimed" and the passage beginning "Before you claim an implementation node" say that, for a node whose `Deliverable:` field names a deliverable, the manager re-runs the recorded search, and searches for each quoted or named passage, over the tip of that deliverable's branch, read through git without checking it out. Every other sentence of those two passages is unchanged in meaning.

*Manager's note, before the claim:* nothing is written after the condition. Both passages it names, "Re-derive an enumerated scope before the node is claimed" and "Before you claim an implementation node", are present in `.claude/skills/expedition/SKILL.md` at `14d17da066`. Its scope came from no search, so there is nothing to re-run.

## Answer

In `.claude/skills/expedition/SKILL.md`, `### Changing one after it is written`, two passages now cover a node whose `Deliverable:` field names a deliverable.
- The passage beginning "Re-derive an enumerated scope before the node is claimed" gains two sentences: "Where the node's `Deliverable:` field names a deliverable, run the search over the tip of that deliverable's branch. Read that tip's files through git, without checking the branch out."
- In the passage beginning "Before you claim an implementation node", two sentences follow "Then search the working tree for each passage the condition quotes or names by heading": "Where the node's `Deliverable:` field names a deliverable, search the tip of that deliverable's branch instead. Read that tip's files through git, without checking the branch out."
No other sentence of either passage changed. Only the last three lines of the second passage were re-wrapped.
Calls made:
- The text says "a deliverable" and not "deliverables", because only an implementation node carries a condition, and an implementation node names exactly one deliverable (node 10).
- The text reuses the "through git, without checking … out" wording that `expedition-triage/SKILL.md` and the non-implementation spawn list in the same `SKILL.md` already use.
- The text names no spawn-given commit. The manager reads the current tip at claim time, as the condition says.
Trigger file: `.claude/rules/expedition-triggers.md` copies neither passage. Neither passage is a manager trigger-duty or the priority, so the trigger file needed no edit.

*Manager's note:* landed as `cf5984eadc` on `master` by fast-forward, after the human's approval; the worktree and branch are removed.

## Review

### Checker run 1 — `PASS`

The checker's entry, as it wrote it:

PASS

Acceptance condition, part by part:
1. Scope (the named place is the work, and the scope came from no search). `git status --short` and `git diff --stat` in the worktree show that only `.claude/skills/expedition/SKILL.md` changed (8 insertions, 4 deletions). The condition records no search command, so there was none to re-run.
2. Location. `grep -n -E "^#{1,4} |^Re-derive an enumerated|^Before you claim an implementation"` puts both passages under `### Changing one after it is written`, before the next heading, `## What is in front of the human, and when`.
3. The first passage, "Re-derive an enumerated scope…", now says: "Where the node's `Deliverable:` field names a deliverable, run the search over the tip of that deliverable's branch. Read that tip's files through git, without checking the branch out." So the recorded search is re-run over the branch tip, read through git, with no checkout. Established by unwrapping the passage (awk range, then `tr '\n' ' '`, then splitting into sentences) on the working copy.
4. The second passage, "Before you claim an implementation node…", now says: "Where the node's `Deliverable:` field names a deliverable, search the tip of that deliverable's branch instead. Read that tip's files through git, without checking the branch out." This sits right after the sentence that searches for each quoted or named passage. Established by the same unwrapped split.
5. Every other sentence is unchanged in meaning. I unwrapped both passages from `git show HEAD:` and from the working copy and compared them sentence by sentence. Every original sentence is still there word for word. The only edits are the two inserted pairs of sentences, plus a rewrap of "than reconstructing one."

The bar:
- The root `CLAUDE.md`, under `## Commands`, says the repository has no build, no tests, no formatter and no CI. I confirmed this against the worktree: there is no package.json, Makefile, *.toml, flake.nix, pre-commit config or .github at the top levels. So there was no command to run. `git diff --check` printed nothing (exit 0), so there are no whitespace errors.
- I read the standards in `/home/mathieu/projects/graph-agent/.scratch/rename-split-upgrade/map-implementation-rules.md`, and nothing else in that file. These four bore on this work:
  - Glossary `_Avoid_` lines: none of the added words (deliverable, tip, branch, search, git, checking out) is a refused term.
  - The `CLAUDE.md` rules for writing: the additions are plain English, one idea per sentence, written as positive rules, with no line-number citations.
  - `/writing-for-agents`: I read it and applied it by hand. It spawns no agents.
  - The trigger file: `grep -i -E "claim|scope|search" .claude/rules/expedition-triggers.md` returns nothing, so the trigger file holds no copy of these passages and needed no edit.
- `/coding-principles`, `/naming` and `graph-conventions.md` gave nothing to hold this prose change against beyond the above.

Note, not a finding: the sentence "Read that tip's files through git, without checking the branch out." now appears in both adjacent passages. The condition requires each passage to say it, so the repetition is the condition's own.

No flags were given, so there were none to check. I wrote no temporary files.

### Gate outcome — approve

The human's words, `verbatim`:

> You can run 2 code slot, I think it should be the default. approve

*Manager's note:* the same message set this effort's code slots to two, recorded in `map-manager-only.md`.
