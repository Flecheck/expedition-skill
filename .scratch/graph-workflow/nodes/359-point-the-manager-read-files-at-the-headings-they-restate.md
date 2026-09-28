# Point the manager-read shipped files at the headings they restate

Type: implementation
Status: open
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
