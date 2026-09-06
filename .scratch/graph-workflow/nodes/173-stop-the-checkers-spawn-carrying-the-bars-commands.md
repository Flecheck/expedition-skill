# Stop the checker's spawn carrying the bar's commands, and narrow what it claims to share with the implementer

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [The checker's bar-commands route](167-the-checkers-bar-commands-route.md)'s worker, and pasted as it wrote it.*

> The checker's given 2 still offers its bar commands as something the spawn may carry,
> which is the one route that can drift from the repo's own statement of them and which contradicts
> the *nothing is fed* rule the human set at node 143's gate. And the contract claims the checker and
> the implementer *"hold the work to one set of rules rather than two"* on the strength of reading one
> file, which is true of the standards and false of the bar's commands. Remove the feed route, and
> narrow the claim.

**Blockers, in the worker's words:** *"none. Nodes 151 and 164 edit the same file; neither quotes nor protects the
sentences this changes, so any order works. Running after node 151 is the tidier order, that node repairing the
bar-and-standards relationship in the same file."*

## Acceptance condition

*Written by node 167's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.claude/skills/expedition-checker/SKILL.md`, relative to the repository root. The
> worker may edit that file and no other, and may not write any file under `.scratch/`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. The file nowhere states or implies that the checker's spawn may carry the bar's commands. In
>    particular, the item in the list of what the checker is given that begins `**The bar**` no
>    longer offers a choice between being given commands and being given the properties alone, and
>    the file no longer holds any sentence conditioned on the checker having been given properties
>    and no commands.
> 2. That same item states the bar's properties in full — the work builds, it warns about nothing,
>    it is formatted, the tests relevant to it pass, and whatever else the repo itself demands is
>    satisfied — and states that the checker discovers the commands from the repo itself.
> 3. Beside that, the item says that a repo stating its own commands to an agent typically states
>    them in its own agent-instruction file. That file is named by role and position only: no
>    particular filename for it appears anywhere in the finished file.
> 4. The item keeps its statement that a repo with no build, no tests and no formatter meets the bar
>    on its remaining half, and that this is a complete bar and not a deficient one.
> 5. The sentence introducing the list of what the checker is given states a count that is
>    arithmetically correct for the items the list then holds, and splits them correctly between
>    those that reach the checker in its spawn and those it reads for itself.
> 6. The sentence that today reads `It is the same file the implementer works from, so the two of
>    you hold the work to one set of rules rather than two` is narrowed, so that what it claims the
>    two agents share is the standards held in that file and not the bar's commands. Its ground —
>    that the implementer works from the same file — is kept.
> 7. No other sentence in the file claims that the checker and the implementer take the bar's
>    commands from the same place.
> 8. No text outside the given-list item beginning `**The bar**` and the sentence quoted in clause 6
>    is deleted or reworded.
> 9. The file names no plugin, requires no skill to be invocable, and nothing added to it assumes a
>    particular repository, machine or toolchain.
> 10. No file other than the one named above is modified.
> 11. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**No blocking edge, and that is its author's judgement rather than the manager's** — recorded as [flag
`167.2`](167-the-checkers-bar-commands-route.md). Three nodes now target
`.claude/skills/expedition-checker/SKILL.md`: this one, [node 151](151-write-the-checker-contracts-how-you-check-section.md)
and [node 164](164-what-a-standards-path-may-hold.md). The manager holds that ordering.

**Its author's own retrospective says nodes 151 and 164 may be defective**, their conditions naming a spawn-feeds-the-
standards mechanism node 143's amendment abolished. That is a finding about other nodes rather than about this one,
and the manager records it here because this node's ordering sits among them.
