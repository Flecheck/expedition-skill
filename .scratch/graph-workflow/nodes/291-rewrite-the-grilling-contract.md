# Rewrite the grilling contract in plain English

Type: implementation
Status: resolved
Blocked by: 290

## Question

Rewrite `.claude/skills/expedition-grilling/SKILL.md` in plain English and shorter, under the pass [node 289](289-a-plain-english-and-compaction-pass-over-the-shipped-files.md) settled.

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

11. **Scope.** The work changes `.claude/skills/expedition-grilling/SKILL.md` and no other path. The rewritten range is the whole file.
12. **The two shared sections are copies.** The after-text's sections headed `## When you raise a flag` and `## When a node you report is an implementation node` are byte-identical to the sections of the same headings in `.claude/skills/expedition-research/SKILL.md` as it stands at the commit this work's branch was created from. For those two sections, this identity takes the place of clauses 1 to 3 and 8. For the rest of the file, clauses 1 to 10 apply as written.

## Amendment by the human, 2026-09-24

*The human approved the manager's proposal, `verbatim`: "ok". The proposal and the answer to A that prompted it are recorded on [node 290](290-rewrite-the-research-contract-as-the-pilot.md). The manager drafted the wording below, and the human amended the condition with it. The original clauses above are left as they were. The clauses below take the place of clauses 1 and 2, add clause 1a, and add a sentence to clause 3.*

1. **Lost or changed statements are rule changes.** The binding statements are: every rule, meaning every instruction, permission, prohibition or duty, and whose it is; every condition or exception attached to a rule; every fixed template; every term the text defines, and its definition; every word the text refuses; and the members and stated count of every closed list. A binding statement of the before-text that has no counterpart anywhere in the whole after-text, or whose counterpart changes the outcome for any case, is a rule change. The checker lists every rule change it finds, each with the before-text statement and its after-text counterpart, or "removed". A rule change does not fail the work.
1a. **Terms `CONTEXT.md` does not define.** A term the before-text defines that `CONTEXT.md` does not define may be dropped as a term, where its meaning is still stated in plain words at the place it was defined. Dropping a term that way is not a rule change.
2. **Added statements are rule changes.** A rule, permission, duty, exception, defined term or refused word that the after-text states and the before-text does not is a rule change. The checker lists it the same way as under clause 1. It does not fail the work.
3. *(added sentence)* A generalisation that changes an outcome, or decides a case the before-text left undecided, is a rule change under clause 1 or clause 2.

## Answer

The grilling contract is rewritten in plain English at 91% of its length, with fences and headings kept, both shared sections copied byte-for-byte from the research contract, and no deliberate rule change.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The human approved the one rule change the checker listed, the dropped "in the same payload", under `### Checker run 1`. The work landed as commit `0a3e68b`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-25. The worker's own text, pasted. The flags are raised under `## Flags` at the gate.*

HANDOVER:      Rewrite the grilling contract in plain English

ANSWER:
`.claude/skills/expedition-grilling/SKILL.md` has been rewritten in plain English in the worktree `.scratch/graph-workflow/worktrees/291-rewrite-the-grilling-contract`, based on `724c361`. The changes are uncommitted.

- **Size.** `wc -w` went from 2,773 to 2,511, which is 91%. The two-thirds target (1,849) is missed. About 850 words are fixed text: the fences hold about 275 words and the two shared sections 576. Outside those, the prose went from about 1,800 to about 1,660 words. This file has more rules per word than the research, implementation and checker contracts, which landed at 86–88%: the reply-settling rules, the numbering rule and the four-row table. Going further would mean cutting rules.
- **Fixed text.** The frontmatter and all five fences are byte-identical to the before-text.
- **Shared sections (clause 12).** `## When you raise a flag` and `## When a node you report is an implementation node` are byte-identical to the research contract's sections at `724c361`. The research file has not changed since `4068519`. The only difference is the blank line before the next heading, the same as node 294's. This file's before-text of both sections was identical to the research before-text at `4068519^`, so every difference in them is one node 290 made and the human approved.
- **Headings (clause 5).** Every before-text heading is kept exactly.
- **Term list.** Every term is defined in `CONTEXT.md` (payload inside its Relay entry), so none was dropped. The file keeps its own list, as nodes 294 and 295 did.
- **Labels and idioms replaced.**
  - The label "standing over sources" was dropped under clause 1a and replaced by the pilot's plain description.
  - "in as many words" (3 places) became "explicitly".
  - The slogan "The graph-file ban is about recording, not about files" is gone. The rule is stated as hard rules 3 and 4, in the pilot's wording.
  - "the whole of what" (3 places) is gone.
  - Other figurative wording was reworded plainly: "hang off it", "branching", "keep your other questions moving", "while the exchange is live", "your recommendation lost … as though it had won", "what the reply reaches", "Each row reaches", "carry on", "per remaining call".
- **Other clauses.**
  - No semicolons outside fences.
  - Bold appears only on the terms at their definitions, and in the copied shared sections.
  - The refused-word grep finds only "ask". Each instance is a grilling worker asking the human (the ordinary mode that `CONTEXT.md`'s Raise `_Avoid_` line contrasts with a raise), the human's own words "ask me later" in the table, or fence text.
  - No method skill was run, so no part of one was skipped.

INDEX LINE:    The grilling contract is rewritten in plain English at 91% of its length, with fences and headings kept, both shared sections copied byte-for-byte from the research contract, and no deliberate rule change.

FLAGS:
ASSUMPTION: I kept "ask" for the grilling worker putting its own questions to the human (5 prose instances, plus "ask me later" as the human's words in the table). `CONTEXT.md`'s Raise `_Avoid_` line refuses *ask* only for the raise, and names asking as "the ordinary mode of a worker built to question the human". That is this worker. *Index:* The grilling contract keeps "ask" for its worker's questions, on the reading that the Raise `_Avoid_` line refuses it only for a raise and names asking as a grilling worker's ordinary mode.

NEW NODES:     none

INVALIDATIONS: none

GATE PAYLOAD:
- **Checker findings:** none yet.
- **Paths touched:** `.claude/skills/expedition-grilling/SKILL.md` only. My scratch copies and search scripts are outside the repo, in `/tmp/claude-1000/n291/` (`search.py`, `dump.py`, `phrases.txt`, `before.md`, `after.md`).
- **Bar:** the repo has no build, test, format or CI commands. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `map-implementation-rules.md` records none either. `git diff --check` is clean.
- **Proposed commit message:**
  ```
  Rewrite the grilling contract in plain English

  Node: graph-workflow/291
  ```

RULE CHANGES

I made no deliberate rule change and used no licence under ruling A. Every entry below is borderline: I judge that it keeps every outcome, and I list it so the checker's list can be matched against mine.

1. **Direct contact.**
   - Before (opening): "you never address the human directly. Every question you ask travels through the manager, which passes it along unaltered…"
   - After: "Every question you ask goes to the human through the manager. The manager passes it along unaltered and answers nothing itself." The prohibition is carried by hard rule 2's "Call no tool that addresses the human" and by the worker definition's "no direct contact with the human".
2. **Worker definition.** Before: "you. One node, no bookkeeping on the graph, no human." After: "…no direct contact with the human." "direct" comes from the before-text's opening, because the relay is contact.
3. **Park definition.** Before: "the human deferring, in as many words." After: "the human explicitly deferring." "banked" is kept as `CONTEXT.md`'s term.
4. **Payload definition.** Before: "awaiting one reply. It carries one of your questions or several, and it is one thing in front of the human either way." After: "carrying one or more of your questions and waiting for one reply. The human receives it as a single message."
5. **Verbatim.** Before: "the human's own words as they said them, against a paraphrase of them." After: "…as they said them. Its opposite is a **paraphrase** of them."
6. **Standing over sources.** The label was dropped under clause 1a, with its meaning in plain words where it was defined (the pilot's wording). This is not a rule change.
7. **Domain vocabulary.** Before: "The words above are the workflow's and hold either way." After: "The words defined under `## Words used exactly` hold either way." The ownership remark "are the workflow's" is removed. The rule that the words hold is kept.
8. **Hard rule 1.** Before: "You never answer one of your own questions on the human's behalf. Where they hand one back to you in as many words, see …" After: "Leave the answer to each of your questions to the human. Where the human explicitly hands a question back to you, follow `### When the answer is not an answer`." It is now stated only in the positive form.
9. **Hard rule 2.** Before: "You have no human-facing tool. Do not call one." After: "Call no tool that addresses the human." The claim of fact is removed and the rule stays, as at node 294. The payload sentence now names its shape's heading instead of "below".
10. **Hard rules 3 and 4.**
    - Before: the graph-file-ban passage ("…yours is to do your own work and never record it when you finish … not what this rule reaches — you make that change like any other work, and no other file with it"), and "You never resolve your node, never mark it, and never create another one. You hand your answer back and the manager writes it…"
    - After: "Put your work in what you hand back, and write no file. If your node's own work is a change to a graph file, make that change and change no other file." and "Leave all recording on the graph to the manager, whatever your node's work is. The manager writes your answer onto your node, marks it, resolves it, and writes its lines… Report a node you have found on your handover's `NEW NODES` part, and create no node yourself."
    - This is the research pilot's wording. "Put your work in what you hand back" may count as an added statement. It is the positive form of "write no file".
11. **Method skill.** Replaced by the pilot's wording. The reason "Such a skill was written for an agent working alone" is removed, and "Leave the conflicting part unrun" became "Skip the conflicting part".
12. **What binds you.**
    - Before: "The discipline below and the shapes under *What you hand back* are the whole of what binds you, and they bind whether or not any such skill is invoked. No part of them is supplied by a skill, waits on one, or changes according to whether one is present."
    - After: "What binds your work is the discipline below and the shapes under `## What you hand back`. They apply in full whether or not a method skill is invoked or present."
    - The literal exclusivity of "the whole of what" is dropped, as node 294 did with the same sentence.
13. **Closed list of the discipline.** Before: "This is the whole of the discipline:" After: "The discipline is the following, in full:". It still has five bullets. No count was added.
14. **Dependency order.**
    - Before: "a decision branching into the decisions that hang off it. So a question whose answer depends on one not yet asked waits for it."
    - After: "first a decision, then the decisions that depend on it. A question whose answer depends on a question not yet asked waits for that question."
    - I kept the before-text's ambiguity, where "waits for it" could mean waiting for it to be asked or to be answered.
15. **Payload membership.**
    - Before: "Two questions may share a payload only where neither's answer depends on the other's; one whose answer depends on another in the same payload is held for a later payload. There is no cap…, independence being the whole of what decides membership."
    - After: "One payload may carry any number of your questions. Two questions may share a payload exactly when neither's answer depends on the other's. Hold a question whose answer depends on another's for a later payload."
    - "exactly when" joins "only where" and "independence … decides membership".
16. **Facts.**
    - Before: "Finding facts is your own job and never the human's … keep your other questions moving … Ask only what no source can tell you."
    - After: "Find facts yourself. … Keep working on your other questions while that search runs. Ask the human only what no source can tell you."
    - "never the human's" is carried by the last sentence.
17. **Ambiguities.** "while the exchange is live" became "during the exchange".
18. **What you hand back.** Before: "Exactly one of three, and never two at once." After: "Each time you end your turn, hand back exactly one of the three shapes below."
19. **Single question.**
    - Before: "One payload, awaiting one reply, carrying one of your questions or several. One question, which is not numbered — numbering is itself the signal…"
    - After: "Hand back one payload. For one question, use the shape below and leave the question unnumbered, because a number signals that a payload holds more than one question."
    - What a payload waits for and carries is now stated only in the payload definition.
20. **Numbering.**
    - Before: "Numbers are never reused and never renumbered: a payload re-asking a question you asked earlier in this attempt uses that question's original number…"
    - After: "A question you asked earlier in this attempt keeps its original number when you ask it again. A question you ask for the first time takes the next number you have not yet used in this attempt. Never reuse or change a number, because a reply such as *"Q1 ok"* would then mean a different question in each payload."
    - I kept the qualifier "earlier in this attempt", so a question from an earlier attempt is not given back its old number.
21. **Assent and divergence.**
    - Before: "Then that option is what they endorsed, and you read it as theirs. Where `DIVERGENCE` is present, your recommendation lost: do not carry on as though it had won."
    - After: "Then read that option as the human's own choice. Where `DIVERGENCE` is present, the human's answer contradicts your recommendation. Continue from their answer, never as though your recommendation had been accepted."
22. **What a reply settles.** Before: "What a reply settles is what the reply reaches, and nothing else." After: "A reply settles what it covers and nothing else, under the following rules."
23. **Bare assent.** "*"ok for recommended"* and forms like it" became "such as *"ok for recommended"*".
24. **Unnamed question.** Before: "unanswered rather than deferred. It goes out in a later payload." After: "stays unanswered, and the human has not deferred it. Put it in a later payload."
25. **Parking.**
    - Before: "Parking is something they state. A question their reply simply failed to name is not a request to defer, and you never hand back park on that ground."
    - After: "Hand back park only when the human states that they defer. A reply that fails to name a question is not a request to defer that question."
26. **Reply form.**
    - Before: "You place no requirement on the form of their reply. Never ask them to number it, never tell them what shape to answer in, and expect no particular shape: numbering your own questions is the whole of what you do…"
    - After: "Accept a reply in whatever form the human writes it, and expect no particular form. Never tell them to number it or what shape to answer in. Numbering your own questions is all you do…"
    - Removed: "The rules above say what a reply means, and nothing here says what one will look like." It restated the sentences before it.
27. **Table.**
    - "carry on" became "continue".
    - "Return one `DELEGATED` flag" became "Hand back".
    - Row 2's "This covers **that question only** —" is removed. It is carried by "Each row applies only to what the reply names" and by the kept "The rest of the exchange stays with the human unless they explicitly say otherwise".
    - Row 3's "that question waits for a later payload" became "hold that question for a later payload".
    - Row 3's "Where what they defer is the payload itself" became "Where the human defers the whole payload". Both park cases are kept.
28. **Scope of a row.**
    - Before: "Each row reaches whatever the reply names: where a payload carried more than one question, a row governs the question the reply applied it to, and every other question in that payload is read under the rules above."
    - After: "Each row applies only to what the reply names. Read every other question in the same payload under the rules in `### question — you need the human`."
29. **Whole-node delegation.**
    - Before: "Whole-node delegation is said explicitly. Only then do you finish the node alone, with one `DELEGATED` flag per remaining call you make."
    - After: "Finish the node alone only when the human explicitly delegates the whole node. Then hand back one `DELEGATED` flag for each remaining decision you make."
30. **Handover.** Before: "Five parts, every time. … and never leave a part off." After: "Hand back all five parts every time. Write `none` in full for a part you have nothing for." "of this" became "of your handover", following the pilot.
31. **Park text.** Before: "Their words go here as they said them, never summarized." After: "Write the human's words here as they said them, without summarizing them."
32. **Replacement attempt.** Before: "Every question answered there is a settled fact. Never ask one of them again." After: "Treat every question answered there as settled, and never ask the human any of them again."
33. **Shared sections.** Replaced by the research contract's copies. Under clause 12 these are not rule changes.

Exception cases I checked against the before-text, all kept:
- Assent as the exception to reasoning from the human's words (1 case).
- Bare assent: settles the recommendations, and nothing that is not one.
- Park in row 3: 2 cases, the payload itself deferred and nothing left to continue with.
- "you decide": that question only, unless the human explicitly says otherwise.
- Hard rule 3: the graph-file exception.
- Method-skill conflicts: 3.
- Handed-back shapes: 3.
- Handover parts: 5.
- Markers: 2.
- The manager's recording acts: 4, which are marking, resolving and the lines in `decisions.md` and `flags.md`, plus writing the answer.
- Hard rules: still 5, in the same order and on the same subjects.

GENERALISATIONS
1. "They apply in full whether or not a method skill is invoked or present" replaces "they bind whether or not any such skill is invoked" and "No part of them is supplied by a skill, waits on one, or changes according to whether one is present".
2. "Two questions may share a payload exactly when neither's answer depends on the other's", with "any number", replaces "only where neither's answer depends on the other's", "There is no cap on how many a payload may carry" and "independence being the whole of what decides membership".
3. "Each row applies only to what the reply names" replaces the table row's "This covers **that question only**" and "Each row reaches whatever the reply names: where a payload carried more than one question, a row governs the question the reply applied it to".
4. Hard rules 3 and 4 (the pilot's wording) replace the before-text's graph-file-ban passage and hard rule 4's "You never resolve your node, never mark it, and never create another one. You hand your answer back and the manager writes it".
5. "Find facts yourself" together with "Ask the human only what no source can tell you" replaces "Finding facts is your own job and never the human's" and "Ask only what no source can tell you".

RE-POINTING SEARCH

**How I searched:**
- All 91 open or claimed nodes' `## Acceptance condition` sections, each with every `## Amendment…` section. The script is `/tmp/claude-1000/n291/search.py`. It collects every `## ` section whose heading starts with "Acceptance condition" or "Amendment", so a manager's note does not end the collection.
- (a) Every quoted span of 12 characters or more (backticks, `*…*`, straight or curly double quotes), normalised, found in the before-text, and checked for whether it survives in the after-text.
- (b) Six-word shingles shared between the before-text and each condition.
- (c) Mentions: `expedition-grilling`, grilling contract, grilling worker, five worker contracts, worker contracts, each of the five, all five, five contracts, every worker contract, hard rule 1 to 5, rule 3, three things, "exactly one of the three".
- (d) Every before-text heading, and the removed or replaced wording:
  - in as many words, travels through the manager, never address the human directly, no human, relayed message, awaiting one reply, one thing in front of the human, stay banked, against a paraphrase
  - Read each of these, is not yours. Leave it unread, standing over sources, domain vocabulary, The words above are the workflow's, hold either way
  - human-facing tool, Do not call one, entire final output, graph-file ban, about recording not about files, is not what this rule reaches, never record it when you finish, never resolve your node, never mark it, never create another one, Your final output is consumed by the manager
  - the hard rules govern, written for an agent working alone, collide with the rules above, unrun, the whole of what binds you, whether or not any such skill is invoked, supplied by a skill, whole of the discipline
  - dependency order, hang off it, held for a later payload, There is no cap, independence being, decides membership, a recommendation you believe, Finding facts is your own job, dispatch an agent of your own, keep your other questions moving, Ask only what no source can tell you, Small ambiguities you settle yourself, while the exchange is live
  - Exactly one of three, never two at once, numbering is itself the signal, visibly separated, fixed for the life of your attempt, never reused and never renumbered, re-asking, Renumbering per payload, Q1 ok, has read none of what you read, You are then resumed with, not a rendering of them, assent to one of the options, ok for recommended, your recommendation lost, as though it had won
  - what the reply reaches, unanswered rather than deferred, Parking is something they state, place no requirement on the form, Never ask them to number it, per-question answer, nothing here says what one will look like
  - carry on, that question only, Each row reaches, Whole-node delegation, per remaining call, Five parts every time, never leave a part off, Two markers are yours, The manager writes every part of this, Their words go here, never summarized, settled fact, Never ask one of them again, one of your questions or several, a later payload, the answer back
- A final grep over all conditions for grilling, payload, park, DELEGATED, relay, numbered and Q1.

**Replacement clauses:**
- **Node 109, the enumerator paragraph**, as amended by nodes 290 and 294. Replace "in `.claude/skills/expedition-research/SKILL.md` and `.claude/skills/expedition-implementation/SKILL.md`" with "in `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md` and `.claude/skills/expedition-grilling/SKILL.md`". I ran the recorded grep `grep -rlnE "against (those four|the four points above)" --include="*.md" .claude/` in the worktree, and it still returns the five worker contracts and no others. The `self-contained` grep still returns the same seven paths.
- **Node 109, clause 6**, as amended by node 294. Replace "or in the research and implementation contracts" with "or in the research, implementation and grilling contracts". The rest is unchanged.
- **Node 148, clause 1**, as amended by node 294. Replace it with: "the bullet beginning `A path may say where, because the checker has the repo` in `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md` and `.claude/skills/expedition-grilling/SKILL.md`, and in any of the five not yet rewritten, the bullet beginning `a **path** may say where`".
- **Node 155, the sentence before its clauses**, as amended by node 294. Replace it with: "Each carries a `## What you read` section opening `Read each of these. Do not trust any summary of them.`, or, in `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md` and `.claude/skills/expedition-grilling/SKILL.md`, `Read each of the following. Do not trust any summary of them.`, followed by a bulleted list of pointers and then a line stating that `flags.md` is not the worker's."
  - In the grilling file, the `flags.md` line ("Leave `flags.md` unread. It is not yours.") follows the list directly.
  - The decisions bullet ("`decisions.md` — the sections the spawn names") is byte-identical, so clauses 1, 3 and 4 still hold.
  - The old sentence had to go: under clause 8e, "these" may not point forward at a list.

**Matched, needing no change:**
- 279: amended clauses 1 and 3 quote the research after-text, which this file now holds byte-for-byte. Clause 2's conflict with byte-for-byte copying is still the manager's open item.
- 43: "`your answer contradicts`" is inside the fence. "Report `NEW NODES` and `INVALIDATIONS` yourself. Nothing else reports them." is kept word for word. The quantify rule is kept in the copied shared section.
- 55: "written by the node that spawned it" is kept.
- 304: "the standing preferences, the fog" is kept. Its recorded grep still returns the same four paths.
- 60: "Hand back all five parts every time" still states the count.
- 61: the opening and the handover paragraph still spell out that the manager passes text along unaltered and answers nothing itself.
- 41: "Two markers are yours" is kept, and the `FLAGS:` line is inside the fence.
- 292, 293, 301 and 302: they quote "in as many words" and "about recording, not about files" only as examples in their own clauses 8c and 8d.
- 134: its shingle hits come from `CONTEXT.md`'s grilling entry, which that node edits. It quotes nothing from this file.
- 73 and 79: they only require that this directory be left unchanged by their own work.
- 44, 81, 89, 96, 97, 111, 146, 228, 285, 312 and 127: hits on other files, or on the manager's own prose.

RETROSPECTIVE
1. **What I had to hunt for.**
   - Whether "ask" is refused for a grilling worker. I found it in `CONTEXT.md`'s Raise `_Avoid_` line, which names asking as the grilling worker's ordinary mode. I looked first at the manager's note in the spawn, which only said "check with care".
   - Whether this file's shared sections matched the research before-text. I checked with `git show 4068519^`.
   - Which conditions node 294 had already amended. Node 294's `RE-POINTING SEARCH` had the list, and I needed only the latest amendment of each.
2. **What arrived that this node did not need.**
   - Most of `map.md`. I needed one pointer and nothing from its long standing-preference items.
   - Of `map-implementation-rules.md`, I needed only rule 5.
   - Node 294's full review (about 360 lines), which I read as a model. Its `RULE CHANGES` and `RE-POINTING SEARCH` parts would have been enough.
   - A per-node list of "conditions last amended by the previous rewrite, and which clause" would have replaced most of my dump reading.
3. **What would have made it easier.**
   - One shared search script, which is node 313. Mine is a small variant of node 294's.
   - The spawn giving this file's fixed share (about 850 of 2,773 words) and a note that this file is denser in rules than the benchmarks.
4. **What was stale, wrong or contradictory.**
   - A pre-existing tension, kept as it was. Under "What a reply settles", bare assent names no question yet settles every recommendation, while the next rule says a question the reply does not name stays unanswered. Only the order of the bullets implies that the assent rule wins. A later node may want to state the precedence.
   - `map.md` still says `CONTEXT.md` is "moving" into `.claude/skills/expedition/`. It is still at the root, as node 294 also reported.

## Review

### Checker run 1 — `PASS`, under the amended condition

*The checker's own text, pasted, 2026-09-25. The checker was resumed from node 294's check.*

> PASS
>
> Node 291, "Rewrite the grilling contract in plain English", meets every clause of the amended acceptance condition, and the bar holds. I found one rule change, which does not fail the work. It rests on a literal reading of one sentence, and you may want to decide which reading is meant.
>
> My contract is the main-tree checker contract. It is unchanged since my last check: its last commit is `76e66e3` and it has no uncommitted edits. The work is `.claude/skills/expedition-grilling/SKILL.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/291-rewrite-the-grilling-contract`, branch base `724c361`. I read the changed path only as the work. Line numbers below are the after-text's.
>
> **Clause by clause**
> 1. **Lost or changed statements: met.** The one rule change is listed below. Dropping the term *standing over sources* is allowed by clause 1a: its meaning is still stated in plain words where it was defined ("by path or glob, which sources are authoritative, which are evidence only, and which hold statements known to be false"), and `CONTEXT.md` does not define it.
> 2. **Added statements: met.** Nothing is added. Several sentences restate the before-text in positive form, and I judged each to give the same outcome:
>    - "Put your work in what you hand back" is the positive form of "You write no file".
>    - "Leave the answer to each of your questions to the human" restates "You never answer one of your own questions on the human's behalf".
>    - "Each time you end your turn, hand back exactly one of the three shapes below" restates "Exactly one of three, and never two at once". A grilling worker hands back once per turn.
>    - "Continue from their answer, never as though your recommendation had been accepted" restates "do not carry on as though it had won".
> 3. **Generalisation: met**, except for the case listed as a rule change. Two merges give the same outcome:
>    - "Hand back park only when the human states that they defer" replaces "Parking is something they state … you never hand back park on that ground". The "ask me later" row still sends the human's stated deferral of a whole payload, or of the last question left, to park.
>    - "Two questions may share a payload exactly when neither's answer depends on the other's" merges the before-text's "only where" with "independence being the whole of what decides membership".
> 4. **Fixed text: met.** The frontmatter and all code fences are byte-identical to the before-text. That covers the two question shapes, the resume block, the handover and park.
> 5. **Headings: met.** Every heading is identical to the before-text.
> 6. **References inside the file: met.** Each one resolves:
>    - "listed under `## What you hand back`" and "the shapes under `## What you hand back`"
>    - "follow `### When the answer is not an answer`"
>    - "the shape under `### question — you need the human`" and "the rules in `### question — you need the human`", where the rules for what a reply settles are
>    - "The words defined under `## Words used exactly`"
>    - "the discipline below", "the three shapes below" and "the shape below"
> 7. **Terms: met.** The terms from `CONTEXT.md` are spelled as it defines them: relay, payload, attempt, park, banked, handover, flag, resolve, verbatim, paraphrase and grilling.
>    - "Ask" is not refused here. The `_Avoid_` line under **Raise** refuses it only for a raise and names asking as "the ordinary mode of a worker built to question the human", which is this worker.
>    - "Payload" names the relay's payload and not a handover.
>    - "Question" and "decision" are ordinary nouns, not names for the grilling kind.
>    - The before-text's "Return one `DELEGATED` flag" is now "Hand back one `DELEGATED` flag".
>    - No new term is coined.
> 8. **Plain English (outside the shared sections): met.**
>    - 8a: every negative rule has its positive form beside it. For example, "Call no tool that addresses the human" sits with "end your turn and make one payload your entire final output", and "Never reuse or change a number" sits with "Keep each question's number".
>    - 8b: bold appears only on "grilling" at its definition, on the word-list terms (including **paraphrase**, defined in the verbatim entry), and in the shared sections.
>    - 8c: both instances of "in as many words" are now "explicitly". "One thing in front of the human" is now "a single message". I found no other figure of speech.
>    - 8d: I found no slogan-shaped sentence, and "the whole of what" does not appear.
>    - 8e: I read every it, this, that, they, these, those and them. Each has one clear referent in its own sentence or the one before.
>    - 8f: no semicolons outside the fences. Each dash is a list separator or part of a heading name.
> 9. **Size (reported, not enforced):** the rewritten range is the whole file. `wc -w` gives 2773 before and 2511 after, which is 91% of the before-text. The target of at most 1849 is missed, which does not fail the work.
> 10. and 11. **Scope: met.** `git status --porcelain --untracked-files=all` shows only `.claude/skills/expedition-grilling/SKILL.md` modified.
> 12. **The two shared sections are copies: met.** Both `## When you raise a flag` and `## When a node you report is an implementation node` are byte-identical to the same sections of `expedition-research/SKILL.md` at `724c361`, apart from blank lines at the section boundary. The research file is unchanged between the base and master.
>
> **RULE CHANGES**
> 1. **A condition dropped from the rule for holding a question (literal reading).**
>    - Before, under `## How you grill`: "one whose answer depends on another in the same payload is held for a later payload."
>    - After, line 85–86: "Hold a question whose answer depends on another's for a later payload."
>    - The phrase "in the same payload" is gone. Read literally, the rule now also holds a question whose answer depends on a question already answered in an earlier payload. The before-text let such a question go out now.
>    - A question that depends on one not yet asked waits under either text, because the first bullet ("waits for that question") covers it.
>    - The sentence just before the new one is about two questions sharing a payload, so the intended reading is probably the same as before. I list it because the words themselves no longer carry the condition.
>
> How far the list reaches: I compared every statement of the before-text outside the two shared sections against the whole after-text. Clause 12 replaces clauses 1 to 3 for those two sections, so they are excluded. The comparison covered:
> - every rule and whose it is, and every condition and exception
> - the five fixed templates and the defined terms
> - the refused words
> - every closed list with its count: the three things handed back, the five bullets of the discipline, the four rows of `### When the answer is not an answer`, the three conflicting skill instructions, the five handover parts, the two markers, and the three things read
>
> I found no rule change beyond the one listed.
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, the bar, the review route, the five ground rules and the five standing rules for writing. The file has the same one-line uncommitted `.gitignore` note in the bar paragraph that I reported for node 294. It does not change what the bar requires.
> - **Standards that bore on this work:** standing rule 5 (plain English), `CONTEXT.md`'s `_Avoid_` lines, `/writing-for-agents`, and all five ground rules, which are met. On ground rule 3, questions go to the human "through the manager", and hard rule 2 says "Call no tool that addresses the human".
> - No reviewing skill is named, so I ran none.

*The manager's note, matching the two lists:* the checker's one rule change is the worker's entry 15 (payload membership), which quotes the same after-text sentence. The worker judged it to keep its outcome, and the checker reads it literally as dropping "in the same payload". Every other entry on the worker's list the checker judged to keep its outcome.


### Gate — approve, 2026-09-25

The human, `verbatim`: *"approve"*. *The manager's note:* the manager's gate payload offered approve, correct (restoring "in the same payload") or reject. The human took approve, so the checker's one listed rule change stands.

## Flags

`291.1` **· settled** `ASSUMPTION` — I kept "ask" for the grilling worker putting its own questions to the human (5 prose instances, plus "ask me later" as the human's words in the table). `CONTEXT.md`'s Raise `_Avoid_` line refuses *ask* only for the raise, and names asking as "the ordinary mode of a worker built to question the human". That is this worker.
