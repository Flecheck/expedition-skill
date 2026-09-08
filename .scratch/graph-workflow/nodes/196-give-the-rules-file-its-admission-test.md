# Give `map-implementation-rules.md` its admission test

Type: implementation
Status: resolved

Blocked by: none

## Question

*Surfaced by [`map-implementation-rules.md` carries accounts of what happened, not only the rules its title
names](191-the-rules-file-carries-accounts-rather-than-rules.md)'s worker, and pasted as it wrote it.*

> The file has no test for what it admits, so accounts of what happened accumulate in it beside the rules its title
> names — the human's own words on reading it: *"I am confused, why is there in map implementation rules stuff that
> are not rules?"*. Node 191 settled the test and the clause that makes it applicable. Write both into the file's
> opening, and apply them to nothing.

**Blockers, in the worker's words:** *"none."*

**Its sequencing note, in the same worker's words and marked by it as not an edge:**

> six nodes are open or claimed on this file (149, 160, 184, 186, 188, 190) and the manager picks nodes whose paths
> are disjoint, so this must not hold a worktree over that file concurrently with another. It touches only the
> file's opening, which no queued node's condition reaches.

## Acceptance condition

*Written by node 191's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map-implementation-rules.md`, and no other file may be edited. The worker may
> not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> Done means all of the following are true of the finished tree.
>
> 1. That file's opening — the text before its first `##` heading — carries a statement, under a bold lead-in of its
>    own, of what the file admits. That statement says all three of these in its own text: (a) a line belongs in the
>    file only where an implementation node's worker or its checker would do something differently for having read
>    it while working a node; (b) how a rule was learned is not that, naming at least attempt counts, what a run
>    cost, who was wrong, what the file said before, and a manager correcting itself; and (c) such material belongs
>    in `map-history.md`, the markdown link the line already carries to the node that shaped it standing in its
>    place.
> 2. The same statement carries, in its own text, the distinction that decides the hard case: a **trigger** is part
>    of a rule and stays, a **history** is not — a trigger being an error string, a symptom, or the condition under
>    which a rule fires, which is how the rule's reader knows it applies.
> 3. The same statement says who applies the test: whoever is already editing a passage applies it to that passage,
>    and no sweep of the file is owed or licensed by it.
> 4. That statement is at most 1,000 bytes.
> 5. **This node writes the test and applies it to nothing.** Every paragraph of the file under `## Landing an
>    implementation node's work` and under `## What the work is held against`, and both blocks of numbered rules —
>    the five ground rules and the four standing rules for writing — are byte-identical to what they were in the
>    worker's tree before this work.
> 6. The new statement does not contradict the file's existing statement that the account behind a line in it is in
>    `map-history.md`.
> 7. This work supersedes nothing: no text is removed from the file, and no strike markers are added.
> 8. Every markdown link in the file resolves to a path that exists.
> 9. No file outside `.scratch/graph-workflow/` is modified.
> 10. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Clause 5 is what makes this node cheap and what makes it safe to run against a congested file.** It writes the
standard and repairs nothing, so it collides with no queued condition's subject; the repairs ride the nodes already
queued on the paragraphs that need them — [node 190](190-the-rules-file-states-one-list-twice.md) for the
review-route paragraph the human selected, and [node
188](188-move-the-landing-section-out-of-the-workers-file.md) for the landing section's narratives.

**Its shipped counterpart is [node 197](197-ship-what-a-file-of-the-map-admits.md)**, which the human directed in
their own words at node 191's interview and which is blocked on node 194.

## Flags

*Both are the worker's own text, pasted. The ids are the manager's bookkeeping and nothing else.*

`196.1` **· settled** `ASSUMPTION` — **On saying `attempt` where the condition says `run`.** Clause 1(b) asks the
statement to name *"what a run cost"*. `CONTEXT.md` refuses `run` as a synonym for both **effort** and **attempt**,
and the glossary is authoritative over this effort's prose, so I wrote *"how many attempts it took, what one
cost"* — the same two categories in the effort's own words. I read the condition as demanding the substance and not
the token. If a checker reads clause 1(b) literally, the statement names the category without using the refused
word.

`196.2` **· settled** `ASSUMPTION` — **On the overlap I could neither avoid nor repair.** The opening's third
paragraph already says the account behind a line here is in `map-history.md`. The new statement says it again, more
specifically, because clause 1(c) requires it in the statement's own text; clause 7 forbids removing the older
sentence. I left both rather than breach either clause, and surfaced a node for the collapse instead of doing it
under a condition that says this node applies the test to nothing.

## Review

### Checker run 1 — `PASS`

*Pasted as the checker wrote it, ordered under its own headings; every sentence is the checker's.*

> **Settled first — the work moved a file I read for standards.** The change is a pure insertion (`git diff
> --numstat` → `10 0`, zero deletions) in the file's opening, above the first `##` heading. I extracted both
> sections that carry standards from the base blob (`59e052b`) and from the working tree and hashed them: `##
> Landing an implementation node's work` — 16577 bytes, sha256 `c837fc157f71` on both sides; `## What the work is
> held against` — 8583 bytes, sha256 `04c60af5a80c` on both sides. So the set of things the standards require or
> refuse is identical element for element. No raise. **The inserted statement is itself a rule about the file, but
> it is the work under check**, and clause 5 says this node applies it to nothing — so I held the work against the
> standards named in `## What the work is held against` and not against the text the work adds.
>
> **Clause 4. Met. 938 bytes.** What I measured: the paragraph as one blank-line-delimited block, from `**What this
> file admits.**` through the closing `.` after the node 191 link, counting its own internal line breaks and no
> trailing newline. Unwrapping the line breaks to single spaces gives the same 938 (930 characters; the difference
> is four em dashes at 3 bytes each). Every reading is under 1,000.
>
> **Clause 5. Met, by diff rather than by reading.** Ten insertions, zero deletions, all ten above the first `##`
> heading; the two named sections hash identically to the base, and both numbered blocks sit inside `## What the
> work is held against`, so they are covered by that identity. **Worth one observation for the manager, not a
> finding:** by the new test's own words, material already in `## Landing an implementation node's work` — attempt
> counts, who was wrong, a manager correcting itself — **would not be admitted**; the statement's own clause 3 and
> the condition's clause 5 are what keep that from being owed here.
>
> **Clause 7. Met.** `~~` occurs 24 times in the base blob and 24 times in the working tree, so no strike marker was
> added. **Clause 8. Met.** I unwrapped the file to single lines — a link wrapping across a newline is invisible to
> a line-wise search — and resolved every `[…](…)` target: **45 links, 27 distinct targets, 0 missing.**
>
> **The bar.** Command half verified from the tree: a `find` to depth 3 for eight manifest and formatter names
> returned nothing, no `.github`, no test directory. **`CONTEXT.md`'s `_Avoid_` lines checked by hand** rather than
> by grep, as the standards section instructs: `attempt` is the preferred term where `retry`/`run`/`session` are
> refused; `sweep` is used in exactly `CONTEXT.md`'s sense in the phrase refusing one. No refused word appears.
> **`/writing-for-agents`** — `trigger` and `history` are used as leading words, repeated as bolded tokens, defined
> once. The one negation is paired with the positive target stated first and with a positive destination for the
> excluded material.

*No `NOT COVERED`. No questions raised.*

### Gate — `approve`

**The human's word, `verbatim`.**

> approve

*One checker run, `PASS`, with no questions and nothing uncovered. No correction round. Both flags are settled by
the approval.*

## Answer

*Pasted as the worker wrote it.*

> **The file now states what it admits, in its opening, and applies it to nothing.** The statement went in as one
> paragraph, 939 bytes, placed second in the opening — directly below the paragraph naming the file's two readers,
> because the test is defined over exactly those readers and belongs beside them, and necessarily above the
> standing sentence *"Nothing below was reworded on the way here"*, which claims a property of everything after it
> that a new paragraph would falsify.
>
> **The change is a pure insertion, and that is proven rather than asserted.** Deleting the added block from the
> finished file reproduces the pre-work file byte for byte — same md5, `8cea461c62ebb7b3396da185829bc718`. So clause
> 5's byte-identity holds over the whole rest of the file and not only over the sections it names: 27,666 bytes in,
> 28,606 out, 940 added, nothing else touched. The strike-marker count is unchanged at 24, so nothing was
> superseded. All 45 markdown links in the file resolve.
>
> **`run` was not used, and `attempt` carries its sense.** The condition asks the statement to name *"what a run
> cost"*. `CONTEXT.md` refuses `run` twice — as a synonym for **effort** and for **attempt** — and the glossary is
> authoritative, so the statement says *"how many attempts it took, what one cost"*, which names attempt counts and
> cost together in the effort's own vocabulary. **The category is the condition's; only the word is this node's.**
>
> **What the statement deliberately does not carry is an account of itself.** Writing the history of the admission
> test into the file the admission test governs is the defect this node closes, so the paragraph states its current
> form and cites node 191, per standing rule 2, and retells none of node 191's worked examples or its reasoning.
>
> **One overlap was left standing rather than repaired.** The opening's third paragraph already ends *"The account
> behind a line here is in `map-history.md`, as it is for a line in `map.md`."* The new statement is strictly more
> specific and subsumes it, but clause 1(c) requires the new statement to say it in its own text and clause 7
> forbids removing anything, so the two now stand together. That is a duplication the file's own standards dislike,
> and it is reported as a node rather than fixed here.

**What the worker reported its work invalidates:** `none`. In its words: *"The statement carries out node 191 and
states a second test beside node 42's rather than widening it; it neither restates nor contradicts node 189's and
node 193's supersession rule, which stands in the paragraph immediately below it."*
