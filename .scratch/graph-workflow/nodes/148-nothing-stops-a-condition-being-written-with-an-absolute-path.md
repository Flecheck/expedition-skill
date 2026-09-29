# Nothing stops the next acceptance condition being written with an absolute path

Type: implementation
Status: superseded
Superseded by: 333, 338

Blocked by: none

## Question

*Surfaced by [The graph's records name absolute paths on a machine that no longer
exists](147-graph-records-name-absolute-paths-on-a-machine.md)'s worker, and pasted as it wrote it.*

> This node repaired 36 absolute paths out of the graph's records, six of them inside live acceptance conditions
> that named a directory their worker and their checker could not reach. Nothing in the shipped files stops it
> recurring. The sentence that licenses a path in a condition says only that *"a **path** may say where — the work
> must touch that file, produce it, or leave it in a stated state — because the checker has the repo"*, and no
> shipped file anywhere states what form that path takes. It appears in five worker contracts and, in its own
> words, in `graph-conventions.md`. This is ground rule 1 — *nothing in the shipped files may assume this repo,
> this machine, or a toolchain* — unenforced at the one place a condition names a location: an absolute path names
> a machine, and the worker and checker that read the condition may be on a different one. Node 147's own filing
> note records this as unminted: *"Nothing recurs-proofs this."*

**Blockers, in the worker's words:** *"none as graph edges. As sequencing: nodes 142 and 146 are open on
`graph-conventions.md`, and node 143 is open on `expedition-implementation/SKILL.md`. With a code slot of one they
serialise regardless, which is the same reasoning node 147's filing note applied to its own six."*

## Acceptance condition

*Written by node 147's worker. Pasted as it wrote it, and not the manager's.*

> The work is these six files: `.claude/skills/expedition/graph-conventions.md`,
> `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-grilling/SKILL.md`,
> `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md`, and
> `.claude/skills/expedition-research/SKILL.md`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. In each of the five `.claude/skills/expedition-*/SKILL.md` files above, the bullet beginning `a **path** may
>    say where` states that such a path is written relative to the repository root, and states the reason: an
>    absolute path names a machine, and the worker and the checker that read the condition may not be on it.
> 2. In `.claude/skills/expedition/graph-conventions.md`, the sentence beginning `A **path** may say where` states
>    the same demand and the same reason, in that file's own words.
> 3. *Recorded enumerator:* `grep -rn -oE '/(home|Users)/[A-Za-z0-9_.-]+/' .claude/skills/`, which at the time this
>    condition was written returned **0** occurrences. Re-run it; the demand is that it still return nothing — so
>    the new rule is stated in words and never by exhibiting an absolute path as an example.
> 4. The addition is at most two sentences in each of the six files. This is a rule of writing, not machinery: the
>    effort prefers short, simple prose that can be changed later.
> 5. Nothing else in any of the six files changes. No other sentence is reworded, no text is deleted or shortened,
>    and no heading, bullet or clause is renumbered.
> 6. No file outside `.claude/skills/` is modified.
> 7. The working tree meets the bar. The bar for this repository is entirely its non-command half: the repository
>    has no build, no tests, no formatter and no CI — no manifest, no task runner, nothing to invoke. So the bar
>    here is the project criteria (the human's global coding principles and naming method), the effort map's
>    standing preferences, `CONTEXT.md`'s `_Avoid_` lines, and this acceptance condition.

## The manager's note at filing

*Not a change to anything above.*

**This is the node [147](147-graph-records-name-absolute-paths-on-a-machine.md)'s own filing note said was
unminted**, now minted with a condition its worker wrote rather than the manager. **The manager has written nothing
into the condition.**

**It is the recurrence guard for a defect the manager itself introduced twice on node 147** — once by writing an
absolute path into that node's condition and once by writing an enumerator that counted a string the condition
itself contained.

## Amendment, 2026-09-24

*Written by [node 290](290-rewrite-the-research-contract-as-the-pilot.md)'s worker and filed by the manager, after that node's work landed as commit `4068519`. Every word of each replacement is fixed by that commit: it quotes the research contract's after-text. The minting author's condition above is left as it was, and these replacements take the place of the clauses they name.*

Node 290's worker searched every open node's `## Acceptance condition` for quoted spans of the research contract's before-text, for mentions of the file, and for each piece of wording its rewrite removed or replaced. The full list of handles is on node 290 under `### Re-pointing duty` and `### Correction round 1`.

- **Clause 1.** It points at "the bullet beginning `a **path** may say where`". Replacement: "the bullet beginning `A path may say where, because the checker has the repo` in `.claude/skills/expedition-research/SKILL.md`, and in any of the five not yet rewritten, the bullet beginning `a **path** may say where`". Once nodes 291 to 294 land, all five start with the after-text form.

## Flags

`148.1` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 290](290-rewrite-the-research-contract-as-the-pilot.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `4068519`.

## The manager's note, 2026-09-24

*The manager's own note.* [Node 290](290-rewrite-the-research-contract-as-the-pilot.md)'s worker reported in its retrospective: "Node 148's clause 7 still counts the map's standing preferences as part of the bar, which nodes 169 and 184 struck."

## Amendment, 2026-09-24 (second)

*Written by [node 299](299-rewrite-graph-conventions-part-1.md)'s worker and filed by the manager, after that node's work landed as commit `0d406b7`. Every word of the replacement is fixed by that commit: it quotes `graph-conventions.md`'s after-text. The minting author's condition above is left as it was. The replacement takes the place of the clause it names. Node 299's worker searched every open node's `## Acceptance condition` for quoted spans of its before-range, matched literally and normalised with each condition joined into one string, and for each phrase its rewrite removed or replaced. The full list of handles is on node 299 under `### Re-pointing duty` and correction rounds 1 to 3.*

- **Clause 2.** Replace "the sentence beginning `A **path** may say where`" with "the sentence beginning `A path may say where:`". The reason "because the checker has the repo" is now cut. Node 148's own demand, adding the relative-path rule and its reason, is unaffected.

`148.2` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 299](299-rewrite-graph-conventions-part-1.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `0d406b7`.

## Amendment, 2026-09-25 (from node 294)

*Written by [node 294](294-rewrite-the-implementation-contract.md)'s worker and filed by the manager, after that node's work landed as commit `724c361`. Every word of the replacement is fixed by that commit: it quotes `expedition-implementation/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 294's worker's search is on node 294 under `RE-POINTING SEARCH`.*

- **Clause 1**, as amended by node 290. Replace it with: "the bullet beginning `A path may say where, because the checker has the repo` in `.claude/skills/expedition-research/SKILL.md` and `.claude/skills/expedition-implementation/SKILL.md`, and in any of the five not yet rewritten, the bullet beginning `a **path** may say where`".

`148.3` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 294](294-rewrite-the-implementation-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `724c361`.

## Amendment, 2026-09-25 (from node 291)

*Written by [node 291](291-rewrite-the-grilling-contract.md)'s worker and filed by the manager, after that node's work landed as commit `0a3e68b`. Every word of the replacement is fixed by that commit: it quotes `expedition-grilling/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 291's worker's search is on node 291 under `RE-POINTING SEARCH`.*

- **Clause 1**, as amended by node 294. Replace it with: "the bullet beginning `A path may say where, because the checker has the repo` in `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md` and `.claude/skills/expedition-grilling/SKILL.md`, and in any of the five not yet rewritten, the bullet beginning `a **path** may say where`".

`148.4` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 291](291-rewrite-the-grilling-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `0a3e68b`.

## Amendment, 2026-09-25 (from node 292)

*Written by [node 292](292-rewrite-the-precondition-contract.md)'s worker and filed by the manager, after that node's work landed as commit `ede2c76`. Every word of the replacement is fixed by that commit: it quotes `expedition-precondition/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 292's worker's search is on node 292 under `RE-POINTING SEARCH` and its addendum.*

- **Clause 1**, as amended by node 291. In the list of files where the bullet begins `A path may say where, because the checker has the repo`, add `.claude/skills/expedition-precondition/SKILL.md`.

`148.5` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 292](292-rewrite-the-precondition-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `ede2c76`.

## Amendment, 2026-09-25 (from node 293)

*Written by [node 293](293-rewrite-the-prototype-contract.md)'s worker and filed by the manager, after that node's work landed as commit `6d26be1`. Every word of the replacement is fixed by that commit: it quotes `expedition-prototype/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 293's worker's search is on node 293 under `RE-POINTING SEARCH`.*

- **Clause 1**, as amended by node 291. In the list of files that hold the bullet beginning `A path may say where, because the checker has the repo`, add `.claude/skills/expedition-prototype/SKILL.md`.

*The manager's note:* the worker reported that the absolute-path grep of clause 3 returns 0.

`148.6` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 293](293-rewrite-the-prototype-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `6d26be1`.

## Superseded, 2026-09-26

*The manager's note.* Its worker-contract part is replaced by [node 333](333-land-the-open-repairs-to-the-five-worker-contracts-in-one-change.md), the merge [node 329](329-group-the-open-nodes-against-the-worker-contracts.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole. Its `graph-conventions.md` sentence is held on node 329 as its remainder R1, for the manager-contract merge of [node 330](330-group-the-open-nodes-against-the-manager-contract.md) to absorb; the manager adds the replacement there when that merge is filed.

## Superseded, 2026-09-26

*The manager's note.* Its `graph-conventions.md` sentence, held on node 329 as remainder R1, is now carried by [node 338](338-say-in-graph-conventions-md-which-file-of-the-map.md) as clause 17a or 17b, on the human's "ok" to node 330's merge.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
