# Write the glossary's starting-an-effort entries

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [node 112](112-what-the-glossary-calls-starting-an-effort.md)'s worker, and pasted as it wrote it.*

> Add the two term entries this node settled to the glossary — `Starting an effort` and `Adoption` — in a section of
> their own, with the `_Avoid_` lines that refuse `charting` and `migration`. This is the write for node 112's
> answer, and it is separate from [node 111](111-write-the-starting-an-effort-section.md), whose scope is `SKILL.md`
> and `graph-conventions.md` and explicitly excludes this file.

**Blockers, in the worker's words:** *"none. Node 112 is its only input. It does **not** block on [node
56](56-ship-the-glossary-into-the-skill-set.md), which moves the glossary — the condition below names the file by a
rule that resolves whichever of the two has happened."*

## Acceptance condition

*Written by node 112's worker. Pasted as it wrote it, and not the manager's.*

> **No wording is demanded anywhere below. Each item is judged as a property of what the text says.**
>
> **Which file.** Exactly one file changes: the glossary — the file holding the workflow's term entries, each written as a bold headword followed by a colon on its own line, then a definition, then in most cases a line beginning `_Avoid_:`. It is `CONTEXT.md` at the repository root, unless a file at `.claude/skills/expedition/CONTEXT.md` holds those entries when this work is claimed, in which case it is that file instead. No other file changes, and no file under `.scratch/` changes.
>
> **How this scope was got.** The enumerator, run while this condition was written: `grep -rn -i "chart" .claude/skills/ CONTEXT.md` returns exactly one line, the glossary's own `Expedition` entry; `grep -rn -i "adopt" .claude/skills/ CONTEXT.md` returns exactly one line, `graph-conventions.md:147`, which uses *"adopted"* in passing about a node's filename and states no act. So this work adds text to one file rather than repairing instances spread across the tree. Two baselines, to be re-run and reported: `grep -c '^\*\*.*\*\*:$'` on the glossary returns **51** and `grep -c '^_Avoid_'` returns **41**; after this work they return **53** and **43**. A place this work touches that is not the one glossary file is **reported and not edited**; reporting it is the whole of what this condition asks for it.
>
> 1. The file gains one new section headed `## Starting an effort`, positioned immediately before its existing section headed `## Closing an effort`. No other section moves, and no existing entry's text changes.
>
> 2. That section holds exactly two term entries and nothing else, each written in the same shape as the entries already in the file.
>
> 3. The first entry's headword is `Starting an effort`. Its definition states all of: that it is the act that creates an effort; that the manager performs it and that it happens before the graph exists; that it produces the effort's files and its first nodes; and that it has two inputs — a conversation with the human, or a directory of work that already exists — which are the only thing the two ways of starting differ in.
>
> 4. That entry's `_Avoid_` line refuses `charting`, `kickoff`, `onboarding`, `bootstrap`, `setup` and `init`. Against `charting` it gives a reason, stating both halves: that this workflow's cartographic metaphor stops at the map and every act beneath it is described plainly, and that the file's existing `Expedition` entry uses the word for what the workflow's ancestor does rather than for anything this workflow performs.
>
> 5. The second entry's headword is `Adoption`. Its definition states all of: that it is starting an effort from a directory of work that already exists; that it is a mode of starting an effort rather than a kind of node; and that it carries steps the other input does not, naming at least these five — taking the effort's name from the directory that already exists, resolving any reserved graph name the directory is already using for something else, deriving the map from the record the effort already wrote rather than from a conversation, declaring the label vocabulary from the foreign label families, and minting the bulk import as `precondition` nodes.
>
> 6. That entry's `_Avoid_` line refuses `migration`, `import`, `onboarding` and `port`. Against `migration` it gives the reason that the word names moving data rather than taking on an effort; against `import`, that importing is one step inside adoption rather than the act itself.
>
> 7. **No entry anywhere in the file gives a name to the way of starting whose input is a conversation.** That way is referred to by its input and never by a word of its own, in this section and everywhere else in the file.
>
> 8. The file's existing `Expedition` entry is left byte-identical to what it was before this work.
>
> 9. The word `charting` appears in the file in exactly one place — the `_Avoid_` line of item 4 — and in no other. The verb *charts* appears only in the `Expedition` entry item 8 preserves.
>
> 10. The work leaves the tree meeting the bar.

## The manager's note at filing

*Not a change to anything above.*

**Three open nodes now edit the glossary** — this one, [node 242](242-the-glossary-says-an-implementation-node-ends-at-the-gate.md) and [node 56](56-ship-the-glossary-into-the-skill-set.md), which moves it. **Two workers must not hold that file at once.** The manager holds the sequencing and has written no blocking edge, none of the three needing what another produces. Node 112's worker measured the wider contention at **34** non-resolved nodes mentioning the glossary, nine of them titled about it — that measurement and the correction of its own earlier estimate are flag `112.3`.

**What node 111 needs, reported by node 112's worker and not done by anyone.** Node 111 is open and unclaimed, and item 2 of its acceptance condition demands its new section *"names both: **charting** … and **adoption**"* — a word node 112's answer refuses. That amendment is **not** this node's work and is not in the condition above. Whether it is anyone's to make is the same open question [node 245](245-node-156s-condition-re-derives-a-weaker-property.md) carries, now with two instances.

## Amendment, 2026-09-24

*Written by [node 299](299-rewrite-graph-conventions-part-1.md)'s worker and filed by the manager, after that node's work landed as commit `0d406b7`. Every word of the replacement is fixed by that commit: it quotes `graph-conventions.md`'s after-text. The minting author's condition above is left as it was. The replacement takes the place of the clause it names. Node 299's worker searched every open node's `## Acceptance condition` for quoted spans of its before-range, matched literally and normalised with each condition joined into one string, and for each phrase its rewrite removed or replaced. The full list of handles is on node 299 under `### Re-pointing duty` and correction rounds 1 to 3.*

- **Scope paragraph.** Replace "`graph-conventions.md:147`" with "`graph-conventions.md`, under `## Adding a node`". Citing by heading keeps the citation valid through node 300's rewrite, under standing writing rule 4.

## Flags

`247.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 299](299-rewrite-graph-conventions-part-1.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `0d406b7`.
