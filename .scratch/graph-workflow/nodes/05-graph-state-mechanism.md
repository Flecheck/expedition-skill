# How the graph's bookkeeping is kept straight

Type: grilling
Status: resolved

## Question

Does the manager maintain the graph by judgment over markdown files, or mechanically via a bundled tool?

## Answer

**Markdown files and prose rules, wayfinder-style — with a named trigger for extracting a tool later.**

Fact established while deciding this: skills *can* ship executables. The official skill-creator documents `scripts/` as a bundled-resource directory, and two of Matt's own skills use it (`diagnosing-bugs/scripts/hitl-loop.template.sh`, `git-guardrails-claude-code/scripts/block-dangerous-git.sh`). Bundled scripts also "execute without loading", so they cost no context until run. So a CLI was genuinely available; it was not chosen.

Why markdown-first anyway:

1. **A CLI's command surface *is* the graph semantics, and those are still open.** A command like `graph revise 4 --because 7` presumes revision works by supersede-edge — exactly the undecided question in [Revision semantics](06-revision-semantics.md). Formalising before deciding what is formalised means building it twice.
2. **skill-creator's own heuristic is extract-after-observation** — bundle a script once you notice agents repeatedly hand-rolling the same helper. The workflow has not been run yet, so any command set is a guess about which bookkeeping actually gets fumbled.
3. **The graph files are a shared artifact with the human**, not just machine state. Markdown readable in a diff and fixable by hand beats a state file plus a tool to interpret it.

Acknowledged counter-argument, to revisit: prose invariants cost manager context every session and rely on the manager's memory, and an LLM drifts on multi-file bookkeeping over a long session. **Revisit trigger:** if a dogfood run shows the manager losing track of statuses, edges or the write lock, extract a *read-only* `check` / `frontier` command first — it needs only edges and statuses (settled) and bakes in no revision policy (unsettled). Mutation stays in prose until its semantics stop moving.

**The `check` command is now specified in everything but the trigger**, by [Graph file format](13-graph-file-format.md), which enumerates **eight invariants that are decidable with no judgement at all** — dangling and superseded and out-of-scope edge targets, missing `Supersedes:`/`Superseded by:` back-edges, reused numbers, undeclared labels, index and flag consistency, missing acceptance conditions, and the attempt-block cap. The reasoning above is unchanged and the trigger still has not fired: this is an additive note recording that the extraction, when it happens, no longer needs designing. It also confirms the prediction in point 1 — the command surface stayed unbuildable exactly until the semantics stopped moving, and the mechanical half turned out to bake in no revision policy whatever.

**A ninth check exists, and it is a different kind**, added by [Git and code-landing policy](11-git-and-code-landing.md): *no uncommitted changes outside the effort's own directory*, which is the precondition for starting an implementation node and the read that tells whether the exclusive code slot is free. Unlike the eight, it reads **git rather than markdown** — so if a `check` command is ever extracted, the write lock stops being a thing the manager remembers and becomes a thing the repository already knows. It also makes one failure legible for free: a dirty product tree with no `claimed` implementation node means an agent died holding the slot, and the diff is the replay input.

## Annotation: the ninth check's premise is replaced by counting worktrees

*Filed by the manager at [Gather the manager's accumulated duties into one enumerated
list](75-gather-the-managers-duties.md)'s resolution, in that worker's own words. **Not reported by node 68's
worker**, this node mentioning the mechanism in passing rather than owning it.*

> Its answer records a ninth check of a different kind from the eight — *"no uncommitted changes outside the
> effort's own directory"* — as *"the precondition for starting an implementation node and the read that tells
> whether the exclusive code slot is free"*, and adds that it makes one failure legible for free: *"a dirty product
> tree with no `claimed` implementation node means an agent died holding the slot, and the diff is the replay
> input."* [Run an implementation node's work in a worktree](68-implementation-in-a-worktree.md) replaces both
> readings by counting live worktrees, and names the old heuristic as one that *"reads the human's own hand-edits as
> a dead worker"*. [Git and code-landing policy](11-git-and-code-landing.md) carries the annotation for its half of
> this; **node 05 does not, and its statement about a future `check` command reading git rather than markdown rests
> on the replaced heuristic.**

**Everything else this node fixed stands**: markdown files and prose rules rather than a CLI, and the extraction
trigger, which has still not fired.
