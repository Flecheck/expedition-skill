# Write the starting-an-effort section and its procedure

Type: implementation
Status: superseded
Superseded by: 337

## Question

*Surfaced by [Starting an effort has no section in the manager's contract](98-starting-an-effort-has-no-section.md)'s
worker, and pasted as it wrote it.*

> Write the two shipped pieces that give starting an effort a home: the `## Starting an effort` section in the
> manager's contract, and the `### Start an effort` procedure in `graph-conventions.md`. This carries node 91's
> answer as well as node 98's — the destination line stating whether an effort is expected to end is part of the same
> prose and lands in the same two files.

**Blockers, in the worker's words:** *"none. Nodes 98 and 91 are the only inputs and both resolve with this
handover."*

## Acceptance condition

*Written by node 98's worker. Pasted as it wrote it, and not the manager's. It carries its scope's enumerator under
[node 94](94-condition-scope-as-a-predicate.md)'s rung 1.*

> Two files change and no others: `.claude/skills/expedition/SKILL.md` and
> `.claude/skills/expedition/graph-conventions.md`.
>
> **How this scope was got.** The enumerator, run while this condition was written:
> `grep -rln -i "starting an effort\|start an effort\|charting\|adoption" .claude/skills CONTEXT.md` returned **no
> files** — nothing in the shipped set states either act, so this work adds text rather than repairing instances of a
> defect spread across the tree. Two structural checks beside it: `grep -n "^## " .claude/skills/expedition/SKILL.md`
> returns fourteen headings, the first `## Words used exactly` and one `## Closing an effort`, none naming an act
> that happens before the graph exists; `grep -n "^### " .claude/skills/expedition/graph-conventions.md` returns
> eight procedure headings — `Claim`, `Resolve`, `Supersede`, `Rule out of scope`, `Park`, `Raise a flag`, `Settle a
> flag`, `Change the map` — none of which creates an effort's files. A place this work touches that is not one of the
> two files above is **reported and not edited**; reporting it is the whole of what this condition asks for it.
>
> 1. `.claude/skills/expedition/SKILL.md` gains a section headed `## Starting an effort`, positioned before its
>    `## Closing an effort` section.
>
> 2. That section states that an effort begins in one of two ways and names both: **charting**, whose input is a
>    conversation with the human, and **adoption**, whose input is a directory of work that already exists. It states
>    that both produce the same thing — the effort's five files and its first nodes — and that they differ only in
>    their input.
>
> 3. That section states that the manager performs the act, and that it happens before the graph exists.
>
> 4. That section states all six of these as what the act establishes, and as the parts both ways share: the effort's
>    name, which is its directory's; the destination, meaning what reaching the end of the effort looks like; whether
>    the effort is expected to reach that destination; the map's standing preferences, the effort's ground rules where
>    it has any, and its standing over sources where it has one; the label vocabulary, declared or declared to be
>    absent; and the effort's first nodes.
>
> 5. That section states that the mechanical detail — which files the act creates and in what order — is in
>    `graph-conventions.md` rather than in this contract.
>
> 6. That section states both halves of what the expectation in item 4 governs: where the effort **is** expected to
>    reach its destination, an empty frontier is the milestone that triggers the whole-graph sweep and the report that
>    precedes a close; where it is **not**, an empty frontier is a surprise rather than a milestone, and that report
>    is an exception path rather than where the effort is heading.
>
> 7. Adoption's own steps are not written into either file. Specifically these seven stay out: taking the effort's
>    name from a directory that already exists rather than choosing one; resolving a reserved graph name the directory
>    is already using for something else; deriving the map from the foreign record rather than from a conversation;
>    declaring the label vocabulary from foreign label families; appending an expedition section to a target
>    repository's tracker doc; building the table that repoints citations inside imported material; and minting a bulk
>    import as `precondition` nodes.
>
> 8. `.claude/skills/expedition/graph-conventions.md` gains, under its `## Procedures` heading and in the same shape
>    as the eight procedures already there, a procedure headed `### Start an effort` that lists every file the act
>    creates, in order: `map.md`, then `map-history.md`, `decisions.md`, `flags.md`, and the `nodes/` directory, and
>    then the effort's first node files by that document's existing `## Adding a node` step.
>
> 9. That procedure's step for `map.md` states that its `## Destination` section says both what reaching the end of
>    the effort looks like and whether the effort is expected to reach it.
>
> 10. `graph-conventions.md`'s existing description of `map.md`'s `## Destination` section, under `## The five
>     files`, currently reads: `## Destination` — what reaching the end of the effort looks like. It is extended to
>     state that the section also says, in one line, whether the effort is expected to reach it — and that where it is
>     not, this is where a manager reads that a non-empty frontier is that effort's steady state rather than a defect.
>
> 11. Neither file states, in any wording, how often efforts end or fail to end.
>
> 12. Nothing outside `.claude/skills/expedition/` changes, and no file under `.scratch/` changes.
>
> 13. The work leaves the tree meeting the bar.

## The manager's note at filing

*Not a change to anything above.*

**This node carries two resolved nodes' writes**, node 98's and node 91's, and node 91's handover says so in terms:
its clauses are items 4, 6, 9 and 10 above. Neither node gets an implementation node of its own.

**It queues against the same file as four others** — nodes 95, 96, 101, 103 and now 109 — and the effort runs one
code slot, so they land one at a time and each rebases onto the last.

## Amendment, 2026-09-24

*Written by [node 299](299-rewrite-graph-conventions-part-1.md)'s worker and filed by the manager, after that node's work landed as commit `0d406b7`. Every word of the replacement is fixed by that commit: it quotes `graph-conventions.md`'s after-text. The minting author's condition above is left as it was. The replacement takes the place of the clause it names. Node 299's worker searched every open node's `## Acceptance condition` for quoted spans of its before-range, matched literally and normalised with each condition joined into one string, and for each phrase its rewrite removed or replaced. The full list of handles is on node 299 under `### Re-pointing duty` and correction rounds 1 to 3.*

- **Clause 4.** It asks for "its standing over sources where it has one", a label `graph-conventions.md` no longer defines. Replace with: "and its declaration of which sources are authoritative, which are evidence only, and which hold statements known to be false, where it has one".

## Flags

`111.1` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 299](299-rewrite-graph-conventions-part-1.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `0d406b7`.

## The manager's note, 2026-09-24

*The manager's own note.* Two workers in the plain-English pass reported stale facts in this node's condition. Node 299's worker: "Node 111's clause 10 cites `## The five files`, but the heading is `## The seven files`." Node 296's worker: "Node 111's recorded count of fourteen `## ` headings was already wrong before this work: there are 15." Both need re-deriving before this node is claimed.

*The manager's note, 2026-09-26:* [node 302](302-rewrite-the-glossary.md)'s worker reported, in its own words: "Node 111's clause 2 names "charting" as a way to start an effort. Node 112's decision, which node 247 carries, refuses that word. This is outside my scope, and I did not verify which of the two is current." Whoever claims this node checks it.

*The manager's note, 2026-09-26:* the human's "ok" to [node 328](328-group-the-open-nodes-against-the-glossary.md)'s C4(a) settles that this node's condition is amended to refuse `charting`, following node 112's decision, rather than to name it. The amendment is applied where this node's demands are filed next: [node 330](330-group-the-open-nodes-against-the-manager-contract.md) merged this node whole into one of its proposed nodes.

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 337](337-carry-the-record-file-test-the-home-of-a-standing.md), the merge [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
