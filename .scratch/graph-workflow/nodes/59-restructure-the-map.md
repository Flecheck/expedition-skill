# Restructure `map.md` to what every worker needs

Type: implementation
Status: claimed

## Question

Carry out parts 1 and 2 of [What the token findings change in the workflow and its
skills](53-what-token-findings-change.md)'s answer: `map.md` keeps only what is strictly necessary for all
agents, and everything else moves **verbatim** to a sibling file it points at.

**Why, measured on the file:** it is 89,214 characters, ~22,300 tokens, and every worker reads all of it **cold
and uncached, once per node**, a subagent never reading its parent's prompt cache. About **74%** of it is append
history a worker cannot act on. At the dogfood target's 179 nodes that is ~4M tokens of re-reading one file, and
it grows monotonically. **The largest measured recurring token cost in the design.**

Reported by node 53's worker, which wrote the acceptance condition below. **Blockers: none** — it touches no
worker contract, so it does not contend for the code slot with nodes 32, 48, 49, 50 or 58.

### The licence this node runs under, in the human's own words

*Carried into the spawn as the human's words rather than the manager's, per [Whether a spawn may override a
shipped worker contract](28-spawn-overriding-a-contract.md)'s fourth spawn element.*

The implementation contract's hard rule 1 is *"You write product code. You write no graph file."* Read
literally, this node could not exist. The manager raised that; the human's ruling, `verbatim`:

> *"The graph file ban is because the manager should handle progress but here it is a work on the map itself,
> not just an update on the map. The rule is more about only doing it's work and not updating when finished as
> it's the manager job."*

So the ban stops a worker doing the manager's **progress bookkeeping**, and does not reach work whose
**subject** is a graph file. **This node's worker may edit `map.md`.** It may still not mark this node, resolve
it, or write a line in `decisions.md` or `flags.md` — that is the part of the rule that stands.

**This licence is for this node only.** The permanent fix is [Qualify the graph-file ban in the worker
contracts](58-qualify-the-graph-file-ban.md), and **this node must not touch any contract's hard rules.**

## Acceptance condition

The work is `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/`, and the file being changed is
`map.md` in that directory. Editing that file is what this node is for: its subject is the map itself rather
than a report of progress on other work.

Before this change `map.md` is 105 lines and 89,214 characters and holds exactly five `##` headings, in this
order: `## Destination`, `## Notes`, `## Decisions so far`, `## Not yet specified`, `## Out of scope`.
`## Not yet specified` is 51,866 characters across seven items, one of which is a single 20,589-character
paragraph; `## Notes` is 33,210 characters. The whole before-state is recoverable from `git diff`.

Done means every one of the following is true of the finished tree.

1. `map.md` holds those same five `##` headings, in that order, and no other heading at `##` level.
2. `map.md` is at most **32,000 characters** by `wc -c`. For scale, the material that must stay measures about
   29,000 characters, so this is a ceiling with headroom rather than a squeeze.
3. A new file sits beside `map.md` in the same directory holding the history moved out of it, and `map.md`
   contains a markdown link to that file. **Neither its filename nor the name it gives itself contains the word
   `provenance`**: this effort's glossary refuses that word by name.
4. **Nothing was deleted, summarised, paraphrased or shortened by the move.** For every line `map.md` loses,
   that line's text appears in the new file. Compare after unwrapping both sides — every file here wraps at
   about 100 columns, so a line-by-line comparison reports differences that are only rewrapping. A difference
   confined to a line's leading markdown (list marker, heading marks, opening emphasis) does not count.
5. Each item under `## Not yet specified` in `map.md` is at most **900 characters**, states what is not yet
   specified and what would settle it, and names by markdown link the nodes that shaped it. **None of them
   recounts what those nodes hold.**
6. The block in `## Notes` beginning with the line `**Ground rules for this effort.**`, and the five numbered
   rules under it, are **byte-identical** to their before-state, recoverable from `git diff`. This block is
   copied verbatim into other agents' instructions, so it may not be reworded, renumbered or reordered.
7. `## Destination` and `## Out of scope` are **byte-identical** to their before-state.
8. The bulleted list in `## Notes` introduced by `**Standing preferences for this effort:**` still holds a
   bullet for every preference it held before. Its bullet beginning `- **The node files are written for agents.`
   says three things, in whatever wording the implementer chooses: that it governs node files, where it stands
   as written; that it governs the shipped worker contracts on the ground that those are mostly format-bearing
   instruction text, which compresses badly, so what may be compressed there is the prose explaining why and
   never the named shapes; and that it does not reach `map.md`.
9. Neither `map.md` nor the new file cites a place inside any file by line number. Where either points inside a
   file it points by heading or by a quoted phrase.
10. `/home/mathieu/projects/graph-agent/.claude/skills/expedition/graph-conventions.md` currently says the graph
    is four files. In the one place it lists those files it names the correct number after this change and
    describes the new file's role in one sentence. It changes in no other respect.
11. No file under any of `/home/mathieu/projects/graph-agent/.claude/skills/expedition-checker/`,
    `.../expedition-grilling/`, `.../expedition-implementation/`, `.../expedition-precondition/`,
    `.../expedition-prototype/`, `.../expedition-research/` is modified.
12. Every markdown link in `map.md` and in the new file resolves to a path that exists.

### Audit at claim time, by the manager

*The manager's own note, not a change to the condition above.* Read against [An acceptance condition is
self-contained text](33-condition-is-self-contained.md) and [The clause that says no resolved node changes
cannot be self-contained](36-resolved-node-clause-cannot-be-self-contained.md).

**All twelve clauses pass, and this is the most carefully self-contained condition in the effort so far.** It
states the before-state numerically **in the condition** rather than pointing at the file for it, and names
`git diff` as the route for the byte-identical clauses — the same repair node 48's condition used. Clause 4
anticipates the false-result family the map has counted twelve of, by ruling out rewrap-only and
leading-markdown-only differences **before** the checker can trip on them.

**Two clauses quantify, and both are permitted.** Clause 11 quantifies over the **tree**, which node 36
permits. Clause 12 quantifies over links in two named files, not over the record.

**One thing verified rather than trusted.** `provenance` is refused by name in `CONTEXT.md`, so clause 3's
prohibition is real and not the worker's invention.

**One risk the condition carries and names.** Clause 2's ceiling and clause 5's per-item cap are the only
clauses that could force a *summary* where clause 4 forbids one. They are reconcilable — the live material
measures ~29,000 characters against a 32,000 ceiling — but if the worker finds them irreconcilable that is a
**raise**, not a choice, because resolving it either way would decide what is safe to lose.

### Correction to the condition's stated before-state, by the manager, at claim time

*Not a change to the condition — the manager may not rewrite one. A correction of fact the checker must hold, and
the manager's own doing.*

The condition states *"Before this change `map.md` is 105 lines and 89,214 characters"*. **It is 106 lines and
92,113 characters.** The difference is one standing preference the manager filed **after** node 53's worker took
its measurement and before this node was claimed — the human's retrospective instruction, ~2,900 characters. The
section figures move with it: `## Notes` is larger by that amount and the fog is unchanged.

**Every clause survives**, and the condition's own design is why. Clauses 4, 6 and 7 name `git diff` as the route
to the before-state rather than the numbers, so they read the true state. Clause 2's 32,000 is a **ceiling**, and
the live material's ~29,000 is unaffected by an addition that is itself live material — though the headroom is now
thinner by ~2,900 characters, which is worth the worker knowing. Clause 5's per-item cap is unaffected, the
addition being in `## Notes` and not in the fog. **What is stale is two numbers in the condition's own preamble,
and nothing that is demanded.**

**Recorded rather than repaired for two reasons.** A condition is not the manager's to rewrite, and a blind
checker handed this condition as text would compare its stated before-state against `git diff` and be **right**
to report the mismatch — so it is told, rather than left to discover a discrepancy the manager caused. This is the
widened ninth requirement from [Workflow self-improvement during
use](19-workflow-self-improvement.md) applied to the manager's own edit: the statement of what changed is owed on
files left in an older form, and here the file left in an older form is the one the condition describes.

**And a commitment the manager makes for the duration of this node.** `map.md` grew ~12,600 characters today,
almost all of it filed by the manager, and this node's worker is editing it. **The manager files nothing further
into `map.md` while this node is claimed.** Anything that would have gone there waits, and goes in afterwards
under whatever structure this node lands — which is also the honest test of whether the new structure holds.
