# Whether the rarely used node kinds and the cascade should stay

Type: grilling
Status: resolved
Supersedes: 87
Blocked by: none

## Answer

Research merges into precondition, prototype stays its own kind, and the never-wired cascade pass and its contract are removed; landed-code drift rides the workers' pre-handover searches.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. It surfaced [node 388](388-merge-research-into-precondition-and-remove-the-cascade-pass.md), implementation, blocked by 382 and 386, and [node 389](389-how-the-sweep-runs-now-that-the-cascades-machinery-is-gone.md), grilling. Node 87 is superseded by this node, as no longer needed. Flags 385.1, 385.2, 385.3, 385.4, 385.5 settle at the node closing report.

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

#### Questions 1 and 3 again, relayed 2026-10-04

*Pasted as the worker handed it back. The manager rebuilt the first two lines, the `NODE:` line and the `ABOUT:` label, which its extraction key cut; every other word is the worker's.*

`````
NODE:          Whether the rarely used node kinds and the cascade should stay
ABOUT:         This node decides whether research, precondition, prototype and the cascade pass each stay, merge into something else, or leave the shipped skills. You asked because some kinds are rarely used and you want the skills compacted.
SO FAR:        Settled by your reply: prototype stays as its own kind ("Q2 I think we should keep prototyping"). Precondition stays in every outcome, because adoption.md imports an existing corpus on precondition nodes. Two questions are still open: Q1 is the research decision, which you leaned to but were unsure about, and Q3 is the cascade, which you asked about. Below, each question first gives the explanation and then asks again. Counts were derived 2026-10-04 and are for scale only: 12 precondition nodes, 10 research nodes and 1 prototype node in about 385.
               Settled on my own authority: removing something from the shipped skills changes only the shipped files. This effort's record keeps its existing research nodes as they are.

Q1. Research and precondition
CONTEXT:       How to choose. Whichever you pick, what you see changes very little: both kinds run without you, and both reach you only when their premise is broken. The choice mostly affects the files and the manager.
               - Arguments for merging:
                 - One fewer contract to keep in step. At least six past nodes (109, 333, 343, 348, 350, 380) each had to make the same edit in all five worker contracts, and node 382 is about to be the seventh. The research contract is about 2,560 words, and three-quarters of its lines also appear in other contracts.
                 - The manager stops having to choose between two kinds it has treated as interchangeable. Gathering the manager's duties went to precondition (nodes 46 and 75). Finding where the skills restate themselves went to research (nodes 355 and 362). Both are the same kind of work.
               - Arguments for keeping research separate:
                 - "Research" is the clearer English word for "go and find out".
                 - Its contract is built entirely around reporting facts honestly. The three rules that matter would move into the precondition contract: say where each fact came from, report "could not establish" rather than guess, and mark your own inference separately.
                 - The precondition contract allows writing setup files. Research nodes would inherit that allowance, which is harmless.
               - What stays the same either way: a fact needed for one of your decisions is still found inside that grilling node, as now. Only a fact that stands on its own needs a node of either kind.
ASK:           Should research merge into precondition?
RECOMMENDED:   Merge, and keep the name `precondition`. The fact-reporting rules move into the precondition contract in about five lines, and the research contract is deleted. This is the kind of compaction you asked for. It removes no capability, only a duplicate contract and a choice the manager was making inconsistently. If "research" reads better to you, merge under that name instead. That is a naming choice, not a different design.
ALTERNATIVES:  Keep both kinds as they are: no compaction, and the manager keeps choosing between two kinds that do the same work.
               Merge under the name `research`: clearer for fact-finding, though it fits adoption's import nodes and setup chores less well.
               Merge research into grilling: a standalone fact would then wait on you with nothing for you to decide.

---

Q3. The cascade pass
CONTEXT:       Your questions, answered.
               - What it was meant to do. When a node is decided, earlier work can become stale, and the cascade was meant to find that and queue fixes without interrupting you. The original design (node 15) split this into three targets:
                 1. Decided nodes whose answer the new decision changes.
                 2. Open nodes whose question or acceptance condition the new decision changes.
                 3. Code that already landed and now disagrees with the new decision. In this effort, that means the shipped skill files.
               - Is it already done another way? Targets 1 and 2, yes. Target 3, partly.
                 - Target 1: every worker reports it in its handover's `INVALIDATIONS` part. Node 382, open and ready, adds a duty to search the decided nodes' answers and conditions before handing back.
                 - Target 2: every worker already searches the open nodes' conditions and questions before handing back (the `CONDITIONS` part). The manager then updates those nodes.
                 - Target 3 is the only part that needed a separate pass. Here is how it actually gets done today:
                   - The worker that makes a decision proposes the "carry this into the shipped files" implementation node itself.
                   - Later workers notice stale text while reading files for their own work. Nodes 304, 307, 242 and 198 were all found that way.
                   - The checker catches some of it.
                   - You catch it at gates. Node 87 came from your own question at a gate.
                   - Once node 382 lands, the deciding worker's search of decided implementation nodes' conditions also reaches the code they landed, because each condition describes its code.
               - Status: the per-target design was settled (node 15). The pass's worker contract shipped (node 44, .claude/skills/expedition-cascade/SKILL.md). But nothing tells the manager to start it: the manager's contract never mentions the cascade. The node that would add that trigger, node 87, has been open since about node 76. So the pass has never run.
               - When it would be used: if wired as designed, after every node is decided. The manager would start a cheap triage agent with the new answer and a list of every node that landed code. That agent picks the landed nodes worth a closer look, and its usual result is "none". Each pick then gets its own agent, which compares that code with the new answer and proposes fix nodes. The end-of-effort sweep would use the same machinery over every answer. That means one extra agent for every decided node, even when it finds nothing.
               - Where it would pay most: an effort with a lot of landed product code whose decisions keep changing after the code lands, such as Lang. That is the honest case for keeping it.
ASK:           Should the cascade pass and its contract be removed, with node 87 dropped as unnecessary?
RECOMMENDED:   Remove it. Delete .claude/skills/expedition-cascade/, mark node 87 superseded as no longer needed, and reword the glossary's `Cascade` and `Sweep` entries, since `Sweep` is defined as "the same work as a cascade". The deciding worker's search under node 382 then covers target 3, as a search inside a worker that already holds the context instead of an extra agent for every decided node. Grounds:
               - Targets 1 and 2 already have working routes.
               - Target 3 is caught today by the routes listed above.
               - Wiring the pass spends Claude credits on every node for a benefit nobody has measured, which ground rule 4 advises against.
               - Removal is reversible: the contract can be restored from commit c64a0e32c if a product effort shows drift that the workers' searches miss.
               The risk: a decision worded differently from an old condition will not match a text search, and on Lang that kind of miss is likelier than here.
ALTERNATIVES:  Keep it and wire it by working node 87: the designed mechanism runs, at one extra agent for every decided node.
               Keep the contract unwired until a product effort needs it: it costs nothing to run, but readers mistake the unwired contract for something the manager runs.
               Remove the pass but add one named step to every worker: search landed code by its commit trailer for what the decision changes. More precise than relying on conditions, but it adds a duty to every worker.

RETROSPECTIVE
1. What I had to hunt for:
   - The resolving worker's search for each Q3 point you asked about. I looked first at glossary.md's `Cascade` entry, then node 15's `## Answer`, and found the actual catchers by grepping who reported nodes 304, 307, 242, 198 and 87.
   - The retrospective name registry. Names are in two forms: kebab-case names in nodes 178, 212 and 243, and bold names in node 215. They were found only by extracting every retrospective section, including those pasted inside handovers in later nodes.
   - Standing item `nothing-pointed-me-at-it`. 1 earlier retrospective carries the name: 178.
2. What arrived that this node did not need: on this resume, nothing; the resume was short and all of it bore on the work. From the first spawn: most of decisions.md, read whole, of which about 10 lines bore on the work.
   - Standing item `read-and-unused`. 2 earlier retrospectives carry it: 141, 215.
3. What would have made this easier:
   - A spawn note naming node 87 and node 15's "never run" finding.
   - In the record, one list of the retrospective names, so that finding them takes one read instead of extracting every retrospective section. The rule says to search instead of keeping such a list, and this is what that search costs.
   - Standing item `nothing-pointed-me-at-it`. 1 earlier retrospective carries it: 178.
4. What was stale, wrong or contradictory:
   - The first spawn's note placed the kinds' definitions in SKILL.md `## Words used exactly`. The manager has acknowledged this. Standing item `unestablished inference`: 1 earlier retrospective carries it, 215.
   - Node 87's question says `cascade` appears twice in SKILL.md; it now appears 0 times. Standing item `stale-number-in-the-record`: 2 earlier retrospectives carry it, 178 and 212.
   - The glossary defines research as facts "from outside the working directory", but 6 of the 10 research nodes audited this repo's own text. Standing item `kind-definition-drifted-from-use`, a new name: 0 earlier retrospectives carry it.
   - This resume's claims checked out against node 385's `## Interview`: the reply is verbatim, the divergence is on Q2, and Q1 and Q3 are open.
`````

#### The human's answer to questions 1 and 3, 2026-10-05

`verbatim`: *"ok"*

*The manager's note:* the manager's message ended "Please answer Q1 and Q3. \"ok for recommended\" takes both.", so the reply takes both `RECOMMENDED` options as the worker wrote them. Q1: "Merge, and keep the name `precondition`. The fact-reporting rules move into the precondition contract in about five lines, and the research contract is deleted." Q3: "Remove it. Delete .claude/skills/expedition-cascade/, mark node 87 superseded as no longer needed, and reword the glossary's `Cascade` and `Sweep` entries, since `Sweep` is defined as \"the same work as a cascade\"." No divergence on either. Q2's divergence of 2026-10-04 stands: prototype stays its own kind.

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      Whether the rarely used node kinds and the cascade should stay
ANSWER:        ## Research merges into precondition, prototype stays, and the cascade pass is removed

The human decided each of the four in their interview, recorded under `## Interview`. The decisions are below.

### Research merges into precondition, and the name `precondition` is kept

Accepted 2026-10-05, `verbatim` *"ok"*, taking the recommendation as written.

- The research contract, `.claude/skills/expedition-research/`, is deleted.
- The precondition contract gains research's three rules for reporting facts:
  - say where each fact was read;
  - report a fact that could not be established as a result, never a plausible answer in its place;
  - mark what you infer separately from what a source states.
- The precondition contract also states that establishing a fact a later node needs is precondition work, and that its worker may read outside the working directory to do it.
- A fact that one decision needs is still found inside that grilling node, through the grilling worker's own reading or its own agents, as the grilling contract already says.

Grounds:
- In this effort the two kinds were used for the same shape of work: work done without the human that establishes facts a later node needs. Gathering the manager's duties (nodes 46 and 75) was filed as precondition. Finding where the skills restate themselves (nodes 355 and 362) was filed as research.
- Precondition's definition already covers fact-finding.
- Both contracts carry the same raise table.
- Each rule change to the worker contracts has had to be made identically in five files. At least six resolved nodes did so (109, 333, 343, 348, 350, 380). The merge makes it four.
- Routing work to cheaper models later is unaffected, because both kinds run without the human.

What is lost, and accepted: "research" as the plainer word for fact-finding.

### Prototype stays its own kind

The human's words, 2026-10-04, `verbatim`: *"Q2 I think we should keep prototyping"*. This diverges from the worker's recommendation to merge prototype into grilling. Prototype keeps its contract, its glossary entry and its `prototypes/NN-<name>/` location. The ground the recommendation set aside stands: product efforts such as Lang or a work project are likelier to need a probe than this one, which has used the kind once (node 8).

### Precondition stays

Precondition is the kind research merges into. adoption.md imports a corpus on precondition nodes.

### The cascade pass and its contract are removed

Accepted 2026-10-05, `verbatim` *"ok"*, taking the recommendation as written.

- `.claude/skills/expedition-cascade/` is deleted.
- The glossary's `Cascade` entry is removed, since no shipped file uses the term afterwards.
- The glossary's `Sweep` entry no longer defines the sweep by reference to the cascade.
- Node 87, which would have added the manager's trigger for the pass, is no longer needed.

What the cascade was for (node 15): when a node resolves, find what it made stale, and queue fixes without interrupting the human. Node 15 named three targets:
1. Resolved nodes whose answer the decision changes. These go to each worker's `INVALIDATIONS`, which node 382 turns into a search of the resolved nodes' `## Answer` and `## Acceptance condition` sections.
2. Open nodes' conditions and questions. Each worker's `CONDITIONS` search already covers these, shipped by nodes 263 and 350.
3. Landed code that departs from the decision. This was the only target that needed a separate spawned pass, and that pass is what is removed. It is caught by:
   - the deciding worker reporting the implementation node that carries its decision into the code;
   - later workers noticing stale text in files they read for their own work (nodes 198, 242, 304 and 307 were found that way);
   - the checker;
   - the human at a gate (node 87 itself came from a gate);
   - once node 382 lands, the deciding worker's search of resolved implementation nodes' conditions, each of which describes the code it landed.

Grounds:
- The pass has never run.
- The manager's contract never says to start it.
- Wiring it would start one agent at every resolution, spending scarce Claude credits on a result node 15 says is ordinarily empty.
- Ground rule 4 refuses machinery built for a need that has not been measured.
- Removal is reversible: commit `c64a0e32c` holds the contract.

The residual risk, accepted: a decision worded differently from an older condition does not match a text search. That miss is likelier on a product effort such as Lang than here.

What this leaves open: the sweep's method. Node 15 had specified it as the cascade's triage run over every resolved answer, and node 10's done test still requires a sweep. The shipped files never stated a method, so nothing shipped loses one. The question goes to a new node, reported with this handover.

### What changes, and what does not

- The shipped changes are one implementation node, reported with this handover.
- This effort's record keeps its existing `Type: research` nodes as they are.
- The effort's frontier script still lists any kind it finds in a node file, so those nodes still show.

INDEX LINE:    Research merges into precondition, prototype stays its own kind, and the never-wired cascade pass and its contract are removed; landed-code drift rides the workers' pre-handover searches.
FLAGS:         ASSUMPTION — The human's "removed from the shipped skill set" was read as reaching the shipped files only. This effort's own record keeps its ten `Type: research` nodes unchanged, because the record is never rewritten and those nodes record what happened. The frontier script lists an unknown kind after the known ones, so those nodes stay visible. — Index: Removing research changes only the shipped files; this effort's existing research nodes keep their `Type: research` line.
               ASSUMPTION — The accepted recommendation said to "reword the glossary's `Cascade` and `Sweep` entries". I read it as removing the `Cascade` entry whole and rewording `Sweep`. After the work no shipped file uses "cascade", and an entry defining a removed mechanism would describe something that does not exist. — Index: The glossary's Cascade entry is removed, not reworded, because no shipped file uses the term once the pass is gone.
               ASSUMPTION — Both shipped changes go into one implementation node, not two. They share glossary.md, and the map groups nodes by file. The node is blocked by 382 and 386, the two open nodes whose conditions edit the research contract and require all five worker contracts to stay identical. Landing after them keeps their conditions true. — Index: The research merge and the cascade removal are one implementation node, sequenced after nodes 382 and 386, which edit the same contracts.
               ASSUMPTION — Four details of the condition are my own choices:
                 - the frontier script's built-in list of kinds drops `research`;
                 - the precondition entry's `_Avoid_` line gains `research`, so the word does not drift back as a kind;
                 - the `Sweep` entry's `_Avoid_` line drops "full cascade";
                 - the exact new wording of the wayfinder-divergences bullet.
               Each follows from the decision, but the human did not see any of them. — Index: The merge's condition drops `research` from the frontier script's kind list, adds it to precondition's _Avoid_ line, and rewords the wayfinder bullet.
               ASSUMPTION — The sweep's method, left unspecified once the cascade goes, is reported as a new grilling node rather than settled here. The human was not asked about the sweep, and its method was never in the shipped files. — Index: How the sweep runs without the cascade's machinery goes to a new grilling node and is not settled at node 385.
NEW NODES:     1. Merge research into precondition and remove the cascade pass
                  Kind: implementation
                  Blockers: 382, 386 (both edit `.claude/skills/expedition-research/SKILL.md` and require the worker contracts to stay identical, so they land first).
                  Question: Carry node 385's answer into the shipped files. Merge the research kind into precondition, delete the research and cascade contracts, and update every shipped statement of the kinds and of the cascade.
                  Acceptance condition:
                  > The work is these eight paths, and no other file may be edited. These are files the workflow ships, so superseded wording is removed rather than struck, and nothing is moved to any history file.
                  >   `.claude/skills/expedition-research/SKILL.md` (deleted)
                  >   `.claude/skills/expedition-cascade/SKILL.md` (deleted)
                  >   `.claude/skills/expedition-precondition/SKILL.md`
                  >   `.claude/skills/expedition/SKILL.md`
                  >   `.claude/skills/expedition/glossary.md`
                  >   `.claude/skills/expedition/graph-conventions.md`
                  >   `.claude/skills/expedition/wayfinder-divergences.md`
                  >   `.claude/skills/expedition/scripts/frontier.sh`
                  >
                  > Scope came from searches over the tracked files outside `.scratch/`, run on 2026-10-05.
                  > - `git ls-files | grep -v '^\.scratch/' | xargs grep -l -i -E '\bresearch\b'` returned the research and cascade contracts, `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/adoption.md`, `.claude/skills/expedition/glossary.md`, `.claude/skills/expedition/graph-conventions.md` and `.claude/skills/expedition/scripts/frontier.sh`. The two matches in `adoption.md` ("research output") use the ordinary word, not the node kind. They are not instances and are not edited.
                  > - `git ls-files | grep -v '^\.scratch/' | xargs grep -l -i 'cascade'` returned the cascade contract and `.claude/skills/expedition/glossary.md`.
                  > - `grep -rn 'five kinds' $(git ls-files | grep -v '^\.scratch/')` returned only the glossary heading `## The five kinds of node`, so no other shipped file cites that heading.
                  > - `.claude/skills/expedition/wayfinder-divergences.md` came from no search. It is a named place: it states the kinds against wayfinder's.
                  > If any of these searches reaches a file outside the list when the work is done, report it and do not edit it.
                  >
                  > Done means every one of the following is true of the finished tree.
                  >
                  > 1. The directories `.claude/skills/expedition-research/` and `.claude/skills/expedition-cascade/` no longer exist.
                  > 2. In `.claude/skills/expedition-precondition/SKILL.md`, the paragraph beginning "Your node's kind is **precondition**" gains this last sentence, word for word: "Establishing a fact that a later node needs, from the working tree or from outside it, is such work, and you may read outside the working directory to do it."
                  > 3. In the same file, under `## Hard rules`, three rules are inserted immediately before the rule "Write your final output for the manager to consume. It is not a message to a person." They go in this order, with exactly these words:
                  >    - "Say where you read each fact you report."
                  >    - "When you could not establish a fact, report that as a result. Never give a plausible answer in its place."
                  >    - "Say what a source states, and mark separately what you infer from it."
                  >    The list then runs from 1 to 8 with no gap. Rules 1 to 4 keep their numbers and words. No other sentence of the file changes.
                  > 4. In `.claude/skills/expedition/SKILL.md`, under `## Spawning a worker`, the bullet beginning "- `research`:" is removed. The `precondition` bullet then reads exactly: "- `precondition`: what must be true when its work is finished, which of its results later nodes depend on, and, where its work establishes facts, the sources and their standing and that it may read outside the working directory." Line wrapping may differ; the words may not. Nothing else in the file changes.
                  > 5. In `.claude/skills/expedition/glossary.md`:
                  >    - (a) The heading `## The five kinds of node` becomes `## The four kinds of node`.
                  >    - (b) The `**research**:` entry is removed, with every line of it.
                  >    - (c) The `**precondition**:` entry's definition reads exactly: "Work that must happen before something else can be decided, including establishing a fact that a later node needs, from the working tree or from outside it. It does only that work: it decides nothing, probes nothing, and produces no product code." Its `_Avoid_` line keeps its three existing items in order and gains a fourth at the end: "research (a fact that a later node needs is precondition work, and a fact that one decision needs is found inside that grilling node)".
                  >    - (d) The `**Cascade**:` entry is removed, with every line of it.
                  >    - (e) The `**Sweep**:` entry's definition reads exactly "A pass that looks for revisions nobody propagated.", and its `_Avoid_` line reads exactly "_Avoid_: audit".
                  >    - (f) No other entry, heading or paragraph changes.
                  > 6. In `.claude/skills/expedition/graph-conventions.md`, the node-file template line `Type: grilling | research | prototype | precondition | implementation` becomes `Type: grilling | prototype | precondition | implementation`. The phrase "as with a `research` node or an AFK `precondition` node" becomes "as with an AFK `precondition` node". Nothing else in the file changes.
                  > 7. In `.claude/skills/expedition/wayfinder-divergences.md`, the bullet beginning "- **The fourth node type is `precondition`**" is replaced, with every line of it, by exactly: "- **`precondition` replaces wayfinder's `task` and also holds what wayfinder calls `research`.** `grilling` and `prototype` are unchanged, and `implementation` is added." Line wrapping may differ. The lead-in "Five differences" and every other line are unchanged.
                  > 8. In `.claude/skills/expedition/scripts/frontier.sh`, the line `type_order = "grilling research prototype precondition implementation"` becomes `type_order = "grilling prototype precondition implementation"`. Nothing else in the file changes. `sh .claude/skills/expedition/scripts/frontier.sh .scratch/graph-workflow` exits with status 0.
                  > 9. `git ls-files | grep -v '^\.scratch/' | xargs grep -n -i -E 'expedition-(research|cascade)|cascade|` + "`research`" + `'` returns nothing. That is: no tracked file outside `.scratch/` names either deleted contract, uses the word "cascade", or writes `research` as a code span.
                  > 10. No file under `.scratch/` changes.
                  > 11. The tree meets the bar.
                  (Read back against the five points: paths are relative; every demand is stated in the text; the material is copied in; nothing quantifies over the record; the scope's searches are stated with their returns beside the list, and an instance outside the list is reported, not edited. Clause 9's pattern, written plainly, is the extended regular expression `expedition-(research|cascade)|cascade|` followed by a backtick, the word research, and a backtick. The worker should quote it in single quotes so the backticks are literal.)

               2. How the sweep runs, now that the cascade's machinery is gone
                  Kind: grilling
                  Blockers: none
                  Question: Node 10's done test requires a whole-graph sweep that produces nothing new, and the glossary defines a sweep as a pass looking for revisions nobody propagated. Node 15 specified the sweep's method as the cascade's triage run over every resolved answer, fanning out per candidate. Node 385 removed the cascade pass, and the shipped files never stated the sweep's method. When an effort's frontier empties, what does the manager run as the sweep, and does that need a shipped procedure or only a sentence in the manager's contract? Candidates the asker should weigh: `expedition-triage` extended to resolved nodes; one agent per group of landed implementation nodes; the human's own reading at the effort closing report.
INVALIDATIONS: - Node 7 (Node type taxonomy): narrowed. The five kinds become four, research merging into precondition. Its prototype/implementation split and its grounds for keeping precondition stand.
               - Node 13 (Graph file format): narrowed. The type vocabulary goes from five values to four.
               - Node 14 (Naming): narrowed. Its annotation's "three of the five name a skill the worker invokes — `/grilling`, `/research`, `/prototype`" loses `/research`.
               - Node 22 (Write the worker contract skills): narrowed. Of its "six standalone skills, one per node kind plus the checker", the research one is gone.
               - Node 06 (Revision semantics): contradicted in part. "Fan-out is an aggressive AFK cascade" no longer describes a spawned pass. Propagation rides the workers' pre-handover searches, and its "queued graph edits rather than human interrupts" holds through those.
               - Node 15 (Cascade pass mechanics): its part 3 (the landed-code triage and per-candidate agents) is withdrawn, and its specification of the sweep as that machinery falls with it. Parts 1 and 2 stand.
               - Node 10 (Done-ness and termination): narrowed. The sweep is still required by the done test, but "the same machinery" no longer exists. Its method goes to the new grilling node.
               - Node 44 (Write the cascade pass's worker contract): the file it shipped is deleted.
               - Node 351: its change to the cascade contract goes with the file.
               - Node 290: the research contract it rewrote as the pilot is deleted. Its shared sections live on in the other contracts.
               - Node 335: the glossary's research entry it qualified is removed.
               - Node 102: extended by rename. Its rule for a research node's flags now applies to an AFK precondition node, which it already covered.
               - Node 372: its H1 was chosen to avoid the cascade's "triage" role name. The clash disappears, and nothing needs to change.
CONDITIONS:    Searched the open nodes' `## Acceptance condition` and `## Question` sections, claimed or not, for: `expedition-research`, `expedition-cascade`, `cascade`, `research` as a kind, `five kinds`, `Type: grilling | research`, `type_order`, `fourth node type`, `Sweep`, and the graph-conventions phrase "a `research` node".
               - 382 and 386 (open): their conditions list `.claude/skills/expedition-research/SKILL.md` and say `.claude/skills/expedition-cascade/SKILL.md` does not change. Both stay true, because the new implementation node is blocked by them and lands after. No replacement.
               - 41 (open, blocked by 170): its condition's file list includes `.claude/skills/expedition-research/SKILL.md`, which becomes wrong once the new node lands. I cannot write the replacement now, because no resolved node or landed work yet fixes its words. When the new node lands, the replacement is the same list without that path, fixed by that landed work. The manager amends it then, node 41 being unclaimed.
               - 32 (open, no condition): question changed. It names the flags.md clause in "five shipped contracts", the research contract among them. After the new node lands there are four, and the research link is dead.
               - 40 (open, no condition): question changed. It quotes graph-conventions' "a `research` node, an AFK `precondition` node", which after the new node reads "an AFK `precondition` node".
               - 87 (open): made unnecessary. The pass whose trigger it would write is removed. Supersede it, pointing at node 385.
               - 135 (open): matched only on another worker's words "a cascade obligation", ordinary usage. Unchanged.
               - 170 (open, no condition): no match. The manager's note that it edits the worker contracts is not borne out; it has no condition yet.
               - 384 and 387 (claimed): no match in their conditions or questions. 384's matches are in its interview and its handover, which minted node 386.
MISSING FROM MAP: none
RETROSPECTIVE
1. What I had to hunt for:
   - `nothing-pointed-me-at-it` — The shipped scope of the merge. Facts and where I found them:
     - the frontier script's built-in kind list, and the wayfinder-divergences bullet, which counts the kinds without saying "research";
     - that 32, 40 and 170 have no condition (from their section headings);
     - that 41's condition lists the research contract.
     I looked first at the spawn's list of nodes, then grepped all tracked files outside `.scratch/` and every open node. 1 earlier retrospective carries this name: 178.
2. What arrived that this node did not need:
   - `decisions-read-whole-for-a-few-lines` — new name; 0 earlier retrospectives carry it. On the first spawn, decisions.md was read whole and about 10 of its 300 lines bore on the work. The ones that mattered: 06, 07, 10, 13, 14, 15, 22, 44, 50, 102, 290, 335, 351, 372. A spawn scoping the index to the nodes on kinds and the cascade would have avoided it. Without labels, that means naming those nodes; the effort declares no label vocabulary.
   - On this resume nothing bore on nothing. The repeated retrospective instructions were needed, because the earlier form did not match derivation (j).
3. What would have made this node easier:
   - `record-is-not-mechanically-scannable` — On the first resume I extracted every retrospective section by hand to find the existing names. Derivation (j), named on this resume, makes it one run. Pointing at it from the first spawn would have saved that hunt. 4 earlier retrospectives carry this name: 178, 212, 220, 387.
4. What I read that was stale, wrong or contradictory:
   - `stale-number-in-the-record` — Node 87's question says `cascade` appears twice in `.claude/skills/expedition/SKILL.md`; it appears 0 times. 4 earlier retrospectives carry this name: 178, 212, 220 (one of these files holds two).
   - `unestablished-inference` — 0 earlier retrospectives carry it in the recognised form; node 215 used the phrase in bold. Two instances:
     - The first spawn placed the kinds' definitions in `.claude/skills/expedition/SKILL.md` under `## Words used exactly`. They are in glossary.md.
     - This resume says nodes 32, 40 and 170 "also edit the worker contracts". None of the three has a condition, 170's question has nothing to do with the worker contracts, and only 32's and 40's questions mention the research contract or a research node.
   - `kind-definition-drifted-from-use` — new name; 0 earlier retrospectives carry it. The glossary defines research as a fact "from outside the working directory", but 6 of the 10 research nodes audited this repo's own text.
`````

## Flags

`385.1` `ASSUMPTION` **· settled** — Removing research changes only the shipped files; the record keeps its `Type: research` nodes. *(The worker's full text is under its handover's `FLAGS`.)*

`385.2` `ASSUMPTION` **· settled** — The glossary's Cascade entry is removed, not reworded. *(The worker's full text is under its handover's `FLAGS`.)*

`385.3` `ASSUMPTION` **· settled** — The merge and the cascade removal are one implementation node, after 382 and 386. *(The worker's full text is under its handover's `FLAGS`.)*

`385.4` `ASSUMPTION` **· settled** — Four details of node 388's condition are the worker's own choices. *(The worker's full text is under its handover's `FLAGS`.)*

`385.5` `ASSUMPTION` **· settled** — The sweep's method goes to a new grilling node. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-10-05:* flags 385.1, 385.2, 385.3, 385.4, 385.5 settle at the node closing report that closes this node.
