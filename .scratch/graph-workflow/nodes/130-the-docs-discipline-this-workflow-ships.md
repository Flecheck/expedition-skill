# The docs discipline this workflow ships instead of depending on one

Type: grilling
Status: claimed

Blocked by: none

## Question

*The human's own request, `verbatim`, arriving as part of a wider direction about depending on an external plugin.
**Minted by the manager and not surfaced by any worker.** The rest of that direction is on [node
113](113-whether-the-method-skill-instruction-does-any-work.md).*

> Add grilling directly on the skill and for the docs part we should make something. Inspired by "/domain-modeling"
> and https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

**What this node holds, and what it does not.** *"Add grilling directly on the skill"* is [node
113](113-whether-the-method-skill-instruction-does-any-work.md)'s subject and stays there. **This node is the second
half: what the workflow ships in place of `/domain-modeling`.** Nothing of the kind exists, and no node reached it.

**What has to be decided.** What the docs discipline is *for* in this workflow — the two candidates the record
already implies are keeping a glossary true as terms move, and writing the record so a later agent can find one fact
in it, which is [node 129](129-what-to-do-about-the-records-token-cost.md)'s subject from the other side. Whether it
is one document or two. Whether it ships as a worker contract, as a section of one, or as its own skill. And which
worker kinds it binds — `/domain-modeling` is named by the grilling contract today and by nothing else, while the
glossary it maintains is read by every kind.

**The two sources the human named**, to be read rather than paraphrased: `mattpocock-skills:domain-modeling`, and the
gist at the URL above. **Neither is authoritative here** — the human said *"inspired by"*, which the manager reads as
evidence rather than as a specification, and marks that reading as the manager's.

## The manager's note at filing

*Not a change to anything above.*

**One fact from an hour ago that bears directly on this and that the human has not seen.** [Node
113](113-whether-the-method-skill-instruction-does-any-work.md)'s worker invoked `/domain-modeling` and reported that
**it excludes its own reader in its opening paragraph** — *"merely reading `CONTEXT.md` for vocabulary is not this
skill… this skill is for when you're changing the model, not just consuming it"* — and that of its six operative
instructions, two write files and three speak to the human, all of which a worker is forbidden to do. **One was
runnable, and running it found two real defects in `CONTEXT.md`.** So the thing this node is asked to be inspired by
is, on measurement, one usable instruction out of six for this workflow's readers.

**The manager has not read the gist**, that being this node's work.

## What the human added after this node was minted

**Their words, `verbatim`:**

> For node 130, qmd is also relevant.

and, in the following message:

> (qmd is a local seach engine)

***The manager's note.*** So this node is not only about a glossary discipline. **A docs discipline that assumes a
local search engine is a different document from one that does not** — the first can say *find the term* where the
second must say *where the term is written down*. **And it collides with ground rule 1**, which forbids a shipped
file to assume this repo, this machine or a toolchain: a discipline that depends on a search engine being installed
is exactly that. Whether the discipline may assume it, must degrade without it, or must not mention it is part of
what this node decides.

**Sequencing this creates, and the manager has not resolved it.** [Node
128](128-whether-qmd-lowers-this-workflows-token-cost.md) establishes what `qmd` is and [node
129](129-what-to-do-about-the-records-token-cost.md) decides whether the workflow adopts it. **This node's answer
turns on that** — but the human minted this node's subject before either existed, and did not say it waits. **The
header carries no `Blocked by:` edge**, because adding one is a claim about what this node needs that only its own
worker or the human can make. It is named here instead.

## A second addition from the human, widening what this node reads

**Their words, `verbatim`:**

> for node 130, for the github link there are also some implementation in the comments and more generally there was a
> lot of inspiration taken from it on a lot of projects, so it might be interesting to look at what was done more
> globally

***The manager's note.*** **This widens the node's sources and does not change its question.** What it adds: the
gist's own comment thread, which they say carries implementations, and the derivative work across other projects.
**None of it is authoritative** — they said *"it might be interesting"*, which the manager reads as an instruction to
look rather than a claim about what will be found, and marks that reading as the manager's.

**What it changes about how this node should be worked, and the manager has not decided it.** A survey of what other
projects did with one idea is **research**, and this is a `grilling` node. Three routes exist and the manager has
taken none: whoever takes this node dispatches a subagent for the survey, which its contract permits and node 113's
answer now states in the grilling contract's own discipline; or a `research` node is minted ahead of it and this one
blocks on it; or the survey is skipped and the node decides from the two sources already named. **The first is the
cheapest and the node's own worker can choose it without anyone's permission.**

## A third addition from the human, and it is about packaging rather than content

**Their words, `verbatim`:**

> for the doc we should try to put it as a "plugin" so that the skill can be used without it or the doc by itself.

***The manager's note.*** **This is a shape constraint on whatever this node produces, and it is the first one this
node has.** The two earlier additions widened what this node reads; this one says what the result must be able to do:
**the expedition skill works without the docs discipline, and the docs discipline works without the expedition
skill.** Their word `plugin` is in quotation marks in their own message, so it names the property — separately
installable, separately usable — rather than necessarily the Claude Code plugin mechanism.

**How it sits against the standing preference already in the map.** That preference says the shipped files must not
depend on the `mattpocock-skills` plugin. **This is not in tension with it**: what they refuse is *depending on
somebody else's plugin*, and what they ask for here is *shipping this effort's own docs discipline so that nothing
depends on it either way*. Both are the same property — no shipped file requires a second thing to be present.

**What it reaches that the manager can name, and has decided none of it.** Ground rule 1 (nothing shipped may assume
this repo, this machine, or a toolchain) already bears on anything installable. [Node
128](128-whether-qmd-lowers-this-workflows-token-cost.md) established that a Claude Code plugin can carry skills and
an MCP server, and that a plugin is a **harder** dependency than a skill where it needs a binary — which is evidence
about what a plugin costs, gathered for a different question. And [node
138](138-where-the-rules-a-checker-is-held-to-live.md) is deciding where a rule set lives and who is handed it, which
is the same shape of question about a different body of text.

**One thing this does not settle and node 138 now owns for every direction of theirs:** whether it binds the shipped
files or this effort only. The manager has again recorded a direction of theirs without putting that to them.

*The manager's note, 2026-09-27:* [node 56](56-ship-the-glossary-into-the-skill-set.md)'s worker reports this node's question is changed, once node 56 lands. Its words, pasted: Node 130 (open), question partly answered: "keeping a glossary true as terms move" is now stated in the glossary itself.

## Interview


#### Questions 1 and 2, relayed 2026-10-02

*Pasted as the worker handed it back.*

`````
NODE:          The docs discipline this workflow ships instead of depending on one (node 130)

ABOUT:         You asked for the shipped skills to stop depending on mattpocock-skills. You also said that "for the docs part we should make something", inspired by `/domain-modeling` and Karpathy's LLM-wiki gist, that qmd is relevant, and that it should be a "plugin" so that each of the two can be used without the other. This node decides what that "something" is. Node 113 has already removed the shipped contracts' invoke-a-skill lines, and node 56 has already shipped the glossary. So this is the last open piece of the no-mattpocock direction. Node 135 (repointing `map.md`'s skill line) is waiting on it.

SO FAR:        What I read and found:
                - **No shipped file names `/domain-modeling` any more.** I grepped `.claude/` and found nothing. It survives only in this effort's `map.md` line "Skills every session should consult", which node 135 repoints once this node resolves.
                - **Two parts of the job are already shipped.** Keeping the workflow's own glossary true: the glossary's opening paragraph now says it covers every term, that coining a term and writing its entry are one change, and that an entry gives the meaning while the rule lives in a contract (node 56). Making the record findable: the five worker contracts say to search the record before reading any file whole (node 129).
                - **What `/domain-modeling` contains.** It keeps a repo's `CONTEXT.md` glossary (bold term, a 1–2 sentence meaning, an `_Avoid_` line) and writes ADRs, only where a decision is hard to reverse, surprising, and a real trade-off. It creates both files lazily. Node 113 measured it: of its six instructions, two write files and three speak to the user. A worker is forbidden to do either, so one instruction was usable.
                - **What the gist contains.** I read it through WebFetch, which returns a summary, not the verbatim text. A curl route to the raw text was refused by the permission system. I read it because your own words ask for the gist and its comments to be looked at, and my contract lets me find facts from the environment. The idea: an LLM keeps a markdown wiki that sits between raw sources and the reader. It has three layers (sources, wiki, and a schema file such as CLAUDE.md) and three operations: ingest, query, and lint (contradictions, stale claims, orphan pages, missing links). It keeps an `index.md` (one line per page) and an append-only `log.md`. qmd is named as an optional search tool.
                - **What the derivative projects did.** A subagent surveyed 8 codebase-oriented derivatives, also through WebFetch summaries. Almost all keep the index, the log and ingest/query/lint. Several add an ADR or decisions folder and rules on who may write which files. Only one has a literal glossary. Nearly all treat search engines (qmd, vectors) as optional and fall back to grep, and one says grep is more reliable at wiki size. One (praneybehl/llm-wiki-plugin) is explicitly built to work alone and alongside another plugin.
                - **What nothing in the workflow covers today:** a host repo's own lasting vocabulary and decisions. An expedition's record lives in `.scratch/<effort>/`. When an expedition runs on another repo (Lang, or a work project), the domain terms and decisions it settles have nowhere lasting to go in that repo.
                - **The workflow already meets such docs without naming them.** The implementation contract's bar includes "whatever else the repo itself demands". So if a repo's agent instructions say "keep docs/glossary.md true", every implementation worker and checker is already held to that, with no edit to any expedition file.
                - **What I settled myself** (raised as ASSUMPTIONs at the end): the survey stays a subagent's work, with no research node minted. Expedition's own `glossary.md` stays governed by its own paragraph and is not moved into the new thing.

Q1. What the docs discipline is, and how it ships
ASK:           Should the "something" be a small standalone skill for a repository's own lasting docs that no expedition file names, or should we ship nothing new because the glossary paragraph and the record-search rule already cover the workflow?
RECOMMENDED:   **A standalone skill, working name `/repo-docs`, in one `SKILL.md` of about 60 lines at `.claude/skills/repo-docs/`.** It references no expedition file, and no expedition file references it. That gives the property your "plugin" asks for: copy the directory alone and it works, or leave it out and Expedition works. Its contents:
                - **Files.** First find what the repo already has (its agent instructions, an existing `CONTEXT.md` or `docs/`). Otherwise create these lazily:
                  - a glossary in the shape both sources and our own glossary share: bold term, colon, a 1–2 sentence meaning, `_Avoid_` line.
                  - one-paragraph decision records, written only under `/domain-modeling`'s three tests.
                  - an index with one line per page, from the gist.
                - **No `log.md`.** Git history already is the append-only log.
                - **Three operations, following the gist's three:**
                  - *Write with the change:* a term or decision that settles gets its entry in the same change.
                  - *Find:* read the index, then search before opening a page whole.
                  - *Check:* report, without fixing, any term used with no entry, any `_Avoid_` word in use, any page the code contradicts, any index line with no page or page with no index line, and any decision overturned without being marked.
                - **Who may write.** Only an agent allowed to write files. An agent that may not write runs Find and Check and reports what it would write. No instruction speaks to the user. These two rules fix the defect node 113 measured, so an expedition worker can actually use it.
                - **What changes on the Expedition side.** Nothing shipped. The two meet through the host repo's agent instructions, which the bar already honours. Node 135 repoints this effort's map line from `/domain-modeling` to `/repo-docs`.

                Why this one: it is the only option that delivers "the doc by itself" as you asked. It adds no lines to the contracts you want compacted. And it covers the one gap left, the host repo's lasting docs, which neither node 56 nor node 129 reaches.
ALTERNATIVES:  - Ship nothing new; node 135 just drops `/domain-modeling` from the map line. Smallest, but it gives no "doc by itself" and leaves host repos' decisions stranded in `.scratch`.
               - A `## How you keep the docs` section inside the contracts, the way node 145 shipped checking. This fails your packaging direction, because the docs could not be used without Expedition.
               - The full Karpathy wiki (raw-sources layer, entity pages, `log.md`, a compile step). Larger than the compaction you asked for, and git already provides the log.
               - A Claude Code plugin manifest. A self-contained skill directory already has the property. Packaging the whole skill set as a plugin would be a separate question.
               - Other names: `/docs-keeping`, `/repo-wiki`. I avoided "project" because our glossary refuses it as a word for an effort.

---

Q2. Whether the shipped text may name qmd
CONTEXT:       Ground rule 1 forbids a shipped file to assume a toolchain. Nodes 128 and 129 kept qmd out of the shipped files on that ground, and flag 129.1 records that nobody ever asked you whether you would relax ground rule 1 for a tool. Your "qmd is also relevant" is the first sign that you might. The answer is the same wherever the text lands.
ASK:           May the docs discipline's shipped text name qmd, or should it describe search only as a property ("search with the best search the environment provides")?
RECOMMENDED:   **Describe it as a property and name no product.** For example: "search the docs before opening a page whole, using whatever search the environment provides, a local search engine if one is installed, otherwise plain text search." qmd is used whenever it is present, and nothing breaks or goes stale when it is absent or replaced. This matches ground rule 1, nodes 128 and 129, and what most of the surveyed derivatives do: search engine optional, falling back to grep.
ALTERNATIVES:  - Name qmd as an optional example with a grep fallback. It assumes nothing, but it ties a shipped file to one product and its install steps (Node 22, Bun, about 2 GB of models).
               - Require qmd. This breaks ground rule 1 and makes the skill a harder dependency than the plugin you asked to drop.

RETROSPECTIVE:
1. What I had to hunt for: where `/domain-modeling` physically lives (a nix store path, found with `find`). Whether reading the URL was allowed: the contract says only "the tree or the environment", the manager's note made it conditional, and the permission system refused one route and allowed another.
2. What arrived that this node did not need: most of `decisions.md`. Only about six lines bore on this node (56, 113, 128, 129, 132, 145). The map's worktree and landing items bore on nothing.
3. What would have made this easier: a spawn naming nodes 145 (the precedent of shipping a discipline as a section) and 135 (the node waiting on this one). I found both by search. A stated rule on whether a grilling worker may fetch a URL the human named would also have helped.
4. What was stale, wrong or contradictory: the manager's note says the contract states whether I may read outside the working directory, and it does not say so explicitly. `map.md`'s "Skills every session should consult" line still names `/domain-modeling` (node 135's expiry, as expected). The node's question frames one candidate purpose as "keeping a glossary true as terms move", which node 56 has since shipped, as the node's own last annotation says.
`````
