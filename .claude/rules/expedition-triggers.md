---
paths:
  - ".scratch/**/map-manager-only.md"
  - "**/expedition/SKILL.md"
---

# Triggers a manager acts on

Three moments, each with the one duty it fires. **Every duty here is a manager's own**, and a worker
reading them acts on none of them.

- **A node finishes**, so the frontier is looked at and a replacement is started as soon as what is
  owed to the record is written.
- **An agent hands something back for the human**, so it goes in front of them as soon as nothing else
  is.
- **The human should have one thing to do**, if the human has nothing to do and there is a question/gate, give it to him. Wait for him to answer before giving him a question. Where several are waiting, pick the one the order gives you and send it — never list them and ask him which to take.

## Priority

- Writing information to files — writing what is supposed to be written.
- Resuming an agent.
- Spawning an agent, respecting the limits.
- Giving a question to the human.
- Waiting, and only where nothing above is available.

## Where every other rule lives

The instruction on how to behave and how to use the map are in the skill `/expedition` and next to it `graph-conventions.md`

Every other rule an effort works under is in its map — `.scratch/<effort>/map.md` and the files beside
it. **This file holds the triggers above and a copy of the priority that orders them, and it overrides
nothing there.** The governing statement of both is in the `/expedition` skill; this file is the copy
that survives a compaction.
