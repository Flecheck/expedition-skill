# How the sweep runs, now that the cascade's machinery is gone

Type: grilling
Status: claimed
Blocked by: none

## Question

Node 10's done test requires a whole-graph sweep that produces nothing new, and the glossary defines a sweep as a pass looking for revisions nobody propagated. Node 15 specified the sweep's method as the cascade's triage run over every resolved answer, fanning out per candidate. Node 385 removed the cascade pass, and the shipped files never stated the sweep's method. When an effort's frontier empties, what does the manager run as the sweep, and does that need a shipped procedure or only a sentence in the manager's contract? Candidates the asker should weigh: `expedition-triage` extended to resolved nodes; one agent per group of landed implementation nodes; the human's own reading at the effort closing report.

*Reported by [node 385](385-whether-the-rarely-used-node-kinds-should-stay.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none"*

## Interview

#### Question 1, relayed 2026-10-05

*Pasted as the worker handed it back.*

`````
NODE:          How the sweep runs, now that the cascade's machinery is gone (node 389, grilling)
ABOUT:         The done test (node 10) still requires "a whole-graph sweep that produces nothing new". The only method the sweep ever had was node 15's cascade machinery, which node 385 removed. This node decides what the manager runs as the sweep when an effort's frontier empties, and where that is written.
SO FAR:        What the shipped files say about the sweep today:
               - The manager's contract, .claude/skills/expedition/SKILL.md, has three lines on it. "A sweep runs only on an empty frontier." An empty frontier "triggers the whole-graph sweep and the effort closing report". The closing report carries "What the sweep found, and every sweep round." No shipped file says how a sweep is done.
               - graph-conventions.md, under `## Mechanical checks`, lists 11 checks that can be decided by reading the files: dangling `Blocked by:` edges, mismatched supersession pairs, reused ids, flag and index agreement, and so on. Under `### Who runs a check, and when` it says that each check runs at the act that could make it false, that "no schedule, no periodic pass and no separately spawned agent runs any of them", and that "a run of every check over the whole graph … remains available at an empty frontier". No script runs these checks; scripts/ holds only frontier.sh.
               - expedition-triage covers open nodes and outstanding flags only. It runs only when the human invokes it ("Run none of it on a schedule or on your own judgement").
               - Node 388 (open, unclaimed) will rewrite the glossary's `Sweep` entry to "A pass that looks for revisions nobody propagated." and remove `Cascade`.

               What node 10 expected the sweep to find: dangling edges, resolved nodes whose code no longer matches, and coupling the graph never recorded. Node 10 also refused an audit agent for missed propagation. It named a semantic miss in code that builds cleanly as an accepted residual risk, with the bar, the mechanical check and the human's own reading of the changes as the backstops. Node 15's note 3 adds that the sweep never runs on a non-terminating effort such as Lang, so it was never the safety net for drift. Since node 385, that drift is caught by the workers' search of the resolved nodes before a handover (node 382, claimed), by the checker, at the gate, and by triage.

               Settled on my own authority: the code-checking part is the only part that costs agents. A rule that checks the graph's files costs nothing beyond running the 11 checks.

               A correction to the manager's notes: in node 385 the cost in Claude credits was raised by that node's worker, not the human. The human asked only what the cascade was for and whether it was still used. The human's own words on credits are in map.md's Notes ("I have a limited amount of claude credits …"). The ground still stands.
ASK:           When the frontier empties, should the sweep be just the 11 mechanical checks run over the whole graph, or should it also have agents re-check the code that landed?
RECOMMENDED:   Just the mechanical checks, written as a few sentences in SKILL.md's `## Closing an effort`, with no new procedure or skill. Proposed wording: "The sweep is a run of every check under `## Mechanical checks` in graph-conventions.md over the whole graph. Give the run to one read-only agent, which reports only the failures. Each failure becomes a node. When the frontier empties again, the sweep runs again." The words "no separately spawned agent" under `### Who runs a check, and when` would gain an exception for this one run. That costs at most one cheap agent per sweep round, and the manager does not have to read every node file into its own context. Code that no longer matches its decision stays with the searches before each handover (node 382), the checker, the gate, and the human's reading at the closing report. That is the residual risk node 10 already named.
               Why:
               - Re-checking old acceptance conditions against the final tree would mostly find text that later decisions changed on purpose. Telling those apart from real drift needs the whole record, which is the context cost that pushed node 15 to fan out.
               - The check would run only on efforts that end, and those are not the efforts where drift matters most.
               - Ground rule 4 refuses machinery for a need nobody has measured, and no effort has reached an empty frontier yet. If a sweep later misses real drift, a semantic pass can be added then.
ALTERNATIVES:  - Also re-check each landed implementation node's acceptance condition against the current tree, with one read-only agent per group of landed nodes that share files (the cascade's fan-out without its trigger). Cost grows with the number of landed nodes, and most of what it finds would be intended changes.
               - Extend expedition-triage to the resolved implementation nodes and run it as the sweep. It is the same check with the same noise, and triage would lose its rule that only the human invokes it.
               - The manager runs the checks itself with no agent, leaving "no separately spawned agent" as it is. This spends the manager's context, which the map names as what runs out first, on reading every node file.
               - The human's reading at the closing report alone, with no mechanical run, and the done test's third condition dropped. The checks already run at every act, so a whole-graph run would usually find nothing. This is the cheapest option, but it removes a backstop that costs very little.

RETROSPECTIVE (provisional; this is a question payload, and the full retrospective comes with the handover):
1. What I had to hunt for: who runs the whole-graph mechanical check. I found it in graph-conventions.md, `### Who runs a check, and when`, after first searching SKILL.md for "sweep". I also had to find whether the human raised the credit cost. It is in node 385's `## Interview` (no), and map.md's Notes holds the human's actual credits quote.
2. What arrived that the node did not need: most of map.md's standing preferences.
3. What would have made the node easier: the spawn naming `## Mechanical checks` and expedition-triage as the existing pieces.
4. What was stale or wrong: the manager's note that "The human raised Claude credits as a cost when asking about the cascade" is wrong, because the 385 worker raised it. The glossary's `Sweep` entry still defines the sweep through the cascade until node 388 lands. I did not yet run derivations.md entry (j) for the item names; I will before the handover.
`````

*The manager's note:* the worker is right. The manager's spawn note said the human raised Claude credits as a cost when asking about the cascade. It was node 385's worker that raised it. The human's own words on credits are in map.md's Notes.
