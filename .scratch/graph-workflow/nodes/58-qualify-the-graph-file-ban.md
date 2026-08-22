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
