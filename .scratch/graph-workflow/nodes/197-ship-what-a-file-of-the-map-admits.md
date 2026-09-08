# Ship what a file of the map admits, in the conventions document

Type: implementation
Status: resolved

Blocked by: 194

## Question

*Surfaced by [`map-implementation-rules.md` carries accounts of what happened, not only the rules its title
names](191-the-rules-file-carries-accounts-rather-than-rules.md)'s worker, and pasted as it wrote it.*

> `graph-conventions.md`'s `## Writing the map` says how a map file is written — current statements, the account
> moving to `map-history.md` — and says nothing about what a map file **admits**, so nothing shipped stops the next
> effort's map siblings filling with accounts the way this effort's did. The human directed that node 191's answer
> ship, `verbatim`: *"I think it should be in graph conventions also"*.

**Blockers, in the worker's words:**

> 194. Node 194's clause 3 widens `## Writing the map` and `### Change the map` from `map.md` to its siblings that
> state current rules, and this node's clause 1 attaches to files as a class rather than to `map.md`, so running it
> first would state the discipline over a scope node 194 then rewrites.

**Its sequencing note, in the same worker's words and marked by it as not an edge:**

> node 142 sits at its gate on this file and nodes 146 and 153 are open on it; the manager sequences rather than
> parallelising worktrees over one file.

## Acceptance condition

*Written by node 191's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.claude/skills/expedition/graph-conventions.md`, and no other file may be edited. The worker may not
> mark this node, resolve it, or write a line in `decisions.md` or `flags.md`. This is a file the workflow ships, so
> it is edited plainly: superseded wording is removed rather than struck, and nothing is moved to any history file.
>
> Done means all of the following are true of the finished tree.
>
> 1. The `## Writing the map` section states what a file of the map **admits**, and not only how one is written. In
>    its own text: each file of the map declares who reads it, and a line belongs in that file only where the reader
>    it declares would do something differently for having read it while working a node. It is stated over the map's
>    files as a class, so that a file holding one kind of worker's rules and a file holding only the manager's are
>    both reached without either being named as the rule's subject. Naming them as examples is permitted.
> 2. The same section states that how a rule was learned is not admitted by that test — naming at least attempt
>    counts, what a run cost, who was wrong, and what a file said before — and that such material belongs in
>    `map-history.md`, the markdown link to the node that shaped the line standing in its place.
> 3. The same section states the distinction that makes the test applicable: a **trigger** is part of a rule and
>    stays, a **history** is not — a trigger being an error string, a symptom, or the condition under which a rule
>    fires, which is how the rule's reader knows it applies.
> 4. The same section states who applies the test: whoever is already editing a passage applies it to that passage,
>    and no sweep of a file is owed or licensed by it.
> 5. What clauses 1 to 4 add totals at most 1,200 bytes. It states demands rather than recounting where they came
>    from, and it names no effort, no node number, and no path outside `.scratch/<effort>/`.
> 6. The material in clauses 1 to 4 is stated **once** in the file. The `## The seven files` gloss for the
>    implementation-rules file may gain at most one clause pointing at `## Writing the map` and gains nothing else,
>    and no other section restates any of it.
> 7. No procedure under `## Procedures` is reworded, and the numbered list under `## Mechanical checks` is unchanged
>    in content, count and order.
> 8. Every markdown link in the file resolves to a path that exists.
> 9. No file outside `.claude/skills/expedition/` is modified.
> 10. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**The manager offered to fold this into [node 194](194-ship-where-the-never-delete-rule-stops.md)'s open condition
rather than mint it, and its author declined**, on the ground recorded as flag `191.4`: node 194's condition was
written by node 189's worker, and adding a demand that author never weighed is the failure node 191's own finding
names. **The manager withdrew the offer rather than pressing it**, so this node exists as a fifth node queued
serially on `graph-conventions.md`, which its author named as the price it accepted.

**Its clause 5 forbids exactly what this effort's own record file did wrong.** *"It states demands rather than
recounting where they came from, and it names no effort, no node number"* — the shipped statement of the admission
test is itself written under the admission test.

## Flags

*Both are the worker's own text, pasted. The ids are the manager's bookkeeping and nothing else.*

`197.1` **· settled** `ASSUMPTION` — **On not shipping the condition's word `run`.** Clause 2 names the unadmitted material by four examples, one being *"what a run cost"*. I shipped `how many attempts it took and what they cost` instead. `run` is refused by `CONTEXT.md`'s **Attempt** entry for precisely this concept, the bar's non-command half includes those `_Avoid_` lines, and the file's own fifth line declares that terms are used exactly as the glossary defines them — so the condition's example word could not ship in this file without breaking the file's own opening. I read clause 2 as demanding that the four kinds of material be named, not that its example words be quoted; all four are named, with attempt counts and their cost in one clause. If clause 2 demanded the wording, this is where the work departs from it.

`197.2` **· settled** `ASSUMPTION` — **On clause 8's reach into a fenced code block.** Clause 8 requires every markdown link in the file to resolve to a path that exists. The file has no markdown link outside a fenced block, and the one link-shaped string inside one is the documented **form** of a `flags.md` line, `[<node name>](nodes/NN-<name>.md)`, whose placeholder path cannot exist. I read clause 8 as not reaching it — the file's own `## Reading the graph` rule 2 excludes fenced blocks — and left it exactly as it stood at `HEAD`. I did not "repair" it, because the only repair is deleting the form the file exists to specify. If clause 8 reaches fenced placeholders, it was unmeetable before this node started.

## Review

### Checker run 1 — `PASS`

*Pasted as the checker wrote it, under its own headings, in its own order. Every sentence is the checker's.*

> ## Settled first: the standard that moved under the check
>
> `graph-conventions.md` is named as a standard by `map-implementation-rules.md` (`## What the work is held against`, both enumerations) **and** is the path under check. I settled this before checking anything else, on operative content alone, from an unwrapped word-level diff (`git diff --word-diff=plain --word-diff-regex='[^[:space:]]+'`) over the whole file rather than a line diff.
>
> The diff contains exactly two changes and nothing else:
> 1. `does.` → `does; what it admits is under `## Writing the map` below.` — a cross-reference. It requires nothing and refuses nothing, so it is not operative content.
> 2. One wholly new paragraph, 8 lines, inserted at line 108.
>
> **Nothing was removed and nothing was altered.** Every element of the standard's operative content that existed at `02f9e38` survives byte-identical — I confirmed this by SHA-256 over the file from `## Adding a node` to EOF (identical both sides), and by the word-diff showing zero deletions elsewhere. So an unmoved statement survives, and it is the whole of the pre-existing standard.
>
> The one added element governs "each file of the map" — the seven files under `.scratch/<effort>/`. The work under check is `.claude/skills/expedition/graph-conventions.md`, a file the workflow *ships*, which the file's own text puts on the other side of that line ("The product the effort changes, and every file the effort ships, are edited plainly"). The added element therefore does not reach the work, and reading the standard from either side gives the same result for every part of this work. The contract's stated ground for raising — *"you have nothing unmoved left to hold the rest of the work against"* — does not obtain. I checked rather than raised. See the question below.
>
> ## Standards I read, and which bore
>
> From `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md`, `## What the work is held against` only; I opened no other file in that directory.
>
> | Standard | Bore? |
> | --- | --- |
> | `/writing-for-agents` | **Yes** — the one that bites. Read as a standard from its SKILL.md, applied by hand. |
> | `CONTEXT.md` `_Avoid_` lines | **Yes** — checked by hand, not by grep list. |
> | This effort's 5 ground rules | **Yes** |
> | The 4 standing rules for writing | **Yes** |
> | `graph-conventions.md` | **Yes** — pre-existing operative content, per above. |
> | `/coding-principles` | Read; no purchase. Prose deliverable, no code. |
> | `/naming` | Read; applied to the coined terms. No defect. |
>
> **No reviewing skill is named for this repo**, and per the rules file I did not go looking for one. I invoked no skill in an agent and spawned nothing, so the "givens supplied" duty never arose. I read the changed path as **the work under check** and derived no statement of intent from its content, per the rules file's record-under-check rule.
>
> `/writing-for-agents` in detail: the paragraph is in-file reference on the right rung, co-located under one heading; "trigger" and "admits" are leading words recruiting real priors; the two prohibitions ("not that", "no sweep is owed") are each paired with the positive target (the destination `map-history.md`; what a trigger *is* and that it *stays*), which is what that skill's negation lever asks; 802 bytes on a 28 KB document is not sprawl; and it is not a no-op — it changes behaviour against the default. The pointer clause front-loads and names its target by heading.
>
> `CONTEXT.md`: the added text uses **"attempt"** and **"sweep"**, both of which are *preferred* glossary terms used in their glossary senses, not refusals. It notably says "what they cost" where the condition said "what a run cost", avoiding `run`, which **is** refused under both **Effort** and **Attempt**. My two grep hits (`learn`, `something`) are false positives — both words sit in a parenthetical rationale, not on the refused list. `where` confirmed not refused by any `_Avoid_` line.
>
> ```
> PASS
> ```
>
> Preamble — work is only `.claude/skills/expedition/graph-conventions.md`; `git status --porcelain -uall` shows exactly that one modified path and no untracked files; `HEAD` is still `02f9e38`, so the node is unmarked and unresolved and no line was written to `decisions.md` or `flags.md`. Nothing struck, nothing moved to a history file: the change is purely additive, zero deletions in the word-diff, no `~~` added.
>
> 1. **Met.** Lines 108-110 state the admits test in the file's own text, over `Each file of the map` as a class. The readers, not the files, are named ("one kind of worker, or the manager alone"), so both `map-implementation-rules.md` and `map-manager-only.md` are reached and neither is the rule's subject.
> 2. **Met.** Line 110-112 names all four: "how many attempts it took" / "and what they cost" / "who was wrong" / "what the file said before", then "That material goes to `map-history.md`, the markdown link to the node that shaped the line standing in its place."
> 3. **Met.** Lines 113-115, bolded: trigger stays, history does not, with error string / symptom / firing condition and "is how the rule's reader knows it applies".
> 4. **Met.** Line 114-115: "Whoever is already editing a passage applies the test to that passage: no sweep of a file is owed or licensed by it."
> 5. **Met.** I counted the inserted paragraph, lines 108-115, including its terminating newline: **802 bytes**. Including its blank separator line: 803. The whole-file delta is **855** (28014 → 28869) = 802 + 1 separator + 52 for the clause-6-permitted gloss clause. All three figures are under 1,200, so the count holds on any reading of "what clauses 1 to 4 add". It states demands with no recounting; scans for node numbers, `NN`, `N.k`, effort names and paths returned nothing but `map-history.md`, which is inside `.scratch/<effort>/`.
> 6. **Met.** Phrase counts over the unwrapped file: "declares who reads it" 1, "would do something differently" 1, "how a rule was learned" 1, "trigger" 1, "history is not" 1, "error string" 1, "symptom" 1. "admits" appears twice — the paragraph's lead-in and the permitted pointer. The gloss gained exactly one clause pointing at `## Writing the map` and nothing else (the `.` → `;` is the join). No other section restates any of it; `### Change the map`'s "See `## Writing the map` above" is a pre-existing pointer, unchanged. I checked the adjacency the condition warns about: the base commit's scope paragraph (103-106) states scope, not the test. I also examined the pre-existing current-statement paragraph (117-122), which is the closer candidate — it overlaps only in naming `map-history.md` as the account's destination, which clause 2 itself *demands* the new text state, and it states none of the four elements. Not a restatement.
> 7. **Met, by byte-identity rather than by reading.** SHA-256 over `## Procedures` to EOF: `d8b5a5f1...` both sides, 6738 bytes both sides. Over `## Mechanical checks` to EOF: `3e665619...` both sides, 1517 bytes both sides. Everything from `## Adding a node` to EOF is byte-identical. The numbered list is 10 items, `1`-`10` in order.
> 8. **Met.** The file contains **zero markdown links outside fenced code blocks** (regex over the unwrapped file found one candidate; a fence-state scan confirms it sits inside a fence). That candidate is the `flags.md` line-form template at line 87, `[<node name>](nodes/NN-<name>.md)` — a template with `NN`/`<name>` metavariables that cannot resolve by construction, whose path is relative to `.scratch/<effort>/` and not to the skill directory, inside a fence the file's own `## Reading the graph` rule 2 tells any scanner to skip, and byte-identical to base. I judged it not a markdown link; disclosing the decision so it is visible rather than assumed.
> 9. **Met.** `git status --porcelain -uall` shows one modified path, inside `.claude/skills/expedition/`.
> 10. **Met.** See below.
>
> **The bar.** Command half: **empty, verified from the tree rather than taken on assertion.** `git ls-files` returns 217 files — 216 `.md` plus `.gitignore`. No manifest, task runner, formatter config, lockfile or ignore-lint file of any kind (searched for `package.json`, `Cargo.toml`, `pyproject.toml`, `Makefile`, `justfile`, `Taskfile`, `.prettierrc`, `.editorconfig`, `.eslintrc`, `rustfmt.toml`, `.markdownlint*`, `flake.nix`, `pre-commit`, and others): none. No `.github/`, `.gitlab-ci`, `.circleci`, `.husky`. No test directory or test file. The only ignore file is `.gitignore`, which ignores `.worktrees/` and `.claude/worktrees/` and invokes nothing. So there was nothing to run, and under the *"if relevant"* clause that is a complete bar. **I ran no command that writes and changed nothing.** Non-command half: held above; nothing bit.

**The question it handed back alongside its `PASS`, in its own words.** It blocks nothing and it is not about this node's condition.

> About the checker contract, not this condition, and it blocks nothing. `expedition-checker/SKILL.md`, under "Where the work moved one of them", tells a checker to compare the standard's operative elements as sets and then: "An element was added, removed or altered. The operative standard has itself moved... Raise it." Read literally, that forces a raise on *any purely additive* edit to a shipped file that the rules file also names as a standard — which is precisely what this node's condition demands, so the branch would make this class of work permanently uncheckable. I did not take it, because the branch's own stated reason ("you have nothing unmoved left to hold the rest of the work against") is false here: nothing pre-existing was removed or altered, and the single added element governs the map's files rather than the shipped file under check. If the human wants that reading enforced instead, this node's PASS was reached on the other one; if not, the branch may want a clause distinguishing an added element that does not reach the work from one that does.

*Nothing came back `NOT COVERED`. In the checker's words: “every clause was establishable from the paths and text I was given.”*

### Gate — `approve`

**The human's word, `verbatim`.**

> approve

*One checker run, `PASS`, with nothing uncovered. No correction round. Both flags are settled by the approval. The manager offered at the gate either to mint a node for the checker-contract branch on the human's word or to mint it anyway on approval; the approval came, so the node is minted — see the manager's note below.*

## Answer

*Pasted as the worker wrote it.*

> `graph-conventions.md`'s `## Writing the map` now states what a file of the map **admits**, not only how one is written. One paragraph was inserted between node 194's scope paragraph and the current-statement paragraph, so the section reads scope → what a file admits → how an item is written → what the move preserves → the size target. Admission before form.
>
> The shipped text, in full:
>
> > **What a file of the map admits.** Each file of the map declares who reads it, and a line belongs in that file only where the reader it declares — one kind of worker, or the manager alone — would do something differently for having read it while working a node. **How a rule was learned is not that**: how many attempts it took and what they cost, who was wrong, what the file said before. That material goes to `map-history.md`, the markdown link to the node that shaped the line standing in its place. **A trigger is part of a rule and stays; a history is not** — an error string, a symptom, or the condition under which a rule fires is how the rule's reader knows it applies. Whoever is already editing a passage applies the test to that passage: no sweep of a file is owed or licensed by it.
>
> **The calls inside it a later reader would otherwise re-derive.**
>
> **The subject is `each file of the map`, and the reader kinds are a parenthetical.** That is what makes the test reach a file holding one kind of worker's rules and a file holding only the manager's without naming either as the rule's subject, and it is why a sibling that does not exist yet is reached the day it is written. No file is named as an example; naming one was permitted and was not needed, the section's own opening paragraph already fixing which files it covers.
>
> **Nothing here restates that opening paragraph.** It says which files the section covers; this says what any of them admits. The two are adjacent and disjoint, which is what clause 6 was guarding.
>
> **`what a run cost` is not the shipped wording, and the substitution is deliberate.** The condition's clause 2 names four kinds of material by example, one of them *"what a run cost"*. `run` is refused by `CONTEXT.md` for exactly this concept — its **Attempt** entry, *"One worker instance on one node"*, refuses `retry, run, session` — and this file's own fifth line says terms are used exactly as the glossary defines them, so shipping `run` would contradict the file's opening. The four kinds are named as `how many attempts it took and what they cost, who was wrong, what the file said before`: attempt counts and the cost of an attempt collapse into one clause in the glossary's own word, and all four kinds are named. Flagged below.
>
> **The trigger clause carries its own reason and no example.** Node 191 worked the distinction on two cases from this effort's record and neither could ship. What replaces them is the operative half — *"is how the rule's reader knows it applies"* — which is the test a later reader applies to a paragraph in hand: an error string, a symptom or a firing condition is the rule, because without it the reader cannot tell the rule reaches them.
>
> **The `## The seven files` gloss for the implementation-rules file gained the one clause clause 6 permits**, `; what it admits is under `## Writing the map` below.` It is a pointer and states none of the test, so the material stands once in the file. It was spent on that gloss because that file's declared reader is the narrow one, which is where a reader meets the question.
>
> **Measured rather than estimated, against the tight caps.** The clauses 1-4 block is **803 bytes** inserted against a 1,200-byte cap. The pointer clause is a further 52 bytes, outside that count on clause 6's own separation of the two. The file goes 28,014 → 28,869 bytes. The block contains no digit, no effort name, no node number, and no path but `map-history.md`.
>
> **Clause 7 was held as byte-identity, not as judgement.** A copy of the file was taken before the first edit and verified equal to `HEAD`; `## Procedures` through `## Mechanical checks`, and the `## Mechanical checks` list to end of file, hash identically to that copy. The numbered list is 10 items, unchanged in content, count and order. The whole-file diff is two hunks and nothing else.
>
> **Clause 8 holds, and on one reading recorded below.** The file contains **no markdown link at all** outside a fenced code block; the sole link-shaped string is `[<node name>](nodes/NN-<name>.md)` inside the `flags.md` form block, a placeholder whose path cannot exist by construction, and the file's own `## Reading the graph` rule 2 says to skip fenced code blocks. Nothing was added that carries a link.
>
> **The bar's command half is empty, verified rather than taken from the spawn.** No manifest, task runner, formatter config or `.github/` anywhere in the tree; `.gitignore` invokes nothing. The non-command half was run: `CONTEXT.md`'s `_Avoid_` terms were matched against the added text programmatically, and the single hit is `where`, which the rules file already establishes is refused by no `_Avoid_` line and is a false positive of that scan. Ground rule 1 holds — the added text names no repo, machine or toolchain, only graph files.

**What the worker reported its work invalidates:** `none`, with two near-misses it recorded because each looks like one. In its words:

> `none`. Two near-misses, recorded because each looks like one.
>
> **Node 196 is a claimed sibling on the same discipline and is not made false or trivial.** It writes the test into `map-implementation-rules.md` over that file's two named readers; this ships the general shape over the reader each map file declares. Node 191's answer wants both, and neither file's wording is the other's.
>
> **Node 195's third passage is stale, and node 194 rather than this node made it so.** Node 195's question quotes the file's opening as saying *"`map.md` is the one file whose superseded text is also *moved* rather than left in place"* and calls that passage doubtful. That wording is no longer in the file — node 194's preamble replaced it. Node 195's two fog passages both still stand, untouched here; one of them is the paragraph immediately below this insertion and was deliberately left alone.
>
> One coordination note, not an invalidation: **node 198 edits the same gloss sentence this node appended a clause to** — the `map-implementation-rules.md` gloss in `## The seven files`. Node 198 removes contents that node 188 removes; the clause added here is a pointer at a heading and is independent of that list, but the two nodes write the same sentence.

