# Naming the workflow and its vocabulary

Type: grilling
Status: resolved
Blocked by: 07

## Question

What is this workflow called, and what are its core terms?

Use the `/naming` skill. Terms in play, currently used loosely and inconsistently:

- The **workflow** itself — invoked as a slash command, so the name is user-facing. The repo is `graph-agent`, which may or may not be the name.
- The **graph**, and a single element of it: node? issue? ticket? Wayfinder says ticket; the user has said issue and node interchangeably.
- The **manager thread** — the user's phrase was "management main ai thread". Firstmate calls its equivalent the first mate, and the human the captain.
- The **subagent** working one element — the user said subtask, which conflates the work with the worker. Firstmate says crewmate.
- The **revision** relationship, whatever [Revision semantics](06-revision-semantics.md) decides it is.
- The **write lock** on code modification.

Now unblocked. [Node type taxonomy](07-node-type-taxonomy.md) fixed the kinds but deliberately did not fix their labels, so the terms it hands over are:

- The five kinds: `research`, `prototype`, `grilling`, `task`, `implementation` — four inherited from wayfinder, one new. Whether `implementation` is the right user-facing word is open.
- The **reviewer** — the independent agent that checks an implementation before it resolves. Not a node type, so it needs a word that does not read like one.
- The **acceptance condition** on an implementation node.
- The **flagged assumption** an implementer leaves behind when it decides a small ambiguity itself.

Added by [Relay protocol](08-relay-protocol.md), which named several things provisionally while resolving and deliberately did not settle any of them:

- The **relay** itself — the channel between subagent and human, and the payload that travels on it. "Relay" is inherited from firstmate, where it meant something else entirely (external channels like X and Discord), which this effort has ruled out of scope. Reusing the word may be a mistake.
- **Park** — a node the human deferred, which has stored its progress and gone back to `open` carrying banked answers.
- **Attempt** — one spawned agent instance working a node, of which there may be up to three before escalation. Distinct from the node, which outlives it.
- **Banked answer** — a human answer already paid for and stored, awaiting a fresh agent.
- **Delegated flag** — the record that the human said "you decide" and the subagent answered instead.
- **Manager note** — the manager's own annotation on a relayed question, drawn only from context it already holds.
- **Provenance** — whether a recorded answer is the human's verbatim words or a manager paraphrase.

Added by [Dogfood target](09-dogfood-target.md), which supplies a competing vocabulary that already exists in the target repo and is in daily use:

- Lang calls an open question a **gap**, not a node, issue or ticket — and labels them by family (`CLASS-`, `LIN-`, `EFF-`, `REG-`, `X-`). It calls a settled decision a **D-number** (`D31–D47`). These are cited by the hundred across its documents, so they are not renameable on a whim.
- Lang's own `docs/agents/issue-tracker.md` uses wayfinder's **ticket**, while this map has used **node** throughout and the human has said issue and node interchangeably. Three words for one thing are now in play across two repos that will be open at the same time during the dogfood.
- Lang also already has a word this map lacks: **claimed** in its sense, plus `handoff` for the resuming point and `superseded` for retired docs — the second of which matches [Revision semantics](06-revision-semantics.md)'s term exactly, which is a point in its favour.

Whether the workflow imposes its vocabulary on an adopted effort or tolerates the local one is really [Adopting an in-flight effort](18-adopting-in-flight-effort.md)'s question; what belongs here is deciding the workflow's own words knowing a clash is coming.

Added by [Done-ness and termination](10-done-ness.md), which named four things and revealed that one existing word is already overloaded:

- The **completion report** — what the manager hands the human when the frontier empties.
- The **sweep** — the cascade agent run over the whole graph with no triggering revision. Currently distinguished from "cascade" only by that scope, which is thin ground for two words.
- The **bar** — the standing quality properties every implementation node must leave the tree meeting. "Standing bar", "quality bar" and "default checks" were all used while resolving; none is settled.
- **Postpone** — the human deferring a flag at report time, which creates a node. That is the *same act* as **park** from [Relay protocol](08-relay-protocol.md), applied to a flag instead of a question. Two words for one mechanism is the exact trap this node exists to catch.
- **Done** now has three meanings in play: a bounded effort that terminates, an open-ended effort that legitimately never does, and this map's own checklist destination. If they keep one word, a reader cannot tell which is meant.

Added by [Graph file format](13-graph-file-format.md), which is the first node to hand over names that are already **written into files** rather than merely used in conversation — so renaming any of them is now a migration, however small:

- **Every field and section name**, now fixed on disk: `Type:`, `Status:`, `Labels:`, `Blocked by:`, `Supersedes:`, `Superseded by:`, and the sections `## Question`, `## Acceptance condition`, `## Answer`, `## Flags`, `## Review`, `## Interview`.
- **`## Interview` versus Lang's `## Comments`.** Lang's tracker doc already says conversation appends to the bottom under `## Comments`; the format kept the log inline for exactly that compatibility and then gave it a different heading, because a relay log is structured — attempts, routing keys, provenance — and "comments" undersells it. This is the one place the format knowingly diverged in name while agreeing in substance, and it is this node's to confirm or overturn.
- **`label`** — a new term, and the field is the human's own addition. A label is a *family or part* (`CLASS`, `part-1`), never a node's id (`CLASS-1`), and the two will be confused constantly unless the words separate them cleanly. Note the collision risk: this map already uses "label" in `Label: wayfinder:map`, for something else entirely.
- **`out-of-scope`** — the fifth status. Lang's author writes `RETIRED` by hand for a neighbouring idea; wayfinder says *ruled out of scope*. Two candidate words, one concept.
- **The three flag markers**: `ASSUMPTION`, `CONDITION-WRONG`, `DELEGATED`. These are the first terms in this effort that are written in caps as machine-readable tokens rather than prose, so they need to be both greppable and readable.
- **The three index files** — `decisions.md` and `flags.md` alongside `map.md`. "Decisions so far" was a *section* name inherited from wayfinder and is now a *file* name, which is a promotion worth noticing.

Added by [Git and code-landing policy](11-git-and-code-landing.md), which named one thing that will be written into every commit message and three that describe the new step at the end of an implementation node:

- **The commit-message token that carries a node's `NN`.** This is the join key between git history and the graph — `git log --grep` is how the cascade finds a node's landed code — so it has to be greppable without matching prose, stable, and tolerable in a repo's log for years. Candidates in play: `[34]`, `n34:`, a trailer line. Lang's author already writes `spec: struct values, effect handlers, sums (D31-D47)` by hand, which is a precedent for parenthesised ids and against a leading token.
- **The gate** — the step where the manager raises a reviewed diff and the human approves it. Currently called "the gate" for lack of anything better, and it collides conceptually with the independent **reviewer**, which is a different actor doing a different check. Two review-shaped things at the end of one node need words that cannot be confused.
- **Approval**, and the **correction round** the subagent runs when the human is not happy. A correction round is emphatically *not* supersession and not a review round in the reviewer's sense; if it is called a review the two logs will be conflated.
- **The two streams** — the per-node code commit, and the periodic commit of the graph's own files. They have no names yet and the distinction is load-bearing, since one goes through the gate and the other never does.

Blocked on the taxonomy: naming the node types before knowing what the types are would be backwards.

Deliberately not started yet: no `CONTEXT.md` glossary exists for this repo. Per the domain-modeling skill, create it lazily when the first term is genuinely resolved — which is this issue. Writing it earlier would only have to be rewritten.

Still true, with a model to copy: **Lang already runs a `CONTEXT.md`** at its repo root — *"the glossary. Terms are defined once, here."* — with its working notes distinguishing settled glossary entries from *"terms the author uses inconsistently with themselves (these are interview questions, not glossary entries)"*. That distinction is worth stealing when this node writes its own.

## Answer

**The workflow is `/expedition`. The metaphor stops at the map: the product and one run of it carry a
cartographic name, and every actor and mechanism underneath is described plainly. One element of the
graph is a `node`.**

The vocabulary now lives in one place — [`CONTEXT.md`](../../../CONTEXT.md) at the repo root, forty
terms in the domain-modeling glossary format. The load-bearing half of that file is not the
definitions but the **`_Avoid_` lines**: this node exists because eight resolved nodes had left
`sweep`/`cascade`, `park`/`postpone`, `node`/`issue`/`ticket`, `bar`/`quality bar`/`default checks`
all live at once. A definition alone does not stop drift; a definition with the rejected words
attached does, because the next agent looking up `postpone` finds it named and refused.

### What the human decided, and the one place they were right against the recommendation

**The register, converged.** `/expedition` with plain internals, over `/graph-agent` literal and over
firstmate's crew metaphor taken all the way down. What it buys: where wayfinder *charts* the way, an
expedition *travels* it, which is precisely the delta this map exists to add — [Lifecycle
scope](03-lifecycle-scope.md) put implementation inside the graph rather than downstream of it, and
the name now says so. And because the metaphor stops at the map, no term has to be translated before
it can be understood: *manager*, *worker*, *checker*, *gate* each say what the thing does.

**The element word: DIVERGENCE, and the recommendation was wrong.** The recommendation was `issue`,
on four arguments — the directory was already `issues/`, the human had used the word themselves, it
is what wayfinder calls the underlying object, and it matches every tracker in existence. The human
rejected it on the fourth argument turned around:

> "maybe issue is not good as a name, since there might be users that are not using the skills and
> they could think it is a github issue?"

That is decisive, and it fails the naming method's own test — **claim no property the value doesn't
have**. Calling it an issue asserts it lives in the repo's issue tracker. It does not: it is a
markdown file in `.scratch/`. In a repo that has real GitHub issues there would be two numbering
spaces both called *issue*, and the commit trailer `Issue: graph-workflow/21` would read as a
reference to a hosted issue that does not exist. Matching the tracker's vocabulary was not a virtue;
it was the collision.

So the survey ran again, and every *richer* candidate failed too:

- `ticket`, `card`, `item`, `story` — the same collision, one tracker further away.
- `step`, `leg` — both imply a sequence, and this is a frontier, not a queue. A false property.
- `waypoint` — collides with nothing and fits `/expedition` exactly, but it is a metaphor word inside
  the plain register just chosen, and it was the expensive option.
- `gap` — Lang's own word for its 179 open questions, so adopting it guarantees a clash on the very
  first adopted effort.
- `question`, `decision` — half of all nodes are implementations.

Which leaves **`node`**: empty of meaning, and honest. It is the type rather than the name, and
normally the method would reject it for that — but the survey shows the alternatives buy their
richness with either a false claim or a collision, and *empty but true* beats *rich but misleading*.
It also happens to be the only word that carries the edges, which is the one structural fact about
the graph that matters, and it is the corpus's word already, so the rename cost was one directory
move and no prose.

**The commit token: the trailer, and a collision nobody had noticed.** `Node: <effort>/<NN>` in the
commit body. [Git and code-landing policy](11-git-and-code-landing.md) had specified "the node's id
in the subject", and deriving the actual token exposed a defect in that: **`NN` restarts at `01` for
every new effort a repo hosts**, so a bare id is ambiguous across efforts and `git log --grep 21`
returns unrelated work from a previous one. The cascade *acts* on what that query returns — it
repoints edges and judges code — so an ambiguous join key is not cosmetic. A trailer has room for the
effort where a subject line does not, it is git-native and exactly greppable
(`git log --grep '^Node: graph-workflow/21$'`), and it keeps subjects readable. The cost accepted is
that the token is invisible in `git log --oneline`; the reader of a join key is an agent, and
`git log -- <path>` prints full messages anyway.

### Three renames, decided on the method rather than asked

1. **`task` → `precondition`.** The old name carried no information — every node is a task in
   ordinary English — and it collided twice: with the human's original word for a worker
   ("subtask"), and with the harness's own task tooling. [Node type
   taxonomy](07-node-type-taxonomy.md) had already written the test as *"precondition versus
   deliverable"*, so the name was sitting in its own answer. Zero nodes carry `Type: task` today, so
   this rename costs nothing. **This is the one user-facing type name changed without asking** — it
   is a single word to overturn.
2. **`reviewer` → `checker`.** Two review-shaped things sat at the end of one implementation node and
   the human's word had to win, because *review* is what they will actually say they are doing. The
   agent gets `checker`, which is also more honest about its job: the taxonomy already required it to
   check against a stated acceptance condition *"or its review collapses into a second opinion"*. So
   the agent **checks**, the human **reviews and approves**, and `## Review` on a node file now
   unambiguously means everything that happened after the code landed.
3. **`sweep` re-derived, not renamed.** It was distinguished from `cascade` only by scope, which the
   node itself called thin ground for two words. The honest distinction is *purpose*: a cascade
   propagates a change it knows about; a sweep looks for changes nobody propagated. Same work,
   opposite direction. Both names survive because they now mean different things.

### Four words killed outright

- **`postpone` → `promote`.** The map flagged park-versus-postpone as *"the exact trap this node
  exists to catch"*. They are not in fact the same mechanism — park returns an existing node to
  `open`, postpone *creates* a node from a flag — but the second was named for the human's intent
  rather than for what happens. Named for the mechanism it is **promote**: turn a flag, or a
  one-line note of friction, into a node. That is also exactly the "promotion step" [Workflow
  self-improvement](19-workflow-self-improvement.md) asks for, so one word now covers both.
- **`provenance` → `verbatim` / `paraphrase`.** A heavyweight abstraction over a two-valued label.
  Mark the answer with what it is.
- **`write lock` → `code slot`.** [Git and code-landing policy](11-git-and-code-landing.md) made
  occupancy a *discovered* property of the working tree, so there is no lock object anywhere in the
  design. A name that promises one would send an agent looking for a file that does not exist. The
  corpus was already drifting to "the slot" on its own.
- **`done` → `resolved` and `closed`.** It was doing triple duty: a node being answered, an effort
  being over, and this map's own checklist. Now a **node resolves** and an **effort is closed**, on
  two different objects, by two different actors — only the human closes. `done`, `finished` and
  `complete` are refused. `completion report` follows it to **closing report**.

### `grilling` survives, and the reason is an axis nobody had stated

The consistency argument said to rename it `decision`, so that all five kinds name their output. It
loses to a better axis that the existing names already follow: **the type names what its worker
does**, and three of the five name a skill the worker literally invokes — `/grilling`, `/research`,
`/prototype`. Under that axis `grilling` is not a stray technique word; it is the procedure, and
`Type: grilling` tells a worker what to run. `precondition` is the one kind with no procedure to
name, which is fitting for the residual category.

This also spares `decisions.md`, which the consistency argument would have forced to `resolved.md`.
It indexes every resolved node including implementations, so "decisions" looked slightly wrong — but
this workflow's whole thesis, from [Lifecycle scope](03-lifecycle-scope.md), is that implementing is
how you find out what to decide. Under that thesis a landed implementation *is* a decision on the
route, and the file is correctly named.

### What was deliberately not renamed

- **`relay`** — kept, and it is a good name rather than merely an inherited one: to relay is to pass
  along unaltered, which is exactly the guarantee [Relay protocol](08-relay-protocol.md) specified
  (verbatim, with a divergence marker, manager answers nothing). The name encodes the constraint.
  Firstmate's different Relay is noted in the glossary and is out of scope here anyway.
- **`park`**, **`banked answer`**, **`manager note`**, **`attempt`**, **`acceptance condition`**,
  **`flag`**, **`the bar`** — all correct English for what they are. `the bar` keeps its bare form:
  *quality bar* is redundant and *default checks* is actively wrong, since [Done-ness and
  termination](10-done-ness.md) made the bar a set of **properties** whose commands are discovered
  per repo.
- **The three flag markers** `ASSUMPTION`, `CONDITION-WRONG`, `DELEGATED` — each names what is being
  reported, and all three are greppable. Kept as written.
- **`out-of-scope`**, against Lang's hand-written `RETIRED`. They are different concepts: out of
  scope means beyond the destination, retired means superseded, and this design already has
  `superseded` for the second. Adopting Lang's word would have merged two statuses.
- **`## Interview` over Lang's `## Comments`** — the one knowing divergence in [Graph file
  format](13-graph-file-format.md), confirmed. An interview log is structured (attempts, answers,
  verbatim-or-paraphrase) and "comments" undersells it; *interview* is also what the `/grilling`
  skill itself calls the exchange.
- **`Labels:`** — kept, because the field genuinely spans two axes the human named (an *area* like
  effects, and a *part* like the first half of a feature), and only a generic word covers both. The
  collision it was flagged for is resolved by retirement rather than by renaming: `Label:
  wayfinder:map` in the map header is a wayfinder artifact with no function in a markdown tracker —
  one map file, identified by its name — so it is struck there and the word belongs to `Labels:`.

### The rename that actually touched disk, and its limit

`issues/` → `nodes/`, and every markdown **link** repointed. What was deliberately *not* rewritten:
the ~200 places the corpus's prose says "node" needed no change, and the handful of illustrative
paths inside resolved nodes — chiefly the directory-layout block in [Graph file
format](13-graph-file-format.md) — were left as written, with an annotation instead. That is the
never-delete rule applied honestly: a link is navigation and repointing it destroys nothing, while a
resolved node's answer is the record of what was decided at the time and stays as it was. The cost is
one stale path in node 13's fenced layout block, and the mitigation is that the authoritative reader
for that will be [Write the graph conventions document](21-conventions-document.md).

### One flag, and it is the first real one on this graph

`CONTEXT.md` is the **first file this effort has written outside `.scratch/`** — a product-tree file
authored by a grilling node, which therefore passed no checker and no gate. [Git and code-landing
policy](11-git-and-code-landing.md) routes *code* through the gate and leaves the graph's own files
to the human's periodic commit; a glossary is neither. The judgement taken is that a decision record
rides the graph commit even when it sits at the repo root, and it is logged as an `ASSUMPTION` in
[flags.md](../flags.md) rather than silently. This is the flag mechanism running for real, on this
graph, before any implementation node has existed — which is one of the seven things [Dogfood
target](09-dogfood-target.md) requires be observed at least once.

Separately and not a flag: the repository is still named `graph-agent`. Renaming it to match the
workflow is the human's call and costs nothing in the graph, since no file refers to the repo by name.

### Consequences

- **[Write the graph conventions document](21-conventions-document.md) is unblocked** — both its
  blockers are resolved, and it becomes the map's first takeable implementation node. It inherits a
  glossary to be written in and a directory that has already moved.
- The map's largest fog item — the implementation nodes that write the skill files — loses a blocker
  and is now waiting on [Subagent context contract](12-subagent-context-contract.md) alone.
- **[Git and code-landing policy](11-git-and-code-landing.md) gains a correction, not a
  supersession**: the token is a trailer carrying the effort, because a bare `NN` is not unique
  within a repo. Its answer named the requirement correctly and got the scope of the id wrong.
- **[Node type taxonomy](07-node-type-taxonomy.md)** keeps four of its five names and loses `task`;
  its reviewer becomes the checker.
- **[Graph file format](13-graph-file-format.md)** has one path changed under it and every field and
  section name confirmed unchanged.
- **[Done-ness and termination](10-done-ness.md)** loses `done` as a word and `postpone` as a
  mechanism name; its completion report becomes the closing report.
- **[Adopting an in-flight effort](18-adopting-in-flight-effort.md)** now knows that Lang's *ticket*
  and *gap* clash with `node` rather than with `issue`, and that the trailer already carries the
  effort name, so an adopted effort's join key is unique from its first commit.
- **No new node.** The second session running with none, and every term the graph had left loose is
  now either settled or explicitly refused.

## Flags

Added by [Write the graph conventions document](21-conventions-document.md), which found this node
failing check 6 — a line in [flags.md](../flags.md) with no `## Flags` section behind it. The flag was
raised before the section that holds one had ever been written by procedure; the text was left where
it landed, in `### One flag, and it is the first real one on this graph` above, and this section is
the entry that check expects. Nothing is moved.

`ASSUMPTION` — wrote [`CONTEXT.md`](../../../CONTEXT.md) into the product tree from a `grilling` node,
so the glossary passed no checker and no gate. See the answer section named above for the full
reasoning and the two alternatives rejected.

## Annotation: two invalidations from node 29 — the glossary moves, and its count was always wrong

*Filed by the manager, in the reporting worker's own words.* [What keeps the shipped files consistent when a
decision changes a term](29-shipped-file-consistency.md)'s worker reported this node twice:

> Its answer puts the glossary at the repository root, and this answer moves it into the shipped set, leaving the
> root path holding a forward pointer. And its count is stale: it fixed *"forty terms"*, the file holds fifty
> term entries and forty `_Avoid_` lines, and the figure was copied from that node into `map.md` and into
> `decisions.md`.

**Verified by the manager rather than taken on trust:** `grep -cE '^\*\*[^*]+\*\*:' CONTEXT.md` returns **50**
and `grep -c '^_Avoid_' CONTEXT.md` returns **40**. So the *"forty"* was never a term count — it was the
`_Avoid_` count, and it propagated as a term count into two other files. The map is corrected;
`decisions.md` is append-only and its line stands with this annotation as the correction.

**This node's own outstanding flag is answered rather than contradicted.** It records that the glossary *"passed
no checker and no gate"* because a `grilling` node wrote it into the product tree. [Ship the glossary inside the
skill directory and make it state its own completeness](56-ship-the-glossary-into-the-skill-set.md) puts it
through both, for the first time.

**Where the glossary sits is now the only part of this node's answer that has moved.** The vocabulary itself, the
forty refusals, and the rule that the glossary is authoritative are all untouched.
