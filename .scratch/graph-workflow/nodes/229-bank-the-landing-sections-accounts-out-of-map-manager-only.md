# Bank the landing section's accounts out of `map-manager-only.md`

Type: implementation
Status: resolved

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

## Review

### Checker run 1 — `PASS`, with one `NOT COVERED` part

*Pasted in summary by the manager with the checker's own sentences quoted; its full outcome is long and its
load-bearing findings are these. It handed back **no questions**.*

> **PASS.** … I settled first whether the work moved a standard. It did not. … Both changed paths are the effort's
> own record. Per the implementation-rules file's rule for that case, I read them as the work under check and
> derived no statement of intent from their content.

- **Scope:** exactly the two files modified, nothing untracked, nothing staged; `decisions.md`, `flags.md`,
  `map.md`, `map-implementation-rules.md` and every node file unmodified.
- **Banking:** *"`map-history.md` is a **pure append**: the pre-work bytes are a byte-exact prefix of the finished
  file (`after[:len(before)] == before`), 11 548 bytes appended."* One new `##` section, last in the file, heading
  byte-compared equal to the required string.
- **The banked passages:** all 13 match the pre-work section byte-for-byte. Then the converse and stronger test —
  *"I deleted the 13 banked passages from the pre-work section and diffed the residue against the finished section.
  **Exactly one deletion run survived, a lone `,` inside a replace opcode that re-supplies the comma** — so nothing
  was removed from that section that is not banked."*
- **Outside the section:** 5,858 bytes above and 11,683 below, identical on both sides.
- **(a)** 18 `~~` markers before, **0** after.
- **(b)** All thirteen strings present. Twelve contiguous. On `could not detach HEAD` it did **not** accept the
  worker's reading — *"My own contract independently mandates the unwrapped search: 'A line is not a unit of
  meaning… unwrap the text into unbroken lines first and search that.'"* It then tested the worker's factual claim
  and confirmed the string is absent as contiguous bytes in the **pre-work** file too, *"so the raw-byte reading was
  never satisfiable without a rewrap, and a rewrap would itself breach the byte-identity demand. Clause (b) is met;
  there is no tension left to report."*
- **(d)** Established mechanically rather than by eye: *"53 unstruck bolded statements in the pre-work section, of
  which 15 do not survive verbatim — and I took all 15 by hand. Every one is a supersession marker … pure history …
  or content sitting under a **struck** parent whose current form survives."* No requirement changed; the code-slot
  count still reads two.
- **(e)** 299 markdown links across both files, searched unwrapped, **0 unresolved**.
- **(f)** `map-manager-only.md` **34,160 → 28,733**. `map-history.md` **117,473 → 129,021**. The section **16,619 →
  11,192**, a 33% cut.

> **NOT COVERED:** … The fourteen edits were deliberately not reproduced in what I was given, so I cannot verify
> that each change sits inside its own named quoted-phrase span, that the count is fourteen, or that the work's
> numbering of them matches the node's. I established the two halves of this that do not need the enumeration …
> What I could not bound is the *insertions* — eight of them — to the fourteen named spans. … To establish this
> part I would need the fourteen quoted spans as text.
>
> **My `PASS` means the parts above and no more.** The party holding the node's enumerated edits is the only one
> that can settle whether the insertions stayed inside their fourteen spans.

### The `NOT COVERED` part, settled by the manager

*The checker named who could settle it, and it is the manager — the enumerated edits were withheld from the checker
deliberately, to keep a transcription slip of the manager's from becoming a standard the work was held against.*

**What the manager ran.** It diffed the pre-work section against the finished section character by character,
which reported **98 raw changed regions**, then merged regions separated by fewer than 120 unchanged characters,
which gives **13**. Each was read against the condition's fourteen edits:

| region | maps to | shape |
| --- | --- | --- |
| 1 | edit 1 | deletes the struck `git worktree add` clause, 85 bytes |
| 2 | edit 2 | deletes the struck one-slot sentence, 111 bytes |
| 3 | edit 3 | deletes the `**What that supersedes**` paragraph, 378 bytes |
| 4 | edit 4 | 151 bytes → `**The route is the human's own**`, 30 |
| 5 | edit 5 | 463 bytes → the commit-trailer line, 95 |
| 6 | edit 6 | 643 bytes → 354 |
| 7 | edit 7 | 1,247 bytes → 841 |
| 8 | edit 8 | deletes the node-140 sentence, 216 bytes |
| 9 | edit 9 | deletes `, after four failed attempts and two wrong diagnoses`, 52 bytes |
| 10, 11 | **both inside edit 10's span** | 877 → 167 and 375 → 236; the gap-merge split one edit in two |
| 12 | edit 11 | **insert-only**, 116 bytes, the only insertion that adds without removing |
| 13 | **edits 12, 13 and 14 together** | 3,181 bytes → 531; those three spans are adjacent, so the gap-merge joined them |

**The count reconciles exactly: 13 merged regions, 14 edits, one edit split across two regions and three adjacent
edits merged into one.** Every region's removed text begins at a span the condition names, and **no changed region
falls outside the fourteen spans** — which, with the checker's own establishment that nothing outside the section
moved at all, closes the part it could not reach.

**One thing the manager is disclosing rather than burying:** this settlement rests on the manager's own reading of
which region maps to which edit, and the manager is the party that withheld the edits from the checker in the first
place. **A second pair of eyes was available and was not used** — the enumerated edits could have gone to a third
agent that had never seen the work. The manager judged the reconciliation mechanical enough to state; whether that
judgement is right is the human's to weigh at the gate.

### Gate — `approve`

**The human's word, `verbatim`.**

> approve

**What it decided.** `approve` on a `PASS`ing tree lands the work as it stands. **Flag `229.1` is settled** — the
reading of clause (b) that treats *byte-identical* as forbidding rewording rather than demanding one physical line,
which the checker reached independently and by a different route.

**What the payload disclosed, and which the approval therefore covers.** That the `NOT COVERED` part was settled
**by the manager alone**, on its own mapping of thirteen diff regions to fourteen edits, and that the manager is the
party that withheld the enumerated edits from the checker in the first place. The payload said in as many words that
a third agent could have been given the spans and was not, and that the judgement was the human's to weigh.

## Flags

*The worker's own text, pasted. **Settled by the approval.***

`229.1` **· settled** `ASSUMPTION` — Clause (b) demands thirteen strings appear "byte-identical" in the finished
section. One of them, `could not detach HEAD`, does not appear as contiguous bytes and did not before this work
began — the file wraps it as `` `could not\n  detach HEAD` `` — and it cannot be made contiguous, because it sits
inside the one bullet the condition says nothing else in changes, and outside the fourteen spans, where
byte-identity is demanded. I read "byte-identical" as the condition's own quotations read it, *not reworded*, with a
markdown soft line break immaterial; on the raw-byte reading the clause would already have been false of an unedited
file. Four independent demonstrations back that reading: the condition's quoted end markers for edits 7, 8 and 13
all fail to match the file's bytes and all fail only by line wrapping, as does clause (c)'s own quoted sentence.
Where the wrapping was mine, I honoured the stricter reading anyway and kept `grep " <repo>" /proc/mounts` and the
`unable to unlink old …: Read-only file system` string each contiguous on one line.

*The manager's note: **the checker refused to take this on the worker's word and got there by its own route**, its
contract independently mandating an unwrapped search. It then tested the worker's factual claim and confirmed the
string was already non-contiguous before any work started. Two parties, two routes, one conclusion.*

## Answer

*Pasted as the worker wrote it, in its own words.*

The fourteen edits landed in `map-manager-only.md`'s `## Landing an implementation node's work`, and every passage
they removed is banked verbatim in `map-history.md` under one new final `##` section.

**Every span was located mechanically, never by eye.** A Python pass read the pre-work bytes, located each span by
its quoted start and end markers as exact byte strings, asserted each marker occurred **exactly once inside the
section**, asserted the fourteen spans did not overlap, and rebuilt the file by copying the untouched runs verbatim
and substituting only inside the spans. **Byte-identity outside the fourteen spans is therefore a property of the
construction rather than something checked afterwards.**

**Three of the condition's quoted markers do not match the file byte-for-byte, and all three differ only in line
wrapping** — the condition quotes this file with markdown soft line breaks normalised to spaces. Each was located by
the file's own bytes instead, and each is still unique inside the section.

**What the section lost is history and what it kept is every trigger.** Gone: how many attempts a measurement took,
which earlier account was wrong, the node-140 illustration, and nine struck regions of which seven existed nowhere
else. Kept: every error string, every verbatim human quotation, and the condition under which each rule fires. **No
rule that binds changed in what it requires.**

**Byte counts.** `map-manager-only.md` 34,160 → 28,733. The section 16,619 → 11,192. `map-history.md` 117,473 →
129,021, the whole growth being the appended section, its prefix byte-identical.

**What the worker reported its work invalidates:** `none`. *Its words:* *"Node 191's rule — that no sweep of a map
file is owed or licensed — is unchanged and is restated as unchanged in the banked section's own lead-in; this work
is the single bounded exception the human licensed at node 225, over one section of one file."*

## Retrospective

*Filed by the manager in the same edit that resolves the node. Pasted as the worker wrote it.*

**1. What I had to hunt for.** Three of the condition's quoted span markers, because they do not exist in the file
as quoted — the whitespace differs. **The gap is that nothing told me the condition's quotations are
whitespace-normalised**, and I had to infer it from three failures. The other hunt was the effort name for the
commit trailer, which I got from `git log | grep 'Node:'`. **Neither my spawn nor my node file nor the map states
it, and every implementation node needs it for exactly one line.**

**2. What arrived that this node did not need.** `map.md` is a mandatory read and is ~50 KB; of it, **one** line
bore on this node. Where I went to a file for one fact and took the whole file: `map-history.md`, 117 KB, opened to
learn the house format of a banked section — I windowed it and paid little, **but only because I guessed to window
it.** The arrangement that would have avoided the `map.md` cost is a heading: this effort's own
`map-implementation-rules.md` opens by saying `map.md` holds only what *every* worker can act on, **and that claim
is not true for a worker whose product is a map file.**

**3. What would have made this node easier.** In the **node file**: one sentence saying the condition's quotations
are normalised to single spaces and that the file's own line wrapping is the authority. **Three of the fourteen
spans and one property clause turn on that, and the node's own worker plainly knew it.** In the **spawn**: the
effort name. **The single largest thing that made this node easy was the condition quoting its spans instead of
describing them**, which made a mechanical `assert count == 1` possible; a condition that had said "the struck
sentence about the manager creating the worktree" would have put the transcription risk back.

**4. What I read that was stale, wrong, or contradicted something else.** (i) The node's `## Question` states the
section at **16,569 bytes**; it measures **16,619**. (ii) `map-implementation-rules.md`'s opening says `map.md` is
read *"whole, cold, once per node by every worker, so it holds only what every worker can act on"* — for this node
one line of it qualified. (iii) The two live contradictions I found inside the section and left, both reported as
new nodes: the reset's sandbox cost stated two ways, and the worktree path stated two ways.
