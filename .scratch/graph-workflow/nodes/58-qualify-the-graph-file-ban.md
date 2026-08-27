# Qualify the graph-file ban in the worker contracts

Type: implementation
Status: open

## Question

Five worker contracts forbid a worker to write a graph file, unqualified — the implementation contract's hard
rule 1 is *"You write product code. You write no graph file."* and the other four say *"You write no file — no
graph file, and no other file."* **That wording blocks a node whose work *is* a graph file**, and one such node
now exists.

**The human's reading, `verbatim`, given when the manager raised the block:** *"The graph file ban is because the
manager should handle progress but here it is a work on the map itself, not just an update on the map. The rule
is more about only doing it's work and not updating when finished as it's the manager job."*

**This node is the second of the two outputs a raise owes.** [Whether a spawn may override a shipped worker
contract](28-spawn-overriding-a-contract.md) fixed that the human's answer to a blocking raise yields **a
licence for that one attempt, flagged on the node, and a node for the permanent fix — always both**. The licence
travels into the map-restructuring node's spawn as the human's own words. This is the permanent fix, and it
exists because **the reading reaches nobody otherwise**: the rule stands unqualified in five files, so every
future worker reads it broadly and the next node whose subject is a graph file is blocked again.

The evidence for *both* rather than one is on the record: node 28 measured that [Whether flags.md survives the
settle-at-close practice](27-does-flags-file-survive.md) took a departure and minted no node, and a session later
the clause stood unchanged in five contracts while the narrowing was still an open question — *"the repair was
lost along with the record"*.

## Acceptance condition

*Written by the manager, for a node the manager minted itself as a raise's second output.* Marked as the
manager's own under [Who writes the acceptance condition for an implementation node the manager mints
itself](39-condition-for-a-manager-minted-node.md), whose constraint 1 confines it to what is already fixed. **The
human's reading is fixed; its wording is not, so this condition states the property and leaves the form.**

1. In each of the five worker contracts —
   `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`,
   `.claude/skills/expedition-precondition/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`,
   `.claude/skills/expedition-research/SKILL.md` — the rule that forbids writing a graph file distinguishes two
   things that its current wording does not: **a worker doing the manager's bookkeeping on the graph**, which
   stays forbidden, from **a worker whose own node's work is a change to a graph file**, which is not what the
   rule is about.
2. The distinguishing property each contract states is the one the human named: the rule is about a worker
   doing only its own work and not recording progress when finished, that being the manager's job. **It is not
   stated as a list of permitted files or permitted nodes**, which would need a judgement this condition does
   not make and nobody has made.
3. Every contract still forbids the thing the rule was written for. After this work, none of the five permits a
   worker to mark its own node, resolve it, write a line in `decisions.md` or `flags.md`, or record its own
   progress anywhere — and where a contract states that separately today, that statement is unchanged.
4. `.claude/skills/expedition-checker/SKILL.md` is not changed: a checker is read-only and writes nothing at
   all, so the distinction does not arise for it.
5. Where `.claude/skills/expedition/graph-conventions.md` states that the manager is the graph's only writer, it
   is left consistent with clause 1 — either because it already is, or by being made so in the same change. It
   is **not** rewritten beyond what that requires.
6. No hard rule is removed or renumbered, and no rule other than the one clause 1 names changes its meaning.
7. The working tree meets the bar.

### What the manager owes whoever claims this

*Not a change to the condition above.*

**Clause 5 is the clause to be careful with, and it is the reason this is not purely a five-file wording job.**
`graph-conventions.md` line 10 reads *"The manager is the graph's only writer, and it writes as a scribe."* Under
the human's reading that sentence is **either still true** — because a worker whose work is a graph file returns
text and the manager still writes it — **or it is not**, because the human asked for an implementation node to
modify the files directly. **Which of those it is has not been decided**, and clause 5 deliberately does not
decide it: it requires consistency, not a particular resolution. If the worker judges that consistency cannot be
reached without deciding it, that is a **raise**, not a choice.

**This node is not token-use work** and is deliberately not started under the human's standing instruction. The
licence carries the one node that needs it in the meantime.

## Annotation: a live instance of clause 5's open question, and it resolves the other way

*Filed by the manager while [What a finding must carry so it can be swept](71-what-a-finding-must-carry.md) was
under check. Not a change to the condition above.*

Clause 5's note says `graph-conventions.md`'s *"The manager is the graph's only writer, and it writes as a scribe"*
is **either still true** — a worker whose work is a graph file returns text and the manager writes it — **or it is
not**, and that which of those it is has not been decided. Node 71 supplies the first instance of the first reading
actually running, so the note now has evidence where it had none.

**What happened.** The manager's spawn told the worker to *"file a `## Retrospective` annotation on the node
file"*. The implementation contract's hard rule 1 — *"You write product code. You write no graph file"* — forbids
that. The worker **reported the contradiction and handed the retrospective back as text**, which the manager then
wrote onto the node. That is the scribe sentence holding, unaltered, in the one case that was supposed to test it.

**Two things this does and does not settle.**

- It **does** show that the return-text-and-let-the-manager-write route works, is cheap, and needed no licence.
  A worker on the case clause 5 worries about — a node whose *subject* is a graph file — would return a whole file
  rather than a section, and nothing in what happened here says whether that scales.
- It **does not** touch the human's reading that this node was minted from, which is about a node whose *work is a
  graph file* rather than a worker recording its own progress. The retrospective is the second kind: it is the
  worker recording something about its own run, which is exactly what the rule was written for.

**And the defect it exposed is the manager's, not a contract's.** `map.md`'s sentence left its subject open —
*"It files as a `## Retrospective` annotation on the node"* — and every retrospective spawn this effort has sent
carried the wrong reading. The map now names the subject. **No worker before this one reported it**, which is
worth more than the fix: the instruction to break a hard rule travelled in every such spawn and was obeyed or
worked around silently.
