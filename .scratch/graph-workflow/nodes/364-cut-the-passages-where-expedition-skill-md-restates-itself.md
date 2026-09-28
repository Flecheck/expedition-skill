# Cut the passages where `expedition/SKILL.md` restates itself

Type: implementation
Status: claimed
Blocked by: none

## Question

Can the passages of `.claude/skills/expedition/SKILL.md` that restate a rule the same file states at another heading be cut or turned into pointers to that heading, without losing a rule?

*Reported by [node 362](362-where-expedition-skill-md-restates-itself.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Acceptance condition

*Authored by node 362's worker and filed by the manager.*

> Scope: the scope came from no search command. The places are a bounding set: node 362's worker read `.claude/skills/expedition/SKILL.md` in full and listed the passages below from that reading. If you find another passage of that file that restates a rule the same file states elsewhere, report it and do not edit it.
>
> All clauses concern `.claude/skills/expedition/SKILL.md`.
>
> 1. `## The gate`: the paragraph beginning "A gate that a standing yes covers" is removed. The last paragraph of `## What is in front of the human, and when`, beginning "An item that a standing yes covers", stays and still names the skill `expedition-standing-yes`.
> 2. `## The order you act in`, item 5, the bullet beginning "Nothing is waiting when there is": it no longer lists the four kinds (gate assembled and unsent, worker blocked on a raise, the manager's own raise, relayed question). It says instead that nothing is waiting when the pending queue under `## What is in front of the human, and when` holds nothing. It still requires saying which of the queue's kinds were checked, and it still says that a gate whose check will not pass is still waiting. `.claude/rules/expedition-triggers.md` is not changed.
> 3. `## The order you act in`, the paragraph after the numbered list: the sentence beginning "So make the last line of what you send" is removed or replaced by a sentence naming `### The last line of a report`. The sentence beginning "A turn that ends with the human idle" stays.
> 4. `## Words used exactly`, the bullet beginning "You own the map.": it no longer states where the ground rules and the standing steering live, and names `### Standing steering, and standing instructions of one effort` for that. Its sentences about where the map records the bar's commands, and about confirming that record against the repo, stay.
> 5. `## What is in front of the human, and when`, the paragraph beginning "A gate waits in arrival order": it no longer restates that a gate is sent after every older thing in tier 1, which the sentence "Within a tier, take things in the order they arrived." already states. It still states that a gate keeps its place in arrival order although it holds a code slot while it waits, and that the manager never moves a gate ahead on its own judgement.
> 6. `## What is in front of the human, and when`: the section states only once that tier 1's membership is fixed and that only the human can add a kind to it. The sentence "Tier 1 keeps its three kinds." is removed. The paragraph beginning "A checker's question never enters the queue" still states that a checker's question never enters the queue and travels inside the gate payload.
> 7. `## What is in front of the human, and when`, the bullet beginning "Settling a flag.": it no longer states when a flag settles. For that it names `## Flags`.
> 8. `### Picking the next node`: the sentence "Those flags settle at the node closing report, so a flag it leaves out is settled without the human seeing it." is removed. The sentence stating that a node closing report carries every flag the node holds, in the fuller form under `### A flag in a payload`, stays.
> 9. `### A flag in a payload`: the sentence "A gate taken under a standing yes settles no flag." is removed. `## Flags` still states that a gate taken under a standing yes is not put to the human and that its node's flags settle at its node closing report.
> 10. `### Standing steering, and standing instructions of one effort`: the section states each of the following once. A standing rule binds an effort only once it is written into that effort's map, and it is written there when the human states it. The next effort starts without it. A rule reaches a shipped skill file only on the human's word, as a node, and never on the manager's own judgement, even where the manager judges the rule to be about the workflow rather than about the effort. Where the human says nothing about a rule's scope, the rule is the effort's alone. The paragraph beginning "The map is a rule's ordinary home" no longer exists as a separate restatement. The section's two bullets, its statement that a standing instruction is recorded as the human's in their words and never presented as a rule of the workflow, and its paragraph beginning "Every worker on an effort is bound" stay.
> 11. `## When an agent dies or is stopped`: the section says only once that whether a resume is possible is found by attempting it and never predicted. The paragraph beginning "Where an attempt's agent carries the mark of a stop from the human's side" no longer restates that such an attempt is not replaced without the human's answer. It still says to keep the node claimed and not to retry the resume, and it still gives the one question with what it names, what would be lost, and its two choices.
> 12. The rule that an attempt recorded as a final stop is never resumed is stated once in the file: either in `## Stopping a running worker` item 5 or in the first paragraph of `## When an agent dies or is stopped`.
> 13. `### Picking the next node`: the sentence "An implementation node is startable when its acceptance condition can be written in full, with nothing in it waiting on an open question." is removed. `### Where you cannot write one in full` still states that the node is not claimed until the condition is complete.
> 14. `### Changing one after it is written`: the sentence "The worker holding the node works to meet the condition as written, and never rewrites it." is removed. The sentence stating that a condition a worker already holds is handed over as written stays.
> 15. For each passage changed under clauses 1 to 14, every statement it no longer holds is still stated at the heading or passage the clause names. No rule is lost.
> 16. These passages are not changed: the bullet of `## Words used exactly` beginning "A dead attempt is resumed", and the paragraph of `## Flags` beginning "Flags reach the effort closing report".
> 17. No heading in `.claude/skills/expedition/SKILL.md` is renamed, added or removed. Every heading a changed passage names exists in the file with exactly the named text.
> 18. No file other than `.claude/skills/expedition/SKILL.md` changes.

*The worker's note for the manager, pasted:* "open node 89 also changes `.claude/skills/expedition/SKILL.md`, and open node 359 cites its headings (this node renames none). Check for overlapping edits before you fill a slot."

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-28. The worker's own text, pasted.*

````
HANDOVER:      Cut the passages where `expedition/SKILL.md` restates itself

ANSWER:

## Answer

`.claude/skills/expedition/SKILL.md` no longer holds the fourteen passages where it restated itself. It went from 9,409 words to 9,070 (`wc -w`), which cuts 339 words. No heading was renamed, added or removed: I diffed the `^#` lines against `HEAD` and they are identical. Every heading a changed passage now names exists with that exact text. No other file changed. Every quoted opening in the condition still matched the file at `53c4be7`, which is byte-identical to master.

Per clause:

1. `## The gate`: the standing-yes paragraph is removed. The standing-yes paragraph at the end of `## What is in front of the human, and when` is untouched.
2. Item 5, second bullet, now reads: "Nothing is waiting when the pending queue under `## What is in front of the human, and when` holds nothing. Say which of its kinds you checked. A gate whose check will not pass is still waiting." I also dropped the claim that all four kinds are "fixed". The queue section fixes only tier 1, so keeping the word would have added a fresh restatement.
3. The "So make the last line…" sentence became "End what you send as `### The last line of a report` says." The "A turn that ends with the human idle" sentence stays.
4. The "You own the map." bullet now names `### Standing steering, and standing instructions of one effort` for which of the human's rules and steering the map holds. Its two sentences on the bar's commands stay. This also removes the old "nowhere else", which contradicted that section.
5. The arrival-order paragraph is now only "Keep a gate at its place in arrival order even though it holds a code slot while it waits. Never move a gate ahead on your own judgement."
6. The tier 1 fact is stated once, where the list is introduced: "Tier 1 holds exactly three kinds of thing. Its membership is fixed, and only the human can add a kind to it:". Two sentences are removed: "Only the human can add a fourth kind to tier 1. Never infer one yourself." and "Tier 1 keeps its three kinds.". The checker-question paragraph keeps "never enters the queue" and "travels inside the gate payload, so it needs no place in tier 1."
7. The "Settling a flag." bullet now reads "Settling a flag. `## Flags` says when it happens."
8. and 9. The two flag-settling sentences are removed. `## Flags` still holds the standing-yes case.
10. `### Standing steering…`: the "ordinary home" paragraph is gone. Also removed from the binding paragraph: "Until it is there, it binds nobody." and "This holds for rules of conduct…". Both repeat that paragraph's own first sentence, whose "whether about what to work on or about how work is done" already covers conduct. The shipped-file paragraph is folded into: "A rule reaches a shipped skill file only on the human's word, and it does so as a node. Never carry one there on your own judgement, even where you judge the rule to be about the workflow rather than about the effort." The scope-silence sentence follows it. "The next effort starts without it." now appears once, in the standing-instruction paragraph. The bullets, the "record it as theirs" sentence and the "Every worker on an effort is bound" paragraph stay.
11. `## When an agent dies or is stopped`: "so test whether a resume is possible, and never predict it" is removed, and "A failed resume starts no agent and costs nothing." stays as the reason. The human-side-stop paragraph drops "do not replace the attempt on your own". It keeps "do not retry the resume", keeping the node claimed, and the one question with its two choices.
12. The final-stop rule now lives only in `## Stopping a running worker` item 5, which is unchanged. I removed "An attempt recorded as a final stop is never resumed." from the first paragraph of `## When an agent dies or is stopped`.
13. and 14. The two sentences are removed. `### Where you cannot write one in full` and "its condition is handed over as written" stay.
16. The dead-attempt bullet and "Flags reach the effort closing report" are unchanged.

Every edited paragraph is rewrapped to the file's 105-column width.

`.claude/rules/expedition-triggers.md` is not changed, because clause 2 forbids it. The map's rules file asks whoever edits the governing statement of the priority to edit that file in the same edit, or say why not. The reason is that the rule itself did not change. The bullet now points at the queue instead of listing its four kinds, and the triggers file's copy of the four kinds still matches the queue section.

INDEX LINE:    `expedition/SKILL.md` cut fourteen self-restatements (339 words, 9,409 to 9,070) into pointers or single statements, headings unchanged, triggers file untouched by condition.

FLAGS:
ASSUMPTION: In clause 10 I also cut two sentences the condition does not name, "Until it is there, it binds nobody." and "This holds for rules of conduct as well as for steering about what gets worked." Both sit in the section clause 10 says must state each thing once, and both restate that same paragraph's first sentence. In clause 2 I dropped the word "fixed" for all four queue kinds, because `## What is in front of the human, and when` fixes only tier 1. In clause 6 I dropped "Never infer one yourself" as covered by "only the human can add a kind to it". I left the rest of the checker-question paragraph ("so it needs no place in tier 1") as it was, since the condition asks only for "Tier 1 keeps its three kinds." to go. I did all this work alone, with no exchange with the human.
Index: node 364's worker also cut two self-restating sentences inside clause 10's section and one "Never infer" sentence in the tier 1 passage, which the condition did not name but whose sections it required to say each rule once.

NEW NODES:     none

INVALIDATIONS: none. No resolved node's answer is contradicted. Node 362's answer measured these passages, and this work carries out its Tier 1 list minus item 4, which is held for node 360.

CONDITIONS:    I searched the `## Acceptance condition` and `## Question` sections of every open or claimed node except 364 for each removed phrase: "Tier 1 keeps", "final stop", "settles no flag", "ordinary home", "nowhere else", "startable when", "never rewrites", "never predict", "every older thing", "fourth kind", "Never infer", "moment that already exists", "last line of what you send", "fixed membership", "binds nobody", "A gate that a standing yes covers", "Nothing is waiting when", "You own the map", "A gate waits in arrival order", "Settling a flag", "rules of conduct", "do not replace the attempt on". I also searched for the path `expedition/SKILL.md`. Findings:
- Node 359's clause 6 names `## Flags` in SKILL.md for the standing-yes flag rule. That heading and its sentence still exist, so no change is needed.
- Node 359's clause 2 names `## When an agent dies or is stopped`, which still exists and still holds the replacement rules.
- Node 157 matched "never rewrites" in a different rule, hard rule 3's "never rewrites history". It is not affected.
- Node 317 concerns `## Flags`' "Flags reach the effort closing report" and `## Closing an effort`, both unchanged.
- Node 89 requires the existing headings to remain. They do.
- Node 34 cites `SKILL.md:830` by line number. Lines have shifted by about 20, but that is a manager's note, not a condition clause.
No replacement clauses. No open node's question is changed.

MISSING FROM MAP: none

GATE PAYLOAD:
- Checker findings: none yet (no checker has run).
- Paths touched: `.claude/skills/expedition/SKILL.md` (in worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/364-self-restate`, branch `worktree-364-self-restate`, uncommitted).
- The bar: I confirmed against the repo that there is still no manifest, build, tests, formatter or CI (the root holds only `.claude`, `CONTEXT.md`, `CONTEXT-MAP.md`, `.gitignore`, `.scratch`). This matches the rules file. The bar is its non-command half: the glossary's `_Avoid_` lines, where the only hit is "queue", which is refused only for the frontier, while "pending queue" is this file's own term; the ground rules and the rules for writing; and the wrap width, with no prose line over 105 columns. No method skill was invoked, so nothing was skipped.
- Proposed commit message:
  ```
  Cut the passages where expedition/SKILL.md restates itself

  Fourteen passages that restated a rule the same file states at another
  heading are removed or turned into pointers to that heading. The file
  goes from 9,409 to 9,070 words; no heading changes.

  Node: graph-workflow/364
  ```

RETROSPECTIVE
1. What I had to hunt for: nothing much. The only real judgement was clause 12, where item 5 says "not to be resumed" in two forms inside the one item. I kept item 5 and cut the sentence in the other section.
2. What arrived that this node did not need: node 362's Tier 2 section and the manager's note about wrap width. Both were cheap. The condition quoted every opening, so the measurement was mostly confirmation.
3. What would have made this easier: the condition could say whether cutting nearby restatements inside a named section is in scope. Clause 10 says "each once", which implies it is, but clause 6's checker paragraph was left ambiguous.
4. What was stale, wrong or contradictory: nothing stale, since every quoted opening matched. One small inaccuracy: the old item 5 bullet called all four queue kinds a "fixed membership", while the queue section fixes only tier 1. The new text no longer claims it. The triggers file's copy still lists the four kinds, which is consistent but now the only enumeration outside the queue section.
````

## Review

### Checker run 1 — `PASS`, with the six rules for writing not covered

*The checker's own text, pasted, 2026-09-28. A fresh checker.*

> PASS
>
> Worktree: /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/364-self-restate (uncommitted, base 53c4be7). I read the one changed path, `.claude/skills/expedition/SKILL.md`, as the work, using `git diff --word-diff=plain`. For every "stated once" or "removed" part below, I counted the phrase in the file after joining its lines, with `tr '\n' ' ' < SKILL.md | grep -o -i '<phrase>' | wc -l`. That count is written below as "count(phrase)=n".
>
> 1. The paragraph "A gate that a standing yes covers" is gone: count=0, and the diff shows it removed from `## The gate`. The last paragraph of `## What is in front of the human, and when` still begins "An item that a standing yes covers" and names `expedition-standing-yes` (read at lines 530-538).
> 2. Item 5's bullet now reads "Nothing is waiting when the pending queue under `## What is in front of the human, and when` holds nothing. Say which of its kinds you checked. A gate whose check will not pass is still waiting." The four kinds are no longer listed (read at lines 83-85). `git status --short` shows `.claude/rules/expedition-triggers.md` unchanged.
> 3. count("So make the last line")=0. The sentence was replaced by "End what you send as `### The last line of a report` says.", and that heading exists. count("A turn that ends with the human idle")=1.
> 4. The bullet "You own the map." now names `### Standing steering, and standing instructions of one effort` and no longer says where the ground rules and steering live. Its sentences about where the map records the bar's commands, and about confirming that record against the repo, are unchanged (lines 31-34).
> 5. count("send a gate after every older")=0. "Keep a gate at its place in arrival order even though it holds a code slot..." and "Never move a gate ahead on your own judgement." remain.
> 6. count("only the human can add")=1, count("fourth kind")=0, count("Never infer one")=0, count("Tier 1 keeps its three kinds")=0. Searched within lines 476-539, "fixed" occurs once. "A checker's question never enters the queue either. It travels inside the gate payload" remains.
> 7. The bullet is now "Settling a flag. `## Flags` says when it happens."
> 8. count("Those flags settle at the node closing report")=0. The sentence that a node closing report carries every flag, "in the fuller form under `### A flag in a payload`", remains.
> 9. count("settles no flag")=0. `## Flags` still says "A gate taken under a standing yes is not put to the human, so that node's flags settle at its node closing report too."
> 10. I read lines 600-620. Each of these occurs once: count("binds an effort only once")=1, "Write it there when the human states it" once, count("The next effort starts without it")=1, count("on the human's word")=1, "Never carry one there on your own judgement, even where you judge the rule to be about the workflow" once, count("the effort's alone")=1. count("ordinary home")=0. The two bullets, the "Record it as theirs, in their words" sentence and the "Every worker on an effort is bound" paragraph all remain.
> 11. count("predict")=0, count("in advance")=1 ("Find out whether a resume is possible by attempting it ... and never decide it in advance"). count("replace the attempt on")=0. The paragraph about the mark of a stop from the human's side still says "do not retry the resume. Keep the node claimed", still gives the one question with what it names and what would be lost, and still offers both choices.
> 12. count("final stop")=1 and count("recorded that way")=1, both only in `## Stopping a running worker` item 5. The sentence was removed from the first paragraph of `## When an agent dies or is stopped`.
> 13. count("An implementation node is startable")=0. `### Where you cannot write one in full` still says "The node is not claimed until the condition is complete."
> 14. count("never rewrites it")=0 and count("handed over as written")=1.
> 15. For each removal I checked that what it said is still stated at the heading or passage its clause names; the evidence is under clauses 1 to 14 above. I judged three removals by reading, since they are not word-for-word matches:
>    - Clause 3: "run item 5's check before you write that nothing is expected of them" is covered by `### The last line of a report` ("Write a line saying nothing is expected of them only when nothing is waiting") together with item 5's own "Before you stop, run a check".
>    - Clause 4: "ground rules ... live in it and nowhere else" is covered by the Standing steering section: "A standing rule the human gives ... about how work is done, binds an effort only once it is written into that effort's map", a rule reaches a shipped file only on the human's word, and otherwise it is the effort's alone. I read the effort's ground rules as standing rules the human gives. That section never uses the term "ground rules".
>    - Clause 6: "Never infer one yourself" is covered by "only the human can add a kind to it".
> 16. No added or removed diff line contains "A dead attempt is resumed" or "Flags reach the effort closing report" (`git diff | grep '^[-+].*\(A dead attempt\|Flags reach\)'` printed nothing).
> 17. I compared the headings of HEAD's version and the worktree's (`diff <(git show HEAD:... | grep '^#') <(grep '^#' SKILL.md)`): they are identical. Every heading a changed passage names exists with exactly that text: `### The last line of a report`, `### Standing steering, and standing instructions of one effort`, `## Flags`, `## What is in front of the human, and when`.
> 18. `git status --short --untracked-files=all` lists only ` M .claude/skills/expedition/SKILL.md`.
>
> The condition records no search command ("the scope came from no search command"), so there was nothing to re-run. I did not sweep the file for other passages that restate themselves; the condition's leftover-cases clause does not ask the checker to.
>
> Bar: `map-implementation-rules.md` records that this repo has no build, no tests, no formatter and no CI. The repo agrees: it has no manifest or task runner. So I ran no build, test or formatter command, and the bar is its non-command half.
> - `git diff --check` printed nothing.
> - No changed line is longer than the file's usual wrap. The only lines over 106 characters are lines 3 and 54-58, which the diff does not touch; HEAD's version also has 5 such lines, with the same maximum of 248.
> - Standards: from `.scratch/graph-workflow/map-implementation-rules.md` I read only the standards it states. Those are: `/coding-principles` and `/naming`, `glossary.md`'s `_Avoid_` lines, the ground rules, the six standing rules for writing, `graph-conventions.md`, `/writing-for-agents`, and the rule that `.claude/rules/expedition-triggers.md` is co-edited with the governing statement.
>   - Bore on this work: `/writing-for-agents`, which I ran in my own context with no agent spawned. The change removes duplication and adds cross-references, which is its "single source of truth" pruning; no finding.
>   - Also bore on it: ground rules 3 and 4, both met, and the co-edit rule. Clause 2 forbids changing the trigger file. The trigger file's four-kind list still describes the queue correctly, so I found no defect.
>   - Glossary `_Avoid_` lines: the edits add no new terms. The only new wording is "its kinds", "holds nothing", "says when it happens" and "on the human's word".
>   - `/coding-principles`, `/naming` and `graph-conventions.md`: nothing in a prose deletion touches them.
>   - No reviewing skill is named for this repo, and I ran none.
> - I read the changed path as the work under the rules file's rule for work that is the effort's own record. The work is a shipped file, not a record file, and it touches no status line, `decisions.md` or `flags.md`.
>
> NOT COVERED:
> - The six standing rules for writing. Your spawn told me to read them from the ground-rules block of the worktree's `map.md`. My contract (`expedition-checker/SKILL.md`, "What you are given", item 5) says the map is not read, and says map content reaches me only as words in the spawn. `map-implementation-rules.md` also says a checker "receives as text in its spawn" these six rules. I did not open `map.md`, and this outcome does not cover the work against those six rules. To close this, re-spawn with the six rules pasted as text; only that part needs re-checking.

*The manager's note:* the gap was the manager's: its spawn pointed the checker at `map.md`, which the checker contract forbids. The manager pasted the block as text and resumed the checker for that part.

### Checker run 1, completed — `FAIL` (the bar)

> FAIL: the bar
>
> Node 336, "Carry the rules on what reaches the human, the code-slot count and the gate's pointer to the work into the manager contract". The work is `git -C /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/336-m1 diff`, uncommitted on 5acd220. Following the rule in map-implementation-rules.md, I read the changed paths, including the two `.scratch/` record files, as the work under check. The acceptance condition is met in every part I could establish. The one failure is against a standard.
>
> ### Finding 1 (the bar: graph-conventions.md `### Change the map`, step 2, and writing rule 2)
>
> - **Instances:** The work replaced the gate-payload sentence in `.scratch/graph-workflow/map-manager-only.md` under `## Landing an implementation node's work`. The new sentence starts "**The gate payload names the worktree's path**" and cites no node that shaped the change: neither node 231 nor node 336. The paragraph's existing citations are nodes 11 and 68, and they predate the change. The `### Change the map` procedure in `.claude/skills/expedition/graph-conventions.md` says step 2 must "replace the item with its new current statement, citing by markdown link the nodes that shaped it". Writing rule 2 in map-implementation-rules.md says the same: "An item states its current form and cites the nodes that shaped it." Only the new `map-history.md` entry links nodes 231 and 336. The same file has precedent: nodes 265 and 277 are linked there for their own changes. Found by `grep -o 'nodes/2[0-9][0-9]-[a-z-]*\.md' .scratch/graph-workflow/map-manager-only.md | sort -u`, which returns 265, 277, 289 and 290, with no 231 and no 336.
> - **Form:** a map-file item this work replaced under `Change the map`, whose new statement carries no markdown link to the node or nodes that shaped the replacement.
> - **Extent:** `git -C <worktree> diff .scratch/graph-workflow/map-manager-only.md | grep '^+' | grep -cE 'nodes/(231|336)-'`. It prints 0 now, and the diff has exactly one `+` line. Clause 17 allows the fix inside the replaced sentence, because it requires the rest of the sentence to keep its meaning and adding a citation leaves it unchanged. A citation added outside that sentence would breach "Nothing else in that file changes".
>
> ### Acceptance condition: all met, apart from the part under NOT COVERED
>
> - **Scope:** met. `git status --short` shows exactly SKILL.md, map-manager-only.md and map-history.md. The diff contains no node file, no decisions.md and no flags.md, so the rules file's bookkeeping rule is not triggered. SKILL.md is edited plainly: superseded wording is removed and nothing is struck through.
> - **Searches:** for the searches below, I unwrapped SKILL.md into unbroken paragraphs with an awk command and ran `grep -noiE` over the result.
> - **1:** met. `## What is in front of the human, and when` now opens "At most one thing awaiting the human's reply … exactly one whenever something is waiting. Nothing displaces a live question or any other live thing." It adds that a payload carrying several of one worker's questions counts as one thing.
> - **2:** met. The phrases "exactly one question" and "one question in front" are gone from that section. The one remaining hit, "the one question in front of the human", sits in the table under `## What is never yours`, in a scope rule outside this section and unchanged.
> - **3:** met. The section says "Never combine questions from different nodes into one payload, and never divide one payload's reply between two workers", and the one-worker sentence follows.
> - **4:** met. The line rule is kept, with the added reason "A thing named in that line but not asked cannot be answered by accident." A grep for `attributab` finds nothing.
> - **5, 6:** met. The channel paragraph gives all three consequences as bullets. The next line reads "Send the human a question that is already waiting. Never make one up …"
> - **7, 8, 9:** met. A new `### The last line of a report` covers the last line and its reason, that the line is short, "in whatever words fit the case", that it holds "at the moment you write it" and promises nothing, and the only-when-nothing-is-waiting rule. It ends "added to whatever else … and replaces none of it." Every `-` line in the diff falls under clauses 1–16 or the amendment.
> - **10:** met. The code-slot bullet covers the trade, that the human sets the number, the two things the manager never does, and naming the trade when the count moves.
> - **11:** met. The item is removed along with its two sentences, and the list now runs 1–7 with no gap, which I read directly. Item 1, "What must your report to the human contain?", still stands.
> - **12:** met. A new paragraph under `### Picking the next node` says "Every worker reads a consistent snapshot … reconciled when the work is integrated, not while they are read."
> - **13:** met. `\b(git|branch|worktree|rebase|merge)\b` finds nothing in SKILL.md.
> - **14:** met, because there is nothing to disagree. `nothing here settles|[0-9]+ (items|questions)|(six|seven|eight) (items|questions)` finds no item count, and the section heading is the only hit.
> - **15, 16:** met. The payload bullet now reads "Where the work is: the path of the working tree that holds it. A gate that describes a change and points at nothing has not been presented." The table cell reads "say where the work is". `command` gets three hits, all about the bar's commands, and none asks for a diff command. "Keep two things out of the payload: the diff, and the acceptance condition." is present once.
> - **17:** met. `git diff --word-diff` on map-manager-only.md shows the only change as `[-path and the command that shows its diff**,-]{+path**,+}`. The ground is unchanged and no other line differs.
> - **18:** met. The removed sentence, extracted from HEAD with `grep -o`, is found verbatim in the new map-history.md (`grep -cF` prints 1). The HEAD content is a byte-exact prefix of the new file (`head -c N | cmp` passes), so the file gained text and lost none. The heading reads "### From *Landing an implementation node's work* — the gate payload's sentence", under a `## Superseded from map-manager-only.md at node 336` heading in the file's existing style. The sentence has no struck-through text.
> - **19, 20, 21:** met. The tier text, the "Three things never enter the queue:" list and all of `## The order you act in` are unchanged: no diff hunk touches them. "Nothing displaces a live question" is kept inside a widened sentence.
> - **22:** met. Comparing the old and new heading lists shows one addition, `### The last line of a report`, and no removal.
> - **Amendment:** met. The bullet now reads "A handover has seven parts every time" and lists all seven, with the `INVALIDATIONS`, `CONDITIONS` and `MISSING FROM MAP` names, plus "an eighth, the gate payload". The parts match the handover labels in the worker contracts: ANSWER, INDEX LINE, FLAGS, NEW NODES, INVALIDATIONS, CONDITIONS and MISSING FROM MAP. No other count of five or six parts remains.
> - **23:** fails, per Finding 1.
>
> ### The bar
>
> The repo has no build, tests, formatter or CI, so there were no commands to run.
> - `git diff --check`: clean, exit 0.
> - `awk 'length>105'` on SKILL.md: hits only lines 3 (frontmatter) and 52–56 (table rows). None of those lines is in the diff; the table row the work changed is short.
>
> ### Standards
>
> I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md` and opened no other file in the effort's directory apart from the two changed paths handed to me as the work.
> - **Bore on the work:**
>   - graph-conventions.md `### Change the map`: breached, Finding 1.
>   - The five writing rules. Rule 2 is breached, Finding 1. Rule 5 holds: each added prohibition stands beside its positive.
>   - `CONTEXT.md` `_Avoid_` lines: checked by hand on the added text, nothing found.
>   - The ground rules: nothing in SKILL.md assumes a repo or a toolchain, and nothing directs an agent to the human.
>   - `/writing-for-agents`: read, nothing found beyond the above.
>   - The record-file rule: applied.
> - **Did not bear on the work:** `/coding-principles` (the work has no code). `/naming` bore only on the new heading, and I found nothing.
> - No reviewing skill is named, so I ran none. The work changes no standard I hold it against.
>
> The condition says its scope came from no search, so there was no command to re-run.
>
> NOT COVERED:
> - "The worker does not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`." The worktree diff contains no such write. What the main tree's record holds is outside what I was given.

*The manager's note:* an unmet bar goes back to the worker. The manager resumes it with this finding.

### Checker run 2 — `PASS`

*The checker's own text, pasted, 2026-09-28, after correction round 1.*

> PASS
>
> This is a re-check after one correction round. Worktree: /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/364-self-restate. The only changed path is `.claude/skills/expedition/SKILL.md`, which I read as the work.
>
> What changed since my last outcome:
> - I re-listed the added words with `git diff -U0 --word-diff=plain | grep -o '{+[^}]*+}'`. The list is the same as last round except for one piece: `{+steering it holds.+}` is now `{+steering the map holds.+}`.
> - `git diff --stat` is unchanged: 1 file, 32 insertions, 55 deletions.
> - I found no change beyond the one your statement names.
> - I re-ran the bar in full, re-checked the parts of the condition the change touches, and re-ran every clause's phrase search anyway.
>
> Acceptance condition (phrase counts are over the file with its lines joined, `tr '\n' ' ' | grep -o -i '<phrase>' | wc -l`):
> 1. "A gate that a standing yes covers" occurs 0 times. `expedition-standing-yes` is still named in the last paragraph of `## What is in front of the human, and when`.
> 2. Item 5's bullet reads "Nothing is waiting when the pending queue under `## What is in front of the human, and when` holds nothing. Say which of its kinds you checked. A gate whose check will not pass is still waiting." `.claude/rules/expedition-triggers.md` is unchanged, per `git status --short --untracked-files=all`.
> 3. "So make the last line" occurs 0 times. It is replaced by "End what you send as `### The last line of a report` says." "A turn that ends with the human idle" occurs 1 time.
> 4. The bullet now reads "You own the map. `### Standing steering, and standing instructions of one effort` says which of the human's rules and steering the map holds." It no longer says where the rules live, and it names that heading instead. The sentences about the bar's commands and about confirming them against the repo stay (`sed -n '30,34p'`).
> 5. "send a gate after every older" occurs 0 times. The sentences about a gate keeping its arrival-order place and never being moved ahead on your own judgement stay.
> 6. "only the human can add" occurs 1 time. "Never infer one" and "Tier 1 keeps its three kinds" each occur 0 times. The paragraph about a checker's question travelling inside the gate payload stays.
> 7. The bullet reads "Settling a flag. `## Flags` says when it happens."
> 8. "Those flags settle at the node closing report" occurs 0 times. The sentence that the node closing report carries every flag in the fuller form stays.
> 9. "settles no flag" occurs 0 times. "not put to the human, so that node" occurs 1 time, in `## Flags`.
> 10. Each of these occurs exactly once: "binds an effort only once", "The next effort starts without it", "on the human's word", "the effort's alone". "ordinary home" occurs 0 times. The section's two bullets, its "Record it as theirs" sentence and its "Every worker on an effort is bound" paragraph stay.
> 11. "predict" occurs 0 times and "in advance" 1 time. The paragraph about a stop from the human's side keeps "do not retry the resume. Keep the node claimed", the one question, what would be lost, and the two choices.
> 12. "final stop" and "recorded that way" each occur 1 time, both only in `## Stopping a running worker` item 5.
> 13. "An implementation node is startable" occurs 0 times. "is not claimed until the condition is complete" occurs 1 time.
> 14. "never rewrites it" occurs 0 times and "handed over as written" 1 time.
> 15. No rule is lost. The evidence is in clauses 1 to 14 above. The clause-4 bullet now points explicitly at the map, which that section covers: "binds an effort only once it is written into that effort's map".
> 16. "A dead attempt is resumed" and "Flags reach the effort closing report" each occur 1 time. Neither appears on a +/- line of the diff.
> 17. The headings in HEAD's version and in the worktree are identical (`diff <(git show HEAD:... | grep '^#') <(grep '^#' ...)`, which printed HEADINGS_SAME). Every heading a changed passage names exists.
> 18. Only ` M .claude/skills/expedition/SKILL.md` is changed.
>
> The condition records no search command, so there was nothing to re-run.
>
> Bar:
> - The repo has no build, tests, formatter or CI, as `map-implementation-rules.md` records and the repo confirms. So I ran no commands of that kind.
> - `git diff --check` printed nothing.
> - Every line over 106 characters is one of lines 3, 54, 56, 57 and 58. The diff touches none of them, so the corrected line is within the file's wrap.
> - I read only the standards stated in `.scratch/graph-workflow/map-implementation-rules.md`. The ones that bore on this work are `/writing-for-agents`, the ground rules, the six standing rules for writing, and the rule to co-edit the triggers file. For that last rule, clause 2 forbids changing the triggers file, and its four-kind list still describes the queue correctly.
> - Ground rules 1 to 5, as you pasted them: met.
> - Six standing rules for writing:
>   - Rule 5: last round's finding is fixed. The pronoun is replaced by "the map", so the sentence has a single subject and no unclear pronoun. Every other pronoun the work added has one clear referent: "its kinds" is the queue, "when it happens" is settling a flag, "carry one there" is a rule into a shipped skill file, and "add a kind to it" means tier 1 or its membership, which read the same.
>   - Rule 1: no shape was compressed.
>   - Rules 2 and 3: do not apply.
>   - Rule 4: every citation the work added names a heading, and it added no line numbers.
>   - Rule 6: each pointer names a heading in the same file, and no heading was renamed.
> - No reviewing skill is named for this repo, and I ran none.
>
> Nothing is left uncovered.

### Gate — approve, `standing yes`, 2026-09-28

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 2 outcome, `PASS`. No exclusion applies: the run handed back no question and no raise, and left nothing uncovered. This settles none of the node's flags; they settle at the node closing report.

## Handover, attempt 1, correction round 1

*Filed by the manager as handed back, 2026-09-28. The worker's own text, pasted.*

````
HANDOVER:      Cut the passages where `expedition/SKILL.md` restates itself

ANSWER:

## Answer

`.claude/skills/expedition/SKILL.md` no longer holds the fourteen passages where it restated itself. It went from 9,409 words to 9,071 (`wc -w`), which cuts 338 words. No heading was renamed, added or removed: I diffed the `^#` lines against `HEAD` and they are identical. Every heading a changed passage now names exists with that exact text. No other file changed. Every quoted opening in the condition still matched the file at `53c4be7`, which is byte-identical to master.

Per clause:

1. `## The gate`: the standing-yes paragraph is removed. The standing-yes paragraph at the end of `## What is in front of the human, and when` is untouched.
2. Item 5, second bullet, now reads: "Nothing is waiting when the pending queue under `## What is in front of the human, and when` holds nothing. Say which of its kinds you checked. A gate whose check will not pass is still waiting." I also dropped the claim that all four kinds are "fixed". The queue section fixes only tier 1, so keeping the word would have added a fresh restatement.
3. The "So make the last line…" sentence became "End what you send as `### The last line of a report` says." The "A turn that ends with the human idle" sentence stays.
4. The "You own the map." bullet now reads: "You own the map. `### Standing steering, and standing instructions of one effort` says which of the human's rules and steering the map holds." Its two sentences on the bar's commands stay. This also removes the old "nowhere else", which contradicted that section.
5. The arrival-order paragraph is now only "Keep a gate at its place in arrival order even though it holds a code slot while it waits. Never move a gate ahead on your own judgement."
6. The tier 1 fact is stated once, where the list is introduced: "Tier 1 holds exactly three kinds of thing. Its membership is fixed, and only the human can add a kind to it:". Two sentences are removed: "Only the human can add a fourth kind to tier 1. Never infer one yourself." and "Tier 1 keeps its three kinds.". The checker-question paragraph keeps "never enters the queue" and "travels inside the gate payload, so it needs no place in tier 1."
7. The "Settling a flag." bullet now reads "Settling a flag. `## Flags` says when it happens."
8. and 9. The two flag-settling sentences are removed. `## Flags` still holds the standing-yes case.
10. `### Standing steering…`: the "ordinary home" paragraph is gone. Also removed from the binding paragraph: "Until it is there, it binds nobody." and "This holds for rules of conduct…". Both repeat that paragraph's own first sentence, whose "whether about what to work on or about how work is done" already covers conduct. The shipped-file paragraph is folded into: "A rule reaches a shipped skill file only on the human's word, and it does so as a node. Never carry one there on your own judgement, even where you judge the rule to be about the workflow rather than about the effort." The scope-silence sentence follows it. "The next effort starts without it." now appears once, in the standing-instruction paragraph. The bullets, the "record it as theirs" sentence and the "Every worker on an effort is bound" paragraph stay.
11. `## When an agent dies or is stopped`: "so test whether a resume is possible, and never predict it" is removed, and "A failed resume starts no agent and costs nothing." stays as the reason. The human-side-stop paragraph drops "do not replace the attempt on your own". It keeps "do not retry the resume", keeping the node claimed, and the one question with its two choices.
12. The final-stop rule now lives only in `## Stopping a running worker` item 5, which is unchanged. I removed "An attempt recorded as a final stop is never resumed." from the first paragraph of `## When an agent dies or is stopped`.
13. and 14. The two sentences are removed. `### Where you cannot write one in full` and "its condition is handed over as written" stay.
16. The dead-attempt bullet and "Flags reach the effort closing report" are unchanged.

Every edited paragraph is rewrapped to the file's 105-column width.

`.claude/rules/expedition-triggers.md` is not changed, because clause 2 forbids it. The map's rules file asks whoever edits the governing statement of the priority to edit that file in the same edit, or say why not. The reason is that the rule itself did not change. The bullet now points at the queue instead of listing its four kinds, and the triggers file's copy of the four kinds still matches the queue section.

INDEX LINE:    `expedition/SKILL.md` cut fourteen self-restatements (338 words, 9,409 to 9,071) into pointers or single statements, headings unchanged, triggers file untouched by condition.

FLAGS:
ASSUMPTION: In clause 10 I also cut two sentences the condition does not name, "Until it is there, it binds nobody." and "This holds for rules of conduct as well as for steering about what gets worked." Both sit in the section clause 10 says must state each thing once, and both restate that same paragraph's first sentence. In clause 2 I dropped the word "fixed" for all four queue kinds, because `## What is in front of the human, and when` fixes only tier 1. In clause 6 I dropped "Never infer one yourself" as covered by "only the human can add a kind to it". I left the rest of the checker-question paragraph ("so it needs no place in tier 1") as it was, since the condition asks only for "Tier 1 keeps its three kinds." to go. I did all this work alone, with no exchange with the human.
Index: node 364's worker also cut two self-restating sentences inside clause 10's section and one "Never infer" sentence in the tier 1 passage, which the condition did not name but whose sections it required to say each rule once.

NEW NODES:     none

INVALIDATIONS: none. No resolved node's answer is contradicted. Node 362's answer measured these passages, and this work carries out its Tier 1 list minus item 4, which is held for node 360.

CONDITIONS:    I searched the `## Acceptance condition` and `## Question` sections of every open or claimed node except 364 for each removed phrase: "Tier 1 keeps", "final stop", "settles no flag", "ordinary home", "nowhere else", "startable when", "never rewrites", "never predict", "every older thing", "fourth kind", "Never infer", "moment that already exists", "last line of what you send", "fixed membership", "binds nobody", "A gate that a standing yes covers", "Nothing is waiting when", "You own the map", "A gate waits in arrival order", "Settling a flag", "rules of conduct", "do not replace the attempt on". I also searched for the path `expedition/SKILL.md`. Findings:
- Node 359's clause 6 names `## Flags` in SKILL.md for the standing-yes flag rule. That heading and its sentence still exist, so no change is needed.
- Node 359's clause 2 names `## When an agent dies or is stopped`, which still exists and still holds the replacement rules.
- Node 157 matched "never rewrites" in a different rule, hard rule 3's "never rewrites history". It is not affected.
- Node 317 concerns `## Flags`' "Flags reach the effort closing report" and `## Closing an effort`, both unchanged.
- Node 89 requires the existing headings to remain. They do.
- Node 34 cites `SKILL.md:830` by line number. Lines have shifted by about 20, but that is a manager's note, not a condition clause.
No replacement clauses. No open node's question is changed.

MISSING FROM MAP: none

GATE PAYLOAD:
- Checker findings and what changed:
  - Finding 1, the pronoun "it" in the "You own the map." bullet had two possible referents. I replaced "it holds" with "the map holds", so the sentence now reads "`### Standing steering, and standing instructions of one effort` says which of the human's rules and steering the map holds." I re-read the other pronouns the work added: "its kinds" (the pending queue), "when it happens" (settling a flag), and "carry one there" (a rule, a shipped skill file). Each has one referent, so nothing else changed. This round touched a passage clause 4 names. The clause still holds: the bullet names that heading, and it no longer says where the rules live.
- Paths touched: `.claude/skills/expedition/SKILL.md` (in worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/364-self-restate`, branch `worktree-364-self-restate`, uncommitted).
- The bar: I confirmed against the repo that there is still no manifest, build, tests, formatter or CI. This matches the rules file. The bar is its non-command half: the glossary's `_Avoid_` lines, where the only hit is "queue", which is refused only for the frontier, while "pending queue" is this file's term; the ground rules and the rules for writing; and the wrap width, with no prose line over 105 columns, re-checked after this round. No method skill was invoked, so nothing was skipped.
- Proposed commit message:
  ```
  Cut the passages where expedition/SKILL.md restates itself

  Fourteen passages that restated a rule the same file states at another
  heading are removed or turned into pointers to that heading. The file
  goes from 9,409 to 9,071 words; no heading changes.

  Node: graph-workflow/364
  ```

RETROSPECTIVE
1. What I had to hunt for: nothing much. The only real judgement was clause 12, where item 5 says "not to be resumed" in two forms inside the one item. I kept item 5 and cut the sentence in the other section.
2. What arrived that this node did not need: node 362's Tier 2 section and the manager's note about wrap width. Both were cheap.
3. What would have made this easier: the condition could say whether cutting nearby restatements inside a named section is in scope. Also, a habit of re-reading each added pronoun against rule 5 before handing back would have caught this round's finding.
4. What was stale, wrong or contradictory: nothing stale, since every quoted opening matched. One small inaccuracy: the old item 5 bullet called all four queue kinds a "fixed membership", while the queue section fixes only tier 1.
````

## Flags

`364.1` `ASSUMPTION` — In clause 10 I also cut two sentences the condition does not name, "Until it is there, it binds nobody." and "This holds for rules of conduct as well as for steering about what gets worked." Both sit in the section clause 10 says must state each thing once, and both restate that same paragraph's first sentence. In clause 2 I dropped the word "fixed" for all four queue kinds, because `## What is in front of the human, and when` fixes only tier 1. In clause 6 I dropped "Never infer one yourself" as covered by "only the human can add a kind to it". I left the rest of the checker-question paragraph ("so it needs no place in tier 1") as it was, since the condition asks only for "Tier 1 keeps its three kinds." to go. I did all this work alone, with no exchange with the human.
