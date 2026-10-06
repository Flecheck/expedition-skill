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
