# Derive how many times each standing item has been reported

Type: implementation
Status: resolved

Blocked by: 210, 219

## Answer

derivations.md gains entry (j). It lists each standing-item name, written as a kebab-case code span opening a list item, with how many retrospectives carry it and in which node files.

*The manager's note:* landed as commit `6149fbca3` after one correction round on a `FAIL`; run 2's `PASS` was taken under the standing yes on 2026-10-04. It surfaced [node 387](387-state-the-written-form-of-a-standing-items-name.md), now unblocked. Flags 220.2, 220.3 and 220.4 settle at the node closing report; 220.1 was withdrawn by its worker.

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

#### The human's answer to raise 1, 2026-10-04

`verbatim`: *"ok"*

The manager had closed the payload with "Please answer: "ok for recommended", or name an alternative." The reply takes the worker's `RECOMMENDED`: "Yes. Keep the draft as written, and file a new node that adds one sentence to map-manager-only.md's retrospective bullet fixing that form, so the spawn asks for names in it."

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      220, Derive how many times each standing item was reported

ANSWER:        `.scratch/graph-workflow/derivations.md` gains one entry, `## (j) Item names carried by the retrospectives`. It is appended after entry (i), and no earlier entry is touched. Its question: for each standing item named in a retrospective, how many retrospectives carry that name, and in which node files? Its means is one block that uses only sh, awk and sort, run from `.scratch/graph-workflow/` over `nodes/[0-9]*-*.md`. Each output line is a count, a name and the node files carrying it, sorted by count and then by name. The file holds no count, no name and no list.

               **The forms it reads.** These were derived from the tree on 2026-10-04, and the entry's text names each one.
               - **Heading forms:** `## Retrospective`, `### Retrospective`, `## RETROSPECTIVE`, `## Retrospective — attempt 1`, `## Retrospective — what the two correction rounds added`, `## Annotation: the retrospective`, `## Annotation: the retrospective, and the manager's note on filing this node` and `### The retrospective`. They are matched by rule rather than by list: text equal to `Retrospective`, `RETROSPECTIVE` or `The retrospective`, or beginning with `Retrospective — ` or `Annotation: the retrospective`, at any level.
               - **Handover part inside a fenced block:** a `RETROSPECTIVE` line, written bare, with a colon, or with a parenthesised suffix. The part ends where its fenced block ends.
               - **Handover part outside any fence:** it ends at the next heading. The amended clause 2 does not list this form. It is about half of all handover parts.
               - **Emphasised openings outside a fence:** `**RETROSPECTIVE**`, `*RETROSPECTIVE, addition to …:*`, `RETROSPECTIVE ADDITION:`, `**Retrospective, added:**` and `**Retrospective, changed:**`. These also end at the next heading.
               - **Blockquoted part:** `> RETROSPECTIVE`, which ends where the blockquote ends.

               **Boundaries.**
               - A section ends at the next heading of the same or higher level.
               - A retrospective heading or part inside an open section belongs to that section.
               - Fences are read by run length and character, the way CommonMark reads them. This matters because pasted handovers are fenced with 4 or 5 backticks and hold 3-backtick fences inside. A plain open/close toggle broke on node 302 and others.
               - A heading inside a fenced block is skipped. The entry states both of clause 3's rules and obeys them.

               **What it excludes.** It does not read node titles, `## The manager's disposal of the retrospective's record items`, or node 70's `## Annotation: this node's retrospective claim is refined, and its own number has moved`. That annotation is node 183's note about node 70's retrospective. It is not a retrospective, so the "sixth heading form" in this node's hold is not a form. Any other heading that mentions "retrospective" and is neither read nor excluded goes to stderr as `heading not covered`. Today that prints nothing.

               **What an item name is.** This was the human's decision at raise 1 ("ok" on RECOMMENDED, 2026-10-04). A name is a numbered or bulleted list item inside a retrospective whose text opens with a code span of two or more lowercase-alphanumeric words joined by hyphens. That is the form nodes 212 and 178 used. Names in bold or in prose (nodes 188, 215, 224 and 244) are not recognised, and the entry says so. The form has no false positives inside retrospectives. It does occur outside them (nodes 289, 350, 355 and 359), so the boundaries above carry the result.

               **What it counts.** The count is node files, not sections. A file carrying a name in several retrospectives (an attempt and a correction round) counts once. A name carried once is reported, per clause 5.

               **Verification.** An independent Python implementation, written from the entry's prose, gives byte-identical name output. It also gives identical sets of retrospective lines, apart from heading and blank lines, which cannot carry a name. This held both over the worktree's `nodes/` and over the main tree's current `nodes/`.

               **Scale.** Dated 2026-10-04, not authoritative, for scale only: 195 node files hold a retrospective. 76 hold one under a heading. 62 hold a fenced handover part, 62 an unfenced one and 1 a blockquoted one. 4 files (290, 296, 299 and 345) hold both a heading form and a part outside it. The entry returns 8 distinct names, all from nodes 178 and 212.

INDEX LINE:    derivations.md gains entry (j). It lists each standing-item name, written as a kebab-case code span opening a list item, across every retrospective form, with node-file counts and files.

FLAGS:         ASSUMPTION: **The count is node files, not retrospective sections.** Clause 1 asks how many retrospectives carry a name, and clause 4 asks for a count and a list of node files. One node file often holds several retrospectives: a first attempt and a final one, or correction-round additions. Counting sections would let one node's worker raise an item's rank by repeating it across rounds. That is not independent repetition, and what the count feeds is the manager's ranking. It would also make the count depend on fine boundary choices, such as where an unfenced part ends. So the entry counts each node file once, and the count equals the length of the file list it prints. I did not ask, since it changes only how the entry's own output is read. Index: Entry (j) in derivations.md counts the node files carrying a standing-item name, not the retrospective sections, so one node's repeated rounds count once.

               ASSUMPTION: **The entry reads retrospective forms the amended clause 2 does not list.** These are: unfenced `RETROSPECTIVE` parts, which end at the next heading; emphasised openings such as `**Retrospective, added:**`; `RETROSPECTIVE ADDITION:`; and a blockquoted `> RETROSPECTIVE`, which ends where the blockquote ends. Clause 2 lists headings and fenced parts, but it opens with "every form" and says the worker derives the current set itself. The unfenced form alone is about half of all handover parts. I chose where each part ends myself. Ending at the next heading can take in trailing manager text, which cannot carry a name in the recognised form. Index: Entry (j) reads unfenced, emphasised and blockquoted RETROSPECTIVE parts too, ending them at the next heading or the end of the blockquote, which clause 2 did not list.

               ASSUMPTION: **Three kinds of heading that mention a retrospective are excluded.** They are: node titles; the manager's `## The manager's disposal of the retrospective's record items`, which is manager text and not a retrospective; and node 70's `## Annotation: this node's retrospective claim is refined, and its own number has moved`, which quotes node 183 on node 70's retrospective. That last heading is the "sixth form" in node 220's hold, taken from node 178. Excluding it contradicts that claim. Any other such heading is printed on stderr, so a new form surfaces. Index: Entry (j) treats node 70's refining annotation and the manager's disposal headings as not retrospectives, contrary to node 178's count of six heading forms.

NEW NODES:     Name: State in the retrospective bullet the form a standing item's name is written in
               Kind: implementation
               Question: map-manager-only.md's retrospective bullet has the worker name each standing item it reports, but fixes no written form. Entry (j) of derivations.md finds names in exactly one form, as the human settled at node 220's raise 1 on 2026-10-04. A name written in any other form is invisible to it, and so to the next worker looking for a name to reuse.
               Blockers: 220 (the entry the bullet points at must have landed)
               Acceptance condition:
               > The work is an edit to one file, `.scratch/graph-workflow/map-manager-only.md`. Nothing else changes.
               >
               > Done means every one of the following is true of the finished tree.
               >
               > 1. In `.scratch/graph-workflow/map-manager-only.md`, the bullet beginning **"Every worker returns a retrospective as the last handover part, on this effort only"** states that the worker writes each standing item's name as a numbered or bulleted list item of its retrospective, whose text opens with the name in a code span. The name is two or more words of lowercase letters and digits joined by hyphens. The name is followed in that list item by the count of earlier retrospectives carrying it and their node ids.
               > 2. That bullet states that the existing names, with their counts and node files, are obtained by running the entry headed `## (j) Item names carried by the retrospectives` in `.scratch/graph-workflow/derivations.md`, and that a name written in any other form is not found by that entry.
               > 3. No statement already in that bullet is changed or removed. In particular, the human's quoted instruction beginning *"Could you, for this effort only, ask subagents"* and the four questions numbered (1) to (4) are unchanged character for character.
               > 4. No file under `.claude/` is modified, and no file in `.scratch/graph-workflow/` other than `map-manager-only.md` is modified.
               > 5. The tree meets the bar.
               >
               > The scope came from no search: the named bullet is the work, not an instance of a defect.
               Joined to no open node: node 284 also edits `map-manager-only.md`, but only its *How the worktree is made* Create bullet, which is a different concern.

INVALIDATIONS: - **Node 212 (extension and narrowing).** Its answer and retrospective say a retrospective sits under five heading forms and that names are found by searching "the retrospective sections". There are now eight heading texts. Retrospectives are also written as handover `RETROSPECTIVE` parts, fenced, unfenced, emphasised or blockquoted, which no heading search reaches. A name is now narrowed to one written form, a kebab-case code span opening a list item, by the human's "ok" on raise 1 (2026-10-04).
               - **Node 219 (extension).** The map-manager-only.md bullet it wrote says the worker finds existing names "by searching the retrospective sections … whatever heading each section was filed under". Entry (j) is now that search, and it also reads handover parts. The bullet stating the name form is the new node above.
               - **Node 178 (contradiction, one point).** Its "35 filings under six heading forms", repeated in node 220's hold, counts node 70's refining annotation as a retrospective heading. It is not one, as given under FLAGS.
               - **Node 210 (extension).** `derivations.md` now holds ten entries, not nine.

CONDITIONS:    I listed the open and claimed nodes in the main tree on 2026-10-04: 17 of them, found by reading the `Status:` header as derivation (e) does. I searched their `## Question` and `## Acceptance condition` sections for `derivations.md`, `retrospective`, `heading form`, `standing item`, `item name` and `map-manager-only`.
               - Node 284: matches only on its own Create bullet in `map-manager-only.md`. My work does not change it.
               - Node 149: its condition names `map-manager-only.md` only in a list of files. No change.
               - Node 185: its question cites "the map's rule that a standing retrospective item reported a second time becomes a node". Node 219 superseded that rule, not my work. Its question is otherwise unchanged by this node.
               - Node 209: mentions a retrospective as its origin only. No change.
               I wrote no replacement clauses and changed no open node's question.

MISSING FROM MAP: Neither map.md nor map-manager-only.md records the forms in which a retrospective actually sits in a node file. The bullet says `## Retrospective` and no other heading. Since node 219 landed (2026-10-02), however, the manager has filed retrospectives as `RETROSPECTIVE` parts of pasted, fenced handovers (nodes 379, 380 and 383, among others). I got the real set by searching `nodes/`. map.md also did not say that no written form for a standing item's name existed. I found that by reading nodes 178, 188, 212, 215, 224 and 244, and the human settled it at raise 1.

GATE PAYLOAD:  Checker findings: none yet; no checker has run.
               Paths touched: `.scratch/graph-workflow/derivations.md` only (additions only; `git diff --check` clean; `git status --short` shows only that file), in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/220-retro-derivation.
               The bar: the repo states no build, test or format commands. Its root holds `.claude`, `CONTEXT.md`, `CONTEXT-MAP.md`, `.gitignore` and `.scratch`. There is no manifest, task runner or CI, and `.gitignore` only ignores worktree paths. This matches `map-implementation-rules.md`'s record, so the bar is its non-command half.
               Run: the entry's block, extracted from the file and run under `sh` from `.scratch/graph-workflow/`, prints 8 lines and nothing on stderr. Its output is byte-identical to an independent Python measurement, over this tree and over the main tree.
               Method skills: none invoked. `/coding-principles`, `/naming` and `/writing-for-agents` were held as standards, not run.
               Proposed commit message:
                 Derive how many retrospectives carry each standing-item name

                 derivations.md gains entry (j). It reads every form a retrospective takes
                 in a node file (the heading forms, and a handover's RETROSPECTIVE part,
                 fenced, unfenced, emphasised or blockquoted) with CommonMark fence
                 lengths, and lists each item name written as a kebab-case code span
                 opening a list item, with the count and the node files carrying it.

                 Node: graph-workflow/220

RETROSPECTIVE:
1. What I had to hunt for: the real set of retrospective forms. No file records it, and the amended clause 2's list was incomplete. Searching the headings of `nodes/` found them, and so did searching lines that begin `RETROSPECTIVE` both inside and outside fences. That second search turned up the unfenced half and the `**Retrospective, added:**` paragraphs. I also had to establish how fences nest: a naive toggle mis-scoped node 302 because of 3-backtick fences inside 5-backtick ones. Whether any item names exist, and in what form, took a grep over the whole corpus and a read of nodes 178, 188, 212, 215, 224 and 244.
   - `record-is-not-mechanically-scannable` — 2 earlier retrospectives carry it (nodes 178, 212). The forms drifted again: the unfenced and emphasised parts. And the map bullet says `## Retrospective` only, while filings since 2026-10-02 are fenced handover parts.
2. What arrived that this node did not need: most of `map.md` (the worktree, landing, grouping, never-delete and heterogeneous-model notes) beyond the numbers rule, the derivations line and the writing rules. In `map-implementation-rules.md`, the worktree, trigger-file and record-as-work paragraphs. Nothing in the spawn bore on nothing, and its list of decisions lines was exactly right.
   - `map-read-whole-for-a-few-items` — 1 earlier retrospective carries it (node 178).
   - `rules-file-read-whole-for-one-section` — 1 earlier retrospective carries it (node 178).
3. What would have made this easier: a recorded statement of where and how the manager files a retrospective, matching its practice. The spawn's naming duty, which arrived only on the resume. A fixed name form from the start, so that clause 4 would not have needed a raise.
   - `spawn-omits-a-duty-the-map-places` — new name; no earlier retrospective carries it. Node 212 reported the same in prose, when its spawn omitted the retrospective duty. Mine omitted the naming duty, and the manager confirmed this for its spawns since 2026-10-02.
4. What was stale, wrong or contradictory: the manager's "117 inside a fenced block" and "no file holding both": about half the parts are unfenced, and 4 files hold both. The hold's "sixth form" from node 178 is not a retrospective heading. The map bullet's "under the heading `## Retrospective` and under no other heading" contradicts the filings since it landed.
   - `stale-number-in-the-record` — 2 earlier retrospectives carry it (nodes 178, 212).
   Counts are from entry (j), run 2026-10-04 over the main tree's `nodes/`; they are not authoritative and are for scale only.
`````

*The manager's note:* the node the worker surfaced is filed as [node 387](387-state-the-written-form-of-a-standing-items-name.md).

## Flags

`220.1` `ASSUMPTION` **· withdrawn by its worker in correction round 1** — Entry (j) in derivations.md counts the node files carrying a standing-item name, not the retrospective sections, so one node's repeated rounds count once. *(The worker's full text is under its handover's `FLAGS`.)*

`220.2` `ASSUMPTION` **· settled** — Entry (j) reads unfenced, emphasised and blockquoted RETROSPECTIVE parts too, ending them at the next heading or the end of the blockquote, which clause 2 did not list. *(The worker's full text is under its handover's `FLAGS`.)*

`220.3` `ASSUMPTION` **· settled** — Entry (j) treats node 70's refining annotation and the manager's disposal headings as not retrospectives, contrary to node 178's count of six heading forms. *(The worker's full text is under its handover's `FLAGS`.)*

## Review

### Checker run 1 — `FAIL` on the acceptance condition

*The checker's own text, pasted, 2026-10-04. A fresh checker; the condition reached it as clause 2 amended, the human's raise-1 direction on the name form as their words, and the node's three flags with ids.*

> FAIL: acceptance condition
>
> Work checked: the uncommitted change to .scratch/graph-workflow/derivations.md in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/220-retro-derivation. The diff is pure addition: entry "## (j) Item names carried by the retrospectives". I read the changed path as the work, under the rules file's paragraph on record files. I read nodes/ only as the measurement target the spawn names. I left the record unread.
>
> ### Finding 1 (clause 1): the entry asks one question and counts another
>
> - **Instances.** The entry's question line reads "For each standing item named in a retrospective, how many retrospectives carry that name, and in which node files?", matching clause 1. Its means counts node files instead. The prose says so: "The count is the number of those node files, so a node file that carries a name in more than one retrospective, such as a first attempt and a correction round, counts once." The block does the same through `if ((name, file) in carried) return` and `count[name]++`, so each name counts once per file.
>   - I demonstrated this on a synthetic two-file `nodes/` tree under $TMPDIR. A name was carried by three retrospectives: two in file 1 (`## Retrospective` and `## Retrospective — attempt 1`) and one in file 2 (a fenced `RETROSPECTIVE:` part). The block printed `2 alpha-one: 1-a.md 2-b.md`, and the number of retrospectives is 3.
>   - On the current tree the two quantities agree. Each node carrying a name (178 and 212) has exactly one retrospective holding names. So the output is right today, and the means still does not answer the stated question.
> - **Form.** The entry's means returns, as a name's count, any quantity other than the number of retrospectives carrying that name.
> - **Extent.** Two sites in the added entry: the paragraph beginning "Each output line is a count", and `read_name()` in the block. List them with `git -C <worktree> diff -U0 -- .scratch/graph-workflow/derivations.md | grep -nE 'number of those node files|in carried|count\[name\]\+\+'`.
>
> ### Finding 2 (clause 2): the means opens the blockquoted form but can read no item in it
>
> - **Instances.** The entry derives a blockquoted form, `> RETROSPECTIVE`, which ends at the first line not beginning with `>`. That form exists in the tree at nodes/131-a-just-do-it-mode-that-skips-grilling.md, under the line `> RETROSPECTIVE (effort-scoped; I wrote no graph file)`. Every line inside such a part begins with `>`.
>   - `read_name()` matches only `/^[ \t]*([0-9]+\.|[-*+])[ \t]+`.../`, so a list item inside a blockquote can never be recognised. The block opens the part and can read nothing from it.
>   - This contradicts the entry's own statements "The block reads every form of both" and "a numbered or bulleted list item inside a retrospective".
>   - Synthetic test: `> RETROSPECTIVE` followed by ``> - `lam-da` quoted list item`` printed nothing for `lam-da`.
>   - No output changes on the current tree: node 131's blockquoted part holds no qualifying item. The same pattern also misses a blockquoted list item inside a heading section.
> - **Form.** A retrospective form the entry names, in which a list item opening with a hyphen-joined lowercase code span cannot match `read_name()`'s pattern.
> - **Extent.** The smallest set containing every instance is the forms the entry names whose lines carry a prefix the pattern does not admit. Of the forms in the entry, that is only the blockquote form: in the sentence "Where the line opens with a blockquote marker", and in the `part == "quoted"` handling against the regex in `read_name()`. I computed this by comparing each named form's line prefix with the pattern.
>
> ### Clause by clause
>
> - **Clause 1: not met** (finding 1). It is met in the other respects:
>   - the entry has its own name, (j);
>   - it sits alongside entries (a) to (i);
>   - its question is on one line;
>   - it gives a means that runs against `nodes/`.
> - **Clause 2: not met** (finding 2), otherwise established.
>   - **Headings.** An awk pass found every heading in nodes/*.md mentioning "retrospective", case-insensitive, skipping fenced blocks. None occur inside fences. Distinct forms:
>     - `## Retrospective`, `### Retrospective`, `## RETROSPECTIVE`;
>     - `## Retrospective — attempt 1`, `## Retrospective — what the two correction rounds added`;
>     - `## Annotation: the retrospective`, `## Annotation: the retrospective, and the manager's note on filing this node`;
>     - `### The retrospective`;
>     - and, not retrospectives: four level-1 titles, 17 `## The manager's disposal of the retrospective's record items`, and node 70's `## Annotation: this node's retrospective claim is refined…`.
>   - The entry names all eight retrospective forms. I instrumented the block to print where it opens a section. It opens every heading except the titles, the disposals, node 70's annotation, and node 86's `### The retrospective`, which sits inside an already-open level-2 section. Its stderr check printed nothing.
>   - **Part starts.** `^[ \t>*_]*(RETROSPECTIVE|Retrospective)` outside or inside fences finds 167 lines: 91 fenced, 76 unfenced. The block opens a fenced part at all 91 and a plain or quoted part at 74. The remaining 2 (nodes 200 and 204) sit inside open `## Annotation: the retrospective` sections. So every start is covered.
>   - The fenced form, "the part ends where its fenced block ends", is stated and coded.
> - **Clause 3: met.** Both statements are present: "A retrospective section's body ends at the next heading of the same or higher level." and "A heading inside a fenced code block is skipped".
>   - Synthetic test: a `###` heading kept the section open, the next `##` closed it, and a `##` inside a 4-backtick fence neither opened nor closed it.
>   - A note that is not a finding: node 86's level-2 section `## Annotation: the retrospective, and the manager's note…` therefore runs on through `### The manager's note`. That note is read as retrospective text. It holds no qualifying item today.
> - **Clause 4: met.**
>   - **The search.** `grep -nE '^[[:space:]>]*([0-9]+\.|[-*+])[[:space:]]+`[a-z0-9]+(-[a-z0-9]+)+`' nodes/*.md` lists every candidate. A broader variant allowing `)`, emphasis and uppercase added only bold-wrapped items outside any retrospective.
>   - **Placing each hit.** I placed each hit by headings, fences and RETROSPECTIVE lines:
>     - inside a retrospective: nodes 178 (under `## Retrospective`, 6 names) and 212 (under `## Retrospective`, 4 names);
>     - outside one: the hits in 289 (under `### Search of open conditions`), 350, 355 and 359 (before the RETROSPECTIVE line in their fences, or under `## Review`).
>   - **Direct measure.** 2 stale-number-in-the-record (178, 212); 2 record-is-not-mechanically-scannable (178, 212); and 1 each for one-rule-stated-at-several-sites, map-read-whole-for-a-few-items, rules-file-read-whole-for-one-section, nothing-pointed-me-at-it (all 178), manager-owes-a-promotion-and-has-not-made-it and worker-forbidden-a-file-reaches-it-by-search (both 212).
>   - **The block's output** under gawk 5.4.1 is identical. A count of retrospectives would also be identical today.
>   - **Nothing written into the file.** None of the 8 names occurs in derivations.md (grep -c each, all 0). The added digits are only regex ranges, `attempt 1`, `{0,3}` and sort keys, so no count, table or measurement is written.
> - **Clause 5: met.** The text states "A name carried by only one retrospective is reported too, so that a name minted once is visible…". The block prints every name with count ≥ 1, and the output contains six names with count 1.
> - **Clause 6: met.**
>   - `git status` shows derivations.md as the only change, with nothing untracked.
>   - `git diff` has a single hunk, `@@ -266,3 +266,110 @@`, of added lines only, so no existing entry changed.
>   - Nothing under `.claude/` changed.
> - **Clause 7, the bar: holds.** Details in the next section.
>
> ### The bar
>
> - **Commands.** The repo states none, and the commands half of the bar is empty. The repo root holds only .claude/, CONTEXT.md, CONTEXT-MAP.md, .gitignore and .scratch/. There is no CLAUDE.md or AGENTS.md, no manifest, no CI.
> - **Whitespace.** `git diff --check` printed nothing and exited 0.
> - **Other awks.** The block gives the same output under `gawk --posix`, nawk 20260426 and busybox awk 1.37.0. Under mawk 1.3.4-20240819 it aborts with `REcompile() - panic: values still on machine stack for ^ {0,3}(```|~~~)`. I record this as information, not a finding: the file only promises that blocks use `awk`, and ground rule 1 binds shipped files, which this is not.
>
> ### Standards
>
> - **Source.** I read only the standards in .scratch/graph-workflow/map-implementation-rules.md, the main tree's copy. It differs from the worktree's copy only in the paragraph reserving decisions.md and flags.md, which bears on nothing here.
> - **What bore on the work:**
>   - **The six writing rules and /writing-for-agents** (on the prose). No breach found: no line-number citations, one idea per sentence, plainly stated.
>   - **The glossary's _Avoid_ lines.** "item" is refused only as a word for a node. "report" and "tree" come from the condition's own wording. No breach.
>   - **/coding-principles and /naming,** applied by hand to the awk block. Function names are clear, and uncovered headings are reported on stderr rather than passing silently. No breach.
>   - **The ground rules.** No breach.
> - **What did not bear:** graph-conventions.md (no mention of derivations). No reviewing skill is named for this repo, so I ran none.
>
> QUESTIONS:
> - None of the three flags is false.
>   - **220.1** is true of the work. The block counts each node file once; synthetic test above.
>   - **220.2** is true. The entry's text and code read unfenced, emphasised and blockquoted parts, ending them at the next heading or at a line not beginning with `>`.
>   - **220.3** is true of the work. The instrumented run opens neither node 70's annotation nor any disposal heading. Its clause about node 178's count makes no claim the work can make true or false.
>
> Temporary files were under $TMPDIR/chk220 and have been removed.

*The manager's note:* a `FAIL` goes back to the worker for a correction round, under "Raise the gate once the checker passes". The human sees it at the gate as one of the checker's runs.

## Handover, correction round 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      220, Derive how many times each standing item was reported. Correction round 1, for checker run 1 (FAIL, acceptance condition)

ANSWER:        As first returned, with these changes to entry (j) in `.scratch/graph-workflow/derivations.md`. Everything else in the entry is as before.
               - **The count is now retrospectives, not node files.** Each retrospective section, and each handover part outside a section, is one retrospective. Each output line is a count, a name and the node files whose retrospectives carry it. The count is the number of retrospectives carrying the name. A node file holding several, such as a first attempt and a correction round, adds one for each and is listed once. To make that count well defined, a line that starts a part while another part is open now ends that part and starts a new one, for example a second `RETROSPECTIVE (correction round 1):` inside the same fenced handover. Inside a heading section, a part still belongs to the section.
               - **A name may sit in a blockquoted list item, behind one or more `>` markers.** Without this, the blockquoted form the entry names, `> RETROSPECTIVE`, could never yield a name.
               - **The fence-opening pattern no longer uses an interval expression.** It was `^ {0,3}`; it is now `^ ? ? ?`. The block now runs under mawk 1.3.4 as well as gawk, with identical output.

INDEX LINE:    derivations.md gains entry (j). It lists each standing-item name, written as a kebab-case code span opening a list item, with how many retrospectives carry it and in which node files.

FLAGS:         Flag 220.1 (counting node files rather than retrospectives) is withdrawn. The work now follows clause 1's literal question, so there is no judgement left to flag. Flags 220.2 and 220.3 stand as first returned.

               ASSUMPTION: **A part-opening line met while another part is open starts a new retrospective.** Counting retrospectives needs each one to have an identity. A pasted handover sometimes holds a second `RETROSPECTIVE (…)` line for a later round in the same fenced block, or a bold `**Retrospective, added:**` paragraph after an unfenced part. Each of those is now its own retrospective, ending the previous part. Inside a retrospective heading section, such a line still belongs to the section, which counts once. I decided this without asking because it only fixes the unit that clause 1 names. Index: Entry (j) treats each RETROSPECTIVE opening line outside a heading section as a new retrospective, so a correction round's part counts separately from the first.

NEW NODES:     As first returned (State in the retrospective bullet the form a standing item's name is written in), with one change. In its clause 1, after "joined by hyphens", add: "The list item may sit inside a blockquote." This keeps it matched to entry (j).

INVALIDATIONS: As first returned.

CONDITIONS:    As first returned. This round changes no word, path or phrase that open conditions quote.

MISSING FROM MAP: As first returned. Also: `derivations.md`'s preamble says each block uses only sh, awk, find, wc, sort, grep and git. It does not say which awk the blocks must run under. I went on by making the block run under mawk as well as gawk.

GATE PAYLOAD:  - **Finding 1 (clause 1: the count was node files).** Fixed, not disputed. The paragraph beginning "Each output line is a count" now defines one retrospective and counts retrospectives. In `read_name()`, `carried` is now keyed by name and a retrospective counter. That counter increases at each section start and each part start. A separate `listed` keeps each file once in the list. On a synthetic tree of two files, the block prints `4 alpha-one: 1-a.md 2-b.md`. File 1 holds `## Retrospective` and `## Retrospective — attempt 1`, each carrying the name. File 2 holds a fenced `RETROSPECTIVE:` part and a `RETROSPECTIVE (correction round 1):` part in the same fenced block, each carrying it. That is four retrospectives in two files. A list item inside an indented fence before the part is not read.
               - **Finding 2 (clause 2: blockquoted form unreadable).** Fixed. `read_name()`'s pattern now admits leading `>` markers: `^([ \t]*>)*[ \t]*([0-9]+\.|[-*+])[ \t]+` followed by the code span. The entry's text says a list item may sit inside a blockquote. On the synthetic tree, `> RETROSPECTIVE (quoted)` followed by ``> - `lam-da` quoted`` prints `1 lam-da: 2-b.md`, and a list item after the blockquote ends is not read.
               - **The checker's mawk note.** Fixed as above. Under mawk 1.3.4 the block's output is identical to gawk's, on the synthetic tree and on this worktree's `nodes/`.
               - **Verification.** I rewrote the independent Python measurement for the new unit, the restart rule and blockquoted names. Its output is byte-identical to the block's over this worktree's `nodes/`, over the main tree's current `nodes/`, and on the synthetic tree. Run on the main tree, the block prints nothing on stderr. On today's trees the counts are unchanged in this worktree. The main tree now also carries node 220's and node 284's filed retrospectives.
               - **Touches the acceptance condition:** yes, clauses 1, 2 and 4, through the paragraphs and the block of entry (j). No existing entry is changed.
               - **Paths touched:** `.scratch/graph-workflow/derivations.md` only, additions only. `git diff --check` is clean, and `git status --short` shows only that file. Worktree: /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/220-retro-derivation.
               - **The bar:** unchanged from the first handover. The repo has no build, test or format commands, so the bar is the standards and the condition.
               - **Proposed commit message:**
                 Derive how many retrospectives carry each standing-item name

                 derivations.md gains entry (j). It reads every form a retrospective takes
                 in a node file (the heading forms, and a handover's RETROSPECTIVE part,
                 fenced, unfenced, emphasised or blockquoted) with CommonMark fence
                 lengths, and lists each item name written as a kebab-case code span
                 opening a list item, with how many retrospectives carry it and in which
                 node files.

                 Node: graph-workflow/220

RETROSPECTIVE (correction round 1):
1. What I had to hunt for: nothing new about the record. The work was re-reading clause 1's literal question against the unit I had chosen, and checking whether mawk was reachable to confirm the checker's note. It was, through `nix shell nixpkgs#mawk`.
   - `cross-check-shares-the-blind-spot` — new name; no earlier retrospective carries it. My independent Python check was written from my own reading. It reproduced both of my misses, the unit and the blockquote, so the agreement between the two implementations proved nothing about them. A synthetic tree with one instance of each named form would have caught finding 2 before the checker did.
2. What arrived that this node did not need: nothing. The two findings came with instances, extent commands and synthetic cases, which is all a fix needs.
3. What would have made this easier: a line in `derivations.md`'s preamble naming the awk dialects every block must run under. The existing entries avoid interval expressions only by habit.
   - `rules-file-read-whole-for-one-section` — 2 earlier retrospectives carry it (nodes 178, 220). Not this round: no file was reread.
4. What was stale, wrong or contradictory: my own flag 220.1. I settled a question clause 1 had already answered in plain words, and recorded it as a judgement.
   - `stale-number-in-the-record` — 3 earlier retrospectives carry it (nodes 178, 212, 220). Not this round: no number was handed to me.
   Counts are from entry (j) as fixed, run 2026-10-04 over the main tree's `nodes/`; they are not authoritative and are for scale only.
`````

## Flags, correction round 1

`220.4` `ASSUMPTION` **· settled** — Entry (j) treats each RETROSPECTIVE opening line outside a heading section as a new retrospective, so a correction round's part counts separately from the first. *(The worker's full text is under correction round 1's `FLAGS`.)*

## Review, continued

### Checker run 2 — `PASS`

*The checker's own text, pasted, 2026-10-04. The run 1 checker, resumed for this node's re-check.*

> PASS
>
> Re-check after the correction round. The work is still the one changed path, .scratch/graph-workflow/derivations.md, in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/220-retro-derivation.
>
> **What changed since run 1.** `git status --short` shows only that file. `git diff` is a single hunk of added lines (`@@ -268,0 +269,111 @@`) with zero removed lines. I read the whole of entry (j) again. The changes I found against run 1:
> - the count is now per retrospective, through a `retrospective` counter and a `carried[name, retrospective]` dedupe, with node files listed once each through `listed[name, file]`;
> - new prose: "Each retrospective section, and each handover part outside a section, is one retrospective" and "A line that starts a part while another part is open ends that part and starts a new one";
> - the fenced-part start no longer requires `part == ""`;
> - `read_name()` now admits `([ \t]*>)*` before the list marker, with prose: "The list item may sit inside a blockquote, behind one or more `>` markers";
> - the fence-open regex is now `^ ? ? ?(```|~~~)` instead of `^ {0,3}`. The diff to the fence regex was not mentioned to me, so I checked it too: it accepts the same 0 to 3 spaces.
>
> I read the changed path as the work, under the rules file's paragraph on record files. The node files under nodes/ are unchanged in the worktree (`git status --short nodes` is empty), and I read them only as the measurement target.
>
> **Clause by clause:**
>
> - **Clause 1: met.** Entry (j) has its own name, sits alongside (a) to (i), and states its question on one line. The means now answers that question: the count is the number of retrospectives carrying the name. Synthetic test under $TMPDIR, the same tree as run 1 plus cases:
>   - a name in three retrospectives across two files printed `3 alpha-one: 1-a.md 2-b.md`;
>   - a name repeated within one retrospective counted once;
>   - two plain correction-round parts in one file printed `2 kappa-ten: 2-b.md`.
>
>   Run 1's finding 1 is resolved.
> - **Clause 2: met.**
>   - The prose names the same eight heading forms, the fenced part ending where its fenced block ends, and the unfenced, emphasised and blockquoted forms.
>   - I instrumented the corrected block to print each place it opens a retrospective: 77 sections, 91 fenced parts and 74 plain or quoted parts. These are the same totals as run 1, and they match my independent enumeration. The 77 sections are the heading counts 61+5+5+1+1+3+1. The other 167 starting lines split into 91 fenced and 76 unfenced, of which 2 sit inside open sections.
>   - The stderr check printed nothing.
>   - Blockquoted items are now read: ``> - `lam-da` `` and the nested ``> > 2. `nu-nu` `` were both reported in the synthetic test. Run 1's finding 2 is resolved.
> - **Clause 3: met.** Both statements are still present: "A retrospective section's body ends at the next heading of the same or higher level." and "A heading inside a fenced code block is skipped".
>   - Synthetic test: a `###` kept the section open, the next `##` closed it (`gamma-three` not reported), a `#` closed it (`eps-five` not reported), and a `##` inside a 4-backtick fence neither opened nor closed it (`delta-four` reported).
>   - Run 1's note still applies: node 86's level-2 annotation section runs on through `### The manager's note`, which holds no qualifying item today.
> - **Clause 4: met.**
>   - The candidate search `grep -cE '^[[:space:]>]*([0-9]+[.)]|[-*+])[[:space:]]+`[a-z0-9]+(-[a-z0-9]+)+`' nodes/*.md` returns the same files and counts as run 1: 178:6, 212:4, 289:7, 350:1, 355:3, 359:7.
>   - I placed each hit as in run 1. Only the hits in 178 and 212 sit inside a retrospective, each node having a single `## Retrospective` holding all of its names. The blockquoted hits in 359 sit under `## Review`, not in a retrospective, and the block does not count them.
>   - Direct measurement: 2 stale-number-in-the-record (178, 212); 2 record-is-not-mechanically-scannable (178, 212); 1 each for one-rule-stated-at-several-sites, map-read-whole-for-a-few-items, rules-file-read-whole-for-one-section and nothing-pointed-me-at-it (all 178); 1 each for manager-owes-a-promotion-and-has-not-made-it and worker-forbidden-a-file-reaches-it-by-search (both 212).
>   - The block's output under gawk 5.4.1 is identical.
>   - Nothing is written into the file: `grep -c` gives 0 for each of the 8 names in derivations.md. The added digits are only regex ranges, `attempt 1` and sort keys, so no count, table or measurement is written.
> - **Clause 5: met.** The sentence "A name carried by only one retrospective is reported too, so that a name minted once is visible…" is still present, and six names print with count 1.
> - **Clause 6: met.** Only derivations.md changed, with additions only. No existing entry and nothing under `.claude/` or elsewhere in `.scratch/graph-workflow/` changed.
> - **Clause 7: met.** The bar holds, as the next section shows.
>
> **The bar.** It has no commands to run here: the repo root holds no CLAUDE.md or AGENTS.md, no manifest, no CI and no formatter. `git diff --check` printed nothing and exited 0. The block gives identical output under gawk `--posix`, mawk 1.3.4-20240819, nawk 20260426 and busybox awk 1.37.0. Run 1's mawk panic is gone.
>
> **Standards.** I read only the standards in .scratch/graph-workflow/map-implementation-rules.md.
> - They bore on the work as follows:
>   - the six writing rules and /writing-for-agents, held against the new prose: no line numbers, one idea per sentence, stated positively;
>   - the glossary's _Avoid_ lines: no breach;
>   - /coding-principles and /naming, held against the block by hand: clear names, and uncovered headings are reported on stderr, so nothing fails silently;
>   - the ground rules.
>
>   None is breached.
> - graph-conventions.md did not bear on the work. No reviewing skill is named for this repo, so I ran none.
>
> QUESTIONS:
> - None of the three flags is false.
>   - **220.2** is true of the work. The text and code read unfenced, emphasised and blockquoted parts, ending them at the next heading or at a line not beginning with `>`. In the synthetic test, `mu-mu` after the quote was not read.
>   - **220.3** is true of the work. The instrumented run opens neither node 70's annotation nor any disposal heading. Its clause about node 178's count makes no claim the work can make true or false.
>   - **220.4** is true of the work. Each RETROSPECTIVE opening line outside a section increments `retrospective`, and two plain correction-round parts in one file counted 2.
>
> Temporary files were under $TMPDIR/chk220b and have been removed.

### The gate, 2026-10-04 — standing yes

`standing yes`. The scope, word for word: *"Approve all gates automatically"*. The checker's `PASS` (run 2) is taken as the human's approval. The run covered every part and handed back no question, and found flags 220.2 to 220.4 true. A gate taken under a standing yes settles no flag, so they settle at the node closing report.
