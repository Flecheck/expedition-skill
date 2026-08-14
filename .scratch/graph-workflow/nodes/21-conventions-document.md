# Write the graph conventions document

Type: implementation
Status: resolved
Blocked by: 11, 14

## Question

Write the shipped document an agent reads to operate the graph — the file format in its user-facing form.

[Graph file format](13-graph-file-format.md) fixed the shape; this node writes it down. **The two are not the same document, and this is not that answer transcribed.** That node's `## Answer` is a decision record: it exists so a human can tell whether a choice still holds, so it carries reasoning, rejected alternatives, and the evidence each call rested on. This document tells an agent what to write in which file, and carries none of that. A reader following it never needs to know why.

In scope: the four files, the node file's fields and sections and their order, the five statuses, the three edge kinds, the label rule, the flag markers, and the procedures for claim / resolve / supersede / rule-out-of-scope / park / raise a flag / settle a flag.

Out of scope, because they are separate implementation nodes that do not exist yet: the manager's own skill, the subagent prompt templates, and the adoption mode.

**This is the map's first implementation node**, which means it is also the first exercise of machinery the map has only reasoned about: the exclusive code slot, the independent reviewer, the standing bar, and an acceptance condition written by a spawner rather than by the worker. [Dogfood target](09-dogfood-target.md)'s coverage criterion wants each of those observed once.

Blocked by [Naming](14-naming.md), because every field name and section heading in this document is a naming decision and writing it first would settle them by accident — the exact mistake [Graph file format](13-graph-file-format.md) was itself blocked to avoid. ~~Blocked by [Git and code-landing policy](11-git-and-code-landing.md), because no implementation node can land before there is a policy for landing; that dependency is general to every implementation node, not special to this one.~~

**That blocker is satisfied** — [Git and code-landing policy](11-git-and-code-landing.md) resolved, so **[Naming](14-naming.md) is the only thing between this node and the frontier.** Two things it now knows about its own landing, both of which it is the first node to experience: its output is one path-limited commit made by the manager after the human approves the diff, and the human's approval is a gate the node cannot resolve without. The document itself does **not** describe that procedure — landing is the manager's skill, which this node's scope explicitly excludes — but this node is the first thing the procedure will be run on.

## Acceptance condition

Written by [Graph file format](13-graph-file-format.md) before any work starts, per [Node type taxonomy](07-node-type-taxonomy.md).

1. Every field, section and status that [Graph file format](13-graph-file-format.md) fixed appears in the document — and no field it did not fix.
2. For each of claim, resolve, supersede, rule-out-of-scope, park, raise a flag and settle a flag, the document states exactly **which files change and in what order**. The at-relay-time ordering from [Relay protocol](08-relay-protocol.md) is stated as an ordering requirement, not left to inference.
3. It contains no reasoning, no rejected alternatives and no justification.
4. Every procedure defined by `Lang/docs/agents/issue-tracker.md` still works as written against this document, and the **two known divergences** — frontier ordering, and resolve appending to `decisions.md` rather than the map body — are called out in a section a target repo can append verbatim.
5. It names no repository, machine, language or toolchain, per the map's portability note.
6. **The objective check:** an independent reviewer can reconstruct the node-file template from the document alone, and what they produce matches.

Per [Node type taxonomy](07-node-type-taxonomy.md) the implementer may not rewrite these conditions, but may flag one as wrong.

## Annotation: unblocked, and there is now a vocabulary to write it in

Added by [Naming](14-naming.md).

- **Both blockers are resolved, so this node is on the frontier** — the map's first takeable implementation node, and the first thing the gate will ever be run on.
- **It is written in the glossary's vocabulary**, and reading [`CONTEXT.md`](../../../CONTEXT.md) is a precondition rather than a courtesy: this document is the authoritative statement of the conventions, so a term that drifts here drifts everywhere downstream of it.
- **The node directory has already moved** from `issues/` to `nodes/`, and the illustrative paths inside [Graph file format](13-graph-file-format.md) were deliberately left as written. Making the layout unambiguous again is therefore something this document has to do, and a candidate line for its acceptance condition.
- **Its own landing is the first exercise of the policy**: a checker pass, the human's approval at the gate, then one path-limited commit carrying `Node: graph-workflow/21` as a trailer.

## Answer

**Two files under `.claude/skills/expedition/`, landed as commit `92407d4`.**
[`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md) is the shipped
statement of the format and the procedures.
[`wayfinder-divergences.md`](../../../.claude/skills/expedition/wayfinder-divergences.md) holds
everything a repo with an existing wayfinder tracker doc needs, and nothing a repo without one does.

It states: the four files and the map's four sections; the node file template with its seven fields, its
mandatory subset and its six sections in order; five statuses with which of them satisfy an edge; five
types; three edge kinds; the label rule; the three flag markers; the frontier; the two scanning rules;
seven procedures, each a numbered file-by-file list carrying an explicit ordering sentence wherever
order is load-bearing; and the eight mechanical checks.

It states no reasoning at all, which was condition 3 and which cost four edits to enforce — a purpose
clause, the rationale for the section order, and the reasons behind both scanning rules all came out.
The design record is where every *why* lives, and this document never points at it.

**The split was the human's, at the gate**, and it is the same objection that killed `issue` one node
earlier: a reader in a repo that has never run `/wayfinder` should not learn a foreign tool's vocabulary
from the authoritative conventions file. `graph-conventions.md` now contains the string `wayfind`
exactly once, as the sibling filename.

### What running the first implementation node taught the map, beyond the document

- **The landing policy's ordering is load-bearing, not conventional.** [Git and code-landing
  policy](11-git-and-code-landing.md) fixes one path-limited commit per implementation node and forbids
  rewriting history; committing on the human's approval before the checker runs risks needing a second
  commit or an amend for the same node. Checker → gate → commit → resolve is therefore forced by the
  two rules it already stated, and this node found that out by being the first thing run through it.
- **An implementation node cannot resolve inside the session that does the work.** Two of the four steps
  belong to someone else. That is the design, and it means the one-node-per-session rhythm the map
  inherited does not describe implementation nodes.
- **Check 6 caught a real violation on the graph that defined it.** [Naming](14-naming.md) had a line in
  [flags.md](../flags.md) with no `## Flags` section behind it — a flag raised before the section that
  holds one existed by procedure. Fixed additively.
- **Three scanning false positives, two of them the exact classes [Graph file
  format](13-graph-file-format.md) predicted** — a `## Flags` heading matched inside a fenced template,
  and fields read outside the header block. The third was new: a flag line whose one-line text contains
  its own link mis-attributes the flag, so the document now fixes the node as the **first** link on the
  line. That is the only format detail this node added rather than encoded.
- **The bar's first discovery ran, and found nothing to run.** No build, no tests, no formatter, no CI,
  so the bar here is entirely its non-command half. Recorded in the map's `## Notes` per [Done-ness and
  termination](10-done-ness.md), which is the manager-maintained region that node created.
- **The checker's payload had to be improvised**, since [Subagent context
  contract](12-subagent-context-contract.md) is open. The four-phase protocol that made condition 6 a
  real test — reconstruct from the shipped files alone, and only then open the node that fixed the
  format — is evidence for that node rather than borrowed from it.

## Flags

`CONDITION-WRONG` — **acceptance condition 4's first clause is false, and [Naming](14-naming.md) is what made it false after the condition was written.** The clause requires that *"every procedure defined by `Lang/docs/agents/issue-tracker.md` still works as written against this document"*. Three of that doc's lines no longer do: its `Child ticket:` and `Frontier:` lines both give the path as `issues/`, which is now `nodes/`; its `Type:` vocabulary offers `task`, which is now `precondition`; and its conversation heading is `## Comments`, which is `## Interview`. Per [Node type taxonomy](07-node-type-taxonomy.md) the condition was **not rewritten**. All three are named in the appendable section instead — which is the clause's own remedy, written for exactly two divergences where there turn out to be five. **The breakage is doc-only and costs the migration nothing:** Lang's `.scratch/` contains no `Type:` line, no `issues/` directory and no `## Comments` heading anywhere, so zero live tickets depend on any of the three. Its spec-completion effort is prose documents, and it has already split `decisions.md` out by hand — which is the second of the two divergences the condition did know about.

`ASSUMPTION` — **the document's path pins where the skill installs.** It is written to `.claude/skills/expedition/graph-conventions.md`, and the map's fog item *How the workflow reaches a repository that is not this one* owns that question and is not sharp enough to be a node yet. Decided on three grounds: it is the harness's own location for a project-scoped skill, it needs no install step to be usable here, and it moves for the cost of a path if [Runtime host](02-runtime-host.md) is replaced. Checked rather than assumed: the repo has no ignore file of any kind, so `.claude/` is committable and the landing policy works there. This is still a judgement made inside live fog rather than one a resolved node fixed.

`ASSUMPTION` — **the document fixes no ordering within the frontier, and states that absence in as many words.** [Human-initiated steering](16-human-steering.md) is open and owns the replacement for *first by number wins*; shipping any order here would settle that node by accident, which is the mistake this node was blocked to avoid once already. The cost is real and is the reader's: someone following the document to pick work finds a stated hole, and the appendable section tells a target repo that its own ordering rule does not apply without saying what does.

`ASSUMPTION` — **resolved on a truncated checker run.** The checker completed Phase 1 and died on a session limit; it never issued an overall verdict. Phase 1 is condition 6 — the objective check, and the only one the implementer cannot perform — and it passed, which is also independent evidence for conditions 1 and 2. Reading that as a pass for the node is an inference, not the checker's word. Re-running phases 2–4 would cost one agent and is the cheapest way to settle this flag.

## Review

**The checker did not run, and its absence is not a pass.** Agent spawning is off in this session, so the second independent agent [Node type taxonomy](07-node-type-taxonomy.md) requires before an implementation node may resolve has not seen this document. Recording that rather than performing a self-check dressed as one: a self-review is the thing that answer explicitly rejected, and acceptance condition 6 names the checker as the whole mechanism. **This node therefore stays `claimed`**, holding the code slot, with the work standing at the gate.

What was self-checked mechanically, and what only the checker can do:

| Condition | State |
| --- | --- |
| 1 — every field, section and status fixed by [Graph file format](13-graph-file-format.md), and no field it did not | **Checked.** Seven fields, six node sections, four map sections, five statuses, five types, three flag markers. Nothing added. One addition sourced from [`CONTEXT.md`](../../../CONTEXT.md) rather than from that node: `DIVERGENCE` as a marker on a recorded answer, which is a marker and not a field. |
| 2 — which files change and in what order, for all seven procedures, with the at-relay-time ordering stated | **Checked.** Seven procedures, each a numbered file-by-file list. Four carry an explicit ordering sentence; the at-relay-time rule is stated as an ordering requirement under `## Interview` rather than left to the park procedure. |
| 3 — no reasoning, no rejected alternatives, no justification | **Checked, and it cost four edits.** A purpose clause on the foreign-label example, the rationale for the section order, and the reasons behind both scanning rules were all removed; the scanning rules now state what the files contain and then bind. Greps for `because`, `the reason`, `rejected`, `in order to` and `trade-off` return nothing. |
| 4 — the target's procedures still work, and the known divergences are appendable | **First clause fails — see the `CONDITION-WRONG` flag.** Second clause met: a fenced block a target repo copies verbatim, naming five differences including both the condition knew about. |
| 5 — names no repository, machine, language or toolchain | **Checked.** Greps for every candidate name return nothing; the foreign-label example was made generic to keep it clear of this line. |
| 6 — an independent checker reconstructs the node-file template from the document alone, and it matches | **Not run.** The one condition that cannot be self-checked by construction. |

Also discharged here, because this is the first implementation node and nothing had done it yet: **the bar's commands were discovered for this repo and written into the map's `## Notes`**, per [Done-ness and termination](10-done-ness.md). The repo has no build, no tests, no formatter and no CI — which under the *"if relevant"* clause is a complete bar, not a deficient one, exactly as it is on the dogfood target.

### Correction round 1 — the human, at the gate

*"I am not too sure about talking about wayfinder in the general doc, maybe add a specific wayfinder
related doc for migration."*

The same objection as the one that killed `issue` in [Naming](14-naming.md), one level up: a reader in
a repo that has never run `/wayfinder` was getting a foreign tool's vocabulary out of the authoritative
conventions file. The final section moved to a sibling,
[`wayfinder-divergences.md`](../../../.claude/skills/expedition/wayfinder-divergences.md), which now
also carries the same/added/different breakdown. `graph-conventions.md` mentions `wayfind` exactly
once, as that filename, in a one-line pointer at the top.

- **Acceptance condition 4's second clause is now satisfied by a sibling file rather than by this
  document.** The clause asks for "a section a target repo can append verbatim"; the appendable fenced
  block is unchanged and ships with the skill, one file over. A checker should not read its absence
  from `graph-conventions.md` as a miss.
- **Named `wayfinder-divergences.md`, not `wayfinder-migration.md`.** *Migration* would promise the
  thing [Adopting an in-flight effort](18-adopting-in-flight-effort.md) owns — importing an effort's
  existing questions, decisions and prose edges into node files — which this node's scope excludes.
  The file says so under *Not covered here*. One word to overturn if the human wants the broader name.
- **No flag for this round.** A correction at the gate keeps the node `claimed` and costs no chain,
  per [Node type taxonomy](07-node-type-taxonomy.md); flags record the worker's judgement calls, not
  the human's instructions.
- Deleting a section from product code does not touch the never-delete rule, which binds the **graph's**
  files. `graph-conventions.md` states that scope in its own words: *"When any graph file changes."*

### The gate: approved

The human's words, verbatim: *"seems good"* — given after correction round 1, on both files. Rounds are
uncapped and closed at one.

**The commit is still withheld, and the reason is the landing policy's own ordering rather than
caution.** [Git and code-landing policy](11-git-and-code-landing.md) fixes *one* path-limited commit
per implementation node and forbids rewriting history. Committing on the approval alone, before the
checker has run, risks exactly the two things that policy refuses: if the check then fails, this node
either takes a second commit or an amend. So the order the policy states — checker, then gate, then one
commit, then resolve — is load-bearing and not merely conventional, which is a property of it this node
discovered by being the first thing run through it.

**Outstanding: acceptance condition 6, and nothing else.** Five conditions self-check clean, condition
4's first clause carries a `CONDITION-WRONG` flag, and condition 6 is the one that cannot be
self-checked by construction. The node stays `claimed` and keeps the code slot until it runs.

### The checker ran, and was cut off after the one phase that mattered

Run read-only on the human's instruction, under a four-phase protocol built so that condition 6 would
be a real test: **reconstruct the node file template from the two shipped files alone, and only then
open the node that fixed it.** A checker that reads the design record first cannot check whether the
document is sufficient, and there was no existing contract to borrow — [Subagent context
contract](12-subagent-context-contract.md) is open, so this payload was improvised and is evidence for
it rather than the other way round.

It completed Phase 1 and died on a session limit before Phase 2. Phases 2–4 never ran.

**Condition 6: PASS, and not narrowly.** From the document alone it reproduced every field, the
mandatory subset, all five statuses, all five types, all six sections in order, the three flag markers,
the four files with their purposes, and all seven procedures with their ordering sentences. It also
recovered rules it was not asked for: `parked` is `open` with a non-empty `## Interview`, under-check is
`claimed`, `NN` is never reused, a foreign label resolves by glob, and the at-relay-time ordering.
Because it did that while blind to [Graph file format](13-graph-file-format.md), the same output is
independent evidence for conditions **1 and 2** as well as 6 — which is the only reason those two are
not left resting on the implementer's own word.

**Two ambiguities found, both real, both fixed.** The protocol told it that an ambiguity forcing a guess
is a condition 6 failure even when the guess is right, and it took that seriously:

1. **Field order in the header was never stated.** The document fixed section order explicitly and said
   nothing about fields, so the reconstruction reproduced the template's order *"without warrant"*.
   Fixed: *"Write the fields in the order shown below."*
2. **`Supersedes:` was silently single-valued.** The edge list writes `Supersedes: NN` against
   `Superseded by: NN, NN`, which reads as single but was never said. Fixed by stating it, in the shape
   [Revision semantics](06-revision-semantics.md) actually describes: one number, and where a node is
   superseded by several, each replacement carries the same one. This keeps mechanical check 2 true in
   both directions.

Neither fix can invalidate a reconstruction that already matched; both remove a guess from the next
reader.

**What is still unchecked.** Conditions 3, 4 and 5 rest on the implementer's greps, which are mechanical
rather than judgement, and on the `CONDITION-WRONG` flag above. No independent agent formed an overall
verdict — Phase 1's pass is being read as a pass, which is an inference and is flagged.
