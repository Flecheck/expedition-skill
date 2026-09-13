# The landing section says the reset requires the sandbox off and also that it is not reliably inside it

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [node 229](229-bank-the-landing-sections-accounts-out-of-map-manager-only.md)'s worker, and pasted as
it wrote it. It found this **outside** its own fourteen spans and left it, the human's licence at node 225 being
bounded to that section's fourteen edits and nothing else.*

> `map-manager-only.md`'s landing section now states the sandbox cost of `git reset --hard` twice and not the same
> way. The first bullet under *How the worktree is made* says flatly that the reset **"requires the sandbox off",
> failing inside it with `Could not reset index file`**; the bullet on `EnterWorktree` being needed for neither step
> now says **"The reset is not reliably inside the sandbox"** and tells the manager to run it sandboxed and expect
> to need the override only when the range crosses a shipped file. A manager reading the first bullet reaches for
> the override every time. Which statement binds, and does the weaker one get replaced under node 189's supersession
> route?

**Blockers, in the worker's words:** *"none. Found outside node 229's fourteen spans and deliberately left, node
229's licence reaching that section's fourteen spans and nothing else."*

## Acceptance condition

*Written by node 229's worker. Pasted as it wrote it, and not the manager's.*

> In `.scratch/graph-workflow/map-manager-only.md`, in the section beginning `## Landing an implementation node's
> work`, the phrase `the reset **requires the sandbox off**, failing inside it with \`Could not reset index file\``
> is replaced so that the section states one rule about when the reset needs the sandbox disabled, and that rule is
> the conditional one: run it sandboxed, and expect to need the override where the range crosses a file under
> `.claude/skills/`. The error string `Could not reset index file` still appears in that section, byte-identical, at
> least once, as does `Read-only file system`. The replaced text is appended verbatim to
> `.scratch/graph-workflow/map-history.md`, inside its existing final section or a new `##` section of its own,
> struck-through text staying struck through; outside what is appended, `map-history.md` is unchanged. No other file
> is modified, the node is not marked or resolved, and no line is written in `decisions.md` or `flags.md` — a change
> to any of those fails this condition. Every markdown link in both edited files resolves to a path that exists,
> except a link to a path outside this repository. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**The manager has been living this contradiction all session and can say which statement the tree supports.** It has
run the reset on five worktrees today. On three it failed sandboxed and needed the override; on one — node 229's —
it **succeeded sandboxed**. So the flat *"requires the sandbox off"* is false as written, and the conditional
statement is the one that matches. **That is evidence for whoever claims this node and not a decision of the
manager's**, which is why the contradiction goes to a node rather than being repaired in passing.

**One thing the evidence does not settle, and the condition does not ask it to.** The conditional statement's stated
trigger is *the range crossing a file under `.claude/skills/`*, and node 229's reset failed sandboxed on a plain
`.scratch/` file with no skills file involved. So the conditional rule's **trigger** may be wrong even though its
shape is right — which is [node 180](180-which-trees-get-the-read-only-skills-overlay.md)'s subject, still open.

**This node and [node 234](234-a-failed-merge-can-leave-the-tree-partially-updated.md) both edit the same section
of the same file** and must not run at once; so does node 160. The manager holds that sequencing and has written no
blocking edge.
