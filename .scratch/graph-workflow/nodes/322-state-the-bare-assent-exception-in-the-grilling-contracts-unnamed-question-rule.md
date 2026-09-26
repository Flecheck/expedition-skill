# State the bare-assent exception in the grilling contract's unnamed-question rule

Type: implementation
Status: resolved
Blocked by: none

## Question

*Surfaced by [node 316](316-bare-assent-and-an-unnamed-question-have-no-stated-precedence.md)'s worker, and filed by the manager as it wrote it.*

Rewrite the unnamed-question bullet under "What a reply settles" in the grilling contract so that it opens with an exception for a bare assent.

## Acceptance condition

*Written by node 316's worker. Pasted as it wrote it, and not the manager's. The manager removed the handover's indentation only.*

In `.claude/skills/expedition-grilling/SKILL.md`, the list of bullets that follows the sentence "A reply settles what it covers and nothing else, under the following rules." holds a bullet that currently reads, as one sentence run across two lines: "A question the reply does not name stays unanswered, and the human has not deferred it. Put it in a later payload. Never read an unnamed question as assent, and never answer it yourself."
1. That bullet's text is replaced by exactly this text, wrapped across lines the way the neighbouring bullets are wrapped: "Unless the reply is a bare assent as in the rule above, a question the reply does not name stays unanswered, and the human has not deferred it. Put it in a later payload. Never read an unnamed question as assent, and never answer it yourself."
2. The bullet immediately above it is the one that begins "A reply that assents to the recommendation without naming any question", and its text is unchanged. So "the rule above" refers to it.
3. The other bullets of that list, the sentence that introduces it and the order of the bullets are unchanged.
4. No other line of `.claude/skills/expedition-grilling/SKILL.md` changes, and no other file changes.

## Answer

The grilling contract's unnamed-question bullet now opens "Unless the reply is a bare assent as in the rule above", so the precedence of bare assent is stated rather than implied.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The human approved. The work landed as commit `a57f9cd`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      State the bare-assent exception in the grilling contract's unnamed-question rule (node 322)

ANSWER:        In `.claude/skills/expedition-grilling/SKILL.md`, under "What a reply settles", the unnamed-question bullet now opens with an exception for a bare assent. It reads: "Unless the reply is a bare assent as in the rule above, a question the reply does not name stays unanswered, and the human has not deferred it. Put it in a later payload. Never read an unnamed question as assent, and never answer it yourself." The bullet directly above it, which begins "A reply that assents to the recommendation without naming any question", is unchanged, so "the rule above" refers to it. The new text is wrapped greedily at the file's 104-column width, the same width as the neighbouring bullets, with a two-space continuation indent, which gives three lines where there were two. No other line of the file changed, the bullets are in the same order, and no other file changed. This carries out node 316's answer.

INDEX LINE:    The grilling contract's unnamed-question bullet now opens "Unless the reply is a bare assent as in the rule above", so the precedence of bare assent is stated rather than implied.

FLAGS:         none

NEW NODES:     none

INVALIDATIONS: none. The change is node 316's answer carried out word for word. It agrees with node 117 §4, with node 126's conditions 4 and 5, and with the text node 291 shipped.

GATE PAYLOAD:  Checker findings: none received yet.
               Paths touched: `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/322-bare-assent-exception/.claude/skills/expedition-grilling/SKILL.md` (repo path `.claude/skills/expedition-grilling/SKILL.md`), uncommitted on branch `worktree-322-bare-assent-exception`.
               The bar: the repo has no build, tests, formatter or CI. I found no manifest or task runner, which matches `map-implementation-rules.md`. So the bar is its non-command half. I checked the new text against the five standing writing rules and the `CONTEXT.md` `_Avoid_` lines, and the glossary refuses no word in the new clause.
               Proposed commit message:
                 State the bare-assent exception in the grilling contract's unnamed-question rule

                 The unnamed-question bullet under "What a reply settles" now opens with
                 "Unless the reply is a bare assent as in the rule above", so a reader no
                 longer has to infer from bullet order that bare assent takes precedence.

                 Node: graph-workflow/322

Method skill: none was invoked, so no part of one was skipped.

RE-POINTING SEARCH:
               Commands, run from the repo root:
               1. `python3 .scratch/graph-workflow/scripts/search-conditions.py 322 de347dc:.claude/skills/expedition-grilling/SKILL.md /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/322-bare-assent-exception/.claude/skills/expedition-grilling/SKILL.md`. It searched 87 conditions and found no GONE line in either report. Every quoted span is KEPT, and every n-gram group reports "0 gone".
               2. `grep -rli "does not name stays unanswered\|unnamed question\|question the reply does not name" .scratch/graph-workflow/nodes/`, filtered by status. The only non-resolved hit is node 322 itself. The other hits (117, 126, 133, 107, 138, 291, 316) are all resolved.
               3. `grep -li "assent\|What a reply settles\|later payload"` over the nodes, keeping those not resolved. Hits: 135 (open), 56 (open), 259 (claimed), 55 (superseded). In 135 and 56 the word is only "the human assented" in prose. Node 259 says only that node 322 edits a different part of the same contract. None of them quotes the changed sentence.
               Result: no open condition quotes text I removed, so I propose no replacement clause and no supersession.

RETROSPECTIVE:
(1) What I had to hunt for. Almost nothing. The one fact I had to work out was what "wrapped the way the neighbouring bullets are wrapped" means as a width. I measured the file's line lengths with awk: the maximum is 104 to 105 columns, apart from three table or long-link lines. I then wrapped the text with Python's textwrap at width 104. Also, the search script's output has no literal "GONE" marker on its data lines, only "KEPT |" lines and "0 gone" counts. A grep for GONE matches only the two section headers, so I had to open the output to confirm it was empty.
(2) What arrived in my context that this node did not need. Most of the implementation contract's parts on correction rounds, replacement attempts and writing conditions for new nodes. Most of `map-implementation-rules.md`, which deals with record-as-work, supersession and history. Node 316's full interview and retrospective, when its `## Answer` plus the acceptance condition were enough, and the condition alone fixes the text. For a node whose condition fixes the text word for word, the spawn could point only at the node file and the bar paragraph of the rules file.
(3) What would have made this node easier. The condition could state a wrap width, such as "wrapped greedily at 104 columns", instead of "the way the neighbouring bullets are wrapped". The search script could print an explicit "no GONE lines" summary, or tag each gone item with GONE, so that a grep for GONE is conclusive.
(4) What I read that was stale, wrong or contradictory. Nothing contradictory. One small point: the spawn says to "read only its GONE lines", but the output has no GONE-tagged data lines when nothing is gone, and only the headers say "GONE". Separately, the new clause uses the term "bare assent", which the contract never defines. "As in the rule above" ties it to the bullet above, so it reads correctly. The condition fixed the text in any case.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-26. The checker was resumed from node 321's check.*

> PASS
>
> Node 322, "State the bare-assent exception in the grilling contract's unnamed-question rule", meets all four parts of its acceptance condition, and the bar holds. The work is a single bullet rewritten in the grilling contract, and nothing else changed.
>
> My contract is the main-tree checker contract, unchanged since my last check: its last commit is `76e66e3` and it has no uncommitted edits. The work is `.claude/skills/expedition-grilling/SKILL.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/322-bare-assent-exception`, on branch `worktree-322-bare-assent-exception`, based on `de347dc`. I read the changed path only as the work. No list of rule changes was asked for this node, so none is given.
>
> **Part by part**
> 1. **The bullet's text is replaced exactly: met.**
>    - I unwrapped the new bullet and compared it string for string with the required text: "Unless the reply is a bare assent as in the rule above, a question the reply does not name stays unanswered, and the human has not deferred it. Put it in a later payload. Never read an unnamed question as assent, and never answer it yourself." They match exactly.
>    - It wraps across three lines of 98, 97 and 51 characters, with the same two-space continuation indent as its neighbours. The neighbouring lines run to about 101–102 characters.
>    - The condition's preamble describes the old bullet as "one sentence run across two lines". It is three sentences across two lines, but the quoted old text matches the before-text word for word, so this does not affect the check.
> 2. **The bullet above is the bare-assent rule, unchanged: met.** The bullet immediately above reads "A reply that assents to the recommendation without naming any question, such as *"ok for recommended"*, settles every question's recommendation in that payload. It settles nothing else in that payload." Its lines are unchanged in the diff, so "the rule above" points at it.
> 3. **The rest of the list, its introduction and the order: met.**
>    - "A reply settles what it covers and nothing else, under the following rules." is unchanged.
>    - The four bullets keep their order: naming, bare assent, unnamed question, park.
>    - The other three bullets are unchanged.
> 4. **No other line or file changes: met.**
>    - `git diff` shows exactly the two old lines removed and the three new lines added, all within this bullet.
>    - `git status --porcelain --untracked-files=all` shows only `.claude/skills/expedition-grilling/SKILL.md` modified.
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, in the same state as at my last check: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:**
>   - Standing rule 5 (plain English): the wording is dictated by the condition and is plain.
>   - `CONTEXT.md`'s `_Avoid_` lines: no refused word is introduced.
>   - All five ground rules, which are met.
> - The two shared sections of the grilling contract are outside the edit, so they remain identical to the other worker contracts.
> - No reviewing skill is named, so I ran none.

### Gate — approve, 2026-09-26

The human, `verbatim`: *"approve"*
