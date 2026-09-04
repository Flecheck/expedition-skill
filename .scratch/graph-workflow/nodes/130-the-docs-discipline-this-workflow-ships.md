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
