# Ship the local merge of a deliverable

Type: implementation
Status: resolved
Labels: SPLIT
Blocked by: ~~07~~, ~~10~~

## Question

This lets a human who works alone on a repository use deliverables without pushing branches or opening pull requests: a deliverable can land by being merged locally into a branch. It writes into the shipped skill files the third form of a deliverable's base, `base: local <branch>`, the default when no form is stated, the merge on the human's yes, how the merge is made, and the cleanup that follows it.

*Manager's note:* minted by the worker of [node 08](08-a-deliverable-that-lands-by-merging-locally.md) on its `NEW NODES` part, with the question and condition below as it wrote them. It gave the blockers as "07, 10 (both edit `.claude/skills/expedition/SKILL.md`, and 07 adds `.claude/skills/expedition-upgrade/SKILL.md`, which this node changes)".

## Acceptance condition

Scope: the files this work may change are named below, and the named places are the work. The scope also came from these searches, run from the repository root over the working tree on 2026-10-12 at commit `7a86d138e0`, before nodes 07 and 10 landed (counts for scale only, not authoritative):
- ~~`grep -rn -i "pull request" .claude` returned 12 lines: 3 in `.claude/skills/expedition/glossary.md`, 2 in `.claude/skills/expedition-cleanup/SKILL.md`, 1 in `.claude/skills/expedition/graph-conventions.md` and 6 in `.claude/skills/expedition/SKILL.md`.~~ *(superseded by amendment 1 below)*
- ~~`grep -rn -i "push" .claude`, keeping the lines that also contain "deliverable", returned 7 lines: 2 in `.claude/skills/expedition-standing-yes/SKILL.md`, 1 in `.claude/skills/expedition/graph-conventions.md`, 3 in `.claude/skills/expedition/SKILL.md` and 1 in `.claude/skills/expedition/glossary.md`.~~ *(superseded by amendment 1 below)*
Re-run both searches before starting, because nodes 07 and 10 land first. Each instance either search finds outside the files named in this condition is reported, not edited.

1. `.claude/skills/expedition/graph-conventions.md`, the paragraph about `## Deliverables` under `## The seven files`, says that a deliverable's base is one of three things:
   - the upstream branch its pull request targets;
   - a local branch it is merged into, with no push and no pull request;
   - the name of another deliverable.
   The block of entry forms holds a third line, `- <name> · branch `<branch>` · base: local `<branch>``, beside the two forms already there. The paragraph's closing sentence says that `## Deliverables` in `SKILL.md` also says how a deliverable is merged locally.
2. `.claude/skills/expedition/glossary.md`, the entry **Deliverable**, says that a deliverable lands on its own branch and then either becomes its own pull request or is merged locally into a branch named in its map entry. The parenthesis in the **Handover** entry's `_Avoid_` line, which today says the word names a piece of work "that lands as its own pull request", says that it lands on its own branch. The **Standing yes** entry says that a standing yes counts as the human's yes both on a push of a deliverable's branch and on a local merge of a deliverable.
3. `.claude/skills/expedition/SKILL.md`, `### Declaring a deliverable`:
   - A deliverable is declared when the human brings a piece of work that is to land as its own pull request or by its own local merge.
   - The effort's landing policy may say which form of base a new deliverable takes by default. Where it says nothing, the deliverable takes an upstream base and lands by push and pull request, and the manager does not ask the human.
   - A deliverable whose base is another deliverable lands the way that deliverable lands.
   - The rule "never from the main checkout", with its reason that graph commits would reach the pull request, applies to a deliverable that lands by pull request. A deliverable with a local base has its branch created from the current tip of that local branch, even where the main checkout has that branch checked out.
4. `.claude/skills/expedition/SKILL.md`, `### Where a deliverable's code lands`: the closing passage says that the node's code reaches the main checkout's branch only when its deliverable lands. That is either through the upstream merge of its pull request, or through the local merge where the deliverable's base is the main checkout's branch. The numbered steps 1 to 5 are unchanged.
5. `.claude/skills/expedition/SKILL.md`, `### Pushing a deliverable's branch`, says that it applies to a deliverable that lands by pull request, and that a deliverable that lands locally is never pushed. Its other rules are unchanged.
6. `.claude/skills/expedition/SKILL.md`, `## Deliverables`, holds a new subsection, `### Merging a deliverable locally`, placed after `### Pushing a deliverable's branch`. It says all of the following:
   - It applies to a deliverable that lands locally.
   - The manager merges it only on the human's yes to that merge. The manager offers the merge when every implementation node naming the deliverable has resolved, and also whenever the human asks. The offer is the manager's own raise, under `## What is in front of the human, and when`. Every merge needs its own yes. A standing yes whose scope covers a merge counts as the human's yes to it.
   - By default, the manager rebases the deliverable's branch onto the current tip of its local branch, then moves the local branch to the deliverable branch's tip by fast-forward only.
   - A rebase that conflicts becomes an implementation node of the deliverable, and the deliverable's branch is left as it was before the rebase.
   - The effort's landing policy may name a merge commit or a squash in place of the default, and the human may name either in their yes to one merge.
   - A squash commit carries the `Node:` trailer of every commit it replaces.
   It names no tool beyond git, and it states the merge as properties rather than as declared commands.
7. `.claude/skills/expedition/SKILL.md`, `### A deliverable whose base is another deliverable`, says that when the base deliverable has merged locally, the dependent's base becomes the local branch the base merged into. The manager then changes the dependent's entry to `local <branch>` and rebases the dependent's branch onto that branch. The existing sentence about a base whose pull request merges upstream is kept.
8. `.claude/skills/expedition/SKILL.md`, `### Cleaning up a merged deliverable`, says two things. For a deliverable that lands by pull request, the manager learns that it merged only when the human says so. For a deliverable that lands locally, the manager made the merge itself, so it proposes the region cleanup right after the merge.
9. `.claude/skills/expedition/SKILL.md`, the passage under `## What is in front of the human, and when` that says "A push of a deliverable's branch is one such item", says that a local merge of a deliverable is one such item too.
10. `.claude/skills/expedition-cleanup/SKILL.md`:
    - Its `description` frontmatter says that the manager also proposes a region cleanup when a deliverable has merged locally.
    - `### A merged deliverable as the region` says that the cleanup is proposed when the human says a deliverable's pull request has merged, or right after the manager has merged a deliverable locally.
    - The sentence about the deliverables "that the human has said merged" covers both routes.
    - The step that deletes the local branch and leaves the remote branch says that a deliverable that landed locally has no remote branch.
    - The section's other rules, including how a node that names several deliverables is treated, are unchanged.
11. `.claude/skills/expedition-standing-yes/SKILL.md`, `## What a standing yes covers`, lists a local merge of a deliverable as an item a standing yes covers. The count of kinds in the sentence before the list matches the list. `## Taking a covered item` says that for a merge, the manager merges the deliverable as `### Merging a deliverable locally` in the `expedition` skill's `SKILL.md` says. A merge belongs to no node, so nothing is recorded on one. The manager names the merged branch in its next report to the human, and quotes the scope text of the standing yes that covered it.
12. `.claude/skills/expedition-upgrade/SKILL.md`, `### A branch that already exists`:
    - The sentence that says the entry "still names a base, which is the branch its pull request targets" says that the entry still names a base, in any of the three forms.
    - The check that the branch holds no commit of the effort's own record, with its reason that such a commit would reach the pull request, applies only to a deliverable that lands by pull request.
    - The check that the main checkout does not have the branch checked out still applies to every promoted branch.
13. Every heading of a file under `.claude/skills/` that this work renames is updated at every place under `.claude/skills/` that cites it by its exact text.
14. `.claude/rules/expedition-triggers.md` changes only where this work edits, in `.claude/skills/expedition/SKILL.md`, the governing statement of one of the manager's trigger-duties or of the priority that orders them. In that case it changes to match.

### Amendment 1 — by the manager, before the claim

The fact that justified it: re-running the condition's two recorded searches from the repository root on 2026-10-12 at commit `a40f9008e8`, after nodes 07 and 10 landed, as the condition says to. The results now read (counts for scale only, not authoritative):

- `grep -rn -i "pull request" .claude` returned 15 lines: 3 in `.claude/skills/expedition/glossary.md`, 2 in `.claude/skills/expedition-cleanup/SKILL.md`, 1 in `.claude/skills/expedition/graph-conventions.md`, 7 in `.claude/skills/expedition/SKILL.md` and 2 in `.claude/skills/expedition-upgrade/SKILL.md`.
- `grep -rn -i "push" .claude`, keeping the lines that also contain "deliverable", returned 9 lines: 3 in `.claude/skills/expedition-standing-yes/SKILL.md`, 1 in `.claude/skills/expedition/graph-conventions.md`, 4 in `.claude/skills/expedition/SKILL.md` and 1 in `.claude/skills/expedition/glossary.md`.

Every file the searches now find is already named in a clause of this condition, so the scope's list of files does not grow. This amendment records the new results and writes no new requirement.

*Manager's note, before the claim:* read everything after the condition. The passages the condition names are present at `a40f9008e8`: `### Declaring a deliverable`, `### Where a deliverable's code lands`, `### Pushing a deliverable's branch`, `### A deliverable whose base is another deliverable`, `### Cleaning up a merged deliverable`, "A push of a deliverable's branch is one such item", `### A merged deliverable as the region`, `## What a standing yes covers`, `## Taking a covered item`, and `### A branch that already exists`. Nodes 07 and 10 resolved, so both blockers are struck.

## Answer

The shipped skill files now support a third way to land a deliverable. A deliverable can take `base: local <branch>` and land by being merged locally into that branch, with no push and no pull request. The design is node 08's. This node wrote it into six files.
- `.claude/skills/expedition/graph-conventions.md`, `## The seven files`: the base can take three forms, given as a list, and the block of entry forms gains `- <name> · branch `<branch>` · base: local `<branch>``. The closing sentence now also points to `## Deliverables` in `SKILL.md` for how a deliverable is merged locally. The description of `## Landing an implementation node's work` gains one sentence: the landing policy may say which form of base a new deliverable takes by default, and how a deliverable is merged locally. No clause asked for that sentence. I added it so that this file agrees with the `SKILL.md` text that refers to the landing policy.
- `.claude/skills/expedition/glossary.md`:
  - **Deliverable**: the deliverable lands on its own branch, which then either becomes its own pull request or is merged locally into a branch named in its map entry. In its `_Avoid_` line, PR now reads "what a pushed deliverable becomes on the host".
  - **Handover** `_Avoid_`: the parenthesis now says the deliverable lands on its own branch.
  - **Standing yes**: it also counts as the human's yes to a local merge of a deliverable.
- `.claude/skills/expedition/SKILL.md`:
  - `### Declaring a deliverable`: a deliverable is declared for a piece of work that lands as its own pull request or by its own local merge. A three-item list says how a deliverable lands, following from its base. The landing policy may set the default form of base. Where the policy says nothing, the base is upstream and the manager does not ask the human. The rule "never from the main checkout" is limited to a deliverable that lands by pull request. A deliverable with a local base has its branch cut from that local branch's current tip.
  - `### Where a deliverable's code lands`: the closing passage says the code reaches the main checkout's branch only when its deliverable lands, either by the upstream merge of its pull request or by the local merge where the base is the main checkout's branch. Steps 1 to 5 are unchanged.
  - `### Pushing a deliverable's branch`: opens by saying it applies to a deliverable that lands by pull request, and that a deliverable that lands locally is never pushed.
  - New `### Merging a deliverable locally`:
    - The merge happens only on the human's yes. The manager offers it, as its own raise, once every implementation node naming the deliverable has resolved, and also whenever the human asks. Every merge needs its own yes. A standing yes whose scope covers the merge counts as that yes.
    - By default the merge is two moves. First, rebase the deliverable's branch onto the local branch's current tip. Second, move the local branch to the deliverable branch's tip, by fast-forward only. Where a checkout has the local branch checked out, the second move is made in that checkout so its files follow the branch. This last point is my own addition: moving a checked-out branch any other way leaves that checkout's files stale.
    - A rebase that conflicts becomes an implementation node of the deliverable, and the branch is left as it was before the rebase.
    - The landing policy, or the human's yes to one merge, may name a merge commit or a squash instead.
    - A squash commit carries the `Node:` trailer of every commit it replaces.
  - `### A deliverable whose base is another deliverable`: when the base deliverable has merged locally, the manager changes the dependent's entry to `local <branch>` and rebases the dependent's branch onto that branch. The existing sentence about a merge upstream is kept.
  - `### Cleaning up a merged deliverable`: for a deliverable that lands by pull request, the manager proposes the region cleanup when the human says it merged. For one that lands locally, it proposes the cleanup right after its own merge.
  - `## What is in front of the human, and when`: a local merge of a deliverable is now named as an item a standing yes can cover, beside the push.
- `.claude/skills/expedition-cleanup/SKILL.md`:
  - The description and `### A merged deliverable as the region` now name both moments for proposing the cleanup: the human says the pull request merged, or the manager has just merged the deliverable locally.
  - The sentence about deliverables "that the human has said merged" now covers both routes.
  - The branch-deletion step says a deliverable that landed locally has no remote branch.
  - The other rules are unchanged, including the rule for a node that names several deliverables.
- `.claude/skills/expedition-standing-yes/SKILL.md`:
  - The description and `## What a standing yes covers` now include the local merge, and the list has five kinds.
  - The closing line of `## What a standing yes never covers` reads "five kinds" and "other than the offer of a push or of a local merge".
  - `## Taking a covered item` has a new step 5. The manager merges as `### Merging a deliverable locally` in the `expedition` skill's `SKILL.md` says, records nothing on any node, names the merged branch in its next report, and quotes the scope text.
- `.claude/skills/expedition-upgrade/SKILL.md`, `### A branch that already exists`:
  - The entry still names a base "in any of the three forms" that `## The seven files` gives.
  - The check that the branch holds no commit of the effort's record applies only to a deliverable that lands by pull request.
  - The check that the main checkout does not have the branch checked out applies to every promoted branch. Its reason is now stated separately: the main checkout's graph commits would otherwise land on the branch. That reason is my wording of node 03's purpose for flag 03.6.
- `.claude/rules/expedition-triggers.md` is unchanged. No trigger-duty and no priority statement in `SKILL.md` changed. The only edit near them adds an example of a covered item to a passage that the trigger file's second duty already covers by pointing to `/expedition-standing-yes`.
- No heading was renamed. One heading was added.

*Manager's note:* landed as `14d17da066` on `master` by fast-forward, after the human's approval; the worktree and branch are removed. The worker's `NEW NODES` part is [node 13](13-fix-the-upgrade-skills-citations-of-its-own-subsection.md).

## Flags

`11.1` `ASSUMPTION` **· settled** — Amendment 1, by the manager before the claim: the re-run of the two recorded searches after nodes 07 and 10 landed found more lines, all in files the condition already names. The amendment records the new results and adds no requirement.

`11.2` `ASSUMPTION` **· settled** — Three small calls go beyond the clauses' literal text. Each was made so that a named file would not contradict itself.
(a) In `graph-conventions.md`, the landing policy's description now says the policy may set a deliverable's default form of base and how it is merged locally. `SKILL.md` now says the policy may say both.
(b) In `expedition-standing-yes`, the description and the closing line of `## What a standing yes never covers` now include the local merge. Otherwise the second would still exclude "every raise of your own other than the offer of a push".
(c) In the glossary's Deliverable `_Avoid_` line, PR now reads "what a pushed deliverable becomes on the host".
I also added one property to the merge: where a checkout has the local branch checked out, the fast-forward is made in that checkout so its files follow. A branch moved any other way leaves that checkout stale.

## Review

### Checker run 1 — `PASS`

The checker's entry, as it wrote it:

PASS

Acceptance condition. Each part was established from `git diff` in the worktree `/home/mathieu/projects/graph-agent/.scratch/rename-split-upgrade/worktrees/11-local-merge` against `a40f9008e8`, unwrapped. I also read `SKILL.md` lines 367-482 and 616-680 in full.

- Part 1, graph-conventions `## The seven files`: met. The paragraph lists the three base forms as bullets, the code block holds the third line `- <name> · branch `<branch>` · base: local `<branch>``, and the closing sentence ends "when its branch is pushed, and how it is merged locally".
- Part 2, glossary: met. **Deliverable** says "lands on its own branch. That branch then either becomes its own pull request, or is merged locally into a branch named in the deliverable's map entry". The Handover `_Avoid_` parenthesis now reads "lands on its own branch". **Standing yes** adds "On a local merge of a deliverable it counts as the human's yes to that merge".
- Part 3, `### Declaring a deliverable`: met. It says "own pull request or by its own local merge". The default when the landing policy is silent is an upstream base, landing by push and pull request, with "Do not ask the human which form to take". A deliverable based on another deliverable "lands the way that deliverable lands". The never-from-main-checkout rule is limited to a deliverable that lands by pull request. A deliverable with a local base is created from that local branch's tip "even where the main checkout has that branch checked out".
- Part 4, `### Where a deliverable's code lands`: met. The closing passage was rewritten as required. The diff hunk touches no line of steps 1-5.
- Part 5, `### Pushing a deliverable's branch`: met. Only the opening paragraph "This applies to a deliverable that lands by pull request. A deliverable that lands locally is never pushed." was added.
- Part 6, `### Merging a deliverable locally`: met. `grep -E '^[-+]#'` over the diff shows it is the only heading added, and it sits directly after Pushing. It states every required element: applies only to a local deliverable; the merge needs the human's yes; it is offered when all of the deliverable's implementation nodes have resolved or when the human asks; the offer is the manager's own raise; every merge needs its own yes; a standing yes covers it; the default is rebase then fast-forward only; a conflicting rebase becomes an implementation node and the branch is left as it was; a merge commit or squash can come from the landing policy or from the human's yes; a squash carries every `Node:` trailer. It names no tool beyond git and gives no commands.
- Part 7, `### A deliverable whose base is another deliverable`: met. The new paragraph sets the entry to `local <branch>` and rebases. The sentence about the upstream merge is kept.
- Part 8, `### Cleaning up a merged deliverable`: met. It has the two bullets: a pull-request deliverable only when the human says it merged, and a local deliverable right after the manager's own merge.
- Part 9: met. "A local merge of a deliverable is one such item too." was added after the push sentence under `## What is in front of the human, and when`.
- Part 10, expedition-cleanup: met. The description adds "or when the manager has merged a deliverable locally". The section lists the two moments. The sentence about merged deliverables now reads "has merged, by either route". The step that deletes the local branch adds "A deliverable that landed locally has no remote branch." The diff touches no other rule, including the one on a node naming several deliverables.
- Part 11, expedition-standing-yes: met. A fifth bullet was added and "four kinds" became "five kinds" in both places. `## Taking a covered item` gains step 5, which cites `### Merging a deliverable locally`, says nothing is recorded on a node, and has the manager name the merged branch and quote the scope text in its next report.
- Part 12, expedition-upgrade `### A branch that already exists`: met. The entry names a base "in any of the three forms". The no-record-commit check is limited to pull-request deliverables. The checked-out check applies to "every such branch".
- Part 13: met. The only heading change is the addition above, so no heading was renamed.
- Part 14: met. `.claude/rules/expedition-triggers.md` is unchanged (`git status`). The work edits no governing statement of a trigger-duty or of the priority. `## The order you act in` is untouched. The one edit under `## What is in front of the human, and when` adds an example of a covered item, and the trigger file's copy holds no such list.
- Scope: the diff touches exactly the six named files.

The searches the condition records. I ran both as written from the repository root (`/home/mathieu/projects/graph-agent`, HEAD `a40f9008e8`).
- `grep -rn -i "pull request" .claude` returned 15 lines, with the same per-file split as recorded (3/2/1/7/2).
- The "push" search kept to lines with "deliverable" returned 9 lines, also matching the recorded split (3/1/4/1).
- Both returns match what the condition records, and every hit is in a named file.
- Run inside the worktree after the work, every hit is still in a named file. Nothing outside the named files needs reporting.

The bar:
- The root `CLAUDE.md` `## Commands` says the repository has no build, no tests, no formatter and no CI. `git ls-files` confirmed it: only markdown files and `.gitignore`. That half of the bar holds vacuously.
- `git diff --check` came back clean.
- The only added lines over 106 characters are the two single-line frontmatter `description:` fields, which were already single long lines.

Standards. I read only the standards in `.scratch/rename-split-upgrade/map-implementation-rules.md`.
- These bore on the work: the glossary `_Avoid_` lines, `graph-conventions.md`, `/writing-for-agents` (read from the `mattpocock-skills` plugin in the nix store), and the root `CLAUDE.md` rules for writing.
- `/coding-principles` and `/naming` bore only lightly, since the work is prose.
- I searched the added lines for the distinctive refused words (PR, feature, retry, subtask, kill, cancel, escalate, auto-approve, review, iteration, task, plan, ticket, issue, session, run, done, complete, finished, summary, and line-number citations). The only hits were "finished" and "done", both in unchanged wording carried inside rewrapped lines.
- Every heading the new text cites exists: `## The seven files`, `## Taking a covered item`, `### A merged deliverable as the region`, `### Change the map`, `### Merging a deliverable locally`.
- Each prohibition sits beside a positive statement. For example, "Do not ask the human…" follows "give the deliverable an upstream base".

The work also changed two of the standards:
- The glossary `_Avoid_` edits change only the reason text in parentheses (Handover, and Deliverable's "pushed deliverable"). The refused words themselves did not move.
- The graph-conventions edit only adds an element, the local base form, which I held against part 1.
- I settled this before checking anything else. Nothing this work must be held against was removed or altered.

No reviewing skill is named in the standards, so I ran none. I spawned no agent.

Process note: while locating the writing-for-agents skill, a failed `find` made `ls` list the file names in the effort directory (`decisions.md`, `flags.md`, `map-history.md`, `map-manager-only.md`, `map.md`, `nodes`, `worktrees`). I opened none of them.

Flags. I checked them after reaching the outcome, and both are true of the work.
- 11.1: the re-run searches at `a40f9008e8` return only lines in named files.
- 11.2: all four claimed edits are present:
  - The landing-policy bullet in graph-conventions adds "It may also say which form of base a new deliverable takes by default, and how a deliverable is merged locally."
  - The standing-yes exclusion line reads "other than the offer of a push or of a local merge".
  - The glossary Deliverable `_Avoid_` reads "PR (the pull request is what a pushed deliverable becomes on the host)".
  - Merge step 2 reads "Where a checkout has the local branch checked out, make the move in that checkout".

No questions. Nothing is uncovered. I wrote no file and changed nothing.

### Gate outcome — approve

The human's words, `verbatim`:

> approve

## Annotation: node 15 renames a heading this node cites

As the worker of [node 15](15-whether-flags-md-is-dropped.md) reported it: 11: a rename. Its `## Acceptance condition` and `## Answer` cite `## The seven files`.
