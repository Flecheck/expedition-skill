# Where the manager-read shipped files restate one another

Type: research
Status: resolved
Blocked by: 354

## Answer

About 380 words of the manager-read files restate a heading the manager already reads, mostly in the stop, standing-yes and cleanup skills; about 330 borderline and 500 glossary-paired words wait on a decision.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The nodes it surfaced are [node 359](359-point-the-manager-read-files-at-the-headings-they-restate.md), [node 360](360-which-copy-stays-where-the-glossary-and-a-contract-agree.md), [node 361](361-whether-a-pointer-that-summarises-its-target-restates-it.md), [node 362](362-where-expedition-skill-md-restates-itself.md). Flags 355.1 and 355.2 settle at the node closing report.

## Question

Under node 253's rule, which passages in the files the manager reads (`expedition/SKILL.md`, `graph-conventions.md`, `adoption.md`, `wayfinder-divergences.md`, `expedition-stop`, `expedition-standing-yes`, `expedition-cleanup`) restate a heading of another of those files that the same reader already reads, and what would pointing save, in words? This includes `expedition-stop`'s `## New work stops`, which suspends the top-up rule without naming its heading (see INVALIDATIONS).

*Reported by [node 253](253-a-shipped-file-points-at-a-sibling-rather-than-restating-it.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words: "Offered because of the human's priority on compaction. I did not ask it: the reply did not reach it, and whether and when to work it is the manager's call."*

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      Where the manager-read shipped files restate one another

ANSWER:

## Answer

### Who reads what (the test's input)

- The manager is told to read `graph-conventions.md` and `glossary.md` before it touches an effort's files. Source: `.claude/skills/expedition/SKILL.md`, opening, "Read it and the glossary, `glossary.md`, before you touch an effort's files." So every manager-read file shares a reader with `SKILL.md`, `graph-conventions.md` and `glossary.md`.
- No worker contract points at `graph-conventions.md`. Source: `grep -ln graph-conventions .claude/skills/*/SKILL.md` returned only `expedition/SKILL.md` and `expedition-standing-yes/SKILL.md`. *Inference:* the manager is the only reader of `graph-conventions.md`, so a restatement between it and `SKILL.md` always has a shared reader.
- `adoption.md` tells its reader to read `SKILL.md`'s `## Starting an effort` and `graph-conventions.md`'s `### Start an effort` first. Source: `adoption.md`, opening.
- `wayfinder-divergences.md` has two readers. One comes from `adoption.md` step 5 and has read `adoption.md`. The other comes from `graph-conventions.md`'s opening ("see `wayfinder-divergences.md`") and has not.
- `expedition-stop`, `expedition-standing-yes` and `expedition-cleanup` are invoked in the manager thread, so their reader has already read `SKILL.md`, `graph-conventions.md` and `glossary.md`. `SKILL.md`'s reader reads `expedition-standing-yes` only once it is invoked. *Inference:* the short standing-yes statements in `SKILL.md` are not instances.
- Rule measured against: `map.md`, ground-rules block, standing rule for writing 6.

Word counts are `wc -w` over the passage quoted or over the stated line span, measured on master at `4601bb0`. "Save" is an estimate: the passage's words minus a pointer sentence of about 12 to 20 words. Passages are cited by heading and opening phrase.

### Tier 1: clear instances (the reader already reads the heading restated)

1. **`expedition-stop` `## What the next manager starts from`**, from "Three states look like an ordinary" through "Parked: `open`, with a non-empty interview." 62 words. It restates `SKILL.md` `### Three states the status line does not show`, whose three bullets say the same thing. Save about 45.
2. **`expedition-stop` `## Agents still running when the session ends`**, the whole section. 72 words. It restates `SKILL.md` `## When an agent dies or is stopped`: "You cannot resume any attempt from an earlier session", replacement, and "Give the new agent the node and everything the human has already said on it … The human never sees the same question twice." The section already names that heading. *Inference:* it states nothing that heading lacks. Save about 50.
3. **`expedition-stop` `## New work stops`**, 44 words. It is the instance node 253 named. It suspends two rules without naming their headings: `SKILL.md` `### Picking the next node` ("When a node finishes, pick the next one, spawn its worker" and "start enough work to bring every count back up to its number") and `SKILL.md` `## The order you act in` item 3 ("Spawn an agent, within the limits."). Rule 6's third sentence asks that both be named by heading. This saves nothing and adds about 10 words. The same passage also suspends `.claude/rules/expedition-triggers.md`'s first trigger ("When a node finishes, look at the frontier and start a replacement"), which is outside the files this node was asked about.
4. **`expedition-standing-yes` `## Recording the invocation`**, the sentences "It binds only once it is written into the map." and "It is this effort's alone, so the next effort starts without it." About 22 words. They restate `SKILL.md` `### Standing steering, and standing instructions of one effort` ("binds an effort only once it is written into that effort's map"; "the rule is the effort's alone"; "the next effort starts without it"). The sentence before them already names that heading. "It stays in force until the human changes it" is not stated there, and stays. Save about 22.
5. **`expedition-standing-yes` `## Taking a covered item`**, step 1, from "Mark the entry `standing yes`, and never `verbatim`." through "or the checker's `PASS`." 35 words. It restates `graph-conventions.md` `### Recording the human's words` almost word for word ("It quotes the scope text of that standing yes word for word, says which standing yes was applied, and quotes what was taken"). The step then points at that same heading. Save about 35.
6. **`expedition-standing-yes` `## Taking a covered item`**, opening, "A covered item never enters the pending queue, and you do not put it to the human." 17 words. It restates `SKILL.md` `## What is in front of the human, and when`, last paragraph ("you do not put it to the human. Such an item never enters the queue."). Save about 15.
7. **`expedition-standing-yes` `## Flags, and the node closing report`**, first paragraph. 42 words. It restates `SKILL.md` `## Flags` ("A gate taken under a standing yes is not put to the human, so that node's flags settle at its node closing report too") and `### A flag in a payload` ("A gate taken under a standing yes settles no flag"). Save about 30. The same section's "It carries every flag the node holds, as any node closing report does." (13 words) restates `SKILL.md` `### Picking the next node` ("A node closing report for a node holding flags carries every one of those flags"). Save about 13.
8. **`expedition-cleanup` `## The rule this skill is an exception to`**, first paragraph. 82 words. It restates `graph-conventions.md`'s opening paragraph "No edit deletes. …", which already states the exception for an invoked act whose purpose is removal, and the entry it leaves. That paragraph sits above `## The seven files` and has no heading of its own. So rule 6's "point at a heading" can only be met by citing it with a quoted phrase, as rule 4 allows, or by giving it a heading. "Remove only text that the effort's version control history already holds" is the skill's own rule and stays. Save about 60.
9. **`expedition-cleanup` `## Flag cleanup`**, "A settled flag whose line has been removed is not a mismatch under the mechanical check that joins …" 28 words. It restates `graph-conventions.md` `## Mechanical checks` check 6 ("A settled flag whose index line has been removed is not a mismatch."). Save about 20. The section's "The effort closing report is built from its lines whose flag is not yet settled." (15 words) restates `SKILL.md` `## Closing an effort` ("taken from the unchecked lines of the effort's index of flags"). Save about 8.
10. **`graph-conventions.md` `### Change the map`**, second paragraph, "The manager runs this procedure, except in one case. …" 56 words. It restates `SKILL.md` `## Writing the graph` ("A worker performs `### Change the map` in the third branch of the test below, and you perform it otherwise", plus the third branch itself), and already names that heading. Under node 312's split, who performs an act is a manager choice, which is `SKILL.md`'s side. Save about 40.
11. **`adoption.md`**, second paragraph of its opening, "Adoption is a way of starting an effort, and not a kind of node. You perform it, before the graph exists. It produces the same files … already exists." 42 words. It restates `SKILL.md` `## Starting an effort` (performed by the manager before the graph exists; the two ways "differ only in their input"). The first paragraph has just told the reader to read that heading. "This file calls that directory's existing files the foreign record." stays. Save about 35.
12. **`expedition-stop`**, opening, "because only the human closes an effort". About 7 words. It restates `SKILL.md` `## Closing an effort`. Save about 5. This is trivial, and it is left out of the proposed condition.

Tier 1 total: about 380 words, out of 11,520 words across `expedition/SKILL.md` and the three invoked skills. By file: `expedition-stop` about 100 of 567, `expedition-standing-yes` about 115 of 797, `expedition-cleanup` about 90 of 747, `graph-conventions.md` about 40, `adoption.md` about 35. So the three invoked skills shrink by roughly 13 to 18 percent each.

### Tier 2: borderline (a reading of rule 6 is needed)

13. **Pointers that also list what their target holds.** Each of these names the heading, as rule 6 asks, and then summarises that heading's contents. Node 312's answer says the pointers it left are "one-sentence" (node 312, `## Answer`).
    - `SKILL.md` `### The human's words`, last paragraph, "`### Recording the human's words` in `graph-conventions.md` holds the form of each entry: …". 57 words. Save about 35.
    - `graph-conventions.md` `### Recording the human's words`, first paragraph, "`### The human's words` in `SKILL.md` says when the manager records an answer, what it pastes, …". 53 words. Save about 30.
    - `SKILL.md` `## Acceptance conditions`, first paragraph, "`## The node file` in `graph-conventions.md` says which nodes carry …". Three sentences, 86 words. Save about 50.
    - `SKILL.md` `### The four constraints on a condition you write yourself`, item 2's list of the three rules. Save about 15.
14. **`graph-conventions.md` `` ### `## Annotation` ``**, "An annotation is the manager's to write and never a worker's, because `## Writing the graph` in `SKILL.md` makes the manager the only writer … writes the annotation from that report." 51 words. It restates `SKILL.md` `## Writing the graph` and the handover's `INVALIDATIONS` part. Save about 30.
15. **`adoption.md` `## Your steps, in order`**:
    - Step 2's list of reserved names (11 words) restates `graph-conventions.md` `## The seven files`. Save about 6.
    - Step 3's bullets restate `SKILL.md` `## Starting an effort`'s list of six things. What adoption adds is "copied verbatim" and "built from the foreign record's own statements". Save about 25.
    - Step 7.4, "Run checks 1, 3 and 4 … as step 9 of `### Start an effort` requires" (22 words), restates that step. Save about 15.
16. **`adoption.md` `### What an imported node looks like`**, the "Its name." bullet's example restates `graph-conventions.md` `## Adding a node`'s `nodes/24-auth-2-token-refresh.md` example. Save about 10. `## Git history`'s last sentence restates the glossary's **Node trailer**. Save about 15.
17. **`wayfinder-divergences.md` `## Not covered here`**, 34 words. The reader who comes from `adoption.md` step 5 has already read what its second sentence summarises. The reader who comes from `graph-conventions.md` has not. Save about 20, for the first reader only.
18. **The rule that an effort not expected to end has a steady-state frontier** is stated three times: `SKILL.md` `## Starting an effort` (63 words, "The expectation decides what an empty frontier means"), `SKILL.md` `## Closing an effort` ("A frontier that never empties is a legitimate steady state"), and `graph-conventions.md` `## The seven files`' `## Destination` bullet (about 35 words). Save about 30.
19. **The parked state** is stated in both `graph-conventions.md` `## Statuses` ("A parked node is `open` with a non-empty `## Interview`") and `SKILL.md` `### Three states the status line does not show`. About 12 words.

Tier 2 total: about 330 words.

### Tier 3: pairs with `glossary.md`, which the manager is told to read

Each pair states one rule both in a glossary entry and at a heading of a contract. Which copy is the home is not settled. `SKILL.md` `## Words used exactly` says a section's rule wins over the glossary, and the glossary says it defines the terms. Sizes are the glossary entry's words and the contract passage's words.

- `SKILL.md` `## Words used exactly`, bullet "A dead attempt is resumed where you can resume it, …" (43), and glossary **Attempt** (61). Near word for word. *Inference:* the bullet adds nothing to the entry, although the section says its bullets "add what those terms demand of you in particular".
- `SKILL.md` `## Words used exactly`, bullet "A handover has seven parts every time: …" (72), and glossary **Handover** (70). Near word for word.
- `SKILL.md` `### You write as a scribe` (76) and glossary **Scribe** (78).
- `SKILL.md` `## Closing an effort` (89), and glossary **Closed** (59) with **Effort closing report** (44). The report's contents list is word for word.
- `SKILL.md` `## Starting an effort`, first two paragraphs (75), and glossary **Starting an effort** (56).
- `adoption.md` `## Your steps, in order`, steps 1 to 4 and 7, and glossary **Adoption** (88), which lists the same steps.
- `SKILL.md` `### Picking the next node` and `## Flags`, and glossary **Node closing report** (80) and **Flag** (106; about 55 of those words cover when a flag settles).
- `SKILL.md` `## Stopping a running worker`, and glossary **Stop** (93) and **Final stop** (43).
- `graph-conventions.md` `## The seven files`' `## Destination` bullet, and glossary **Destination** (70).

Tier 3 upper bound: about 500 words, if one copy of each pair were cut down to a pointer or to a defining sentence.

### Checked and not instances

- `expedition-stop` `## Finish the work already under way`. It points at `## What is in front of the human, and when`, `## What is never yours` and `### Three outcomes, and no fourth` by heading, and restates none of them.
- `wayfinder-divergences.md` `## Changed`. Its block is text appended to a foreign tracker doc, so it has to be restated. `## Unchanged` and `## Added` are differences from a foreign scheme, not restatements for this reader.
- `expedition-standing-yes` step 2's `STANDING YES:` resume line. The worker contracts hold that line, and the manager does not read the worker contracts.
- The standing-yes pointers inside `SKILL.md`. Their reader has not read `expedition-standing-yes` unless it has been invoked.

### Outside the files asked about (noted, not measured in full)

- `.claude/rules/expedition-triggers.md` `## Priority` copies `SKILL.md` `## The order you act in` items 1 to 5 on purpose. Its stated ground is "this copy stays in context after a compaction."
- `SKILL.md` restates itself. Its standing-yes paragraph in `## The gate` (41 words) and the one in `## What is in front of the human, and when` (51 words) are nearly identical. Item 5 of `## The order you act in` lists the pending queue's four kinds, which the tier-1 list states again.

### What this settles

Pointing would save about 380 words at the clear instances. That is most of it in the three invoked skills, which are the files the human finds long. The borderline instances hold about 330 more, and the glossary pairs up to about 500 more, but both of those depend on a reading or a decision that is not yet made. The `## New work stops` fix saves nothing and costs about 10 words.

INDEX LINE:    About 380 words of the manager-read files restate a heading the manager already reads, mostly in the stop, standing-yes and cleanup skills; about 330 borderline and 500 glossary-paired words wait on a decision.

FLAGS:
- ASSUMPTION: The question lists seven files and leaves out `glossary.md`. The spawn lists it as a source, and `SKILL.md`'s opening tells the manager to read it. So I treated it as a file the manager already reads, and reported its overlaps in a separate tier (Tier 3) without choosing which copy is the home. The glossary has no heading per term, only bold entries under group headings, so pointing at it means pointing at a term. What I did: I read all eight files in full, listed the glossary entries that restate a contract passage, and measured both sides with `wc -w`.
  Index: Counted `glossary.md` as manager-read and listed its overlaps with the contracts apart, not deciding which copy stays.
- ASSUMPTION: Some pointers name the heading, as rule 6 asks, and then summarise that heading's contents; one is three sentences long. Rule 6 does not say whether such a summary counts as restating, so I put these pointers in Tier 2 as borderline, not in Tier 1. Node 312's answer describes its pointers as "one-sentence", which some of these are not. What I did: I measured each pointer paragraph and estimated what cutting it to a one-sentence pointer would save.
  Index: Classed pointers that also summarise their target as borderline under rule 6, not as clear restatements.

NEW NODES:

1. Name: Point the manager-read shipped files at the headings they restate
   Kind: implementation
   Blocked by: none (node 355 resolves with this handover)
   Question: In the stop, standing-yes and cleanup skills, `graph-conventions.md` and `adoption.md`, can the passages node 355 found restating a heading the manager already reads be replaced by pointers to that heading, and can `## New work stops` name the rules it suspends?
   Acceptance condition:
   > Scope: the scope came from no search command. The places are a bounding set: node 355's worker read these eight files in full: `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/graph-conventions.md`, `.claude/skills/expedition/adoption.md`, `.claude/skills/expedition/wayfinder-divergences.md`, `.claude/skills/expedition/glossary.md`, `.claude/skills/expedition-stop/SKILL.md`, `.claude/skills/expedition-standing-yes/SKILL.md` and `.claude/skills/expedition-cleanup/SKILL.md`. It listed the passages below from that reading. If you find another passage that restates a heading of another of those files, report it and do not edit it.
   >
   > 1. `.claude/skills/expedition-stop/SKILL.md`, `## What the next manager starts from`: the three bulleted states (waiting at a gate, a worker holding an unanswered question, parked) and the sentence introducing them are no longer written out. The section names the heading `### Three states the status line does not show` in `.claude/skills/expedition/SKILL.md` instead. The sentence "Write no handoff document" and the sentence about finding a live worktree through version control stay.
   > 2. `.claude/skills/expedition-stop/SKILL.md`, `## Agents still running when the session ends`: the section no longer states how the next manager replaces an attempt, or what the new attempt is given. For that it names `## When an agent dies or is stopped` in `.claude/skills/expedition/SKILL.md`. It may still state that the next manager cannot resume an attempt that is still running.
   > 3. `.claude/skills/expedition-stop/SKILL.md`, `## New work stops`: the section names each rule it suspends by its heading in `.claude/skills/expedition/SKILL.md`: `### Picking the next node` and `## The order you act in`. It states the change in its own words: claim no node, spawn a worker only for a node already under way, leave the frontier as it is, and leave the counts below their numbers when a node finishes. It does not restate the suspended rules.
   > 4. `.claude/skills/expedition-standing-yes/SKILL.md`, `## Recording the invocation`: the section no longer states that the invocation binds only once it is written into the map, or that it is this effort's alone and the next effort starts without it. It keeps its pointer to `### Standing steering, and standing instructions of one effort`, the sentence that the invocation stays in force until the human changes it, and the paragraph on more than one standing yes being in force.
   > 5. `.claude/skills/expedition-standing-yes/SKILL.md`, `## Taking a covered item`: step 1 no longer states how the entry is marked or what it quotes (the `standing yes` mark, never `verbatim`, the scope text word for word, which standing yes was applied, and what was taken). For that it names `### Recording the human's words` in `.claude/skills/expedition/graph-conventions.md`. Step 1 still says that a question or a raise is recorded under `## Interview` and a gate under `## Review`. The section's opening no longer states that a covered item never enters the pending queue and is not put to the human, except by naming `## What is in front of the human, and when` in `.claude/skills/expedition/SKILL.md`. The instruction to take the item in the same turn stays.
   > 6. `.claude/skills/expedition-standing-yes/SKILL.md`, `## Flags, and the node closing report`: the section no longer states that a gate taken under a standing yes settles no flag and that the node's flags settle at the node closing report, except by naming `## Flags` in `.claude/skills/expedition/SKILL.md`. The sentence "It carries every flag the node holds, as any node closing report does." is removed. The section still says that the node closing report names every item taken under a standing yes with its scope, and that the human may take a listed item back by naming it.
   > 7. `.claude/skills/expedition-cleanup/SKILL.md`, `## The rule this skill is an exception to`: the first paragraph no longer restates the never-delete rule or its exception for an invoked act whose purpose is removal. It points at the opening paragraph of `.claude/skills/expedition/graph-conventions.md` that begins "No edit deletes.", by quoting that phrase or, if that paragraph is given a heading in this change, by the heading. The sentence "Remove only text that the effort's version control history already holds, so the entry's claim is true." stays in meaning.
   > 8. `.claude/skills/expedition-cleanup/SKILL.md`, `## Flag cleanup`: the sentence "A settled flag whose line has been removed is not a mismatch under the mechanical check that joins a node's `## Flags` entry to its line in `flags.md`." is replaced by a pointer to check 6 under `## Mechanical checks` in `.claude/skills/expedition/graph-conventions.md`, or is removed.
   > 9. `.claude/skills/expedition/graph-conventions.md`, `### Change the map`: the paragraph beginning "The manager runs this procedure, except in one case." no longer restates who runs the procedure. It names `## Writing the graph` in `.claude/skills/expedition/SKILL.md` for that.
   > 10. `.claude/skills/expedition/adoption.md`, opening: the sentences "Adoption is a way of starting an effort, and not a kind of node. You perform it, before the graph exists. It produces the same files as starting from a conversation, and its input is a directory of work that already exists." are no longer stated. The sentence "This file calls that directory's existing files the foreign record." stays.
   > 11. For each passage changed under clauses 1 to 10, every statement it no longer holds is still stated at the heading or passage the clause names. No rule is lost.
   > 12. No heading in any file under `.claude/skills/` is renamed. The one allowed addition is a heading for the paragraph in clause 7. Every heading a changed passage cites exists in the named file with exactly the cited text.
   > 13. No file other than the six named in clauses 1 to 10 changes.
   Note for the manager: node 357 (claimed) edits `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition/glossary.md`. This node only cites `SKILL.md` and does not edit it, but check for overlapping edits before you fill a slot.

2. Name: Which copy stays where the glossary and a contract state the same rule
   Kind: grilling
   Blocked by: none
   Question: For the pairs node 355 lists in its Tier 3 (for example `SKILL.md`'s attempt and handover bullets under `## Words used exactly`, which nearly repeat the glossary's **Attempt** and **Handover**, and `## Closing an effort`, which repeats **Closed** and **Effort closing report**), which copy stays: the glossary entry cut to its defining sentence, or the contract passage replaced by a pointer to the entry? This decides up to about 500 words.

3. Name: Whether a pointer that summarises its target restates it
   Kind: grilling
   Blocked by: none
   Question: Under standing rule for writing 6, does a pointer that names a heading and then summarises what that heading holds count as restating it? Examples: `SKILL.md` `## Acceptance conditions`' three-sentence first paragraph, `SKILL.md` `### The human's words`' last paragraph, and `graph-conventions.md` `### Recording the human's words`' first paragraph. If it does, should every such pointer be one sentence? This decides about 330 words (node 355, Tier 2).

4. Name: Where `expedition/SKILL.md` restates itself
   Kind: research
   Blocked by: none
   Question: Which passages of `.claude/skills/expedition/SKILL.md` restate another passage of the same file, and what would cutting each save, in words? Known examples: the two standing-yes paragraphs in `## The gate` and `## What is in front of the human, and when`, and item 5 of `## The order you act in` against the tier-1 list.

INVALIDATIONS:
- Node 312, a narrowing. Its answer says "Each rule that both … stated is now stated in one of them" and "Where the other file needs the rule, it now has a one-sentence pointer to a heading." Two exceptions remain in the landed text. First, who runs `### Change the map` is still stated both in `graph-conventions.md` `### Change the map` and in `SKILL.md` `## Writing the graph`. Second, `SKILL.md` `## Acceptance conditions`' pointer paragraph is three sentences, and `SKILL.md` `### The human's words`' pointer paragraph is two.
- Node 166 (the stop skill), an extension of the narrowing node 253 already recorded. `## New work stops` suspends `## The order you act in` item 3 as well as `### Picking the next node`, and neither is named.

CONDITIONS: I searched every open and claimed node's `## Acceptance condition` and `## Question` for these terms: `expedition-stop`, `expedition-standing-yes`, `expedition-cleanup`, `adoption.md`, `wayfinder-divergences`, `glossary.md`, "What the next manager starts from", "Agents still running", "Taking a covered item", "Recording the invocation", "rule this skill is an exception", "Flag cleanup", "New work stops", "Three states", "Change the map", "Recording the human's words", "The human's words", "Standing steering", "Words used exactly", "Closing an effort", "Starting an effort", "top-up" and "restat". Matches came from nodes 104, 152, 156, 162, 170, 190, 317, 357, 83, 87 and 355 itself. None of them is made wrong. This node establishes a list and changes no word, path or heading. Node 357 (claimed) lists lines in `glossary.md` and `SKILL.md`. This node edits neither, but the implementation node proposed above shares its files. I wrote no replacement clauses, and my work changes no open node's question.

MISSING FROM MAP: none

RETROSPECTIVE
1. What I had to hunt for: which files each reader is "already told to read". The rule turns on this, and neither the map nor the node states it. I derived it from `SKILL.md`'s opening, `adoption.md`'s opening, and a grep of the worker contracts for `graph-conventions`. I also had to find where the four `expedition/` files are. The spawn gives them as bare names, and they are in `.claude/skills/expedition/`, not at the repository root.
2. What arrived that this node did not need: most of `map.md`. Only the ground-rules block, rule 6, and the never-delete note bore on the work. Of the `decisions.md` lines, only node 312's and node 253's were used.
3. What would have made this easier: a spawn line saying "the manager reads SKILL.md, graph-conventions.md and glossary.md always, and the rest when invoked or when adopting". The spawn could also give full paths for the four `expedition/` files. It should also say whether `glossary.md` is inside the question: the node's list leaves it out and the spawn's source list includes it.
4. What was stale, wrong or contradictory: the node's question lists seven files and leaves out `glossary.md`, but the spawn lists it as authoritative. The never-delete paragraph that `expedition-cleanup` restates has no heading, so rule 6's "point at a heading" cannot be met there without a new heading or rule 4's quoted phrase. Node 312's answer says every shared rule now lives in one file with one-sentence pointers, and the landed text has the exceptions listed under INVALIDATIONS.
`````

## Flags

`355.1` `ASSUMPTION` **· settled** — Counted `glossary.md` as manager-read and listed its overlaps with the contracts apart. *(The worker's full text is under its handover's `FLAGS`.)*

`355.2` `ASSUMPTION` **· settled** — Classed pointers that also summarise their target as borderline under rule 6. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-09-28:* flags 355.1 and 355.2 settle at the node closing report that closes this node.
