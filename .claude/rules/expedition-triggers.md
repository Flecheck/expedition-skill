---
paths:
  - ".scratch/**/map-manager-only.md"
  - "**/expedition/SKILL.md"
  - "~/.claude/skills/expedition/SKILL.md"
---

# Triggers a manager acts on

Each of the three moments below starts one duty. Every duty here is the manager's own, so a worker
reading this file acts on none of them.

- When a node finishes, look at the frontier and start a replacement as soon as what is owed to the
  record is written.
- When an agent hands back something for the human, put it in front of the human as soon as nothing
  else is in front of them. Where a standing yes covers it, take it as `/expedition-standing-yes` says
  instead.
- The human should have one thing to do. If the human has nothing to do and there is a question or a gate, give it to him. Wait for him to answer before giving him a question. Where several are waiting, pick the one the order gives you and send it. Never list them and ask him which to take.

## Priority

1. Write information to files: write what is supposed to be written.
2. Resume an agent.
3. Spawn an agent, within the limits.
4. Give a question to the human. The human should always have something to do, and this item keeps
   that true.
5. Before you stop, run a check, which is not an act. It passes when nothing an agent handed back is
   still unfiled, and either the human has something to do or provably nothing is waiting: no gate
   assembled and unsent, no worker blocked on a raise, no raise of your own, and no relayed question.
   If the check fails, send what this order gives you, then stop. Once it passes you are waiting, and
   you never wait in place of running it.

## Where every other rule lives

The instructions on how to behave and how to use the map are in the skill `/expedition` and, next to it, in `graph-conventions.md`.

Every other rule an effort works under is in its map: `.scratch/<effort>/map.md` and the files beside
it. This file holds the triggers above and a copy of the priority that orders them. The `/expedition`
skill holds the governing statement of both, and this copy stays in context after a compaction. Where
this file and the map differ, follow the map.
