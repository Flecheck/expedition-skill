# Merge research into precondition and remove the cascade pass

Type: implementation
Status: open
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
