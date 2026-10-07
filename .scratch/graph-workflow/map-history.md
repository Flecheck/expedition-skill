# Map history: what `map.md` used to say

The append history moved out of [`map.md`](map.md), verbatim. Every quoted paragraph below stood in that
file and stands here unchanged: nothing was summarised, shortened, reworded or dropped on the way out.
The headings, and the occasional italic note beside a quotation, are this file's own.
**Nothing here is needed in order to work a node.** The map keeps each note, standing preference and fog
item it carries; what is here is the account some of them had accumulated behind that statement. A note
the map carries and this file does not quote had no such account to move.

Moved by [Restructure `map.md` to what every worker needs](nodes/59-restructure-the-map.md), carrying
out the decision at [What the token findings change in the workflow and its
skills](nodes/53-what-token-findings-change.md): every worker read the whole map cold and uncached once
per node, and about three quarters of what it read was history it could not act on. The move deletes
nothing, so it needs no exception to the never-delete rule and no judgement about any single paragraph
— the same bulk verbatim move [decisions.md](decisions.md) was created by.

**How to read it.** The sections below mirror the map's own, in the map's order. Text already marked
`~~struck through~~` was superseded before the move and stays struck. Where the map now carries a
shorter form of something quoted here, the map's form is the live one and this is the earlier one.

## The map's retired header

~~Label: wayfinder:map~~ **Retired** by [Naming](nodes/14-naming.md): a wayfinder artifact with no function in a markdown tracker, where one file named `map.md` identifies itself. The word `label` now belongs to the per-node `Labels:` field and nothing else.

## Notes

### `/writing-for-agents`: a preference recorded, obstructed twice, dissolved, renamed and landed

Its live residue is the ground rule the map still carries, the one beginning *“Prose deliverables are held against the `/writing-for-agents` standard”*.

**And `/writing-great-skills`, for writing and for reviewing the skill files themselves.** The human's instruction, added while three nodes were in flight: *"For the map, I think we should use /writing-great-skills to help write skill and to review skills"*. It belongs here more than any of the others do, because this effort's product **is** skill files — so a reference on what makes a skill predictable is a standard the work should be held against rather than a method for reaching a decision. It bears on both halves of an implementation node: the worker writing a contract, and the bar the checker holds it to, the checker's own contract already telling it to go and find *"a skill that reviews code, or anything doing that job under another name"*.

**Two obstructions the manager found on filing that instruction, neither of them resolved and neither this note's to resolve.** First, **it cannot be invoked by any agent the workflow spawns.** Its frontmatter carries `disable-model-invocation: true`, and its own body states what that means: *"only you, typing its name, can invoke it — and no other skill can."* So it never appears in a worker's or a checker's skill list, and the *invoke if present* patch the contracts use for every other method skill is inoperative for this one. It reaches an agent only as a **file to be read**, or as text the manager carries — and the manager carrying it is what makes the manager the author of the standard, which [An acceptance condition is self-contained text](nodes/33-condition-is-self-contained.md) forbids for conditions and the same reasoning resists here. Second, **it is a plugin skill, from the same `mattpocock-skills` plugin as `/grilling`, `/domain-modeling` and `/prototype`.** So it is a **seventh** method skill that does not travel, deepening rather than easing the defect recorded in the fog under *how the workflow reaches a repository that is not this one* — and it lands squarely on the sharper question that item already holds, whether expedition must vendor its own discipline rather than borrow its ancestor's. Reading it by path is possible and the path is a nix store hash, which is machine-specific and not a thing to ship.

~~So this preference is **recorded and not yet carried into the shipped files**: what a spawn may say about a skill no spawned agent can invoke is an open question rather than an edit anybody can make. Recorded here rather than minted as a node because the shape of the fix is exactly what is unknown, and a node minted around a guess would be the delta-list failure over again.~~

**Settled by the human as soon as the obstructions were put to them**, in their words: *"It won't be shipped, it's specific to this repo."* So this is a **repo-specific standing preference and nothing is carried into the shipped skill files at all** — which dissolves both obstructions rather than working around them, and neither of the two findings above survives as a problem.

The travel obstruction goes away because nothing travels: a preference that is never shipped cannot fail to reach another machine, and this adds no seventh dependency to the fog item it appeared to deepen. The invocation obstruction goes away by a route that landed the same day and was not written for this: a **worker** reads `map.md` and therefore reads this note directly, and a **checker** reads no map but now receives the effort's ground rules as text copied into its spawn, fixed by [The checker's spawn carries the effort's ground rules](nodes/42-checker-spawn-carries-ground-rules.md). Both parties are reachable already, and neither needs to invoke anything.

What remains true and is a fact rather than an obstruction: **the skill is user-invoked, so an agent reads it as a file and never fires it by name.** Both parties should be told to go and find it rather than given a path — the two copies on this machine sit under different nix store hashes, so a path is not stable even here, while the skill is locatable by name inside the `mattpocock-skills` plugin under `skills/productivity/writing-great-skills/`, with its full definitions disclosed to a `GLOSSARY.md` beside it. That is this map's own standing preference applied to itself: **prefer properties that are discovered over commands that are declared.**

~~**And `/writing-great-skills`, for writing and for reviewing the skill files themselves.**~~ **The skill is now `/writing-for-agents`, and everything above about it is stale in three places.** The human's words: *"Also, I did an update, /writing-great-skills was renamed/changed to /writing-for-agents."* Measured rather than taken on trust: it is **not on this machine** — both `mattpocock-skills` copies in the nix store still hold `writing-great-skills`, nothing named `writing-for-agents` exists under the store paths, `~/.claude/`, `~/dotfiles/` or this repo, and **no skill reload changes that**, the plugin being a nix flake input pinned in `~/dotfiles/flake.lock` at rev `2ab9580` against an upstream `HEAD` of `5b15a47`. What is stale: **it is not a rename** — the scope widened from skills to *"any document an agent consumes"*, `GLOSSARY.md` (201 lines) was replaced by `SKILL-MECHANICS.md` (22 lines) with the definitions folded inward, and two concepts are new (**the two loads**, and **sprawl** as a failure mode distinct from duplication). **`disable-model-invocation` is gone**, so the fact recorded above — *"the skill is user-invoked, so an agent reads it as a file and never fires it by name"* — will be **false** the moment the input is updated, and the whole invocation obstruction this note spent three paragraphs dissolving stops existing rather than being worked around. And **the preference itself is unchanged**: this stays a repo-specific standing preference that is never shipped, per the human's *"It won't be shipped, it's specific to this repo."* **The input has now been updated and the skill is on disk**, at a third store path, with `flake.lock` pinned at `5b15a47` — so *"will be false the moment the input is updated"* is now simply **false**: `disable-model-invocation` is gone, the skill is **model-invoked**, and an agent can fire it by name rather than reading it as a file. Every workaround the three paragraphs above reasoned through is retired in fact. Two facts replace them. **A session already running does not see it** — the skill registry is loaded per process against a store path that changed, so any worker that must *invoke* the standard has to be spawned from a session started after the rebuild. And **the store path changed twice in one day**, which is this map's *prefer properties that are discovered over commands that are declared* earning its keep for the third time on this one skill: nothing may ever carry that path. Held against the new text by [Re-review the shipped files against `/writing-for-agents`](nodes/54-review-against-writing-for-agents.md); the token half of it feeds [How an agent workflow and its skills reduce their own token cost](nodes/52-token-cost-of-a-workflow.md) and both land at [What the token findings change in the workflow and its skills](nodes/53-what-token-findings-change.md).

### Standing preferences: the seven bullets that had an account behind them

Seven of the map's eleven standing preferences had an account behind them, and those seven are quoted
below in the form they had before the map kept the preference alone — the nodes that found it, the
measurements behind it, and the reasoning that produced it. All eleven are still live, and the map still
holds a bullet for every one, the other four unchanged and so not quoted here.

- **The human is the scarce resource.** Parallelism exists to saturate the human, not the machine. **This is right about what to optimise and wrong about what fails first**, per [Friction from running this map by hand](nodes/24-self-hosted-friction.md): the human never broke, and a node cost the manager ~200k tokens of context, compacted between nodes as standing procedure. At the dogfood target's 179 nodes that is ~36M tokens of manager context if the manager keeps doing the work itself.
- **Most of the context lives in the workers, not in the manager.** The human's stated intent, verbatim: *"Ideally in the final workflow, most of the context is in the workers and not in the manager."* It governs decisions no single node owns — what a spawn carries, what a handover returns, whether the manager renders or points, and whether the manager grills a node itself when it could delegate. A manager that ends a node holding everything the node held has failed at its job even if the node resolved. The inherited sizing rule budgets **100k per node**; the manager has been paying double, and the difference is its own overhead rather than the node's work.
- **The node files are written for agents. The human works from the manager's chat and from code review.** Their words, `verbatim`, at [Carry the recorded deltas into the shipped skill files](nodes/26-carry-deltas-into-shipped-files.md)'s gate: *"I expect the nodes to be mostly targeted to agents, as I will mostly work from what the manager says (questions from subagents) and with code review."* Four things follow. **A node's reader is the next agent**, so completeness for an agent beats brevity for a human, and the density of these files is correct rather than a failure of editing. **The human's two interfaces are the manager's chat payload and the diff**, which is why both must stand alone — the same message required a flag to reach them with what was done, why, and the context, *"Idealy I don't have to go into the files to find out what happened and how to respond"*. **It answers part of the fog item on how the human sees graph progress**: the view is the manager's narration plus code review, not a rendered graph — leaving only the frontier and the outstanding flags genuinely unsurfaced. And **it reprices the never-delete tension rather than dissolving it**: a bloated node costs *agent context* instead of human patience, and [Friction from running this map by hand](nodes/24-self-hosted-friction.md) already found agent context to be the binding constraint. Not cheaper — differently expensive, and against the resource that was already failing first.
- **The manager never idles, and proposes the next work itself as each node finishes.** The human's standing instruction, `verbatim`: *"You can start new tasks. You should automatically propose to start a new task when a task finish"*. So a closing report is not an ending: it names what is being started next. This is **recorded here rather than held in the manager's context** because that is what [What the manager works on next, and how the human redirects it](nodes/16-human-steering.md) fixed for a standing instruction, and it is the first instruction filed under that rule — arriving one message after that node resolved. It **confirms** rather than contradicts that node's *the manager picks and reports; it never asks*: proposing is the report, and the human's override is one line. What it adds is that the report is owed **automatically at the moment a node closes**, where the node had only fixed what the report contains.
- **Approving a node's end settles that node's flags.** The human's standing instruction, `verbatim`: *"Also, when I approve the end of the node, the flags should be considered ok"*. So the manager does not ask a second time — the approval at a gate, or the last answer on a grilling node, **is** the settlement. Filed here under the rule [What the manager works on next, and how the human redirects it](nodes/16-human-steering.md) fixed for standing instructions, and annotated onto [Whether flags.md survives the settle-at-close practice](nodes/27-does-flags-file-survive.md), whose practice it refines. **The consequence the manager must carry:** the gate payload has to present every flag the node holds, because approval now discharges them — a payload that omits one settles it silently.
- **Every worker returns a retrospective as a sixth handover part, on this effort only.** The human's standing instruction, `verbatim`: *"Could you, for this effort only, ask subagents, when they finish the node, a retrospective of what could be improved (making the work easier, something else), where the tokens are used, what could be done to use less tokens (better access to the information they need ? so they don't have to try to find it ? useless information ? something else ?)."* **Effort-scoped and never shipped**, like the `/writing-for-agents` preference — so it is carried in the spawn and changes no contract. It is compatible with the handover shape rather than a departure from it: *"five parts, every time… never leave a part off"* is a floor, not a ceiling, and node 28's floor on the manager forbids widening what a worker **writes to a file**, which returned text is not. **It goes in the spawn and not in a follow-up, which is the one design call the instruction left open**: asking after the handover is a resume, and node 52 measured that a subagent's cache expires in five minutes, so a late question re-pays the worker's whole conversation — node 53's worker measured its own at ~52,000 tokens, more than twice the map read the whole exercise is trying to reduce. Asked in the spawn it costs output tokens only, and it still answers *when they finish the node*, the retrospective being part of the handover. **The worker is asked only what it can know.** It has no tokenizer (flag `52.1`) and no view of its own usage, so it reports what it hunted for, what it read and did not use, what would have made the work easier, and what it found stale or contradictory; the manager supplies the numbers from `/usage`'s per-subagent attribution and `/context`, which node 52 established the harness already prints. **The four questions, as the spawn puts them:** what did you have to hunt for — the fact, where you found it, where you looked first; what did you read and not use; what would have made this node easier, in the spawn, the node file, or the contract; and what did you read that was stale, wrong, or contradicted something else. It **files as a `## Retrospective` annotation on the node**, which keeps the mandatory section order untouched. Two costs stated rather than discovered: the retrospective is itself output tokens on every node and text every later reader of that node pays for, and **nothing aggregates them** — the aggregate being the whole point, that is the same defect node 48's worker named about left-unrun method-skill parts, and for now the aggregate is the manager's report rather than a file. Distinct from [Workflow self-improvement during use](nodes/19-workflow-self-improvement.md)'s `FRICTION` flag, which is opportunistic, raised where noticed, and travels off this repo; this is systematic, asked every time, and never leaves it.
- **Token-use improvement is prioritised above the rest of the frontier.** The human's standing instruction, `verbatim`: *"We should also bump the priority for improvement to token use"*. Given immediately after [How an agent workflow and its skills reduce their own token cost](nodes/52-token-cost-of-a-workflow.md) measured that **every worker reads this whole map cold and uncached, once per node — ~19,840 tokens, 81% of the entire shipped corpus, ~4M tokens across the dogfood target's 179 nodes.** Filed here under the rule [What the manager works on next, and how the human redirects it](nodes/16-human-steering.md) fixed for standing instructions, and it is a **redirection of that node's default rather than an exception to it**: the alternation between a design stream and a delivery stream stands, and within each stream a node that reduces the workflow's own token cost outranks one that does not. What it does **not** license: prioritising a saving over a correctness finding, and prioritising a saving whose size has not been measured — node 52 settled two candidates as non-issues *by measurement* (the always-loaded description surface at ~180 tokens across all six contracts, and tool-schema deferral being already on by default) and asked that neither absorb any budget. **A ranking by predicted saving is the *token maxing* failure in reverse and is not what this instruction buys.** The first node it ranks up is [What the token findings change in the workflow and its skills](nodes/53-what-token-findings-change.md), which is live, and whatever implementation nodes it reports.

### The landing policy in the form it had before worktrees

*The paragraph below stood in the map until [Run an implementation node's work in a
worktree](nodes/68-implementation-in-a-worktree.md) was carried into it by [Carry the worktree lifecycle
into the shipped files](nodes/74-carry-the-worktree-lifecycle.md). It is moved here verbatim; the map
carries the current statement.*

**Landing policy, now settled and binding on this map too**, since it carries execution: the manager makes one path-limited commit per implementation node, containing only that node's code, and only after the human has approved the diff — with the independent reviewer having passed it first. No branch is ever created or switched, nothing is ever pushed, and history is never rewritten. The graph's own files are *not* committed per node; they are committed periodically by the human, which is safe only because node files are append-only. Fixed by [Git and code-landing policy](nodes/11-git-and-code-landing.md).

### The operational notes in their full form

~~**Known prerequisite:** this directory is not yet a git repository, and the design already assumes git (`--ff-only` landing). `git init` must happen before any implementation node runs.~~ **Resolved:** `graph-agent` is a git repository and every graph file is tracked under commit `cf7e549 start`. Noted separately in [Git and code-landing policy](nodes/11-git-and-code-landing.md): the dogfood's code lands in **Lang's** repository, not this one, so that is the repo the landing policy has to work in.

**The dogfood target is [Lang](/home/mathieu/projects/Lang)**, decided in [Dogfood target](nodes/09-dogfood-target.md). Every design call from here has a concrete first user: ~~~130 open spec gaps, ~47 existing decisions~~ **179 distinct gap labels across 188 inventory rows in 13 families, 43 settled decisions and 48 consistency rows** — counted rather than estimated by [Graph file format](nodes/13-graph-file-format.md), and a third larger than the figure this map reasoned with for three sessions — a compiler that is only a lexer and parser and expects to be rebuilt, and an existing tracker doc at `Lang/docs/agents/issue-tracker.md` whose conventions this graph already borrows. When a choice is close, prefer the one that survives that repo.

**Claude tokens are scarce, and a worker will eventually not be a Claude subagent.** The human's constraint at work: *"I have a limited amount of claude credits but unlimited use of gemma 4 (and probably other soon)"*, so an expedition should be able to send cheap bounded work to a cheap model and keep Claude for the hard nodes. Two axes hide in that and only one is cheap — swapping a worker's **model**, and swapping the **harness** that runs it. Claude Code's spawn surface offers Claude models only and its API endpoint is per-process, so a heterogeneous fleet cannot be spawned from inside one manager session at all: it needs several processes and something between them, which is the firstmate shape already in the fog. **The sequencing is the human's: finish the Claude-subagent version as v1, then redraw for a heterogeneous one** — which under this map's own rule is a fresh effort rather than a resumption, and is what keeps v1 small. What v1 owes v2 is only insurance that costs nothing today: a worker contract that stands alone as a file rather than depending on skill invocation (a condition on [Write the worker contract skills](nodes/22-worker-contract-skills.md)), and a **measured** spend per node type from the dogfood so v2's routing is designed from data. Deliberately *not* added: a per-node model or capability field. The node's type already predicts what it needs, the format is the hard-to-reverse core, and the trigger for revisiting is a model choice that has to stay stable across attempts.

**The graph is four files**, fixed by [Graph file format](nodes/13-graph-file-format.md): this `map.md`, the append-only index [decisions.md](decisions.md), the append-only [flags.md](flags.md), and one file per node at ~~`issues/NN-<name>.md`~~ **`nodes/NN-<name>.md`** — renamed by [Naming](nodes/14-naming.md), because `issue` is a hosted-tracker word and a repo may hold real ones. A node's identity is its sequential `NN`, permanently; its name is free-form and carries a foreign label when the effort was adopted from somewhere else.

**The workflow is named `/expedition`, and its vocabulary is now fixed**, by [Naming](nodes/14-naming.md). The metaphor stops at the map: the product and one run of it are cartographic, and every actor and mechanism underneath is described plainly — **manager**, **worker**, **checker**, **gate**, **node**. ~~Forty terms~~ **Fifty terms** live in [`CONTEXT.md`](../../CONTEXT.md) with their rejected synonyms attached, which is the part that does the work — **corrected at [What keeps the shipped files consistent when a decision changes a term](nodes/29-shipped-file-consistency.md), where the count was measured rather than repeated: `CONTEXT.md` holds 50 term entries and 40 `_Avoid_` lines, so the *"forty"* was never a term count at all. It was the count of refusals, and it propagated as a term count out of [Naming](nodes/14-naming.md) into this file and into [decisions.md](decisions.md).** That file is also **moving**, into `.claude/skills/expedition/CONTEXT.md` with a `CONTEXT-MAP.md` at the root and the root path left resolving as a forward pointer — [Ship the glossary inside the skill directory and make it state its own completeness](nodes/56-ship-the-glossary-into-the-skill-set.md) — because a glossary the shipped files declare authoritative and which does not travel with them is the defect node 29 was opened for. `postpone`, `provenance`, `write lock`, `done`, `issue`, `ticket` and `task` are all now refused by name. Four words changed under previously-resolved nodes — `task` → `precondition`, `reviewer` → `checker`, `completion report` → `closing report`, and `done` split into a node **resolving** and an effort being **closed** — and the node directory moved from `issues/` to `nodes/`. Prose written before this point still says the old words; that is the never-delete rule, not drift, and the glossary is authoritative.

**This `## Notes` section also carries two optional blocks for whatever effort is being run**, fixed by [Subagent context contract](nodes/12-subagent-context-contract.md): the effort's **ground rules**, and a **source hierarchy** declared over paths and globs marking which sources are authoritative, which are evidence only, and which are known to contain false statements. Both are prose, both are optional, and absent a hierarchy every source a worker is pointed at is authoritative. They live here because `map.md` is already a pointer every worker receives. ~~*This* effort declares neither: its sources are all authoritative, and its ground rules are the standing preferences above.~~

**Superseded** by [What keeps the shipped files consistent when a decision changes a term](nodes/29-shipped-file-consistency.md), the human assenting to it in their own words. That sentence said two things that cannot both be acted on — *declares neither*, and *its ground rules are the standing preferences* — and the shipped checker contract offers two branches with no third, so the manager decided which before every check, on its own judgement, with no record of what it handed over. **This effort declares a ground-rules block and no source hierarchy**, its sources all being authoritative. The block is the five items below; the manager copies them as text into every checker spawn and adds nothing of its own, and where a check needs a constraint the block does not hold, that is a **raise** under [Whether a spawn may override a shipped worker contract](nodes/28-spawn-overriding-a-contract.md)'s rule rather than the manager's judgement.

Every one is drawn from a standing preference above, and every one passes the test [The checker's spawn carries the effort's ground rules](nodes/42-checker-spawn-carries-ground-rules.md) shipped for what may travel to a blind checker: **a standing constraint true of any node's work, rather than an account of what happened.** That test is what keeps most of this map out of the block — the manager-context findings, the token measurements and the landing policy's history are accounts, and a checker holding them would be reading the record it is kept blind from. **A sixth item was offered by the manager and declined by the human**, in their words *"the checker should know that the skills are not the map and that they can be modified, no ?"* — the product-file half of the never-delete rule, which the manager had been passing as its own gloss and which exists in no file. It was **redundant rather than load-bearing**: the never-delete preference above is scoped by its own words to files *in the graph*, and the checker contract's hard rule that *a property nobody stated is not a finding* means a checker handed this block cannot fault a product file for removing text. **The block is complete as of today and is appended to like any other part of this map**; the one change known to be coming is whatever [What the token findings change in the workflow and its skills](nodes/53-what-token-findings-change.md) settles about the density preference, which bears on item 5. Lang's are the reason the mechanism exists — `docs/superseded/` "contains statements known to be false", and a worker handed that repo walks into it unprompted.

### Nine deltas the shipped conventions document did not yet carry, and how each was discharged

~~**Two deltas**~~ ~~**Three deltas**~~ ~~**Four deltas**~~ ~~**Five deltas**~~ ~~**Six deltas**~~ ~~**Seven deltas**~~ ~~**Eight deltas**~~ ~~**Nine deltas the shipped [`graph-conventions.md`](../../.claude/skills/expedition/graph-conventions.md) does not yet carry**~~ **Nine deltas, now discharged** by [Carry the recorded deltas into the shipped skill files](nodes/26-carry-deltas-into-shipped-files.md) — every one of them is in that document, in its own voice. What follows stays as the record of what was carried and why, and remains the only place the reasoning behind each delta is written down; the document states the rules, not their history. All nine were decided after that document landed. From [Subagent context contract](nodes/12-subagent-context-contract.md): the `## Notes` blocks just described, and the reading of *"the manager is the graph's only writer"* — it means **scribe**, so the manager pastes a worker's handover under the right headings and never re-authors, shortens or re-renders it. From [Human review of landed code](nodes/20-human-code-review.md): **`## Review` has a required shape** — the checker's chronology one entry per run each naming `PASS` or `FAIL`, each correction round numbered with the human's words verbatim, and the gate's outcome named as one of approve / correct / reject, with a reject also recording what popped up and which route the node took. The document's current wording permits a gate whose outcome cannot be recovered from the record. From [When an AFK worker cannot proceed](nodes/23-worker-cannot-proceed.md): that chronology needs a **third entry kind, for a checker run that raised instead of judging**, since a raising checker issues no verdict at all. **Also from that node, and found while writing the worker contracts:** two of the document's sentences about `CONDITION-WRONG` are now stale — *"Its worker may raise a `CONDITION-WRONG` flag against it and may not rewrite it"* and *"`CONDITION-WRONG` — the worker judged its acceptance condition wrong."* A wrong acceptance condition trips trigger 1, so the worker **raises** and the **manager** files the flag once the human answers *carry on, ship it anyway*. **Sixth: every flag carries an id, `NN.k`** — the node's own number, then a sequence within that node, allocated in write order and never reused. The human's instruction at [Write the worker contract skills](nodes/22-worker-contract-skills.md)'s gate, because a flag with no id can only be pointed at by its position in a list. It goes in both places a flag lives: between the checkbox and the marker in [flags.md](flags.md), which carries the form itself, and in front of the marker on the node's `## Flags` entry. It also turns mechanical check 6 into an exact join rather than a match on prose. The twenty flags already in [flags.md](flags.md) predate it and are un-id'd; retro-fitting them is mechanical, that file being already in node order. **Seventh: a flag confirmed by the human is marked `settled` on the node too**, not only by its checkbox in `flags.md`. The human's instruction at the same gate, on the same ground as the ids: someone reading a node cannot tell which of its judgements are still live without opening a second file. This **overrules** [Graph file format](nodes/13-graph-file-format.md)'s *"the checkbox lives only in `flags.md`, so the two can never disagree"* — the state is now genuinely in two places, and the document must say which wins when they differ. It also fixes the word: `settle` is a flag's, `resolve` is a node's. And one thing that is not a delta but belongs with it: a flag's entry at the point it was raised must say **what produced it** — for a flag written from a worker's own unprompted judgement, what the worker actually did, in its words. A one-line summary is enough in the `## Flags` section and is not enough in the round that created it. **Eighth: the write and the resume go together.** The document's ordering requirement reads *"write the human's answer into `## Interview` at relay time — the moment the human gives it, **before** the manager attempts to resume the worker."* That was written assuming a resume blocks the manager. It does not — a resume is a background send — so the manager issues **both in one turn** and the worker thinks while the record lands. The human's instruction while watching a relay run, verbatim: *"maybe first restart the worker and then write the file, it might gain a bit of parralellism"*. What the rule protects is untouched: the answer is on disk before the worker can return, so a dead worker still leaves the human's words banked. Only the word *before* goes. This is the first correction to that document that came from **the human watching the manager work** rather than from a node deciding something — every other delta here was a decision arriving after the document shipped. Found at [Off-contract subagent output](nodes/17-off-contract-output.md). **Ninth: what goes onto `## Interview` and `## Review` when the human takes an option as offered** — the manager pastes their reply as they wrote it, however terse, marked `verbatim`, with the option or outcome it points at quoted beside it and attributed to whoever wrote it. Nothing is rendered, so nothing on either log is `paraphrase` unless the manager genuinely could not avoid rendering it; where a terse reply does not name which option it points at, the manager records the reply and asks. From [What is recorded when the human takes an option as offered](nodes/25-recording-an-option-taken.md), and it is the first delta that corrects **a practice the manager had already been following two different ways** rather than a sentence the document got wrong. ~~The next implementation node to touch that document carries all eight.~~ **That node now exists**: [Carry the recorded deltas into the shipped skill files](nodes/26-carry-deltas-into-shipped-files.md), on the frontier with no blockers, carrying all nine. It was minted rather than added as a tenth line here for a reason worth keeping: node 25 also invalidated **one sentence in two of the six worker contracts**, and this list covers only `graph-conventions.md`, so that fix had nowhere to be recorded at all. A delta list works until a delta lands on a file the list does not track. Recorded here rather than fixed there, because a second commit against a resolved node is what the landing policy forbids.

## Decisions so far

### Why the index was split out of the map

The reason is the never-delete rule itself: an index can only ever be appended to, so it grows without bound in node count, while this map's other sections grow only with fog items and notes. Two growth rates, two files. At Lang's 179 nodes an index in this style would be ~25k tokens per session load, which contradicts the map's job of being the whole map at low resolution.

## Not yet specified

Each item below is the fog item as it stood, with every update every node had appended to it. The map
carries the current statement of each item still in the fog. Two are here only: **failure handling**,
whose two halves were both answered, and **whether a research node is warranted**, spent as a question
— whose live residue the map carries as an item on standards that live outside the repository.

### The implementation nodes that write the actual skill files

- **The implementation nodes that write the actual skill files** — the manager's skill, the issue-subagent prompt templates, the invocation surface. Cannot be sized until the taxonomy, relay and file format land. This is where most of the remaining work lives. The taxonomy has now landed, so the remaining blockers to sizing are the relay and the file format — and it is now known that each of these nodes will carry a spawner-written acceptance condition and an independent review before it can resolve. [Dogfood target](nodes/09-dogfood-target.md) adds a requirement the skill files did not previously have: they must be able to **adopt an effort already in progress**, not only chart a new one, because the first real run is a migration. Two more arrive with [Done-ness and termination](nodes/10-done-ness.md): they must express the quality bar as **properties whose commands are discovered per repo** rather than a hardcoded toolchain, and they must be copyable to a machine holding none of this repo's context. **Partially graduated** by [Graph file format](nodes/13-graph-file-format.md): the stated precondition — taxonomy, relay and file format all landed — is now met, and the piece the format fully determines has become [Write the graph conventions document](nodes/21-conventions-document.md), the map's first implementation node. The rest still waits, and now on a shorter list: [Naming](nodes/14-naming.md), because the skill files are written *in* the vocabulary, and [Subagent context contract](nodes/12-subagent-context-contract.md), because the prompt templates are its output. **[Git and code-landing policy](nodes/11-git-and-code-landing.md) removed the other blocker from all of them** — every implementation node now knows how its output lands and who approves it — leaving [Write the graph conventions document](nodes/21-conventions-document.md) waiting on Naming alone. **[Naming](nodes/14-naming.md) has now landed too, so that node is on the frontier** — the map's first takeable implementation node, and the first thing the gate will ever be run on. The rest of this fog item is down to a single blocker, [Subagent context contract](nodes/12-subagent-context-contract.md), and one further requirement: the skill files are written *in* the glossary's vocabulary, so `CONTEXT.md` is an input to every one of them rather than a by-product. **The first of these files has now landed** — [Write the graph conventions document](nodes/21-conventions-document.md) resolved, and the workflow has product files and a commit for the first time. Three pieces are left in this item, all still on [Subagent context contract](nodes/12-subagent-context-contract.md): the **manager's own skill**, the **worker prompt templates**, and the **adoption mode**. What that node's resolution now has to serve is concrete rather than hypothetical: the checker payload was improvised to run this node and is recorded on it, and the landing lifecycle it has to describe is known to be forced — checker, gate, one commit, resolve — because committing earlier would need a second commit for one node, which the landing policy forbids. **[Subagent context contract](nodes/12-subagent-context-contract.md) has now resolved and one of the three pieces has graduated out of this fog**: the worker prompt templates are [Write the worker contract skills](nodes/22-worker-contract-skills.md) — six contracts, one per node type plus the checker, with an acceptance condition already written and one blocker left, [Human review of landed code](nodes/20-human-code-review.md), for the single row carrying the gate payload. **Two pieces remain here.** The **manager's own skill** is the one that needs nearly everything still open — [Cascade pass mechanics](nodes/15-cascade-pass-mechanics.md) for the propagation pass it runs, [Human-initiated steering](nodes/16-human-steering.md) for how it takes direction, [Off-contract subagent output](nodes/17-off-contract-output.md) for what it does with a malformed handover, and ~~[Human review of landed code](nodes/20-human-code-review.md) for the gate it raises~~ — so it is the last file written rather than the first. The **adoption mode** is [Adopting an in-flight effort](nodes/18-adopting-in-flight-effort.md)'s to specify before anything writes it. **[Human review of landed code](nodes/20-human-code-review.md) has now resolved**, so the manager's skill is down to three blockers ~~and [Write the worker contract skills](nodes/22-worker-contract-skills.md) is on the frontier — the map's second implementation node, and the first written after the gate it passes through was specified rather than improvised~~. What that node inherits beyond its own condition: the gate payload's contents for the implementation row, the correction-round reporting duty that decides whether a re-check runs, and one renamed token in the checker's contract. **It did not stay on the frontier for long.** The human's steering in the same session created [When an AFK worker cannot proceed](nodes/23-worker-cannot-proceed.md) — an AFK worker's channel for *the premise is broken* — and two of the six contracts cannot be written before it resolves. The manager's skill gains it as a fourth blocker too, since the manager is what receives such a raise. So the contracts are one grilling node away again rather than takeable, and the lesson is the map's own premise arriving on schedule: **the implementation node was re-blocked by a decision nobody had asked for, before a line of it was written** — which is cheaper than the second commit against a resolved node it would have cost an hour later. **Unblocked again** by [When an AFK worker cannot proceed](nodes/23-worker-cannot-proceed.md): the six contracts are takeable, and the manager's skill is down to three blockers. **And now landed**, as commit `e72f444` — [Write the worker contract skills](nodes/22-worker-contract-skills.md) resolved, so two of this item's three pieces are done and what is left here is the **manager's own skill** and the **adoption mode**. The manager's skill leaves that node holding five requirements it did not have, every one of them learned by *running* the contracts rather than by reasoning about them. **It settles a node's flags as it closes that node**, putting them to the human then rather than leaving them for the closing report — the human's instruction, on the ground that while the node is open the work is still there, so acting on a flag is cheap; eleven of eleven were settled that way, against [Friction from running this map by hand](nodes/24-self-hosted-friction.md)'s measured fifteen-outstanding-zero-settled, and it thins [Done-ness and termination](nodes/10-done-ness.md)'s closing report to the flags nobody could settle in the moment. **It gathers a node's flags as a step of raising one**, never as a tidy-up: a flag raised after that node's `## Flags` section had been assembled lived only inside its own paragraph for two rounds, which is the same complaint the ids were introduced to answer. **It hands a re-checking checker the time of the previous outcome** alongside the statement of what changed, since a checker holds no timestamp of its own and must re-read any file whose modification time it cannot place — three consecutive checkers re-read one file for that reason. **It names the contract's path in every spawn and says the file on disk wins**, because the harness serves the skill body it loaded and a contract edited mid-session does not reach a worker spawned afterwards. **It hands the checker the bar's non-command half as this map records it**, rather than as the phrase the improvised spawns used. And one thing it may not assume: ~~that a stopped worker can be resumed — the harness refuses, which makes a stop more destructive than a death.~~ **Falsified by running it, at [Restructure `map.md` to what every worker needs](nodes/59-restructure-the-map.md): a checker stopped by the harness mid-re-check was resumed by message and carried on from where it stopped. So a stop is recoverable like a death, and it is the second harness prediction in this effort falsified by use rather than by reasoning — the first being at [What the checker contract owes to having been run](nodes/31-checker-contract-owes.md).** **[Off-contract subagent output](nodes/17-off-contract-output.md) has now resolved, taking the manager's skill down to two blockers** — [Cascade pass mechanics](nodes/15-cascade-pass-mechanics.md) and [Human-initiated steering](nodes/16-human-steering.md) — and it is the first blocker of the three to be removed by a **worker** rather than by the manager grilling directly. What it hands the manager's skill is a rule about the manager's own judgement rather than about a worker's: **file what you can paste, flag what departed, and re-prompt only what you cannot file at all** — with one check the manager runs itself before filing, holding a handover's `ANSWER` against the `## Interview` it wrote in the same turn it resumed the worker. That check ran once, on the handover that created it, and what it caught was **the manager's own note having become part of the node's permanent text**, which is a sharper warning for whoever writes that skill than any of the five requirements above. **[Whether a spawn may override a shipped worker contract](nodes/28-spawn-overriding-a-contract.md) adds a sixth requirement and one whole mechanism, without being a blocker of either kind.** The mechanism is **the manager's own blocking raise**, which nothing in the design had described — everything the manager says to the human today is a relay, a gate, or a flag settlement, and the glossary's `raise` already covers this one since [Carry the recorded deltas into the shipped skill files](nodes/26-carry-deltas-into-shipped-files.md) generalised it to *an agent putting something to the human*. The manager may not depart from a shipped contract on its own authority; where a clause blocks the node in front of it, it raises, and the human's answer yields **two outputs, always both** — a licence for that one attempt, flagged on the node, and a node for the permanent fix. The evidence for *both* is that [Whether flags.md survives the settle-at-close practice](nodes/27-does-flags-file-survive.md) took the departure and minted no node, and a session later the clause stood unchanged in five contracts while node 28 still carried the narrowing as an open question — the repair was lost along with the record, and is now [Narrow the flags.md clause in the worker contracts](nodes/32-narrow-flags-file-clause.md). Three more things for that skill: **the floor** — nothing the manager sends a worker may widen what that worker *writes*, since the write rules are what keep the manager the graph's only writer; **a carried direction of the human's is marked as their words rather than as the manager's**, and is neither a per-type addition nor a manager note, so [Subagent context contract](nodes/12-subagent-context-contract.md)'s spawn template gains a fourth element; and **the rule is written over anything the manager sends a worker, spawn or resume**, three of the four departures having arrived on a resume. One diagnostic worth carrying into the skill: at two firings in thirty-one nodes the raise is cheap, and **a rate materially above that reports that the contracts are wrong rather than anything about the node in front of the manager.** **[An acceptance condition is self-contained text](nodes/33-condition-is-self-contained.md) adds a seventh requirement, and it is the first that constrains what the manager may *withhold* rather than what it may send:** a condition that points at material the checker was not given is **handed over unrepaired**, because supplying what it omits makes the manager the author of the standard the work is judged against. The manager may raise such a condition before spending a check on it, or let the checker raise it — and the manager tested that on itself at the same node, predicting its own condition 6 would be uncheckable and handing it over anyway. What came back is the finding that matters here: **the blind checker returned `PASS` and named one clause as outside what it could establish**, neither passing nor failing it, which is the third return shape improvised for the fourth time and is now [What the checker contract owes to having been run](nodes/31-checker-contract-owes.md)'s to fix. The manager verified the reserved clause itself, against the handover it holds and the checker does not — so *the manager is the residual checker of anything a condition addresses to a party that cannot see it*, which is a duty the skill has to state rather than a gap. One more thing that node measured rather than argued: **nine of thirty-one acceptance conditions written across this effort fail the rule**, and the failures cluster not by author but by clause — every condition written by a spawning node's worker passes, and what fails is a clause summarising something the writer had open in front of them. Two boilerplate sentences account for seven of the nine, one of which cannot be repaired by copying at all and is now [The clause that says no resolved node changes cannot be self-contained](nodes/36-resolved-node-clause-cannot-be-self-contained.md). **That node adds an eighth requirement, and it is the first to make one of the other seven avoidable rather than permanent.** Its condition was written with every demand landing in a file, and its checker **reserved nothing** — the first check in this effort where the manager held no residual at all, against node 33's three reserved clauses on one condition. So the residual-checker duty is a **consequence of a badly written condition rather than a standing part of the manager's job**: the skill says write the condition so there is nothing to hold, and hold what is left only where something was. It is also **the first manager-written acceptance condition in this effort to be established in full** — node 26's was amended twice and node 33's came back with three clauses unestablishable — which is evidence [A worker's handover carries no acceptance condition for the node it mints](nodes/35-handover-mints-no-condition.md) has to weigh: what fixed it was the writer applying node 33's rule against their own text, not a different party writing it, so moving the pen may not be the repair that node is looking for. Two smaller things for the same skill. **The gate payload asks the human to name the outcome** rather than leaving it to be read: node 33's gate arrived as *"you can continue"*, naming none of approve / correct / reject and costing a recorded reading on the node, and one clause asking for the word returned *"approve"* here. And **the manager states which paths are the work, which is not a repair of the condition** — the tree held a `.scratch/` modification that was the manager's own bookkeeping, and saying so is the checker contract's third given, *the work — the paths that changed*. Worth stating because the two acts look identical from outside and node 33's rule forbids only one of them. **[What the checker contract owes to having been run](nodes/31-checker-contract-owes.md) falsifies one of the five requirements above and turns node 36's eighth into a practice.** The falsified one is *"it names the contract's path in every spawn and says the file on disk wins, because the harness serves the skill body it loaded and a contract edited mid-session does not reach a worker spawned afterwards."* That node's work rewrote `expedition-checker/SKILL.md`, and the checker spawned afterwards reported *"my instructions match the post-change text"* — so a contract edited mid-session **does** reach a worker spawned afterwards, at least where the spawn names it and the worker invokes it by name in a fresh subagent. The requirement's remedy survives and its reason does not: naming the path and saying the file on disk wins is still right, but the hazard it guards against is the opposite of the one recorded. What it actually guards against is now known: **a node that edits a contract silently changes the contract of every worker spawned after it**, including its own checker, which is how flag `31.2` came to exist. Whoever writes that skill states the hazard in that direction, and the previous observation stays on the record as something that was true of one harness path and not of this one. The practice is the **audit at claim time**: node 31's condition was manager-written and carried a standing warning to read it against the files, and the manager did that before spawning — finding six defects including a flat self-contradiction that would have cost a raise rather than a check. Its checker then reserved nothing, which is **two consecutive checks with no residual** after node 36's first. Two is a practice where one was an instance, and the practice is cheap: a manager reading its own condition against node 33's rule and node 36's before it hands the node to anyone. **[A worker's handover carries no acceptance condition for the node it mints](nodes/35-handover-mints-no-condition.md) bounds that practice and adds a ninth requirement.** The bound: its condition was manager-written and audited at claim time, the audit found and repaired two defects, and **the blind checker then found a third the audit had missed** — a clause the condition dictated that was right for three of the five contracts and wrong for two, visible only by holding the condition against a file the condition does not name. So the practice is *audit plus a check that can still catch what the audit missed*, not an audit that makes the check a formality, and the skill states it that way. The ninth requirement is a duty the manager was not discharging at all, found by that node's checker on its re-check: **a statement of what changed must cover commits as well as the working tree.** Two files it holds standards against — `graph-conventions.md` and its own contract — had moved between its baseline and its resume, by the commits this effort landed at nodes 31 and 36, and nothing in the resume said so; it discovered them itself and settled that no standard had moved under the check before reading a line of the work. Its words: *"a statement of what changed which names only the working tree can leave a checker to discover a moved standard on its own."* This effort commits after every implementation node, so the case is not rare but structural — the manager names what landed since the checker's baseline, not only what is dirty in the tree. One thing that node also measured about the same checker: it corrected its **own** previous outcome, having labelled its baseline from the session-start git snapshot, which was already stale when it began. The diff it took was right and only the printed id was wrong — but a blind checker is structurally exposed to that, the snapshot being a fact that expires with nothing telling it when. **[Workflow self-improvement during use](nodes/19-workflow-self-improvement.md) widens that ninth requirement and hands the skill a whole mechanism it had no case for.** The widening: the statement of what changed is owed not only on commits but on **which existing files are left in the older form**, because an implementation node that changes a file other nodes of the same effort are written against leaves them behind, and the manager carries that statement into every later spawn and re-check. The limit is recorded rather than repaired: that duty does **not** cover a node writing the new form wrong in its own file, which is what actually happened — node 26 holds exactly nine flags and is the node that shipped the flag-entry form, so the nine nonconforming entries were its own, written after its own change. What covers that is conformance checking, and that is [What keeps the shipped files consistent when a decision changes a term](nodes/29-shipped-file-consistency.md)'s, which is now **load-bearing for a permission the human has already granted** while being open with nobody on it. The mechanism is the manager's route past **blocking friction with its own contracts**: it may not invent a workaround, so it **raises**, and the human's instruction travels as their own words in that one spawn — becoming a line in the effort's ground rules only where the same instruction is needed more than once. On an effort whose repository does not own the skill files, node 28's *two outputs, always both* cannot hold, the second being impossible there, so the `FRICTION` flag takes the node's place: raise, licence, flag. One thing the skill must not do to the blind checker, endorsed by the human in their words — *"fair point from the manager"* — is assume the ground rules reach it: the checker reads no map, so a standing constraint reaches it only by being **copied into its spawn as text**, the way the bar's non-command half already travels, and never as an account of what happened, which is [The checker's spawn carries the effort's ground rules](nodes/42-checker-spawn-carries-ground-rules.md).

### Whether the Claude Code subagent runtime proves too simple

- **Whether the Claude Code subagent runtime proves too simple**, and the upgrade path to a firstmate shape (real sessions, worktrees, file mailboxes) if so. Only judgeable after a dogfood run. The taxonomy raised the load: every implementation node now spends a second AFK agent on independent review, and ~~the HITL budget is disjoint from the code slot~~ **— corrected by [Git and code-landing policy](nodes/11-git-and-code-landing.md): the two budgets are not disjoint. An implementation node ends in a human gate, so the code slot's occupant is a third claimant on the human's queue, and it is the only one that holds a lock while it waits** — so more agents run concurrently than first assumed. The dogfood target now supplies the number to judge against: **~130 nodes**, where the design has so far only been reasoned about at 17. It will also be judged in **more than one environment**, per [Done-ness and termination](nodes/10-done-ness.md): "too simple" now has to be false on an unknown stack as well as at ~130 nodes. **A third way to be too simple, and the first that is economic rather than technical**, from the human's credit constraint in the Notes above: the question stops being *can the runtime hold 179 nodes* and becomes *can it run a node on a model of the manager's choosing*. It cannot today — Claude models only, endpoint per-process — so this item's trigger may fire before either scale or portability pulls it, and its answer is already named: several processes with a mailbox, which is firstmate. Two places the design spends double and would spend cheapest: every implementation node runs a **checker** as a second agent, and the **cascade** and **sweep** are whole-graph scans. All three check bounded work against stated criteria — the largest share of the bill and the safest work to give a weaker model, a blind checker most of all. Grilling and implementation are where the expensive model earns its keep. So the dogfood carries back **spend per node type**, alongside the friction record [Dogfood target](nodes/09-dogfood-target.md) already requires. **This item now has evidence, and it indicts something none of the three predicted ways expected** — [Friction from running this map by hand](nodes/24-self-hosted-friction.md), which found that across every session that built these 24 nodes the thing that broke was neither node count, nor an unknown stack, nor a model choice: it was **the manager's own context**, every time, including mid-session. Two hard data alongside it: a checker died after one of four phases on a single node's check, and the relay has been run exactly once, in a prototype, because nodes 09–20 were all grilled by the manager directly. So the runtime's weakest point is the long-lived thread rather than the fleet under it, and a bigger graph tool or a cheaper worker fixes neither. That also reprices this map's governing principle: *the human is the scarce resource* is right about what to optimise and wrong about what fails first, so any design that spends manager context freely — rendering diffs, re-authoring handovers, re-deriving checks by hand — was priced against the wrong constraint. **The human raised the cost directly while the map's second implementation node stood at its gate** — *"using opus for everything is running through my tokens quite fast"* — and added a question this item never asked: **what model the manager itself needs**, since its job in the finished design is *"relatively straightforward"*. Four things follow. **One premise here is too pessimistic:** this item records that a mixed fleet *"cannot be spawned from inside one manager session at all"*, which is true of mixed **harnesses** and false of mixed **Claude models** — the spawn surface takes a model per worker today, so the manager can already put a cheap model on cheap work, and only a non-Claude worker needs the several-processes redraw. The cheapest half of the saving is available in v1 with no redraw at all. **The first measured numbers exist:** [Write the worker contract skills](nodes/22-worker-contract-skills.md) spent 100k, 101k and 82k worker tokens across three checker attempts on one 820-line prose deliverable — ~283k on checking alone, on a node whose implementation the manager did itself. That is the first row of the spend-per-kind table this item and [Dogfood target](nodes/09-dogfood-target.md) both ask the dogfood to carry back, and it is the row this item predicted would be largest. **The manager's own model has a sharp test and the map already contains it:** the standing preference is *most of the context lives in the workers, not in the manager*, and [Subagent context contract](nodes/12-subagent-context-contract.md) made the manager a **scribe** that pastes and never re-authors — and a scribe does not need the expensive model. So **if the scribe rule holds, a cheap manager is enough; if the manager needs the expensive model, the scribe rule is not holding**, which turns the model choice into a measurement of the design rather than a decision beside it. Still deliberately absent is a per-node model field, for the reason already given — the kind predicts what a node needs; what is missing is where the kind-to-model mapping lives, and the candidates are the worker contracts and the manager's own skill. Sharp enough to be a node, and parked at the human's word — *"also for later"* — rather than promoted.

### Resume and recovery

- **Resume and recovery** — what happens when the manager's context compacts or its session dies mid-graph. Firstmate's answer is that all state lives on disk and the next session reconciles; whether prose rules are enough to make that work here is unknown. [Relay protocol](nodes/08-relay-protocol.md) supplied the first real mechanism: routing keys and the interview log are durable on disk per attempt, so a fresh manager can re-adopt interviews that are still live. What is still unknown is everything the manager holds that is *not* an interview — chiefly the node-name-to-routing-key mapping as a whole, and whatever it knew about why it chose the nodes it chose. [Dogfood target](nodes/09-dogfood-target.md) turns up a hand-built precedent worth reading before deciding this: Lang's `handoff.md` is a human's manual answer to exactly this problem — 193 lines holding where the work stands, the live question, and a recommended order for the next session.

### Failure handling, and the two nodes it graduated into

- ~~**Failure handling** — a subagent that dies mid-question, returns garbage, or exceeds its context before answering.~~ **Graduated** by [Relay protocol](nodes/08-relay-protocol.md), which split it in two and answered one half. The **death and context-exhaustion** half is answered there: lazy detection by failed resume, replay from the node's at-relay-time log, two-respawn cap, then escalation as a node-too-coarse decision. The **garbage** half is now [Off-contract subagent output](nodes/17-off-contract-output.md), because a live-but-off-contract agent shares no remedy with a dead one. Kept here, struck through, per the standing rule that nothing is deleted. **Both halves are now answered**, the second by that node — and it retired the word this item was written in: there is no *garbage* category. A live worker's return is on-contract whenever the manager can file it, however far it departs from what its contract wrote down, and the departure becomes a flag rather than a rejection. Only a return the manager genuinely cannot file — a required part absent, or a shape with no heading — is re-prompted, once. The two halves turn out to share one boundary after all: **a worker that cannot be reached is a death**, so a stopped worker falls to [Relay protocol](nodes/08-relay-protocol.md)'s route and not to this one.

### How the human sees graph progress

- **How the human sees graph progress** — whether anything renders the graph, or reading the files is enough. Sharpened by the revision decision: supersession chains are the record of where the graph keeps rubbing, and a cascade that supersedes eleven nodes without saying so is a surprise waiting for the next human read. Both only pay off if something surfaces them. Sharpened again by [Relay protocol](nodes/08-relay-protocol.md): a **parked** node is back to `open` while holding answers the human already paid for, so a graph read must make half-interviewed nodes distinguishable from never-started ones — otherwise a deferral becomes invisible debt. This is now the presentation counterpart to [Human-initiated steering](nodes/16-human-steering.md), which is the control side of the same problem; steering is useless without a view to steer from. Sharpened hard by [Dogfood target](nodes/09-dogfood-target.md): at Lang's ~130 nodes with ~40 unblocked at once, "reading the files is enough" stops being plausible — the human cannot hold that frontier in their head, and the map's own index grows past a hundred lines, which contradicts its job of being the whole map at low resolution loaded once per session. **Split rather than sharpened** by [Done-ness and termination](nodes/10-done-ness.md): the *code* view left the fog as its own node, [Human review of landed code](nodes/20-human-code-review.md), because rejecting landed code changes the graph and so carries a decision. What stays here is the graph-state view, which gains one artifact to build on — the completion report — and one more thing it must surface: **outstanding flags**, which are invisible today and accumulate for the whole life of an effort. **Made much cheaper** by [Graph file format](nodes/13-graph-file-format.md): the two things a view most needs to show now exist as files a human can read directly — [decisions.md](decisions.md) and [flags.md](flags.md) — and `Labels:` gives the view an axis to *scope* by, which is what makes a 179-node graph presentable at all. A parked node also became mechanically detectable for free: `Status: open` with a non-empty `## Interview`. One more state to surface arrives with [Git and code-landing policy](nodes/11-git-and-code-landing.md): **an implementation node awaiting the human's approval holds the exclusive code slot while it waits**, so a view that does not show it makes the one blocking item in the whole system invisible.

### How the workflow reaches a repository that is not this one

- **How the workflow reaches a repository that is not this one.** Recorded by [Done-ness and termination](nodes/10-done-ness.md): the human will run it on work projects, on another machine. Whether that needs anything beyond copying the skill files — an install step, a per-repo bar file, a way to carry the map conventions into a repo with its own tracker doc — is not sharp enough to state as a question yet. Adjacent to [Adopting an in-flight effort](nodes/18-adopting-in-flight-effort.md), which is about adopting an effort rather than reaching a machine. **[Subagent context contract](nodes/12-subagent-context-contract.md) found the first concrete thing that does not travel.** The contracts name method skills — `/grilling`, `/domain-modeling`, `/prototype`, `/research`, `/naming`, `/coding-principles` — and on this machine four are a plugin and two are the human's own; **not one of them is per-repo**, so copying the expedition skill into a work project carries none of them along, and a spawn there would name skills that do not exist. Patched for now by naming them *invoke if present*, which is a flag rather than an answer. The sharper question this item now holds is whether expedition must **vendor its own grilling discipline** rather than borrow its ancestor's — which is also the last structural dependency on the plugin this workflow descends from. **One thing that does travel is now decided**, by [Workflow self-improvement during use](nodes/19-workflow-self-improvement.md): friction with the workflow noticed on an effort in another repository is raised there as a **`FRICTION` flag** and is fixed only here, because *"the effort in another project will never fix the skill"* — the human's words. Nothing crosses the boundary but the human: no file channel exists by design, multi-repo dispatch being out of scope below and [Git and code-landing policy](nodes/11-git-and-code-landing.md) coordinating nothing cross-repo. So a foreign effort's whole duty is the flag plus, where the friction blocks, the human's carried instruction — and **nothing there may be made to wait on the skill being fixed**, no acceptance condition and no closing condition, since such an effort could never close. This repo holds no standing inbox for what comes back: a batch of carried friction is a bounded destination and a fresh effort is charted for it, which is what settling such a flag *does* when nothing is live here. **This item's *"first concrete thing that does not travel"* turns out to have a second, worse face, found by [Review every shipped file against `/writing-great-skills`](nodes/47-review-shipped-skills.md) and demonstrated on that worker itself.** The patch recorded above — naming the method skills *invoke if present* — assumed the failure was **absence**: a spawn naming a skill that is not there, with the contract's own fallback covering it. The failure that actually occurred is **presence**: on this machine each of the four named skills *is* there and **instructs the worker to do something its own contract forbids**. `/research` says write findings to a file, against *"You write no file"*; `/grilling` addresses the human in the first person, against *"You have no human-facing tool"*; `/domain-modeling` edits `CONTEXT.md`, the glossary this effort declares authoritative; `/prototype` places work in the product tree and commits it. Only `expedition-checker/SKILL.md` resolves such a conflict, with *"Where a skill's procedure and your blindness conflict, blindness wins."* So *invoke if present* is not merely a flag rather than an answer — it is a flag on the **wrong hazard**. That is [Reconcile a method skill's instructions with the contract's hard rules](nodes/48-method-skill-conflicts-hard-rules.md). **A third face is the addressing itself**: four of the six are registered `mattpocock-skills:<name>` and two are bare, so a worker told to invoke `/research` must translate the name, and where it does not the fallback governs **silently** — nobody learns a skill it should have used existed. That is [What a contract may name as a method skill](nodes/51-what-a-contract-may-name.md). **And the dependency proved live rather than theoretical within one session:** `/writing-great-skills` was renamed to `/writing-for-agents` upstream, rewritten rather than renamed, with its disclosed reference file replaced and `disable-model-invocation` dropped — so a bare name pointing into that plugin went stale on a rev bump, and the only thing that told this workflow was the human noticing. The sharper question this item holds, whether expedition must **vendor its own discipline rather than borrow its ancestor's**, now has evidence on both sides rather than only a suspicion.

### Extraction of a graph tool

- **Extraction of a graph tool**, per the revisit trigger in the graph-state decision. The revision decision moved this closer: there is now a status that does not satisfy an edge, two edge directions to keep consistent, and repointing work for the cascade — all currently prose. [Dogfood target](nodes/09-dogfood-target.md) moves it closer again, twice: prose bookkeeping over ~130 nodes is a different proposition from 17, and the migration itself is a **bulk mechanical transformation** — invert ~130 prose blocks-lists into `Blocked by:` edges, import ~47 decisions — which is precisely the shape of work a script does well and an agent does expensively and inconsistently. A third push from [Done-ness and termination](nodes/10-done-ness.md): the **sweep** must collect every outstanding flag across the whole graph before an effort can close, which is a scan over ~130 files that a script does exactly and an agent does slowly and differently each time. **Now specified in everything but the trigger** by [Graph file format](nodes/13-graph-file-format.md), which lists the **eight mechanical invariants** a `check` would enforce — every one decidable without judgement, which is exactly the boundary between a script's work and the cascade's. That node also removed one of the three pushes: flags live in [flags.md](flags.md) with their state, so collecting them is a single-file read rather than a 179-file scan, and no longer an argument for extraction. **[Write the graph conventions document](nodes/21-conventions-document.md) supplied the first real evidence**, from writing and then running the checks by hand: five naive scans in one session produced false positives, every one of them from a rule the format had already stated — a heading matched inside a fenced template, fields read below the header block, `flags.md`'s own format example counted as an outstanding flag. Two of the eight invariants count **lines in an index file**, and only one carries the rule that makes it mechanizable: the document fixes *"the flag's node is the first link on the line"* for `flags.md`, and check 5 needs the same for `decisions.md`, where an entry's text may cite other nodes and [Dogfood target](nodes/09-dogfood-target.md)'s entry already cites [Graph file format](nodes/13-graph-file-format.md). **Confirmed by running it** during [Subagent context contract](nodes/12-subagent-context-contract.md): under a naive all-links scan that entry gives [Graph file format](nodes/13-graph-file-format.md) two index lines and check 5 fails on a graph that is correct. Predicted last session, measured this one. Re-deriving these greps per session is the cost being paid, and it is now measured rather than predicted. **Counted, finally**, by [Friction from running this map by hand](nodes/24-self-hosted-friction.md): one hand re-derivation per session for the life of the effort, a throwaway checker living in `$TMPDIR` that has been rewritten more than once because it dies with the temp directory, and five false positives from naive scans in a single session. Nothing on this item is speculative any more, and the only thing still missing is the trigger. **One more false-negative class, from [Carry the recorded deltas into the shipped skill files](nodes/26-carry-deltas-into-shipped-files.md), and it is the first found by an agent that was not looking for it:** a **line-based grep misses any phrase that wraps**, and every file in this effort wraps at ~100 columns. The blind checker hit it twice in one run — confirming a shared wording across three files, and establishing what a **reflow** had changed — and both times it unwrapped the text before searching rather than trusting the line. Two of the eight invariants count lines in an index file and several of the rest match on prose, so a `check` written naively over lines is wrong for the same reason those five earlier false positives were. Add it to what the extracted tool has to get right, and note that it also invalidates the checker contract's *"comparing modification times… is enough"* — carried to [What the checker contract owes to having been run](nodes/31-checker-contract-owes.md). **And running the checks at that node's resolution cost five more false results in one sitting, bringing the measured total to eleven:** field lines inside [Graph file format](nodes/13-graph-file-format.md)'s own fenced templates read as real `Status:` and `Superseded by:` fields, inventing a supersession to a node numbered 88; a naive unwrap that joined list items into one entry, so `decisions.md` counted zero lines; `### Attempt`, which names a **dead checker run** in node 22's `## Review`, counted as an `## Interview` attempt and failed check 8 on a correct graph; placeholder paths in fenced examples and inline code counted as broken links; and — the one that matters — **flag prose citing another node's id read as a flag entry**, because node 26's own `## Flags` cites `17.4`, `25.4`, `27.3` and `26.4` mid-sentence while explaining itself. That last is the exact analogue of the `decisions.md` citation false positive recorded above, arriving in the file the sixth delta had just made joinable, and it exposes a gap in the **shipped** wording: check 6 says *"every `## Flags` entry"* without saying that an entry is **line-anchored**, which is the same omission [Graph file format](nodes/13-graph-file-format.md) closed for `flags.md` by fixing *"the flag's node is the first link on the line"*. Eleven false results across seven sessions, every one of them from a rule the format either states elsewhere or fails to state at all. **One of this item's three counted frictions turns out to be an artifact of where the script was put, not of the script being throwaway.** At [What the checker contract owes to having been run](nodes/31-checker-contract-owes.md) the checker survived the session boundary and ran unmodified, for the first time — because it had been written to the session's own job directory rather than to `$TMPDIR`. So *"rewritten more than once because it dies with the temp directory"* is a storage-location cost with a free remedy, and it should stop being counted as evidence for extraction. The other two frictions are untouched and are the real ones: the eleven false results, and the hand re-derivation of the greps themselves. **A twelfth at [Whether a spawn may override a shipped worker contract](nodes/28-spawn-overriding-a-contract.md), and beside it the first finding of a different kind.** The false result is the same family again: check 6 read a flag as `settled` by matching the bare word anywhere in its prose, and flag `28.3` reads *"settled from the file rather than asked"* — so a flag explaining itself marked itself settled. The rule it missed is stated: `graph-conventions.md` fixes the marker as `**· settled**`, and prose never carries `**·`. But tightening the script to the documented **position** — id, marker, then type marker — failed on nine correct flags, and that is the finding: **node 26 writes the marker after the type marker and node 27 before it, so 22 entries follow the shipped form and 9 do not.** Nothing among the eight checks verifies conformance to a form the conventions document fixes, which is why the divergence survived a session and was found only by a scanner that had to be loosened to tolerate it. The nine were normalised at this node; the general question — a shipped form that nothing checks — belongs to [What keeps the shipped files consistent when a decision changes a term](nodes/29-shipped-file-consistency.md), and it is the first instance of that node's problem arising **inside** the graph files rather than in the product.

### When to flip landing to asynchronous

- **When to flip landing to asynchronous**, and what changes in the human's day when it happens. [Git and code-landing policy](nodes/11-git-and-code-landing.md) settled v1 as approve-then-commit and identified the seam as a single step — the manager committing before the gate rather than after — with the trigger being the code slot idling on approvals. What is not sharp yet is what asynchronous review actually looks like from the human's side: reviewing commits after the fact means rejection arrives as a replacement node landing a forward fix, which is a different experience from correcting a subagent live. Adjacent to [Human review of landed code](nodes/20-human-code-review.md), which specifies the synchronous gate, and to [Human-initiated steering](nodes/16-human-steering.md), since a human reviewing asynchronously is choosing what to look at. **Now it has something to be a delta on, and one cost the seam-is-a-single-step framing did not price.** That node fixed a gate with three outcomes, and the third does not survive the flip: `reject` means *this code should not be kept*, discharged today by cleaning the working tree. After a commit there is nothing to clean — reject becomes a forward revert, so the cheapest of the three outcomes becomes the most expensive one and the only one that costs a permanent mark in history. The other two are genuinely unchanged. So the flip is one step *plus* a repriced outcome, and the trigger to watch is still the code slot idling on approvals. **The trigger now has two sources rather than one**, per [When an AFK worker cannot proceed](nodes/23-worker-cannot-proceed.md): a blocked worker also idles the slot on human attention, unscheduled, so the gate is no longer the only claimant that holds it.

### What happens when never-delete makes this map too expensive to load

- **What happens when never-delete makes this map too expensive to load.** Opened by [Friction from running this map by hand](nodes/24-self-hosted-friction.md), and it **falsifies the reasoning [Graph file format](nodes/13-graph-file-format.md) split `decisions.md` out on**. That node argued two growth rates: an index grows without bound in node count, while *"this map's other sections grow only with fog items and notes"* — so two files. The other two sections grew anyway, and not in item count but in **words per item**: `## Notes` is fifteen paragraphs, and single fog items now carry eight append-marked updates from eight different nodes inside one paragraph, correct as a record and no longer readable as a view. The same tension shows up one level down, on node files: a worker's first act is to read its own node, and several now interleave struck-through paragraphs with live ones. **Never-delete and load-once-cheaply are in direct conflict and never-delete is winning**, which is the right way round for a record and the wrong way round for the party that has to read it before starting work. Not sharp enough to be a node because the remedy is genuinely unclear — split again, prune struck-through text into an archive file, cap an item's updates, or accept it and give the map a rendered view. Adjacent to *how the human sees graph progress*, which is the same problem for a different reader, and to *extraction of a graph tool*, which is where a summariser would live if the answer is a tool. **Repriced, and one of the four remedies has now been exercised once.** The standing preference above settles who the reader is — the node files are for **agents** — so the cost of never-delete is agent context rather than human patience, which is the resource [Friction from running this map by hand](nodes/24-self-hosted-friction.md) found fails first. That makes the conflict sharper rather than softer. And at [Carry the recorded deltas into the shipped skill files](nodes/26-carry-deltas-into-shipped-files.md) the **prune** remedy was used deliberately for the first time: three correction rounds had left that node's `## Answer` holding a handover about 95% identical to the final one and wrong in five places, so the final handover **replaced** it rather than being stacked beside it, on the never-delete rule's own escape — *information leaves a file only when it is clearly wrong* — with every difference already recorded round by round in `## Review`. One instance is not a practice. What it establishes is that the escape clause is wide enough to do the job when the superseded text is a near-duplicate, which is the only case where stacking costs a reader ~1700 words for a 5% difference. **This item's own name is now measured wrong, by [How an agent workflow and its skills reduce their own token cost](nodes/52-token-cost-of-a-workflow.md).** Struck-through text is **1,649 characters of 79,361 in this map — 2.1%** — and **4,269 of 982,260 across all 54 node files — 0.4%**. Superseded text is a rounding error. What makes this map expensive is **live** prose under the **append-in-place** practice: the fog paragraph at line 75 is 20,589 characters ≈ 5,147 tokens on its own, larger than any shipped contract and 26% of the file. So *never-delete is winning* is false and the conflict is real: of the four remedies listed above, **prune struck text into an archive recovers 2.1% and cap an item's updates addresses the actual cost.** And the cost has a payer nobody had named: **every worker reads this whole map, cold and uncached, once per node** — ~19,840 tokens, 4.4× the largest shipped contract and 81% of the whole shipped corpus — because *"a subagent starts its own conversation with its own system prompt and tool set… Its first request doesn't read the parent's cache."* At the dogfood target's 179 nodes that is **~4M tokens of uncached map re-reading alone**, on a file that grows monotonically. That reframes the whole item: it is not *when does this map become too expensive to load*, it is **already the single largest recurring token cost in the design**, and the reader who pays is a worker rather than the manager. Still not sharp enough to be a node — the remedy is a judgement, and it is [What the token findings change in the workflow and its skills](nodes/53-what-token-findings-change.md)'s, where node 52 routed *shrinking what a worker reads of this map* as the sharpest of its four.

*A note on the paragraph above, which is quoted rather than endorsed:* it points at a fog item by the
line number it sat on, and that pointer was already stale when it was written. The rule it breaks is
fixed at [What the token findings change in the workflow and its
skills](nodes/53-what-token-findings-change.md), under its heading `### Four standing rules of this
effort`: *“Cite a file by heading or by a quoted phrase, never by line number.”* The item the stale
pointer means is the one quoted directly above this note.

### Whether a research node is warranted

- **Whether a research node is warranted** — none exists yet, because every open question is a design decision rather than an external fact. The trigger written here was "if revision semantics stalls"; it did not stall, so that trigger is spent, and no research node is outstanding on this account. **The premise is now retired** by [Dogfood target](nodes/09-dogfood-target.md): it held only because every question on *this* map is a design decision. Lang's do not all behave that way — `CLASS-1` ("the box") is specified as nothing but a description and *a pointer to Effekt's paper*, which is an external fact to go and read. So the first genuine research node arrives with the dogfood, and the coverage criterion requires one to be run. ~~**The criterion is now discharged, and not by the dogfood.**~~ **The criterion is discharged three times over, all on this effort and all from the human's own steering rather than from a stalled decision.** [Review every shipped file against `/writing-great-skills`](nodes/47-review-shipped-skills.md) was the first: it read a standard living in a plugin outside this repo and returned facts with sources, and it was worth running — six findings, six places the files already met the standard, and it **falsified a measurement the manager had written into its own node**. Then [Re-review the shipped files against `/writing-for-agents`](nodes/54-review-against-writing-for-agents.md), because that standard was renamed and rewritten upstream the same day; and [How an agent workflow and its skills reduce their own token cost](nodes/52-token-cost-of-a-workflow.md), which reads the open internet. So this item is spent as a *question* and leaves two facts behind it. **A research node's real trigger was neither of the two written here.** It was not *revision semantics stalling* and not *the dogfood's external facts* — it was **the product being held against a standard that lives somewhere else**, which is a trigger this map never wrote down and which fires on any effort whose deliverable has an external yardstick. **And an external standard can move under a resolved node.** Node 47 resolved and was superseded within the hour by an upstream rename it had no way to see, which is a failure mode no node in this effort had met: the cascade fires when *this graph's* decisions move, and nothing watches a source outside the repository. Recorded here rather than minted, because the remedy is unclear and a node built on a guess is the delta-list failure again.

## Out of scope

Nothing moved: the map carries this section unchanged.

## Notes — the standing preference on the manager never idling, before node 93

*Moved verbatim by the manager when [Rules added to one effort's map](nodes/93-effort-scoped-custom-rules.md)
established that a standing rule binds only once it is in the map, and the human strengthened this one from
**propose** to **start**. Superseded text, moved rather than struck in place, per `## Writing the map`.*

- **The manager never idles, and proposes the next work itself as each node finishes.** The human's standing instruction, `verbatim`: *"You can start new tasks. You should automatically propose to start a new task when a task finish"*. So a closing report is not an ending: it names what is being started next, and it is owed automatically at the moment a node closes. Filed here under the rule [What the manager works on next, and how the human redirects it](nodes/16-human-steering.md) fixed for standing instructions; proposing is the report, and the human's override is one line.

## Notes — the standing preference on one question at a time, before the human set a grilling-node target

*Moved verbatim by the manager when the human answered [The manager starts the next node rather than proposing
it](nodes/100-the-manager-starts-the-next-node-rather-than-proposing-it.md)'s raise with a target count and a top-up
rule. Superseded text, moved rather than struck in place, per `## Writing the map`.*

- **The human is asked one question at a time.** Two grilling nodes run at once to keep the human's queue full, per [Concurrency model](nodes/04-concurrency-model.md) — a queue, which the manager serves one at a time. Where a second worker's question arrives while one is outstanding, the manager holds it and relays it after the first is answered. Their instruction, `verbatim`, after the manager stacked two: *"You forgot that it should be only one question at once."*

## Superseded from `## Not yet specified`, at nodes 98 and 91's filing

*Moved verbatim under the `Change the map` procedure. Reported as stale by node 98's worker, whose retrospective
found it: the manager's own skill had shipped at [node 76](nodes/76-write-the-manager-skill.md) and the item still
said it had no node.*

> - **The implementation nodes that write the actual skill files.** Two pieces are left. The **manager's own skill**
>   has no node yet and both blockers it last carried have since resolved; the requirements it has accumulated sit on
>   the nodes that produced them rather than being restated here — chiefly [subagent context
>   contract](nodes/12-subagent-context-contract.md), [what the manager reports to the
>   human](nodes/46-what-the-manager-reports.md) and [collapse the manager's discipline onto
>   `scribe`](nodes/61-collapse-onto-scribe.md), with the cascade's own contract already split out as [write the
>   cascade pass's worker contract](nodes/44-cascade-worker-contract.md). The **adoption mode** waits on [adopting an
>   in-flight effort](nodes/18-adopting-in-flight-effort.md). What would settle the item: a node per remaining file,
>   each with a spawner-written acceptance condition.

## Superseded from `## Destination`, at node 91's filing

*Nothing was replaced — the section gained a line rather than losing one. Recorded here so the addition's moment is
findable: before node 91, `## Destination` said what reaching the end looked like and said nothing about whether
reaching it was expected.*

## Superseded from `## Notes`, at node 103's filing — the standing preference on settling a node's flags

*Moved verbatim under the `Change the map` procedure by [Carry the pick-report settling moment into the shipped files
and the map](nodes/103-carry-the-pick-report-settling-moment.md)'s worker. The clause that failed is
**the last answer on a grilling node**: a grilling node's flags do not exist at that moment, established at [A node's
flags arrive after the human moment that was supposed to settle
them](nodes/99-flags-arrive-after-the-node-s-human-moment.md) and widened to every kind of node at [Whether a
research node's and an AFK precondition node's flags settle at the pick report too](nodes/102-do-afk-nodes-flags-settle-at-the-pick-report.md).
The human's quoted instruction is unchanged by the replacement.*

> - **Approving a node's end settles that node's flags.** The human's standing instruction, `verbatim`: *"Also, when I approve the end of the node, the flags should be considered ok"*. So the manager does not ask a second time — the approval at a gate, or the last answer on a grilling node, **is** the settlement, and it refines the practice on [Whether flags.md survives the settle-at-close practice](nodes/27-does-flags-file-survive.md). **The consequence the manager must carry:** the gate payload has to present every flag the node holds, because a payload that omits one settles it silently.

## Superseded from `## Notes`, at node 119's resolution

*Moved verbatim by the manager before the map was changed, under the map's own change procedure. The clause that
failed is the closing one: **the two things it said were unsettled are now settled** by [Whether a dead attempt is
resumed from its transcript rather than replaced](nodes/119-dead-attempt-respawned-rather-than-resumed.md), which also
established the possibility the rule was conditional on. The human's quoted instructions are unchanged by the
replacement, and the replacement points at the node rather than restating it.*

> - **An agent is resumed wherever it can be resumed, a checker and a dead attempt included.** Two standing instructions of the human's, given together, `verbatim`: *"The checkers should be resumed, it is expensive to figure out things multiple times. For the dead attempts it should be changed to resume also"*, and then, widening it: *"Whenever it can be resumed, resume I think"*. So the manager's default is **resume**, and respawning is what it does when resuming is not available. **It reverses two things the shipped files say** — the glossary's *"a dead worker is replaced"*, and the practice of a fresh checker per run — and the human's ground is neither of the ones the manager had in mind: it is that **rediscovering the same facts costs more than the independence it buys**, which this map already evidences, two checker runs having spent their largest single cost finding the review route. **In force on this effort from now**, under [Rules added to one effort's map, and what makes them legitimate](nodes/93-effort-scoped-custom-rules.md). **Two things it does not settle**, left to [Whether a dead attempt is resumed from its transcript rather than replaced](nodes/119-dead-attempt-respawned-rather-than-resumed.md): what a resumed checker may re-use — its findings about the repo, yes; its own verdict on the work, unresolved — and what establishes that a dead attempt's state is sound enough to continue from.

## Superseded from `## Notes`, at node 114's check — three corrections

*Moved verbatim by the manager before the map was changed, under the map's own change procedure. All three were
found by [`CONTEXT.md`'s `Destination` entry does not say the destination states whether the effort is expected to
end](nodes/114-context-destination-entry-omits-the-expectation.md)'s worker in its retrospective, and all three were
re-verified by the manager before this edit rather than taken from the report. **One of the three the worker stated
more strongly than the facts support**, and the replacement is narrower than what it asked for; the difference is
recorded in the note beside each.*

**1. The bar line claimed the repository has no ignore file.**

> `graph-agent` has **no build, no tests, no formatter and no CI** — no ignore file, no manifest, no task runner,
> nothing to invoke.

*Verified false: `ls .gitignore` and `git ls-files .gitignore` both return it, 223 bytes, tracked, added by the
worktree landing policy to ignore `.worktrees/`. The bar's conclusion is untouched — a `.gitignore` is nothing to
invoke — and two checkers have already established the empty command half independently while reading this false
parenthetical.*

**2. The review route listed `where` among `CONTEXT.md`'s ordinary-English refusals.**

> about a third being ordinary English refused only for one concept — `report`, `run`, `session`, `index`, `plan`,
> `item`, `question`, `where` — so a scan for them returns false positives and the distinctive refusals are checked
> by hand instead.

*Verified false: no `_Avoid_` line in `CONTEXT.md` refuses `where`. Exactly one `_Avoid_` line contains the word,
the `Raise` entry's, and there it is a conjunction inside the gloss on `ask` rather than a refused term. The map
presented the list as **measured**, so a checker taking it literally would grep for a non-refusal in a file where
the word appears throughout. The other seven are genuine.*

**3. The retrospective item called the retrospective a sixth handover part.**

> - **Every worker returns a retrospective as a sixth handover part, on this effort only.**

*The worker reported this as the map being **off by one**. It is not, and the correction is narrower than the
report. Verified: `expedition-grilling/SKILL.md` says *"Five parts, every time"* and
`expedition-implementation/SKILL.md` says *"Six parts, every time"*, the sixth being the gate payload. So the
retrospective is the **sixth** part on the four kinds whose handover has five, and the **seventh** on an
implementation node. The map's wording was right for four of the five kinds and wrong only for implementation;
the worker read the implementation contract, which is the one case where its claim held.*

## Archived when the human's checker direction arrived, 2026-09-04

**The review route's naming of a reviewing skill, and its account of how much of that skill may run.** Superseded by
the human's standing direction that the checker must not go looking for the skill or the rules, and that
`mattpocock-skills:code-review` is not to be used at all. Their words are in the map's `## Notes`. The superseded
text, `verbatim`:

> **The reviewing skill is `mattpocock-skills:code-review`, and only part of it may run here.** Its spec step
> searches `docs/`, `specs/` and **`.scratch/`** for a requirements document — and `.scratch/` is this effort's
> record, which a checker is blind to by design, so that step is left unrun and the acceptance condition is the only
> statement of intent. Its standards step looks for `CODING_STANDARDS.md` or `CONTRIBUTING.md`, neither of which
> exists here, so the sources above are supplied by hand. Where it runs an agent of its own, that agent is **given**
> the standards, the paths, the diff and the condition's mandated constraints, and is **denied** the node files,
> `decisions.md` and `flags.md` — so it is handed no less than the checker and has nothing to go looking for.

*What of the paragraph is **not** superseded and stays in the map: the list of standards to hold work against, the
measured trap about `CONTEXT.md`'s refused words being unusable as a grep list, and the `where` correction. Those are
the rules themselves, which the human's direction keeps — it moves where the rules come from, not what they are.*

## Superseded from `map.md` at node 139, when the manager's material moved out

Four lines of [`map.md`](map.md) changed rather than moved when [Move the manager's material out of the map, and give each item a soft size target](nodes/139-move-the-managers-material-out-of-the-map.md) split [map-manager-only.md](map-manager-only.md) out of it. The five bodies that **moved** are not quoted here: they stand verbatim in `map-manager-only.md`, which is part of the map and not history. These four are the lines the split reworded, quoted `verbatim` in the form they had before it.

*The opening sentence, whose admission test went from `a worker` to `every worker` — one word, and 30% of the file:*

> **Every worker reads this whole file, cold, once per node, so it holds only what a worker can act on.** Where a line below has an account behind it — how it came to say what it says — that account is in [map-history.md](map-history.md), moved there verbatim by [Restructure `map.md` to what every worker needs](nodes/59-restructure-the-map.md): read that file when a line here has more history than it states, and this one to work a node. Whether the split falls in the right place is settled by measurement rather than argument — a worker reporting what this file did not tell it is [A worker reports what the map did not tell it](nodes/60-worker-reports-map-shortfall.md).

*The standing direction on the checker's rules, which cited the review route by its position in the file:*

> - **The rules a checker holds work against are given to it, never found by it — and the implementer is held against the same ones.** The human's standing direction, `verbatim`: *"Also I don't know if I have talked about it but in the checker, it shouldn't try to find the skill/rules, they should be at the map level and sent by the manager or just read by the checker. I don't know if it is still the case but we shouldn't use matt pockock skills code review skill as it is too generic. (it is easier to change the rule when its in a file than when the checker finds stuff by itself. The rules should also be used by the implementer"*. **Their stated ground is changeability**: a rule written in a file can be edited, where a rule a checker discovers for itself cannot. **In force on this effort from now**, under [Rules added to one effort's map, and what makes them legitimate](nodes/93-effort-scoped-custom-rules.md). **What it reaches, and it is more than one file:** the checker's contract, which today tells a checker to *find* a reviewing skill before it reads the work and to hold the work against whatever rules it found; the review route above, whose naming of a reviewing skill is superseded by it; **ground rule 5**, which locates `/writing-for-agents` in a plugin by name; and the implementation contract, which is held against the bar rather than against a named rule set. **What it does not settle, and the manager has decided none of it:** where the rules live now that they are not discovered, what a checker is given in place of a reviewing skill's procedure, and whether the implementer receives the same text or a pointer to it.

*The note on Claude tokens and a non-Claude worker, which cited the fog by its position in the file:*

> **Claude tokens are scarce, and a worker will eventually not be a Claude subagent.** The human's constraint at work: *"I have a limited amount of claude credits but unlimited use of gemma 4 (and probably other soon)"*, so an expedition should be able to send cheap bounded work to a cheap model and keep Claude for the hard nodes. Two axes hide in that and only one is cheap: a worker's **model** is already choosable per spawn, while swapping the **harness** cannot be done from inside one manager session at all — it needs several processes and something between them, which is the firstmate shape in the fog below. **The sequencing is the human's: finish the Claude-subagent version as v1, then redraw for a heterogeneous one** — a fresh effort under this map's own rule rather than a resumption, which is what keeps v1 small. What v1 owes v2 is only insurance that costs nothing today: a worker contract that stands alone as a file, and a **measured** spend per node type from the dogfood so v2's routing is designed from data. Deliberately absent: a per-node model or capability field, the node's kind already predicting what it needs.

*The graph's file count, five before the split and six after it:*

> **The graph is five files**, fixed by [Graph file format](nodes/13-graph-file-format.md) and extended by [Restructure `map.md` to what every worker needs](nodes/59-restructure-the-map.md): this `map.md`, the append-only index [decisions.md](decisions.md), the append-only [flags.md](flags.md), one file per node at `nodes/NN-<name>.md`, and [map-history.md](map-history.md), which holds the append history moved out of this map and is read for the account behind a line rather than to work a node. A node's identity is its sequential `NN`, permanently; its name is free-form and carries a foreign label when the effort was adopted from somewhere else.

## Superseded from `map.md` at node 140, when the implementer's and checker's material moved out

Two lines of [`map.md`](map.md) changed rather than moved when [Move the implementer's and checker's material out of the map](nodes/140-move-the-implementers-and-checkers-material-out-of-the-map.md) split [map-implementation-rules.md](map-implementation-rules.md) out of it and out of [map-manager-only.md](map-manager-only.md). The five bodies that **moved** are not quoted here: they stand verbatim in `map-implementation-rules.md`, which is part of the map and not history. `map-manager-only.md` keeps its own superseded sentence in place, beside the live one, rather than sending it here.

*The pointer to the manager's file, which listed the review route among what that file holds — the review route having moved on to the file the implementer and the checker read:*

> **What only the manager acts on is in [map-manager-only.md](map-manager-only.md)**, a part of this map that no worker reads: the review route, the dogfood target, the label vocabulary, the fog, and what is out of scope — moved there by [Move the manager's material out of the map, and give each item a soft size target](nodes/139-move-the-managers-material-out-of-the-map.md).

*The graph's file count, six before this split and seven after it. The line is superseded in place in `map.md` rather than moved, `six` standing struck beside `seven`, and it is quoted here whole so that the before-state of every line the split changed is in one place:*

> **The graph is six files**, fixed by [Graph file format](nodes/13-graph-file-format.md) and extended by [Restructure `map.md` to what every worker needs](nodes/59-restructure-the-map.md) and by [Move the manager's material out of the map, and give each item a soft size target](nodes/139-move-the-managers-material-out-of-the-map.md): this `map.md`, the append-only index [decisions.md](decisions.md), the append-only [flags.md](flags.md), one file per node at `nodes/NN-<name>.md`, [map-history.md](map-history.md), which holds the append history moved out of this map and is read for the account behind a line rather than to work a node, and `map-manager-only.md`, which holds the part of the map only the manager acts on. A node's identity is its sequential `NN`, permanently; its name is free-form and carries a foreign label when the effort was adopted from somewhere else.

## Not yet specified — superseded at the close of the session that ran nodes 129-163

*Moved verbatim under the `Change the map` procedure. Its replacement records a reconciliation procedure
that was run and verified rather than designed.*

- **Resume and recovery** — what happens when the manager's context compacts or its session dies mid-graph. Durable per-attempt state exists, per [relay protocol](nodes/08-relay-protocol.md), so what is unspecified is everything the manager holds that is *not* an interview: the node-name-to-routing-key mapping as a whole, and whatever it knew about why it chose the nodes it chose. What would settle it: a reconciliation procedure a fresh manager runs from disk. Worth reading before deciding, per [dogfood target](nodes/09-dogfood-target.md): Lang's hand-built `handoff.md` is a human's manual answer to this exact problem.

## Notes — the retrospective's four questions, superseded at node 141

*Moved verbatim under the `Change the map` procedure. Questions 2 and 3 are re-rendered; 1 and 4 stand.*

**The four questions, as the spawn puts them:** what did you have to hunt for — the fact, where you found it, where you looked first; what did you read and not use; what would have made this node easier, in the spawn, the node file, or the contract; and what did you read that was stale, wrong, or contradicted something else.

## Notes — the grilling-node target, before the human raised it to three

*Moved verbatim at the human's instruction raising the count. The clause as it stood, inside the standing preference
on one question at a time:*

> and **the target for concurrently running nodes that need the human is two for this effort**, settable by them, with the manager starting whatever it takes to return to that target the moment a node finishes.

## Notes — the grilling-node target at three, before the human set it to two alongside a second code slot

*Moved verbatim under the `Change the map` procedure. The clause as it stood:*

> and **the target for concurrently running nodes that need the human is three for this effort**, settable by them, with the manager starting whatever it takes to return to that target the moment a node finishes. **It was two and the human raised it**, `verbatim`: *"you can start a 3rd grilling"*. The manager read that as setting the count rather than as permission for one extra start, on the ground that the sentence above makes the amount a number the human sets — *"2 by default by the user can ask for more"* — and it tops up to three from now.

## Superseded from `map-implementation-rules.md` — the code-slot count at one

*Moved under the `Change the map` procedure when the human set two implementation workers alongside two grilling
nodes. The sentence is also struck in place in the rules file, that file's own idiom. As it stood:*

> **How many implementation workers run at once is a setting of the effort, and for this effort it is one.**

## Notes — the standing preference on never-delete, before its two boundaries were written into it

*Moved verbatim under the `Change the map` procedure, carrying [Where the never-delete rule
stops](nodes/189-where-the-never-delete-rule-stops.md)'s answer into the preference itself. It said nothing about the
rule stopping at a rule statement, and its illustration `— a node or this map —` was twice read as an exhaustive
list of the files it reached. The bullet as it stood among `map.md`'s standing preferences:*

> **An in-place update never deletes.** When any file in the graph is edited — a node or this map — superseded text is marked as superseded and left where it is, and new text is added around it. Information leaves a file only when it is clearly wrong or the human asks for it gone. Quiet deletion is most damaging and least visible in the map itself.

## Notes — the token-use preference, before the human corrected the manager's gloss on predicted saving

*Superseded at [node 183](nodes/183-nothing-measures-the-record-about-itself.md)'s interview. The clause carried the
human's `verbatim` instruction and then a sentence of the manager's own that read a prohibition into it; their
correction, `verbatim`: "I don't think I said something about forbiding saving by prediced savings ? having real
number is better fo cource but guessing can help." Banked verbatim, and the replacement stands in `map.md`.*

- **Token-use improvement is prioritised above the rest of the frontier.** The human's standing instruction, `verbatim`: *"We should also bump the priority for improvement to token use"*. It is a **redirection** of [What the manager works on next, and how the human redirects it](nodes/16-human-steering.md)'s default rather than an exception to it: the alternation between a design stream and a delivery stream stands, and within each stream a node that reduces the workflow's own token cost outranks one that does not. What it does **not** license: prioritising a saving over a correctness finding, or prioritising one whose size has not been measured — **a ranking by predicted saving is the *token maxing* failure in reverse.**

## Not yet specified — extraction of a graph tool, which node 183 made specifiable

*Moved verbatim under the `Resolve` procedure's steps 4 and 5 at [Nothing measures the record about
itself](nodes/183-nothing-measures-the-record-about-itself.md), whose answer supplied the trigger this item was
waiting for and split it into two nodes: [write the
derivations](nodes/210-write-the-derivations-this-effort-derives-by-hand.md) for the measuring half, and [nothing
triggers the ten mechanical checks](nodes/213-nothing-triggers-the-ten-mechanical-checks.md) for the verdict half,
which node 183's own answer states its remedy does not reach. The item as it stood:*

- **Extraction of a graph tool.** Specified in everything but the trigger: the mechanical invariants a `check` would enforce are listed in [graph file format](nodes/13-graph-file-format.md), and the cost of not having one is measured rather than predicted — **twelve false results from hand-written scans across seven sessions**, plus one hand re-derivation of those scans per session. What would settle it: the trigger to write it. Shaped by [write the graph conventions document](nodes/21-conventions-document.md), [friction from running this map by hand](nodes/24-self-hosted-friction.md) and [what the checker contract owes to having been run](nodes/31-checker-contract-owes.md); the rules such a tool must not get wrong are being moved next to the checks by [co-locate the scan rules with the mechanical checks](nodes/49-colocate-scan-rules.md).

## Superseded from `map-implementation-rules.md`'s opening — the second statement that an account belongs here

*Moved verbatim under the `Change the map` procedure at [Collapse the rules file's two statements that accounts live
in `map-history.md`](nodes/200-collapse-the-rules-files-two-map-history-statements.md). It stood in the text before
that file's first `##` heading, trailing the paragraph beginning "Nothing below was reworded on the way here", whose
subject is the verbatim move rather than where an account lives. The admission test added at [node
196](nodes/196-give-the-rules-file-its-admission-test.md) states the same thing as a consequence of the test, where a
reader needs it, so this stood as a second statement of it and under a lead-in it did not belong to. **It stated a
rule rather than recorded what happened, so it took this route rather than strike-in-place**, on [Where the
never-delete rule stops](nodes/189-where-the-never-delete-rule-stops.md)'s test. The sentence as it stood:*

> The account behind a line here is in [map-history.md](map-history.md), as it is for a line in `map.md`.

## Notes — the moved-standard licence, retired when the branch was repaired at node 223

*Banked verbatim by the manager at node 223's landing, before the item was replaced. The licence's own
text says it expires when the branch is repaired; node 223 is that repair, so the expiry is the item's own
rather than a decision of the manager's.*

- **A checker that hits the contract's moved-standard branch carries on and discloses, until the branch is
repaired.** The human's answer at [node 178](nodes/178-whether-adding-a-standard-is-a-moved-standard.md), `verbatim`:
*"Q1 ok Q2 ok"*, taking that node's worker's recommendation in its own words — *"Carry on and disclose. […] The
disclosure is the safeguard: it reaches you at the node's gate either way, without a stopped check."* **What it
licenses**, precisely: where the work under check has edited a document that holds a standard, the checker issues
its outcome and says in that outcome that it settled the branch and on what reading, instead of raising and handing
back no outcome. **What it does not license:** anything else in the checker's contract, and no departure by a worker
of any other kind. **Its ground is measured** — 37 of 161 commits touched such a document, and four checkers had
already improvised past the branch in the same direction with none having authority to. **It expires when the branch
is repaired**, which is `Q1.`'s answer: the branch stops a check only where a rule *this* work must be judged by has
itself changed and no unchanged statement of it survives. **The manager carries this in a checker's spawn** for as
long as it stands, marked as the human's and not as the manager's.

## Superseded from `map-manager-only.md` — the landing section's accounts

*Banked verbatim under the `Change the map` procedure at [Bank the landing section's accounts out of
`map-manager-only.md`](nodes/229-bank-the-landing-sections-accounts-out-of-map-manager-only.md). It is the one
bounded exception the human licensed to [node
191](nodes/191-the-rules-file-carries-accounts-rather-than-rules.md)'s rule that no sweep of a map file is owed
or licensed: the route runs over `## Landing an implementation node's work` and over nothing else, and node
191's rule is unchanged for every other section, file and sibling. The ground, settled at [node
225](nodes/225-whether-map-manager-only-gets-an-admission-test.md), is that node 191's refusal rested on the
nodes queued on that file being how it converges, which was measured false for this section: the passages
carrying the largest accounts are touched by no open node. **What left the section is history** — how a rule was
learned, how many attempts it took, what one cost, who was wrong, and what the file said before. **What stayed
is every trigger**: the error strings, the human's verbatim words, and the condition under which each rule
fires. Each passage below is reproduced byte-identical to the text it had in that section, struck-through text
staying struck through, under the number of the edit that removed it. Edit 11 appended rather than removed, so
it has no passage here.*

### Edit 1 — the manager creating the worktree by hand

*From the landing policy paragraph. Deleted, and it stood as:*

~~the manager creates for that node with `git worktree add` off the current `HEAD`~~ 

### Edit 2 — the code-slot count at one

*From the code-slot paragraph. Deleted, and it stood as:*

~~**How many implementation workers run at once is a setting of the effort, and for this effort it is one.**~~ 

### Edit 3 — what the branch-per-node policy superseded

*From the landing section, after the code-slot paragraph. Deleted, and it stood as:*

**What that supersedes**: this map used to say *"No branch is ever created or switched, nothing is ever pushed, and history is never rewritten"*, and two of those three clauses no longer hold — the workflow branches per node, and a rebase rewrites history. *Nothing is ever pushed* is the one that stands untouched. The sentence in full is in [map-history.md](map-history.md).

### Edit 4 — the manager creating nothing

*From the first bullet under *How the worktree is made*. Replaced, and it stood as:*

~~**The manager creates nothing.** It spawns the implementation worker with the harness's worktree isolation.~~
  **Superseded by the human's own route**

### Edit 5 — the harness picking the path and the branch

*From the second bullet under *How the worktree is made*. Replaced, and it stood as:*

- ~~The
  harness picks the path, `.claude/worktrees/agent-<agentId>/`, and the branch, `worktree-agent-<agentId>`, and the
  manager learns both from the worker's completion notification. **The node's id is no longer in either**; the commit
  trailer `Node: <effort>/<NN>` is the join key and is the manager's to write.~~ **Superseded by the bullet
  above**: the node's id is in the path and the branch again, and the commit trailer stays the join key regardless.

### Edit 6 — `worktree.baseRef` = `head` as the typical case

*From the bullet on what the reset costs in practice. Replaced, and it stood as:*

— ~~**which is the typical case, and is theirs rather than this effort's**~~
  **which is measured at [node 175](nodes/175-what-the-worktree-cycle-does-to-the-sandbox.md) not to hold on this
  machine: the setting is absent, so the default `fresh` applies, every harness worktree lands on `origin/master`, and
  the base is always stale. Three worktrees created during that node all recorded `CLAUDE_BASE` = `origin/master`
  while `master` was ahead. The three-case account still stands; the case it called typical is the one that never
  happens here, and the reset always runs.** — the
  worktree lands on `HEAD` and no reset happens at all.

### Edit 7 — the reset measured as inside the sandbox, and its correction

*From the bullet on `EnterWorktree` being needed for neither step. Replaced, and it stood as:*

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

### Edit 8 — what a late reset would have done to node 140

*From the bullet on verifying the base at every spawn. Deleted, and it stood as:*

 Node 140 was moving text
  verbatim between files, so a late reset there would have silently reverted [node
  147](nodes/147-graph-records-name-absolute-paths-on-a-machine.md)'s landed work with every check passing.

### Edit 9 — how node 143's measurement was reached

*From the bullet on a failed rebase leaving its partial checkout behind. Replaced, and it stood as:*

Measured at node 143, after four failed attempts and two wrong diagnoses.

### Edit 10 — the three rounds of experiment, and the read-only-skills rule they replaced

*From the bullet on the sandbox restriction that bites this lifecycle. Replaced, and it stood as:*

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

### Edit 12 — the `git -C` asymmetry

*From the sub-bullet on the `git -C` asymmetry. Replaced, and it stood as:*

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

### Edit 13 — two distinct sandbox restrictions

*From the bullet on two distinct sandbox restrictions. Deleted, and it stood as:*

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

### Edit 14 — the merge step needing the sandbox off

*From the bullet on the merge step needing the sandbox off. Deleted, and it stood as:*

- ~~**The merge step needs the sandbox off where the node touched a shipped file.**~~ Measured at node 140: `git merge
  --ff-only` failed with `unable to unlink old '.claude/skills/expedition/graph-conventions.md': Read-only file
  system`, `/proc/mounts` showing `.claude/skills` bind-mounted `ro` inside the manager's sandbox. **`HEAD` does not
  move and nothing is lost** — the commit stays on its branch and the merge succeeds on a retry outside the sandbox —
  but the manager must expect it rather than discover it, since most of the open frontier touches `.claude/skills/`.

## Superseded from `map.md`'s `## Notes` at node 244 — the harness-worktree rule's closing sentence, which said the route question was open

*Moved verbatim under the `Change the map` procedure. It closed the standing preference beginning "A worktree is
created by the harness, never by hand." and was wrong three times over: it called the route question open when
[Which harness route creates an implementation node's worktree](nodes/150-which-harness-route-creates-a-worktree.md)
had resolved; it offered two candidate routes, the manager entering or an isolated worker, when the route in force is
the human's own third and the isolated-worker route it pointed at is the superseded one; and its constraint that the
manager must stay in the main tree is contradicted by the landed practice, in which the manager enters the worktree
transiently to create it and returns. It stated a rule that currently binds, so it took this route rather than
strike-in-place, on [Where the never-delete rule stops](nodes/189-where-the-never-delete-rule-stops.md)'s test. The
sentence as it stood:*

> **One point of fit it does not settle, and the manager has decided none of it:** `EnterWorktree` switches *the calling session* into the worktree, and the manager must stay in the main tree to own the graph, while the party that needs to be in the worktree is the worker and then the checker — so which of the harness's two routes carries this (the manager entering, or an isolated worker) is open and is [Which harness route creates an implementation node's worktree](nodes/150-which-harness-route-creates-a-worktree.md).

## Superseded from `map.md`'s `## Notes` at node 260 — the steering that the manager never asks which waiting thing to take next, before it shipped

*Moved verbatim under the `Change the map` procedure. It was this effort's own steering for as long as the
prohibition stood nowhere in the shipped files; [The never-ask-which rule is stated for picking a node and not for
what is already waiting](nodes/260-never-ask-which-is-stated-for-nodes-not-for-what-waits.md) carried it into
`.claude/skills/expedition/SKILL.md` and `.claude/rules/expedition-triggers.md`, which is where it stopped being
this effort's own, and `map.md` now carries a pointer in its place. It stated a rule that currently binds, so it
took this route rather than strike-in-place, on [Where the never-delete rule
stops](nodes/189-where-the-never-delete-rule-stops.md)'s test. The human's words that set it are inside the
paragraph and survive here. The paragraph as it stood:*

> **The manager never asks the human to choose which waiting thing to take next.** Their standing instruction, `verbatim`: *"Just give stuff, don't ask me too choose"*. It reaches the **manager's reports** rather than a worker's payload: where more than one thing is waiting, the manager picks by the rules it already has — one thing in front of the human at a time, tier 1 before tier 2, arrival order within a tier — and sends it, rather than ending a report by listing what is waiting and inviting a pick. **What it does not reach** is a question a *worker* puts to the human that genuinely offers options: that is the worker's question and the manager relays it whole. Naming in one line what else is waiting stays, since the one-question rule requires it and it invites nothing. **In force on this effort from now**, under [Rules added to one effort's map, and what makes them legitimate](nodes/93-effort-scoped-custom-rules.md).

## Superseded from `map.md`'s `## Notes` at node 268 — the standing instruction that a worktree is created by the harness and never by hand

*Moved verbatim under the `Change the map` procedure at [Carry the plain-git worktree route into the
map](nodes/268-carry-the-plain-git-worktree-route-into-the-map.md), carrying out [Should the worktree route drop
`EnterWorktree` for plain git, behind a
script](nodes/265-should-the-worktree-route-drop-enterworktree-for-git.md). It held two things the human reversed on
their own word: the standing instruction that a worktree is created by the harness and never by hand, and [node
150](nodes/150-which-harness-route-creates-a-worktree.md)'s `EnterWorktree`-then-reset route. What replaces it in
`map.md` is the worker-facing half of the plain-git route, with the whole of it in
[map-manager-only.md](map-manager-only.md) under *How the worktree is made*. It stated a rule that currently binds, so
it took this route rather than strike-in-place, on [Where the never-delete rule
stops](nodes/189-where-the-never-delete-rule-stops.md)'s test. The human's words that set it, and the `EBUSY`
measurement behind them, are inside the paragraph and survive here. The paragraph as it stood:*

> **A worktree is created by the harness, never by hand.** The human's standing instruction, `verbatim`, after the manager hand-rolled one and then could not remove it: *"when you use worktrees, you should use the EnterWorktree skill instead of creating worktrees by hand - that way you don't have all these worktree management issues afterwards"*. **What went wrong is measured rather than argued:** the sandbox bind-mounts `.git/config` read-only and makes `.git/worktrees/<name>` its own mountpoint, so `git worktree remove` and `git worktree prune` both return `EBUSY` and the stale entry stays in `git worktree list` — which on this effort reads as an **occupied code slot**, the slot's occupancy being discovered by counting live worktrees. **In force on this effort from now**, under [Rules added to one effort's map, and what makes them legitimate](nodes/93-effort-scoped-custom-rules.md). **The route is settled, and it is the human's own:** the manager calls `EnterWorktree` with a name tied to the node, checks the base the worktree landed on, and `git reset --hard`es it to the manager's own `HEAD` before any worker reads the tree. The manager works from the main tree, and enters the worktree only to create it and bring it to that base. The route is stated in full in [map-manager-only.md](map-manager-only.md), and was settled at [Which harness route creates an implementation node's worktree](nodes/150-which-harness-route-creates-a-worktree.md).

## Superseded from `map-manager-only.md` at node 268 — the `EnterWorktree`-then-reset route

*Moved verbatim under the `Change the map` procedure at [Carry the plain-git worktree route into the
map](nodes/268-carry-the-plain-git-worktree-route-into-the-map.md), carrying out [Should the worktree route drop
`EnterWorktree` for plain git, behind a
script](nodes/265-should-the-worktree-route-drop-enterworktree-for-git.md). What replaces every passage below is the
plain-git route now stated under *How the worktree is made* in that file. Each passage stated a rule that currently
bound, so it took this route rather than strike-in-place, on [Where the never-delete rule
stops](nodes/189-where-the-never-delete-rule-stops.md)'s test, and each is reproduced byte-identical to the text it
had there, under a heading naming where it came from. **The section's measurements were not displaced**: the sandbox
bullet and its three sub-bullets stayed where they are and are marked there, their job being to record what was
measured rather than to state a rule.*

### From the landing policy — who makes the worktree, and where it sits

*A clause of the first sentence. Replaced, and it stood as:*

**created by the harness rather than by hand — see the standing instruction immediately below**, on a branch whose name carries the node's id, placed at `.worktrees/NN-<name>/` **inside** the repository and ignored there.

### From *How the worktree is made* — the section's opening

*Replaced, and it stood as:*

**How the worktree is made, settled at [Which harness route creates an implementation node's
worktree](nodes/150-which-harness-route-creates-a-worktree.md).** Added beside the landing policy above rather than
rewritten into it, because [node 152](nodes/152-where-the-harness-worktree-instruction-lives.md) and [node
144](nodes/144-make-the-rules-file-stand-alone.md) hold conditions quoting that paragraph's exact phrases.

### From *How the worktree is made* — the route bullet

*Replaced, and it stood as:*

- **The route is the human's own**, `verbatim`: *"It calls EnterWorktree specifying a name tied to the node
  and vaguely describing the node's title"*, then *"If it didn't land on HEAD … it does `git reset` itself to reach
  the proper base"*. **The manager calls `EnterWorktree` with a node-tied name**, checks the base it landed on, and
  `git reset --hard`es to its own `HEAD` **before any worker reads the tree** — which is why this needs no
  `worktree.baseRef` setting and assumes no machine. Measured: `EnterWorktree` lands on `origin/master` under the
  default, and the reset **requires the sandbox off**, failing inside it with `Could not reset index file`. The path
  is `.claude/worktrees/<name>/` and the branch `worktree-<name>`, so **the node's id is back in both**.

### From *How the worktree is made* — what the reset costs in practice

*Replaced, and it stood as:*

- **What the reset costs in practice, settled by the human**, `verbatim`:

  > ok so looks like we can indeed do the EnterWorktree -> reset process - that will work so long as either we aren't
  > working on skills (otherwise the agent can ask unsandboxed for the reset and it will be fine) - or if the user
  > already has set baseRef=head in their global config, which will typically be the case.

  So the route stands, and the sandbox restriction above is a cost rather than an obstacle. Three cases, and the
  manager does not need to decide between them in advance: a node touching no file under `.claude/skills/` resets
  inside the sandbox; a node that does asks for that one command unsandboxed; and where `worktree.baseRef` is already
  `head` in the human's global config the worktree lands on `HEAD` and no reset happens at all. **That third case does not occur on this
  machine**: the setting is absent, so the default `fresh` applies, every harness worktree lands on
  `origin/master`, the base is always stale, and the reset always runs — measured at [node
  175](nodes/175-what-the-worktree-cycle-does-to-the-sandbox.md). **The base check still runs in every case**, since what it
  guards against is landing on the wrong base for any reason, not against one configuration.

### From *How the worktree is made* — the manager needing `EnterWorktree` for neither the base check nor the reset

*Replaced, and it stood as:*

- **The manager needs `EnterWorktree` for neither the base check nor the reset.** `cat
  .git/worktrees/<name>/CLAUDE_BASE` and `git -C <worktree> rev-parse HEAD` both answer the base check
  read-only from the main tree, and `git -C <worktree> reset --hard <ref>` runs there too — so **the manager's
  own session never has to leave the main tree**. **The reset is not reliably inside the sandbox**: on one
  worktree it succeeded across a `.claude/skills` file, and on another the same command failed with
  `unable to unlink old '.claude/skills/expedition-grilling/SKILL.md': Read-only file system` and needed the
  sandbox off. Run it sandboxed, and expect to need the override when the range crosses a shipped file. What
  triggers the overlay on one tree and not another is [node
  180](nodes/180-which-trees-get-the-read-only-skills-overlay.md). Where the instruction to use `EnterWorktree`
  now stands is [node 152](nodes/152-where-the-harness-worktree-instruction-lives.md)'s.

### From *How the worktree is made* — the manager verifying the base at every spawn

*Replaced, and it stood as:*

- **The manager verifies the base at every spawn.** A harness worktree's base is governed by `worktree.baseRef`,
  whose default `fresh` means `origin/<default-branch>` — frozen forever on an effort that never pushes. The setting
  is `head`, but **the setting is a property of the environment, cannot be passed per call, and does not travel to
  another machine**, so under ground rule 1 it is observed rather than trusted. Immediately after the spawn the
  manager reads `.git/worktrees/<name>/CLAUDE_BASE`, or runs `git -C <worktree> rev-parse HEAD`, and compares it to
  its own `HEAD`. **Not equal: stop the worker, remove the worktree, and raise it** — never reset the tree in place,
  which leaves it holding pre-repair content for every file the worker has not touched.

### From *How the worktree is made* — the ground for never re-spawning a correction round with isolation

*Replaced, and it stood as:*

- **A correction round resumes the worker** and never re-spawns it with isolation, a second isolated spawn creating a
  second empty tree at a fresh base and stranding the first one's work. Where resume is unavailable the replacement
  is pointed at the surviving path. Flagged at `150.3` as unverified.

## Superseded from `map-manager-only.md` at node 277 — the removal step, and the claim that no step of the route needs an override

*Moved verbatim under the `Change the map` procedure at [The removal step of the worktree route does not work as
written](nodes/277-the-removal-step-of-the-worktree-route-does-not-work-as-written.md). Both passages stated a rule
that currently bound, so each took this route rather than strike-in-place, on [Where the never-delete rule
stops](nodes/189-where-the-never-delete-rule-stops.md)'s test, and each is reproduced byte-identical to the text it
had under *How the worktree is made*. What replaces them is the same route with the removal stated as running with
the sandbox off, carrying its symptom, its trigger and its recovery; the creation, base and writing statements the
first passage over-reached are unchanged and keep their claim that they need no override.*

### From *How the worktree is made* — no step of the route needing a tool call or an override

*Replaced, and it stood as:*

- **No step of the route needs a harness tool call or a sandbox override**, by the manager or by the worker. Settled
  at [node 265](nodes/265-should-the-worktree-route-drop-enterworktree-for-git.md).

### From *How the worktree is made* — the removal bullet

*Replaced, and it stood as:*

- **Remove**: `git worktree remove --force <path>`, then `git branch -D worktree-<NN>-<name>`. Settled at [node
  265](nodes/265-should-the-worktree-route-drop-enterworktree-for-git.md).

## Superseded from `map.md`'s `## Notes` at node 281 — the claim that no step of the worktree route needs a tool call or an override

*Moved verbatim under the `Change the map` procedure at [`map.md` repeats the false no-override claim about the
worktree route](nodes/281-map-repeats-the-false-no-override-claim-about-the-worktree-route.md), carrying out [The
removal step of the worktree route does not work as
written](nodes/277-the-removal-step-of-the-worktree-route-does-not-work-as-written.md), which removed the same
sentence from [map-manager-only.md](map-manager-only.md) and was confined to two files, so it reported this second
copy rather than touching it. The sentence stated a rule that currently bound, so it took this route rather than
strike-in-place, on [Where the never-delete rule stops](nodes/189-where-the-never-delete-rule-stops.md)'s test, and
it is reproduced byte-identical to the text it had under `## Notes`. What replaces it states that creating the
worktree, putting it on its base and a worker writing it need neither, and that the removal is the exception and
runs with the sandbox off, pointing at *How the worktree is made* for its symptom, its trigger and its recovery.
The rest of the paragraph it sat in is unchanged and is not reproduced here.*

*Replaced, and it stood as:*

**No step of the route needs a harness tool call or a sandbox override**, by the manager or by the worker.

## Superseded from `map-implementation-rules.md` and `map.md` at node 289 — the four standing rules for writing, before the fifth was added

### From `map-implementation-rules.md`

**The bar's commands for this repo, discovered on first use** and recorded here so no later node re-derives them, per [Done-ness and termination](nodes/10-done-ness.md). `graph-agent` has **no build, no tests, no formatter and no CI** — no manifest, no task runner, nothing to invoke; the one ignore file, `.gitignore`, ~~ignores `.worktrees/`~~ **ignores `.worktrees/` and `.claude/worktrees/`, the second added at [node 158](nodes/158-ignore-the-harness-worktree-directory.md)** and invokes nothing. Corrected at node 114's check, having claimed no ignore file after one was added by the landing policy; the superseded wording is in [map-history.md](map-history.md). So the bar here is entirely its non-command half: the project criteria (the human's global coding principles and `/naming`), ~~this map's own standing preferences~~ **this effort's ground rules and its four standing rules for writing, the two blocks this file holds below — `map.md`'s standing preferences are not part of the bar, on [node 42](nodes/42-checker-spawn-carries-ground-rules.md)'s test as the review route below states**, `CONTEXT.md`'s `_Avoid_` lines, [`graph-conventions.md`](../../.claude/skills/expedition/graph-conventions.md), `/writing-for-agents`, and the node's acceptance condition — the last two added at [node 184](nodes/184-the-bar-and-the-standards-are-two-different-lists.md). **The two enumerations in this section are one set of standards and not two**: this half is what an implementation node's worker writes to, and the review route's *"standards to hold work against"* below is what its checker holds the finished work against. The *"human's global coding principles"* here is `/coding-principles` there, and the one this half adds is the **node's acceptance condition**, which reaches a checker by its own route. Under the *"if relevant"* clause that is a **complete** bar rather than a deficient one — the same shape the dogfood target has, one step thinner. First discovered and used by [Write the graph conventions document](nodes/21-conventions-document.md).

### From `map-implementation-rules.md`

**The review route for this repo, discovered on first use** and recorded here so no later checker re-derives it, on the same ground as the bar's commands above. Two checker runs spent their largest single cost finding this, and one of them nearly reported the prose standard absent. **The standards to hold work against:** `/coding-principles` and `/naming`; [`CONTEXT.md`](../../CONTEXT.md)'s `_Avoid_` lines; ~~this map's standing preferences, ground rules and four standing rules~~ **this effort's ground rules and its four standing rules for writing, both of which this file holds below**; [`graph-conventions.md`](../../.claude/skills/expedition/graph-conventions.md); and `/writing-for-agents`, which is the standard that bites on prose deliverables and which `/coding-principles` barely touches. **`map.md`'s standing preferences are not among the standards, as a whole.** A standing preference may be an account of what happened or a steer about what gets worked, and only a standing constraint true of any node's work may be held against a piece of work by a reader blind to the record. That test is [node 42](nodes/42-checker-spawn-carries-ground-rules.md)'s; the **ground rules** and the **four standing rules for writing**, both held below in this file, are the two blocks that pass it, and the struck wording named the preferences alongside them — a defect from node 42 onward, found at [node 138](nodes/138-where-the-rules-a-checker-is-held-to-live.md) and carried out here. **No reviewing skill is named for this repo, and a checker does not go looking for one.** The standards above are the whole of what work is held against, and they reach a checker as text rather than as something it discovers — the human's standing direction below. The superseded naming of `mattpocock-skills:code-review`, and the account of how much of it could run, are in [map-history.md](map-history.md). **One trap, measured:** `CONTEXT.md`'s refused words are largely unusable as a grep list, about a third being ordinary English refused only for one concept — `report`, `run`, `session`, `index`, `plan`, `item` and `question` — so a scan for them returns false positives and the distinctive refusals are checked by hand instead. **`where` was on this list and is not refused by any `_Avoid_` line**, found at node 114's check; the superseded wording is in [map-history.md](map-history.md).

### From `map-implementation-rules.md`

**Four standing rules for writing anything in this effort**, fixed by [What the token findings change in the workflow and its skills](nodes/53-what-token-findings-change.md) and held against every prose deliverable. They are rules of writing, where the ground rules above are rules of scope.

### From `map.md`'s `## Notes`

**The four standing rules for writing anything in this effort are in [map-implementation-rules.md](map-implementation-rules.md)** too, held against every prose deliverable and fixed by [node 53](nodes/53-what-token-findings-change.md) — moved by [node 144](nodes/144-make-the-rules-file-stand-alone.md).

## 2026-09-26, the retrospective's place among the handover parts (node 333)

Superseded wording from `map.md`'s `## Notes`, replaced when node 333 landed two new handover parts:

> the **sixth** on the four kinds whose handover has five parts, the **seventh** on an implementation node, whose handover has six. Corrected at node 114's check, having said `sixth` for every kind; the superseded wording is in [map-history.md](map-history.md).

## Superseded from `map-manager-only.md` at node 336 — the gate payload's command that shows the diff

*Moved verbatim under the `Change the map` procedure at [Carry the rules on what reaches the human, the code-slot
count and the gate's pointer to the work into the manager
contract](nodes/336-carry-the-rules-on-what-reaches-the-human-the-code.md), carrying out [A gate payload stops
carrying a command that prints a diff](nodes/231-a-gate-payload-stops-carrying-a-diff-command.md), on the human's
instruction that the diff command is not useful to them. The sentence stated a rule that currently bound, so it took
this route rather than strike-in-place, on [Where the never-delete rule
stops](nodes/189-where-the-never-delete-rule-stops.md)'s test. What replaces it names the worktree's path and no
command, and keeps the ground it gives. The rest of the paragraph it sat in is unchanged and is not reproduced here.*

### From *Landing an implementation node's work* — the gate payload's sentence

*Replaced, and it stood as:*

**The gate payload names the worktree's path and the command that shows its diff**, because an implementation node's work is uncommitted in a checkout outside the repository and `git diff` where the human is standing does not show it — their words on being handed a gate without it: *"what are the changes ? I don't see them in git ?"*.


### From *Notes* — the retrospective bullet's filing sentence

*Replaced 2026-09-27 on the human's "ok for A": node 340 defined an annotation in `graph-conventions.md` as what a later piece of work changed about a node's answer, headed `## Annotation[: …]`, which a retrospective is not. What replaces it files the retrospective as its own `## Retrospective` section, placed last. The rest of the bullet is unchanged and is not reproduced here.*

*Replaced, and it stood as:*

**The worker hands it back as text and the manager files it** as a `## Retrospective` annotation on the node, which keeps the mandatory section order untouched.


### From *Notes* — two bullets that named the retired "pick report"

*Replaced 2026-09-27: [node 137](nodes/137-rename-the-two-reports-and-repair-the-avoid-line.md) (`fe2610b`) retired "pick report" for "node closing report"; node 344's worker reported that these bullets still used it. Only the term changed. They stood as:*

- **Approving a node's end settles that node's flags.** The human's standing instruction, `verbatim`: *"Also, when I approve the end of the node, the flags should be considered ok"*. So the manager does not ask a second time. **The settling moment is the first human moment the node's close reaches** — an implementation node's **gate** where it has one, and otherwise the **pick report** that closes the node — fixed at [A node's flags arrive after the human moment that was supposed to settle them](nodes/99-flags-arrive-after-the-node-s-human-moment.md) and widened to every kind of node, `prototype` and AFK kinds included, at [Whether a research node's and an AFK precondition node's flags settle at the pick report too](nodes/102-do-afk-nodes-flags-settle-at-the-pick-report.md), and refining the practice on [Whether flags.md survives the settle-at-close practice](nodes/27-does-flags-file-survive.md). The close is the earliest moment that works: a node's flags do not exist until its worker hands them back, which is after every exchange that node had with the human. **The pick report awaits no answer**, so the settlement rides whatever the human says next, whatever that next thing is about; where they never speak again nothing settles and those flags reach the closing report, and the manager never settles a flag on its own judgement or on the passage of time. **The consequence the manager must carry:** every report that closes a node — a gate payload, or a pick report — presents every flag that node holds, in the fuller form a gate payload uses, because a report that omits one settles it silently. The superseded wording is in [map-history.md](map-history.md).
- **A standing yes is in force: every gate is approved on the checker's `PASS`.** The human invoked `/expedition-standing-yes` on 2026-09-27, `verbatim`: *"Let's try it out. Approve all gates automatically"*. Scope text: *"Approve all gates automatically"*. It covers gates only, not workers' questions or raises, and never what the skill excludes (a `FAIL`, a checker's raise or question, a gate whose check will not pass, an uncovered owed part, a reject, a condition judged wrong). Each gate taken under it is recorded on its node's `## Review` marked `standing yes`, and the node's flags settle at the pick report that closes it. It stays in force until the human changes it.

## Superseded from `map-implementation-rules.md` at node 346 — the clause that no sweep of the file is licensed

*Moved verbatim under the `Change the map` procedure at [Allow a sweep of a map file, in
`graph-conventions.md`](nodes/346-allow-a-sweep-of-a-map-file-in-graph-conventions-md.md), carrying out [node
345](nodes/345-workers-report-most-of-map-md-bore-on-nothing.md)'s answer on the human's "ok for recommended". What
replaces it says no sweep of the file is owed and one is allowed. The rest of the paragraph it sat in is unchanged and
is not reproduced here.*

### From the file's opening, *What this file admits* — the sentence on who applies the test

*Replaced, and it stood as:*

**Whoever is already editing a passage applies this to that
passage**, and no sweep of the file is owed or licensed by it. Settled at [node
191](nodes/191-the-rules-file-carries-accounts-rather-than-rules.md).

## Superseded from `map.md`'s `## Notes` at node 345 — the accounts moved out of the items that stay, and two items reworded after moving

*Moved verbatim under the `Change the map` procedure by the manager's pass carrying out [node 345](nodes/345-workers-report-most-of-map-md-bore-on-nothing.md)'s answer, point 2, on the human's "ok for recommended". Each item below stood in `map.md` as quoted and was replaced by a shorter current statement. The items that moved whole to [map-manager-only.md](map-manager-only.md) and [map-implementation-rules.md](map-implementation-rules.md) are not quoted here unless they were then reworded: they stand verbatim in those files, which are part of the map and not history.*

### From *Notes* — the standing preference that the shipped files should not depend on the `mattpocock-skills` plugin

*Replaced, and it stood as:*

- **The shipped files should not depend on the `mattpocock-skills` plugin.** The human's standing direction, `verbatim`: *"I also would want the skill to not depend on mattpockock, I don't know what is the status of this. Add grilling directly on the skill and for the docs part we should make something. Inspired by "/domain-modeling" and https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"*. It goes further than ground rule 2, which requires only that each contract **stand alone as a file rather than depend on a skill being invocable**: this asks that the dependency not exist. **What it reaches, which is more than the contracts:** the `Skills every session should consult` line above, and **ground rule 5**, which locates `/writing-for-agents` in that plugin by name and against which every prose deliverable on this effort is held. **In force on this effort from now**, under [Rules added to one effort's map, and what makes them legitimate](nodes/93-effort-scoped-custom-rules.md). **What it does not do is settle the two open questions it lands on**, and the manager has changed neither: what happens to the contracts' invoke-a-skill line is [Whether the contracts' instruction to invoke a method skill is doing any work](nodes/113-whether-the-method-skill-instruction-does-any-work.md), whose first question was already in front of the human when this arrived, and what the workflow ships in place of `/domain-modeling` is [The docs discipline this workflow ships instead of depending on one](nodes/130-the-docs-discipline-this-workflow-ships.md).

### From *Notes* — the standing direction that a checker's rules are given to it, never found by it

*Replaced, and it stood as:*

- **The rules a checker holds work against are given to it, never found by it — and the implementer is held against the same ones.** The human's standing direction, `verbatim`: *"Also I don't know if I have talked about it but in the checker, it shouldn't try to find the skill/rules, they should be at the map level and sent by the manager or just read by the checker. I don't know if it is still the case but we shouldn't use matt pockock skills code review skill as it is too generic. (it is easier to change the rule when its in a file than when the checker finds stuff by itself. The rules should also be used by the implementer"*. **Their stated ground is changeability**: a rule written in a file can be edited, where a rule a checker discovers for itself cannot. **In force on this effort from now**, under [Rules added to one effort's map, and what makes them legitimate](nodes/93-effort-scoped-custom-rules.md). **What it reaches, and it is more than one file:** the checker's contract, which today tells a checker to *find* a reviewing skill before it reads the work and to hold the work against whatever rules it found; the review route recorded for this repo, whose naming of a reviewing skill is superseded by it; **ground rule 5**, which locates `/writing-for-agents` in a plugin by name; and the implementation contract, which is held against the bar rather than against a named rule set. **What it does not settle, and the manager has decided none of it:** where the rules live now that they are not discovered, what a checker is given in place of a reviewing skill's procedure, and whether the implementer receives the same text or a pointer to it.

### From *Notes* — the standing instruction that nodes are grouped by file

*Replaced, and it stood as:*

- **Nodes are grouped by file, and a related defect goes into a node that already exists.** The human's standing instruction, given 2026-09-26 after the manager agreed that nodes changing a few lines each cost more in overhead than in work, `verbatim`: *"You can do the groups. To avoid the issue, maybe we can make so that if it is related, put the defect in an already existing node ?"* The groups are the manager's proposal they accepted: open nodes against the same file are merged into one node whose condition carries the clauses of the nodes it replaces, and conflicts between those clauses go to the human. *The manager's reading of the second sentence:* where a worker surfaces a defect related to an open, unclaimed node, the defect is added to that node's condition as an amendment rather than minted as a new node. Shipping that rule into the contracts is [node 327](nodes/327-a-related-defect-joins-an-open-node-instead-of-becoming-a-new-one.md). Moments later, `verbatim`: *"I think we shouldn't be too afraid of updating a node before it is started"*. *The manager's reading:* a node that is open and unclaimed may have its condition amended, by the manager or from a worker's report, without a separate question to the human first; the amendment is recorded as one, with a flag that settles at the node's gate, and a claimed node's condition stays as written. Node 327 carries this too.

### From *Notes* — the standing instruction that a decision of the human's own may be proposed for change

*Replaced, and it stood as:*

- **A decision of the human's own may be proposed for change, on the same footing as one the workflow made.** Their standing instruction, `verbatim`, given after the manager told them the opposite: *"You can offer to change a rule I made, the rules I choose where because I though they where the best at the point they where chosen, but in the spirit of this skill, as we make stuff, we discover stuff and that can make us decide an earlier desision was wrong"*. **What it corrects** is the manager's own statement that a rule the workflow wrote may be proposed for change while a rule of theirs could only be asked about — a distinction they do not hold and which would have made a worker soften a recommendation against one of their decisions. **What it does not license:** a worker still never changes a settled decision itself, and the proposal reaches them as a question with its ground stated. What changes is that *whose decision it was* is not a reason to weaken the proposal, and that discovery falsifying an earlier choice is the expected case rather than an awkward one. **This is the ground the never-delete rule's own authorship was corrected on**, that rule being the workflow's and approved by them rather than theirs, recorded at [node 189](nodes/189-where-the-never-delete-rule-stops.md).

### From *Notes* — the standing instruction that a condition forcing a contradiction is a raise

*Replaced, and it stood as:*

- **Where an agent sees that its acceptance condition forces a contradiction, that is a raise and not a flag.** The
human's standing instruction, `verbatim`, given at [node
200](nodes/200-collapse-the-rules-files-two-map-history-statements.md)'s gate after both that node's worker and its
checker had reported the same collision and neither had raised it: *"If both the checker and implementer knew it, I
would have expeted a raise at least."* **What it corrects** is two agents' reading of their own contracts as
licensing a decide-and-flag where the thing decided was that a clause of the condition cannot be honoured together
with a standard the work is held against. The worker's own words were *"Decided rather than raised: the condition is
satisfiable either way and the cost of the wrong choice is one sentence"*, and the checker's were that the wording
*"was not the worker's to depart from, which is why this is a question and not a finding against the work"* — both
correct about their own authority and both stopping short of the one route that would have reached the human before
the work was done. **What it does not license:** a raise on any hard clause, or a worker stopping because a
condition is inconvenient; the trigger is a contradiction the agent can name between the condition and something
the work is measured against. **In force on this effort from now**, and its carriage into the shipped contracts is
[node 214](nodes/214-a-condition-that-contradicts-a-standard-is-a-raise.md).

### From *Notes* — the note on the workflow's name and vocabulary

*Replaced, and it stood as:*

**The workflow is named `/expedition`, and its vocabulary is fixed**, by [Naming](nodes/14-naming.md). The metaphor stops at the map: the product and one run of it are cartographic, and every actor and mechanism underneath is described plainly — **manager**, **worker**, **checker**, **gate**, **node**. [`CONTEXT.md`](../../CONTEXT.md) holds ~~**50 term entries and 40 `_Avoid_` lines**, measured at [What keeps the shipped files consistent when a decision changes a term](nodes/29-shipped-file-consistency.md)~~ **51 term entries and 41 `_Avoid_` lines, counted 2026-09-10** by [node 224](nodes/224-the-glossary-says-the-map-is-read-once-per-session.md)'s worker and independently by its checker — **the node-29 figures were already wrong before that node's own edit, which added neither an entry nor an `_Avoid_` line.** Dated and non-authoritative under [node 183](nodes/183-nothing-measures-the-record-about-itself.md): re-derive rather than trust it, and the refusals are the part that does the work: `postpone`, `provenance`, `write lock`, `done`, `issue`, `ticket` and `task` are refused by name. ~~That file is **moving** into `.claude/skills/expedition/CONTEXT.md`, with a `CONTEXT-MAP.md` at the root and the root path left resolving as a forward pointer~~ **That file is still at the root.** ~~**Where it moves and what it is called are open at [Ship the glossary inside the skill directory and make it state its own completeness](nodes/56-ship-the-glossary-into-the-skill-set.md), where the human's direction is to rename it; struck after node 294's worker reported the old wording stale**~~ **[Ship the glossary inside the skill directory and make it state its own completeness](nodes/56-ship-the-glossary-into-the-skill-set.md) moves it to `.claude/skills/expedition/glossary.md`, the name the human chose on 2026-09-25; the moving line before it was struck after node 294's worker reported it stale** — because a glossary the shipped files declare authoritative and which does not travel with them is a defect. **Prose written before a word changed still says the old word: that is the never-delete rule rather than drift, and the glossary is authoritative.**

### From *Notes* — the standing preference that the manager never idles, reworded in `map-manager-only.md` at node 256

*Replaced, and it stood as:*

- **The manager never idles, and *starts* the next work itself the moment a node finishes.** Two standing instructions of the human's, the second strengthening the first. `verbatim`: *"You can start new tasks. You should automatically propose to start a new task when a task finish"*, and then *"Also the manager should proactively start new nodes when one has finished"*. **Proposing is not enough**: the manager picks, spawns the worker, and reports the pick as work already under way. That report awaits no answer and takes no place in the human's queue, and their redirection of a pick is a correction after the fact rather than a permission that was waited for. What bounds how much is started is two counts, each a setting of this effort: the code-slot count for implementation nodes, and the target for concurrently running nodes that need the human, in the bullet below. Filed here under the rule [What the manager works on next, and how the human redirects it](nodes/16-human-steering.md) fixed for standing instructions, and **shipped** into the manager's contract by [The manager starts the next node rather than proposing it](nodes/100-the-manager-starts-the-next-node-rather-than-proposing-it.md), landed as commit `47703bb`. Earlier wordings are in [map-history.md](map-history.md).

### From *Notes* — the standing preference that a payload goes over as soon as it is ready, reworded in `map-manager-only.md` at node 256

*Replaced, and it stood as:*

- **A payload goes over as soon as it is ready, and still one at a time.** The human's instruction, `verbatim`,
after the manager had sat on three finished payloads while waiting to be asked for each: *"Stop waiting for me to
ask to give the questions"*. **The manager then over-read it and sent all three at once**, and was corrected,
`verbatim`: *"Why did you give everything ?"* — so the one-question rule above is untouched and what was wrong was
never the count. **What was wrong was the trigger.** The manager had been treating *the human answering* as what
released the next payload, so a finished payload could wait through two landings before reaching them. **The
trigger is the payload being ready**, and the count stays one.

## Superseded from `map-manager-only.md`'s `## Not yet specified` at node 80 — the firstmate upgrade list naming worktrees

*Moved verbatim under the `Change the map` procedure by the same pass, carrying out [node 80](nodes/80-map-items-nodes-64-and-68-left-stale.md)'s clause 2.*

- **Whether the Claude Code subagent runtime proves too simple**, and the upgrade path to a firstmate shape — real sessions, worktrees, file mailboxes — if it does. Three ways it could be: node count at the dogfood's 179, an unknown stack, and — economic rather than technical — running a node on a model of the manager's choosing. What would settle it: a dogfood run carrying back the friction record and a **measured spend per node type**. The evidence so far indicts none of the three: the weak point is the long-lived manager thread rather than the fleet under it, per [friction from running this map by hand](nodes/24-self-hosted-friction.md). Parked here at the human's word: what model the manager itself needs, and where a kind-to-model mapping lives. Adjacent: [whether the AFK passes move to the dynamic-workflow runtime](nodes/62-afk-passes-on-the-workflow-runtime.md).

## Superseded from `map-implementation-rules.md` at node 347 — the sentence that named a pass over the file a sweep

*Moved verbatim under the `Change the map` procedure at [Rename "sweep of a file" to a word the glossary does not
own](nodes/347-rename-sweep-of-a-file-to-a-word-the-glossary-does-not-own.md), carrying out the human's "ok" to the
manager's recommendation at node 346's gate. The glossary's **Sweep** is the whole-graph pass, so what replaces it
calls a pass over one map file under the admission test a pass over the whole file. The rest of the paragraph it sat
in is unchanged and is not reproduced here.*

### From the file's opening, *What this file admits* — the sentence on who applies the test

*Replaced, and it stood as:*

**Whoever is already editing a passage applies this to that
passage**. No sweep of the file is owed, and one is allowed. Settled at [node
191](nodes/191-the-rules-file-carries-accounts-rather-than-rules.md), and the sweep allowed at [node
346](nodes/346-allow-a-sweep-of-a-map-file-in-graph-conventions-md.md).

## Superseded from `map.md` and `map-implementation-rules.md` at node 348 — the ground rules placed in the rules file

*Moved verbatim under the `Change the map` procedure at [Keep the ground rules in `map.md` and strike the sibling-file allowance](nodes/348-keep-the-ground-rules-in-map-md-and-strike-the-sibling-file-allowance.md), carrying out [node 168](nodes/168-where-a-non-implementation-worker-gets-the-ground-rules.md)'s answer: the effort's ground rules sit in `map.md`'s `## Notes`, which every worker reads, and in no sibling file of the map. The ground-rules block itself moved back from `map-implementation-rules.md` to `map.md` unchanged, so it is not appended. Each sentence below is shown alone, the rest of its paragraph being unchanged.*

### From `map.md`'s `## Notes` — the pointer to the ground rules in the rules file

*Removed, the block it pointed at standing in its place, and it stood as:*

**Ground rules for this effort, now in [map-implementation-rules.md](map-implementation-rules.md)**: five numbered rules of scope, and the test a rule passes to join them — moved there by [node 144](nodes/144-make-the-rules-file-stand-alone.md) so that file stands alone for a reader who does not read this map.

### From `map.md`'s `## Notes` — the pointer to the five standing rules for writing

*Replaced, the word "too" having leaned on the pointer above, and it stood as:*

**The five standing rules for writing anything in this effort are in [map-implementation-rules.md](map-implementation-rules.md)** too, held against every prose deliverable and fixed by [node 53](nodes/53-what-token-findings-change.md) and, for the fifth, [node 289](nodes/289-a-plain-english-and-compaction-pass-over-the-shipped-files.md) — moved by [node 144](nodes/144-make-the-rules-file-stand-alone.md).

### From `map-implementation-rules.md`'s `## What the work is held against` — the bar's list of its non-command half

*Replaced, and it stood as:*

So the bar here is entirely its non-command half: the project criteria (the human's global coding principles and `/naming`), ~~this map's own standing preferences~~ **this effort's ground rules and its five standing rules for writing, the two blocks this file holds below — `map.md`'s standing preferences are not part of the bar, on [node 42](nodes/42-checker-spawn-carries-ground-rules.md)'s test as the review route below states**, `CONTEXT.md`'s `_Avoid_` lines, [`graph-conventions.md`](../../.claude/skills/expedition/graph-conventions.md), `/writing-for-agents`, and the node's acceptance condition — the last two added at [node 184](nodes/184-the-bar-and-the-standards-are-two-different-lists.md).

### From `map-implementation-rules.md`'s `## What the work is held against` — the review route's list of the standards

*Replaced, and it stood as:*

**The standards to hold work against:** `/coding-principles` and `/naming`; [`CONTEXT.md`](../../CONTEXT.md)'s `_Avoid_` lines; ~~this map's standing preferences, ground rules and four standing rules~~ **this effort's ground rules and its five standing rules for writing, both of which this file holds below**; [`graph-conventions.md`](../../.claude/skills/expedition/graph-conventions.md); and `/writing-for-agents`, which is the standard that bites on prose deliverables and which `/coding-principles` barely touches.

### From `map-implementation-rules.md`'s `## What the work is held against` — the two blocks that pass node 42's test

*Replaced, and it stood as:*

That test is [node 42](nodes/42-checker-spawn-carries-ground-rules.md)'s; the **ground rules** and the **five standing rules for writing**, both held below in this file, are the two blocks that pass it, and the struck wording named the preferences alongside them — a defect from node 42 onward, found at [node 138](nodes/138-where-the-rules-a-checker-is-held-to-live.md) and carried out here.

### From `map-implementation-rules.md`'s `## What the work is held against` — the five standing rules for writing, set against the ground rules

*Replaced, and it stood as:*

They are rules of writing, where the ground rules above are rules of scope.

### From `map.md`'s `## Notes` — the glossary's location, superseded when node 56 landed, 2026-09-27

*Replaced, and it stood as:*

**Skills every session should consult:** `/grilling` and `/domain-modeling` by default, `/naming` for terminology, `/coding-principles` before writing code, `/prototype` for prototype nodes. **Plus one file, not a skill:** [`CONTEXT.md`](../../CONTEXT.md) at the repo root is the glossary, and reading it is a precondition for writing anything — its `_Avoid_` lines are what stop a settled term from drifting back.

**The workflow is named `/expedition`, and its vocabulary is fixed**, by [Naming](nodes/14-naming.md). The metaphor stops at the map: the product and one run of it are cartographic, and every actor and mechanism underneath is described plainly — **manager**, **worker**, **checker**, **gate**, **node**. [`CONTEXT.md`](../../CONTEXT.md) holds **51 term entries and 41 `_Avoid_` lines, counted 2026-09-10** by [node 224](nodes/224-the-glossary-says-the-map-is-read-once-per-session.md)'s worker and independently by its checker. Dated and non-authoritative under [node 183](nodes/183-nothing-measures-the-record-about-itself.md): re-derive rather than trust it, and the refusals are the part that does the work: `postpone`, `provenance`, `write lock`, `done`, `issue`, `ticket` and `task` are refused by name. **That file is still at the root.** [Ship the glossary inside the skill directory and make it state its own completeness](nodes/56-ship-the-glossary-into-the-skill-set.md) moves it to `.claude/skills/expedition/glossary.md`, the name the human chose on 2026-09-25, because a glossary the shipped files declare authoritative and which does not travel with them is a defect. **Prose written before a word changed still says the old word: that is the never-delete rule rather than drift, and the glossary is authoritative.** The earlier counts and wordings are in [map-history.md](map-history.md).

## Superseded from `map-manager-only.md` at node 160 — the rebase conflict aborted, the record committed by the human, and node 160 named as open

*Replaced under the `Change the map` procedure at [node 160](nodes/160-carry-the-integration-conflict-rule-into-the-map.md), which carried [node 115](nodes/115-two-writers-edit-the-map-at-once.md)'s integration-conflict rule and the record commits of [node 176](nodes/176-the-managers-record-edits-collide-with-a-landing.md) and [node 266](nodes/266-a-worker-cannot-see-the-record-the-manager-has-not-committed.md) into the map.*

### From *Landing an implementation node's work* — the landing policy's sentence on a rebase conflict

*Replaced, and it stood as:*

**A rebase conflict is resolved by nobody in the moment**: the manager runs `git rebase --abort` and the node takes a correction round with the worker respawned.

### From *Landing an implementation node's work* — the landing policy's sentence on committing the graph's own files

*Replaced, and it stood as:*

The graph's own files are *not* committed per node; they are committed periodically by the human, which is safe only because node files are append-only.

### From *Landing an implementation node's work* — the code-slot paragraph's sentence naming node 160 as open

*Replaced, and it stood as:*

**What the manager carries with the second slot** is that two implementation workers may hold two worktrees over the same shipped file, so it picks nodes whose paths are disjoint; the integration-conflict question that raises is [node 115](nodes/115-two-writers-edit-the-map-at-once.md)'s, still open at [node 160](nodes/160-carry-the-integration-conflict-rule-into-the-map.md) and [node 162](nodes/162-how-much-of-the-integration-rule-ships.md).

## Superseded from `map.md` and `map-implementation-rules.md` at node 352 — the five standing rules for writing placed in the rules file

*Moved verbatim under the `Change the map` procedure at [Move the five standing rules for writing into `map.md`'s ground-rules block](nodes/352-move-the-five-standing-rules-for-writing-into-the-ground-rules-block.md), carrying out [node 349](nodes/349-whether-the-five-standing-rules-for-writing-reach-other-workers.md)'s answer: the five standing rules for writing sit inside the ground-rules block in `map.md`'s `## Notes`, which every worker reads and which the manager copies into every checker spawn. The five numbered rules themselves moved unchanged, and are appended below with the paragraph that introduced them. Each sentence shown alone is shown without the rest of its paragraph, which is unchanged.*

### From `map.md`'s `## Notes` — the paragraph that followed the ground rules

*Replaced, its claim that every rule above is drawn from a standing preference not being true of the rules for writing, and it stood as:*

Every rule above is drawn from a standing preference, and every one passes the test [The checker's spawn carries the effort's ground rules](nodes/42-checker-spawn-carries-ground-rules.md) shipped for what may travel to a blind checker: **a standing constraint true of any node's work, rather than an account of what happened.** That test is what keeps the rest of this file out of the block, and the block is appended to like any other part of this map.

### From `map.md`'s `## Notes` — the pointer to the five standing rules for writing

*Removed, the list it pointed at standing inside the ground-rules block in its place, and it stood as:*

**The five standing rules for writing anything in this effort are in [map-implementation-rules.md](map-implementation-rules.md)**, held against every prose deliverable and fixed by [node 53](nodes/53-what-token-findings-change.md) and, for the fifth, [node 289](nodes/289-a-plain-english-and-compaction-pass-over-the-shipped-files.md) — moved by [node 144](nodes/144-make-the-rules-file-stand-alone.md).

### From `map-implementation-rules.md`'s `## What the work is held against` — the bar's list of its non-command half

*Replaced, and it stood as:*

So the bar here is entirely its non-command half: the project criteria (the human's global coding principles and `/naming`); this effort's ground rules, which [`map.md`](map.md) holds in its `## Notes` and which a checker receives as text in its spawn; this effort's five standing rules for writing, which this file holds below; `CONTEXT.md`'s `_Avoid_` lines; [`graph-conventions.md`](../../.claude/skills/expedition/graph-conventions.md); `/writing-for-agents`; and the node's acceptance condition — the last two added at [node 184](nodes/184-the-bar-and-the-standards-are-two-different-lists.md).

### From `map-implementation-rules.md`'s `## What the work is held against` — the review route's list of the standards

*Replaced, and it stood as:*

**The standards to hold work against:** `/coding-principles` and `/naming`; [`CONTEXT.md`](../../CONTEXT.md)'s `_Avoid_` lines; this effort's ground rules, which [`map.md`](map.md) holds in its `## Notes` and which a checker receives as text in its spawn, placed there at [node 348](nodes/348-keep-the-ground-rules-in-map-md-and-strike-the-sibling-file-allowance.md); this effort's five standing rules for writing, which this file holds below; [`graph-conventions.md`](../../.claude/skills/expedition/graph-conventions.md); and `/writing-for-agents`, which is the standard that bites on prose deliverables and which `/coding-principles` barely touches.

### From `map-implementation-rules.md`'s `## What the work is held against` — the two blocks that pass node 42's test

*Replaced, and it stood as:*

That test is [node 42](nodes/42-checker-spawn-carries-ground-rules.md)'s; the **ground rules**, held in `map.md`, and the **five standing rules for writing**, held below in this file, are the two blocks that pass it.

### From `map-implementation-rules.md`'s `## What the work is held against` — the five standing rules for writing

*Removed, the list now standing inside the ground-rules block in `map.md`'s `## Notes`, and it stood as:*

**Five standing rules for writing anything in this effort**, the first four fixed by [What the token findings change in the workflow and its skills](nodes/53-what-token-findings-change.md) and the fifth by [node 289](nodes/289-a-plain-english-and-compaction-pass-over-the-shipped-files.md) and held against every prose deliverable. They are rules of writing, where this effort's ground rules, held in [`map.md`](map.md)'s `## Notes`, are rules of scope.

1. **Compress the prose that explains why; never compress the shapes.**
2. **An item states its current form and cites the nodes that shaped it; it does not restate what they hold.**
3. **A long answer is navigable by heading**, so a reader following a link for one fact reads one section.
4. **Cite a file by heading or by a quoted phrase, never by line number.** Append-in-place shifts every line below the append, so a line number decays without anything reporting it.
5. **Write plain English.** State a rule as what to do; use a prohibition only where the rule cannot be said as what to do, and then beside the positive. Bold a term only where it is defined. Say any idea that is not a term defined in `CONTEXT.md` in plain words, with no figure of speech and no coined phrase. Make statements directly rather than as slogan-shaped contrasts. Write every sentence grammatically, with one clear referent for each pronoun. Put one idea in each sentence.

### The glossary's old name, superseded in `map.md` and `map-implementation-rules.md` after node 352 landed, 2026-09-28

*The manager's own change, approved with node 352's gate. [Node 56](nodes/56-ship-the-glossary-into-the-skill-set.md) moved the glossary to `.claude/skills/expedition/glossary.md`. Replaced, and each line stood as:*

**In `map.md`:**

5. **Write plain English.** State a rule as what to do; use a prohibition only where the rule cannot be said as what to do, and then beside the positive. Bold a term only where it is defined. Say any idea that is not a term defined in `CONTEXT.md` in plain words, with no figure of speech and no coined phrase. Make statements directly rather than as slogan-shaped contrasts. Write every sentence grammatically, with one clear referent for each pronoun. Put one idea in each sentence.

**In `map-implementation-rules.md`:**

**The bar's commands for this repo, discovered on first use** and recorded here so no later node re-derives them, per [Done-ness and termination](nodes/10-done-ness.md). `graph-agent` has **no build, no tests, no formatter and no CI** — no manifest, no task runner, nothing to invoke; the one ignore file, `.gitignore`, ~~ignores `.worktrees/`~~ **ignores `.worktrees/` and `.claude/worktrees/`, the second added at [node 158](nodes/158-ignore-the-harness-worktree-directory.md)** **and `.scratch/graph-workflow/worktrees/`, the current path, whose absence here node 297's worker reported** and invokes nothing. Corrected at node 114's check, having claimed no ignore file after one was added by the landing policy; the superseded wording is in [map-history.md](map-history.md). So the bar here is entirely its non-command half: the project criteria (the human's global coding principles and `/naming`); this effort's ground rules, which [`map.md`](map.md) holds in its `## Notes` and which a checker receives as text in its spawn; this effort's five standing rules for writing, which [`map.md`](map.md)'s `## Notes` holds inside the ground-rules block and which a checker receives as text in its spawn with the ground rules; `CONTEXT.md`'s `_Avoid_` lines; [`graph-conventions.md`](../../.claude/skills/expedition/graph-conventions.md); `/writing-for-agents`; and the node's acceptance condition — the last two added at [node 184](nodes/184-the-bar-and-the-standards-are-two-different-lists.md). `map.md`'s standing preferences are not part of the bar, on [node 42](nodes/42-checker-spawn-carries-ground-rules.md)'s test as the review route below states. **The two enumerations in this section are one set of standards and not two**: this half is what an implementation node's worker writes to, and the review route's *"standards to hold work against"* below is what its checker holds the finished work against. The *"human's global coding principles"* here is `/coding-principles` there, and the one this half adds is the **node's acceptance condition**, which reaches a checker by its own route. Under the *"if relevant"* clause that is a **complete** bar rather than a deficient one — the same shape the dogfood target has, one step thinner. First discovered and used by [Write the graph conventions document](nodes/21-conventions-document.md).

**In `map-implementation-rules.md`:**

**The review route for this repo, discovered on first use** and recorded here so no later checker re-derives it, on the same ground as the bar's commands above. Two checker runs spent their largest single cost finding this, and one of them nearly reported the prose standard absent. **The standards to hold work against:** `/coding-principles` and `/naming`; [`CONTEXT.md`](../../CONTEXT.md)'s `_Avoid_` lines; this effort's ground rules, which [`map.md`](map.md) holds in its `## Notes` and which a checker receives as text in its spawn, placed there at [node 348](nodes/348-keep-the-ground-rules-in-map-md-and-strike-the-sibling-file-allowance.md); this effort's five standing rules for writing, which [`map.md`](map.md)'s `## Notes` holds inside the ground-rules block and which a checker receives as text in its spawn with the ground rules; [`graph-conventions.md`](../../.claude/skills/expedition/graph-conventions.md); and `/writing-for-agents`, which is the standard that bites on prose deliverables and which `/coding-principles` barely touches. **`map.md`'s standing preferences are not among the standards, as a whole.** A standing preference may be an account of what happened or a steer about what gets worked, and only a standing constraint true of any node's work may be held against a piece of work by a reader blind to the record. That test is [node 42](nodes/42-checker-spawn-carries-ground-rules.md)'s; the **ground rules** and the **five standing rules for writing**, both held in `map.md`'s `## Notes` inside the ground-rules block and received by a checker as text in its spawn, are the two blocks that pass it. **No reviewing skill is named for this repo, and a checker does not go looking for one.** The standards above are the whole of what work is held against, and they reach a checker as text rather than as something it discovers — the human's standing direction below. The superseded naming of `mattpocock-skills:code-review`, and the account of how much of it could run, are in [map-history.md](map-history.md). **One trap, measured:** `CONTEXT.md`'s refused words are largely unusable as a grep list, about a third being ordinary English refused only for one concept — `report`, `run`, `session`, `index`, `plan`, `item` and `question` — so a scan for them returns false positives and the distinctive refusals are checked by hand instead. **`where` was on this list and is not refused by any `_Avoid_` line**, found at node 114's check; the superseded wording is in [map-history.md](map-history.md).

## Superseded from `map.md` and `map-implementation-rules.md` at node 354 — the standing rules for writing counted as five

*Replaced under the `Change the map` procedure at [Add the sixth standing rule for writing: point at a heading of a file the reader already reads](nodes/354-add-the-sixth-standing-rule-for-writing.md), which adds [node 253](nodes/253-a-shipped-file-points-at-a-sibling-rather-than-restating-it.md)'s rule as the sixth standing rule for writing. Rules 1 to 5 are unchanged. Each sentence shown alone is shown without the rest of its paragraph, which is unchanged.*

### From `map.md`'s `## Notes` — the lead-in to the standing rules for writing

*Replaced, naming node 253 as the node that fixed the sixth rule, and it stood as:*

**This effort's standing rules for writing**, held against every prose deliverable. The first four were fixed by [node 53](nodes/53-what-token-findings-change.md) and the fifth by [node 289](nodes/289-a-plain-english-and-compaction-pass-over-the-shipped-files.md).

### From `map-implementation-rules.md`'s `## What the work is held against` — the bar's list of its non-command half

*Replaced, counting six rules, and the sentence stood as:*

So the bar here is entirely its non-command half: the project criteria (the human's global coding principles and `/naming`); this effort's ground rules, which [`map.md`](map.md) holds in its `## Notes` and which a checker receives as text in its spawn; this effort's five standing rules for writing, which [`map.md`](map.md)'s `## Notes` holds inside the ground-rules block and which a checker receives as text in its spawn with the ground rules; `glossary.md`'s `_Avoid_` lines; [`graph-conventions.md`](../../.claude/skills/expedition/graph-conventions.md); `/writing-for-agents`; and the node's acceptance condition — the last two added at [node 184](nodes/184-the-bar-and-the-standards-are-two-different-lists.md).

### From `map-implementation-rules.md`'s `## What the work is held against` — the review route's list of the standards

*Replaced, counting six rules, and the sentence stood as:*

**The standards to hold work against:** `/coding-principles` and `/naming`; [`glossary.md`](../../.claude/skills/expedition/glossary.md)'s `_Avoid_` lines; this effort's ground rules, which [`map.md`](map.md) holds in its `## Notes` and which a checker receives as text in its spawn, placed there at [node 348](nodes/348-keep-the-ground-rules-in-map-md-and-strike-the-sibling-file-allowance.md); this effort's five standing rules for writing, which [`map.md`](map.md)'s `## Notes` holds inside the ground-rules block and which a checker receives as text in its spawn with the ground rules; [`graph-conventions.md`](../../.claude/skills/expedition/graph-conventions.md); and `/writing-for-agents`, which is the standard that bites on prose deliverables and which `/coding-principles` barely touches.

### From `map-implementation-rules.md`'s `## What the work is held against` — the two blocks that pass node 42's test

*Replaced, counting six rules, and the sentence stood as:*

That test is [node 42](nodes/42-checker-spawn-carries-ground-rules.md)'s; the **ground rules** and the **five standing rules for writing**, both held in `map.md`'s `## Notes` inside the ground-rules block and received by a checker as text in its spawn, are the two blocks that pass it.

### From `map-manager-only.md`'s *Landing an implementation node's work* — the code-slot paragraph, superseded when node 162 resolved, 2026-09-28

*The manager's own change. Replaced, and the paragraph stood as:*

**How many implementation workers run at once is a setting of the effort, and for this effort it is two**, raised from one by the human while directing the manager at the shipping backlog, `verbatim`: *"should we do 2 implementer and 2 grilling to go through the shipping backlog ?"*. **What the manager carries with the second slot** is that two implementation workers may hold two worktrees over the same shipped file, so it picks nodes whose paths are disjoint; the integration conflicts that raises are resolved as the landing policy above states, settled at [node 115](nodes/115-two-writers-edit-the-map-at-once.md) and carried here at [node 160](nodes/160-carry-the-integration-conflict-rule-into-the-map.md), and how much of that rule ships is still open at [node 162](nodes/162-how-much-of-the-integration-rule-ships.md). The superseded sentence is also in [map-history.md](map-history.md). A code slot is therefore a count rather than a property, and raising the count changes a number and no part of the lifecycle above. **A slot's occupancy is discovered by counting the live worktrees** — one per claimed implementation node — rather than by inspecting the working tree for uncommitted changes, so the human's own edits no longer read as an occupied slot. Set at [Run an implementation node's work in a worktree](nodes/68-implementation-in-a-worktree.md). Raising the count buys parallel implementation at the price of integration conflicts. The human sets the count. The manager does not raise it on its own judgement, and does not treat the effort's current value as a ceiling. The human's words, `verbatim`: *"but the framework should allow user to tell the manager to increase parallelization, at the expanse of odds of having to resolve merge conflicts"*. Settled at [node 115](nodes/115-two-writers-edit-the-map-at-once.md).

### From `map-manager-only.md` — the item "When `decisions.md` stops being small enough", superseded at node 358, 2026-09-28

*Replaced, and it stood as:*

- **When `decisions.md` stops being small enough.** The human kept it on every worker's read-whole list, `verbatim`:
  *"it's small enough"*, on the ground that a fed context is used where a search is not. That ground has two halves
  and only one expires: the mechanism does not, but the size claim is about a file that grows by one capped line per
  resolved node and never shrinks. **The anchor is this effort's own precedent — `map.md` was judged to need
  splitting at 43,847 bytes** — and it is node 129's worker's number rather than the human's, flagged at `129.4`.
  What would settle it: `decisions.md` approaching that size, at which point part (ii) of node 129's package is
  re-offered.

## Superseded from `map-manager-only.md` at node 234 — the claim that a merge failed in the sandbox loses nothing

*Replaced under the `Change the map` procedure at [node 234](nodes/234-a-failed-merge-can-leave-the-tree-partially-updated.md), which states that the merge may write some of the changed files before it fails, and states the repair. The two earlier statements of the same claim are already in this file, under Edit 13 and Edit 14 of `## Superseded from map-manager-only.md — the landing section's accounts`. The sentence is shown without the rest of its sub-bullet.*

### From *Landing an implementation node's work* — the sandbox restriction's sub-bullet on what it hits

*Replaced, and it stood as:*

`HEAD` does not move and nothing is lost in either case; both succeed outside the sandbox.

## Not superseded, only narrowed, in `map-manager-only.md` on 2026-09-29 — the resume item

*The manager's note:* the item beginning "**An agent is resumed wherever it can be resumed, a checker and a dead attempt included.**" gained one sentence after "So the manager's default is **resume**, …", narrowing the checker's case to resumes within one node, on the human's words recorded there. No sentence was removed, so no text is banked here.

## Superseded from `map.md` at node 367 — the sixth standing rule for writing, before it said what a pointer may hold

*Replaced under the `Change the map` procedure at [Say in rule 6 what a pointer may hold](nodes/367-say-in-rule-6-what-a-pointer-may-hold.md), which adds two sentences after rule 6's first sentence, carrying [node 361](nodes/361-whether-a-pointer-that-summarises-its-target-restates-it.md)'s ruling. Rules 1 to 5 are unchanged. Of rule 6's four existing sentences, only the second changed, its words "Where the reader is not" becoming "Where the reader is not told to read that file" by the human's decision at the gate.*

### From `map.md`'s `## Notes` — the lead-in to the standing rules for writing

*Replaced, naming node 361 beside node 253 as a node that shaped the sixth rule, and it stood as:*

**This effort's standing rules for writing**, held against every prose deliverable. The first four were fixed by [node 53](nodes/53-what-token-findings-change.md), the fifth by [node 289](nodes/289-a-plain-english-and-compaction-pass-over-the-shipped-files.md) and the sixth by [node 253](nodes/253-a-shipped-file-points-at-a-sibling-rather-than-restating-it.md).

### From `map.md`'s `## Notes` — the sixth standing rule for writing

*Replaced, and it stood as:*

6. **Point at a heading of another shipped file instead of restating what it holds, where the reader is already told to read that file.** Where the reader is not, restate what the reader needs when the file pointed at is mostly text that reader does not need, so the reader is not sent to read it. A passage that changes a rule for its own case names that rule by heading and states the change in its own words. Rename a heading that another shipped file cites only in the change that updates every citation of it, found by searching the shipped files for the heading's exact text.

## Superseded from `map-manager-only.md` at node 80 — the asynchronous-landing item's seam and reject

*Replaced under the `Change the map` procedure at [Update the map items that nodes 64 and 68 left stale](nodes/80-map-items-nodes-64-and-68-left-stale.md), whose condition node 366 replaced. The sentence described the flip to asynchronous landing against a landing policy with no worktree, where approval was one commit and a reject cleaned the working tree. What replaces it describes the flip against the four landing steps and the worktree removal that `## Landing an implementation node's work` now states. The rest of the item is unchanged and is not reproduced here.*

### From `## Not yet specified` — the item beginning "When to flip landing to asynchronous"

*Replaced, and it stood as:*

The seam is one step — the manager committing before the gate rather than after — but one gate outcome does not survive it: **reject** becomes a forward revert rather than a cleaned tree, so the cheapest of the three becomes the most expensive and the only one that marks history.

## Superseded from `map-implementation-rules.md` at node 190 — the standards stated twice, and the struck ignore-file wording

*Replaced under the `Change the map` procedure at [The rules file states one list of standards twice](nodes/190-the-rules-file-states-one-list-twice.md), which states the standards once, as a list under its own lead-in at the head of `## What the work is held against`, and has the bar paragraph and the review route point at it. The bar paragraph's sentence on the ignore file now names `.gitignore`'s three patterns with no struck-through text. The accounts of how each paragraph was learned were left out of the new text, under the file's own *What this file admits*. Both paragraphs are shown whole.*

### From the file's opening, *How a rule in this file is superseded* — the sentence on the struck rule statements below

*Removed, since no struck rule statement remains in the file, and it stood as:*

**The struck rule statements below predate this and are not licence to add another.**

### From `## What the work is held against` — the bar's commands for this repo

*Replaced, and it stood as:*

**The bar's commands for this repo, discovered on first use** and recorded here so no later node re-derives them, per [Done-ness and termination](nodes/10-done-ness.md). `graph-agent` has **no build, no tests, no formatter and no CI** — no manifest, no task runner, nothing to invoke; the one ignore file, `.gitignore`, ~~ignores `.worktrees/`~~ **ignores `.worktrees/` and `.claude/worktrees/`, the second added at [node 158](nodes/158-ignore-the-harness-worktree-directory.md)** **and `.scratch/graph-workflow/worktrees/`, the current path, whose absence here node 297's worker reported** and invokes nothing. Corrected at node 114's check, having claimed no ignore file after one was added by the landing policy; the superseded wording is in [map-history.md](map-history.md). So the bar here is entirely its non-command half: the project criteria (the human's global coding principles and `/naming`); this effort's ground rules, which [`map.md`](map.md) holds in its `## Notes` and which a checker receives as text in its spawn; this effort's six standing rules for writing, which [`map.md`](map.md)'s `## Notes` holds inside the ground-rules block and which a checker receives as text in its spawn with the ground rules; `glossary.md`'s `_Avoid_` lines; [`graph-conventions.md`](../../.claude/skills/expedition/graph-conventions.md); `/writing-for-agents`; and the node's acceptance condition — the last two added at [node 184](nodes/184-the-bar-and-the-standards-are-two-different-lists.md). `map.md`'s standing preferences are not part of the bar, on [node 42](nodes/42-checker-spawn-carries-ground-rules.md)'s test as the review route below states. **The two enumerations in this section are one set of standards and not two**: this half is what an implementation node's worker writes to, and the review route's *"standards to hold work against"* below is what its checker holds the finished work against. The *"human's global coding principles"* here is `/coding-principles` there, and the one this half adds is the **node's acceptance condition**, which reaches a checker by its own route. Under the *"if relevant"* clause that is a **complete** bar rather than a deficient one — the same shape the dogfood target has, one step thinner. First discovered and used by [Write the graph conventions document](nodes/21-conventions-document.md).

### From `## What the work is held against` — the review route for this repo

*Replaced, and it stood as:*

**The review route for this repo, discovered on first use** and recorded here so no later checker re-derives it, on the same ground as the bar's commands above. Two checker runs spent their largest single cost finding this, and one of them nearly reported the prose standard absent. **The standards to hold work against:** `/coding-principles` and `/naming`; [`glossary.md`](../../.claude/skills/expedition/glossary.md)'s `_Avoid_` lines; this effort's ground rules, which [`map.md`](map.md) holds in its `## Notes` and which a checker receives as text in its spawn, placed there at [node 348](nodes/348-keep-the-ground-rules-in-map-md-and-strike-the-sibling-file-allowance.md); this effort's six standing rules for writing, which [`map.md`](map.md)'s `## Notes` holds inside the ground-rules block and which a checker receives as text in its spawn with the ground rules; [`graph-conventions.md`](../../.claude/skills/expedition/graph-conventions.md); and `/writing-for-agents`, which is the standard that bites on prose deliverables and which `/coding-principles` barely touches. **`map.md`'s standing preferences are not among the standards, as a whole.** A standing preference may be an account of what happened or a steer about what gets worked, and only a standing constraint true of any node's work may be held against a piece of work by a reader blind to the record. That test is [node 42](nodes/42-checker-spawn-carries-ground-rules.md)'s; the **ground rules** and the **six standing rules for writing**, both held in `map.md`'s `## Notes` inside the ground-rules block and received by a checker as text in its spawn, are the two blocks that pass it. **No reviewing skill is named for this repo, and a checker does not go looking for one.** The standards above are the whole of what work is held against, and they reach a checker as text rather than as something it discovers — the human's standing direction below. The superseded naming of `mattpocock-skills:code-review`, and the account of how much of it could run, are in [map-history.md](map-history.md). **One trap, measured:** `glossary.md`'s refused words are largely unusable as a grep list, about a third being ordinary English refused only for one concept — `report`, `run`, `session`, `index`, `plan`, `item` and `question` — so a scan for them returns false positives and the distinctive refusals are checked by hand instead. **`where` was on this list and is not refused by any `_Avoid_` line**, found at node 114's check; the superseded wording is in [map-history.md](map-history.md).

## Superseded from `map-manager-only.md` at node 219 — the retrospective bullet's mint-on-second-report rule and its filing sentence

*Replaced under the `Change the map` procedure at [Replace the mint-on-second-report rule in the map's retrospective item](nodes/219-replace-the-mint-on-second-report-rule-in-the-map.md), carrying out [node 212](nodes/212-the-mint-on-second-report-rule-is-defeated.md)'s answer. What replaces them has the worker name and count each standing item it reports, ranks a repeated item rather than minting a node on it, and has the manager write the retrospective in the edit that resolves the node. The rest of the bullet is unchanged and is not reproduced here.*

### From `map-manager-only.md`'s `## Notes` — the retrospective bullet's sentence on the manager's two duties

*Replaced, and it stood as:*

**Two duties on the manager come with them**, in place of anything that sweeps the answers later: it disposes of each item naming the record in the report that closes that node — acting on it, minting a node, or saying why not — and **on the second report of the same standing item it mints a node**, repetition being where the weight is and the manager having missed three repeats of one finding.

### From `map-manager-only.md`'s `## Notes` — the retrospective bullet's filing sentence

*Replaced, and it stood as:*

**The worker hands it back as text and the manager files it** in a section of its own headed `## Retrospective`, placed last in the node file.

## Superseded from `map-manager-only.md` at node 276 — the landing policy's ground for naming the worktree's path

*Replaced under the `Change the map` procedure at [The landing policy says the work sits outside the repository](nodes/276-the-landing-policy-says-the-work-sits-outside-the-repository.md). The sentence grounded the rule that the gate payload names the worktree's path on the work sitting in a checkout outside the repository, and the worktree has been inside the repository since [Run an implementation node's work in a worktree](nodes/68-implementation-in-a-worktree.md). What replaces it keeps the rule and grounds it on the work being uncommitted, so that the path is how the work is found. The rest of the paragraph is unchanged and is not reproduced here.*

### From *Landing an implementation node's work* — the landing policy's sentence on what the gate payload names

*Replaced, and it stood as:*

**The gate payload names the worktree's path** ([node 231](nodes/231-a-gate-payload-stops-carrying-a-diff-command.md), [node 336](nodes/336-carry-the-rules-on-what-reaches-the-human-the-code.md)), because an implementation node's work is uncommitted in a checkout outside the repository and `git diff` where the human is standing does not show it — their words on being handed a gate without it: *"what are the changes ? I don't see them in git ?"*.

## Superseded from `map.md`'s `## Notes` at node 211 — the item that a fact about the record is derived rather than stored

*Replaced under the `Change the map` procedure at [State in the map what a number handed to another agent must carry](nodes/211-what-a-number-handed-to-another-agent-must-carry.md), which writes into the item the rule [node 183](nodes/183-nothing-measures-the-record-about-itself.md) settled: a number about the record that is handed on carries its date and is marked not authoritative and for scale only, and its receiver re-derives it. The item's sentence on `derivations.md` is unchanged. The item is shown whole.*

### From *Notes* — the item that a fact about the record is derived rather than stored

*Replaced, and it stood as:*

- **A fact about the record is derived rather than stored.** [`.scratch/graph-workflow/derivations.md`](derivations.md) holds the means of deriving the facts this effort measures about its own record, holds no values, and is not one of the graph's files. A number a worker receives from anywhere, whether a spawn, a handover or a line of the record, is re-derived before it is relied on. Settled at [node 183](nodes/183-nothing-measures-the-record-about-itself.md).

## Superseded from `map-implementation-rules.md` at node 381 — the sentence reserving `decisions.md` and `flags.md` to the manager in every case

*Replaced under the `Change the map` procedure at [The rules file reserves `decisions.md` to the manager even where a node's own work is that file](nodes/381-the-rules-file-reserves-decisions-md-even-where-it-is-the-work.md). The sentence made any change to the node's own status line, to `decisions.md` or to `flags.md` bookkeeping reserved to the manager, and had the checker fail it, even where the node's acceptance condition required that change. What replaces it keeps the status line reserved in every case and reserves `decisions.md` and `flags.md` except where the acceptance condition requires a change to that file, which is then the node's work. The paragraph's other sentences are unchanged. The paragraph is shown whole.*

### From `## What the work is held against` — the paragraph beginning "An implementation node's work on this effort may be the effort's own record"

*Replaced, and it stood as:*

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

## Superseded from `map-manager-only.md` at node 284 — the create command's relative path, and the writability check's

*Replaced under the `Change the map` procedure at [The worktree route's create command names a relative path and
never says from where](nodes/284-the-worktree-create-command-names-a-relative-path.md). Each passage gave a path
relative to the shell's working directory. The create bullet said only that the manager works from the main tree,
which names the tree and not the directory, and the writability check named no directory at all. Each stated a
rule that currently binds, so it took this route rather than strike-in-place, on [Where the never-delete rule
stops](nodes/189-where-the-never-delete-rule-stops.md)'s test, and each is reproduced byte-identical to the text it
had under *How the worktree is made*. What replaces the create bullet runs the command as `git -C <repo root>`,
`<repo root>` being the main tree's absolute path. What replaces the writability check prefixes its path with
`<repo root>`. The rest of the section is unchanged and is not reproduced here.*

### From *How the worktree is made* — the create bullet

*Replaced, and it stood as:*

- **Create.** The manager makes each implementation node's worktree from the main tree with one plain git command:
  `git worktree add -b worktree-<NN>-<name> .scratch/graph-workflow/worktrees/<NN>-<name>`, where `<NN>` is the
  node's id — so the id is in the path and in the branch. Settled at [node
  265](nodes/265-should-the-worktree-route-drop-enterworktree-for-git.md).

### From *How the worktree is made* — the bullet on the route's one failure mode

*Replaced, and it stood as:*

- **The route's one failure mode, and the read-only command that catches it.** The route works because
  `.scratch/graph-workflow` is inside the manager's sandbox writable region, and **that has not always been so** —
  in one session the manager's own shell could not append to `flags.md` in that directory while it could write the
  node files one level below. **So the manager runs `test -w .scratch/graph-workflow` before creating a worktree.**
  Where that check fails the worktree can be **neither created nor written** and there is no fallback, no tool call
  being able to widen the region for that path, so it is **raised to the human** rather than worked around. Settled
  at [node 265](nodes/265-should-the-worktree-route-drop-enterworktree-for-git.md).

## Superseded from `map.md`'s `## Notes` at node 135 — the skills line naming `/grilling` and `/domain-modeling`

*Replaced under the `Change the map` procedure at [Repoint the map's `## Notes` skill line when its two replacements land](nodes/135-repoint-the-maps-skill-line-when-its-replacements-land.md). The line was correct when [node 113](nodes/113-whether-the-method-skill-instruction-does-any-work.md) kept it, and stopped being correct when its two replacements landed: the batching rules in the grilling contract at [node 126](nodes/126-carry-question-batching-into-the-grilling-contract.md), and `/repo-docs`, which [node 130](nodes/130-the-docs-discipline-this-workflow-ships.md) named as replacing `/domain-modeling`, at [node 383](nodes/383-ship-the-repo-docs-skill.md). The new line names `/repo-docs` in place of `/domain-modeling`, points at the grilling contract's `## How you grill` in place of `/grilling`, and leaves `/naming`, `/coding-principles`, `/prototype` and the glossary sentence unchanged. The item is shown whole.*

### From *Notes* — the skills line

*Replaced, and it stood as:*

**Skills every session should consult:** `/grilling` and `/domain-modeling` by default, `/naming` for terminology, `/coding-principles` before writing code, `/prototype` for prototype nodes. **Plus one file, not a skill:** [`glossary.md`](../../.claude/skills/expedition/glossary.md) in the skill directory is the glossary, moved there by [node 56](nodes/56-ship-the-glossary-into-the-skill-set.md), and reading it is a precondition for writing anything — its `_Avoid_` lines are what stop a settled term from drifting back.

## Superseded from `map-manager-only.md` at node 391 — the retrospective bullet's filing sentences and its two duplicated sentences on existing names

*Replaced under the `Change the map` procedure at [File a retrospective where the worker put it, and fold the bullet's duplicated sentences](nodes/391-file-a-retrospective-where-the-worker-put-it.md). The filing sentences had the manager copy a retrospective out under a `## Retrospective` heading placed last in the node file. What replaces them has the manager file a retrospective where the worker put it, as the last part of the pasted handover or question payload, and leaves a retrospective filed under that heading before 2026-10-05 where it is. Two older sentences said again what the bullet's newer sentences on a name's written form already say, as [node 387](nodes/387-state-the-written-form-of-a-standing-items-name.md)'s checker found. They are removed, and the sentence that points at derivations.md entry (j) gains the older sentence's "not from memory" clause. The rest of the bullet is unchanged and is not reproduced here.*

### From `map-manager-only.md`'s `## Notes` — the retrospective bullet's two older sentences on a name's count and on finding existing names

*Removed, and they stood as:*

It states how many earlier retrospectives carry that name, and lists their node ids. It finds the existing names by searching the retrospective sections of the files under `.scratch/graph-workflow/nodes/`, whatever heading each section was filed under, and not from memory or from any list held elsewhere.

### From `map-manager-only.md`'s `## Notes` — the retrospective bullet's sentence pointing at derivations.md entry (j)

*Replaced, and it stood as:*

The worker obtains the existing names, with their counts and node files, by running the entry headed `## (j) Item names carried by the retrospectives` in [derivations.md](derivations.md).

### From `map-manager-only.md`'s `## Notes` — the retrospective bullet's filing sentences

*Replaced, and they stood as:*

The manager writes it into the node file in the same edit that writes that node's answer, its flags and its line in `decisions.md`. It is written last in the file, so the mandatory section order is untouched. It is written under the heading `## Retrospective` and under no other heading. It is not an annotation, since `graph-conventions.md` defines an annotation as what a later piece of work changed about a node's answer. It is a section the shipped node-file format does not list, allowed on this effort only; the human's `verbatim` "ok for A", 2026-09-27, on the manager's question after [node 340](nodes/340-add-the-annotation-section-and-what-a-hard-rule-is.md) landed.

## Superseded from `map.md`'s `## Notes` at 2026-10-07 — the bold sentence of the standing instruction on a condition that forces a contradiction

*Replaced under the `Change the map` procedure by the manager, on the human's `verbatim` "ok", 2026-10-07, to the manager's recommendation to narrow it to what [node 214](nodes/214-a-condition-that-contradicts-a-standard-is-a-raise.md) shipped. The rest of the bullet, including the human's quoted words, is unchanged and is not reproduced here.*

### From `map.md`'s `## Notes` — the bullet's bold opening sentence

*Replaced, and it stood as:*

**Where an agent sees that its acceptance condition forces a contradiction, that is a raise and not a flag.**

