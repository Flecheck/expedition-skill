# Derive how many times each standing item has been reported

Type: implementation
Status: claimed

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

## Interview

#### Raise 1, relayed 2026-10-04

*Pasted as the worker handed it back.*

`````
NODE:          220, Derive how many times each standing item was reported

ABOUT:         The node adds one entry to `.scratch/graph-workflow/derivations.md`. The entry lists every standing-item name carried by the retrospectives in `nodes/`, with a count and the node files for each name. The entry is drafted, run and cross-checked in the worktree. I have stopped before handover because clause 4 assumes an item name can be picked out mechanically, and nothing in the record makes that true.

SO FAR:        What I read: the contract, the node file (including the hold and the 2026-10-04 amendment), map.md, map-implementation-rules.md, map-manager-only.md's retrospective bullet, decisions.md lines for nodes 183, 210, 212 and 219, and derivations.md. I searched every node file for retrospective forms, and I read nodes 178, 188, 212, 215, 244, 302, 350 and 383 where the search led me.

               What I built, uncommitted in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/220-retro-derivation: a new entry "(j) Item names carried by the retrospectives", appended at the end of `.scratch/graph-workflow/derivations.md`. That is the only changed path, and the diff is additions only. The entry is one sh/awk/sort block, and its text names every form it reads:
               - Heading forms: `## Retrospective`, `### Retrospective`, `## RETROSPECTIVE`, `## Retrospective — attempt 1`, `## Retrospective — what the two correction rounds added`, `## Annotation: the retrospective`, `## Annotation: the retrospective, and the manager's note on filing this node`, and `### The retrospective` (which sits inside the previous one; a nested heading counts as one section).
               - Excluded headings: node titles, the manager's `## The manager's disposal of the retrospective's record items`, and node 70's `## Annotation: this node's retrospective claim is refined, and its own number has moved`. That annotation is a later node's note about node 70's retrospective, not a retrospective. So the hold's "sixth form" is not a form.
               - Handover parts inside a fence: a line starting `RETROSPECTIVE`, `RETROSPECTIVE:` or `RETROSPECTIVE (…)`. The part ends where its fence ends.
               - Forms the amended clause 2 does not list, found because the clause says to derive the current set:
                 - the same part pasted with no fence at all, which ends at the next heading;
                 - lines opening with emphasis (`**RETROSPECTIVE**`, `*RETROSPECTIVE, addition to (4):*`);
                 - `RETROSPECTIVE ADDITION:`;
                 - correction-round paragraphs `**Retrospective, added:**` and `**Retrospective, changed:**`;
                 - a blockquoted `> RETROSPECTIVE`, which ends where the blockquote ends.
               - The entry states clause 3's two rules and obeys both.
               - Fences are parsed by run length. Handovers are fenced with 4 or 5 backticks and hold 3-backtick fences inside, so a naive toggle breaks: my first prototype mis-scoped nodes 302 and others.
               - Any heading that mentions "retrospective" but is neither a form nor excluded is printed on stderr. Today it prints nothing.
               - I cross-checked against an independent Python implementation written from the entry's prose. The sets of retrospective lines agree exactly, apart from headings and blank lines, and the name output is byte-identical.

               Measurements, dated 2026-10-04, not authoritative and for scale only: 195 node files hold a retrospective. 76 hold one under a heading. 62 hold a fenced handover part, 62 hold an unfenced one and 1 holds a blockquoted one. 4 files hold both a heading form and a part outside it: 290, 296, 299 and 345. So the manager's "117 inside a fenced block, no file holding both" does not hold: about half of the handover parts are unfenced.

               The finding that stops me is about item names. Only nodes 212 and 178 write names in a form a program can pick out: a list item that opens with a code span of hyphen-joined lowercase words. Between them they hold 10 names, 8 distinct. Nodes 188 and 215 name items as "Standing item: *x*" or "Standing item: **x**". Node 224 names one in an inline code span with spaces. Node 244 names one in bold running prose. No other retrospective names an item. That includes every retrospective filed since node 219's rule landed on 2026-10-02 (nodes 130, 156, 270, 379, 380 and 383 among them), apparently because the spawns stopped asking for names: mine asks the four questions and not for names. The map bullet says the worker "gives that item a short name" but fixes no written form. So "each item name present" (clause 4) and "each standing item named in a retrospective" (clause 1) have no mechanical referent. My draft recognises one form only: a list item opening with a kebab-case code span. In the retrospectives that form has no false positives today. Outside them it does occur (nodes 289, 350, 355 and 359), so the section boundaries matter.

               Settled on my own authority, to be flagged at handover:
               (a) The count is node files, not retrospective sections: a file with an attempt and a correction round counts once, so ranking reflects distinct nodes.
               (b) Unfenced and emphasised forms are read, per clause 2's "derives the current set itself".
               (c) Node 70's annotation and the disposal headings are excluded.

ASK:           May the entry define the item name by one written form, a list item inside a retrospective that opens with a code span of hyphen-joined lowercase words, as nodes 212 and 178 wrote them? Names in any other form would not be returned. Clause 4's "each item name present" would then be measured against that definition.

RECOMMENDED:   Yes. Keep the draft as written, and file a new node that adds one sentence to map-manager-only.md's retrospective bullet fixing that form, so the spawn asks for names in it. The grounds:
               - It is the form the rule's own author (node 212) and its first follower (node 178) used.
               - It has no false positives in retrospectives today.
               - Without a fixed form no derivation can enumerate names, and enumerating them is what clause 5 exists for.
               - The bold and prose names in nodes 188, 215, 224 and 244 are a handful, and the next worker can re-mint them in the form.
               I would also tell the manager that spawns since 2026-10-02 omit the naming duty. Until they carry it, this entry will only ever return the 2026-09 names.

ALTERNATIVES:  - Also recognise "Standing item: *x*" and "Standing item: **x**" (nodes 188 and 215): about 4 more names, at the cost of a second pattern. Nodes 224 and 244 are still missed.
               - Make the entry take a name as input and return the retrospectives whose text contains it, case-insensitively, with no enumeration. Clauses 4 and 5 would need amending.
               - Amend clauses 1 and 4 to say "names written in the form the entry states". Same outcome as RECOMMENDED, but made explicit in the condition.
`````

*The manager's note:* the worker is right on two of the manager's errors. The spawn's "117 inside a fenced block, no file holding both" was wrong: about half the handover parts are unfenced, and four files hold both forms. And the manager's spawns since node 219 landed asked for the four-question retrospective but not for the standing-item names that `map-manager-only.md`'s retrospective bullet requires.
