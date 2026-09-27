# Ship an `expedition-cleanup` skill

Type: implementation
Status: resolved

Blocked by: ~~338~~

## Question

*Surfaced by [Pruning a long-running effort's map](70-pruning-a-long-running-map.md)'s worker, and pasted as it
wrote it.*

> The human asked for cleanup to be an invoked skill on the model of `expedition-stop`, with two operations:
> removing a finished subject region the human names, and removing settled entries from the flag index. Ship it.

**Blockers, in the worker's words:** *"new node 1 above"* — which is [node
201](201-ship-the-cleanup-exemption-and-the-flag-check.md). Its ground is flag `70.5`: the settled-flag operation
makes the graph fail a mechanical check the same workflow ships, so the check is amended before the skill that
breaches it exists.

**The human's own words that fixed the shape**, `verbatim`, at node 70's interview:

> For the action of doing the cleanup I would see like the stop skill, a cleanup skill. For the cleanup skill, it is
> designed to delete things so it should be fine.

And, settling the second operation, `verbatim`: *"do cleanup flags"*.

## Acceptance condition

*Written by node 70's worker. Pasted as it wrote it, and not the manager's.*

> The work is a new skill under `.claude/skills/expedition-cleanup/`. Done means every one of the following is true
> of the finished tree.
>
> 1. A file `.claude/skills/expedition-cleanup/SKILL.md` exists, with the frontmatter shape the sibling
>    `expedition-*` skills use, and a description saying it is invoked in an expedition's manager thread to remove
>    record that a finished part of the effort no longer needs.
> 2. It states the standing rule it is an exception to, in its own words — that an edit to a file of the effort's
>    record never deletes, superseded text being marked and left where it is — and states that the rule guards
>    against removal that is unannounced, so an invoked act whose declared purpose is removal falls outside it.
> 3. It describes **two operations**, each given a distinct name, and states that each is invoked separately and
>    that neither implies the other.
> 4. For the first operation, removing a finished region, it states all of the following:
>    a. the region is named by the human in their own words, describing a part of the effort's subject matter whose
>       work is finished, and the skill never judges on its own that a region is finished;
>    b. the skill proposes the set of nodes it reads that naming to mean and presents that set for the human's
>       confirmation or amendment, and removes nothing before that confirmation;
>    c. three conditions the proposed set must meet, with the skill removing nothing from a set failing any of them:
>       every node in the set is resolved; nothing outside the set — no remaining node, and no other file of the
>       record — refers to any node in it; and the human has confirmed the set;
>    d. where a declared grouping field is present on nodes it may be used to propose the set faster, and that it is
>       never required, most efforts having few or none;
>    e. the operation reaches every file of the effort's record, removing the part of each attributable to the
>       region, and is not confined to the node files;
>    f. what is removed is each node's account of what happened, and what is left in its place is a single entry
>       naming the region as the human named it, the identifiers of the nodes removed, and the fact that the removed
>       text remains recoverable from the effort's version control history;
>    g. text stating a rule that currently binds is never removed by this operation, and the reason as a property:
>       such text is held in the effort's rule files rather than on a node, so it is not in a region to begin with.
> 5. For the second operation, removing settled flag entries, it states all of the following:
>    a. the effort's flag index carries one line per flag with its state, and the report built from it is the lines
>       not yet settled;
>    b. the operation removes the lines whose flag is settled and leaves the lines whose flag is outstanding;
>    c. nothing is lost, because a flag's prose and its settled marking both live on the node that raised it, and
>       the operation does not modify that node;
>    d. removing a settled line is not a mismatch against the mechanical check joining a node's flag entry to its
>       index line.
> 6. It states that the skill removes nothing on a criterion of age, of how long a file has grown, or of text having
>    been marked superseded — the two operations above are the whole of what it does.
> 7. **It assumes no particular repository, machine, or toolchain**, names no plugin, requires no skill to be
>    invocable, and names no command. Where it must refer to a commit, to version control, or to searching the
>    record, it states the property and not the command.
> 8. It addresses the manager throughout. Where an operation requires the human's confirmation it directs the
>    manager to obtain it, and it instructs no agent other than the manager to address the human.
> 9. It is at most 5,000 bytes.
> 10. No file outside `.claude/skills/expedition-cleanup/` is created or modified.
> 11. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This is the second file the workflow has not written yet to reach the frontier**, the other being [node
166](166-ship-an-expedition-stop-skill.md)'s stop skill, which the human named as this one's model and which is
still open. Under the priority order they approved, *the files the workflow has not written yet* is the only group
that moves toward the destination — so this node sits in that group rather than in the shipping backlog.

**Its clause 4(g) is what [node 189](189-where-the-never-delete-rule-stops.md) bought.** Before that node resolved,
a region's nodes could hold text stating a rule that bound the whole effort, and removing the region would have
taken it. Node 189's cut moved such text off the nodes and into the rule files, so the guarantee is structural
rather than a caution the skill has to enforce. Its author put it as *"closed by construction rather than by
care"*.

**Its clause 9's 5,000-byte cap is the author's own** and is not drawn from any rule of this effort's. The manager
records that it was chosen rather than derived, so a worker that finds it binding has somewhere to point.

*The manager's note, 2026-09-26:* node 201 was superseded by [node 338](338-say-in-graph-conventions-md-which-file-of-the-map.md), so this node's blocker is re-pointed to 338.

## Answer

`expedition-cleanup` ships two separately invoked operations. Region cleanup removes a human-named, confirmed set of resolved nodes that nothing refers to, and leaves a recoverable entry. Flag cleanup removes settled lines from `flags.md`.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `89135d3`. Flags 202.1 to 202.3 settle at the node closing report.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      Ship an `expedition-cleanup` skill

ANSWER:        A new skill at `.claude/skills/expedition-cleanup/SKILL.md`, 4,176 bytes. It is shaped like `expedition-stop` and `expedition-standing-yes`: frontmatter with `name:` and `description:`, a body written to the manager, and the siblings' wrap width, with every body line at 105 characters or fewer. Sections:
- `## The rule this skill is an exception to` gives the never-delete rule in the skill's own words. Its exception follows the wording node 338 put into `graph-conventions.md`: the rule guards against removal that is unannounced; an act that is invoked and whose declared purpose is removal is announced by being invoked; and such an act leaves an entry that names what was removed and says it can be recovered from version control. One sentence is added: remove only text that the effort's version control history already holds, so the entry's claim is true.
- `## Two operations` names the two operations **region cleanup** and **flag cleanup**. Each is invoked separately and neither implies the other. Where the invocation does not say which, the manager asks the human. Nothing is removed because it is old, because its file is long, or because it is marked superseded.
- `## Region cleanup`:
  - The human names the region. The manager never judges on its own that a region is finished.
  - The manager proposes the set of nodes and may use `Labels:` to do it faster. Labels are never required.
  - The set must meet three conditions: every node is resolved; nothing outside the set refers to any node in it; and the human has confirmed it.
  - A further stop: a node in the set that holds an outstanding flag blocks the removal until that flag is put to the human (flag 202.2).
  - The removal reaches every file of the record, and the node files are not the only ones.
  - One entry is written in `decisions.md` where the region's lines stood (flag 202.3). It carries the region's name, the ids of the removed nodes, and the fact that the text can be recovered.
  - Text stating a rule that binds is never in a region, because such text lives in the map's files.
- `## Flag cleanup` removes the `- [x]` lines from `flags.md`, leaves the `- [ ]` lines, and changes no node file. Nothing is lost, because the flag's prose and its `settled` marking stay on the node. A removed settled line is not a mismatch under the mechanical check that joins a node's flag entry to its index line.
- `## Reporting`: the manager tells the human what each operation removed.

The skill names no command, plugin or toolchain, and requires no skill to be invocable.

INDEX LINE:    `expedition-cleanup` ships two separately invoked operations. Region cleanup removes a human-named, confirmed set of resolved nodes that nothing refers to, and leaves a recoverable entry. Flag cleanup removes settled lines from `flags.md`.

FLAGS:
- ASSUMPTION 202.1: On node: Clause 4c says nothing outside the set, meaning "no other file of the record", may refer to any node in it. Clause 4e says the operation removes the region's part of every file. Read literally, the region's own lines in `decisions.md` and `flags.md` would count as "outside" references and would always block the removal. I wrote the condition as: nothing outside the set refers to any node in it, whether a remaining node or a part of another file of the record that this operation does not remove. This reading lets 4c and 4e both hold. Index: `expedition-cleanup` reads "nothing outside the set refers to it" as excluding the parts of other record files that the region cleanup itself removes, so that clauses 4c and 4e can both hold.
- ASSUMPTION 202.2: On node: A resolved node can still hold an outstanding flag, because flags settle at the pick report, and that report awaits no answer. Removing such a node's `flags.md` line would drop the flag from the closing report without anyone seeing it. So I added a stop beside the condition's three conditions, which are stated unchanged: a node in the set that holds an outstanding flag blocks the removal until that flag is put to the human. This adds to the condition and contradicts none of it. Index: `expedition-cleanup`'s region cleanup also stops on a node holding an outstanding flag, so that removing its line never drops the flag from the closing report.
- ASSUMPTION 202.3: On node: The condition does not say where the single left-behind entry goes. I placed it in `decisions.md`, where the region's index lines stood. That file is the record's index of what was decided, so a later reader who looks for the removed nodes looks there. Index: `expedition-cleanup` writes its one left-behind region entry in `decisions.md`, where the region's lines stood.

NEW NODES:     none

INVALIDATIONS: One narrowing. `graph-conventions.md` calls `flags.md` "Append-only", and its opening paragraph says a settled flag is marked rather than removed. Region cleanup and flag cleanup now remove lines from `flags.md`, and region cleanup removes lines from `decisions.md`. Both do it under the invoked-removal exception that node 338 already put into `graph-conventions.md`, so nothing is contradicted. The "Append-only" labels now stand subject to that exception. Node 70's answer is carried out as designed, with the refinements in flags 202.1 to 202.3.

CONDITIONS:    I searched every open or claimed node's `## Acceptance condition` for `expedition-cleanup`, `cleanup`, `clean-up`, `never-delete`, `never delete`, `region`, `settled flag` and `recoverable`. Matches outside node 202: 160, 190, 232, 221 and 80, which touch never-delete or file names only and are not affected. Node 88 (open) says: "The rule that flags.md is append-only and that a settled flag is checked rather than removed still holds after the work, stated wherever it is stated now." That clause binds only node 88's own work and stays true of it, so I wrote no replacement. Whoever claims node 88 should know that invoked flag cleanup now removes settled lines. No replacement clauses written.

MISSING FROM MAP: none. `graph-conventions.md` in the worktree gave the rest: the node-338 exception wording, check 6's settled-line clause, and the fact that `Labels:` is the declared grouping field.

GATE PAYLOAD:
- Checker findings: none yet, as no checker has run.
- Bar: the repo has no manifest, build, tests, formatter or CI. The worktree root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`, which matches `map-implementation-rules.md`. The bar is its non-command half: `/coding-principles`, `/naming`, `CONTEXT.md`'s `_Avoid_` lines, `graph-conventions.md`, `/writing-for-agents`, the ground rules, the five writing rules and the condition. `CONTEXT.md` refuses "finished", but only for the concept of a closed effort. The condition requires "finished" for a region, so I kept it. I avoided "item" and "index" as names for the map.
- Size: 4,176 bytes, under clause 9's 5,000.
- Paths touched: `.claude/skills/expedition-cleanup/SKILL.md` (new) in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/202-cleanup`. `git status --porcelain -uall` returns exactly `?? .claude/skills/expedition-cleanup/SKILL.md`. I stayed out of the files node 137 holds.
- Proposed commit message:
  ```
  Ship /expedition-cleanup: remove a finished region or settled flag lines from the record

  Node: graph-workflow/202
  ```

No method skill was invoked, so nothing of one was skipped.

RETROSPECTIVE
1. What I had to hunt for: two facts, both found by grepping the worktree's `graph-conventions.md`. The first was whether a "declared grouping field" exists under another name; it is `Labels:`. The second was where the closing report takes its flags from (`## Closing an effort` in `SKILL.md`). The node-338 wording was also in `graph-conventions.md`, near the top.
2. What arrived that this node did not need: most of `map.md` (about 42 KB), whose standing preferences on counts, payloads, token priority and resume bear nothing on this node; only the never-delete preference mattered. In `map-implementation-rules.md`, the record-as-work rule and the supersession paragraph did not apply. The decisions grep matched long struck lines, which I cut by width.
3. What would have made this easier: the spawn or the node naming where the single left-behind entry goes. The condition resolving the literal clash between 4c and 4e (flag 202.1). A note on resolved nodes that still hold unsettled flags (flag 202.2).
4. What was stale, wrong or contradictory: the node's question still says its blocker is node 201; only the manager's later note re-points it to 338. Clauses 4c and 4e conflict when read literally (flag 202.1). `graph-conventions.md` still labels `decisions.md` and `flags.md` "Append-only" with no pointer to the invoked-removal exception it states above.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 327's check; the condition reached it as a verbatim copy in `$TMPDIR/c202.md`.*

> PASS
>
> This is the check of node 202, "Ship an `expedition-cleanup` skill". The work is the new, untracked file `.claude/skills/expedition-cleanup/SKILL.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/202-cleanup`, on base eef448a. I read the condition in full from `/tmp/claude-1000/c202.md`, and the file in full with `cat -n`.
>
> - **Clause 1:** met. The frontmatter has only `name: expedition-cleanup` and `description:`, the same shape as `expedition-stop` and the other sibling skills. The description says "The human invokes it in an expedition's manager thread to remove record that a finished part of the effort no longer needs".
> - **Clause 2:** met. `## The rule this skill is an exception to` states: "An edit to a file of the effort's record never deletes. Superseded text is marked and left where it stands. That rule guards against removal that is unannounced. An act that is invoked and whose declared purpose is removal is announced by being invoked, so the rule does not reach it."
> - **Clause 3:** met. `## Two operations` names **region cleanup** and **flag cleanup**, and says "The human invokes each one separately, and neither implies the other."
> - **Clause 4, region cleanup:** met.
>   - 4a: the human names the region in their own words, and the file says "Never judge on your own that a region is finished."
>   - 4b: step 1 proposes the set. Step 4 has the manager "Put the set in front of the human for confirmation or amendment. Remove nothing before they confirm it."
>   - 4c: step 2 lists the three conditions: every node is `resolved`; nothing outside the set refers to any node in it, neither a remaining node nor another file of the record; and the human has confirmed. It says "you remove nothing from a set that fails any of them". Step 3 adds a further stop, an outstanding flag. The condition does not forbid a further stop, and none of the three is weakened.
>   - 4d: "Where the effort's nodes carry `Labels:`, you may use them to propose the set faster. Labels are never required, and most efforts declare few or none."
>   - 4e: step 5 says "Remove the region from every file of the effort's record, and not from the node files alone".
>   - 4f: the file says "What this removes is each node's account of what happened". Step 6 writes one entry that names the region as the human named it, lists the removed ids, and says the text remains recoverable from version control history.
>   - 4g: rule-stating text "is never removed by this operation. Such text is held in the map's files, which are the effort's rule files, rather than on a node. So it is never in a region to begin with."
> - **Clause 5, flag cleanup:** met.
>   - 5a: `flags.md` holds one line per flag with its state, and "The closing report is built from its lines whose flag is not yet settled."
>   - 5b: steps 1 and 2 remove the `- [x]` lines and leave the `- [ ]` lines.
>   - 5c: "Nothing is lost. A flag's prose and its `settled` marking both live on the node that raised it, and this operation does not modify that node."
>   - 5d: "A settled flag whose line has been removed is not a mismatch under the mechanical check that joins a node's `## Flags` entry to its line in `flags.md`."
> - **Clause 6:** met. "It removes no text because the text is old, because its file has grown long, or because the text is marked superseded", and "The two operations are the whole of what this skill does."
> - **Clause 7:** met. `grep -niE 'git|plugin|mattpocock|/home|grep|rm |`[a-z]+ -'` finds nothing. Version control is stated only as a property ("the effort's version control history"). No skill is required to be invocable.
> - **Clause 8:** met. The skill opens "You are the manager of an expedition" and addresses the manager throughout. Confirmation goes through the manager ("Put the set in front of the human…", "ask the human", "Report to the human"). No other agent is told to address the human.
> - **Clause 9:** met. `wc -c` gives 4176 bytes, which is 5,000 or less.
> - **Clause 10:** met. `git status --short --untracked-files=all` shows only `?? .claude/skills/expedition-cleanup/SKILL.md`, and `git diff --stat` is empty.
> - **Clause 11:** met. See the bar below.
>
> **The bar:**
> - The repo has no build, tests, formatter or CI, so there are no commands to run.
> - The new file has no trailing whitespace.
> - Its only line over 105 characters is the frontmatter description, at 227. The sibling `expedition-stop` description is also a single long line.
>
> **Standards:** as in my earlier checks, I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`.
> - These bore on the work:
>   - The `CONTEXT.md` `_Avoid_` lines: I checked by hand. "closing report" and "report" are the glossary's own terms, and no distinctive refused word appears.
>   - The writing rules: bold is used only where **region cleanup**, **flag cleanup** and **region** are defined. The prohibitions stand beside positives. Citations are by heading or quoted phrase.
>   - `/writing-for-agents`: the description front-loads its trigger. Nothing else found.
>   - The ground rules: nothing assumes a repo, machine or toolchain, and only the manager addresses the human.
>   - graph-conventions.md: the skill agrees with its never-delete exception and with check 6's settled-line clause.
> - `/coding-principles` and `/naming` did not bear on the work: it is prose, and its operation names are descriptive.
> - No reviewing skill is named, so I ran none.
>
> The condition records no search command.
>
> NOT COVERED:
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The condition does not demand this; the rules file makes it a bookkeeping rule. The worktree shows no such write, and what the main tree's record holds is outside what I was given.

### Gate — approve, `standing yes`, 2026-09-27

Taken under the standing yes recorded in `map.md`'s `## Notes` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and its one NOT COVERED item is the worker's bookkeeping. This settles none of the node's flags; they settle at the node closing report.

## Flags

`202.1` `ASSUMPTION` **· settled** — Clause 4c says nothing outside the set, meaning "no other file of the record", may refer to any node in it. Clause 4e says the operation removes the region's part of every file. Read literally, the region's own lines in `decisions.md` and `flags.md` would count as "outside" references and would always block the removal. I wrote the condition as: nothing outside the set refers to any node in it, whether a remaining node or a part of another file of the record that this operation does not remove. This reading lets 4c and 4e both hold. — `expedition-cleanup` reads "nothing outside the set refers to it" as excluding the parts of other record files that the region cleanup itself removes, so that clauses 4c and 4e can both hold.

`202.2` `ASSUMPTION` **· settled** — A resolved node can still hold an outstanding flag, because flags settle at the pick report, and that report awaits no answer. Removing such a node's `flags.md` line would drop the flag from the closing report without anyone seeing it. So I added a stop beside the condition's three conditions, which are stated unchanged: a node in the set that holds an outstanding flag blocks the removal until that flag is put to the human. This adds to the condition and contradicts none of it. — `expedition-cleanup`'s region cleanup also stops on a node holding an outstanding flag, so that removing its line never drops the flag from the closing report.

`202.3` `ASSUMPTION` **· settled** — The condition does not say where the single left-behind entry goes. I placed it in `decisions.md`, where the region's index lines stood. That file is the record's index of what was decided, so a later reader who looks for the removed nodes looks there. — `expedition-cleanup` writes its one left-behind region entry in `decisions.md`, where the region's lines stood.

*The manager's note, 2026-09-27:* flags 202.1 to 202.3 settle at the node closing report that closes this node, which names its gate as taken under the standing yes.
