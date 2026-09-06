# Carry the record-node reading rule into the implementation-rules file

Type: implementation
Status: resolved

Blocked by: none — [node 144](144-make-the-rules-file-stand-alone.md) landed as `37a3d28`

## Question

*Surfaced by [An acceptance condition demands facts about files the checker is told it does not read](163-a-condition-demands-facts-the-checker-does-not-read.md)'s worker, and pasted as it wrote it.*

> Write into `map-implementation-rules.md` the rule that an implementation
> node's work may be this effort's own record, that its checker reads the changed paths
> as the work under check and derives no intent from them, and that a change to the
> node's own status line, `decisions.md` or `flags.md` is a `FAIL`.

**Blockers, in the worker's words:** *"**node 144**, which is claimed and edits this same file to make it stand
alone. Two writers on one file; this node waits for 144 to land."*

## Acceptance condition

*Written by node 163's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map-implementation-rules.md`. The worker may
> edit that file and no other. It may not mark this node, resolve it, or write a line
> in `decisions.md` or in `flags.md`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. One new continuous passage, of not more than 25 lines, sits under the existing
>    heading `## What the work is held against`, beside the paragraph beginning
>    `**The review route for this repo, discovered on first use**`. It is not under a
>    heading of its own, and the file gains no new `##` heading.
> 2. The passage states that on this effort an implementation node's work may be the
>    effort's own record — the files in the directory that holds `map.md` — and that
>    where it is, the checker reads the changed paths it was given as **the work under
>    check**, whatever directory those paths sit in.
> 3. It states that the checker derives no statement of intent or decision from those
>    files: their content is material under check rather than something to reason
>    from, so a resolved node's `## Answer`, a line in `decisions.md`, or a passage in
>    `map.md` appearing among the changed paths tells it nothing about what this work
>    was meant to be. It states that the acceptance condition remains the only
>    statement of intent the checker has.
> 4. It states that the checker's own contract's instruction to read the
>    implementation-rules file for its standards and to open no other file beside it
>    governs the route by which standards reach the checker, and not the changed paths
>    it was given as the work.
> 5. It states that a change to the node's own status line, to `decisions.md`, or to
>    `flags.md` is bookkeeping reserved to the manager; that the checker reports such
>    a change among the work as a `FAIL` on the acceptance condition; and that this
>    holds whether or not the acceptance condition itself excluded those paths.
> 6. It states that the checker says in its outcome that it read the changed paths as
>    the work under this rule.
> 7. The passage states each of the above in full, so that a reader who opens no other
>    file knows what is required. A citation of the node or nodes that shaped it may
>    accompany the statement and carries no part of what it demands.
> 8. The paragraph beginning `**The review route for this repo, discovered on first
>    use**` and the paragraph beginning `**The bar's commands for this repo,
>    discovered on first use**` are unchanged in what they require.
> 9. Nothing under the heading `## Landing an implementation node's work` is changed.
> 10. No text is deleted from the file: any wording this passage supersedes is marked
>    as superseded and left where it is.
> 11. No file outside the one named above is modified.
> 12. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Three nodes now queue on `map-implementation-rules.md`**: this one, [node
144](144-make-the-rules-file-stand-alone.md) which is at its gate, and [node
169](169-rules-file-bar-paragraph-names-the-maps-standing-preferences.md). The manager holds that ordering; the
`Blocked by: 144` edge is the only one written, and it is the one this node's author asked for.

**This node's clause 5 repairs [node 80](80-map-items-nodes-64-and-68-left-stale.md) and [node
156](156-four-resolved-nodes-have-no-index-line.md) without either condition being edited**, per its author's answer.
The manager records the claim and has verified nothing.

## Flags

*The worker's own text, pasted. The id and the link are the manager's bookkeeping and nothing else.*

`171.1` **· settled** `ASSUMPTION` — This passage adds operative content to the very file the checker reads for its standards,
and the checker's contract has a section, `### Where the work moved one of them`, whose second bullet
says that when an element of a standard is added the checker has nothing unmoved to hold the rest of the
work against and must raise. Read literally that directs this node's own checker to raise rather than
produce an outcome. I judged the section aimed at a standard being *rewritten* — here the pre-existing
standards are element-for-element unmoved and the added element is the work itself, so a check is still
possible — and wrote the passage rather than raising. Node 144 rewrote this same file and landed, so the
situation is not new. I hold no authority over the checker's contract and did not touch it; the question
is reported as a new node below.

## Review

***The manager's note before the first check.*** **The manager has spawned this node's checker with no licence and no
instruction about what it may read**, which is a departure from what it did at [node
144](144-make-the-rules-file-stand-alone.md) and is deliberate. Node 144's two paths included `map.md`, which the
checker's contract puts out of reach entirely, so the manager raised it and the human granted a licence. **This node's
one path is `map-implementation-rules.md` — the single file that contract already sends a checker into.** Whether it
may read that file *as the work* rather than *for its standards*, and whether flag `171.1`'s bullet directs it to
raise, are both questions its own contract answers. **The manager has answered neither.** A raise is a legitimate
outcome and the manager will carry it to the human rather than pre-authorising past it.

### Checker run 1 — `PASS`

*Pasted as the checker wrote it, ordered under its own headings; every sentence is the checker's.*

> **First, the thing my contract makes me settle before anything else.** The single changed path is `map-implementation-rules.md` — the file my contract sends me to for the standards. Under `### Where the work moved one of them` I split the standards into operative content and rationale and compared the sets element by element, from `git show HEAD:<path>` against the working file:
>
> - The diff is `20 0` — a pure insertion at line 108, one hunk, zero deleted lines. Old lines 1–107 are byte-identical to new 1–107 (`diff -q`, IDENTICAL); old 108–end byte-identical to new 128–end (IDENTICAL).
> - Every standard therefore sits unmoved: the review route paragraph naming them, the bar's commands paragraph, the ground rules block, the four standing rules for writing. `CONTEXT.md`, `graph-conventions.md`, `/coding-principles`, `/naming`, `/writing-for-agents` are all outside the changed path.
> - The set of things required or refused **of work** is identical on both sides. The inserted passage demands things of the *checker's reading procedure*, and by its own words it "stands beside the standards named above rather than in place of any of them, and supersedes no wording in this file" — which the zero-deletion diff confirms.
> - Its one outcome-bearing clause (bookkeeping among the work is a `FAIL`) is conditional on a node status line, `decisions.md` or `flags.md` appearing among the changed paths. None does. **My outcome is identical read from either side of the change**, which is exactly what leaves the check possible. So: sets identical, no raise, I checked.
>
> I read the changed path as **the work under check**. I reached that from my own contract's given 3 and its `Where the work moved one of them` section — not from the rule the work introduces — so nothing here is circular. I read the file in both capacities: in full as the work, and for its pre-existing standards as standards, deriving no statement of intent from any of it.
>
> **Acceptance condition, part by part.** 1. One passage, lines 108–126: 19 lines (≤ 25), continuous — first blank line after it is 127. Under the existing heading (line 102), immediately after the review-route paragraph (line 106). Heading list before and after is identical — no new `##`. 2. States it, unwrapped. 3. All four clauses present verbatim or near-verbatim. 4. Present. 5. All three clauses present. 6. Present verbatim. 7. Every demand is stated in the passage's own prose; the node 163 citation accompanies it and the passage says outright "the citation carries no part of what the rule demands". The cited path resolves (existence test only — I read no node file). 8. Both named paragraphs fall inside the byte-identical 1–107 range. Unchanged, not merely equivalent. 9. `## Landing an implementation node's work` spans lines 7–101, entirely inside the byte-identical range. Untouched. 10. Zero deleted lines. 11. `git status --porcelain -uall` returns exactly one line, that path. 12. The bar — below.
>
> **The bar.** Command half verified empty rather than assumed: repo root holds only `.claude`, `CONTEXT.md`, `.gitignore`, `.scratch`; a `find` for the usual manifests returns nothing; no `.github`. Complete on its remaining half, not deficient. Non-command half, against the standards the rules file names and only those: **`CONTEXT.md`'s `_Avoid_` lines** — one hit, `project`, inside the human's `verbatim` quote, which the scribe convention forbids altering; `bookkeeping` is not refused, `decision` is refused only as a name for the grilling node kind. **Four standing rules** — cites node 163 without restating it; sits under an existing heading; no line numbers; shapes stated in full. **Ground rules** — 1 and 2 do not bite (this file is not shipped); 3 holds. **`graph-conventions.md`** — consistent with "That is about recording, not about files" and "No edit deletes". **`/writing-for-agents`** — every prohibition paired with its positive target; no no-op sentence; vocabulary reuses existing leading words. Hygiene: no trailing whitespace, no tabs, no CR, ends in a newline, max added line 116 chars.
>
> **No reviewing skill.** The standards name none and I went looking for none. No enumerator is recorded in the condition, so that duty never engaged.
>
> **Two things I considered and set aside as not findings**, so the manager knows they were looked at rather than missed. First, the Landing section's "The graph's own files are *not* committed per node" reads oddly beside a rule saying a node's work may be the record — but the two populations differ, condition 9 fenced that section off anyway, and they reconcile as written. Second, the passage uses "record" for the files, where `CONTEXT.md`'s Manager entry uses it for what the manager writes; the wording is the condition's own, the `_Avoid_` lines do not refuse it, and the shipped checker contract uses the word the same broad way.
>
> **Blindness held.** Inside the effort's directory I read the content of `map-implementation-rules.md` and nothing else — `map.md`, `decisions.md`, `flags.md`, `map-history.md` and node 163 were touched only by a `test -e` existence check for the citation, never opened.

*No `NOT COVERED`. No questions raised.*

***The manager's note.*** **This run answers [node 178](178-whether-adding-a-standard-is-a-moved-standard.md)'s question
by measurement rather than by argument, and it is the third agent to meet that bullet.** Node 144's checker called it
*"a bright line"* and declined to cross it on the ground that its stated reason did not obtain; node 171's worker
judged the same and shipped, flagging itself at `171.1`; this checker settled it on a test neither of them stated —
**that its outcome is identical read from either side of the change**, which is what leaves a check possible. The
manager records the convergence and settles nothing: node 178 remains open and is the human's.

**No licence was spent on this check**, and none was needed. That is the difference from [node
144](144-make-the-rules-file-stand-alone.md), whose paths included `map.md`.

### Gate — `approve`

**The human's word, `verbatim`.**

> approve

*No correction round; run 1's `PASS` is the only run. Flag `171.1` is settled by the approval. **Landed as `e6f6233`**,
rebased onto `8cc9b79` and fast-forwarded; worktree removed, branch deleted.*

***The manager's note on the landing, because it corrects the map.*** **The merge ran entirely inside the sandbox and
needed no override**, this node touching only `.scratch/`. **Removing the worktree afterwards did need one**, the
sandbox carrying `ro` mounts *inside* that worktree — on its own `.claude/skills` and `.git` — so `git worktree
remove` could not delete them. That is [node 175](175-what-the-worktree-cycle-does-to-the-sandbox.md)'s finding
confirming itself in the same landing: what decides is the paths written against the writing session's region, not
which tree the command is issued from. It is also [node
180](180-which-trees-get-the-read-only-skills-overlay.md)'s subject — this worktree carried the overlay, and node 175
measured others that did not.

## Answer

*The manager's, assembled from the worker's own report of what it wrote. The passage itself is in
`map-implementation-rules.md` under `## What the work is held against`, and is the authoritative text.*

The rules file now states, in nineteen lines and in its own words, that an implementation node's work on this effort
may be the effort's own record; that where it is, the checker reads **the changed paths it was given as the work under
check**, whatever directory they sit in; that it derives no statement of intent or decision from them, so a resolved
node's `## Answer`, a line in `decisions.md` or a passage in `map.md` among the changed paths tells it nothing about
what the work was meant to be, the acceptance condition staying its only statement of intent; that the checker
contract's instruction to read the implementation-rules file for its standards and open no other file beside it
governs **the route by which standards reach it** and not the changed paths it was handed as the work; that a change
to the node's own status line, to `decisions.md` or to `flags.md` is bookkeeping reserved to the manager and is a
`FAIL` on the acceptance condition whether or not the condition excluded those paths; and that the checker says in its
outcome that it read the changed paths under this rule. It supersedes no wording and deletes nothing — the diff is
twenty insertions and zero deletions.

**Three calls its worker made that a later reader would otherwise re-derive**, in its own words:

> **Nothing in the file is superseded, and the passage says so.** Clause 10 asks that superseded wording be marked.
> The candidate was the review-route paragraph's *"The standards above are the whole of what work is held against"*,
> which reads as a cap that a rule added below would break. That sentence's subject is reviewing skills — it says the
> standards are given as text rather than discovered — and this passage is a reading rule for how the checker treats
> the changed paths rather than a further entry in the standards list that sentence enumerates. Editing it was also
> barred by clause 8. So the passage closes the question in its own text instead.
>
> **It is one paragraph, not a bulleted block.** "One new continuous passage" admits a strict reading where blank
> lines make several passages; a single unbroken paragraph satisfies both readings.
>
> **The checker's outcome word is `outcome`, not `report`.** `CONTEXT.md` refuses `report` for anything but the
> closing report, and the checker's own contract calls its verdict its outcome.

**What the worker reported its work invalidates:** `none`.
