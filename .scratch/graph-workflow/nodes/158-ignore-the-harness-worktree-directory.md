# Ignore the harness's worktree directory

Type: implementation
Status: resolved

Blocked by: none

## Question

*Surfaced by [Which harness route creates an implementation node's
worktree](150-which-harness-route-creates-a-worktree.md)'s worker, and pasted as it wrote it.*

> The repository's `.gitignore` ignores `.worktrees/`, the path the landing policy used when the manager created
> worktrees by hand. The harness creates them at `.claude/worktrees/` instead, which no rule covers, so a live
> worktree appears as untracked in the main tree's `git status`, is traversed by repo-wide searches, and has been
> observed duplicating this workflow's own skill files into the manager's context.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 150's worker. Pasted as it wrote it, and not the manager's.*

> After the work, the file `.gitignore` at the repository root contains an entry that causes git to ignore the
> directory `.claude/worktrees/`, immediately preceded by a comment stating that this directory holds the git
> worktrees the agent harness creates for implementation workers, and that it is ignored so those worktrees are never
> committed. The file's existing entry ignoring `.worktrees/` is still present, and the existing comment lines above
> it are still present and unaltered. Running `git status --porcelain` from the repository root produces no line
> whose path begins with `.claude/worktrees`. No file other than `.gitignore` is changed anywhere in the repository.
> The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**The pollution is confirmed in the manager's own context**, not only in `git status`: the harness surfaced all seven
`expedition*` skills a second time, scoped to `.claude/worktrees/agent-ac549d7fb8ff2bf22/`, in the manager's skill
list. Every agent spawned while a worktree is live pays for that.

**The manager did not make this one-line change itself**, though it could have and was tempted to. Having already
acted once today on its own authority in breach of its contract — flag `140.8` — it minted the node instead.

**Flag `68.2` bears on it and stays open**: it recorded that an ignore rule could not be assumed for a repository the
workflow does not own. This node's condition is scoped to this repository only and asserts nothing about any other.

## Answer

*The worker's own text, pasted.*

`.gitignore` at the repository root gains a second entry, `.claude/worktrees/`, below the existing `.worktrees/`
entry and separated from it by a blank line, under a four-line comment. The existing three comment lines and
`.worktrees/` are byte-unaltered; the diff is purely additive.

The new entry sits at `.gitignore:10`, and `git check-ignore -v` confirms it matches every shape the harness
produces: `.claude/worktrees/`, `.claude/worktrees/agent-ac549d7fb8ff2bf22` (the agent-id form node 150 first
recorded), and a file nested inside a node-named worktree. `.worktrees/12-x` still resolves to `.gitignore:4`, so the
older entry keeps working. `.claude/skills/expedition/SKILL.md` is confirmed **not** ignored — the pattern is
anchored by its embedded slash and reaches nothing outside `.claude/worktrees/`. Nothing under `.claude/worktrees` is
tracked, so no already-tracked file is orphaned by the rule.

**Two calls a later reader would otherwise re-derive.** *The new block goes below the existing one, and `.worktrees/`
is not marked superseded* — marking it was not available, the acceptance condition requiring the existing comment
lines to be *"still present and unaltered"* and a strike-through altering them; the relationship is carried in the
new comment's third line instead. *Where the condition's `git status --porcelain` clause is satisfied, and where it
is not yet* — in the worktree it returns exactly ` M .gitignore`; in the main tree it returned `?? .claude/worktrees/`
until this landed, because that checkout still held the old `.gitignore`.

**Its first reported facts, which the spawn asked for because the manager was verifying a mechanism it could not
observe:** working directory `/home/ten/Projects/expedition/.claude/worktrees/158-ignore-harness-worktrees`, and
`HEAD` `6795ca9` — both matching the spawn. **So a worker spawned while the manager is inside a worktree inherits
it**, which was the last unmeasured step of the worktree route.

***The manager's note.*** **Landed as commit `305d372`**, and the effect is visible rather than argued: `git status
--porcelain -uall` in the main tree returned `?? .claude/worktrees/158-ignore-harness-worktrees/` before the merge
and returns nothing after it.

**Removing the worktree afterwards failed inside the sandbox with `Device or resource busy`**, and succeeded on a
prune outside it. **This contradicts [node 150](150-which-harness-route-creates-a-worktree.md)'s measurement 8**,
which recorded the `EBUSY` failure as no longer reproducing. The cause is now established rather than guessed: the
sandbox bind-mounts the worktree's admin directory `.git/worktrees/<name>`, and a mountpoint cannot be removed. Those
mounts exist only inside the sandbox's own namespace — `/proc/mounts` shows them from inside and not from outside —
which is why a probe run in a different context did not see them.


## Flags

*Each entry is the worker's own prose, pasted. The manager added the id and the marker and nothing else.*

`158.1` **· settled** `ASSUMPTION` — **The comment says more than the condition demands.** The condition demands the comment state
two things: that the directory holds the harness's worktrees for implementation workers, and that it is ignored so
they are never committed. Both are stated in the first two lines. I added two more — that `.worktrees/` above is the
path the landing policy used when the manager made worktrees by hand, and a pointer to
`map-implementation-rules.md`'s "How the worktree is made". My ground: a reader meeting two near-identical worktree
entries with no stated relationship has to go and derive which is live, and that derivation is what the third line
spends four words preventing. The condition does not forbid extra content and nothing added contradicts it, but the
choice was mine.

`158.2` **· settled** `ASSUMPTION` — **The stale pointer frozen by my own condition was surfaced as a node rather than raised.**
The existing comment I am required to leave unaltered ends "See `.scratch/graph-workflow/map.md`, the landing
policy", and the landing policy moved out of `map.md` to `map-implementation-rules.md` at node 140. That pointer is
therefore stale, and my condition forbids me to fix it. This is arguably raise trigger 1 — a broken thing that is not
mine to change. I decided against a raise on two grounds: the pointer still *resolves*, since `map.md` carries an
explicit forwarding line naming `map-implementation-rules.md` and the landing policy among its contents, so it costs
a reader one extra hop rather than failing; and a raise would spend the human's single live question on a one-hop
pointer when the node route carries it for nothing. Reported under NODES SURFACED instead. If the human would rather
I had raised, this is the judgement to revisit.

## The manager's note after the handover

*Not a change to anything above.*

**This node verified the one step of the worktree route that was still unmeasured.** Its first reported facts were
its own `pwd` — the worktree the spawn named — and its `HEAD`, `6795ca9`, the manager's `HEAD` at spawn. **So a
worker spawned while the manager is inside a worktree does inherit it.** Flag `150.3` is unchanged, its subject being
the other direction — pointing a *replacement* at a surviving worktree when resume is unavailable.

**Its invalidation is against the map and is the manager's to carry.** `map-implementation-rules.md`'s bar paragraph
says *"the one ignore file, `.gitignore`, ignores `.worktrees/` and invokes nothing"*, which this work makes
incomplete in the same way node 114's check once found it. **The load-bearing half — *and invokes nothing* — still
holds**, so the bar itself does not move. The manager has not amended the sentence while this node is claimed and its
own condition forbids it to touch that file; the amendment is made when this node lands.

**Its retrospective found a live contradiction the manager confirms**: `map.md`'s ground rule 5 still locates the
prose standard by plugin name, while `decisions.md` records [node
132](132-does-the-plugin-direction-reach-the-efforts-own-bar.md) as having settled that it states its demands in the
rules file instead. The repair is [node 149](149-state-the-prose-standards-demands-in-the-rules-file.md), which is
blocked on node 144 and has not landed. **Nothing in either file says a settled decision is not yet carried out**,
and the worker's point stands: a worker cannot tell a not-yet-landed decision from a broken one.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted. It was spawned by the manager, not by the worker, and was given the acceptance
condition as extracted text.*

**Standards found and used** — *"given to me, not discovered — I did not go looking for a reviewing skill, and
invoked none, so no part of one ran and nothing was delegated to an agent"*: `/coding-principles`, `/naming`,
`CONTEXT.md`'s `_Avoid_` lines, `graph-conventions.md`, and `/writing-for-agents`. **None of them is a path the work
touched, so no standard moved under the check.**

**The entry.** `.gitignore` line 10 is `.claude/worktrees/`. `git check-ignore -v` returns that rule for the
directory and for content beneath it, and **the rule's source is the file under judgement**, not `.git/info/exclude`
or a global.

**The comment.** Lines 6–9, contiguous with the entry, no blank line between. Both demanded statements present. *"The
two further lines in the block … are additional content the condition does not forbid."*

**The freeze on existing text, established byte-wise rather than by eye:** *"the `HEAD:.gitignore` blob is an exact
prefix of the working file (`new.startswith(old)` is `True`), and the added tail is exactly the five new lines. `git
diff` is a pure-addition hunk with no `-` line."*

**The `git status` clause, and the reading it did not pick silently.** Judged against the tree the work is in, and
**agreed with rather than merely accepted**: *"the work is uncommitted, so the main checkout necessarily still
carries the old `.gitignore`, and the clause is not establishable there until the work lands."* It then stated the
other reading in full and **corroborated the rule against a real directory read-only**, running the main checkout's
status with the new file supplied as an extra exclude: no `.claude/worktrees` line. *"So the entry does suppress the
real directory, and the main tree's line goes away when the work lands."*

**Scope, established from the tree rather than from the worker's word:** `HEAD` is `6795ca9…` as stated,
`git status --porcelain -uall` is ` M .gitignore` alone, `git diff --stat HEAD` is `1 file changed, 6 insertions(+)`,
`git diff --cached` is empty.

**The bar: holds**, non-command half in full. `CONTEXT.md`'s `_Avoid_` lines were *"checked by hand rather than by
grep, the map's own measured trap being that about a third of the refused words are ordinary English."* Standing rule
4 was the live one and passes: the citation is a quoted phrase, *"How the worktree is made"*, which resolves in
`map-implementation-rules.md`. The never-delete constraint holds — six added lines, no removed line.

***The manager's note.*** **The run covered the whole condition and named no part it could not reach**, so this entry
carries no `NOT COVERED:` label.

### Gate — `approve`

**The human's word**, `verbatim`:

> approve 158

The payload carried checker run 1's `PASS`, both of this node's flags, the one path touched, the worktree and the
command showing its diff, and the proposed commit message. **Approving the gate settles both flags.** No correction
round was taken.
