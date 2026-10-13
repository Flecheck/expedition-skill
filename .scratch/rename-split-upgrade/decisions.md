## RENAME

- [01](nodes/01-what-the-repository-is-renamed-to.md) — The repository is renamed `expedition-skill`. The human renamed it on GitHub and renames the local checkout and its Claude Code project directory between sessions. The manager resets `origin`. One node edits two lines.
- [04](nodes/04-update-the-two-lines-that-name-the-old-repository-name.md) — The root `CLAUDE.md` is retitled `# expedition-skill` and the glossary's Expedition `_Avoid_` line is now `_Avoid_: wayfinder`, so no tracked file outside `.scratch/` names `graph-agent`.

## Unlabelled

- [09](nodes/09-an-implementation-node-may-widen-its-own-scope.md) — An implementation worker may edit outside its condition's list on three grounds (made wrong by its own change, further instance, enabling change), one flag per place; the checker verifies; an enabling change too big pauses the node.
- [18](nodes/18-take-a-pause-under-a-standing-yes.md) — `expedition-standing-yes` now says that where a covered raise recommends a pause, the manager also carries out `## A paused implementation node` in the `expedition` skill, by pointer.
- [16](nodes/16-two-code-slots-by-default.md) — The manager contract now gives code slots a default of two, unless the effort's map sets another number, matching the default for nodes that need the human.
- [17](nodes/17-count-a-paused-node-out-of-frontier-sh.md) — frontier.sh now leaves a paused implementation node (claimed, with an unresolved blocker) out of its code-slot count and says so; SKILL.md's manual-subtraction sentence is removed.
- [15](nodes/15-whether-flags-md-is-dropped.md) — `flags.md` is dropped; each node's `## Flags` entry, opening with a one-sentence report, is the only record of a flag; only outstanding off-product `FRICTION` flags reach the effort closing report and region cleanup.
- [14](nodes/14-ship-the-rule-for-widening-scope.md) — Shipped node 09's widening rule: workers may edit outside the condition's list on three flagged grounds that the checker verifies, and a too-big enabling change pauses the node behind an enabling node.
- [19](nodes/19-ship-dropping-flags-md.md) — Shipped dropping `flags.md`: a node's `## Flags` entry, opening with a one-sentence report, is the only flag record. Check 6 now checks ids. Flag cleanup is gone. `## The seven files` became `## The graph's files`.

## SPLIT

- [02](nodes/02-several-deliverables-in-one-effort.md) — An effort may declare deliverables, each with its own branch. A node's worktree is cut from its deliverable's branch, which approval fast-forwards. The manager pushes on the human's yes, the human opens the pull request, and merged deliverables are cleaned up by region.
- [05](nodes/05-ship-deliverables.md) — Shipped deliverables: glossary entry, `## Deliverables` list and `Deliverable:` field with check 12, landing, push, base and rebase rules in SKILL.md, merged-deliverable region cleanup, and a standing yes covering a push.
- [06](nodes/06-which-checkout-a-non-implementation-worker-reads.md) — Any node may carry `Deliverable:`. Implementation nodes name exactly one deliverable, other nodes zero or more. Non-implementation workers read each listed deliverable's code at a spawn-given commit through git. Cleanup waits until every listed deliverable has merged.
- [08](nodes/08-a-deliverable-that-lands-by-merging-locally.md) — A deliverable may take `base: local <branch>` and land by a local merge on the human's yes: rebase and fast-forward by default, overridable; with no stated default, deliverables push upstream.
- [10](nodes/10-ship-deliverable-on-every-node-kind.md) — Shipped: `Deliverable:` on any node, with exactly one name on an implementation node. Non-implementation spawns give each deliverable's branch and commit, read through git. Cleanup waits for every listed deliverable. Triage and scoping searches read deliverable branches.
- [11](nodes/11-ship-the-local-merge-of-a-deliverable.md) — Shipped `base: local <branch>`: on the human's yes a deliverable lands locally by rebase then fast-forward, overridable by policy or per merge, with cleanup proposed right after, and standing yes covering it.
- [12](nodes/12-re-derive-a-deliverable-nodes-scope-against-its-branch.md) — Shipped: before claiming a node whose `Deliverable:` names a deliverable, the manager re-runs its scope search and searches for quoted passages on that deliverable's branch tip, read through git.

## UPGRADE

- [03](nodes/03-upgrade-a-conversation-into-an-expedition.md) — `/expedition-upgrade <request>` makes the conversation's thread the manager of a new or named effort. Past decisions go into one resolved node, and uncommitted work goes into a gated implementation node.
- [07](nodes/07-ship-expedition-upgrade.md) — Shipped `.claude/skills/expedition-upgrade/SKILL.md`. It covers the request, the steps, what is carried into the record, transcript extraction, a promoted existing branch and uncommitted changes. `## Starting an effort` now points to it.
- [13](nodes/13-fix-the-upgrade-skills-citations-of-its-own-subsection.md) — Steps 3 and 6 of `/expedition-upgrade` now cite `### A branch that already exists` at its real heading level. The search found no other instance in the shipped files.
