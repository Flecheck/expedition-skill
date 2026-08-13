# Git and code-landing policy

Type: grilling
Status: open
Blocked by: 06

## Question

How does code produced by an implementation subagent land, and how is that recorded in git?

Settled inputs: one code-modifying subagent at a time in v1 (no worktrees); later, worktrees plus `git merge --ff-only` onto the manager's branch. This issue works out the rest.

- Branch layout: one branch for the whole effort, or a branch per implementation node?
- Does an implementation subagent **commit its own work**, or hand a diff back to the manager to commit?
- How is the single-writer lock actually expressed, given the manager is the only thing that spawns subagents — is it an explicit recorded lock, or an emergent property of the manager's scheduling?
- How does a **revision** land against code that already shipped — a new commit forward, or a rewrite of the earlier one? (Depends directly on [Revision semantics](06-revision-semantics.md).)
- Does the effort's history stay legible as a record of the route walked, or is it squashed at the end?

Added by [Node type taxonomy](07-node-type-taxonomy.md), which now also depends on this node:

- **Prototype artifacts live outside the product tree**, so a prototype never contends for the exclusive code slot. This was adopted on agent judgement rather than asked, and this node owns where things land, so it is the place to confirm or overturn it. If prototypes *do* land in the tracked tree, the concurrency consequence is immediate: a HITL prototype and an AFK implementation could no longer run at the same time.
- **Landing includes a review step.** An implementation node is not resolved until an independent read-only agent has checked it, so "how code lands" is now implement → review → possibly rework → land, with the code slot held throughout.

Prerequisite noticed while charting: **this directory is not yet a git repository.** Whatever this issue decides, `git init` has to happen before any implementation node can run.
