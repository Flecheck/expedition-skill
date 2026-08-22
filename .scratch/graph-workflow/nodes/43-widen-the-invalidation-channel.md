# Widen the invalidation channel from contradiction to change

Type: implementation
Status: open

## Question

Every worker contract asks for *which resolved node your work contradicts*, and the traffic that part has to
carry is mostly renames, extensions and narrowings — measured at fifteen of eighteen propagations onto
resolved nodes arriving through the manager's reading instead. Reword the part, in the six shipped files that
carry the wording, so its scope is any resolved node whose answer the work changes what it says.

Reported by [Cascade pass mechanics](15-cascade-pass-mechanics.md)'s worker, which wrote the acceptance
condition below. It is part 1 of that node's answer, and the part the human endorsed first.

**Blockers: none. Sequencing only** — `graph-conventions.md` is live territory for [Record a checker's
not-covered part on `## Review`](38-recording-a-not-covered-part.md) and the five contracts for
[Checking a flag before the human sees it](30-checking-a-flag-before-the-human.md), [Narrow the flags.md
clause in the worker contracts](32-narrow-flags-file-clause.md) and [Nothing tells a worker to hold its work
against the record](37-invalidations-is-not-a-check.md), and the code slot is exclusive, so this runs alone
rather than beside any of them.

## Acceptance condition

Six files change, and no other file in the repository changes:

- `.claude/skills/expedition-grilling/SKILL.md`
- `.claude/skills/expedition-research/SKILL.md`
- `.claude/skills/expedition-prototype/SKILL.md`
- `.claude/skills/expedition-precondition/SKILL.md`
- `.claude/skills/expedition-implementation/SKILL.md`
- `.claude/skills/expedition/graph-conventions.md`

1. Each of the five `SKILL.md` files carries one line inside its handover block of the form
   `INVALIDATIONS: <which resolved node your ... contradicts, and how>`. The noun differs per file and
   the current text is: `your answer contradicts` in the grilling and prototype files, `your facts
   contradict` in the research file, and `your work contradicts` in the precondition and implementation
   files. After the change, each of those five lines asks for any resolved node whose answer this work
   **changes what it says** — not only one it contradicts — and names four kinds inline so that a worker
   reading only that line knows the scope: a **rename**, an **extension**, a **narrowing**, and a
   **contradiction**. Each file keeps its own noun (`answer`, `facts`, `work`) rather than the five being
   unified onto one.
2. Each of the five files states, in prose near that line, that an outright contradiction is the minority
   case and a renamed term or a narrowed rule is the ordinary one, so its reader does not treat the part
   as reserved for conflict.
3. `.claude/skills/expedition/graph-conventions.md` carries one sentence describing the same part, whose
   current text is: `` `INVALIDATIONS` — which resolved node its work contradicts, and how — answered by
   the party that built the work and may read the record to see what it touches. `` That sentence is
   reworded to the same widened scope and names the same four kinds.
4. Nothing else in any of the six files changes meaning. Specifically, all five `SKILL.md` files still
   carry the sentence ``Report `NEW NODES` and `INVALIDATIONS` yourself. Nothing else reports them.``
   unchanged, and all six files still carry, unchanged, the rule that a demand quantifying over the whole
   record — that the work contradicts no decision, that everything in it traces back to one — belongs on
   the handover's invalidation part and in no acceptance condition.
5. `.claude/skills/expedition-checker/SKILL.md` does not change. The checker returns no invalidation part
   and must not gain one.
6. No file under `.scratch/` changes.
7. The tree meets the bar.
