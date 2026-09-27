# Carry the node closing report term into `expedition-standing-yes`

Type: implementation
Status: resolved
Blocked by: ~~137~~

## Question

`.claude/skills/expedition-standing-yes/SKILL.md` still says `pick report`, which node 137 retired in favour of "node closing report". Carry the term into that file.

*Reported by [node 137](137-rename-the-two-reports-and-repair-the-avoid-line.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Acceptance condition

*Authored by node 137's worker and filed by the manager.*

> The one file, and no others: `.claude/skills/expedition-standing-yes/SKILL.md`.
> 1. `grep -n "pick report" .claude/skills/expedition-standing-yes/SKILL.md` returns nothing. At commit `eb3b217` it returned 4 lines: the heading `## Flags, and the pick report` and three in the body of that section ("settle at the pick report that closes the node", "The pick report that closes a node names every item", "as any pick report that closes a node does"). Re-run it; the demand is that it return nothing, whatever the count has become.
> 2. Each occurrence becomes "node closing report". The heading becomes `## Flags, and the node closing report`. Where a sentence said "the pick report that closes the node", the words "that closes the node" may be dropped or kept, as the sentence needs.
> 3. No rule in the file is removed or renumbered, and none changes its meaning.
> 4. The working tree meets the bar.
>
> Every word is fixed by node 137's landed glossary entry and by the file's text at `eb3b217`.

## Amendment, 2026-09-27 (from node 137)

*Written by the manager on the human's "ok for recommended" at [node 137](137-rename-the-two-reports-and-repair-the-avoid-line.md)'s gate, which took the recommendation to fold this defect into this node. The defect was reported by node 137's checker, beside its `PASS`. Every word is fixed by node 137's landed glossary entries (`fe2610b`) and by the file's text at `fe2610b`.*

- **The work's scope.** The one file becomes two: `.claude/skills/expedition-standing-yes/SKILL.md` and `.claude/skills/expedition-cleanup/SKILL.md`.
- **A new clause.** "In `.claude/skills/expedition-cleanup/SKILL.md`, the two bare uses of "closing report" that mean the effort-level report read "effort closing report". At `fe2610b` they are at line 45 ("would drop it from the closing report") and line 61 ("The closing report is built from its lines whose flag is not yet settled"). After the work, `grep -niE 'closing report' .claude/skills/expedition-cleanup/SKILL.md | grep -viE '(node|effort) closing report'` returns nothing."
- **Clause 3** applies to both files.

## Answer

`expedition-standing-yes` now says "node closing report" in place of the retired "pick report", and `expedition-cleanup`'s two bare uses of "closing report" now say "effort closing report".

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `e4beb1d`. Flag 344.1 settles at the node closing report. The two `map.md` bullets the worker named were carried to the new term by the manager, with the old text in `map-history.md`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      Carry the node closing report term into `expedition-standing-yes`
ANSWER:        Both shipped files now use node 137's terms (`fe2610b`, `CONTEXT.md` entries `**Node closing report**:` and `**Effort closing report**:`).
               - `.claude/skills/expedition-standing-yes/SKILL.md`: the heading reads `## Flags, and the node closing report`. All three body uses of "pick report" now read "node closing report". I dropped the words "that closes the node" / "that closes a node" in each place because the term already says it. That left "every item on that node" without an antecedent in its sentence, so it now reads "every item on the node", referring back to the node of the paragraph before. Both paragraphs were rewrapped to the file's 105-column width. No rule was removed or renumbered, and none changed meaning.
               - `.claude/skills/expedition-cleanup/SKILL.md`: the two bare uses of "closing report" meant the effort-level report, so both now read "effort closing report": region cleanup step 3, and the opening sentence of `## Flag cleanup`, rewrapped at 105. The glossary makes the bare form mean the node closing report, which is why these two needed the prefix.
               Verification: `grep -n "pick report" .claude/skills/expedition-standing-yes/SKILL.md` returns nothing. `grep -niE 'closing report' .claude/skills/expedition-cleanup/SKILL.md | grep -viE '(node|effort) closing report'` returns nothing. The only lines over 105 columns in either file are the pre-existing frontmatter `description:` lines.
INDEX LINE:    `expedition-standing-yes` now says "node closing report" in place of the retired "pick report", and `expedition-cleanup`'s two bare uses of "closing report" now say "effort closing report".
FLAGS:         none
NEW NODES:     none
INVALIDATIONS: none among resolved nodes. For the manager, not as an invalidation: two lines of `map.md` that state current rules still say "pick report". These are the standing preference "Approving a node's end settles that node's flags" ("the **pick report** that closes the node", "The pick report awaits no answer", "a gate payload, or a pick report") and the standing-yes preference ("the node's flags settle at the pick report that closes it"). Under the `Change the map` procedure these would be replaced by the current term. That is record work and was not done here.
CONDITIONS:    I searched every open or claimed node file for `expedition-standing-yes/SKILL.md`, `expedition-cleanup/SKILL.md` and `pick report`. Matches other than this node: 317 (in `## Question`/manager's note; the node has no `## Acceptance condition` section) and 32 (in an `## Annotation`; the node has no `## Acceptance condition` section). No acceptance-condition clause matched, so there are no replacements.
MISSING FROM MAP: none
GATE PAYLOAD:  Checker findings: none yet (no checker run received).
               Bar: the repo root holds only `.claude`, `CONTEXT.md`, `.gitignore`, `.scratch`. There is no manifest, no CI, no build, no tests and no formatter, which matches the rules file's record. The non-command half (standards, `_Avoid_` lines, writing rules, the acceptance condition) was applied by hand.
               Paths touched (worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/344-term`, uncommitted):
                 .claude/skills/expedition-standing-yes/SKILL.md
                 .claude/skills/expedition-cleanup/SKILL.md
               Proposed commit message:
                 Carry the node and effort closing report terms into standing-yes and cleanup

                 expedition-standing-yes said "pick report", retired by node 137; it now says
                 "node closing report". expedition-cleanup's two bare "closing report" uses
                 meant the effort-level report and now say "effort closing report".

                 Node: graph-workflow/344

RETROSPECTIVE
1. What you had to hunt for: only the wrap width (measured at 105 with awk) and whether open nodes' conditions named either path (grep over the node files). The glossary terms were exactly where the spawn said.
2. What arrived that this node did not need: nearly all of `map.md` (about 42 KB), which the contract makes me read in full. None of it bore on a two-file term swap. The same goes for most of `map-implementation-rules.md` past the bar paragraph and the writing rules. The spawn's manager notes were all useful.
3. What would have made this easier: nothing much. The node file's condition and amendment were self-contained, with line numbers and verification greps. A contract allowance to skip reading `map.md` whole for a pure terminology node would save the largest cost.
4. What was stale, wrong or contradictory: `map.md`'s standing preferences on flag settlement and on the standing yes still use "pick report", a term the glossary retired at `fe2610b` (see INVALIDATIONS). The rules file's count "five standing rules" and the other items I read were consistent.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 137's check; the condition reached it as a verbatim copy in `$TMPDIR/c344.md`.*

> PASS
>
> This is the check of node 344, "Carry the node closing report term into `expedition-standing-yes`". The work is the uncommitted diff in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/344-term`, on base fe2610b. I read the whole condition, including its amendment from node 137, in `/tmp/claude-1000/c344.md`.
>
> **Parts of the condition:**
>
> - **Scope, as widened by the amendment to two files:** met. `git status --short --untracked-files=all` shows exactly `.claude/skills/expedition-standing-yes/SKILL.md` and `.claude/skills/expedition-cleanup/SKILL.md`. The diff contains nothing under `.scratch/`, and no `decisions.md` or `flags.md`.
> - **Clause 1:** met. I re-ran the recorded search, `grep -n "pick report" .claude/skills/expedition-standing-yes/SKILL.md`. It prints nothing (exit 1). The condition recorded 4 lines at eb3b217, which are the 4 lines the diff changes.
> - **Clause 2:** met.
>   - The heading now reads `## Flags, and the node closing report`.
>   - The three body uses now read "settle at the node closing report" (with "that closes the node" dropped, which the clause allows), "The node closing report names every item on the node…" and "as any node closing report does".
> - **Amendment's new clause:** met.
>   - `.claude/skills/expedition-cleanup/SKILL.md` line 45 now reads "would drop it from the effort closing report".
>   - Line 61 now reads "The effort closing report is built from its lines whose flag is not yet settled."
>   - I ran the clause's own search, `grep -niE 'closing report' .claude/skills/expedition-cleanup/SKILL.md | grep -viE '(node|effort) closing report'`. It prints nothing (exit 1).
> - **Clause 3, applied to both files:** met.
>   - Every changed line only swaps the term, drops "that closes the node", or rewraps. One more wording change: "every item on that node" became "every item on the node", which refers to the same node.
>   - No heading is removed and no numbered step is touched.
> - **Clause 4:** met. See the bar below.
>
> **Whole-tree search:** `grep -rn "pick report" --include=*.md .claude/ CONTEXT.md` prints nothing. `grep -rniE 'closing report' --include=*.md .claude/ | grep -viE '(node|effort|session.s) closing report'` prints nothing either. So no bare or retired use remains in the shipped files.
>
> **The bar:**
> - The repo has no build, tests, formatter or CI, so there are no commands to run.
> - `git diff --check` is clean (exit 0).
> - No added line exceeds the file's wrap width.
>
> **Standards:** as in my earlier checks, I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`.
> - These bore on the work, and I found nothing against any of them:
>   - `CONTEXT.md` `_Avoid_` lines. The new terms are the glossary's own.
>   - The writing rules.
>   - `/writing-for-agents`.
>   - The ground rules.
> - `/coding-principles` and `/naming` did not bear on the work.
> - No reviewing skill is named, so I ran none.
>
> NOT COVERED:
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The condition does not demand this; the rules file makes it a bookkeeping rule. The worktree diff contains no such write, and what the main tree's record holds is outside what I was given.

### Gate — approve, `standing yes`, 2026-09-27

Taken under the standing yes recorded in `map.md`'s `## Notes` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and its one NOT COVERED item is the worker's bookkeeping. This settles none of the node's flags; they settle at the node closing report.

## Flags

`344.1` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above.* The cleanup skill's two bare uses of "closing report" were folded into this node on the human's "ok for recommended", widening its one-file scope to two.

*The manager's note, 2026-09-27:* flag 344.1 settles at the node closing report that closes this node, which names its gate as taken under the standing yes.
