# Rewrite the precondition contract in plain English

Type: implementation
Status: resolved
Blocked by: 290

## Question

Rewrite `.claude/skills/expedition-precondition/SKILL.md` in plain English and shorter, under the pass [node 289](289-a-plain-english-and-compaction-pass-over-the-shipped-files.md) settled.

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

11. **Scope.** The work changes `.claude/skills/expedition-precondition/SKILL.md` and no other path. The rewritten range is the whole file.
12. **The two shared sections are copies.** The after-text's sections headed `## When you raise a flag` and `## When a node you report is an implementation node` are byte-identical to the sections of the same headings in `.claude/skills/expedition-research/SKILL.md` as it stands at the commit this work's branch was created from. For those two sections, this identity takes the place of clauses 1 to 3 and 8. For the rest of the file, clauses 1 to 10 apply as written.

## Amendment by the human, 2026-09-24

*The human approved the manager's proposal, `verbatim`: "ok". The proposal and the answer to A that prompted it are recorded on [node 290](290-rewrite-the-research-contract-as-the-pilot.md). The manager drafted the wording below, and the human amended the condition with it. The original clauses above are left as they were. The clauses below take the place of clauses 1 and 2, add clause 1a, and add a sentence to clause 3.*

1. **Lost or changed statements are rule changes.** The binding statements are: every rule, meaning every instruction, permission, prohibition or duty, and whose it is; every condition or exception attached to a rule; every fixed template; every term the text defines, and its definition; every word the text refuses; and the members and stated count of every closed list. A binding statement of the before-text that has no counterpart anywhere in the whole after-text, or whose counterpart changes the outcome for any case, is a rule change. The checker lists every rule change it finds, each with the before-text statement and its after-text counterpart, or "removed". A rule change does not fail the work.
1a. **Terms `CONTEXT.md` does not define.** A term the before-text defines that `CONTEXT.md` does not define may be dropped as a term, where its meaning is still stated in plain words at the place it was defined. Dropping a term that way is not a rule change.
2. **Added statements are rule changes.** A rule, permission, duty, exception, defined term or refused word that the after-text states and the before-text does not is a rule change. The checker lists it the same way as under clause 1. It does not fail the work.
3. *(added sentence)* A generalisation that changes an outcome, or decides a case the before-text left undecided, is a rule change under clause 1 or clause 2.

## Answer

The precondition contract is rewritten in plain English at 93% of its length. Fences and headings are kept, the shared sections are copied from the research contract, and one deliberate rule change is made, to hard rule 4.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`, as changed by its addendum and correction round 1. The checker found no rule change under `### Checker run 2`, and judged the worker's R1 to keep its outcome. The human approved. The work landed as commit `ede2c76`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-25. The worker's own text, pasted. The flags are raised under `## Flags` at the gate. The manager's later instruction to phrase list amendments as additions reached the worker after it had handed back.*

HANDOVER:      Rewrite the precondition contract in plain English

ANSWER:
`.claude/skills/expedition-precondition/SKILL.md` is rewritten in plain English in the worktree `.scratch/graph-workflow/worktrees/292-rewrite-the-precondition-contract`, based on `0a3e68b`. The changes are uncommitted.

- **Size.** `wc -w` went from 2,218 to 2,053, which is 93%. The two-thirds target (1,479) is missed. The fences hold 232 words and are unchanged. The two shared sections went from 700 to 576 words, because they are now copies of the research contract's. The rest of the prose went from 1,286 to 1,245 words. That prose was already short, and most of it is rules, tables and the shape descriptions.
- **Fixed text.** The frontmatter and all four fences are byte-identical to the before-text.
- **Shared sections (clause 12).** `## When you raise a flag` and `## When a node you report is an implementation node` are byte-identical to the research contract at `0a3e68b`, checked by extracting each section from both files and comparing them.
- **Headings (clause 5).** Every before-text heading is kept exactly. `diff` of the heading lines is empty.
- **Term list.** The file keeps its own list, as nodes 291, 294 and 295 did. Every term on it is defined in `CONTEXT.md`, so none was dropped. The shared definitions use the wording of the rewritten contracts: node, manager, worker (grilling's "no direct contact"), resolve, verbatim.
- **Labels dropped under clause 1a and ruling B.** "standing over sources" is replaced by the pilot's plain description. "pick report" is replaced by "the report the manager sends the human when your node closes". The bold labels **continue** and **stop** became plain list items, as node 294 did. Bold was also removed from "attempt", which the before-text bolded but never defined.
- **Idioms and slogans replaced.** "Drive it yourself", "in as many words" (now "explicitly"), "The graph-file ban is about recording, not about files" (now hard rules 1 and 2 in the pilot's wording), "not what this rule reaches", "upstream of yours", "reaches past this node", "a genuine fork", "carry on", "keep going", "first human moment your node's close reaches", "settled cold", "meets your node", "rather than tidy".
- **Other clauses.** There are no semicolons outside fences. Bold appears only on terms where they are defined. No prose sentence outside the term list holds a dash aside. In-file references now name headings (`## What you hand back`, `### When the answer is not an answer`) instead of "below" or italics. The refused-word grep finds only "ask me later" (the human's words in the table), the fixed `ASK:` line, and "done" in its ordinary sense ("could not be done", "a step ... as done", and the fixed heading "the work is done"). No sentence of the worker's own uses "ask".
- **Bar.** The repo has no build, test, format or CI commands. Its root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `map-implementation-rules.md` records none either. `git diff --check` is clean. The recorded enumerators of nodes 109 and 148 still return what those conditions expect: 5 paths for the read-back grep, 7 for `self-contained`, and 0 absolute paths.
- **Method skill.** None exists for this kind, and none was run.

INDEX LINE:    The precondition contract is rewritten in plain English at 93% of its length. Fences and headings are kept, the shared sections are copied from the research contract, and one deliberate rule change is made, to hard rule 4.

FLAGS:
ASSUMPTION: I dropped the label "pick report" under ruling B and clause 1a. `CONTEXT.md` uses the phrase inside its Flag and Raise entries but has no entry for it, and this file defined it in bold. Its meaning stays in plain words at the same place: "the report the manager sends the human when your node closes". `expedition/SKILL.md` and `graph-conventions.md` still use the term, and node 137 plans to rename it. I have proposed an amendment to node 137 so that its rename covers this periphrasis. *Index:* The precondition contract no longer says "pick report". It describes that report in plain words, on the reading that `CONTEXT.md` has no entry for the term.

NEW NODES:     none

INVALIDATIONS: none

GATE PAYLOAD:
- **Checker findings:** none yet.
- **Paths touched:** `.claude/skills/expedition-precondition/SKILL.md` only. My scratch files are outside the repo in `/tmp/claude-1000/n292/`: `before.md`, `after.md`, `shared.md`, `search.py`, `dump.py`, `phrases.txt`, and the results `q.txt`, `n.txt` and `p.txt`.
- **Proposed commit message:**
  ```
  Rewrite the precondition contract in plain English

  Node: graph-workflow/292
  ```

RULE CHANGES

**Deliberate, under ruling A (one change):**

R1. **Hard rule 4, the output when the worker needs the human.**
- Before: "When you need the human, end your turn and make the checklist your entire final output, in the shape below."
- After: "When you need the human, end your turn and make your entire final output the question shape under `## What you hand back`. Call no tool that addresses the human."
- Why it makes sense in the file: the question shape's heading is "the human has to do something, or decide something", and its `ASK` holds "one question, or one checklist". Read literally, the before-text sent every need of the human out as "the checklist". That left a decision question with no stated output. The after-text sends both through the one shape the file defines for them.

**Borderline changes. I judge that each keeps every outcome, and I list them so the checker's list can be matched against mine:**

R2. **Opening, direct contact.**
- Before: "You are not the manager, and you never address the human directly. Everything that reaches them travels through the manager, which passes it along unaltered and answers nothing itself."
- After: "…and you are not its manager. … Everything the human receives from you goes through the manager. The manager passes it along unaltered and answers nothing itself."
- The ban on direct address is now stated by hard rule 4 ("Call no tool that addresses the human") and by the worker definition ("no direct contact with the human"). "from you" was added. It names the worker's own output, which is what the before-text's "them … reaches" meant in context.

R3. **"Drive it yourself wherever you can."**
- After: "Do the work yourself wherever you can." The checklist sentence keeps its three examples, now as gerunds, and it keeps "through the relay and wait".

R4. **Worker definition.**
- Before: "you. One node, no bookkeeping on the graph, no human."
- After: "you, working one node with no bookkeeping on the graph and no direct contact with the human." This is grilling's wording, because the relay is contact.

R5. **Park definition.** The bold was removed from "attempt", a word the before-text bolded but never defined. The word stays.

R6. **Verbatim.**
- Before: "…as they said them, against a **paraphrase** of them."
- After: "…as they said them. Its opposite is a **paraphrase** of them."

R7. **Resolve.**
- Before: "The manager's act, never yours."
- After: "It is the manager's act, never yours."

R8. **`## What you read` list.**
- Before: 3 bullets, the first being "your node's own file — its `## Question` first, then what the spawn says must be true when you are finished, and which resulting facts later nodes depend on".
- After: 4 bullets. The first, "your node's own file — its `## Question` first", is followed by "what the spawn says must be true when you are finished, and which resulting facts later nodes depend on".
- The list states no count. Its members and their order are the same. The `map.md` and `decisions.md` bullets are byte-identical.
- "Read each of these." became "Read each of the following."
- "`flags.md` is not yours. Leave it unread." became "Leave `flags.md` unread. It is not yours."

R9. **Standing over sources, and bold "ground rules".** The label was dropped under clause 1a and replaced with the pilot's plain description. Under clause 1a this is not a rule change.

R10. **Hard rule 1.**
- Before: "You write no product code and no graph file. Where the work itself requires a file — … — write it and say so in your handover." It was followed by the slogan passage, whose content was: bookkeeping is the manager's job, never record your work when you finish, and a node whose own work is a change to a graph file makes that change "like any other work".
- After: "Where the work itself requires a file, such as a configuration, a directory or an installed dependency, write it and say so in your handover. Write no product code. Write a graph file only where your node's own work is a change to that file."
- "never record it when you finish" is carried by hard rule 2's "Leave all recording on the graph to the manager".

R11. **Hard rule 2.**
- Before: hard rule 1's last sentence ("Marking your node, resolving it, and its lines in `decisions.md` and `flags.md` stay the manager's whatever your node's work is"), and hard rule 2 ("You never resolve your node, never mark it, and never create another one. You hand your answer back and the manager writes it, and a node you have found is reported on your handover's `NEW NODES` part rather than created as a file").
- After (the pilot's wording): "Leave all recording on the graph to the manager, whatever your node's work is. The manager writes your answer onto your node, marks it, resolves it, and writes its lines in `decisions.md` and `flags.md`. Report a node you have found on your handover's `NEW NODES` part, and create no node yourself."

R12. **Hard rule 3.**
- Before: "You never answer your own question on the human's behalf, and you never carry out a step yourself that the node reserved for them. Where they hand a question back to you in as many words, see *When the answer is not an answer*."
- After: "Leave to the human the answer to your own question and every step the node reserved for them. Where the human explicitly hands a question back to you, follow `### When the answer is not an answer`."

R13. **Hard rule 4, the tool clause.**
- Before: "You have no human-facing tool. Do not call one."
- After: "Call no tool that addresses the human." The claim of fact is removed and the rule stays, as at nodes 291 and 294.
- The file still has 5 hard rules, in the same order and on the same subjects.

R14. **Hard rule 5.**
- Before: "Your final output is consumed by the manager."
- After: "Write your final output for the manager to consume."

R15. **Triggers.**
- Before: "**Raise** when any one of these holds:" and "One trigger is enough."
- After: "Raise if any one of the three triggers in the table below holds."
- Table rows:
  - "a resolved node upstream of yours" became "a resolved node your node depends on".
  - "the decision reaches past this node" became "the decision affects more than this node".
  - "a genuine fork where you hold no recommendation you believe" became "because the choice is genuinely open and you hold no recommendation you believe".
  - The rows are still unnumbered and still three.

R16. **Raise shape.**
- Before: "A raise is not a fourth thing to hand back: it is the question shape under *What you hand back*, used for a broken premise rather than for a step of the work. Hand it back, then stop and wait."
- After: "To raise, hand back the question shape under `## What you hand back`, about the broken premise instead of a step of the work. Then stop and wait."
- "not a fourth thing" is now carried by "hand back exactly one of the three shapes below". It is no longer stated on its own.

R17. **Answers to a raise.**
- Before: "**continue**, and you carry on; or **stop**, and you are finished, writing nothing further and handing nothing further back."
- After: two list items. "Continue. Resume the work." and "Stop. You are finished. Write nothing more, and hand nothing more back." The bold labels were dropped.

R18. **Below the triggers.**
- Before: "Below all three triggers: decide it, keep going, and return one `ASSUMPTION` flag. It settles at the **pick report** the manager sends when your node closes, which is the first human moment your node's close reaches. Write it short and plain enough to be settled cold: that report is where the human meets your node for the first time."
- After: "Where none of the three triggers holds, decide the matter yourself, continue the work, and hand back one `ASSUMPTION` flag. The flag settles at the report the manager sends the human when your node closes. That report is where the human first sees your node, so write the flag short and plain enough to be settled without reading anything else."
- The "pick report" label was dropped under clause 1a. The clause "which is the first human moment your node's close reaches" was removed as explanation of why. The rule, that the flag settles at that report, is kept.

R19. **What you hand back.**
- Before: "Exactly one of three, and never two at once."
- After: "Each time you end your turn, hand back exactly one of the three shapes below." This is grilling's wording.

R20. **ABOUT and SO FAR.**
- Before: "The human has read none of what you read. Write `ABOUT` and `SO FAR` every time, the first one included."
- After: "Write `ABOUT` and `SO FAR` every time you hand back this shape, the first time included, because the human has read none of what you read."

R21. **Table in `### When the answer is not an answer`.**
- "carry on" became "continue" (rows 1, 2 and 4).
- "Return one `DELEGATED` flag" became "Hand back one".
- Bold was removed from "that question only" and from "park".
- "carry on against the new one" became "continue with the new question".

R22. **Handover parts.**
- Before: "Five parts, every time. … and never leave a part off."
- After: "Hand back all five parts every time. Write `none` in full for a part you have nothing for."

R23. **Resulting facts.**
- Before: "gets those resulting facts from `ANSWER` and from nowhere else."
- After: "finds the resulting facts in `ANSWER` and nowhere else."

R24. **Shortfall.**
- Before: "`ANSWER` says what and how far you got, and leaves the shortfall visible rather than tidy."
- After: "say in `ANSWER` what it was and how far you got, and leave the shortfall visible."

R25. **Markers and the manager's writing.**
- Commas were added to the markers sentence.
- "every part of this" became "every part of your handover", followed by "So write `ANSWER`…", as in the pilot.

R26. **Park text.**
- Before: "Their words go here as they said them, never summarized."
- After: "Write the human's words here as they said them, without summarizing them."

R27. **Replacement attempt.**
- Before: "Everything the human already said there is a settled fact, and any step they already took is done. Never put one of them back to them."
- After: "Treat everything the human already said there as settled, and every step they already took as done. Never put a question the human answered there, or a step they took there, to the human again."

R28. **Shared sections.** These are replaced by the research contract's copies. Under clause 12 this is not a rule change. For the record, the copies no longer carry these before-text sentences, which node 290 removed and the human approved: "You are the party that holds what it takes…", "Its cap is stated here so you need not open the file", "it never writes your sentence for you", and "never as a tidy-up afterwards".

I checked these counts and cases against the before-text, and all are kept:
- 3 handed-back shapes
- 5 handover parts
- 2 markers
- 3 triggers
- 2 answers to a raise
- 4 table rows
- 5 hard rules
- the graph-file exception
- the manager's recording acts: writing the answer, marking, resolving, and the lines in `decisions.md` and `flags.md`
- "that question only" for "you decide"

GENERALISATIONS
1. Hard rule 2 ("Leave all recording on the graph to the manager, whatever your node's work is…") replaces three statements:
   - the before-text's "Bookkeeping on the graph is the manager's job; yours is to do your own work and never record it when you finish"
   - hard rule 1's "Marking your node, resolving it, and its lines … stay the manager's whatever your node's work is"
   - hard rule 2's "You never resolve your node, never mark it, and never create another one. You hand your answer back and the manager writes it"
2. "Write a graph file only where your node's own work is a change to that file" replaces "You write … no graph file" and "a node whose own work is a change to a graph file is not what this rule reaches — you make that change like any other work".
3. "Raise if any one of the three triggers in the table below holds" replaces "Raise when any one of these holds" and "One trigger is enough."
4. "hand back exactly one of the three shapes below", with "To raise, hand back the question shape", replaces "never two at once" and "A raise is not a fourth thing to hand back".

RE-POINTING SEARCH

**How I searched.**
- I searched all 90 open or claimed nodes other than 292. For each, the script took the `## Acceptance condition` section and every `## Amendment…` section, wherever it sits. The script is `/tmp/claude-1000/n292/search.py`, adapted from node 291's.
- (a) Every quoted span of 12 characters or more, normalised, that is found in the before-text, checked for whether it survives in the after-text.
- (b) Six-word shingles shared between the before-text and each condition.
- (c) The phrase list in `/tmp/claude-1000/n292/phrases.txt`, about 130 handles:
  - file mentions: `expedition-precondition`, precondition contract/worker/node, five worker contracts, each of the five, all five
  - counts and positions: hard rule 1 to 5, rule 3, rule 4, item 1 to 4, three things, "exactly one of the three", "Exactly one of three", never two at once
  - every before-text heading
  - every removed or replaced phrase: Drive it yourself, only a person can take, precise checklist, travels through the manager, never address the human directly, no human, standing over sources, ground rules, human-facing tool, Do not call one, entire final output, graph-file ban, about recording not about files, not what this rule reaches, never record it when you finish, like any other work, never resolve your node, never mark it, never create another one, rather than created as a file, on the human's behalf, reserved for them, in as many words, make the checklist, in the shape below, consumed by the manager, no method skill, One trigger is enough, upstream of yours, reaches past this node, genuine fork, not a fourth thing, carry on, writing nothing further, Below all three triggers, keep going, pick report, first human moment, settled cold, meets your node for the first time, the first one included, that question only, Five parts every time, never leave a part off, from nowhere else, shortfall visible rather than tidy, The manager writes every part of this, Their words go here, never summarized, settled fact, Never put one of them back
  - the removed shared-section phrases: the party that holds what it takes, never writes your sentence, Its cap is stated here, two caps, report-shaped, read cold, quantifies over the record, paid for there, against those four, a **path** may say where, self-contained text, the demand itself, copy into
- I re-ran the recorded enumerators of nodes 109, 148 and 304 in the worktree.

**Replacement clauses:**
- **Node 109, the enumerator paragraph**, as amended by node 291. Replace "in `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md` and `.claude/skills/expedition-grilling/SKILL.md`" with "in `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-grilling/SKILL.md` and `.claude/skills/expedition-precondition/SKILL.md`". The recorded grep `grep -rlnE "against (those four|the four points above)" --include="*.md" .claude/` still returns the five worker contracts and no others. The `self-contained` grep still returns the same seven paths.
- **Node 109, clause 6**, as amended by node 291. Replace "or in the research, implementation and grilling contracts" with "or in the research, implementation, grilling and precondition contracts". The rest is unchanged.
- **Node 148, clause 1**, as amended by node 291. Replace it with: "the bullet beginning `A path may say where, because the checker has the repo` in `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-grilling/SKILL.md` and `.claude/skills/expedition-precondition/SKILL.md`, and in any of the five not yet rewritten, the bullet beginning `a **path** may say where`". Clause 3's grep still returns 0.
- **Node 155, the sentence before its clauses**, as amended by node 291. Replace it with: "Each carries a `## What you read` section opening `Read each of these. Do not trust any summary of them.`, or, in `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-grilling/SKILL.md` and `.claude/skills/expedition-precondition/SKILL.md`, `Read each of the following. Do not trust any summary of them.`, followed by a bulleted list of pointers and then a line stating that `flags.md` is not the worker's."
  - For the manager's note: in the precondition file the `flags.md` line ("Leave `flags.md` unread. It is not yours.") follows the list directly. The list now has four bullets, because the node-file bullet was split in two. The decisions bullet is byte-identical, so clauses 1, 3 and 4 still hold.
- **Node 137, clause 6.** The precondition file's one `pick report` is gone, so the recorded grep now finds nothing in that file. The same message is still named there by a periphrasis. Proposed addition after clause 6's last sentence: "`.claude/skills/expedition-precondition/SKILL.md` no longer says `pick report`. It reads *"The flag settles at the report the manager sends the human when your node closes."* That phrase names the node-level report, and it is replaced by the node-level term." The file stays in node 137's scope list, so no other clause changes.

**Matched, needing no change:**
- 304: "the standing preferences, the fog" is kept. Its grep still returns the same four paths.
- 43: the `INVALIDATIONS:` line with "your work contradicts" is inside the fence. "Report `NEW NODES` and `INVALIDATIONS` yourself. Nothing else reports them." is kept word for word. The rule against quantifying over the record is kept in the copied shared section.
- 55: "written by the node that spawned it" is kept, and so is the instruction that follows it.
- 279: its amended clause 1 quotes the research after-text, which this file now holds byte for byte. Clause 2 is still the manager's open item.
- 60: "Hand back all five parts every time" still states the count.
- 61: the opening and the handover paragraph still say that the manager passes text along unaltered and answers nothing itself.
- 41: no quote. The markers sentence and the `FLAGS:` line are kept.
- 57: it asks for the research raise "in the same terms as" this file and quotes nothing from it. For its worker's information, this file no longer states "not a fourth thing" in so many words. It is carried by "exactly one of the three shapes".
- 312: every heading is kept.
- 73 and 79: they only forbid their own work from changing this directory.
- 293, 301 and 302: they quote "in as many words" and "about recording, not about files" only as examples in their own clauses 8c and 8d.
- 111, 228 and 97: their "standing over sources" hits are about `graph-conventions.md` and were already amended by node 299.
- 118, 156 and 309: their "pick report" hits are about `expedition/SKILL.md`, `decisions.md` and `graph-conventions.md`.
- 44, 81, 87, 96, 105, 127, 146, 149, 151, 152, 160, 161, 190, 226, 230, 232, 234, 247, 258, 271, 276, 280, 284, 285, 287 and 288: hits on other files, on generic words ("decisions.md", "three things", "item 4"), or on the manager's own prose.

RETROSPECTIVE
1. **What I had to hunt for.**
   - Whether "pick report" counts as a `CONTEXT.md` term. I grepped `CONTEXT.md` and found it only inside the Flag and Raise entries, with no entry of its own. I then grepped `.claude/`, which led me to node 137's rename plan through the search.
   - Nodes 109, 148 and 155's latest amendments. I found them by listing each node's `## ` headings, as the spawn suggested.
2. **What arrived in my context that this node did not need.**
   - Most of `map.md`, about 50 KB. I used none of its standing preferences.
   - Of `map-implementation-rules.md`, I needed only rule 5 and the bar line.
   - Node 291's full handover, about 200 lines, which I read as a model. Its RULE CHANGES and RE-POINTING SEARCH headings alone would have done.
   - A different arrangement that would avoid this: the spawn could give the exact `sed` ranges, or the manager could keep a short file of the latest amendment clause per re-pointed node.
3. **What would have made it easier.**
   - One shared search script with the node number as an argument, which is node 313. I copied and edited node 291's.
   - A note in the spawn that "pick report" appears in `CONTEXT.md` prose without an entry, and that node 137 renames it. That would have settled the ruling-B question at once.
4. **What was stale, wrong or contradictory.**
   - This file defines "verbatim" and "paraphrase" but never uses either word elsewhere. It is harmless, and I kept it for consistency with the grilling contract. A later node could remove the definition from both files.
   - Before the rewrite, hard rule 4 ("make the checklist your entire final output") did not fit the question shape's own heading ("or decide something"). R1 fixes that.
   - `map.md` still says a spawn-carried retrospective is the "sixth" part on five-part handovers, which is consistent. I found nothing else stale.

### Addendum — list amendments rephrased as additions

*The worker's own text, pasted, 2026-09-25, sent after its handover in answer to the manager's instruction.*

Node 292 addendum: the amendments for nodes 109, 148 and 155, rephrased as additions as you asked. Your instruction arrived after my handover had been delivered, so this message replaces the first four bullets of the handover's RE-POINTING SEARCH "Replacement clauses". Everything else in the handover stands, including the node 137 proposal and the "Matched, needing no change" list.

- **Node 109, the enumerator paragraph**, as amended by node 291. In the list of files that hold *"against the four points above"*, add `.claude/skills/expedition-precondition/SKILL.md`. The recorded grep `grep -rlnE "against (those four|the four points above)" --include="*.md" .claude/` still returns the five worker contracts and no others. The `self-contained` grep still returns the same seven paths.
- **Node 109, clause 6**, as amended by node 291. In the list of contracts whose read-back sentence reads *"check what you wrote against the four points above"*, add the precondition contract. The rest is unchanged.
- **Node 148, clause 1**, as amended by node 291. In the list of files where the bullet begins `A path may say where, because the checker has the repo`, add `.claude/skills/expedition-precondition/SKILL.md`. Clause 3's grep still returns 0.
- **Node 155, the sentence before its clauses**, as amended by node 291. In the list of files whose `## What you read` section opens `Read each of the following. Do not trust any summary of them.`, add `.claude/skills/expedition-precondition/SKILL.md`.
  - For the manager's note: in the precondition file the `flags.md` line ("Leave `flags.md` unread. It is not yours.") follows the list directly. The list now has four bullets, because the node-file bullet was split in two. The decisions bullet is byte-identical, so clauses 1, 3 and 4 still hold.

Each quoted wording is present in the after-text at `.scratch/graph-workflow/worktrees/292-rewrite-the-precondition-contract/.claude/skills/expedition-precondition/SKILL.md`.

## Review

### Checker run 1 — `FAIL`, acceptance condition (as amended by the human)

*The checker's own text, pasted, 2026-09-25. The checker was resumed from node 291's check, and resumed again after a usage-limit stop.*

> FAIL: acceptance condition
>
> Node 292, "Rewrite the precondition contract in plain English", fails on one sentence under clause 8e. Everything else is met, I found no rule changes, and the bar holds. The fix is a one-sentence rewording.
>
> My contract is the main-tree checker contract. It is unchanged since my last check: its last commit is `76e66e3` and it has no uncommitted edits. The work is `.claude/skills/expedition-precondition/SKILL.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/292-rewrite-the-precondition-contract`, branch base `0a3e68b`. I read the changed path only as the work.
>
> The acceptance condition reached me partly by reference: "word for word the condition you held for node 291", with clause 11 given in full. I hold node 291's condition text as it was copied to me, so I checked against that text with clause 11 replaced. Line numbers below are the after-text's.
>
> **Finding: clause 8e, a "this" with no clear referent (1 instance)**
> - **Instance:** line 125, in the "you decide" row of the `### When the answer is not an answer` table: "decide it and continue. Hand back one `DELEGATED` flag naming what you decided. This covers that question only."
>   - The sentence just before names only the `DELEGATED` flag. The intended referent is the human's "you decide", which is in the other cell of the row and outside that window.
>   - Read with the flag as the referent, the sentence no longer says what it is meant to say: that the delegation reaches only that question and the rest stays with the human.
>   - The before-text has the same sentence. The rewrite is still held to 8e for it, because the rewritten range is the whole file.
>   - Wording such as "The human's delegation covers that question only" would meet the clause.
> - **Form:** a "this", "that", "these" or "those" whose intended referent is not in its own sentence or the one before, outside the two shared sections and outside code fences.
> - **Extent (bounding set):** every hit of `awk '/^```/{f=!f;next} !f{print NR": "$0}' .claude/skills/expedition-precondition/SKILL.md | grep -i -w -E 'it|this|that|they|these|those'` outside lines 170–218, which are the two shared sections. I read each hit by hand, and this is the only instance. Line 109's "this shape" refers to the question shape of the section it stands in, and I judged it clear.
>
> **Clause by clause**
> 1. **Lost or changed statements: met.** No rule change is found, and the list below says how far that reaches. Clause 1a allows dropping two terms, because `CONTEXT.md` defines neither and each meaning is still stated in plain words where it was defined:
>    - *standing over sources*, now "by path or glob, which sources are authoritative, which are evidence only, and which hold statements known to be false".
>    - *pick report*, now "the report the manager sends the human when your node closes", and "That report is where the human first sees your node". `CONTEXT.md` uses the words "pick report" but gives them no entry of their own.
> 2. **Added statements: met.** Nothing is added.
> 3. **Generalisation: met.** Two changes merge or widen statements, and I judged both to give the same outcome:
>    - Hard rule 4 went from "make the checklist your entire final output, in the shape below" to "make your entire final output the question shape under `## What you hand back`". The shape the before-text pointed at is that question shape. Its `ASK:` field holds "one question, or one checklist", so a decision was already covered.
>    - "A raise is not a fourth thing to hand back: it is the question shape …" became "To raise, hand back the question shape …", together with "exactly one of the three shapes below".
> 4. **Fixed text: met.** The frontmatter and all code fences are byte-identical to the before-text. That covers the question shape, the resume block, the handover and park.
> 5. **Headings: met.** Every heading is identical to the before-text.
> 6. **References inside the file: met.** Each one resolves: "listed under `## What you hand back`", "follow `### When the answer is not an answer`", "the question shape under `## What you hand back`" (used twice), "the table below" and "the three shapes below".
> 7. **Terms: met.**
>    - The terms from `CONTEXT.md` are spelled as it defines them: relay, park, banked, attempt, handover, flag, resolve, verbatim, paraphrase and precondition.
>    - The before-text's "return one … flag" is now "hand back". "Return" is refused for the handover concept.
>    - "Report" in "the report the manager sends" names the report that closes the node, not a handover.
>    - "Ask" appears only inside the fence and in the human's quoted words "ask me later".
>    - No new term is coined.
> 8. **Plain English (outside the shared sections): fails on 8e**, as above. The other five properties hold:
>    - 8a: every negative rule has its positive form beside it. "Write no product code" sits in the rule that says which files to write, and "Write nothing more, and hand nothing more back" follows "You are finished".
>    - 8b: bold appears only on "precondition" at its definition, on the word-list terms (including **paraphrase**), and in the shared sections.
>    - 8c: "settled cold" became "settled without reading anything else". "The first human moment your node's close reaches" became "where the human first sees your node". I found no other figure of speech.
>    - 8d: I found no slogan-shaped sentence, and "the whole of what" does not appear.
>    - 8f: no semicolons outside the fences. Each dash is a list separator or part of a heading.
> 9. **Size (reported, not enforced):** the rewritten range is the whole file. `wc -w` gives 2218 before and 2053 after, which is 93% of the before-text. The target of at most 1479 is missed, which does not fail the work.
> 10. and 11. **Scope: met.** `git status --porcelain --untracked-files=all` shows only `.claude/skills/expedition-precondition/SKILL.md` modified.
> 12. **The two shared sections are copies: met.** Both `## When you raise a flag` and `## When a node you report is an implementation node` are byte-identical to the same sections of `expedition-research/SKILL.md` at `0a3e68b`, apart from blank lines at the section boundary.
>
> **RULE CHANGES**
>
> None found.
>
> How far the list reaches: I compared every statement of the before-text outside the two shared sections against the whole after-text. Clause 12 replaces clauses 1 to 3 for those two sections, so they are excluded. The comparison covered every rule and whose it is, every condition and exception, the four fixed templates, the defined terms, the refused words, and every closed list with its count:
> - the three triggers
> - the two answers to a raise
> - the three things handed back
> - the four table rows
> - the five handover parts
> - the two markers
> - the things read
>
> The before-text's first reading item is now two list items, with the same content in the same order.
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, the bar, the review route, the five ground rules and the five standing rules for writing. The file is in the same state as at node 291: it still has the one-line uncommitted `.gitignore` note, which does not change what the bar requires.
> - **Standards that bore on this work:** standing rule 5 (plain English), `CONTEXT.md`'s `_Avoid_` lines, `/writing-for-agents`, and all five ground rules, which are met. On ground rule 3, everything the human receives "goes through the manager", and hard rule 4 says "Call no tool that addresses the human".
> - No reviewing skill is named, so I ran none.

*The manager's note, matching the two lists:* the checker found no rule change. The worker's R1 (hard rule 4) is listed by the worker as its one deliberate rule change under ruling A. The checker judged it to keep its outcome, under clause 3. What goes back is the clause 8e finding.

*The manager's note, on the spawn:* the manager gave this checker the condition partly by reference to node 291's, against its own rule that the checker gets the condition as extracted text. The checker checked against the node 291 text it held, with clause 11 replaced. The manager sends the condition in full on the next run.

### Correction round 1 — the worker's changes for checker run 1

*The worker's own text, pasted, 2026-09-25.*

Node 292, correction round 1: the clause 8e finding is fixed with a one-sentence change, and no rule changed.

**What I changed.** In `.claude/skills/expedition-precondition/SKILL.md`, in the "you decide" row of the `### When the answer is not an answer` table, I replaced "This covers that question only." with "The human's delegation covers that question only." This is the checker's suggested wording. The sentence now names its own subject, so it has no pronoun that needs a referent. Nothing else in the file changed.

**Whether the change touched what the condition names.** Yes. The table is inside the rewritten range, which is the whole file, and the change is aimed at clause 8e. The change is outside the code blocks, the frontmatter, the headings and the two shared sections, so clauses 4, 5 and 12 still hold. `wc -w` is now 2,055, up from 2,053. `git diff --check` is clean.

**Parts that differ from the first handover:**
- **RULE CHANGES:** R21 changes. Bold was removed from "that question only", and the sentence's subject "This" became "The human's delegation". The outcome is the same: the delegation covers only the question the human handed back. No new rule change.
- **RE-POINTING SEARCH:** I searched the `## Acceptance condition` and `## Amendment…` sections of all 89 open or claimed nodes other than 292 for "This covers", "that question only", "delegation covers" and "you decide". Nothing matched, so no new replacement clause is needed. The phrase appears only on node 291, which is resolved, and on node 292 itself.
- **GATE PAYLOAD:**
  - Checker finding (clause 8e, "This covers that question only.", line 125): fixed with the new wording above.
  - Paths touched: still only `.claude/skills/expedition-precondition/SKILL.md`.
  - The proposed commit message is unchanged.

**Everything else:** every other part is as first returned, including the ANSWER, INDEX LINE, FLAGS, NEW NODES, INVALIDATIONS, GENERALISATIONS and RETROSPECTIVE parts. The amendments for nodes 109, 148 and 155 are the ones rephrased as additions in my earlier message.

### Checker run 2 — `PASS`, under the amended condition

*The checker's own text, pasted, 2026-09-25.*

> PASS
>
> This is check 2 of node 292, "Rewrite the precondition contract in plain English". The run-1 finding under clause 8e is fixed, and the correction changes nothing else. The work meets the acceptance condition as now given in full, and the bar holds. I found no rule changes.
>
> My contract is the main-tree checker contract, unchanged since run 1. The work is `.claude/skills/expedition-precondition/SKILL.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/292-rewrite-the-precondition-contract`, branch base `0a3e68b`. I read the changed path only as the work.
>
> **The acceptance condition.** This time it arrived in full, as text. I compared it with the node-291 text I used in run 1. It is word for word the same apart from clause 11, which names `.claude/skills/expedition-precondition/SKILL.md`. So nothing I established in run 1 was established against different wording.
>
> **What changed since run 1.** No statement of changes came with this check, so I compared the whole file against the run-1 text I read in full. The only edit is line 125, in the "you decide" row of `### When the answer is not an answer`:
> - Before: "This covers that question only."
> - After: "The human's delegation covers that question only."
>
> The line count is unchanged at 224. The word count went from 2053 to 2055, which matches this one edit.
>
> **Clause by clause**
> 1. **Lost or changed statements: met.** No rule change is found. The edit gives the sentence the meaning it was intended to have: the delegation covers only that question. My run-1 comparison stands for the rest of the file, including the two terms clause 1a allows dropping, *standing over sources* and *pick report*.
> 2. **Added statements: met.** Nothing is added.
> 3. **Generalisation: met**, as in run 1. The edit does not reach this clause.
> 4. **Fixed text: met.** Re-run: the frontmatter and all code fences are byte-identical to the before-text.
> 5. **Headings: met.** Re-run: every heading is identical to the before-text.
> 6. **References inside the file: met**, as in run 1. The edit adds no reference.
> 7. **Terms: met.** "Delegation" is ordinary English and not a new term. The flag it goes with is still spelled `DELEGATED`.
> 8. **Plain English (outside the shared sections): met.**
>    - 8e: the run-1 instance now names its referent directly, "The human's delegation". The other it, this, that, they, these and those I read in run 1 stand as judged, and "this shape" on line 109 is still clear.
>    - 8a, 8b, 8c, 8d and 8f are unaffected by the edit. Re-run: there are no semicolons outside the fences, and the same 16 bold terms appear.
> 9. **Size (reported, not enforced):** the rewritten range is the whole file. `wc -w` gives 2218 before and 2055 after, which is 93% of the before-text. The target of at most 1479 is missed, which does not fail the work.
> 10. and 11. **Scope: met.** `git status --porcelain --untracked-files=all` shows only `.claude/skills/expedition-precondition/SKILL.md` modified.
> 12. **The two shared sections are copies: met.** Re-run: both `## When you raise a flag` and `## When a node you report is an implementation node` are byte-identical to the same sections of `expedition-research/SKILL.md` at `0a3e68b`, apart from blank lines at the section boundary.
>
> **RULE CHANGES** (for the file as it now stands)
>
> None found.
>
> How far the list reaches: every statement of the before-text outside the two shared sections, compared against the whole after-text. Clause 12 replaces clauses 1 to 3 for those two sections, so they are excluded. The comparison covered every rule and whose it is, every condition and exception, the four fixed templates, the defined terms, the refused words, and every closed list with its count:
> - the three triggers
> - the two answers to a raise
> - the three things handed back
> - the four table rows
> - the five handover parts
> - the two markers
> - the things read
>
> This is the full run-1 comparison, together with the one edit above, read against the before-text.
>
> **The bar, re-run in full**
> - The repo has no build, tests, formatter or CI, and `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md`, in the same state as in run 1: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:** standing rule 5, `CONTEXT.md`'s `_Avoid_` lines, `/writing-for-agents`, and all five ground rules, which are met.
> - No reviewing skill is named, so I ran none.

*The manager's note, matching the two lists:* the checker found no rule change. The worker's list has one deliberate rule change, R1 (hard rule 4), which the checker judged to keep its outcome. Nothing on the checker's list is missing from the worker's.


### Gate — approve, 2026-09-25

The human, `verbatim`: *"approve"*

## Flags

`292.1` **· settled** `ASSUMPTION` — I dropped the label "pick report" under ruling B and clause 1a. `CONTEXT.md` uses the phrase inside its Flag and Raise entries but has no entry for it, and this file defined it in bold. Its meaning stays in plain words at the same place: "the report the manager sends the human when your node closes". `expedition/SKILL.md` and `graph-conventions.md` still use the term, and node 137 plans to rename it. I have proposed an amendment to node 137 so that its rename covers this periphrasis.
