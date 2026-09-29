# Friction from running this map by hand

Type: precondition
Status: resolved

## Question

Write down the friction observed while running this workflow by hand on its own map, before the record
of it decays further.

Raised by the human as steering: *"You should write your findings down somewhere, I don't know if it is
a new node or something else."*

[Dogfood target](09-dogfood-target.md) requires *"a record of the friction found while using it"* as the
Lang run's second output. This node records the fact that **a second corpus already exists and nobody
had written it down**: every session that produced these 23 nodes was the workflow being operated by
hand, by a manager with no skill files for most of it. That is a real effort's worth of use, paid for
already.

It is a `precondition` because it decides nothing and produces no product code, and because two open
questions cannot be judged without it — whether the runtime is too simple, and whether the graph needs a
tool.

**This record is retrospective and partly from memory, which makes it weaker than one kept live.** The
per-session transcripts under `~/.claude/projects/` are the primary source and are not summarised here.
That weakness is itself the first finding.

## Answer

### What actually hurt

**1. The mechanical checks were re-derived by hand, every session.** The eight invariants
[Graph file format](13-graph-file-format.md) fixed are all decidable by reading files, and nothing reads
them. [Write the graph conventions document](21-conventions-document.md) produced five naive-scan false
positives in one session, every one from a rule the format had already stated. The session after it
ported a checker to Perl — after discovering the machine has no `python3` and no `node` — and ran it
three times; this session ran it twice more. **The script lives in `$TMPDIR` and has been rewritten more
than once**, because it dies with the temp directory and was never product. This is the
tool-extraction fog item's evidence, and the cost is now measured rather than predicted: one
re-derivation per session, indefinitely.

**2. `map.md` has outgrown its own job description.** It is defined as *"the whole effort at low
resolution, read once per session"*. It is now ~74 lines of which the `## Notes` block is fifteen
paragraphs and the fog is six single paragraphs of 300+ words each. **The never-delete rule and the
load-once-cheaply job are in direct tension, and never-delete is winning.** The split of
[decisions.md](../decisions.md) out of the map bought exactly one growth axis back; the other two —
notes and fog — were left growing.

**3. Fog items grow by accretion into archaeology.** The implementation-nodes fog item carries about
eight append-marked updates from eight different nodes inside one paragraph, each beginning *"Partially
graduated by…"* or *"Now also…"*. It is a correct record and it is no longer a *view*. The format says
fog is written as loosely or fully as the view allows; it says nothing about what happens after the
tenth update to the same item.

**4. Never-delete makes node files expensive for the party that has to read them.** A worker's first act
is to read its own node file. Several now interleave struck-through paragraphs with live ones, and
[Git and code-landing policy](11-git-and-code-landing.md) carries an annotation that *corrects its own
answer* a hundred lines below that answer. The rule is right for the record and it taxes the reader —
and the reader is the worker, not the human.

**5. Flags are write-only.** Thirteen outstanding, zero settled, across 23 nodes. They were designed to
cost nothing until the closing report, and the evidence is that they also *do* nothing until then. Only
[Human review of landed code](20-human-code-review.md) found a place where acting on one is cheap. On an
effort that runs for months this is a large, invisible, growing pile.

**6. The graph stayed uncommitted for the entire design.** [Git and code-landing
policy](11-git-and-code-landing.md) says the human commits the graph *"periodically"*. In practice
nobody did until the human was asked directly, at 23 nodes and two commits. Not a tool problem — a
policy that depends on an unprompted habit did not get one.

**7. The one-node-per-session rhythm describes one type out of five.** [Write the graph conventions
document](21-conventions-document.md) found that an implementation node cannot resolve in the session
that does the work, because two of its four steps belong to someone else. This node found that a
precondition arguably should not count against the rhythm at all. What is left is that the rule
describes `grilling` and was inherited as though it described everything.

### What the record says about the runtime, which is the question nobody could answer

This is the part that bears on [Runtime that hosts the manager and its
subagents](02-runtime-host.md)'s standing *"might be a bit too simple"*.

**8. The manager's context is the binding constraint — not the human's attention.** The map's governing
principle is *"the human is the scarce resource; parallelism exists to saturate the human, not the
machine."* Across these sessions the human was never the thing that broke. **The manager's context was,
repeatedly**, including inside this session. Every session ended or compacted before its work did. The
principle is not wrong about what to *optimise*, but it is wrong about what will *fail first*, and every
design that spends manager context freely — rendering diffs, re-authoring handovers, re-deriving checks —
was priced against the wrong constraint.

**9. A checker died on a session limit.** [Write the graph conventions
document](21-conventions-document.md)'s checker completed one of four phases against a ~600-line document
and never issued a verdict; the node resolved on an inference, and the `ASSUMPTION` flag recording that
is still outstanding. First hard datum on *too simple*: a single AFK agent could not complete a
single-node check.

**10. The relay has been exercised once, in a prototype, and never since.** Nodes 09 through 20 were
grilled by the manager **directly**, with no worker and no relay — each one carries a flag saying so.
The design's central mechanism has one run behind it, and the manager-as-scribe rule decided last session
has zero, because there has never been a handover to scribe. **The workflow has mostly been designed
rather than used**, and its own map is much weaker evidence for it than the node count suggests.

### What worked, recorded because a friction log that only lists pain is not a record

**11. The `decisions.md` cap works, visibly.** The ten pre-cap entries run 40–120 words each; the six
capped ones run ~25 and are strictly more usable. The difference is legible in one file.

**12. Refer-by-name held across 23 nodes.** Not once has narration needed a bare id, and the map is
readable aloud. The cheapest rule on the map by a wide margin.

**13. The map's `## Notes` as a manager-maintained region works.** The bar's discovered commands, the
source hierarchy, the credit constraint and three conventions-document deltas were all written there by
different sessions and all found again by later ones. It is the one growing region that has not decayed.

**14. `_Avoid_` lines caught real drift.** `issue`, `task`, `reviewer`, `done` and `REJECT` were each
stopped by name rather than by anyone remembering. The rename of `REJECT` this session was caught only
because the glossary makes collisions visible.

### What this changes

- **[Runtime that hosts the manager and its subagents](02-runtime-host.md)'s flag now has evidence, and
  it points somewhere unexpected.** *Too simple* was expected to fail on node count or on portability.
  The observed failure is **the manager's own context**, every session, and that is not fixed by a bigger
  graph tool or a cheaper model.
- **The tool-extraction fog item is no longer arguing from prediction.** One hand re-derivation per
  session, a throwaway script rewritten more than once, five false positives in a single session.
- **[Graph file format](13-graph-file-format.md) has an unreckoned growth problem.** It split
  `decisions.md` out for exactly this reason and left `## Notes` and the fog growing on the same
  never-delete terms.
- **[Dogfood target](09-dogfood-target.md) should require its friction record be kept *during* the run.**
  This one was written afterwards and is weaker for it — findings 1, 5 and 8 are reconstructions, and the
  per-session detail behind them is in transcripts nobody will re-read.
- **[Workflow self-improvement during use](19-workflow-self-improvement.md) inherits a live example**: at
  least three findings here are fixable *by* the workflow *while* it runs, which is precisely that node's
  question.
- **No new node, and deliberately so.** Each finding lands on a question the map already holds. Promoting
  any of them now would pre-empt the node that owns it.

## Annotation: finding 8 was right about the constraint and wrong about the mechanism

Added on the human's correction, given immediately after this node resolved. Verbatim: *"For the manager
context, I compacted it in between each task as one task took aroung 200k tokens. Ideally in the final
workflow, most of the context is in the workers and not in the manager."*

**Nothing broke. It was operated.** Finding 8 said the manager's context *"was, repeatedly, [the thing
that broke]"*, which reads as a failure discovered in flight. It was not: the human compacted between
nodes as standing procedure, because a node costs about that much. The direction of the finding stands
and its mechanism was wrong — a managed cost, not a crash.

**And the number makes the finding quantitative, which it badly needed:**

- **~200k tokens of manager context per node.** Measured across the sessions that built this graph, by
  the person paying for them.
- **The inherited sizing rule says 100k.** A node's question is specified as *"sized to one 100K token
  agent session"*. The manager pays roughly **double** what that budgets, and the gap is exactly its
  overhead — reading `map.md` and the graph, holding the interview, writing the files — none of which a
  worker handed three pointers would carry.
- **Extrapolated to the dogfood target, hand-operation is impossible rather than merely slow.** 179
  nodes × ~200k ≈ **36M tokens of manager context** if the manager keeps doing the work itself. That is
  the number that ends the argument, and it is the same argument finding 10 makes from a different
  direction: the relay exists to move that cost off the manager and has been used once.

**The human's own statement of intent, now a standing preference on the map:** *most of the context lives
in the workers, not in the manager.* Recorded in `map.md`'s `## Notes`, because it governs decisions no
single node owns — what a spawn carries, what a handover returns, whether the manager renders or points.

### Finding 15 — a node's name hid its contents from the person who wrote it

Surfaced in the same message. The human proposed creating a node for prioritisation of work, *"as just
taking issues in order is not good enough"*, and that node already existed: [Human-initiated
steering](16-human-steering.md) has owned the manager's selection policy since [Dogfood
target](09-dogfood-target.md) sharpened it, holds Lang's fan-out-ranking precedent, and holds the
flags-pulled-forward point the human raised in the same breath.

The refer-by-name rule is finding 12 and it works — **but it only works if the name covers the node.**
This one is named for the *override* and owns the *policy* being overridden. Two costs, both real: a
duplicate node was nearly created, and the node sat on the frontier for four sessions while the thing it
answers was being felt as friction. Cheap to fix and its own node's call, since renaming is free while a
node is unstarted.

## Flags

`ASSUMPTION` — **resolved as a second node in one session**, which the inherited one-node-per-session
rhythm forbids. Defended on the grounds that a `precondition` asks the human nothing, decides nothing, and
costs only machine context — and that its input was this session's memory, which is the thing that
expires. Finding 7 above is the same rule failing for a different type, so this is evidence for revisiting
the rhythm rather than an exception carved for convenience.

`ASSUMPTION` — **written retrospectively rather than during the run**, so findings 1, 5 and 8 are
reconstructions from a manager's memory across compacted sessions rather than notes taken at the time. The
transcripts are the primary source and were not re-read to produce this.

## Annotation: finding 4 names the wrong party, measured

*Filed by the manager, in the reporting worker's own words.* [How an agent workflow and its skills reduce their
own token cost](52-token-cost-of-a-workflow.md)'s worker reported this as an `INVALIDATION` against this node:

> Both state that never-delete and load-once-cheaply are in direct conflict *and that never-delete is winning*.
> Measured: struck-through text is 1,649 of 79,361 characters in `map.md` (2.1%) and 4,269 of 982,260 across all
> 54 node files (0.4%). The cost is live prose under the append-in-place practice — `map.md:75` alone is 20,589
> characters, 26% of the file — not retained superseded text. The conflict is real; the party winning it is
> misidentified, and one of the fog item's four candidate remedies (prune struck text into an archive) is
> therefore worth 2.1% while another (cap an item's updates) addresses the actual cost.

**Finding 8 is not invalidated and is supported, with one correction of frame**, in the same worker's words:
*"it is the binding constraint on the **window**, priced by the harness at the cached-read rate, so it is an
accuracy and capacity limit rather than the place the bill is incurred."* The bill is the fleet: every worker
pays its whole opening payload **uncached**, because a subagent's prefix differs from its parent's and reads none
of the parent's cache.

*The manager's note, 2026-09-29:* this node's flags carry no ids, so none can be marked in place. They are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*), by their lines in `flags.md`.
