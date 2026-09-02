# A node's flags arrive after the human moment that was supposed to settle them

Type: grilling
Status: resolved

## Question

**The human reported this as a defect in the shipped skill.** Their words, `verbatim`: *"I think there is an issue
with the skill, when I say approve, the flags are supposed to be approved also."* They said it while pointing at
[flags.md](../flags.md)'s lines for `18.4`, `18.5` and `18.6` — six flags left unchecked on a node whose answer they
had already given.

### The rule, and why it cannot be performed as written

`.claude/skills/expedition/SKILL.md` states: *"A node's flags are settled at the human moment that ends that node — a
grilling node's last answer, an implementation node's gate — while the work is still in front of everybody and
judging a flag is cheap."* [map.md](../map.md) carries the human's standing instruction behind it, `verbatim`: *"Also,
when I approve the end of the node, the flags should be considered ok"*.

**For an implementation node the rule works.** Its flags exist before the gate, the gate payload carries them, and
the approval settles them. That is what happened at [Qualify the graph-file ban in the worker
contracts](58-qualify-the-graph-file-ban.md), whose four flags settled the moment the human said *"approve."*

**For a grilling node the rule is unperformable, and it is unperformable by construction.** A grilling worker's flags
arrive in its **handover**, which comes after its last question is answered. So at the human moment that is supposed
to settle them, they do not yet exist. The rule names that moment anyway.

The same holds for every node kind whose flags reach the manager only in the handover, which is all of them except
implementation: `research` and an AFK `precondition` have no human moment at all, and the contract already routes
those to the closing report. **Grilling is the case nothing routes** — it has a human moment, and its flags miss it.

### The evidence is three nodes in one session, handled three different ways

- **[The human rejects *most efforts never end*](86-most-efforts-never-end-rejected.md)** — the manager reported the
  close, said the three flags would settle with the human's next reply unless they objected, and settled them when a
  reply came that was about something else.
- **[How a condition's scope is amended](82-amending-a-condition-whose-scope-was-too-narrow.md)** — the manager
  reported the two flags as *"not urgent"* and left them unchecked.
- **[Adopting an in-flight effort](18-adopting-in-flight-effort.md)** — the manager filed six flags unchecked and
  said they *"had no human moment"*.

**Three dispositions, one session, one manager, no rule.** All eight were settled afterwards at the human's
complaint, which is the route the contract calls the exception path.

### What the answer has to settle

1. **What the settling moment is for a node whose flags arrive with its answer.** The candidates are: the manager's
   report of the node's close, settled on the human's next word whatever it is about; a settling act of its own,
   which the contract currently says is *not* a claimant for the human's attention and so may not take a turn; or the
   worker raising its flags before its last question so they ride the existing moment.
2. **Whether a flag can be settled by silence.** The standing instruction ties settlement to the human *approving*.
   A grilling node's close is reported and not approved — nothing asks them to approve it — so either the close
   report starts asking, or settlement stops requiring their word.
3. **Whether `## What is in front of the human, and when` changes.** It lists settling a flag among the three things
   that are *not* claimants, precisely because it rides a moment that already exists. If a grilling node has no such
   moment, that entry is what has to give.

### What is not this node's

The **content** of any particular flag. This is about when and how a flag is settled, never about whether any
judgement in one was right.

## Where it came from

The human, unprompted, having noticed six unchecked lines in `flags.md` for a node they had already answered. Minted
by the manager at their instruction; the framing above is the manager's and their words are quoted verbatim at the
top.

## Interview

### Attempt 1 — which moment settles a grilling node's flags

**Q1, from the worker.** *"For a grilling node, should the settling moment be the report you get when that node
closes and the manager proposes the next work — with that report obliged to carry every flag the node holds, in full
— so that your reply to it is the settlement?"* Its recommendation, in its words: *"Yes."* Its three alternatives
were that flags take a turn of their own, that the worker raises its flags before its last question, and that they
wait for the effort's closing report.

**A1, from the human**, `verbatim`: *"ok for recommended."*

**The option taken**, quoted from the worker, which wrote it: the settling moment is *"the report you get when that
node closes and the manager proposes the next work — with that report obliged to carry every flag the node holds, in
full — so that your reply to it is the settlement."* Not a divergence.

**What the worker attached to the recommendation and the answer therefore carries**: that the repair is *"changing
four words in the shipped files ('a grilling node's last answer' becomes 'the report that closes the node') rather
than by adding a mechanism"*, and that the gate's existing duty carries over — *"a payload that omits a flag settles
that flag silently, so every flag the node holds must be in the report."*

## Answer

*Written by the node's worker and pasted as it wrote it.*

**A grilling node's flags are settled at the pick report that closes it, and not at its last answer.** The human, on
the recommendation: *"ok for recommended."*

The rule was unperformable because it named a moment the flags had not reached yet. It named the wrong moment rather
than a missing one: a moment already existed, one message later, and nothing had noticed it was a human moment.

### The moment

The **pick report** — the message the manager owes the instant a node closes, naming what it has started next. It is
already unprompted, already owed on every node's close, and the manager is holding the worker's handover when it
writes one. Nothing new is created.

### It awaits no answer, and the settlement rides one anyway

This is the part that had to survive [The manager starts the next node rather than proposing
it](100-the-manager-starts-the-next-node-rather-than-proposing-it.md), which makes the pick report explicitly a
non-claimant that expects no reply and turns a redirection into a correction after the fact.

**Awaiting an answer and being settled by one are different acts.** The manager holds nothing open, blocks nothing,
and takes no place in the human's queue. The settlement **rides** whatever the human says next rather than waiting
for it.

- The human's next word settles the flags **whatever that word is about**. It need not mention them.
- **Where the human never speaks again, nothing settles.** The flags stay outstanding and reach the effort's closing
  report by the existing route for a flag whose moment never came.
- **The manager never settles a flag on its own judgement, or on the passage of time.** Silence is not settlement; a
  word is.

Node 100's model is the same discipline: the manager acts, and the human corrects after the fact. This applies it to
flags rather than departing from it.

### The duty that comes with it, and why it is this node's to impose

**A pick report closing a node that holds flags carries every one of them, in the fuller form a gate payload uses** —
what was decided, why, and the context needed to answer it — because a payload that omits a flag settles that flag
silently. That rule already stands at the gate in the manager's contract; this extends it to the pick report
unchanged.

**The demand is this node's and not [node 46](46-what-the-manager-reports.md)'s.** Node 46 asks what the manager's
report *contains* and is a collation. This node asks what makes the act a **settlement**, and a report that does not
present a flag cannot settle it — the demand is constitutive of the answer rather than an item on a list. Node 46
inherits it as a fifth duty to collate and does not get to re-decide it.

### What this legitimises and what it rejects

Of the three dispositions one manager reached in one session, this endorses **one**:

- [The human rejects *most efforts never end*](86-most-efforts-never-end-rejected.md) — settling on a reply that was
  about something else was **right on timing**. What was wrong is that the report had not presented the flags in a
  form the human could judge. The defect was presentation, not silence.
- [How a condition's scope is amended](82-amending-a-condition-whose-scope-was-too-narrow.md) — leaving flags
  unchecked as *"not urgent"* is not a disposition; urgency was never the trigger.
- [Adopting an in-flight effort](18-adopting-in-flight-effort.md) — *"had no human moment"* was false. It had one,
  one message later.

### What does not change

`## What is in front of the human, and when` stands as written. Settling a flag is still not a claimant, still on the
ground that it rides a moment that already exists. Only the identification of the moment was wrong. (Raised as flag,
below — nobody was asked.)

### The name

The shipped contract calls it **the pick report**. The effort's map calls the same message *"a closing report"*,
which is the glossary's name for the once-per-effort report the manager hands over when the frontier empties. Two
different things under one name, in the effort's two most-read files. Every per-node use is *pick report*.

### What this reaches beyond grilling, and does not settle

Every node's close is reported by the same pick report — a `research` node's and an AFK `precondition` node's
included. So the ground on which those two kinds are routed to the closing report, that they *"never end in front of
the human"*, is false. Whether they should move is not what the human assented to and is reported as a node.

### What the worker returned as `INVALIDATIONS`

*Pasted as it wrote it.*

[Whether flags.md survives the settle-at-close practice](27-does-flags-file-survive.md) — its **conclusion stands and
one of its grounds is false**. Its answer states, under *"Why the premise cannot hold"*, that *"the practice cannot
reach every node by construction"* because a `research` node's and an AFK `precondition` node's flags *"wait for the
closing report, because those kinds never end in front of the human."* Every node's close is reported by a pick
report, so those two kinds do end in front of the human. The node's decision — that `flags.md` stays, as the capped
index of every judgement an agent made on its own — does not rest on that ground and is untouched: its other two
grounds, the outstanding flags whose nodes resolved before the practice existed and a flag surviving its own gate,
are unaffected. The same false ground is repeated in `graph-conventions.md`'s `### Settle a flag`, which is why the
implementation node above touches it and the grilling node above decides what replaces it.

Nothing else. The node file's own claim that `research` and an AFK `precondition` *"have no human moment at all"* is
the same falsehood, but that is this node's framing rather than a resolved node.

## Flags

*Each entry is the worker's own prose, pasted. The manager added the id, the marker and the state.*

`99.1` **· settled** `ASSUMPTION` — **the three-non-claimants entry stands.** The manager contract's `## What is in front of the
human, and when` lists settling a flag among three things that are not claimants for the human's attention, on the
ground that it rides a moment that already exists. This node's third sub-question asked whether that entry is what
has to give. I judged it decided by the first sub-question rather than separately, and settled it on my own
authority: the pick report is a moment that already exists and awaits no answer, so settling a flag on it still takes
no turn, and the entry's ground holds unchanged. I did not spend a round of the human's attention on it and nobody
was asked.

`99.2` **· settled** `ASSUMPTION` — **the name of the per-node message.** The answer has to name the moment, and the moment had two
names. The shipped manager contract calls it the pick report; the effort's map calls it *"a closing report"*, which
is what `CONTEXT.md` calls the once-per-effort report, and whose `Handover` entry already says *"report (the closing
report owns that word)"*. I chose **pick report** on my own authority, on the ground that it is the shipped name and
the collision is the map's, and wrote the map's repair into the implementation node's condition. `/naming` was not
run and the human was not asked.

`99.3` **· settled** `ASSUMPTION` — **what the human's next word settles.** The human assented to their reply to a report settling
that report's flags. Node 100 then established that the manager starts the next node immediately, so more than one
pick report can reach the human before they speak once. I settled the case they were not asked about: the human's
next word settles every flag presented to them since their last word, across however many nodes. The alternative —
the manager tracking which word belongs to which report — reintroduces exactly the bookkeeping the non-claimant rule
exists to avoid, and over-settling is recoverable where the state the human complained about is not: a settled flag
can still be promoted to a node, and `flags.md` already records that a checked box means the human dealt with a flag
rather than agreed with it.
