# Cut the pointers that list their target to one clause

Type: implementation
Status: claimed
Blocked by: none

## Question

Can the four pointers node 355 found listing or summarising their target heading be cut to the heading and one clause about what the reader goes there for?

*Reported by [node 361](361-whether-a-pointer-that-summarises-its-target-restates-it.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Acceptance condition

*Authored by node 361's worker and filed by the manager.*

> The work is `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition/graph-conventions.md`, and no other file may be edited. Scope: the scope came from no search command. The places are the four passages listed below, which node 355's worker found by reading both files in full. If you find another pointer in any file under `.claude/skills/` that lists the items its target heading holds or states that heading's rules, report it and do not edit it.
>
> A **pointer** here means text that names a heading of another file so that the reader goes there. In the finished form, each pointer names the heading and says, in one clause at most, what the reader goes there for. It lists none of the items that heading holds and states none of its rules. Example of the finished form, already in `graph-conventions.md`: "`## Acceptance conditions` in `SKILL.md` says who writes it and who may change it after it is written."
>
> Done means all of the following are true of the finished tree.
> 1. `.claude/skills/expedition/SKILL.md`, `### The human's words`, last paragraph: the pointer to `### Recording the human's words` in `graph-conventions.md` is in the finished form. The paragraph no longer names the three marks `verbatim`, `paraphrase` and `standing yes`, the quoted option, or `## Interview` and `## Review` as where an entry goes. The pointer to where `graph-conventions.md` states the rule for the `DIVERGENCE` mark stays, in the finished form.
> 2. `.claude/skills/expedition/graph-conventions.md`, `### Recording the human's words`, first paragraph: the pointer to `### The human's words` in `SKILL.md` is in the finished form. It no longer lists when the manager records an answer, what it pastes, when it marks an answer `paraphrase`, and what it does with a terse reply. The sentence saying that the section's rules cover `## Interview` and `## Review` stays.
> 3. `.claude/skills/expedition/SKILL.md`, `## Acceptance conditions`, first paragraph: it points at `graph-conventions.md` in the finished form, in one sentence or in one sentence per heading it names. It no longer states the self-contained rule, the demand about the record as a whole, or what a condition owes about the search that produced its scope. The second paragraph ("Where an agent minted the node, …") is unchanged.
> 4. `.claude/skills/expedition/SKILL.md`, `### The four constraints on a condition you write yourself`, item 2: the item still says to read the condition back before the node is claimed and to record that reading on the node. It no longer names the three rules one by one. Instead it points, in the finished form, at the heading of `graph-conventions.md` that holds them.
> 5. Each statement that clauses 1 to 4 remove is still stated at the heading the pointer names. No rule is lost.
> 6. No heading in any file under `.claude/skills/` is renamed. Every heading a changed pointer cites exists in the named file with exactly the cited text.

*The worker's note for the manager, pasted:* "this concerns the same two files as node 359 (`SKILL.md`, `graph-conventions.md`), but different passages. Node 359 is claimed, so under the contract these would be filed as a new node. If 359 is unclaimed when you file this, the clauses below may join its condition instead."

## Handover, attempt 1

*The worker's own text, pasted, 2026-09-29.*

````
HANDOVER:      Cut the pointers that list their target to one clause

ANSWER:        Yes. All four pointers now name their target heading and say in one clause what the reader goes there for. Only `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition/graph-conventions.md` changed.
  1. `SKILL.md`, `### The human's words`, last paragraph. It now reads: "`### Recording the human's words` in `graph-conventions.md` says what form each recorded entry takes. The same file's description of `## Interview` states the rule for the `DIVERGENCE` mark." The paragraph no longer lists the three marks, the quoted option or the two sections. The `DIVERGENCE` pointer stays, and I also cut the phrase that described what the mark is put on.
  2. `graph-conventions.md`, `### Recording the human's words`, first paragraph. The sentence about which sections the rules cover (`## Interview` and `## Review`) stays. It is followed by: "`### The human's words` in `SKILL.md` says when and how the manager records an answer."
  3. `SKILL.md`, `## Acceptance conditions`, first paragraph. The pointers to `## The node file` and `### Claim` were already in the finished form and are unchanged. The third sentence now reads: "The description of `## Acceptance condition` under `## The node file` states the rules that bind every condition." That is one sentence per heading named. The second paragraph is unchanged.
  4. `SKILL.md`, `### The four constraints on a condition you write yourself`, item 2. It still says to read the condition back before the node is claimed and to record that reading on the node. It no longer counts or names the rules, and it points at "the description of `## Acceptance condition` under `## The node file` in `graph-conventions.md`". The count "three" was dropped because a count summarises the target, and that description holds more rules than three.
  Nothing that was removed is lost. The three rules on a condition (self-contained, no demand about the record as a whole, and what a condition owes about its search, with when it is malformed) are all under `### \`## Acceptance condition\``. The three marks and the quoted option are under `### Recording the human's words`. When the manager records, what it pastes, when it marks `paraphrase` and what it does with a terse reply are all under `### The human's words`. No heading was renamed. Every cited heading exists with exactly the cited text. The nested headings are cited the way the files already cite them: "the description of `## X` under `## The node file`".

INDEX LINE:    Four pointers in `SKILL.md` and `graph-conventions.md` now name their target heading and one clause of purpose, and no longer list the marks, rules or duties those headings hold.

FLAGS:         ASSUMPTION: Clause 1 removes the words saying that `### Recording the human's words` holds "whether an entry goes under `## Interview` or `## Review`". Clause 5 requires that each removed statement still be stated at the heading the pointer names. That heading's first sentence names the two sections as the ones that hold the human's words. Which kind of entry goes in which section is stated under the sibling descriptions `### \`## Review\`` and `### \`## Interview\`` in the same file, not under the named heading itself. I judged that no rule is lost: the removed words described the target, and the placement rule is still in `graph-conventions.md`. I did not edit the target to repeat it.
  Index sentence: node 368 judged that removing "whether an entry goes under Interview or Review" from a SKILL.md pointer loses no rule, because the per-section placement stays under graph-conventions.md's `## Review` and `## Interview` descriptions.

NEW NODES:     One instance the report-only clause reaches, reported and not edited. In `.claude/skills/expedition/graph-conventions.md`, `### How a check reads the files`, the first bullet reads "`## Reading the graph` above holds three of them: fields are read only from the header block, fenced code blocks are skipped, and node numbers are taken from a `Blocked by:` field by the rule stated there." It lists the rules its target heading holds.
  Whether it is a defect is not settled. The bullet sits in a list of the rules a check reads by, so listing them may be what that list is for. The judgement belongs to node 361's rule, and I did not propose a node for it.
  How I found it: a grep over `.claude/skills/` for a backticked heading followed in the same sentence by "holds/states/says/lists/covers/describes" and then ":", ", and", "the three" or "the two". That grep is heuristic and does not bound every case. Its only other matches were the `your \`## Flags\` entry holds that account instead` lines in the five worker contracts. Those are not pointers.

INVALIDATIONS: none. The edits carry out node 361's definition of a pointer on the four passages node 355 found. They change no resolved node's answer. Node 359's landed passages were not touched.

CONDITIONS:    I searched the `## Acceptance condition` and `## Question` sections of all 64 nodes with status open or claimed for these phrases: "Recording the human's words", "### The human's words", "three marks", "self-contained rule", "four constraints on a condition", "## Acceptance conditions`", "How a check reads the files" and "three rules that bind". Only node 368 matched. No replacement clauses, and no open question changed. Node 367 writes the same pointer definition into map.md rule 6. That is not in this tree and does not overlap these edits.

MISSING FROM MAP: none

GATE PAYLOAD:  The checker has not run yet, so there are no findings to address.
  Paths touched: `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition/graph-conventions.md`. The work is uncommitted in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/368-pointers`, on branch worktree-368-pointers.
  The bar: the repo has no build, tests, formatter or CI. The worktree root holds only `.claude`, `CONTEXT-MAP.md`, `CONTEXT.md`, `.gitignore` and `.scratch`, which agrees with `map-implementation-rules.md`. So the bar is its non-command half.
  `.claude/rules/expedition-triggers.md` has no copy of these passages, so it did not need the same edit.
  Proposed commit message:
    Cut four pointers to their heading and one clause

    SKILL.md's `### The human's words`, `## Acceptance conditions` and constraint 2, and graph-conventions.md's `### Recording the human's words`, now name the heading they point at and what the reader goes there for, and no longer list what it holds.

    Node: graph-workflow/368

RETROSPECTIVE:
1. What I had to hunt for: the settled way to cite a heading whose text is itself backticked, such as `### \`## Acceptance condition\``. I copied the files' existing "description of `## X` under `## The node file`" form. I also had to check whether "whether an entry goes under Interview or Review" is really stated at the named heading. It only partly is, hence the flag.
2. What arrived that this node did not need: most of map.md, and most of map-implementation-rules.md except the bar paragraph. The manager's note about node 367 was useful only as a check that nothing overlaps.
3. What would have made this easier: a clause 5 that says whether "stated at the heading the pointer names" includes sibling headings of the same file. Also, the condition could have given the cut text as the reason for each removal, which would have made the flag unnecessary.
4. What was stale, wrong or contradictory: the node file's worker note about joining node 359 is stale, as the manager said. The removed SKILL.md text claimed that `### Recording the human's words` holds "whether an entry goes under `## Interview` or `## Review`", which that section does not really state. So the old pointer's summary was slightly inaccurate.
````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-29. A fresh checker; the condition reached it as a verbatim copy in `$TMPDIR/c368.md`.*

> PASS
>
> Worktree: /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/368-pointers. I produced the diff with `git -C <worktree> diff`. `git status --short` shows exactly two modified paths, `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition/graph-conventions.md`, and nothing else. So no other file was edited, and there is no bookkeeping path (node status line, `decisions.md`, `flags.md`). Under the rule in map-implementation-rules.md, I read the changed paths as the work.
>
> Scope statement: the condition states that its scope came from no search command, so there was no recorded command to run.
>
> One line per part:
> - Part 1 (SKILL.md `### The human's words`, last paragraph): I read the section with `awk '/^### The human.s words/,/^### Two things/'`. The paragraph is now two sentences.
>   - "`### Recording the human's words` in `graph-conventions.md` says what form each recorded entry takes."
>   - "The same file's description of `## Interview` states the rule for the `DIVERGENCE` mark."
>   - Each pointer has one clause. Neither names the three marks or the quoted option, and neither says which section an entry goes under. The DIVERGENCE pointer stays, in the finished form. Met.
> - Part 2 (graph-conventions.md `### Recording the human's words`, first paragraph): it now reads "`### The human's words` in `SKILL.md` says when and how the manager records an answer." That is one clause, and the four listed items are gone. The sentence "The rules in this section cover `## Interview` and `## Review`, …" is unchanged, as the diff shows. Met.
> - Part 3 (SKILL.md `## Acceptance conditions`, first paragraph): it now has two sentences over three cited headings (`## The node file`, `### Claim`, `## Acceptance condition`). That stays within "one sentence per heading it names".
>   - Each pointer has one clause: "says which nodes carry…", "says when such a node may be claimed", "states the rules that bind every condition".
>   - The self-contained rule, the demand about the whole record and the search rule are no longer stated.
>   - The diff has no hunk touching the second paragraph ("Where an agent minted the node, …"). Met.
> - Part 4 (`### The four constraints…`, item 2): it still says to read the condition back before the node is claimed and to record that reading on the node. It no longer names the three rules. It now points at "the description of `## Acceptance condition` under `## The node file` in `graph-conventions.md`". Met.
> - Part 5 (no rule lost): I read graph-conventions.md `### `## Acceptance condition``. It still states all three rules: the self-contained rule ("A condition is self-contained text…"), the demand about the whole record ("A demand about the record as a whole belongs on the handover…") and the search rule ("Where a condition's scope was derived from a search…", with its three items).
>   - SKILL.md `### The human's words` still states when the manager records an answer, pasting, the `paraphrase` mark, and the terse reply whose option is unclear.
>   - `### Recording the human's words` still states the three marks and the quoted option.
>   - `### `## Interview`` still states the DIVERGENCE rule.
>   - Removed item "whether an entry goes under `## Interview` or `## Review`": at the cited heading, the only matching text is the retained sentence that the section's rules cover both sections. Part 2 explicitly preserves that sentence, and I held part 5 met on it. See the question below. Met.
> - Part 6 (no heading renamed, cited headings exist): the diff changes no heading line; `git diff -U0 | grep '^+#'` finds nothing. `grep -n '^#'` over both files confirms every cited heading exists:
>   - `### Recording the human's words`, `### `## Interview``, `## The node file`, `### Claim` and `### `## Acceptance condition`` in graph-conventions.md.
>   - `### The human's words` in SKILL.md.
>   - Met.
> - Residual clause: I searched every `.md` under `.claude/skills/`, unwrapped into paragraphs, with the pattern `` `#+ …` (in|of) `….md` … (holds|says|states) …: ``. It returned nothing, so there are no other listing pointers to report from that search. The search is narrow, so this does not show that none exist.
>
> The bar: map-implementation-rules.md records that this repo has no build, no tests, no formatter and no CI. So there were no commands to run beyond:
> - `git diff --check`, which printed nothing (no whitespace errors).
> - A line-length check. The added lines are at most 103 columns, and graph-conventions.md's maximum is 105, so the file's wrap width is kept.
>
> Standards: I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`. They are `/coding-principles`, `/naming`, glossary.md's `_Avoid_` lines, the ground rules, the six writing rules, graph-conventions.md and `/writing-for-agents`. No reviewing skill is named, so I ran none. I checked the standards by hand.
> - Writing rules 4, 5 and 6 bore on this work. Every pointer cites by heading. Each new sentence has one idea, is grammatical and has a clear referent. The pointers point rather than restate.
> - None of the new words appear in any `_Avoid_` line (checked against `grep -n -i avoid glossary.md`).
> - None of the added text assumes this repo, this machine or a toolchain.
> - The passages edited are not trigger-duties: `.claude/rules/expedition-triggers.md` has no hits for DIVERGENCE, self-contained or "Recording the human". So no companion edit is owed.
> - `/coding-principles` and `/naming` did not bear on this prose-only change.
>
> QUESTIONS:
> - About `### Recording the human's words` in graph-conventions.md. SKILL.md used to say this heading holds "whether an entry goes under `## Interview` or `## Review`". That clause is now removed, as part 1 demands. The heading itself says only that its rules cover both sections. It does not say which section a given entry goes under; that is stated under `### `## Review`` item 2 and `### `## Interview``.
>   - This gap was already there before the change, and the work did not widen it. Part 2 of the condition explicitly keeps the sentence that covers both sections.
>   - Should that heading also say which section an entry goes under, or point at the two section descriptions?
>   - Form: a statement that an earlier pointer said its target heading held, which the target heading does not actually state.
>   - Extent: this finding has no extent, and its instances are not exhaustive. This is the only instance I found, in the two changed files.

*The manager's note:* the checker handed back a question beside its outcome, so the standing yes does not cover this gate; it goes to the human.

## Flags

`368.1` `ASSUMPTION` — *The worker's own text.* Clause 1 removes the words saying that `### Recording the human's words` holds "whether an entry goes under `## Interview` or `## Review`". Clause 5 requires that each removed statement still be stated at the heading the pointer names. That heading's first sentence names the two sections as the ones that hold the human's words. Which kind of entry goes in which section is stated under the sibling descriptions `### \`## Review\`` and `### \`## Interview\`` in the same file, not under the named heading itself. I judged that no rule is lost: the removed words described the target, and the placement rule is still in `graph-conventions.md`. I did not edit the target to repeat it.
