# What `/to-spec` and `/to-tickets` put in a ticket that this workflow's nodes lack

Type: grilling
Status: claimed
Blocked by: none

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
