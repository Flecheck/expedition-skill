# Map: what only the manager acts on

**The manager is this file's reader, and this file is part of the map.** [`map.md`](map.md) is read whole, cold, once per node by every worker, so it holds only what *every* worker can act on; what only the manager acts on is here, where no worker pays for it. Everything below binds this effort exactly as it did in `map.md` — the standing preference that *"A standing rule binds this effort only once it is written here"* reaches this file too, `here` being the map rather than one of its files. Moved verbatim by [Move the manager's material out of the map, and give each item a soft size target](nodes/139-move-the-managers-material-out-of-the-map.md), carrying out [`map.md` has grown back most of what node 59's restructure saved](nodes/136-the-map-has-grown-back-what-node-59-saved.md), which is where the ground for moving each of them is.

**Nothing below was reworded on the way here**, so a paragraph that says *above* or *below* may be pointing at something still in `map.md`: the out-of-scope line's *"The Notes above"* does. Read those two words as naming the map rather than this file. The account behind a line here is in [map-history.md](map-history.md), as it is for a line in `map.md`.

*Superseded at [Move the implementer's and checker's material out of the map](nodes/140-move-the-implementers-and-checkers-material-out-of-the-map.md), which moved the review route on to [map-implementation-rules.md](map-implementation-rules.md), the file an implementation node's worker and its checker read. Left here under the never-delete rule, and no longer this file's account of what it holds. The sentence as it stood:*

> **Nothing below was reworded on the way here**, so a paragraph that says *above* or *below* may be pointing at something still in `map.md`: the review route's *"the same ground as the bar's commands above"* and *"the human's standing direction below"* both do. Read those two words as naming the map rather than this file. The account behind a line here is in [map-history.md](map-history.md), as it is for a line in `map.md`.

**How an implementation node's work is landed came here from [map-implementation-rules.md](map-implementation-rules.md)**, moved byte-identical by [node 188](nodes/188-move-the-landing-section-out-of-the-workers-file.md), landing being the manager's rather than a worker's or a checker's. **Its *above* and *below* words resolve inside that section itself**, not into `map.md`.

## Notes

**The dogfood target is [Lang](/home/mathieu/projects/Lang)**, decided in [Dogfood target](nodes/09-dogfood-target.md): **179 distinct gap labels across 188 inventory rows in 13 families, 43 settled decisions and 48 consistency rows** — counted by [Graph file format](nodes/13-graph-file-format.md) — a compiler that is only a lexer and parser and expects to be rebuilt, and an existing tracker doc at `Lang/docs/agents/issue-tracker.md` whose conventions this graph already borrows. **The dogfood's code lands in Lang's repository and not in this one**, per [Git and code-landing policy](nodes/11-git-and-code-landing.md), so that is the repo the landing policy has to work in. When a choice is close, prefer the one that survives that repo.

**The order the manager works the frontier in, approved by the human.** They asked for the frontier grouped and for a
proposed order, and answered `verbatim`: *"otherwise ok for how you priorize"* — the *otherwise* being their own two
overrides in the same breath, the counts and question batching, both recorded where they belong. So this is **standing
steering** and binds until they change it, and the manager reports it back in every pick it constrains. It sits under
[What the manager works on next, and how the human redirects it](nodes/16-human-steering.md)'s rule rather than
replacing that node's answer: the alternation between a design stream and a delivery stream stands, as does the
standing preference ranking token-cost work first within each stream. The order, as the manager proposed it and they
approved it:

1. **Statements in the record that are now false**, chiefly the consequences of the map split at [node
   139](nodes/139-move-the-managers-material-out-of-the-map.md), [node
   140](nodes/140-move-the-implementers-and-checkers-material-out-of-the-map.md) and [node
   144](nodes/144-make-the-rules-file-stand-alone.md) — cheapest on the graph, and each one misleads every worker
   that reads it.
2. **The files the workflow has not written yet**, continuously — starting an effort, the adoption procedure, the
   cascade contract, the checker's `## How you check` section, an `expedition-stop` skill. **The only group that
   moves toward the destination.**
3. **The shipping backlog** — the open implementation nodes carrying an already-settled decision into a shipped
   file — one per delivery slot in the background.
4. **The open design questions** only where they block the above, or where the human names one.
5. **The glossary repairs** last.

**The manager's own statement accompanying it, which the human did not contradict and which is not part of the
order:** this effort mints nodes faster than it closes them, the open design questions grow fastest, and this map
says the effort is **expected to end** — so ending it is a scoping act on those questions rather than an outcome
reachable by working them.

**The plain-English pass runs before the backlog, one file at a time.** Settled at [node 289](nodes/289-a-plain-english-and-compaction-pass-over-the-shipped-files.md), whose Q4 the human answered `verbatim`: *"4. ok"*, taking the recommendation *"Before, one file at a time. While a file's rewrite is in progress, no other implementation node on that file starts."* So:
- no other implementation node that names a shipped file is claimed until the rewrite of that file has landed;
- once it has landed, an open node that names the file is claimed only after its condition has been re-pointed at the new text or the node has been superseded;
- the manager files each rewrite's re-pointed conditions and stand-downs once that rewrite lands.

**Two rulings the human gave at the pilot's gate bind every rewrite in the pass**, `verbatim`: *"A ok B like the pilot C you can update"*, recorded on [node 290](nodes/290-rewrite-the-research-contract-as-the-pilot.md). B: a name a shipped file defines that `CONTEXT.md` does not is said in plain words and the label is dropped, as the pilot did. This also resolves [node 305](nodes/305-whether-standing-over-sources-becomes-a-glossary-term.md). C: rewrite freely, and update the open conditions that quote the old text. Every rewrite spawn carries both. A, asked again and answered `verbatim`: *"A. we can do 2 if it make sense in the file"*: a rewrite may cut deeper by changing rules where that makes sense in the file, each change listed at its gate for approval. The human then amended the pass's open conditions to carry A and B, `verbatim`: *"ok"*: a checker lists every rule change it finds rather than failing it, a term `CONTEXT.md` does not define may be dropped where its meaning stays in plain words, and each gate shows the worker's list of rule changes beside the checker's. The amendment is filed on nodes 291 to 302.

Nodes whose work touches no shipped file are unaffected. The pilot, [node 290](nodes/290-rewrite-the-research-contract-as-the-pilot.md), is worked alone, and nothing else in the pass is claimed until its gate has set the style.

**Label vocabulary for this effort: none declared.** `Labels:` is an optional per-node field holding the *family* a node belongs to, and it exists so the human can scope work to one area of a large graph. A node may only use a label declared here, so that `EFF` / `effect` / `effects` cannot drift into three labels. At 20 nodes this effort has no reader for them; an adopted effort declares its own vocabulary here — Lang's would be its 13 gap families.

## Landing an implementation node's work

**Landing policy**, which binds this map too, since this map carries execution. An implementation node's worker works in a **git worktree** **the manager creates with plain git — see *How the worktree is made* below**, on a branch whose name carries the node's id, placed at `.scratch/graph-workflow/worktrees/<NN>-<name>` **inside** the repository and ignored there. **The human's instruction**, `verbatim`, after a worktree outside the repository made a gate's diff invisible to them: *"For the worktree, I think it might be needed as otherwise it is too anoying for the review"*. It requires an ignore rule, which is exactly what flag `68.2` refused to assume for a repository the workflow does not own — so this is the effort's own practice and **not** a change to what the workflow ships; the flag stands open. The changes stay **uncommitted** through the checker and through the human's gate. On approval the manager makes one path-limited commit of that node's paths, rebases the branch onto the branch the manager thread is on, re-runs the bar's commands on the rebased result, merges with `git merge --ff-only`, then removes the worktree and deletes the branch. **A rebase conflict is resolved by nobody in the moment**: the manager runs `git rebase --abort` and the node takes a correction round with the worker respawned. A post-rebase bar failure likewise takes a correction round, and the work does not land. On reject the worktree is removed and its branch deleted; where the human asks for the work to be kept, the manager commits it onto that branch before removing the directory. **Nothing is ever pushed.** **The gate payload names the worktree's path and the command that shows its diff**, because an implementation node's work is uncommitted in a checkout outside the repository and `git diff` where the human is standing does not show it — their words on being handed a gate without it: *"what are the changes ? I don't see them in git ?"*. One of the human's two interfaces is the diff, so a gate that describes one and points at nothing has not been presented. The graph's own files are *not* committed per node; they are committed periodically by the human, which is safe only because node files are append-only. Fixed by [Git and code-landing policy](nodes/11-git-and-code-landing.md) and reshaped by [Run an implementation node's work in a worktree](nodes/68-implementation-in-a-worktree.md).

**How many implementation workers run at once is a setting of the effort, and for this effort it is two**, raised from one by the human while directing the manager at the shipping backlog, `verbatim`: *"should we do 2 implementer and 2 grilling to go through the shipping backlog ?"*. **What the manager carries with the second slot** is that two implementation workers may hold two worktrees over the same shipped file, so it picks nodes whose paths are disjoint; the integration-conflict question that raises is [node 115](nodes/115-two-writers-edit-the-map-at-once.md)'s, still open at [node 160](nodes/160-carry-the-integration-conflict-rule-into-the-map.md) and [node 162](nodes/162-how-much-of-the-integration-rule-ships.md). The superseded sentence is also in [map-history.md](map-history.md). A code slot is therefore a count rather than a property, and raising the count changes a number and no part of the lifecycle above. **A slot's occupancy is discovered by counting the live worktrees** — one per claimed implementation node — rather than by inspecting the working tree for uncommitted changes, so the human's own edits no longer read as an occupied slot. Set at [Run an implementation node's work in a worktree](nodes/68-implementation-in-a-worktree.md).

**How the worktree is made, settled at [Should the worktree route drop `EnterWorktree` for plain git, behind a
script](nodes/265-should-the-worktree-route-drop-enterworktree-for-git.md).** Stated beside the landing policy above
rather than rewritten into it, because two pointers in the repository's `.gitignore` cite this section by the quoted
phrase *How the worktree is made*, and [node
152](nodes/152-where-the-harness-worktree-instruction-lives.md) and [node
144](nodes/144-make-the-rules-file-stand-alone.md) hold conditions quoting its phrases. **The route this replaces is
banked whole in [map-history.md](map-history.md).**

- **Create.** The manager makes each implementation node's worktree from the main tree with one plain git command:
  `git worktree add -b worktree-<NN>-<name> .scratch/graph-workflow/worktrees/<NN>-<name>`, where `<NN>` is the
  node's id — so the id is in the path and in the branch. Settled at [node
  265](nodes/265-should-the-worktree-route-drop-enterworktree-for-git.md).
- **Base.** That command lands the worktree on the manager's current `HEAD` by git's own default, so **no base reset
  is performed** and **no `worktree.baseRef` setting is relied on**: it is git's own semantics rather than a
  configuration, so it holds on a machine nobody has configured. Settled at [node
  265](nodes/265-should-the-worktree-route-drop-enterworktree-for-git.md).
- **Creating the worktree, putting it on its base, and writing it need no harness tool call and no sandbox
  override**, by the manager or by the worker. **The removal is the exception, and the *Remove* bullet states it.**
  Settled at [node 265](nodes/265-should-the-worktree-route-drop-enterworktree-for-git.md) and narrowed to those
  three steps at [node
  277](nodes/277-the-removal-step-of-the-worktree-route-does-not-work-as-written.md).
- **The worker writes its worktree by absolute path.** It calls no tool to reach it, enters and leaves nothing, and
  owes no cleanup — there is no first act to get wrong and no refusal to handle. Settled at [node
  265](nodes/265-should-the-worktree-route-drop-enterworktree-for-git.md).
- **Remove, and the removal runs with the sandbox off**: `git worktree remove --force <path>`, then `git branch -D
  worktree-<NN>-<name>`. **Attempted inside the sandbox the removal can fail**, on `.git/worktrees/<name>` with
  `error: failed to delete '.git/worktrees/<name>': Device or resource busy`, and **what it leaves is not a clean
  tree**: the working directory goes, the admin directory under `.git/worktrees/` stays, the entry turns
  `prunable`, `git worktree list` keeps reporting a tree that no longer exists, and the branch will not delete —
  *"cannot delete branch … used by worktree at …"*. **The recovery, for an entry already left stale**, is `git
  worktree prune` with the sandbox off, after which `git branch -D` succeeds. **What fails is the unlink of a mount
  point**: the sandbox places two bind mounts on some worktrees — `.git/worktrees/<name>` read-write and its
  `commondir` read-only — and a mount point cannot be unlinked. **Which worktrees carry them is a fit over seven
  observations rather than a demonstrated mechanism**: every worktree removed by the session that created it
  carried neither mount and came away clean, while the one removal that failed and the only other tree found
  carrying them had each outlived the session that created it. **So the trigger is a worktree outliving the session
  that made it** — and why that is what does it is unestablished, nobody having shown how the mounts come to be
  there. **The trigger is stated so that a reader knows the rule is not paranoia, and not as a condition on when to
  obey it**: a live tree shows no mount to inspect beforehand, the manager cannot always tell which case it is in,
  the override costs one call, and the failure costs a stale entry in the very thing a code slot's occupancy is
  counted from. The two commands are [node
  265](nodes/265-should-the-worktree-route-drop-enterworktree-for-git.md)'s; the rest is settled at [node
  277](nodes/277-the-removal-step-of-the-worktree-route-does-not-work-as-written.md).
- **The commit trailer `Node: <effort>/<NN>` is the join key, and it is the manager's to write.**
- **The route's one failure mode, and the read-only command that catches it.** The route works because
  `.scratch/graph-workflow` is inside the manager's sandbox writable region, and **that has not always been so** —
  in one session the manager's own shell could not append to `flags.md` in that directory while it could write the
  node files one level below. **So the manager runs `test -w .scratch/graph-workflow` before creating a worktree.**
  Where that check fails the worktree can be **neither created nor written** and there is no fallback, no tool call
  being able to widen the region for that path, so it is **raised to the human** rather than worked around. Settled
  at [node 265](nodes/265-should-the-worktree-route-drop-enterworktree-for-git.md).
- **A failed rebase leaves its partial checkout behind, and every retry then meets the dirt its predecessor made.**
  Measured at node 143. `git rebase` reported only `could not
  detach HEAD`; the underlying `git checkout --detach` reports the real cause, which was local changes and untracked
  files that **the previous failed rebase had itself written**. **Cleaning and rebasing in separate calls cannot
  converge.** The repair is one pass: `reset --hard` to the branch's own commit, `clean` the record directory, then
  rebase — and read `git checkout --detach <target>` rather than the rebase's summary when it fails again.

- **A correction round resumes the worker**, and where resume is unavailable the replacement is spawned without
  isolation and pointed at the worktree's absolute path. **The worktree is the manager's and outlives every worker
  in it**, so no respawn can strand work already written there. Flagged at `150.3` as unverified.
- **One sandbox restriction bites this lifecycle.** The operative rule, measured: the sandbox is a set of
  bind mounts **recomputed for every command**, and a command succeeds only where every path it writes lies
  inside a `rw` mount and outside a `ro` one. **The manager reads its own region with**
  `grep " <repo>" /proc/mounts | awk '{split($4,a,","); print a[1]" "$2}' | sort -u` — read-only, one call.
  Whether it is told to, and when, is [node 179](nodes/179-the-manager-sees-its-own-writable-region.md); what
  triggers the overlay on one tree and not another is [node
  180](nodes/180-which-trees-get-the-read-only-skills-overlay.md).
  **The three sub-bullets below are measurements, and two of the operations they name — a reset, and an *entered*
  worktree — are steps of no route any longer**, [node
  265](nodes/265-should-the-worktree-route-drop-enterworktree-for-git.md) having removed both. They are marked here
  rather than removed; the merge step they also name is still in the landing policy above, and what bites it is
  unchanged.
  - **What it hits.** `git merge --ff-only` in the main tree, of a branch that changed a file under `.claude/skills/`
    — `unable to unlink old …`. And `git reset --hard <ref>` inside an *entered* worktree, where the range crosses
    such a file — `Could not reset index file to revision`. `HEAD` does not move and nothing is lost in either case;
    both succeed outside the sandbox. **The manager must expect this rather than discover it**, most of the open
    frontier touching `.claude/skills/`.
  - **What it does not hit, established by experiment rather than inferred.** `git add` and `git commit` from inside
    an entered worktree both succeed. `.git/index` is writable in the main tree and in a worktree's admin directory.
    `git reset --hard` succeeds inside an entered worktree where the commit range touches no file under
    `.claude/skills/`. So the operation is irrelevant; **only the paths the operation must write matter.**
  - **What decides is whether the target path is inside the writing session's writable region**, not which
    tree the command is issued from. From a session whose region did *not* contain the worktree path, `git -C
    <harness worktree> reset --hard` failed on plain `.scratch/` files with `Read-only file system`, no
    skills file involved; from a session whose region *did* contain it, the same command succeeded across a
    `.claude/skills` file. Harness worktrees do sometimes carry their own `<wt>/.claude/skills` `ro` mount.


## Not yet specified

- **The implementation nodes that write the actual skill files.** Three pieces are left, and the manager's own skill is no longer one of them — [Write the first version of the manager's skill](nodes/76-write-the-manager-skill.md) resolved and shipped it. What remains: **starting an effort**, which has a node in [Write the starting-an-effort section and its procedure](nodes/111-write-the-starting-an-effort-section.md); the **adoption mode**, in [Write the adoption procedure](nodes/97-write-the-adoption-procedure.md); and the **cascade's own contract**, in [write the cascade pass's worker contract](nodes/44-cascade-worker-contract.md). The requirements the manager's skill accumulated sit on the nodes that produced them rather than being restated here — chiefly [subagent context contract](nodes/12-subagent-context-contract.md), [what the manager reports to the human](nodes/46-what-the-manager-reports.md) and [collapse the manager's discipline onto `scribe`](nodes/61-collapse-onto-scribe.md), with the cascade's own contract already split out as [write the cascade pass's worker contract](nodes/44-cascade-worker-contract.md). The **adoption mode** waits on [adopting an in-flight effort](nodes/18-adopting-in-flight-effort.md). What would settle the item: a node per remaining file, each with a spawner-written acceptance condition.
- **Whether the Claude Code subagent runtime proves too simple**, and the upgrade path to a firstmate shape — real sessions, worktrees, file mailboxes — if it does. Three ways it could be: node count at the dogfood's 179, an unknown stack, and — economic rather than technical — running a node on a model of the manager's choosing. What would settle it: a dogfood run carrying back the friction record and a **measured spend per node type**. The evidence so far indicts none of the three: the weak point is the long-lived manager thread rather than the fleet under it, per [friction from running this map by hand](nodes/24-self-hosted-friction.md). Parked here at the human's word: what model the manager itself needs, and where a kind-to-model mapping lives. Adjacent: [whether the AFK passes move to the dynamic-workflow runtime](nodes/62-afk-passes-on-the-workflow-runtime.md).
- **Resume and recovery** — what happens when the manager's context compacts or its session dies mid-graph.
  **Mostly discharged by measurement rather than by design, and this is the account.** A fresh manager ran this
  effort's graph cold at the start of a session and reconstructed it from the files alone; at the end of that session
  it verified, against three live nodes, that the **three states the manager's contract ~~says~~ then said "nothing in the files
  shows" are in fact derivable**, which its section `### Three states the status line does not show` has stated since
  [node 314](nodes/314-the-manager-contract-says-three-node-states-show-in-no-file.md) landed as `4cc74de`:
  - **waiting at a gate** — `Status: claimed`, a `## Review` carrying a checker outcome, and no `### Gate` entry;
  - **a worker holding an unanswered question** — `Status: claimed`, a `## Interview` holding a question, and no
    answer recorded under it;
  - **banked and parked** — `Status: open` with a non-empty `## Interview`, which `graph-conventions.md` already
    states.
  A live worktree comes from `git worktree list`, and the code slot's occupancy from counting them. **What does not
  survive is the routing keys**, and nothing needs to: resumability dies with the manager's session, so every attempt
  is unresumable to a fresh thread and the contract's replacement procedure — replay everything the human said,
  marked settled — is what runs. Each node's `## Interview` records that its key does not survive.
  **What is left unspecified is narrower than this item began:** why the manager chose the nodes it chose, which no
  file holds. Worth reading if that is ever taken up, per [dogfood target](nodes/09-dogfood-target.md): Lang's
  hand-built `handoff.md` is a human's manual answer to the whole problem.
- **How the human sees graph progress.** Their two interfaces are settled — the manager's narration and code review — so what is left unspecified is narrower than the item started: the **frontier** and the **outstanding flags** are surfaced by nothing, and a **parked** node, a **superseded** one, and an implementation node **holding the code slot while it waits at its gate** all read as an ordinary open node. What would settle it: a decision on whether anything renders the graph, and on what it shows. Shaped by [relay protocol](nodes/08-relay-protocol.md), [graph file format](nodes/13-graph-file-format.md), [git and code-landing policy](nodes/11-git-and-code-landing.md), and [what the manager reports to the human](nodes/46-what-the-manager-reports.md), which is the control side of the same problem.
- **How the workflow reaches a repository that is not this one.** Whether anything beyond copying the skill files is needed — an install step, a per-repo bar file, a way to carry these conventions into a repo with its own tracker doc — is not sharp enough to be a question. The named dependency is the six **method skills**, none of them per-repo. What would settle it: a decision on whether expedition **vendors its own discipline** rather than borrowing its ancestor's. Shaped by [done-ness and termination](nodes/10-done-ness.md), [subagent context contract](nodes/12-subagent-context-contract.md), [workflow self-improvement during use](nodes/19-workflow-self-improvement.md), [reconcile a method skill's instructions with the contract's hard rules](nodes/48-method-skill-conflicts-hard-rules.md) and [what a contract may name as a method skill](nodes/51-what-a-contract-may-name.md).
- **When to flip landing to asynchronous**, and what changes in the human's day when it happens. The seam is one step — the manager committing before the gate rather than after — but one gate outcome does not survive it: **reject** becomes a forward revert rather than a cleaned tree, so the cheapest of the three becomes the most expensive and the only one that marks history. What is unspecified is what asynchronous review looks like from the human's side. What would settle it: the trigger, which is the code slot idling on human attention and now has two claimants rather than one. Shaped by [git and code-landing policy](nodes/11-git-and-code-landing.md), [human review of landed code](nodes/20-human-code-review.md) and [when an AFK worker cannot proceed](nodes/23-worker-cannot-proceed.md).
- **What never-delete costs the reader of a node file.** Settled for this map, whose history moved out, and open for the **node files**: a worker's first act is to read its own node, and several interleave struck-through paragraphs with live ones. Struck text is a rounding error — 0.4% of the node corpus — so the cost is **live restatement under append-in-place** rather than supersession. What would settle it: whether an item's updates are capped, pruned into an archive, or accepted with a rendered view over them. Pruning has been used once, on a near-duplicate: not yet a practice. Shaped by [friction from running this map by hand](nodes/24-self-hosted-friction.md), [how an agent workflow and its skills reduce their own token cost](nodes/52-token-cost-of-a-workflow.md) and [what the token findings change in the workflow and its skills](nodes/53-what-token-findings-change.md).
- **Nothing watches a standard that lives outside this repository.** The cascade fires when this graph's own decisions move, and an external yardstick can move under a resolved node with nothing noticing — one did, within an hour of the node that read it resolving. What is unspecified is the remedy, which is why this is fog rather than a node built on a guess. What would settle it: a decision on whether anything re-reads an external source, and on what trigger. Shaped by [review every shipped file against `/writing-great-skills`](nodes/47-review-shipped-skills.md) and [re-review the shipped files against `/writing-for-agents`](nodes/54-review-against-writing-for-agents.md).

## Out of scope

- **Multi-repo and remote fleets** — firstmate's secondmates, SSH-reachable homes, cross-machine dispatch. Beyond a single-repo workflow.
- **Non-Claude-Code harness support** — Codex, Grok, OpenCode. The runtime decision picked one harness deliberately; portability is a different effort. **Still out of scope, and now with an expectation attached:** the human intends to come back for a heterogeneous fleet once v1 works, driven by Claude credit scarcity rather than preference. Under this map's own rule that is a redrawn destination and therefore a fresh effort inheriting v1's contracts, not a resumption of this one. Recorded here rather than graduated — nothing in this section becomes fog.
- **External channels** — firstmate's Relay (X, Discord). The destination names one human on one channel.
- **Cost and token accounting**, dashboards, fleet telemetry. **This line contradicts two fog items above, and [How an agent workflow and its skills reduce their own token cost](nodes/52-token-cost-of-a-workflow.md) sharpened the contradiction rather than resolving it.** The Notes above require the dogfood to carry back a **measured spend per node type**, and the fog item on runtime simplicity requires the same. Meanwhile the harness already *prints* what those ask for: `/usage` attributes recent usage to **skills, subagents, plugins and individual MCP servers** as percentages, reports cache read against cache write per model, resets on `/clear`, and raises **behavior flags** *"such as long context or cache misses, flagged when one accounts for 10% or more of recent usage"*; `/context` shows what consumes space; a statusline reading `current_usage` shows creation against read live; OpenTelemetry exports per-session cache counts. That worker's own framing, reported rather than decided: **reading numbers the harness already prints is not building accounting**, and as written this line reads as forbidding the measurement the fog demands. Not resolved here, because narrowing an out-of-scope line is a scoping act and this section's own rule is that nothing in it becomes fog without the destination being redrawn. It is one line for the human, and it is [What the token findings change in the workflow and its skills](nodes/53-what-token-findings-change.md)'s if they would rather it be decided with the rest.

- **When `qmd` is worth reconsidering.** Refused for now at [What to do about the record's token cost, given what
  `qmd` turns out to be](nodes/129-what-to-do-about-the-records-token-cost.md), on the ground that its saving over
  plain search is unmeasured and the free alternative it would replace had never been instructed. **The trigger is a
  worker reporting that it could not find a fact because it did not know the fact's wording** — the one thing `qmd`
  does that lexical search cannot. What would settle it: such a report, after the search-the-record instruction has
  landed. Held by nothing but this line and the manager reading it.
- **When `decisions.md` stops being small enough.** The human kept it on every worker's read-whole list, `verbatim`:
  *"it's small enough"*, on the ground that a fed context is used where a search is not. That ground has two halves
  and only one expires: the mechanism does not, but the size claim is about a file that grows by one capped line per
  resolved node and never shrinks. **The anchor is this effort's own precedent — `map.md` was judged to need
  splitting at 43,847 bytes** — and it is node 129's worker's number rather than the human's, flagged at `129.4`.
  What would settle it: `decisions.md` approaching that size, at which point part (ii) of node 129's package is
  re-offered.
