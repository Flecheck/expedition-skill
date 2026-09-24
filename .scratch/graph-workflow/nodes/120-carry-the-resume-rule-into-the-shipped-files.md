# Carry the resume rule into the shipped files

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [Whether a dead attempt is resumed from its transcript rather than
replaced](119-dead-attempt-respawned-rather-than-resumed.md)'s worker, and pasted as it wrote it.*

> The shipped files say a dead worker is replaced. Node 119 decides it is resumed wherever the harness allows. Bring
> the shipped set into line.

**Blockers, in the worker's words:** *"node 119 resolved."* Node 119 is resolved, so this node is unblocked at
filing.

## Acceptance condition

*Written by node 119's worker. Pasted as it wrote it, and not the manager's.*

> The work edits the files below and leaves each in the state described.
>
> 1. `.claude/skills/expedition/SKILL.md`, section `## When an agent dies or is stopped`. In its own prose it must
>    say all of: that a dead attempt is resumed rather than replaced wherever the harness allows, replacement being
>    the fallback; that sending a message to an agent reports which of three states it is in, and the manager acts on
>    the answer rather than deciding in advance — a reply that the message was queued for delivery at the agent's
>    next tool round means it is alive and still working, a reply that the agent is being resumed means it had
>    stopped (whether it completed or the harness terminated it) and has been resumed from its transcript, and a
>    failure saying no transcript was found for that agent id means it is gone and must be replaced; that a failed
>    resume starts no agent and costs nothing, so possibility is tested and never predicted; that resumability is
>    scoped to the manager's own session, every attempt spawned in the current session being resumable and no attempt
>    from an earlier session being resumable at all even though its transcript still exists on disk; that a dead
>    run's state is read from its transcript's record count and byte size and never from the one-line summary the
>    harness surfaces as its result; that a dead run's cause of death is the last record of its own transcript and,
>    where that cause is a usage quota, names the time the quota resets; that where the cause is a shared usage quota
>    the manager waits for the stated reset and then resumes, a replacement being unavailable in the same window so
>    that waiting costs nothing replacing would gain; and that where a live run has already overtaken a dead one,
>    measured in transcript records, the live run finishes and the dead one is held as the fallback.
> 2. The same section must state that the rule reaches the checker: a checker is resumed to continue or revise a
>    check it is still conducting, including a re-check after a correction round, and is spawned fresh only where the
>    purpose is a second opinion on a verdict already delivered; and that a resumed re-check re-runs the bar's
>    command half rather than carrying it over, and re-establishes that no standard moved under the check.
> 3. The same section must no longer assert that an agent the human stopped cannot be resumed, and must no longer
>    instruct the manager to spawn a fresh agent with a full replayed transcript as the primary recovery. Replay
>    remains only as the fallback for the case where the resume fails.
> 4. `CONTEXT.md`: the `attempt` entry reads "A node outlives its attempts: a dead worker is replaced, and the
>    replacement is a new attempt recorded after it." It must no longer state that a dead worker is replaced, and
>    must instead state that a dead worker is resumed where the harness allows and replaced only where it does not.
>    The superseded wording is marked as superseded and left in place rather than deleted.
> 5. `.claude/skills/expedition/graph-conventions.md`, section `### ## Interview`. Its dead-attempt marking must
>    additionally require that the attempt's entry carries the dead run's transcript record count and its cause of
>    death as the harness stated it. It must also say that a resumed attempt is recorded as the same attempt
>    continuing rather than as a new attempt block, so the at-most-three-attempt-blocks limit is unaffected by any
>    resume.
> 6. Any other file under `.claude/skills/` that states or implies that a dead worker or dead checker is replaced,
>    respawned, or given a replayed transcript as the primary recovery is brought into line with items 1–5. The work
>    reports the search that found them — the terms searched and the files searched — and reports any instance found
>    outside items 1–5 rather than silently editing it or silently omitting it.
> 7. No claim of a token or cost saving appears as a measured quantity unless the number and what measured it are in
>    the work's own text.
> 8. The standing bar for this repository.

## The manager's note at filing

*Not a change to anything above.*

**Clause 6 is this condition's own enumerator rung under [node 94](94-condition-scope-as-a-predicate.md), and it is
supplied as a duty on the worker rather than as a search already run.** The manager has not re-derived it and has not
amended the condition. Whether a condition may discharge node 94's rung by delegating the search to its own worker,
instead of carrying an enumerator and its return, is a question this condition raises and no node answers.

**Clause 5 names the section `### ## Interview`, which is how the worker wrote it.** The manager did not correct it;
the file on disk wins, and a worker that cannot find that heading reports it.

## Annotation: two clauses of this condition are invalidated before the node was ever claimed

*Filed by the manager from [What can actually stop a running worker](122-what-can-stop-a-running-worker.md)'s
`INVALIDATIONS`, in that node's own words. **The condition above is not amended by this annotation**, and the manager
has not touched it: rewriting a condition is not the manager's, and a condition that is wrong goes to the human. The
node is open and holds no work, so [Revision semantics](06-revision-semantics.md)'s in-place route is available to
whoever is entitled to take it.*

> **Clause 3 instructs the worker to delete a true statement.** It says the section *"must no longer assert that an
> agent the human stopped cannot be resumed."* That assertion is **correct for every route the manager has**, and it
> is now grounded in the harness's source rather than resting on nobody's measurement: a resume of an agent carrying
> `stoppedByUser` is refused unless the request is `userInitiated`, which is set only for a message the human types.
> What the sentence needs is the missing half — that the human themselves can revive it, which clears the flag — not
> deletion.
>
> **Clause 1 mandates a three-state table that is missing the state that matters.** It requires the section to say a
> send *"reports which of three states it is in"* and enumerates alive, resumed, and gone. There is a fourth for an
> agent target, `agent-stopped-by-user`, which returns `success:false` with `Agent "<name>" was stopped by the user
> and was not resumed. Treat its work as cancelled; only start a new agent for it if the user explicitly asks.` and
> **attempts no resume at all**. A manager holding the three-row table reads that reply as neither of its three rows.

**The manager's note, and not node 122's worker's text.** Both defects are in clauses this node inherited from [node
119](119-dead-attempt-respawned-rather-than-resumed.md)'s answer, written before anything about the human's stop was
established. **Node 122's retrospective names the pattern behind them**: *"the record's claims about the harness are
all of the form 'you cannot', and they are wrong in the permissive direction every time … Node 119 corrected five of
these and introduced two more of the same kind, because it inferred a general incapacity from one refusal it did not
read the reason for."*

**What is not affected.** Clauses 2, 4, 5, 6, 7 and 8 are untouched by this, and clause 1's other demands — the
session scoping, reading a dead run's state from its transcript, the quota-reset behaviour, the overtaking clause —
all stand, node 122 having confirmed rather than contradicted them.

**One overlap the whoever-claims-this must know:** [Give the manager's contract a procedure for stopping a running
worker](124-a-procedure-for-stopping-a-running-worker.md) edits the same section of the same file and is sequenced
after this node on its own author's instruction.

## Amendment, 2026-09-24 (from node 296)

*Written by [node 296](296-rewrite-the-manager-contract-part-1.md)'s worker and filed by the manager, after that node's work landed as commit `6745f37`. Every word of the replacement is fixed by that commit or by `CONTEXT.md`. The minting author's condition above is left as it was. The replacement takes the place of the clause it names. Node 296's worker's search handles are on node 296 under its `#### Re-pointing search` and correction rounds.*

- **Clause 4.** It quotes the `CONTEXT.md` `attempt` entry as "…a new attempt recorded after it." That wording was only `SKILL.md`'s, and this work removes it. Replacement for the quoted sentence: "`CONTEXT.md`: the `attempt` entry reads "A node outlives its attempts: a dead worker is replaced, and the replacement is a new attempt."" The rest of clause 4 is unchanged.

`120.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 296](296-rewrite-the-manager-contract-part-1.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `6745f37` or by `CONTEXT.md`.
