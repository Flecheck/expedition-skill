# Whether the manager sends the human questions in batches

Type: grilling
Status: claimed

## Question

**The human asked for this node.** Their words, `verbatim`: *"I think we might want to do like the new grilling
skill, where questions are sent in batches. I think it might be more efficient in terms of token and it reduces
context switching for the user. Can you create a grilling node for it"*

### What the effort has fixed against this, and what it has not

**One question at a time is settled and has just been restated.** [When the human's channel is free, and whether the
manager must fill every gap in it](108-when-the-humans-channel-is-free.md) closed on the human's own wording, `verbatim`:
*"there should be at most one question offered to the user and if there is none and there is a question waiting from
one of the subagents, it should be offered to the user"* — a ceiling of one and a floor of one. And [What the manager
works on next, and how the human redirects it](16-human-steering.md) records the measured cause of the ceiling: two
questions were asked at once, a reply named an option in one and named nothing in the other, and the manager could
not tell which node the reply belonged to. **So this node is not a fresh question. It asks the human to revisit a
rule they set, on a ground they have now supplied.**

**What is genuinely open.** The two claims in the instruction are both about cost rather than about correctness — that
batching is cheaper in tokens, and that it reduces the human's context switching — and neither has been measured on
this effort. Against them stands the attributability problem node 16 measured, which a batch reintroduces by
construction. The batch's shape is undecided in every part: how many, whether a batch may mix tiers, whether a gate
may sit in one, what happens when a reply answers three of four, and whether the ceiling of one becomes a ceiling of
one *batch*.

**The named prior art is a file this effort has not read.** The instruction points at *"the new grilling skill"* — an
external skill of the same family as the `/grilling` this effort's contracts name, and the effort's own record has
nothing about how it batches. Reading it is part of this node's work, and it is the one thing here that may need a
source outside the working directory.

## The manager's note at filing

*Not a change to anything above.*

**Filed as grilling and not as implementation**, because the shape is undecided and because a rule the human set is
what would change. The manager wrote none of the question's substance: the paragraphs above state what the record
already fixes and what it does not, and take no position on whether batching is right.

**Three of the effort's own flags are the standing evidence against the token claim being obvious**, and whoever
holds this node should weigh them rather than take the manager's word: `102.3`, `94.5` and `91.3` each record a
grilling worker declining to invoke a method skill *because the load was not judged worth its cost* — so this effort
has a measured habit of treating per-question overhead as small. Whether a batch's saving is in the manager's tokens,
the worker's, or the human's attention is not stated in the instruction and is not the same question.

**Adjacent and deliberately not merged:** [Whether the contracts' instruction to invoke a method skill is doing any
work](113-whether-the-method-skill-instruction-does-any-work.md) is about the same external skill family and decides
nothing about batching.
