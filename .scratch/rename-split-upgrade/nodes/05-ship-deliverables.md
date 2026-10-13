# Ship deliverables: several branches and pull requests in one effort

Type: implementation
Status: resolved
Labels: SPLIT

## Question

This lets a human run one expedition holding several mostly independent pieces of work, each landing on its own branch as its own pull request, with each piece cleaned out of the graph once it has merged. It writes the deliverable mechanism into the shipped skill files, so that any manager in any repository can run it.

*Manager's note:* minted by the worker of [node 02](02-several-deliverables-in-one-effort.md) on its `NEW NODES` part, with the question and condition below as it wrote them.

## Acceptance condition

Scope: this work names its places rather than fixing instances of a defect, so its scope came from no search. The files it may change are `.claude/skills/expedition/glossary.md`, `.claude/skills/expedition/graph-conventions.md`, `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition-cleanup/SKILL.md`, and `.claude/rules/expedition-triggers.md` (only as clause 9 allows). Any other file found to need a change is reported, not edited.

1. `glossary.md` has an entry for the term **Deliverable**. It says that a deliverable is one piece of an effort's work that lands on its own branch and becomes its own pull request, that it is declared in the effort's map, and that each implementation node belongs to at most one deliverable. The entry for **Handover** still lists `deliverable` in its `_Avoid_` line, and the reason given there no longer says the word is unused. It says that the word names another concept.
2. `graph-conventions.md` says that `map-manager-only.md` may hold a list of deliverables. Each entry gives the deliverable's name, its branch, and its base, and the base is either the upstream branch its pull request targets or the name of another deliverable. The file says that an effort whose map declares no deliverables lands as its landing policy says, with no deliverable involved. It also says that an entry is added when a deliverable is declared and removed when that deliverable is cleaned up.
3. `graph-conventions.md`'s node-file template and its description of the header fields include `Deliverable: <name>`, carried only by implementation nodes, holding exactly one name. Its `## Mechanical checks` gains a check that every `Deliverable:` value names an entry in the map's list of deliverables, and that only implementation nodes carry the field.
4. The shipped files state these landing rules for an implementation node that names a deliverable. The node's worktree is cut from the tip of its deliverable's branch. On approval the code commit is made on the node's own branch, and the deliverable's branch then moves to that commit by fast-forward only. Where the deliverable's branch has moved since the worktree was cut, the node's commit is put on its tip first, and a conflict starts a correction round naming the conflicted paths. The main checkout does not receive the node's code. A deliverable's branch is created when the deliverable is declared, from its base, and never from the main checkout.
5. `SKILL.md` says that the manager pushes a deliverable's branch only on the human's yes to that push, and that the human creates the pull request. It says that the manager offers the push when every implementation node naming that deliverable has resolved, and whenever the human asks. It says that every push needs its own yes, including a push that overwrites the remote branch after a rebase. It says that a standing yes covering the push counts as that yes.
6. The shipped files say that a deliverable whose base is another deliverable has its branch cut from that deliverable's branch. They say that a node may be blocked on a node of its own deliverable or of its deliverable's base, and on no other deliverable's node. When the base deliverable gains commits the dependent one needs, the manager rebases the dependent branch onto the base's branch. When the base deliverable's pull request merges upstream, the dependent's base becomes the upstream branch and the manager rebases onto it. A rebase that conflicts becomes an implementation node of the dependent deliverable.
7. `expedition-cleanup/SKILL.md`'s region cleanup says how a deliverable is cleaned up. When the human says a deliverable's pull request has merged, the manager proposes a region cleanup whose region is that deliverable. The proposed set is the nodes naming that deliverable, plus each resolved node whose every dependent is in the set. The skill's existing conditions and the human's confirmation still apply. Once the record is cleaned, the manager removes the deliverable's entry from the map's list and deletes the deliverable's local branch. The remote branch is not touched.
8. No shipped file names git-branchless or any other tool beyond git as required. Push and branch operations are stated as properties, not as declared commands.
9. `.claude/rules/expedition-triggers.md` changes only where this work edits, in `.claude/skills/expedition/SKILL.md`, the governing statement of one of the manager's trigger-duties or of the priority that orders them. In that case it changes to match.
10. Every heading of a file under `.claude/skills/` that this work renames is updated at every place under `.claude/skills/` that cites it by its exact text.

*Manager's note, before the claim:* the passages the condition names are present on 2026-10-12: the glossary's **Handover** `_Avoid_` line lists `deliverable` with no reason of its own, and `expedition-cleanup/SKILL.md` has a `## Region cleanup` heading. Nothing is written after the condition but this note.


### Amendment 1 — written by the manager, taken by the human at the gate

The human's reply at the gate, `verbatim`: *"correct"*, in answer to the manager's question, which offered correct as "amending node 05's condition to add the four stale files". The source of the four files: the checker's run 1 and run 2 questions and the worker's fix for run 1, recorded under `## Review`. This amendment widens the scope clause and adds clause 11. The condition's other clauses stand as written.

Scope, widened: the files this work may change also include `.claude/skills/expedition-standing-yes/SKILL.md`, `.claude/skills/expedition/adoption.md` and `.claude/skills/expedition/wayfinder-divergences.md`.

11. The shipped files outside the original list agree with this work:
    - `.claude/skills/expedition-standing-yes/SKILL.md` says that a push of a deliverable's branch is an item a standing yes can cover, and says what the manager does with a covered push, consistent with `### Pushing a deliverable's branch` in `.claude/skills/expedition/SKILL.md`. Neither file contradicts the other.
    - The frontmatter `description` of `.claude/skills/expedition-cleanup/SKILL.md` no longer says only that the human invokes it, since the manager proposes a region cleanup for a merged deliverable.
    - `.claude/skills/expedition/adoption.md`'s step that runs the checks of `### Start an effort` names checks 1, 3, 4 and 12, matching step 9 of `### Start an effort` in `.claude/skills/expedition/graph-conventions.md`.
    - `.claude/skills/expedition/wayfinder-divergences.md` `## Added` lists the `Deliverable:` node field and the optional `## Deliverables` list in `map-manager-only.md`.


## Answer

The deliverable mechanism that node 02 decided is now written into the shipped skill files. It is opt-in: an effort that declares no deliverables lands as its landing policy says.
- `glossary.md`: a new **Deliverable** entry under `## Landing code`. **Handover**'s `_Avoid_` line still refuses `deliverable`, and now gives the reason that the word names another concept. The **Standing yes** entry gains one sentence: on a push of a deliverable's branch, a standing yes counts as the human's yes to that push.
- `graph-conventions.md`, under `## The seven files`: `map-manager-only.md` may hold `## Deliverables`. The section gives two fenced entry forms, one with base `upstream <branch>` and one with base `deliverable <name>`. It says when an entry is added and when it is removed. Changing or removing an entry follows `### Change the map`, so the old text moves to `map-history.md` and check 11 still holds. An effort that declares none lands as its landing policy says.
- `graph-conventions.md`, node file: the template gains `Deliverable: <name>` between `Status:` and `Labels:`. A description paragraph says the field is carried only by implementation nodes and holds exactly one name. New mechanical check 12 says every `Deliverable:` value names an entry under `## Deliverables`, and only implementation nodes carry the field. Check 12 is added to the run-at-the-act steps of `## Adding a node`, `### Start an effort` and `### Change the map`.
- `SKILL.md`: a new `## Deliverables` section after `## The gate`, with subsections on declaring a deliverable, where its code lands, pushing its branch, a deliverable whose base is another deliverable, and cleaning up a merged deliverable. `## The gate` gains a one-line pointer to it.
- `expedition-cleanup/SKILL.md`: a new `### A merged deliverable as the region` under `## Region cleanup`. `## Two operations` names it as the one region cleanup proposed without the human invoking the skill. `## Reporting` covers whether the entry and branch were removed.
Calls a later reader would otherwise re-derive:
(a) Offering a push is the manager's own raise, so it sits in tier 1 of the queue that already exists. No new queue kind or trigger is added. The trigger file is unchanged because no governing statement of a trigger-duty or of the priority was edited.
(b) `expedition-standing-yes` limits a standing yes to three kinds of item and excludes the manager's own raise. `SKILL.md` therefore changes that rule for a push only, naming the heading `## What a standing yes covers` (CLAUDE.md writing rule 6).
(c) The cleanup set's second item reads "each resolved node that blocks at least one node, and whose every dependent is in the set". It is applied again until it adds nothing. Without "at least one", every resolved node with no dependents would join the set, because "every dependent is in the set" is true when there are none.
(d) A deliverable's entry is removed, and its local branch deleted, only once no remaining node names it. Otherwise check 12 would fail on a base deliverable's node kept because a dependent deliverable's node is blocked on it.
(e) The blocking limit applies only to nodes that name a deliverable. A node with no deliverable, such as a grilling node, is not limited by it.
(f) A rebase that conflicts is left undone, and the manager mints the implementation node.
Nothing names git-branchless, and every git step is written as a property rather than a command.

*Manager's note:* point (b) above was superseded in correction round 1, recorded under `## Review`: `expedition-standing-yes` now lists a push as a fourth kind of item, and `SKILL.md` defers to it rather than stating an exception. Landed as `7a86d138e0` on `master` by fast-forward, after the human's approval; the worktree and branch are removed. The worker's grilling node from its `NEW NODES` part is node 06; the follow-up it later reported for four stale files was folded into this node by amendment 1.

## Flags

`05.1` `ASSUMPTION` **· settled** — (push offer is the manager's own raise): The shipped files had no kind of queue item for offering a push. I made the offer the manager's own raise, which tier 1 already holds, rather than add a kind that only the human may add. A standing yes does not cover the manager's own raise, so `SKILL.md` names `## What a standing yes covers` in `expedition-standing-yes` and changes it for a push only. That skill file was outside my scope and is left unchanged.

`05.2` `ASSUMPTION` **· settled** — (cleanup set needs a real dependent, applied repeatedly): Read literally, "each resolved node whose every dependent is in the set" is true of every node that has no dependents, which would sweep every unrelated finished leaf node into the deliverable's cleanup. I required at least one dependent, defined a dependent as a node listing it in `Blocked by:`, and made the item apply again until it adds nothing, so that a chain of grilling nodes serving only that deliverable is caught.

`05.3` `ASSUMPTION` **· settled** — (entry and branch kept while a node still names the deliverable): Condition 7 removes the entry once the record is cleaned, but a base deliverable's node can stay because a dependent deliverable's node is blocked on it. Removing the entry then would break check 12. So the entry and local branch go only once no remaining node names the deliverable, and a later cleanup removes them.

`05.4` `ASSUMPTION` **· settled** — (blocking limit only binds nodes that name a deliverable): Clause 6 says "a node may be blocked on a node of its own deliverable or of its base". A node with no deliverable has no own deliverable, and reading the clause literally would forbid such a node, for example a grilling node, from waiting on any deliverable's work. I wrote that such a node is not limited by the rule.
`05.6` `ASSUMPTION` **· settled** — Amendment 1 to the acceptance condition, written by the manager and taken by the human at the gate with *"correct"*: it widens the scope to three more files and adds clause 11, so that the node leaves no shipped file stale.

`05.5` `ASSUMPTION` **· settled** — (a push taken under a standing yes): `expedition-standing-yes`'s `## Taking a covered item` records a covered item on its node, and a push has no node. I had the manager push in the turn it would have offered the push, and then say in its next report to the human which branch it pushed, quoting the standing yes's scope text. Nothing is written to the record, which keeps the push exception short.

## Review

### Checker run 1 — `FAIL`, the bar

The checker's entry, as it wrote it:

FAIL: the bar

Finding 1: a stale pointer in SKILL.md now contradicts the new push exception.
- Instances: `.claude/skills/expedition/SKILL.md`, `## What is in front of the human, and when`, last paragraph: "An item that a standing yes covers is handled by the skill `expedition-standing-yes` ... That skill says which items a standing yes can cover, and what you do in place of putting one to the human." The work's new `### Pushing a deliverable's branch` makes a push coverable by a standing yes. `expedition-standing-yes` does not list a push under `## What a standing yes covers`. Its `## Taking a covered item` gives no step for one. So the pointer sends the manager to a skill that no longer says which items are covered, and that has nothing to do for a covered push. This file is in the work's scope, so the worker could have fixed it. Standard breached: the root CLAUDE.md rule for writing 6 (a pointer says what the reader goes there for), and `/writing-for-agents` `## Pruning` (relevance: a line goes stale when the behaviour it describes changes). Found by `grep -n -i 'standing yes\|standing-yes'` over the four changed files, then reading each hit.
- Form: a statement in an editable file that says `expedition-standing-yes` alone fixes which items a standing yes covers, or what the manager does with a covered item. Since this work, that statement leaves out the push.
- Extent: `grep -n -i 'standing yes\|standing-yes' .claude/skills/expedition/SKILL.md .claude/skills/expedition/glossary.md .claude/skills/expedition/graph-conventions.md .claude/skills/expedition-cleanup/SKILL.md`. Of its hits, I judged only SKILL.md 615-617 to be an instance. SKILL.md:52 ("take a standing yes as `expedition-standing-yes` says") is a borderline candidate.

The acceptance condition, part by part. All parts hold, so the condition is met. Method: I read `git diff` over the worktree and ran a grep, over unwrapped text, for each part.
1. Met. The glossary has a `**Deliverable**:` entry. It says the deliverable lands on its own branch and becomes its own pull request, is declared in the effort's map, and that each implementation node belongs to at most one. The Handover `_Avoid_` line keeps `deliverable`, and its reason now says that word names another concept.
2. Met. `graph-conventions.md`, `## The seven files`, says `map-manager-only.md` may hold `## Deliverables`. Each entry gives a name, a branch and a base, in two forms: upstream, or another deliverable. The same passage says an effort with no deliverables lands as its landing policy says, and that an entry is added on declaration and removed on cleanup.
3. Met. The `## The node file` template has a `Deliverable: <name>` line, and the paragraph before it says the field is carried only by implementation nodes and holds exactly one name. `## Mechanical checks` has a new check 12. The check-step lists in Adding a node, Start an effort and Change the map now include 12.
4. Met. SKILL.md `### Where a deliverable's code lands`, steps 1-5, and its closing line say: the worktree is cut from the deliverable's tip; the code commit is made on the node's own branch; the deliverable's branch moves by fast-forward only; the commit is put on the moved tip first, and a conflict starts a correction round naming the conflicted paths; the main checkout never receives the code. `### Declaring a deliverable` says the branch is created from its base and never from the main checkout.
5. Met. `### Pushing a deliverable's branch` has every element: push only on the human's yes; the human creates the pull request; the offer is made when every implementation node has resolved, and whenever asked; every push needs its own yes, including an overwrite after a rebase; a standing yes covering the push counts.
6. Met. `### A deliverable whose base is another deliverable` has every element: the branch is cut from the base deliverable's branch; a node may be blocked on its own deliverable or its base and no other; rebase when the base gains commits; rebase onto upstream when the base's pull request merges; a conflicting rebase becomes an implementation node of the dependent deliverable.
7. Met, under the reading set out in QUESTIONS. The new `expedition-cleanup/SKILL.md` section `### A merged deliverable as the region` has the trigger and the set. It says steps 2 to 6 apply unchanged. It removes the map entry and deletes the local branch, and leaves the remote branch alone.
8. Met. A grep of the added lines for `branchless|git |gh |jj|graphite|stack|--force|push --|merge-base` found no tool or command. Push and branch operations are stated as properties.
9. Met. `.claude/rules/expedition-triggers.md` is unchanged, according to `git status`. The SKILL.md hunks do not touch `## The order you act in` or the trigger statements.
10. Met, with nothing to update. `git diff -U0 | grep '^[-+]#'` shows only added headings, so no heading was renamed.
- The condition records no search for its scope, so there was nothing to re-run. No file outside the scope list was edited, according to `git diff --name-only`.

The bar: the repository has no build, tests, formatter or CI. Root CLAUDE.md `## Commands` says so, and the worktree's root holds no package or Makefile files and no `.github` directory, so there was no command to run. I read only the standards in `.scratch/rename-split-upgrade/map-implementation-rules.md`: `/coding-principles`, `/naming`, the glossary's `_Avoid_` lines, `graph-conventions.md`, `/writing-for-agents` (read from the mattpocock-skills plugin), the root CLAUDE.md rules for writing, and the trigger-file rule. All of them bore on this work. I checked the `_Avoid_` refusals in the added lines by hand. "item" and "report" are used in their ordinary sense, which is fine. No reviewing skill is named, so none was run.

QUESTIONS:
- Part 7, how to read "each resolved node whose every dependent is in the set". Taken literally, a resolved node with no dependents qualifies, because "every dependent" is then trivially true. That reading would sweep every dependent-less resolved node in the effort into the set. I took the reading that the node must have at least one dependent, all in the set, which is what the work does (flag 05.2). Under the literal reading the work fails part 7. Does the human confirm this reading?
- Part 7 against part 3. Part 7 says that once the record is cleaned the entry is removed and the local branch deleted, with no condition attached. If a node naming the deliverable survives the cleanup (for example, the human amends the set), removing the entry makes check 12 from part 3 fail. I checked the work under the reading where both parts hold: remove the entry only once no remaining node names the deliverable (flag 05.3). The other reading, unconditional removal, fails part 7 as the work stands. Does the human accept this reading?
- A condition met but still wrong. The wording here is the condition's own, so departing from it was not the worker's call. Part 5 makes a standing yes cover a push, and the work states this as an exception in SKILL.md. But `expedition-standing-yes` is outside the scope and was not changed. Its `## What a standing yes never covers` says "Anything outside the three kinds above is not covered either, your own raise included", "whatever the scope says". Its `## Taking a covered item` has no step for a push. Should a follow-up change `expedition-standing-yes`?
- Out-of-scope files the work has made stale. These can only be reported, not edited. (a) `.claude/skills/expedition/adoption.md`, step 7.4: "Run checks 1, 3 and 4 ... as step 9 of `### Start an effort` requires". Step 9 now names checks 1, 3, 4 and 12. (b) `.claude/skills/expedition/wayfinder-divergences.md` `## Added` lists the added header fields (`Labels:`, `Supersedes:`), but does not list `Deliverable:`. Extent: `grep -rnE 'checks? [0-9, and]+' .claude/skills` and a read of the field lists in `wayfinder-divergences.md`. I cannot see whether the worker already reported these.

Flags (checked after the outcome): 05.1, 05.2, 05.3 and 05.4 are each true of the work, so none is false.

### The worker's fix for checker run 1, as the worker wrote it

Finding 1 (stale pointer to `expedition-standing-yes`): fixed, in `.claude/skills/expedition/SKILL.md` only.
- `## What is in front of the human, and when`, last paragraph: after "That skill says which items a standing yes can cover, and what you do in place of putting one to the human." added "The exception is a push of a deliverable's branch, which `### Pushing a deliverable's branch` covers."
- The borderline instance, the `## What is never yours` table row: its second cell now reads "take a standing yes as `expedition-standing-yes` says, or for a push as `### Pushing a deliverable's branch` says".
- The checker also noted that `expedition-standing-yes` gives no step for a covered push. So `### Pushing a deliverable's branch` now says what to do with one: "Push a covered branch in the turn you would otherwise have offered the push. Say in your next report to the human which branch you pushed, and quote the scope text of the standing yes that covered it." This is a small new decision, flagged below.
- I checked the trigger file's line "Where a standing yes covers it, take it as `/expedition-standing-yes` says instead". It concerns something an agent hands back, and a push offer is the manager's own raise, so it is not an instance. `.claude/rules/expedition-triggers.md` stays unchanged, because no governing statement of a trigger-duty or of the priority was edited.

Does the correction touch anything the condition names? Yes. Clause 5 covers the standing yes on a push, and the new sentences sit in `### Pushing a deliverable's branch`. Clause 5's content is unchanged and only made actionable, but re-check clause 5.

The checker's two out-of-scope reports, left unedited because the condition's scope clause lists neither file:
- `.claude/skills/expedition/adoption.md` step 7.4 names checks "1, 3 and 4" where `### Start an effort` step 9 now names 1, 3, 4 and 12. Clause to give a follow-up node: "`.claude/skills/expedition/adoption.md`'s step that runs the checks of `### Start an effort` names checks 1, 3, 4 and 12, matching step 9 of `### Start an effort` in `.claude/skills/expedition/graph-conventions.md`."
- `.claude/skills/expedition/wayfinder-divergences.md` `## Added` does not list the `Deliverable:` field. Clause to give a follow-up node: "`.claude/skills/expedition/wayfinder-divergences.md` `## Added` lists the `Deliverable:` node field and the optional `## Deliverables` list in `map-manager-only.md`."
These can join the follow-up already reported for `expedition-standing-yes/SKILL.md` (`## What a standing yes covers` and `## Taking a covered item` do not list a push) and for the `expedition-cleanup` frontmatter description. That makes one small implementation node bringing four out-of-scope files into step.

Paths touched this round: `.claude/skills/expedition/SKILL.md`.

### Checker run 2 — `PASS` (re-check)

The checker's entry, as it wrote it:

PASS (re-check of node 05, same worktree)

What changed, and what I did about it:
- I re-established the work from the files, not from the worker's description of its change. `git diff` hunk headers for `.claude/skills/expedition/SKILL.md` show four hunks: the `## What is never yours` table row (`@@ -49`), the landing-policy pointer (`@@ -330`), `## Deliverables` (`@@ -352`) and the queue paragraph (`@@ -547`). The new text in the first and last hunks, and the added sentences under `### Pushing a deliverable's branch`, match the worker's account word for word. `git diff --stat` for the other three files is unchanged from the last round (cleanup 33, glossary 13, graph-conventions 37), and their modification times predate SKILL.md's. So I let my earlier results on them stand.
- Finding 1 is resolved. `## What is in front of the human, and when` now ends with "The exception is a push of a deliverable's branch, which `### Pushing a deliverable's branch` covers." The table row now points at `### Pushing a deliverable's branch` for a push. That heading exists in the same file. `grep -n -i 'standing yes\|standing-yes'` over the four changed files leaves no other hit that says `expedition-standing-yes` alone decides what a standing yes covers.

Standards: none changed since my last read. `.scratch/rename-split-upgrade/map-implementation-rules.md` was last modified at 21:03, before my first read, and I again read only the standards in it. The root CLAUDE.md is unchanged, last modified at 21:19. This round edited neither `glossary.md` nor `graph-conventions.md`, both of which are themselves standards. `/writing-for-agents` sits in a read-only store path. I checked the added sentences against the glossary's `_Avoid_` lines by hand: "report" there is a report to the human, which is its correct sense.

Clause 5, re-established against the new text in `### Pushing a deliverable's branch`:
- Push only on the human's yes, and the human creates the pull request: present.
- Offer the push when every implementation node naming the deliverable has resolved, and whenever the human asks: present.
- Every push needs its own yes, including an overwrite after a rebase: present.
- A standing yes covering the push counts as that yes: present.
- The new sentences ("Push a covered branch in the turn you would otherwise have offered the push. Say in your next report ... quote the scope text") contradict none of these. A covered push is still made on a yes, the standing yes, so each push still has its own yes.

Clauses 9 and 10: still met. `.claude/rules/expedition-triggers.md` is unchanged (`git status`). `git diff | grep '^[-+]#'` shows only added headings, none removed or renamed. The hunks do not touch `## The order you act in`. I accept the worker's reading of the trigger file's standing-yes line: it concerns things an agent hands back, and a push offer is the manager's own raise.

Clauses 1-4 and 6-8: established last round and not affected by this change, so I let them stand.

The bar: the repository has no build, tests, formatter or CI. The root CLAUDE.md `## Commands` says so, and the worktree root holds no such tooling. No command exists to run.

QUESTIONS (the ones still open from last round):
- Part 7, the reading of "each resolved node whose every dependent is in the set". I took the reading that a node must have at least one dependent, all of them in the set (flag 05.2). Read literally, every resolved node with no dependents would join the set. Does the human confirm this reading?
- Part 7 against part 3. I took the reading that the map entry and the local branch are removed only once no remaining node names the deliverable (flag 05.3). Removing them with no condition would break check 12. Does the human accept this reading?
- `expedition-standing-yes`, which is outside this node's scope, still says under `## What a standing yes never covers` that anything outside the three kinds is not covered, "your own raise included", "whatever the scope says". SKILL.md now gives the push exception and a step for a covered push. A manager reading only the standing-yes skill would still meet the contradiction. Is a follow-up change to that skill wanted?
- Two out-of-scope files are stale. `adoption.md` step 7.4 still says to run "checks 1, 3 and 4 ... as step 9 of `### Start an effort` requires", but step 9 now names 1, 3, 4 and 12. `wayfinder-divergences.md` `## Added` does not list the `Deliverable:` field.

Flags: 05.1-05.4 are still true of the work. 05.5 is true. The new text has the push made in the turn the offer would have been made, and names it in the next report with the scope quoted. None of the four changed files gives any step that records such a push on a node.

### The human's reply at the gate, `verbatim`

> approve, for the checker ok . Also right now the rules seems to somewhat prevent having a implementation node scope increase when the checker or the worker finds issues. I feel like the work itself should be more important than having an explicit list of files to change. Maybe the worker/checker can increase the scope by giving a reason if it finds something when implementing the node ? I don't really like the fact that there are stale files introduced by the node. Maybe not approve and correct instead to fix it ?

*Manager's note:* the reply opens with "approve" and closes by asking whether to correct instead. The outcome is not yet clear, so nothing is committed; the manager asked the human which. "for the checker ok" answers the checker's questions: the readings of flags 05.2 and 05.3 hold, and the follow-up on the stale files is wanted.

### Correction round 1

The human's words, `verbatim`: *"correct"*. What it asks for: Amendment 1 under `## Acceptance condition`, bringing the four stale files into step.

What the worker changed, as it wrote it:

1. `.claude/skills/expedition-standing-yes/SKILL.md`
   - `## What a standing yes covers`: it now says "four kinds of item, and no other". The fourth kind is "A push of a deliverable's branch, which you would otherwise offer the human as your own raise. The standing yes is taken as the human's yes to that one push."
   - The closing line of `## What a standing yes never covers` now reads: "Anything outside the four kinds above is not covered either. That includes every raise of your own other than the offer of a push."
   - `## Taking a covered item`: step 1 now applies to a question, a raise or a gate. A new step 4 reads: "For a push, push the deliverable's branch. A push belongs to no node, so nothing is recorded on one. Say in your next report to the human which branch you pushed, and quote the scope text of the standing yes that covered it."
   - The frontmatter `description` gains: "It may also cover a push of a deliverable's branch."

2. Made consistent with that, in `.claude/skills/expedition/SKILL.md`:
   - `### Pushing a deliverable's branch` no longer states an exception to the standing-yes skill. It now says: "A standing yes whose scope covers a push counts as the human's yes to that push. `## Taking a covered item` in `expedition-standing-yes` says what you do with a covered push." Clause 5's sentence stands. The steps live only in the standing-yes skill, so they are not stated twice (CLAUDE.md writing rule 6).
   - The last paragraph of `## What is in front of the human, and when` ends: "A push of a deliverable's branch is one such item." This replaces round 0's "exception" sentence.
   - The `## What is never yours` row is back to its original text, "take a standing yes as `expedition-standing-yes` says". The skill now lists the push, so that text is true again.
   - Neither file contradicts the other. A search for "three kinds" finds no stale count about standing yes. The remaining hits are about tier 1, `## Review` entries and edges.

3. `.claude/skills/expedition-cleanup/SKILL.md` frontmatter `description` gains: "The manager also reads it to propose a region cleanup when the human says a deliverable's pull request has merged."

4. `.claude/skills/expedition/adoption.md`: step 7.4 now reads "Run checks 1, 3, 4 and 12 under `## Mechanical checks` in `graph-conventions.md`, as step 9 of `### Start an effort` requires."

5. `.claude/skills/expedition/wayfinder-divergences.md` `## Added` gains: "The `Deliverable:` field, on an `implementation` node only, and the optional `## Deliverables` list in `map-manager-only.md` that it names an entry of."

Does the correction touch anything the condition names? Yes: clause 11, all four parts; clause 5, through the rewording of the standing-yes sentence in `### Pushing a deliverable's branch`. No heading was renamed (clause 10). `.claude/rules/expedition-triggers.md` is unchanged.

Flags: no new flag. The assumption about a push taken under a standing yes, filed last round, now describes the behaviour stated in `expedition-standing-yes` `## Taking a covered item` step 4, rather than an exception in `SKILL.md`. The reported follow-up node for the four stale files is now unnecessary.

Paths touched this round: `.claude/skills/expedition-standing-yes/SKILL.md`, `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition-cleanup/SKILL.md`, `.claude/skills/expedition/adoption.md`, `.claude/skills/expedition/wayfinder-divergences.md`.

### Checker run 3 — `PASS` (re-check after correction round 1, against the amended condition)

The checker's entry, as it wrote it:

PASS (re-check after correction round 1, against the amended condition)

Scope as widened: `git status --short` lists seven modified paths. They are the original four plus `.claude/skills/expedition-standing-yes/SKILL.md`, `.claude/skills/expedition/adoption.md` and `.claude/skills/expedition/wayfinder-divergences.md`. All seven are inside the amended list. `.claude/rules/expedition-triggers.md` is unchanged.

What changed this round, re-established from `git diff` and not from the worker's account:
- `expedition/SKILL.md`. The `## What is never yours` table row is back to its original text, and that hunk is gone from the diff. The text is accurate again, because `expedition-standing-yes` now covers a push. `### Pushing a deliverable's branch` now ends "A standing yes whose scope covers a push counts as the human's yes to that push. `## Taking a covered item` in `expedition-standing-yes` says what you do with a covered push." The queue paragraph now ends "A push of a deliverable's branch is one such item." No heading is removed or renamed: `git diff | grep '^[-+]#'` shows only added headings. The trigger statements and `## The order you act in` are untouched.
- `glossary.md` and `graph-conventions.md` were last modified at 21:44, before this round, and their diff stats are unchanged (13 and 37). My earlier results on them stand.

Clause 5, re-checked against the new wording in `### Pushing a deliverable's branch`:
- Push only on the human's yes, and the human creates the pull request: present.
- Offer the push when every implementation node naming the deliverable has resolved, and whenever the human asks: present.
- Every push needs its own yes, including an overwrite after a rebase: present.
- A standing yes covering the push counts as that yes: present.
- The new step 4 in `expedition-standing-yes` says "push the deliverable's branch", one push per yes. This is consistent with "every push needs its own yes".

Clause 11:
- Standing-yes skill: met. `## What a standing yes covers` now lists four kinds, including "A push of a deliverable's branch ... taken as the human's yes to that one push". `## What a standing yes never covers` now excludes "every raise of your own other than the offer of a push". `## Taking a covered item` has step 4, push and report. Step 1, which records the item on the node, is limited to a question, a raise or a gate. Nothing in it contradicts `### Pushing a deliverable's branch`, which defers to it. `grep -rn 'three kinds' .claude/skills` finds no leftover statement of three covered kinds. The remaining hits are about the tiers, entry kinds and edges, which are unrelated.
- Cleanup frontmatter: met. The `description` now adds "The manager also reads it to propose a region cleanup when the human says a deliverable's pull request has merged."
- `adoption.md` step 7.4: met. It now reads "Run checks 1, 3, 4 and 12", which matches step 9 of `### Start an effort` (`graph-conventions.md`).
- `wayfinder-divergences.md` `## Added`: met. It lists "The `Deliverable:` field, on an `implementation` node only, and the optional `## Deliverables` list in `map-manager-only.md` that it names an entry of."

Clauses 1-4 and 6-10: no change this round affects them. They stand as established, under the readings of part 7 that the human has now confirmed.

The bar: the repository has no build, tests, formatter or CI. The root CLAUDE.md `## Commands` says so, so there is no command to run. The standards are unchanged since my last read: `map-implementation-rules.md` was last modified at 21:03 and the root CLAUDE.md at 21:19, and the glossary and graph-conventions did not change this round. I read only the standards in `map-implementation-rules.md`. I checked the new sentences against the glossary's `_Avoid_` lines by hand. "report" there is a report to the human, and "item" means a kind of item a standing yes covers, not a node. Neither is a refused use. I found no breach of rules 1-6 for writing in the added text.

Flags: 05.1-05.5 are true of the work. For 05.5, step 4 records nothing on a node, and the push is taken "in the same turn you would otherwise have queued it". 05.6 describes the amendment, which lives in the record, and makes no claim the work can make true or false.

### Gate outcome — approve

The human's words, `verbatim`:

> approve

## Annotation: node 06 extends what this node shipped

As the worker of [node 06](06-which-checkout-a-non-implementation-worker-reads.md) reported it: Node 05 (resolved, landed as `7a86d138e0`): extended. Its condition clause 3 and its shipped text say `Deliverable:` is "carried only by implementation nodes, holding exactly one name", and that check 12 says "Only implementation nodes carry the field". `wayfinder-divergences.md` says "on an `implementation` node only". The cleanup region's first item takes "every node whose `Deliverable:` field names that deliverable", and `SKILL.md` still says "every other worker reads the main checkout". The node minted above changes each of these.

*Manager's note:* "the node minted above" is [node 10](10-ship-deliverable-on-every-node-kind.md).

## Annotation: node 08 adds a local-merge counterpart

As the worker of [node 08](08-a-deliverable-that-lands-by-merging-locally.md) reported it: Node 05: an extension of what it shipped. Its clauses on the entry's base, "upstream branch or another deliverable", and on the main checkout receiving code "only through the upstream merge", and its push and cleanup clauses now have a local-merge counterpart. The new node ships these changes.

## Annotation: node 07 adds an upgrade-only exception to `### Declaring a deliverable`

As the worker of [node 07](07-ship-expedition-upgrade.md) reported it: Node 05 is extended, not contradicted. Its `### Declaring a deliverable` rule (create the branch from the base's tip) now has an upgrade-only exception, stated in `expedition-upgrade`, which names that heading.

## Annotation: node 10 extends and narrows what this node shipped

As the worker of [node 10](10-ship-deliverable-on-every-node-kind.md) reported it: Node 05 (resolved): extended and narrowed. Its condition clause 3 and its answer say `Deliverable:` is "carried only by implementation nodes", and that check 12 says only implementation nodes carry it. Its wayfinder clause says "on an `implementation` node only". Its clause 6 says a node may be blocked on "a node of its own deliverable or of its deliverable's base". All of these now read: any node may carry the field, an implementation node holds one name, and a node belongs to every deliverable it names for the blocking rule. Assumption 05.4, which says a node with no deliverable is not limited, still holds. Node 02 (resolved): its assumption 02.2 is narrowed as node 06's answer states, and node 10 ships that narrowing. Node 06: implemented, not contradicted.

## Annotation: node 11 ships the local merge

As the worker of [node 11](11-ship-the-local-merge-of-a-deliverable.md) reported it: Node 05: an extension of what it shipped: the glossary Deliverable entry and the Handover `_Avoid_` parenthesis; the two forms of base, now three; "The main checkout never receives the node's code", now replaced; push applies only to a deliverable that lands by pull request; cleanup, also proposed after a local merge; standing yes, "four kinds", now five.

## Annotation: node 15 renames a heading this answer cites

As the worker of [node 15](15-whether-flags-md-is-dropped.md) reported it: 05: a rename. Its `## Answer` cites `graph-conventions.md` `## The seven files`, which becomes `## The graph's files`.
