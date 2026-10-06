# A spawn points at the decisions index without naming which sections bear on the node

Type: implementation
Status: claimed

Blocked by: 392

## Question

This work lets every worker find the decisions that bear on its node without reading the whole index of decisions. It works on any effort, with or without a label vocabulary.

*The opening sentence above was written by [node 392](392-write-the-acceptance-conditions-for-the-five-kept-nodes.md)'s worker and filed by the manager on 2026-10-06.*

*Minted by the manager under the map's rule that a standing retrospective item reported a second time becomes a node.
Reported by [node 175](175-what-the-worktree-cycle-does-to-the-sandbox.md)'s worker and then by [node
169](169-rules-file-bar-paragraph-names-the-maps-standing-preferences.md)'s.*

**The shipped contracts already provide for scoping**, and the manager's own contract states it: a spawn carries
*"the effort's index of decisions scoped by label where a vocabulary exists"*, and a worker contract tells its reader
to read *"the sections the spawn names"*. **This effort declares no label vocabulary, and the manager has been
writing the pointer flat every time**, saying only that it is unscoped.

**The two reports.** Node 175's worker: *"`decisions.md` was pointed at with no section named, so I grepped it rather
than reading it and used two of its 111 lines — naming the sections, as the contract says the spawn should, would
have cost nothing."* Node 169's worker, on a one-line edit: *"I cited nothing from it and can identify nothing it
stopped me doing… A different arrangement that would have avoided it: the spawn naming which sections of
`decisions.md` bear on the node, which the contract already provides for and which this spawn did not use."*

**What is open:** whether the manager can scope an index that has no declared vocabulary and no headings; whether the
answer is a heading structure in `decisions.md`, a per-spawn list of node numbers, or a declared label vocabulary this
effort has so far refused; and whether any of it is this effort's practice or reaches a shipped file.

*Added 2026-09-28 by the manager, the text written by [node 358](358-whether-decisions-mds-size-trigger-is-re-offered-or-retired.md)'s worker:* **`decisions.md` is 80,400 bytes**, past the ~43,847-byte anchor at which node 129's package said part (ii) would be re-offered, which is taking the file off every worker's read-whole list. The human's ground for keeping it read whole at node 129 was *"it's small enough"*, and it no longer holds. [Node 358](358-whether-decisions-mds-size-trigger-is-re-offered-or-retired.md) retired that size trigger and made this node the place where part (ii) is re-offered, in the scoped form spawns already use.

## Acceptance condition

*Authored by [node 392](392-write-the-acceptance-conditions-for-the-five-kept-nodes.md)'s worker, from the human's 2026-10-06 decision where the node has one, and filed by the manager.*

> Done when all of the following hold.
>
> 1. Each of the following four files, under `## What you read`, no longer lists `decisions.md` among the things read in full:
>    - `.claude/skills/expedition-grilling/SKILL.md`
>    - `.claude/skills/expedition-prototype/SKILL.md`
>    - `.claude/skills/expedition-precondition/SKILL.md`
>    - `.claude/skills/expedition-implementation/SKILL.md`
>
>    Before this work, each file lists it as "`decisions.md` — the sections the spawn names".
> 2. Each of those four files, under `## What you read`, states the following: the worker searches `decisions.md` for its node's terms and paths, and for any node numbers the spawn names; and the worker reads only the lines that match.
> 3. The text that states clause 2's search is byte-identical across the four files.
> 4. The paragraph beginning "Read everything the list above names in full." is byte-identical across the four files after this work, as it is before.
> 5. `.claude/skills/expedition/SKILL.md`, under `## Spawning a worker`, states that a spawn may name the node numbers whose lines in the effort's index of decisions the manager already knows bear on the node. It does not present that index as something the worker reads in full. This condition demands nothing of that section's sentence "Where the effort has a label vocabulary, scope that index by label.": it may stay, change or go.
> 6. The phrase "the sections the spawn names" appears in no file under `.claude/`.
> 7. The working tree meets the bar.
>
> Scope: on 2026-10-06, `grep -rn "sections the spawn names" .claude/` was run over the working tree. It returned one line in each of the four files of clause 1, each the list item "`decisions.md` — the sections the spawn names" under `## What you read`, and nothing else. `.claude/skills/expedition/SKILL.md` is named because it is part of the work, not because the search found it. Any instance the search reaches outside these five files is reported and not edited.

## The manager's note at filing

*Not a change to anything above.*

**This is the manager's own conduct.** The scoping instruction is in the manager's contract, the flat pointer is the
manager's wording, and it has been written the same way in every spawn this session.

**It bears directly on [node 165](165-measure-whether-a-fed-file-earns-its-place.md)'s live measurement**, whose
subject is whether a fed `decisions.md` earns its place. **Node 169's worker offered itself as evidence**, in its own
words: *"an implementation worker on a record-file node is a cheaper case to measure, and this node is a clean
negative data point."* The manager records the offer and has not folded it into node 165's protocol, whose three
pairs are fixed to grilling nodes and whose readout was fixed before the first pair ran.

## Annotation: this node's provenance miscounts its own item

*Filed by the manager from [The rule that mints a node on a repeated retrospective
item](212-the-mint-on-second-report-rule-is-defeated.md)'s worker, in that worker's own words. Nothing above is
changed, the count being the manager's error and not this node's subject.*

> Node 185's provenance reads "Minted by the manager under the map's rule that a standing retrospective item
> reported a second time becomes a node." The item it names — a spawn pointing at `decisions.md` without saying
> which sections bear on the node — is at roughly seventeen prior reports. So the single prompt application of the
> rule miscounted by an order of magnitude, and that wrong count is now the node's recorded provenance.

**The two reports named above are real and are not withdrawn**; what is wrong is *"a second time"*, and it is the
manager's sentence. **This node's subject and its urgency both go up rather than down**: an item at roughly
seventeen reports is the most-reported item on the effort after `map.md`'s whole-file read.

*The manager's note, 2026-09-28:* [node 356](356-whether-node-165s-remaining-shadow-pairs-still-run.md)'s worker reports this node's question changed. Its words, pasted: **Node 185 (open grilling):** a premise in its filing note is overtaken. That note calls node 165 a "live measurement" that the scoping practice "bears directly on". The measurement is retired, so node 185 need not protect a protocol any more. The new node above is related to it.

*The manager's note, 2026-10-06:* kept at the triage the human invoked and approved (`verbatim` *"ok"*). A read-only agent checked it against the current files and found it still live; it has no acceptance condition yet.

## Interview

#### The human's answer, 2026-10-06

*The manager put the node's question directly, after the 2026-10-06 triage kept the node. The manager's recommendation, as sent:* "the worker contracts tell the worker to search `decisions.md` for its node's terms and paths, plus any node numbers the spawn names, and read only the lines that match. The spawn may name node numbers I already know are relevant. This works on any effort, with or without labels." *Alternatives offered: the spawn alone names the relevant node numbers; add headings to `decisions.md`; declare a label vocabulary. The message ended:* "Please answer node 185. \"ok for recommended\" takes the search."

`verbatim`: *"ok"*

*The manager's note:* the reply takes the recommendation. The condition is still to be written.

## Handover, attempt 1

*Pasted as the worker handed it back, 2026-10-06.*

`````
HANDOVER:      A spawn points at the decisions index without naming which sections bear on the node

ANSWER:
The four worker contracts no longer list `decisions.md` among the files read in full. Each now tells the worker to search it. The manager's contract lets a spawn name the relevant node numbers instead of pointing at the index as something to read.

- In `.claude/skills/expedition-{grilling,prototype,precondition,implementation}/SKILL.md`, under `## What you read`:
  - The list item "- `decisions.md` — the sections the spawn names" is removed.
  - A new paragraph sits between the unchanged "Read everything the list above names in full." paragraph and "Leave `flags.md` unread. It is not yours." It reads, byte-identical in all four files:
    "Search `decisions.md` for your node's terms and paths, and for any node numbers the spawn names. Read only the lines that match."
  - It goes after the read-in-full paragraph, not inside or just after the list, so that "the list above" keeps meaning only what is read whole. `decisions.md` now falls under that paragraph's "Search the rest of the effort's record" as well, and the two do not conflict.
- In `.claude/skills/expedition/SKILL.md`, under `## Spawning a worker`, the pointer bullet now names only the worker's node file and the effort's map. A new bullet follows it:
  "The node numbers whose lines in the effort's index of decisions you already know bear on the node. The spawn may name them and need not. The worker searches that index for those numbers and for its node's own terms and paths, rather than reading it."
- The sentences "Where the effort has a label vocabulary, scope that index by label. Scoping is a filter, so the index stays a pointer." are removed. Flag 392.3 left that choice open. The search works with or without labels, and no worker contract tells a worker what to do with a label scope.
- Unchanged: graph-conventions.md's grouping of `decisions.md` lines under labels, and labels narrowing the frontier. Neither depended on the spawn sentence.
- The existing "Write a note only from context you already hold" rule already covers the "already know" in the new bullet.

INDEX LINE:    Workers search `decisions.md` for their node's terms, paths and any node numbers the spawn names, reading only matching lines; a spawn may name known-relevant node numbers; label scoping dropped.

FLAGS:
- ASSUMPTION: I removed the manager contract's label-scoping sentence and its "Scoping is a filter" follow-up rather than keeping them.
  - Grounds: the search replaces scoping on every effort. No worker contract says what to do with a label scope. The human's decision set a declared label vocabulary aside as an alternative. Labels still group `decisions.md` lines and narrow the frontier, in graph-conventions.md.
  - Index sentence: The manager contract's "scope that index by label" sentence was dropped, since workers now search `decisions.md` rather than read a scoped part of it.
- ASSUMPTION: I placed the search paragraph after the unchanged "Read everything the list above names in full." paragraph, not in the list or between the list and that paragraph.
  - Grounds: "the list above" then still names only what is read whole, and the new rule sits beside the general search rule it narrows.
  - Index sentence: The worker contracts' `decisions.md` search rule sits as its own paragraph after the read-in-full paragraph, not in the pointer list.

NEW NODES:     none

INVALIDATIONS:
- Node 129 (record token cost): its "`decisions.md` stays read whole" is contradicted. Part (ii), re-offered here, is now taken in search form.
- Node 358: what it moved into node 185 is now carried out. No contradiction.
- Node 13 (graph file format): narrowed. Its "a worker receives … `decisions.md` scoped by label", and its "a session scoped to one area reads one section", no longer describe what a spawn does. The label grouping of `decisions.md` itself still stands.
- Node 12 (subagent context contract): narrowed. Its pointer set "node file, `map.md`, and `decisions.md` scoped by label" and "Scoping a pointer is a filter instruction" are superseded. A spawn now carries the node file and the map, plus optional node numbers.
- Node 297 (manager contract rewrite, part 2): its rewording "Scoping is a filter, so the index stays a pointer." is removed.
- Node 333 (D3): it kept "- `decisions.md` — the sections the spawn names" byte-identical. That item is now gone. This is a rename of the rule, not a contradiction of 333's work at the time.
- Node 28: it cites "the sections the spawn names" as an example of binding content a spawn fills. That example no longer exists. The other examples it cites stand.
- Nodes 291, 293 and 294 (contract rewrites) carried the removed list item. It is now replaced.

CONDITIONS:
- What I searched: open nodes 13 (actually resolved), 40, 41, 185 and 317. In their `## Acceptance condition` and `## Question` sections I searched for "sections the spawn names", "scope that index by label", "Scoping is a filter", "scoped by label", "index of decisions", "label vocabulary", "What you read", "Spawning a worker", "Read everything the list above" and `decisions.md`.
- Result: no open node other than 185 matches. No replacement clauses, and no other open node's question is changed.
- For INVALIDATIONS I ran the same phrases over the resolved nodes, reading only the matches.

MISSING FROM MAP:
- The map does not say which nodes are open. I derived it from the `Status:` lines.

GATE PAYLOAD:
- Checker findings: none yet (first run).
- Bar: I looked at the worktree root. It holds `.claude`, `CONTEXT-MAP.md`, `CONTEXT.md`, `.gitignore` and `.scratch`, with no manifest and no CLAUDE.md or AGENTS.md. The repo states no build, test or format command, so the recorded "no build, no tests, no formatter" stands, and the bar is the standards plus the condition.
- Checks I ran:
  - `grep -rn "sections the spawn names" .claude/` returns nothing (clause 6).
  - The "Read everything the list above names in full." paragraph has the same md5 in all four files before and after (clause 4).
  - The new search paragraph has the same md5 in all four files (clause 3).
  - The search reached no instance outside the five files.
- Paths touched (worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/185-decisions-search, uncommitted):
  - .claude/skills/expedition-grilling/SKILL.md
  - .claude/skills/expedition-prototype/SKILL.md
  - .claude/skills/expedition-precondition/SKILL.md
  - .claude/skills/expedition-implementation/SKILL.md
  - .claude/skills/expedition/SKILL.md
- Proposed commit message:

  Workers search decisions.md instead of reading named sections

  The four worker contracts drop "decisions.md — the sections the spawn
  names" from the read-in-full list and instead search decisions.md for
  the node's terms and paths and any node numbers the spawn names, reading
  only matching lines. The manager's spawn may name the node numbers it
  already knows bear on the node; the label-scoping sentence is dropped.

  Node: graph-workflow/185

- Method skills: none invoked, so nothing was skipped.

RETROSPECTIVE
(1) What I had to hunt for:
- Whether removing the label-scoping sentence left anything without its target. I searched `.claude/` for label, index of decisions and `decisions.md`, and found graph-conventions' label grouping, which does not depend on the sentence.
- Whether `.claude/rules/expedition-triggers.md` copies the spawning text. It does not.
- The open-node list, from the `Status:` lines.
- I looked in the node file first for all three, and none was there.

(2) What arrived that this node did not need:
- `map-read-whole-for-a-few-items` (carried by 15 earlier retrospectives: 135, 178, 205, 214, 220, 284, 317, 382, 386, 387, 388, 389, 390, 391, 392). From map.md I needed only the ground rules and the six writing rules.
- `rules-file-read-whole-for-one-section` (carried by 12 retrospectives in 11 files: 178, 214, 220, 317, 382, 386, 387, 388, 390, 391, 392). I needed only the bar's commands paragraph.
- The node file's provenance, filing note and miscount annotation bore nothing on the condition.

(3) What would have made this easier:
- A spawn line listing the open node ids for the CONDITIONS search.

(4) Stale or contradicting material I read:
- `stale-number-in-the-record` (carried by 10 retrospectives in 9 files: 178, 212, 220, 382, 385, 386, 388, 391, 392). The node's question gives `decisions.md` as 80,400 bytes, and `wc -c` gave 102,204 on 2026-10-06 (for scale only).
- `question-quotes-superseded-text` (carried by 3 retrospectives: 214, 317, 392). The question quotes the manager contract as "the effort's index of decisions scoped by label where a vocabulary exists". The shipped text before this work read "Where the effort has a label vocabulary, scope that index by label."
`````

## Flags

`185.1` `ASSUMPTION` — The manager contract's label-scoping sentence was dropped. *(The worker's full text is under its handover's `FLAGS`.)*

`185.2` `ASSUMPTION` — The search rule sits as its own paragraph after the read-in-full paragraph. *(The worker's full text is under its handover's `FLAGS`.)*
