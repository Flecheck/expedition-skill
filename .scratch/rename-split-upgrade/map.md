# Map: rename the repository, run several deliverables in one effort, upgrade a conversation into an expedition

**This effort is closed.** The human closed it on 2026-10-13, `verbatim`: *"close"*, after the effort closing report that followed sweep round 1. Its rules bind no later effort.

Every worker reads this whole file once per node. What only the manager acts on is in
[map-manager-only.md](map-manager-only.md). What an implementation node's work is held to is in
[map-implementation-rules.md](map-implementation-rules.md).

## Destination

Three improvements to the expedition workflow have landed in this repository's shipped files, each
from the human's request that started this effort:

1. **Rename.** The repository carries a new name, something like `expedition-skill`, and every
   reference to the old name `graph-agent` that the rename makes wrong is updated.
2. **Several deliverables in one effort.** One effort can hold several pieces of work on the same repo
   that are slightly related but mostly independent. Each piece is worked in its own worktree and
   lands on its own branch as its own pull request. When a piece is finished, the graph is cleaned of
   what that piece no longer needs.
3. **Upgrading a conversation.** A conversation that was not started as an expedition can be turned
   into one, so that work which proved too complex, or which turned out to be several tasks, is split
   into an effort's nodes.

The effort is expected to reach this destination.

The human, on destination 2, `verbatim`: *"Also for Destination 2, I am not sure yet but I might want it to be my main way of working and continue indefinity on it for all small tasks, as I have new things to do I add then and when they are merged I cleanup the graph."*

The human's request, `verbatim`, as it started the effort:

> I have a few improvements I have in mind. First the repo should be renamed to something like
> expedition-skill or something similar. Second: I have a new use case, I want to work on multiple
> things at once on the same repo, the things are slightly related but are mostly independent. I would
> like to run them in an expedition, and when each part is finished, cleanup the graph. Here each
> feature/thing would be worked on different worktrees and pushed as different pull requests on
> different branches. For example, in the last few days I started to work on a feature, this feature
> caused me to start bechmarking, the benchmark made me optimize and optimasation needed an upgrade of
> the packages of the repo that was unblocked recently to be done. During the benchmarks and
> optimization, I found bugs so I had to make a bug fix ... . I had to handle all of the spliting of
> task myself and some chat where too big for the 1M context and so I had to compact which can cause
> quite a bit of loss of information. And the third thing, linked, is to be able to convert a current
> conversation to run on the expedition skill. The idea is that if I see it is too complex or there are
> multiple tasks, I can upgrade it to an expedition and then split the work.

## Notes

- **Domain.** The product of this effort is the expedition skill files under `.claude/skills/`, and
  `.claude/rules/expedition-triggers.md`. The root `CLAUDE.md` states the rules for writing them, the
  standards they are held to, and the duty to keep the trigger file in step with `SKILL.md`.
- **Ground rules.** Work in this effort is held to the standards listed under `## Standards` in the
  root `CLAUDE.md`, and to its `## Rules for the files under .claude/skills/`. Nothing is pushed
  without the human's word.
- **Sources.** The shipped files under `.claude/skills/` and `.claude/rules/`, and the root
  `CLAUDE.md`, are authoritative. `.scratch/graph-workflow/` is the record of a closed effort. It is
  evidence only, and its rules bind nothing in this effort.

## Decisions so far

See [decisions.md](decisions.md).
