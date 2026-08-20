# Nothing carries a flag's account of what produced it out of a worker

Type: implementation
Status: open

## Question

[`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md)'s `### Raise a flag`
procedure requires a **third** piece of writing for every flag, beyond the two [A worker's handover carries
no acceptance condition for the node it mints](35-handover-mints-no-condition.md) just fixed:

> The round that raised the flag — an `## Interview` attempt or a `## Review` round — says **what produced
> it**, and for a flag written from a worker's own unprompted judgement that means what the worker actually
> did, in its words. A one-line summary is enough under `## Flags`; it is not enough in the round that
> created it. Where there is no round at all — a `research` node, an AFK `precondition` node — the
> `## Flags` entry carries that account itself.

**No handover part carries that text out of any worker.** After node 35 the five contracts ask for the
`## Flags` prose and the `flags.md` sentence, and nothing else. So the account — *what the worker actually
did*, explicitly *in its words* — has no route from the party that holds it to the file that requires it.

### This is the same defect a third time, which is why it is a node and not a clause

Node 35's subject was a handover part naming fewer artifacts than the graph needs: `NEW NODES` naming four
elements where an implementation node needs five, and `FLAGS` naming one artifact where a flag entry lands
in two. This is the third instance and the one that node could not reach — its acceptance condition named
two places, so a worker complying with it produced a section that says two.

Found by that node's **blind checker**, as a note attached to the question that opened its correction round.
Promoted to a node by the human, whose words on being shown it were *"we will need to do something"* against
the manager's proposal to mint rather than fix in place.

### What the answer has to decide, and one thing it must not assume

**Where the account goes when there is a round, versus when there is not.** The clause splits: with a round,
the account belongs to the `## Interview` attempt or the `## Review` round; with no round — `research`, AFK
`precondition` — it belongs to the `## Flags` entry, which node 35's correction round taught those two
contracts. So the no-round half is now covered and **the round half is not**: for a grilling, prototype or
implementation worker, nothing carries the account to the round that created it.

**Not to assume: that this is a sixth handover part.** Two cheaper shapes exist. The `FLAGS` part could ask
for the account as a third element beside the prose and the sentence, since it is flag text and travels with
the flag. Or the account may already be reaching the round by another route — a raise's `SO FAR`, a
correction round's report of what changed — in which case what is missing is the instruction to file it
there rather than the text itself. Establish which before adding a part: [Off-contract subagent
output](17-off-contract-output.md) settled that the manager files what it can paste, and a part that
duplicates text already arriving is cost with no gain.

**One asymmetry worth checking rather than assuming.** The requirement says *in its words*, which is the
scribe rule biting: the manager may not write this account, and the two measured instances of the manager
authoring flag text — nodes 33 and 36, flag `33.4` — are the same failure this one would produce.

### The acceptance condition is owed

Written by whoever spawns this. Note that it may not be claimed without one, and that node 35's evidence
says the writer should read it back against the self-containment rule before handing it over — a duty the
five worker contracts now carry and the manager's own skill does not.

### What the answer touches

The five `.claude/skills/expedition-<type>/SKILL.md` contracts, and `graph-conventions.md` only if the clause
above turns out to be the thing that is wrong rather than the contracts.

**Sequencing, not a blocker.** Those five files are also the live territory of [Checking a flag before the
human sees it](30-checking-a-flag-before-the-human.md), [Narrow the flags.md clause in the worker
contracts](32-narrow-flags-file-clause.md) and [Nothing tells a worker to hold its work against the
record](37-invalidations-is-not-a-check.md). The landing policy forbids a second commit against one **node**,
not against one **file**, so these may run in any order — but not concurrently, the code slot being
exclusive.
