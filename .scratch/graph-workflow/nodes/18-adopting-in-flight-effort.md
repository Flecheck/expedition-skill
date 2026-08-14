# Adopting an in-flight effort

Type: grilling
Status: open
Blocked by: 13

## Question

How does an effort that is already in progress get onto the workflow?

Surfaced by [Dogfood target](09-dogfood-target.md), which made this a hard precondition rather than a nice-to-have: the first real run is a **migration** of Lang's `.scratch/spec-completion/` effort, not a fresh charting session. Nothing in the graph so far assumes anything exists before the manager arrives.

What arrives with an in-flight effort, using Lang as the concrete case:

- **Decisions already made.** `decisions.md` is 2028 lines, numbered to `D47`, each with the author's reasoning. Do these become resolved nodes, one per decision? Entries in the map's Decisions-so-far pointing at the original document? Or does the original stay authoritative and get linked rather than converted? A resolved node is supposed to hold its own answer, so pointing at a shared file breaks the "a decision lives in exactly one place" rule — but converting 47 decisions into 47 files is a large mechanical act that could lose the reasoning's continuity.
- **Questions already labelled, in families.** ~130 gaps as `CLASS-1`, `LIN-3`, `EFF-1`, `X-14`, `PRIN-*`, `REPR-*`, `REFL-*`, `TOOL-*`. The graph numbers nodes `NN` sequentially. Does the existing label survive as the node's identity, as an alias, or not at all? The labels are load-bearing: they are cited by the hundred inside `inventory.md`'s own blocks-lists, and in `decisions.md`.
- **Edges already written, in prose.** Each foundational gap lists what it blocks (`"Blocks CLASS-2,4,7,9,10, X-1,2,9,15,16,17,18"`). These are the reverse direction of `Blocked by:` and have to be inverted on import.
- **Answers that landed outside the effort's own bookkeeping.** `inventory.md` audited `docs/` at 538 lines; `docs/` has since been restructured into `docs/spec/` and `docs/superseded/`, and decisions reached `D47`. So **some gaps are already resolved and the inventory does not know it.** The import must reconcile, not transcribe. Is that reconciliation an AFK job the migration does by reading, or does every candidate need the human to confirm it is really answered?
- **A hand-written resuming point.** `handoff.md` (193 lines) holds where the work stands, the live question, and a recommended order. This is a human's manual solution to the map's *Resume and recovery* problem, and it is evidence about what a manager would need to reconstruct itself.
- **Effort-local ground rules.** *"Docs win over code"*, *"no invented semantics"*, *"facts are the agent's job; decisions are the author's"*, and a warning that one source file (`Garbage Collection_ Reality vs. Perception.md`) is *"not normative unless it is the author's own words"*. These must reach every subagent — see [Subagent context contract](12-subagent-context-contract.md).
- **A tracker doc that already defines the conventions, slightly differently.** `docs/agents/issue-tracker.md` has four node types (no `implementation`), two statuses (`claimed`/`resolved`, no `open`/`superseded`), and no supersession. Does adoption rewrite the target repo's tracker doc, or must the workflow be compatible with what is there?

Also open, and more general than Lang:

- Is adoption a **node type**, a one-off `task`, or a distinct mode of the workflow alongside charting?
- Does an adopted effort's map get written from scratch by the migration, or derived mechanically?
- What is deliberately *not* imported? Lang's `consistency.md`, `terminology.md`, `answers-from-transcript.md` and `transcript-findings.md` are research outputs rather than questions or decisions, and may belong as linked assets rather than nodes.

~~Blocked on [Graph file format](13-graph-file-format.md): what a node file must contain decides what an import has to produce, and whether a foreign label can live alongside `NN`.~~ **Now unblocked**, and the import's target is fully specified. What that node settled, so this one need not:

- **Identity is `NN`, sequential, and the foreign label goes in the free-form name** — `issues/24-class-2-implicit-boxing.md`. No `Alias:` field. This answers the second bullet above and it answers it in the cheapest possible way: the filename becomes the label→id lookup, so the hundreds of `Blocks CLASS-2,4,7,9,10` citations inside Lang's own prose stay resolvable by a directory glob with nothing maintained.
- **`Labels:` exists**, so Lang's 13 gap families become a declared vocabulary in the map's Notes, and the `X-*` gaps' `REF × BOX` prose column becomes two real labels each. The import must produce them; it is the one field of the format that Lang's corpus can fill better than a fresh effort ever could.
- **43 decisions, not 47** — counted. They become one capped line each in `decisions.md`, pointing at a node per decision. So the first bullet above has a shape to argue against rather than three open options: the question left is whether the node holds the reasoning or links `decisions.md`'s original entry.
- **The tracker-doc question is answered:** the format is a structural superset of `Lang/docs/agents/issue-tracker.md`, so **adoption appends a section to it rather than rewriting it**, and every ticket already written under that doc stays valid. Two divergences to spell out: frontier ordering, and resolve appending to `decisions.md` instead of the map body.
- **The scale is bigger than this node says: 179 distinct labels across 188 inventory rows**, plus 48 consistency rows that may or may not be nodes. The "~130" figure came from an estimate; every judgement here about whether a bulk transformation is worth scripting should use the real number.

Added by [Git and code-landing policy](11-git-and-code-landing.md), which settles two inputs and hands over one limitation:

- **Adoption changes nothing about the target's git.** No branch is created, nothing is pushed, history is never rewritten, and the graph's own files stay the human's periodic commit — which is already how Lang is worked, so adoption asks the human to change no habit. What starts on adoption day is only this: from the first implementation node onward, its code lands as one path-limited commit naming the node.
- **The join key is not retro-fitted.** Lang's existing commits do not name nodes — the closest thing is `849ed64 spec: … (D31-D47)`, invented by hand — so an adopted effort begins with no landed-code lineage for anything already in the tree. Whether the migration should *try* to attribute existing code to imported gaps, or simply accept a history that starts empty, is this node's call. Accepting it is the cheap answer and probably the right one: 43 decisions across 56 commits would be guesswork, and a wrong attribution is worse than none.

Still this node's own business, and untouched by the format: whether adoption is a type, a `task` or a mode; whether the map is written or derived; what is deliberately not imported; and the reconciliation problem — gaps already answered by decisions the inventory never learned about.

## Annotation

Added by [Naming](14-naming.md).

- **The clash to reconcile is Lang's `gap` and `ticket` against `node`**, not against `issue`. Both are now in the glossary's refused list, which makes the conflict mechanical rather than stylistic: a worker reading [`CONTEXT.md`](../../../CONTEXT.md) is told `gap` is not the word, while Lang's own corpus says it 179 times. That sharpens this node's question and hands it a concrete third option — keep the foreign label in the node's free-form name, which the format already does, and refuse the foreign *word* only in newly written prose.
- **An adopted effort's join key is unique from its first commit.** The commit trailer is `Node: <effort>/<NN>`, carrying the effort name, so a second effort in Lang years later cannot collide with this one. That also lowers the cost of this node's likely call to accept an empty landed-code history: nothing about the emptiness propagates forward.
