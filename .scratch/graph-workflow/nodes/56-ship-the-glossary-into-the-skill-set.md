# Ship the glossary inside the skill directory and make it state its own completeness

Type: implementation
Status: claimed

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

### The name, 2026-09-25

The manager asked, `verbatim`: *"What name should node 56 give `CONTEXT.md`?"*, recommending *"`glossary.md`, giving `.claude/skills/expedition/glossary.md`"*, with *"`expedition-glossary.md`"* as the alternative.

The human, `verbatim`: *"glossary is fine"*. This takes the manager's recommended option, `.claude/skills/expedition/glossary.md`.

## Amendment by the human, 2026-09-25

*The human chose the name above in answer to a question that said their choice would become their amendment to this condition. The manager wrote the wording below as a direct substitution. The original clauses above are left as they were.*

Wherever the acceptance condition above names `.claude/skills/expedition/CONTEXT.md`, read `.claude/skills/expedition/glossary.md`. Nothing else in the condition changes.

*The manager's note:* the substitution leaves clause 2 (a root `CONTEXT-MAP.md` linking the glossary) and clause 5 (the root `CONTEXT.md` kept as a pointer, marked superseded) as they were. Whether those two still fit a file no longer called `CONTEXT.md` is a question for this node's worker to raise, not something this amendment decides.

*The manager's note, 2026-09-26:* [node 302](302-rewrite-the-glossary.md) rewrote `CONTEXT.md` in plain English (landed `de347dc`), keeping 51 term entries and 41 `_Avoid_` lines. Its worker reported two things for this node, in its own words: "Node 56's condition section says "`CONTEXT.md` today holds exactly **50** term entries", but its clause 1, and the file, say 51." And: "`CONTEXT.md`'s intro names `.scratch/graph-workflow/nodes/`, a path specific to this effort, in a shipped file. That goes against ground rule 1. I kept it, because node 56 rewrites the file's head."

*The manager's note, 2026-09-26:* the human's "ok" to [node 328](328-group-the-open-nodes-against-the-glossary.md)'s C5 settles that this node's condition is amended before it is claimed: clause 1's exact entry count (51, and the note's stale 50) is re-pointed to the count at claim time, the stale fallback path `.claude/skills/expedition/CONTEXT.md` in other nodes is read as `.claude/skills/expedition/glossary.md`, and the conditions naming the root `CONTEXT.md` that node 328 lists (137, 120, 258, 124, 61, 109) are checked against the move. This node goes last among the glossary's changes.

## Amendment, 2026-09-27 (from node 338)

*Written by [node 338](338-say-in-graph-conventions-md-which-file-of-the-map.md)'s worker under its `CONDITIONS`, and filed by the manager after that node landed as commit `968b1ec`. Every word is fixed by the glossary's map entry and by `graph-conventions.md` as landed.*

- **Clause 4.** Where it says ground rules are "declared in its map's `## Notes`", read "declared in its map".

*The manager's note, 2026-09-27:* [node 342](342-ship-expedition-standing-yes.md)'s worker reports under its `CONDITIONS` that clause 1's counts (51 / at least 40) are stale: at `eb3b217` the root `CONTEXT.md` holds 56 term entries and 45 `_Avoid_` lines, so with clause 4's `ground rules` entry the moved file would hold 57 and at least 45. Its proposed replacement clause names the path `.claude/skills/expedition/CONTEXT.md`, which the amendment by the human above reads as `glossary.md`. The note above on node 328's C5 already re-points clause 1's count to the count at claim time, so no new amendment is filed; this note records the current figures.

## Amendment, 2026-09-27 (from node 97)

*Written by [node 97](97-write-the-adoption-procedure.md)'s worker under its `NEW NODES`, as a related defect joined to this open, unclaimed node, and filed by the manager under the rule [node 327](327-a-related-defect-joins-an-open-node-instead-of-becoming-a-new-one.md) landed. Pasted as it wrote it. Its words are fixed by this node's amendment by the human (`glossary.md`, 2026-09-25) and by node 97's work once it lands.*

- **A new clause, read under the amendment by the human that substitutes `glossary.md`.** "6a. Wherever `.claude/skills/expedition/adoption.md` names the glossary, it names `glossary.md`, the file beside it in `.claude/skills/expedition/`."

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

````
HANDOVER:      Ship the glossary inside the skill directory and make it state its own completeness

ANSWER:
The glossary now lives at `.claude/skills/expedition/glossary.md`, the name the human chose on 2026-09-25, so it ships with the skill files. The root files that still point at the old path keep working.

- **`.claude/skills/expedition/glossary.md`** (new). It is the root `CONTEXT.md` as of `07446c4`, with two changes. Clause 7 allows both of them, and nothing else differs (checked with `diff` against `git show HEAD:CONTEXT.md`).
  - *A completeness paragraph (clause 3).* It is now the first paragraph after the `# Expedition` heading, ahead of the workflow description, so the file literally opens with it before any term entry. It says the glossary is complete over the vocabulary of the files that declare it authoritative, so a term those files use has an entry. It says coining a term and writing its entry are one change. It says a term used with no entry is a defect in the change that introduced it.
  - *The old intro paragraph is rewritten into that one, with two edits to it.*
    - The path `.scratch/graph-workflow/nodes/` is dropped. It is specific to this effort and so breaks ground rule 1. Node 302's worker had left it for this node.
    - "A term is added only when the node that settles it resolves" becomes "A term is added only once a node has settled it". The old timing (the entry is added at resolution) conflicts with "coining and writing its entry are one change", because the change is committed before the node resolves.
  - *A `**Ground rules**:` entry (clause 4, as amended by node 338 to "declared in its map").* It sits right after `**Map**:`. It has three sentences and no `_Avoid_` line: the standing constraints an effort works under, declared in its map, each true of any node's work in that effort; that is what makes them safe to copy as text into a checker's spawn, since the checker does not read the map; an account of what happened is never a ground rule.
  - *Counts.* Clause 1 was re-pointed to the counts at claim time. At `07446c4` the root file held **57** term entries (`grep -c '^\*\*[^*]*\*\*:'`) and **45** `_Avoid_` lines. The new file holds **58** and **45**.
- **Root `CONTEXT.md` (clause 5).** It now holds only a heading "Superseded: the glossary has moved" and one sentence saying the file is superseded in place, with a link to `.claude/skills/expedition/glossary.md`. It has no term entries. This keeps the record's links to `../../CONTEXT.md` working.
- **Root `CONTEXT-MAP.md` (clause 2, new).** It has one bullet linking `.claude/skills/expedition/glossary.md` under the name Expedition, with one line saying what it is: the vocabulary the `/expedition` skill files are written in.
- **Pointers updated to the new file (clause 6, clause 6a, and the manager's 2026-09-24 note).**
  - `graph-conventions.md`: "the glossary (`glossary.md`, beside this file)".
  - `adoption.md`: "the glossary (`glossary.md`)".
  - The two `SKILL.md` lines in `.claude/skills/expedition/` that named `CONTEXT.md`.
  - All three files are in the same directory as `glossary.md`, so a bare file name resolves from each file's own directory. No other shipped file named `CONTEXT.md`: `grep -rn CONTEXT .claude` finds only the grilling contract's `CONTEXT:` field.
- **Whether clauses 2 and 5 still fit the new name** (the manager left this to the worker).
  - *They still fit.* The human's reason for renaming was that a host repository's own root `CONTEXT.md` could be confused with ours. That concerns the shipped copy only. The root `CONTEXT.md` and `CONTEXT-MAP.md` belong to this repository and are not shipped, so ground rule 1 does not reach them.
  - *Clause 5 still does its job:* the effort's record links `../../CONTEXT.md` in many places, and those links must keep resolving.
  - *Clause 2 is still useful:* it points readers and tools that follow the context-map convention at a glossary that no longer has the conventional name.
  - I implemented both as written, as flag 56.2.
- **The `implementer` question from the annotation.** I did not settle it here. Clause 7 forbids rewording the Checker entry, and adding a headword would break the count. It is carried as its own node under NEW NODES.
- **Bar.** The repo has no build, tests, formatter or CI. The worktree root holds only `.claude/`, `.scratch/`, `.gitignore` and the markdown files, with no manifest or task runner. That matches `map-implementation-rules.md`. The bar is its non-command half, and I held the prose to the five standing writing rules and the ground rules. No method skill was invoked, so no part of one was skipped.
- **Clause 8.** `git status` shows nothing changed under `.scratch/`.

INDEX LINE:    The glossary moves to `.claude/skills/expedition/glossary.md` with a completeness paragraph and a `Ground rules` entry. The root `CONTEXT.md` becomes a superseded pointer, and `CONTEXT-MAP.md` links the new file.

FLAGS:
- ASSUMPTION (56.2): Clauses 2 and 5 were implemented as written, without a raise. The rename's reason (confusion with a host repo's `CONTEXT.md`) concerns only the shipped copy. The root `CONTEXT.md` pointer keeps the record's many `../../CONTEXT.md` links working. `CONTEXT-MAP.md` points tools that follow the context-map convention at a file no longer called `CONTEXT.md`. Neither root file ships.
  Index: Node 56 kept a root `CONTEXT.md` pointer and a root `CONTEXT-MAP.md` after the rename to `glossary.md`, because neither ships and both keep old links and tools finding the glossary.
- ASSUMPTION (56.3): The glossary's intro is rewritten. The effort-specific path `.scratch/graph-workflow/nodes/` is dropped (ground rule 1). "added only when the node that settles it resolves" becomes "added only once a node has settled it", because the old timing conflicted with the new "coining a term and writing its entry are one change". The completeness paragraph is placed first, before the workflow description, so the file literally opens with it.
  Index: Node 56 dropped an effort-specific path from the glossary's intro and relaxed "added when the settling node resolves" to "once a node has settled it", to fit the new one-change rule.
- ASSUMPTION (56.4): The completeness paragraph is written as a rule, not as a claim that every term has an entry today. The tree still has terms used without a headword: `implementer`, in the glossary's own Checker entry and five times in the checker contract. Possibly also the markers `ASSUMPTION` and `CONDITION-WRONG`, which appear in the contracts and in the Acceptance condition entry's prose. Under the paragraph each is a defect of the change that introduced it, not of this one. I did not fix them, because clause 7 forbids rewording entries and clause 1 fixes the count. A checker at this gate may name them.
  Index: Node 56's completeness paragraph is a rule for future changes; gaps already in the tree, such as `implementer`, are left to their own node rather than fixed here.

NEW NODES:
- Name: Whether `implementer` becomes a glossary headword or leaves the shipped files
  Kind: grilling
  Question: `implementer` has no headword in `.claude/skills/expedition/glossary.md`. It is used in the glossary's own Checker entry ("the implementer never does") and in `.claude/skills/expedition-checker/SKILL.md` (five places, e.g. "the part of the work the implementer may edit"). The implementation contract names the same party "the worker holding the code". Node 56's completeness paragraph now makes a term used with no entry a defect. Should the glossary gain `implementer` as a headword, with an `_Avoid_` line if needed, or should every use become "the worker holding the code" (or "the worker") so the word leaves the shipped files? Also: are the flag markers `ASSUMPTION` and `CONDITION-WRONG` terms the glossary owes entries for?
  Blockers: this node (56).

INVALIDATIONS:
- Node 29 (shipped-file consistency): its mechanism is carried out as it describes, with one rename: the file is `glossary.md`, not `CONTEXT.md`.
- Node 14 (Naming): "terms fixed in CONTEXT.md" is renamed. The glossary is now `.claude/skills/expedition/glossary.md`, and root `CONTEXT.md` is a superseded pointer.
- Node 296 (manager contract part 1): its term list "pointing at `CONTEXT.md`" now points at `glossary.md`. This is a rename.
- Node 302 (glossary rewrite): the intro paragraph it kept is rewritten. The effort path is removed and the timing sentence is relaxed. This narrows it.
- The record, which only the manager may edit (clause 8 keeps me out of `.scratch/`):
  - `map.md`, `## Notes`, the "Skills every session should consult" line: "[`CONTEXT.md`](../../CONTEXT.md) at the repo root is the glossary".
  - `map.md`, `## Notes`, the vocabulary paragraph: "holds **51 term entries and 41 `_Avoid_` lines**" and "**That file is still at the root.**". Both are now false: the file moved and holds 58 entries and 45 `_Avoid_` lines.
  - `map-implementation-rules.md`: the bar paragraph's "`CONTEXT.md`'s `_Avoid_` lines", and the review route's "[`CONTEXT.md`](../../CONTEXT.md)'s `_Avoid_` lines" and "`CONTEXT.md`'s refused words".
  - All of these still resolve, through the pointer, but they name the old location.

CONDITIONS:
- Searched for: `CONTEXT.md`, `CONTEXT-MAP`, `glossary`, `ground rule` (case-insensitive), inside the `## Acceptance condition` and `## Question` sections of every open or claimed node except 56 (64 open and 4 claimed; the search was an awk pass over those sections).
- Node 190 (open, unclaimed): clause 1 "`CONTEXT.md`'s `_Avoid_` lines" should read "`.claude/skills/expedition/glossary.md`'s `_Avoid_` lines". Clause 2 "that `CONTEXT.md`'s refused words return false positives" should read "that `.claude/skills/expedition/glossary.md`'s refused words return false positives". The path is fixed by this node's work in the tree, the human's 2026-09-25 choice of name.
- Node 284 (open, unclaimed): in its bar sentence, "`CONTEXT.md`'s `_Avoid_` lines" should read "`.claude/skills/expedition/glossary.md`'s `_Avoid_` lines". Same source for the path.
- Node 41 (open), question changed: the entry for `FRICTION` that its worker owes under the bar now goes in `.claude/skills/expedition/glossary.md`. The completeness paragraph node 29 designed is now in place, so node 41 is the mechanism's first test as planned. Its manager-note link `[CONTEXT.md](../../../CONTEXT.md)` now reaches the superseded pointer. Its condition clause "written into that effort's ground rules in `map.md`'s `## Notes`" agrees with the new `Ground rules` entry.
- Node 130 (open), question partly answered: "keeping a glossary true as terms move" is now stated in the glossary itself.
- Nodes 84 and 208 (open), questions: `CONTEXT.md` becomes `.claude/skills/expedition/glossary.md`. This is a rename only.
- Nodes 80, 149, 156, 170, 181, 221, 253, 270, 30, 317, 83, 85 and 87 matched only on the general words "glossary" or "ground rule", or on a historical node file name. Nothing to change.
- Node 328's list (137, 120, 258, 124, 61, 109): none of them is open any more, so none turned up in the search.

MISSING FROM MAP: `map.md` gives the glossary as root `CONTEXT.md` with 51 entries and 41 `_Avoid_` lines, "counted 2026-09-10". The counts at claim time were 57 and 45. I got them by grep over the worktree (node 342's note, 56 and 45 at `eb3b217`, was also stale by one entry). Whether clauses 2 and 5 still fit was left open in the node file. I settled it myself as flag 56.2.

GATE PAYLOAD:
- Checker findings: none yet; no checker has run.
- Paths touched (worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/56-glossary`):
  - `.claude/skills/expedition/glossary.md` (new, untracked)
  - `CONTEXT-MAP.md` (new, untracked)
  - `CONTEXT.md`
  - `.claude/skills/expedition/SKILL.md`
  - `.claude/skills/expedition/graph-conventions.md`
  - `.claude/skills/expedition/adoption.md`
  - Nothing is staged. `glossary.md` was created by copying, not by `git mv`, so the manager's commit must add both untracked files.
- Proposed commit message:

  Ship the glossary as .claude/skills/expedition/glossary.md

  Move the glossary inside the skill directory so it travels with the
  skill files. Open it with a paragraph stating it is complete over the
  vocabulary of the files that declare it authoritative, and add the
  missing Ground rules entry. The root CONTEXT.md becomes a superseded
  pointer, CONTEXT-MAP.md links the new file, and the manager contract,
  graph-conventions.md and adoption.md name glossary.md.

  Node: graph-workflow/56

RETROSPECTIVE
1. What I had to hunt for: the current entry and `_Avoid_` counts, because the condition's numbers had been re-pointed "to the count at claim time" without giving the count. Also which open nodes are open: there is no list, so I derived it from the `Status:` lines. And whether any other shipped file names `CONTEXT.md`: only the three the node file and amendments mention do.
2. What arrived that this node did not need: the manager's note on node 41 sequencing and the note on 29.1, which were context rather than work. Most of `map.md`'s `## Notes`, and all of `map-implementation-rules.md` except the bar paragraph.
3. What would have made this easier: the spawn or node file stating the claim-time counts (57 and 45) and the resulting target (58 and at least 45). One line settling whether "opens with a paragraph" means literally first, or just before the first entry. And an explicit statement that the `implementer` question should become a new node rather than a raise, instead of "raise or carry as its own node, the manager has not decided".
4. What was stale, wrong or contradictory:
   - Clause 1's 51 and 40 (the file had 57 and 45).
   - The manager note's "exactly 50".
   - Node 342's "56 term entries" (57 at `07446c4`).
   - `map.md`'s 51 and 41 and "still at the root".
   - Clause 4's "`## Notes`", already amended.
   - The old intro's "added only when the node that settles it resolves" was in tension with clause 3's "one change" and was relaxed (flag 56.3).
   - The quotes in the condition still match the files: `graph-conventions.md` "the glossary (`CONTEXT.md`)", and the `SKILL.md` and `adoption.md` references were all present as described.
````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 350's check; the condition reached it as a verbatim copy in `$TMPDIR/c56.md`.*

> PASS
>
> This is the check of node 56, "Ship the glossary into the skill set". The work is in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/56-glossary`, on base 07446c4. It consists of two new untracked files, `.claude/skills/expedition/glossary.md` and `CONTEXT-MAP.md`, plus uncommitted diffs to `CONTEXT.md`, `.claude/skills/expedition/SKILL.md`, `graph-conventions.md` and `adoption.md`.
>
> I read the whole of `/tmp/claude-1000/c56.md`. I read the condition as its amendments leave it:
> - the human's substitution: `.claude/skills/expedition/CONTEXT.md` reads as `.claude/skills/expedition/glossary.md`;
> - node 338's clause 4: "declared in its map";
> - node 97's clause 6a;
> - clause 1's entry count re-pointed to the count at claim time, which the human settled at node 328's C5.
>
> I treated the annotation section as context, not as condition.
>
> **Parts of the condition**
>
> - **1:** met. `git show HEAD:CONTEXT.md` has 57 lines matching `^\*\*[^*]+\*\*:$` and 45 lines beginning `_Avoid_`. So the count at claim time is 57, plus clause 4's entry, which makes 58. `glossary.md` has 58 term lines, each holding only the bold term and a colon, and 45 `_Avoid_` lines. That meets "at least 40", and also the 45 in the current-figures note.
> - **2:** met. The root `CONTEXT-MAP.md` holds one line: "[Expedition](.claude/skills/expedition/glossary.md): the vocabulary the `/expedition` skill files are written in." The link resolves.
> - **3:** met. The paragraph before the first entry says all three things:
>   - the glossary "is complete over the vocabulary of the files that declare it authoritative, so a term those files use in this vocabulary has an entry here";
>   - "Coining such a term and writing its entry are one change";
>   - "A term used with no entry is a defect in the change that introduced it."
> - **4 (as amended):** met. `**Ground rules**:` has the same form as the other entries, with a three-sentence definition. It says the ground rules are "The standing constraints an effort works under, declared in its map, each true of any node's work in that effort". It gives that as what makes them "safe to copy as text into a checker's spawn, since the checker does not read the map". It ends "An account of what happened is never a ground rule." At HEAD there was no such entry: grepping `CONTEXT.md` for `^\*\*[Gg]round rules\*\*` returns nothing.
> - **5:** met. The root `CONTEXT.md` holds no term entry. Its whole content is the heading "# Superseded: the glossary has moved" and a pointer: "This file is superseded in place. The glossary is now [`.claude/skills/expedition/glossary.md`](…)." The link resolves from the root.
> - **6:** met. `graph-conventions.md` names the glossary in one place only: "the glossary (`glossary.md`, beside this file)". That path resolves from the file's own directory. `grep -n -i 'glossary\|CONTEXT'` finds no other mention.
> - **6a:** met. `adoption.md` now says "the glossary (`glossary.md`)". This is the file beside it. Its two other mentions ("the glossary refuses", "the glossary's words") give no path.
> - **7:** met. Running `diff` of HEAD's `CONTEXT.md` against `glossary.md` shows only two differences:
>   - the opening paragraph is rewritten to carry clause 3's statements;
>   - the `**Ground rules**:` entry is added.
>
>   No term entry and no `_Avoid_` line differs. The rewritten opening also drops the effort-specific path `.scratch/graph-workflow/nodes/`, which removes a ground-rule-1 breach. That paragraph is the one clause 3 requires, and it is not a term entry.
> - **8:** met. `git status --short .scratch` prints nothing.
> - **9:** met. See the bar below.
> - **Beyond the clauses:** `SKILL.md`'s two mentions of the glossary are re-pointed from `CONTEXT.md` to `glossary.md`. `grep -rn 'CONTEXT\.md\|glossary\.md' .claude/` finds no remaining reference to the old name.
>
> **The bar**
>
> - The worktree's `map-implementation-rules.md` records no build, tests, formatter or CI, and the repo root confirms it: there is no manifest or task runner.
> - `git diff --check` is clean (exit 0).
> - The three new or replaced files have no trailing whitespace and no line over 105 characters.
>
> **Standards.** As in my earlier checks, I read only the standards in `map-implementation-rules.md`, together with the ground rules given as text.
>
> - These bore on the work, and I found nothing against them:
>   - the ground rules. Rule 1 is better for the dropped path, and every pointer uses a relative path;
>   - the `_Avoid_` lines in `CONTEXT.md`;
>   - the writing rules;
>   - `/writing-for-agents`.
> - `/coding-principles` and `/naming` did not bear on the work. The file name `glossary.md` is the human's choice.
> - The work moves the glossary, which the standards name as `CONTEXT.md`'s `_Avoid_` lines. Every `_Avoid_` line is byte-identical in `glossary.md`, so no element moved, and the root path still leads to it.
> - No reviewing skill is named, so I ran none.
>
> NOT COVERED:
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The worktree shows no `.scratch/` change. What the main tree's record holds is outside what I was given.

### Gate — approve, `standing yes`, 2026-09-27

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and its one NOT COVERED item is the worker's bookkeeping. This settles none of the node's flags; they settle at the node closing report.

## Flags

`56.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above.* Node 97's related-defect clause 6a was added to this node's condition without asking the human first; it binds once node 97's `adoption.md` has landed.

`56.2` `ASSUMPTION` — Clauses 2 and 5 were implemented as written, without a raise. The rename's reason (confusion with a host repo's `CONTEXT.md`) concerns only the shipped copy. The root `CONTEXT.md` pointer keeps the record's many `../../CONTEXT.md` links working. `CONTEXT-MAP.md` points tools that follow the context-map convention at a file no longer called `CONTEXT.md`. Neither root file ships.

`56.3` `ASSUMPTION` — The glossary's intro is rewritten. The effort-specific path `.scratch/graph-workflow/nodes/` is dropped (ground rule 1). "added only when the node that settles it resolves" becomes "added only once a node has settled it", because the old timing conflicted with the new "coining a term and writing its entry are one change". The completeness paragraph is placed first, before the workflow description, so the file literally opens with it.

`56.4` `ASSUMPTION` — The completeness paragraph is written as a rule, not as a claim that every term has an entry today. The tree still has terms used without a headword: `implementer`, in the glossary's own Checker entry and five times in the checker contract. Possibly also the markers `ASSUMPTION` and `CONDITION-WRONG`, which appear in the contracts and in the Acceptance condition entry's prose. Under the paragraph each is a defect of the change that introduced it, not of this one. I did not fix them, because clause 7 forbids rewording entries and clause 1 fixes the count. A checker at this gate may name them.
