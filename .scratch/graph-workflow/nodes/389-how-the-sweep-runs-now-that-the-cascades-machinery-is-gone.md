# How the sweep runs, now that the cascade's machinery is gone

Type: grilling
Status: resolved
Blocked by: none

## Answer

The sweep at an empty frontier is every mechanical check run over the whole graph by one read-only agent, with each failure becoming a node; no agent re-checks landed code.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. It surfaced [node 390](390-state-the-sweep-as-a-whole-graph-run-of-the-mechanical-checks.md), implementation. Flags 389.1, 389.2 settle at the node closing report.

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

#### The human's answer to question 1, 2026-10-05

`verbatim`: *"ok"*

*The manager's note:* the manager's message ended "Please answer node 389's question. \"ok for recommended\" takes the mechanical checks only.", so the reply takes the worker's `RECOMMENDED`: "Just the mechanical checks, written as a few sentences in SKILL.md's `## Closing an effort`, with no new procedure or skill." No divergence.

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      How the sweep runs, now that the cascade's machinery is gone

ANSWER:        Accepted 2026-10-05, `verbatim` "ok", taking the recommendation as written.

               ### The sweep is the mechanical checks, run over the whole graph

               When an effort's frontier empties, the sweep is a run of every check under `## Mechanical checks` in `graph-conventions.md` over the whole graph. The manager gives that run to one read-only agent, which reports only the failures. Each failure becomes a node. When the frontier empties again, the sweep runs again, and every round still goes into the effort closing report.

               The sweep spawns no agent to re-check landed code. Code that no longer matches a later decision is left to:
               - the search each worker makes of the resolved nodes before it hands back (node 382);
               - the checker;
               - the gate;
               - the human's reading at the closing report.

               That is the residual risk node 10 already named: a semantic miss in code that builds cleanly.

               ### Where it is written

               A few sentences in the manager's contract, `SKILL.md`, under `## Closing an effort`. There is no new procedure and no new skill. In `graph-conventions.md`, `### Who runs a check, and when` says "no separately spawned agent runs any of them". That sentence gains an exception for the sweep's run.

               ### Grounds

               - Re-checking old acceptance conditions against the final tree would mostly find text that later decisions changed on purpose. Telling those changes apart from real drift needs the whole record, which is the context cost that pushed node 15 to fan out.
               - The sweep runs only on efforts that end. Node 15's note 3 says that on a non-terminating effort such as Lang it never fires.
               - Ground rule 4 refuses machinery for a need nobody has measured, and no effort has yet reached an empty frontier. If a sweep later misses real drift, a semantic pass can be added then.
               - Giving the run to one agent keeps the manager's own context from reading every node file. The map names that context as what runs out first.

               ### Set aside

               - One read-only agent per group of landed implementation nodes.
               - `expedition-triage` extended to resolved nodes and run as the sweep. That would also break triage's rule that only the human invokes it.
               - The manager running the checks itself.
               - The human's reading alone, with the done test's third condition dropped.

INDEX LINE:    The sweep at an empty frontier is every mechanical check run over the whole graph by one read-only agent, with each failure becoming a node; no agent re-checks landed code.

FLAGS:         ASSUMPTION — The human accepted the SKILL.md wording I proposed. The wording for the exception in graph-conventions.md's `### Who runs a check, and when` is mine. I wrote it to say only that the sweep is the exception, and to point at `## Closing an effort` for who runs the sweep, under writing rule 6. — Index: The graph-conventions.md wording that makes the sweep the one exception to "no separately spawned agent" was written by node 389's worker, not by the human.
               ASSUMPTION — I leave the glossary's `Sweep` entry as node 388's clause (e) writes it, "A pass that looks for revisions nobody propagated.", and mint no edit to it. A run of the mechanical checks finds a kind of unpropagated revision, such as a node still blocked by a superseded node, so the definition stays true though loose. Node 388 is claimed, and its condition stays as written. — Index: The glossary's Sweep entry is left as node 388 writes it, being loose but still true of a mechanical-check sweep.

NEW NODES:     Name: State the sweep as a whole-graph run of the mechanical checks
               Kind: implementation
               Question: Carry node 389's answer into the shipped files. The manager's contract says what the sweep is and who runs it, and graph-conventions.md makes the sweep the one exception to its rule that no separately spawned agent runs a check.
               Blockers: none. Note for the manager's slot filter: node 388 (claimed) edits both files in other sections, and node 317 (open, no condition) concerns the flags bullet of the same `## Closing an effort` section.
               Acceptance condition:
               > The work is these two paths, and no other file may be edited. These are files the workflow ships, so superseded wording is removed rather than struck, and nothing is moved to any history file.
               >   `.claude/skills/expedition/SKILL.md`
               >   `.claude/skills/expedition/graph-conventions.md`
               >
               > The scope came from no search: these two places are the work, not instances of a defect.
               >
               > Done means every one of the following is true of the finished tree.
               >
               > 1. In `.claude/skills/expedition/SKILL.md`, the section `## Closing an effort` ends with its bulleted list, whose last bullet is "- What the sweep found, and every sweep round." Immediately after that list, still inside the section, there is a new paragraph with exactly these words: "The sweep is a run of every check under `## Mechanical checks` in `graph-conventions.md` over the whole graph. Give the run to one read-only agent, which reports only the failures. Each failure becomes a node. When the frontier empties again, the sweep runs again." Line wrapping may differ, but the words may not. Nothing else in the file changes.
               > 2. In `.claude/skills/expedition/graph-conventions.md`, under `### Who runs a check, and when`, these two sentences: "No schedule, no periodic pass and no separately spawned agent runs any of them. One run is not tied to an act: a run of every check over the whole graph, which remains available at an empty frontier." are replaced by exactly: "No schedule, no periodic pass and no separately spawned agent runs any of them, with one exception. The sweep runs every check over the whole graph at an empty frontier, and `## Closing an effort` in `SKILL.md` says who runs it." Line wrapping may differ, but the words may not. Nothing else in the file changes.
               > 3. No file under `.scratch/` changes.
               > 4. The tree meets the bar.
               Read back against the five points: the paths are relative; every demand is stated in the text; the old and new words are copied in; nothing quantifies over the record; and the scope is stated as coming from no search. Over the tracked files outside `.scratch/`, `grep -i 'separately spawned\|whole graph\|whole-graph'` returned only SKILL.md (the "triggers the whole-graph sweep" line, which stays) and the graph-conventions.md sentence above.

INVALIDATIONS: - Node 10 (Done-ness and termination): narrowed. Condition 3 of the done test stands, and the sweep is now the whole-graph run of the mechanical checks. Node 10 listed "resolved nodes whose code no longer matches" and "coupling the graph never recorded" under "What the sweep found". The sweep no longer looks for those, which fall to the backstops node 10 already named. Its section "The final sweep" ("the cascade agent run with the whole graph as its scope") and its annotation "the sweep now has a shape" no longer describe the method.
               - Node 15 (Cascade pass mechanics): its specification of the sweep as triage over every resolved answer, already withdrawn by node 385, is replaced by this answer.
               - Node 385: extended. The open part it handed on, the sweep's method, is answered here.

CONDITIONS:    I searched the `## Acceptance condition` and `## Question` sections of the open and claimed nodes for: `sweep`, `Mechanical checks`, `Who runs a check`, `separately spawned agent`, `Closing an effort`, `empty frontier` and `whole graph`.
               Matches:
               - Node 388 (claimed): clause 5(e) sets the `Sweep` entry. It stays valid, and I write no replacement, since a claimed node's condition stays as written in any case.
               - Node 317 (open, no condition): its question concerns the flags bullet under `## Closing an effort`. Its question is unchanged, and the two pieces of work only share a section.
               - Node 13 also matched, but it is resolved; its `Status` line matched a later line of the file.
               - Node 389 matched itself.
               Node 41 (open) edits graph-conventions.md's flag markers, a different concern, so I joined nothing to it. No unclaimed node's clause is made wrong, and no replacement is written.

MISSING FROM MAP: none

RETROSPECTIVE

The item names and counts below come from running derivations.md entry (j) on 2026-10-05. They are not authoritative and are for scale only.

1. What I had to hunt for:
   - Who may run the whole-graph check. I found it in graph-conventions.md under `### Who runs a check, and when`, after first searching SKILL.md for "sweep".
   - Whether the human had raised Claude credits at node 385. I found the human's own words in node 385's `## Interview` (they had not), and the human's credits quote in map.md's Notes.
   - `nothing-pointed-me-at-it`: 3 earlier retrospectives carry it (nodes 135, 178, 385). Neither the spawn nor the node named graph-conventions.md's `## Mechanical checks` or its exception sentence, which were the existing pieces this decision is built on.
2. What arrived that the node did not need:
   - `map-read-whole-for-a-few-items`: 9 earlier retrospectives carry it (nodes 135, 178, 205, 220, 284, 382, 386, 387, 388). Of map.md I used ground rule 4, the credits note, the expectation line, and writing rules 5 and 6. Most of the standing preferences bore on nothing.
   - The retrospective bullet in map-manager-only.md is a single paragraph of about 900 words. I went to it for the four questions and the naming form. The spawn already paraphrased both, so a pointer to derivations (j) alone would have served.
3. What would have made this node easier: the spawn naming `## Mechanical checks`, `### Who runs a check, and when`, and expedition-triage's scope as the candidate building blocks, beside the three candidates it listed.
4. What I read that was stale, wrong, or contradicted something else:
   - `unestablished-inference`: 1 earlier retrospective carries it (node 385). The manager's note said "The human raised Claude credits as a cost when asking about the cascade". The node 385 worker raised that cost, not the human.
   - The glossary's `Sweep` entry still defines the sweep as "the same work as a cascade" until node 388 lands.
   - Node 10's "The final sweep" section and its annotation describe a method that no longer exists.
   - The first spawn said node 388 was open; it is claimed.

Skipped from the method skills: nothing invoked.
`````

## Flags

`389.1` `ASSUMPTION` **· settled** — The graph-conventions.md exception wording is the worker's, not the human's. *(The worker's full text is under its handover's `FLAGS`.)*

`389.2` `ASSUMPTION` **· settled** — The glossary's Sweep entry is left as node 388 writes it. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-10-05:* flags 389.1, 389.2 settle at the node closing report that closes this node.
