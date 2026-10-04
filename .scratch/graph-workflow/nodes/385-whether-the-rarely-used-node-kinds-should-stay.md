# Whether the rarely used node kinds and the cascade should stay

Type: grilling
Status: claimed
Blocked by: none

## Question

*The human's own question, `verbatim`, 2026-10-04. **Minted by the manager and not surfaced by any worker.***

> Also I feel like a lot of node types are no really used right now (cascade, precondition, research) when are they used. Should some of them be removed (mostly research, I feel like you are mostly using grilling instead ?)

*The manager's note, with figures derived 2026-10-04 by counting `Type:` lines under `nodes/`. They are not authoritative and are for scale only: 232 implementation, 128 grilling, 12 precondition, 10 research and 1 prototype node. Of the 10 research nodes, 9 are resolved and one is out of scope, and the most recent is node 362. Node 130's worker did its web research inside a grilling node, through its own subagents, and minted no research node (flag 130.1). The cascade is a pass, not a node kind; whoever works this re-derives how often it has run.*

The answer decides, for each of research, precondition, prototype and the cascade, whether it stays, merges into another kind, or is removed from the shipped skill set, and on what ground. The human wants the skills compacted.

## Interview

#### Questions 1 to 3, relayed 2026-10-04

*Pasted as the worker handed it back.*

`````
NODE:          Whether the rarely used node kinds and the cascade should stay
ABOUT:         For each of research, precondition, prototype and the cascade pass, this node decides whether it stays, merges into another kind, or leaves the shipped skill set. The human asked because a few node kinds are rarely used and they want the skills compacted.
SO FAR:        I re-derived the facts on 2026-10-04. The counts below are for scale only and are not authoritative.
               - Usage by Type: line, matching the manager's figures: 232 implementation, 129 grilling (this node included), 12 precondition, 10 research, 1 prototype. The only prototype node is node 8, the relay protocol. It was early and it worked: two subagents were prototyped live.
               - What research nodes actually were: the glossary defines research as "a fact from outside the working directory". Only 4 of the 10 were outside facts (122, 128, 217 and 282, all harness or tool facts). The other 6 were audits of the repo's own text: 47 and 54 reviewed the skills against a writing standard, 52 measured token cost, 180 is out of scope, and 355 and 362 found where the skills restate themselves.
               - What precondition nodes were: mostly the same shape. 46 and 75 gathered the manager's duties, 328-330 grouped the open nodes, 341 drafted a condition, 313 and 324 built a search script. In practice the line between research and precondition is blurred: both are work done without the human that establishes facts a later node needs.
               - Research inside grilling is already the shipped rule. The grilling contract says "Find facts yourself... read it or dispatch an agent of your own". Node 130 did exactly that (flag 130.1). So a separate research node earns its place only when the fact stands alone, or feeds several nodes or an implementation node directly. 355→359 and 362→364 went straight from research to implementation with no decision in between. Grilling cannot absorb that case without spending the human's attention on a node that has nothing to decide.
               - How much the contracts overlap. Unique lines each contract shares with the grilling contract: research 137 of 187, precondition 158 of 220, prototype 179 of 219. Word counts: research 2,558, prototype 2,987, precondition 3,009, cascade 1,973. The whole shipped set is about 45,500 words. Node 50 kept the shared blocks duplicated because no worker reads more than one contract, so a single worker's read barely changes. The real cost is upkeep: at least six nodes (109, 333, 343, 348, 350, 380) each had to make the same edit in all five worker contracts, and node 382, still open, is a seventh.
               - The cascade has never run, and nothing tells the manager to run it. The manager contract (.claude/skills/expedition/SKILL.md) never mentions the word "cascade". Node 15 said the manager's contract would gain "when triage is spawned"; that never landed. The wiring is node 87, which has been open since node 76's gate. Its condition waits on a question to the human: which file the manager's duties go in. Once wired, the pass spawns one triage agent at every resolution, and node 15 says an empty result is the ordinary one. Node 15 also measured 28 propagations: none landed on code, and its own text says the pass covers one of the three ways this kind of miss arises. Node 382 is open and ready. It has every worker search the resolved nodes' `## Answer` and `## Acceptance condition` sections before handing back. A resolved implementation node's condition describes its landed code, so the resolving worker already reaches the landed nodes its decision changes, without a separate spawn.
               - Precondition stays in any outcome: adoption.md imports a corpus on precondition nodes.
               - The manager's consideration (one effort's usage may not show what a kind is for) holds. Q1 and Q2 therefore rest on overlap, not on usage counts: each merge keeps every capability and removes only a contract.
               Settled on my own authority: "removed from the shipped skill set" means changes to the shipped files only. This effort's record keeps its existing `Type: research` and `Type: prototype` nodes as they are.

Q1. Research and precondition
CONTEXT:       This is the human's main suspicion ("mostly research"). The usage above shows research has two real cases: a fact found inside a decision, which grilling already covers, and a fact that stands alone, which grilling cannot cover.
ASK:           Should research merge into precondition as one kind for work done without the human that establishes what a later node needs?
RECOMMENDED:   Merge research into precondition and keep the name `precondition`. Delete .claude/skills/expedition-research/. The precondition contract gains research's three method rules: say where each fact was read, report a fact you could not establish as a result, and mark what you infer separately from what a source states. Its spawn also says it may read outside the working directory. That is about five lines. Research facts found inside a decision stay in grilling, as they already do. Grounds: in this effort the two kinds were used for the same shape of work. Precondition's definition, "work that must happen before something else can be decided", already covers fact-finding. Both kinds share the same raise table. And it is one fewer contract for every future rule change. Routing work to a cheaper model later is unaffected, since both kinds run without the human.
ALTERNATIVES:  Keep both kinds as they are: no change and no compaction.
               Merge, but keep the name `research` for the merged kind: clearer English for fact-finding, but it fits adoption's import nodes and git-init-style chores badly.
               Merge research into grilling: this turns standalone fact-finding into a node that needs the human, and costs their attention for nothing to decide.
               Remove research and add nothing: standalone facts would have no home other than a grilling node with nothing to ask.

---

Q2. Prototype
CONTEXT:       It has been used once in about 385 nodes. Product efforts such as Lang or a work project, where a UI or API probe is useful, are likelier to need it than this one.
ASK:           Should prototype merge into grilling, keeping the ability to build a throwaway probe?
RECOMMENDED:   Merge it into grilling and delete .claude/skills/expedition-prototype/. The grilling contract gains a short paragraph: where the human can judge a built thing better than a question, build the cheapest probe in `prototypes/NN-<name>/`, outside the product tree and never product code, then ask what it changes. Its rule that the worker writes no file gains that one exception. Grounds: the prototype contract shares about 82% of its unique lines with grilling. Both kinds are a worker interviewing the human, and neither holds the code slot. The only differences are where the probe goes and building it first. The capability survives for product efforts, without a separate contract.
ALTERNATIVES:  Keep prototype as its own kind: the safest choice for future product efforts, at about 3,000 words of nearly duplicated contract.
               Remove prototype and add nothing to grilling: a grilling worker then has no sanctioned place to leave a probe the human can see between turns.

---

Q3. The cascade pass
CONTEXT:       The cascade is a pass, not a kind. It has a shipped contract (.claude/skills/expedition-cascade/SKILL.md) but no trigger, and node 87, which would add the trigger, is still open.
ASK:           Should the cascade pass and its contract be removed, with node 87 dropped as unnecessary?
RECOMMENDED:   Remove it. Delete .claude/skills/expedition-cascade/, mark node 87 superseded because the work it would do is no longer needed, and reword the glossary's `Cascade` and `Sweep` entries. `Sweep` is currently defined as "the same work as a cascade". The landed-code drift the pass was meant to catch goes to the resolving worker's search of the resolved nodes' answers and conditions (node 382). That search reaches every landed implementation node through its condition, at the cost of a grep inside a worker that already holds the context, instead of a spawn at every resolution. Grounds: it has never run; it is not wired; wiring it costs Claude credits on every node; the drift it targets is caught today by workers' searches, the checker, the gate and expedition-triage; and ground rule 4 refuses machinery built for a need nobody has measured. Removal is reversible, because commit c64a0e32c holds the contract. The honest risk: on Lang, decisions change code semantics more often than here, and a decision whose words do not match a condition's words will slip past a text search.
ALTERNATIVES:  Keep it and wire it by working node 87: this activates the designed mechanism at one spawn per resolution, with no evidence yet that it pays.
               Keep the contract unwired until a product effort shows the need: this ships dead text that readers take for live machinery, as the spawn's own notes did.
               Fold the pass's triage into the resolving worker's contract explicitly (a named search of landed code by commit trailer), on top of node 382: more precise than conditions alone, but it adds a duty to every worker.

RETROSPECTIVE
1. What I had to hunt for: the fact that the cascade is unwired. The manager contract never mentions it, and node 87 is open. I found it by grepping the shipped files and listing open nodes that mention "cascade". I also had to find where the kinds are actually defined, which is glossary.md `## The five kinds of node` and not SKILL.md.
2. What arrived that this node did not need: most of decisions.md. About 10 of its roughly 300 lines bore on this node (7, 15, 44, 50, 87 by way of 272, 130, 349/382, 372). The worktree, landing and map-restructure lines were all unused.
3. What would have made this easier: a spawn note naming node 87 (the cascade's missing manager-side wiring) and node 15's "it has never run" finding. Together they decide most of Q3.
4. What was stale, wrong or contradictory: the manager's note says the kinds and the cascade are defined in .claude/skills/expedition/SKILL.md `## Words used exactly`. That is wrong. That section defers to glossary.md, which defines the kinds and `Cascade`. SKILL.md mentions the kinds only under `## Spawning a worker` and never mentions the cascade. Node 87's question says `cascade` appears twice in SKILL.md, which is stale (it appears 0 times now). The glossary's research definition ("from outside the working directory") does not match 6 of the 10 research nodes, which audited this repo's own text.
`````

*The manager's note:* the worker is right that the manager's spawn placed the kinds' definitions in `SKILL.md`'s `## Words used exactly`; that section defers to `glossary.md`, which holds them.

#### The human's answer to questions 1 to 3, 2026-10-04

`verbatim`: *"Q2 I think we should keep prototyping Q3 what is the status of the cascade, what was it supposed to do, it is already done by anyther way ? When should it be used ? Q1 I think we could do that ? I am not sure what's better"*

*The manager's note:* **Q2 is a divergence.** It takes the alternative "Keep prototype as its own kind", not the `RECOMMENDED` merge. **Q3 is not answered.** The human asks four things back: what the cascade's status is, what it was meant to do, whether that is already done another way, and when it should be used. **Q1 is not settled.** The reply leans to the merge ("I think we could do that ?") and says it is unsure which is better. The manager does not take it as an "ok". All three go back to the worker holding the interview.
