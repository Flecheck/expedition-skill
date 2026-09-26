# `CONTEXT.md`'s `Closing report` entry lists three contents where the settled report has six

Type: implementation
Status: resolved

## Question

*Surfaced by [What the manager reports to the human, in one place](46-what-the-manager-reports.md)'s worker, and
pasted as it wrote it.*

> `CONTEXT.md`'s **Closing report** entry says the manager hands over *"what was decided, what landed, and every flag
> still outstanding"*. Node 10 and `.claude/skills/expedition/SKILL.md` fix six items and make the report a delta
> scoped to what the human has not already seen. `CONTEXT.md` is declared authoritative and ships with the skill set,
> so a reader taking it at its word writes a report short by half. Node 103's condition reaches `CONTEXT.md`'s
> **Flag** entry and not this one; node 90's reaches the **Closed** entry and not this one.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 46's worker. Pasted as it wrote it, and not the manager's.*

> `CONTEXT.md`'s **Closing report** entry states that the report is a delta scoped to what the human has not already
> seen, and that it carries what landed, the supersession chains, the state of the bar, every outstanding flag, what
> the sweep found, and every sweep round. Its `_Avoid_` line is unchanged. No other entry in `CONTEXT.md` changes —
> in particular the **Closed**, **Flag** and **Handover** entries are untouched, those being other nodes' work. No
> file under `.claude/skills/` changes and no file under `.scratch/` changes. The working tree meets the bar.

## Answer

`CONTEXT.md`'s Closing report entry now says the report covers only what the human has not seen and lists the manager contract's six items; `_Avoid_` unchanged.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The human approved. The work landed as commit `64db5aa`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      `CONTEXT.md`'s `Closing report` entry lists three contents where the settled report has six

ANSWER:        `CONTEXT.md`'s **Closing report** entry, under `## Closing an effort`, now reads: *"What the manager hands the human once the frontier empties. It covers only what the human has not already seen. It carries what landed, the supersession chains, the state of the bar, every flag still outstanding, what the sweep found, and every sweep round."* Its `_Avoid_: completion report, summary` line is unchanged, and no other entry changed.

The premise was checked against the manager contract as it stands after the plain-English rewrite. `.claude/skills/expedition/SKILL.md`, under `## Closing an effort`, still says the report "covers only what the human has not already seen" and lists the same six items. So the condition's list is current.

Calls a later reader would otherwise have to re-derive:
- "what was decided" is dropped from the entry because the manager contract does not list it.
- The entry says "covers only what the human has not already seen", which is the manager contract's wording, and not the condition's word "delta". Under standing rule 5 (plain English), the contract's wording is the better choice.
- The contract says where the outstanding flags come from ("taken from the unchecked lines of the effort's index of flags and never reconstructed by you"). That clause is left out. It is a duty of the manager, it stays in the manager contract, and a glossary entry defines the term.
- "once the frontier empties" and "every flag still outstanding" keep the entry's existing wording.
- The existing wrap width of about 102 columns is kept. The new lines are 97, 101 and 57 columns long.

INDEX LINE:    `CONTEXT.md`'s Closing report entry now says the report covers only what the human has not seen and lists the manager contract's six items; `_Avoid_` unchanged.

FLAGS:         ASSUMPTION: I wrote "covers only what the human has not already seen", the manager contract's own phrase, where the acceptance condition says "a delta scoped to what the human has not already seen". The two say the same thing, and standing rule 5 asks for plain words over jargon. I kept the entry's existing "every flag still outstanding" and did not carry in the contract's clause about where those flags come from. That clause is the manager's duty and stays in the manager contract. No round took place on this node. What I actually did was read the manager contract's `## Closing an effort`, confirm that its six items match the condition, and rewrite the entry's content sentence only.
               Index sentence: At node 106 the glossary's Closing report entry took the manager contract's phrase "covers only what the human has not already seen" in place of the condition's word "delta", and left out the contract's clause about where outstanding flags come from.

NEW NODES:     none

INVALIDATIONS: none among resolved nodes. One open node is affected: node 137, "Rename the two reports and repair the `_Avoid_` line that reserved the word", status open. Clause 1 of its acceptance condition (written by node 107's worker) defines the **effort closing report** as "what was decided, what landed, and every flag still outstanding". Clause 2 renames this same entry and says "Its meaning is unchanged". After this node lands, a worker following clause 1 would write back the three-item list this node just removed, and clause 2's "unchanged" would then be false. The manager needs to repair node 137's condition before that node is claimed, because its worker may not rewrite the condition itself.

GATE PAYLOAD:  Checker findings: none yet (no checker has run).
               Paths touched: `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/106-closing-report-entry/CONTEXT.md` only.
               Bar: I checked the repo and it has no build, tests, formatter or CI: no manifest or task runner, and a `.gitignore` that runs nothing. This matches the record in `map-implementation-rules.md`, so the recorded commands need no repair. The non-command half was checked. The new text uses no word refused by an `_Avoid_` line ("sweep round" is not refused; "review round" is refused only for the correction round). It follows standing rule 5, with one idea per sentence and no bold except the existing entry heading, and it keeps the wrap width.
               Proposed commit message:
                 Give the glossary's Closing report entry the manager contract's six items

                 The entry listed what was decided, what landed and outstanding flags. The
                 manager contract has the report cover only what the human has not already
                 seen, and carry what landed, the supersession chains, the state of the bar,
                 every outstanding flag, what the sweep found, and every sweep round.

                 Node: graph-workflow/106

RETROSPECTIVE:
1. What I had to hunt for: nothing I needed for the edit. The closing-report section of the manager contract was found with one grep for "closing report". Node 137's conflicting condition was found by following decisions.md line 92 (node 107) to the nodes that mention "effort closing report". That was a side search, and it found the one thing that needs acting on.
2. What arrived that this node did not need: most of `map.md`. Its standing preferences had no bearing on a three-line glossary edit. Of `map-implementation-rules.md`, only the bar paragraph, the review-route standards and the five writing rules were used; the record-as-work paragraph and the file's own supersession rules were not. The implementation contract's sections on reporting implementation nodes and on replacement attempts did not apply.
3. What would have made this easier: the spawn or the node file could name the manager contract's heading where the six items live (`## Closing an effort` in `.claude/skills/expedition/SKILL.md`). The record could also link node 137 from node 106, since both conditions govern the same entry and nothing connects them.
4. What was stale, wrong or contradictory: node 137's acceptance condition, clauses 1 and 2, as set out under INVALIDATIONS. Also, `map.md`'s paragraph about `CONTEXT.md` says node 56 moves the glossary to `.claude/skills/expedition/glossary.md`, but it is still at the root as `CONTEXT.md`. That is consistent with the move not having landed yet, and the spawn noted it.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-26. The checker was resumed from node 325's check.*

> PASS
>
> Node 106, "`CONTEXT.md`'s `Closing report` entry lists three contents where the settled report has six", meets its acceptance condition, and the bar holds. The work rewrites one entry in the glossary, and nothing else changed.
>
> My contract is the main-tree checker contract, unchanged since my last check: its last commit is `76e66e3` and it has no uncommitted edits. The work is `CONTEXT.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/106-closing-report-entry`, on branch `worktree-106-closing-report-entry`, with HEAD and merge-base both at `c52c03e`. I read the changed path only as the work.
>
> `CONTEXT.md`'s `_Avoid_` lines are one of the standards this work is held against. The edit does not touch any `_Avoid_` line, so no standard moved.
>
> **Part by part**
> 1. **The entry states the report's scope and its six contents: met.**
>    - Before: "What the manager hands the human once the frontier empties: what was decided, what landed, and every flag still outstanding."
>    - After: "What the manager hands the human once the frontier empties. It covers only what the human has not already seen. It carries what landed, the supersession chains, the state of the bar, every flag still outstanding, what the sweep found, and every sweep round."
>    - "It covers only what the human has not already seen" states the scope the condition calls a delta limited to what the human has not already seen.
>    - All six contents are listed: what landed, the supersession chains, the state of the bar, every outstanding flag, what the sweep found, and every sweep round.
> 2. **The `_Avoid_` line is unchanged: met.** It still reads "_Avoid_: completion report, summary".
> 3. **No other entry changes: met.** `git diff` touches only the Closing report entry's definition lines. The **Closed**, **Flag** and **Handover** entries are untouched.
> 4. **Nothing under `.claude/skills/` or `.scratch/` changes, and no other path changes: met.** `git status --porcelain --untracked-files=all` shows only `CONTEXT.md` modified. That matches the worker's report, which I checked rather than relied on.
> 5. **The working tree meets the bar: met**, as below.
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, in the same state as at my last check: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:**
>   - Standing rule 5 (plain English): three short sentences, each holding one idea.
>   - `CONTEXT.md`'s `_Avoid_` lines: none is changed. No refused word is introduced, and "summary" does not appear in the new text.
>   - All five ground rules, which are met.
> - No reviewing skill is named, so I ran none.

### Gate — approve, 2026-09-26

The human, `verbatim`: *"approve"*

## Flags

`106.1` **· settled** `ASSUMPTION` — I wrote "covers only what the human has not already seen", the manager contract's own phrase, where the acceptance condition says "a delta scoped to what the human has not already seen". The two say the same thing, and standing rule 5 asks for plain words over jargon. I kept the entry's existing "every flag still outstanding" and did not carry in the contract's clause about where those flags come from. That clause is the manager's duty and stays in the manager contract. No round took place on this node. What I actually did was read the manager contract's `## Closing an effort`, confirm that its six items match the condition, and rewrite the entry's content sentence only.
