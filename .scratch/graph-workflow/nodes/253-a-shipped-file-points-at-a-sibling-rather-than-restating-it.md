# A shipped file points at a sibling shipped file rather than restating it, and nothing says so

Type: grilling
Status: resolved

Blocked by: none

## Answer

A shipped file points at a heading of a file its reader already reads, and restates text found in a file otherwise unread and mostly unneeded; an effort-only sixth writing rule.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The nodes it surfaced are [node 354](354-add-the-sixth-standing-rule-for-writing.md) and [node 355](355-where-the-manager-read-shipped-files-restate-one-another.md). Flags 253.1 and 253.2 settle at the node closing report.

## Question

*Minted by the manager under this effort's rule that a retrospective item naming the record is disposed of in the
report that closes its node. The question is the manager's; the finding and its ground are [node
166](166-ship-an-expedition-stop-skill.md)'s worker's.*

**The human corrected the same thing twice by hand, on one node, and no rule in this effort states it.**

At node 166's second gate they pointed at a paragraph of the new `expedition-stop` skill and said, `verbatim`:

> I think it is duplicated from the normal way the manager works, maybe try to refer to the normal way of proceding
> in the skill as to not duplicate the instructions

The worker then applied the same ground a second time, at a passage the human had not pointed at, and **declined to
apply it a third time** where a contract rule was restated in order to be overridden — all on its own judgement,
recorded as flag `166.5`.

**Node 166's worker's own statement of the gap**, `verbatim`:

> the human's correction is a rule about how a skill refers to a sibling skill, and nothing in this effort's record
> states it. The four standing rules for writing cover compression, citation and navigability;
> `/writing-for-agents` states single-source-of-truth for a document against itself. Neither says *a shipped file
> points at a sibling shipped file's heading rather than restating its content* — which is exactly what the human
> asked for twice now, first as a gate correction and now as a general instinct I was told to apply at my own
> judgement. It would be worth a standing rule, because the next shipped file will face the same choice with nobody
> to correct it.

**What is actually unsettled, and it is more than whether to write the rule down.**

- **Where the boundary sits.** The worker found one case where the ground does *not* apply: a passage that restates
  a contract rule **in order to suspend it**, which is unreadable without the rule being named. Any rule written
  here has to carry that exception or it will be applied wrongly.
- **What a pointer may name.** The worker pointed at **headings** of the manager's own contract rather than at a
  path, on the ground that its reader already holds that contract — and the checker accepted that as satisfying the
  effort's ground rule 2, which requires each shipped contract to stand alone rather than depend on a skill being
  invocable. Whether a heading citation is always safe, and what happens when the pointed-at heading is renamed, is
  not settled: node 166's file now depends on four headings' wording in a file four other open nodes edit.
- **Whether it binds this effort only, or ships.** Under the map's rule a standing rule binds this effort once
  written in the map, and reaches a shipped file only where the human says so. This one is *about* the shipped
  files, which makes the distinction load-bearing rather than formal.

## The manager's note at filing

*Not a change to anything above.*

**The manager has not written the rule and is not proposing wording.** It records only what it holds: it carried the
human's ground into the correction-round spawn as *"the same instinct may apply elsewhere in the file … but that is
your judgement and a flag if you take it"*, which is what produced flag `166.5` — so the one piece of evidence about
where the boundary sits exists because the manager declined to draw it.

**Two shipped files already point at each other today**, and neither does it under a rule: `expedition-stop`'s four
citations of the manager's contract, landed at `f22dd5c`, and the worker contracts' existing instruction to read
`graph-conventions.md`. Whatever is decided here reaches both.

## Interview

#### Questions 1 to 3, relayed 2026-09-27

*Pasted as the worker handed it back.*

```
NODE:          A shipped file points at a sibling shipped file rather than restating it, and nothing says so (253)
ABOUT:         This node decides whether "point at the other file's heading, don't repeat what it says" becomes a written rule, where the rule stops, and whom it binds. It comes up now because you gave token use priority and asked for the skills to be compacted, and this rule is what makes files shorter without losing anything.
SO FAR:        I read the node, map.md, the decisions.md lines on the topic, nodes 50, 312 and 166 (flag 166.5), flag 289.4, the five writing rules in map-implementation-rules.md, and the shipped tree as it stands on master.
               - What the rule is about. At node 166's gate you told its worker to point at the manager's normal procedure rather than repeat it. The worker then did the same once more on its own judgement. It declined a third time, at a sentence that repeats the manager's top-up rule in order to switch it off, because that sentence cannot be read without the rule it switches off. No written rule covers this. Writing rule 2 is about record items citing nodes, and rule 4 is about citing by heading rather than by line number.
               - What already happens, with no rule behind it. Pointing happens only between files the manager reads. Node 312 split the rules shared by expedition/SKILL.md and graph-conventions.md into one file each, with one-line pointers to headings, and you approved it. expedition-stop, expedition-standing-yes and expedition-cleanup point at headings of the manager's contract or of graph-conventions.md.
               - Worker contracts point at nothing. They repeat shared blocks on purpose: at node 50 you said "keep them duplicated", on the ground that each worker reads only one contract, so the repeated text never costs any single reader anything. So a pointer only saves tokens when the reader already reads the file it points at, which lines up with ground rule 2 (each worker contract stands alone). I do not propose reopening node 50. Removing repeats across the worker contracts would make no worker's read shorter.
               - The node file is out of date on one point. It says the worker contracts "instruct to read graph-conventions.md". None does today (grep: 0 hits in all six worker contracts).
               - Renamed headings. Pass 289 guarded against them only as its own worker's assumption (flag 289.4): a heading whose exact text appears in another shipped file or in the live map files keeps that text. Node 313's script checks this, but only for the rewrite nodes. Nothing standing covers it. Node 29 part 3 ("ok for 29") already refused new mechanical checks.

Q1. What the rule says, and where it stops
ASK:           Should the rule be: a shipped file points at a heading of another shipped file wherever its reader already reads that file, and restates otherwise, with the exception for a passage that switches a rule off for its own case?
RECOMMENDED:   Yes, in this wording: "Where a shipped file's reader is already told to read another shipped file, point at that file's heading instead of restating what it holds. A worker contract restates what it needs, because its reader reads no other shipped file. A passage that changes a rule for its own case names the rule by heading and states the change in its own words." This matches all three cases on record: node 312's split, expedition-stop's pointers, and node 50's duplication. It also covers the case the 166 worker declined, since expedition-stop can now say "the top-up rule under <heading> does not apply; leave the counts below" and no longer repeats the rule.
ALTERNATIVES:  - Point everywhere, worker contracts included. This reopens node 50, conflicts with ground rule 2, and saves no reader any tokens.
               - Write no rule and leave it to each worker's judgement plus correction at the gate. Nothing stops the next file from repeating content.
               - Point only by path, never by heading. The reader then opens a whole file for one rule.

---

Q2. Whom it binds
ASK:           Should the rule bind this effort only, as a sixth writing rule in map-implementation-rules.md, rather than being written into a shipped file?
RECOMMENDED:   This effort only. The rule governs how the workflow's own files are written, and on any other effort those files are never edited, so a shipped copy would never be used there. The writing rules file is read by exactly the implementers and checkers who edit shipped files. It sits beside rule 4 (cite by heading), which it builds on.
ALTERNATIVES:  - Ship it in the manager contract, so any effort that edits the skills gets it. That is extra prose in every manager's read for a case only this effort has.
               - Put it in map.md's standing preferences. Every worker would read it, but only implementers act on it.

---

Q3. When a heading that another file points at is renamed
ASK:           Should the rule also say that a heading another shipped file points at may be renamed only in the same change that updates every citation of it, found by searching the shipped files for the heading's exact text?
RECOMMENDED:   Yes, as one more sentence of the same rule. It turns pass 289's assumption into a standing rule at the cost of one sentence. It adds no mechanical check, so it stays within node 29 part 3. It also protects expedition-stop, whose four heading citations point into a file other open nodes edit.
ALTERNATIVES:  - Freeze cited headings, so they are never renamed. This blocks legitimate rewrites.
               - Add a mechanical check. You refused that at node 29 part 3.
               - Say nothing, leave broken pointers for the checker to catch, and accept that a rename passes silently.
```

*The manager's note, 2026-09-27:* Q2 recommends a sixth writing rule in `map-implementation-rules.md`. [Node 349](349-whether-the-five-standing-rules-for-writing-reach-other-workers.md)'s question, which is in front of the human first, is whether the five writing rules move from that file to `map.md`. Its answer may change where Q2's rule would go.

#### The human's answer to questions 1 to 3, 2026-09-27

The human, `verbatim`: *"ok but when it's a file that would not be read and where there is a lot otherwise not useful information, it can be useful to duplicate to prevent reading useless information"*. The "ok" takes the worker's recommendations on Q1 ("Yes, in this wording: …"), Q2 ("This effort only.") and Q3 ("Yes, as one more sentence of the same rule."). The rest adds a qualification to Q1's rule, in the human's own words above. The manager does not read it as choosing among the offered options, and relays it to the worker unaltered.

## Handover, attempt 1

*Pasted as the worker handed it back.*

````
HANDOVER:      A shipped file points at a sibling shipped file rather than restating it, and nothing says so

ANSWER:
**A shipped file points at a heading of another shipped file where its reader already reads that file. Where the reader does not, it restates what it needs if the other file is mostly text that reader does not need.** This is this effort's rule only: a sixth standing rule for writing, held with the other five. It is not written into any shipped file.

The rule, as it will be written:

> 6. **Point at a heading of another shipped file instead of restating what it holds, where the reader is already told to read that file.** Where the reader is not, restate what the reader needs when the file pointed at is mostly text that reader does not need, so the reader is not sent to read it. A passage that changes a rule for its own case names that rule by heading and states the change in its own words. Rename a heading that another shipped file cites only in the change that updates every citation of it, found by searching the shipped files for the heading's exact text.

How it was reached. The payload put three questions, each with a recommendation:
- Q1: point where the reader already reads the target, restate otherwise, with an exception for a passage that switches a rule off.
- Q2: bind this effort only, as a writing rule.
- Q3: rename a cited heading only in the change that updates every citation.

The human's reply, `verbatim`: *"ok but when it's a file that would not be read and where there is a lot otherwise not useful information, it can be useful to duplicate to prevent reading useless information"*.

- **"ok"** is assent without naming a question, so it settles all three recommendations.
- **The "but" clause refines Q1.** Restating is justified when following the pointer would make the reader open a file it would otherwise not read, mostly full of text it does not need. The rule's second sentence states exactly that. Pointing stays allowed where the target would not otherwise be read but its text is small and relevant.

What the rule is consistent with, as the tree stands on 2026-09-27:
- **Node 312:** `expedition/SKILL.md` and `graph-conventions.md` state each shared rule once, with one-line heading pointers. Both are read by the manager.
- **The manager-invoked skills** (`expedition-stop`, `expedition-standing-yes`, `expedition-cleanup`) point at headings of the manager's files.
- **Node 50's "keep them duplicated":** the six worker contracts point at no other shipped file (grep for `graph-conventions` over them returns 0). Each worker reads one contract, and any other contract would be mostly text that worker does not need.
- **Ground rule 2:** each shipped worker contract stands alone.

The exception resolves the case node 166's worker declined (flag `166.5`). A passage that suspends a rule does not restate the rule. It names it by heading and says what changes.

The rename sentence turns into a standing rule what pass 289 applied only as an assumption (flag `289.4`: cited headings keep their text). It allows a rename provided every citation moves with it, and adds no mechanical check, which node 29 part 3 refused.

**Where it is written.** The writing rules sit wherever the effort holds them. Once node 352 lands, that is the list in `map.md`'s ground-rules block. So the checker receives this rule as text in its spawn along with the rest of that block.

INDEX LINE:    A shipped file points at a heading of a file its reader already reads, and restates text found in a file otherwise unread and mostly unneeded; an effort-only sixth writing rule.

FLAGS:
- ASSUMPTION: I read "ok but …" as a bare assent that settles all three recommendations, with the "but" clause refining Q1 rather than rejecting it. The rule's second sentence carries the refinement. The human named no question. Under the contract, a bare "ok" settles every recommendation in the payload, and the clause that follows addresses only Q1's content (when to duplicate).
  Index: Node 253 read the human's "ok but …" as assent to all three recommendations, with the "but" refining when restating beats pointing.
- ASSUMPTION: Q2 recommended `map-implementation-rules.md` as the rule's home. After the questions were asked, node 352 began moving the five writing rules from that file into `map.md`'s ground-rules block. I placed the rule with the writing rules wherever they are held, which will be `map.md` once 352 lands. What the human assented to was "this effort only, as a sixth writing rule", and the file named was only where those rules lived at the time.
  Index: Node 253's rule goes with the writing rules into map.md's ground-rules block, not the rules file Q2 named, because node 352 moves them.

NEW NODES:
1. Name: Add the sixth standing rule for writing: point at a heading of a file the reader already reads.
   Kind: implementation
   Question: Write node 253's rule as the sixth standing rule for writing, in the list that holds the other five.
   Blockers: node 352. The rule goes into the list 352 creates, and 352 is claimed, so its condition cannot take this clause.
   Acceptance condition:
   > The work is `.scratch/graph-workflow/map.md`, `.scratch/graph-workflow/map-implementation-rules.md` and `.scratch/graph-workflow/map-history.md`, and no other file may be edited. The worker may not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
   >
   > Done means all of the following are true of the finished tree.
   > 1. In `map.md`'s `## Notes`, the numbered list of this effort's standing rules for writing, inside the block that begins with the bold line "**Ground rules for this effort.**", ends with a sixth rule, word for word as below. Rules 1 to 5 of that list are not reworded, renumbered or reordered.
   >    6. **Point at a heading of another shipped file instead of restating what it holds, where the reader is already told to read that file.** Where the reader is not, restate what the reader needs when the file pointed at is mostly text that reader does not need, so the reader is not sent to read it. A passage that changes a rule for its own case names that rule by heading and states the change in its own words. Rename a heading that another shipped file cites only in the change that updates every citation of it, found by searching the shipped files for the heading's exact text.
   > 2. The list's bold lead-in links `nodes/253-a-shipped-file-points-at-a-sibling-rather-than-restating-it.md` as the node that fixed the sixth rule. Wherever the lead-in gives the number of rules, it says six.
   > 3. No sentence in `map.md`, `map-implementation-rules.md` or `map-manager-only.md` gives the number of this effort's standing rules for writing as four or five.
   > 4. Every text this work removes from `map.md` or `map-implementation-rules.md` is appended verbatim to `map-history.md`, under a heading that mirrors the section it came from, with struck-through text staying struck through. `map-history.md` gains text and loses none.
   > 5. Every markdown link in the three files resolves to a path that exists.
   >
   > Scope search for clause 3: `grep -rn -i "rules for writing" .scratch/graph-workflow/map.md .scratch/graph-workflow/map-implementation-rules.md .scratch/graph-workflow/map-manager-only.md .claude/skills`. Run over the working tree on 2026-09-27, before node 352 landed, it returned 1 line in `map.md` (the paragraph beginning "The five standing rules for writing anything in this effort") and 3 matches in `map-implementation-rules.md` (the bar paragraph, and the review route paragraph twice). It returned none in `map-manager-only.md` or `.claude/skills`. Node 352 moves these lines, so the worker re-runs the command on the tree it starts from and edits every match in the three editable files. A match the search reaches in any other file is reported, not edited.
2. Name: Where the manager-read shipped files restate one another.
   Kind: research
   Question: Under node 253's rule, which passages in the files the manager reads (`expedition/SKILL.md`, `graph-conventions.md`, `adoption.md`, `wayfinder-divergences.md`, `expedition-stop`, `expedition-standing-yes`, `expedition-cleanup`) restate a heading of another of those files that the same reader already reads, and what would pointing save, in words? This includes `expedition-stop`'s `## New work stops`, which suspends the top-up rule without naming its heading (see INVALIDATIONS).
   Blockers: new node 1 above.
   Offered because of the human's priority on compaction. I did not ask it: the reply did not reach it, and whether and when to work it is the manager's call.

INVALIDATIONS:
- Node 166 (flag `166.5`), a narrowing. The worker declined to point at `## Start no new node`, because the passage restates the top-up rule in order to suspend it. The new rule keeps the exception but changes its form: such a passage names the suspended rule by heading and states the change in its own words. It no longer restates the rule. `expedition-stop`'s current text ("When a node finishes, leave the effort's counts below their numbers rather than starting work to bring them back up.") states the change but names no heading. That is a defect under the new rule. I folded it into new node 2 and did not file it separately.
- Node 289 (flag `289.4`), an extension that also narrows. Its pass-time assumption, that a heading cited elsewhere keeps its text, becomes a standing rule in a looser form: a cited heading may be renamed in the same change that updates every citation.
- Node 50: no change. Its duplication of the worker contracts' shared blocks is what the new rule's second sentence prescribes.

CONDITIONS:    I searched the `## Acceptance condition` and `## Amendment` sections of every open and claimed node for "restat", "duplicat", heading rename or citation, "cited heading", "writing rules", "five standing rules" and "standing rules for writing".
               Matches: 152, 156, 190, 230, 284, 352.
               - 152, 156 and 230 concern record text, not shipped files. My rule does not touch them.
               - Node 352 (claimed) is the blocker of new node 1. Its clause 1 fixes a lead-in whose count my work changes. The change is placed in new node 1 and not in 352's condition.
               - Node 190 (open, unclaimed): clause 4, and clause 1 as amended by node 348, say "five standing rules for writing". Once new node 1 lands, "five" is wrong. I write no replacement now, because "six" is fixed by no resolved node or landed work yet. The manager owes this replacement when new node 1 lands.
               - Node 284 (open) already says "four standing rules for writing", which node 289 made stale. That is not caused by my work. Noted only.

MISSING FROM MAP: - map.md does not say which shipped files each reader reads (the manager: its contract, `graph-conventions.md` and the three invoked skills; a worker: its one contract). The whole boundary rests on this. I derived it by grepping the shipped tree for cross-file references.
                  - map.md did not say that the writing rules' location was changing. The manager's note supplied that.

Skipped method-skill parts: none. I invoked no method skill.

RETROSPECTIVE
1. What I had to hunt for:
   - Whether any rule already covered pointing. I had to find writing rules 2 and 4 in `map-implementation-rules.md`, since the spawn named only map.md and decisions.md.
   - The precedents: node 50's answer and node 312's split. The decisions.md index lines led to them, but their grounds were only in the node files.
   - How renamed headings are handled today (flag `289.4`, node 313's script).
   - Which shipped files point at which, by grep.
2. What arrived that this node did not need: nothing significant. The reading list was small and fit the node.
3. What would have made this easier:
   - The spawn naming flag `289.4` and nodes 50 and 312 as the three standing precedents on pointing versus duplicating.
   - The spawn naming the file that holds the writing rules, which is where the new rule had to land.
   - The node file saying which files each reader reads.
4. What was stale, wrong or contradictory:
   - The node file's "the worker contracts' existing instruction to read `graph-conventions.md`" is false today: no worker contract names that file.
   - Q2's placement went stale between the payload and the answer, because node 352 started moving the writing rules out of `map-implementation-rules.md`.
   - Node 284's condition still says "four standing rules for writing".
````

## Flags

`253.1` `ASSUMPTION` **· settled** — I read "ok but …" as a bare assent that settles all three recommendations, with the "but" clause refining Q1 rather than rejecting it. *(The worker's full text is under its handover's `FLAGS`.)*

`253.2` `ASSUMPTION` **· settled** — Q2 recommended `map-implementation-rules.md` as the rule's home; the rule goes with the writing rules wherever they are held. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-09-27:* flags 253.1 and 253.2 settle at the node closing report that closes this node.
