# Point the manager-read shipped files at the headings they restate

Type: implementation
Status: claimed
Blocked by: none

## Question

In the stop, standing-yes and cleanup skills, `graph-conventions.md` and `adoption.md`, can the passages node 355 found restating a heading the manager already reads be replaced by pointers to that heading, and can `## New work stops` name the rules it suspends?

*Reported by [node 355](355-where-the-manager-read-shipped-files-restate-one-another.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Acceptance condition

*Authored by node 355's worker and filed by the manager.*

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

*The worker's note for the manager, pasted:* "node 357 (claimed) edits `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition/glossary.md`. This node only cites `SKILL.md` and does not edit it, but check for overlapping edits before you fill a slot."

*The manager's note, 2026-09-28:* node 357 has since landed (`d1e6c52`), so the overlap that note warns of is gone.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-28. The worker's own text, pasted.*

````
HANDOVER:      Point the manager-read shipped files at the headings they restate

ANSWER:

## Answer

Carried out clauses 1 to 10 in the worktree `.scratch/graph-workflow/worktrees/359-pointers` (branch `worktree-359-pointers`, cut from `d1528a7`). Five files changed, 26 lines added and 44 removed. `.claude/skills/expedition/SKILL.md` is cited and was not edited. Every passage the condition quotes still matched the file at `d1528a7` before it was edited.

- `expedition-stop/SKILL.md`, `## New work stops` (clause 3): the section now names what it suspends, for the rest of the session: "the parts of `### Picking the next node` that start new work, and item 3 of `## The order you act in`". The change is then stated in the section's own words and does not restate the suspended rules. It names item 3 because that is the item of `## The order you act in` that spawns an agent.
- `expedition-stop/SKILL.md`, `## What the next manager starts from` (clause 1): the introducing sentence and the three bullets are replaced by one sentence naming `### Three states the status line does not show`. "Write no handoff document" and the live-worktree sentence stay.
- `expedition-stop/SKILL.md`, `## Agents still running when the session ends` (clause 2): the section keeps the sentence saying that the next manager cannot resume a running attempt. Its rest is one sentence naming `## When an agent dies or is stopped`, which holds the replacement rule and the replay of the human's words. "Nothing is lost." went with it.
- `expedition-standing-yes/SKILL.md`, `## Recording the invocation` (clause 4): the sentences on binding once written and on being this effort's alone are removed. The pointer and the in-force sentence stay. The two uses of "it" with different referents in the kept sentence ("governs it as it governs") became "governs the invocation as it governs".
- `expedition-standing-yes/SKILL.md`, `## Taking a covered item` (clause 5): the opening now reads "Your contract's `## What is in front of the human, and when` keeps a covered item out of the pending queue." The same-turn instruction stays. Step 1 keeps the Interview/Review placement and the pointer to `### Recording the human's words`. It drops the marking and quoting rules, and it drops "as the gate's outcome", which that heading also states.
- `expedition-standing-yes/SKILL.md`, `## Flags, and the node closing report` (clause 6): the first paragraph is now one sentence naming `## Flags`. "It carries every flag the node holds …" is removed. That rule is in `### Picking the next node`. The sentences on naming each item with its scope, and on taking an item back, stay.
- `expedition-cleanup/SKILL.md`, `## The rule this skill is an exception to` (clause 7): the paragraph now points at the opening paragraph of `graph-conventions.md` by quoting its first words, "No edit deletes.". No heading was added. The pointer also tells the manager to leave the entry that paragraph describes, so the kept sentence's "the entry's claim" has something to refer to.
- `expedition-cleanup/SKILL.md`, `## Flag cleanup` (clause 8): the mismatch sentence is removed. Check 6 in `graph-conventions.md` states the rule.
- `graph-conventions.md`, `### Change the map` (clause 9): the four-sentence paragraph is now "`## Writing the graph` in `SKILL.md` says who runs this procedure."
- `adoption.md`, opening (clause 10): the three sentences are removed. "This file calls that directory's existing files the foreign record." is unchanged and moved up to follow the first sentence, whose "a directory of work that already exists" is what "that directory" refers to.

Clause 11 checks. Each removed statement was compared against the text at the target it now points to:
- Three states: `SKILL.md` `### Three states the status line does not show`.
- Replacement and replay: `## When an agent dies or is stopped`.
- Binding only once written, and the effort's alone: `### Standing steering, and standing instructions of one effort`.
- Mark, scope quote and what was taken: `graph-conventions.md` `### Recording the human's words`.
- Never enters the queue: the last paragraph of `## What is in front of the human, and when`.
- Flags settling: `## Flags`.
- Flags carried in the report: `### Picking the next node`.
- Never-delete rule, its exception and the entry: the "No edit deletes." paragraph.
- Removed index line is not a mismatch: `## Mechanical checks` check 6.
- Who runs the procedure: `## Writing the graph`.
- Adoption facts: `## Starting an effort`.

The one exception is "not a kind of node", which `## Starting an effort` implies but does not state. The glossary's **Adoption** entry states it word for word. See flag 1.

Clause 12 checks. No heading was renamed or added (`git diff -U0 | grep '^[-+]#'` returned nothing). Every cited heading exists with its exact text, checked with `grep -x` against `SKILL.md` and `graph-conventions.md`. The phrase "No edit deletes." occurs once in `graph-conventions.md`.

Clause 13 check: the only changes are to five of the six files the condition names.

Other checks: lines wrap within each file's existing width of 103 to 105 columns, the frontmatter apart. No bold was added. Each pronoun in the added text was re-read and has one referent.

Passages found outside the list, reported and not edited:
- `expedition-cleanup` `## Flag cleanup`: "The effort closing report is built from its lines whose flag is not yet settled." restates `SKILL.md` `## Closing an effort`. This is node 355's Tier 1 item 9, second half, which the condition left out.
- `expedition-stop` `## New work stops`: it also suspends the first trigger in `.claude/rules/expedition-triggers.md`. Clause 13 keeps that file out of this change, and the text does not name it.

INDEX LINE:    The stop, standing-yes and cleanup skills, `graph-conventions.md` and `adoption.md` now point at ten headings they restated, and `## New work stops` names the two rules it suspends.

FLAGS:
- ASSUMPTION: Clause 10 removes "Adoption is a way of starting an effort, and not a kind of node." `SKILL.md` `## Starting an effort`, which `adoption.md` points at, says adoption is one of the two ways an effort begins. It never says "not a kind of node". The glossary's **Adoption** entry does say it ("It is a way of starting an effort, not a kind of node"), and the manager is told to read the glossary. So I judged clause 11 met by the glossary and did not add the phrase to `SKILL.md`, which clause 13 keeps unchanged. What I did: searched every file under `.claude/skills/` for "kind of node". The glossary is the only place that still states it.
  Index: Judged "not a kind of node", cut from `adoption.md`, as still stated because the glossary's Adoption entry holds it, although `## Starting an effort` only implies it.
- ASSUMPTION: Clauses 5 and 6 require that a statement appear "except by naming" a heading. I read that as allowing a one-sentence pointer that says what the heading governs, for example "Your contract's `## What is in front of the human, and when` keeps a covered item out of the pending queue" and "`## Flags` in your contract says when a node's flags settle where its gate was taken under a standing yes". A bare heading with no subject reads worse. What I did: wrote each pointer as one sentence, with no list of the target's contents. That is the narrow form node 361 is asking about.
  Index: Read "except by naming the heading" as allowing one pointer sentence that says what the heading governs, with no list of its contents.

NEW NODES:     none

INVALIDATIONS:
- Node 166 (the stop skill), an extension. `## New work stops` now names `### Picking the next node` and `## The order you act in` item 3 as the rules it suspends. This carries out the narrowing that nodes 253 and 355 recorded.
- Node 312, a narrowing that is now repaired for one of its two exceptions. `graph-conventions.md` `### Change the map` no longer restates who runs the procedure. The second exception node 355 recorded is untouched: the multi-sentence pointer paragraphs in `SKILL.md`, which node 361 is asking about.
- Node 355: its Tier 1 items 1 to 11 are carried out, except the second half of item 9 and item 12, which the condition excluded. Its word counts for those passages describe text that no longer exists.

CONDITIONS:    I searched the `## Acceptance condition` and `## Question` of all 65 open or claimed nodes for these terms: `expedition-stop`, `expedition-standing-yes`, `expedition-cleanup`, `adoption.md`, `graph-conventions.md`, "Change the map", "New work stops", "What the next manager starts from", "Agents still running", "Recording the invocation", "Taking a covered item", "Flags, and the node closing report", "rule this skill is an exception", "Flag cleanup", "No edit deletes", "foreign record", "standing yes", "cleanup", "stop skill", "who runs", "Three states", "not a kind of node", "mechanical check" and "check 6".
- Apart from node 359 itself, the stop/standing-yes/cleanup/adoption terms matched nothing.
- The `graph-conventions.md` matches in nodes 284, 190, 104, 232, 41, 210, 87, 40, 13, 80, 170, 234, 363 and 361 do not touch the passages changed here.
- Node 361 quotes `SKILL.md` `### The human's words` and `graph-conventions.md` `### Recording the human's words`, both unchanged.
- Node 365's "who runs" is about a check before a claim.
- Node 88's "check 6" concerns check 6's own wording, which is unchanged.
- Node 170's "three states" is about a different subject.
No clause is made wrong, and I wrote no replacement. No open node's question changes. Node 361's question still stands, and the pointers written here are in the one-sentence form its question asks about.

MISSING FROM MAP: none

GATE PAYLOAD:
- Checker findings: none yet, because no checker has run.
- Paths touched, all relative to the worktree root `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/359-pointers`:
  - `.claude/skills/expedition-stop/SKILL.md`
  - `.claude/skills/expedition-standing-yes/SKILL.md`
  - `.claude/skills/expedition-cleanup/SKILL.md`
  - `.claude/skills/expedition/graph-conventions.md`
  - `.claude/skills/expedition/adoption.md`
- Bar: the repo's current state matches the rules file's record. There is no build, no tests, no formatter and no CI. The repo root holds only `.claude`, `CONTEXT-MAP.md`, `CONTEXT.md`, `.gitignore` and `.scratch`. `.gitignore` ignores `.worktrees/`, `.claude/worktrees/` and `.scratch/graph-workflow/worktrees/`, as recorded, and invokes nothing. So the bar is the non-command half, and no commands were run.
- Method-skill parts skipped: none. No method skill was invoked.
- Proposed commit message:

  Point the manager-read skill files at the headings they restate

  The stop, standing-yes and cleanup skills, graph-conventions.md and
  adoption.md restated rules held at headings the manager already reads.
  Each passage now names that heading instead. The stop skill's
  "New work stops" names the two rules of the manager contract it
  suspends.

  Node: graph-workflow/359

RETROSPECTIVE
1. What I had to hunt for: whether "not a kind of node" survives anywhere after clause 10. `## Starting an effort` only implies it, and I found it in the glossary by searching. I also had to work out which item of `## The order you act in` the stop skill suspends. Node 355's handover named item 3, which saved the search.
2. What arrived that this node did not need: most of `map.md`, including the standing preferences and the history pointers. Most of node 355's handover, Tiers 2 and 3 and the flags, was also unneeded. Only Tier 1 mattered.
3. What would have made this easier: a note in the condition, or in the spawn, on how far a pointer may describe its target. Clauses 5 and 6 say "except by naming", and whether a one-sentence gloss is allowed is exactly node 361's open question. Clause 10 could also have named where "not a kind of node" still lives.
4. What was stale, wrong or contradictory: nothing stale. Every quoted passage matched `d1528a7`. Clause 13 says "the six named in clauses 1 to 10", but those clauses edit only five files, because `SKILL.md` is only cited. That is not a contradiction, only loose wording.
````

## Flags

`359.1` `ASSUMPTION` — Clause 10 removes "Adoption is a way of starting an effort, and not a kind of node." `SKILL.md` `## Starting an effort`, which `adoption.md` points at, says adoption is one of the two ways an effort begins. It never says "not a kind of node". The glossary's **Adoption** entry does say it ("It is a way of starting an effort, not a kind of node"), and the manager is told to read the glossary. So I judged clause 11 met by the glossary and did not add the phrase to `SKILL.md`, which clause 13 keeps unchanged. What I did: searched every file under `.claude/skills/` for "kind of node". The glossary is the only place that still states it.

`359.2` `ASSUMPTION` — Clauses 5 and 6 require that a statement appear "except by naming" a heading. I read that as allowing a one-sentence pointer that says what the heading governs, for example "Your contract's `## What is in front of the human, and when` keeps a covered item out of the pending queue" and "`## Flags` in your contract says when a node's flags settle where its gate was taken under a standing yes". A bare heading with no subject reads worse. What I did: wrote each pointer as one sentence, with no list of the target's contents. That is the narrow form node 361 is asking about.
