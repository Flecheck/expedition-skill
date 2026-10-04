# Whether the worktree lifecycle is worth putting behind a script

Type: grilling
Status: resolved

Blocked by: none

## Answer

No script for the worktree lifecycle: shipping one would hard-code this effort's landing policy against ground rule 1, and the hand-run commands rarely fail since their rules were written.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. It surfaced no node. Its `INVALIDATIONS` extend node 265; the manager notes it here and edits nothing. Flags 270.1, 270.2 settle at the node closing report.

## Question

*Surfaced by [node 265](265-should-the-worktree-route-drop-enterworktree-for-git.md)'s worker, and pasted as it
wrote it. **The question inside it is the human's own**, given alongside node 265's and deliberately held back from
that payload because its answer depended on node 265's.*

> The human's own, `verbatim`: *"We can maybe create a script to do to simplify the work"*. Node 265 settled which
> route a script would automate and did not settle whether to build one. The lifecycle is now four plain git
> commands — create, the `test -w` check, remove, delete branch — with no harness tool in the path, so a script can
> carry the whole of it for the first time. What a script would have to be worth: it would be the first executable
> artifact this effort ships, it would need to work on a repository this machine has never seen under ground rule 1,
> and the alternative is four commands written in the map.

**Blockers, in the worker's words:** *"none. Node 265 has settled what it depended on."*

## The manager's note at filing

*Not a change to anything above.*

**The manager has now run the new route once, by hand, and offers that as material rather than as a position.**
Creating [node 269](269-ignore-the-new-worktree-path.md)'s worktree was four things in one command line: the `test
-w` check, `git worktree add -b`, and two reads confirming the tree landed on `HEAD`. It needed no reset and no
sandbox override, and it is the first worktree this effort ever made without a harness tool.

**What the manager does not know and will not guess**: whether four commands run twice per node is friction worth an
artifact, or whether the friction the human was reacting to was the *old* route's reset and override — both of which
node 265 removed without any script at all.

**Ground rule 1 is the sharp edge here and it is not a formality.** *"Nothing in the shipped files may assume this
repo, this machine, or a toolchain."* A script is a toolchain assumption in a way four documented commands are not,
and this effort has never shipped an executable. Whoever works this should treat that rule as the question rather
than as an obstacle to route around.

## Interview

#### Question 1, relayed 2026-10-04

*Pasted as the worker handed it back.*

`````
NODE:          Whether the worktree lifecycle is worth putting behind a script (node 270)
ABOUT:         This node decides your own suggestion at node 265: "We can maybe create a script to do to simplify the work". It comes up now because node 265 held it back until the worktree route was settled. That route is now plain git, with no harness tool in it.
SO FAR:        - What the manager runs for each implementation node today. This comes from `map-manager-only.md`'s `## Landing an implementation node's work` and from the manager's own account.
                 - When the worktree is cut: commit the record, run `test -w .scratch/graph-workflow`, then `git worktree add -b worktree-<NN>-<name> <path>`.
                 - At landing: make a path-limited commit in the worktree, rebase it onto master, run `git diff --check`, `git merge --ff-only`, `git worktree remove --force` and `git branch -D`.
                 - The last three steps have to run with the sandbox off: the merge under node 369, the removal and branch delete under node 277.
                 - The rebase often hits a two-block conflict at the end of `map-history.md`, which the manager fixes by keeping both blocks. That is the manager's account and I did not re-check it. `git diff --check` is the manager's own habit and is written nowhere in the record.
               - How often: about 84 landings since the plain-git route came in on 2026-09-22. I counted `Node:` commit trailers on 2026-10-04. This number is for scale only, so re-derive it before relying on it.
               - Removing the reset and the `EnterWorktree` call (node 265) did not remove the friction. Four incidents came from running correct commands in the wrong place or the wrong way:
                 1. A relative path run from the wrong directory doubled the worktree path. That left two whole worktrees untracked and not ignored, and the record commit nearly staged them. This is node 284, still open.
                 2. A removal run inside the sandbox left a stale worktree entry and a branch that would not delete (node 277).
                 3. A merge run inside the sandbox wrote some of its files and then blocked the retry (nodes 234 and 369).
                 4. A failed rebase left a partial checkout behind, and every retry ran into it (measured at node 143).
               - Script precedent: this node's question says the effort has never shipped an executable. That is out of date. `.claude/skills/expedition/scripts/frontier.sh` ships (nodes 273 and 285). The effort also keeps one script that is not shipped, `.scratch/graph-workflow/scripts/search-conditions.py` (node 313).
                 - Node 273 shipped `frontier.sh` because ground rule 1 protects the host project's stack, and that script reads only the expedition's own markdown.
                 - Node 273 also said plainly that its yes does not carry over to this node, because this script would run git against the host repository.
               - What the shipped files say about worktrees: almost nothing, on purpose. `SKILL.md` says "How code lands is set by the effort's own landing policy", and fixes only the order: approval before any commit, the graph before cleanup. The worktree directory inside the repository, the branch names and the sandbox workarounds are all this effort's own practice, written in `map-manager-only.md`. Flag 68.2 refused to assume an ignore rule in a repository the workflow does not own, and it is still open.
ASK:           Should the worktree lifecycle get a script? If so, should it belong to this effort only, in `.scratch/graph-workflow/scripts/` beside `search-conditions.py`, or ship with the skill files beside `frontier.sh`?
RECOMMENDED:   Yes, as a script for this effort only, not shipped.
               - Why a script: the commands run about twice per node, and all four incidents came from how the commands were run, not from what they said. A script fixes that by construction:
                 - It builds the absolute path from `git rev-parse --show-toplevel`, so node 284's doubled path cannot happen again.
                 - It runs the steps in the order the landing policy states.
                 - Its landing half is one call with the sandbox off instead of three.
                 - Fewer manager tool calls per landing also fits "most of the context lives in the workers".
               - Why not shipped, which is the ground rule 1 question:
                 - The script would hard-code exactly what the shipped files leave to each effort's landing policy: a worktree directory inside this effort's record, this effort's branch names, and workarounds for this machine's sandbox. Shipping it would make one effort's landing policy the workflow's, which reverses the split `SKILL.md` states.
                 - It would also make the shipped skills longer, and you want them compacted.
                 - Kept inside the effort, it is not a shipped file, so ground rule 1 does not apply. It can also rely on this repo's facts, such as the bar having no build or test commands, so `git diff --check` is the whole post-rebase check.
               - The shape I would write into the implementation node's acceptance condition: one POSIX sh script with three commands.
                 - `create <NN> <name>`: runs the `test -w` check, then `git worktree add -b` at the absolute path. If the check fails, it stops and reports.
                 - `land <NN> <name>`: runs with the sandbox off, after the manager's own commits. Those commits stay by hand because the paths, the message and the `Node:` trailer need the manager's judgement. It rebases, runs `git diff --check`, merges with `--ff-only`, removes the worktree and deletes the branch.
                   - On any conflict or failure it stops and prints git's message. It never resolves a conflict, never aborts a rebase and never discards a file.
                   - The `map-history.md` union stays the manager's to resolve by hand, after which the manager runs `land` again.
                 - `discard <NN> <name>`: for a reject or a superseded node, runs `remove --force`, `prune` and `branch -D`, with the sandbox off.
               - The landing section's Create and Remove bullets would then point at the script instead of listing the commands. Everything else in that section stays.
               - Node 284 (the Create bullet's relative path) is open, in the same file and about the same concern, so it would join that node.
ALTERNATIVES:  - No script, keep the commands written in the landing section. Set aside: all four incidents happened while the commands were already written there correctly.
               - Ship it beside `frontier.sh`. Set aside under ground rule 1, for the reasons above. Wanting it later would mean a new grilling node on what landing policy the workflow itself ships.
               - Script only `create` and `discard`, and keep landing by hand. Set aside: the merge and rebase incidents, and the calls that need the sandbox off, are all in the landing half.

RETROSPECTIVE
1. What I had to hunt for:
   - Whether the shipped files say anything about how a worktree is made. They do not: `SKILL.md` leaves landing to each effort's policy. That fact is what decides shipped versus effort-only.
   - The incidents after node 265. These were in nodes 284, 277, 234 and 369, not in node 265.
   - The landing count, from commit trailers.
   - That an effort-only script already exists (`search-conditions.py`). The map never mentions it.
2. What arrived that this node did not need: most of `decisions.md`. The lines that bore on this node were 05, 68, 265, 273, 277, 285, 313, 234, 369 and 284's neighbours, about ten of 300 lines. Most of `map.md`'s standing preferences beyond ground rule 1, "most context in workers" and the compaction wish.
3. What would have made this easier:
   - A spawn line saying that the shipped files leave the landing policy to each effort.
   - A spawn line listing the incident nodes since node 265.
4. What was stale, wrong or contradictory:
   - The node's question says the script "would be the first executable artifact this effort ships". The manager's note was right that this is stale, because `frontier.sh` ships.
   - The question calls the lifecycle "four plain git commands". The real per-node sequence is about nine steps.
   - The manager's note puts all three sandbox-off steps under node 369. Node 369 covers only the merge. The removal and the branch delete are node 277's.
`````

*The manager's note:* the worker is right that the manager's spawn put all three sandbox-off steps under node 369. Node 369 covers the merge, and node 277 covers the removal and the branch delete.

#### The human's answer to question 1, 2026-10-04

`verbatim`: *"for 270, I would say that we want either a shipped script or no script.  since you say shipping a script would be bad because there is logic specific to this project I would say no script ? I guess the script for only this effort is fairly low value but we could still make it if you think mistakes happen often and it would improve things"*

*The manager's note:* **a divergence.** The reply does not take the `RECOMMENDED` (a script for this effort only). It leans to the alternative "No script, keep the commands written in the landing section", and leaves the effort-only script open on a condition: "if you think mistakes happen often and it would improve things". That condition is a judgement handed back, so it goes to the worker holding the interview, not to the manager.

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      Whether the worktree lifecycle is worth putting behind a script

ANSWER:        **No script.** The worktree lifecycle stays as commands written in `map-manager-only.md`'s `## Landing an implementation node's work`. No script is built for it, shipped or kept in the effort.

               **Why not shipped.** The human's words were: *"we want either a shipped script or no script"*. A shipped script is ruled out by ground rule 1. It would put into the shipped files what those files deliberately leave to each effort's own landing policy. `SKILL.md` says *"How code lands is set by the effort's own landing policy"* and fixes only the order (approval before any commit, the graph before cleanup). The script would hard-code all of these:
               - a worktree directory inside this effort's record, `.scratch/graph-workflow/worktrees/`;
               - this effort's branch names;
               - workarounds for this machine's sandbox, namely the merge and the removal run with the sandbox off.

               Node 273 shipped `frontier.sh` because that script reads only the expedition's own markdown. That ground does not reach a script that runs git against the host repository, and node 273 said so itself (flag 273.3).

               **Why not a script kept in the effort.** The human made this conditional: *"we could still make it if you think mistakes happen often and it would improve things"*. The worker judged that mistakes do not happen often, on the record as of 2026-10-04:
               - Under the plain-git route (in force since 2026-09-22) the record holds two lifecycle incidents. Node 277 is a removal run inside the sandbox that left a stale worktree entry. Node 284 is a relative path run from the wrong directory, which doubled the worktree path. Both nodes were filed on 2026-09-24, in the route's first days.
               - Each incident was answered by a written rule or habit: node 277's sandbox-off removal, and the manager's switch to absolute paths. Node 284's rewording of the Create bullet is still open.
               - Two other incidents are older than the plain-git route: node 234's partially written merge (filed 2026-09-13) and the rebase leftovers measured at node 143 (filed 2026-09-04). Node 234's has since been answered by node 369's rule that the merge runs with the sandbox off from the first attempt.
               - The worker found no lifecycle incident recorded after 2026-09-24. There have been about 84 landings since 2026-09-22, counted from `Node:` commit trailers on 2026-10-04. That count is for scale only and is to be re-derived before anyone relies on it.

               The failures came at the start of a new route and were each closed by a written line. They are not recurring. So a script would mainly save the manager a few tool calls per landing, and it would be a second statement of the landing policy that the map's text then has to be kept in step with. On that evidence it is not worth building, and the human's own reading — *"fairly low value"* — stands.

               **What this leaves in place.** Node 284 is now the only fix for the Create bullet's relative path, since no script will build that path by construction.

INDEX LINE:    No script for the worktree lifecycle: shipping one would hard-code this effort's landing policy against ground rule 1, and the hand-run commands rarely fail since their rules were written.

FLAGS:         DELEGATED — The human made the effort-only script conditional on the worker judging *"if you think mistakes happen often and it would improve things"*. The worker judged that they do not, and answered no script. Its evidence was dated incidents set against landings counted from commit trailers on 2026-10-04:
               - Under the plain-git route since 2026-09-22 there were two incidents (nodes 277 and 284), both filed 2026-09-24, and each answered by a written rule or habit.
               - Nothing later was found, across about 84 landings (scale only; re-derive).
               - The other two incidents (nodes 234 and 143) are older than the route. Node 234's has been answered by node 369.
               The judgement also corrects the worker's first payload. That payload listed all four incidents as evidence that the friction outlived node 265, and two of them are older than node 265. A later run of hand-run failures under the route would reopen the question as an effort-only script, which the human left open on exactly that condition.
               Index sentence: The worker decided, at the human's handing back, that the hand-run worktree commands fail too rarely to justify a script for this effort only, so none is built.

               ASSUMPTION — The worker reads the human's *"we want either a shipped script or no script"* as the ground for this answer only. It is not proposed as a standing rule for the effort's map, because the human did not say to add a rule, and under node 93 a rule binds only once it is written in the map.
               Index sentence: The human's "either a shipped script or no script" is recorded as this node's ground, not written into the map as a standing rule about scripts.

NEW NODES:     none

INVALIDATIONS: No resolved node is contradicted.
               - Node 265 is extended. Its name ends "behind a script", and it held the script half back, ending its answer with *"The script half is not settled here"*. That half is now answered: no script.
               - Node 273's flag 273.3 (*"a yes here does not carry a yes there"*) agrees with this answer and is unchanged.
               - Node 05's answer that skills may ship executables is unchanged.

CONDITIONS:    Searched the `## Question` and `## Acceptance condition` sections of every open and claimed node for: `script`, `four commands` / `four plain git commands`, `executable`, `node 270`, and the lifecycle-script wording. Searched resolved nodes' `## Answer` sections for `node 270` and for lifecycle-and-script wording.
               - The only open match is node 270 itself.
               - Node 284 (the Create bullet's relative path) did not match the search. I checked it by hand: its question and condition are unchanged by this answer, and it remains needed, since no script will supply the absolute path.
               - No replacement clause is written, and no open node's question is changed.

MISSING FROM MAP: `map.md` did not say that the shipped files leave the landing policy, and so the whole worktree lifecycle, to each effort. That fact decides shipped versus kept-in-the-effort. I found it in `.claude/skills/expedition/SKILL.md` ("How code lands is set by the effort's own landing policy") and in `graph-conventions.md`'s description of `map-manager-only.md`. `map.md` also never mentions that the effort keeps scripts of its own in `.scratch/graph-workflow/scripts/`; I found that by listing the directory.

RETROSPECTIVE
1. What I had to hunt for:
   - That the shipped files leave the landing policy to each effort (in `SKILL.md`, not the map).
   - The incidents after node 265, which are spread across nodes 277, 284, 234 and 369.
   - Each incident's filing date, from git, to tell which ones are older than the plain-git route. This is the fact the delegated judgement turned on, and I did not check it before my first payload.
   - The landing count, from commit trailers.
   - The effort-only `scripts/` directory.
2. What arrived that this node did not need:
   - Most of `decisions.md`; about ten of its roughly 300 lines bore on this node (05, 68, 265, 273, 277, 284, 285, 313, 234, 369).
   - Most of `map.md`'s standing preferences other than ground rule 1, "most context in workers" and the compaction wish.
   - The landing section's sandbox measurements beyond the merge and removal bullets.
3. What would have made this easier:
   - A dated list of lifecycle incidents in the spawn, or a derivation in `derivations.md` that lists them.
   - A line in the spawn saying that the shipped files leave the landing policy to each effort.
4. What was stale, wrong or contradictory:
   - The node's question says the script would be the first executable this effort ships. That is out of date: `frontier.sh` ships.
   - The question calls the lifecycle "four plain git commands". The real sequence per node is about nine steps.
   - The manager's first spawn note put all three sandbox-off steps under node 369. Node 369 covers only the merge; the removal and branch delete are node 277's.
   - My own first payload was wrong: it presented two incidents older than the route (nodes 234 and 143) as evidence that the friction outlived node 265. It is corrected in the DELEGATED flag above.
   - The coordinator's message checked out: the divergence it reports matches the human's words, and it is right that the conditional hands the judgement back to me.
`````

## Flags

`270.1` `DELEGATED` **· settled** — The worker judged, at the human's handing back, that hand-run worktree commands fail too rarely to justify an effort-only script. *(The worker's full text is under its handover's `FLAGS`.)*

`270.2` `ASSUMPTION` **· settled** — The human's "either a shipped script or no script" is this node's ground, not a standing rule in the map. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-10-04:* flags 270.1, 270.2 settle at the node closing report that closes this node.
