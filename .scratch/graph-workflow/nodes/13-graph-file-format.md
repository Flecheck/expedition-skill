# Graph file format

Type: grilling
Status: resolved
Blocked by: 06, 07

## Question

What files represent the graph, with what fields, and where do they live?

Settled input: markdown files and prose rules, wayfinder-style, not a CLI ([Graph state mechanism](05-graph-state-mechanism.md)). This issue fixes the actual shape.

- Directory: reuse `.scratch/<effort>/` as this map does, or a distinct location since this workflow is not wayfinder?
- One file per node plus an index map, as wayfinder does — or a different split?
- How are edges encoded? Wayfinder's `Blocked by: NN, NN` covers blocking, but revision may need a second edge kind (supersedes, invalidated-by) depending on [Revision semantics](06-revision-semantics.md).
- What is the status vocabulary? Wayfinder has open / claimed / resolved. Revisable nodes may need more — superseded, needs-revision — and implementation nodes may need a landed-but-unverified state.
- Does the index still carry a one-line gist per closed node, and does that stay accurate when a node is later revised?
- Is node identity stable across revision? If a node is superseded, does the number get reused, and do inbound edges follow?

Settled by [Revision semantics](06-revision-semantics.md), so this node encodes rather than decides it:

- Status vocabulary gains `superseded`, and `superseded` does **not** satisfy a `Blocked by` edge — a dangling edge onto a superseded node is an error the format should make detectable.
- Two edge directions, both required: `Superseded by: NN, NN` on the old node (so a stale answer is never read as current) and `Supersedes: NN` on the replacement (so "is this a revision?" is a local read).
- Node identity is stable and numbers are never reused.
- No `Touches:` field on implementation nodes — cascade scope is agent judgement, explicitly not declared bookkeeping.
- Superseded text stays in the file, marked as superseded, rather than being deleted — so the format needs a place to put it.

Settled by [Node type taxonomy](07-node-type-taxonomy.md), so this node encodes rather than decides it:

- The type vocabulary is exactly five: `research`, `prototype`, `grilling`, `task`, `implementation`.
- Implementation nodes carry an **acceptance condition**, written by the spawning node before work starts — so it is a field the spawner fills, not one the worker fills.
- There must be somewhere to put an implementer's **flagged assumptions**, and somewhere for the **reviewer's outcome**. Neither is a status: a node under review or carrying flags is still just claimed or resolved.
- No landed-but-unverified status is needed, because verification happens inside the implementation node rather than after it.

Settled by [Relay protocol](08-relay-protocol.md), which adds a whole dimension this node did not know about — a node file is now also an **interview log**:

- A node carries **per-attempt relay blocks**: the attempt's opaque routing key, and an append-only log of each relayed question and each human answer, written at relay time. Whether the log sits inline in the node file or in a sibling file is a format call and belongs here.
- Answers carry **provenance** — the human's verbatim words versus a manager paraphrase — because a paraphrase silently becomes the permanent record.
- Attempts can be marked **dead**, and there is a **two-respawn cap** to count against.
- A parked node carries **banked progress**: answers already paid for by the human, on a node that has gone back to `open`. The format must make a half-interviewed node distinguishable from a never-started one, or a deferral becomes invisible debt.
- **Delegated flags**, where the human said "you decide" and the subagent answered.
- Still **no new status** for any of this: parked is `open`, under-review is `claimed`, and flags are not statuses. The status vocabulary stays at open / claimed / resolved / superseded.

Constrained by [Dogfood target](09-dogfood-target.md), which gives the format a first real corpus instead of a hypothetical one — and this node now **blocks** [Adopting an in-flight effort](18-adopting-in-flight-effort.md), because what a node file must contain decides what an import has to produce:

- **The format must survive a foreign identifier scheme.** Lang's ~130 gaps are labelled `CLASS-1`, `LIN-3`, `EFF-1`, `X-14`, `PRIN-*`, and those labels are cited by the hundred inside its own documents. Either a node carries an alias field alongside its `NN`, or every one of those citations breaks on import.
- **It must be importable, not just writable.** ~47 existing decisions and ~130 existing questions with prose edges have to become files. A format that is only comfortable when written one node at a time by an agent will fight the migration.
- **Scale is now a number: ~130 nodes.** That reprices two choices this node already lists. Whether relay logs sit inline or in a sibling file stops being cosmetic once nodes accumulate multi-attempt interview logs; and the index carrying a one-line gist per resolved node means a map body of well over a hundred lines, which is no longer "the whole map at low resolution, loaded once per session".
- **A target repo may already have a tracker doc.** Lang's `docs/agents/issue-tracker.md` defines four types (no `implementation`), two statuses (no `open`, no `superseded`), and no supersession. So the format either has to be a compatible superset or adoption has to rewrite the target's doc — a call this node should make rather than leave to the migration.

Added by [Done-ness and termination](10-done-ness.md) — the first requirements on this format that come from an automated **reader** rather than a writer:

- **Flags must be mechanically collectable.** The final sweep gathers every outstanding flag across the whole graph into the completion report: assumption flags, acceptance conditions an implementer marked as wrong, and delegated answers. If those live as free prose in a node body, the sweep has to re-read and re-judge ~130 node files every time it runs. A fixed marker turns that into a scan.
- **A flag needs a settled/outstanding distinction.** At report time the human settles some on the spot and postpones others into nodes. A flag with no state stays in the file forever and gets re-reported at every subsequent sweep, so the report degrades into noise exactly as the effort nears its end.
- **The map's Notes now hold machine-written content**, which is new: the standing bar's per-repo commands are discovered on first use and recorded there so later nodes do not re-derive them. The map body therefore has a region the manager maintains, alongside the regions the human writes.
- Consistent with the decision above: **still no new status.** Flags are not statuses, and settled-versus-outstanding is a property of a flag, not of a node.

Blocked on revision semantics and the taxonomy because the fields are a direct encoding of both. Fixing the format first would just be deciding those two by accident.

## Answer

**Wayfinder's local-markdown tracker, extended in four places and split into four files.** Two of the splits were forced rather than chosen: the standing never-delete rule makes every index append-only, and an append-only file cannot also be the file that has to stay small enough to load every session.

### Identity is `NN`; the name carries everything else

**DIVERGENCE from the recommendation.** I proposed making the id an arbitrary string token so Lang's `CLASS-1` could *be* the id, on the grounds that the hundreds of `Blocks CLASS-2,4,7,9,10` citations inside its own prose would otherwise dangle. The human kept `NN`: *"a sequential number is a stable format and numbers don't change so it is good for search."* A foreign label is neither guaranteed unique across families nor safe from a family being renamed; a number is both, permanently.

The objection the recommendation rested on **dissolves rather than losing**: with the label in the free-form name — `issues/24-class-2-implicit-boxing.md` — resolving `CLASS-2` to a node is a directory glob, so **the filename is the lookup table** and nobody maintains a mapping.

- **`NN` is the identity.** Sequential, allocated by the manager, stable, never reused (per [Revision semantics](06-revision-semantics.md)).
- **The name is free-form, and carries a foreign label when one exists.** For an adopted effort this is required, not cosmetic — it is the only thing that keeps the target's existing citations resolvable.
- **No `Alias:` field.** It would be a second place for a fact the filename already holds.
- Id allocation needs no locking: the manager is the graph's single writer, per [Relay protocol](08-relay-protocol.md).

### `Labels:` — the human's addition, and the most useful thing in this node

Proposed by the human unprompted: an optional multi-valued field holding the *family* a node belongs to — `CLASS`, not `CLASS-1` — *"so that it is then possible to label all nodes that are about a specific part of the problem, so that it is easier for the manager to find task, ex: the user want to work only on the first part of a feature."*

It pays for itself three times over:

- **It answers a question another node was stuck on.** [Human-initiated steering](16-human-steering.md) records that "first frontier node by number wins" is indefensible at this scale, and the only replacement it had evidence for was fan-out ranking — which orders the whole frontier but cannot express *"not that area at all"*. A label is a **subset selector**, a different axis from priority, and it is precisely the steering act that node says has no mechanism.
- **It makes Lang's cross-cutting gaps queryable.** `X-9 | REF × BOX` encodes its two areas in a prose table column that nothing can read. As `Labels: REF, CLASS` it surfaces when either area is asked for — and **38 of the 179 gaps are `X-*`**, so a fifth of the corpus, and the hardest fifth, gains structure it does not have today.
- **One field serves both axes the human named** — topic (`EFF`) and part-of-a-feature (`part-1`) — which is the argument for free-form strings over a fixed taxonomy.

Three constraints, the second adopted on agent judgement:

1. **Labels are a filter, never structure.** `Blocked by:` remains the only ordering truth. The cascade must never walk labels and "do all `CLASS` before `LIN`" must never be inferable — that would be a second edge kind maintained by hand, which [Revision semantics](06-revision-semantics.md) already rejected when it killed the `Touches:` field.
2. **The label vocabulary is declared in the map's Notes**, and a node may only use a declared label. Reason: drift. A free-for-all yields `EFF`, `effect` and `effects` inside a week, and a filter that silently misses a third of its matches is worse than no filter. This also puts labels in the same manager-maintained region of the map as the discovered bar commands from [Done-ness and termination](10-done-ness.md).
3. **Optional, absent by default.** A fresh 15-node effort needs none. This map declares no vocabulary and its 20 nodes carry no labels — adding them here would be bookkeeping with no reader.

Deliberately **not namespaced** (`area:EFF` / `phase:1`) in v1. If topic and phase labels collide in practice, that is friction for [Workflow self-improvement](19-workflow-self-improvement.md) to catch, and cheaper to discover than to predict.

### Four files, and why the count is not two

```
.scratch/<effort>/
  map.md            Destination, Notes, Not-yet-specified, Out-of-scope.
                    Bounded by fog items and notes, not by node count.
                    Loaded every session.
  decisions.md      One capped line per resolved node. Append-only.
  flags.md          One capped line per flag, with its settled/outstanding
                    state. Append-only. The only file the sweep must read whole.
  issues/NN-<name>.md   One file per node. All detail.
```

**The directory is `.scratch/<effort>/`** — unchanged from wayfinder and from this map, and confirmed by lookup rather than assumed: Lang ignores only `/target` and `/.direnv`, so `.scratch/` is **committed** there, exactly as it is here. The graph is version-controlled in the target too.

**The index left the map because the never-delete rule made it unbounded.** An index entry can only ever be appended (or struck through), so the file holding it grows monotonically in node count, while the map's other sections grow only with fog items. Two growth rates, two files. Lang reached the same layout by hand: `decisions.md` separate from `inventory.md`.

**Index entries are capped at one line — one sentence, ~25 words.** Enough to judge relevance; never a restatement, because the detail already lives in the node and the map's own rule is that a decision lives in exactly one place. This map has been breaking that rule: the [Done-ness and termination](10-done-ness.md) entry is a ten-line paragraph. At 179 nodes that style is ~25k tokens per session load; capped, it is ~5k. The ten existing entries **move verbatim** rather than being shortened — never-delete holds — and are marked as pre-cap.

**`decisions.md` is grouped by label** where a vocabulary exists, so a session scoped to one area reads one section instead of the whole index. Flat where it does not.

**`flags.md` holds state; the node holds text.** The human chose the same split as the index, for the requirement [Done-ness and termination](10-done-ness.md) delegated here: the sweep must collect every outstanding flag before an effort can close, and a 179-file grep per sweep is a scan the design should not need. The checkbox lives **only** in `flags.md`, so settling a flag never touches a node file and the two can never disagree — the completion report is the unchecked lines.

### The node file

Mandatory: the name, `Type:`, `Status:`. Everything else appears only when it has a value. Fields are bare `Key: value` lines, not YAML frontmatter, because Lang's tracker doc already reads that way and compatibility is worth more than parseability the graph does not need.

**Fields live in the header block — everything above the first `##` heading — and nowhere else.** This rule was not chosen, it was discovered: verifying the graph at the end of this session, a grep for `^Status: open` matched the template *inside this node's own answer* and briefly reported a resolved node as sitting on the frontier. A format that documents itself will always contain lines indistinguishable from real fields, so a scanner that reads the whole file is wrong on the very node that defines it. The header rule makes the region unambiguous and costs nothing, since fields were already written there.

```markdown
# <free-form name — carries a foreign label when one exists>

Type: grilling | research | prototype | task | implementation
Status: open | claimed | resolved | superseded | out-of-scope
Labels: EFF, REG
Blocked by: 31, 47
Supersedes: 12
Superseded by: 88

## Question
## Acceptance condition     <- implementation only; written by the spawning node
## Answer                   <- appended on resolution
## Flags
## Review
## Interview
```

The ordering is load-bearing: **what a reader needs first is at the top, and everything that grows is at the bottom.** A subagent, a reviewer and the human all open a node for its question; only a respawned attempt needs the interview log.

- **`## Flags`** — free prose per flag, prefixed `ASSUMPTION`, `CONDITION-WRONG` or `DELEGATED`, covering the three kinds from [Node type taxonomy](07-node-type-taxonomy.md) and [Relay protocol](08-relay-protocol.md). No checkbox here; state lives in `flags.md`.
- **`## Review`** — the reviewer's outcome, appended per round. Rounds accumulate in one node because a rejection is not supersession (taxonomy, point 2), so the file shows how many times an implementation was sent back.
- **`## Interview`** — one block per attempt: its routing key, then each relayed question and each human answer appended **at relay time**, each answer marked `verbatim` or `paraphrase`. A dead attempt is marked in its own heading. Two things fall out for free rather than needing fields: the **respawn cap** is the number of attempt blocks (at most three), and **banked progress** is simply a non-empty `## Interview` on a node whose `Status:` is `open` — which satisfies [Relay protocol](08-relay-protocol.md)'s demand that a half-interviewed node be distinguishable from a never-started one.

**The interview log sits inline, at the bottom, rather than in a sibling file** — adopted on judgement, and the closest call in this answer. For it: Lang's tracker doc already says *"comments and conversation history append to the bottom of the file under a `## Comments` heading"*, so inline is the compatible choice; a respawn hands the fresh subagent one file rather than two; and there is no second file to fall out of sync. Against it: at 179 nodes with multi-attempt interviews, node files could end up mostly transcript. **Revisit trigger:** if a node file's interview outgrows its question and answer combined, split it to `issues/NN-<name>.interview.md` — the same shape as the two indexes, so the move costs a path and nothing else.

**Superseded text stays where it was**, struck through or explicitly marked, per the standing rule — including in `decisions.md`, where a superseded node's line is struck through in place and the replacement gets a new line of its own. The cascade already visits every affected node, so it does this at no extra cost, and the index stays accurate without anything rewriting history.

### A fifth status: `out-of-scope`

Found from the wayfinder rules rather than from the inputs: ruling an existing ticket out of scope requires it to be *closed*, and a local-markdown tracker has no "closed" other than a `Status:` value. None of the four fits. `resolved` is actively wrong — it would satisfy `Blocked by:` edges and it would put a scope boundary in the decisions index, which wayfinder explicitly forbids.

So: **`out-of-scope`, and it does not satisfy an edge** — a `Blocked by:` onto it is an error, exactly like `superseded`. The reason is not symmetry: ruling B out of scope means A's dependency on B has to be revisited, because either A is also out of scope or its premise was wrong. Silently unblocking A would let it run on a dead premise. The same mechanical check catches both, and an out-of-scope node's line goes in the map's **Out of scope** section, never in `decisions.md`.

**Adopted on agent judgement, and it does cut against a standing preference** — the human's principle is to avoid machinery for predicted needs, and this case has not yet occurred on this map. It is one word in a vocabulary list rather than machinery, the alternative is wrong rather than merely simpler, and on a corpus where the author already writes `Q11 — RETIRED, the question was malformed` by hand it will occur early.

### The status vocabulary is otherwise unchanged, and that is now a checked claim

`open` / `claimed` / `resolved` / `superseded` / `out-of-scope`. Three prior nodes each demanded "no new status" for a mechanism — parked is `open`, under-review is `claimed`, flags are not statuses — and every one of those holds here. `out-of-scope` is not an exception to any of them: it is the one case none of them considered.

Lang's own decision log is worth recording as support, because a human working this problem by hand converged on most of this vocabulary independently: `Q4 — PARKED`, `Q9 — SUPERSEDED by D15`, `Q13 — RESOLVED by D25`, `Q14 — OPEN`, `MUT-7 — NEW REQUIREMENT`, plus `(tentative)` and `(proposed)`. **Park and supersession-with-a-forward-pointer were both reinvented there without prompting**, which is the strongest evidence this map has that [Revision semantics](06-revision-semantics.md) and [Relay protocol](08-relay-protocol.md) picked shapes a working author actually reaches for.

### It is a superset of the target's tracker doc, so adoption extends rather than rewrites

Checked line by line against `Lang/docs/agents/issue-tracker.md`. Identical: the directory layout, `map.md`, `issues/NN-<slug>.md` numbered from `01`, the `Type:` and `Status:` and `Blocked by:` lines, the frontier scan, the claim procedure, and appending conversation to the bottom of the file. Extended: five types where it has four, five statuses where it has two, three edge kinds where it has one, plus `Labels:` and the flag and review sections.

Exactly **two behavioural divergences**, and both are already owned elsewhere: the frontier's *"first by number wins"*, which [Human-initiated steering](16-human-steering.md) is replacing, and resolve appending to `decisions.md` rather than to the map body.

So the call this node was asked to make: **adoption appends a section to the target's tracker doc; it does not rewrite it.** Every ticket already written under that doc stays valid unchanged, which is the property that makes a 179-node migration thinkable at all.

### What a `check` would enforce

[Graph state mechanism](05-graph-state-mechanism.md) named a read-only `check` as the first thing to extract if drift appears. It could not be specified before now; it can be, and this is the list, which is also the sweep's mechanical half:

1. Every `Blocked by:` target exists, and is not `superseded` or `out-of-scope`.
2. Every `Superseded by:` has a matching `Supersedes:`, both directions present.
3. No `NN` used twice; no gaps that indicate a reused number.
4. Every `Labels:` entry appears in the map's declared vocabulary.
5. Every `resolved` node has an `## Answer` and exactly one line in `decisions.md`.
6. Every `## Flags` entry has a line in `flags.md`, and none the other way.
7. Every `implementation` node has an `## Acceptance condition` before it is `claimed`.
8. No node has more than three `## Interview` attempt blocks.

Eight invariants, all mechanical, none requiring judgement — which is the shape of thing worth extracting and the opposite of the cascade's work.

Two scanning rules they depend on, both learned by running the checks against this graph rather than reasoned out: **read fields only from the header block**, per above, and **skip fenced code blocks** — the second false positive of the session was `issues/NN-<name>.md`, a placeholder inside `flags.md`'s own format example, reported as a broken link.

### Consequences

- **[Adopting an in-flight effort](18-adopting-in-flight-effort.md) unblocks**, and its import target is now fully specified: `NN` ids with labels in names, `Labels:` from Lang's 13 families, prose blocks-lists inverted into `Blocked by:`, 43 decisions into capped `decisions.md` lines, and a section appended to Lang's tracker doc rather than a rewrite.
- **One new node:** [Write the graph conventions document](21-conventions-document.md) — an `implementation` node, the map's first, blocked by [Naming](14-naming.md) and [Git and code-landing policy](11-git-and-code-landing.md). This answer is a decision record; the shipped document is instructions with the reasoning stripped out, and they are not the same artifact.
- **The scale number on this map was wrong.** It has said "~130 gaps" since [Dogfood target](09-dogfood-target.md). Lang's inventory holds **179 distinct labels across 188 table rows** in 13 families, plus 43 settled decisions and 48 consistency rows. Every place the map reasons about scale is reasoning about a corpus a third larger than it thought.
- [Naming](14-naming.md) inherits every field and section name above, plus `## Interview` versus Lang's `## Comments`, plus one term this node coined: **label**.
- [Cascade pass mechanics](15-cascade-pass-mechanics.md) gains two concrete duties — striking through a superseded node's `decisions.md` line, and appending flag lines to `flags.md` — and the eight invariants above as the mechanical half of the sweep.
- [Human-initiated steering](16-human-steering.md) gains its subset selector.
- [Subagent context contract](12-subagent-context-contract.md) now knows the exact pointer set a worker receives: the node file, `map.md`, and `decisions.md` scoped by label.
- The map's *Extraction of a graph tool* fog is now specified in everything but the trigger.

## Annotation: one path changed, every name confirmed

Added by [Naming](14-naming.md), which this answer explicitly handed the field and section names to.

- **`issues/NN-<name>.md` → `nodes/NN-<name>.md`.** `issue` is a hosted-tracker word: in a repo with real GitHub issues there would be two numbering spaces sharing one name, and a commit trailer reading `Issue: 21` would point at something that does not exist. The directory has moved and every link is repointed. **The illustrative paths in this answer — including the layout block above — were left exactly as written**, per the never-delete rule: they record what was decided at the time. The authoritative statement of the layout is [Write the graph conventions document](21-conventions-document.md).
- **Every field and section name is confirmed unchanged**: `Type:`, `Status:`, `Labels:`, `Blocked by:`, `Supersedes:`, `Superseded by:`, and `## Question`, `## Acceptance condition`, `## Answer`, `## Flags`, `## Review`, `## Interview`. So is the fifth status `out-of-scope`, against Lang's hand-written `RETIRED` — the two are different concepts, and this design already has `superseded` for the second.
- **`## Interview` over Lang's `## Comments` is confirmed** — this answer's one knowing divergence in name. An interview log is structured, and *interview* is what the `/grilling` skill itself calls the exchange.
- **`Labels:` keeps its name, and the collision is resolved by retirement instead.** `Label: wayfinder:map` had no function in a markdown tracker holding one file called `map.md`, so it is struck from the map and the word `label` belongs to `Labels:` alone.
- **`decisions.md` keeps its name**, though it indexes resolved implementation nodes too. Under [Lifecycle scope](03-lifecycle-scope.md)'s thesis — implementing is how you find out what to decide — a landed implementation *is* a decision on the route, so the name is correct rather than merely convenient. `resolved.md` was the alternative considered.

## Annotation: the two bookkeeping duties are the manager's steps, not the pass's writes

Added by [Cascade pass mechanics](15-cascade-pass-mechanics.md), reported as an `INVALIDATIONS` entry by
that node's worker, in its words:

> **[Graph file format](13-graph-file-format.md).** Its consequences read *"[Cascade pass mechanics] gains
> two concrete duties — striking through a superseded node's `decisions.md` line, and appending flag lines
> to `flags.md`"*, and its answer says the cascade *"does this at no extra cost"*. Under this answer no
> agent in the pass writes any file, so both duties are the manager's procedural steps — where the shipped
> `graph-conventions.md` already puts them, under `Supersede` and `Raise a flag`. The duties survive
> intact; only the party performing them changes.

Flagged as that worker's own judgement at `15.3`.

## Annotation: the graph becomes five files, and for the reason this node got wrong

*Filed by the manager, in the reporting worker's own words.* From [What the token findings change in the workflow
and its skills](53-what-token-findings-change.md):

> Its answer fixes *"the graph is four files"*; part 2 of this answer makes it five. Its stated reason for
> splitting `decisions.md` out — two growth rates, an index growing without bound in node count while *"this
> map's other sections grow only with fog items and notes"* — is already recorded as falsified in the map's own
> fog, and this answer acts on that falsification: the other sections grew too, in **words per item** rather than
> item count. So the same remedy is applied to the same file for the reason node 13 got wrong, on measured
> numbers rather than predicted ones.

**Everything else this node fixed is untouched**: the identity conventions, the `Labels:` field, the fifth
status, and the eight mechanical invariants — now nine. The repair is [Restructure `map.md` to what every worker
needs](59-restructure-the-map.md), whose clause 10 requires `graph-conventions.md` to name the correct number
and describe the new file's role.

**Worth keeping beside it: the split this node made was right and its reasoning was the weaker half.** It
predicted one growth rate would dominate; the measurement four days later found the growth is **words per item**
in every section, which is why `map.md` reached 92,113 characters while `decisions.md` stayed at one capped line
per node. The remedy that works is the same one — an index cites and never restates — applied to the file this
node exempted.
