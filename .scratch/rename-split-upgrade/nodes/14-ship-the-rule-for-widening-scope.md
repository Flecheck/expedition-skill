# Ship the rule for widening an implementation node's scope

Type: implementation
Status: resolved
Blocked by: ~~11~~

## Question

This lets an implementation node's worker fix what its own work makes wrong, or what the work needs, outside its condition's list of files, so that a node does not land leaving files stale and does not stop for every needed refactor. It also lets a worker pause its node behind a node for an enabling change too big to make inside it. The shipped files today say that a place outside a condition's list is reported and never edited.

*Manager's note:* minted by the worker of [node 09](09-an-implementation-node-may-widen-its-own-scope.md) on its `NEW NODES` part, with the question and condition below as it wrote them. It gave the blockers as "11 (it edits `.claude/skills/expedition/SKILL.md`, the glossary and the standing-yes skill while claimed; ordering avoids a conflict). Node 12 also edits `.claude/skills/expedition/SKILL.md`, in `### Changing one after it is written`, which this work does not need to touch, so the manager may order the two."

## Acceptance condition

Scope: for clauses 1, 2, 3, 5 and 6 the named places are the work, and their scope came from no search. Clause 4's places came from this search, run from the repository root over the working tree on 2026-10-12 at commit `a40f9008e8`: `grep -rn -i "reported and not\|reported, not edited\|permission to edit\|residual clause" .claude/skills .claude/rules`. It returned seven lines (count for scale only, not authoritative; node 11 may have changed these files since): `expedition-prototype/SKILL.md`, `expedition-precondition/SKILL.md`, `expedition-grilling/SKILL.md` and `expedition-implementation/SKILL.md`, each with the bullet "Write into the condition that an instance the search reaches outside the list is reported and not edited"; two lines of `expedition/graph-conventions.md` in the paragraph beginning "An instance the search reaches outside the condition's list"; and `expedition-checker/SKILL.md` in `### The search a condition records`. Re-run the search before starting. The files this work may change are those named in this condition: `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-checker/SKILL.md`, `.claude/skills/expedition/graph-conventions.md`, `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/glossary.md`, and `.claude/rules/expedition-triggers.md` only as clause 7 allows. An instance the search finds outside these files is reported and not edited.

In the clauses below, "the three grounds" means the following.
- (i) The node's own change makes the place wrong. Examples are a stale count, a pointer to something the work moved, a statement the work now contradicts, and, in code, a caller of a function or type whose signature the work changed, or a test, document or configuration file describing what changed. This ground has no size limit.
- (ii) The place is a further instance of the defect the condition describes.
- (iii) The change is an enabling change: the work cannot meet its condition or the bar without it.
On every ground, the edit writes no requirement that is not already fixed by a resolved node, the shipped files, the condition or the work's own change. A repair that needs a judgement nobody has made is a raise.

1. `.claude/skills/expedition-implementation/SKILL.md` says each of the following:
   - The worker may edit a place outside its condition's list of files, on its own authority and without a raise, on exactly the three grounds, each stated with its examples and its test.
   - For each place it edits on those grounds, the worker hands back one `ASSUMPTION` flag naming the place, the reason and the ground, and lists the place in `GATE PAYLOAD` among the paths it touched.
   - The condition's text is not changed by such an edit.
   - A defect the work comes across that none of the three grounds covers is reported on `NEW NODES` as a new node of whatever kind fits, a grilling node where deciding the fix needs the human. The existing rule for joining a defect to an open node of the same file and concern still applies.
   - An edit beyond the condition's clauses inside a file the condition lists is still allowed and flagged.
2. `.claude/skills/expedition-implementation/SKILL.md` also says that where an enabling change is too big to make inside the node, the worker raises under trigger 1 (the size of its own node). The worker judges whether it is too big. The raise proposes a node for the enabling change, with its name, its question and its acceptance condition. Among the human's answers to a raise, the file names a pause: the worker leaves its work as it is and waits, and once the enabling node has landed it is resumed with "continue" on a worktree that holds both the landed enabling change and its own work. Where bringing its work onto that commit conflicts, the worker fixes the conflicted files in place and runs no git command.
3. `.claude/skills/expedition-checker/SKILL.md` states the three grounds and says each of the following:
   - A place the work made wrong is a finding wherever it lies, inside or outside the condition's list.
   - An edit outside the list is not a `FAIL` where a flag the checker received names that place and gives a reason on one of the three grounds, and the reason holds. The checker establishes whether the reason holds from the work. For ground (iii) it asks whether the work would meet its condition or the bar without the edit.
   - An edit outside the list with no such flag, or whose reason does not hold, is a `FAIL` on the acceptance condition.
   - The bullet in `### The search a condition records` that says the condition's residual clause routes an instance outside its list to being reported and not edited agrees with this.
4. Each place clause 4's search finds now says that an instance outside a condition's list is edited only on the three grounds, with a flag naming the place and the reason, and that any other instance is reported and not edited. In `.claude/skills/expedition/graph-conventions.md`, the paragraph beginning "An instance the search reaches outside the condition's list" no longer says the worker never has a permission to edit.
5. `.claude/skills/expedition/SKILL.md` says what the manager does when the human answers a worker's raise with a pause:
   - The manager mints the enabling node from the raise, marked as proposed by that worker, and adds it to the paused node's `Blocked by:`.
   - The paused node stays `claimed` and keeps its worktree, with its work left in place.
   - While the paused node is blocked, its worktree does not count against the effort's code slots.
   - When the enabling node lands, the manager brings the paused node's worktree onto the commit where the enabling node landed, keeping the paused work. A conflict goes to the paused worker to fix in place.
   - The manager then resumes the paused worker with "continue". Where the worker cannot be resumed, a replacement attempt takes the node under the existing rules for an agent that died or was stopped.
6. `.claude/skills/expedition/glossary.md`'s entry **Code slot** agrees with clause 5: a paused, blocked node's worktree does not count against the code slots.
7. `.claude/rules/expedition-triggers.md` is unchanged, unless the work changes, in `.claude/skills/expedition/SKILL.md`, the governing statement of a trigger duty or of the priority. In that case the trigger file is changed in the same way.
8. No statement left in the files this condition names contradicts clauses 1 to 6. No heading is renamed unless every citation of it under `.claude/skills/` is updated in the same change.

*Manager's note, before the claim:* re-ran the recorded search at `cf5984eadc`; it returned 7 lines in the same files as recorded, so the scope has not grown. Node 11 resolved, so the blocker is struck. Nothing else is written after the condition.

## Answer

The rule from node 09 is now in the shipped files. The work is uncommitted in worktree /home/mathieu/projects/graph-agent/.scratch/rename-split-upgrade/worktrees/14-widening-scope, on branch `worktree-14-widening-scope`, cut from `cf5984eadc`.

- `.claude/skills/expedition-implementation/SKILL.md`
  - New section `## A place outside your condition's list`. It states the three grounds, each with its examples and its test, and says ground 1 has no size limit. It says the edit writes no requirement that is not already fixed by a resolved node, the shipped files, the condition or the work's own change. A repair that needs a judgement nobody has made is a raise.
  - Each such place gets one `ASSUMPTION` flag naming the place, the reason and the ground. The flag's index sentence must carry all three, because that sentence is all of the flag the checker receives. The place is also listed in `GATE PAYLOAD`.
  - The condition's text is unchanged by such an edit, and the edit is allowed even where an older condition says "reported and not edited". An edit beyond the clauses inside a listed file is still allowed and flagged.
  - A defect none of the grounds covers goes on `NEW NODES`, as a grilling node where deciding the fix needs the human. The related-defect join rule still applies.
  - An enabling change too big for the node is a raise under trigger 1 (the size of its own node). The worker judges what is too big. The raise proposes the enabling node's name, question and acceptance condition.
  - `### The raise` now lists three answers: Continue, Stop and Pause. On a pause, the worker leaves its work and waits. Once the enabling node lands, it is resumed with "continue" on a worktree holding both changes. A conflict comes to it first, as conflicted files to fix in place with no git command. A `STANDING YES` on a raise whose `RECOMMENDED` was the pause is read as the pause.
  - The opening sentence on holding a code slot now names the pause exception.
  - The fifth point of `## When a node you report is an implementation node` was rewritten to the new residual clause.
- `.claude/skills/expedition-checker/SKILL.md`
  - New section `### An edit outside the condition's list` under `## How you check`. It states the three grounds. A place the work made wrong is a finding wherever it lies. An outside edit is not a `FAIL` where a given flag names the place with a reason on one of the grounds and the reason holds, judged from the work. For ground 3 the checker asks whether the work would meet its condition or the bar without the edit. With no such flag, or a reason that does not hold, the edit is a `FAIL` on the acceptance condition. This holds even against an older condition's "reported and not edited".
  - `### The search a condition records`: the residual-clause bullet and the sentence after it now agree with the new section.
  - `### The flags, after your outcome`: one exception added. A flag naming an outside place is read, and its reason judged, before the outcome.
- Grilling, precondition and prototype contracts: the condition-writing bullet now says an outside instance is edited only on the three grounds (restated, since those workers do not read the implementation contract), with a flag naming the place and the reason. Any other instance is reported and not edited.
- `.claude/skills/expedition/graph-conventions.md`
  - The paragraph beginning "An instance the search reaches outside the condition's list" says the same, and no longer mentions a permission to edit. It points to the implementation contract for the grounds in full.
  - "the clause that excludes every other file" became "the clause that limits edits to every other file".
- `.claude/skills/expedition/SKILL.md`
  - New section `## A paused implementation node`, before `## Deliverables`. Its steps: mint the enabling node from the raise, marked as proposed by that worker, filing the worker's condition. Where the paused node names a deliverable, its `Deliverable:` field follows `### A deliverable whose base is another deliverable`. Add the enabling node to `Blocked by:`. The node stays `claimed` with its worktree and work. While blocked, the worktree counts against no code slot; a paused node reads as `claimed` with an unresolved `Blocked by:` node. On landing, bring the worktree onto the landing commit, keeping the work, and send any conflict to the paused worker. Then resume with "continue", or replace the attempt under `## When an agent dies or is stopped`.
  - `### Picking the next node`: the code-slot bullet says a paused node holds no slot while blocked. The `frontier.sh` paragraph says the script counts a paused node as claimed, so the manager subtracts it.
- `.claude/skills/expedition/glossary.md`
  - **Code slot**: a paused node's worktree is not counted while the node is blocked.
  - New entries **Enabling change** (which also defines "enabling node") and **Pause**.
  - **Park**'s `_Avoid_` line no longer refuses "pause" bare. It now points to **Pause** as a different act.
  - **Raise**: its answer continues, stops, or pauses the node.
- `.claude/rules/expedition-triggers.md` is unchanged. No trigger duty or priority statement in `SKILL.md` was edited.
- No heading was renamed.
- The bar: the root `CLAUDE.md` `## Commands` confirms there is no build, no tests, no formatter and no CI, which matches `map-implementation-rules.md`. So nothing was run. Prose was held to the `## Rules for the files under .claude/skills/`. I checked by hand that new lines are at most 105 characters and that no code span wraps.
- Scope search re-run at `cf5984eadc` before starting: 7 lines in the recorded files, matching the record (count for scale only, not authoritative).

**MISSING FROM MAP, as the worker wrote it:** The map does not say that the effort runs two code slots, or which other node is in flight. The spawn told me (node 13 on `expedition-upgrade/SKILL.md`). Node 12's record shows the human set two slots, recorded in `map-manager-only.md`, which I did not read.

*Manager's note:* landed as `47beb1c218` on `master`, after the human's approval: the node's commit was put on top of `master` (node 13 had landed in another file) and then fast-forwarded; the worktree and branch are removed. The worker's `NEW NODES` part is [node 17](17-count-a-paused-node-out-of-frontier-sh.md) and [node 18](18-take-a-pause-under-a-standing-yes.md).

## Flags

`14.1` `ASSUMPTION` **· settled** — "Pause" was a refused word under the glossary's **Park** (`_Avoid_: pause, ...`), but the condition requires "pause" for a different act. I added glossary entries **Pause** and **Enabling change**, both settled by node 09, since the glossary must hold every term the files use. I changed Park's `_Avoid_` to "pause (that names a different act, under **Pause**)".

`14.2` `ASSUMPTION` **· settled** — A standing yes takes a worker's `RECOMMENDED`, and a too-big-enabling-change raise will usually recommend a pause. The implementation contract read that line only as "continue", so I added "Where your `RECOMMENDED` was the pause, read it as the pause". Ground 1 (my change made it incomplete), inside a listed file.

`14.3` `ASSUMPTION` **· settled** — `expedition/scripts/frontier.sh` counts every claimed implementation node against the slots, so it counts a paused node. The script is outside my condition's list and my condition forbids editing it. I added a sentence in `SKILL.md` telling the manager to subtract paused nodes, and proposed a node to fix the script (NEW NODES).

`14.4` `ASSUMPTION` **· settled** — Node 09 did not say which deliverable an enabling node names. I pointed to the existing rule in `### A deliverable whose base is another deliverable` rather than writing a new one.

`14.5` `ASSUMPTION` **· settled** — The checker is blind to resolved nodes, so it cannot test "fixed by a resolved node, the shipped files...". In the checker contract I worded that limit as "the edit adds places to the work, and adds no requirement of its own".

`14.6` `ASSUMPTION` **· settled** — `### The flags, after your outcome` told the checker to change no outcome because of flags and to ignore their reasons, which contradicts clause 3. I added a named exception for flags that name an outside place. I also required the index sentence of such a flag to carry place, reason and ground, since the checker receives only that sentence.

`14.7` `ASSUMPTION` **· settled** — Some edits inside listed files went beyond the literal clauses, to remove statements contradicting clauses 1 to 6:
- graph-conventions' "clause that excludes every other file" became "limits edits to";
- the implementation contract's opening code-slot sentence;
- the glossary's **Raise** entry, whose answers were only continue or stop.

## Review

### Checker run 1 — `PASS`

The checker's entry, as it wrote it:

PASS

Contract followed: the main checkout's /home/mathieu/projects/graph-agent/.claude/skills/expedition-checker/SKILL.md, not the worktree's edited copy. Work checked: `git diff` in /home/mathieu/projects/graph-agent/.scratch/rename-split-upgrade/worktrees/14-widening-scope against cf5984eadc. Eight files changed, all named in the condition's list. `.claude/rules/` is unchanged and so is `scripts/frontier.sh`. Nothing outside the list was edited, so no outside-list rule is engaged.

Per part of the condition:
- Scope / recorded search: I ran `grep -rn -i "reported and not\|reported, not edited\|permission to edit\|residual clause" .claude/skills .claude/rules` as `git grep` at a40f9008e8. It returned exactly the 7 recorded lines: prototype, precondition, grilling and implementation SKILL.md each have the "Write into the condition…reported and not" bullet, graph-conventions.md has 2 lines in "An instance the search reaches outside…", and checker SKILL.md has 1 line in `### The search a condition records`. That matches the recorded return. At cf5984eadc the same 7 places are found. On the worktree it now returns 9 lines, all in listed files, all of them the rewritten text. There is no mismatch and no place outside the list.
- Clause 1: I read the new `## A place outside your condition's list` in expedition-implementation/SKILL.md.
  - It covers the three grounds, each with its examples and a "Test:".
  - It requires one ASSUMPTION flag per place, naming the place, the reason and the ground, and the place listed in GATE PAYLOAD.
  - It says "leaves your condition's text as it is".
  - It routes an uncovered defect to NEW NODES (grilling where the human must decide), with the join-to-open-node rule cited.
  - It allows an edit beyond the clauses inside a listed file, with a flag.
  - Met.
- Clause 2: same section, last paragraph. The worker judges size and raises under trigger 1 (size of own node), proposing the node's name, question and condition. `### The raise` now lists "one of three ways", including Pause: leave work, wait, resume with "continue" on a worktree holding both, and fix conflicted files in place with no git command. Met.
- Clause 3: new `### An edit outside the condition's list` in expedition-checker/SKILL.md.
  - It states the three grounds, plus a limit sentence: "adds no requirement of its own". That is a shorter form of the condition's limit; flag 14.5 claims it.
  - It has the three bullets: made-wrong place is a finding wherever it lies; flagged edit with a reason that holds is not a FAIL, judged from the work, with ground 3 asked as "would meet … without the edit"; unflagged edit or one whose reason fails is a FAIL on the acceptance condition.
  - The residual-clause bullet in `### The search a condition records` is rewritten to agree.
  - `### The flags, after your outcome` gains a matching exception.
  - Met.
- Clause 4: unwrapped python search of every place from the recorded search.
  - Grilling, precondition and prototype now say "edited only on one of three grounds, with a flag naming the place and the reason…Write too that any other instance is reported and not edited".
  - Implementation says the same, pointing at its own heading.
  - The checker bullet is updated.
  - The graph-conventions paragraph is rewritten, and "never a permission to edit" is gone (grep finds it nowhere).
  - Met.
- Clause 5: new `## A paused implementation node` in expedition/SKILL.md, steps 1–6. It covers:
  - minting the node marked as proposed by that worker;
  - adding it to `Blocked by:`;
  - staying `claimed` and keeping the worktree and work;
  - the worktree counting against no code slot while blocked;
  - bringing the worktree onto the commit where the enabling node landed, with conflicts going to the worker in place;
  - resuming with "continue", with a replacement under `## When an agent dies or is stopped`.
  - The slot-count bullet in `### Picking the next node` cross-references it. Every cited heading exists.
  - Met.
- Clause 6: glossary **Code slot** gains "A paused node's worktree is not counted while the node is blocked." Met.
- Clause 7: `git status` shows .claude/rules/expedition-triggers.md unchanged. The SKILL.md changes touch no trigger duty and no Priority statement: they are a new section, the slot-count bullet and the frontier.sh paragraph. Met.
- Clause 8: no heading removed or renamed (`git diff -U0 | grep '^[-+]#'` shows 3 additions only). I searched the listed files for statements contradicting clauses 1–6, unwrapped: "one of two ways", "continues that worker", "holds/keeping the code slot", "never a permission", "outside … list", "until your work has landed", the `claimed`/`Blocked by:` rules in `## Statuses`, `## Mechanical checks`, the frontier definition, and `### Three states the status line does not show`.
  - The remaining "one of two ways" (precondition raise, starting an effort) concerns other acts.
  - "keeping the code slot" applies only while a raise waits, and the code-slot exception at the top of the implementation contract covers the pause.
  - No contradiction found in the files I hold. Met.

The bar: the root CLAUDE.md `## Commands` says there is no build, no tests, no formatter and no CI, so there is no command to run. I confirmed this against the repo: no build, CI or package files and no .github. `git diff --check` printed nothing. No added line is over 105 columns, so it matches the surrounding wrap.

Standards: I read only the standards in .scratch/rename-split-upgrade/map-implementation-rules.md. They are /coding-principles, /naming, the glossary's _Avoid_ lines, graph-conventions.md, /writing-for-agents, the root CLAUDE.md `## Rules for the files under .claude/skills/`, and the trigger-file rule. The ones that bore on this work:
- **Glossary `_Avoid_` lines:** I grepped added lines for distinctive refusals and found none. The hits for "ask", "report", "queue" and "run" are ordinary English or the condition's own words. Park's refusal of "pause" was narrowed, and a new Pause entry refuses "park".
- **Writing rules 4 and 6:** no line-number citations, and every heading pointer resolves.
- **Trigger-file rule:** not triggered.
- **graph-conventions.md:** the work itself changed it, so I settled first what moved. The altered element is the "never a permission to edit" rule. This work makes no outside-list edit, so it need not be held against that element. The check is untouched.

I held /writing-for-agents by hand and invoked no reviewing skill, because the standards name none as a reviewer.

Flags (checked after the outcome): 14.1–14.7 are each true of the work.
- 14.1: Pause and Enabling change entries added, and Park's _Avoid_ narrowed.
- 14.2: the implementation contract reads "Where your RECOMMENDED was the pause, read it as the pause".
- 14.3: the frontier.sh paragraph tells the manager to subtract paused nodes, and scripts/frontier.sh is unchanged.
- 14.4: step 1 cites `### A deliverable whose base is another deliverable`.
- 14.5: the checker's limit sentence.
- 14.6: the flags-section exception, plus the index-sentence instruction in the implementation contract.
- 14.7: three rewordings, at the code-slot paragraph of the implementation contract, the glossary Raise answer, and graph-conventions "limits edits to every other file".

No false flag.

QUESTIONS: none.
NOT COVERED: none.

No temporary files were written.

### Gate outcome — approve

The human's words, `verbatim`:

> approve

## Annotation: node 18 extends the pause to a standing yes

As the worker of [node 18](18-take-a-pause-under-a-standing-yes.md) reported it: Node 14 (resolved): an extension. Its flag 14.2 made the worker read a `STANDING YES` line as the pause. The manager's side now carries out the pause steps as well. No contradiction.

## Annotation: node 19 renames the flag sentence this answer names

As the worker of [node 19](19-ship-dropping-flags-md.md) reported it: 14: a rename. Its `## Answer` says "the flag's index sentence must carry all three". The implementation contract now says "the sentence that opens the flag's entry".

## Annotation: node 17 supersedes the hand subtraction

As the worker of [node 17](17-count-a-paused-node-out-of-frontier-sh.md) reported it: Node 14 (resolved) is narrowed. Its answer says the `frontier.sh` paragraph in SKILL.md tells the manager to subtract paused nodes. Its flag 14.3 records that it added that sentence and that the script counts a paused node. Both statements describe the state before this node, and they are now superseded: the script leaves the paused node out, and the sentence is gone. Node 09's rule (a paused node holds no slot while blocked) is unchanged, and the script now matches it.
