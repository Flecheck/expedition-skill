# The checker is given the review route instead of finding it

Type: implementation
Status: open

## Question

The checker contract tells the checker to **go and find** the standards and the reviewing skill: *"Find these before
you read the work."* Every checker therefore re-derives the same answer, and the derivation is the most expensive
part of the check.

**Measured, on two runs of the same checker.** Its own words, from [Restructure `map.md` to what every worker
needs](59-restructure-the-map.md)'s retrospective:

> Everything in my context said the standard was unreachable and I nearly reported it absent. I found it only with a
> `find /` sweep… **This was the largest single cost of the check, and the standard turned out to be the one that
> mattered most** — the work is prose, and `coding-principles` barely touched it.

On its second run, handed the same facts in its spawn, it reported: *"Almost nothing, and that is the difference the
spawn made… last round each of those cost a search."*

### The human's instruction, `verbatim`

> *"For the checker, it need to find how to review, we should put it in the map with the list of stuff to follow and
> then give it to him when we spawn it so that it doesn't have to find it"*

**The map half is already done** — the manager filed *the review route for this repo, discovered on first use* into
`map.md`'s `## Notes`, beside the bar's commands, on the same ground that note gives: recorded so no later node
re-derives it. **This node is the other half**: making the contract expect it rather than hunt.

## What has to change, and the one real difficulty

`## The standards this repo and this machine carry` instructs the checker to find the standards. If the spawn now
supplies them, that instruction is partly superseded and a checker following the contract literally does the search
anyway. **The contract has to say that the route arrives in the spawn, and what to do when it does not** — the
workflow must still run on a repo whose map records no route, where finding is the only option.

There is a second-order effect worth naming: the found-versus-given distinction is exactly what the contract's own
*"a property nobody stated is not a finding"* rule turns on. A standard the checker **was given** is stated; a
standard it **went and found** is one it decided was relevant. Handing the route over therefore narrows what a
checker may fault work for, which is a real change and not only a saving.

## What is not yet decided, and is why this has no acceptance condition yet

**Whether this is a sixth given or part of the existing fourth.** [The checker's spawn carries the effort's ground
rules](42-checker-spawn-carries-ground-rules.md) fixed the count at **five** and its answer records that the count
was verified against every file mentioning it. The bar's non-command half already travels *"as this map records
it"*, and the review route now sits beside the bar's commands in the same section — so the cheaper reading is that
it rides the fourth given and no count changes. The alternative is a sixth given with a duty attached, as node 42
gave the fifth (`Follow them.`).

The manager has **not** written a condition, under [A worker's handover carries no acceptance condition for the node
it mints](35-handover-mints-no-condition.md)'s permission, because that choice should be made before the condition
rather than inside it.

**Blockers: none**, but it edits `.claude/skills/expedition-checker/SKILL.md` and so contends for the code slot with
[The checker has no form for two clauses of one condition that cannot both hold](66-two-clauses-that-cannot-both-hold.md)
and [What a finding must carry so it can be swept](71-what-a-finding-must-carry.md), both of which edit the same
file. **Those three should probably be one node**, on the ground node 48 was bundled: one file, one check, one gate.
