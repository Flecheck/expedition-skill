# How an agent workflow and its skills reduce their own token cost

Type: research
Status: resolved

## Question

Go and find what is known — on the internet and in the material already on this machine — about reducing the
token cost of **an agent workflow and the skill files that drive it**. Report facts with sources.

The human's instruction, `verbatim`: *"I think we will need to do some token optimisation at some point. We can
spawn a reseach node to do some research on how to optimize token usage (using internet) to find what can be
done to reduce the usage of agents and subagents skills. And then follow it up with a grilling node. We can then
add new rules for writing skills , updates to the workflow and update to the skills. One issue with looking at
internet is that there is a lot of stuff about how a user reduces the usage, here we want to reduce the usage of
a workflow and of skills so it might be harder to find."*

**The subject is the workflow's own spend, not a user's habits.** The human named this obstacle themselves and
it is the node's main risk: most published material is advice to a person typing in a chat window — be
concise, start a new conversation, pick a cheaper model. That is **out of scope**. What is in scope is the cost
a *designed* workflow pays whether or not a human is present:

- **Always-loaded surface** — every skill description sitting in every agent's window every turn, whether it
  fires or not, times every agent spawned.
- **Spawn payload** — what the manager copies into each worker and each checker. This effort copies the
  acceptance condition, the bar, the ground rules and the work paths into every check, deliberately, because the
  checker reads no map.
- **Handover** — what comes back, and how much of it the manager then holds.
- **Fan-out** — one checker per implementation node, plus whole-graph passes. Measured here: one node spent
  ~283k worker tokens on **checking alone**, across three attempts.
- **The long-lived thread** — the manager's own context, measured in this effort at ~200k per node and named its
  first-failing resource.

### What this node must do beyond searching

- **Say what is already answered locally, and do not re-derive it.** `/writing-for-agents` in the
  `mattpocock-skills` plugin — upstream rev `5b15a47`, not yet on this machine, so **read it from upstream or
  from the plugin path if it has landed** — already carries a `## Pruning` section that is largely this subject:
  single source of truth and duplication, **the environment as a source of truth and a document that restates it
  as a cache** *"earning its load only when the lookup is expensive"*, **relevance** and **sediment**, and
  **no-ops** (*"an instruction the model already obeys by default pays load to say nothing"*, with the test
  named model-relative and settled by running the document). It also names **context load** and **cognitive
  load** as two budgets, **sprawl** as a failure mode, and **leading words** as a token-for-token compression
  lever. Report what the external material adds **beyond** that, and where it contradicts it.
- **Distinguish what is measured from what is asserted.** Blog-post advice with no numbers is an assertion; say
  so. Where a source reports a measurement, carry the number and the setup.
- **Name the mechanisms available in this harness specifically** where a source's mechanism has an analogue here
  — subagent isolation, prompt caching, model choice per worker, background agents, tool-schema deferral — and
  say plainly where it does not.
- Where a finding turns on a judgement only the human can make, report it for [What the token findings change in
  the workflow and its skills](53-what-token-findings-change.md) rather than deciding it.

**Blockers: none.** It reads outside sources and writes no product.

### Why `research` and not `grilling`

It produces **facts with sources**, from material outside the working directory, and involves the human
nowhere. Under [Concurrency model](04-concurrency-model.md) AFK research *"may fan out freely"*, so it costs
nothing against the interview slots or the code slot. The decisions it feeds are node 53's.

## Answer

**The human's predicted hazard was real but not the whole picture.** In the worker's words: *"Searching on the
workflow-side terms (spawn payload, orchestrator context, fan-out, per-agent prefix, checker cost) reaches a
body of material that is about designed workflows and is largely **measured**. Three things made it reachable:
Anthropic's own harness documentation now has pages written for exactly this question, there is a 2026 arXiv
literature on orchestration-layer token economics, and the caching literature is entirely workflow-side because
caching is a property of how requests are assembled rather than of what a user types."*

**What is genuinely thin:** *"nobody publishes on the cost of a **human-gated** workflow. Every measured
orchestration source assumes an unattended run. The interview-and-gate shape this effort is built on has no
external cost literature at all, and that is a finding rather than a gap in the search."*

### 1. Context is not spend, and the effort's two baseline numbers measure different resources

`map.md`'s **~200k of manager context per node** is a **window** figure. Claude Code's own docs price it:
*"Claude Code sends your full conversation with every request… With prompt caching, Claude Code re-reads that
history at the cached token rate"*, and `cache_read_input_tokens` is *"billed at roughly 10% of the standard
input rate"*. The **~283k on checking alone** for one node is a **spend** figure, at close to full uncached
rate, for the mechanism in section 3.

So the manager's 200k is primarily an **accuracy and capacity** problem, not a bill. Chroma's context-rot study
across 18 models found *"model performance consistently degraded with increasing input length"* even on
retrieval; Anthropic names the same effect — *"every token attends to every other token, creating n²
relationships"*. **The worker's inference, marked as such:** node 24's *"the manager's context was the thing
that broke"* is right about the failure and would be wrong if restated as *the manager is where the money goes*.
**The fleet is where the money goes.**

### 2. The always-loaded surface is measured, and it is a non-issue for this corpus

The six shipped contracts' `description:` lines total **725 characters ≈ 180 tokens**. That is the entire
always-loaded surface the eight shipped files impose. For scale, external measured figures: ~100 tokens per
skill at the metadata tier; a six-month production study of 17 skills measured with tiktoken `cl100k_base`
finding bodies of ~790 and ~2,050 tokens, where *"the token math worked out well for about 13 of them. The other
four cost more than they saved"*; reported problem cases of 1,500–3,033 tokens of index at 87–103 installed
skills. **Settled as a non-issue by measurement, and it should absorb none of node 53's budget.**

One caveat that is real and belongs to upstream's ledger rather than ours: `disable-model-invocation` zeroes
context load and upstream prices the shifted cost as *human cognitive load*. **In a workflow it is a
spawn-payload token cost too** — a worker that cannot invoke a skill must be handed it as spawn text or read it
by path — and upstream's accounting has no slot for that. `map.md:21-29` is a worked instance.

### 3. The spawn payload is the real per-node cost, and the harness names the mechanism

Primary, from `code.claude.com/docs/en/prompt-caching`, section *Subagents and the cache*:

> *"A subagent starts its own conversation with its own system prompt and tool set, separate from the parent's.
> Its first request doesn't read the parent's cache, because the two prefixes differ, and it warms a cache of its
> own across its turns. Subagents use the five-minute TTL even on a subscription, since the automatic one-hour
> TTL applies to the main conversation."*

**So every worker and every checker pays full uncached input for its entire opening payload**, and nothing of
the manager's warm 200k helps it. The 5-minute TTL means a worker paused for a human answer — the whole
interview shape — is liable to come back cold.

Measured on this corpus (characters exact; tokens are `chars/4`, per flag `52.1`):

| Component | chars | ≈ tokens |
| --- | --- | --- |
| `map.md` — every worker reads it in full | 79,361 | **19,840** |
| `expedition/graph-conventions.md` | 21,791 | 5,447 |
| `expedition-checker/SKILL.md` | 18,030 | 4,507 |
| `expedition-implementation/SKILL.md` | 14,039 | 3,509 |
| all eight shipped files | 97,469 | 24,367 |
| **one fog paragraph**, `map.md:75` | 20,589 | **5,147** |
| all 54 node files | 982,260 | 245,565 |

**`map.md` is 4.4× the largest shipped contract and 81% of the whole shipped corpus, and every worker reads all
of it, cold, once per node.** A research worker's floor before doing any work is map + contract + node ≈ 22,800
tokens. **At 179 nodes that is ~4M tokens of uncached map re-reading alone, and the map grows monotonically
under never-delete.** The cheapest large lever the findings expose, and it appears nowhere in the effort's
record.

Anthropic's own spawn advice is startlingly small by comparison — *"Each subagent needs an objective, an output
format, guidance on the tools and sources to use, and clear task boundaries"* — and the cost page: *"Keep spawn
prompts focused… everything in the spawn prompt adds to their context from the start."*

**What this reprices about node 50.** Node 50's 700 byte-identical words per contract is ~4,060 chars ≈
**~1,015 tokens per worker spawn**, paid once then cached inside that worker. Against the same worker's ~19,840
tokens of map, **the duplication is ~5% of one worker's opening read.** The worker's inference, reported to node
53 rather than decided: *"on token cost alone the duplication does not clear the bar for a remedy that costs
exact agreement, and the argument for changing it has to stand on maintenance rather than on tokens."*

### 4. Paid once per spawn versus paid every turn — the ~10× distinction upstream cannot make

Primary: *"Skills and commands inject their instructions as user messages at the point of invocation. Nothing
earlier in the conversation changes."* So **a contract's body is a once-per-spawn cost at full rate, then a
cached read** — never a per-turn full-rate cost. **The sharpest thing the external material adds beyond
`/writing-for-agents`:** upstream's `## Pruning` reasons about context load as one undifferentiated budget and
has no account of prompt caching at all. Under caching the two classes it merges differ by ~10×, and only one
compounds with turn count. **Pruning effort spent on the wrong class buys almost nothing.**

The cache list node 53 needs, all from the same primary page. **Invalidates everything:** switching model
(*"each model has its own cache"*), changing effort level (*"keyed by effort level as well as model"*), fast
mode, connecting/disconnecting an MCP server, denying a whole tool, upgrading Claude Code, `/compact`.
**Keeps the cache:** editing repo files, editing CLAUDE.md mid-session (which also means the edit *doesn't
apply*), output style, permission mode, invoking skills and commands, `/recap`, `/rewind`, spawning a subagent.
`/rewind` is **strictly cheaper than** `/compact` for abandoning a path. `/clear` costs nothing; `/compact`
*"reads the conversation it summarizes"* but *"while the cache is warm, that request reads your prefix from the
cache"* — **so the effort's standing practice of compacting between nodes is cheap only inside the TTL**, one
hour on a subscription, five minutes once drawing on credits, with `ENABLE_PROMPT_CACHING_1H=1` holding the
hour. And **cache scope is per machine *and* per directory**: *"That includes worktrees of the same repository."*
So `isolation: worktree` forfeits prefix sharing — a cost the effort has never priced.

### 5. Fan-out: a prefix-sharing mechanism whose preconditions are exactly this effort's free variables

Primary, `code.claude.com/docs/en/workflows`: *"Agents in the same run can read each other's prompt cache. Two
agents that run with the same model, effort level, agent type, tools, output schema, and working directory build
the same tools-and-system-prompt prefix… When a fan-out starts several matching agents at once, Claude Code
holds all but the first until the first agent's response begins."* Two honest boundaries the worker named: this
is documented for the dynamic-workflow runtime and not for `Agent`-tool spawns, and the shared prefix is the
tools-and-system-prompt layer, not the spawn message. **But the five preconditions name five things this effort
varies freely.**

The same page answers the manager-context problem — *"intermediate results stay in script variables instead of
landing in Claude's context"*, with a JSON `schema` making a handover's shape **machine-enforced** rather than
prose-enforced — with a **decisive** limitation: *"No mid-run user input — only agent permission prompts can
pause a run. For sign-off between stages, run each stage as its own workflow."* The worker's inference: a
workflow can host the AFK fan-out — checker passes, cascade, sweep — and **cannot host an interview or a gate.**

### 6. Fork versus named subagent — an either/or the record does not contain

*"A fork, by contrast, inherits the parent's system prompt, tools, and conversation history exactly, so its first
request reads the parent's cache."* So: a **named subagent** starts cold, keeps its own cache, and **may take a
cheaper model**; a **fork** reads the parent's cache at ~10% but inherits the parent's whole context **and the
parent's model**. The worker's inference: the effort's *most of the context lives in the workers* preference and
its credit constraint both point at the named subagent, and both therefore **choose** the cold start. **You
cannot have a cheap model and a warm cache on the same worker.**

### 7. Tool-schema deferral is already pulled, by default

*"MCP tool definitions are deferred by default."* Observed directly on this node: ~110 deferred tool names with
schemas withheld. **The finding is that it is not a lever this effort can pull — it is already pulled, and
nothing in the shipped files touches it.** Stated so node 53 spends no rule on it.

### 8. Measured external numbers

**The most on-subject source, and a controlled experiment.** *The Harness Effect: How Orchestration Design Sets
the Token Economics of Enterprise Agentic AI* (arXiv 2607.06906, 8 July 2026), 22 locked tasks, six models,
*"changing only the orchestration layer"*: *"the harness cuts blended cost per task 41% ($0.21->$0.12), median
wall-clock 44%, and tokens per task 38% (14.2k->8.8k), with task-completion quality at parity… Efficiency is
model-invariant — every model gets cheaper (33-61%)… On this workload the orchestration layer moved cost per
task more than the full spread of the model menu did."* It names the failure mode **token maxing**. Caveats:
enterprise workload, vendor-authored, 22 tasks, quality gain self-described as directional.

**Anthropic's multi-agent research system:** *"agents typically use about 4× more tokens than chat
interactions"*; *"multi-agent systems use about 15× more tokens than chats"*; *"token usage by itself explains
80% of the variance"* on BrowseComp. Effort-scaling rules given as prompt content. And the boundary: *"some
domains that require all agents to share the same context or involve many dependencies between agents are not a
good fit."*

**Claude Code's own multiplier:** *"Agent teams use approximately 7x more tokens than standard sessions when
teammates run in plan mode."*

**Caching, controlled.** *Don't Break the Cache* (arXiv 2601.06007): *"prompt caching reduces API costs by
41-80% and improves time to first token by 13-31%"*, and *"placing dynamic content at the end of system prompts
and excluding dynamic tool results, provides more consistent benefits than naive full-context caching."*

**Tactic-by-tactic.** *Local-Splitter* (arXiv 2604.12301): *"T1 (local routing) combined with T2 (prompt
compression) achieves 45-79% cloud token savings on edit-heavy and explanation-heavy workloads"*, and *"the
optimal tactic subset is workload-dependent, which we believe is the most actionable finding."* **The closest
external analogue to this effort's stated v2 plan**, measured at 45-79%.

**The dissenting position.** Cognition's *Don't Build Multi-Agents* argues context partitioning is the
fragility, allowing subagents in exactly one case — where investigative work need not remain in the main
agent's history. The worker's inference: *"that one permitted case is precisely what this effort's research and
checker nodes are, which makes Cognition's position an argument for the effort's shape rather than against it."*

### 9. The counterweight: compressing a contract is not safe in the general case

The penalty concentrates on **format- and structure-bearing** instruction text rather than on semantic content.
Search-summarised figures: LLMLingua-2 on agent prompts — *"compression rates exceeding 30% led to failure on
all tasks"* in a web-shopping scenario, attributed to loss of format crucial for agent tasks; passage-counting
accuracy from below 20% to below 4.5%; summarisation stable to 5.7×; manual restructuring typically 20-40% with
no quality loss.

The worker's inference, and it is the boundary node 53 needs before writing any rule: *"the expedition contracts
are mostly format-bearing — a five-part handover with named parts, a required `## Review` shape, a flag marker
fixed as `**· settled**`, a flag id form `NN.k`, four tests a condition is read back against. That is the exact
class the literature finds most fragile. **The safe compression target is the prose that explains why, and the
unsafe target is the shapes.**"*

This is **compatible** with upstream's leading-words lever rather than opposed: *"upstream compresses
description… That is the semantic class the literature finds robust. The literature's penalty falls on
format-bearing text, which leading words never touches. Compress adjectives, never compress shapes."*

### 10. The harness already ships the instruments the map twice asks for

`/usage` reports input, output, **cache read and cache write** per model, resetting on `/clear`, plus *"recent
usage attributed to skills, subagents, plugins, and individual MCP servers"* and **behavior flags** *"such as
long context or cache misses, flagged when one accounts for 10% or more"*. `/context` shows what consumes
space. A statusline reading `current_usage` shows creation against read, where *"a high read-to-creation ratio
means caching is working well."* `/workflows` shows per-agent usage live. OpenTelemetry exports per-session
cache read and creation.

**Reported to node 53 rather than decided:** `map.md`'s `## Out of scope` rules out *"Cost and token accounting,
dashboards, fleet telemetry"* while two fog items **require** a measured spend-per-node-type table. **Reading
numbers the harness already prints is not building accounting**, and as written the out-of-scope line reads as
forbidding the measurement the fog demands.

### 11. Measured locally: never-delete is not what makes `map.md` expensive

Measured by regex over `~~…~~` spans: **`map.md` 1,649 struck characters of 79,361 — 2.1%**, across 20 spans;
**all 54 node files 4,269 of 982,260 — 0.4%**, across 35 spans.

**Superseded text is a rounding error.** What makes `map.md` expensive is **live** prose: the append-marked fog
paragraphs, one of which (`map.md:75`) is 20,589 characters ≈ 5,147 tokens on its own — larger than any shipped
contract, and 26% of the file every worker reads cold. **The conflict is real; the party winning it is
misidentified. It is the append-in-place practice, not never-delete.** Of the fog item's four candidate
remedies, *prune struck text into an archive* would recover 2.1% and *cap an item's updates* addresses the
actual cost.

### 12. What is not established

- **No source measures a human-gated agent workflow.** The cost of a worker idling across a human answer, and
  of its 5-minute subagent TTL expiring while it waits, is stated as a mechanism by the harness docs and
  measured by nobody.
- **No source gives a cost figure for a *checker* specifically.** Nearest: a strong model as verifier at 193
  tokens per prompt against 483 as generator (~2.5×), and LangChain finding batched criteria *"an order of
  magnitude cheaper for the same model"* — both search-summarised — plus the ceiling that frontier models
  *"only agree on labels 95.7% of the time"*. **This effort's own 283k remains the only figure for a checker on
  a prose deliverable.**
- **Whether `Agent`-tool spawns get the fan-out prefix stagger** is documented neither way.
- **No number for how much a shorter `map.md` would save**, that depending on choices only node 53 can make.

## Flags

`52.1` `ASSUMPTION` — **Every local token figure is `chars/4`, not a tokenizer count.** The node asked it to
measure rather than estimate; it could not — no `python3` and no tokenizer in the sandbox — and the one external
study publishing a per-line ratio measured skills averaging ~28 chars/line against this corpus's ~100. It
applied `chars/4` uniformly and **left every character count beside its estimate**, so any figure can be
recomputed without re-reading the corpus. Its own statement of what this means: *"the **ratios** here are sound
… and none of the findings turns on a figure being exact. The **absolute** numbers are ±20% and should not be
quoted as measurements without a tokenizer run. The character counts are exact."*

`52.2` `ASSUMPTION` — **It ruled that a search engine's summary of an unfetched page is evidence rather than
authority.** `map.md` declares no source hierarchy, so *"every source you are pointed at is authoritative"* —
but it was pointed at four sources and found several dozen. It split the material three ways: **primary and
fetched** carries facts on its own; **fetched secondary** carries facts with its setup named; and
**search-summarised, unfetched** is marked inline at every use with **no finding resting on it alone**. Its
words: *"the load-bearing findings — the subagent cold start, the fan-out stagger, the cache-invalidation list,
the four measured papers, the local measurements — are all first-class, and the third class is there for breadth
rather than for weight."*

## `NEW NODES`: none, reported deliberately

In the worker's words: *"Every candidate I found is a judgement about the workflow's design, which is node 53's
by this node's own scope boundary, and the four sharpest are routed there in the answer above: shrinking what a
worker reads of `map.md`; the fork-versus-cheap-model either/or; homogenising a checker fan-out's five prefix
conditions; and whether the dynamic-workflow runtime hosts the AFK passes given that it forbids mid-run human
input. The one candidate that is not a judgement — instrumenting the next few nodes with `/usage` attribution to
produce the spend-per-node-type table — is already committed by two of `map.md`'s fog items, and minting a node
for something the map already commits to is the delta-list failure the map warns about."*
