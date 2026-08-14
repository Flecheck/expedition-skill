# Runtime that hosts the manager and its subagents

Type: grilling
Status: resolved

## Question

What runtime hosts the manager thread and the per-issue subagents?

## Answer

**Claude Code skills plus the built-in subagent tooling** — provisionally.

The workflow is a set of skill files. The manager is an ordinary Claude Code session that spawns one subagent per issue with the `Agent` tool. A subagent needing human input pauses by returning a question; the manager relays it and resumes the same subagent with `SendMessage`, which continues it with its context intact. Verified: this harness's `SendMessage` resumes an already-spawned agent without losing its context, so a question round-trip needs no external processes.

Rejected for now: a firstmate-style distro (tmux windows, file mailboxes, per-crewmate worktrees) and a custom Claude Agent SDK orchestrator. Both are strictly more machinery.

**Flagged as provisional by the user:** "it might be a bit too simple but we will see." Treat this as a decision to revisit after the first dogfood run, not a settled one. The upgrade path is the firstmate shape — see the map's *Not yet specified*.
