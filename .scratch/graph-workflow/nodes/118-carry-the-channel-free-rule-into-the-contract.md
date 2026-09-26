# Carry the channel-free rule and the manager's duty to fill a gap into the manager's contract

Type: implementation
Status: superseded
Superseded by: 336

## Question

*Surfaced by [When the human's channel is free, and whether the manager must fill every gap in
it](108-when-the-humans-channel-is-free.md)'s worker, and pasted as it wrote it.*

> `.claude/skills/expedition/SKILL.md`'s `## What is in front of the human, and when` states the ceiling and never
> says when a question stops being live, and places no duty on the manager to serve a free channel. Both are now
> settled and the shipped file carries neither.

**Blockers, in the worker's words:** *"none. Node 100's work has landed, and the sentences this node adds sit beside
it rather than over it. It is not blocked by the batching node: clause 3 below is what makes the text survive a
changed ceiling."*

## Acceptance condition

*Written by node 108's worker. Pasted as it wrote it, and not the manager's.*

> 1. `.claude/skills/expedition/SKILL.md` states that a question occupies the human's channel only while it awaits
>    their answer, so the channel is free from the moment the manager records their reply. It states three
>    consequences by name: a gate answered with a correction leaves the channel free for the whole of the correction
>    round and any re-check that follows; anything the manager sends that awaits no answer — a report of a pick, a
>    notice that an agent died, the closing report — leaves the channel free the instant it is sent; and a node
>    sitting at its gate, a worker running, or a check in flight does not occupy the channel at all.
> 2. It states the manager's duty in both halves: at most one question is in front of the human at a time, and
>    whenever none is in front of them and a written question is waiting, the manager offers it **at once, in the
>    same act** rather than at its next message. It states that an idle channel with a written question waiting is a
>    defect.
> 3. It states that the ceiling in clause 2 is a number the effort may set and that the duty is to top up to it —
>    whenever fewer than that number are in front of the human and something is waiting, the manager offers at once.
>    The text reads correctly if the number is not one.
> 4. It states that the manager writes no forecast of when it will serve the queue: the line ending a report says
>    what is expected of the human at the moment it is written and promises nothing about later, and *"nothing is
>    expected of you"* is truthful only when nothing is waiting.
> 5. It states that the manager offers a question already waiting and never manufactures one to fill the channel.
> 6. These are unchanged in meaning: that nothing displaces a live question; the two tiers, and tier 1's three fixed
>    members; and the sentence beginning *"Three things are not claimants at all"* together with the three things it
>    names, which this work neither extends nor renumbers.
> 7. No section of `.claude/skills/expedition/SKILL.md` is removed, and no rule in it other than what clauses 1–5 add
>    changes its meaning.
> 8. No other file under `.claude/skills/` changes, and no file under `.scratch/` changes.
> 9. The working tree meets the bar.

**One tension the worker should know about rather than discover**, in node 108's worker's words: *"clauses 1 and 6
stand slightly apart on purpose. Clause 1 requires the file to say a pick report leaves the channel free; clause 6
forbids touching the sentence that lists three non-claimants. Both are deliberate — whether that list should name a
pick report is an outstanding flag belonging to the human, and this node is not the place it is settled."*

## The manager's note at filing

*Not a change to anything above.*

**This condition carries no enumerator and states no bounding set**, which [node
94](94-condition-scope-as-a-predicate.md)'s rung 3 permits — the work adds text to one named section rather than
repairing instances of a defect spread across the tree — but the condition does not say so in as many words. The
manager has **not** amended it: supplying a rung is within the manager's permission at node 82's guard 1, and doing
it here would be supplying a rung to a condition that needs none. Named so a checker does not read the absence as the
defect node 94 is about.

## Amendment, 2026-09-25 (from node 298)

*Written by [node 298](298-rewrite-the-manager-contract-part-3.md)'s worker and filed by the manager, after that node's work landed as commit `9d8044c`. Every word of the replacement is fixed by that commit: it quotes `expedition/SKILL.md`'s after-text. The minting author's condition above is left as it was. Node 298's worker's search is on node 298 under `RE-POINTING SEARCH`.*

- **Clause 6.** Replace "the sentence beginning *"Three things are not claimants at all"* together with the three things it names" with "the sentence *"Three things never enter the queue:"* together with the three things it lists".

*The manager's note:* the worker also reported that the manager's note under this condition ("the sentence that lists three non-claimants") needs the same wording change. That is the manager's text, not a clause.

## Flags

`118.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from node 298's re-pointing list, on the ground that every word of the replacement is fixed by commit `9d8044c`.

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 336](336-carry-the-rules-on-what-reaches-the-human-the-code.md), the merge [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole.
