# Map: the rules an implementation node's work is held to

An implementation node's worker and its checker read this file.

## What the work is held against

- **The bar's commands.** The root `CLAUDE.md`, under `## Commands`, states that this repository has
  no build, no tests, no formatter and no CI. Confirm that against the repository before relying on
  it.
- **The standards.** `/coding-principles` and `/naming`; the `_Avoid_` lines of
  `.claude/skills/expedition/glossary.md`; `.claude/skills/expedition/graph-conventions.md`; and
  `/writing-for-agents`, found by name in the `mattpocock-skills` plugin. The rules for writing under
  `## Rules for the files under .claude/skills/` in the root `CLAUDE.md` apply to every shipped file.
- **The trigger file.** A change to the governing statement, in `.claude/skills/expedition/SKILL.md`,
  of a manager trigger-duty or of the priority that orders them, edits
  `.claude/rules/expedition-triggers.md` in the same change, or says plainly why not.
