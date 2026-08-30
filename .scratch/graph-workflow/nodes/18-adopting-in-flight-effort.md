# Adopting an in-flight effort

Type: grilling
Status: resolved
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

## Interview

### Attempt 1 — what adoption produces on day one

**Q1, from the worker.** *"What does adopting an effort produce on day one — the whole graph, the whole graph but
only after the stale parts have been reconciled, or just the map, with Lang's own files left standing as the
queue?"* Its recommendation, in its words: *"The whole graph, as-is, on day one."* Its two alternatives were to
reconcile first and import what survives, and to import the map only, leaving Lang's `inventory.md` and
`decisions.md` authoritative and standing as the queue.

**A1, from the human**, `verbatim`: *"18 ok"*

**The option taken**, quoted from the worker, which wrote it: *"The whole graph, as-is, on day one."* Mint a node for
every one of the 188 inventory rows and for every settled decision, wire `Blocked by:` from the prose blocks-lists,
fix the dead evidence paths mechanically, and **reconcile nothing during the import**. Not a divergence.

**Three things the worker named as waiting on this answer and not asked here**, carried forward rather than settled:
who performs the import, the manager being the graph's only writer and 200+ node files not being a manager-sized
act; where the adoption procedure's text lives; and whether an imported decision's node holds its reasoning or links
Lang's original entry.

## Answer

*Written by the node's worker and pasted as it wrote it.*

**Adoption is a mode of starting an effort, not a node type — and the manager's own part of it is small.** It is the
counterpart to charting: the act that exists before there is a graph. What distinguishes it is only its input.
Charting starts from a conversation; adoption starts from a directory of work that already exists.

The human's answer, `verbatim`: *"18 ok"*, taking the option offered to them: *"The whole graph, as-is, on day one."*
So the import transcribes and reconciles nothing, and a question the foreign record has already answered is imported
as an ordinary node and resolved afterwards by ordinary graph work.

### What the manager itself does

Seven steps, all of them bounded, none of them requiring the corpus to be read:

1. **Take the effort's name from the directory that already exists.** Lang's is `spec-completion`, and the graph's
   files land in that directory rather than beside it.
2. **Resolve the reserved names first.** Five names are the graph's: `map.md`, `map-history.md`, `decisions.md`,
   `flags.md`, `nodes/`. An adopted directory may already be using one for something else, and Lang is using two —
   `decisions.md`, under a different meaning, and `README.md` doing the map's job under a different name.
3. **Write `map.md`, derived rather than invented.** Its `## Notes` already has slots for exactly what an in-flight
   effort brings: the effort's ground rules and a standing over sources by path and glob. Both are copied verbatim
   from what the effort already wrote. For Lang, `README.md`'s three rules go into the first slot as they stand, and
   the second slot is filled three ways — `docs/spec/**` authoritative, `docs/superseded/**` evidence only, and
   `Garbage Collection_ Reality vs. Perception.md` holding statements known to be false, which is `README.md`'s own
   warning restated in the block's own terms. The destination and the fog come from `handoff.md`. **This effort
   declared no source hierarchy and so has never used that block; the first adoption is where it earns its keep.**
4. **Declare the label vocabulary** — the foreign families, as families and not as labels: `CLASS`, `TYPE`, `LIN`,
   `REF`, `GEN`, `FN`, `MUT`, `REG`, `EFF`, `TAGS`, `PAT`, `SEM`, `X`.
5. **Append the expedition section to the target's tracker doc** where it has one, per `wayfinder-divergences.md`,
   which needs one line more than it now carries: that the effort was adopted, and where its nodes are.
6. **Create the remaining graph files empty.**
7. **Mint the import as the graph's first nodes, and stop.**

### The bulk import is work, and it is a worker's

The manager cannot write two hundred node files. Its context is the resource this effort has measured failing first,
and the import is the largest single mechanical act the workflow will ever perform.

So the import is done by **`precondition` nodes** — it decides nothing, probes nothing, and produces no product code
— in two passes, which is what `graph-conventions.md` already prescribes for creating several nodes at once: **pass
one mints every node file, and can be split by family and run in parallel; pass two wires `Blocked by:` from the
prose blocks-lists**, and is one node because inverting an edge needs the whole label-to-`NN` map at once.

**This rests on a rule that is not yet on disk.** [Qualify the graph-file ban in the worker
contracts](58-qualify-the-graph-file-ban.md) is at its gate and uncommitted: the ban is about *recording* rather than
about files, and a worker whose own node's work *is* a change to a graph file makes that change itself. The import is
exactly that case. Read against the contracts as they stand on disk today, no worker may write a node file and this
part of the answer has no performer. **If node 58 is rejected at its gate, this section is the part of this answer to
revisit** — and the fallback is bad enough to be worth naming: the manager doing it itself.

Node 09 reached the same shape from the other direction, listing *"task (the migration)"* as this effort's example of
that node kind before the kind was renamed.

### A foreign file on a reserved name moves; it is not deleted and it is not left in place

**The rule: its content moves verbatim into the node files that now hold it, and the reserved name is then rewritten
to its expedition meaning.** Nothing is summarised, shortened or discarded on the way.

This is the move this effort already performed on itself, and the reasoning transfers with it: `map.md`'s history
went verbatim to `map-history.md`, and `graph-conventions.md` records why that is not an exemption — *"The
never-delete rule is satisfied by the move rather than exempted from it."*

For Lang this settles the question node 18 left open — whether a decision's node holds its reasoning or links the
original — and it settles it as **holds**, because the original file's *name* is what the graph needs. Each entry
becomes a node; that entry's full text becomes that node's `## Answer`; and `decisions.md` is rewritten in place as
the capped index, one line per node, each linking the node that now holds the entry. The author is told by
`README.md` to read `decisions.md` first, and after adoption they still can: it is an index of the same material
rather than a different set of it.

**The foreign entries' own states map onto expedition statuses**, and the mapping is mechanical: a question marked
superseded by a decision becomes a `superseded` node, with **both** `Supersedes:` and `Superseded by:` written so the
pair is complete; a retired one becomes `out-of-scope`; a parked one becomes `open` carrying an `## Interview`.
**This records a supersession rather than performing one**, so it does not discharge the dogfood's item 8, which says
supersession of a node that already holds work must not be faked.

### Which foreign files become nodes, and which are linked

**A file holding questions or decisions is imported. A file holding research output is linked from the map. A file
that is genuinely either gets a node of its own rather than being decided by the import.**

For Lang: `inventory.md` and `decisions.md` import. `terminology.md` and `transcript-findings.md` are linked. Two are
ambiguous and each gets a node in the adopted graph — `consistency.md`, whose 48 rows are partly contradictions to
decide and partly evidence; and `answers-from-transcript.md`, which is mostly a reconciliation already performed by
hand **and also names four label families that appear nowhere in `inventory.md`'s own tables**, so linking it
silently drops gaps.

### Citations inside imported material are repointed by a table built once

Imported prose cites paths, and in an effort old enough to be worth adopting some of those paths have moved. **The
manager builds the lookup table before the import and the import applies it mechanically**; building it is judgement
and applying it is not.

Lang's is seven entries and it is not the pure prefix rewrite it looks like. `inventory.md` carries 261 citations
across seven filenames and **not one of them resolves today**. Five moved into `docs/superseded/` keeping their
names; two were renamed as well — `objects.md` is now `superseded/effects_objects.md` and `flow.md` is now
`superseded/control_flow.md`. Repointing them is safe only because step 3 declared `docs/superseded/**` evidence
only, which is what stops the import from turning 261 dead pointers into 261 live citations of material the effort
has quarantined.

**The same restructure was already propagated into `decisions.md`, which cites `superseded/…` paths throughout, and
never into `inventory.md`.** That asymmetry is what the reconciliation work inherits.

### Reconciliation is graph work, not an import step

The corpus is measurably stale and says so itself: `handoff.md` states the gaps *"have not been re-swept since D17"*
— thirty decisions ago — and that *"its counts substantially overstate what is open"*. Not one row in the directory
carries a `Status:` line, though `inventory.md` declares a legend for one, so every gap imports as `open`.

Under the human's answer none of that is the import's problem. **The author's own next step becomes the adopted
graph's first real node**: `handoff.md`'s recommended order opens with *"Re-sweep `inventory.md` against D17–D47"*,
and notes it needs no interview turns — so it is an AFK `precondition` node, and it is what makes the frontier mean
anything.

### Two things adoption deliberately does not do

**It does not touch the target's git.** No branch, no push, no rewrite, and **no existing commit is attributed to an
imported node**. Node 11 handed this call here and called accepting an empty lineage the cheap and probably right
answer; it is. Lang's closest thing to a join key is one hand-written subject line, `849ed64 spec: … (D31-D47)`, and
attributing 47 decisions across the history behind it would be guesswork. A wrong attribution is worse than none, and
the node trailer `Node: <effort>/<NN>` carries the effort's name, so nothing about the emptiness propagates into a
later effort in the same repository.

**It does not rewrite the foreign vocabulary.** Lang's corpus says `gap` and `ticket`, both of which `CONTEXT.md`
refuses. Imported prose moves verbatim and keeps its own words; the glossary's refusals bind **newly written** prose
only. This is the same treatment the map already gives its own superseded wording — *"Prose written before a word
changed still says the old word: that is the never-delete rule rather than drift"* — and the foreign label survives
where node 13 put it, in the free-form filename, so `CLASS-6` is findable as `nodes/NN-class-6-….md` by glob and
never as a field.

### What this answer depends on and does not supply

**Adoption is one of two entry points and the other one is unwritten.** The manager's shipped contract has no section
on starting an effort at all, and `CONTEXT.md`'s fifty entries hold no word for either — neither charting nor
adoption. So the steps above that are *not* peculiar to adoption — writing the map, declaring the labels, fixing the
destination — are stated here for want of anywhere else, and belong with charting when charting is written. [Node
91](91-charting-records-whether-an-effort-ends.md) sits next to this hole but does not fill it: it asks whether
charting records that an effort is expected to end, which presumes the section this answer needs.

Three files this answer reads against were being changed while it was written — `graph-conventions.md`,
`.claude/skills/expedition/SKILL.md` and `CONTEXT.md`, under node 58, passed and waiting at its gate. Every quotation
above is from the versions on disk, which are pre-change.

### What the worker returned as `INVALIDATIONS`

*Pasted as it wrote it. The manager files these.*

**[Graph file format](13-graph-file-format.md) undercounts the corpus it was counting, and two other nodes repeat the
number.** Its answer states *"43 decisions, not 47 — counted"*; node 18's own text repeats it as *"**43 decisions,
not 47** — counted"*, and node 09's correction annotation carries it as *"43 settled decisions (not ~47)"*.

Counted again: `decisions.md` holds **47** decision entries, `D1` through `D47` contiguous, none of them retracted —
plus **9** question entries carrying their own states, which node 13 counted as neither. The corpus is **56**
importable entries, not 43.

**The cause is diagnosable and is the failure the map already tracks.** Four of the entries — `D27` through `D30` —
are written one heading level deeper than the rest, at `###` rather than `##`. A scan anchored on `^## D` returns
exactly 43. This is a thirteenth instance of the map's *"twelve false results from hand-written scans across seven
sessions"*, and it is the first one to have reached three node files and a decision index.

What it changes: node 13's conclusions about the *format* are untouched — nothing in them turns on the count. What it
changes is every scale argument built on 43, including this node's own, all of which hold about 30% more strongly
than they were written to.

**A secondary correction to the same node, on ground rather than on conclusion.** Node 13 justifies appending to the
target's tracker doc rather than rewriting it by *"Every ticket already written under that doc stays valid unchanged,
which is the property that makes a 179-node migration thinkable at all."* Lang's tracker doc specifies an `issues/`
directory, and **that directory has never been created — zero tickets exist under it.** The property is vacuous for
this target. The conclusion stands, but on the other grounds node 13 gave rather than on that one.

## Flags

*Each entry is the worker's own prose, pasted. The manager added the id, the marker and the state.*

`18.1` **· settled** `ASSUMPTION` — **Adoption ships as its own file, `.claude/skills/expedition/adoption.md`, rather than as a
section of `graph-conventions.md` or of the manager's contract.** Decided on two grounds. There is a precedent of
exactly this shape already in the directory: `wayfinder-divergences.md` is a per-target file the manager reads only
when the target needs it, and its own closing section names this procedure as the thing it does not cover —
*"Importing an effort that is already under way … That is a separate procedure."* And on read cost: the two documents
that would otherwise carry it are read on every effort, while adoption is read only on the efforts that are
adoptions.

`18.2` **· settled** `ASSUMPTION` — **A foreign file occupying a reserved graph name has its content moved verbatim into node
files, and the name is then rewritten to its expedition meaning.** Decided by analogy with this effort's own `map.md`
→ `map-history.md` move, where the never-delete rule was satisfied by moving rather than exempted from. The concrete
consequence is large enough to be worth the human's eye: Lang's `decisions.md` stops being 2028 lines of the author's
reasoning and becomes a capped index, with all 47 decisions and 9 questions held in node files instead. Nothing is
lost, and the file `README.md` tells the author to read first still holds an entry per decision.

`18.3` **· settled** `ASSUMPTION` — **The bulk import is performed by workers on `precondition` nodes rather than by the manager.**
The manager cannot hold two hundred node files, and node 09 independently listed the migration as that node kind. It
rests on [node 58](58-qualify-the-graph-file-ban.md)'s qualified graph-file ban, which is **passed but uncommitted
and waiting at its gate**: read against the contracts as they stand on disk, no worker may write a node file and this
part of the answer has no performer at all. If node 58 is rejected, this is the part to revisit.

`18.4` **· settled** `ASSUMPTION` — **Which foreign files import as nodes and which are linked, stated as a rule rather than as a
list**: a file holding questions or decisions imports, a file holding research output is linked from the map, and an
ambiguous file gets a node of its own rather than being decided by the import. Applied to Lang it leaves two
ambiguous — `consistency.md` and `answers-from-transcript.md` — and the second matters more than it looks, because it
names four label families (`PRIN`, `REPR`, `REFL`, `TOOL`) that appear nowhere in `inventory.md`'s tables, so linking
it silently drops gaps.

`18.5` **· settled** `ASSUMPTION` — **No existing commit is attributed to an imported node, and an adopted effort begins with an
empty landed-code lineage.** [Node 11](11-git-and-code-landing.md) handed this call to this node and called accepting
it the cheap and probably right answer. Verified against the target: its one hand-written join attempt is the subject
line `849ed64 spec: … (D31-D47)`, and reconstructing the rest would be guesswork over 47 decisions.

`18.6` **· settled** `ASSUMPTION` — **Imported prose keeps its own vocabulary; the glossary's refusals bind newly written prose
only.** Lang's corpus says `gap` and `ticket`, both refused by `CONTEXT.md`. [Node 14](14-naming.md)'s annotation
offered this as the third option and the format already supports it — the foreign label lives in the free-form
filename and never in a field. It is also the treatment the map already gives its own superseded wording.
