# Carry the recorded deltas into the shipped skill files

Type: implementation
Status: open

## Question

Three files have shipped and have since gone stale. Bring them up to date in one pass.

**[`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md)** owes the **nine
deltas** listed in [map.md](../map.md)'s `## Notes` — eight recorded there before this node existed, plus
[What is recorded when the human takes an option as offered](25-recording-an-option-taken.md)'s rule, which
is the ninth.

**[`expedition-grilling/SKILL.md`](../../../.claude/skills/expedition-grilling/SKILL.md)** and
**[`expedition-prototype/SKILL.md`](../../../.claude/skills/expedition-prototype/SKILL.md)** each carry one
sentence that is now wrong for a case the workflow has just made ordinary. Both say, of `HUMAN ANSWER`,
*"Reason from what they wrote rather than from the option you offered."* That was written against a
rendering. Against a **terse assent** — *"ok for recommended"* — the option **is** what the human endorsed,
and a worker obeying the sentence literally would discard the content of the answer. The two contracts need
a carve-out and have none. `expedition-precondition` and `expedition-implementation` carry the same
`HUMAN ANSWER` block without that sentence and need nothing; the sentence was verified on disk to live in
exactly those two files, both at line 98.

Reported by [What is recorded when the human takes an option as
offered](25-recording-an-option-taken.md)'s worker. Its own note on where this belongs: the map's delta
list covers only `graph-conventions.md`, so **the contract sentence has no home today** — which is what
makes this a node rather than another line on that list.

Why one node and not three: the landing policy allows exactly one commit per implementation node, so a file
touched here cannot be touched again without superseding this node. Everything owed to these three files at
the time this node is claimed goes in it.

## Acceptance condition

1. Every one of the nine deltas recorded in [map.md](../map.md)'s `## Notes` is present in
   `graph-conventions.md`, in that document's own voice rather than as a changelog. The map's delta
   paragraph is annotated as discharged **in place** — struck through, not deleted, per the standing rule.
2. `graph-conventions.md` states [What is recorded when the human takes an option as
   offered](25-recording-an-option-taken.md)'s rule for **both** `## Interview` and `## Review`: the
   manager pastes the human's reply as they wrote it, however terse, marked `verbatim`; the option or
   outcome it points at is quoted beside it and attributed to whoever wrote it; nothing is rendered, so
   nothing on either log is marked `paraphrase` unless the manager genuinely could not avoid rendering it.
   It also states the residual case — where a terse reply does not make clear which option it points at,
   the manager records the reply and asks which.
3. `expedition-grilling/SKILL.md` and `expedition-prototype/SKILL.md` carry the carve-out: where the
   human's words are an assent to a named option, that option is what they endorsed and the worker reads it
   as theirs. Placed with the sentence it qualifies. The other four contracts are unchanged.
4. No decision on any resolved node is changed. This node moves text; where the shipped files and a node
   disagree, the node wins and the file is what moves.
5. The bar as [map.md](../map.md) records it for this repo: no build, no tests, no formatter, so the
   project criteria, this map's standing preferences, [`CONTEXT.md`](../../../CONTEXT.md)'s `_Avoid_` lines,
   and these conditions are the whole of it.
