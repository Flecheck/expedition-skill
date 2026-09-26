# What a standards path may hold, given the checker's blindness to the record

Type: implementation
Status: superseded
Superseded by: 334

Blocked by: 143, 151

## Question

*Surfaced by [The rules a checker and an implementer work to arrive by the spawn, never by a
search](143-rules-arrive-by-the-spawn-never-by-a-search.md)'s worker, and pasted as it wrote it.*

> The checker's contract now lets a standard reach it as a path it reads. On this effort the standards live partly
> inside the map — `map.md`'s standing preferences, ground rules and four standing rules, and
> `map-implementation-rules.md`'s review route — and those files also hold the landing policy, the links to every
> node, and the reasoning behind the work: exactly the record the checker is kept blind to, and which its contract
> tells it in as many words that it does not read and does not go looking for. The contract already states what may
> be copied to a checker **as a ground rule** and what may not, on the ground that a rule holding everywhere tells it
> nothing about this work in particular. It states nothing of the kind for the standards route, which this node
> opened. So a manager naming the map as a standards path hands the checker the record through a door the contract
> itself holds open.

**Blockers, in the worker's words:** *"this node (143), and node 151, which edits the same file and the same
region."*

## Acceptance condition

*Written by node 143's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.claude/skills/expedition-checker/SKILL.md`. The worker may edit that file and no other, and may not
> write any file under `.scratch/`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. Where the file describes the standards reaching the checker as a path it reads, it states what such a path may
>    hold: the standards themselves, and not the record behind the work — the reasoning that led to it, the effort it
>    belongs to, or the rest of the work around it.
> 2. The file states what the checker does where a path it was given as a standard holds record material alongside
>    the standards: it reads the standards in that file and reads nothing else in it, and it says in its outcome that
>    it did so.
> 3. Both statements sit under the heading that describes the standards the checker holds the work against, beside
>    the two routes by which they reach it, rather than in a section of their own.
> 4. The file's existing statement of what may be copied to the checker as a ground rule and what may not is
>    unchanged in what it requires.
> 5. The file's statement that the checker does not read the record and does not go looking for it is unchanged in
>    what it requires.
> 6. The file names no plugin and requires no skill to be invocable.
> 7. Nothing added assumes a particular repository, machine, or toolchain.
> 8. No file outside the one named above is modified.
> 9. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This node was named to the human as already filed before its file existed.** The manager reported *"Its worker also
surfaced a node I've filed as 164"* in a session report and did not write the file until the session's close, when it
checked. The report was wrong when it was made.

**Its subject is adjacent to [node 163](163-a-condition-demands-facts-the-checker-does-not-read.md) and the two do
not overlap.** Node 163 asks whether a checker may read the changed graph files **as the work under check**; this
node asks what a file handed to it **as a standard** may contain. One is about the diff, the other about the givens.
Node 163's worker independently found that the blindfold is against *"a second statement of intent, not a
directory"*, which is the distinction both nodes turn on.

## Amendment, 2026-09-25 (from node 295)

*Written by [node 295](295-rewrite-the-checker-contract.md)'s worker and filed by the manager, after that node's work landed as commit `76e66e3`. Every word of the replacement is fixed by that commit: it quotes `expedition-checker/SKILL.md`'s after-text. The minting author's condition above is left as it was. Node 295's worker's search is on node 295 under `RE-POINTING SEARCH:`.*

- **Clause 4.** Replace "The file's existing statement of what may be copied to the checker as a ground rule and what may not" with "The file's statement beginning "A ground rule is a standing constraint on the effort that is true of any node's work"".

*The manager's note:* node 295's worker also reported that clause 3's "the two routes by which they reach it" was already stale before that rewrite, since the file has had one route since the standards moved into a file. It did not repair it, and no replacement is fixed by the landed text, so nothing is filed for clause 3.

## Flags

`164.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from node 295's re-pointing list, on the ground that every word of the replacement is fixed by commit `76e66e3`.

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 334](334-land-the-open-repairs-to-the-checker-contract-in-one-change.md), the merge [node 329](329-group-the-open-nodes-against-the-worker-contracts.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole.
