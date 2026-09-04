# Whether `qmd` lowers this workflow's token cost, and what it would cost to adopt

Type: research
Status: resolved

Blocked by: none

## Question

*The human's own request, `verbatim`. **Minted by the manager from their message and not surfaced by any worker.***

> Would it be interesting to add https://github.com/tobi/qmd to lower token usage, to help with all the issues ?
> Maybe create a research node and then grilling

**What to establish**, written by the manager under the constraint that a research node's question fixes what is read
and never what is concluded:

1. **What `qmd` is and what it actually does**, from its own repository rather than from any description of it. Its
   licence, its dependencies, what it needs installed, and whether it runs on this machine.
2. **Where in this workflow it could bear**, against the measured costs this effort already holds rather than against
   a guess: `map.md` at ~19,840 tokens read cold by every worker once per node; `decisions.md` read whole by several
   workers to use four lines; node files that workers report reading in full to use fifteen lines; and the
   five-minute prompt-cache TTL fixed at [node 52](52-token-cost-of-a-workflow.md).
3. **What adopting it would cost**, including the thing that decides it under this effort's own ground rules: whether
   it makes any shipped file depend on a tool being installed. **Ground rule 1 forbids a shipped file assuming this
   repo, this machine, or a toolchain**, and the human has separately directed that the skill not depend on an
   external plugin — recorded on [node 113](113-whether-the-method-skill-instruction-does-any-work.md). A tool the
   workflow requires is a harder dependency than a skill it invokes.
4. **Whether the alternative the human named in the same breath is the same problem or a different one.** Their
   words, `verbatim`: *"Or maybe make the nodes easier to grep, traverse. I don't know if it is nessesary ?"* Establish
   whether these are two routes to one end — less context read per node — or two different problems. That comparison
   is what [node 129](129-what-to-do-about-the-records-token-cost.md) decides on.

**It may read outside the working directory**, and it must: the repository at the URL above, and the record's own
files.

## The manager's note at filing

*Not a change to anything above.*

**The human framed this as *"to help with all the issues"***, and the manager has not read that as naming a
particular set. **What the record actually holds** is a repeated, measured complaint from workers rather than a
suspicion: seven consecutive retrospectives report reading `map.md` whole to act on a handful of lines, and three
report that `decisions.md`'s one-line cap hid the fact that made a node relevant. **That is the evidence this node
has**, and whether `qmd` touches it is exactly what is unestablished.

**The manager has not looked at the URL.** Reading it is this node's work, and a manager's note is capped at context
it already holds.

## What the human added after this node was minted

**Their words, `verbatim`:**

> (qmd is a local seach engine)

***The manager's note.*** This is the only description of the tool anywhere on the graph, and it is **theirs rather
than the repository's** — clause 1 above still asks that what `qmd` is be established from its own repository, and
this line is now the expectation that establishing it should either confirm or correct. **If the repository says
something other than a local search engine, that is a finding rather than a discrepancy to smooth over.**

**What it does to clause 4.** Their alternative — *"make the nodes easier to grep, traverse"* — reads differently
against a search engine than against a compression tool: a search engine and a more greppable record are two ways of
doing the same thing rather than two different problems. **The manager has not concluded that**, and clause 4's
comparison is still what node 129 decides on; the reading is offered as the human's description and not as a result.

## Answer

*Attempt 1's handover, pasted as its worker wrote it. The manager authored none of it.*

### 1. What `qmd` is, from its own repository

Cloned at `HEAD` = `dbfd0b4736aeaf761d1a16ca8e424f071df8feb9`, dated 18 Aug 2026, into a temporary directory outside
this repo.

- **Licence: MIT**, `LICENSE`, "Copyright (c) 2024-2026 Tobi Lutke".
- **What it says it is**, `package.json` `description`: *"Query Markup Documents - On-device hybrid search for
  markdown files with BM25, vector search, and LLM reranking"*. `README.md`'s opening line: *"An on-device search
  engine for everything you need to remember. Index your markdown notes, meeting transcripts, documentation, and
  knowledge bases… Ideal for your agentic flows."* Version `2.8.3`.
- **The human's description is confirmed, near-verbatim.** They wrote *"(qmd is a local seach engine)"*; the
  repository says "on-device search engine". No discrepancy to report on the substance. It under-describes in **two
  ways that decide clause 3**, and both are findings rather than corrections:
  1. It is a **hybrid** engine — BM25 (SQLite FTS5) plus vector search plus an LLM reranker plus a fine-tuned
     query-expansion model — which is why it carries **three GGUF models totalling ~2.04 GB** rather than being a
     lightweight indexer.
  2. It **ships as a Claude Code plugin with an MCP server**. `.claude-plugin/marketplace.json` declares a plugin
     named `qmd` with `"skills": ["./qmd", "./release"]` and `"mcpServers": {"qmd": {"command": "qmd", "args":
     ["mcp"]}}`, and `README.md`'s *"Claude Code — Install the plugin (recommended)"* gives `claude plugin
     marketplace add tobi/qmd` / `claude plugin install qmd@qmd`. This is the fact that collides with the human's own
     standing direction, in section 4 below.
- **What it needs installed.** `package.json` `engines`: `node >= 22`. `README.md`'s `### System Requirements` adds
  **`Bun >= 1.0.0`** and, on macOS, Homebrew SQLite "for extension support". Thirteen runtime dependencies, the
  load-bearing ones being `node-llama-cpp 3.20.0`, `better-sqlite3 ^13.0.3` (native, rebuilt with `node-gyp`),
  `sqlite-vec 0.1.9`, four `tree-sitter` grammars, and `@modelcontextprotocol/server 2.0.0`.
- **The models**, `README.md` `### GGUF Models (via node-llama-cpp)`, "auto-downloaded on first use" from HuggingFace
  into `~/.cache/qmd/models/`: `embeddinggemma-300M-Q8_0` ~300 MB (embeddings), `qwen3-reranker-0.6b-q8_0` ~640 MB
  (reranking), `qmd-query-expansion-1.7B-q4_k_m` ~1.1 GB (query expansion).
- **A tier that needs no models.** `qmd search` is BM25/FTS5 only. Its own skill file states the fallback: *"If `qmd
  query` is slow or model/GPU setup fails, fall back to `qmd search`"*, and lists as a pitfall that *"Model-backed
  commands can be environment-sensitive."* So `qmd search` and `qmd get`/`multi-get` are usable with zero model
  download; `qmd query`, `qmd vsearch` and reranking are not.

### 2. Whether it runs on this machine

**Not by the documented route, and yes by another.** Probed directly:

- `node`, `npm`, `npx`, `bun`, `pnpm`, `sqlite3` are **all absent**. `python3` is present (3.13.15). So `npm install
  -g @tobilu/qmd` — the only installation method `README.md` gives — **cannot run here at all**.
- The repository ships a `flake.nix`, and `nix` 2.34.8 is present. `nix flake show` evaluates cleanly and declares
  `packages.default`, `apps.default` and `devShells.default` for `x86_64-linux` (this machine's `uname -m` is
  `x86_64`), plus a **home-manager module** taking `cfg.package` into `home.packages`.
- `nix build --dry-run .#default` resolved the whole closure: **"these 2 derivations will be built"**, **"these 50
  paths will be fetched (118.8 MiB download, 477.3 MiB unpacked)"** — pulling `nodejs-24.13.0`, `bun`,
  `node-gyp-12.1.0`, `python3-3.13.11` and `sqlite-3.51.2`. The flake's `buildPhase` runs `node-gyp rebuild
  --release` on `better-sqlite3`.
- **So: installable here, via nix, at ~119 MiB of store fetch plus ~2.04 GB of models on first model-backed use.** No
  prior state exists — neither `~/.config/qmd` nor `~/.cache/qmd` is present.
- **Marked as inference, not fact:** `/dev/dri/renderD128` exists and `nvidia-smi` does not, so there is no CUDA
  device. `node-llama-cpp` would run CPU or Vulkan here. Reranking 30 candidates per query on CPU is a latency cost
  this node did not measure, and `README.md` names a related cost — the stdio MCP transport is launched per client,
  and HTTP transport exists precisely "for a shared, long-lived server that avoids repeated model loading."
- **I did not build or run it.** Every claim above about qmd's behaviour comes from its own files, not from
  observation. See flag `128.1`.

### 3. Where it could bear, against this effort's measured costs

**Current measurements, taken now.** Token figures use the **nominal 4.0 bytes-per-token ratio**, which node 113
established is a rule of thumb rather than a tokenizer count; the byte counts are exact.

| Component | bytes now | ≈ tokens | previously measured |
| --- | --- | --- | --- |
| `map.md` | **42,566** | ~10,642 | 79,361 at node 52; 26,971 after node 59's restructure; 40,344 at node 113 |
| `decisions.md` — 90 lines | 21,973 | ~5,493 | — |
| all node files — **136** of them | **2,356,865** | ~589,216 | 982,260 across 54 files at node 52 |
| all **9** shipped files | 149,030 | ~37,258 | 97,469 across 8 files at node 52 |
| **what this node's own spawn mandated** | **102,558** | **~25,640** | — |

Of this node's own mandated read, `map.md` is 42% and node 52 alone is 25%.

**The three reads split into two classes, and qmd reaches only one of them.**

- **The mandatory read — `map.md`, and a worker's own node file.** qmd **cannot** touch this, and the reason is
  structural rather than a matter of tuning. A search engine requires a query, and a worker reads `map.md` whole
  precisely because it holds standing constraints *a worker cannot know it needs until it has read them*. You cannot
  query for the rules you do not know exist. The seven retrospectives naming which lines mattered are evidence for a
  **static** remedy — a per-kind digest, or bounding the file — not for a search tool. Same for a worker's own node:
  the map's own standing preference is that a node file's reader "needs that node whole".
- **The discretionary read — `decisions.md`, and the 2.36 MB node corpus.** This is where qmd could bear, and it is
  also where a **measured, zero-cost lever already exists and has never been pulled.**

**The decisive measurement.** A worker needing node 52's five-minute-TTL fact:

- Reading `nodes/52-token-cost-of-a-workflow.md` whole: **25,295 bytes ≈ 6,324 tokens**.
- `grep -rn "five-minute\|5-minute" nodes/` returns **1,799 bytes ≈ 450 tokens** of output, and correctly names node
  52 first among five files.

**Lexical search over the node corpus is already ~14× cheaper than reading the node whose fact you need, costs
nothing to install, and works on any machine.** Nothing in the shipped worker contracts tells a worker to do it. I
used it on this node: I retrieved the four `decisions.md` lines I needed with one `grep`, never reading the
21,973-byte file whole — the act three prior workers reported not having.

**And the record's index is provably lossy in a way no search tool repairs.** `grep -c "five-minute\|5-minute"
decisions.md` returns **0**. The fact clause 2 of this node names is *absent from the index*, because the one-line cap
excluded it. So the three workers' complaint that "`decisions.md`'s one-line cap hid the fact that made a node
relevant" is now a **demonstrated property rather than an impression** — and it is not a retrieval failure. **No
engine, lexical or semantic, can return what the file does not contain.** Indexing the node corpus instead of the
index would fix it; so would a richer index. qmd is one of those two and not the other.

**What qmd adds over `grep`, stated honestly.** One thing, and it is real: `vec:`/`hyde:` search finds a concept
**phrased differently from the query**. Every worker on this graph is in exactly that position — spawned cold,
without the record's own wording. My own probe shows the shape of the gap: I found the "comes back cold" fact only
because I already knew node 52's phrasing. Secondarily, qmd's `get "#docid:120:40"` windowing and its per-collection
**contexts** (the README calls contexts "the key feature… Don't sleep on it!") are retrieval affordances the `Read`
tool's `offset`/`limit` partly duplicates.

**But this is a capability gain, not a token saving.** Nobody currently reads across the 136-node, ~589k-token corpus
— it is unreadable, so no cost is being paid for it. qmd would **enable a read that is not happening**, which is
worth having and is not what this node was asked. Against `map.md`'s own warning that *"a ranking by predicted saving
is the token maxing failure in reverse"*, the measured saving qmd delivers over the already-available `grep` is
**unquantified**, and cannot be quantified without installing it.

### 4. What adopting it would cost — and the two verdicts

**In the shipped files: forbidden, and not a close call.** Two independent grounds, either sufficient:

- **Ground rule 1** — *"Nothing in the shipped files may assume this repo, this machine, or a toolchain. Prefer
  properties that are discovered over commands that are declared."* A contract instructing a worker to run `qmd
  query` declares a command and assumes a toolchain: Node ≥ 22, Bun ≥ 1.0, a native `better-sqlite3` build, and ~2.04
  GB of downloaded model weights. This machine — the effort's *own* machine — fails that assumption today, having no
  `node` and no `bun`. Against the map's *"The workflow will also be run on repositories this machine has never
  seen"*, a tool dependency is the exact failure the rule exists to prevent.
- **The human's standing direction**, now in the map: *"I also would want the skill to not depend on mattpockock, I
  don't know what is the status of this."* **qmd ships as a Claude Code plugin**, so adopting it into the shipped
  files creates the same class of dependency the human has just directed be removed — and a **strictly harder** one:
  `mattpocock-skills` is pure markdown, where the qmd plugin additionally requires a binary, a compiled native
  extension, an MCP server process and 2 GB of weights. **The manager's framing in the spawn is confirmed by the
  repository's own packaging**: a tool the workflow requires is a harder dependency than a skill it invokes, and here
  the tool arrives *as* a plugin.

**In this effort's own record: available and permitted, with a weak measured case.** `.scratch/` ships nothing, so
neither ground above reaches it; the machine can install qmd via nix at ~119 MiB; and 2.36 MB of markdown notes is
qmd's stated subject exactly. The adoption cost, itemised:

- **One-off:** ~119 MiB nix closure, ~2.04 GB models, `qmd collection add` + `qmd update` + `qmd embed` over 136
  files.
- **Per-write, ongoing:** the record is **append-in-place and never deletes**, so every node edit dirties that node's
  chunks and `qmd embed` must re-run. The map's own practice makes this a recurring cost rather than a one-time
  index.
- **Always-loaded context:** ~50 tokens for the skill's `description`. Its `SKILL.md` body is **11,182 bytes ≈ 2,795
  tokens**, plus `references/mcp-setup.md` at 2,808 bytes — paid per spawn that loads it, at the uncached rate node
  52 established every worker pays on its opening payload.
- **MCP tool schemas: ~free.** Node 52 established *"MCP tool definitions are deferred by default"*, and I observed
  the same directly — eight deferred tool names in my own context with schemas withheld. qmd's MCP server exposes
  four tools (`query`, `get`, `multi_get`, `status`), so it adds four deferred names, not four schemas.
- **One cache invalidation.** Node 52's cache list has *"connecting/disconnecting an MCP server"* among the acts that
  **invalidate** the prompt cache. Adding the server mid-effort costs the manager's warm context once.
- **Per-query output.** A search's own results and any `qmd get` output enter the context at full rate. **A search is
  only cheaper than a read when retrieved bytes plus query overhead beat the whole file** — which the grep
  measurement above shows holds comfortably for a targeted fact and would not hold for a broad query returning thirty
  reranked candidates.

**The node returns both verdicts**, as the spawn anticipated: **forbidden in the shipped files, permitted in the
effort's own record**, and in the record its case is unproven because the free alternative it would replace has never
been exercised.

### 5. Clause 4 — the human's alternative is the same problem, with a cheaper answer already installed

Their words: *"Or maybe make the nodes easier to grep, traverse. I don't know if it is nessesary ?"*

**One problem, two routes, and the routes are not equal.** Both aim at the same end — read less per node by
retrieving the part you need — so the manager's reading of this is confirmed rather than corrected. They diverge on
two axes that decide it:

- **Lexical vs semantic.** `grep` needs the record's own wording; a cold worker does not have it. That is the one
  thing qmd genuinely adds, and it is unmeasured here.
- **Writing vs tooling.** Greppability is a property of *how the record is written* — stable headings, a richer index
  than one line, per-node front-matter — and **survives ground rule 1 untouched**, needing nothing installed and
  working in a repository this machine has never seen. qmd is a property of *tooling*, and does not survive it.
  **This asymmetry, rather than retrieval quality, is what separates them for anything shipped.**

Both routes are also blocked on the same prior fact: **the index does not contain what workers went looking for**,
measured above. Neither route helps until that changes.

**On node 136 — adjacent, not the same problem, and the boundary is sharp.** Node 136 asks what bounds `map.md`'s
growth; `map.md` is the **mandatory** read, and search cannot serve a read whose whole point is that the reader does
not know what they need. This node's subject is the **discretionary** reads, which search can serve. Bounding the map
is the only lever on the map. **The mandatory/discretionary line is where the two nodes divide**, and I answer
nothing of node 136's.

### 6. What is not established

- **Whether qmd outperforms `grep` on this corpus, and by how much.** It is not installed; no retrieval quality or
  token figure here is measured. This is the number the record would need before adopting it, and producing it
  requires the install.
- **Its CPU-only latency here**, there being no CUDA device.
- **Whether `qmd embed` keeps up with append-in-place editing** at this record's write rate.

## Flags this node raised

`128.1` — `ASSUMPTION`, in the worker's own words:

> **I established that `qmd` builds on this machine and stopped short of building it.** `nix build --dry-run
> .#default` resolved the full closure (2 derivations to build, 50 paths to fetch, 118.8 MiB) which settles
> buildability, and I judged that an actual install — ~119 MiB of nix store plus ~2.04 GB of model weights written to
> `~/.cache/qmd/` on a machine this node does not own, to answer a question whose verdict for the shipped files is
> decided by a written ground rule rather than by any measurement — was not mine to make. **The consequence, stated
> plainly so nothing downstream mistakes it:** every claim in this answer about what `qmd` *does* is from its own
> repository files, and **nothing here is an observation of `qmd` running**. The measurements I did take — the
> record's current sizes, the grep-versus-whole-file comparison, the absence of `node`/`bun`, the nix closure — are
> all first-hand. The one figure the record would need to actually adopt this, qmd's retrieval quality against `grep`
> on this corpus, is the one an install would have produced, and it is named as unestablished in section 6.

## Nodes this node surfaced

**`none`, reported deliberately.** The worker's own account:

> Two candidates surfaced and both are already owned. The **qmd-versus-greppability comparison** is routed to node
> 129 by this node's own clause 4, and I have given it the two axes it needs (lexical-vs-semantic, and
> writing-vs-tooling with only the latter surviving ground rule 1). The **one-line cap on `decisions.md`** is now a
> measured defect rather than a complaint — the fact three workers went looking for appears zero times in the file —
> and that is node 129's subject, "what to do about the record's token cost", rather than a new node. The third thing
> I found, that **nothing in the shipped contracts tells a worker to search the record before reading a file whole**,
> is a 14×-measured unexercised lever; minting a node for it would pre-empt node 129's decision on the same corpus,
> so it is reported there and here instead.

## What this node's work invalidates

**Node 52, flag `52.1`, partially contradicted.** In the worker's words:

> It states the worker "could not" measure tokens: *"no `python3` and no tokenizer in the sandbox"*. **`python3` is
> present** — 3.13.15, at `/home/mathieu/.nix-profile/bin/python3`. **The tokenizer half stands and the conclusion is
> unaffected:** `tiktoken`, `transformers`, `tokenizers` and `sentencepiece` are all absent and `pip` is absent, so
> no tokenizer count is available and the nominal 4.0 ratio remains the only route. What is wrong is the stated
> *reason*, and it matters only because a later node reading that flag would wrongly conclude this machine has no
> Python.

**Node 52's corpus table is superseded by growth, which is an update rather than a contradiction.** In the worker's
words:

> Its "all 54 node files 982,260" is now 136 files and 2,356,865 bytes; "all eight shipped files 97,469" is now nine
> files and 149,030 bytes. The current figures are in section 3 beside the old ones.

***The manager's note.*** Both are carried onto node 52 as annotations rather than edits, the never-delete rule
holding. Neither reaches `map.md`, which quotes no size figure of its own.

## Retrospective — attempt 1

*Pasted as the worker wrote it.*

**What I had to hunt for that the spawn or node could have told me.** Two things, both cheap to have supplied. First,
**that this machine has no `node` and no `bun`** — the single fact that decides clause 1's "whether it runs here",
found in one `command -v` sweep, and neither the node nor the spawn hinted the answer might be *no*. Second, **the
record's current sizes**. The spawn gave me `map.md` at 40,344 bytes from node 113 and node 52's table via the node
file; both were stale, and I had to re-measure everything (map now 42,566; 136 nodes not 54). A spawn that carried a
current three-line size table would have saved a full round.

**What I read and did not use.** `map.md` in full — **42,566 bytes, 42% of my mandated read** — to act on four
things: ground rule 1, the no-external-plugin direction, the token-priority rule with its "token maxing in reverse"
warning, and the label-vocabulary line. About 4,000 bytes of 42,566, so **~90% of the largest file I read was
unused**, which is the seventh-plus instance of the complaint this node was partly about. I also read node 52 whole
(25,295 bytes) for perhaps six facts. **Both are the mandatory class I concluded qmd cannot help with** — I could not
have queried for ground rules I did not know existed — so this is not a self-refutation, but it is the measurement,
taken on myself: the two reads I could not avoid were 66% of my intake.

**What I did *not* read whole, and what that shows.** `decisions.md`. One `grep` returned the four lines I needed. The
spawn warned me three workers had read it whole to use four lines and I simply did not, which is where this node's
central finding came from. **The lever was found by using it, not by researching it.**

**What would have made this node easier.** A one-line statement in the spawn of what `map.md` lines a *research*
worker on this node actually needs. The spawn came close — it told me which constraint would likely decide the node —
and then still required the whole file to confirm the constraint's wording. The manager's note was otherwise unusually
good: naming the ground-rule collision in advance let me go looking for the packaging fact
(`.claude-plugin/marketplace.json`) that turned a predicted collision into a documented one.

**What I found stale, wrong, or contradicting something else.**

1. **Flag `52.1`'s "no python3"** — wrong now, detailed under `INVALIDATIONS`.
2. **The spawn's claim that node 52's index entry "does not mention the fact that makes it relevant" is half right,
   and the half that is wrong cost me a read.** The entry *does* name the fact most relevant to me — *"`map.md` at
   ~19.8k tokens dominates that payload"*. What it omits is the **five-minute TTL**, which my node's clause 2 names.
   So the warning was right about the *cap being lossy* and wrong about *which fact was missing*, and I read node 52
   whole partly to find out which. A worker reported the shape of this problem; the report then propagated slightly
   off-target — the same pattern node 52's own annotation names, where "an unestablished claim hardened by
   repetition."
3. **`map.md`'s ~19,840-token figure is quoted live in my own node file's clause 2** and is stale by a factor of ~1.9,
   the file having been restructured since. Node 52's table is correctly dated where it sits; the node file that
   *quotes* it is not. **Restating a measurement in a second file is where the staleness entered** — which is
   standing rule 2's exact prohibition, "an item states its current form and cites the nodes that shaped it; it does
   not restate what they hold."
4. **`map.md`'s growth is measurable and monotonic**: 26,971 after node 59's restructure, 40,344 at node 113,
   **42,566 now**. It has recovered 58% of what the restructure removed. Node 136's business, noted only because I
   measured it.

***The manager's note on the retrospective, and not the worker's.*** **Its finding 2 is a correction of me and I
accept it.** My spawn said node 52's index entry does not mention the fact that makes it relevant; the entry does name
the token-dominance fact, and what it omits is the TTL. That is a **fifth** instance this session of my stating more
in a spawn than the record supported, and the worker paid for it with a 25,295-byte read. **Its finding 3 is a defect
in a node file the manager wrote**, quoting node 52's map figure rather than citing it, and it is the standing writing
rule's own prohibition applied to a node rather than to the map — the first time anyone has pointed that rule at a
node file. **Its first two retrospective asks are the same ask two other workers have now made** and the manager has
still not minted: that a spawn carry facts the runtime can simply tell you.
