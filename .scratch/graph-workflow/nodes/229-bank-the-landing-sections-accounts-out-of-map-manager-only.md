# Bank the landing section's accounts out of `map-manager-only.md`

Type: implementation
Status: claimed

Blocked by: none

## Question

*Specified by [node 225](225-whether-map-manager-only-gets-an-admission-test.md)'s worker after the human licensed
it, and pasted as that worker wrote it.*

> The human licensed one bounded exception to [node
> 191](191-the-rules-file-carries-accounts-rather-than-rules.md)'s rule that no sweep of a map file is owed or
> licensed: node 189's supersession route runs once over `## Landing an implementation node's work` in
> `map-manager-only.md`, and over nothing else. Node 191's rule is unchanged everywhere else, and this node widens
> it to no other section, no other file and no sibling. The ground is that node 191's refusal rested on *"the six
> nodes queued on this file are how the file converges"*, which was measured false for this section: the passages
> carrying the largest accounts are touched by no open node. The section is 16,569 bytes, 49% of the file, and holds
> 9 struck-through regions of which 7 exist nowhere else.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 225's worker. Pasted as it wrote it, and not the manager's.*

> **Scope.** The work is two files and no others: `.scratch/graph-workflow/map-manager-only.md` and
> `.scratch/graph-workflow/map-history.md`. Editing `map-history.md` is required, not merely permitted — the
> supersession route is an append to it, and a scope that excluded it would make this condition unsatisfiable. No
> other file may be modified. The worker may not mark this node, resolve it, or write a line in `decisions.md` or
> `flags.md`; a change to any of those is a failure of this condition.
>
> **Where the removed text goes.** `map-history.md` gains exactly one new `##` section, appended as its final
> section, whose heading is exactly:
>
> `## Superseded from \`map-manager-only.md\` — the landing section's accounts`
>
> Every passage removed from `map-manager-only.md` by edits 1 to 14 below is reproduced inside that section
> **byte-identical to the text it had before this work started**, struck-through text staying struck through.
> Nothing else in `map-history.md` is changed: outside the appended section the file is byte-identical to its
> pre-work state.
>
> **What is edited.** Exactly the fourteen edits below, in `map-manager-only.md`'s section beginning with the
> heading `## Landing an implementation node's work` and ending immediately before the heading `## Not yet
> specified`. Each names its span by quoted phrase. Outside these fourteen spans, `map-manager-only.md` is
> byte-identical to its pre-work state — the whole of the file above and below that section included.
>
> 1. In the paragraph beginning `**Landing policy**`, delete `~~the manager creates for that node with \`git
>    worktree add\` off the current \`HEAD\`~~ `, including the single trailing space, so the sentence reads `...
>    works in a **git worktree** **created by the harness rather than by hand — see the standing instruction
>    immediately below**, on a branch ...`. The phrase `see the standing instruction immediately below` survives
>    unchanged; open node 152's condition quotes it.
> 2. Delete the leading `~~**How many implementation workers run at once is a setting of the effort, and for this
>    effort it is one.**~~ `, including the single trailing space. Everything after it in that paragraph stands, the
>    sentence `The superseded sentence is also in [map-history.md](map-history.md).` included.
> 3. Delete the whole paragraph beginning `**What that supersedes**: this map used to say` and ending `The sentence
>    in full is in [map-history.md](map-history.md).`, together with one adjoining blank line.
> 4. Replace the span beginning `~~**The manager creates nothing.**` and ending `**Superseded by the human's own
>    route**` — that is, the struck sentence and the four words immediately following it — with exactly `**The route
>    is the human's own**`. The rest of that bullet, the human's two `verbatim` quotations included, is unchanged.
> 5. Replace the whole bullet beginning `- ~~The` and ending `the commit trailer stays the join key regardless.`
>    with exactly this one line:
>
>    `- **The commit trailer \`Node: <effort>/<NN>\` is the join key, and it is the manager's to write.**`
>
> 6. Replace the span beginning `— ~~**which is the typical case` and ending `worktree lands on \`HEAD\` and no
>    reset happens at all.` with exactly:
>
>    `the worktree lands on \`HEAD\` and no reset happens at all. **That third case does not occur on this
>    machine**: the setting is absent, so the default \`fresh\` applies, every harness worktree lands on
>    \`origin/master\`, the base is always stale, and the reset always runs — measured at [node
>    175](nodes/175-what-the-worktree-cycle-does-to-the-sandbox.md).`
>
>    The sentence beginning `**The base check still runs in every case**` that follows it is unchanged.
> 7. Replace the whole bullet beginning `- **The manager needs \`EnterWorktree\` for neither the base check nor the
>    reset**` and ending `is [node 152](nodes/152-where-the-harness-worktree-instruction-lives.md)'s.` with exactly:
>
>    `- **The manager needs \`EnterWorktree\` for neither the base check nor the reset.** \`cat
>    .git/worktrees/<name>/CLAUDE_BASE\` and \`git -C <worktree> rev-parse HEAD\` both answer the base check
>    read-only from the main tree, and \`git -C <worktree> reset --hard <ref>\` runs there too — so **the manager's
>    own session never has to leave the main tree**. **The reset is not reliably inside the sandbox**: on one
>    worktree it succeeded across a \`.claude/skills\` file, and on another the same command failed with \`unable to
>    unlink old '.claude/skills/expedition-grilling/SKILL.md': Read-only file system\` and needed the sandbox off.
>    Run it sandboxed, and expect to need the override when the range crosses a shipped file. What triggers the
>    overlay on one tree and not another is [node
>    180](nodes/180-which-trees-get-the-read-only-skills-overlay.md). Where the instruction to use \`EnterWorktree\`
>    now stands is [node 152](nodes/152-where-the-harness-worktree-instruction-lives.md)'s.`
>
> 8. In the bullet beginning `- **The manager verifies the base at every spawn.**`, delete the final sentence `
>    Node 140 was moving text verbatim between files, so a late reset there would have silently reverted [node
>    147](nodes/147-graph-records-name-absolute-paths-on-a-machine.md)'s landed work with every check passing.`, so
>    the bullet ends `...for every file the worker has not touched.`
> 9. In the bullet beginning `- **A failed rebase leaves its partial checkout behind`, replace `Measured at node
>    143, after four failed attempts and two wrong diagnoses.` with `Measured at node 143.` Nothing else in that
>    bullet changes: `could not detach HEAD`, `git checkout --detach`, and the one-pass repair instruction all stay.
> 10. Replace the span beginning `- **One sandbox restriction bites this lifecycle, and it took three rounds of
>     experiment to state correctly.**` and ending `and not about harness-created worktrees being treated
>     differently from hand-made ones.` with exactly:
>
>     `- **One sandbox restriction bites this lifecycle.** The operative rule, measured: the sandbox is a set of
>     bind mounts **recomputed for every command**, and a command succeeds only where every path it writes lies
>     inside a \`rw\` mount and outside a \`ro\` one. **The manager reads its own region with** \`grep " <repo>"
>     /proc/mounts | awk '{split($4,a,","); print a[1]" "$2}' | sort -u\` — read-only, one call. Whether it is told
>     to, and when, is [node 179](nodes/179-the-manager-sees-its-own-writable-region.md); what triggers the overlay
>     on one tree and not another is [node 180](nodes/180-which-trees-get-the-read-only-skills-overlay.md).`
>
> 11. In the sub-bullet beginning `  - **What it hits.**`, append after `both succeed outside the sandbox.` the
>     sentence ` **The manager must expect this rather than discover it**, most of the open frontier touching
>     \`.claude/skills/\`.` Nothing else in that sub-bullet changes, and the sub-bullet beginning `  - **What it
>     does not hit` is untouched.
> 12. Replace the whole sub-bullet beginning `  - ~~**The one asymmetry` and ending `is not reliably true.` with
>     exactly:
>
>     `  - **What decides is whether the target path is inside the writing session's writable region**, not which
>     tree the command is issued from. From a session whose region did *not* contain the worktree path, \`git -C
>     <harness worktree> reset --hard\` failed on plain \`.scratch/\` files with \`Read-only file system\`, no
>     skills file involved; from a session whose region *did* contain it, the same command succeeded across a
>     \`.claude/skills\` file. Harness worktrees do sometimes carry their own \`<wt>/.claude/skills\` \`ro\` mount.`
>
> 13. Delete the whole bullet beginning `- ~~**Two distinct sandbox restrictions bite this lifecycle` and ending `as
>     does a plain write to that worktree's own \`.claude/skills/\`.` — the struck header and both of its
>     sub-bullets.
> 14. Delete the whole bullet beginning `- ~~**The merge step needs the sandbox off where the node touched a shipped
>     file.**~~` and ending `since most of the open frontier touches \`.claude/skills/\`.`
>
> **What must be true of the finished tree.**
>
> a. The section from `## Landing an implementation node's work` to the heading after it contains **zero**
>    occurrences of `~~`. All nine struck regions are gone.
> b. Every one of these strings still appears, byte-identical, somewhere in that section: `could not detach HEAD`;
>    `git checkout --detach`; `Could not reset index file`; `unable to unlink old`; `Read-only file system`; `grep "
>    <repo>" /proc/mounts`; `For the worktree, I think it might be needed as otherwise it is too anoying for the
>    review`; `what are the changes ? I don't see them in git ?`; `should we do 2 implementer and 2 grilling to go
>    through the shipping backlog ?`; `It calls EnterWorktree specifying a name tied to the node`; `see the standing
>    instruction immediately below`; `Node: <effort>/<NN>`; `Nothing is ever pushed.`
> c. The sentence beginning `Added beside the landing policy above rather than rewritten into it` is unchanged and
>    still present.
> d. No rule that currently binds is changed in what it requires. The landing lifecycle — worktree, uncommitted
>    through the gate, path-limited commit, rebase, bar re-run, `--ff-only` merge, nothing pushed, correction round
>    on conflict — reads the same as before, and the code-slot count still reads two.
> e. Every markdown link in both edited files resolves to a path that exists, except a link to a path outside this
>    repository, which is out of scope.
> f. `map-manager-only.md` is smaller than it was and `map-history.md` is larger; report both before-and-after byte
>    counts and the section's before-and-after byte count.
> g. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This node exists because the human licensed it, and the licence is bounded by its own terms.** Their words,
`verbatim`, at node 225: *"Q1 ok Q2 ok"*, taking the recommendation quoted on that node. **Node 191's rule is not
changed and this node does not widen it** — no other section, no other file, no sibling.

**The manager has added a fifteenth thing to no part of this condition**, and one measured fact arrived after it was
written that a later node may want: at node 198's landing, a sandboxed `git merge --ff-only` left the main tree
**partially updated** before failing, which the section's own text does not say it does. That is recorded on [node
216](216-what-a-correction-round-after-a-rebase-conflict-owes.md) rather than added here, because this condition
turns on byte-identity outside its fourteen spans and the manager will not perturb the file it is about to be held
against.

**The manager edits `map-manager-only.md` for nothing while this node is open**, that being the same collision that
produced the rebase conflict at node 200.
