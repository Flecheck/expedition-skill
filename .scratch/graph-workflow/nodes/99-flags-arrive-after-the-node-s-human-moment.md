# A node's flags arrive after the human moment that was supposed to settle them

Type: grilling
Status: claimed

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
