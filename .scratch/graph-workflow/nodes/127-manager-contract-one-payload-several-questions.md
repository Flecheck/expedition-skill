# Say in the manager's contract that one payload may carry several of one worker's questions

Type: implementation
Status: superseded
Superseded by: 336

Blocked by: none

## Question

*Surfaced by [Whether the manager sends the human questions in batches](117-questions-sent-in-batches.md)'s worker,
and pasted as it wrote it.*

> The manager's contract says exactly one *question* is in front of the human, which is false of a payload carrying
> two, and it justifies the names-what-else-is-waiting rule on a ground that a multi-question payload falsifies.
> Repair both, and state that the manager never batches across nodes.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 117's worker. Pasted as it wrote it, and not the manager's.*

> In `.claude/skills/expedition/SKILL.md`, the section headed `## What is in front of the human, and when` states all
> of the following, and nothing in that section contradicts any of them.
>
> 1. What is in front of the human at any time is exactly one thing awaiting their reply, and nothing ever displaces
>    a live one. Where that thing is a payload relayed from a worker, it may carry more than one question from that
>    one worker and still counts as one.
> 2. That section does not state that exactly one *question* is in front of the human, that wording being false of a
>    payload carrying two.
> 3. The rule that a relayed payload names in one line whatever else is waiting — by node name and kind only, never
>    restating another payload's question or its options — is kept.
> 4. The reason that section gives for item 3 is that a named-but-unasked item cannot be answered by accident. That
>    section does not justify item 3 on the ground that it keeps a terse reply attributable to exactly one thing,
>    that ground being false of a payload which carries more than one answerable question by design.
> 5. The manager never combines questions from different nodes into one payload, and never divides one payload's
>    reply between two workers: a payload comes from one worker, and its reply goes back to that one worker
>    unaltered.
> 6. This condition demands nothing about any other sentence in that section or that file — in particular nothing
>    about what the things that are not claimants are called — so a change to any other term there neither satisfies
>    nor breaks it.

## The manager's note at filing

*Not a change to anything above.*

**Clause 6 is written to survive node 107's rename**, which was live and unanswered when this condition was written.
That is the first condition on this graph to immunise itself against another node's pending decision, and it is worth
copying.

**One collision the manager must sequence rather than the worker.** This node and [node
118](118-carry-the-channel-free-rule-into-the-contract.md) both edit `## What is in front of the human, and when`.
Node 118 carries node 108's channel-free rule into the same section. With a code slot of one they serialise, but
whichever runs second reads a section the other moved.

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 336](336-carry-the-rules-on-what-reaches-the-human-the-code.md), the merge [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole.
