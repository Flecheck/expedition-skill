# Cut the glossary entries that restate a shipped section's rule to their meaning

Type: implementation
Status: claimed
Blocked by: none

## Question

Can each glossary entry in the nine pairs node 355 found be cut to its meaning and its `_Avoid_` line? Can the rule stay at the shipped section that states it, and the glossary's opening gain a sentence saying this is where rules go?

*Reported by [node 360](360-which-copy-stays-where-the-glossary-and-a-contract-agree.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Acceptance condition

*Authored by node 360's worker and filed by the manager.*

> The work is `.claude/skills/expedition/glossary.md` and `.claude/skills/expedition/SKILL.md`, and no other file may be edited. Scope: the scope came from no search command. The places are a bounding set taken from a reading in full of eight files: `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/graph-conventions.md`, `.claude/skills/expedition/adoption.md`, `.claude/skills/expedition/wayfinder-divergences.md`, `.claude/skills/expedition/glossary.md`, `.claude/skills/expedition-stop/SKILL.md`, `.claude/skills/expedition-standing-yes/SKILL.md` and `.claude/skills/expedition-cleanup/SKILL.md`. If you find another glossary entry that states a rule a shipped section also states, report it and do not edit it.
>
> In the clauses below, an entry is a bold term line in `.claude/skills/expedition/glossary.md` and the text under it. "Its text becomes X" means that the text between the bold term line and the entry's `_Avoid_` line (or the end of the entry, where it has none) is exactly X. The bold term line and the `_Avoid_` line stay word for word.
>
> 1. The glossary's opening paragraph gains this sentence, word for word, directly after "A term is added only once a node has settled it.": "An entry says what the term means; a rule about the term is stated in the contract section that acts on it, and not here."
> 2. `**Attempt**:` Its text becomes: "One worker instance on one node. A node lasts longer than any of its attempts. A resumed worker continues the same attempt, and a replacement is a new attempt."
> 3. `**Handover**:` Its text becomes: "What a worker returns when it has finished."
> 4. `**Scribe**:` Its text becomes: "How the manager writes. It pastes what an agent handed back under the right heading, as it was handed back."
> 5. `**Closed**:` Its text becomes: "The human's declaration that an effort is over."
> 6. `**Effort closing report**:` Its text becomes: "What the manager hands the human once the frontier empties."
> 7. `**Starting an effort**:` The sentence "The manager performs it, and it happens before the graph exists." is removed. The rest of its text is unchanged.
> 8. `**Adoption**:` Its text becomes: "Starting an effort from a directory of work that already exists. It is a way of starting an effort, not a kind of node."
> 9. `**Node closing report**:` Its text becomes: "The message the manager sends the human the moment a node closes. An unqualified "closing report" means this report. Prose written before this term was settled uses "closing report" for the effort closing report."
> 10. `**Flag**:` Its text becomes: "A note recording a judgement that an agent made on its own and that the human may want to revisit. The agent is usually a worker, and it is the manager where a judgement of the manager's own went into the graph. Raising a flag blocks nothing."
> 11. `**Stop**:` Its text becomes: "Ending a running worker's work before it hands back."
> 12. `**Final stop**:` Its text becomes: "A stop the human says is final."
> 13. `**Destination**:` Its last sentence, beginning "Where the effort is not expected to reach it", is removed. Its first three sentences are unchanged.
> 14. In `.claude/skills/expedition/SKILL.md`, under `## Words used exactly`, the bullet beginning "A dead attempt is resumed where you can resume it" becomes exactly: "- A replacement is a new attempt, recorded after the one it replaces." The bullet beginning "A handover has seven parts every time" is unchanged.
> 15. No rule is lost. Each sentence removed under clauses 2 to 14 states nothing that the place named for it here does not also state:
>     - Attempt, and the clause 14 bullet: `## When an agent dies or is stopped` in `.claude/skills/expedition/SKILL.md`.
>     - Handover: the handover bullet under `## Words used exactly` and `### You write as a scribe`, both in that file.
>     - Scribe: `### You write as a scribe`.
>     - Closed: `## Closing an effort` and `## Starting an effort`.
>     - Effort closing report: `## Closing an effort`.
>     - Starting an effort: `## Starting an effort`.
>     - Node closing report: `### Picking the next node`.
>     - Flag: `## Flags`.
>     - Stop and Final stop: `## Stopping a running worker`.
>     - Adoption: `## Your steps, in order` in `.claude/skills/expedition/adoption.md`.
>     - Destination: the `## Destination` bullet under `## The seven files` in `.claude/skills/expedition/graph-conventions.md`.
>     Where a sentence those clauses name states something its place does not, that sentence stays in the entry, and the worker reports it rather than moving it.
> 16. No glossary entry is added, removed, renamed or reordered, and no `_Avoid_` line changes. No heading in any file under `.claude/skills/` is added, removed or renamed. `.claude/skills/expedition/SKILL.md` changes only as clause 14 says.

*The worker's note for the manager, pasted:* "node 363 edits `glossary.md`'s **Correction round** entry, and node 368 edits pointer paragraphs in `SKILL.md`. Neither touches the entries or the bullet named here, but they share files, so check before you fill a second code slot. The condition uses a quoted opening phrase rather than a line number throughout."

## Handover, attempt 1

*The worker's own text, pasted, 2026-10-02.*

````
HANDOVER:      Cut the glossary entries that restate a shipped section's rule to their meaning

ANSWER:        The glossary's opening paragraph now says, directly after "A term is added only once a node has settled it.", "An entry says what the term means; a rule about the term is stated in the contract section that acts on it, and not here." Clauses 2 to 7 and 9 to 13 of the condition are applied word for word. Attempt, Handover, Scribe, Closed, Effort closing report, Node closing report, Flag, Stop and Final stop are cut to the exact text the condition gives. Starting an effort loses "The manager performs it, and it happens before the graph exists." and keeps the rest of its text, rewrapped only. Destination loses its last sentence. In `.claude/skills/expedition/SKILL.md`, under `## Words used exactly`, the dead-attempt bullet now reads "- A replacement is a new attempt, recorded after the one it replaces." The handover bullet is unchanged.

**Adoption is not cut. Clause 15 kept it.** The sentence clause 8 would remove ("It carries steps that starting from a conversation does not: ... and minting the bulk import as `precondition` nodes.") states the node kind `precondition`. The place clause 15 names for it, `## Your steps, in order` in `adoption.md`, does not state that kind. Step 7 says only "Mint the import nodes" and points at `## The bulk import`. The kind is stated elsewhere in `adoption.md`: in its opening paragraph ("Their kind is `precondition`") and in `## The bulk import`. That place also never says that starting from a conversation lacks these steps. So, as clause 15 directs, the Adoption entry is left whole and reported here. A NEW NODES block below proposes the cut.

How each other removed sentence was matched against its named place, under clause 15:
- Attempt, and the clause 14 bullet: `## When an agent dies or is stopped` says "Resume its attempt wherever you can resume it, rather than replacing it. Replacement is the fallback ... an attempt whose agent was stopped from the human's side is never replaced without the human's answer."
- Handover: the seven parts and the eighth are in the handover bullet. "The manager files it unaltered" is in `### You write as a scribe` ("Paste each part ... as the agent wrote it").
- Scribe: never re-author/shorten/re-order/re-render, your own words beside it as a marked note, and no gloss are all stated in `### You write as a scribe`. "join them into one continuous text" was read as the same thing as the section's "placing runs one after another" (see the flag).
- Closed: `## Closing an effort` says "Only the human closes an effort. Report that the conditions hold, and nothing more. A frontier that never empties is a legitimate steady state." That last sentence, unqualified, covers the narrower glossary sentence.
- Effort closing report: `## Closing an effort` holds the "covers only what the human has not already seen" sentence and the five carried items.
- Starting an effort: `## Starting an effort` has "You perform it, and it happens before the graph exists."
- Node closing report: `### Picking the next node` names the closed node and the node started, says the report awaits no answer and takes no place in the queue, and says it carries every flag. "because those flags settle there" is a reason, and `## Flags` states it as a rule.
- Flag: `## Flags` gives the gate, or else the node closing report, as the moment flags settle, and gives the one case in which flags reach the effort closing report.
- Stop and Final stop: `## Stopping a running worker` holds every removed sentence. It says the manager performs every stop with `TaskStop` at the human's word, that a stopped worker can be resumed within the session, and how a stop from the human's side differs, including revival by typing. It says a message is not a stop, being received late and possibly declined. Its step 5 says the attempt is recorded as not to be resumed and that no manager resumes it. Its statement that both stops can be revived covers "no stop from either side removes a worker for good".
- Destination: the `## Destination` bullet in `graph-conventions.md` says "Where the effort is not expected to, this line is where a manager reads that a non-empty frontier is that effort's steady state rather than a defect."

Clause 16 was checked by diffing the old and new files: the bold term lines, the `_Avoid_` lines and the headings of `glossary.md` are unchanged, and the headings of `SKILL.md` are unchanged.

Other glossary entries that state a rule a shipped section also states, reported and not edited, under the condition's scope sentence. These were spotted while reading and only spot-checked, not verified exhaustively:
- Checker: "The manager starts it, and the worker never does, because whoever spawns it chooses what it sees" is also in `## The checker` in `SKILL.md`.
- Gate: "does not render the diff into the conversation" is also in `### The payload`.
- Manager: "never answers one on the human's behalf" is also in `## What is never yours`.
- Acceptance condition: the raise and `CONDITION-WRONG` sentences are also in the implementation contract's `## The acceptance condition` and `## What you hand back`. Not checked against SKILL.md.
- Reject: the worktree removal, branch deletion and keep-by-commit sentences may also be stated in `graph-conventions.md`. Not checked.
- Code slot: occupancy is counted from live worktrees. Not checked against a section.

INDEX LINE:    Nine glossary entries and Starting an effort are cut to their meaning. The glossary's opening says rules live in contract sections. Adoption is kept whole, because its named place omits `precondition`.

FLAGS:         ASSUMPTION: For the Scribe entry, I read "join them into one continuous text" as stated by `### You write as a scribe`, whose list of what assembling is includes "placing runs one after another". Placing pieces one after another is joining them into one continuous text. So the sentence was removed under clause 4 rather than kept under clause 15. If the human reads it as a broader permission than the section's, the fix is to restore that one sentence to the Scribe entry.
Index: Node 370 read the Scribe entry's "join them into one continuous text" as the same thing as "placing runs one after another" in `### You write as a scribe`, and cut it.
ASSUMPTION: For the Adoption entry, I held clause 15 to the place it names, `## Your steps, in order` in `adoption.md`. That place does not state the `precondition` kind of the import nodes, or that starting from a conversation lacks these steps. So the whole sentence stays, clause 8 is not applied, and the residue is proposed as a new node. The kind is stated elsewhere in the same file, so no rule would have been lost by cutting it. Holding to the place named was the reading the condition's own fallback sentence asks for.
Index: Node 370 kept the glossary's whole Adoption sentence, because `## Your steps, in order` in `adoption.md` does not state that import nodes are `precondition` nodes.

NEW NODES:     Name: Cut the glossary's Adoption entry to its meaning
Kind: implementation
Question: Can the glossary's **Adoption** entry lose its sentence listing adoption's steps, now that `adoption.md` states those steps and the kind of the import nodes?
Blockers: none
Acceptance condition:
> The work is `.claude/skills/expedition/glossary.md`, and no other file may be edited. Scope: no search produced it. The one place named is the work itself, not an instance of a defect.
> 1. In `.claude/skills/expedition/glossary.md`, the text between the line `**Adoption**:` and its `_Avoid_` line is exactly: "Starting an effort from a directory of work that already exists. It is a way of starting an effort, not a kind of node." The bold term line and the `_Avoid_` line stay word for word.
> 2. No rule is lost. Every part of the removed sentence ("It carries steps that starting from a conversation does not: taking the effort's name from the directory that already exists, resolving any reserved graph name the directory already uses for something else, deriving the map from the record the effort already wrote rather than from a conversation, declaring the label vocabulary from the foreign label families, and minting the bulk import as `precondition` nodes.") is stated in `.claude/skills/expedition/adoption.md`, read as a whole: its opening paragraphs, `## Your steps, in order` and `## The bulk import`. Where a part is stated nowhere in that file, the sentence stays and the worker reports it.
> 3. No other glossary entry, `_Avoid_` line or heading in any file under `.claude/skills/` changes.

INVALIDATIONS: Node 360 is narrowed in application. Its answer is that the section keeps the rule and the entry keeps the meaning, and the glossary's opening now says so. That answer is applied to every pair except Adoption, which keeps its rule sentence until the new node above lands. Nothing it says is contradicted.

CONDITIONS:    I searched the open nodes' `## Question` and `## Acceptance condition` sections for: glossary; the headwords Attempt, Handover, Scribe, Closed, Effort closing report, Node closing report, Starting an effort, Adoption, Flag, Stop, Final stop and Destination; "dead attempt"; "seven parts"; and the new opening sentence. Node 317 (open, unclaimed, no condition yet) has a changed question. Its manager's note says its work "keeps `CONTEXT.md`'s `**Flag**:` entry in line with whatever it decides". The glossary's Flag entry no longer states when a flag reaches the effort closing report. That part of node 317's work is now unnecessary, and only `## Flags` and `## Closing an effort` in `SKILL.md` remain to reconcile. No other open node's condition or question matched in a way this work makes wrong. I wrote no replacement clauses.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings: none yet, because no check has run.
Paths touched: `.claude/skills/expedition/glossary.md` and `.claude/skills/expedition/SKILL.md`. Worktree: /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/370-glossary
Bar: the repo has no manifest, build, tests, formatter or CI, which agrees with `map-implementation-rules.md`. So the bar is its non-command half. The edited lines keep the file's wrap width, with no line over 105 characters.
Proposed commit message:
Cut glossary entries that restate a contract section's rule

The glossary's opening now says that an entry states meaning, and that rules live in
the contract section that acts on the term. Attempt, Handover, Scribe, Closed,
Effort closing report, Node closing report, Flag, Stop, Final stop, Destination and
Starting an effort drop the sentences their sections already state. The manager
contract's dead-attempt bullet keeps only the replacement sentence. Adoption is kept
whole, because the steps section it points at does not name the import nodes' kind.

Node: graph-workflow/370

RETROSPECTIVE:
1. What I had to hunt for: where `adoption.md` states the `precondition` kind. It is in the file's opening and in `## The bulk import`, not in the section clause 15 names. Also the exact wording of each named section, which meant reading the whole of the 818-line `SKILL.md`.
2. What arrived that this node did not need: most of `map.md` (worktree history, the v2 model note, the never-delete account) and most of `map-implementation-rules.md` (the trigger-file rule, the record-as-work rule). The `.claude/rules/expedition-triggers.md` auto-load was not needed either.
3. What would have made this easier: if the condition named every place a removed sentence is stated, for example "adoption.md as a whole" for Adoption, the clause 15 judgement would have been mechanical. A section-scoped read list would also have helped, since only about 8 sections of `SKILL.md` mattered.
4. What was stale, wrong or contradictory: clause 15's named place for Adoption is too narrow to hold the rule clause 8 removes, so clauses 8 and 15 cannot both be fully met. Clause 15's own fallback settles the conflict. Node 317's note still refers to `CONTEXT.md`'s Flag entry, which now lives in `glossary.md`.
````

## Review

### Checker run 1 — `FAIL` (acceptance condition)

*The checker's own text, pasted, 2026-10-02. A fresh checker; the condition reached it as a verbatim copy in `$TMPDIR/c370.md`.*

> FAIL: acceptance condition
>
> Scope of reading: I read the changed paths `.claude/skills/expedition/glossary.md` and `.claude/skills/expedition/SKILL.md` in worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/370-glossary` as the work, under the map-implementation-rules rule for record paths. Neither path is a record path. I also read the places that clause 15 names: SKILL.md sections, `adoption.md` `## Your steps, in order`, and the `graph-conventions.md` `## Destination` bullet. In `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md` I read only the standards and opened no other file in that directory.
>
> ### Finding 1: a removed sentence states something its named place does not (clause 15, Node closing report)
> - Instances: the old `**Node closing report**:` text had the sentence "It carries in full every flag that node holds, because those flags settle there." The work removed it to meet clause 9. Clause 15 names `### Picking the next node` as this entry's place. That section states that the report carries every one of the node's flags ("A node closing report for a node holding flags carries every one of those flags, in the fuller form ..."). It never states that those flags settle at the node closing report. Search: unwrap `### Picking the next node` and grep it for `settle`. It returns nothing:
>   `awk '/^### Picking the next node/{f=1;next} f&&/^##/{f=0} f' .claude/skills/expedition/SKILL.md | tr '\n' ' ' | grep -o -i '[^.]*settle[^.]*\.'`
>   The fact is stated only under `## Flags`, which is the Flag entry's place and not this one's. Clause 15 says such a sentence "stays in the entry, and the worker reports it rather than moving it". The worker did exactly that for Adoption. The two other removed sentences of this entry are stated in the named place: "names the node that just closed, and the node and kind you started" and "awaits no answer and takes no place in the queue above".
> - Form: a sentence removed under clauses 2 to 14 that contains a statement with no counterpart, in any wording, in the section clause 15 names for that entry.
> - Extent: the smallest set that provably contains every instance is the sentences that `git -C <worktree> diff -- .claude/skills/expedition/glossary.md .claude/skills/expedition/SKILL.md` shows as removed. I compared each of them against its named place, entry by entry. This was the only one with no counterpart. Checked and held: Attempt plus the clause 14 bullet against `## When an agent dies or is stopped`. Handover against the handover bullet and `### You write as a scribe`. Scribe against `### You write as a scribe`. Closed against `## Closing an effort` and `## Starting an effort`. Effort closing report against `## Closing an effort`. Starting an effort against `## Starting an effort`. Flag against `## Flags`. Stop and Final stop against `## Stopping a running worker`. Destination against the graph-conventions `## Destination` bullet. One judgement call: the Final stop sentence "The record makes a stop final, because no stop from either side removes a worker for good." I counted it as stated in substance, from step 5 together with the resumability and revivability of both kinds of stop.
>
> ### What held, part by part
> - Scope and no other file edited: `git status --porcelain --untracked-files=all` lists only the two allowed paths, both modified.
> - Clause 1: the unwrapped opening paragraph contains "A term is added only once a node has settled it. An entry says what the term means; a rule about the term is stated in the contract section that acts on it, and not here. The reasoning" (substring check in Python).
> - Clauses 2 to 6 and 9 to 12: each entry's unwrapped text, between the bold line and the `_Avoid_` line, equals the dictated text exactly (Python parse of the glossary, string equality). This covers Attempt, Handover, Scribe, Closed, Effort closing report, Node closing report, Flag, Stop and Final stop.
> - Clause 7: the old Starting an effort text with only that sentence deleted equals the new text.
> - Clause 13: the new Destination text equals the old text cut at " Where the effort is not expected".
> - Clause 8 (Adoption): the text is unchanged and does not equal the dictated text. This is legitimate under clause 15's carve-out. `adoption.md` `## Your steps, in order` never states that the bulk import is minted "as `precondition` nodes" (grep finds `precondition` only at lines 10 and 68 of `adoption.md`, outside that section). It also never states the contrast with starting from a conversation. So the sentence stays.
> - Clause 14: the SKILL.md diff is the one bullet replaced by "- A replacement is a new attempt, recorded after the one it replaces." The "A handover has seven parts every time" bullet is untouched.
> - Clause 16: all 58 entries are in the same order with the same names, and every `_Avoid_` line is identical to HEAD (Python comparison against `git show HEAD:...`). No `#` heading lines were added or removed in the diff. SKILL.md changes only as clause 14 says.
>
> ### The bar
> The repo has no build, no tests, no formatter and no CI (recorded in map-implementation-rules.md; the worktree root has only `CONTEXT.md` and `CONTEXT-MAP.md`, with no CLAUDE.md or AGENTS.md giving commands). `git diff --check` printed nothing (rc=0). The longest added line is 102 characters, within the files' existing wrap width.
>
> Standards read: `/coding-principles`, `/naming`, the glossary's `_Avoid_` lines, the ground rules, the six standing rules for writing, `graph-conventions.md` and `/writing-for-agents`. No reviewing skill is named for this repo, so I ran none.
> - Bore on the work: the `_Avoid_` lines (no refused word in the new text, checked by hand), writing rules 5 and 6 (no heading renamed, no new restatement), and ground rules 1 and 4 (nothing repo-specific added).
> - Did not bear on this deletion-only prose change: coding-principles and naming.
> - The `.claude/rules/expedition-triggers.md` sync rule does not apply, because the edited bullet is outside `## The order you act in` and `## What is in front of the human, and when`.
> - No standard was moved by the work.
>
> NOT COVERED:
> - "Where a sentence those clauses name states something its place does not, that sentence stays in the entry, and the worker reports it rather than moving it." Whether the worker reported the retained Adoption sentence, and the Node closing report sentence once it is restored, is in its handover. That is outside the paths I hold.
>
> QUESTIONS:
> - Is the "because those flags settle there" sentence still correct to keep in the Node closing report entry? Flags on an implementation node that has a gate settle at the gate, not at the node closing report (`## Flags`). Clause 15's wording, which is the condition's and not the worker's to depart from, makes the sentence stay in the entry when it fails the check. Keeping it would keep a statement the glossary's new opening sentence says belongs in a contract section.

*The manager's note:* a `FAIL` is outside the standing yes. Finding 1 and the checker's question turn on whether clause 15's named place for the Node closing report entry is to be widened to `## Flags`, which only the human can amend; it goes to the human.

## Flags

`370.1` `ASSUMPTION` — *The worker's own text.* For the Scribe entry, I read "join them into one continuous text" as stated by `### You write as a scribe`, whose list of what assembling is includes "placing runs one after another". Placing pieces one after another is joining them into one continuous text. So the sentence was removed under clause 4 rather than kept under clause 15. If the human reads it as a broader permission than the section's, the fix is to restore that one sentence to the Scribe entry.

`370.2` `ASSUMPTION` — *The worker's own text.* For the Adoption entry, I held clause 15 to the place it names, `## Your steps, in order` in `adoption.md`. That place does not state the `precondition` kind of the import nodes, or that starting from a conversation lacks these steps. So the whole sentence stays, clause 8 is not applied, and the residue is proposed as a new node. The kind is stated elsewhere in the same file, so no rule would have been lost by cutting it. Holding to the place named was the reading the condition's own fallback sentence asks for.
