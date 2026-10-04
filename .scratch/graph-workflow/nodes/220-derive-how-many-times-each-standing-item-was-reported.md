# Derive how many times each standing item has been reported

Type: implementation
Status: open

Blocked by: 210, 219

## Question

*Surfaced by [The rule that mints a node on a repeated retrospective item has been defeated by its own
test](212-the-mint-on-second-report-rule-is-defeated.md)'s worker, and pasted as it wrote it.*

> Once the retrospective names the standing item it reports, repetition becomes derivable, and the
>            derivation belongs beside the nine that node 210 writes. It is a separate node rather than a tenth
>            clause on node 210 because node 210 is unblocked today and this depends on the map edit landing;
>            node 210's condition is left untouched. The requirement that the derivation match every heading form
>            is in the condition because scanning for one form miscounted twice while this node was being worked.

**Blockers, in the worker's words:** 210, and Node A above

## Acceptance condition

*Written by node 212's worker. Pasted as it wrote it, and not the manager's.*

> The work is one added entry in `.scratch/graph-workflow/derivations.md`. Nothing else changes.
>
> Done means every one of the following is true of the finished tree.
>
> 1. `.scratch/graph-workflow/derivations.md` carries a new entry with its own name, alongside the entries already
>    there. It states in one line the question it answers — for each standing item named in a retrospective, how
>    many retrospectives carry that name and in which node files — and then gives the means of answering it
>    against the tree at `.scratch/graph-workflow/nodes/`.
>
> 2. *(Superseded 2026-10-04 by the human's amendment under `## Amendment, 2026-10-04`; the clause that binds is there.)* ~~The entry's own text names every heading under which a retrospective section is written in that directory,
>    and the means it gives matches all of them. As of 2026-09-09 those headings are `## Retrospective`,
>    `## Retrospective — attempt 1`, `## Annotation: the retrospective`, `## Annotation: the retrospective, and
>    the manager's note on filing this node`, and `### The retrospective` — **stated as of that date, not
>    authoritative, and not to be relied on.** The worker derives the current set itself and the entry covers what
>    it finds.~~
>
> 3. The entry states in its own text that a retrospective section's body ends at the next heading of the same or
>    higher level, and that a heading appearing inside a fenced code block is skipped, and it is written so that
>    it obeys both.
>
> 4. Run against the tree as the entry gives it, the entry returns, for each item name present, a count and a list
>    of node files equal to what direct measurement of that same quantity returns at the same moment. **No count,
>    no item name and no list is written into the file**, and the file gains no table, series or recorded
>    measurement.
>
> 5. The entry states that an item name carried by only one retrospective is reported too, so that a name minted
>    once is visible to the next worker looking for an existing name to reuse.
>
> 6. No entry already in `derivations.md` is changed or removed, no file under `.claude/` is modified, and no other
>    file in `.scratch/graph-workflow/` is modified.
>
> 7. The tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Its author explained why it is not a tenth clause on [node
210](210-write-the-derivations-this-effort-derives-by-hand.md)**, which the manager had offered to put to the human
as an amendment: node 210 is unblocked today, this depends on node 219's map edit landing, and *"a condition written
by node 183's worker is not mine to extend."* **Node 210 is left untouched and unblocked.** That is flag `212.5`,
whose author noted the amendment is one line if the human would rather have it.

**Its clause 2 exists because its own author was caught by what the clause forbids.** Scanning for one heading form
miscounted twice; the entry must name every form it matches or *"it reproduces the bug it exists to fix"*.

## Held: this condition's own clause 2 undercounts the thing it exists to protect

*Filed by the manager from [node 178](178-whether-adding-a-standard-is-a-moved-standard.md)'s worker, in its own
words. **Do not claim this node until the human has amended clause 2.***

> **Node 220's acceptance condition is itself wrong on the number it exists to protect.** Node 220 is open and its
> condition names **five** retrospective heading forms "as of 2026-09-09", written expressly so its worker would not
> undercount by searching one form. There are **six**: it misses node 70's `## Annotation: this node's retrospective
> claim is refined, and its own number has moved`, which landed in commit `8bb5d02` *before* node 212 resolved in
> `54d03b3` the same day. So the clause written to prevent an undercount is an undercount, and a worker following it
> will reproduce the bug the node exists to fix. Node 212's answer carries the same five. **This should be amended
> before node 220 is claimed**, and amending a condition is not mine — I report it.

**Why the manager has not amended it.** The condition is node 212's worker's, not the manager's, and rewriting one
is never the manager's — a condition that is wrong goes to the human. **Clause 2 already anticipates this in part**:
it says the five are stated *"as of that date, not authoritative, and not to be relied on"* and that *"the worker
derives the current set itself and the entry covers what it finds"*, so a worker obeying the whole clause would
find six. **What is wrong is the enumeration inside a clause that also tells its reader to distrust it**, which is
the same shape as every stale number this effort has recorded.

**The manager's own count was five too**, taken from node 212's answer and repeated in a spawn, so this is a third
carrier of the stale figure rather than a defect of node 212's worker alone.

## Amendment, 2026-10-04

*The human's amendment. The human's reply, `verbatim`: "ok". It took the replacement the manager offered as "Recommended", which the manager wrote in full in the question, so the words are the manager's and the decision is the human's. The manager's grounds, given in the question: re-derived on 2026-10-04 (not authoritative, for scale only), 79 node files hold a retrospective under a heading and 117 hold it as a handover's `RETROSPECTIVE` part inside a fenced block, with no file holding both. Clause 3 tells the entry to skip headings inside fenced blocks, so the old clause 2 would miss most of them. This lifts the hold above.*

**Clause 2, as it now binds:**

> 2. The entry's own text names every form in which a retrospective is written in that directory: each heading under which a retrospective section sits, and a handover's `RETROSPECTIVE` part pasted inside a fenced block, which ends where its fenced block ends. The worker derives the current set of forms itself, and the means the entry gives matches all of them.
