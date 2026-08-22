# Collapse the manager's discipline onto the leading word `scribe`

Type: implementation
Status: open

## Question

A pretrained one-word token for the manager's whole discipline exists, is correct, and **reaches no worker**.
Put it where the workers are.

Found by running the standard's own instruction — *"Assume every document is carrying restatements that leading
words retire. Go find them."* Reported first by [Re-review the shipped files against
`/writing-for-agents`](54-review-against-writing-for-agents.md), then scoped and conditioned by [What the token
findings change in the workflow and its skills](53-what-token-findings-change.md)'s worker.

**Admissible only because of node 53's second ruling.** Wholesale compression of these contracts is out — the
compression penalty concentrates on format-bearing instruction text, and one measured study found compression
past 30% failed every task in an agent scenario. **A leading word replaces adjectives and sentences and never a
shape**, which is the boundary that lets this through: *compress the prose that explains why, never the shapes.*

**Blockers: none.** Contends with nodes 32, 48, 49, 50, 58 and 60 for the code slot on the same five files.
**Scoped to `scribe` deliberately**, flagged as `53.5`: the six-site self-contained-condition test partly overlaps
the byte-identical blocks [Whether the five contracts' shared blocks stay
duplicated](50-shared-blocks-stay-duplicated.md) is deciding, and the four `unwrap` sites were reported on that
worker's `INVALIDATIONS` instead, because whether the human's *"discards stay discarded"* reaches a discard that
was itself about a contract is theirs to read.

## Acceptance condition

The work is these six files: `/home/mathieu/projects/graph-agent/.claude/skills/expedition-research/SKILL.md`,
`.../expedition-grilling/SKILL.md`, `.../expedition-prototype/SKILL.md`, `.../expedition-precondition/SKILL.md`,
`.../expedition-implementation/SKILL.md`, and `/home/mathieu/projects/graph-agent/CONTEXT.md`.

Measured before this change, so none of it need be taken on trust: `scribe` appears **exactly once** anywhere
under `/home/mathieu/projects/graph-agent/.claude/skills/`, at `expedition/graph-conventions.md` line 10 — a file
no worker contract points at — and appears **nowhere** in `CONTEXT.md`. The idea it names is that the manager
copies an agent's text onto the graph unaltered, authors nothing of its own onto it, and answers nothing itself.
That idea is spelled out as a sentence at **ten** places across the five worker contracts: the opening paragraph
of each, and the paragraph about the handover in each.

Done means every one of the following is true of the finished tree.

1. `CONTEXT.md` holds an entry for `scribe`, in the same form as the entries around it, defining it as: the
   manager copies an agent's text onto the graph unaltered, authors nothing of its own onto it, and answers
   nothing itself.
2. Each of the five worker contracts lists `scribe` among the words it says it uses exactly, under the heading
   `## Words used exactly` that each already has, with that same definition.
3. Each of the five worker contracts then **uses the word** where it previously spelled the idea out — at least
   in its opening paragraph and in its paragraph about the handover.
4. In each of those five files, the idea is written out as a sentence **at most once**: the definition under
   `## Words used exactly`. Every other site uses the word.
5. No hard rule in any of the five files is reworded.
6. Nothing else in the six files changes, and no file outside them changes.

### What the manager owes whoever claims this

*Not a change to the condition above.* **Clause 1 edits `CONTEXT.md`, which two other nodes also edit** — [Ship
the glossary inside the skill directory and make it state its own
completeness](56-ship-the-glossary-into-the-skill-set.md) moves it and rewrites its head, and [Give a research
node the cannot-proceed raise](57-research-can-raise.md) changes its `research` entry. None of the three blocks
another; **none of the three is concurrently claimable with another**, and whichever lands last inherits the file
the others left. Node 56 is the one that moves it, so landing that first costs the other two nothing.
