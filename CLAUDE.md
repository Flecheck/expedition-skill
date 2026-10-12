# expedition-skill

## What this repository holds

- The `/expedition` workflow's skill files, under `.claude/skills/`. The vocabulary they are written in is `.claude/skills/expedition/glossary.md`.
- `.claude/rules/expedition-triggers.md`, which the harness loads by itself into an agent that reads a file matching its `paths:` frontmatter.
- One directory per effort, at `.scratch/<effort>/`, holding that effort's record. An effort's map is the file `map.md` in that directory. Its sibling files hold what only some readers need.

## Commands

This is the repository's own statement of its commands. It has no build, no tests, no formatter and no CI, so there is no command to run. The bar here is therefore the standards listed under `## Standards`, plus the node's acceptance condition.

## Standards

Work in this repository is held to:

- `/coding-principles` and `/naming`;
- the `_Avoid_` lines of `.claude/skills/expedition/glossary.md`;
- `.claude/skills/expedition/graph-conventions.md`;
- `/writing-for-agents`.

## Rules for the files under `.claude/skills/`

Ground rules:

1. Nothing in these files may assume this repository, this machine, or a toolchain. Prefer properties that are discovered over commands that are declared.
2. Each worker contract stands alone as a file, rather than depending on any skill being invocable.
3. The human talks only to the manager. No agent the workflow spawns addresses the human directly, and nothing in the files may tell one to.
4. Prefer short, simple prose that can be changed later over machinery built for predicted needs. Reserve heavy design for the hard-to-reverse core.
5. Prose in these files is held against the `/writing-for-agents` standard. That standard is specific to this repository and is never shipped. Locate it by name in the `mattpocock-skills` plugin, rather than by path.

Rules for writing:

1. Compress the prose that explains why. Never compress the shapes.
2. An entry states its current form and cites the nodes that shaped it. It does not restate what they hold.
3. A long answer is navigable by heading, so a reader following a link for one fact reads one section.
4. Cite a file by heading or by a quoted phrase, never by line number. Append-in-place shifts every line below the append, so a line number decays without anything reporting it.
5. Write plain English. State a rule as what to do. Use a prohibition only where the rule cannot be said as what to do, and then beside the positive. Bold a term only where it is defined. Say any idea that is not a term defined in the glossary in plain words, with no figure of speech and no coined phrase. Make statements directly rather than as slogan-shaped contrasts. Write every sentence grammatically, with one clear referent for each pronoun. Put one idea in each sentence.
6. Point at a heading of another file under `.claude/skills/` instead of restating what it holds, where the reader is already told to read that file. A pointer names the heading and says, in one clause at most, what the reader goes there for. It lists none of the entries that heading holds and states none of its rules. Where the reader is not told to read that file, and that file is mostly text the reader does not need, restate what the reader needs, so the reader is not sent to read it. A passage that changes a rule for its own case names that rule by heading and states the change in its own words. Rename a heading that another file under `.claude/skills/` cites only in the change that updates every citation of it. Find those citations by searching the files under `.claude/skills/` for the heading's exact text.

## The trigger file

`.claude/rules/expedition-triggers.md` holds a copy of the manager's trigger-duties and of the priority that orders them. Their governing statement is in `.claude/skills/expedition/SKILL.md`. Whoever edits, in that `SKILL.md`, the governing statement of one of those duties, or of the priority, edits `.claude/rules/expedition-triggers.md` in the same change, or says plainly why not.

## The worktree of an implementation node

- The manager makes it with plain `git worktree add`, at `.scratch/<effort>/worktrees/<NN>-<name>`, on a branch `worktree-<NN>-<name>`. `<NN>` is the node's id.
- `.gitignore` ignores that path.
- The worker writes the tree by absolute path, and owes no cleanup.
- The fast-forward merge into the main checkout, and the worktree's removal, run with the sandbox off.

The full steps, with the failure each sandbox-off step avoids, are in `.scratch/graph-workflow/map-manager-only.md` under `## Landing an implementation node's work`, in the passage headed *How the worktree is made*.

## Two traps

- Many refused words in the glossary's `_Avoid_` lines are ordinary English, refused only for one concept, such as `report`, `run`, `session` and `question`. A grep for them gives false positives. Check the distinctive refusals by hand.
- A number about an effort's record that is handed to another agent, or written into an acceptance condition, carries the date it was derived. The text carrying it says the number is for scale only and is not authoritative.

## Pushing

Nothing is ever pushed without the human's word.
