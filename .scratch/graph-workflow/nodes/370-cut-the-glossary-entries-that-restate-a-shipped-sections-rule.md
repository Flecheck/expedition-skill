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
