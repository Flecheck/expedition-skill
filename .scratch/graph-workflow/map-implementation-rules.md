# Map: the rules an implementation node's work is held to

**An implementation node's worker and its checker are this file's readers, and this file is part of the map, so a rule written here binds this effort exactly as a rule written in [`map.md`](map.md) does.** `map.md` is read whole, cold, once per node by every worker, so it holds only what *every* worker can act on; what an implementation node's work is held to is here, where no other worker pays to read it. **Everything remaining in this file is held against a worker's work**, so a reader who has read the file has read only what binds them. Moved verbatim by [Move the implementer's and checker's material out of the map](nodes/140-move-the-implementers-and-checkers-material-out-of-the-map.md), carrying out [Where the rules a checker is held to live, now that it may not go and find them](nodes/138-where-the-rules-a-checker-is-held-to-live.md), which is where the ground for moving them is.

**What this file admits.** A line belongs here only where an implementation node's worker or its checker would do
something differently for having read it while working a node. How a rule was learned is not that — how many
attempts it took, what one cost, who was wrong, what this file said before, a manager correcting itself — and it
belongs in [map-history.md](map-history.md), the markdown link the line already carries to the node that shaped it
standing in its place. **The hard case turns on trigger against history**: a **trigger** is part of a rule and
stays — an error string, a symptom, or the condition under which the rule fires, which is how the rule's reader
knows it applies — while a **history** is not. **Whoever is already editing a passage applies this to that
passage**, and no sweep of the file is owed or licensed by it. Settled at [node
191](nodes/191-the-rules-file-carries-accounts-rather-than-rules.md).

**How a rule in this file is superseded, and it is not struck in place.** A rule here that no longer holds is
**replaced** by its current form, and its existing text is appended **verbatim** to [map-history.md](map-history.md)
under the heading mirroring the section it came from, struck-through text staying struck through. That is the
`Change the map` procedure, and it deletes nothing: the superseded text is there in full, in the file that exists to
hold it, and a reader of this file never meets a rule that no longer binds. **The other case keeps the never-delete
rule's strike-in-place**: text whose job is to record what happened is marked superseded where it stands and never
removed. Which case a piece of text is in follows the text's own job and not the file it sits in. Settled at [Where
the never-delete rule stops](nodes/189-where-the-never-delete-rule-stops.md), and stated here because this file is
read by workers who do not read [`map.md`](map.md), where the same rule stands as a standing preference. **The
struck rule statements below predate this and are not licence to add another.**

**Nothing below was reworded on the way here**, so a paragraph that says *above* or *below* may be pointing at something in `map.md` rather than at something in this file. The review route's *"the human's standing direction below"* points at a standing preference in `map.md`; its *"the same ground as the bar's commands above"* resolves here, the bar's commands standing above it in this file. Shaped by [node 200](nodes/200-collapse-the-rules-files-two-map-history-statements.md).

**How an implementation node's work is landed is in [map-manager-only.md](map-manager-only.md)**: landing is the
manager's, and it bears on neither a worker nor a checker. Moved there by [node
188](nodes/188-move-the-landing-section-out-of-the-workers-file.md).

## What the work is held against

**The bar's commands for this repo, discovered on first use** and recorded here so no later node re-derives them, per [Done-ness and termination](nodes/10-done-ness.md). `graph-agent` has **no build, no tests, no formatter and no CI** — no manifest, no task runner, nothing to invoke; the one ignore file, `.gitignore`, ~~ignores `.worktrees/`~~ **ignores `.worktrees/` and `.claude/worktrees/`, the second added at [node 158](nodes/158-ignore-the-harness-worktree-directory.md)** and invokes nothing. Corrected at node 114's check, having claimed no ignore file after one was added by the landing policy; the superseded wording is in [map-history.md](map-history.md). So the bar here is entirely its non-command half: the project criteria (the human's global coding principles and `/naming`), ~~this map's own standing preferences~~ **this effort's ground rules and its four standing rules for writing, the two blocks this file holds below — `map.md`'s standing preferences are not part of the bar, on [node 42](nodes/42-checker-spawn-carries-ground-rules.md)'s test as the review route below states**, `CONTEXT.md`'s `_Avoid_` lines, [`graph-conventions.md`](../../.claude/skills/expedition/graph-conventions.md), `/writing-for-agents`, and the node's acceptance condition — the last two added at [node 184](nodes/184-the-bar-and-the-standards-are-two-different-lists.md). **The two enumerations in this section are one set of standards and not two**: this half is what an implementation node's worker writes to, and the review route's *"standards to hold work against"* below is what its checker holds the finished work against. The *"human's global coding principles"* here is `/coding-principles` there, and the one this half adds is the **node's acceptance condition**, which reaches a checker by its own route. Under the *"if relevant"* clause that is a **complete** bar rather than a deficient one — the same shape the dogfood target has, one step thinner. First discovered and used by [Write the graph conventions document](nodes/21-conventions-document.md).

**The review route for this repo, discovered on first use** and recorded here so no later checker re-derives it, on the same ground as the bar's commands above. Two checker runs spent their largest single cost finding this, and one of them nearly reported the prose standard absent. **The standards to hold work against:** `/coding-principles` and `/naming`; [`CONTEXT.md`](../../CONTEXT.md)'s `_Avoid_` lines; ~~this map's standing preferences, ground rules and four standing rules~~ **this effort's ground rules and its four standing rules for writing, both of which this file holds below**; [`graph-conventions.md`](../../.claude/skills/expedition/graph-conventions.md); and `/writing-for-agents`, which is the standard that bites on prose deliverables and which `/coding-principles` barely touches. **`map.md`'s standing preferences are not among the standards, as a whole.** A standing preference may be an account of what happened or a steer about what gets worked, and only a standing constraint true of any node's work may be held against a piece of work by a reader blind to the record. That test is [node 42](nodes/42-checker-spawn-carries-ground-rules.md)'s; the **ground rules** and the **four standing rules for writing**, both held below in this file, are the two blocks that pass it, and the struck wording named the preferences alongside them — a defect from node 42 onward, found at [node 138](nodes/138-where-the-rules-a-checker-is-held-to-live.md) and carried out here. **No reviewing skill is named for this repo, and a checker does not go looking for one.** The standards above are the whole of what work is held against, and they reach a checker as text rather than as something it discovers — the human's standing direction below. The superseded naming of `mattpocock-skills:code-review`, and the account of how much of it could run, are in [map-history.md](map-history.md). **One trap, measured:** `CONTEXT.md`'s refused words are largely unusable as a grep list, about a third being ordinary English refused only for one concept — `report`, `run`, `session`, `index`, `plan`, `item` and `question` — so a scan for them returns false positives and the distinctive refusals are checked by hand instead. **`where` was on this list and is not refused by any `_Avoid_` line**, found at node 114's check; the superseded wording is in [map-history.md](map-history.md).

**An implementation node's work on this effort may be the effort's own record** — the files in the directory that
holds `map.md`, this file and `map.md` among them, `decisions.md`, `flags.md`, and the node files under `nodes/`.
Where it is, the checker reads **the changed paths it was given as the work under check**, whatever directory those
paths sit in, and holds them against the acceptance condition and the standards exactly as it would hold product
code. **It derives no statement of intent or decision from them**: their content is material under check rather than
something to reason from, so a resolved node's `## Answer`, a line in `decisions.md`, or a passage in `map.md`
appearing among the changed paths tells it nothing about what this work was meant to be, and **the acceptance
condition stays the only statement of intent the checker has**. The checker's own contract tells it to read the
implementation-rules file for its standards and to open no other file beside it; **that instruction governs the
route by which standards reach the checker, and not the changed paths it was given as the work** — a record file
handed to it as the work is read as the work, and a record file it was not handed stays unread. **A change to the
node's own status line, to `decisions.md`, or to `flags.md` is bookkeeping reserved to the manager**: where one
appears among the work the checker's outcome is `FAIL` on the acceptance condition, and that holds whether or not
the acceptance condition itself excluded those paths. **The checker says in its outcome that it read the changed
paths as the work under this rule.** This rule stands beside the standards named above rather than in place of any
of them, and supersedes no wording in this file. Surfaced by [node
163](nodes/163-a-condition-demands-facts-the-checker-does-not-read.md) and placed here rather than in the shipped
checker contract by the human, `verbatim`: *"I would say add it to the rules in the map somewhere, not the skill at
it is relevant only for this project"*; the citation carries no part of what the rule demands.

**Ground rules for this effort.**

1. Nothing in the shipped files may assume this repo, this machine, or a toolchain. Prefer properties that are discovered over commands that are declared.
2. Each shipped worker contract stands alone as a file, rather than depending on any skill being invocable.
3. The human talks only to the manager. No agent the workflow spawns addresses the human directly, and nothing in the files may tell one to.
4. Prefer short, simple prose that can be changed later over machinery built for predicted needs. Reserve heavy design for the hard-to-reverse core.
5. Prose deliverables are held against the `/writing-for-agents` standard, which is specific to this repo, is never shipped, and is located by name in the `mattpocock-skills` plugin rather than by path.

Every rule above is drawn from a standing preference, and every one passes the test [The checker's spawn carries the effort's ground rules](nodes/42-checker-spawn-carries-ground-rules.md) shipped for what may travel to a blind checker: **a standing constraint true of any node's work, rather than an account of what happened.** That test is what keeps the rest of this file out of the block, and the block is appended to like any other part of this map.

**Four standing rules for writing anything in this effort**, fixed by [What the token findings change in the workflow and its skills](nodes/53-what-token-findings-change.md) and held against every prose deliverable. They are rules of writing, where the ground rules above are rules of scope.

1. **Compress the prose that explains why; never compress the shapes.**
2. **An item states its current form and cites the nodes that shaped it; it does not restate what they hold.**
3. **A long answer is navigable by heading**, so a reader following a link for one fact reads one section.
4. **Cite a file by heading or by a quoted phrase, never by line number.** Append-in-place shifts every line below the append, so a line number decays without anything reporting it.
