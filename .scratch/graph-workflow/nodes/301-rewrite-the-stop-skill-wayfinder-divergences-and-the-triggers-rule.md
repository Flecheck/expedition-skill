# Rewrite the stop skill, `wayfinder-divergences.md` and the triggers rule in plain English

Type: implementation
Status: resolved
Blocked by: 290, 298

## Question

Rewrite `.claude/skills/expedition-stop/SKILL.md`, `.claude/skills/expedition/wayfinder-divergences.md` and `.claude/rules/expedition-triggers.md` in plain English and shorter, under the pass [node 289](289-a-plain-english-and-compaction-pass-over-the-shipped-files.md) settled.

> Beside the work, the handover carries three things. (1) For every open node whose `## Acceptance condition` quotes text or a heading from the before-text of what this node rewrites: either a replacement for each affected clause, quoting the after-text, or a proposal that the node be superseded as unnecessary, with the reason. Name the search you ran. (2) Every generalisation made, naming the statements it replaced. (3) Any rule judged dead or a default behaviour, reported as a new node and left in the text.

## Acceptance condition

*Authored by node 289's worker and filed by the manager. Node 289's worker's COMMON CLAUSES block, copied in full, then this node's own clauses, verbatim. COMMON CLAUSES apply to each of the three files separately.*

**Terms.** *The before-text* of a file is that file as it stands at the commit this work's branch was created from, read with `git show $(git merge-base HEAD master):<path>` in the worktree. *The after-text* is the file in the worktree. *The rewritten range* is the part of the file this condition's own clauses name, or the whole file where they name no part.

1. **Nothing binding is lost.** Every binding statement in the before-text has a counterpart somewhere in the whole after-text that gives the same outcome in every case. The binding statements are: every rule, meaning every instruction, permission, prohibition or duty, and whose it is; every condition or exception attached to a rule; every fixed template; every term the text defines, and its definition; every word the text refuses; and the members and stated count of every closed list. A binding statement with no counterpart, or whose counterpart changes the outcome for any case, fails this clause.
2. **Nothing binding is added.** The after-text states no rule, permission, duty, exception, defined term or refused word that the before-text does not.
3. **Generalisation.** Several before-text statements may be replaced by one general statement only where every case each of them decided comes out the same under it, and it decides no case the before-text left undecided.
4. **Fixed text.** Everything inside code fences, and the frontmatter block at the top of the file where there is one, is byte-identical to the before-text.
5. **Headings.** A heading of the before-text whose exact text appears in any other of the following files keeps that exact text in the after-text: `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/graph-conventions.md`, `.claude/skills/expedition/wayfinder-divergences.md`, `.claude/skills/expedition-checker/SKILL.md`, `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-stop/SKILL.md`, `CONTEXT.md`, `.claude/rules/expedition-triggers.md`, `.scratch/graph-workflow/map.md`, `.scratch/graph-workflow/map-manager-only.md`, `.scratch/graph-workflow/map-implementation-rules.md`, `.gitignore`. Any other heading may be reworded, merged or removed, provided clause 1 holds.
6. **References inside the file.** Every reference the after-text makes to another part of the same file, such as "below", "above" or "under *X*", points at something the after-text holds.
7. **Terms.** Where the before-text uses a term defined in `CONTEXT.md`, the after-text spells that term as `CONTEXT.md` defines it wherever the idea recurs. The after-text uses no word that a `CONTEXT.md` `_Avoid_` line refuses, for the concept that line refuses it for, and coins no new term.
8. **Plain English.** Within the rewritten range, prose outside code fences has these six properties. The checker names each passage it judges to breach one, and which property it breaches.
   a. A rule is stated as what to do. A prohibition appears only where the rule cannot be stated as what to do, and then beside the positive statement.
   b. Bold appears only on a term at the place where it is defined. No clause or sentence is bolded for emphasis.
   c. An idea that is not a term defined in `CONTEXT.md` is said in plain words, with no figure of speech and no coined phrase. The following, from the shipped files, are the kind ruled out: "neither pen reaches", "rides a moment that already exists", "claimants", "in as many words".
   d. Statements are direct. No sentence is a slogan-shaped contrast or reversal, of the kind "the ban is about recording, not about files" or "amending is never authoring". No sentence uses "the whole of what".
   e. Every sentence is grammatical, and each "it", "this", "that", "they", "these" or "those" has one clear referent in the same sentence or the one before. The following is the kind ruled out: "Two things that is not, and neither is loosened by it."
   f. One idea per sentence. No sentence holds more than one dash-delimited aside, or more than one semicolon.
9. **Size, reported and not enforced.** The checker reports the `wc -w` count of the rewritten range in the before-text and in the after-text. The target is an after-text of at most two thirds of the before-text. Missing the target does not fail the work.
10. **Scope.** The work changes no path except those this condition's own clauses name, and within a named file, no text outside the rewritten range: that text is byte-identical to the before-text.

11. **Scope.** The work changes `.claude/skills/expedition-stop/SKILL.md`, `.claude/skills/expedition/wayfinder-divergences.md` and `.claude/rules/expedition-triggers.md`, and no other path. The rewritten range is the whole of each file.
12. **The human's own sentences.** In `.claude/rules/expedition-triggers.md`, these two sentences keep their meaning. Only their grammar may change: "if the human has nothing to do and there is a question/gate, give it to him. Wait for him to answer before giving him a question." and "The instruction on how to behave and how to use the map are in the skill `/expedition` and next to it `graph-conventions.md`".
13. **The triggers file stays a copy.** Every duty and every priority item that `.claude/rules/expedition-triggers.md` states is also stated, with the same outcome, in `.claude/skills/expedition/SKILL.md` as it stands in the worktree, and the triggers file adds none that `SKILL.md` lacks.

## Amendment by the human, 2026-09-24

*The human approved the manager's proposal, `verbatim`: "ok". The proposal and the answer to A that prompted it are recorded on [node 290](290-rewrite-the-research-contract-as-the-pilot.md). The manager drafted the wording below, and the human amended the condition with it. The original clauses above are left as they were. The clauses below take the place of clauses 1 and 2, add clause 1a, and add a sentence to clause 3.*

1. **Lost or changed statements are rule changes.** The binding statements are: every rule, meaning every instruction, permission, prohibition or duty, and whose it is; every condition or exception attached to a rule; every fixed template; every term the text defines, and its definition; every word the text refuses; and the members and stated count of every closed list. A binding statement of the before-text that has no counterpart anywhere in the whole after-text, or whose counterpart changes the outcome for any case, is a rule change. The checker lists every rule change it finds, each with the before-text statement and its after-text counterpart, or "removed". A rule change does not fail the work.
1a. **Terms `CONTEXT.md` does not define.** A term the before-text defines that `CONTEXT.md` does not define may be dropped as a term, where its meaning is still stated in plain words at the place it was defined. Dropping a term that way is not a rule change.
2. **Added statements are rule changes.** A rule, permission, duty, exception, defined term or refused word that the after-text states and the before-text does not is a rule change. The checker lists it the same way as under clause 1. It does not fail the work.
3. *(added sentence)* A generalisation that changes an outcome, or decides a case the before-text left undecided, is a rule change under clause 1 or clause 2.

## Answer

The stop skill, `wayfinder-divergences.md` and the triggers rule are rewritten in plain English with every rule kept; "claimants" and a partly false "tier 1" claim are removed, and no open condition needed re-pointing.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1, finding one rule change, the worker's own rule change 1. The human approved. The work landed as commit `02bdd3b`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-25. The worker's own text, pasted. The flags are raised under `## Flags` at the gate.*

HANDOVER:      Rewrite the stop skill, `wayfinder-divergences.md` and the triggers rule in plain English

ANSWER:
I rewrote all three files in plain English, in the worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/301-rewrite-the-stop-skill-divergences-and-triggers`. Nothing is committed.

- `.claude/skills/expedition-stop/SKILL.md`
  - The body is rewritten. The frontmatter is byte-identical.
  - Four headings are renamed. No other listed file uses them, so clause 5 does not protect them:
    - "Start no new node" → "New work stops"
    - "Finish the work in flight" → "Finish the work already under way"
    - "Write no handoff document" → "What the next manager starts from"
    - "What does not survive, and why it costs nothing" → "Agents still running when the session ends"
  - "Claimants" is gone.
  - "In flight" is gone from the prose. It stays in the fixed frontmatter description.
  - Every citation of a manager-contract heading now carries its exact `##`/`###` text, and every such heading exists in `.claude/skills/expedition/SKILL.md`.
- `.claude/skills/expedition/wayfinder-divergences.md`
  - The prose is rewritten.
  - The heading "Read differently" is now "Changed".
  - The two lists are unchanged.
  - The fenced block is byte-identical.
- `.claude/rules/expedition-triggers.md`
  - Frontmatter is byte-identical.
  - The three triggers are now imperative sentences.
  - The priority list is numbered 1 to 5 and worded to match `SKILL.md`'s `## The order you act in`.
  - Only the grammar of the human's two sentences changed: "question/gate" became "question or a gate", and "The instruction … are … and next to it `graph-conventions.md`" became "The instructions … are … and, next to it, in `graph-conventions.md`." I kept them unwrapped, as the human wrote them.
  - Clause 13: every trigger and priority item is stated in `SKILL.md` with the same outcome. The triggers file adds no duty that `SKILL.md` lacks.

Calls a later reader would otherwise have to re-derive:
- **Contradiction left in place.** The stop skill still says that three node states can be worked out from the node's own file. The manager contract's `### Three states nothing in the files shows` still says they cannot. Node 314 settles this. The after-text keeps the before-text's three derivations word for word, which is also the wording node 314's condition asks the manager contract to take.
- **Words kept on purpose.**
  - "session" is used for the manager thread's life, not for an effort or an attempt. The file defines it as "the life of your own thread".
  - "ticket" means wayfinder's own tickets.
  - "ask him which to take" is the manager asking the human, not a worker's raise.
  - "never asked … twice" is about the human.
  - None of these is a refused use under `CONTEXT.md`.
- **Headings.** No before-text heading of the three files appears in any file clause 5 lists, so all were free to change.

Size (`wc -w`, before → after):
| file | before | after | two-thirds target |
| --- | --- | --- | --- |
| stop skill | 585 | 567 | 390 |
| divergences | 330 | 330 | 220 |
| triggers | 364 | 370 | 243 |

All three miss the soft target. The before-texts were already short. Plain English splits the dash-and-semicolon sentences into several sentences. In the divergences file, the fenced block and the two lists are fixed and make up most of the words.

Bar: the repo has no build, tests, formatter or CI. I checked: no manifest or task runner, which matches the record in `map-implementation-rules.md`. `git diff --check` is clean.

RULE CHANGES:

*Stop skill*
1. Before: "Both are already tier 1 claimants in your contract's `What is in front of the human, and when`". After: removed. The next sentence still says that section governs how each thing is put to the human. Why it makes sense: in this file the claim decided nothing, because that section decides the tier. It was also wrong in part: a worker's relayed interview question is tier 2, not tier 1. And it held the refused coinage "claimants".
2. Before: "All a session ending adds is that none of them is left over." After: merged. The paragraph's first sentence says "Put the work that needs the human in front of them before the session ends", and the sections are said to govern "as they always do". Borderline: I believe no outcome changes. Also listed under generalisations.
3. Before: "The effort is not being closed: only the human closes one, and nothing here does that." After: "Leave the effort open, because only the human closes an effort." Borderline: a statement of fact became an instruction to the manager. The outcome is the same.
4. Before: "a handover that has arrived is filed, the node it answers is resolved on it". After: "File a handover that has arrived, and resolve the node it answers." Borderline: the qualifier "on it" is gone. Resolving the node the handover answers already means writing that handover's answer onto it.
5. Before: "…so a handoff document would only copy it." After: the reason is cut. "Write no handoff document. Leave the next manager the record, which already holds everything a fresh manager needs." Borderline: this is an explanation of why, which the pass may cut. The rule is kept.
6. Before: "this session — your own thread's life, not the effort —". After: "A session is the life of your own thread." The "not the effort" contrast is now carried by "Leave the effort open". Borderline, same outcome.

*Divergences file*
7. Before: "A repo with no such doc needs nothing from this file." After: "This file is only for a repo whose tracker doc already describes…". Borderline, same outcome.
8. Before: "nothing in that doc has to be rewritten or removed". After: "No other part of that doc needs to be rewritten or removed." Borderline: "other" excludes the appended block, which the before-text also did not count as a rewrite.

*Triggers file*
9. Before: "and it overrides nothing there". After: "Where this file and the map differ, follow the map." The prohibition became its positive form. Borderline: when the two conflict, the map prevails in both.
10. Before: "this file is the copy that survives a compaction". After: "this copy stays in context after a compaction". Borderline: the figure became literal words.
11. Before: "Every duty here is a manager's own, and a worker reading them acts on none of them." After: "…so a worker reading this file acts on none of them." Borderline: "them" (the duties) became "this file". Same outcome.

No other before-text rule, condition, template, defined term, refused word or closed-list count changed. All the closed lists keep their members and counts:
- the three things that happen
- the two cases
- the three states
- the four parts of the closing report, and the three things outstanding for the human
- the divergences file's two lists of five and its five changes
- the three triggers
- the five priority items
- the four things that must not be waiting

RE-POINTING SEARCH:
- **Script.** I used node 293's script, adapted and kept as `$TMPDIR/n301/s301.py`, with before and after text in `$TMPDIR/n301/`.
- **Scope.** It covered the `## Acceptance condition…` and `## Amendment…` sections of the 87 open and claimed nodes, excluding 301. It ran in three modes:
  - quoted spans of the joined before-texts, 12 characters or longer, checked for whether they survive
  - 6-word n-grams
  - a list of phrases
- **Handles searched:**
  - the three paths; "stop skill", "triggers rule", "triggers file"
  - every before-text heading: Closing a management session; Start no new node; Finish the work in flight; Write no handoff document; What does not survive; why it costs nothing; The session's closing report; Differences from a wayfinder tracker; Read differently; Not covered here; Triggers a manager acts on; Where every other rule lives; Priority; Unchanged; Added
  - the removed or replaced phrases: claimants; tier 1 claimants; top up; in flight; handoff; derivable; read as an ordinary node; survives a compaction; overrides nothing; a check rather than an act; Waiting is the state; the one duty it fires; respecting the limits; Five things; nothing in that doc has to be rewritten; needs nothing from this file; unresumable; routes you to
- **Matches:**
  - 105, 118, 127 ("claimants", "top up", "in flight"): all quote `.claude/skills/expedition/SKILL.md`, not these files. No replacement needed from this node.
  - 97 (a pointer "to the closing section of `wayfinder-divergences.md`"): the closing section is still `## Not covered here`. The clause still holds, and no replacement is needed.
  - 226 (names `.claude/rules/expedition-triggers.md`, requires a record statement that the file "overrides nothing in the map", and requires the file to stay byte-identical during 226's own work): the property is still true, since the after-text says "Where this file and the map differ, follow the map". No clause quotes this file's text, so no replacement is needed. Side note, not mine to fix: 226 clause 1 describes the file as holding "the trigger form of duties stated elsewhere in the map", but both before-text and after-text say the governing statement is in the `/expedition` skill.
  - 314 (shared n-grams): it asks the manager contract to adopt the stop skill's three derivations. They are kept word for word. No replacement needed.
  - 120, 202 (n-grams "three states", "nothing is lost"): these are coincidental matches.
  - 302, and this node itself: they only list the paths in the common clauses.
- **Result:** no open condition needs a replacement clause, and I propose no supersession.

GENERALISATIONS:
- Stop skill: "Work that cannot move without the human goes in front of them before the session ends, rather than being left standing" and "All a session ending adds is that none of them is left over" became one sentence, "Put the work that needs the human in front of them before the session ends", plus "as they always do" on the sentence about which sections govern. Every case comes out the same: every gate and unanswered question goes to the human before the end, and nothing else about how they are handled changes.

INDEX LINE:    The stop skill, `wayfinder-divergences.md` and the triggers rule are rewritten in plain English with every rule kept; "claimants" and a partly false "tier 1" claim are removed, and no open condition needed re-pointing.

FLAGS:
ASSUMPTION: Removed the stop skill's claim that a gate and a worker's unanswered question are both "tier 1 claimants". It held a refused coinage and is wrong for a relayed interview question, which is tier 2. The skill still defers to `## What is in front of the human, and when`, which decides the tier, so no case changes. I listed it as rule change 1. What I did: rewrote the three files, ran the re-pointing search described above, and settled this on my own because it touches no file but this one.
Index sentence: The stop skill no longer says both kinds of human-bound work are tier 1, because a relayed interview question is tier 2 and the manager contract's queue section decides the tier.

NEW NODES:     none

INVALIDATIONS: none. The stop skill's "each can be worked out from the node's own file" still contradicts the manager contract's `### Three states nothing in the files shows`. This work did not create that contradiction, and node 314 settles it.

GATE PAYLOAD:
- Checker findings: none yet.
- Paths touched:
  - `.claude/skills/expedition-stop/SKILL.md`
  - `.claude/skills/expedition/wayfinder-divergences.md`
  - `.claude/rules/expedition-triggers.md`
- Proposed commit message:
  ```
  Rewrite the stop skill, the wayfinder divergences and the triggers rule in plain English

  Node: graph-workflow/301
  ```

Method skills: none invoked, so nothing was skipped.

RETROSPECTIVE:
1. **What I had to hunt for.**
   - Whether any before-text heading is protected by clause 5. I grepped every heading against all 16 listed files; nothing named this up front. None are protected, and a one-line statement in the spawn would have saved the check.
   - Whether the manager contract states the three triggers, for clause 13. I grepped for "finishes" and found it in `### Picking the next node` and `## The order you act in`.
   - Node 293's script needed `TMPDIR`, the input file names and the self-exclusion adapted before it would run.
2. **What arrived that this node did not need.**
   - Most of `map-implementation-rules.md`: only standing rule 5 and the bar paragraph applied.
   - The manager's note on clause 7's grep list was useful, but most of its pattern hit nothing in these small files.
   - Reading most of the manager contract (about 6,300 words) for clause 13 and the cited headings. A short extract of `## The order you act in`, `## What is in front of the human, and when` and `### Picking the next node` would have been enough.
3. **What would have made it easier.**
   - Saying that no heading of the three files is clause-5-protected.
   - Saying that "in flight" also counts as a figure under 8c, and that the frontmatter keeps it.
   - A generic version of the search script that takes the before and after files as arguments.
   - The size target cannot be reached on files this short, where fenced or listed text makes up much of the word count. Saying so up front would stop a worker from spending passes chasing it.
4. **What was stale, wrong or contradicted something else.**
   - The stop skill's "tier 1 claimants" is wrong for relayed interview questions, which are tier 2.
   - The three-states contradiction with the manager contract, already known and owned by node 314.
   - Node 226 clause 1 says the triggers file holds duties "stated elsewhere in the map", but they are stated in the `/expedition` skill.
   - `map-implementation-rules.md` still says the map's reader reads it "cold". That is the kind of figure checkers are failing in shipped files, though it binds only this effort's record.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-25. The checker was resumed from node 304's check.*

> PASS
>
> Node 301, "Rewrite the stop skill, `wayfinder-divergences.md` and the triggers rule in plain English", meets every clause of the amended acceptance condition for all three files, and the bar holds. I found one rule change, in the stop skill, which does not fail the work. Missing the size target does not fail it either.
>
> My contract is the main-tree checker contract, unchanged since my last check: its last commit is `76e66e3` and it has no uncommitted edits. The work is in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/301-rewrite-the-stop-skill-divergences-and-triggers`, on branch `worktree-301-rewrite-the-stop-skill-divergences-and-triggers`, based on `ede2c76`. I read the changed paths only as the work. Line numbers below are the after-text's.
>
> **RULE CHANGES**
>
> `.claude/skills/expedition-stop/SKILL.md`:
> 1. **A statement about the queue was removed.**
>    - Before, under `## Finish the work in flight`: "Both are already tier 1 claimants in your contract's `What is in front of the human, and when`". "Both" means every node waiting at a gate and every worker holding an unanswered question.
>    - After: removed. The after-text leaves the placement to the manager contract: its sections "govern how each is put to the human and what an answer does, as they always do".
>    - The two cases differ in one place. The manager contract's tier 1 holds only a gate, a worker blocked on a raise, and your own raise. A worker's unanswered relayed interview question is tier 2. Read literally, the before-text placed that question in tier 1 at session end. Under the after-text it stays in tier 2.
>    - The before-text's own "unchanged" and "already" suggest the statement was meant only to describe the contract. I list it because it no longer has a counterpart. Removing it also removes "claimants", one of the ruled-out words that clause 8c names.
>
> `.claude/skills/expedition/wayfinder-divergences.md`: none found.
>
> `.claude/rules/expedition-triggers.md`: none found.
>
> How far the list reaches: for each file, I compared every statement of the before-text against the whole after-text. The comparison covered every rule and whose it is, every condition and exception, the fixed templates and frontmatter, the defined terms, the refused words, and every closed list with its count:
> - **stop skill:** the three steps in order, the two cases of work under way, the three states shown as ordinary nodes, and the four items of the closing report.
> - **divergences file:** the five unchanged items, the five added items, and the five differences with the block to append.
> - **triggers file:** the three moments and their duties, the five priority items, and item 5's four waiting things.
>
> **Clause by clause** (each clause checked for each file)
> 1. **Lost or changed statements: met.** The one rule change is listed above. Otherwise I judged each reworded statement to give the same outcome:
>    - In the stop skill, "a slot a finishing node leaves empty stays empty" became "leave the effort's counts below their numbers rather than starting work to bring them back up".
>    - In the divergences file, "A repo with no such doc needs nothing from this file" became "This file is only for a repo whose tracker doc …".
>    - In the triggers file, "it overrides nothing there", meaning the map, became "Where this file and the map differ, follow the map".
> 1a. **Terms `CONTEXT.md` does not define: met.** No defined term is dropped. The stop skill's inline definition of the session ("your own thread's life, not the effort") is kept as "A session is the life of your own thread".
> 2. **Added statements: met.** Nothing is added. "Write no handoff document" and "Leave the effort open" restate the before-text's "Write no handoff document" heading and "nothing here does that", meaning close the effort.
> 3. **Generalisation: met**, apart from the rule change listed. In the triggers file, item 5's "C and (A or B)" order of conditions is the same test as before, and the same as the manager contract's item 5.
> 4. **Fixed text: met.** For all three files, the frontmatter and all code fences are byte-identical to the before-text. That covers the stop skill's description, the triggers file's `paths:` block, and the divergences file's `## Expedition operations` block.
> 5. **Headings: met.**
>    - Five headings were renamed. In the stop skill: `## Start no new node`, `## Finish the work in flight`, `## Write no handoff document`, and `## What does not survive, and why it costs nothing`. In the divergences file: `## Read differently`.
>    - I searched the listed files unwrapped for each old heading text, in the worktree and in the main tree's `.scratch/graph-workflow/` map files. None appears in any other listed file. The only hits are the stop skill's own frontmatter description and body, and clause 5 counts only other files.
>    - The triggers file's headings are unchanged.
> 6. **References inside the file: met.** Each one resolves:
>    - Stop skill: "as in the first case", and "the case under `## Finish the work already under way`".
>    - Triggers file: "the three moments below", "the triggers above", and "what this order gives you".
>    - Divergences file: "the block below".
>    - The stop skill also points at the manager contract. `## What is in front of the human, and when`, `## What is never yours`, `### Three outcomes, and no fourth` and `## When an agent dies or is stopped` all exist in `.claude/skills/expedition/SKILL.md` at those heading levels.
> 7. **Terms: met.**
>    - "Session" names the manager thread's session, not an effort or an attempt, which are what the `_Avoid_` lines refuse it for. The before-text and the fixed frontmatter use it the same way.
>    - "Ticket" and "`/wayfinder`" name the other tracker's own items and the ancestor skill. They do not name a node or this workflow.
>    - "The session's closing report" is kept as in the before-text.
>    - No new term is coined.
> 8. **Plain English: met** in all three files.
>    - 8a: every prohibition has its positive form beside it. For example, "Write no handoff document. Leave the next manager the record", and "Never list them and ask him which to take" after "pick the one the order gives you and send it".
>    - 8b: no bold remains in the prose of any of the three files. The before-text's emphasis bolding is gone, and the bold inside the fixed block is untouched.
>    - 8c: these phrases are replaced with plain words: "claimants", "rides …" style figures, "costs nothing", "read differently", and "survives a compaction", which is now "stays in context after a compaction".
>    - 8d: I found no slogan-shaped sentence, and "the whole of what" does not appear.
>    - 8e: I read every it, this, that, they, these and those, and each has one clear referent in its own sentence or the one before.
>    - 8f: no semicolons and no dashes appear in the prose outside the fences, except the fixed frontmatter and the heading `### Three outcomes, and no fourth`.
> 9. **Size (reported, not enforced):**
>    - Stop skill: 585 before, 567 after, 97%. The target is at most 390.
>    - `wayfinder-divergences.md`: 330 before, 330 after, 100%. The target is at most 220.
>    - `expedition-triggers.md`: 364 before, 370 after, 102%. The target is at most 242.
>    - All three miss the target, which does not fail the work.
> 10. and 11. **Scope: met.** `git status --porcelain --untracked-files=all` shows only the three named files modified, with no untracked files.
> 12. **The human's own sentences: met.** Only the grammar changed:
>    - "if the human has nothing to do and there is a question/gate, give it to him." became "If the human has nothing to do and there is a question or a gate, give it to him."
>    - "Wait for him to answer before giving him a question." is unchanged.
>    - "The instruction on how to behave and how to use the map are in the skill `/expedition` and next to it `graph-conventions.md`" became "The instructions on how to behave and how to use the map are in the skill `/expedition` and, next to it, in `graph-conventions.md`."
> 13. **The triggers file stays a copy: met.** I compared it against the worktree's `.claude/skills/expedition/SKILL.md`.
>    - Priority items 1 to 5 match `## The order you act in` items 1 to 5, including item 5's check and its four waiting things.
>    - "When a node finishes, look at the frontier and start a replacement" matches `### Picking the next node`: "When a node finishes, pick the next one, spawn its worker". Priority item 1 comes before item 3, which covers "as soon as what is owed to the record is written".
>    - "Put it in front of the human as soon as nothing else is in front of them" and the third moment's duties match `## What is in front of the human, and when`: "Keep exactly one question in front of the human at a time", "Send the one thing that the tiers and arrival order choose", and "Never ask the human which waiting thing to take next".
>    - The file's statement about its own standing ("Where this file and the map differ, follow the map") is not a trigger duty or a priority item. I did not count it as an addition. The before-text said the same as "it overrides nothing there".
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, in the same state as at my last check: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:**
>   - Standing rule 5 (plain English), which is the same property as clause 8.
>   - `CONTEXT.md`'s `_Avoid_` lines.
>   - `graph-conventions.md`, which names `wayfinder-divergences.md` as its companion and is consistent with it.
>   - `/writing-for-agents`.
>   - All five ground rules, which are met. Nothing in the three files tells an agent to address the human.
> - No reviewing skill is named, so I ran none.

*The manager's note, matching the two lists:* the checker's one rule change is the worker's rule change 1, which the worker listed as deliberate and flagged. The worker's ten borderline entries (2 to 11) are ones the checker judged to keep their outcome. Nothing on the checker's list is missing from the worker's.


### Gate — approve, 2026-09-25

The human, `verbatim`: *"approve"*

## Flags

`301.1` **· settled** `ASSUMPTION` — Removed the stop skill's claim that a gate and a worker's unanswered question are both "tier 1 claimants". It held a refused coinage and is wrong for a relayed interview question, which is tier 2. The skill still defers to `## What is in front of the human, and when`, which decides the tier, so no case changes. I listed it as rule change 1. What I did: rewrote the three files, ran the re-pointing search described above, and settled this on my own because it touches no file but this one.
