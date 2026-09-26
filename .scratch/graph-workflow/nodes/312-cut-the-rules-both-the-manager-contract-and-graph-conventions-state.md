# Cut the rules that both the manager contract and `graph-conventions.md` state

Type: implementation
Status: resolved
Blocked by: 297, 298

## Question

The human, `verbatim`, after approving node 300: *"wait for 300, we should also cut the duplicate rules, I don't know if they need to be cut in the manager contract or the graph-convention"*. It answers node 300's flag `300.2`, whose worker kept rules that `graph-conventions.md` shares with `.claude/skills/expedition/SKILL.md`, such as when flags settle and the order for recording the human's answers. Node 300 had already landed as `527596c` when this arrived.

Each rule that both files state should be stated in one of them, with the other pointing at it where a reader needs it. Which file keeps each rule is being put to the human. The acceptance condition waits on that answer, and so does node 298, the last rewrite of the manager contract.

*Manager's note: minted by the manager. The condition is the manager's to write once the human has answered.*

## Acceptance condition

*Written by the manager, which minted this node. Every demand in it is fixed by the human's answer below, by the pass conditions of nodes 291 to 302 as the human amended them, or by the state of the files.*

**Terms.** *The before-text* of a file is that file as it stands at the commit this work's branch was created from, read with `git show $(git merge-base HEAD master):<path>` in the worktree. *The after-text* is the file in the worktree. *The two files* are `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition/graph-conventions.md`. *A shared rule* is a binding statement in the before-text of one of the two files that has a counterpart with the same outcome in the before-text of the other.

1. **Each shared rule is stated once.** In the after-texts, each shared rule is stated in exactly one of the two files, chosen as follows:
   - in `graph-conventions.md` where the rule is about the graph's files: their format, what each section holds, or the steps of a procedure that changes them;
   - in `SKILL.md` where the rule is about the manager's choices: when it acts, what it may decide, or what goes in front of the human.
2. **Pointers.** Where the file that no longer states a shared rule has a passage that needs it, that passage points at the other file's heading in one sentence.
3. **Lost or changed statements are rule changes.** The binding statements are: every rule, meaning every instruction, permission, prohibition or duty, and whose it is; every condition or exception attached to a rule; every fixed template; every term the text defines, and its definition; every word the text refuses; and the members and stated count of every closed list. A binding statement of either before-text that has no counterpart with the same outcome in either after-text is a rule change. So is a binding statement in either after-text that neither before-text states. The checker lists every rule change it finds, each with the before-text statement and its after-text counterpart, or "removed". A rule change does not fail the work.
4. **Fixed text.** Everything inside code fences, and the frontmatter block at the top of each file, is byte-identical to the before-text.
5. **Headings.** A heading of either before-text whose exact text appears in any other of the following files keeps that exact text: `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/graph-conventions.md`, `.claude/skills/expedition/wayfinder-divergences.md`, `.claude/skills/expedition-checker/SKILL.md`, `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-stop/SKILL.md`, `CONTEXT.md`, `.claude/rules/expedition-triggers.md`, `.scratch/graph-workflow/map.md`, `.scratch/graph-workflow/map-manager-only.md`, `.scratch/graph-workflow/map-implementation-rules.md`, `.gitignore`.
6. **References.** Every reference either after-text makes to a part of itself or of the other file points at something that after-text holds.
7. **Plain English.** Prose the work changes, outside code fences, has these six properties. The checker names each passage it judges to breach one, and which property it breaches.
   a. A rule is stated as what to do. A prohibition appears only where the rule cannot be stated as what to do, and then beside the positive statement.
   b. Bold appears only on a term at the place where it is defined.
   c. An idea that is not a term defined in `CONTEXT.md` is said in plain words, with no figure of speech and no coined phrase.
   d. Statements are direct. No sentence is a slogan-shaped contrast or reversal.
   e. Every sentence is grammatical, and each "it", "this", "that", "they", "these" or "those" has one clear referent in the same sentence or the one before.
   f. One idea per sentence. No sentence holds more than one dash-delimited aside, or more than one semicolon.
8. **Terms.** The after-texts use no word that a `CONTEXT.md` `_Avoid_` line refuses, for the concept that line refuses it for, and coin no new term.
9. **Size, reported and not enforced.** The checker reports the `wc -w` count of each of the two files before and after.
10. **Scope.** The work changes the two files and no other path.

## The manager's reading of this condition, 2026-09-24

*The manager's own note.* Read back against the two rules that bind every condition. **Self-contained:** the split between the files is written out in clause 1 in the words of the proposal the human approved, and every other clause is copied from the pass conditions as the human amended them. Nothing sends the checker to the record. **No demand over the record:** every clause is about the two files and the tree. None holds the work against the effort's decisions.

## Interview

**The human's answer, 2026-09-24**, `verbatim`: *"ok for the split"*, to the manager's proposal: *"`graph-conventions.md` keeps rules about the files: their format, what each section holds, and the step-by-step procedures that change them … The manager contract keeps rules about the manager's choices: when it acts, what it may decide, and what goes in front of you … Where a reader of one file needs a rule the other holds, it gets a one-line pointer instead of a second copy."*

## Answer

Rules stated in both SKILL.md and graph-conventions.md now live in one, split as the human approved: file format and procedures there, manager choices here, with one-line heading pointers.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The human approved the one rule change the checker listed, the `DIVERGENCE` mark narrowed to `## Interview`, under `### Checker run 1`. The work landed as commit `e64b3de`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-25. The worker's own text, pasted. The flags are raised under `## Flags` at the gate.*

HANDOVER:      Cut the rules that both the manager contract and `graph-conventions.md` state

ANSWER:
Each rule that both `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition/graph-conventions.md` stated is now stated in one of them, split by clause 1. Where the other file needs the rule, it now has a one-sentence pointer to a heading. No heading changed. No fenced block changed. The frontmatter did not change. Only these two paths changed. Word counts (`wc -w`), before → after: SKILL.md 6229 → 6298, graph-conventions.md 4471 → 3904, total 10700 → 10202.

What moved:
- **Out of graph-conventions.md, now only in SKILL.md:**
  - the sole-writer and scribe rules;
  - the graph-file-work carve-out;
  - how the manager hands a condition to the checker, and what it does with a defective condition;
  - who writes a condition;
  - the four parties who may change a condition, the two provisos, the scope extension, the three things an amendment cannot cover, and the duty to search open conditions;
  - when the human's answer is written, and the resume/same-turn rule;
  - pasting a terse reply, including the "ok for recommended" example;
  - recording an ambiguous reply and asking which option it means;
  - who establishes a NOT COVERED part, and by when;
  - the three routes after a reject;
  - when flags settle, and the closing-report two-case list;
  - whose text a `flags.md` line is;
  - where the closing report takes its outstanding flags from.
- **Out of SKILL.md, now only in graph-conventions.md:**
  - the two-write raise and settle procedures, and "the index wins";
  - the claim rule for implementation nodes, and "no other kind carries one";
  - the self-contained rule;
  - the `verbatim` and `paraphrase` marks and what they mean;
  - quoting an offered option;
  - the `DIVERGENCE` mark, now written as the manager's act;
  - the definition of a flag's "marker";
  - what the landing policy covers;
  - where the map records the bar's commands;
  - the claim surviving an agent's death.
- **Sentences that appeared in only one file moved with their rule, so no rule was lost:**
  - graph-conventions.md → SKILL.md: "you raise such a condition where you find it before the check; the checker raises one it cannot check"; "the human at the gate, or a later run of the check, may establish it instead"; the case of flags raised before the settling rule existed.
  - SKILL.md → graph-conventions.md: the landing policy's path-limited commit and each of the three outcomes; the reason for the `DIVERGENCE` mark.

Calls a later reader would otherwise have to re-derive:
1. **Fenced blocks win over clause 1.** graph-conventions.md's node-file template still says "implementation only; written by the spawning node". That fence is fixed text under clause 4, so the template statement stays, and the prose rule on who writes a condition sits in SKILL.md.
2. **The node 311 contradiction is left standing and is not decided here.**
   - graph-conventions.md still says: "The human changes only a condition on a node nobody holds yet. A condition under a live worker reaches the human by that worker's raise, and by no other route."
   - SKILL.md still says: "The human may also amend a condition of their own accord at any time."
   - The party's and the manager's limit to unheld nodes, which both files had, is now only in SKILL.md.
3. **The render/paraphrase contradiction is left standing.** SKILL.md says "You never render a reply". graph-conventions.md allows `paraphrase` "only where it could not avoid rendering". The outcomes differ, so it is not a shared rule. It is reported under NEW NODES.
4. **Overlaps kept in both files because their outcomes differ.** Details are in the shared-rules list below.
5. **INVALIDATIONS rewording.** graph-conventions.md's "Every worker returns `INVALIDATIONS` on its handover instead…" duplicated SKILL.md's five-part handover. It now reads: "Such a demand goes in the handover's `INVALIDATIONS` part, which names which resolved node the work contradicts and how."

INDEX LINE:    Rules stated in both SKILL.md and graph-conventions.md now live in one, split as the human approved: file format and procedures there, manager choices here, with one-line heading pointers.

FLAGS:
- `312.1` ASSUMPTION — graph-conventions.md's node-file template fence still states "implementation only; written by the spawning node". Clause 4 fixes fence text, so I kept that template statement even though the prose rule on who writes a condition now lives in SKILL.md. I read clause 4 as winning over clause 1 for fenced text.
  Index: A fenced template in graph-conventions.md still states who writes a condition, because clause 4 fixed fence text while clause 1 moved that rule's prose into SKILL.md.
- `312.2` ASSUMPTION — Six overlaps are kept in both files, because I judged the two outcomes different or the graph-conventions.md text a reason rather than a rule. The six are listed under "Borderline overlaps kept in both files" below. A strict checker may count one as a shared rule.
  Index: Six near-duplicates between SKILL.md and graph-conventions.md were kept, judged different in outcome or a reason rather than a rule; the checker may disagree.
- `312.3` ASSUMPTION — I did not settle node 311's contradiction. graph-conventions.md keeps the human-only-unheld limit and the "no other route" sentence where node 311 expects them. SKILL.md keeps "of their own accord at any time". Moving either sentence would have decided node 311.
  Index: The contradiction on whether the human may amend a held node's condition was left in both files for node 311 to settle.

NEW NODES:
- Name: The manager contract forbids rendering a reply while graph-conventions.md permits a paraphrase
  Kind: grilling
  Question: SKILL.md's `### The human's words` says "You never render a reply, so its mark never depends on your judgement." graph-conventions.md's `### Recording the human's words` says "The manager marks an answer `paraphrase` only where it could not avoid rendering the answer in its own words." Both were already in the before-texts at 9d8044c. Is the manager ever allowed to render a reply, and if so, which file states when?
  Blockers: none

INVALIDATIONS:
No resolved node's decision is contradicted. The answers of nodes 296–300 describe the two files' contents, and this work changes where some rules are stated:
- The amendment rules and the checker-handling rule no longer appear in graph-conventions.md's `### ## Acceptance condition`.
- The settling paragraphs no longer appear in `### Settle a flag`.
- The recording timing and terse-reply rules no longer appear in `### Recording the human's words`.
- The raise/settle procedure steps no longer appear in SKILL.md's `## Flags`.

GATE PAYLOAD:
- Checker findings: none yet; the checker has not run.
- Paths touched: `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/graph-conventions.md`. Scratch files, not in the repo: `$TMPDIR/n312/` (`search.py`, `diff.txt`, `SKILL.before.md`, `GC.before.md`, `quotes.py`).
- Bar: the repo has no build, tests, formatter or CI. `.gitignore` lists `.worktrees/`, `.claude/worktrees/` and `.scratch/graph-workflow/worktrees/`, which matches the rules file. The bar is the non-command half only. The refused-word grep over added lines, checked by hand against `CONTEXT.md`'s `_Avoid_` lines, found nothing refused for its concept: "return", "complete", "rewrites" and "report" were each checked. The fences, the frontmatter and the heading lists are byte-identical, checked by script.
- Proposed commit message:
  Cut the rules both the manager contract and graph-conventions.md state

  Each rule the two files shared now lives in one: graph-conventions.md keeps file format, section contents and procedures; SKILL.md keeps the manager's choices. The other file points at the heading in one sentence.

  Node: graph-workflow/312

RULE CHANGES (before → after, and why):
By my reading, no binding statement lost its outcome. Every one below is a move or rewording, listed so the checker can compare its own list.
1. GC "The manager writes the human's answer into its section the moment the human speaks, at relay time. Resuming a worker is a background send and does not block, so the manager sends the resume and writes the answer in the same turn." → SKILL "Write the human's words onto the node at the moment they are spoken… A resume is sent in the background and you do not wait for it, so send the resume and write the answer in the same turn." Why: "when it acts", so SKILL.md. "At relay time" is covered by "the moment they are spoken".
2. SKILL "mark it `verbatim`. That mark says the answer is the human's own words rather than your rendering of them." → GC "A reply pasted as the human wrote it is marked `verbatim`. That mark says the answer is the human's own words rather than the manager's rendering of them." Why: marker format belongs in GC.
3. SKILL "Where the reply takes an option it was offered, quote that option in the same entry and attribute it…" → removed; GC's wider version ("option or an outcome") stands. Why: entry form.
4. SKILL "Where the answer contradicts the worker's recommendation, mark it a divergence, so the worker does not read a bare answer as agreement and resolve as though its recommendation had been taken." and GC "An answer that contradicts the recommendation the worker gave is also marked `DIVERGENCE`." → GC "The manager also marks `DIVERGENCE` on an answer that contradicts the recommendation the worker gave, so the worker does not read an unmarked answer as agreement and resolve as though its recommendation had been taken." Why: entry form. Made active so it still says whose act it is.
5. GC "The manager pastes the reply as the human wrote it, however terse… A reply such as *"ok for recommended"* is a complete answer and is recorded as one." and "the manager records the reply and asks which." → SKILL (paste as written; the example; ask which). Why: what the manager may decide, and what goes in front of the human.
6. GC "It is written by the node that spawned this node, before any work starts. Its worker may not rewrite it. A worker that judges the condition wrong raises it." → SKILL "Where an agent minted the node, that agent wrote the condition before any work on the node started, and you file it. Where you minted the node, you write the condition." and "The worker holding the node works to meet the condition as written, and never rewrites it. A worker that judges the condition wrong raises it, and the human answers." Why: who writes and who may change is a manager choice. "Works to meet … as written" is the positive that 7a requires, and I count it as the same outcome as "may not rewrite". Borderline: for a manager-minted node, "before any work starts" now comes from the claim rule.
7. GC "Four parties may change a condition after it is written:" and its four bullets → SKILL list with the same four members and count ("The condition's own worker, by raising it." / "The party that established a fact that makes a clause of the condition wrong." / "You." / "The human, who receives everything else."). The bullets' provisos and conditions are already in SKILL's paragraphs.
8. GC "The last three change only a condition on a node nobody holds yet. A condition under a live worker reaches the human by that worker's raise, and by no other route." → split. The party-and-manager half is SKILL's existing "The amendments in this section, by the party that established a fact and by you, apply only to a node nobody holds yet". The human half stays in GC: "The human changes only a condition on a node nobody holds yet. A condition under a live worker reaches the human by that worker's raise, and by no other route." Why: flag 312.3.
9. GC "An amendment only transcribes words already fixed elsewhere. Writing a whole condition for a node that an agent created is a different act. That act is not the manager's." → removed. SKILL's provisos, "Filing it is your ordinary scribe act…", and the table row "authoring an acceptance condition for a node an agent minted | file the one that agent wrote…" hold the same.
10. GC's three things an amendment cannot reach, and GC's search duty → removed. SKILL's near-identical text stands.
11. GC "The manager hands a condition that points anyway to the checker as written… The manager raises such a condition where it meets one before the check. The checker raises one it cannot check." → SKILL `## The checker` already had the first half and gains "Where you find such a condition before the check, you raise it. The checker raises one it cannot check."
12. GC "Every worker returns `INVALIDATIONS` on its handover instead, naming which resolved node its work contradicts and how." → GC "Such a demand goes in the handover's `INVALIDATIONS` part, which names which resolved node the work contradicts and how." The duty to return that part is SKILL's "A handover has five parts every time". Borderline.
13. GC "Whoever holds the context writes that line as a report when the flag is raised. Nobody reconstructs it later." → GC "…one sentence long, written as a report." plus a pointer. SKILL has "The text of both of a flag's entries is the raising agent's… write no sentence for it", and GC's `### Raise a flag` has "never left to a tidy-up afterwards". Borderline.
14. GC "The closing report's outstanding flags are the unchecked lines of `flags.md`." → removed. SKILL `## Closing an effort` "Every outstanding flag, taken from the unchecked lines of the effort's index of flags" stands.
15. SKILL "Raise a flag in two writes, in order: the entry on the node first, then its line in the effort's index of flags. Both writes are part of raising it." and "Settle a flag in two writes as well, on the node and in the index. Where the two disagree, the index wins." → removed. GC's `### Raise a flag`, `### Settle a flag`, and "Where they disagree, `flags.md` wins" stand.
16. GC `### Settle a flag`'s three paragraphs (settle moment, pick report, "Flags reach the closing report in two cases only…") → SKILL `## Flags` keeps its own settle-moment text and gains the two-case paragraph. SKILL's "…stay outstanding and reach the closing report" became "…stay outstanding", because case two now carries it.
17. SKILL "A flag carries a marker, one word saying which kind of judgement the flag records." → GC `### ## Flags` "Each entry starts with the flag's id and then its marker, one word saying which kind of judgement the flag records. There are three markers:". This moves a term's definition.
18. SKILL "An implementation node cannot be claimed until it carries an acceptance condition. No other kind of node carries one." → removed. GC `### Claim`, the template fence and check 7 stand.
19. SKILL "Every condition is self-contained text. Its reader is a checker that has not read the node, so everything needed to judge the work is in the condition itself." → removed. GC's self-contained paragraph stands. SKILL's constraint 2 now names "the self-contained rule and the rule against a demand about the record as a whole, both in `graph-conventions.md`".
20. SKILL "How code lands is set by the effort's own landing policy, recorded in its map. The policy says where a worker's tree is, what one path-limited commit of that node's paths takes, and what happens to that tree on each of the three outcomes." → GC landing bullet "where a node's worker works, what one path-limited commit of that node's paths takes, and what happens to the worker's tree on each of the gate's three outcomes", with a SKILL pointer. GC's "between the gate and the repository" was dropped as covered. Borderline.
21. SKILL "Usually you establish it, since you hold the handover." kept, with GC's "the checker does not see" and "The human at the gate, or a later run of the check, may do so instead" added. GC "The manager usually does… Every part is established by the gate at the latest." → removed.
22. GC Review "which of three routes the node then took: `out-of-scope`, `superseded` by a replacement, or back to `open` behind a new `Blocked by:` edge" → "which of the three routes under `### What reject means` in `SKILL.md` the node then took". The same three members are stated in SKILL.
23. SKILL "The node keeps its number, its file and its claim. The claim belongs to the node, not to the agent. A crash never releases it." → "The node keeps its number, its file and its claim, under the rules for a node's number in `## Adding a node` and for `claimed` in `## Statuses` of `graph-conventions.md`." GC `claimed` says "a worker that dies does not release it".
24. SKILL "The map also holds the record of the bar's commands once they are discovered for this repo." → a pointer to GC `## The seven files`. GC's Notes bullet stands. The confirmation duty stays in SKILL.
25. GC "The manager is the only writer of the graph's record. It writes as a scribe. A worker returns text. The manager pastes…" and the graph-file carve-out paragraph → removed. SKILL `## Writing the graph` and `### You write as a scribe` stand.
26. New sentence in GC `### Park`: "Answers already relayed are already on the node, because `### The human's words` in `SKILL.md` has the manager write each one there as it is given." It gives a reason and a pointer. No new rule.

SHARED RULES FOUND (which file kept each, which bullet of clause 1 decided it, and where the pointer is):
1. Sole writer of the record → SKILL (manager's choice). Pointer: GC opening → `## Writing the graph`.
2. Scribe pasting → SKILL (what it may decide). Same pointer.
3. The graph-file-work carve-out; recording stays the manager's → SKILL (what it may decide). Same pointer.
4. The map holds the bar's commands → GC (what a section holds). Pointer: SKILL "Words used exactly" map bullet → `## The seven files`.
5. The landing policy is in the map, and what it covers → GC (what a section holds). Pointer: SKILL `### Three outcomes, and no fourth` → `## The seven files`.
6. The closing report's flags are the unchecked `flags.md` lines → SKILL (what goes in front of the human). Pointer: GC `flags.md` paragraph → `## Closing an effort`.
7. The flag line's text is the raising agent's and is never reconstructed → SKILL (what it may decide). Pointer: GC `flags.md` paragraph → `## Flags`.
8. `flags.md` / the index wins a disagreement → GC (format). SKILL needs no pointer beyond the procedures pointer in `## Flags`.
9. Raise a flag in two writes, both part of raising → GC (procedure steps). Pointer: SKILL `## Flags` → `### Raise a flag`.
10. Settle a flag in two writes → GC (procedure steps). Pointer: SKILL `## Flags` → `### Settle a flag`.
11. The settle moment, the pick report, never settling on judgement or time, and the closing-report cases → SKILL (when it acts). Pointer: GC `### Settle a flag` → `## Flags`.
12. A flag carries a marker, and its definition → GC (format). SKILL no longer uses the word.
13. The claim rule for implementation nodes, and "no other kind carries one" → GC (procedure step and format). Pointer: SKILL `## Acceptance conditions` → `## The node file` and `### Claim`.
14. The self-contained rule → GC (what the section holds). Pointer: SKILL `## Acceptance conditions` → the `## Acceptance condition` description, and constraint 2.
15. Who writes a condition (spawning or minting node; manager-minted is the manager's; not the manager's for an agent-minted node) → SKILL (what it may decide), except the template fence under clause 4 (flag 312.1). Pointer: GC `### ## Acceptance condition` → `## Acceptance conditions`.
16. The worker may not rewrite the condition and raises instead → SKILL (what it may decide, with amendments). Same pointer.
17. Hand a defective condition to the checker as written; the missing part goes to the human → SKILL (what it may decide). Pointer: GC → `## The checker`.
18. The four parties, the provisos, the manager's own amendments, scope extension, the human receives everything else → SKILL (what it may decide). Pointer: GC → `## Acceptance conditions`.
19. Party and manager amendments apply only to unheld nodes → SKILL. The human's limit stays in GC (flag 312.3).
20. An amendment only transcribes; writing a whole condition for an agent-minted node is not the manager's → SKILL.
21. The three things an amendment cannot reach → SKILL.
22. The duty to search open conditions → SKILL.
23. Recording at the moment spoken, plus resume and write in the same turn → SKILL (when it acts). Pointer: GC `### Recording the human's words` → `### The human's words`; also GC `### Park`.
24. Paste the reply however terse → SKILL (what it may decide). Same pointer.
25. The `verbatim` mark and its meaning → GC (format). Pointer: SKILL `### The human's words` → `### Recording the human's words`.
26. Quote the offered option in the same entry → GC (entry form). Same SKILL pointer.
27. An ambiguous terse reply: record it and ask which → SKILL (what goes in front of the human). GC pointer as in 23.
28. The `DIVERGENCE` mark → GC (format). Pointer: SKILL `### The human's words` → GC's description of `## Interview`.
29. A NOT COVERED part is established by the gate at the latest, usually by the manager → SKILL (when it acts). Pointer: GC `### ## Review` → `### The payload`.
30. The three routes after a reject → SKILL (what it may decide). Pointer: GC `### ## Review` item 3 → `### What reject means`.
31. A claim belongs to the node and a crash does not release it → GC (status meaning). Pointer: SKILL `## When an agent dies or is stopped` → `## Statuses` and `## Adding a node`.
32. Every worker returns INVALIDATIONS → SKILL's handover definition. GC reworded to describe where the demand goes (rule change 12).

Borderline overlaps kept in both files (flag 312.2):
- "Read it before touching an effort's files": GC's version binds every reader, SKILL's binds only the manager.
- The ground rules live in the map: SKILL's rule is that they live nowhere else, GC's is that `## Notes` has an optional block for them.
- At most three interview attempts: GC's is a format cap, SKILL's is the manager putting a third failure to the human.
- "The checker has not read the node": in GC this is a premise of the self-contained rule, not an instruction.
- "The sweep and the closing report are built from `flags.md`": in GC this is the reason behind "flags.md wins", and the sweep half appears only in GC.
- A checker that raised gets no outcome: the `## Review` entry and the gate payload are different records.

RE-POINTING SEARCH:
- **What I searched:** the open and claimed nodes (143, excluding 312). In each, every section headed `## Acceptance condition`, `## Amendment…`, `## A second condition…` or `## A second author's condition…`, wherever it sits in the file, so amendments filed after a manager's note are included.
- **Handles:**
  - 6-gram and 5-gram word shingles of every removed or replaced before-text block of both files, from `git diff -U0`, normalised;
  - every quoted span (in "…", *…*, `…`) of three or more words, tested two ways: present in a file's before-text and absent from its after-text, and contained in a removed block;
  - the heading names `### Settle a flag`, `### Raise a flag`, `### Recording the human's words`, `### The human's words`, the `## Acceptance condition`/`## Acceptance conditions` sections, `## The checker`, `### The payload`, `### What reject means`, `## Statuses`, `## When an agent dies or is stopped`, `## Closing an effort`, `## Writing the graph`, `## The seven files`, `## Flags`, `## Review`, `## Interview`, `## Words used exactly`, `### A flag in a payload` and `### The four constraints…`, searched in conditions that name either file.
- No heading was removed or moved.
- **Matches that need action:**
  - **Node 309 (implementation, open), `## Acceptance condition`.** Replacement condition: "In `.claude/skills/expedition/SKILL.md`, under `## Flags`, the paragraph beginning "Flags reach the closing report" states one case only: a flag whose pick report the human never answered, because they never spoke again. It no longer states the case of a flag raised before the settling rule existed. No other sentence in the file changes, and no other path changes. The working tree meets the bar." Fixed by this work: the paragraph now reads "Flags reach the closing report in two cases only. The first is a flag raised before this settling rule existed, on a node already resolved. The second is a flag whose pick report the human never answered, because they never spoke again." under SKILL.md `## Flags`. GC `### Settle a flag` now says only "`## Flags` in `SKILL.md` says when a node's flags settle, and which flags reach the closing report."
  - **Node 43, `## Amendment, 2026-09-24`, clause 3.** Replace the quoted current text with: `` Such a demand goes in the handover's `INVALIDATIONS` part, which names which resolved node the work contradicts and how. `` It is still one sentence, so "That sentence is reworded" stays. Clause 4 still holds: GC still says "A demand about the record as a whole belongs on the handover and in no condition, whatever its wording."
  - **Node 61, `## Amendment, 2026-09-24`, preamble.** Node 299's proposed wording quotes GC's "It writes as a scribe.", which this work removes. GC no longer uses the word `scribe`. Replace the proposed wording with: "in `expedition/SKILL.md`, under `### You write as a scribe`; `expedition/graph-conventions.md` no longer uses the word, and its opening says "`## Writing the graph` in `SKILL.md`, the file beside this one, says who writes the graph's record and how the manager pastes what a worker hands it."" The manager's existing question, whether node 61 still needs doing, stands.
  - **Node 55 (open), `## Acceptance condition`: I propose it be superseded.**
    - Clauses 1–2 demand that GC's acceptance-condition section state who writes a manager-minted condition and the manager's four constraints. SKILL.md already states both, in `## Acceptance conditions` ("Where you minted the node, you write the condition.") and `### The four constraints on a condition you write yourself`, and the human's split puts them there.
    - Clause 5 requires GC to still fix "its worker may not rewrite it and raises instead", "a condition exists before any work starts" and "a condition which points anyway is handed to the checker unrepaired". This work moved all three to SKILL.md.
    - What is still live is clause 3 (CONTEXT.md's entry still says "written by the node that spawned it" unqualified) and the GC template fence annotation "written by the spawning node". A narrower replacement node could cover those two.
  - **Node 109 (open), clause 5.** It demands that GC's `### Acceptance condition` and SKILL's `## Acceptance conditions` each carry the extent rule. That would re-create a duplicate the human's split forbids. My text falsifies no quoted words, and its enumerator `grep -rln "self-contained"` still returns both files. Changing the clause needs a judgement, so it goes to the human. My recommendation: GC states clauses 1–4, and SKILL states the manager's duties with a pointer.
- **Matched but unaffected:**
  - 234, 236, 276: they name map-manager-only.md's `## Landing an implementation node's work`, which GC's bullet still names.
  - 278, 280: SKILL `## Acceptance conditions` still holds the amendment exception.
  - 287: it is about SKILL's `## Writing the graph`, which is unchanged.
  - 89: its demand is on SKILL.md and is not falsified.
  - 41, 49, 96, 111, 120, 153, 228, 44, 57, 155, 214, 254: generic phrases or text that stays.
  - The recurring "every word of the replacement is…" hits are amendment boilerplate.
- **Outside the searched sections:** node 311's `## Question` quotes GC as limiting "the human, the party and the manager". After this work GC limits only the human, and SKILL limits the party and the manager. Node 314 (three states) is untouched and still valid.
- **Scripts:** `$TMPDIR/n312/search.py` (shingles; run with n as the argument) and `$TMPDIR/n312/quotes.py` (quoted spans).

RETROSPECTIVE:
1. **What I had to hunt for.**
   - Which open conditions depend on moved text. Only my own shingle and quoted-span scripts found node 309, node 61's amendment and node 43's amendment. The spawn and node file named none of them.
   - The earlier n298 script reads only `## Acceptance condition` runs until a stop heading, and it does miss later `## Amendment` sections, as warned.
   - The quoted-span check has a false negative: node 309's "Flags reach the closing report" survives as a substring of the new pointer, so only the shingle pass caught it.
   - Whether "manager contract" is a glossary term, from a grep of CONTEXT.md. It is not, so GC now refers to `SKILL.md` by path.
2. **What arrived that this node did not need.**
   - Most of `map.md`'s standing preferences: the resume, token and priority preferences, the retrospective bullet, and more. I needed only the Notes pointers.
   - Most of `map-implementation-rules.md`'s account paragraphs. I needed only standing rule 5 and the bar record.
   - `.claude/rules/expedition-triggers.md`, auto-loaded twice (the main tree's copy and the worktree's).
   - A different arrangement: a heading in map-implementation-rules.md that holds only the rules and the bar record would let a text-move node read one section.
3. **What would have made it easier.**
   - Clause 3's "binding statement" could say whether a reason or premise counts. That decides most of the borderline cases in flag 312.2.
   - The condition could say how clause 4 (fixed fences) interacts with clause 1 when a shared rule sits in a fence.
   - A shipped re-pointing script, as node 313 proposes.
   - The spawn could list the open nodes whose conditions predate the split and demand duplicates (55, 109).
4. **What was stale, wrong or contradictory.**
   - Both files already contradicted each other on the human amending a held node (node 311) and on rendering versus paraphrase (NEW NODES above).
   - SKILL's `### Three states nothing in the files shows` against GC's "A parked node is `open` with a non-empty `## Interview`" (node 314).
   - Within GC, `## Notes` holds the bar's commands, yet `map-implementation-rules.md` also holds them (nodes 153, 228).
   - Node 55's and node 109's conditions demand duplicates that the human's split now rules out.
   - Node 311's question will be stale once this lands.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-25. The checker was resumed from node 298's check.*

> PASS
>
> This is node 312, "Cut the rules that both the manager contract and `graph-conventions.md` state". I started from the givens only and carried nothing over from nodes 296, 297 or 298.
> - The worktree is `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/312-cut-the-shared-rules`.
> - The before-texts are `git show 9d8044c:<path>`, which is the merge-base, for both files.
> - I read both after-texts whole and walked every hunk of both diffs.
>
> **Clause by clause**
>
> **Clause 1 holds.** Each shared rule the work handled is now stated in one file only:
> - **Moved to `SKILL.md`:**
>   - who writes the graph's record and how the manager pastes
>   - sending the resume and writing the answer in the same turn
>   - that "ok for recommended" is a complete answer
>   - that you raise a defective condition you meet before the check, and the checker raises one it cannot check
>   - who establishes an owed `NOT COVERED:` part, and by when
>   - when flags settle, and which flags reach the closing report
>   - the four parties that may change a condition
>   - the three limits on an amendment
>   - the search before a fact is handed back
> - **Moved to `graph-conventions.md`:**
>   - the definition of a flag's marker
>   - what the `verbatim` mark says, and the quoted option
>   - the `DIVERGENCE` mark
>   - what the landing policy covers, and that the map records it
>   - the bar's commands in the map
>   - the raise and settle writes, and that the index wins
>   - which nodes carry a condition, and claiming only once one exists
>   - the self-contained rule
>   - that the claim belongs to the node and survives a death
>
> I judge none of these placed in the wrong file. Two overlaps remain, and I judge neither a shared rule under the condition's definition (a counterpart with the same outcome):
> - `### Claim` in `graph-conventions.md` says "Claim an `implementation` node only once it has an `## Acceptance condition`". `SKILL.md` says "The node is not claimed until the condition is complete". The two conditions differ: present against complete.
> - `### \`## Interview\`` says "A node holds at most three attempt blocks". `SKILL.md` says "After two replacements, treat a third failure as evidence…". The first is a limit on the file format, and the second is a decision the manager makes. Each sits in the file that clause 1 names for its side.
>
> **Clause 2 holds.** Every passage that lost a rule points at the other file's heading in one sentence per pointer:
> - In `graph-conventions.md`, the pointers are the opening paragraph, the `flags.md` entry, `### \`## Acceptance condition\`` (twice), `### Recording the human's words`, the reject routes in `## Review`, the owed part, `### Park` and `### Settle a flag`.
> - In `SKILL.md`, the pointers are the map entry, the landing policy, `### The human's words`, `## Flags`, `## Acceptance conditions`, the four constraints item 2, and `## When an agent dies or is stopped`.
> - Every pointed-at heading exists. Every claim a pointer makes about its target is true of the target.
>
> **Clause 3:** see RULE CHANGES below.
>
> **Clause 4 holds.** Both frontmatter blocks and every code fence in both files are byte-identical.
>
> **Clause 5 holds.** Every heading of both files is byte-identical.
>
> **Clause 6 holds.** These references resolve:
> - the cross-file pointers above
> - within `graph-conventions.md`, "check 9 below" and "`## Writing the map` below"
> - within `SKILL.md`, "under the raise above" and "under `### A flag in a payload` above"
>
> **Clause 7 holds** for the changed prose:
> - no bold was added
> - each prohibition sits beside its positive
> - I found no figure of speech and no slogan
> - every pronoun in the added lines has one clear referent
> - no added sentence has more than one dash aside or more than one semicolon
>
> **Clause 8 holds.** No `_Avoid_` word is used in the refused sense, and no new term is coined. The hits for "return" and "payload" are ordinary uses: "the worker can return", and the heading `### The payload`.
>
> **Clause 9 (reported):**
>
> | file | before | after | change |
> | --- | --- | --- | --- |
> | `SKILL.md` | 6229 words | 6298 words | +69 |
> | `graph-conventions.md` | 4471 words | 3904 words | −567 |
>
> **Clause 10 holds.** Only `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition/graph-conventions.md` changed, and nothing is untracked.
>
> **The bar holds.** The repo root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. It has no manifest, task runner, formatter or CI, so there is no command to run and nothing was printed. The non-command half is met.
> - I read the standards in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md`: the ground rules, the five standing rules for writing, `/coding-principles` and `/naming`, `CONTEXT.md`'s `_Avoid_` lines, `graph-conventions.md`, and `/writing-for-agents`.
> - The ones that bore on this work are ground rules 1 and 4, writing rules 4 and 5, the `_Avoid_` lines, and `/writing-for-agents`. Writing rule 4 applies because every pointer cites by heading, not by line number.
> - The standards name no reviewing skill, so I ran none.
>
> RULE CHANGES
>
> 1. **The `DIVERGENCE` mark is narrowed to `## Interview`.**
>    - Before, `SKILL.md` `### The human's words` said: "Where the answer contradicts the worker's recommendation, mark it a divergence, so the worker does not read a bare answer as agreement…". That section covers every recorded answer, including answers recorded under `## Review`.
>    - Before, `graph-conventions.md` stated it under `## Interview` only: "An answer that contradicts the recommendation the worker gave is also marked `DIVERGENCE`".
>    - After, the rule is in `graph-conventions.md`'s `## Interview` description only: "The manager also marks `DIVERGENCE` on an answer that contradicts the recommendation the worker gave…". `SKILL.md` points there: "The same file's description of `## Interview` states the rule for the `DIVERGENCE` mark".
>    - The case that changes: a human's answer recorded under `## Review` that contradicts the worker's recommendation was marked before, and no rule reaches it now.
>
> I found no other rule changes. These statements look changed but give the same outcome:
> - "Whoever holds the context writes that line as a report when the flag is raised" is covered by `SKILL.md` `## Flags`, "The text of both of a flag's entries is the raising agent's", together with `### Raise a flag`.
> - "Nobody reconstructs it later" is covered by "never left to a tidy-up afterwards" and "never reconstructed by you".
> - "Every worker returns `INVALIDATIONS`" is covered by the handover's five parts in `SKILL.md`, and "Such a demand goes in the handover's `INVALIDATIONS` part".
> - "It is written by the node that spawned this node, before any work starts" is covered by `SKILL.md`'s minted-by-agent or minted-by-you sentence, `### Claim`, and the unchanged fenced template.
> - "Its worker may not rewrite it" is covered by "The worker holding the node works to meet the condition as written, and never rewrites it".
> - "The manager pastes the reply … and marks it `verbatim`" is covered by "A reply pasted as the human wrote it is marked `verbatim`".
> - The reject routes' status names in `## Review` are covered by the three routes under `### What reject means`, which map to the same statuses.
> - "The claim belongs to the node, not to the agent. A crash never releases it." is covered by `## Statuses`, "The claim belongs to the node, so a worker that dies does not release it".
> - "An implementation node cannot be claimed until it carries an acceptance condition. No other kind of node carries one." is covered by `### Claim` and the fenced "implementation only".
>
> **How far the list reaches:** a bounding set, every hunk of both diffs, meaning all removed and all added text. Each before-text statement in those hunks was held against both after-texts. Each added statement was held against both before-texts. Text outside the hunks is unchanged, so it is its own counterpart.
>
> **Observations, not findings.** These are contradictions that were already in the before-texts and that this work did not create or resolve:
> - **When the human may amend a condition.**
>   - `graph-conventions.md` `### \`## Acceptance condition\`` says "The human changes only a condition on a node nobody holds yet. A condition under a live worker reaches the human by that worker's raise, and by no other route."
>   - `SKILL.md` `### Changing one after it is written` says "The human may also amend a condition of their own accord at any time."
>   - The same two statements stood in the before-texts, where they were "The last three change only…" against "…at any time". Their outcomes differ, so the pair is not a shared rule under clause 1. By clause 1's criteria, the `graph-conventions.md` sentences are about the human's choices rather than the file.
> - **Which flags reach the closing report.** `SKILL.md` now holds both "Flags reach the closing report in two cases only" and, under `## Closing an effort`, "Every outstanding flag". An outstanding flag on a node not yet closed fits neither of the two cases. Before, the two statements sat in different files.
> - **Whether you ever render a reply.** `SKILL.md` says "You never render a reply". `graph-conventions.md` says the manager marks `paraphrase` "only where it could not avoid rendering the answer". This is unchanged from the before-texts.
>
> Files:
> - `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/312-cut-the-shared-rules/.claude/skills/expedition/SKILL.md`
> - `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/312-cut-the-shared-rules/.claude/skills/expedition/graph-conventions.md`

*The manager's note, matching the two lists:* the checker's one rule change is the worker's entry 4 (the `DIVERGENCE` mark). The worker judged the move to keep its outcome, and the checker finds it narrows the mark to `## Interview`. Every other entry on the worker's list the checker judged to keep its outcome.


### Gate — approve, 2026-09-25

The human, `verbatim`: *"approve"*

## Flags

`312.1` **· settled** `ASSUMPTION` — graph-conventions.md's node-file template fence still states "implementation only; written by the spawning node". Clause 4 fixes fence text, so I kept that template statement even though the prose rule on who writes a condition now lives in SKILL.md. I read clause 4 as winning over clause 1 for fenced text.

`312.2` **· settled** `ASSUMPTION` — Six overlaps are kept in both files, because I judged the two outcomes different or the graph-conventions.md text a reason rather than a rule. The six are listed under "Borderline overlaps kept in both files" below. A strict checker may count one as a shared rule.

`312.3` **· settled** `ASSUMPTION` — I did not settle node 311's contradiction. graph-conventions.md keeps the human-only-unheld limit and the "no other route" sentence where node 311 expects them. SKILL.md keeps "of their own accord at any time". Moving either sentence would have decided node 311.
