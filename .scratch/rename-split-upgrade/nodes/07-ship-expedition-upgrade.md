# Ship `/expedition-upgrade`

Type: implementation
Status: resolved
Labels: UPGRADE
Blocked by: ~~05~~

## Question

This lets the human turn a conversation that was not started as an expedition into one. The conversation's own thread becomes the manager, and the work done so far, decided or still open, is carried into an effort's record. Write the `expedition-upgrade` skill and point to it from the manager contract's `## Starting an effort`.

*Manager's note:* minted by the worker of [node 03](03-upgrade-a-conversation-into-an-expedition.md) on its `NEW NODES` part, with the question and condition below as it wrote them.

## Acceptance condition

Scope: this work names its places rather than fixing instances of a defect, so its scope came from no search. The files it may change are `.claude/skills/expedition-upgrade/SKILL.md`, which it creates, and `.claude/skills/expedition/SKILL.md`. It changes `.claude/rules/expedition-triggers.md` only as clause 12 allows. Any other file found to need a change is reported, not edited.

1. `.claude/skills/expedition-upgrade/SKILL.md` exists. Its frontmatter has `name: expedition-upgrade` and a `description` saying that the human invokes it, with a request, in a conversation that was not started as an expedition, to turn that conversation into an expedition whose manager is the conversation's own thread.
2. The skill tells the thread to read the manager contract, the `expedition` skill's `SKILL.md`, and to act as the manager from then on. It says that from the upgrade on, the thread does no node's work itself.
3. The skill says that the request given with the invocation names the destination, the deliverables, and either a new effort or an existing effort by name. It says that where the request leaves the destination, whether the effort is expected to reach it, or the deliverables unstated, the manager asks the human for them and does not write them itself.
4. For a new effort, the skill says that the effort is started as the manager contract's `## Starting an effort` describes, with the conversation as its starting point. For an existing effort, it says that the upgrade adds the deliverables and nodes to that effort, and that each new node takes the next unused node number. It says that only one thread manages an effort at a time, and that the human ends any other manager session on that effort with `/expedition-stop` before invoking the upgrade.
~~5. The skill says that commits made before the upgrade stay as they are and are linked to no node. It says that a branch that already exists may be declared as a deliverable's branch, in place of creating a new branch from the deliverable's base. It names the rule it changes for this case by its heading in the file that states it, and states the change in its own words.~~ *(superseded by the amendment below)*
6. The skill says that background agents still running in the conversation finish before the upgrade starts, and that what they return counts as part of the conversation.
7. The skill says what is carried into the record:
   - The decisions already made in the conversation go into one resolved node, or into a few where the conversation did several unrelated things. The human's words are its answer. Where the human assented to a recommendation of the agent, the recommendation is kept beside the assent.
   - The questions still open become grilling nodes, grouped as grilling nodes usually are, with no limit of one question per node.
   - Each choice the agent made without the human's agreement becomes an `ASSUMPTION` flag, and is not recorded as the human's decision.
   - Findings that exist only in the conversation and took real effort to obtain go into one file in the effort's directory. That file is linked from the map's `## Notes` and marked as the agent's work.
   - The conversation's chronology, and facts that can be read again from the working tree, are not carried.
   - The record is written so that the effort needs nothing from the conversation once the upgrade is done.
8. The skill says that the manager checks whether the environment keeps a full transcript of the conversation, and does not assume that it does. Where one exists, a worker on a `precondition` node reads it, the manager does not, and that worker takes out the human's words and the decisions of clause 7, marked `verbatim` with the transcript cited as their source. Where none exists, the existing rule for recording words no longer in context applies. The skill names the rule it changes, `### The human's words` in the manager contract, and states the change in its own words. It names no tool-specific path or file format.
9. The skill says that uncommitted changes in the conversation's working tree move into the worktree of a new implementation node, which names a deliverable. That deliverable is the one the request ties the work to, and the manager asks the human where it is unclear. The manager writes that node's acceptance condition, which covers the whole change, including the part written before the upgrade. The change goes through the checker and the gate like any other implementation node's work. Planned work that was not started becomes open nodes.
10. The skill gives no procedure for deciding how the work is split into nodes beyond the grouping of clause 7. It leaves that split to the manager's reading of the conversation.
11. `.claude/skills/expedition/SKILL.md`'s `## Starting an effort` gains a pointer to the `expedition-upgrade` skill, for a conversation that already holds work. The pointer sits beside the existing sentence pointing to `adoption.md`. It says in one clause at most what the reader goes there for. The statement that the two ways of starting differ only in their starting point stays true. No glossary term is added for the upgrade.
12. `.claude/rules/expedition-triggers.md` changes only where this work edits, in `.claude/skills/expedition/SKILL.md`, the governing statement of one of the manager's trigger-duties or of the priority that orders them. In that case it changes to match.
13. Every heading of a file under `.claude/skills/` that this work renames is updated at every place under `.claude/skills/` that cites it by its exact text.

### Amendment 1, to clause 5 — by the worker of node 03, filed by the manager

What fixed the words, as that worker wrote it: the human's answer on node 03, verbatim *"a existing branch can be promoted to a deliverable"*, and node 02's resolved answer, which says the main checkout's graph commits must not reach the pull request. The fact behind it: node 05's text, read in its worktree, puts the rule under `### Declaring a deliverable` in `.claude/skills/expedition/SKILL.md`: create the branch "from the current tip of its base", "never from the main checkout, because the main checkout holds graph commits, and they would reach the pull request".

Clause 5 now reads:

5. The skill says that commits made before the upgrade stay as they are and are linked to no node. It says that a branch that already exists may be declared as a deliverable's branch, in place of a branch created from the deliverable's base. The deliverable's entry still names a base, which is the branch its pull request targets. The skill names the rule it changes for this case, `### Declaring a deliverable` in the `expedition` skill's `SKILL.md`, and states the change in its own words. It says that a promoted branch holds no commit of the effort's own record, and that the main checkout does not have the branch checked out once the upgrade is done, because a commit of the effort's record would otherwise reach the pull request. Where either of these does not hold, the manager asks the human what to do and changes neither the branch nor the checkout itself.

*Manager's note:* `### Declaring a deliverable` is node 05's uncommitted text, under check. Before node 07 is claimed, the manager searches the landed tree for that heading.

## Answer

Shipped the skill `.claude/skills/expedition-upgrade/SKILL.md` and a pointer to it in `.claude/skills/expedition/SKILL.md`'s `## Starting an effort`.

The skill's frontmatter has `name: expedition-upgrade` and a description saying that the human invokes it, with a request, in a conversation not started as an expedition, to make the conversation's own thread its manager. It sets no `disable-model-invocation`, which matches the sibling skills `expedition-stop` and `expedition-standing-yes`. The body has these parts, in this order:
- An opening: read the manager contract, act as manager from then on, and do no node's work yourself from the upgrade on.
- `## What the request names`: the destination, the deliverables, and a new or a named existing effort. Where one of these is unstated, ask the human and write none of it yourself.
- `## Your steps, in order`, six steps:
  1. Let running background agents finish. What they return counts as part of the conversation.
  2. Start a new effort as `## Starting an effort` describes. For an existing effort, add to it, with the next unused node numbers, after the human has ended any other management session on it with `/expedition-stop`.
  3. Declare the deliverables.
  4. Carry the conversation into the record.
  5. Carry the work already done or under way.
  6. Check each existing branch declared as a deliverable's branch.
  It ends with the completion statement: write the record so that the effort needs nothing from the conversation once the upgrade is done.
- `## What is carried into the record`, with the rules of node 03's Q2 answer:
  - Past decisions go into one resolved `grilling` node, or into a few. Their answer is the human's words, with the agent's recommendation kept beside an assent.
  - Open questions become grilling nodes.
  - Unagreed choices become `ASSUMPTION` flags.
  - Costly findings go into one file linked from `## Notes` and marked as the agent's work.
  - Chronology and facts that can be read again from the tree are left out.
  - The split into nodes is left to the manager's reading of the conversation.
- Its subsection `### The human's words, where the conversation was compacted`. The manager checks for a transcript and does not assume one. Where one exists, a `precondition` worker reads it and extracts the words and decisions, marked `verbatim` and citing the transcript. The manager then writes the decision nodes from that worker's handover. The subsection names `### The human's words` as the rule it changes. Where there is no transcript, that rule applies unchanged. No tool path or file format is named.
- `## Work already done or under way`, in four parts:
  - Commits made before the upgrade stay as they are, linked to no node.
  - `### A branch that already exists`: such a branch may be declared as a deliverable's branch, and the entry still names a base, which is the branch its pull request targets. This names `### Declaring a deliverable` as the rule it changes. After the rest of the upgrade, the manager checks that the branch holds no commit of the effort's record and is not checked out in the main checkout. Where either fails, the manager asks the human and changes neither the branch nor the checkout.
  - Uncommitted changes outside the effort's record move into the worktree of a new implementation node. That node names the deliverable the request ties the work to, and the manager asks where this is unclear. The manager writes the node's condition, which covers the whole change, and the change goes through the checker and the gate.
  - Planned work that was not started becomes open nodes.

The pointer added after the `adoption.md` sentence in `## Starting an effort` reads: "Where the conversation already holds work, the skill `expedition-upgrade` adds the steps that carry that work into the effort." The upgrade still takes a conversation as its input, so the statement that the ways of starting differ only in their input stays true. No glossary term was added. No trigger-duty statement and no heading was changed, so `.claude/rules/expedition-triggers.md` is untouched.

*Manager's note:* landed as `9c0083ffbd` on `master` by fast-forward, after the human's approval; the worktree and branch are removed.

## Flags

`07.1` `ASSUMPTION` **· settled** — Amendment 1 to clause 5, written by the worker of node 03 after its handover and filed by the manager under `### Changing one after it is written`. The worker handed no flag sentence for the amendment itself; its own judgement behind the amendment is flag `03.6` on node 03.

*Manager's note, before the claim:* read everything after the condition: amendment 1 and its flag `07.1`. Searched the landed tree on 2026-10-12: `### Declaring a deliverable` is at `.claude/skills/expedition/SKILL.md`, landed by node 05 as `7a86d138e0`; `## Starting an effort` and its sentence pointing to `adoption.md` are present; `### The human's words` is present. Node 05 resolved, so the blocker is struck.

`07.2` `ASSUMPTION` **· settled** — The node or nodes of decisions already made have the kind `grilling`, written as resolved. Node 03 said "one resolved node" but gave no kind, and every node file needs a `Type:`. Grilling is the kind for a decision only the human can make, which is what these nodes hold.

`07.3` `ASSUMPTION` **· settled** — Where a transcript exists, the `precondition` worker hands back the extracted words and decisions, and the manager writes the decision nodes from that handover as scribe. The worker does not write those node files itself. Answers and statuses are the manager's under the contracts, and clause 8 only says that the worker "takes out" the words.

`07.4` `ASSUMPTION` **· settled** — An `ASSUMPTION` flag for a choice the conversation's agent made is written by the upgrading thread, which made the choice, and placed on the decision node it bears on. This is the manager filing a flag about its own conduct, which the manager contract lists as unsettled in `## What nothing here settles`, item 2. Clause 7 requires the flag, and no other party could write it.

`07.5` `ASSUMPTION` **· settled** — The check of an existing branch declared as a deliverable's branch is placed after the rest of the upgrade, matching the condition's "once the upgrade is done". The rule to change neither the branch nor the checkout therefore does not clash with moving uncommitted changes out of the working tree. Only changes "outside the effort's own record" move, because in an existing effort the main checkout's uncommitted changes may be graph files.

## Review

### Checker run 1 — `PASS`

The checker's entry, as it wrote it:

PASS

Work: uncommitted changes in /home/mathieu/projects/graph-agent/.scratch/rename-split-upgrade/worktrees/07-ship-expedition-upgrade. `git status --short` shows only `M .claude/skills/expedition/SKILL.md` and `?? .claude/skills/expedition-upgrade/`, so the change stays inside the condition's scope. Every search below was run over the unwrapped text of `.claude/skills/expedition-upgrade/SKILL.md` (written "U" below) and of `git diff` on `.claude/skills/expedition/SKILL.md`.

Condition, part by part:
- Scope: `git status --short` and `git diff HEAD --stat` show only the two permitted paths. `.claude/rules/` is unchanged.
- 1: U's frontmatter has `name: expedition-upgrade`. Its description says "The human invokes it, with a request, in a conversation that was not started as an expedition, to turn that conversation into an expedition whose manager is the conversation's own thread."
- 2: U says "Read the manager contract now. It is the `SKILL.md` of the skill `expedition`. Act as the manager from then on. From the upgrade on, do no node's work yourself."
- 3: U's `## What the request names` lists the destination, the deliverables, and a new effort or an existing effort named by its name. It covers asking about the destination, the expectation of reaching it and the deliverables where they are unstated, and says "Write none of these three yourself."
- 4: U's step 2 covers both cases. A new effort is started as `## Starting an effort` describes, with the conversation as its starting point. For an existing effort, the deliverables and nodes are added and each new node takes the "next unused node number". U also says "Only one thread manages an effort at a time" and that the human uses `/expedition-stop` before invoking the upgrade.
- 5 (amended text): U's `### Commits made before the upgrade` says they "stay as they are. No node is linked to them." U's `### A branch that already exists` covers the rest:
  - a branch that already exists takes the place of a branch created from the base;
  - the entry "still names a base, which is the branch its pull request targets";
  - it names `### Declaring a deliverable` in the manager contract and states the change in its own words;
  - it gives the two checks (no commit of the effort's own record, and not checked out in the main checkout) with the reason ("a commit of the effort's record would otherwise reach the pull request");
  - it says to ask the human and to "Change neither the branch nor the checkout yourself."
- 6: U's step 1 says background agents finish before the upgrade starts, and "What they return counts as part of the conversation."
- 7: U's `## What is carried into the record` covers each item:
  - decided matters go into one resolved grilling node, or a few for unrelated things;
  - the human's words are the answer, and the recommendation is kept beside the assent;
  - open questions become grilling nodes, grouped as usual, with "A node may hold more than one question";
  - each choice made without the human's agreement becomes an ASSUMPTION flag, "never as the human's decision";
  - findings go into one file in the effort's directory, linked from the map's `## Notes` and marked as the agent's own work;
  - chronology and facts that can be read again from the working tree are left out;
  - U says "Write the record so that the effort needs nothing from the conversation once the upgrade is done."
- 8: U's `### The human's words, where the conversation was compacted` covers each item:
  - it says to check for a transcript and not to assume one exists;
  - where one exists, the precondition worker reads it and the manager does not, and the extracted words and decisions are marked `verbatim` with the transcript cited;
  - where none exists, the existing rule applies unchanged;
  - it names `### The human's words` and states the change.
  - A grep of U for `.jsonl`, `~/`, `.claude/projects`, `Claude Code` and `/tmp` found nothing, so U names no tool-specific path or file format.
- 9: U's `### Uncommitted changes` covers each item:
  - the changes move into the worktree of a new implementation node, which names the deliverable the request ties the work to;
  - the manager asks the human where that deliverable is unclear;
  - the manager writes the condition, which covers the whole change "including the part written before the upgrade";
  - the change goes through the checker and the gate.
  - U's `### Planned work` turns work that was planned and not started into open nodes.
- 10: The only text in U about splitting is "How the rest of the work splits into nodes is yours to read from the conversation." Reading U through found no other procedure for it.
- 11: The diff adds one sentence right after the `adoption.md` sentence in `## Starting an effort`. It says what the reader goes there for in one clause: "adds the steps that carry that work into the effort". The input is still a conversation, so "they differ only in their input" stays true. `glossary.md` is unchanged.
- 12: The only edit to the manager contract is in `## Starting an effort`, which is not a trigger-duty statement. A grep of `.claude/rules/expedition-triggers.md` for "starting an effort" or "adoption" found nothing, and that file is unchanged.
- 13: The diff renames no heading.

Bar:
- `## Commands` in the root `CLAUDE.md` says the repository has no build, no tests, no formatter and no CI. `git ls-files` confirms this: the tracked files hold no build or test configuration, and the only script, `scripts/frontier.sh`, is untouched.
- `git diff --check` and a trailing-whitespace grep on U printed nothing.
- No line of U is over 105 characters except the frontmatter `description`, which is a single line as in the other skill files.

Standards: I read only the standards in `.scratch/rename-split-upgrade/map-implementation-rules.md`. Four bore on this work:
- The `_Avoid_` lines of the glossary. I grepped U for the refused words. The only hits are ordinary-English uses: "return" (in clause 6's own wording), "done", "management session" (already used in the manager contract), and "working tree". None of them names the refused concept.
- The `CLAUDE.md` rules for writing:
  - Every citation is by heading.
  - The headings U cites (`## Starting an effort`, `### Declaring a deliverable`, `### The human's words`, `## Acceptance conditions`) all exist in the manager contract.
  - Each prohibition sits beside a positive instruction.
  - The bold in U is on step and list labels, which matches the sibling `adoption.md`.
- `/writing-for-agents`: I applied it by hand and found no breach.
- The trigger-file rule: it does not apply (see part 12).

`/coding-principles`, `/naming` and `graph-conventions.md` were not relevant to this prose beyond the node kinds and flag names, which U uses as defined. No reviewing skill is named by the standards, and none was run.

Flags, checked after the outcome:
- 07.1 makes no claim the work can make true or false.
- 07.2, 07.3, 07.4 and 07.5 are true of the work:
  - 07.2: U says "one `grilling` node, written as resolved".
  - 07.3: U says "Write the nodes of decisions already made from what that worker hands back".
  - 07.4: U says "Record it as your own choice".
  - 07.5: U says "outside the effort's own record". Its step 6 and the words "Once the rest of the upgrade is done" put the branch check after the rest of the upgrade.

I wrote no file.

### Gate outcome — approve

The human's words, `verbatim`:

> approve

## Annotation: node 11 narrows the promoted-branch rules

As the worker of [node 11](11-ship-the-local-merge-of-a-deliverable.md) reported it: Node 07: a narrowing. In `### A branch that already exists`, the base may take any of the three forms. The check against commits of the record applies only to a deliverable that lands by pull request. The checkout check keeps its scope, and its reason is now given on its own.
