# The worktree route's create command names a relative path and never says from where

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [node 281](281-map-repeats-the-false-no-override-claim-about-the-worktree-route.md)'s worker, and
pasted as it wrote it.*

> The Create bullet of `map-manager-only.md`'s *How the worktree is made* gives `git worktree add -b
> worktree-<NN>-<name> .scratch/graph-workflow/worktrees/<NN>-<name>` and says the manager works *"from the main
> tree"*. **"From the main tree" names the tree, not the working directory** — so a manager whose cwd is
> `.scratch/graph-workflow/` is still in the main tree and gets a **doubled** path. That is what happened for this
> node and for node 267: both worktrees are at
> `.scratch/graph-workflow/.scratch/graph-workflow/worktrees/<NN>-<name>`. **The doubled path escapes
> `.gitignore`** — the rule node 269 landed is anchored at the repo root and does not match it — so `git status` at
> the root shows `?? .scratch/graph-workflow/.scratch/`, measured, and `git check-ignore` returns non-matching. **Two
> entire worktrees are currently sitting untracked-and-unignored in the repository.** Should the bullet state an
> absolute path, or state the directory the command is run from?

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 281's worker. Pasted as it wrote it, and not the manager's.*

> Done when all four hold.
>
> **1.** `map-manager-only.md`'s *How the worktree is made* Create bullet states the worktree path in a form that
> resolves to `<repo root>/.scratch/graph-workflow/worktrees/<NN>-<name>` **whatever working directory the command
> is issued from** — either by giving an absolute path or by naming the working directory the command must be run
> from as part of the command.
>
> **2.** Whatever it now states, `git check-ignore` matches the resulting path against the repository's
> `.gitignore` — that is, **the created worktree is ignored**.
>
> **3.** Any wording the change displaces that states a rule currently binding is **replaced**, not struck in place,
> and its existing text is appended verbatim to `.scratch/graph-workflow/map-history.md` under a heading mirroring
> the section it came from, struck-through text staying struck through; `map-history.md` gains text and loses none.
>
> **4.** No file outside `map-manager-only.md` and `map-history.md` is modified; nothing is written in
> `decisions.md` or `flags.md`; no node's status line is touched. The bar applies: this repository has no build, no
> tests, no formatter and no CI, which is a complete bar on its remaining half, so what binds is the project
> criteria, `CONTEXT.md`'s `_Avoid_` lines, `graph-conventions.md`, `/writing-for-agents`, `/coding-principles`,
> `/naming`, and this effort's ground rules and four standing rules for writing.

## The manager's note at filing

*Not a change to anything above.*

**The manager caused this and it was live in the repository when the worker found it.** Flag `281.2` holds the
manager's half: it ran `git worktree add` with a relative path from a cwd that was not the repository root, then
wrote the non-existent path into the spawn, costing that worker two tool calls before `git worktree list` told it
where it actually was.

**One consequence the worker could not see, measured by the manager after the report.** The manager's periodic
record-state commit is `git add .scratch/graph-workflow`, **and the doubled path is underneath it** — `git add
--dry-run` staged both worktrees. **The manager would have committed two entire working trees into the record.**
That is closed for now by a local-only `.git/info/exclude` entry, which touches no tracked file; **this node is what
stops it recurring.**

**Clause 2 is the load-bearing one and it is testable rather than arguable**: whatever the bullet says, the path it
produces must be one `git check-ignore` matches. A claiming worker should run that command rather than reason about
the anchor.

**The manager's own conduct has changed already** — it creates worktrees with an absolute path — which is the
ordinary order on this effort and is also the thing that makes a node like this feel like ceremony. That tension is
[node 283](283-what-makes-a-change-to-a-record-file-a-node-rather-than-bookkeeping.md)'s subject and is in front of
the human.

## A second author's condition for the same defect

***Filed by the manager, not merged.*** [Node
267](267-the-priority-list-does-not-say-the-human-must-always-have-something-to-do.md)'s worker found this
independently, an hour after node 281's worker, and wrote its own condition. **The manager has not folded the two
together** — that would be authoring a condition out of two agents' text — but this one **adds two demands the
condition above lacks**, and whoever claims this node should have them:

> **1.** … `map.md`'s paragraph beginning *"An implementation node's worktree is made with plain git"* states the
> same path in the same form.
>
> **2.** `.gitignore` ignores the path any worktree created by that route occupies. … Verified by `git check-ignore
> -v` against a path under the route's location, **which must report `.gitignore` and not `.git/info/exclude`.**
>
> **3.** Nothing in the work depends on `.git/info/exclude`, and the work neither reads nor writes that file.
>
> **4.** No existing git worktree is moved, removed or renamed, and no branch is created, deleted or checked out.

**Clause 2's second half is the sharper demand and it is aimed at the manager's own containment.** The local
exclude the manager added closes the hole on this machine only; **it is untracked and does not survive a clone.**
Node 281's worker's condition would be satisfied by a path the local exclude happens to cover; this one would not.

**Clause 4 matters because two live worktrees sit at the doubled path right now**, one of them holding finished work
at a gate. A worker repairing the *rule* must not try to repair the *directories*.

**The scope differs too**: the condition above is two files, this one is three — it adds `.gitignore`. **Whoever
claims this node picks, and says which it took.**

## The manager's note, 2026-09-23

*The manager's own note, not an amendment.* This node's `## Acceptance condition` quotes the words "four standing rules for writing". Since [node 289](289-a-plain-english-and-compaction-pass-over-the-shipped-files.md), `map-implementation-rules.md` holds five standing rules for writing and says "five" where it said "four". Found by the manager's search of the open conditions for "four standing rules". The clause must be re-pointed before this node is claimed.

## Amendment, 2026-09-27 (from node 56)

*Written by [node 56](56-ship-the-glossary-into-the-skill-set.md)'s worker under its `CONDITIONS`, and filed by the manager. Pasted as it wrote it.*

- Node 284 (open, unclaimed): in its bar sentence, "`CONTEXT.md`'s `_Avoid_` lines" should read "`.claude/skills/expedition/glossary.md`'s `_Avoid_` lines". Same source for the path.

## Amendment, 2026-09-28 (from node 354)

*Written by [node 354](354-add-the-sixth-standing-rule-for-writing.md)'s worker under its `CONDITIONS`, and filed by the manager. Pasted as it wrote it. It binds once node 354 lands.*

- Node 284 (open, unclaimed). Clause 4's bar sentence says "this effort's ground rules and four standing rules for writing". The manager's note of 2026-09-23 on that node already records that this is stale. Replacement for that phrase: "this effort's ground rules and six standing rules for writing". It is fixed by the same landed work.

## Flags

`284.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment from node 56 above.* Node 56's replacement naming `.claude/skills/expedition/glossary.md` in place of `CONTEXT.md` was filed on this open, unclaimed node without asking the human first.

`284.2` `ASSUMPTION` — *The manager's own entry, carrying the amendment from node 354 above.* Node 354's replacement of "five" (or "four") with "six" standing rules for writing was filed on this open, unclaimed node without asking the human first.
