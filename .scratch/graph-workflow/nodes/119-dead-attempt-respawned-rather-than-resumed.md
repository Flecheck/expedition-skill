# Whether a dead attempt is resumed from its transcript rather than replaced

Type: grilling
Status: claimed

## Question

**The human asked this.** Their words, `verbatim`: *"Why are the work/checker respawned and not resumed ? It would
prevent using to many tokens no ? Or you can't ?"*

### What the files fix today, and what the manager has actually been doing

**A live worker is resumed, and that is shipped.** `CONTEXT.md` and the manager's contract both say a worker *"is
resumed in place rather than replaced"*, and every grilling answer and every correction round this effort has run
went back to the same agent.

**A dead attempt is replaced, and that is also shipped.** The glossary's `attempt` entry: *"A node outlives its
attempts: a dead worker is replaced, and the replacement is a new attempt recorded after it."* [Relay
protocol](08-relay-protocol.md) built the recovery around replacement — *"death is detected lazily by a failed
resume, recovered by replaying an at-relay-time log on the node file, capped at two respawns"* — and the whole
at-relay-time write rule exists so that a replacement starts with the human's banked words.

**Three deaths on this effort, all replaced.** [What the manager reports to the human, in one
place](46-what-the-manager-reports.md)'s attempt 1 died having spent roughly 485k tokens, and its scan was written to
`recovered/` precisely so attempt 2 would not re-run it — a mechanism invented because replacement throws work away,
and now [The `recovered/` directory is a sixth file kind the graph's conventions do not
define](104-recovered-directory-is-a-sixth-file-kind.md). [Starting an effort has no section in the manager's
contract](98-starting-an-effort-has-no-section.md)'s attempt 1 died after the human's answer had reached disk, and
attempt 2 re-read the node and both its blockers. [Carry the pick-report settling moment into the shipped files and
the map](103-carry-the-pick-report-settling-moment.md)'s first checker died having read nothing.

**What the human's question exposes.** The harness reports, on every death, that the agent *can be sent another
message and resumed from its transcript*. Nothing in the shipped files considers that. So *replace* may be a rule
written when resume was believed impossible, and the cost of it is measurable rather than hypothetical: one dead
attempt on this effort cost 485k tokens and a sixth file kind to salvage.

**What stands against resuming.** A checker is a different case from a worker: it is deliberately blind and
deliberately independent, and a checker resumed after a correction round carries its own earlier verdict, which is
why every re-check on this effort was a fresh agent **by design and not by accident**. And a resumed dead attempt's
state is unknown in a way a replacement's is not — nobody has established what a limit-killed agent's context holds,
or whether a worker that died mid-write left the tree in a state it will not re-examine.

### The question

Is a dead attempt resumed from its transcript rather than replaced — and if so, does that reach a **checker**, whose
independence is the reason re-checks are fresh agents? What establishes that a resumed dead attempt's state is sound
enough to continue from, and what happens when it is not?

## The manager's note at filing

*Not a change to anything above.*

**This node has priority over most of the frontier by a standing rule of the human's**, in the map: *"Token-use
improvement is prioritised above the rest of the frontier"* — with that rule's own caveat, that a ranking by
*predicted* saving is the token-maxing failure in reverse. The 485k figure at node 46 is measured; what resuming
would have saved is not.

**The manager has not answered the human's question and this node file does not answer it.** The paragraphs above
state what the shipped files say, what the manager did, and what the harness reports. Whether the manager *could*
have resumed those three dead attempts is part of what this node establishes.
