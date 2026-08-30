# The manager starts the next node rather than proposing it and waiting

Type: implementation
Status: claimed

## Question

**The human reported this as a defect in the shipped skill.** Their words, `verbatim`: *"Also the manager should
proactively start new nodes when one has finished."*

### What the files say now, and why it is not enough

[map.md](../map.md) carries their earlier standing instruction, `verbatim`: *"You can start new tasks. You should
automatically propose to start a new task when a task finish"*, and the map renders it as *"The manager never idles,
and proposes the next work itself as each node finishes."*

`.claude/skills/expedition/SKILL.md`'s `### Picking the next node` says: *"Pick it yourself and report the pick.
Never ask which node to work."*

**Both say pick, and neither says start.** Nothing in either file says the manager spawns the worker rather than
waiting for the human to react to the pick, and nothing names the moment at which it does so. **The instance that
produced this node is a manager doing exactly the permitted thing and still stalling**: at [Adopting an in-flight
effort](18-adopting-in-flight-effort.md)'s close it reported the node finished, named [Write the adoption
procedure](97-write-the-adoption-procedure.md) as the strongest next pick, wrote *"Nothing is expected of you"*, and
started nothing. The code slot sat empty and both grilling channels sat empty.

**Reporting a pick and then stopping is indistinguishable, from the human's side, from asking which node to work** —
which the contract already forbids. The prohibition has no effect because the report that replaces the question is
still a report the manager waits on.

## Acceptance condition

***Written by the manager, for a node the manager minted itself*** at the human's instruction. Marked as the
manager's own under [Who writes the acceptance condition for an implementation node the manager mints
itself](39-condition-for-a-manager-minted-node.md), whose constraint 1 confines it to what is already fixed. **The
human's instruction is fixed; its wording and its placement in the file are not, so this condition states the
properties and leaves the form.**

1. `.claude/skills/expedition/SKILL.md` states that when a node finishes, the manager **starts** the next work rather
   than proposing it and waiting: it picks, spawns, and reports the pick as something already under way.
2. It states that the report of a pick awaits no answer, and that the human's redirection of a pick is a correction
   after the fact rather than a permission the manager waits for.
3. It states what bounds how much the manager starts, in terms the file already carries: the effort's code-slot count
   for implementation nodes, and the rule that exactly one question is in front of the human at a time for nodes that
   need one. A pick that would exceed either is not started.
4. It states that the manager reports what it started, so that a pick the human would have made differently is
   visible to them at the moment it is made and not only at that node's close.
5. Where `### Picking the next node` today says *"Pick it yourself and report the pick. Never ask which node to work"*,
   that prohibition still stands after the work and is not weakened.
6. No other file under `.claude/skills/` changes, and no file under `.scratch/` changes.
7. No section of `.claude/skills/expedition/SKILL.md` is removed, and no rule in it other than what clauses 1–4 add
   changes its meaning. In particular the nine duties it lists as unsettled are not reduced, and `## What is in front
   of the human, and when`'s one-question-at-a-time rule and its two tiers are unchanged.
8. The working tree meets the bar.

### The manager's read-back, recorded before the claim

*[Node 39](39-condition-for-a-manager-minted-node.md)'s constraint 2 requires the condition to be read back against
the two rules that bind every condition, and that reading recorded on the node.*

- **Self-contained text.** It passes. Each demanded property is written out here rather than pointed at; the one
  existing sentence it protects is quoted in clause 5; the file it changes is named by path and the checker has the
  repo. Clause 3 names two bounds by their function and the file states both, so a checker reads them there.
- **It does not quantify over the record.** It passes. Every clause is a demand about the state of one file or about
  what changed in the tree, which `graph-conventions.md` permits by name. No clause holds the work against the
  effort's resolved nodes.

### What this node does not settle, stated so no one reads it into the condition

**Whether the manager may start a node that needs the human before the human's channel is free.** Clause 3 forbids it
by pointing at the existing one-at-a-time rule, which is the conservative reading of what is already fixed. Whether a
worker may be spawned to do its reading while its question queues is a change to that rule and belongs to the human,
not to this condition.

## Where it came from

The human, unprompted, immediately after a manager reported a node finished and started nothing. Minted by the
manager at their instruction; the question above and the acceptance condition are the manager's, and the instruction
itself is quoted verbatim at the top.

## Flags

*Each entry is the worker's own prose, pasted. The manager added the id, the marker and the state.*

`100.1` `ASSUMPTION` — **The human-channel bound reads as a bound on starting, not on running.** Clause 3 demands
that a pick exceeding *"exactly one question is in front of the human at a time"* is not started, and the node's own
unsettled section fixes the conservative reading. I settled the ambiguity it leaves: whether that forbids two HITL
nodes running concurrently, or only forbids starting one onto an occupied channel. I wrote the latter, and said so in
the text. The former would contradict the effort's map (*"Two grilling nodes run at once to keep the human's queue
full"*) and would empty tier 2 of the queue, which clause 7 requires be unchanged; under the latter, a second
grilling node is started the moment the channel frees and everything already in the file stays true.

`100.2` `ASSUMPTION` — **The pick report's "awaits no answer" was written in `### Picking the next node` rather than
added to the list of three non-claimants.** `## What is in front of the human, and when` enumerates *"Three things
are not claimants at all"*, and a pick report is arguably a fourth. I left that sentence untouched because clause 7
forbids changing the meaning of any rule clauses 1–4 do not add, and the sentence claims no exhaustiveness. If the
human would rather the list read four, that is a one-line edit to a sentence I deliberately did not touch.
