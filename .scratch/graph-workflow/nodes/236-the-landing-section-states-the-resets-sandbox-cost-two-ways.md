# The landing section says the reset requires the sandbox off and also that it is not reliably inside it

Type: implementation
Status: claimed

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

## Interview

#### Raise 1, relayed 2026-09-28

*Pasted as the worker handed it back. The worker is stopped until the human answers.*

```
NODE:          The landing section says the reset requires the sandbox off and also that it is not reliably inside it (236)
ABOUT:         Node 236 was meant to replace the flat "the reset requires the sandbox off" statement in `map-manager-only.md`'s landing section with the conditional one, and bank the old text in `map-history.md`. I stopped before editing anything: the phrase the condition tells me to replace is no longer in the file.
SO FAR:        I read the contract, the node file, `map.md`, `map-implementation-rules.md`, the landing section of `map-manager-only.md` (`## Landing an implementation node's work`) in full, and the lines in `decisions.md` about the sandbox, resets and landing. All of these were read in the worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/236-resets` at `26ae202`.
               - **The condition's target is gone.** A search of the worktree for `requires the sandbox off` and `not reliably inside` finds neither phrase in `map-manager-only.md`. Both appear only in `map-history.md`: line ~639, under `### From *How the worktree is made* — the route bullet`, and line ~668, under `### From *How the worktree is made* — the manager needing EnterWorktree for neither the base check nor the reset`. Both headings sit inside `## Superseded from map-manager-only.md at node 268 — the EnterWorktree-then-reset route`.
               - **Who removed them, and why.** `git log -S` shows commit `8933f1d` ("Carry the plain-git worktree route into the map", node 268) took both bullets out of the section. It banked them verbatim in `map-history.md`. Node 265 dropped `EnterWorktree` and the base reset from the route altogether. The route is now `git worktree add`, and the `Base.` bullet says "no base reset is performed".
               - **What the section says about the reset today.** It is mentioned only in the measurement sub-bullets under "One sandbox restriction bites this lifecycle". That bullet already says the reset "and an *entered* worktree — are steps of no route any longer". The sub-bullets contain `Could not reset index file to revision`, the reset succeeding inside the sandbox where the range touches no `.claude/skills/` file, and `Read-only file system`.
               - **So the contradiction no longer exists.** Two of the condition's clauses cannot be carried out. "The phrase … is replaced" has nothing to act on. "The replaced text is appended verbatim to `map-history.md`" is already done, at node 268. The clause "the section states one rule … run it sandboxed, and expect to need the override where the range crosses a file under `.claude/skills/`" could only be met by adding an instruction for a step no route has. That would contradict node 265's route, and node 180 holds the trigger open anyway. The two byte-identical string clauses are already true of the tree without any edit.
               - The manager's note warned that quotes might have moved. This one did not move: it left the section a full cycle before nodes 160 and 230.
               - I made no edits. The worktree is clean.
ASK:           The condition names a phrase node 268 already replaced and banked. May node 236 be discharged as already satisfied by the landed tree, with no edit, the way node 227 was discharged by node 249's landing?
RECOMMENDED:   Discharge with no edit. The contradiction the node asks about ended when node 268 removed both statements and node 265 removed the reset from the route. Banking the old text, which the condition also asks for, is already done under node 268's heading in `map-history.md`. The two error strings the condition wants kept are still in the section. Any edit I could make would add a rule for a step that no longer exists. The open question about what triggers the read-only overlay stays where it is, at node 180.
ALTERNATIVES:  - Rewrite the condition so the measurement sub-bullets carry a "run it sandboxed" instruction. I set this aside because it states a rule for a step no route performs.
               - Close the node as invalidated by node 268 rather than discharged. This is bookkeeping only: the outcome is the same, and only the reason recorded differs.
               - Have me edit the sub-bullets anyway to add "Read-only file system" or remove the reset measurements. I set this aside because the strings are already present, and removing measurements is outside this node's scope.

RETROSPECTIVE
1. What I had to hunt for: whether the quoted phrase still existed, and if not, where it went. A grep plus `git log -S` answered both. Neither the spawn nor the node file said the reset had left the route.
2. What arrived that this node did not need: most of `map.md` and all of `map-implementation-rules.md` beyond its worktree paragraph. The `decisions.md` lines about the sandbox and landing were mostly irrelevant too, except the node 265 and node 268 lines, which were decisive.
3. What would have made this easier: a check at claim time that the condition's quoted phrase still exists in the file it names, which is one grep. Also a note on the node or in the spawn that node 268 banked the `EnterWorktree`-then-reset route. The node was filed at node 229 and outlived its subject.
4. What was stale, wrong or contradictory: the node's acceptance condition and its `## Question` both quote text that node 268 (`8933f1d`) removed. The manager's filing note ("has run the reset on five worktrees today") describes a route that no longer resets. The manager's notes say node 160 and node 230 might have moved quotes; in fact the change came earlier, at node 268.
```
