# The manager contract's open question 5 and the search duty three sections above it do not know about each other

Type: implementation
Status: superseded
Superseded by: 337

Blocked by: ~~95~~ **none — node 95 resolved and landed at `b095bb6`.**

## Question

*Surfaced by [node 95](95-carry-the-widening-rule-into-the-shipped-files.md)'s worker, and pasted as it wrote it.*

> `.claude/skills/expedition/SKILL.md`'s `## What nothing here settles` item 5 asks *"Does anything tell a worker to
> go and look at the record when it reports what its work invalidates?"* and answers *"Nothing does."* After node 95
> the same file tells a party to go and look, before handing back, at one bounded class — the open nodes'
> `## Acceptance condition` sections. [Node 263](263-nothing-tells-the-falsifying-party-to-go-and-look.md) settled
> that the general question stays separate from the narrow duty and gave its ground; nothing in the file connects
> the two, and **item 5's *"Nothing does"* now reads as false at its own file's scale.** Node 252's and node 263's
> workers each reported, independently, that nothing on the graph connects the records of this one hole; **this is
> the same finding inside a shipped file.**

**Blockers, in the worker's words:** *"node 95."*

## Acceptance condition

*Written by node 95's worker. Pasted as it wrote it, and not the manager's.*

> 1. `.claude/skills/expedition/SKILL.md`'s `## What nothing here settles` item 5 still stands as an unsettled
>    question, still states that the general duty over the effort's record does not exist, and additionally names
>    the one bounded class where a duty to look does exist — the open nodes' acceptance conditions — pointing at the
>    section of that same file which states it by its heading rather than by a line number.
> 2. The items in `## What nothing here settles` keep their numbers and their order, none is removed, and no item
>    other than item 5 changes meaning.
> 3. That file's `## Acceptance conditions` section is not changed by this work.
> 4. No file other than `.claude/skills/expedition/SKILL.md` is changed, and no file under `.scratch/` is changed.
> 5. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Three agents have now found one hole from three directions and none of them could see the others.** Node 252's
worker reported that nothing on the graph connects the records of it; node 263's worker found [node
37](37-invalidations-is-not-a-check.md) by grepping on a hunch and reported that nothing links it to anything; and
this worker found the same disconnection **inside a shipped file**, where an open question and its own partial
answer sit three sections apart and neither names the other.

**Node 37 is still open and is still the general version.** Node 263 settled that it stays separate and gave its
ground — different corpus, differently indexed, different consequence. **This node does not touch that**; it makes
the shipped file stop asserting that nothing exists when part of it now does.

**The `Blocked by: 95` edge is real**: clause 1 requires item 5 to point at a statement node 95 has not landed yet.

## Amendment, 2026-09-25 (from node 298)

*Written by [node 298](298-rewrite-the-manager-contract-part-3.md)'s worker and filed by the manager, after that node's work landed as commit `9d8044c`. Every word of the replacement is fixed by that commit: it quotes `expedition/SKILL.md`'s after-text. The minting author's condition above is left as it was. Node 298's worker's search is on node 298 under `RE-POINTING SEARCH`.*

- **Clause 1.** Replace "`## What nothing here settles` item 5" with "`## What nothing here settles` item 4, the item reading *"Does anything tell a worker to look at the record when it reports what its work invalidates?"*". The rest of the clause is unchanged, and so is clause 2.

## Flags

`280.1` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from node 298's re-pointing list, on the ground that every word of the replacement is fixed by commit `9d8044c`.

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 337](337-carry-the-record-file-test-the-home-of-a-standing.md), the merge [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
