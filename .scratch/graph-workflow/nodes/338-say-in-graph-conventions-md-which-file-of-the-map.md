# Say in graph-conventions.md which file of the map holds what, and where the never-delete rule reaches

Type: implementation
Status: open
Supersedes: 146, 153, 195, 201, 206, 228, 233, 308, 148, 43
Blocked by: none

## Question

Nodes 146, 153, 195, 201, 206, 228, 233 and 308 each correct a few lines of `graph-conventions.md` about which file of a split map holds what, and about where the never-delete rule applies. Make all their changes in one piece of work.

*Proposed by [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker and filed by the manager, on the human's "ok" to node 330's merge and its conflicts' recommendations. The worker wrote each condition to the recommended option of every conflict.* *The manager's note:* on the manager's proposal, which the human took, node 329's remainder R1 (the `graph-conventions.md` sentences of nodes 148 and 43, written by node 329's worker) is folded in as clauses 17a and 17b, and clause 20's "1 to 17" is widened to "1 to 17b".

*The worker's blockers:* none

## Acceptance condition

*Written by node 330's worker, with clauses 17a and 17b from node 329's worker.*

> The work is `.claude/skills/expedition/graph-conventions.md`, and no other file changes. No file under `.scratch/` changes. The worker does not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`. The file is one the workflow ships, so it is edited plainly: superseded wording is removed, and nothing is struck through or moved to a history file. The places named below are the work itself, so this scope came from no search.
>
> Done means every one of the following is true of the finished file. Each clause names, in brackets, the node its demand comes from.
>
> **Which file of the map holds what**
>
> 1. (153, 228) Under `## The seven files`, the description of `map.md`'s `## Notes` no longer states that `map.md`'s `## Notes` holds the declared label vocabulary or the bar's commands. Before this work it says "The manager also maintains two things here: the declared label vocabulary, and the bar's commands once they have been discovered for this repo." Wherever the file says which file holds either, it names `map-manager-only.md` for the declared label vocabulary and `map-implementation-rules.md` for the bar's commands. The rest of that description of `## Notes` keeps its meaning, except as clause 2 states.
> 2. (228) No statement in the file requires the effort's ground rules, or its declaration of which sources are authoritative, which are evidence only, and which hold statements known to be false, to sit in `map.md`'s `## Notes` specifically. Each such statement either names the map as a whole, or says plainly that the item lives in `map.md`'s `## Notes` unless the effort holds it in a sibling file of the map.
> 3. (146) Every rule in the file written against "the map's `## Notes`" states which file's `## Notes` it governs. In particular, the 500-byte target for an item under `## Writing the map` and the numbered check under `## Mechanical checks` that reports an item over that target each name the file they apply to.
> 4. (206, 228) No sentence in `## Labels` states or implies that the labels a node may use are declared in `map.md`'s `## Notes` or in any section of `map.md`. Before this work its first bullet reads "A node uses only labels declared in the map's `## Notes`." The section names `map-manager-only.md` as where a declared label vocabulary lives. The rule that a node may use only a declared label stays in force and is not weakened.
> 5. (206) `## Labels`'s other statements are unchanged: "A label names the family or part a node belongs to, for example `CLASS` rather than `CLASS-1`. Labels are optional, and a node may carry several.", "A label is only a filter. Order comes from `Blocked by:` edges and never from a label.", "A node's identity is its `NN` and never a label.", and "An effort that declares no vocabulary has no labels on any node."
> 6. (195) The sentence under `## Writing the map` beginning "Every note, standing preference and fog item" names, for each kind of item it lists, the file of the map that holds that kind, and where two kinds live in different files it says so. Before this work that sentence places all three kinds in `map.md`, while the file's own `## The seven files` places the fog, `## Not yet specified`, in `map-manager-only.md`.
> 7. (195) The opening sentence of `### Change the map`, which before this work reads "Use this when a note, standing preference or fog item in `map.md` no longer says what holds.", names the file that holds each kind of item being changed. Where that depends on the kind, it says so.
> 8. (308) Two statements no longer disagree about how often `map.md` is read: the fenced block under `## The seven files`, which before this work describes `map.md` as "Read once per session.", and the sentence under `## Writing the map` "Every worker reads all of `map.md` once per node, so its size is a cost paid once per node." Which of them changes is the worker's choice.
>
> **Where the never-delete rule reaches**
>
> 9. (233) The file states this test in these words: *"text is rule-stating if an agent could act differently because of it today; it is record-stating if it only tells you what was already decided or done."*
> 10. (233) The file states that what a text is settles that a superseded version of it must never be left readable as though it still binds, and that where the superseded text goes is a second and separate question.
> 11. (233) The file states that where superseded text goes is settled by whether the file holding it already archives its own subject. A node file does, holding every superseded thing about its one node, so its superseded text stays in it. `map.md`, and every sibling of it that states rules that currently bind, does not, so its superseded text is appended verbatim to `map-history.md`.
> 12. (233) The file states four things about an implementation node's acceptance condition:
>     - it is rule-stating while its node is live;
>     - a superseded clause of one stays in the node file and is never appended to `map-history.md`;
>     - such a clause is marked superseded where the clause itself stands, rather than only recorded elsewhere in the node file;
>     - the reason is that the checker is handed the condition as text and does not read the node.
> 13. (233) Before this work, two statements disagree. The paragraph after the one opening "No edit deletes." says "Inside the graph's files, what happens to superseded text depends on the text's job, whichever file holds it." `## Writing the map` says "The graph's other files record what happened: `decisions.md`, `flags.md`, the node files, and `map-history.md`, which holds superseded text only. Superseded text in those files stays where it is." The second sorts by file what the first says is sorted by text. After this work the file does not both say the cut follows the text and sort the node files onto the record side because they are node files.
> 14. (233) The file still describes `map-history.md` as holding superseded text only and as never being rewritten.
> 15. (201) The paragraph stating that no edit to a graph file deletes also states, in its own text, that the rule does not reach removal performed by an act that is invoked and whose declared purpose is removal. It gives the reason as a property: the rule guards against deletion that is unannounced, and being invoked for that purpose is the announcement.
> 16. (201) That statement says what such an act leaves behind in place of what it removed: an entry naming what was removed and recording that the text remains recoverable from the effort's version control history. It states this as a property and names no command and no tool.
> 17. (201) The numbered check under `## Mechanical checks` requiring that every flag entry on a node has a matching line in `flags.md` states two things: a settled flag whose index line has been removed is not a mismatch, and an outstanding flag missing its index line still is one.
> 17a. *(node 148, by way of node 329's remainder R1.1)* *(node 148)* The sentence beginning "A path may say where:" states that such a path is written relative to the repository root, and states the reason: an absolute path names a machine, and the worker and the checker that read the condition may not be on it. The addition is at most two sentences. `grep -rn -oE '/(home|Users)/[A-Za-z0-9_.-]+/' .claude/skills/` returns nothing after the work.
> 17b. *(node 43, by way of node 329's remainder R1.2)* *(node 43)* The sentence "Such a demand goes in the handover's `INVALIDATIONS` part, which names which resolved node the work contradicts and how." is reworded so the part covers any resolved node whose answer the work changes what it says. It names a rename, an extension, a narrowing and a contradiction. "A demand about the record as a whole belongs on the handover and in no condition, whatever its wording." is unchanged.
>
> **What does not change**
>
> 18. (233, 195) The numbered steps of `### Change the map` are unchanged in content, count and order.
> 19. (201, 233, 146) The numbered list under `## Mechanical checks` keeps its existing items, in their order and with their numbers. The only checks whose text changes are the one clause 17 names and the one clause 3 names. The work may add at most one new item, after the existing ones, stating that a superseded clause of an acceptance condition is marked where it stands.
> 20. (201, 195, 206) No procedure under `## Procedures` is reworded except as clause 7 states, and no section changes other than those clauses 1 to 17b name.
> 21. (228, 201, 233) The file names no file of an effort's directory other than the seven listed under `## The seven files`. Every markdown link in the file outside a fenced code block resolves to a path that exists, and the work adds no link to a path that does not exist.
> 22. (206) The file names no plugin, requires no skill to be invocable, and assumes no particular repository, machine or toolchain.
> 23. The working tree meets the bar.
