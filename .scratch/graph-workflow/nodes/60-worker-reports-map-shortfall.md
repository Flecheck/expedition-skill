# A worker reports what the map did not tell it

Type: implementation
Status: superseded
Superseded by: 333

## Question

Carry out part 3 of [What the token findings change in the workflow and its
skills](53-what-token-findings-change.md)'s answer: the five worker contracts gain a **non-blocking** handover
part on which a worker reports what it needed about the effort and `map.md` did not supply, so the manager can
promote that material back into the live section.

**This is the part the human's own question produced.** Node 53's worker had recommended a partition and the
human asked whether workers could instead ask the manager; testing that found the pause too expensive, but it
exposed the real weakness — *"a partition has to be **right**, and a bad one strands material a worker needed,
silently, with no correction mechanism."* This closes that: **the partition does not have to be right on day
one, because it becomes right by measured demand.**

**Modelled on a shipped pattern rather than invented.** `expedition-checker/SKILL.md`'s `QUESTIONS:` part is
already exactly this — *"You do not wait for an answer, and your outcome never depends on one"* — the one
existing worker-to-manager channel that is not a relay to the human. Verified: `QUESTIONS` appears **once** in
the checker contract and **zero** times in the five worker contracts.

Reported by node 53's worker, which wrote the acceptance condition below.

**Blockers: none**, but it edits the same five files as nodes 32, 48, 49, 50 and 58, and the exclusive code slot
means it cannot run concurrently with any of them — flag `47.2` already priced that contention. Reported as its
own node rather than folded into [Restructure `map.md` to what every worker
needs](59-restructure-the-map.md) because **the file sets are disjoint**; the ordering is not safety-critical,
since after node 59 lands a worker can still follow the map's pointer to the material.

## Acceptance condition

The work is these five files: `.claude/skills/expedition-research/SKILL.md`,
`.../expedition-grilling/SKILL.md`, `.../expedition-prototype/SKILL.md`, `.../expedition-precondition/SKILL.md`,
`.../expedition-implementation/SKILL.md`.

Done means every one of the following is true of the finished tree.

1. Each of the five gains one new part on the worker's handover, labelled `MISSING FROM MAP:`, listed among the
   parts that file already names and **counted in whatever statement that file makes about how many parts a
   handover has**.
2. Each file says in its own voice what goes there: anything about the effort the worker needed that `map.md`
   did not tell it, and where it got that instead or how it went on without it.
3. Each file says that this part **never blocks** — the worker does not wait for an answer, and nothing in its
   handover depends on one.
4. Each file says that `none` is written there when the worker has nothing for it, consistent with how that file
   already treats a part it has nothing for.
5. Where a file already describes a route for something a worker cannot go on without, it says that this part is
   **not** that route.
6. `MISSING FROM MAP` appears in those five files and in **no other file** under
   `.claude/`.
7. No hard rule in any of the five files is reworded, nothing else in them changes, and no file outside them
   changes.

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 333](333-land-the-open-repairs-to-the-five-worker-contracts-in-one-change.md), the merge [node 329](329-group-the-open-nodes-against-the-worker-contracts.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole.
