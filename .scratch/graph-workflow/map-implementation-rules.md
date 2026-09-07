# Map: the rules an implementation node's work is held to

**An implementation node's worker and its checker are this file's readers, and this file is part of the map, so a rule written here binds this effort exactly as a rule written in [`map.md`](map.md) does.** `map.md` is read whole, cold, once per node by every worker, so it holds only what *every* worker can act on; what an implementation node's work is held to is here, where no other worker pays to read it. Moved verbatim by [Move the implementer's and checker's material out of the map](nodes/140-move-the-implementers-and-checkers-material-out-of-the-map.md), carrying out [Where the rules a checker is held to live, now that it may not go and find them](nodes/138-where-the-rules-a-checker-is-held-to-live.md), which is where the ground for moving them is.

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

**Nothing below was reworded on the way here**, so a paragraph that says *above* or *below* may be pointing at something in `map.md` rather than at something in this file. The review route's *"the human's standing direction below"* points at a standing preference in `map.md`; its *"the same ground as the bar's commands above"* resolves here, the bar's commands standing above it in this file. The account behind a line here is in [map-history.md](map-history.md), as it is for a line in `map.md`.

## Landing an implementation node's work

**Landing policy**, which binds this map too, since this map carries execution. An implementation node's worker works in a **git worktree** ~~the manager creates for that node with `git worktree add` off the current `HEAD`~~ **created by the harness rather than by hand — see the standing instruction immediately below**, on a branch whose name carries the node's id, placed at `.worktrees/NN-<name>/` **inside** the repository and ignored there. **The human's instruction**, `verbatim`, after a worktree outside the repository made a gate's diff invisible to them: *"For the worktree, I think it might be needed as otherwise it is too anoying for the review"*. It requires an ignore rule, which is exactly what flag `68.2` refused to assume for a repository the workflow does not own — so this is the effort's own practice and **not** a change to what the workflow ships; the flag stands open. The changes stay **uncommitted** through the checker and through the human's gate. On approval the manager makes one path-limited commit of that node's paths, rebases the branch onto the branch the manager thread is on, re-runs the bar's commands on the rebased result, merges with `git merge --ff-only`, then removes the worktree and deletes the branch. **A rebase conflict is resolved by nobody in the moment**: the manager runs `git rebase --abort` and the node takes a correction round with the worker respawned. A post-rebase bar failure likewise takes a correction round, and the work does not land. On reject the worktree is removed and its branch deleted; where the human asks for the work to be kept, the manager commits it onto that branch before removing the directory. **Nothing is ever pushed.** **The gate payload names the worktree's path and the command that shows its diff**, because an implementation node's work is uncommitted in a checkout outside the repository and `git diff` where the human is standing does not show it — their words on being handed a gate without it: *"what are the changes ? I don't see them in git ?"*. One of the human's two interfaces is the diff, so a gate that describes one and points at nothing has not been presented. The graph's own files are *not* committed per node; they are committed periodically by the human, which is safe only because node files are append-only. Fixed by [Git and code-landing policy](nodes/11-git-and-code-landing.md) and reshaped by [Run an implementation node's work in a worktree](nodes/68-implementation-in-a-worktree.md).

~~**How many implementation workers run at once is a setting of the effort, and for this effort it is one.**~~ **How many implementation workers run at once is a setting of the effort, and for this effort it is two**, raised from one by the human while directing the manager at the shipping backlog, `verbatim`: *"should we do 2 implementer and 2 grilling to go through the shipping backlog ?"*. **What the manager carries with the second slot** is that two implementation workers may hold two worktrees over the same shipped file, so it picks nodes whose paths are disjoint; the integration-conflict question that raises is [node 115](nodes/115-two-writers-edit-the-map-at-once.md)'s, still open at [node 160](nodes/160-carry-the-integration-conflict-rule-into-the-map.md) and [node 162](nodes/162-how-much-of-the-integration-rule-ships.md). The superseded sentence is also in [map-history.md](map-history.md). A code slot is therefore a count rather than a property, and raising the count changes a number and no part of the lifecycle above. **A slot's occupancy is discovered by counting the live worktrees** — one per claimed implementation node — rather than by inspecting the working tree for uncommitted changes, so the human's own edits no longer read as an occupied slot. Set at [Run an implementation node's work in a worktree](nodes/68-implementation-in-a-worktree.md).

**What that supersedes**: this map used to say *"No branch is ever created or switched, nothing is ever pushed, and history is never rewritten"*, and two of those three clauses no longer hold — the workflow branches per node, and a rebase rewrites history. *Nothing is ever pushed* is the one that stands untouched. The sentence in full is in [map-history.md](map-history.md).

**How the worktree is made, settled at [Which harness route creates an implementation node's
worktree](nodes/150-which-harness-route-creates-a-worktree.md).** Added beside the landing policy above rather than
rewritten into it, because [node 152](nodes/152-where-the-harness-worktree-instruction-lives.md) and [node
144](nodes/144-make-the-rules-file-stand-alone.md) hold conditions quoting that paragraph's exact phrases.

- ~~**The manager creates nothing.** It spawns the implementation worker with the harness's worktree isolation.~~
  **Superseded by the human's own route**, `verbatim`: *"It calls EnterWorktree specifying a name tied to the node
  and vaguely describing the node's title"*, then *"If it didn't land on HEAD … it does `git reset` itself to reach
  the proper base"*. **The manager calls `EnterWorktree` with a node-tied name**, checks the base it landed on, and
  `git reset --hard`es to its own `HEAD` **before any worker reads the tree** — which is why this needs no
  `worktree.baseRef` setting and assumes no machine. Measured: `EnterWorktree` lands on `origin/master` under the
  default, and the reset **requires the sandbox off**, failing inside it with `Could not reset index file`. The path
  is `.claude/worktrees/<name>/` and the branch `worktree-<name>`, so **the node's id is back in both**.
- ~~The
  harness picks the path, `.claude/worktrees/agent-<agentId>/`, and the branch, `worktree-agent-<agentId>`, and the
  manager learns both from the worker's completion notification. **The node's id is no longer in either**; the commit
  trailer `Node: <effort>/<NN>` is the join key and is the manager's to write.~~ **Superseded by the bullet
  above**: the node's id is in the path and the branch again, and the commit trailer stays the join key regardless.
- **What the reset costs in practice, settled by the human**, `verbatim`:

  > ok so looks like we can indeed do the EnterWorktree -> reset process - that will work so long as either we aren't
  > working on skills (otherwise the agent can ask unsandboxed for the reset and it will be fine) - or if the user
  > already has set baseRef=head in their global config, which will typically be the case.

  So the route stands, and the sandbox restriction above is a cost rather than an obstacle. Three cases, and the
  manager does not need to decide between them in advance: a node touching no file under `.claude/skills/` resets
  inside the sandbox; a node that does asks for that one command unsandboxed; and where `worktree.baseRef` is already
  `head` in the human's global config — ~~**which is the typical case, and is theirs rather than this effort's**~~
  **which is measured at [node 175](nodes/175-what-the-worktree-cycle-does-to-the-sandbox.md) not to hold on this
  machine: the setting is absent, so the default `fresh` applies, every harness worktree lands on `origin/master`, and
  the base is always stale. Three worktrees created during that node all recorded `CLAUDE_BASE` = `origin/master`
  while `master` was ahead. The three-case account still stands; the case it called typical is the one that never
  happens here, and the reset always runs.** — the
  worktree lands on `HEAD` and no reset happens at all. **The base check still runs in every case**, since what it
  guards against is landing on the wrong base for any reason, not against one configuration.

- **The manager needs `EnterWorktree` for neither the base check nor the reset**, measured at [node
  175](nodes/175-what-the-worktree-cycle-does-to-the-sandbox.md): `cat .git/worktrees/<name>/CLAUDE_BASE` and
  `git -C <worktree> rev-parse HEAD` both answer the base check read-only from the main tree, and
  `git -C <worktree> reset --hard <ref>` succeeded there **inside the sandbox even across a `.claude/skills` file**.
  So **the manager's own session never has to leave the main tree**, and the cycle that migrated its writable region
  was avoidable. **The sandbox half of that does not generalise, and the manager corrected it within the hour**: on
  node 169's worktree the same command failed with `unable to unlink old
  '.claude/skills/expedition-grilling/SKILL.md': Read-only file system` and needed the sandbox off. Node 175's test
  worktree carried no `ro` overlay on its own `.claude/skills` and node 169's did — which is exactly [node
  180](nodes/180-which-trees-get-the-read-only-skills-overlay.md)'s question. **What stands is the base check and the
  route; what does not is any prediction that the reset stays inside the sandbox.** Read it as: run it sandboxed, and
  expect to need the override when the range crosses a shipped file. Where the instruction to use `EnterWorktree` now stands is [node
  152](nodes/152-where-the-harness-worktree-instruction-lives.md)'s.
- **The manager verifies the base at every spawn.** A harness worktree's base is governed by `worktree.baseRef`,
  whose default `fresh` means `origin/<default-branch>` — frozen forever on an effort that never pushes. The setting
  is `head`, but **the setting is a property of the environment, cannot be passed per call, and does not travel to
  another machine**, so under ground rule 1 it is observed rather than trusted. Immediately after the spawn the
  manager reads `.git/worktrees/<name>/CLAUDE_BASE`, or runs `git -C <worktree> rev-parse HEAD`, and compares it to
  its own `HEAD`. **Not equal: stop the worker, remove the worktree, and raise it** — never reset the tree in place,
  which leaves it holding pre-repair content for every file the worker has not touched. Node 140 was moving text
  verbatim between files, so a late reset there would have silently reverted [node
  147](nodes/147-graph-records-name-absolute-paths-on-a-machine.md)'s landed work with every check passing.
- **A failed rebase leaves its partial checkout behind, and every retry then meets the dirt its predecessor made.**
  Measured at node 143, after four failed attempts and two wrong diagnoses. `git rebase` reported only `could not
  detach HEAD`; the underlying `git checkout --detach` reports the real cause, which was local changes and untracked
  files that **the previous failed rebase had itself written**. **Cleaning and rebasing in separate calls cannot
  converge.** The repair is one pass: `reset --hard` to the branch's own commit, `clean` the record directory, then
  rebase — and read `git checkout --detach <target>` rather than the rebase's summary when it fails again.

- **A correction round resumes the worker** and never re-spawns it with isolation, a second isolated spawn creating a
  second empty tree at a fresh base and stranding the first one's work. Where resume is unavailable the replacement
  is pointed at the surviving path. Flagged at `150.3` as unverified.
- **One sandbox restriction bites this lifecycle, and it took three rounds of experiment to state correctly.** Two
  earlier accounts of it in this file were wrong and are struck below. ~~**The rule: the sandbox mounts
  `.claude/skills` read-only in whichever tree the session is standing in — the main checkout, or an entered
  worktree. Any git operation that must write a file under it fails.**~~ **Incomplete rather than false, and
  superseded at [node 175](nodes/175-what-the-worktree-cycle-does-to-the-sandbox.md).** The `ro` overlay was observed
  on trees the session was *not* standing in, and the `ro` deny is **not** the constraint that bites when the region
  has migrated: **the allow-set is, and it is far smaller than "everything but skills".** The operative rule, measured:
  the sandbox is a set of bind mounts **recomputed for every command**, and a command succeeds only where every path it
  writes lies inside a `rw` mount and outside a `ro` one. **The manager reads its own region with**
  `grep " <repo>" /proc/mounts | awk '{split($4,a,","); print a[1]" "$2}' | sort -u` — read-only, one call. Whether it
  is told to, and when, is [node 179](nodes/179-the-manager-sees-its-own-writable-region.md); what triggers the overlay
  on one tree and not another is [node 180](nodes/180-which-trees-get-the-read-only-skills-overlay.md). It is not about worktrees, not about the git
  index, and not about harness-created worktrees being treated differently from hand-made ones.
  - **What it hits.** `git merge --ff-only` in the main tree, of a branch that changed a file under `.claude/skills/`
    — `unable to unlink old …`. And `git reset --hard <ref>` inside an *entered* worktree, where the range crosses
    such a file — `Could not reset index file to revision`. `HEAD` does not move and nothing is lost in either case;
    both succeed outside the sandbox.
  - **What it does not hit, established by experiment rather than inferred.** `git add` and `git commit` from inside
    an entered worktree both succeed. `.git/index` is writable in the main tree and in a worktree's admin directory.
    `git reset --hard` succeeds inside an entered worktree where the commit range touches no file under
    `.claude/skills/`. So the operation is irrelevant; **only the paths the operation must write matter.**
  - ~~**The one asymmetry, and it is a hole rather than a feature.** A worktree operated *from the main tree* with
    `git -C` escapes the rule entirely, because the deny list names `<repo>/.claude/skills` and a worktree at another
    path is not that. So the same reset that fails from inside a worktree succeeds when run on it from outside. The
    protection is on the session's own tree, not on the repository's skills.~~ **Superseded at [node
    175](nodes/175-what-the-worktree-cycle-does-to-the-sandbox.md): the conclusion holds only conditionally and the
    stated reason is wrong.** Measured there: from a session whose region did *not* contain the worktree path,
    `git -C <harness worktree> reset --hard` failed on plain `.scratch/` files with `Read-only file system`, no skills
    file involved; from a session whose region *did* contain it, the same command succeeded across a `.claude/skills`
    file. **What decides is whether the target path is inside the writing session's writable region**, not which tree
    the command is issued from — and harness worktrees do sometimes carry their own `<wt>/.claude/skills` `ro` mount,
    so *"a worktree at another path is not that"* is not reliably true.
- ~~**Two distinct sandbox restrictions bite this lifecycle, and they were once conflated. Isolated by experiment.**~~
  - **The merge step needs the sandbox off where the node touched a file under `.claude/skills/`.** The **main
    tree's** `.claude/skills` is a read-only bind mount; `touch` on a file there fails with `Read-only file system`.
    So `git merge --ff-only` of a branch that changed one fails with `unable to unlink old …`. `HEAD` does not move
    and nothing is lost; the merge succeeds outside the sandbox.
  - **The reset step needs the sandbox off only for a *harness-created* worktree.** Measured both ways on one tree: a
    worktree made by `git worktree add` resets across the same commits **inside** the sandbox without error, while
    one made by `EnterWorktree` fails with `Could not reset index file to revision`. The difference visible in
    `/proc/mounts` is that the sandbox places read-only bind mounts inside a harness worktree's admin directory —
    `.git/worktrees/<name>/config.worktree` and `.../commondir` — and places none at all on a hand-made one.
    **Correlation established both ways; the exact write that fails is not isolated.** Writing `.git` is not the
    problem in general: `git add` and `git commit` both succeed inside the sandbox in a harness worktree, as does a
    plain write to that worktree's own `.claude/skills/`.
- ~~**The merge step needs the sandbox off where the node touched a shipped file.**~~ Measured at node 140: `git merge
  --ff-only` failed with `unable to unlink old '.claude/skills/expedition/graph-conventions.md': Read-only file
  system`, `/proc/mounts` showing `.claude/skills` bind-mounted `ro` inside the manager's sandbox. **`HEAD` does not
  move and nothing is lost** — the commit stays on its branch and the merge succeeds on a retry outside the sandbox —
  but the manager must expect it rather than discover it, since most of the open frontier touches `.claude/skills/`.


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
