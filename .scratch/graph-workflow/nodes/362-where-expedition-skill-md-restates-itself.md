# Where `expedition/SKILL.md` restates itself

Type: research
Status: resolved
Blocked by: none

## Answer

`expedition/SKILL.md` restates itself in about 380 clear words (queue membership, flag settling, standing steering, agent death) and about 300 borderline; no heading needs renaming to cut them.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The node it surfaced is [node 364](364-cut-the-passages-where-expedition-skill-md-restates-itself.md). Flags 362.1 to 362.3 settle at the node closing report.

## Question

Which passages of `.claude/skills/expedition/SKILL.md` restate another passage of the same file, and what would cutting each save, in words? Known examples: the two standing-yes paragraphs in `## The gate` and `## What is in front of the human, and when`, and item 5 of `## The order you act in` against the tier-1 list.

*Reported by [node 355](355-where-the-manager-read-shipped-files-restate-one-another.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      Where `expedition/SKILL.md` restates itself

ANSWER:

## Answer

### Method and scope

- File measured: `.claude/skills/expedition/SKILL.md` on master at `be27d1e`. The file last changed at `d1e6c52`. I read it in full. Its body is 9,409 words, counted by splitting on whitespace, the same count as `wc -w`.
- Rule measured against: `map.md`, the ground-rules block, standing rule for writing 6. Rule 6 is written about pointing at "a heading of another shipped file". This node applies the same test inside one file, because every manager session reads `SKILL.md` whole, so its reader has always already read the passage being restated (see flag 1). Rule 1 ("Compress the prose that explains why; never compress the shapes") decides which instances are borderline: tables and lists are shapes.
- Sizes are word counts of the quoted passage, with whitespace normalised. "Save" is an estimate: the passage's words minus whatever the passage keeps or the pointer it becomes. Passages are named by heading and opening phrase.
- Node 355 already measured some pairs, and they are not measured again here. They are listed at the end.

### Tier 1: clear instances (the same file states the rule at the heading named)

1. **`## The gate`**, paragraph "A gate that a standing yes covers is handled by the skill `expedition-standing-yes` …", 39 words. It restates the last paragraph of `## What is in front of the human, and when`, "An item that a standing yes covers is handled by the skill …" (51 words), which covers every item, gates included. Cutting it saves 39.
2. **`## The order you act in`**, item 5, bullet "Nothing is waiting when there is …", 74 words. The part from "no gate assembled and unsent" through "say which of them you checked" is 57 words. It lists the four kinds of the pending queue and then says "Those four are the whole, fixed membership of the pending queue under `## What is in front of the human, and when`". That section's tier 1 list (gate, blocked worker, own raise) and tier 2 (relayed interview questions) state the same four. The bullet could say that nothing is waiting when that queue is empty, say which kinds were checked, and keep "A gate whose check will not pass is still waiting." Saves about 35. Caveat: `.claude/rules/expedition-triggers.md` `## Priority` item 5 holds its own copy of the four kinds, on purpose ("this copy stays in context after a compaction"). It stays as it is (see flag 2).
3. **`## The order you act in`**, the paragraph after the list, the sentence "So make the last line of what you send say what the human is to act on, and run item 5's check before you write that nothing is expected of them.", 31 words. It restates `### The last line of a report` ("Every report you put in front of the human ends with one short line naming what is expected of them" and "Write a line saying nothing is expected of them only when nothing is waiting."). The sentence before it ("A turn that ends with the human idle …") stays. Saves about 20 as a pointer, or 31 if cut.
4. **`## Words used exactly`**, bullet "A dead attempt is resumed where you can resume it, …", 43 words. Its first two sentences (31 words) restate the first paragraph of `## When an agent dies or is stopped` ("Resume its attempt wherever you can resume it, rather than replacing it. … an attempt whose agent was stopped from the human's side is never replaced without the human's answer."). "A replacement is a new attempt, recorded after the one it replaces." (12 words) is stated nowhere else and stays. Saves 31. Node 360 is open on this bullet against the glossary's **Attempt**, so this instance is held out of the proposed condition.
5. **`## Words used exactly`**, bullet "You own the map. The effort's ground rules and the standing steering the human has given live in it and nowhere else.", 23 words, up to "nowhere else". It restates `### Standing steering, and standing instructions of one effort`, and contradicts it: that section says "The map is a rule's ordinary home, and usually its only one" and "A rule reaches a shipped skill file only where the human says so". A pointer to that heading removes the contradiction. Saves about 13. The bullet's sentences on the bar's commands stay.
6. **`## What is in front of the human, and when`**, paragraph "A gate waits in arrival order like the other two kinds in tier 1. …", 68 words. It restates "Within a tier, take things in the order they arrived." from the same section. What it adds, and keeps, is that a gate keeps its place although it holds a code slot while it waits, and that you never move a gate ahead on your own judgement. Saves about 35.
7. **`## What is in front of the human, and when`**: the section says three times that tier 1 is fixed. The three are "Tier 1 holds exactly three kinds of thing, and its membership is fixed", "Only the human can add a fourth kind to tier 1. Never infer one yourself." (15 words), and "Tier 1 keeps its three kinds." (5 words). Saves about 10.
8. **Same section**, paragraph "A checker's question never enters the queue either. …", 28 words. "so it needs no place in tier 1. Tier 1 keeps its three kinds." adds nothing, and `### The payload` already says the checker's questions are carried "to the human with the rest of the payload". Saves about 15 (this overlaps item 7 by 5 words).
9. **Same section**, bullet under "Three things never enter the queue", "Settling a flag. It happens at a moment that already exists: an implementation node's gate, or the node closing report of any other node.", 25 words. It restates `## Flags`, "Settle a node's flags at its gate, where it is an implementation node that has one. Otherwise, settle them at the node closing report." Saves about 17 by keeping "Settling a flag." and naming `## Flags`.
10. **`### Picking the next node`**, the sentence "Those flags settle at the node closing report, so a flag it leaves out is settled without the human seeing it.", 21 words. It restates `## Flags` (where flags settle) and `### A flag in a payload` ("a flag left out of the payload is settled without the human seeing it"). Saves 21.
11. **`### A flag in a payload`**, the sentence "A gate taken under a standing yes settles no flag.", 9 words. It restates `## Flags`, "A gate taken under a standing yes is not put to the human, so that node's flags settle at its node closing report too." (24 words). Saves 9.
12. **`### Standing steering, and standing instructions of one effort`**, 311 words, repeats itself.
    - "The next effort starts without it" appears in the paragraph "Some of what binds you …" (47 words) and again in "The map is a rule's ordinary home …" (45 words).
    - "Lives in the map" is said in the bullet "A scope or an emphasis is standing. Write it into the effort's map", in "binds an effort only once it is written into that effort's map. Write it there when the human states it." and in "a rule the human gives lives in the map and nowhere else".
    - In the paragraph "A rule reaches a shipped skill file only where the human says so, …" (69 words), the second sentence, "Carry a rule into a shipped file only on the human's word, …" (34 words), restates the first. Its extra content, "even where you judge the rule to be about the workflow rather than about the effort", stays.
    - Cutting the paragraph "The map is a rule's ordinary home …" and folding the second sentence into the first saves about 65.
13. **`## When an agent dies or is stopped`**, "Find out whether a resume is possible by attempting it …, and never decide it in advance. A failed resume starts no agent and costs nothing, so test whether a resume is possible, and never predict it." The second half repeats the first. The last clause, 20 words from "A failed resume", repeats most. Saves about 10.
14. **Same section**, paragraph "Where an attempt's agent carries the mark of a stop from the human's side, do not replace the attempt on your own, and do not retry the resume." (28 words in that sentence). It restates the section's first paragraph ("never replaced without the human's answer"). The rest of the paragraph, the one question and its two choices, stays. Saves about 15.
15. **The rule that a final stop is never resumed** is stated twice: `## Stopping a running worker` item 5, "No manager resumes an attempt recorded that way." (8 words), and `## When an agent dies or is stopped`, "An attempt recorded as a final stop is never resumed." (10 words). Saves about 8.
16. **`### Picking the next node`**, "An implementation node is startable when its acceptance condition can be written in full, with nothing in it waiting on an open question.", 23 words. It restates `### Where you cannot write one in full` ("The node is not claimed until the condition is complete.") and the paragraph before it in the same section, "One kind of pick waits on the human …" (52 words, which names "a node whose acceptance condition you cannot write in full"). Saves 23.
17. **`### Changing one after it is written`**, "The worker holding the node works to meet the condition as written, and never rewrites it.", 16 words. It restates the sentence just before it ("its condition is handed over as written") and `## What is never yours`' row "rewriting an acceptance condition". Saves 16.

Tier 1 total: about 380 words, about 4 percent of the file. Holding item 4 out for node 360 leaves about 350.

### Tier 2: borderline (a shape, a reason stated locally, or a premise another section needs)

18. **`## What is never yours`**, the table, 221 words. The right-hand cells restate the sections that hold each rule:
    - "re-authoring what an agent wrote" (22) restates `### You write as a scribe`.
    - "authoring an acceptance condition for a node an agent minted" (28) restates `## Acceptance conditions`' "Where an agent minted the node, … you file it".
    - "authoring the text of an agent's flag" (21) restates `## Flags`' first paragraph.
    - "rewriting an acceptance condition" (43) restates `### Changing one after it is written` and `## The checker`'s "Hand a defective condition to the checker as written".
    - "rendering a diff into the conversation" (14) restates `### The payload`'s "Point at the tree rather than rendering the diff into the conversation".
    - "closing an effort" (17) restates `## Closing an effort`'s "Only the human closes an effort. Report that the conditions hold".
    - The table is a shape under rule 1, and it serves as an index. Cutting the cells to heading pointers saves about 70.
19. **Messages that await no answer.** That the node closing report, the notice that an agent died and the effort closing report await no answer is stated at:
    - `## What is in front of the human, and when`, second consequence, "Anything you send that awaits no answer …" (34 words)
    - `## The order you act in` item 5, first bullet, "A message that awaits no answer leaves them nothing to do …" (35 words)
    - the "Three things never enter the queue" bullets for the notice and the report (12 and 15 words)
    - `### Picking the next node`, "It awaits no answer and takes no place in the queue above." (12 words)
    - `## Flags`, "The node closing report awaits no answer"
    - `## When an agent dies or is stopped`, "That notice awaits no answer, and nothing is owed back." (10 words)

    Each copy is also a local reason, and the node closing report is not in the "never enter the queue" list. Saves about 35.
20. **`### Three outcomes, and no fourth`**, "The one other thing that permits a commit is a standing yes covering the gate, which `expedition-standing-yes` takes as the human's approval.", 22 words. It restates standing-yes handling covered by the queue section's standing-yes paragraph. Saves about 22.
21. **`## Flags`**, "Flags reach the effort closing report in one case only: …", 25 words. It overlaps the previous paragraph ("Where the human never speaks again, nothing settles, and those flags stay outstanding") and `## Closing an effort` ("Every outstanding flag"). Saves about 20. Held out for open node 317, which is about exactly these two statements.
22. **Premises restated inside `## Conflicts this contract leaves open` and `## What nothing here settles`.**
    - Conflict 1, "A flag that reaches the human at a gate must carry what was done, why, and the context needed to answer it." (22 words), restates `### A flag in a payload`.
    - Conflict 2, "You may not supply what a condition leaves out, because that would make you the author of the standard the work is judged" (23 words), restates `## The checker`.
    - Item 2, "A flag put in front of the human must be expanded with the context needed to answer it." (18 words), restates `### A flag in a payload`.
    - Item 4, "One bounded class does carry a duty to look … states that duty." (30 words), is a pointer that also summarises its target, which is node 361's question.
    - A conflict has to state its two sides, and heading pointers could do that. Saves about 55 together.
23. **`### Three outcomes, and no fourth`**, "This contract fixes only the order: approval before any commit, and the graph before the cleanup." (16 words). It restates the approve and reject bullets. Saves about 10.
24. **Opening**, "Your job is to keep the graph true, to keep one thing awaiting the human's reply in front of them whenever something is waiting, …" (30 words). It restates `## What is in front of the human, and when`'s first sentence and item 4 of the order. It is a deliberate summary of the job. Saves about 15.
25. **`## Stopping a running worker`**, last paragraph, "Every resume you attempt on that agent is then refused, while the human can still revive the agent by typing to it." (22 words). Against it: `## When an agent dies or is stopped`, the third outcome "No resume is attempted at all", "An agent stopped by the user still has its transcript, and the human can still revive it." (17 words), and the question's first choice "the human revives the agent by typing to it". Saves about 20.
26. **`## Stopping a running worker`**, "A worker stopped with `TaskStop` keeps its transcript. It can be resumed afterwards within your session, like any other stopped agent." (21 words). It overlaps `## When an agent dies or is stopped`'s "Resuming is limited to your own session." Saves about 10. The same section's "So where you need a worker to actually stop, use `TaskStop`, and never a message." (15 words) repeats its opening ("you perform it with `TaskStop`"). Saves about 12.
27. Small ones:
    - `## Words used exactly`, "You are the manager, and you own and write the graph's files." (13 words), against `## Writing the graph`, "You are the only writer of the graph's record." Saves about 10.
    - `## The checker`, "Copy the block of ground rules as text, and add nothing of your own." (14 words), against its own bullet "copied as text". Saves about 8.
    - `## Starting an effort`, "Both produce the same thing, … and they differ only in their input." (18 words), against "told apart by their input". Saves about 6.

Tier 2 total: about 300 words.

### Checked and not instances

- `## Words used exactly`, "A sweep runs only on an empty frontier." `## Starting an effort` says an empty frontier triggers the sweep. It does not say the sweep runs only then.
- `## Writing the graph`, "A worker performs `### Change the map` in the third branch of the test below …". It ties the procedure's name to the third branch, which does not name the procedure.
- `### Picking the next node`, "you perform such a stop with `TaskStop`, as `## Stopping a running worker` says". It is a pointer.
- `## Spawning a worker`, "Write a note only from context you already hold", against the queue section's "Write the line from context you already hold". The two sentences are about different things.
- The opening's "nothing you send one may tell it to address the human directly", against the spawn bullet "no channel to the human". The first limits what the manager writes. The second says what a spawn states.

### Already measured by node 355, not measured again

- The steady-state frontier rule in `## Starting an effort` and `## Closing an effort` (node 355, Tier 2, item 18).
- `### The four constraints on a condition you write yourself`, item 2's list of three rules (node 355, Tier 2, item 13). *Inference:* inside this file, it also repeats the first paragraph of `## Acceptance conditions`.
- The two standing-yes paragraphs (item 1 above). Node 355 gave 41 words for the one in `## The gate`, and this count is 39 at `be27d1e`.

### What this settles

Cutting the clear instances saves about 380 words of the 9,409 that every manager session loads, and about 350 once the one passage held for node 360 is set aside. The borderline instances hold about 300 more. They turn on rule 1's protection of shapes, on node 361's question about pointers that summarise, and on node 317. The biggest single clusters are:
- `### Standing steering, and standing instructions of one effort` (about 65)
- the pending-queue rules repeated between `## The order you act in` and `## What is in front of the human, and when` (about 95 over items 2, 6, 7 and 8)
- when flags settle (about 47 over items 9 to 11)

INDEX LINE:    `expedition/SKILL.md` restates itself in about 380 clear words (queue membership, flag settling, standing steering, agent death) and about 300 borderline; no heading needs renaming to cut them.

FLAGS:
- ASSUMPTION: Standing rule for writing 6 is written about restating "another shipped file". The node asks about one file restating itself. I applied rule 6's test by analogy, since the manager reads `SKILL.md` whole and has always already read the passage restated, and used rule 1 to mark tables and lists as borderline. What I did: I read `SKILL.md` in full, grouped the passages that state the same rule, and counted each passage's words at `be27d1e`.
  Index: Applied rule 6's point-don't-restate test inside one file by analogy, and counted tables and lists as borderline under rule 1.
- ASSUMPTION: The proposed condition shortens `## The order you act in` item 5's list of the four kinds of the pending queue, while `.claude/rules/expedition-triggers.md` `## Priority` keeps its own full list. That file says it holds a copy that survives compaction and that the skill holds the governing statement, so a fuller copy there contradicts nothing. What I did: I left the rules file out of the condition and named it as unchanged.
  Index: Let `SKILL.md` item 5 point at the pending queue while the triggers file keeps its fuller copy of the four kinds.
- ASSUMPTION: I held two clear-or-near instances out of the proposed condition because open nodes decide them: the dead-attempt bullet in `## Words used exactly` (node 360) and `## Flags`' "Flags reach the effort closing report in one case only" (node 317). What I did: I listed them with their sizes and wrote no clause for them.
  Index: Held the passages that open nodes 360 and 317 decide out of the proposed `SKILL.md` self-restatement cut.

NEW NODES:

1. Name: Cut the passages where `expedition/SKILL.md` restates itself
   Kind: implementation
   Blocked by: none (node 362 resolves with this handover)
   Question: Can the passages of `.claude/skills/expedition/SKILL.md` that restate a rule the same file states at another heading be cut or turned into pointers to that heading, without losing a rule?
   Acceptance condition:
   > Scope: the scope came from no search command. The places are a bounding set: node 362's worker read `.claude/skills/expedition/SKILL.md` in full and listed the passages below from that reading. If you find another passage of that file that restates a rule the same file states elsewhere, report it and do not edit it.
   >
   > All clauses concern `.claude/skills/expedition/SKILL.md`.
   >
   > 1. `## The gate`: the paragraph beginning "A gate that a standing yes covers" is removed. The last paragraph of `## What is in front of the human, and when`, beginning "An item that a standing yes covers", stays and still names the skill `expedition-standing-yes`.
   > 2. `## The order you act in`, item 5, the bullet beginning "Nothing is waiting when there is": it no longer lists the four kinds (gate assembled and unsent, worker blocked on a raise, the manager's own raise, relayed question). It says instead that nothing is waiting when the pending queue under `## What is in front of the human, and when` holds nothing. It still requires saying which of the queue's kinds were checked, and it still says that a gate whose check will not pass is still waiting. `.claude/rules/expedition-triggers.md` is not changed.
   > 3. `## The order you act in`, the paragraph after the numbered list: the sentence beginning "So make the last line of what you send" is removed or replaced by a sentence naming `### The last line of a report`. The sentence beginning "A turn that ends with the human idle" stays.
   > 4. `## Words used exactly`, the bullet beginning "You own the map.": it no longer states where the ground rules and the standing steering live, and names `### Standing steering, and standing instructions of one effort` for that. Its sentences about where the map records the bar's commands, and about confirming that record against the repo, stay.
   > 5. `## What is in front of the human, and when`, the paragraph beginning "A gate waits in arrival order": it no longer restates that a gate is sent after every older thing in tier 1, which the sentence "Within a tier, take things in the order they arrived." already states. It still states that a gate keeps its place in arrival order although it holds a code slot while it waits, and that the manager never moves a gate ahead on its own judgement.
   > 6. `## What is in front of the human, and when`: the section states only once that tier 1's membership is fixed and that only the human can add a kind to it. The sentence "Tier 1 keeps its three kinds." is removed. The paragraph beginning "A checker's question never enters the queue" still states that a checker's question never enters the queue and travels inside the gate payload.
   > 7. `## What is in front of the human, and when`, the bullet beginning "Settling a flag.": it no longer states when a flag settles. For that it names `## Flags`.
   > 8. `### Picking the next node`: the sentence "Those flags settle at the node closing report, so a flag it leaves out is settled without the human seeing it." is removed. The sentence stating that a node closing report carries every flag the node holds, in the fuller form under `### A flag in a payload`, stays.
   > 9. `### A flag in a payload`: the sentence "A gate taken under a standing yes settles no flag." is removed. `## Flags` still states that a gate taken under a standing yes is not put to the human and that its node's flags settle at its node closing report.
   > 10. `### Standing steering, and standing instructions of one effort`: the section states each of the following once. A standing rule binds an effort only once it is written into that effort's map, and it is written there when the human states it. The next effort starts without it. A rule reaches a shipped skill file only on the human's word, as a node, and never on the manager's own judgement, even where the manager judges the rule to be about the workflow rather than about the effort. Where the human says nothing about a rule's scope, the rule is the effort's alone. The paragraph beginning "The map is a rule's ordinary home" no longer exists as a separate restatement. The section's two bullets, its statement that a standing instruction is recorded as the human's in their words and never presented as a rule of the workflow, and its paragraph beginning "Every worker on an effort is bound" stay.
   > 11. `## When an agent dies or is stopped`: the section says only once that whether a resume is possible is found by attempting it and never predicted. The paragraph beginning "Where an attempt's agent carries the mark of a stop from the human's side" no longer restates that such an attempt is not replaced without the human's answer. It still says to keep the node claimed and not to retry the resume, and it still gives the one question with what it names, what would be lost, and its two choices.
   > 12. The rule that an attempt recorded as a final stop is never resumed is stated once in the file: either in `## Stopping a running worker` item 5 or in the first paragraph of `## When an agent dies or is stopped`.
   > 13. `### Picking the next node`: the sentence "An implementation node is startable when its acceptance condition can be written in full, with nothing in it waiting on an open question." is removed. `### Where you cannot write one in full` still states that the node is not claimed until the condition is complete.
   > 14. `### Changing one after it is written`: the sentence "The worker holding the node works to meet the condition as written, and never rewrites it." is removed. The sentence stating that a condition a worker already holds is handed over as written stays.
   > 15. For each passage changed under clauses 1 to 14, every statement it no longer holds is still stated at the heading or passage the clause names. No rule is lost.
   > 16. These passages are not changed: the bullet of `## Words used exactly` beginning "A dead attempt is resumed", and the paragraph of `## Flags` beginning "Flags reach the effort closing report".
   > 17. No heading in `.claude/skills/expedition/SKILL.md` is renamed, added or removed. Every heading a changed passage names exists in the file with exactly the named text.
   > 18. No file other than `.claude/skills/expedition/SKILL.md` changes.
   Note for the manager: open node 89 also changes `.claude/skills/expedition/SKILL.md`, and open node 359 cites its headings (this node renames none). Check for overlapping edits before you fill a slot.

INVALIDATIONS:
- Node 355, an extension and a small correction. Its `### Outside the files asked about` gives the `## The gate` standing-yes paragraph as 41 words. It measures 39 at `be27d1e`. Its two examples of the file restating itself are confirmed and join about 15 other instances listed here.
- No resolved node is contradicted.

CONDITIONS: I searched every open or claimed node's `## Acceptance condition` and `## Question` sections (66 nodes) for `expedition/SKILL.md`, "restat", "standing yes", "order you act in", "Standing steering", "pending queue", "tier 1", "What is never yours", "When an agent dies", "Stopping a running worker", "Words used exactly", "last line of a report" and "Picking the next node". Matches came from nodes 34, 83, 87, 89, 104, 152, 156, 190, 317, 359, 360, 361 and 362 itself. I read what matched.
- Node 317 (open, implementation, no condition yet) concerns the same `## Flags` passage as Tier 2 item 21. My work leaves its question as it is, and I held that passage out of the proposed condition.
- Node 360 (open, grilling): part of its question is informed but not changed. The `## Words used exactly` dead-attempt bullet it names also restates `## When an agent dies or is stopped` inside the same file (Tier 1 item 4). So whichever copy node 360 keeps, the bullet's first two sentences are a restatement.
- Node 361 (open, grilling): Tier 2 item 22's `## What nothing here settles` item 4 is another example of its question. Its question does not change.
- Node 89 (open) edits the same file. Its condition is not made wrong.
- None of the other matches is affected. I wrote no replacement clauses.

MISSING FROM MAP: Standing rule for writing 6 covers restating another shipped file, and the map states no rule for a file restating itself. I went on by applying rule 6's test by analogy (flag 1).

RETROSPECTIVE
1. What I had to hunt for: whether any open node already owns a passage I would list. That meant searching the conditions and questions, which turned up nodes 317 and 360. I also had to find whether a restated passage has a deliberate copy elsewhere, which is `expedition-triggers.md` for item 5. The rules file was in my context by chance and not through the spawn.
2. What arrived that this node did not need: most of `map.md`. Only the ground-rules block and the writing rules bore on the work. Most of node 355's handover was about other files. Its `### Outside the files asked about` and the list of what it measured were the parts I used.
3. What would have made this easier: a spawn line naming the open nodes that already touch `SKILL.md` passages (317, 360, 361, 89). A line saying whether rule 6 is meant to govern restatement inside one file, or only between files.
4. What was stale, wrong or contradictory: `SKILL.md` `## Words used exactly` says ground rules and standing steering "live in it and nowhere else". `### Standing steering, and standing instructions of one effort` says the map is "usually" a rule's only home and that a rule can reach a shipped file on the human's word. Node 317's `## Question` still quotes "two cases only". Its manager note records that the passage now says "one case only". Node 355 gave the gate's standing-yes paragraph as 41 words, and it is 39 now.
`````

## Flags

`362.1` `ASSUMPTION` **· settled** — Standing rule for writing 6 is written about restating "another shipped file". *(The worker's full text is under its handover's `FLAGS`.)*

`362.2` `ASSUMPTION` **· settled** — The proposed condition shortens `## The order you act in` item 5's list of the four kinds of the pending queue, while `.claude/rules/expedition-triggers.md` `## Priority` keeps its own full list. *(The worker's full text is under its handover's `FLAGS`.)*

`362.3` `ASSUMPTION` **· settled** — I held two clear-or-near instances out of the proposed condition because open nodes decide them: the dead-attempt bullet in `## Words used exactly` (node 360) and `## Flags`' "Flags reach the effort closing report in one case only" (node 317). *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-09-28:* flags 362.1 to 362.3 settle at the node closing report that closes this node.
