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
