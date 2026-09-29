# Collapse the manager's discipline onto the leading word `scribe`

Type: implementation
Status: superseded
Superseded by: 76

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

The work is these six files: `.claude/skills/expedition-research/SKILL.md`,
`.../expedition-grilling/SKILL.md`, `.../expedition-prototype/SKILL.md`, `.../expedition-precondition/SKILL.md`,
`.../expedition-implementation/SKILL.md`, and `CONTEXT.md`.

Measured before this change, so none of it need be taken on trust: `scribe` appears **exactly once** anywhere
under `.claude/skills/`, at `expedition/graph-conventions.md` line 10 — a file
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

## The manager's note, 2026-09-24

*The manager's own note.* [Node 290](290-rewrite-the-research-contract-as-the-pilot.md)'s worker reported in its retrospective: "Node 61's premise is false for this file: the research contract's opening never spelled out the scribe idea."

## Amendment, 2026-09-24

*Written by [node 299](299-rewrite-graph-conventions-part-1.md)'s worker and filed by the manager, after that node's work landed as commit `0d406b7`. Every word of the replacement is fixed by that commit: it quotes `graph-conventions.md`'s after-text. The minting author's condition above is left as it was. The replacement takes the place of the clause it names. Node 299's worker searched every open node's `## Acceptance condition` for quoted spans of its before-range, matched literally and normalised with each condition joined into one string, and for each phrase its rewrite removed or replaced. The full list of handles is on node 299 under `### Re-pointing duty` and correction rounds 1 to 3.*

- **Preamble.** It cites "`expedition/graph-conventions.md` line 10". Proposed wording: "in `expedition/graph-conventions.md`'s sentence *"It writes as a scribe."*, under its opening". The same preamble's claims were already false before this work. `scribe` appears "exactly once", but `expedition/SKILL.md` uses it about ten times. It appears "nowhere in `CONTEXT.md`", but `CONTEXT.md` now has a `Scribe` entry. Whether node 61 still needs doing is for the manager.

## Flags

`61.1` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 299](299-rewrite-graph-conventions-part-1.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `0d406b7`.

## Amendment, 2026-09-25 (from node 312)

*Written by [node 312](312-cut-the-rules-both-the-manager-contract-and-graph-conventions-state.md)'s worker and filed by the manager, after that node's work landed as commit `e64b3de`. Every word of the replacement is fixed by that commit: it quotes the after-text of `expedition/SKILL.md` and `expedition/graph-conventions.md`. The minting author's condition and any earlier amendment above are left as they were. Node 312's worker's search is on node 312 under `RE-POINTING SEARCH:`.*

- **Preamble**, as amended by node 299. Replace the proposed wording with: "in `expedition/SKILL.md`, under `### You write as a scribe`; `expedition/graph-conventions.md` no longer uses the word, and its opening says "`## Writing the graph` in `SKILL.md`, the file beside this one, says who writes the graph's record and how the manager pastes what a worker hands it."" The manager's existing question, whether node 61 still needs doing, stands.

`61.2` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 312](312-cut-the-rules-both-the-manager-contract-and-graph-conventions-state.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `e64b3de`.

## Superseded, 2026-09-26

*The manager's note.* Made unnecessary by [node 76](76-write-the-manager-skill.md), whose landing (`4f9781b`) gave the glossary its **Scribe** entry and the manager contract its scribe wording. [Node 328](328-group-the-open-nodes-against-the-glossary.md)'s worker (its conflict C7) and node 329's worker (its conflict 8) both found this node's premise false and its definition in conflict with the existing entry; the human took the manager's pick to supersede it with their "ok".

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
