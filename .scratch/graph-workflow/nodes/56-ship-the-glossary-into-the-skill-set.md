# Ship the glossary inside the skill directory and make it state its own completeness

Type: implementation
Status: open

## Question

The glossary is the file the shipped documents declare authoritative for every term, and it sits at the
repository root rather than in the shipped set — so copying `.claude/skills/` to another repository carries none
of it, and the pointer there resolves to **that** repository's own root `CONTEXT.md` instead. Move it inside the
skill directory, leave the root path resolving, and make the file state the property that lets a blind checker
report a term shipped with no entry. Take the one missing entry that is already known while the file is open.

Reported by [What keeps the shipped files consistent when a decision changes a
term](29-shipped-file-consistency.md)'s worker, which wrote the acceptance condition below. **The human assented
to all three parts of the mechanism** before it was written: *"ok for 29"*, then *"ok for the recommandations"*.

**Why the completeness paragraph is the whole mechanism.** The blind checker's contract carries the hard rule
*"A property nobody stated is not a finding."* The duty to add a glossary entry is stated nowhere, so the one
party that reads a shipped file cold is **forbidden** from reporting a term with no entry — which is why both
live absences were found by the manager reading a condition by hand. Clause 3 converts that miss into one the
checker **must** report, and it reaches the checker on the bar, so no acceptance condition ever mentions it.

## Acceptance condition

Done when all of the following hold.

1. `.claude/skills/expedition/CONTEXT.md` exists and is the glossary: **51** term entries, each written as a
   line holding only the term in bold followed by a colon, and **at least 40** lines beginning `_Avoid_`.
2. The repository root holds `CONTEXT-MAP.md`. It links `.claude/skills/expedition/CONTEXT.md` and says in one
   line what that context is.
3. `.claude/skills/expedition/CONTEXT.md` opens, before its first term entry, with a paragraph stating all three
   of these: that the glossary is complete over the vocabulary of the files which declare it authoritative, so
   that a term those files use in this vocabulary has an entry in it; that coining such a term and writing its
   entry are one change; and that a term used with no entry is a defect in the change that introduced it.
4. That file holds an entry for **ground rules**, in the same form as its other entries — the term in bold, then
   a definition of one to three sentences — stating all three of these: that they are the standing constraints
   an effort works under, declared in its map's `## Notes`; that they are true of any node's work in that
   effort, which is what makes them safe to copy as text into a checker's spawn, the checker reading no map; and
   that an account of what happened is never one.
5. The repository root still holds `CONTEXT.md`. It holds no term entry, its whole content is a pointer to
   `.claude/skills/expedition/CONTEXT.md`, and it is marked as superseded in place rather than emptied — so that
   a link to the root path still resolves to a file that says where the glossary went.
6. Wherever `.claude/skills/expedition/graph-conventions.md` names the glossary, the path it gives resolves to
   `.claude/skills/expedition/CONTEXT.md` from that document's own directory, and not from the repository root.
7. No term entry's wording changes, and no `_Avoid_` line is removed, other than the entry clause 4 requires and
   the paragraph clause 3 requires.
8. No file under `.scratch/` is changed by this work.
9. The working tree meets the bar.

### What the manager owes whoever claims this

*The manager's own note, not a change to the condition above.*

**The two counts in clause 1 are verified.** `CONTEXT.md` today holds exactly **50** term entries matching
`^\*\*…\*\*:` and exactly **40** `_Avoid_` lines. So clause 1's **51** is 50 plus the `ground rules` entry
clause 4 requires, and *"at least 40"* permits the new entry to carry an `_Avoid_` line or not. **`ground rules`
has no entry today** — verified, `grep '^\*\*[Gg]round rules\*\*' CONTEXT.md` returns nothing — which is one of
the two absences this whole node exists because of.

**Clause 8 puts this node's own graph file out of scope, which means the map corrections are the manager's.**
Two are owed and neither is this work's: `map.md`'s *"forty terms"* becomes fifty, and its *"declares neither"*
sentence is superseded by the declared ground-rules block. The manager made both at node 29's resolution.

**One sequencing constraint, and it is the mechanism's first real test.** [Ship the FRICTION flag and the
self-edit disclosure duty](41-ship-the-friction-flag.md) is now `Blocked by:` this node. It coins `FRICTION` and
its own condition never mentions the glossary, so **landing it second means its worker owes the entry under the
bar** — without the condition being amended and without the manager writing it. If that fails, clause 3's
paragraph is not doing the work this node claims for it.

**And one thing this node does not claim, flagged as `29.1` on the node that reported it.** Shipping the
glossary makes it reachable **inside the shipped set**, not **by a worker**: no `SKILL.md` points at anything in
`.claude/skills/expedition/`, and that directory holds no `SKILL.md` of its own. Nothing in this condition fixes
that, and it was deliberately routed to the manager's own unwritten skill rather than minted as a node.

## Annotation: `implementer` is used in the glossary's own prose and is not a headword

*Filed by the manager at [What a finding must carry so it can be swept](71-what-a-finding-must-carry.md)'s check,
on the human's word. Not a change to anything above.*

Node 71's blind checker reported that the checker contract had gained *"the implementer"* — *"the part of the work
the implementer may edit"* — and that `CONTEXT.md`'s actors are Manager, Worker and Checker. It routed this as a
question rather than a finding, correctly: the wording is that node's acceptance condition's own and so was not its
worker's to depart from.

**The premise is narrower than the checker could establish.** `CONTEXT.md` already uses the word in its own prose,
inside the **Checker** entry: *"Started by the manager and never by the implementer, because whoever spawns it
chooses what it sees."* So the word is not new to the shipped corpus and names no new party. What is true is that
**it is used and is not a headword** — and the checker contract's own `## Words used exactly` does not carry it
either, while `.claude/skills/expedition-implementation/SKILL.md` names the same party as *"the worker holding the
code"*.

**What is open, therefore:** whether the glossary gains `implementer` as a headword with an `_Avoid_` line, or
whether both uses become *"the worker holding the code"* and the word leaves the corpus. Nothing turns on it today.

**The human's word**, `verbatim`: *"ok"*, on the manager's recommendation that it not be settled now and be picked
up by this node, which is already moving that file. **This is not an addition to this node's acceptance condition**
— it is one more entry-level question for whoever claims it, to raise or to carry as its own node, and the manager
has not decided which.

## The human's direction, 2026-09-24

`verbatim`, at node 296's gate: *"approve, we will fix the glossary issuea after, I think we need to rename the file in node 56"*. The manager had put it to them, `verbatim`: *"Node 56: keep its `CONTEXT.md` name inside the skill folder, or amend it to a distinct name such as `glossary.md`?"*. The reason given was that a host repository's own root `CONTEXT.md` can be confused with ours.

*The manager's note:* the direction is to rename, and the new name is not yet chosen. This node's condition names `.claude/skills/expedition/CONTEXT.md` throughout, so it is amended by the human before it is claimed. Since node 296 landed (`6745f37`), `.claude/skills/expedition/SKILL.md` also points at `CONTEXT.md` by name, beside `graph-conventions.md`, so the rename re-points both.
