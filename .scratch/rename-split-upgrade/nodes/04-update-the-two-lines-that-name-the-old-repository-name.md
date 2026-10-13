# Update the two lines that name the old repository name

Type: implementation
Status: resolved
Labels: RENAME

## Question

The repository is renamed from `graph-agent` to `expedition-skill`. This work makes the repository's own text name it correctly. It also removes a shipped glossary entry that names this one repository, so the skill files assume no particular repository. Retitle the root `CLAUDE.md`, and drop `graph-agent` from the glossary's `_Avoid_` line under Expedition.

*Manager's note:* minted by the worker of [node 01](01-what-the-repository-is-renamed-to.md) on its `NEW NODES` part, with the question and condition below as it wrote them.

## Acceptance condition

1. The first line of `CLAUDE.md` at the repository root is exactly `# expedition-skill`. Before the change it was `# graph-agent`. No other line of `CLAUDE.md` changes.
2. In `.claude/skills/expedition/glossary.md`, the `_Avoid_` line that directly follows the definition of the term **Expedition** reads exactly `_Avoid_: wayfinder`. Before the change it read `_Avoid_: graph-agent (the repository's name, not the workflow's), wayfinder`. No other line of that file changes.
3. No tracked file under `.scratch/` changes, and no other tracked file changes.
4. Scope: on 2026-10-12, the command `grep -rn "graph-agent" --exclude-dir=.git --exclude-dir=.scratch .`, run from the repository root over the working tree, returned exactly two lines. One was `CLAUDE.md:1:# graph-agent`. The other was `.claude/skills/expedition/glossary.md:22:_Avoid_: graph-agent (the repository's name, not the workflow's), wayfinder`. The line number is the line number of that date and is for scale only. After the work, the same command returns nothing. An instance it finds outside the two files above is reported and not edited.

*Manager's note, before the claim:* re-ran the recorded command from the repository root on 2026-10-12. It returned the same two lines, so the scope has not grown. Both quoted passages are present.

## Answer

The two edits are made in the worktree, uncommitted. The root `CLAUDE.md`'s first line changed from `# graph-agent` to `# expedition-skill`. In `.claude/skills/expedition/glossary.md`, the `_Avoid_` line under the term **Expedition** changed from `_Avoid_: graph-agent (the repository's name, not the workflow's), wayfinder` to `_Avoid_: wayfinder`. No other line changed, and no other file changed. After the edits, the scope command `grep -rn "graph-agent" --exclude-dir=.git --exclude-dir=.scratch .`, run from the worktree root, returns one line: `.git:1:gitdir: /home/mathieu/projects/graph-agent/.git/worktrees/04-update-the-two-lines`. In a linked worktree, `.git` is a file rather than a directory, so `--exclude-dir=.git` does not exclude it. The line holds the main checkout's absolute path, which still carries the old name until the human renames the checkout. It is git's own metadata and is not tracked. It was reported and not edited. In the main checkout, where `.git` is a directory, the same command returns nothing. Adding `--exclude=.git` in the worktree also returns nothing (exit status 1).

*Manager's note:* landed as `7fb8f31f22` on `master` by fast-forward, after the human's approval. The worktree and its branch are removed.

## Review

### Checker run 1 — `PASS`

The checker's entry, as it wrote it:

PASS

1. CLAUDE.md first line. `head -1 CLAUDE.md | od -c` gives exactly `# expedition-skill\n`. `git diff -- CLAUDE.md` shows one hunk that changes only line 1, from `# graph-agent` to `# expedition-skill`.
2. The glossary `_Avoid_` line under **Expedition**. `sed -n 18,23p .claude/skills/expedition/glossary.md` shows that the line directly after the definition of **Expedition** is exactly `_Avoid_: wayfinder`. `git diff -- .claude/skills/expedition/glossary.md` shows one hunk that changes only that line, from `_Avoid_: graph-agent (the repository's name, not the workflow's), wayfinder`.
3. No other tracked file changed. `git status --porcelain --untracked-files=all` lists only ` M .claude/skills/expedition/glossary.md` and ` M CLAUDE.md`. `git diff --stat` shows 2 files changed, 2 insertions and 2 deletions. Nothing under `.scratch/` changed. The worktree HEAD is `316fc9fb15`, which is also the main checkout's HEAD.
4. The recorded search. I ran `grep -rn "graph-agent" --exclude-dir=.git --exclude-dir=.scratch .` as written from the worktree root. It returned one line: `.git:1:gitdir: /home/mathieu/projects/graph-agent/.git/worktrees/04-update-the-two-lines`. The condition records an empty return, so this does not match. See QUESTIONS. I then ran the same command with `--exclude=.git` added, and it returned nothing (exit 1). Every repository file the command searches is free of `graph-agent`.

The bar:
- Commands. The root `CLAUDE.md`, under `## Commands`, says the repository has no build, no tests, no formatter and no CI. I confirmed this with `git ls-files`. No package.json, Makefile, Cargo, pyproject, flake, CI, pre-commit or formatter config is tracked outside `.scratch/`. The one script is `.claude/skills/expedition/scripts/frontier.sh`, and the work does not touch it. There was nothing to run.
- Standards. I read only the standards in `.scratch/rename-split-upgrade/map-implementation-rules.md`. Those standards are `/coding-principles`, `/naming`, the glossary's `_Avoid_` lines, `graph-conventions.md`, `/writing-for-agents`, the root `CLAUDE.md` rules for writing, and the trigger-file rule. I held the work against them by hand and invoked no skill. The change is two lines of plain text with no code.
- The ones that bore on this work:
  - The glossary's `_Avoid_` lines. I settled what moved first. The work removed one element: `graph-agent` is no longer refused for Expedition. This work does not have to be held against that element, because neither changed line uses `graph-agent` as a name for the workflow. No `_Avoid_` line refuses `expedition-skill`: `grep -n "_Avoid_" glossary.md | grep -i -e skill -e expedition -e repo` returns no such refusal.
  - Writing rule 6 on renaming a heading. Renaming the `# graph-agent` heading leaves no stale citation. The search in part 4, with `.git` excluded, finds no other occurrence of `graph-agent`.
  - The trigger-file rule does not apply, because `SKILL.md` was not touched.

QUESTIONS:
- The condition's recorded command does not return nothing when run in this worktree.
  - Instance: it returns `.git:1:gitdir: /home/mathieu/projects/graph-agent/.git/worktrees/04-update-the-two-lines`. In a linked worktree `.git` is a file, not a directory, so `--exclude-dir=.git` does not exclude it. The line is git's pointer to the main checkout's absolute path. That path contains the directory name `graph-agent`. The pointer is not tracked repository content, and the worker cannot edit it.
  - Form: a line that the recorded command returns from outside the tracked working tree.
  - Extent: `git ls-files -z | xargs -0 grep -n "graph-agent" -- 2>/dev/null | grep -v '^\.scratch/'` lists every candidate the worker may edit. It returns nothing.
  - Run in the main checkout after landing, where `.git` is a directory, the command should return nothing. The command's wording comes from the condition, so departing from it was not the worker's choice.

### Gate outcome — approve

The human's words, `verbatim`:

> approve
