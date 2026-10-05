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
