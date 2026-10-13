# Count a paused node out of frontier.sh's code slots

Type: implementation
Status: resolved
Blocked by: ~~14~~

## Question

This lets a manager read free code slots straight from `frontier.sh` when a node is paused, instead of correcting its count by hand. Today the script counts every claimed implementation node against the slots, including a paused one, which is claimed with an unresolved `Blocked by:` node.

*Manager's note:* minted by the worker of [node 14](14-ship-the-rule-for-widening-scope.md) on its `NEW NODES` part, with the question and condition below as it wrote them.

## Acceptance condition

Scope: the named places are the work, and the scope came from no search. The files this work may change are `.claude/skills/expedition/scripts/frontier.sh` and `.claude/skills/expedition/SKILL.md`. Any other instance is edited only on the three grounds the implementation contract states, with a flag naming the place and the reason; any other is reported and not edited.

1. `frontier.sh`'s count of implementation nodes against the code-slot target leaves out every `claimed` implementation node whose `Blocked by:` field, read by the script's existing blocker rule, names a node that is not `resolved`.
2. The script's printed line for that count says that a paused node is not counted.
3. In `.claude/skills/expedition/SKILL.md`, the sentence "It counts a paused implementation node as claimed, so take each paused node off its count of implementation nodes." is removed. No other sentence there changes in meaning.

*Manager's note, before the claim:* nothing is written after the condition. The sentence clause 3 quotes is present in `.claude/skills/expedition/SKILL.md` at `6cbf5ed0cf`, wrapped across lines. Its scope came from no search. Node 14 resolved, so the blocker is struck.

## Answer

`frontier.sh` no longer counts a paused implementation node against the code slots. A paused node is one that is `claimed`, of type `implementation`, and has a `Blocked by:` node that is not `resolved`. The blocker loop that already decided whether an open node is startable has been moved, unchanged, into one awk function, `has_unresolved_blocker(n)`. The startable check and the new paused check both call it. That function is the script's existing blocker rule: it skips struck entries, code spans and link targets, and treats a blocker that is unknown or not resolved as blocking. The printed line now reads `implementation, the nodes that hold a code slot, not counting a paused node: N of M`. In `.claude/skills/expedition/SKILL.md`, the paragraph on `scripts/frontier.sh` loses the sentence "It counts a paused implementation node as claimed, so take each paused node off its count of implementation nodes." The rest of that paragraph is only rewrapped, with the same words. Only implementation nodes are left out of the count. A claimed grilling node with an unresolved blocker is still counted, because the condition and the pause rule are about code slots only.

*Manager's note:* landed as `b4043115ff` on `master` by fast-forward, after the human's approval; the worktree and branch are removed.

## Flags

`17.1` `ASSUMPTION` **· settled** — The paused check in frontier.sh applies only to implementation nodes, so a claimed grilling node with an unresolved blocker still counts against the human target. Clause 1 is about the code-slot count only. The pause in `## A paused implementation node` is defined only for implementation nodes. Leaving the grilling count alone keeps its line's meaning as it was.

## Review

### Checker run 1 — `PASS`

The checker's entry, as it wrote it:

PASS

Condition, part by part:
1. Implementation nodes that are `claimed` and have an unresolved blocker are left out of the count. Both scripts were run on a fixture in a temporary directory, which has since been removed. In the fixture, node 01 is a resolved implementation node. Node 02 is a claimed implementation node blocked by 01. Node 03 is a claimed implementation node blocked by 05, which is claimed. Node 04 is a claimed implementation node with the field `` `[05](x.md)`, ~~06~~, 99 ``, which leaves only 99, a node that does not exist. Node 05 is a claimed grilling node blocked by 06. Node 09 is a claimed implementation node with no blocker. There are also three open implementation nodes, 06, 07 and 08. The HEAD script (`git show HEAD:.../frontier.sh`) printed implementation 4 of 2. The new script printed 2 of 2, which counts 02 and 09 and leaves out 03 and 04. The startable list was identical under both: 6 f and 7 g. The check reuses the script's existing rule through the new `has_unresolved_blocker`, which calls `blocker_numbers` and the same resolved test that the open-node path now also uses (diff of the `END` block).
2. The printed line now reads "implementation, the nodes that hold a code slot, not counting a paused node: %d of %d". Established from the diff and from the new script's output.
3. Both versions of SKILL.md were joined into single lines and compared in python3. The sentence "It counts a paused implementation node as claimed, so take each paused node off its count of implementation nodes." is in HEAD and absent from the work. Removing that one sentence from the HEAD text gives exactly the new text (`o.replace(s,"",1)==n` is True), so the only other change is rewrapping and no other sentence changed.
Scope: `git status --short --untracked-files=all` shows only the two listed files modified. Nothing outside the list was edited. The condition records no search, so no recorded command was run.

The bar: The root CLAUDE.md `## Commands` says the repository has no build, no tests, no formatter and no CI. I confirmed this: the root holds only .claude, CLAUDE.md, CONTEXT*.md, .gitignore and .scratch, with no .github, and neither shellcheck nor shfmt is installed. As an extra check I ran `sh -n frontier.sh`, which passed, and the script exited 0 on the fixture. The style is consistent with the file: tab indentation, and the new function declares its locals as extra parameters like the existing functions do.

Standards: I read only the standards in `/home/mathieu/projects/graph-agent/.scratch/rename-split-upgrade/map-implementation-rules.md`. These are /coding-principles, /naming, the glossary's `_Avoid_` lines, graph-conventions.md, /writing-for-agents, the root CLAUDE.md writing rules, and the trigger-file rule. These bore on the work:
- Naming: `has_unresolved_blocker` and `is_paused` are clear names.
- No-silent-fail: a blocker that does not exist counts as unresolved, the same as the existing rule.
- Glossary: "paused" matches **Pause** and **Code slot** ("A paused node's worktree is not counted while the node is blocked"). No `_Avoid_` term is introduced.
- The SKILL.md edit removes a now-false instruction and is consistent with `## A paused implementation node` item 4.
- Trigger file: not touched. The edited passage describes frontier.sh, which is neither a trigger-duty nor the priority, so `.claude/rules/expedition-triggers.md` did not need to change.
No reviewing skill is named by the standards, so none was run. The standards were applied by hand.

Not checked: whether the script runs under awks other than gawk. No mawk, nawk or busybox awk is installed on this machine.

Flags: 17.1 is true of the work. On the fixture, the claimed grilling node 05, whose blocker 06 is unresolved, still counts: grilling showed 1 of 2.

Worktree: /home/mathieu/projects/graph-agent/.scratch/rename-split-upgrade/worktrees/17-frontier-paused

### Gate outcome — approve

The human's words, `verbatim`:

> approve
