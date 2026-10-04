# What `/to-spec` and `/to-tickets` put in a ticket that this workflow's nodes lack

Type: grilling
Status: resolved
Blocked by: none

## Answer

From `/to-spec` and `/to-tickets` only a one-or-two-sentence intent line at the head of an implementation node's question is taken; testing stays with repo rules, slicing goes to the fog.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. It surfaced [node 386](386-begin-an-implementation-nodes-question-with-its-intent.md), which ships the intent line. The manager wrote its fog item on splitting work into `map-manager-only.md`'s `## Not yet specified`, as the handover proposed. Its `INVALIDATIONS` extend nodes 35 and 39. Flags 384.1, 384.2, 384.3 settle at the node closing report.

## Question

*The human's own question, `verbatim`, 2026-10-04, asked while node 380's gate was in front of them. **Minted by the manager and not surfaced by any worker.***

> I have a question in matt pockock skills /to-spec and /to-tickets I feel that they generate a ticket that is much bigger that what was generated for 383, it there some stuff that we should take ?

"383" is [node 383](383-ship-the-repo-docs-skill.md), whose node file holds the question and acceptance condition node 130's worker wrote for it. The two skills are installed with the `mattpocock-skills` plugin. On this machine, on 2026-10-04, a copy sits under `/nix/store/*-claude-code-mattpocock-skills-patched/skills/engineering/to-spec` and `.../to-tickets` (the store path is this machine's, and may change).

The answer decides what, if anything, from those skills' tickets this workflow's implementation nodes should take: in the question, the acceptance condition, or what a spawn carries. It also decides where the change would land.

## Interview

#### Questions 1 to 4, relayed 2026-10-04

*Pasted as the worker handed it back.*

`````
NODE:          What `/to-spec` and `/to-tickets` put in a ticket that this workflow's nodes lack (node 384)
ABOUT:         Decides what, if anything, this workflow's implementation nodes should take from the two mattpocock skills' output, and which shipped file each taken item goes into. The human asked this while comparing that output with node 383, the `/repo-docs` node.

SO FAR:        I read both skills. There are two store copies (`shg018…` and `w0svxj…`), and both skills are byte-identical in them, so it does not matter which copy is current. I also read node 383, the map, decisions.md, and the shipped rules on conditions, spawns, the bar, and the node-file template.

               What the two skills produce:
               - `/to-spec` writes one parent spec. Its sections are: Problem and Solution (both from the user's point of view); a deliberately "LONG, extremely extensive" list of user stories; Implementation Decisions (modules, interfaces, schema, API, with no file paths or code snippets); Testing Decisions (what a good test is, which modules are tested, existing tests to follow, and test seams chosen at the highest point and checked with the user); Out of Scope; Further Notes.
               - `/to-tickets` splits work into tracer-bullet vertical slices. Each slice is sized to one fresh context window, is demoable on its own, and has prefactoring done first. A wide refactor is sequenced as expand, then migrate in batches, then contract. The user is asked about granularity and blocking edges. Each ticket is small: a "What to build" paragraph (end-to-end behaviour, user's point of view), Blocked by, Status, an acceptance-criteria checklist, and a link to the parent.

               Why 383 feels smaller. The impression comes mostly from `/to-spec`'s narrative sections, not from the ticket. In this workflow the spec's equivalent is the grilling node that decided the work. For 383 that is node 130, whose file is about 7,600 words. Node 383 is only the slice. Its acceptance condition is 700 words. Across all 232 implementation nodes in the graph, the median condition is 360 words and the 75th percentile is 685. These figures were derived on 2026-10-04 with awk over the `## Acceptance condition` sections. They are for scale only, not authoritative, and should be re-derived before anyone relies on them. So 383's condition is at the larger end, and it is far stricter than a `/to-tickets` checklist. What 383 does not have is any line of intent: its `## Question` is one sentence that points at node 130.

               What this workflow already covers:
               - Blocked by: the `Blocked by:` field.
               - Status: the `Status:` field.
               - Parent: the provenance line on the node.
               - Acceptance criteria: the self-contained condition, held by a blind checker.
               - Implementation decisions: settled on grilling nodes and copied into the condition.
               - The prototype-snippet exception: covered by "copy in any material held elsewhere".
               - Glossary and ADRs: covered by the repo's own docs and `map-implementation-rules.md`.
               - Sized to one session: the glossary's `Node` entry already says so.
               - A slice that cannot land green: implementation trigger 1 already makes "the size of your own node" a raise, and hard rule 6 makes a needed split a raise.

               Not covered anywhere in the shipped files:
               - Any duty to write tests or to choose where they go. The bar requires only that "the tests relevant to your change pass".
               - Any statement in an implementation node of what the work is for.
               - Any guidance on slicing a wide refactor.

               Whatever is taken would be written into this workflow's own files, never invoked from the plugin, per the standing direction not to depend on mattpocock-skills. I use "ticket" only for the plugin's output. The glossary refuses it as a word for a node.

Q1. Testing: say that new behaviour gets tested, and how
CONTEXT:       On a repo with code, a worker can pass today's bar without writing any test of what it built. On this effort it has never come up, because every implementation node so far produced prose.
ASK:           Should the bar require that the behaviour a change adds or alters is covered by tests where the repo has tests, with one sentence telling the worker how?
RECOMMENDED:   Yes, as one implementation node with two parts:
               (a) The bar gains the property "the behaviour the change adds or alters is covered by tests, where the repo has tests". It goes into the bar's statement in `expedition-implementation/SKILL.md` `## The bar`, the checker contract's bar given, and the glossary's `Bar` entry. Because it is a bar property, the blind checker holds every node to it, and no condition author has to remember it.
               (b) `## How you implement` gains one sentence: test external behaviour, at the highest existing seam that reaches it, with the repo's existing tests as the model.
               This extends node 10's bar, and I would report that under INVALIDATIONS. Cost: about 40 words across three files.
ALTERNATIVES:  - A per-node condition clause naming the behaviour to test (pushes seam choices onto grilling workers who may not have read the code).
               - The how-sentence only, with no bar change (the checker would not check it).
               - A map-only rule for this effort (does nothing here, since this effort's work is prose).
               - Take nothing until a code effort shows the gap.

---

Q2. One line of intent in an implementation node's question
CONTEXT:       A condition says what must be true, not what it is for. The worker decides small ambiguities on its own. Today the only route to intent is often a link to a long deciding node, about 7,600 words for 383.
ASK:           Should the author of an implementation node write, in its `## Question`, one or two sentences saying what the work makes possible and for whom (the equivalent of `/to-tickets`' "What to build"), rather than only pointing at the deciding node?
RECOMMENDED:   Yes. The worker who mints the node, or the manager, writes it.
               - Workers: one clause in the `NEW NODES` description of `## When a node you report is an implementation node`. That section is byte-identical in the grilling, implementation, precondition, prototype and research contracts, so the change lands in all five.
               - Manager: one clause in `expedition/SKILL.md` `### The four constraints on a condition you write yourself`.
               The checker is unaffected, since it never reads the question. Cost: about 20 words in each of six files. It goes against the compaction wish, which is why I limit it to one sentence.
ALTERNATIVES:  - Leave the question as a pointer (standing writing rule 2 favours citing over restating, and in 383's case the condition's clause 1 already gives the intent).
               - Have the spawn carry the intent (the manager would be writing material that is not its own).
               - A full Problem/Solution pair (the deciding grilling node already holds that).

---

Q3. Slicing guidance, and the wide refactor as expand, migrate, contract
CONTEXT:       The bar makes every implementation node land green. So a rename spanning many call sites has to be split into: expand (add the new form beside the old); migrate in batches, each its own node blocked by the expand; contract (remove the old form), blocked by every migrate batch. Nothing shipped says this.
ASK:           Should guidance on how to split work into implementation nodes (expand, migrate, contract for a wide refactor; prefactoring first) ship now?
RECOMMENDED:   Not now. It is a predicted need, and ground rule 4 says not to build for predicted needs. The case is already caught at runtime: a node too large to land green triggers implementation trigger 1 ("the size of your own node"), and hard rule 6 makes a needed split a raise. The human then decides the split. Shipping it would add one paragraph to each of the five copies of the shared section. Instead, the manager adds one line to the fog in `map-manager-only.md`, so the pattern is to hand when a code effort first raises it.
ALTERNATIVES:  - Ship one paragraph now in the five copies of the shared section.
               - Ship it in `graph-conventions.md` `## Adding a node` (the workers who mint nodes do not read that file).
               - Drop it with no fog line.

---

Q4. Leave out the rest
ASK:           Should everything else in the two skills stay out?
RECOMMENDED:   Yes. Each item and why it stays out:
               - The long user-story list: the condition's clauses are the checkable form, and the list only adds size.
               - The ban on file paths: conditions require repo-relative paths so the checker can find the work. Paths going stale is handled by the check before a claim, at node 373.
               - Separate Problem, Solution and Further Notes sections: the deciding grilling node holds these.
               - An Out of Scope section: conditions already carry "no other file changes", and instances found outside the list are reported, not edited.
               - Asking the human about granularity: the human is the scarce resource, and the manager files the `NEW NODES` workers report.
               - Tracker publishing and the `ready-for-agent` label: they do not apply here.
               - The prototype-snippet exception and the glossary/ADR reading: already covered.
ALTERNATIVES:  - Take the Out of Scope section as an optional part of a condition.
               - Take a short user-story list for nodes whose work is product behaviour.

RETROSPECTIVE:
1. What I had to hunt for: where the spec-like material for 383 lives (node 130). Whether the shipped files say anything about writing tests or slicing work: they do not, and finding that out took a sweep of them. That trigger 1 already covers node size.
2. What arrived that this node did not need: about 85% of decisions.md (worktrees, landing, flags, map moves). Only node 10 (the bar), nodes 33 and 94 (condition rules), node 130, and node 373 bore on this node.
3. What would have made this easier: the spawn naming node 130 as 383's deciding node. A derivation in derivations.md for condition sizes by node kind; I wrote the awk myself.
4. What was stale, wrong or contradictory: the manager's claim that several store copies exist is true, but those copies are byte-identical for both skills, so "check which one is current" was moot. The claim that 383's condition is "fairly tight" holds for precision, but by size it sits near the 75th percentile, not at the small end. map.md says the glossary holds "58 term entries"; node 302's index line says 51. I did not re-derive it, because this node does not need it.
`````

*The manager's note:* the worker is right that the manager's spawn called node 383's condition "fairly tight" where by size it sits near the 75th percentile.

#### The human's answer to questions 1 to 4, 2026-10-04

`verbatim`: *"Q1 I feel that will be in the repo rules if the user wants tdd or a lot of tests Q2 ok Q3 ok Q4 ok"*

*The manager's note:* **Q1 is a divergence.** It does not take the `RECOMMENDED` (a test-coverage property in the bar). It leaves testing to the repo's own rules, which the bar already honours through "whatever else the repo itself demands". That is closest to the alternative "Take nothing until a code effort shows the gap", though the reply gives its own ground. Q2, Q3 and Q4 take the worker's `RECOMMENDED`.

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      What `/to-spec` and `/to-tickets` put in a ticket that this workflow's nodes lack

ANSWER:
**One item is taken from the two mattpocock skills, one is kept for later, and the rest stays out.** The taken item is a line of intent at the head of an implementation node's question. The item kept for later is guidance on splitting work into nodes, as a fog line. Nothing is invoked from the plugin. What is taken is written into this workflow's own files.

**Why 383 looked smaller.** The size of the skills' output comes mostly from `/to-spec`'s narrative sections: problem, solution, a deliberately long list of user stories, implementation and testing decisions. In this workflow that material lives on the grilling node that decided the work. For node 383 that is node 130, whose file is about 7,600 words. Node 383 holds only the slice. Its acceptance condition is 700 words. Across the 232 implementation nodes, the median condition is 360 words and the 75th percentile is 685. These figures were derived on 2026-10-04 with awk over the `## Acceptance condition` sections. They are for scale only, not authoritative, and are re-derived before anyone relies on them. A `/to-tickets` ticket itself is small: a "What to build" paragraph, the tickets that block it, a status, and a checklist of acceptance criteria. The workflow already covers every part of that except the "What to build" paragraph.

**Testing (Q1): no change.** The worker recommended adding a test-coverage property to the bar. The human declined, `verbatim`: *"I feel that will be in the repo rules if the user wants tdd or a lot of tests"*. The bar already satisfies "whatever else the repo itself demands", and an effort's own standards live in `map-implementation-rules.md`. So testing stays with the repo's own rules, and the bar is unchanged.

**Intent (Q2): taken.** The author of an implementation node begins the node's `## Question` with one or two sentences saying what the work makes possible and for whom. This is the equivalent of `/to-tickets`' "What to build". A worker that mints the node writes it, and so does the manager when the manager mints the node. The reason: a condition states what must be true, not what it is for, and the worker that claims the node decides small ambiguities on its own. The checker is unaffected, because it never reads the question. It ships as the implementation node reported below.

**Splitting work into nodes (Q3): not shipped.** For a wide refactor this means expand, migrate in batches, then contract, with prefactoring first. Not shipping it follows ground rule 4, since it is a predicted need. A node too large to land green is already a raise: implementation trigger 1 covers "the size of your own node", and hard rule 6 covers a needed split. The manager writes one fog item for it in `map-manager-only.md` `## Not yet specified`, as its own change to the graph's files under `## Writing the graph`'s second branch. `### Change the map` says a new item is written straight into its file. Proposed text:

> - **How work is split into implementation nodes on a repository with code.** Nothing shipped says how. Every implementation node must land green, so a wide mechanical change, such as renaming something used across the codebase, cannot be one node. The known pattern is expand, migrate, contract: add the new form beside the old; move the callers over in batches, each batch its own node blocked by the expand; then remove the old form in a node blocked by every batch. Prefactoring comes first. It comes from mattpocock's `/to-tickets` and was left unshipped at [node 384](nodes/384-what-to-spec-and-to-tickets-put-in-a-ticket-that-our-conditions-lack.md), because implementation trigger 1 and hard rule 6 already make an oversized node a raise. Take it up when a code effort first raises one.

**Left out (Q4).** Each item, with the reason it stays out:
- The user-story list: the condition's clauses are the checkable form.
- The ban on file paths: conditions need repo-relative paths, and staleness is handled by the check before a claim.
- Separate Problem, Solution and Further Notes sections: the deciding grilling node holds these.
- An Out of Scope section: conditions already exclude other files, and instances outside the list are reported, not edited.
- Asking the human about granularity: the human's attention is the scarce resource.
- Tracker publishing and labels.
- The prototype-snippet exception and glossary or ADR reading: already covered.

INDEX LINE:    From `/to-spec` and `/to-tickets` only a one-or-two-sentence intent line at the head of an implementation node's question is taken; testing stays with repo rules, slicing goes to the fog.

FLAGS:
- ASSUMPTION — The cascade contract is left out of the intent line. The approved recommendation named the five worker contracts and the manager. The cascade's per-candidate agent also reports implementation nodes, but its `### A node you report` block already requires its `QUESTION` to state "the departure that produced it". That departure is the fix's purpose, so adding the sentence there would mostly repeat it and lengthen a file the human wants compacted. Index sentence: The intent line was not added to the cascade contract, whose reported node's question already states the departure it repairs.
- ASSUMPTION — The manager's sentence sits in `expedition/SKILL.md` `## Acceptance conditions`, immediately after "Where you minted the node, you write the condition.". The recommendation said "one clause in `### The four constraints on a condition you write yourself`". That list's items constrain the condition, not the question, and a fifth item would make the heading's "four" false. Index sentence: The manager's intent-line sentence was placed beside "Where you minted the node, you write the condition", not as a fifth item under the four constraints.
- ASSUMPTION — The new node's condition fixes the exact words of both added sentences, which I wrote. The human approved the content, not the wording. Fixing the words keeps the five copies identical and makes the condition easy to check. Index sentence: The exact wording of the intent-line sentences in the new node's condition is the worker's, not the human's.

NEW NODES:
Name:      Begin an implementation node's question with what the work makes possible and for whom
Kind:      implementation
Question:  Make the author of an implementation node begin its `## Question` with one or two sentences saying what the work makes possible and for whom. The worker that claims the node then has the work's purpose without reading the long node that decided it. The sentence goes into the five worker contracts' shared section on reporting an implementation node, and into the manager contract's `## Acceptance conditions`. Reported by node 384, which took this from the "What to build" part of mattpocock's `/to-tickets`.
Blockers:  none. Node 382 is open and has exactly the same six files as its work: the five worker contracts and `.claude/skills/expedition/SKILL.md`. Its concern is different, a search of resolved nodes before handing back, so this is not a join under the same-file, same-concern rule. Two consequences for the manager. With one code slot, the two nodes cannot run at once. If the manager merges them under the map's group-by-file preference, node 382's clause 3 ("no other sentence changes"), clause 5 ("nothing outside the change in clause 4 changes", "does not grow") and this node's clause 4 conflict, and go to the human. The two nodes' anchor sentences do not overlap, so either can land first unchanged.
Acceptance condition:
> The work is these six files, and no other file may be edited:
>   `.claude/skills/expedition-grilling/SKILL.md`
>   `.claude/skills/expedition-research/SKILL.md`
>   `.claude/skills/expedition-prototype/SKILL.md`
>   `.claude/skills/expedition-precondition/SKILL.md`
>   `.claude/skills/expedition-implementation/SKILL.md`
>   `.claude/skills/expedition/SKILL.md`
> These are files the workflow ships, so nothing is struck through and nothing is moved to any history file.
>
> Scope: the named places are the work, not instances of a defect, so the scope came from no search. On 2026-10-04, `grep -c 'No other kind of node carries a' .claude/skills/expedition-{grilling,research,prototype,precondition,implementation}/SKILL.md` returned 1 for each of the five files, and `grep -c 'Where you minted the node, you write the condition.' .claude/skills/expedition/SKILL.md` returned 1. These locate the anchors. They do not bound a scope.
>
> Done means every one of the following is true of the finished tree.
>
> 1. In each of the five worker contracts, under the heading `## When a node you report is an implementation node`, a new paragraph sits immediately after the paragraph that ends "No other kind of node carries a condition." and before the paragraph beginning "If you genuinely cannot say what done means". The new paragraph is exactly: "Begin the node's question with one or two sentences that say what the work makes possible and for whom. The worker that claims the node then knows what the work is for without reading the node that spawned it." Line wrapping may differ. The words may not.
> 2. The paragraph added in clause 1 is byte-identical across the five worker contracts, line wrapping included.
> 3. In `.claude/skills/expedition/SKILL.md`, under `## Acceptance conditions`, the sentence "You also begin its question with one or two sentences that say what the work makes possible and for whom." sits immediately after the sentence "Where you minted the node, you write the condition." and before the sentence beginning "Where a condition carries none of the three things". Re-wrapping that paragraph's lines is permitted. Its other words may not change.
> 4. Apart from clauses 1 and 3, no sentence in the six files changes. In particular, every heading is unchanged, including `### The four constraints on a condition you write yourself`, and the handover block's line beginning `NEW NODES:` is unchanged in each worker contract.
> 5. No file under `.scratch/` changes. `.claude/skills/expedition-checker/SKILL.md`, `.claude/skills/expedition-cascade/SKILL.md`, `.claude/skills/expedition/graph-conventions.md` and `.claude/skills/expedition/glossary.md` do not change.
> 6. The tree meets the bar.

INVALIDATIONS:
- Node 35 (a worker's handover carries no condition for the node it mints; the worker that reports an implementation node writes its condition): extended. That worker now also begins the reported node's question with a sentence of intent.
- Node 39 (who writes the condition for a node the manager mints): extended. The manager now also begins such a node's question with a sentence of intent.
- Node 10 (the bar): unchanged. Q1 was declined, so the bar gains no test-coverage property. Its existing "whatever else the repo itself demands" is the route the human named for testing rules.
- No resolved node states what an implementation node's `## Question` holds. A search of resolved nodes for "implementation node's question" returned nothing. Matches for the shared section's heading and for "Where you minted the node, you write" are citations, not rules, and no heading is renamed.

CONDITIONS:    I searched the conditions and questions of the 18 open nodes for: "When a node you report is an implementation node", "Where you minted the node", "four constraints", "## Acceptance conditions", "NEW NODES", "Not yet specified", "to-tickets|expand|wide refactor" and "what the work makes possible|intent". Matches:
- Nodes 40 and 32 match "four constraints". Both refer to node 39's constraints on a condition and are untouched.
- Nodes 382, 40 and 214 match "NEW NODES" only as a provenance or a protected sentence. Node 382's condition clause 3 protects sentences my new node also leaves unchanged.
No clause of an unclaimed node's condition is made wrong, so I write no replacement. No open node's question changes. The file overlap with node 382 is named under NEW NODES.

MISSING FROM MAP: none

Method-skill note: no method skill was invoked, so no part was skipped.

RETROSPECTIVE:
1. What I had to hunt for: That node 382 has exactly the same six files as the new node. Only the pre-handover search over open conditions surfaced it. Whether the five copies of the shared section are still byte-identical: they are, apart from a trailing blank line in the research copy. Who writes a fog line: `## Writing the graph`'s second branch together with `### Change the map`'s "A new item is written straight into its file".
2. What arrived that this node did not need: most of decisions.md again, on resume as at the start. The resume message itself was all needed.
3. What would have made this easier: a frontier view, or a listing, of which open implementation nodes edit which shipped files. Collisions like the one with 382 would then show without a search. `expedition/SKILL.md` notes that the frontier script cannot see file collisions.
4. What was stale, wrong or contradictory: nothing in the resume message. Its claims matched node 384's `## Interview` (commit `cf131955a`), including the manager's reading of Q1 as a divergence. One small mismatch in my own earlier payload: Q2's RECOMMENDED put the manager's clause in `### The four constraints…`, a list whose items constrain the condition, not the question. The second ASSUMPTION flag covers the move.
`````

## Flags

`384.1` `ASSUMPTION` **· settled** — The intent line was not added to the cascade contract. *(The worker's full text is under its handover's `FLAGS`.)*

`384.2` `ASSUMPTION` **· settled** — The manager's intent-line sentence goes beside "Where you minted the node, you write the condition", not under the four constraints. *(The worker's full text is under its handover's `FLAGS`.)*

`384.3` `ASSUMPTION` **· settled** — The exact wording of the intent-line sentences in node 386's condition is the worker's. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-10-04:* flags 384.1, 384.2, 384.3 settle at the node closing report that closes this node.
