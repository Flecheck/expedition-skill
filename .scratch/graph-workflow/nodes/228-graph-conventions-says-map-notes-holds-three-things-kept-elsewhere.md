# `graph-conventions.md` says `map.md`'s `## Notes` holds three things this effort's map keeps elsewhere

Type: implementation
Status: superseded
Superseded by: 338

Blocked by: none

## Question

*Surfaced by [node 198](198-two-files-describe-the-rules-file-by-contents-node-188-removes.md)'s worker, and pasted
as it wrote it.*

> Under `## The seven files`, the `map.md` gloss says `## Notes` carries *"the two things the manager maintains
> here: the **declared label vocabulary**, and the bar's commands once they have been discovered for this repo"*,
> and that the ground rules and a standing over sources are optional blocks that *"live here"*. On this effort the
> label vocabulary is in `map-manager-only.md`, the bar's commands are in `map-implementation-rules.md`, and the
> ground rules moved there too at node 144; `## Labels` further says *"A node may only use a label declared in the
> map's `## Notes`"*. Found by node 198's worker while editing the paragraph above it. Unlike node 198's two targets
> this is not simply stale text: the shipped file is generic, and an effort that never splits its map keeps all of
> it in `## Notes`, so the question is whether these clauses should say *the map* — a sibling being part of the map
> — rather than `map.md`'s `## Notes`, and that is a judgement rather than a repair, which is why node 198 did not
> make it.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 198's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.claude/skills/expedition/graph-conventions.md` and no other file may be edited. It is a shipped
> file, so it is edited plainly: superseded wording is removed and nothing is struck in place or moved to a history
> file. The worker may not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> Done means all of the following are true of the finished tree.
>
> 1. No statement in the file requires a named item — the declared label vocabulary, the bar's commands, an effort's
>    ground rules, or a standing over sources — to sit in `map.md`'s `## Notes` specifically, where an effort may
>    instead hold it in a sibling file of the map. Each such statement either names the map as a whole or says
>    plainly that the item lives in `## Notes` unless the effort has moved it to a sibling.
> 2. The rule under `## Labels` that a node may only use a declared label is preserved, and states where that
>    declaration may live in terms consistent with clause 1.
> 3. The file names no file outside the seven it lists under `## The seven files`.
> 4. Every markdown link in the file outside a fenced code block resolves to a path that exists.
> 5. No file other than `.claude/skills/expedition/graph-conventions.md` is modified.
> 6. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Its author drew a distinction the manager would not have drawn, and it is why this is a node rather than a
correction inside node 198.** Node 198's two targets were stale text in a file that had fallen behind a move. This
is not: the shipped file is **generic**, so its statement is correct for any effort that never splits its map, and
wrong only for one that has. The repair is therefore a judgement about what the shipped file should assume, not a
repointing — and its author said so and declined to make it under a condition scoped to repointing.

**Two files must not hold `graph-conventions.md` at once.** This node and [node
222](222-the-conventions-file-says-a-worker-reads-the-whole-map.md) both edit it, as did node 198. **The manager
holds that sequencing and has written no blocking edge**, neither node needing what the other produces.

## Amendment, 2026-09-24

*Written by [node 299](299-rewrite-graph-conventions-part-1.md)'s worker and filed by the manager, after that node's work landed as commit `0d406b7`. Every word of the replacement is fixed by that commit: it quotes `graph-conventions.md`'s after-text. The minting author's condition above is left as it was. The replacement takes the place of the clause it names. Node 299's worker searched every open node's `## Acceptance condition` for quoted spans of its before-range, matched literally and normalised with each condition joined into one string, and for each phrase its rewrite removed or replaced. The full list of handles is on node 299 under `### Re-pointing duty` and correction rounds 1 to 3.*

- **Clause 1.** Replace "or a standing over sources" with "or the declaration of which sources are authoritative, which are evidence only, and which hold statements known to be false". The file no longer names that item by label. The rest is unchanged.

## Flags

`228.1` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 299](299-rewrite-graph-conventions-part-1.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `0d406b7`.

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 338](338-say-in-graph-conventions-md-which-file-of-the-map.md), the merge [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
