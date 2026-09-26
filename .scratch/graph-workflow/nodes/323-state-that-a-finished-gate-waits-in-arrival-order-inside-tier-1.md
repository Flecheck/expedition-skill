# State that a finished gate waits in arrival order inside tier 1

Type: implementation
Status: resolved
Blocked by: none

## Question

*Surfaced by [node 257](257-whether-a-finished-gate-may-jump-an-older-question.md)'s worker, and filed by the manager as it wrote it.*

Carry node 257's decision into the manager's contract. Inside tier 1, a gate waits in arrival order behind older items. Only the human's one-time request puts a gate first. The conflict comes off the list of conflicts left open.

## Acceptance condition

*Written by node 257's worker. Pasted as it wrote it, and not the manager's. The manager removed the handover's indentation only.*

The file `.claude/skills/expedition/SKILL.md` is changed as follows, and no other file is changed.
(1) Under the heading `## Conflicts this contract leaves open`, the bullet that begins "Arrival order against the cost of a waiting gate." is gone entirely. That bullet includes the sentences "A waiting gate holds a code slot, and a relayed question does not." and "Nothing says whether a gate may go ahead of an older tier 1 question." The other two bullets in that section are unchanged. The section's opening paragraph still reads true of what remains.
(2) Under the heading `## What is in front of the human, and when`, the text near the tier 1 list states two things in plain words. First, a gate waits in arrival order like the other two kinds in tier 1. A finished gate is sent after any older tier 1 item, such as an older blocked worker's raise or an older raise of the manager's own, and the manager never moves a gate ahead on its own judgement, for example because the gate holds a code slot. Second, the human may ask for a waiting gate to be sent first. That request applies once and lapses once used.
(3) The existing rules in that section still hold as written: tier 1 holds exactly three kinds of thing, tier 1 goes ahead of tier 2, nothing displaces a live question, and the manager never asks the human which waiting thing to take next. Nothing added contradicts any of them.
(4) No sentence anywhere in the file still says the ordering of a gate against an older tier 1 item is unsettled or left open.

## Answer

The manager's contract now says a gate waits in arrival order inside tier 1, and only the human's one-time request sends it first. The gate-ordering conflict is removed from the list of open conflicts.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The human approved. The work landed as commit `ed4ed20`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      State that a finished gate waits in arrival order inside tier 1
ANSWER:        The manager's contract, `.claude/skills/expedition/SKILL.md`, now states node 257's decision in `## What is in front of the human, and when` and no longer lists the gate-ordering conflict as open.

               **What was added.** Two paragraphs sit directly after the tier list and the "Tier 2 holds relayed interview questions..." paragraph:
               - "A gate waits in arrival order like the other two kinds in tier 1. Send a gate after every older thing in tier 1, such as an older raise from a blocked worker or an older raise of your own. Keep a gate at its place in arrival order even though it holds a code slot while it waits. Never move a gate ahead on your own judgement."
               - "The human may ask for a waiting gate to be sent first. That gate then goes ahead of everything else in the queue. It is still sent only when nothing is in front of the human. The request applies once and lapses once it is used."

               **What was changed.** The sentence "Send the one thing that the tiers and arrival order choose." became "Send the one thing that the tiers and arrival order choose, or the gate the human asked for." Without that change, the human's override would contradict the sentence. The "Never ask the human which waiting thing to take next..." sentence that follows it is unchanged apart from rewrapping.

               **What was removed.** The third bullet of `## Conflicts this contract leaves open`, "Arrival order against the cost of a waiting gate. ...", is gone entirely. The other two bullets and the section's opening paragraph are unchanged. "Each conflict below is named and left unresolved" still reads true of the two that remain.

               **Calls a later reader would otherwise re-derive.**
               - The override paragraph says the requested gate "is still sent only when nothing is in front of the human". This keeps "Nothing displaces a live question" true. It uses the wording the file already uses in `### Picking the next node` ("it waits until nothing is in front of them"). "When the live question is parked" was rejected because parking is only one of the ways a live question ends.
               - "Thing" is used in place of the condition's "tier 1 item". The file already says "three kinds of thing" and "waiting thing", and `CONTEXT.md` refuses "item" for a node.
               - "Finished gate" was shortened to "a gate", because anything in the queue is already a gate ready to send.
               - Every rule clause (3) protects still holds as written: tier 1's three fixed kinds, tier 1 ahead of tier 2, nothing displacing a live question, and never asking the human which waiting thing to take next.
               - No shipped file other than `SKILL.md` referred to the removed conflict (grep over the worktree's `.md` files outside `.scratch`).
INDEX LINE:    The manager's contract now says a gate waits in arrival order inside tier 1, and only the human's one-time request sends it first. The gate-ordering conflict is removed from the list of open conflicts.
FLAGS:         none
NEW NODES:     none
INVALIDATIONS: none. This carries out node 257's answer and contradicts no resolved node.
GATE PAYLOAD:  The checker has not run yet, so no findings are addressed.
               Paths touched: `.claude/skills/expedition/SKILL.md` (in the worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/323-gate-waits-in-arrival-order`, uncommitted).
               The bar: the repo has no build, tests, formatter or CI, and none were found. The bar is its non-command half, as `map-implementation-rules.md` records. New lines are wrapped at 104 columns or fewer.
               Proposed commit message:
                 State that a gate waits in arrival order inside tier 1

                 Drop the gate-ordering conflict from the manager contract's open list, and
                 name the human's one-time request to send a waiting gate first.

                 Node: graph-workflow/323

RE-POINTING SEARCH
Commands run, from the repo root:
- `python3 .scratch/graph-workflow/scripts/search-conditions.py 323 f630aa3:.claude/skills/expedition/SKILL.md .scratch/graph-workflow/worktrees/323-gate-waits-in-arrival-order/.claude/skills/expedition/SKILL.md`, run twice, the second time after the final edit and filtered with `grep -E "GONE \||^# "`. It searched 86 conditions. It found no GONE quoted span. The only GONE n-gram runs were the two known false ones: "is in front of the human at a time" (node 118) and "what is in front of the human at" (node 127). Every heading is still present.
- A grep across every node file with `Status: open` or `claimed` (138 files) for `arrival|relayed question does not|go ahead|Send the one thing|leaves open|conflicts this|throughput|gate first|tier 1`. The only match other than node 323 was node 118's clause 6, "the two tiers, and tier 1's three fixed members" unchanged in meaning. That still holds. Node 214's hit was an unrelated use of the word "arrival".
Result: no open condition quotes the removed bullet or the changed sentence. No replacement clause or supersession is proposed.

Method skill parts skipped: none. No method skill was invoked.

RETROSPECTIVE (effort-scoped)
(1) What I had to hunt for. Almost nothing. The node file's condition, node 257's handover and the spawn's section names pointed straight at both places. The one check I made myself was whether "parked" covers every way a live question ends. I looked at `CONTEXT.md`'s **Park** entry and found it covers deferral only, so I used "nothing is in front of the human" instead. I also checked `CONTEXT.md`'s `_Avoid_` lines for "item" and "finished" myself.
(2) What arrived that this node did not need. The whole of `map-implementation-rules.md`'s preamble, which covers supersession, history and review-route history. Only the ground rules and the five writing rules bore on this node. The auto-loaded `expedition-triggers.md` also arrived twice, once from the main tree and once from the worktree. The git-status snapshot of dozens of modified node files arrived as well. A rules file that opens with the binding blocks would let a worker stop reading early.
(3) What would have made it easier. A note in the condition or the spawn that the "Send the one thing that the tiers and arrival order choose" sentence has to change, or be read as covering the override, for the added override to be consistent. I had to spot that tension myself. The spawn's list of false GONE runs was useful and was accurate.
(4) What was stale, wrong or contradictory. The condition's "tier 1 item" collides with `CONTEXT.md`'s refusal of "item" (for a node). That is harmless, because the condition allows plain words, but a checker reading strictly might note it. The search script counts 86 conditions against 138 open or claimed nodes. The difference looks like nodes without conditions, not a defect, but the output does not say so.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-26. The checker was resumed from node 322's check.*

> PASS
>
> Node 323, "State that a finished gate waits in arrival order inside tier 1", meets all four parts of its acceptance condition, and the bar holds. The work removes one bullet from the open-conflicts section and adds two paragraphs to the queue section, and nothing else changed.
>
> My contract is the main-tree checker contract, unchanged since my last check: its last commit is `76e66e3` and it has no uncommitted edits. The work is `.claude/skills/expedition/SKILL.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/323-gate-waits-in-arrival-order`, on branch `worktree-323-gate-waits-in-arrival-order`, based on `f630aa3`. I read the changed path only as the work. No list of rule changes was asked for this node, so none is given.
>
> **Part by part**
> 1. **The open-conflict bullet is gone: met.**
>    - Under `## Conflicts this contract leaves open`, the whole bullet beginning "Arrival order against the cost of a waiting gate." is removed. It contained "A waiting gate holds a code slot, and a relayed question does not." and "Nothing says whether a gate may go ahead of an older tier 1 question."
>    - The other two bullets are unchanged in the diff: the scribe rule against the fuller form of a flag, and supplying what a condition leaves out against writing a whole condition.
>    - The opening paragraph, "Each conflict below is named and left unresolved…", still holds of the two that remain.
> 2. **The gate's place in the queue is stated near the tier 1 list: met.** Two new paragraphs follow the tier 1 list and its "Within a tier, take things in the order they arrived" sentence.
>    - The first says a gate waits in arrival order:
>      - "A gate waits in arrival order like the other two kinds in tier 1."
>      - "Send a gate after every older thing in tier 1, such as an older raise from a blocked worker or an older raise of your own."
>      - "Keep a gate at its place in arrival order even though it holds a code slot while it waits. Never move a gate ahead on your own judgement."
>    - The second says the human may ask for a gate first:
>      - "The human may ask for a waiting gate to be sent first."
>      - "The request applies once and lapses once it is used."
>    - The second paragraph also says: "That gate then goes ahead of everything else in the queue. It is still sent only when nothing is in front of the human." Both follow from "sent first" and from the existing rule that nothing displaces a live question.
> 3. **The existing rules still hold as written: met.** The rest of the section is unchanged, and nothing added contradicts it:
>    - "Tier 1 holds exactly three kinds of thing, and its membership is fixed", with its three-item list.
>    - "tier 1 goes ahead of tier 2".
>    - "Nothing displaces a live question". The requested gate is still sent only when nothing is in front of the human.
>    - The never-ask rule is kept, now reading "Send the one thing that the tiers and arrival order choose, or the gate the human asked for. Never ask the human which waiting thing to take next…". A request the human makes of their own accord does not have the manager asking.
> 4. **No sentence still says the gate's ordering is unsettled: met.**
>    - I searched the file unwrapped for sentences pairing "gate" with order, ahead, older, throughput, open or settle. Every hit is one of the new sentences.
>    - `## What nothing here settles` holds eight items, and none concerns a gate's order.
>    - Only this one file changed: `git status --porcelain --untracked-files=all` shows `.claude/skills/expedition/SKILL.md` alone.
>    - The file's headings are identical to the before-text.
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, in the same state as at my last check: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:**
>   - Standing rule 5 (plain English): the new text states its rules positively. "Never move a gate ahead on your own judgement" sits beside "Keep a gate at its place in arrival order".
>   - `CONTEXT.md`'s `_Avoid_` lines: no refused word is introduced.
>   - All five ground rules, which are met.
> - No reviewing skill is named, so I ran none.

### Gate — approve, 2026-09-26

The human, `verbatim`: *"approve"*
