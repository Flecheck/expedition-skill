# Merge research into precondition and remove the cascade pass

Type: implementation
Status: claimed
Blocked by: 382, 386

## Question

Carry node 385's answer into the shipped files. Merge the research kind into precondition, delete the research and cascade contracts, and update every shipped statement of the kinds and of the cascade.

*Reported by [node 385](385-whether-the-rarely-used-node-kinds-should-stay.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "382, 386 (both edit `.claude/skills/expedition-research/SKILL.md` and require the worker contracts to stay identical, so they land first)."*

## Acceptance condition

*Authored by node 385's worker and filed by the manager. The worker's note beside it, pasted: (Read back against the five points: paths are relative; every demand is stated in the text; the material is copied in; nothing quantifies over the record; the scope's searches are stated with their returns beside the list, and an instance outside the list is reported, not edited. Clause 9's pattern, written plainly, is the extended regular expression `expedition-(research|cascade)|cascade|` followed by a backtick, the word research, and a backtick. The worker should quote it in single quotes so the backticks are literal.)*

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

## Amendment, 2026-10-05 (the human's answer to raise 1)

*Clause 9 gains the exception the worker recommended and the human accepted, in the worker's words. The clause as filed stays above, unchanged.*

> 9. `git ls-files | grep -v '^\.scratch/' | xargs grep -n -i -E 'expedition-(research|cascade)|cascade|` + "`research`" + `'` returns nothing, except the line in `.claude/skills/expedition/wayfinder-divergences.md` that clause 7 requires.

## Interview

#### Raise 1, relayed 2026-10-05

*Pasted as the worker handed it back.*

`````
NODE:          Merge research into precondition and remove the cascade pass (388)
ABOUT:         This node merges the research kind into precondition and removes the cascade pass from the shipped workflow files. All the edits are made in the worktree. One clause cannot be met together with another, so the node is stopped before the checker.
SO FAR:        I read the implementation contract, node 388, map.md, map-implementation-rules.md and decisions.md's line for node 385. I re-ran the condition's three scope searches in the worktree (.scratch/graph-workflow/worktrees/388-merge-kinds, base 01919a8eb). They return exactly the files the condition lists, so nodes 382 and 386 moved nothing that matters here. adoption.md still matches only on the ordinary word "research output", which is not the node kind, so it is not edited.
               The worktree holds every edit that clauses 1 to 8 ask for, word for word:
               - Both contract directories are deleted. I staged the two deletions in the index, and nothing is committed. While the deletions were unstaged, `git ls-files` still listed the two files, so clause 9's command printed "No such file" errors.
               - The precondition contract has its added sentence and rules 5 to 7, with the old rule 5 now rule 8.
               - In SKILL.md the research bullet is removed and the precondition bullet is rewritten.
               - In the glossary: the heading now says four kinds, the research and Cascade entries are removed, the precondition definition is rewritten with a fourth _Avoid_ item, and the Sweep entry is trimmed.
               - graph-conventions.md has its two replacements. I did not rewrap the shortened line, because the clause says nothing else in the file changes.
               - wayfinder-divergences.md has its bullet replaced.
               - frontier.sh's type_order is changed. `sh .claude/skills/expedition/scripts/frontier.sh .scratch/graph-workflow` exits 0. No open or claimed node has `Type: research`, and the script already handles unknown types.
               - Nothing under .scratch/ is changed. The repo has no build, tests or formatter, as map-implementation-rules.md records. Its root has no CLAUDE.md, AGENTS.md or manifest, so there are no repo commands to confirm against.
               Clauses 7 and 9 contradict each other:
               - Clause 7 requires this exact text in wayfinder-divergences.md: "- **`precondition` replaces wayfinder's `task` and also holds what wayfinder calls `research`.** ...". It writes `research` as a code span.
               - Clause 9 requires that no tracked file outside .scratch/ writes `research` as a code span.
               With clause 7 done exactly, clause 9's command returns one line: `.claude/skills/expedition/wayfinder-divergences.md:38:- **`precondition` replaces wayfinder's `task` and also holds what wayfinder calls `research`.**`. No other line matches. This line is in a file the condition lists, so it is not an outside instance that I could just report. The condition cannot be met as written, and only the human can amend it (trigger 1, and the map's standing rule that such a contradiction is a raise). The worktree is exactly as described, and nothing has been reverted.
ASK:           The condition cannot hold both clause 7's exact text and clause 9's "no `research` code span". Which should change?
RECOMMENDED:   Keep clause 7's text and amend clause 9 to exclude that one line. For example, add: "except the line in `.claude/skills/expedition/wayfinder-divergences.md` that clause 7 requires". Clause 9 is meant to catch leftover uses of the removed node kind. The divergences bullet names wayfinder's own type, which still exists in wayfinder. The same bullet writes wayfinder's other types (`task`, `grilling`, `prototype`) as code spans, so plain text there would be the odd one out. No re-edit is needed. The work then meets every clause as amended.
ALTERNATIVES:  - Amend clause 7 to write "what wayfinder calls research" without backticks. Clause 9 then passes unchanged, but the bullet becomes inconsistent with how it writes wayfinder's other types.
               - Amend clause 9's pattern to drop the `research` code-span alternative altogether. This is broader than needed, and it loses the check on the removed kind everywhere else.

RETROSPECTIVE
1. What I had to hunt for: the item names, from derivations.md's (j) entry. I ran it by extracting the block, as the spawn directs. Nothing else needed hunting. The spawn gave me the paths, the condition and the decision line.
2. What arrived that this node did not need: most of map.md and map-implementation-rules.md. The contract requires reading them whole, but this node used only the bar's paragraph and the standards list.
   - `map-read-whole-for-a-few-items`: 8 earlier retrospectives carry it (nodes 135, 178, 205, 220, 284, 382, 386, 387).
   - `rules-file-read-whole-for-one-section`: 6 earlier retrospectives carry it (nodes 178, 220, 382, 386, 387).
3. What would have made this node easier: a self-check by the condition's author. Running the finished condition's own clause 9 against the text clause 7 dictates would have caught the contradiction before filing. The author's read-back covered the five points, which are about form. It did not cover whether the clauses can all be true together.
   - `condition-clauses-contradict-each-other`: newly minted; no earlier retrospective carries it.
4. What I read that was stale, wrong or contradicted something else: only the contradiction above, between clause 7 and clause 9. The manager's notes held: the scope searches still return the same files after nodes 382 and 386 landed.
`````

#### The human's answer to raise 1, 2026-10-05

`verbatim`: *"ok"*

*The manager's note:* the manager's message ended "Please answer node 388's raise. \"ok for recommended\" takes the exception in clause 9.", so the reply takes the worker's `RECOMMENDED`: "Keep clause 7's text and amend clause 9 to exclude that one line. For example, add: \"except the line in `.claude/skills/expedition/wayfinder-divergences.md` that clause 7 requires\"." No divergence. The amendment is filed below.

## Handover, attempt 1

*Pasted as the worker handed it back, 2026-10-05.*

`````
HANDOVER:      Merge research into precondition and remove the cascade pass (388)
ANSWER:        The research kind is merged into precondition. The research and cascade worker contracts are deleted, along with every shipped statement of them. The work was done against the condition as amended by the human's answer to raise 1 ("ok", on the recommended exception in clause 9).
               - `.claude/skills/expedition-research/` and `.claude/skills/expedition-cascade/` are deleted. Their deletions are staged in the index, and nothing else is staged. Without the staging, `git ls-files` would still list the two files and clause 9's command would print "No such file" errors.
               - `.claude/skills/expedition-precondition/SKILL.md`: the kind paragraph ends with "Establishing a fact that a later node needs, from the working tree or from outside it, is such work, and you may read outside the working directory to do it." Under `## Hard rules`, rules 5 to 7 are new: say where each fact was read; report a fact that could not be established as a result and never give a plausible answer in its place; mark what a source states separately from what is inferred from it. The old rule 5 is now rule 8. Rules 1 to 4 are unchanged.
               - `.claude/skills/expedition/SKILL.md`, `## Spawning a worker`: the `research` bullet is gone. The `precondition` bullet now adds "and, where its work establishes facts, the sources and their standing and that it may read outside the working directory".
               - `.claude/skills/expedition/glossary.md`:
                 - The heading now reads `## The four kinds of node`.
                 - The `research` and `Cascade` entries are removed.
                 - `precondition` covers establishing a fact a later node needs. Its `_Avoid_` line gains research, with the reason.
                 - `Sweep` is now "A pass that looks for revisions nobody propagated." with "_Avoid_: audit".
               - `.claude/skills/expedition/graph-conventions.md`: the template line now reads `Type: grilling | prototype | precondition | implementation`. The no-round example now reads "as with an AFK `precondition` node". I did not rewrap that now-shorter line, because the condition allows no other change to the file.
               - `.claude/skills/expedition/wayfinder-divergences.md`: the precondition bullet now says `precondition` replaces wayfinder's `task` and also holds what wayfinder calls `research`.
               - `.claude/skills/expedition/scripts/frontier.sh`: `type_order` drops research. A node that still carries `Type: research` is not rejected: the script already appends unknown types after the known ones. No open or claimed node carries it.
               Verified on the finished tree:
               - Clause 9's command returns only the wayfinder-divergences.md line that the amendment excepts.
               - `sh .claude/skills/expedition/scripts/frontier.sh .scratch/graph-workflow` exits 0.
               - Nothing under `.scratch/` changed.
               - The condition's three scope searches, re-run after nodes 382 and 386 landed, return the same files. `adoption.md` matches only the ordinary phrase "research output", which is not the node kind, so it is not edited.
               - The bar: the repo has no build, tests or formatter. Its root has no CLAUDE.md, AGENTS.md or manifest, so there are no repo commands. This matches map-implementation-rules.md's record, and the bar is its non-command half.
INDEX LINE:    Research merged into precondition and the research and cascade contracts deleted. The glossary, spawning bullets, node template, wayfinder divergences and frontier type order now name four kinds.
FLAGS:         none
NEW NODES:     none
INVALIDATIONS: This work carries out node 385's decision, so the resolved nodes it changes are the ones that decision already overrode. Now that it lands, they are contradicted in the shipped files:
               - 07 (node type taxonomy): there are four kinds, not five.
               - 13 (graph file format): the template line and the type vocabulary lose research.
               - 15 (cascade pass mechanics), 44 (cascade worker contract) and 351 (the cascade's per-candidate agent): their shipped product is deleted.
               - 290 (research contract as pilot) and 335 (the glossary's research entry): their shipped product is deleted.
               - 10 (done-ness): its sweep was defined through the cascade. The glossary's Sweep entry no longer says that, and node 389 (claimed) owns the method.
               - 292 (rewrite the precondition contract): extended by three hard rules and the fact-establishing sentence, with the rule list renumbered so its last rule is 8.
               Other resolved nodes landed edits inside the research or cascade contract as one of several contracts: 26, 35, 48, 75, 333, 380, 382, 386 among the matches. Those edits are narrowed: the copy in the deleted file is gone, and the copies in the remaining contracts stand.
CONDITIONS:    What I searched for:
               - The open nodes' `## Acceptance condition` and `## Question`, all 11 open or claimed nodes (counted 2026-10-05, for scale only, not authoritative), for: expedition-research, expedition-cascade, cascade, research (word and code span), "five kinds", "kinds of node", type_order, "fourth node type", "full cascade", "Sweep", "precondition`: what must", "Write your final output for the manager", "rule 5", wayfinder-divergences, frontier.sh, "may read outside the working directory", "research node".
               - The resolved nodes' `## Answer` and `## Acceptance condition` for the same terms.
               What matched, by node:
               - Node 41 (open, unclaimed): condition clause 7 lists `.claude/skills/expedition-research/SKILL.md` among "these five files", and that path is now deleted. Replacement for clause 7: "7. Each of these four files lists `FRICTION` among the markers its worker may use, and includes it in that file's `FLAGS:` handover line, with its meaning stated as a defect in the expedition workflow itself that this worker noticed while using it: `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md`". Its words are the clause's own minus that path. Its fixing is this node's landed work deleting the research contract. Node 385's worker reported the same, and the manager's 2026-10-05 note on node 41 already anticipates it.
               - Node 32 (open, no condition): its question names the clause in "five shipped contracts" with a research link. There are now four, and that link is dead. The term changed and the count narrowed. The manager's 2026-10-05 note already records this.
               - Node 40 (open): its question quotes graph-conventions' "a `research` node, an AFK `precondition` node". The text now reads "an AFK `precondition` node". The quoted text is renamed, and the manager's note already records this.
               - Node 389 (claimed grilling): its question presumes this node rewrites `Sweep` and removes `Cascade`. That is now true in the tree, and it calls node 388 "open, unclaimed", which is stale. Its premise is confirmed, not changed.
               No open node's condition cites the precondition contract's rule numbers, so the renumbering of its last rule from 5 to 8 breaks no citation.
MISSING FROM MAP: none
GATE PAYLOAD:  The checker has not run yet, so there are no findings to address.
               Paths touched (all in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/388-merge-kinds):
               - .claude/skills/expedition-research/SKILL.md (deleted, staged)
               - .claude/skills/expedition-cascade/SKILL.md (deleted, staged)
               - .claude/skills/expedition-precondition/SKILL.md
               - .claude/skills/expedition/SKILL.md
               - .claude/skills/expedition/glossary.md
               - .claude/skills/expedition/graph-conventions.md
               - .claude/skills/expedition/wayfinder-divergences.md
               - .claude/skills/expedition/scripts/frontier.sh
               Proposed commit message:
                 Merge research into precondition and remove the cascade pass

                 Delete the research and cascade worker contracts. Give the precondition
                 contract the fact-establishing work and three rules on reporting facts,
                 and bring the glossary, the spawning bullets, the node template, the
                 wayfinder divergences and the frontier's type order to four kinds.

                 Node: graph-workflow/388

RETROSPECTIVE
Covers only what is new since the raise:
1. What I had to hunt for: the open-node and resolved-node searches. A loose `Status: (open|claimed)` grep also matched nodes that quote a status inside their text, such as node 13, which is resolved. Anchoring the pattern to the whole line, `^Status: (open|claimed)$`, fixed it. I also took the commit trailer's form, `Node: graph-workflow/NN`, from the last commits rather than from any rule.
2. What arrived that this node did not need: nothing new.
3. What would have made this node easier: a derivation in derivations.md that lists the open and claimed nodes, with the anchored pattern. Every worker re-derives that list before its handover.
   - `open-node-list-re-derived-by-hand`: newly minted; no earlier retrospective carries it.
4. What I read that was stale, wrong or contradicted something else: node 389's question calls node 388 "open, unclaimed", which was stale by the time I read it.
   - `stale-number-in-the-record`: does not fit, because this is a stale status, not a stale number.
   - `stale-status-quoted-in-a-question`: newly minted; no earlier retrospective carries it.
`````
