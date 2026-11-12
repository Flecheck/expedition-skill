# Port into the root `CLAUDE.md` the rule that node files are written for agents

Type: implementation
Status: superseded
Superseded by: 05

## Question

*Superseded on 2026-11-12, with its acceptance condition: the human moved the decision to [node 05](05-whether-to-port-three-lost-graph-workflow-rules.md). See `### Gate 2 — reject` under `## Review`.*

*Written by the manager.* This lets every agent that starts in this repository, on any effort, know
that an effort's node files are written for the next agent and not for the human, and that the human
works from the manager's chat and the diff. Today that rule lives only in the closed `graph-workflow`
effort's map, which binds no later effort.

The human, `verbatim`, 2026-11-11, answering the manager's list of rules lost between
`.scratch/graph-workflow/map.md` and the root `CLAUDE.md`, where this rule was item 4: *"rules:
4 -> port it"*.

The rule, as `.scratch/graph-workflow/map.md` states it under `## Notes`:

> **The node files are written for agents. The human works from the manager's chat and from code
> review.** Their words, `verbatim`, at [Carry the recorded deltas into the shipped skill
> files](nodes/26-carry-deltas-into-shipped-files.md)'s gate: *"I expect the nodes to be mostly
> targeted to agents, as I will mostly work from what the manager says (questions from subagents) and
> with code review."* **Narrowed by document class** at [What the token findings change in the
> workflow and its skills](nodes/53-what-token-findings-change.md). Over **node files** it stands
> exactly as written: that reader is the next agent, claiming that node and needing it whole, so
> completeness for an agent beats brevity for a human. Over the **shipped worker contracts** it stands
> on a different ground — they are mostly format-bearing instruction text, which compresses badly — so
> what may be compressed there is the prose explaining why, and never the named shapes. Over
> **`map.md`** it does not reach: this file's reader is not the next agent in the singular but every
> worker on every node, each needing a different fraction. And **the human's two interfaces are the
> manager's chat payload and the diff**, which is why both must stand alone.

## Acceptance condition

*Superseded with the node, on 2026-11-12. It binds no work.*

*Written by the manager.* Scope: the named place is the work, and the scope came from no search. The
one file this work may change is `CLAUDE.md` at the repository root. Any other file found to need a
change is reported, not edited.

1. `CLAUDE.md` states that the node files of an effort, under `.scratch/<effort>/nodes/`, are written
   for agents rather than for the human.
2. `CLAUDE.md` states that a node file's reader is the next agent, which claims that node and needs it
   whole, so in a node file completeness for that agent comes before brevity for a human.
3. `CLAUDE.md` states that this does not reach an effort's map files, whose reader is every worker on
   every node, each needing a different part.
4. `CLAUDE.md` states that the human works from two things, the manager's messages in the chat and the
   diff, so each of the two stands alone.
5. `CLAUDE.md` quotes the human's words word for word: *"I expect the nodes to be mostly targeted to
   agents, as I will mostly work from what the manager says (questions from subagents) and with code
   review."*
6. No other sentence of `CLAUDE.md` changes in meaning.

*Manager's note, reading the condition back against `### Acceptance condition` under
`## The node file` in `graph-conventions.md`:* it is self-contained and states what must be true in
its own words; its one path is relative to the repository root; it states that its scope came from no
search, because the named place is the work; it makes no demand about the record as a whole; and every
demand is fixed by the human's words above and by the map rule quoted in `## Question`. The map rule's
clause on the shipped worker contracts is left out, because the root `CLAUDE.md`'s writing rule 1,
"Compress the prose that explains why. Never compress the shapes.", already states it. Where the new
text goes in `CLAUDE.md`, and its wording, are the worker's.

## Flags

`04.1` `ASSUMPTION` **· settled** — *Manager's note: withdrawn by the worker after checker run 1; the work no longer makes this judgement. See `## Review`.* I defined the condition's "map files" as `map.md` and the `map-*.md` files beside it, which is wider than the source rule's single `map.md`. The rule quoted from `.scratch/graph-workflow/map.md` exempts only `map.md`. Clause 3 of the condition says "an effort's map files, whose reader is every worker on every node". Every worker reads `map.md`. Only some workers read the `map-*.md` siblings, such as `map-implementation-rules.md`, and only the manager reads `map-manager-only.md`. So the stated reason ("every worker on every node") fits `map.md` exactly, and fits the siblings only loosely. I followed the condition's plural and named the files so that `decisions.md` and other record files are not swept in. If the human means `map.md` alone, the fix is to change that bullet to "an effort's map, `map.md`".

`04.2` `ASSUMPTION` **· settled** — I wrote "the manager's messages in the chat" rather than the source's "the manager's chat payload", because the glossary refuses `payload` for the handover concept. "Messages" is the condition's own word.

`04.3` `ASSUMPTION` **· settled** — The new item 7 sits in a list headed for the files under `.claude/skills/`, but it governs files under `.scratch/`. I placed it there because the human named "the list of general writing rules", and that list is it. Its writing rules 2 and 3 already govern the effort's record rather than the skill files. Item 7 also names its own files, so no reader takes it to govern the skill files.

## Handover, attempt 1

The worker's handover, as it wrote it:

```
ANSWER:        The root `CLAUDE.md` now has a section `## Who reads an effort's node files`. It sits between `## What this repository holds` and `## Commands`. I put it there because it is about the effort's record, which the section before it introduces. The section is four bullets and one line quoting the human:
                - The node files of an effort, under `.scratch/<effort>/nodes/`, are written for agents rather than for the human. (clause 1)
                - A node file's reader is the next agent, which claims that node and needs it whole. So in a node file, completeness for that agent comes before brevity for a human. (clause 2)
                - The rule does not reach an effort's map files, `map.md` and the `map-*.md` files beside it. Their reader is every worker on every node, and each worker needs a different part of them. (clause 3)
                - The human works from two things, the manager's messages in the chat and the diff, so each of the two stands alone. (clause 4)
                - The human's words, quoted word for word as clause 5 requires.
                No other line of `CLAUDE.md` changed (clause 6). The diff adds 9 lines and removes none.
                Two wording choices. First, I wrote "messages" where the graph-workflow map says "chat payload", because the glossary refuses `payload` for the handover concept. Second, I defined "map files" as `map.md` plus the `map-*.md` files beside it. That keeps `decisions.md` and other files of the record out of the exemption. Following the condition's word, it also widens the source's "`map.md`" to cover the map's sibling files.
                The bar: I confirmed that the repository has no build, test, formatter or CI. The tree holds no build manifest or CI configuration, and the root `CLAUDE.md` `## Commands` says the same. This matches `map-implementation-rules.md`. So there was no command to run, and the bar is the standards plus the condition.

INDEX LINE:    The root `CLAUDE.md` gains `## Who reads an effort's node files`: node files are written for the next agent and completeness comes first there; map files are exempt; the human works from the chat and the diff.

FLAGS:         (filed under ## Flags above, as 04.1 and 04.2)

NEW NODES:     none

INVALIDATIONS: none

CONDITIONS:    I searched the open nodes 01, 02, 03 and 05 and `decisions.md` (which is empty) for "written for agents", "node files" and "CLAUDE.md". Only node 05 matched. Its question weighs porting three other graph-workflow rules into the root `CLAUDE.md`. My work does not change that question. The file it would edit now also holds the new section, which could be relevant if node 05 places a rule nearby. I wrote no replacement clauses.

MISSING FROM MAP: none

GATE PAYLOAD:  The checker has found nothing yet.
               Path touched: `CLAUDE.md` at the root of the worktree (`/home/ten/Projects/expedition-skill/.scratch/manager-own-choices/worktrees/04-port-the-node-files-rule/CLAUDE.md`). Nothing else.
               No other node of this effort is written against a moved file.
               Proposed commit message:
                 CLAUDE.md: node files are written for agents

                 Port from the closed graph-workflow map the rule that an effort's node
                 files are written for the next agent, that map files are exempt, and
                 that the human works from the manager's chat and the diff.

                 Node: manager-own-choices/04
```

## Review

### Checker run 1 — `FAIL`, the acceptance condition

The checker's entry, as it wrote it:

```
FAIL: acceptance condition

Entry 1: the work's definition of "map files" makes its statement for part 3 false and contradicts sentences that already stand
- Instances: the added bullet reads *"This rule does not reach an effort's map files, `map.md` and the `map-*.md` files beside it. Their reader is every worker on every node, and each worker needs a different part of them."* By widening "map files" to every `map-*.md`, the work claims that every worker on every node reads those files. Three texts I read say otherwise:
  - An unchanged sentence of the same `CLAUDE.md`, under `## What this repository holds`: *"An effort's map is the file `map.md` in that directory. Its sibling files hold what only some readers need."*
  - The `**Map**` entry of `.claude/skills/expedition/glossary.md`: *"Material that only one kind of reader acts on is kept in another file beside that part."*
  - The opening of `.scratch/manager-own-choices/map-implementation-rules.md`, a `map-*.md` file: *"An implementation node's worker and its checker read this file."* `map-manager-only.md`, which the root `CLAUDE.md` cites, also names a single reader in its own filename.

  The condition's own words do not force this. Part 3 says only "an effort's map files". The widening is the worker's choice (flag `04.1`), so this is a place the work made wrong, namely a statement the work now contradicts. It is not a defect of the condition. Narrowing the bullet to `map.md`, which is what `CLAUDE.md` itself calls an effort's map, makes part 3 true without contradicting anything.
  How found: read the diff (`git diff` in the worktree), then the glossary `**Map**` entry, the unchanged `CLAUDE.md` lines, and the first line of `map-implementation-rules.md`.
- Form: a sentence added by the work that gives a reader set ("every worker on every node") to a file set containing a file that the repository says has some other, narrower reader set.
- Extent: `grep -n 'map-\*\.md\|map files\|Their reader' CLAUDE.md`, run in `/home/ten/Projects/expedition-skill/.scratch/manager-own-choices/worktrees/04-port-the-node-files-rule`. Within the file the worker may edit, it lists the one added bullet.

Parts of the condition, each established on the diff (`git diff` and `git diff --numstat`, which gives `9 0 CLAUDE.md`):
1. Met. The added bullet reads *"The node files of an effort, under `.scratch/<effort>/nodes/`, are written for agents rather than for the human."*
2. Met. *"A node file's reader is the next agent, which claims that node and needs it whole. In a node file, completeness for that agent therefore comes before brevity for a human."*
3. Stated, but false as worded. See Entry 1.
4. Met. *"The human works from two things: the manager's messages in the chat, and the diff. Each of the two therefore stands alone."*
5. Met. I unwrapped the diff (`git diff | tr '\n' ' '`) and grepped for the human's sentence as a fixed string. It matched exactly, in italics and in quotes.
6. Met. `--numstat` reports 9 lines added and 0 removed, and `git diff | grep '^-'` shows only the `--- a/CLAUDE.md` header. No existing sentence was edited. Entry 1 is about a contradiction the new text sets up against an unchanged sentence. That sentence's own wording did not change.

Scope: the diff touches only `CLAUDE.md`, so no file outside the condition's list was edited. The condition records no search command, so there was nothing to re-run.

The bar: `CLAUDE.md` `## Commands` says the repository has no build, no tests, no formatter and no CI. Listing the tree's root confirmed this: there is no manifest, build file or CI configuration, so there was no command to run. Against the standards, the bar holds.
- I read only the standards in `.scratch/manager-own-choices/map-implementation-rules.md` and opened nothing else in the effort's directory, apart from that file's first line quoted in Entry 1.
- Standards that bore on this work:
  - `/writing-for-agents`, read from the `mattpocock-skills` plugin. The new section sits under one heading, states its points positively, and duplicates nothing. No finding.
  - The glossary's `_Avoid_` lines, checked by hand. `payload` is avoided. `subagents` appears only inside the word-for-word quote that part 5 requires. `report`, `session`, `question` and `task` are not used in a refused sense. No finding.
- Standards that did not bear on it: `/coding-principles`, `/naming` (no code, no identifiers) and `graph-conventions.md` (no graph file changed). The trigger-file rule did not apply either, because `SKILL.md` was not touched.
- The rules for writing under `## Rules for the files under .claude/skills/` apply to shipped files, and the root `CLAUDE.md` is not one, so I held the work to them only where they overlap with `/writing-for-agents`.
- I ran no reviewing skill, because the standards name none.

QUESTIONS:
- None about the flags. Both are true of the work.
  - `04.1`: the bullet does define map files as `map.md` and the `map-*.md` files beside it (same search as Entry 1's extent).
  - `04.2`: the text says "the manager's messages in the chat", and `grep -n payload CLAUDE.md` finds nothing in the added lines.

I wrote no temporary files.
```

### The worker's fix after checker run 1

What the worker changed for the finding, as it wrote it:

```
I fixed the checker's finding in my tree: the map-files bullet in `CLAUDE.md` now covers only `map.md`.

What I changed for the finding. The third bullet of `## Who reads an effort's node files` now reads:

> This rule does not reach an effort's map, the file `map.md`. Its reader is every worker on every node, and each worker needs a different part of it.

The checker was right. Widening the bullet to the `map-*.md` sibling files made the "every worker on every node" claim false. It also contradicted three texts: `CLAUDE.md`'s own "Its sibling files hold what only some readers need.", the glossary's **Map** entry, and the opening line of `map-implementation-rules.md`. The bullet now uses `CLAUDE.md`'s own definition of an effort's map, which matches the graph-workflow rule this was ported from.

Whether the correction touched something the condition names. Yes, it touched clause 3, which demands the statement that the rule does not reach an effort's map files. The bullet still makes that statement, now about `map.md` alone. Clauses 1, 2, 4 and 5, and the quote, are unchanged. Clause 6 still holds, because no other sentence of `CLAUDE.md` changed.

Paths touched. Only `CLAUDE.md` at the root of the worktree. Nothing is committed.

Changes to my flags.
- I withdraw the first ASSUMPTION flag, on widening "map files" to the `map-*.md` files. The work no longer makes that judgement.
- The second ASSUMPTION flag stands.

The ANSWER of my handover should now describe the third bullet as covering only `map.md`, as `CLAUDE.md` itself defines an effort's map. The INDEX LINE stands.

Proposed commit message:

CLAUDE.md: node files are written for agents

Port from the closed graph-workflow map the rule that an effort's node
files are written for the next agent, that the map is exempt, and that
the human works from the manager's chat and the diff.

Node: manager-own-choices/04
```

### Checker run 2 — `PASS`

The checker's entry, as it wrote it:

```
PASS

This re-check covers the corrected work. Its run-1 finding is fixed, and the bar still holds.

What I re-checked.
- I read the full current diff again rather than relying on the worker's account. `git status --short` in the worktree lists only ` M CLAUDE.md`, and `git diff --numstat` gives `9 0 CLAUDE.md`.
- The only change since run 1 is the third bullet, which matches the worker's account. I found no change it did not mention.
- I did not re-establish parts 1, 2, 4 and 5. The correction leaves their lines byte-identical to run 1, so they stand as established then.

Parts of the condition:
1. Met (stands from run 1). "The node files of an effort, under `.scratch/<effort>/nodes/`, are written for agents rather than for the human."
2. Met (stands from run 1). "A node file's reader is the next agent, which claims that node and needs it whole. In a node file, completeness for that agent therefore comes before brevity for a human."
3. Met (re-established). The bullet now reads "This rule does not reach an effort's map, the file `map.md`. Its reader is every worker on every node, and each worker needs a different part of it."
   - This matches the unchanged `CLAUDE.md` sentence "An effort's map is the file `map.md` in that directory. Its sibling files hold what only some readers need."
   - It also matches the glossary's `**Map**` entry: "Every worker reads one part of it once per node."
   - `grep -n 'map-\*\.md\|map files\|Their reader' CLAUDE.md`, the run-1 extent, now returns nothing, so the contradiction from run 1 is gone.
4. Met (stands from run 1). "The human works from two things: the manager's messages in the chat, and the diff. Each of the two therefore stands alone."
5. Met (re-run). I grepped the unwrapped diff (`git diff | tr '\n' ' '`) for the quote as a fixed string, and it matched exactly once.
6. Met (re-run). `git diff | grep '^-'` shows only the `--- a/CLAUDE.md` header. No existing sentence was edited, and no new text now contradicts one.

Scope. Only `CLAUDE.md` changed, so nothing outside the condition's list was edited. The condition records no search command.

The bar (re-run in full).
- Commands. `ls -a` of the tree's root shows no manifest, build file, formatter configuration or CI, which matches `CLAUDE.md` `## Commands`. There is no command to run.
- Have the standards changed since I last read them? No.
  - `map-implementation-rules.md`: I re-read it, and its content is identical to my run-1 read. Its last modification is `2026-11-11 23:48`.
  - `glossary.md`: unchanged on disk since `2026-10-15`.
  - `/writing-for-agents`: read from an unchanging Nix store path.
  - `CLAUDE.md`: its `## Standards` and `## Rules for the files under .claude/skills/` sections are outside the diff hunk.
  - The work moved no standard.
- What I read. Only the standards in `.scratch/manager-own-choices/map-implementation-rules.md`. I opened no other file in the effort's directory.
- Standards that bore on this work.
  - `/writing-for-agents`: the corrected bullet is plain, positive and has one referent ("Its" means `map.md`). No finding.
  - The glossary's `_Avoid_` lines, checked by hand: `grep -n payload CLAUDE.md` finds nothing, and `subagents` appears only inside the quote that part 5 requires. No finding.
- Standards that did not bear. `/coding-principles`, `/naming` and `graph-conventions.md` had nothing to apply to, and the trigger-file rule did not apply either, because `SKILL.md` is untouched. The writing rules for `.claude/skills/` files bind shipped files, and the root `CLAUDE.md` is not one.
- Reviewing skills. I ran none, because the standards name none.

Flags (checked after the outcome).
- `04.2` is true of the work: the text says "the manager's messages in the chat", and `payload` is absent.
- `04.1` was withdrawn, and the wider definition it described is no longer in the work.

No questions. I wrote no temporary files.
```

### Gate 1 — correct

The gate was raised on checker run 2's `PASS`. The human's words, 2026-11-12, `verbatim`:

*"Who reads an effort's node files in a section is clearly not how the other rules were migrated, it should just be a small bullet in the cloud.md that lists general writing rules."*

### Correction round 1

The human's words are under `### Gate 1 — correct` above. Passed to the worker as written.

What the worker changed in correction round 1, as it wrote it:

```
I made the human's correction, and the acceptance condition still holds, so nothing needed raising. The rule is now one bullet in the `CLAUDE.md` list of writing rules, and the separate section is gone.

What I changed. I deleted the `## Who reads an effort's node files` section. I added the rule as item 7 of "Rules for writing:", the list of general writing rules under `## Rules for the files under .claude/skills/`. I read "cloud.md" in the human's words as `CLAUDE.md`. The item is the only line the diff adds:

> 7. Write an effort's node files, under `.scratch/<effort>/nodes/`, for agents rather than for the human. A node file's reader is the next agent, which claims that node and needs it whole, so completeness for that agent comes before brevity for a human. This rule does not reach an effort's map, the file `map.md`, whose reader is every worker on every node, each needing a different part of it. The human works from two things, the manager's messages in the chat and the diff, so each of the two stands alone. The human's words: *"I expect the nodes to be mostly targeted to agents, as I will mostly work from what the manager says (questions from subagents) and with code review."*

The item is phrased as an instruction, as writing rule 5 asks. It still carries all five parts of the condition, plus the narrowing to `map.md` from the checker's round.

Whether the correction touched something the condition names. Yes, it moved and reworded the text for clauses 1 to 5, and each one still holds. Clause 6: no other sentence of `CLAUDE.md` changes in meaning.

Paths touched. Only `CLAUDE.md` in the worktree. Nothing is committed.

Changes to my flags. The "messages" for "payload" ASSUMPTION flag still stands. I add one ASSUMPTION flag (filed as 04.3).

For the ANSWER: the rule is item 7 of "Rules for writing:" in the root `CLAUDE.md`, and the separate section is gone. The INDEX LINE should read: "The root `CLAUDE.md` gains writing rule 7: node files are written for the next agent and completeness comes first there; `map.md` is exempt; the human works from the chat and the diff."

Proposed commit message:

CLAUDE.md: node files are written for agents

Add, as writing rule 7, the rule from the closed graph-workflow map that
an effort's node files are written for the next agent, that the map is
exempt, and that the human works from the manager's chat and the diff.

Node: manager-own-choices/04
```

### Checker run 3 — `PASS`

The checker's entry, as it wrote it:

```
PASS

This re-check covers the corrected work. Every part of the condition is met, and the bar holds.

What I re-checked.
- I read the full current diff rather than relying on the worker's account. `git status --short` in the worktree lists only ` M CLAUDE.md`, and `git diff --numstat` gives `1 0 CLAUDE.md`.
- The `## Who reads an effort's node files` section is gone: `grep -n 'Who reads' CLAUDE.md` returns nothing.
- The whole change is now one added line, item 7 of "Rules for writing:" under `## Rules for the files under .claude/skills/`. This matches the worker's account, and I found no change it did not mention.
- Parts 1 to 5 now sit in new text, so I established all six parts again on item 7.

Parts of the condition:
1. Met. "Write an effort's node files, under `.scratch/<effort>/nodes/`, for agents rather than for the human."
2. Met. "A node file's reader is the next agent, which claims that node and needs it whole, so completeness for that agent comes before brevity for a human."
3. Met. "This rule does not reach an effort's map, the file `map.md`, whose reader is every worker on every node, each needing a different part of it." This is consistent with the unchanged `CLAUDE.md` sentence "An effort's map is the file `map.md` in that directory." `grep -n 'map-\*\.md' CLAUDE.md` returns nothing.
4. Met. "The human works from two things, the manager's messages in the chat and the diff, so each of the two stands alone."
5. Met. I grepped the unwrapped diff (`git diff | tr '\n' ' '`) for the quote as a fixed string, and it matched exactly once, in italics and in quotes after "The human's words:".
6. Met. `git diff | grep '^-'` shows only the `--- a/CLAUDE.md` header, so no existing sentence of `CLAUDE.md` was edited. Items 1 to 6 of the list are byte-identical to `d49b11e`.

Scope. Only `CLAUDE.md` changed, so nothing outside the condition's list was edited. The condition records no search command.

The bar (re-run in full).
- Commands. There are none to run. The tree's root has no build file, no formatter configuration and no CI, which matches `CLAUDE.md` `## Commands`.
- Have the standards changed since I last read them? No.
  - `map-implementation-rules.md`: re-read, and identical to my earlier reads. Its last modification is still `2026-11-11 23:48`.
  - `.claude/skills/`: `git diff --quiet d49b11e -- .claude` reports it unchanged in the worktree.
  - The glossary: the worktree copy shows a fresh modification time. Its content matches the commit, and `cmp` against the main checkout's copy finds them identical, so its content did not move.
  - `/writing-for-agents`: read from an unchanging Nix store path.
- The work added to a standard. Item 7 is a new entry in `CLAUDE.md`'s rules for writing, which the standards cite. It is purely additive, and every earlier entry is unmoved. I held item 7 against the condition as changed text, and I held the work against none of what item 7 itself introduces.
- What I read. Only the standards in `.scratch/manager-own-choices/map-implementation-rules.md`, and no other file in the effort's directory.
- Standards that bore on this work.
  - `/writing-for-agents`: item 7 states its rule as what to do, and each pronoun has one referent. No finding.
  - The glossary's `_Avoid_` lines, checked by hand: `grep -n payload CLAUDE.md` returns nothing, and `subagents` appears only inside the quote that part 5 requires. No finding.
- Standards that did not bear. `/coding-principles`, `/naming` and `graph-conventions.md` had nothing to apply to, and the trigger-file rule did not apply either, because `SKILL.md` is untouched. The writing rules for `.claude/skills/` files bind shipped files, and the root `CLAUDE.md` is not one.
- Reviewing skills. I ran none, because the standards name none.

Flags (checked after the outcome).
- `04.2` is true: item 7 says "the manager's messages in the chat", and `payload` is absent.
- `04.3` is true: item 7 sits in the list under `## Rules for the files under .claude/skills/`, and it names `.scratch/<effort>/nodes/`.
- `04.1` stays withdrawn, and the wider definition it described is absent.

No questions. I wrote no temporary files.
```

### Gate 2 — reject

The gate was raised again on checker run 3's `PASS`. The human's words, 2026-11-12, `verbatim`:

*"actually for the claude.md change, let's move it to the node for flecheck like the others so he can decide"*

*Manager's note:* the human named no outcome. The manager took it as a reject, because the node's question changed from porting the rule to deciding whether to port it. What implementing the node surfaced: the rule's placement in `CLAUDE.md` is not settled. Its own section was corrected to an item of the writing rules, and that list is headed for the files under `.claude/skills/` (flag `04.3`). Route: the node asked the wrong question, so [node 05](05-whether-to-port-three-lost-graph-workflow-rules.md), whose question now carries this rule as item 4, supersedes it. The node's flags settle at this gate. The worktree and its branch are removed after this edit, and the work is not kept: its text is quoted in `### Correction round 1` above.
