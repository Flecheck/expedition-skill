# Every manager report ends with one line saying what is expected of the human

Type: implementation
Status: open

## Question

**The human asked for this node.** Their words, `verbatim`, given at [Qualify the graph-file ban in the worker
contracts](58-qualify-the-graph-file-ban.md)'s gate: *"Also I want to add to the manager skill to always end with a
short phrase that says what is expected of the user, like what you did now. So that can look at the last line and
know what I need to look into. Create a node"*.

**The instance they are pointing at** is that gate's own last line, which read `**Approve, correct, or reject.**` —
one short line, at the very end, naming the act the human is being asked to perform.

### What the manager's contract says today, and what it does not

`.claude/skills/expedition/SKILL.md` has a whole section on what reaches the human — `## What is in front of the
human, and when` — which fixes the one-at-a-time rule, the two tiers, and the three things that are not claimants.
**None of it says anything about the shape of what the manager writes.** The contract's own list of duties nobody has
settled opens with exactly this hole: *"What must your report to the human contain? Duties have accumulated on it
from several directions and nothing collates them, so there is no statement of what a complete one looks like."*

So this node does **not** settle that duty. It adds one property to the end of a report and leaves everything else
about a report's contents where it is.

### Why the last line rather than the first

The human's stated reason is a scanning one, in their words: *"So that can look at the last line and know what I need
to look into."* The position is load-bearing rather than incidental — a report ending in prose leaves the reader
searching for the ask, and the ask is the only part they must act on.

### What is unsettled and is left to whoever claims this

- **A report that asks for nothing.** Several things the manager sends await no answer at all: telling the human an
  agent died, reporting a pick, the closing report. Whether those end with a line saying *nothing is expected of you*
  or end with no such line is not settled here.
- **Whether the line names the node.** A gate's *approve, correct, or reject* is unambiguous because only one gate is
  ever in front of the human; a report that both closes one node and starts another may need to say which.

## Acceptance condition

***Written by the manager, for a node the manager minted itself*** at the human's instruction. Marked as the
manager's own under [Who writes the acceptance condition for an implementation node the manager mints
itself](39-condition-for-a-manager-minted-node.md), whose constraint 1 confines it to what is already fixed. **The
human's instruction is fixed; its wording and its placement in the file are not, so this condition states the
property and leaves the form.**

1. `.claude/skills/expedition/SKILL.md` states that every report the manager puts in front of the human **ends with
   one short line naming what is expected of them**, and that this line is the last thing in the report.
2. It states the reason, which is the human's own: that the reader can look at the last line alone and know what they
   must act on.
3. It states what the line contains — the act or the choice being asked for — and that it is short. It does **not**
   prescribe a fixed set of wordings, which would need a judgement this condition does not make and nobody has made.
4. Where the contract already names a report or a payload that reaches the human, that statement is not weakened: the
   new rule adds a closing line and removes nothing any existing section requires.
5. No other file under `.claude/skills/` changes, and no file under `.scratch/` changes.
6. No section of `.claude/skills/expedition/SKILL.md` is removed, and no rule in it other than what clauses 1–3 add
   changes its meaning. In particular the nine duties listed as unsettled are not reduced to eight: the first of them
   — what a complete report must contain — is **not** settled by this work, and still stands as an open duty after
   it.
7. The working tree meets the bar.

### The manager's read-back, recorded before the claim

*[Node 39](39-condition-for-a-manager-minted-node.md)'s constraint 2 requires the condition to be read back against
the two rules that bind every condition, and that reading recorded on the node.*

- **Self-contained text.** It passes. The property demanded, its reason and its placement are written out here rather
  than pointed at; the file it changes is named by path, and the checker has the repo. Clause 6's reference to the
  nine unsettled duties names a list inside the file under change, which the checker can read there.
- **It does not quantify over the record.** It passes. Every clause is a demand about the state of one file or about
  what changed in the tree, which `graph-conventions.md` permits by name. No clause holds the work against the
  effort's resolved nodes.

## Where it came from

The human, unprompted, in the same reply that approved node 58's gate. Minted by the manager at their instruction;
the question above and the acceptance condition are the manager's, and the instruction itself is quoted verbatim at
the top.
