# Map: the rules an implementation node's work is held to

**An implementation node's worker and its checker are this file's readers, and this file is part of the map, so a rule written here binds this effort exactly as a rule written in [`map.md`](map.md) does.** `map.md` is read whole, cold, once per node by every worker, so it holds only what *every* worker can act on; what an implementation node's work is held to is here, where no other worker pays to read it. **Everything remaining in this file is held against a worker's work**, so a reader who has read the file has read only what binds them. Moved verbatim by [Move the implementer's and checker's material out of the map](nodes/140-move-the-implementers-and-checkers-material-out-of-the-map.md), carrying out [Where the rules a checker is held to live, now that it may not go and find them](nodes/138-where-the-rules-a-checker-is-held-to-live.md), which is where the ground for moving them is.

**What this file admits.** A line belongs here only where an implementation node's worker or its checker would do
something differently for having read it while working a node. How a rule was learned is not that — how many
attempts it took, what one cost, who was wrong, what this file said before, a manager correcting itself — and it
belongs in [map-history.md](map-history.md), the markdown link the line already carries to the node that shaped it
standing in its place. **The hard case turns on trigger against history**: a **trigger** is part of a rule and
stays — an error string, a symptom, or the condition under which the rule fires, which is how the rule's reader
knows it applies — while a **history** is not. **Whoever is already editing a passage applies this to that
passage**. No pass over the whole file is owed, and one is allowed. Settled at [node
191](nodes/191-the-rules-file-carries-accounts-rather-than-rules.md), and the pass over the whole file allowed at
[node 346](nodes/346-allow-a-sweep-of-a-map-file-in-graph-conventions-md.md).

**How a rule in this file is superseded, and it is not struck in place.** A rule here that no longer holds is
**replaced** by its current form, and its existing text is appended **verbatim** to [map-history.md](map-history.md)
under the heading mirroring the section it came from, struck-through text staying struck through. That is the
`Change the map` procedure, and it deletes nothing: the superseded text is there in full, in the file that exists to
hold it, and a reader of this file never meets a rule that no longer binds. **The other case keeps the never-delete
rule's strike-in-place**: text whose job is to record what happened is marked superseded where it stands and never
removed. Which case a piece of text is in follows the text's own job and not the file it sits in. Settled at [Where
the never-delete rule stops](nodes/189-where-the-never-delete-rule-stops.md), and stated here because this file is
read by workers who do not read [`map.md`](map.md), where the same rule stands as a standing preference.

**Nothing below was reworded on the way here**, so a paragraph that says *above* or *below* may be pointing at something in `map.md` rather than at something in this file. The review route's *"the human's standing direction below"* points at a standing preference in `map.md`; its *"the same ground as the bar's commands above"* resolves here, the bar's commands standing above it in this file. Shaped by [node 200](nodes/200-collapse-the-rules-files-two-map-history-statements.md).

**How an implementation node's work is landed is in [map-manager-only.md](map-manager-only.md)**: landing is the
manager's, and it bears on neither a worker nor a checker. Moved there by [node
188](nodes/188-move-the-landing-section-out-of-the-workers-file.md).

*Moved verbatim from [`map.md`](map.md)'s `## Notes` by the manager's pass carrying out [node 345](nodes/345-workers-report-most-of-map-md-bore-on-nothing.md)'s answer, its readers being an implementation node's worker and checker.*

**An implementation node's worktree is made with plain git, and a worker reaches it by path.** The manager creates it from the main tree with `git worktree add`, at `.scratch/graph-workflow/worktrees/<NN>-<name>` on a branch `worktree-<NN>-<name>`, where `<NN>` is the node's id. **A worker writes that tree by absolute path, calls no tool to reach or leave it, and owes no cleanup** — there is no first act to get wrong. **Creating the worktree, putting it on its base, and a worker writing it need no harness tool call and no sandbox override**, by the manager or by the worker. **The removal is the exception, and it runs with the sandbox off.** It is the manager's step and no worker's — the cleanup a worker owes is still none — and its symptom, its trigger and its recovery are stated in [map-manager-only.md](map-manager-only.md) under *How the worktree is made* rather than restated here. Settled at [The removal step of the worktree route does not work as written](nodes/277-the-removal-step-of-the-worktree-route-does-not-work-as-written.md), which narrowed the claim to those three steps and stated the removal as the exception. The route is stated in full in [map-manager-only.md](map-manager-only.md) under *How the worktree is made*, and was settled at [Should the worktree route drop `EnterWorktree` for plain git, behind a script](nodes/265-should-the-worktree-route-drop-enterworktree-for-git.md), which supersedes both the standing instruction this paragraph replaces and [Which harness route creates an implementation node's worktree](nodes/150-which-harness-route-creates-a-worktree.md)'s route. The superseded paragraph is in [map-history.md](map-history.md).

## What the work is held against

**The standards an implementation node's work is held against.** Its worker writes to them, and its checker holds the finished work against them. They are one list, made one by [node 184](nodes/184-the-bar-and-the-standards-are-two-different-lists.md) and stated once by [node 190](nodes/190-the-rules-file-states-one-list-twice.md):

- `/coding-principles` and `/naming`, the human's global coding principles;
- [`.claude/skills/expedition/glossary.md`](../../.claude/skills/expedition/glossary.md)'s `_Avoid_` lines;
- this effort's ground rules, which [`map.md`](map.md) holds in its `## Notes` and which a checker receives as text in its spawn, placed there at [node 348](nodes/348-keep-the-ground-rules-in-map-md-and-strike-the-sibling-file-allowance.md);
- this effort's six standing rules for writing, which [`map.md`](map.md)'s `## Notes` holds inside the ground-rules block and which a checker receives as text in its spawn with the ground rules;
- [`graph-conventions.md`](../../.claude/skills/expedition/graph-conventions.md);
- `/writing-for-agents`, which is the standard that bites on prose deliverables and which `/coding-principles` barely touches.

**`map.md`'s standing preferences are not among the standards, as a whole.** A standing preference may be an account of what happened or a steer about what gets worked, and only a standing constraint true of any node's work may be held against a piece of work by a reader blind to the record. That test is [node 42](nodes/42-checker-spawn-carries-ground-rules.md)'s; the **ground rules** and the **six standing rules for writing**, both held in `map.md`'s `## Notes` inside the ground-rules block and received by a checker as text in its spawn, are the two blocks that pass it.

**The bar's commands for this repo, discovered on first use** and recorded here so no later node re-derives them, per [Done-ness and termination](nodes/10-done-ness.md). `graph-agent` has **no build, no tests, no formatter and no CI** — no manifest, no task runner, nothing to invoke; the one ignore file, `.gitignore`, ignores `.worktrees/`, `.claude/worktrees/` and `.scratch/graph-workflow/worktrees/` and invokes nothing, so the bar's command half is empty, and under the *"if relevant"* clause that is a **complete** bar rather than a deficient one. So the bar here is entirely its non-command half: the standards listed at the head of this section, and the **node's acceptance condition**, which binds too and reaches a checker by its own route. First discovered and used by [Write the graph conventions document](nodes/21-conventions-document.md). The superseded wordings are in [map-history.md](map-history.md).

**The review route for this repo, discovered on first use** and recorded here so no later checker re-derives it, on the same ground as the bar's commands above. **A checker holds the finished work against the standards listed at the head of this section**, and they are the whole of what it holds work against. **No reviewing skill is named for this repo, and a checker does not go looking for one.** The standards reach a checker as text rather than as something it discovers — the human's standing direction below. The superseded naming of `mattpocock-skills:code-review`, and the account of how much of it could run, are in [map-history.md](map-history.md). **One trap, measured:** `.claude/skills/expedition/glossary.md`'s refused words are largely unusable as a grep list, about a third being ordinary English refused only for one concept — `report`, `run`, `session`, `index`, `plan`, `item` and `question` — so a scan for them returns false positives and the distinctive refusals are checked by hand instead. **`where` was on this list and is not refused by any `_Avoid_` line**, found at node 114's check; the superseded wording is in [map-history.md](map-history.md).

The harness loads `.claude/rules/expedition-triggers.md`, without any spawn or hook, into an agent that reads a file
matching its `paths:` frontmatter, meaning an effort's `map-manager-only.md` or the shipped `/expedition` skill's
`SKILL.md`, and into no other agent. The file holds a copy of the manager's trigger-duties and of the priority that
orders them. The governing statement of both is in `.claude/skills/expedition/SKILL.md`, under
`## The order you act in` and `## What is in front of the human, and when`. Where the file and the map differ, the
map is followed. Whoever edits the governing statement in `SKILL.md` of one of those duties, or of the priority, edits
`.claude/rules/expedition-triggers.md` in the same edit, or says plainly why not. Settled at [node
226](nodes/226-nothing-in-the-record-says-the-auto-loaded-trigger-file-exists.md).

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
