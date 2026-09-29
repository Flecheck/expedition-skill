# The manager sees its own writable region before it spawns a worker or lands work

Type: grilling
Status: resolved

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

## Interview

### Attempt 1

*The attempt's routing key does not survive the manager's session, so it is not recorded here.*

**The worker's question** is pasted in full on the manager's relay; its `ASK` and `RECOMMENDED` are quoted below with
the human's reply, which is the form `graph-conventions.md` asks for.

**The human's reply, `verbatim`.**

> no schedule

**The option it takes**, quoted from the worker's own `ASK` and `RECOMMENDED` and attributed to the worker:

> **ASK:** Should the manager run this region check on a schedule — before each spawn, before each landing, or after
> each worktree cycle — or not on a schedule at all, running it only as a diagnostic when a write has actually failed?
>
> **RECOMMENDED:** **No schedule. Run it as a diagnostic when something fails, and close the silent case at the worker
> instead of at the manager.**

***The manager's note.*** **Not a divergence**: the reply names the `RECOMMENDED` route and none of the five
alternatives. **What it does not name either way** is the worker's own honest caveat — that the recommendation is half
a fix, class A staying silent until an implementation worker probes its own tree — which the worker offered to report
as a node rather than assume. The manager has not read the reply as settling that and has not settled it.

***The manager's note on evidence produced after the question was relayed.*** **The landing of [node
169](169-rules-file-bar-paragraph-names-the-maps-standing-preferences.md) ran while the manager's region was in state
A and succeeded**, because the five paths that landing actually writes were all writable though the repository root
was not. The manager reports the observation on both nodes and draws no conclusion; it arrived after the human had
the question and did not reach them before they answered.

## Answer

*Pasted as the worker wrote it.*

> **The manager runs no scheduled region check.** The human's words, `verbatim`: *"no schedule"* — naming the recommendation and none of the five alternatives put to them.
>
> **The ground is stronger than *not worth it*: a scheduled check cannot work, because a region is not healthy or broken on its own.** Node 175's operative rule already says a command succeeds exactly when every path it writes lies inside a `rw` mount and outside a `ro` one. Read strictly, that makes writability a relation between a session and *a set of paths*, never a property of a session — so there is nothing for a scheduled reading to be a reading *of*, and a schedule cannot know which paths the next operation will write. Three observations from this node measure it:
>
> - **The manager landed node 169 from a session with no writable repository root, and the landing succeeded**, because the five paths that landing writes were all writable. A scheduled region reading would have called that session broken and held a landing that was fine.
> - **This node's worker ran its whole node from that same shape** and was never impeded, because a grilling worker writes nothing.
> - **The region changed twice under this worker in one node.** Worktree `169`'s tree was writable at the node's start and denied by its end, and worktree `177`'s mounts appeared in between. A reading describes the instant it was taken and nothing after it.
>
> **What the manager does instead: the mount table is a diagnostic, run after a write has failed, not before one.** Its value is telling two shapes of denial apart, because they have different remedies: a **`ro` entry over a path inside a tree** means the tree is yours and one path is denied, and the operation succeeds on a retry with the sandbox off; **the tree missing from the table entirely** means it is not yours to write at all, and only waiting cures it.
>
> **Two instruments, and which one applies follows from what you are doing.** `test -w <path>` answers *will this exact write succeed*, directly, with no verdict rule to get wrong, and it was measured here to agree with the actual outcome on all four paths tried. The mount table answers *what shape is the denial*, which `test -w` cannot say. The first is the manager's, on the paths an operation is about to write; the second is for after a failure. **Neither is a health check, and the record should stop using the words healthy and broken for a region.**
>
> **A third instrument that looks available and is not: the agent's own system prompt.** Its sandbox block named a worktree that no longer existed. An agent cannot learn its region from its prompt.
>
> **Where this lives: this effort only, and nothing ships.**
>
> **What this node does not close.** A worker handed a tree it cannot write still discovers that only at its first git write, because the file-editing tools keep succeeding throughout. No manager-side schedule can catch it. That is reported as a node rather than settled here.

**What the worker reported its work invalidates, pasted as it wrote it.**

> **Node 175's `## Answer`, in two places, and only in its characterisation — every measurement it reports stands.**
>
> 1. *"A **broken** session's set has a different root: … with **no repo root at all**, exactly the manager's reported failure."* A set without the repository root is not thereby broken. The manager landed node 169 from exactly that shape and the landing succeeded; this node's worker ran its whole node from it unimpeded. What node 175's own operative rule supports is that a session is writable *relative to a set of paths*, which is a relation and admits no verdict on a session alone. **The word `broken` is what made both the manager and this node's worker start from the belief that a scheduled health check was coherent.**
> 2. *"So a manager whose region has migrated silently cripples **every** worker it spawns while that lasts."* Too strong by the same step. It cripples every worker whose needed paths fall outside its region, which is not every worker.

## Flags

*Both are the worker's own text, pasted.*

`179.1` `ASSUMPTION` **· settled** — **this rule is this effort's and reaches no shipped file.** The node's question had a second half, where the instruction lives, and it was settled against the record rather than put to the human: `map.md`'s rule that a standing rule reaches a shipped file only where the human says so, and its constraint that the shipped files assume no machine or toolchain, which a `/proc/mounts` instruction would. The human was told in the payload's `SO FAR` that this had been settled this way and that one word would overturn it. No word came either way, so it stands.

`179.2` `ASSUMPTION` **· settled** — **the per-path `test -w` is recorded as available, not as required.** The manager was measured running `test -w` on a landing's five paths before running it, successfully, and that evidence arrived after the human had already declined a check before each landing. A per-path test of the very next command's precondition is a different instrument from a scheduled reading of general health — the two disagreed on the same session and the per-path one was right — but mandating it would reinstate a moment the human declined. So the answer records it as available to whoever is about to write and stops short of requiring it.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
