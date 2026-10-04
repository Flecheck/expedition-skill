# The docs discipline this workflow ships instead of depending on one

Type: grilling
Status: resolved

Blocked by: none

## Answer

The workflow ships `/repo-docs`, a standalone ~50-line skill keeping a repo's glossary and decision records, reviewed with each change, searched with grep; Expedition never names it.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. It surfaced [node 383](383-ship-the-repo-docs-skill.md), which ships the skill. Its `INVALIDATIONS` extend nodes 113 and 145 and narrow nodes 128 and 129 consistently. Its `CONDITIONS` report that node 135's trigger is now node 383's landing, and the manager moved that edge. Flags 130.1, 130.2, 130.3, 130.4 settle at the node closing report.

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

#### The human's answer to questions 1 and 2, 2026-10-04

`verbatim`: *"I think the proposition is ok, but there should be research done on what other people do, there was quite a few project that tries to make Karpathy's LLM-wiki and similar, I want to know what they did before choosing"*

*The manager's note:* **a divergence.** The reply does not take the `RECOMMENDED` now. It finds the proposition acceptable and asks for research on what other projects built on Karpathy's LLM-wiki, and similar ones, did before a choice is made. It names neither question, so the manager reads it as covering both, and the worker holding the interview decides how to proceed. The payload had reported a survey of 8 derivatives done through fetch summaries by a subagent of the worker.

#### Questions 1 and 2 again, with the research, relayed 2026-10-04

*Pasted as the worker handed it back. The manager rebuilt the first two lines, the `NODE:` line and the `ABOUT:` label, which its extraction key cut; every other word is the worker's.*

`````
NODE:          The docs discipline this workflow ships instead of depending on one (node 130)

ABOUT:         This node decides what replaces `/domain-modeling`, so that the shipped skills stop depending on mattpocock-skills. You found the earlier proposal (a small standalone `/repo-docs` skill, and qmd described only as a property) ok in principle. You asked to see what other projects built on Karpathy's LLM-wiki, and similar ones, did before choosing. Below is that research, then the same two questions with the proposal revised where the research moved it.

SO FAR:        **How the research was done.** Three subagents ran in parallel. The first read the gist's whole comment thread through the GitHub API. The second searched for LLM-wiki implementations aimed at code repositories and coding agents. The third surveyed similar patterns that coding agents use to keep a repo's docs: Cline Memory Bank, Kiro steering, spec-kit, BMAD, Claude Code memory, AGENTS.md, Serena, Basic Memory, claude-mem, ADRs/MADR, and Matt Pocock's own doc page for `/domain-modeling`. Most per-project detail came through WebFetch, which returns a summary rather than the raw text. Star counts and the comment-thread counts were read directly from the API. I checked the `/domain-modeling` quotes below against the installed file myself.

               **Scale.** The gist has 1,132 comments. 625 of them link an implementation: 391 distinct repos and 41 gists, about 430 in all. Most are personal research notebooks fed by outside sources. Only a minority keep a software repo's own docs. The ones read in detail are listed by name and star count:
               - LLM-wiki skills and plugins: Astro-Han/karpathy-llm-wiki 2.4k, ussumant/llm-wiki-compiler 325, kfchou/wiki-skills 186, praneybehl/llm-wiki-plugin 116.
               - Codebase-oriented: giodra96/project-wiki, junbjnnn/llm-wiki, eliavamar/repositories-wiki, narailabs/doc-wiki, theafh/ai-modules, LARIkoz/eidetic.
               - The most-starred implementation of all is AgriciDaniel/claude-obsidian at 15.3k, an Obsidian vault manager rather than repo docs.

               **What they keep from the gist.** Almost all keep:
               - immutable raw sources, the wiki, and a schema file (AGENTS.md or CLAUDE.md);
               - an `index.md` and an append-only `log.md`;
               - ingest, query and lint.

               Two refinements:
               - kfchou generates its index from the pages and gitignores it: "the index is generated, not hand-maintained".
               - The most-used projects cap page size and have lint enforce the cap.

               **What they add.** The largest addition, across the whole thread, is control over what gets written back:
               - review of a write plan before it is applied (claude-obsidian);
               - contradictions surfaced for a human rather than resolved automatically (theafh);
               - only the human may mark a page verified, enforced by a hook (chrislemke);
               - agent-written content counted at half weight until a human promotes it (eidetic).

               Lint converges on broken links and orphan pages, schema or format violations, and staleness. Only a few check contradictions or drift as a first-class step.

               **Search.** Grep is the default nearly everywhere. Astro-Han, the most-starred skill, says "grep and read are more reliable" at its scale. Where qmd is named (junbjnnn, rarce/git-wiki, ussumant) it is an optional speed-up for 50–100+ pages, with grep as the fallback.

               **What was found against building a big code wiki.** narailabs/doc-wiki published a benchmark with no lift: an autonomous ticket-fix pass rate of 57/92 without the wiki against 54/92 with it. It also withdrew an earlier, more favourable benchmark.

               **The similar, non-wiki patterns** split docs three ways:
               - what stays stable (product and tech context, or a glossary);
               - what is happening now (progress or active context);
               - why something was chosen (decision records).

               Every system that reads all its docs at the start of a session (Cline Memory Bank, Claude Code memory, BMAD) has had to add a size cap or split files once the docs grew. Almost none checks for stale content automatically. Writes happen either on an explicit command or inline when something is settled. ADRs are never edited once accepted: a new record supersedes the old one, which matches this workflow's never-delete rule.

               **`/domain-modeling`'s own documentation** names three problems, verified in the installed file:
               - "the file turns into a running spec. This is the most-reported problem with the skill, across several models".
               - Automatic invocation is "the weakest part of the skill".
               - "an unreviewed, agent-authored glossary is worse than none: it becomes confident-sounding lore".

               **What I conclude for this choice:**
               - The surveyed projects confirm writing at the moment a term or decision is settled, decision records that are superseded rather than edited, and grep as the default search.
               - They argue against a hand-kept index, pages that describe the code, and any agent write that no human reviews.
               - The standalone shape still stands. A skill copied in alone and composing with other workflows is common (praneybehl, Serena, Astro-Han).

Q1. What the docs discipline is, and how it ships
CONTEXT:       The same question as before. The recommendation is revised in three places, each marked "changed" below with the finding behind it.
ASK:           Should the docs discipline be a small standalone skill for a repository's own lasting docs that no expedition file names, or should we ship nothing new?
RECOMMENDED:   **A standalone skill, working name `/repo-docs`, in one `SKILL.md` of about 50 lines at `.claude/skills/repo-docs/`.** No expedition file names it, and it names none. Copied in alone it works, and left out Expedition works. The two meet through the host repo's agent instructions, which the implementation bar already enforces ("whatever else the repo itself demands"). Its contents:
               - **Only what the code cannot tell a reader** (changed). It holds a glossary (bold term, a 1–2 sentence meaning, an `_Avoid_` line) and decision records (one paragraph each, written only when a decision is hard to reverse, surprising, and a real trade-off). It holds no pages describing the code, because doc-wiki measured no lift from one.
               - **No hand-kept index and no `log.md`** (changed). The glossary is one file and a decision file's name carries its number and title, so the directory listing serves as the index and git as the log. That removes a file that has to be kept in sync and that a check would have to watch, which is the reason kfchou generates its index.
               - **Write with the change.** A term or decision that settles gets its entry in the same change. A superseded decision is never edited: a new record names the one it replaces.
               - **Every write is reviewed** (changed). A docs edit goes in a change the human reviews, like code, and is never a side write. An agent that may not write files only searches and checks, and reports what it would write. This answers both the "confident lore" warning and the thread's main addition.
               - **Check, which reports and does not fix:**
                 - a term used with no entry;
                 - an `_Avoid_` word in use;
                 - a glossary entry that states a rule or an implementation detail, which is the running-spec guard;
                 - an entry the code contradicts;
                 - a decision overturned without a superseding record.
               - **Nothing speaks to the user.**
               - **On this effort.** Node 135 repoints `map.md`'s skill line from `/domain-modeling` to `/repo-docs`.
ALTERNATIVES:  - Ship nothing new and drop `/domain-modeling` from the map line. This gives no "doc by itself", and host repos' decisions stay stranded in `.scratch`.
               - Keep a hand-maintained `index.md` and a `log.md` as the gist does. Most implementations keep both, but for a glossary plus numbered decision files they duplicate the listing and git, and add something to drift.
               - Follow the gist fully: raw-sources layer, topic pages, ingest/query/lint over a code wiki. This is the common shape in the thread, but doc-wiki's benchmark measured no gain for coding work, and it is the size you asked to avoid.
               - A section inside the expedition contracts, as node 145 did for checking. That fails your packaging direction.
               - A Claude Code plugin manifest. Not needed for the property, and packaging the whole skill set as a plugin is a separate question.

---

Q2. Whether the shipped text may name qmd
CONTEXT:       The same question as before, now with the field's practice behind it. Ground rule 1 forbids a shipped file to assume a toolchain.
ASK:           May the docs skill's text name qmd, or should it describe search only as a property?
RECOMMENDED:   **As a property, naming no product.** For example: "search before opening a file whole, using the best search the environment provides: a local search engine if one is installed, otherwise plain text search". qmd is used when present, and the skill keeps working when it is absent or replaced. The research supports this. Grep is the default nearly everywhere, the most-starred skill says grep is more reliable at wiki size, and projects that name qmd treat it as optional above 50–100 pages. A glossary and a set of decision records stay well under that size.
ALTERNATIVES:  - Name qmd as an optional speed-up with a grep fallback, as junbjnnn and rarce do. It assumes nothing, but it ties a shipped file to one product (Node 22, Bun, about 2 GB of models), and at this skill's size it would never be needed.
               - Require qmd. This breaks ground rule 1.

RETROSPECTIVE:
1. What I had to hunt for: a route to the gist's raw text and comments. My own curl to the GitHub API was refused by the permission system. A subagent reached the same API and read the full thread, which is how the comment counts are exact.
2. What arrived that this node did not need: nothing new this round. The manager's message was short and every claim in it checked out: the answer is recorded under `## Interview`, marked a divergence, and names neither question.
3. What would have made this easier: knowing at the first round that you would want the survey shown rather than summarised. The first payload gave the survey five lines. A rule that a worker who relies on a survey presents its findings to the human would have saved this round.
4. What was stale, wrong or contradictory: the first survey (WebFetch summaries) is partly superseded. A subagent reported that two WebFetch calls on the same gist page returned different, partly non-matching comment summaries, and the API enumeration replaces them. Those were notes I had marked as not verbatim.
`````

#### The human's answer to questions 1 and 2 (second relay), 2026-10-04

`verbatim`: *"q1 ok q2 just use grep for now"*

*The manager's note:* Q1 takes the worker's `RECOMMENDED`, the standalone `/repo-docs` skill of about 50 lines as revised after the research. **Q2 is a divergence.** It takes neither the `RECOMMENDED` ("As a property, naming no product") nor either alternative: it says to use grep, "for now".

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      The docs discipline this workflow ships instead of depending on one

ANSWER:        **The workflow ships a small standalone skill, `/repo-docs`, at `.claude/skills/repo-docs/SKILL.md`. It keeps a repository's own glossary and decision records true as work changes them, and it searches with grep.** No expedition file names it, and it names no expedition file. A repo can use either one without the other, which is the property the human's "plugin" asked for. The two meet only through the host repo's own agent instructions. The implementation contract's bar already holds work to those ("whatever else the repo itself demands"), so no expedition contract changes. Settled by the human, `verbatim`: *"q1 ok q2 just use grep for now"*. That came after their first reply, `verbatim`: *"I think the proposition is ok, but there should be research done on what other people do, there was quite a few project that tries to make Karpathy's LLM-wiki and similar, I want to know what they did before choosing"*.

               **What the skill holds, as approved (Q1, the worker's recommendation as revised after the research):**
               - **Only what the code cannot tell a reader.** That means a glossary and decision records, and no pages describing the code.
                 - Glossary entries: a bold term, a meaning of one or two sentences, and an `_Avoid_` line.
                 - Decision records: one paragraph each, written only where a decision is hard to reverse, surprising without context, and a real trade-off.
               - **Files.** The agent first finds where the repo already keeps these. It creates a file only when it has a first entry to write.
               - **No index file and no log file.** The directory listing and version-control history serve for both.
               - **Write with the change.** A term or decision settled in a change gets its entry in that same change.
               - **Decisions are superseded, never edited.** A new record names the one it replaces.
               - **Every docs edit is reviewed.** It goes in a change the human reviews with the rest of the work. An agent that may not write files only searches and checks, and reports what it would write.
               - **Check, which reports and does not fix:**
                 - a term used with no entry;
                 - an `_Avoid_` word in use;
                 - a glossary entry that states a rule or an implementation detail;
                 - an entry the code contradicts;
                 - a decision overturned with no superseding record.
               - **Nobody is addressed.** No instruction tells the agent to ask the user anything.

               **Search (Q2): grep, "for now".** This is a divergence from the worker's recommendation, which was to describe search as a property and name no product. The skill names grep and names no search engine. "For now" is not carried into the shipped text. Revisiting qmd stays on the record's existing route: node 129's trigger, a worker reporting it could not find a fact because it did not know the fact's wording.

               **What the choice rests on.** Two sources were read: `/domain-modeling` (the installed skill and its own doc page) and Karpathy's LLM-wiki gist. Three surveys of what others built were run, and their results went to the human in full on the second relay (recorded under `## Interview`):
               - The gist thread holds 1,132 comments linking about 430 implementations, counted through the GitHub API.
               - Codebase-oriented LLM-wiki skills and plugins.
               - Similar agent-kept docs: Cline Memory Bank, Kiro steering, spec-kit, BMAD, Claude Code memory, AGENTS.md, Serena, Basic Memory, claude-mem, ADRs/MADR.

               Most per-project detail came through WebFetch summaries. The decisive findings:
               - grep is the default search nearly everywhere.
               - The field's main addition to the gist is control over what an agent writes back.
               - One codebase-wiki benchmark showed no lift from the wiki (narailabs/doc-wiki, 57/92 without against 54/92 with).
               - `/domain-modeling`'s own doc names its most-reported failure, the glossary becoming "a running spec". It also warns that "an unreviewed, agent-authored glossary is worse than none".

               **What this node does not change.** The expedition skill's own `glossary.md` stays governed by its own opening paragraph (node 56) and is not brought under `/repo-docs`. The record-search rule in the worker contracts (node 129) is untouched.

INDEX LINE:    The workflow ships `/repo-docs`, a standalone ~50-line skill keeping a repo's glossary and decision records, reviewed with each change, searched with grep; Expedition never names it.

FLAGS:         ASSUMPTION — *Node:* The research the human asked for was done inside this attempt by three of my own subagents, and no `research` node was minted. I read their reply as the contract's "go read X first" row, which says to read and then continue with the same questions. The findings went to the human in full in the second payload before they chose. Fetching from the web rests on two things: the contract's "find facts from the tree or the environment", and the human's own direction to look at the gist, its comments and derivative work. One route, my own curl to the GitHub API, was refused by the permission system. *Index:* Node 130's survey of LLM-wiki derivatives was run by its own worker's subagents and shown to the human before they chose; no research node was minted.

               ASSUMPTION — *Node:* Expedition's own `.claude/skills/expedition/glossary.md` is not brought under `/repo-docs`. It stays governed by its own opening paragraph, which node 56 shipped. `/repo-docs` is for a host repository's lasting docs, and tying the two together would break the property that each works without the other. *Index:* `/repo-docs` does not govern Expedition's own glossary, which stays under its own completeness paragraph so the two remain independent.

               ASSUMPTION — *Node:* I read "just use grep for now" as follows. The shipped skill names grep as its search and names no search engine or embedding tool. "For now" stays out of the shipped text, because a promise of later change in a shipped file would date it. Revisiting rests on node 129's existing qmd trigger in the record. I did not add "or an equivalent plain-text search" to the condition as a demand; the worker may add it. *Index:* "just use grep for now" became a skill that names grep and no engine; "for now" lives only in the record, via node 129's qmd trigger.

               ASSUMPTION — *Node:* Two details of the condition are mine. First, "about 50 lines" became a cap of 650 words counted by `wc -w`, frontmatter included, because a line count depends on wrap width and a word count does not. Second, the name `repo-docs` is taken as final. The recommendation called it a "working name", and the human's "q1 ok" took the recommendation without renaming it. *Index:* `/repo-docs` keeps its working name as final and its ~50-line size became a 650-word cap; both were the worker's renderings of the approved option.

NEW NODES:     **Ship the `/repo-docs` skill**
               Kind: implementation
               Question: Write the standalone docs skill node 130 settled, as one new file, `.claude/skills/repo-docs/SKILL.md`.
               Blockers: none.
               Acceptance condition:
               > Done when all of the following hold.
               >
               > 1. The file `.claude/skills/repo-docs/SKILL.md` exists and is the only file in the directory `.claude/skills/repo-docs/`. It opens with YAML frontmatter holding `name: repo-docs` and a `description` saying the skill is for keeping a repository's glossary and decision records true as work changes the repository.
               > 2. The file is at most 650 words as counted by `wc -w .claude/skills/repo-docs/SKILL.md`, frontmatter included.
               > 3. The file stands alone. `grep -n -i -E 'expedition|mattpocock|domain-modeling|qmd|\.scratch' .claude/skills/repo-docs/SKILL.md` returns nothing. The file names no other skill and tells the reader to read no file outside the repository it is working in, apart from that repository's own files. `grep -rn 'repo-docs' .claude/skills/` returns matches only inside `.claude/skills/repo-docs/`.
               > 4. Before anything is created, the file tells the agent to find where the repository already keeps a glossary and decision records, and to use those: its agent instructions files (such as `AGENTS.md` or `CLAUDE.md`), an existing glossary file, an existing directory of decision records. It names one default path for a glossary and one default directory for decision records, both relative to the repository root, to be used only when that search finds none. It tells the agent to create a file only when there is a first entry to write in it.
               > 5. The file keeps two kinds of content and no others.
               >    - A glossary. Each entry is a term in bold followed by a colon, a meaning of one or two sentences, and a line beginning `_Avoid_` listing rejected synonyms. The file says a glossary entry states what a term means and holds no rule, no implementation detail and no specification.
               >    - Decision records. Each is one file, about a paragraph long, whose file name carries a sequential number and a title. The file says a decision record is written only when all three hold: the decision is hard to reverse, it would surprise a reader who lacks the context, and it was the result of a real trade-off between alternatives.
               >    - The file says the skill keeps no pages describing what the code does.
               > 6. The file tells the agent to create no index file and no log file, and says the directory listing and the version-control history serve those purposes.
               > 7. The file tells the agent that a term or decision settled in a change gets its glossary entry or decision record in that same change.
               > 8. The file says an accepted decision record is not edited to change the decision. A changed decision gets a new record that names the record it replaces.
               > 9. The file says every edit to these docs goes into a change that the human reviews together with the rest of the work, never as a separate write. It says an agent not permitted to write files only searches and checks, and reports the entries it would write.
               > 10. The file tells the agent to search with grep before opening a file whole. It names no other search tool, search engine, index or embedding tool.
               > 11. The file gives a check operation that reports and fixes nothing. The check reports each of these five:
               >     - a term used in the repository with no glossary entry;
               >     - a word listed on an `_Avoid_` line in use for that term's meaning;
               >     - a glossary entry that states a rule or an implementation detail;
               >     - a glossary entry or decision record that the code contradicts;
               >     - a decision overturned with no record superseding it.
               > 12. The file contains no instruction to ask the user anything, to address the user, or to wait for a reply. What it produces is stated as entries written or a report returned to whoever invoked it.
               > 13. No file outside `.claude/skills/repo-docs/` is changed.
               >
               > Scope: the work creates a file, and the named places are the work rather than instances of a defect. So the scope came from no search. The `grep` commands in clauses 3 and 10 are demands on the finished file, not a scope search.

INVALIDATIONS: No resolved node is contradicted.
               - Extension: [node 113](113-whether-the-method-skill-instruction-does-any-work.md)'s answer names "node 130 ships the docs discipline that replaces `/domain-modeling`" as a forward reference. It now has a referent, `/repo-docs`, shipped by the new node.
               - Extension: [node 145](145-whether-the-workflow-ships-its-own-reviewing-discipline.md)'s answer says the count of separately packaged discipline deliverables "stays at one, and it is node 130's". That deliverable is now named, and it is separately installable as node 145 assumed.
               - Narrowing, consistent: [nodes 128](128-whether-qmd-lowers-this-workflows-token-cost.md) and [129](129-what-to-do-about-the-records-token-cost.md) kept qmd out of the shipped files. This answer keeps it out too, by the human's direction (grep, "for now") rather than only by ground rule 1. Flag 129.1's open point, whether the human would relax ground rule 1 for a tool, was put to them here. They chose grep "for now", which leaves ground rule 1 as it is.
               - Unaffected: [node 56](56-ship-the-glossary-into-the-skill-set.md)'s glossary paragraph stays the discipline for Expedition's own vocabulary.

CONDITIONS:    **What I searched.** The `## Acceptance condition`, `## Question` and `## What must be true when it is done` sections of all 20 open or claimed nodes, for: `domain-modeling`, `repo-docs`, `qmd`, `130-the-docs`, `node 130`, `decision record`, `ADR`, `docs discipline` and `grep`. I also searched them for any glob or count over the shipped skill set (`.claude/skills/*`, `expedition*`, "every skill", "shipped set", "twelve", "eleven"), because the new node adds a skill directory beside the expedition ones.

               **Results.**
               - Nodes 380 and 382 scope their work with `grep ... .claude/skills/*/SKILL.md` for phrases that the new file will not contain, so no clause of theirs becomes wrong.
               - No clause of any unclaimed node's condition is made wrong, so I write no replacement.
               - **Open node whose question changes:** [node 135](135-repoint-the-maps-skill-line-when-its-replacements-land.md) ("Repoint the map's `## Notes` skill line when its two replacements land"). Its question is answered in part: the shipped text that replaces `/domain-modeling` is `.claude/skills/repo-docs/SKILL.md`, invoked as `/repo-docs`.
               - The trigger for node 135 is now the new node's landing, not node 130's resolution. Its `Blocked by: 126, 130` should read `126` plus the new node "Ship the `/repo-docs` skill". That is the manager's edit to make or put to the human.

MISSING FROM MAP: Whether a worker may fetch from the web. The map and the contract are both silent; the contract says only "find facts from the tree or the environment". I relied on that clause and on the human's own direction to read the gist, and the permission system refused one route and allowed another. The map's standing-preferences item on the `mattpocock-skills` direction still says what ships in place of `/domain-modeling` "is" node 130. That stays true as a pointer, and the manager may want it to name `/repo-docs` once the new node lands, which is node 135's subject.

RETROSPECTIVE:
1. What I had to hunt for: where `/domain-modeling` lives on disk (a nix store path). A route to the gist's raw text and comment thread: my own curl was refused, and a subagent later reached the GitHub API. Whether adding a skill directory makes any open condition's glob over `.claude/skills/*` wrong: it does not, after a search.
2. What arrived that this node did not need: most of `decisions.md`, of which about six lines bore on this node (56, 113, 128, 129, 132, 145), and the map's worktree, landing and code-slot items.
3. What would have made this easier: a spawn naming node 145 (the precedent of shipping a discipline) and node 135 (the node waiting on this one). A stated rule on whether a worker may fetch a URL the human named. And knowing from the start that the human wanted a survey's findings shown rather than summarised, which cost one relay.
4. What was stale, wrong or contradictory: the manager's first note said the contract states whether I may read outside the working directory, and it does not say so explicitly. The node's question still lists "keeping a glossary true as terms move" as a candidate purpose, which node 56 had already shipped. My first survey's comment summaries were partly unreliable: two WebFetch calls on one page disagreed. The API enumeration replaced them. Node 135's `Blocked by: 130` now points at the wrong trigger, as stated under CONDITIONS. All claims in the manager's last message checked out against node 130's `## Interview`.
`````

## Flags

`130.1` `ASSUMPTION` **· settled** — The research was run by the worker's own subagents inside this attempt, and no research node was minted. *(The worker's full text is under its handover's `FLAGS`.)*

`130.2` `ASSUMPTION` **· settled** — Expedition's own glossary.md is not brought under /repo-docs. *(The worker's full text is under its handover's `FLAGS`.)*

`130.3` `ASSUMPTION` **· settled** — "just use grep for now" became a skill naming grep and no engine; "for now" stays in the record only. *(The worker's full text is under its handover's `FLAGS`.)*

`130.4` `ASSUMPTION` **· settled** — The working name repo-docs is final, and ~50 lines became a 650-word cap. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-10-04:* flags 130.1, 130.2, 130.3, 130.4 settle at the node closing report that closes this node.
