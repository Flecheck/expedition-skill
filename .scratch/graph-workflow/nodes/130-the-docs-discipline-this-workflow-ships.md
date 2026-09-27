# The docs discipline this workflow ships instead of depending on one

Type: grilling
Status: open

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
