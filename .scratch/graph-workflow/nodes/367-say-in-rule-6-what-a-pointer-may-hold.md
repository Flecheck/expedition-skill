# Say in rule 6 what a pointer may hold

Type: implementation
Status: claimed
Blocked by: none

## Question

Can standing rule for writing 6 in `map.md` say that a pointer names the heading and, in one clause at most, what the reader goes there for, listing none of the target's items and stating none of its rules?

*Reported by [node 361](361-whether-a-pointer-that-summarises-its-target-restates-it.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Acceptance condition

*Authored by node 361's worker and filed by the manager.*

> The work is `.scratch/graph-workflow/map.md` and `.scratch/graph-workflow/map-history.md`, and no other file may be edited. The worker may not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`. The scope came from no search: the named place is the work.
>
> Done means all of the following are true of the finished tree.
> 1. In `map.md`'s `## Notes`, rule 6 of the numbered list of this effort's standing rules for writing keeps its four existing sentences word for word. Directly after its first sentence ("**Point at a heading of another shipped file instead of restating what it holds, where the reader is already told to read that file.**") it gains these two sentences, word for word: "A pointer names the heading and says, in one clause at most, what the reader goes there for. It lists none of the items that heading holds and states none of its rules."
> 2. Rules 1 to 5 are not reworded, renumbered or reordered.
> 3. The list's bold lead-in names `nodes/361-whether-a-pointer-that-summarises-its-target-restates-it.md` as a markdown link, as a node that shaped the sixth rule.
> 4. The text rule 6 held before this change is appended verbatim to `map-history.md`, under a heading that mirrors the section it came from. `map-history.md` gains text and loses none.
> 5. Every markdown link in the two files resolves to a path that exists.

## Handover, attempt 1

*The worker's own text, pasted, 2026-09-29.*

````
HANDOVER:      Say in rule 6 what a pointer may hold

ANSWER:        Standing rule for writing 6 in `map.md`'s `## Notes` now says what a pointer may hold. Directly after its first sentence it gains two sentences, word for word as the condition gives them: "A pointer names the heading and says, in one clause at most, what the reader goes there for. It lists none of the items that heading holds and states none of its rules." Its four existing sentences are unchanged and stay in their order after the new two. Rules 1 to 5 are unchanged. The list's bold lead-in now ends "...and the sixth by [node 253](...) and [node 361](nodes/361-whether-a-pointer-that-summarises-its-target-restates-it.md)." This carries node 361's ruling into the rule, so a checker is held to it by the rule's own text and no longer needs it passed alongside as "the node 361 ruling".

The change followed `graph-conventions.md`'s `### Change the map`. `map-history.md` gained one section at its end, `## Superseded from `map.md` at node 367 — the sixth standing rule for writing, before it said what a pointer may hold`. It has two `###` subsections, each holding one replaced line verbatim: the lead-in and rule 6. Both came from `map.md`'s `## Notes`, and the shape follows node 354's section. Banking the lead-in was not required by clause 4. It was banked because the lead-in is also rule-stating text that this change replaced.

Checks run over the touched material:
- Check 11 passes: the old `map-history.md` is a byte-exact prefix of the new one (+1,729 bytes), and both removed `map.md` lines appear byte-identically in the appended text.
- Check 4 does not apply, since no `Labels:` line was touched.
- Check 10 reports rule 6's item at 750 bytes, against the 500-byte soft target. It was about 590 bytes before. The lead-in is 449 bytes. Check 10 reports and never fails.
- Every relative markdown link in both files resolves, with 0 broken.
- Rule 6 was compared by script against the expected full text and matches exactly. Rules 1 to 5 are byte-identical before and after.

The bar: the repo states no build, test, format or CI commands. The worktree root holds only `.claude`, `.scratch`, `CONTEXT.md`, `CONTEXT-MAP.md` and `.gitignore`, with no manifest and no `.github`. This matches `map-implementation-rules.md`'s record, so the bar is its non-command half.

INDEX LINE:    Rule 6 now says a pointer names the heading and, in one clause at most, what the reader goes there for, listing none of its items and stating none of its rules.

FLAGS:         none

NEW NODES:     none

INVALIDATIONS: Extension of [node 253](nodes/253-a-shipped-file-points-at-a-sibling-rather-than-restating-it.md)'s rule and of [node 354](nodes/354-add-the-sixth-standing-rule-for-writing.md)'s landed text of rule 6: the rule gains two sentences on what a pointer may hold. No contradiction: node 361's answer is carried as written, and rule 6's count, number and position are unchanged.

CONDITIONS:    Searched the `## Acceptance condition` and `## Question` sections of every open or claimed node for "rule 6", "sixth", "standing rule(s) for writing", "one clause" and "Point at a heading of another shipped". Matches:
- Nodes 190 and 284: their clauses count the standing rules for writing. This work keeps the count at six, so no clause is made wrong.
- Node 359, claimed: its review text cites "rule 6 with the node 361 ruling". That stays true once this lands, since the ruling becomes part of rule 6. No change.
- Node 368: its condition states the same pointer definition in its own text. It is consistent with this work and not made wrong.
- Nodes 104, 40, 30 and 84: matched on unrelated uses of "sixth" or "one clause".
No replacement clause is written, and no open question changes.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings: none received yet. Paths touched: `.scratch/graph-workflow/map.md` and `.scratch/graph-workflow/map-history.md`, both in the worktree `.scratch/graph-workflow/worktrees/367-rule6`. Nothing is committed. Proposed commit message:

    Rule 6 says what a pointer may hold

    Standing rule for writing 6 in map.md gains two sentences after its
    first: a pointer names the heading and, in one clause at most, what the
    reader goes there for, and lists none of its items and states none of
    its rules. The lead-in names node 361 beside node 253. The replaced
    lead-in and rule 6 are appended verbatim to map-history.md.

    Node: graph-workflow/367

RETROSPECTIVE:
1. What I had to hunt for: the exact heading shape `map-history.md` uses for a supersession from `map.md`'s `## Notes`. I found it by grepping the file's headings and copying node 354's section. I also had to find which checks the `Change the map` procedure makes the changer run (4, 10 and 11), which are in `graph-conventions.md`.
2. What arrived that this node did not need: nearly all of `decisions.md` (about 270 lines). Only the node 253, 354 and 361 lines bore on this work. Most of `map-implementation-rules.md` did not bear on it either (the worktree route, the trigger file, the record-reading rule).
3. What would have made this easier: a pointer in the node or the spawn to the precedent `map-history.md` section to mirror (node 354's). Also a note that clause 4 banks only rule 6, while the lead-in change in clause 3 is also a replaced rule text, so the worker need not decide whether to bank it.
4. What was stale, wrong or contradictory: nothing contradictory. The condition's clause 4 names only rule 6's old text for banking, although clause 3 also replaces the lead-in. I banked both. This adds text and removes none, so clause 4 still holds.
````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-29. The checker was resumed from node 369's check; the condition reached it as a verbatim copy in `$TMPDIR/c367.md`.*

> PASS
>
> Node 367, "Say in rule 6 what a pointer may hold". This is a fresh check, and nothing from earlier nodes carries over. I read only the standards section of `map-implementation-rules.md` ("What the work is held against"). The ground rules and the six standing rules for writing came as text from `/tmp/claude-1000/ground.md`. I read the two changed paths as the work, under that file's rule on record files as work, including `map.md`'s `## Notes` as the spawn directed.
>
> **What moved in a standard, settled first.**
> - The work edits standing rule for writing 6, which is one of the standards.
> - I compared the elements rule 6 requires before and after the change. It gains two sentences, which are new elements, and every earlier element is kept word for word (the Python check under clause 1). So the change is purely additive.
> - Under the contract, I held the work against the unmoved elements. I did not hold it against the two added sentences, which are part of the work and were checked against the acceptance condition instead. Rules 1 to 5 did not move.
>
> **Scope: met.**
> - `git status --porcelain --untracked-files=all` lists only ` M .scratch/graph-workflow/map.md` and ` M .scratch/graph-workflow/map-history.md`.
> - There is no change to a node status line, `decisions.md` or `flags.md`.
>
> **Clause 1: met.**
> - In `map.md`, the rule-6 line sits under `## Notes`: `grep -n '^#' map.md` puts line 75 between `## Notes` (line 22) and `## Decisions so far` (line 79).
> - A Python check split HEAD's `6. **` line after its bold first sentence and inserted the two mandated sentences word for word. The result is identical to the worktree's `6. **` line (`rule6 exact: True`). So the four existing sentences are unchanged, and the new pair comes directly after sentence one.
>
> **Clause 2: met.**
> - For n = 1 to 5, the md5 of `grep "^$n\. \*\*"` is the same at HEAD and in the worktree.
>
> **Clause 3: met.**
> - The lead-in now ends "…the sixth by [node 253](…) and [node 361](nodes/361-whether-a-pointer-that-summarises-its-target-restates-it.md)." The target exists (see clause 5).
>
> **Clause 4: met.**
> - HEAD's old rule-6 line matches exactly one whole line in `map-history.md`: `grep -Fxc -f` returned 1.
> - It sits under `## Superseded from \`map.md\` at node 367 — …` and `### From \`map.md\`'s \`## Notes\` — the sixth standing rule for writing`. That heading mirrors the section the rule came from.
> - HEAD's old lead-in is also banked word for word, under its own subheading (count 1).
> - `git diff --numstat` gives `16 0` for `map-history.md`. There are zero `^-` lines, so the file gains text and loses none.
>
> **Clause 5: met.**
> - From `.scratch/graph-workflow/`, every relative `](…)` target in both files, with its anchor stripped, passes `[ -e ]`. The loop reported nothing missing.
>
> The condition says "The scope came from no search", so there was no recorded command to re-run.
>
> **The bar.**
> - The repo has no build, tests, formatter or CI. Its root holds only `CONTEXT.md` and `CONTEXT-MAP.md`, which agrees with `map-implementation-rules.md`. There were no commands to run.
> - On the non-command half, I held both files' added text against the five ground rules, the unmoved standing rules for writing, `/writing-for-agents`, and the glossary's `_Avoid_` refusals, checked by hand. None found a defect.
>   - Rule 5: no bold was added except the existing heading-style lead-in.
>   - Rule 4: the history file cites by heading.
> - No reviewing skill is named, so I ran none.
>
> QUESTIONS:
> - A possible defect that comes from complying with the condition. The wording and the placement are the condition's own, so they were not the worker's to depart from.
>   - Rule 6's existing second sentence begins with the elliptical "Where the reader is not, …". It used to mean "where the reader is not already told to read that file", with its antecedent at the end of the first sentence.
>   - Clause 1 requires the two new sentences to go directly between them, and requires the existing sentences to stay word for word. So "Where the reader is not" now follows "It lists none of the items that heading holds and states none of its rules". The nearest reading of "is not" becomes unclear, for example "not going there".
>   - Standing rule for writing 5 asks for "one clear referent for each pronoun" and grammatical sentences.
>   - Should the elided clause be restored in that sentence, for example as "Where the reader is not told to read that file, …"? That would amend clause 1's "word for word", which only the condition's owner can decide.
>
> My only writes were scratch files in `$TMPDIR` for the comparisons.

*The manager's note:* the checker handed back a question beside its outcome, so the standing yes does not cover this gate; it goes to the human.

#### The human's answer at the gate, 2026-10-02

The manager put checker run 1's question to the human, recommending one correction: restore the elided words so the sentence reads "Where the reader is not told to read that file, restate what the reader needs…". The alternative offered was to approve as is. The human, `verbatim`: *"ok"*. The manager had said "ok for recommended" would mean that correction. So the gate's outcome is **correct**, and the node goes to correction round 1.

## Handover, attempt 1, correction round 1

*The worker's own text, pasted, 2026-10-02.*

````
HANDOVER:      Say in rule 6 what a pointer may hold (correction round 1)

ANSWER:        Standing rule for writing 6 in `map.md`'s `## Notes` now says what a pointer may hold. Directly after its first sentence it gains two sentences: "A pointer names the heading and says, in one clause at most, what the reader goes there for. It lists none of the items that heading holds and states none of its rules."

Rule 6's existing second sentence now opens "Where the reader is not told to read that file, restate what the reader needs…". The words "told to read that file" were restored by the human's decision at the gate. With the new sentences between them, the shorter "Where the reader is not" no longer pointed back at the first sentence, which goes against rule 5's one clear referent per pronoun. Clause 1 asked for that sentence to be kept word for word, and this is the one departure from it. Rule 6's other three existing sentences are unchanged, and so are rules 1 to 5.

The list's bold lead-in names [node 361](nodes/361-whether-a-pointer-that-summarises-its-target-restates-it.md) beside node 253 as a node that fixed the sixth rule. The replaced lead-in and the old rule 6 are appended verbatim to `map-history.md`, under `## Superseded from `map.md` at node 367 — the sixth standing rule for writing, before it said what a pointer may hold`. That section's italic note now records the second sentence's change too.

INDEX LINE:    Rule 6 now says a pointer names the heading and, in one clause at most, what the reader goes there for, listing none of its items and stating none of its rules.

FLAGS:         none

NEW NODES:     none

INVALIDATIONS: Extension of [node 253](nodes/253-a-shipped-file-points-at-a-sibling-rather-than-restating-it.md)'s rule and of [node 354](nodes/354-add-the-sixth-standing-rule-for-writing.md)'s landed rule 6: two sentences are added, and the second sentence's elided words are restated. The meaning of that sentence is unchanged. No contradiction.

CONDITIONS:    Unchanged from attempt 1. I searched every open or claimed node's acceptance condition and question for "rule 6", "sixth", "standing rule(s) for writing", "one clause", "Point at a heading of another shipped" and "Where the reader is not". No clause is made wrong and no open question changes.

MISSING FROM MAP: none

GATE PAYLOAD:  For the checker's question (the elided "is not" lost its antecedent once the new sentences came before it), and the human's "ok" taking the manager's recommendation:
- In `map.md`, rule 6's second existing sentence now opens "Where the reader is not told to read that file, restate".
- `map-history.md` already held that sentence's old text, inside the old rule 6 banked in attempt 1. Nothing new was banked.
- In `map-history.md`, the italic note of this node's own appended section, written in attempt 1 and not yet committed, was corrected. It said rule 6's four existing sentences were unchanged, and it now names the second sentence's change and that the human made it at the gate.
- The pre-change `map-history.md` is still a byte-exact prefix of the new one, so check 11 holds.
- This touches clause 1: the one departure from "word for word" was decided by the human. No other clause is affected.

Paths touched, in the worktree `.scratch/graph-workflow/worktrees/367-rule6`: `.scratch/graph-workflow/map.md` and `.scratch/graph-workflow/map-history.md`. Nothing is committed.

Proposed commit message:

    Rule 6 says what a pointer may hold

    Standing rule for writing 6 in map.md gains two sentences after its
    first: a pointer names the heading and, in one clause at most, what the
    reader goes there for, and lists none of its items and states none of
    its rules. Its second sentence's elided "told to read that file" is
    restored so it keeps its referent. The lead-in names node 361 beside
    node 253. The replaced lead-in and rule 6 are appended verbatim to
    map-history.md.

    Node: graph-workflow/367
````

### Checker run 2 — `PASS`

*The checker's own text, pasted, 2026-10-02, after correction round 1. The same checker, resumed within this node.*

> PASS
>
> This is a re-check of node 367, "Say in rule 6 what a pointer may hold", after correction round 1. I held it against `/tmp/claude-1000/c367.md` under the human's gate decision as the manager relayed it. That decision removes "word for word" for rule 6's second existing sentence only, so that its opening "Where the reader is not, restate" becomes "Where the reader is not told to read that file, restate". "Word for word" still binds every other part of clause 1.
> - I read only the standards section of `map-implementation-rules.md`.
> - The ground rules and the six standing rules for writing came as text from `/tmp/claude-1000/ground.md`.
> - I read the two changed paths as the work, under that file's rule on record files as work.
>
> **What changed since the last check.**
> - The worker's handover names two changes: rule 6's second sentence, and the italic note in `map-history.md`.
> - I re-ran every clause check against the tree rather than relying on that statement.
> - Base `a19c84f` is unchanged.
> - `git diff --numstat` is still `16 0` for `map-history.md` and `2 2` for `map.md`.
> - The only change the tree shows beyond the two the handover names is none.
> - The bar was re-run in full.
>
> **Settled first: rule 6 is a standard, and this work moves it.**
> - Rule 6 gains two sentences, which are new elements.
> - One existing sentence moves under the human's decision: "the reader is not told to read that file" says out loud what the old wording left implied, and requires nothing new.
> - Every other element of rule 6, and all of rules 1 to 5, is unmoved. I held the work against those and not against the added sentences.
>
> **Scope: met.**
> - `git status --porcelain --untracked-files=all` lists only ` M .scratch/graph-workflow/map.md` and ` M .scratch/graph-workflow/map-history.md`.
> - There is no change to a node status line, `decisions.md` or `flags.md`.
>
> **Clause 1, as the decision reads it: met.**
> - A Python check built the expected line from three pieces:
>   - HEAD's rule-6 line;
>   - the two mandated sentences, inserted word for word directly after its first sentence;
>   - the single substitution "Where the reader is not, restate" → "Where the reader is not told to read that file, restate".
> - The result equals the worktree's `6. **` line exactly (`True`). So sentences 1, 3 and 4 are unchanged, and sentence 2 differs only by the decided words.
> - The line is under `## Notes`, between `## Notes` (line 22) and `## Decisions so far` (line 79).
>
> **Clause 2: met.**
> - For n = 1 to 5, the md5 of `grep "^$n\. \*\*" map.md` is identical at HEAD and in the worktree.
>
> **Clause 3: met.**
> - The lead-in still names `[node 361](nodes/361-whether-a-pointer-that-summarises-its-target-restates-it.md)` beside node 253 as a node that shaped the sixth rule. `grep -c 'node 361' map.md` returns 1.
>
> **Clause 4: met.**
> - HEAD's rule-6 line matches one whole line in `map-history.md` (`grep -Fxc -f`, count 1), under the node-367 `## Superseded from \`map.md\` …` heading with its `### From \`map.md\`'s \`## Notes\` — the sixth standing rule for writing` subheading.
> - HEAD's lead-in is banked word for word too (count 1).
> - The diff has 0 `^-` lines, so the file gains text and loses none.
> - The rewritten italic note states the second-sentence change and attributes it to the human's gate decision. It is added text only.
> - Nothing more had to be banked: HEAD's full rule 6, including the old second sentence, is already appended.
>
> **Clause 5: met.**
> - From `.scratch/graph-workflow/`, every relative `](…)` target in both files, with its anchor stripped, passes `[ -e ]`. The loop reported nothing missing.
>
> **The bar.**
> - The repo has no build, tests, formatter or CI, so there were no commands to run.
> - I held the added text in both files against the five ground rules, the unmoved standing rules for writing, `/writing-for-agents`, and the glossary's `_Avoid_` refusals, checked by hand. None found a defect.
> - Rule 5's one-referent concern from last round is gone now that the clause names what the reader is not told.
> - The only bold spans on added lines are the existing lead-in and rule 6's first sentence, plus their banked copies. The work introduces no new bold.
> - No reviewing skill is named, so I ran none.
>
> My only writes were scratch files in `$TMPDIR` for the comparisons.

### Gate — approve, `standing yes`, 2026-10-02

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 2 outcome, `PASS`. No exclusion applies: run 2 handed back no question and no raise, and left no part of the condition uncovered. Run 1's question was settled by the human at the gate above. The node raised no flags.
