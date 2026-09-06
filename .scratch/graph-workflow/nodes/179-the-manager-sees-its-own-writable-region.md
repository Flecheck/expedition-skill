# The manager sees its own writable region before it spawns a worker or lands work

Type: grilling
Status: claimed

Blocked by: none

## Question

*Surfaced by [What the harness worktree cycle does to the manager's writable region](175-what-the-worktree-cycle-does-to-the-sandbox.md)'s worker, and pasted as it wrote it.*

> The manager's region can migrate mid-session and, while it has, every worker it spawns inherits the migration — an
> isolated implementation worker was measured unable to write its own worktree, and the file-editing tools keep
> working throughout so nothing fails visibly until a git write. Does the manager run a cheap region check (one
> `/proc/mounts` read, no risk, no writes), and if so at which moments — before each spawn, before each landing, or
> only after a worktree cycle — and where does that instruction live: this effort's map, or the shipped manager
> contract?

**Blockers, in the worker's words:** *"none. Depends on node 175's answer only."*

## The manager's note at filing

*Not a change to anything above.*

**Its blocker is discharged: node 175 resolved.**

**This is the node the human asked for**, `verbatim`: *"we should make it so that there isn't issues like that
later"*. [Node 176](176-the-managers-record-edits-collide-with-a-landing.md) is the other half — that one is the
landing policy's gap, this one is the detector.

**Its check is `/proc/mounts` and costs nothing.** Node 175 measured the one-liner:
`grep " <repo>" /proc/mounts | awk '{split($4,a,","); print a[1]" "$2}' | sort -u`. Read-only, no writes, one call.
Whether that is a thing the manager should be told to do, and where that instruction lives, is the question and is not
the manager's to answer.

**The severity is the part not to lose.** Node 175 measured a worker spawned during a broken window that could not
write its own worktree, and two workers spawned minutes apart with different regions. So the failure is silent, it is
inherited, and the file-editing tools mask it.
