# Rewrite the prototype contract in plain English

Type: implementation
Status: resolved
Blocked by: 290

## Question

Rewrite `.claude/skills/expedition-prototype/SKILL.md` in plain English and shorter, under the pass [node 289](289-a-plain-english-and-compaction-pass-over-the-shipped-files.md) settled.

> Beside the work, the handover carries three things. (1) For every open node whose `## Acceptance condition` quotes text or a heading from the before-text of what this node rewrites: either a replacement for each affected clause, quoting the after-text, or a proposal that the node be superseded as unnecessary, with the reason. Name the search you ran. (2) Every generalisation made, naming the statements it replaced. (3) Any rule judged dead or a default behaviour, reported as a new node and left in the text.

## Acceptance condition

*Authored by node 289's worker and filed by the manager. Node 289's worker's COMMON CLAUSES block, copied in full, then this node's own clauses, verbatim.*

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

11. **Scope.** The work changes `.claude/skills/expedition-prototype/SKILL.md` and no other path. The rewritten range is the whole file.
12. **The two shared sections are copies.** The after-text's sections headed `## When you raise a flag` and `## When a node you report is an implementation node` are byte-identical to the sections of the same headings in `.claude/skills/expedition-research/SKILL.md` as it stands at the commit this work's branch was created from. For those two sections, this identity takes the place of clauses 1 to 3 and 8. For the rest of the file, clauses 1 to 10 apply as written.

## Amendment by the human, 2026-09-24

*The human approved the manager's proposal, `verbatim`: "ok". The proposal and the answer to A that prompted it are recorded on [node 290](290-rewrite-the-research-contract-as-the-pilot.md). The manager drafted the wording below, and the human amended the condition with it. The original clauses above are left as they were. The clauses below take the place of clauses 1 and 2, add clause 1a, and add a sentence to clause 3.*

1. **Lost or changed statements are rule changes.** The binding statements are: every rule, meaning every instruction, permission, prohibition or duty, and whose it is; every condition or exception attached to a rule; every fixed template; every term the text defines, and its definition; every word the text refuses; and the members and stated count of every closed list. A binding statement of the before-text that has no counterpart anywhere in the whole after-text, or whose counterpart changes the outcome for any case, is a rule change. The checker lists every rule change it finds, each with the before-text statement and its after-text counterpart, or "removed". A rule change does not fail the work.
1a. **Terms `CONTEXT.md` does not define.** A term the before-text defines that `CONTEXT.md` does not define may be dropped as a term, where its meaning is still stated in plain words at the place it was defined. Dropping a term that way is not a rule change.
2. **Added statements are rule changes.** A rule, permission, duty, exception, defined term or refused word that the after-text states and the before-text does not is a rule change. The checker lists it the same way as under clause 1. It does not fail the work.
3. *(added sentence)* A generalisation that changes an outcome, or decides a case the before-text left undecided, is a rule change under clause 1 or clause 2.

## Answer

The prototype contract is rewritten in plain English at 93% of its length, with fences and headings kept, both shared sections copied byte-for-byte from the research contract, and no deliberate rule change.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`, as changed by correction round 1. The checker found no rule change under `### Checker run 2`, and judged every entry on the worker's list to keep its outcome. The human approved. The work landed as commit `6d26be1`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-25. The worker's own text, pasted. The worker was resumed once after a usage-limit stop. The flags are raised under `## Flags` at the gate.*

HANDOVER:      Rewrite the prototype contract in plain English

(On resume: I checked the worktree before writing. It held exactly my earlier write, with nothing else changed. The one edit I made after resuming restores "It is never yours." to the `code slot` definition, because node 81's condition needs that text. See the re-pointing search.)

ANSWER:
`.claude/skills/expedition-prototype/SKILL.md` has been rewritten in plain English in the worktree `.scratch/graph-workflow/worktrees/293-rewrite-the-prototype-contract`, based on `e64b3de`. The changes are uncommitted.

- **Size.** `wc -w` went from 2,176 to 2,033, which is 93%. The two-thirds target (1,451) is missed.
  - The fences hold about 220 words and are fixed.
  - The two shared sections went from 700 to 576 words. That cut came from copying node 290's approved text.
  - The rest of the prose, frontmatter included, went from 1,256 to 1,237 words. The before-text was already terse. Much of its prose is sentences this file shares with the rewritten research, implementation and grilling contracts, and I took those in the wording those contracts already use: the method-skill paragraph, the `## What you read` list, the sources sentence, the human-answer paragraph and the handover paragraphs. Cutting further would mean changing rules or breaking that shared wording.
- **Fixed text.** The frontmatter and all four fences are byte-identical to the before-text.
- **Shared sections (clause 12).** `## When you raise a flag` and `## When a node you report is an implementation node` are byte-identical to the research contract's sections at `e64b3de`. The only difference is the blank line before the next heading, as at nodes 291 and 294. This file's before-text of both sections was byte-identical to the research before-text at `4068519^`, apart from one trailing blank line. So every difference in those sections is one node 290 made and the human approved.
- **Headings (clause 5).** Every before-text heading is kept exactly, in the same order.
- **Term list.** Every term is one `CONTEXT.md` defines, so none was dropped. The file keeps its own list, as nodes 291, 294 and 295 did.
- **Labels and idioms replaced.**
  - "standing over sources" was dropped as a label under clause 1a and replaced by the pilot's plain description.
  - "in as many words" (2 places) became "explicitly".
  - The slogan "The graph-file ban is about recording, not about files" is gone. Its rule is now hard rule 2.
  - "the whole of the discipline" became "The discipline is the following, in full".
  - These were reworded plainly:
    - "The reaction is the point"
    - "Rough is correct here"
    - "put it in front of the human"
    - "is not what this rule reaches"
    - "your recommendation lost … as though it had won"
    - "carry on"
    - "per remaining call"
    - "Leave the conflicting part unrun"
- **Other checks.**
  - There are no semicolons outside the fences.
  - Bold appears only on terms where they are defined, and in the copied shared sections. The bold on "attempt" in the park definition, on "park" in the table, and on the emphasised clauses is removed.
  - The refused-word grep finds only "ask". Every hit is the prototype worker putting its own questions to the human, the human's words "ask me later" in the table, or fence text. See the flag.
  - No method skill was run, so none was skipped.

INDEX LINE:    The prototype contract is rewritten in plain English at 93% of its length, with fences and headings kept, both shared sections copied byte-for-byte from the research contract, and no deliberate rule change.

FLAGS:
ASSUMPTION: I kept "ask" for the prototype worker putting its own questions to the human. That covers the opening, the discipline's bullets 2, 3 and 5, and the replacement-attempt section, plus "ask me later" as the human's words in the table. `CONTEXT.md`'s Raise `_Avoid_` line refuses *ask* only for a raise. It names asking as "the ordinary mode of a worker built to question the human", and the prototype discipline is to show the probe and ask what it changes. This is the same reading node 291's gate approved for the grilling contract. *Index:* The prototype contract keeps "ask" for its worker's questions to the human, on the reading that the Raise `_Avoid_` line refuses it only for a raise.

NEW NODES:     none. I judged no rule dead or something the model does by default anyway.

INVALIDATIONS: none

GATE PAYLOAD:
- **Checker findings:** none yet.
- **Paths touched:** `.claude/skills/expedition-prototype/SKILL.md` only. My scratch copies and scripts are outside the repo, in `/tmp/claude-1000/n293/`: `search.py`, `dump.py`, `phrases.txt`, `before.md`, `after.md`, `shared.md` and `out.txt`.
- **Bar:** the repo has no build, test, format or CI commands. The root holds only `.claude`, `CONTEXT.md`, `.gitignore`, `.scratch` and `.worktrees`, and `map-implementation-rules.md` records none either. `git diff --check` is clean, and `git status` shows only the one path.
- **Proposed commit message:**
  ```
  Rewrite the prototype contract in plain English

  Node: graph-workflow/293
  ```

RULE CHANGES

I made no deliberate rule change and used no licence under ruling A. Every entry below is borderline: I judge that it keeps every outcome, and I list it so the checker's list can be matched against mine. The shared sections are excluded, because under clause 12 they are copies and not rule changes.

1. **Opening, direct contact.**
   - Before: "You are not the manager, and you never address the human directly. Every question you ask travels through the manager, which passes it along unaltered and answers nothing itself."
   - After: "…and you are not its manager." then "Every question you ask goes to the human through the manager. The manager passes it along unaltered and answers nothing itself."
   - The ban on addressing the human directly is carried by hard rule 4 ("Call no tool that addresses the human") and by the worker definition ("no direct contact with the human").
   - "*What you hand back*" became "`## What you hand back`".
2. **Kind paragraph.**
   - Before: "The reaction is the point, so the node is not finished when the probe is built."
   - After: "The human's reaction to the probe is what the node is for, so your work continues after the probe is built."
   - "the reaction" is now said to be the human's.
3. **Worker definition.** Before: "you. One node, no bookkeeping on the graph, no human." After: "you, working one node with no bookkeeping on the graph and no direct contact with the human." "direct" is taken from the before-text's opening, because the relay is contact. This is node 291's wording.
4. **Park definition.** The bold on "attempt" is removed. This file does not define attempt, and clause 8b allows bold only where a term is defined. "banked" is kept as `CONTEXT.md`'s term.
5. **Code slot definition.** Before: "…at a time. Never yours." After: "…at a time. It is never yours." This makes the sentence grammatical and changes no outcome.
6. **Resolve and verbatim.**
   - Resolve: "The manager's act, never yours." became "It is the manager's act, never yours."
   - Verbatim: "against a **paraphrase** of them" became "Its opposite is a **paraphrase** of them."
7. **What you read.** "Read each of these." became "Read each of the following." "`flags.md` is not yours. Leave it unread." became "Leave `flags.md` unread. It is not yours." The label "standing over sources" was dropped under clause 1a, which is not a rule change. The bold on "ground rules" is removed.
8. **Hard rule 1.**
   - Before: "Everything you build lives in `prototypes/NN-<name>/`. Nothing you build enters the product tree, and nothing you build becomes product code."
   - After: "Put everything you build in `prototypes/NN-<name>/`. Keep all of it out of the product tree, and make none of it product code."
   - Statements of fact became instructions. "nothing you build becomes product code" (by anyone) is now "make none of it product code" (by you).
   - "You do not hold the code slot." is kept byte-identical.
9. **Hard rule 2, the graph-file ban.**
   - Before: "You write no graph file." Then the slogan. Then "Bookkeeping on the graph is the manager's job; yours is to do your own work and never record it when you finish. So a node whose own work is a change to a graph file is not what this rule reaches — you make that change like any other work. Marking your node, resolving it, and its lines in `decisions.md` and `flags.md` stay the manager's whatever your node's work is."
   - After: "Write a graph file only where your node's own work is a change to that file. Leave all recording on the graph to the manager, whatever your node's work is. The manager marks your node, resolves it, and writes its lines in `decisions.md` and `flags.md`."
   - The ban-plus-exception is now an "only where" permission. The slogan is removed.
10. **Hard rule 3.** Before: "You never answer your own question on the human's behalf. Where they hand one back to you in as many words, see *When the answer is not an answer*." After: "Leave the answer to each of your questions to the human. Where the human explicitly hands a question back to you, follow `### When the answer is not an answer`."
11. **Hard rule 4.** Before: "You have no human-facing tool. Do not call one. When you have a question, end your turn and make that question your entire final output, in the shape below." After: "To put a question to the human, end your turn and make that question your entire final output, in the shape under `### question — you need the human`. Call no tool that addresses the human." The claim of fact is removed and the rule stays, as at nodes 291 and 294.
12. **Hard rule 5.**
    - Before: "You never resolve your node, never mark it, and never create another one. You hand your answer back and the manager writes it, and a node you have found is reported on your handover's `NEW NODES` part rather than created as a file."
    - After: "Hand your answer back, and the manager writes it onto your node. Report a node you have found on your handover's `NEW NODES` part, and create no node yourself."
    - "never resolve … never mark" is now stated once, as the manager's acts in hard rule 2 ("The manager marks your node, resolves it"). "rather than created as a file" is now "create no node yourself".
    - Hard rules are still six, in the same order and on the same subjects.
13. **Hard rule 6.** "Your final output is consumed by the manager." became "Write your final output for the manager to consume."
14. **Method-skill paragraph.** Replaced by the pilot's wording.
    - The reason "Such a skill was written for an agent working alone" is removed.
    - "Leave the conflicting part unrun" became "Skip the conflicting part", and "which part you left" became "which part you skipped".
    - The three conflicting instructions are kept, now as a list.
15. **The discipline.**
    - "This is the whole of the discipline:" became "The discipline is the following, in full:". It still has five bullets, and no count was added.
    - Bullet 1: "Rough is correct here." became "A rough probe is correct."
    - Bullet 2: "Build it first, then put it in front of the human and ask what it changes." became "Build it first. Then show it to the human and ask what it changes."
    - Bullet 3: "One question at a time. Wait for the answer before asking the next." became "Ask one question at a time, and wait for its answer before you ask the next."
    - Bullet 4: "Every question carries a recommendation…" became "Give every question a recommendation…"
    - Bullet 5: "Any fact the files can tell you, read. Ask only what they cannot." became "Read any fact the files can tell you. Ask the human only what the files cannot tell you." "the human" is now explicit.
16. **What you hand back.** Before: "Exactly one of three, and never two at once." After: "Each time you end your turn, hand back exactly one of the three shapes below." Node 291's checker accepted the same sentence, because a worker hands back once per turn.
17. **After the question shape.**
    - "The human has read none of what you read. Write `ABOUT` and `SO FAR` on every question, the first one included." became one sentence joined by "because".
    - "Name the artifact by path and let them open it; never paste it into `SO FAR`." became "Name the artifact by path for the human to open, and never paste it into `SO FAR`."
18. **Human answer paragraph.** Replaced by node 291's wording.
    - "except where what they wrote is an assent to one of the options you offered" became "unless the reply assents to one of your options".
    - "that option is what they endorsed, and you read it as theirs" became "read that option as the human's own choice".
    - "your recommendation lost: do not carry on as though it had won" became "the human's answer contradicts your recommendation. Continue from their answer, never as though your recommendation had been accepted."
    - The one exception, assent, is kept.
19. **Table.**
    - "carry on" became "continue" in rows 1, 2 and 4.
    - Row 2: "Return one `DELEGATED` flag" became "Hand back one". "This covers **that question only** — the rest of the exchange stays with the human unless they say otherwise in as many words." became "This applies to that question only. The rest of the exchange stays with the human unless they explicitly say otherwise."
    - Row 3: the bold on "park" is removed.
    - Row 4: "carry on against the new one" became "continue with the new question".
    - It still has four rows.
20. **Whole-node delegation.** Before: "Whole-node delegation is said explicitly. Only then do you finish the node alone, with one `DELEGATED` flag per remaining call you make." After: "Finish the node alone only when the human explicitly delegates the whole node. Then hand back one `DELEGATED` flag for each remaining decision you make." "call" became "decision".
21. **Handover.** Before: "Five parts, every time. Write `none` in full for any part you have nothing for, and never leave a part off." After: "Hand back all five parts every time. Write `none` in full for a part you have nothing for."
22. **Artifact.** Before: "The artifact is linked, never copied into `ANSWER`." After: "Link the artifact in `ANSWER`, and never copy it in." The fence already asks for "the artifact linked by path" in `ANSWER`.
23. **Markers and recording.** The markers sentence only gained commas, and there are still two markers. "The manager writes every part of this" became "…of your handover", and "So" was added before "write `ANSWER`".
24. **Park text.** "Their words go here as they said them, never summarized." became "Write the human's words here as they said them, without summarizing them."
25. **Replacement attempt.**
    - Before: "The spawn carries the record of the earlier attempt, and whatever the previous attempt built is still in `prototypes/NN-<name>/`. Every question answered in that record is a settled fact. Never ask one of them again."
    - After: the first sentence is split in two. The rest became "Treat every question answered in that record as settled, and never ask the human any of them again."

Closed lists and exception cases I checked, all kept:
- Three handed-back shapes.
- Six hard rules.
- Three conflicting skill instructions.
- Five discipline bullets.
- Four table rows.
- Five handover parts.
- Two markers.
- Four things read.
- The one assent exception.
- The graph-file exception.
- "you decide" covers that question only, unless the human says otherwise explicitly.
- Whole-node delegation only when the human states it explicitly.

GENERALISATIONS
1. Hard rule 2's "Leave all recording on the graph to the manager, whatever your node's work is. The manager marks your node, resolves it, and writes its lines…" replaces these before-text statements:
   - "Bookkeeping on the graph is the manager's job; yours is to do your own work and never record it when you finish"
   - "Marking your node, resolving it, and its lines in `decisions.md` and `flags.md` stay the manager's whatever your node's work is"
   - hard rule 5's "You never resolve your node, never mark it"
2. "Write a graph file only where your node's own work is a change to that file" replaces "You write no graph file", the slogan, and "So a node whose own work **is** a change to a graph file is not what this rule reaches — you make that change like any other work."
3. "Each time you end your turn, hand back exactly one of the three shapes below" replaces "Exactly one of three, and never two at once."
4. "Hand back all five parts every time" replaces "Five parts, every time" and "never leave a part off."

RE-POINTING SEARCH

**How I searched:**
- **Scope.** All 89 open or claimed nodes, excluding 293. For each, I collected the `## Acceptance condition` section and every `## Amendment…` section wherever it sits. The script is `/tmp/claude-1000/n293/search.py`, a copy of node 291's with the paths changed.
- **(a) Quoted spans.** Every quoted span of 12 characters or more (backticks, `*…*`, straight or curly double quotes), normalised, found in the before-text, and checked for whether it survives in the after-text.
- **(b) Shingles.** Six-word shingles shared between the before-text and each condition.
- **(c) Mentions of the file, and counts and positions:**
  - expedition-prototype, prototype contract, prototype worker, five worker contracts, worker contracts, each of the five, all five, five contracts, every worker contract
  - hard rule 1 to 6, rule 6, six hard rules, three things, exactly one of the three, Exactly one of three, never two at once, item 4, item 5
- **(d) Every before-text heading**, and the removed or replaced wording:
  - in as many words, travels through the manager, never address the human directly, You are not the manager, One node, no bookkeeping on the graph, no human, the channel and the payload carrying your question, the human deferring your question, stay banked, Never yours, The manager's act, never yours, against a paraphrase
  - Read each of these, is not yours. Leave it unread, standing over sources, ground rules
  - Everything you build lives in, Nothing you build enters the product tree, nothing you build becomes product code, You do not hold the code slot
  - You write no graph file, graph-file ban, about recording, not about files, is not what this rule reaches, never record it when you finish, like any other work, stay the manager's whatever your node's work is
  - You never answer your own question, on the human's behalf, human-facing tool, Do not call one, entire final output, in the shape below, never resolve your node, never mark it, never create another one, rather than created as a file, Your final output is consumed by the manager
  - the hard rules govern, written for an agent working alone, collide with the rules above, unrun, which part you left, whole of the discipline
  - cheapest thing that can be reacted to, Rough is correct, put it in front of the human, ask what it changes, One question at a time, Wait for the answer before asking the next, a recommendation you believe, Any fact the files can tell you, Ask only what they cannot, The reaction is the point, not finished when the probe is built
  - has read none of what you read, the first one included, let them open it, never paste it into, You are then resumed with, not a rendering of them, an assent to one of the options, ok for recommended, what they endorsed, your recommendation lost, as though it had won
  - carry on, that question only, Whole-node delegation, per remaining call, Five parts, every time, never leave a part off, The artifact is linked, never copied into, Two markers are yours, The manager writes every part of this, Their words go here, never summarized, settled fact, Never ask one of them again, whatever the previous attempt built
  - all eleven headings, and "the fog"
- **Re-run commands.** I re-ran the enumerators recorded by nodes 109, 148 and 304 in the worktree.

**Replacement clauses:**
- **Node 81, entry 3.** This is the one clause my rewrite would otherwise have broken. My first draft dropped "Never yours", so I restored it as "It is never yours." and entry 3's demand to keep it still holds. Only the quoted "currently reads" text differs. Replace:
  - "It currently reads: *"the right to modify product code, held by one worker at a time. Never yours."*" with "It currently reads: *"the right to modify product code, held by one worker at a time. It is never yours."*"
  - "and keeps *"Never yours"*" with "and keeps *"It is never yours"*"
  - "its hard rule 1, *"You do not hold the code slot"*, is true under the lifecycle and is left exactly as it stands" with "its hard rule 1's sentence *"You do not hold the code slot."*, which is true under the lifecycle, is left exactly as it stands". That sentence is byte-identical in the after-text. The rest of hard rule 1 now reads "Put everything you build in `prototypes/NN-<name>/`. Keep all of it out of the product tree, and make none of it product code."
- **Node 109, the enumerator paragraph**, as amended by nodes 290, 294 and 291. In the list of files that hold *"against the four points above"*, add `.claude/skills/expedition-prototype/SKILL.md`.
  - `grep -rlnE "against (those four|the four points above)" --include="*.md" .claude/` in the worktree still returns the five worker contracts and no others.
  - The `self-contained` grep still returns the same seven paths.
- **Node 109, clause 6**, as amended by node 291. In the list of contracts whose read-back sentence is *"check what you wrote against the four points above"*, add the prototype contract. The rest is unchanged.
- **Node 148, clause 1**, as amended by node 291. In the list of files that hold the bullet beginning `A path may say where, because the checker has the repo`, add `.claude/skills/expedition-prototype/SKILL.md`. The fallback "in any of the five not yet rewritten, the bullet beginning `a **path** may say where`" still covers the precondition contract until node 292 lands. The absolute-path grep of clause 3 returns 0.
- **Node 155, the sentence before its clauses**, as amended by node 291. In the list of files whose `## What you read` section opens `Read each of the following. Do not trust any summary of them.`, add `.claude/skills/expedition-prototype/SKILL.md`.
  - In the prototype file, the `flags.md` line ("Leave `flags.md` unread. It is not yours.") follows the list directly.
  - The decisions bullet ("`decisions.md` — the sections the spawn names") is byte-identical, so clauses 1, 3 and 4 still hold.

**Matched, needing no change:**
- **279:** the amended clauses 1 and 3 quote the research after-text, which this file now holds byte-for-byte. Clause 2's conflict with byte-for-byte copying is still the manager's open item.
- **304:** the bullet "the standing preferences, the fog" is kept. Its recorded grep still returns the same four paths.
- **43:** `your answer contradicts` is inside the fence. "Report `NEW NODES` and `INVALIDATIONS` yourself. Nothing else reports them." is kept word for word. The rule on a demand about the whole record is kept in the copied shared section.
- **41:** the prototype contract still lists its markers, and its `FLAGS:` fence line is unchanged.
- **60:** "Hand back all five parts every time" still states the count.
- **61:** the opening ("The manager passes it along unaltered and answers nothing itself") and the handover paragraph ("writes every part of your handover onto the graph unaltered") still spell the idea out, so its "ten places" premise still holds for this file.
- **57:** this file still carries a channel to the human.
- **73, 79 and 87:** they only require this directory, or its headings, to be left unchanged by their own work. Every heading is kept.
- **292, 301 and 302:** they quote "in as many words" and "about recording, not about files" only as examples in their own clauses 8c and 8d.
- **Hits on other files or on the manager's own prose:** 44, 96, 97, 105, 111, 118, 127, 134, 146, 149, 151, 152, 156, 160, 161, 190, 226, 228, 230, 232, 234, 247, 258, 271, 276, 278, 280, 284, 285, 287, 288 and 318.

RETROSPECTIVE
1. **What I had to hunt for.**
   - Whether this file's shared sections matched the research before-text. I checked with `git show 4068519^`, and they match apart from one trailing blank line. The spawn's "about 576" words for the shared sections is the after-text figure. The before-text held 700, so most of this file's size cut came from the copy.
   - That node 81 requires "Never yours" to be kept. The search found it, not any pointer. I looked first at the benchmarks and the manager's notes, which do not mention node 81.
2. **What arrived that this node did not need.**
   - Almost all of `map.md`. I needed only the note that `CONTEXT.md` is the glossary.
   - Of `map-implementation-rules.md`, I needed only rule 5.
   - Node 291's full file. Its `RULE CHANGES`, `RE-POINTING SEARCH` and checker run were all I used, and they were the most useful model.
   - Node 109's full condition text, when I needed only its latest amendment. A per-node note of "conditions the previous rewrite amended, and the clause" would have replaced most of the dump reading.
3. **What would have made it easier.**
   - One shared search script with the node number as an argument (node 313), and a shared phrases file holding the handles common to the five contracts.
   - A spawn that lists nodes whose conditions quote this file's specific text, such as node 81 here, and not only the list-of-files nodes 109, 148 and 155.
   - A spawn that gives the before-text size of the shared sections, so the size expectation is set on the prose that can actually be cut.
4. **What was stale, wrong or contradictory.**
   - `map.md` still says of `CONTEXT.md` "Where it moves … are open", and that is correct. But node 81's condition still hedges on `CONTEXT.md` having moved to `.claude/skills/expedition/CONTEXT.md`, which has not happened.
   - The spawn's "about 576 words in the two shared sections" is the research after-text figure, not this file's before-text figure of 700.

## Review

### Checker run 1 — `FAIL`, acceptance condition (as amended by the human)

*The checker's own text, pasted, 2026-09-25. The checker was resumed from node 292's check.*

> FAIL: acceptance condition
>
> Node 293, "Rewrite the prototype contract in plain English", fails on one sentence under clause 8e. Everything else is met, I found no rule changes, and the bar holds. The fix is a one-phrase rewording.
>
> My contract is the main-tree checker contract. It is unchanged since my last check: its last commit is `76e66e3` and it has no uncommitted edits. The work is `.claude/skills/expedition-prototype/SKILL.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/293-rewrite-the-prototype-contract`, branch base `e64b3de`. I read the changed path only as the work. Line numbers below are the after-text's.
>
> **Finding: clause 8e, a "this" with no clear referent (1 instance)**
> - **Instance:** line 122, in the "you decide" row of the `### When the answer is not an answer` table: "answer it yourself and continue. Hand back one `DELEGATED` flag naming what you decided. This applies to that question only."
>   - The sentence just before names only the `DELEGATED` flag and "what you decided". The intended referent is the human's "you decide", the delegation, which sits in the other cell of the row and outside that window.
>   - The next sentence ("The rest of the exchange stays with the human unless they explicitly say otherwise") restores the rule's meaning, but it does not give "This" a referent.
>   - Wording such as "The human's delegation applies to that question only" would meet the clause.
> - **Form:** a "this", "that", "these" or "those" whose intended referent is not in its own sentence or the one before, outside the two shared sections and outside code fences.
> - **Extent (bounding set):** every hit of `awk '/^```/{f=!f;next} !f{print NR": "$0}' .claude/skills/expedition-prototype/SKILL.md | grep -i -w -E 'it|this|that|they|these|those'` outside the two shared sections, which are the lines from `## When you raise a flag` up to `## If you are a replacement attempt`. I read each hit by hand, and this is the only instance.
>
> **Clause by clause**
> 1. **Lost or changed statements: met.** No rule change is found, and the list below says how far that reaches. Dropping the term *standing over sources* is allowed by clause 1a: `CONTEXT.md` does not define it, and its meaning is still stated in plain words where it was defined ("by path or glob, which sources are authoritative, which are evidence only, and which hold statements known to be false").
> 2. **Added statements: met.** Nothing is added. The positive forms give the same outcome:
>    - Hard rule 1 went from "Nothing you build enters the product tree, and nothing you build becomes product code" to "Keep all of it out of the product tree, and make none of it product code".
>    - "Leave the answer to each of your questions to the human" restates the before-text's "You never answer your own question on the human's behalf".
>    - "Each time you end your turn, hand back exactly one of the three shapes below" restates "Exactly one of three, and never two at once".
> 3. **Generalisation: met.** The before-text's hard rules 2 and 5 are regrouped:
>    - Hard rule 2 now carries the graph-file exception and the manager's marking, resolving and lines.
>    - Hard rule 5 carries "the manager writes it onto your node" and the `NEW NODES` report.
>
>    Every case comes out the same.
> 4. **Fixed text: met.** The frontmatter and all code fences are byte-identical to the before-text. That covers the question shape, the resume block, the handover and park.
> 5. **Headings: met.** Every heading is identical to the before-text.
> 6. **References inside the file: met.** Each one resolves: "listed under `## What you hand back`", "follow `### When the answer is not an answer`", "the shape under `### question — you need the human`" and "the three shapes below".
> 7. **Terms: met.**
>    - The terms from `CONTEXT.md` are spelled as it defines them: relay, park, banked, attempt, handover, flag, code slot, resolve, verbatim, paraphrase and prototype.
>    - The before-text's "Return one `DELEGATED` flag" is now "Hand back". "Return" is refused for the handover concept.
>    - "Discarded" is `CONTEXT.md`'s own definition of prototype. It is not the refused name for a reject.
>    - "Ask" is the ordinary mode of a worker built to question the human, which is what the `_Avoid_` line under **Raise** allows.
>    - No new term is coined.
> 8. **Plain English (outside the shared sections): fails on 8e**, as above. The other five properties hold:
>    - 8a: every negative rule has its positive form beside it. For example, "never paste it into `SO FAR`" sits with "Name the artifact by path", and "never copy it in" sits with "Link the artifact in `ANSWER`".
>    - 8b: bold appears only on "prototype" at its definition, on the word-list terms (including **paraphrase**), and in the shared sections.
>    - 8c: the before-text had "in as many words" (twice), "Rough is correct here" and "put it in front of the human". These are now "explicitly", "A rough probe is correct" and "show it to the human". I found no other figure of speech.
>    - 8d: I found no slogan-shaped sentence, and "the whole of what" does not appear.
>    - 8f: no semicolons outside the fences. Each dash is a list separator or part of a heading.
> 9. **Size (reported, not enforced):** the rewritten range is the whole file. `wc -w` gives 2176 before and 2033 after, which is 93% of the before-text. The target of at most 1451 is missed, which does not fail the work.
> 10. and 11. **Scope: met.** `git status --porcelain --untracked-files=all` shows only `.claude/skills/expedition-prototype/SKILL.md` modified.
> 12. **The two shared sections are copies: met.** Both `## When you raise a flag` and `## When a node you report is an implementation node` are byte-identical to the same sections of `expedition-research/SKILL.md` at `e64b3de`, apart from blank lines at the section boundary.
>
> **RULE CHANGES**
>
> None found.
>
> How far the list reaches: I compared every statement of the before-text outside the two shared sections against the whole after-text. Clause 12 replaces clauses 1 to 3 for those two sections, so they are excluded. The comparison covered every rule and whose it is, every condition and exception, the four fixed templates, the defined terms, the refused words, and every closed list with its count:
> - the three things handed back
> - the five bullets of the discipline
> - the four table rows
> - the three conflicting skill instructions
> - the five handover parts
> - the two markers
> - the four things read
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, in the same state as at nodes 291 and 292: the bar, the review route, the five ground rules and the five standing rules for writing. Its one-line uncommitted `.gitignore` note does not change what the bar requires.
> - **Standards that bore on this work:**
>   - Standing rule 5 (plain English), which is the same property as clause 8.
>   - `CONTEXT.md`'s `_Avoid_` lines.
>   - `/writing-for-agents`.
>   - All five ground rules, which are met. On ground rule 3, every question "goes to the human through the manager", and hard rule 4 says "Call no tool that addresses the human".
> - No reviewing skill is named, so I ran none.

*The manager's note, matching the two lists:* the checker found no rule change, and every entry on the worker's list is one the checker judged to keep its outcome. What goes back is the clause 8e finding.

### Correction round 1 — the worker's changes for checker run 1

*The worker's own text, pasted, 2026-09-25.*

I fixed the one clause 8e finding, a "This" with no clear referent. It was one sentence in the "you decide" row of the `### When the answer is not an answer` table in `.claude/skills/expedition-prototype/SKILL.md`.

- **Before:** "Hand back one `DELEGATED` flag naming what you decided. This applies to that question only."
- **After:** "Hand back one `DELEGATED` flag naming what you decided. The human's delegation applies to that question only."

This is the checker's suggested wording. "that question" refers to the question the human answered with "you decide". Nothing else in the file changed.

**Did it touch what the condition names:** it touches only the rewritten range, which is the whole file, and only clause 8e's subject. It changes no rule, no fixed text, no heading and no shared section. Clause 12 still holds. `git diff --check` is clean, and `git status` still shows only that path. `wc -w` is now 2,035, up from 2,033, which is still 93% of the before-text's 2,176.

**Handover parts that differ:**

- **ANSWER, size bullet:** `wc -w` went from 2,176 to 2,035, which is 93%. Every other part of ANSWER is as first returned.
- **GATE PAYLOAD, checker findings:** checker run 1 returned `FAIL` on clause 8e, for one "This" without a referent in the "you decide" table row. I replaced it with "The human's delegation applies to that question only." The paths touched are unchanged: `.claude/skills/expedition-prototype/SKILL.md` only. The proposed commit message is unchanged.
- **RULE CHANGES, entry 19 (Table), row 2:** it now reads: "This covers **that question only** — the rest of the exchange stays with the human unless they say otherwise in as many words." became "The human's delegation applies to that question only. The rest of the exchange stays with the human unless they explicitly say otherwise." Same outcome, so it is not a rule change.
- **RE-POINTING SEARCH:** no change. None of the 89 conditions quotes "This covers" or "that question only" from this file. I already searched "that question only" as a handle.

Every other part is as first returned: INDEX LINE, FLAGS, NEW NODES, INVALIDATIONS, GENERALISATIONS and RETROSPECTIVE.

### Checker run 2 — `PASS`, under the amended condition

*The checker's own text, pasted, 2026-09-25.*

> PASS
>
> This is check 2 of node 293, "Rewrite the prototype contract in plain English". The clause 8e finding from run 1 is fixed, and the correction changes nothing else. The work now meets the acceptance condition and the bar, and I found no rule changes.
>
> My contract is the main-tree checker contract, unchanged since run 1. The acceptance condition is the full text sent for run 1, and the bar and ground rules are the same. The work is `.claude/skills/expedition-prototype/SKILL.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/293-rewrite-the-prototype-contract`, branch base `e64b3de`. I read the changed path only as the work.
>
> **What changed since run 1.** No statement of changes came with this check, so I compared the whole file against the run-1 text I read in full. There is one edit, at line 122, in the "you decide" row of `### When the answer is not an answer`:
> - Before: "This applies to that question only."
> - After: "The human's delegation applies to that question only."
>
> I found no other edit. The word count went from 2033 to 2035, which matches that one edit. The file has 219 lines.
>
> **Clause by clause**
> 1. **Lost or changed statements: met.** No rule change is found. The edit names the referent the sentence was meant to have. My run-1 comparison stands for the rest of the file, including the term *standing over sources*, which clause 1a allows dropping.
> 2. **Added statements: met.** Nothing is added. "Delegation" is ordinary English, not a new term, and the flag it goes with is still spelled `DELEGATED`.
> 3. **Generalisation: met.** My run-1 finding stands, and the edit does not affect this clause.
> 4. **Fixed text: met.** Re-run: the frontmatter and all code fences are byte-identical to the before-text.
> 5. **Headings: met.** Re-run: every heading is identical to the before-text.
> 6. **References inside the file: met**, as in run 1. The edit adds no reference.
> 7. **Terms: met**, as in run 1. The edit introduces no refused word.
> 8. **Plain English (outside the shared sections): met.**
>    - 8e: the run-1 instance now names its referent directly. The other pronouns I read in run 1 stand as judged.
>    - 8a, 8b, 8c, 8d and 8f are unaffected by the edit. Re-run: there are no semicolons outside the fences, and the same 17 bold terms appear.
> 9. **Size (reported, not enforced):** the rewritten range is the whole file. `wc -w` gives 2176 before and 2035 after, which is 94% of the before-text. The target of at most 1451 is missed, which does not fail the work.
> 10. and 11. **Scope: met.** `git status --porcelain --untracked-files=all` shows only `.claude/skills/expedition-prototype/SKILL.md` modified.
> 12. **The two shared sections are copies: met.** Re-run: both `## When you raise a flag` and `## When a node you report is an implementation node` are byte-identical to the same sections of `expedition-research/SKILL.md` at `e64b3de`, apart from blank lines at the section boundary.
>
> **RULE CHANGES** (for the file as it now stands)
>
> None found.
>
> How far the list reaches: I compared every statement of the before-text outside the two shared sections against the whole after-text. Clause 12 replaces clauses 1 to 3 for those two sections, so they are excluded. The comparison covered every rule and whose it is, every condition and exception, the four fixed templates, the defined terms, the refused words, and every closed list with its count:
> - the three things handed back
> - the five bullets of the discipline
> - the four table rows
> - the three conflicting skill instructions
> - the five handover parts
> - the two markers
> - the four things read
>
> This is the full run-1 comparison, with the one edit above read against the before-text.
>
> **The bar, re-run in full**
> - The repo has no build, tests, formatter or CI, and `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md`, in the same state as in run 1: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:** standing rule 5, `CONTEXT.md`'s `_Avoid_` lines, `/writing-for-agents`, and all five ground rules, which are met.
> - No reviewing skill is named, so I ran none.

*The manager's note, matching the two lists:* the checker found no rule change, and every entry on the worker's list is one the checker judged to keep its outcome.


### Gate — approve, 2026-09-25

The human, `verbatim`: *"approve"*

## Flags

`293.1` **· settled** `ASSUMPTION` — I kept "ask" for the prototype worker putting its own questions to the human. That covers the opening, the discipline's bullets 2, 3 and 5, and the replacement-attempt section, plus "ask me later" as the human's words in the table. `CONTEXT.md`'s Raise `_Avoid_` line refuses *ask* only for a raise. It names asking as "the ordinary mode of a worker built to question the human", and the prototype discipline is to show the probe and ask what it changes. This is the same reading node 291's gate approved for the grilling contract.
