# Carry the open-question search into the shipped contracts

Type: implementation
Status: resolved
Blocked by: 348

## Question

Node 272 decided that the search every party runs before handing back a fact covers the open nodes' `## Question` sections as well as their `## Acceptance condition` sections. The party reports each open node whose question its work changes, and the manager updates it in place. The shipped files state the search over conditions only.

*The manager's note: blocked on node 348, which is editing the same paragraph of the five worker contracts.* *Reported by [node 272](272-the-cascades-open-node-half-is-parked-on-a-ground-that-turns-out-to-be-false.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Acceptance condition

*Authored by node 272's worker and filed by the manager.*

> The files in scope are these six. The five worker contracts are `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md` and `.claude/skills/expedition-implementation/SKILL.md`. The sixth is the manager's contract, `.claude/skills/expedition/SKILL.md`.
> The scope came from a search. `grep -n -F "search the open nodes' \`## Acceptance condition\` sections for what your" .claude/skills/*/SKILL.md` returned exactly the five worker contracts, and `grep -n -F "It searches the open nodes' \`## Acceptance condition\` sections" .claude/skills/expedition/SKILL.md` returned the manager's contract. An instance the same searches reach outside these six files is reported and not edited.
> After this work:
> - (a) In each of the five worker contracts, the paragraph beginning "Before you write your handover, search the open nodes' `## Acceptance condition` sections" also tells the worker to search the open nodes' `## Question` sections. It uses the same handles: each word its work refuses, each path it changes or moves something out of, and each phrase it supersedes. It covers every open node, claimed or not, and the worker reads only what matches.
> - (b) In each of those five contracts, the handover's `CONDITIONS` part, or a part placed beside it, asks the worker to name the open nodes whose `## Question` its work changes (a renamed term, a part answered, or the node made unnecessary) and to say how.
> - (c) In `.claude/skills/expedition/SKILL.md`, the paragraph beginning "Before a party hands back a fact it established" says three things. The search also covers the open nodes' `## Question` sections. The manager updates an unclaimed node's question in place with the old wording marked, per graph-conventions.md's rule for an open, unclaimed node whose question has only changed. Where no party established the fact, the manager does that search.
> - (d) Each of the six files states that a question naming a thing in different words from the change's will not match, and that this is accepted.
> - (e) No file under `.scratch/` is changed.
> - (f) Every heading in each of the six files, as listed by `grep -n '^#\{1,6\} '` before the work, is still present afterwards, in the same order.

## Answer

All six shipped contracts now extend the pre-handover search to open nodes' questions; workers report changed questions under CONDITIONS; the manager updates unclaimed ones in place.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `0006cc5`. Flags 350.1, 350.2 settle at the node closing report.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

````
HANDOVER:      Carry the open-question search into the shipped contracts (350)

ANSWER:
**The pre-handover search now covers open nodes' `## Question` sections in all six shipped contracts, as node 272 decided.** The work is uncommitted in the worktree `.scratch/graph-workflow/worktrees/350-open-question`.

**The five worker contracts** (grilling, research, prototype, precondition, implementation). After the edit, the paragraph and the template line are byte-identical across all five.
- The paragraph beginning "Before you write your handover, search the open nodes' `## Acceptance condition` sections" keeps that opening word for word, so both the condition's anchor and its scope grep still match. A sentence after the condition search tells the worker to search the open nodes' `## Question` sections the same way: the same words, paths and phrases, in every open node, claimed or not, reading only what matches.
- Near the end of that paragraph, a new passage tells the worker to name in `CONDITIONS` each open node whose question its work changes, and to say how: a term in it renamed, a part of it answered, or the node made unnecessary. The paragraph ends by saying that a question naming a thing in different words will not match the search, and that this miss is accepted.
- **The change goes in the existing `CONDITIONS` part, and no new part was added.** A new part would have changed each contract's "all N parts" count and the handover shape the manager parses. The template line now reads: what you searched the open nodes' conditions and questions for; each replacement clause, with what fixed its words; and each open node whose question your work changes, and how.

**The manager's contract, `.claude/skills/expedition/SKILL.md`.**
- The paragraph beginning "Before a party hands back a fact it established" now says four things:
  - the search covers `## Question` sections as well as conditions;
  - the party names each open node whose question its work changes;
  - the manager updates an unclaimed node's question in place with the old wording marked, under the rule in `graph-conventions.md`'s `### Supersede` for an open, unclaimed node whose question has only changed;
  - where no party established the fact, the manager does the search.
- It keeps "what to do about a claimed node stays yours". It also states the accepted synonym miss.
- The old text said "Where no such party exists". It now says "Where no party established the fact", which is the condition's own wording.
- **One more edit, outside the named paragraph:** in `## What nothing here settles`, item 4 said the only bounded class with a duty to look was "the open nodes' acceptance conditions". That became false with this work, so it now reads "the open nodes' acceptance conditions and questions". This is flagged below.

**The claimed-node case is still the manager's.** Following node 272's second ASSUMPTION flag, no contract gives permission to edit a claimed node's question.

**Wrap width.** The wrap widths were kept: at most 104 columns in the worker paragraph and 105 in the manager's. No heading changed in any of the six files, checked by diffing `grep '^#\{1,6\} '` output taken before and after.

INDEX LINE:    All six shipped contracts now extend the pre-handover search to open nodes' questions; workers report changed questions under CONDITIONS; the manager updates unclaimed ones in place.

FLAGS:
ASSUMPTION: This node's own prose: node 350 edited one sentence in `.claude/skills/expedition/SKILL.md` outside the paragraph its condition names. Item 4 of `## What nothing here settles` said "One bounded class does carry a duty to look, the open nodes' acceptance conditions". After this work that is false. So it now reads "the open nodes' acceptance conditions and questions". The file is one of the six in scope, the concern is the same, and leaving the sentence as it was would have shipped a contradiction inside the manager's contract. The condition's "reported and not edited" clause covers instances outside the six files, so it does not apply here. Index sentence: Node 350 also corrected the manager contract's "What nothing here settles" item 4, which named only acceptance conditions as carrying a duty to look, to add questions.

ASSUMPTION: This node's own prose: condition (b) allowed either the `CONDITIONS` part or a part placed beside it. Node 350 extended `CONDITIONS` and added no new handover part, because a new part would change each contract's handover part count and the shape the manager parses. Index sentence: Node 350 carried changed-question reports inside the existing CONDITIONS handover part rather than adding a ninth part to the worker handovers.

NEW NODES:     none

INVALIDATIONS:
- **Node 272: none contradicted.** This work carries out its rule as stated.
- **Node 263: extension, already recorded by node 272.** Its handle search is now shipped over `## Question` sections as well.
- **Node 15: no new change.** Node 272 already recorded how part 2 is narrowed and extended, and this work ships that.

CONDITIONS:
**What I searched for.** I ran the search over every open or claimed node (70 files), over whole files rather than only the condition and question sections, then read the matches. The phrases were:
- `Acceptance condition\` sections`
- `search the open nodes`
- `It searches the open nodes`
- `Where no such party exists`
- `what you searched the open nodes`
- `open-question`
- `## Question\` section`
- `questions that fact`
- `conditions that fact makes wrong`
- `CONDITIONS`

**What the search found.**
- Apart from node 350 itself, the only relevant hit is node 87's `## Amendment, 2026-09-27 (from node 272)`. Its replacement text for the fourth duty agrees with what now ships, so no replacement clause is owed.
- Nodes 41, 190, 230 and 56 matched `CONDITIONS` only in amendment provenance lines, which have a different concern.

**Question changed: node 87 (open, unclaimed), "part of it answered".** The fourth duty in its question ("open-node targets stay manual", already superseded by node 272's amendment) is now stated in the shipped manager contract, in the paragraph beginning "Before a party hands back a fact it established". So a worker on node 87 will find that duty already in place. The manager can mark this in 87's question. No replacement clause for its condition is written, since the amendment already carries the text.

MISSING FROM MAP: none

GATE PAYLOAD:
- **Checker findings:** none yet, as no checker has run.
- **The bar:** confirmed against the repo. It has no build, no tests, no formatter and no CI. The only file of that kind is `.gitignore`, whose three entries match the rules file's record. So the bar is its non-command half. `git diff --check` is clean. No file under `.scratch/` is changed (`git status --short` lists only the six skill files).
- **Paths touched:**
  - `.claude/skills/expedition-grilling/SKILL.md`
  - `.claude/skills/expedition-research/SKILL.md`
  - `.claude/skills/expedition-prototype/SKILL.md`
  - `.claude/skills/expedition-precondition/SKILL.md`
  - `.claude/skills/expedition-implementation/SKILL.md`
  - `.claude/skills/expedition/SKILL.md`
- **Scratch files:** I wrote temporary heading snapshots to `$TMPDIR/h350/` for the check on clause (f), then deleted them.
- **Proposed commit message:**
  ```
  Extend the pre-handover search to open nodes' questions

  The five worker contracts and the manager's contract now have every party
  search open nodes' `## Question` sections alongside their acceptance
  conditions, and report under CONDITIONS each open node whose question its
  work changes. The manager updates an unclaimed node's question in place,
  old wording marked, under graph-conventions.md's Supersede rule. The
  synonym miss is stated as accepted.

  Node: graph-workflow/350
  ```

RETROSPECTIVE:
1. **What I had to hunt for.**
   - Where `graph-conventions.md` states the rule for "an open, unclaimed node whose question has only changed". It is under `### Supersede`. Node 272's condition cites it without the heading.
   - Whether the five worker paragraphs and templates were still byte-identical after node 348. They were.
2. **What arrived that this node did not need.** Most of `map.md` and all of `map-implementation-rules.md` beyond the bar paragraph. Node 272's full handover, where its `**The rule.**` bullets alone would have done.
3. **What would have made this easier.** The condition could name `### Supersede` as the heading holding the in-place rule. It could also say whether "the paragraph beginning X" must keep that exact opening. I kept it, so the anchor still greps.
4. **What was stale, wrong or contradictory.**
   - All the condition's quotes still matched after nodes 348 and 351.
   - The manager contract's `## What nothing here settles` item 4 would have gone stale because of this work. I fixed it (flag 1). The condition's search did not reach it, because its scope grep targeted only the one paragraph.
   - `.claude/skills/expedition-cascade/SKILL.md` has a join search over conditions only ("Before you report a node, search the open nodes' `## Acceptance condition` sections for the path the…"). That is a defect-join by path, a different concern, and it was not edited.
````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 348's check; the condition reached it as a verbatim copy in `$TMPDIR/c350.md`.*

> PASS
>
> This is the check of node 350, "Carry the open-question search into the shipped contracts". The work is the uncommitted diff in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/350-open-question`, on base 7bfa1e8. I read the whole condition in `/tmp/claude-1000/c350.md`, and the ground rules in `/tmp/claude-1000/ground.md`.
>
> **Parts of the condition**
>
> - **Scope: the six files.** Met.
>   - `git status --short --untracked-files=all` shows exactly the six: `.claude/skills/expedition/SKILL.md` and the grilling, research, prototype, precondition and implementation contracts.
> - **The recorded searches.** They match the recorded return.
>   - I ran them on HEAD with `git grep`. `-F "search the open nodes' \`## Acceptance condition\` sections for what your"` returns the five worker contracts. `-F "It searches the open nodes' \`## Acceptance condition\` sections"` returns `expedition/SKILL.md` line 472.
>   - Run on the worked tree, the first search again returns only the five contracts, so no instance lies outside the six files.
>   - A broader search, `grep -rn -F "## Acceptance condition\` sections"` over `.claude/` and `CONTEXT.md`, also finds `expedition-cascade/SKILL.md` line 121. That line is the cascade's join search ("for the path the departure is in"), a different search from the recorded one, and the recorded searches do not reach it.
> - **(a)** Met in all five contracts. The paragraph beginning "Before you write your handover, search the open nodes' `## Acceptance condition` sections" now adds: "Search the open nodes' `## Question` sections the same way, for the same words, paths and phrases, in every open node, claimed or not, and read only what matches."
> - **(b)** Met in all five contracts.
>   - The `CONDITIONS:` line of each handover block now ends "and each open node whose question your work changes, and how".
>   - The paragraph adds: "Where your work changes an open node's question, name that node in `CONDITIONS` and say how: a term in it renamed, a part of it answered, or the node made unnecessary."
> - **(c)** Met. In `expedition/SKILL.md`, the paragraph beginning "Before a party hands back a fact it established" now says all three things:
>   - the search covers "the open nodes' `## Acceptance condition` sections and their `## Question` sections";
>   - "Update an unclaimed node's question in place with the old wording marked, under the rule in `graph-conventions.md`'s `### Supersede` for an open, unclaimed node whose question has only changed". That rule exists: "A node whose question has only changed, and which is `open`, unclaimed and holds no work, … Update it in place instead, marking the old wording.";
>   - "Where no party established the fact, you do the search."
> - **(d)** Met in all six files. The five contracts say "A question that names a thing in words different from the ones your work uses will not match this search, and that miss is accepted." The manager contract says the same, with "the work" in place of "your work".
> - **(e)** Met. No `.scratch/` path appears in the status.
> - **(f)** Met. For each of the six files, `diff` of `grep '^#\{1,6\} '` at HEAD against the working file prints nothing.
> - **One further change.** Item 4 under `## What nothing here settles` now names "acceptance conditions and questions" as the bounded class that carries a duty to look. This keeps it consistent with (c), and the condition forbids no such change inside the six files.
>
> **The bar**
>
> - The rules file records that the repo has no build, no tests, no formatter and no CI. The worktree root confirms it: no manifest or task runner. So there are no commands to run.
> - `git diff --check` is clean (exit 0).
> - No added line is longer than 105 characters.
>
> **Standards.** As in my earlier checks, I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`, plus the ground rules handed to me as text.
>
> - These bore on the work, and I found nothing against them:
>   - The ground rules: each contract carries the rule in its own words, no tool is named, and nothing addresses the human.
>   - `CONTEXT.md` `_Avoid_` lines.
>   - The writing rules: citations are by heading.
>   - `/writing-for-agents`.
>   - `graph-conventions.md`: the manager's update follows its `### Supersede` rule.
> - `/coding-principles` and `/naming` did not bear on the work.
> - No reviewing skill is named, so I ran none.
>
> NOT COVERED:
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The condition does not demand this; the rules file makes it a bookkeeping rule. The worktree shows no `.scratch/` change. What the main tree's record holds is outside what I was given.

### Gate — approve, `standing yes`, 2026-09-27

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and its one NOT COVERED item is the worker's bookkeeping. This settles none of the node's flags; they settle at the node closing report.

## Flags

`350.1` `ASSUMPTION` **· settled** — This node's own prose: node 350 edited one sentence in `.claude/skills/expedition/SKILL.md` outside the paragraph its condition names. Item 4 of `## What nothing here settles` said "One bounded class does carry a duty to look, the open nodes' acceptance conditions". After this work that is false. So it now reads "the open nodes' acceptance conditions and questions". The file is one of the six in scope, the concern is the same, and leaving the sentence as it was would have shipped a contradiction inside the manager's contract. The condition's "reported and not edited" clause covers instances outside the six files, so it does not apply here. Index sentence: Node 350 also corrected the manager contract's "What nothing here settles" item 4, which named only acceptance conditions as carrying a duty to look, to add questions.

`350.2` `ASSUMPTION` **· settled** — This node's own prose: condition (b) allowed either the `CONDITIONS` part or a part placed beside it. Node 350 extended `CONDITIONS` and added no new handover part, because a new part would change each contract's handover part count and the shape the manager parses. Index sentence: Node 350 carried changed-question reports inside the existing CONDITIONS handover part rather than adding a ninth part to the worker handovers.

*The manager's note, 2026-09-27:* flags 350.1, 350.2 settle at the node closing report that closes this node, which names its gate as taken under the standing yes.
