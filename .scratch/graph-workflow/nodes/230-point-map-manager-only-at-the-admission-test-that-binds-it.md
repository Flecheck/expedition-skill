# Point `map-manager-only.md` at the admission test that already binds it

Type: implementation
Status: claimed

Blocked by: 229

## Question

*Specified by [node 225](225-whether-map-manager-only-gets-an-admission-test.md)'s worker after the human chose a
pointer over a restatement, and pasted as that worker wrote it.*

> `map-manager-only.md`'s opening declares its reader and says nothing about what it admits, while its sibling
> `map-implementation-rules.md` opens with an admission test in its own words — so a reader comparing them reads the
> silence as *this file is under no test*. It is: [node 197](197-ship-what-a-file-of-the-map-admits.md)'s shipped
> statement in `graph-conventions.md`'s `## Writing the map` is stated over the reader each file of the map
> declares and names *"the manager alone"* explicitly. The human chose a pointer over a restatement, a full local
> restatement being the duplication node 196 created and node 200 was spent collapsing.

**Blocker, in the worker's words:** *"the sweep node above. Both nodes write `map-manager-only.md`, and the sweep's
condition turns on byte-identity outside its own fourteen edits, so the two are sequenced rather than parallelised
— this map's own rule for two workers over one file."*

## Acceptance condition

*Written by node 225's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map-manager-only.md` and no other file may be edited. The worker may not mark
> this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> Done means all of the following are true of the finished tree.
>
> 1. The file's opening gains **exactly one new paragraph**, placed directly below the paragraph beginning `**The
>    manager is this file's reader** ` and above the paragraph beginning `**Nothing below was reworded on the way
>    here**`. That position is required: the second paragraph claims a property of everything after it, which a
>    paragraph inserted below it would falsify.
> 2. The new paragraph says, in its own words: that what this file admits is stated in `graph-conventions.md`'s
>    `## Writing the map` section, over the reader each file of the map declares; that this file's declared reader
>    is the manager; and that the test is **not** restated here. It cites this node by markdown link in the form the
>    file's other items use.
> 3. **It states none of the test's content.** It does not say what a line must do to earn its place, does not name
>    what is inadmissible, does not distinguish a trigger from a history, and does not state who applies the test or
>    that no sweep is owed. A paragraph containing any of those is a restatement and fails this clause.
> 4. The new paragraph is **at most 400 bytes**, including its trailing newline.
> 5. The change is a **pure insertion**: deleting the new paragraph and its blank separator line from the finished
>    file reproduces the pre-work file byte for byte. Report the md5 of both to show it.
> 6. The count of `~~` occurrences in the file is unchanged, and no existing sentence is reworded, moved or removed.
> 7. Every markdown link in the file resolves to a path that exists, except a link to a path outside this
>    repository, which is out of scope.
> 8. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**The blocking edge is the worker's own and the manager has written it as stated.** Both nodes write
`map-manager-only.md`, and node 229's condition demands byte-identity outside its fourteen spans, so a parallel run
would make node 229 unsatisfiable through no fault of its worker.

**Clause 6 will read differently after node 229 lands, and that is deliberate rather than a defect.** It says the
count of `~~` occurrences is unchanged; node 229's clause (a) drives that count to **zero** in the landing section.
So this clause binds whatever the count is when this node starts, which is what *unchanged* means, and the two
conditions do not disagree.

## Amendment, 2026-09-27 (from node 347)

*Written by [node 347](347-rename-sweep-of-a-file-to-a-word-the-glossary-does-not-own.md)'s worker under its `CONDITIONS`, and filed by the manager after that node landed as commit `4b538be`, whose `graph-conventions.md` text ("No pass over a whole file is owed under the test, and one is allowed.") fixes every word of it.*

- **Clause 3's last sentence pair.** Where it reads "...does not state who applies the test or that no sweep is owed. A paragraph containing any of those is a restatement and fails this clause.", read "...does not state who applies the test, that no pass over a whole file is owed, or that one is allowed. A paragraph containing any of those is a restatement and fails this clause."

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-28. The worker's own text, pasted.*

````
HANDOVER:      Point `map-manager-only.md` at the admission test that already binds it

ANSWER:        `.scratch/graph-workflow/map-manager-only.md`'s opening gains one paragraph. It sits directly below the paragraph that begins `**The manager is this file's reader, and this file is part of the map.**` and directly above the paragraph that begins `**Nothing below was reworded on the way here**`. The paragraph reads:

               > What this file admits is stated in [`graph-conventions.md`](../../.claude/skills/expedition/graph-conventions.md) under `## Writing the map`, over the reader each file of the map declares. This file's declared reader is the manager. The test is not restated here. Placed here by [node 230](nodes/230-point-map-manager-only-at-the-admission-test-that-binds-it.md).

               Calls a later reader would otherwise have to re-derive:
               - The paragraph goes above "Nothing below was reworded" because that paragraph makes a claim about everything after it, and a paragraph added below it would make the claim false.
               - The paragraph has no bold. The file's other opening paragraphs lead with a bold sentence, but writing rule 5 allows bold only where a term is defined, and this paragraph defines none.
               - The paragraph links `graph-conventions.md` by the relative path `../../.claude/skills/expedition/graph-conventions.md`. That is the same form `map.md` uses for `glossary.md`, and the path resolves.
               - The paragraph states nothing of the test's content. It does not say what earns a line its place, what is inadmissible, how a trigger differs from a history, who applies the test, or whether a pass over a whole file is owed or allowed. The only thing it takes from the test is "over the reader each file of the map declares", which clause 2 of the condition requires.
               - Measurements: the paragraph is 364 bytes including its trailing newline, against a limit of 400. The file's md5 was `3473e4b62a246c9bd57235bbdb9a2091` before the work and is `247fbe1bca106182b7255afbf4db716f` after. Deleting lines 5 and 6 (the new paragraph and its blank separator line) gives back `3473e4b62a246c9bd57235bbdb9a2091`, so the change is a pure insertion. The file had 6 `~~` occurrences before and has 6 after. Every relative markdown link in the file resolves. The one absolute link, `/home/mathieu/projects/Lang`, points outside the repository and is out of scope (it exists on this machine anyway).

INDEX LINE:    `map-manager-only.md`'s opening gains one paragraph pointing at `graph-conventions.md`'s `## Writing the map` for what it admits, naming the manager as its reader, restating nothing.

FLAGS:         ASSUMPTION: Clause 1 of the condition quotes the upper paragraph as beginning `**The manager is this file's reader** `, with the bold closing after "reader". The file actually reads `**The manager is this file's reader, and this file is part of the map.**`. There is exactly one such paragraph, and it sits directly above "Nothing below was reworded", so I read the quote as naming it and placed the new paragraph between the two. I did not raise this, because the position is unambiguous and nothing else in the condition depends on the exact quote.
               Index: Node 230's condition quotes the upper opening paragraph of `map-manager-only.md` with its bold span cut short; the worker read it as the file's only such paragraph and placed the insertion there.

NEW NODES:     none

INVALIDATIONS: Node 225 (resolved). Its index line in `decisions.md` says `map-manager-only.md` "gains one pointer sentence". What landed is one paragraph of four sentences: the pointer, the declared reader, the not-restated statement and the citation. Clause 2 of this node's condition requires all four. This narrows the index line's wording and does not contradict the node. No other resolved node is changed.

CONDITIONS:    I searched the `## Acceptance condition` and `## Question` sections of the 67 open nodes (every node not resolved, out of scope or superseded) for these phrases: "manager is this file's reader", "Nothing below was reworded", "admission test", "What this file admits". I also searched them for `map-manager-only.md` together with "opening", "byte", "paragraph", "reader" or "admits".
               - The first two phrases and "What this file admits" match only node 230 itself.
               - "admission test" also matches nodes 186 and 214. Both are about `map-implementation-rules.md`'s test, and this work does not touch them.
               - `map-manager-only.md` appears in 17 other open nodes. Only these touched the opening or byte-level claims:
                 - Nodes 352 and 354 run scope greps for "rules for writing", which the new paragraph does not contain, so their counts are unchanged.
                 - Nodes 254 and 276 quote the landing-policy paragraph, which is unchanged.
               No clause needs replacing and no open node's question changes.

MISSING FROM MAP: none. The map told me where `map-manager-only.md` sits and who reads it. The test's text came from `graph-conventions.md`'s `## Writing the map`, which the node file names.

GATE PAYLOAD:  Checker findings: none yet.
               Paths touched: `.scratch/graph-workflow/map-manager-only.md` only, in the worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/230-admission` (two added lines). There is no append to `map-history.md`, so this does not collide with node 352's pending changes.
               Bar: the repo root holds `.claude/`, `.scratch/`, `.gitignore`, `CONTEXT.md` and `CONTEXT-MAP.md`. There is no manifest, task runner, test suite, formatter or CI. That agrees with the record in `map-implementation-rules.md` ("no build, no tests, no formatter and no CI"), so the bar is its non-command half: the ground rules, the five writing rules, `graph-conventions.md`, `/writing-for-agents`, and the acceptance condition. One difference to report: that record's statement of `.gitignore`'s patterns is not something I re-verified in full, because this node does not touch it.
               Method skills: none invoked, so nothing was skipped.
               Proposed commit message:
               ```
               Point map-manager-only.md at the admission test in graph-conventions.md

               The opening gains one paragraph naming graph-conventions.md's
               "Writing the map" as where what the file admits is stated, and the
               manager as its declared reader, without restating the test.

               Node: graph-workflow/230
               ```

RETROSPECTIVE
1. What I had to hunt for: whether `graph-conventions.md`'s `## Writing the map` still says "the manager alone" (it does, as "one kind of worker, or the manager alone"), and which relative path form the map files use to link into `.claude/skills` (found in `map.md`'s glossary link).
2. What arrived that this node did not need: almost all of `map.md` (about 45 KB combined with the rules file) and the manager's note about node 352. Only the rules file's writing rules and the bar paragraph were used.
3. What would have made this easier: a condition that quoted each anchor paragraph's first bold span exactly, or anchored on a plain prefix such as "The manager is this file's reader". A spawn line naming the md5 command to use would also have helped.
4. What was stale, wrong or contradictory: the clause 1 quote does not match the file's bold span (flagged above). Node 225's index line says "one pointer sentence" while the condition requires a four-part paragraph (under INVALIDATIONS). `map.md` says "The graph is ~~six~~ seven files" while `decisions.md` line 34 still says "six files". That was already known, and I did not touch it.
````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 226's check; the condition reached it as a verbatim copy in `$TMPDIR/c230.md`.*

> PASS
>
> Node 230, "Point `map-manager-only.md` at the admission test that already binds it". The work is the uncommitted diff to `.scratch/graph-workflow/map-manager-only.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/230-admission`, on base ad51d38. Following the rules file, I read this record file as the work. I read the whole condition in `/tmp/claude-1000/c230.md`, with node 347's amendment applied to clause 3. I held the work to the ground rules in `/tmp/claude-1000/ground.md` and to the five writing rules now in the worktree's `map.md`.
>
> **Parts of the condition**
>
> - **Scope:** met. `git status --short --untracked-files=all` shows only `map-manager-only.md`. No node file, `decisions.md` or `flags.md` changed.
> - **1:** met. Exactly one paragraph is added, at line 5. It sits directly below the paragraph beginning `**The manager is this file's reader**` and directly above the one beginning `**Nothing below was reworded on the way here**`.
> - **2:** met. The paragraph says all three things and cites the node by markdown link, in the file's "Settled at / Moved … by [node]" style:
>   - "What this file admits is stated in [`graph-conventions.md`](../../.claude/skills/expedition/graph-conventions.md) under `## Writing the map`, over the reader each file of the map declares."
>   - "This file's declared reader is the manager."
>   - "The test is not restated here."
>   - "Placed here by [node 230](nodes/230-point-map-manager-only-at-the-admission-test-that-binds-it.md)."
> - **3 (amended):** met. The paragraph states none of the test's content. It does not say what a line must do to earn its place, names nothing as inadmissible, and does not mention a trigger or a history. It says nothing about who applies the test, and nothing about whether a pass over a whole file is owed or allowed.
> - **4:** met. `sed -n 5p | wc -c` gives 364 bytes, including the trailing newline. The limit is 400.
> - **5:** met. Deleting lines 5–6 (the paragraph and its blank separator) reproduces the pre-work file byte for byte.
>   - md5 of `git show HEAD:…/map-manager-only.md`: `3473e4b62a246c9bd57235bbdb9a2091`.
>   - md5 of `sed '5,6d'` on the finished file: `3473e4b62a246c9bd57235bbdb9a2091`.
>   - Line 6 is 1 byte, which is the blank line.
> - **6:** met. There are 6 `~~` occurrences both before and after. Clause 5's byte-for-byte result shows no existing sentence was reworded, moved or removed.
> - **7:** met. Every `](path)` target outside fenced blocks resolves. Relative paths were resolved from `.scratch/graph-workflow/`, including `../../.claude/skills/expedition/graph-conventions.md`. The one absolute path, `/home/mathieu/projects/Lang`, also exists.
> - **8:** met. See the bar below.
>
> **The bar**
>
> - The rules file records no build, tests, formatter or CI, and the repo confirms that.
> - `git diff --check` is clean (exit 0).
>
> **Standards**
>
> - These bore on the work, and I found nothing against any of them:
>   - `graph-conventions.md`'s `## Writing the map`. Pointing at the test instead of restating it keeps a single statement of the rule.
>   - The writing rules. Rule 2 (cite, do not restate) and rule 4 (cite by heading) are met, and each sentence carries one idea.
>   - `CONTEXT.md`'s `_Avoid_` lines.
>   - `/writing-for-agents`.
>   - The ground rules.
> - No reviewing skill is named, so I ran none.
>
> NOT COVERED:
> - None of the condition's parts is uncovered. The worktree diff establishes that the worker wrote nothing to the node, `decisions.md` or `flags.md`.

### Gate — approve, `standing yes`, 2026-09-27

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and its one NOT COVERED item is the worker's bookkeeping. This settles none of the node's flags; they settle at the node closing report.

## Flags

`230.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above.* Node 347's replacement for clause 3's last sentence pair was filed on this open, unclaimed node without asking the human first.

`230.2` `ASSUMPTION` — Clause 1 of the condition quotes the upper paragraph as beginning `**The manager is this file's reader** `, with the bold closing after "reader". The file actually reads `**The manager is this file's reader, and this file is part of the map.**`. There is exactly one such paragraph, and it sits directly above "Nothing below was reworded", so I read the quote as naming it and placed the new paragraph between the two. I did not raise this, because the position is unambiguous and nothing else in the condition depends on the exact quote.
