# Qualify the glossary's research entry for the research raise

Type: implementation
Status: resolved
Supersedes: 57
Blocked by: none

## Question

Once the research contract has a raise, the glossary's `research` entry is false where it says the node is worked without the human.

*Proposed by [node 329](329-group-the-open-nodes-against-the-worker-contracts.md)'s worker and filed by the manager, on the human's "ok" to node 329's merge and its conflicts' recommendations.* *The worker's sequencing note:* "Best landed with or after W." W is [node 333](333-land-the-open-repairs-to-the-five-worker-contracts-in-one-change.md). *The manager's note:* this node changes `CONTEXT.md`, which [node 332](332-repair-the-glossarys-code-slot-reject-kinds-grilling-and-closed-text.md) is changing now; it is claimed after 332 lands.

## Acceptance condition

*Written by node 329's worker.*

R2.1 *(node 57)* In `CONTEXT.md` at the repository root, the `research` entry no longer says without qualification that a research node is worked without the human, which it states today as "It is worked without the human." It says a research node's ordinary work is done without the human, and that its worker may raise where the node's premise is broken. The entry has no `_Avoid_` line, and gains none.
R2.2 No other entry is edited, and no other file changes. The working tree meets the bar.

*The manager's note, 2026-09-26:* [node 333](333-land-the-open-repairs-to-the-five-worker-contracts-in-one-change.md)'s worker reports that `CONTEXT.md`'s `**Handover**:` entry, which lists five things, is stale since node 333 landed (`5acd220`) two new handover parts, `CONDITIONS` and `MISSING FROM MAP`. It wrote no clause for it. This glossary node is where it belongs; its condition is to gain one before it is claimed.

## Answer

The glossary's `research` entry now says its worker may raise on a broken premise. The `Handover` entry now lists the seven parts, plus an implementation worker's eighth, the gate payload.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The human approved. The work landed as commit `b4970ed`. Flag 335.1 is settled at this gate.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      Qualify the glossary's research entry for the research raise
ANSWER:        Two entries in `CONTEXT.md` changed. No other entry and no other file changed. Line width stays at 102.
                - **`research`**: the sentence "It is worked without the human." is replaced by "Its ordinary work is done without the human. Its worker may raise where the node's premise is broken." This is two sentences because standing rule for writing 5 asks for one idea per sentence. The entry had no `_Avoid_` line before and has none now. The wording matches the research contract's `## When the premise is broken` (landed in `5acd220`) and the `implementation` entry's "raises only when its premise is broken".
                - **`Handover`**: the entry now says a worker returns seven parts: its node's answer written as the node will hold it, the index line, its flags, the new nodes it found, which resolved node its work changes, the open conditions it searched and any replacement clauses it wrote, and what `map.md` did not tell it. It then says "An implementation worker returns an eighth part, the gate payload." The parts follow the contracts' labels (ANSWER, INDEX LINE, FLAGS, NEW NODES, INVALIDATIONS, CONDITIONS, MISSING FROM MAP, GATE PAYLOAD), and the phrases are the amendment's own. The old part "the nodes it invalidated" is replaced by "which resolved node its work changes", which is how the amendment and the contracts' `INVALIDATIONS` part describe it. "The manager files it unaltered." is word for word the same, but it now sits at the end of the last wrapped line instead of on a line of its own. The `_Avoid_` line is unchanged.
                - **One wording call**: "gate payload" is the amendment's term and the contracts' GATE PAYLOAD label. It stays even though the same entry's `_Avoid_` line refuses "payload" as a name for the handover. The refusal is about what the handover is called. "Gate payload" names one part of it, so the two do not clash.
                - **Counts**: 53 bold term lines and 43 `_Avoid_` lines, both the same as at `5c12368`.
INDEX LINE:    The glossary's `research` entry now says its worker may raise on a broken premise. The `Handover` entry now lists the seven parts, plus an implementation worker's eighth, the gate payload.
FLAGS:         none
NEW NODES:     none
INVALIDATIONS: [node 302](302-rewrite-the-glossary.md) (resolved), extension: the `research` and `Handover` wordings it wrote are replaced so they match the landed contracts. This carries into the glossary what nodes 333 (`5acd220`) and 336 already decided. Nothing contradicts a decision. Node 57 is superseded by this node, not resolved, so it is not listed.
CONDITIONS:    **Searched for**:
                - the phrases "worked without the human", "nodes it invalidated", "Handover**" and "handover … entry", and "research entry", across all node files
                - `CONTEXT.md` in every open node's `## Acceptance condition`: nodes 137, 124, 156, 109, 190, 56, 337, 41 and 284
                - within those conditions: handover, research, without the human, invalidated, seven parts, five
                **Findings**: I wrote no replacement clauses.
                - Only node 137 clause 5 touches an entry I edited, and it touches the `Handover` `_Avoid_` line, which I left unchanged.
                - Separately, clause 5 quotes that line as "(the closing report owns that word)", but the file says "(the closing report uses that word)". This was already stale before my work. I did not cause it, so I wrote no replacement.
                - Node 56 moves the whole glossary and quotes neither entry.
MISSING FROM MAP: none
GATE PAYLOAD:  **Checker findings**: none received yet.
                **Paths touched**: `CONTEXT.md` in worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/335-glossary`. Nothing else, uncommitted.
                **The bar**:
                - The worktree root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`, with no manifest, no task runner and no CI. This confirms the recorded "no build, no tests, no formatter", so the bar here is the part without commands.
                - The `_Avoid_` refusals, the writing rules and the 102 wrap width all hold. No line is over 102.
                - I skipped no method skill.
                **Proposed commit message**:
                Qualify the glossary's research and handover entries for the landed contracts

                The research entry says its worker may raise on a broken premise; the
                handover entry lists the seven parts and an implementation worker's gate
                payload.

                Node: graph-workflow/335

RETROSPECTIVE:
1. **What I had to hunt for**: very little.
   - The research raise's wording: I found it by pulling `## When the premise is broken` with sed. The spawn named the section, which helped.
   - Whether "payload" in "gate payload" clashes with the Handover `_Avoid_` line: I settled it myself (see ANSWER).
   - The open-condition search: about three greps.
2. **What arrived that this node did not need**:
   - Most of `map.md`: the standing preferences on resume, worktrees and tokens bore on nothing here.
   - About half of `map-implementation-rules.md`: its history preamble and the paragraph on work that is the effort's own record.
   - Most of the implementation contract's sections on reporting a new implementation node and on correction rounds.
   - For a glossary edit with an exact demand, the useful parts were the node file, the two landed sections the text follows, the writing rules and the ground rules.
   - One avoidable cost: my first cat of the contract, node and rules together overflowed into a saved file, so I read it twice. That was my own batching.
3. **What would have made this easier**:
   - The amendment already gives the demand in full, and that worked well.
   - The spawn's list of labels saved a lookup.
   - A one-line note in the node on whether "The manager files it unaltered." must stay on its own line would remove the one small doubt I had. I read "unchanged" as referring to the text, not the layout.
4. **What was stale, wrong or contradictory**:
   - Node 137 clause 5 quotes the Handover `_Avoid_` line as "owns that word", but the file says "uses that word".
   - The decisions index has no line for node 336, so the only record of the handover amendment I found was on this node.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 338's check.*

> PASS
>
> Node 335, "Qualify the glossary's research entry for the research raise". The work is the uncommitted diff in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/335-glossary` (base 5c12368). I established every part from `git diff` and `grep -n -A6 '^\*\*research\*\*\|^\*\*Handover\*\*' CONTEXT.md`. The one exception is listed under NOT COVERED below.
>
> - **R2.1, first half:** met. The `research` entry no longer contains "It is worked without the human."
> - **R2.1, second half:** met. It now reads "Its ordinary work is done without the human. Its worker may raise where the node's premise is broken." The entry has no `_Avoid_` line: the line after it is blank, followed by `**prototype**:`.
> - **R2.2 and the added demand's fence ("No other entry is edited", "No other file changes"), read as their union:** met. `git status --short` shows only `CONTEXT.md`. The diff has exactly two hunks, one in the `research` entry and one in the `Handover` entry.
> - **Added demand, the seven parts:** met. The `Handover` entry now reads "in seven parts" and lists them in order:
>   1. its node's answer written as the node will hold it;
>   2. the index line;
>   3. its flags;
>   4. the new nodes it found;
>   5. which resolved node its work changes;
>   6. the open conditions it searched and any replacement clauses it wrote;
>   7. what `map.md` did not tell it.
> - **Added demand, the eighth part:** met. The entry says "An implementation worker returns an eighth part, the gate payload."
> - **Added demand, unchanged text:** met. "The manager files it unaltered." is still the last sentence. The `_Avoid_` line is a context line in the diff, so it is unchanged.
> - **The working tree meets the bar (both demands):** met, see below.
>
> **The bar:**
> - The repo has no build, tests, formatter or CI, so there are no commands to run.
> - `git diff --check`: clean, exit 0.
> - `awk 'length>105' CONTEXT.md`: prints nothing, so the file's line width holds.
>
> **Standards:** I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`, as for my earlier checks.
> - Bore on this work:
>   - `CONTEXT.md`'s `_Avoid_` lines, checked by hand against the added text. "payload" appears only inside the separate term "gate payload", and the condition dictates that wording.
>   - The five writing rules. Each added sentence carries one idea, and no bold was added.
>   - `/writing-for-agents`: nothing found.
>   - The ground rules: nothing assumes a repo, a machine or a toolchain, and nothing addresses the human.
> - Did not bear on this work: `/coding-principles` and `/naming`, because the work is prose and names nothing new.
> - No reviewing skill is named, so I ran none. The work changes no standard I hold it against.
>
> The condition records no search command, so there was nothing to re-run.
>
> NOT COVERED:
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The condition does not demand this explicitly, but the rules file makes it a bookkeeping rule. The worktree diff contains no such write. What the main tree's record holds is outside what I was given.

### Gate — approve, 2026-09-27

The human, `verbatim`: *"approve"*

## Amendment, 2026-09-26 (from node 336)

*Written by [node 336](336-carry-the-rules-on-what-reaches-the-human-the-code.md)'s worker as a new node's condition, and folded into this open glossary node by the manager under the human's standing instruction that a related defect joins a node that already exists. Pasted as that worker wrote it. Both demands now stand together; each keeps its own fence over the one entry it names, and "No other file changes" in each is read as the union: `CONTEXT.md`'s `research` and `Handover` entries.*

- **An added demand.** "The work is `CONTEXT.md`. No other file changes. The `**Handover**:` entry lists what a worker returns as seven parts: its node's answer written as the node will hold it, the index line, its flags, the new nodes it found, which resolved node its work changes, the open conditions it searched and any replacement clauses it wrote, and what `map.md` did not tell it. It says an implementation worker returns an eighth part, the gate payload. The entry's last sentence, "The manager files it unaltered.", and its `_Avoid_` line are unchanged. The working tree meets the bar."

## Flags

`335.1` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above.* Node 336's proposed node was folded into this node, and the two fences are read as their union.
