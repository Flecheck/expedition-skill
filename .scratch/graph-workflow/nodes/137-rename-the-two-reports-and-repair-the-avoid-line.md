# Rename the two reports and repair the `_Avoid_` line that reserved the word

Type: implementation
Status: resolved

Blocked by: none

## Question

*Surfaced by [`CONTEXT.md` reserves the word `report` to the closing
report](107-context-reserves-the-word-report.md)'s worker, and pasted as it wrote it.*

> `CONTEXT.md` and three shipped files name the manager's per-node message `pick report` and its per-effort message
> `closing report`, and `CONTEXT.md`'s `Handover` entry refuses the word `report` on the false ground that one term
> owns it. Carry the settled pair — **effort closing report** and **node closing report**, with the unqualified form
> meaning the node one — into all four files, and repair the refusal's stated ground.

**Blockers, in the worker's words:** *"none. It shares `.claude/skills/expedition/SKILL.md` with node 133, which is
live in a worktree and holds the code slot; that is a sequencing matter for the manager rather than an edge."*

## Acceptance condition

*Written by node 107's worker. Pasted as it wrote it, and not the manager's.*

> The four files, and no others: `CONTEXT.md`; `.claude/skills/expedition/SKILL.md`;
> `.claude/skills/expedition/graph-conventions.md`; `.claude/skills/expedition-precondition/SKILL.md`.
>
> 1. **Two named reports exist in the vocabulary, defined as follows.** An **effort closing report** is what the
>    manager hands the human once the frontier empties: what was decided, what landed, and every flag still
>    outstanding. It happens once per effort. A **node closing report** is the message the manager sends the instant a
>    node closes, naming the node that closed, carrying in full every flag that node holds — it being where those
>    flags settle — and naming whatever work the manager started in response; it awaits no answer and takes no place
>    in the human's question queue. An **unqualified `closing report` means the node-level one.**
> 2. `CONTEXT.md`'s entry headed `**Closing report**:` is renamed to `**Effort closing report**:`. Its meaning is
>    unchanged and its `_Avoid_: completion report, summary` is kept.
> 3. `CONTEXT.md` gains an entry for the node-level report under its `## Talking to the human` heading, defining it
>    as clause 1 does.
> 4. One of those two entries states that an unqualified "closing report" means the node-level report, and that prose
>    written before this change uses it for the effort-level one. Wording is the worker's; both halves must be
>    present.
> 5. `CONTEXT.md`'s `**Handover**:` entry ends today with `_Avoid_: report (the closing report owns that word),
>    return, payload, deliverable`. After the work that line still refuses all four words, and its parenthetical no
>    longer asserts that any one term exclusively owns the word "report". It states instead that a report goes to the
>    human and a handover goes to the manager. Wording is the worker's; the recommended form is `_Avoid_: report (a
>    report goes to the human; a handover goes to the manager), return, payload, deliverable`.
> 6. **The term `pick report` appears nowhere in the four files.** Each occurrence becomes the node-level term, bare
>    or `node`-prefixed as its sentence needs. *Recorded enumerator:* `grep -rn "pick report" --include=*.md .claude/
>    CONTEXT.md`, which returned **14** occurrences at commit `106380a` — 8 in `expedition/SKILL.md`, 3 in
>    `graph-conventions.md`, 2 in `CONTEXT.md`, 1 in `expedition-precondition/SKILL.md`. Re-run it; the demand is
>    that it return nothing, whatever the count has become.
> 7. **Every use of `closing report` that means the effort-level report carries the `effort` prefix**, the bare form
>    now meaning the other one. *Recorded enumerator:* `grep -rni "closing report" --include=*.md .claude/
>    CONTEXT.md`, which returned **7** occurrences at commit `106380a`, of which clause 2 renames one (the entry
>    heading) and clause 5 rewrites one (the `Handover` `_Avoid_` line), leaving **5** to take the prefix. Re-run it
>    and judge each remaining occurrence by which report it means.
> 8. `expedition/SKILL.md` today reads *"Say in the report accompanying the pick that it is yours, and in a line or
>    two what it demands."* That periphrasis names the same message as clause 1's node-level term and is replaced by
>    that term.
> 9. No rule in any of the four files is removed or renumbered, and none other than the ones clauses 2–8 name changes
>    its meaning. In particular the prohibition in clause 5's `_Avoid_` line still refuses all four of its words.
> 10. The working tree meets the bar.
>
> *Written by node 107's worker, which found the work and phrased it. Read back against the two rules binding every
> condition: it is **self-contained**, every demand being in its own words with the two sentences it changes quoted
> and the enumerators written out, so its reader goes nowhere else; and it **does not quantify over the record**,
> every clause being answerable from the four files and the diff.*

## The manager's note at filing

*Not a change to anything above.*

**This is the first condition on the graph to carry an enumerator with a stated return on both of its counting
clauses.** Clauses 6 and 7 each name a command, its return at a named commit, and the arithmetic that gets from that
return to the demand. Under [node 110](110-does-the-checker-rerun-the-enumerator.md)'s rule its checker will re-run
both and report each return **alongside** its outcome, so a count that has moved since `106380a` is reported and
never on its own a `FAIL`. **The counts will have moved**: node 133 is live in a worktree touching
`expedition/SKILL.md`, which holds 8 of clause 6's 14.

**Two things the manager must sequence rather than edge.** Node 133 holds the code slot and shares one file with this
node. [Node 134](134-repair-two-context-defects-node-113-found.md) edits `CONTEXT.md` too, and its two sites — the
kinds-of-node section and the `grilling` entry — are disjoint from this node's five, so they do not collide; with a
code slot of one they serialise anyway.

**Flag `107.3` bears directly on clause 5.** It records that the recommended parenthetical wording is a
recommendation rather than the human's own words, which is why clause 5 demands properties and offers the wording.
The worker holding this node may improve on it.

## Amendment, 2026-09-25 (from node 297)

*Written by [node 297](297-rewrite-the-manager-contract-part-2.md)'s worker and filed by the manager, after that node's work landed as commit `e6c43fb`. Every word of the replacement is fixed by that commit and by this node's own clause 6: it quotes `expedition/SKILL.md`'s after-text. The minting author's condition above is left as it was. Node 297's worker's search is on node 297 under `### Re-pointing search`.*

- **Clause 8.** Replace it with: "8. `expedition/SKILL.md` today reads *"Say in the pick report that the condition is yours, and say in a line or two what it demands."* Its `pick report` takes the node-level term under clause 6, like every other occurrence."

## Flags

`137.1` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from node 297's re-pointing list, on the ground that every word of the replacement is fixed by commit `e6c43fb`.

## Amendment, 2026-09-25 (from node 292)

*Written by [node 292](292-rewrite-the-precondition-contract.md)'s worker and filed by the manager, after that node's work landed as commit `ede2c76`. Every word of the replacement is fixed by that commit: it quotes `expedition-precondition/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 292's worker's search is on node 292 under `RE-POINTING SEARCH` and its addendum.*

- **Clause 6.** After clause 6's last sentence, add: "`.claude/skills/expedition-precondition/SKILL.md` no longer says `pick report`. It reads *"The flag settles at the report the manager sends the human when your node closes."* That phrase names the node-level report, and it is replaced by the node-level term." The file stays in this node's scope list, so no other clause changes.

`137.2` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 292](292-rewrite-the-precondition-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `ede2c76`.

## Amendment, 2026-09-26 (from node 302)

*Written by [node 302](302-rewrite-the-glossary.md)'s worker and filed by the manager, after that node's work landed as commit `de347dc`. Every word of the replacement is fixed by that commit: it quotes `CONTEXT.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 302's worker's search is on node 302 under `RE-POINTING SEARCH`.*

- **Clause 5.** "`CONTEXT.md`'s `**Handover**:` entry ends today with `_Avoid_: report (the closing report owns that word), return, payload, deliverable`." becomes "`CONTEXT.md`'s `**Handover**:` entry ends today with `_Avoid_: report (the closing report uses that word), return, payload, deliverable`." The rest of clause 5 is unchanged.

*The manager's note:* the worker reported that clause 6's recorded count, "2 in `CONTEXT.md`" for `pick report`, and clause 7's `closing report` occurrences in `CONTEXT.md` (3) are the same before and after.

`137.3` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 302](302-rewrite-the-glossary.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `de347dc`.

`137.4` `ASSUMPTION` **· settled** — *From attempt 1's handover.* Clause 6 says `pick report` "appears nowhere in the four files". It also says its enumerator, which searches all of `.claude/`, must "return nothing". At `eb3b217` the enumerator still returns 4 lines, all in `.claude/skills/expedition-standing-yes/SKILL.md`. Node 342 created that file after the condition was written, and it is outside the condition's "four files, and no others". I read the demand as scoped to the four files, which is what the enumerator covered when it was recorded (14 = 8+3+2+1, all in the four files). I left the fifth file unedited, as the spawn directed, and reported its repair under NEW NODES. If the manager judges this an incoherent clause rather than a count that moved, the question goes to the human at the gate. — Node 137 read clause 6's "return nothing" as scoped to its four files, leaving four `pick report` hits in the later `expedition-standing-yes` skill for a new node.

`137.5` `ASSUMPTION` **· settled** — *From attempt 1's handover.* The Node closing report entry says the report is sent "the moment a node closes". The `Resolve` entry's `_Avoid_` refuses "close". I kept "closes" for three reasons: the settled term's own name carries "closing"; the sense is a node's work ending in front of the human, not resolution; and the files already said "the pick report that closes the node" in this sense. — Node 137 kept "closes" in the node closing report's definition despite Resolve refusing "close", since the settled term's own name carries it.

`137.6` `ASSUMPTION` **· settled** — *From attempt 1's handover.* Beyond clause 7's grep, I renamed two periphrases in `expedition/SKILL.md` ("the report that precedes a close") to "the effort closing report". This does not change their meaning. — Node 137 named the effort closing report in two SKILL.md sentences that described it by periphrasis, meaning unchanged.

`137.7` `ASSUMPTION` **· settled** — *From attempt 1's handover.* In `expedition/SKILL.md`'s amendment list, item 5 needed its two reports told apart once both became node closing reports. It now says "the node closing report that names the node as started" and "that node's own node closing report". This sits in the amendment section, which node 327 is also editing, so the two changes need reconciling when they are integrated. — Node 137 reworded amendment item 5 in SKILL.md to tell apart the two node closing reports it names, a site node 327 also edits.

*The manager's note, 2026-09-26:* [node 106](106-context-closing-report-entry-lists-three.md)'s worker reports, under its `INVALIDATIONS`, that clause 1 of this node's condition defines the effort closing report as "what was decided, what landed, and every flag still outstanding", and clause 2 says the renamed entry's meaning is unchanged. Node 106 replaces that three-item list with the manager contract's six items. Once 106 lands, a worker following clause 1 would put the three-item list back. Repairing this condition goes to the human; this node is not started until they answer.

*The manager's note, 2026-09-26:* the human's "ok" to [node 328](328-group-the-open-nodes-against-the-glossary.md)'s C6, on the manager's pick, settles that clause 1 of this node's condition is amended to define the effort closing report by node 106's six items rather than by "what was decided, what landed, and every flag still outstanding". Node 106's landed text (`64db5aa`): "What the manager hands the human once the frontier empties. It covers only what the human has not already seen. It carries what landed, the supersession chains, the state of the bar, every flag still outstanding, what the sweep found, and every sweep round."

*The manager's note, 2026-09-27:* [node 335](335-qualify-the-glossarys-research-entry-for-the-research-raise.md)'s worker reports that clause 5 of this node's condition quotes the glossary's Handover `_Avoid_` line as "(the closing report owns that word)", where the file says "(the closing report uses that word)". Stale before its work.

## Answer

The glossary and three shipped files now name the effort closing report and the node closing report, with the bare form meaning the node one; `pick report` is retired and Handover's `_Avoid_` line no longer says one term owns "report".

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1 with two questions. The human took the manager's recommendation. The work landed as commit `fe2610b`. Flags 137.1 to 137.7 are settled at this gate. The cleanup skill's two bare uses are folded into [node 344](344-carry-the-node-closing-report-term-into-expedition-standing-yes.md); the worker's replacement clause for node 41 is filed on node 41.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      Rename the two reports and repair the `_Avoid_` line that reserved the word

ANSWER:
The vocabulary now has two named reports. `pick report` is gone from the four files in scope. Every effort-level use of "closing report" carries the `effort` prefix.

How I read the condition. I worked to clause 1 as amended in the manager's note of 2026-09-26 (the human's "ok" to node 328's C6): the effort closing report is defined by node 106's six items. `CONTEXT.md` at `eb3b217` already held that six-item text, so the rename in clause 2 keeps it word for word. For clause 5, I took node 302's amendment: the before-text is "(the closing report uses that word)". For clause 8, I took node 297's amendment. For clause 6, I added node 292's sentence.

What each file now says:

- `CONTEXT.md`
  - The `**Closing report**:` entry is renamed `**Effort closing report**:`. Its text and its `_Avoid_: completion report, summary` are unchanged (clause 2).
  - A new `**Node closing report**:` entry sits at the end of `## Talking to the human`, after `Standing yes` (clause 3). It says: sent the moment a node closes; names the node that closed; carries in full every flag that node holds, because those flags settle there; names the work the manager started in response; awaits no answer and takes no place in the queue of things waiting for the human. It also carries both halves of clause 4: "An unqualified "closing report" means this report. Prose written before this term was settled uses "closing report" for the effort closing report."
  - The Handover `_Avoid_` line now reads `_Avoid_: report (a report goes to the human; a handover goes to the manager), return, payload, deliverable`. This is clause 5's recommended form. It wraps onto two lines, as other `_Avoid_` lines in the file do.
  - The `Flag` entry now says "otherwise the node closing report" and "into the effort closing report".
  - The `Raise` entry now says "or the node closing report". Its paragraph is rewrapped to the file's width.
- `.claude/skills/expedition/SKILL.md`
  - All 15 `pick report` occurrences became "node closing report".
  - The clause-8 sentence (as amended by node 297) now reads "Say in the node closing report that the condition is yours, ...".
  - Item 5 of the amendment list read "named in the pick report … named in the report that closes that node instead". It now reads "named in the node closing report that names the node as started … named in that node's own node closing report instead". I reworded it this way because both halves are now node closing reports, of different nodes.
  - Three effort-level "closing report" uses gained `effort`: the priority-list check, the channel-free bullet, and "never enter the queue".
  - Two periphrases of the effort-level report ("the report that precedes a close"), in `## Starting an effort` and `## Closing an effort`, now name the effort closing report. Meaning is unchanged. I did this so that graph-conventions' pointer to `## Closing an effort` lands on the term.
- `.claude/skills/expedition/graph-conventions.md`: its three "closing report" uses (the `flags.md` description, the disagree rule, and the pointer after `### Settle a flag`'s steps) became "effort closing report".
- `.claude/skills/expedition-precondition/SKILL.md`: "The flag settles at the report the manager sends the human when your node closes" now reads "The flag settles at the node closing report, which the manager sends the human when your node closes" (node 292's amendment).

No rule was removed or renumbered (clause 9). The Handover `_Avoid_` line still refuses report, return, payload and deliverable.

Enumerator returns. These are the counts at `eb3b217`, not the recorded ones, which had moved.
- Clause 6, `grep -rn "pick report" --include=*.md .claude/ CONTEXT.md`
  - Before: 21 lines. 15 in `expedition/SKILL.md`, 2 in `CONTEXT.md`, 0 in `graph-conventions.md`, 0 in `expedition-precondition/SKILL.md`, and 4 in `.claude/skills/expedition-standing-yes/SKILL.md`, which is outside the four files. The recorded 14 at `106380a` was 8/3/2/1.
  - After: 4 lines, all in `expedition-standing-yes/SKILL.md`. That file was left unedited on the spawn's instruction and is reported under NEW NODES.
- Clause 7, `grep -rni "closing report" --include=*.md .claude/ CONTEXT.md`
  - Before: 12 lines. 3 in `CONTEXT.md`, 3 in `SKILL.md`, 3 in `graph-conventions.md`, and 3 in `.claude/skills/expedition-stop/SKILL.md`, which is outside the four files. That makes 9 in scope against the recorded 7. Of the 9, clause 2 renamed 1 (the entry heading) and clause 5 rewrote 1 (the `_Avoid_` line). The other 7 were all effort-level and all took the prefix.
  - After: every hit in the four files is either prefixed or deliberately bare. The only bare ones are the two quoted uses inside the Node closing report entry, where clause 4 needs them. The node-level term has many new hits.

Left as found:
- `.claude/skills/expedition-stop/SKILL.md` names a third report, "the session's closing report". It is qualified by "session's" and is outside scope. The glossary has no entry for it. The manager may want one. I do not propose it as a node here.

INDEX LINE:    The glossary and three shipped files now name the effort closing report and the node closing report, with the bare form meaning the node one; `pick report` is retired and Handover's `_Avoid_` line no longer says one term owns "report".

FLAGS:
- ASSUMPTION: Clause 6 says `pick report` "appears nowhere in the four files". It also says its enumerator, which searches all of `.claude/`, must "return nothing". At `eb3b217` the enumerator still returns 4 lines, all in `.claude/skills/expedition-standing-yes/SKILL.md`. Node 342 created that file after the condition was written, and it is outside the condition's "four files, and no others". I read the demand as scoped to the four files, which is what the enumerator covered when it was recorded (14 = 8+3+2+1, all in the four files). I left the fifth file unedited, as the spawn directed, and reported its repair under NEW NODES. If the manager judges this an incoherent clause rather than a count that moved, the question goes to the human at the gate.
  Index: Node 137 read clause 6's "return nothing" as scoped to its four files, leaving four `pick report` hits in the later `expedition-standing-yes` skill for a new node.
- ASSUMPTION: The Node closing report entry says the report is sent "the moment a node closes". The `Resolve` entry's `_Avoid_` refuses "close". I kept "closes" for three reasons: the settled term's own name carries "closing"; the sense is a node's work ending in front of the human, not resolution; and the files already said "the pick report that closes the node" in this sense.
  Index: Node 137 kept "closes" in the node closing report's definition despite Resolve refusing "close", since the settled term's own name carries it.
- ASSUMPTION: Beyond clause 7's grep, I renamed two periphrases in `expedition/SKILL.md` ("the report that precedes a close") to "the effort closing report". This does not change their meaning.
  Index: Node 137 named the effort closing report in two SKILL.md sentences that described it by periphrasis, meaning unchanged.
- ASSUMPTION: In `expedition/SKILL.md`'s amendment list, item 5 needed its two reports told apart once both became node closing reports. It now says "the node closing report that names the node as started" and "that node's own node closing report". This sits in the amendment section, which node 327 is also editing, so the two changes need reconciling when they are integrated.
  Index: Node 137 reworded amendment item 5 in SKILL.md to tell apart the two node closing reports it names, a site node 327 also edits.

NEW NODES:
- Name: Carry the node closing report term into `expedition-standing-yes`
  Kind: implementation
  Question: `.claude/skills/expedition-standing-yes/SKILL.md` still says `pick report`, which node 137 retired in favour of "node closing report". Carry the term into that file.
  Blockers: node 137. The glossary entry `**Node closing report**:` must have landed first.
  Acceptance condition:
  > The one file, and no others: `.claude/skills/expedition-standing-yes/SKILL.md`.
  > 1. `grep -n "pick report" .claude/skills/expedition-standing-yes/SKILL.md` returns nothing. At commit `eb3b217` it returned 4 lines: the heading `## Flags, and the pick report` and three in the body of that section ("settle at the pick report that closes the node", "The pick report that closes a node names every item", "as any pick report that closes a node does"). Re-run it; the demand is that it return nothing, whatever the count has become.
  > 2. Each occurrence becomes "node closing report". The heading becomes `## Flags, and the node closing report`. Where a sentence said "the pick report that closes the node", the words "that closes the node" may be dropped or kept, as the sentence needs.
  > 3. No rule in the file is removed or renumbered, and none changes its meaning.
  > 4. The working tree meets the bar.
  Every word is fixed by node 137's landed glossary entry and by the file's text at `eb3b217`.

INVALIDATIONS:
- These nodes use `pick report` in their answers and index lines. Each is a rename to "node closing report" and is otherwise unchanged. Older prose keeps the old word under the never-delete rule: 39, 99, 100, 102, 103, 309, 310 and 342.
- Node 106: a rename. The entry it rewrote is now headed `**Effort closing report**:`, and its text is unchanged.
- Node 107: its decision is carried out, with no change to what it says.
- `map.md`'s standing preference "Approving a node's end settles that node's flags" is rule text, not a node. It says "pick report" several times and uses bare "closing report" for the effort-level one. Under the `Change the map` procedure it would be replaced by its current form. It belongs to the manager.

CONDITIONS:
I searched the `## Acceptance condition` sections (amendments included) of every open or claimed node for these phrases: "pick report", "closing report", "report the manager sends", "report that closes", "report that precedes", "report accompanying", "uses that word" and "owns that word".
- Node 137: its own condition. Nothing to replace.
- Node 327 (claimed): no match.
- Node 41 (open, unclaimed) matched once. Its condition reads "outstanding — left unchecked, meaning carried, and re-surfaced in that effort's closing report." Under the new rule, bare "closing report" means the node-level report, and here "that effort's" is a possessive rather than the `effort` prefix.
  - Replacement: "outstanding — left unchecked, meaning carried, and re-surfaced in the effort closing report of that effort."
  - Fixed by: node 137's `**Effort closing report**:` entry in `CONTEXT.md`, once that lands.

MISSING FROM MAP: none

GATE PAYLOAD:
- Checker findings: none yet. The checker has not run.
- Paths touched, all in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/137-reports`:
  - `CONTEXT.md`
  - `.claude/skills/expedition/SKILL.md`
  - `.claude/skills/expedition/graph-conventions.md`
  - `.claude/skills/expedition-precondition/SKILL.md`
- Nothing else touched. Uncommitted on `worktree-137-reports`.
- The bar: confirmed against the repo that it has no build, no tests, no formatter and no CI. The only files at the root are `.claude/`, `CONTEXT.md`, `.gitignore` and `.scratch/`. This matches the rules file. The non-command half is checked:
  - `_Avoid_` lines: checked by hand. "closes" is flagged above. "queue" in the new entry means the human's pending queue, not the frontier.
  - Wrap widths are kept: `CONTEXT.md` ≤102, the three others ≤105. No added line is wider.
- Proposed commit message:

  ```
  Name the effort closing report and the node closing report, and retire "pick report"

  Rename CONTEXT.md's Closing report entry to Effort closing report and add a
  Node closing report entry, the bare form meaning the node one. Carry the pair
  into the manager contract, graph-conventions.md and the precondition contract,
  and repair the Handover _Avoid_ line so it no longer says one term owns the
  word "report".

  Node: graph-workflow/137
  ```

RETROSPECTIVE
1. What I had to hunt for. I re-derived the counts at `eb3b217` for each file and the `pick report` hits outside the four files. The spawn warned the counts had moved but gave none, so I ran `git show eb3b217:<path> | grep`. Finding the open nodes' conditions needed an awk extraction per node file, because a whole-file grep matched about 60 nodes, mostly resolved ones.
2. What arrived that this node did not need. Most of `map.md` (about 41 KB), read whole because the contract requires it: the worktree route, token and credit strategy, the retrospective rule's history. Only its Notes on the glossary and on the never-delete rule bore on this node. The first `cat` of map.md plus the rules file overflowed to a persisted file, and I had to re-read it.
3. What would have made this easier. The spawn or the node could have stated at `eb3b217` which files outside the four hit each enumerator (standing-yes for `pick report`, expedition-stop for `closing report`), and whether clause 6's "return nothing" should be read as scoped to the four files. That is the one real judgement this node had to make. A single amended text of the condition would have saved assembling it from the original, three amendment sections and two dated notes.
4. What was stale, wrong or contradictory.
   - Clause 6's recorded count (14, with 3 in graph-conventions and 1 in precondition) was stale. At `eb3b217` graph-conventions and precondition had 0, and SKILL.md had 15.
   - Clause 7's recorded 7 was 9 within scope, plus 3 in expedition-stop.
   - Clause 5's quote said "owns" (known).
   - Clause 1's three-item list was superseded (known).
   - Clause 6's enumerator reaches beyond the condition's "four files, and no others", which is now a live conflict because node 342's file exists.

### Carried onto master `eef448a`, 2026-09-27

*The manager resumed the worker after node 327 landed, before the check. The worker's own report, pasted:*

NODE 137: CARRIED ONTO THE NEW MASTER (uncommitted)

New base: `eef448a` ("Let a related defect join an open node's condition instead of minting a new node"). Branch `worktree-137-reports` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/137-reports`. I saved the diff to `$TMPDIR/n137/work.diff` and copied the four files there. Then `git reset --hard`, `git rebase master`, and `git apply --3way`. I did not use `git stash`. The index is reset, so the changes are unstaged.

What the resolution changed in my text: `git apply --3way` applied cleanly to `CONTEXT.md`, `graph-conventions.md` and `expedition-precondition/SKILL.md`. It hit one conflict, in `.claude/skills/expedition/SKILL.md`, in the amendment list under `### Changing one after it is written`. I resolved it by keeping node 327's item 4 as landed and my item 5 as I handed it back. The result:

```
4. It is carried as a flag of its own, which settles at that node's gate under `## Flags`.
5. It is named in the node closing report that names the node as started. Where the amendment is made
   after the node is claimed, it is named in that node's own node closing report instead.
```

My item-4 side was the old `eb3b217` text, "It is carried as a flag.". It was dropped because it was not mine. My text is otherwise unchanged. The same flag stands: item 5 sits in the section 327 edited.

Renamed in 327's text: nothing. Its additions to the four files contain no "pick report", no bare "closing report", and no roundabout name for either report. The only "report" words it added are the verb "report(s)" in the related-defect lines. At `eef448a` before my change, the `pick report` counts were still 2 in `CONTEXT.md`, 15 in `SKILL.md`, 0 in `graph-conventions.md` and 0 in the precondition contract. So 327 added none.

Enumerators on the result:
- Clause 6, `grep -rn "pick report" --include=*.md .claude/ CONTEXT.md`: 4 lines, all in `.claude/skills/expedition-standing-yes/SKILL.md` (lines 80, 83, 86 and 87). The four files return nothing. This is unchanged from my handover, and so is the clause-6 flag.
- Clause 7, `grep -rni "closing report" --include=*.md .claude/ CONTEXT.md`: 33 lines.
  - In the four files, every hit is either "effort closing report" or "node closing report".
  - The two exceptions are the deliberate bare quotes in `CONTEXT.md`'s Node closing report entry (lines 299–300), which clause 4 needs.
  - The other 3 are in `.claude/skills/expedition-stop/SKILL.md` ("the session's closing report"), outside the four files and left as found.

`git diff --stat`:
```
 .claude/skills/expedition-precondition/SKILL.md |  6 +--
 .claude/skills/expedition/SKILL.md              | 56 +++++++++++++------------
 .claude/skills/expedition/graph-conventions.md  | 12 +++---
 CONTEXT.md                                      | 28 ++++++++-----
 4 files changed, 57 insertions(+), 45 deletions(-)
```

`git diff --check`: no output, exit 0. No added line is wider than each file's wrap width.

Paths touched: the same four as in the handover. The rest of the handover stands as delivered.

## Review

### Checker run 1 — `PASS`, with two questions

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 202's check; the condition reached it as a verbatim copy in `$TMPDIR/c137.md`, assembled from the condition and its three amendment sections.*

> PASS
>
> Node 137, "Rename the two reports and repair the `_Avoid_` line that reserved the word". The work is the uncommitted diff in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/137-reports`, on base eef448a. I read the whole condition in `/tmp/claude-1000/c137.md`, including its amendments from nodes 297, 292 and 302 and the manager's dated notes. Following the notes, I held clause 1's effort-level definition to node 106's six items, and clause 5's before-text to "uses".
>
> **Parts of the condition**
>
> - **Scope ("the four files, and no others"):** met. `git status --short --untracked-files=all` shows exactly `CONTEXT.md`, `expedition/SKILL.md`, `graph-conventions.md` and `expedition-precondition/SKILL.md`. The diff contains no `.scratch/` file, no `decisions.md` and no `flags.md`.
> - **Clause 1:** met.
>   - `**Effort closing report**:` (CONTEXT.md, line 380) is unchanged in body and carries the six items: what landed, supersession chains, state of the bar, outstanding flags, what the sweep found, every sweep round.
>   - The new `**Node closing report**:` (line 295) covers each part of the definition: the message the manager sends the moment a node closes, naming it; carrying every flag in full "because those flags settle there"; naming the work started; awaiting no answer and taking no place in the queue.
>   - It also says "An unqualified "closing report" means this report."
> - **Clause 2:** met. `**Closing report**:` is renamed `**Effort closing report**:`. The body is a context line in the diff, so it is unchanged. `_Avoid_: completion report, summary` is kept (line 384).
> - **Clause 3:** met. The node-level entry sits at line 295, between `## Talking to the human` (line 237) and `## Landing code` (line 302), so it falls under the required heading.
> - **Clause 4:** met. The node-level entry has both halves: the unqualified term means this report, and "Prose written before this term was settled uses "closing report" for the effort closing report."
> - **Clause 5:** met. The Handover line now reads `_Avoid_: report (a report goes to the human; a handover goes to the manager), return, payload, deliverable`. All four words are still refused, no term owns "report", and this is the recommended form.
> - **Clause 6:** met in the four files. Re-running the recorded enumerator, `grep -rn "pick report" --include=*.md .claude/ CONTEXT.md`, returns 4 lines, all in `.claude/skills/expedition-standing-yes/SKILL.md` (lines 80, 83, 86, 87) and none in the four files. See QUESTIONS for the enumerator's "return nothing".
>   - The node-292 amendment is met: the precondition contract now reads "The flag settles at the node closing report, which the manager sends the human when your node closes."
> - **Clause 7:** met.
>   - Re-running `grep -rni "closing report" --include=*.md .claude/ CONTEXT.md`, every hit in the four files is prefixed: "node closing report" for the node-level report, "effort closing report" for the effort-level one. I judged each hit by which report it means.
>   - The only bare hits are in the new entry's own definition. I confirmed this by joining each paragraph of the four files into one line and grepping for `closing report` not preceded by `node` or `effort`.
>   - The other hits are `expedition-stop`'s "the session's closing report", which is qualified and outside the four files.
> - **Clause 8** (as amended from node 297): met. Item 4 now reads "Say in the node closing report that the condition is yours, and say in a line or two what it demands."
> - **Clause 9:** met.
>   - No rule is removed, no numbered item is renumbered, and every numbered list keeps its items.
>   - The remaining changes are renames with meaning unchanged:
>     - the two "report that precedes a close" periphrases now read "the effort closing report";
>     - amendment item 5 now reads "the node closing report that names the node as started" and "that node's own node closing report";
>     - "The pick report awaits no answer" now reads "It awaits no answer";
>     - the `**Raise**:` entry is rewrapped with only the term swapped.
>   - Clause 5's `_Avoid_` line still refuses all four words.
>   - Joined-paragraph greps for `pick report|report that (closes|precedes)|report accompanying|report the manager sends` over the four files return nothing.
> - **Clause 10:** met. See the bar below.
>
> **The bar**
>
> - The repo has no build, tests, formatter or CI, so there are no commands to run.
> - `git diff --check` is clean (exit 0).
> - No added line exceeds the files' wrap width.
>
> **Standards**
>
> As in my earlier checks, I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`.
>
> - **CONTEXT.md's `_Avoid_` lines:** checked by hand. The Resolve entry refuses "close", but the new entry's "the moment a node closes" uses the word in the settled term's own sense. That is flag 137.5, carried in the condition as given. Nothing else found.
> - **Writing rules:** citations are by heading, and the only bold is on the defined terms.
> - **`/writing-for-agents`:** nothing found.
> - **Ground rules:** nothing assumes a repo, machine or toolchain, and nothing addresses the human.
> - **Did not bear:** `/coding-principles` and `/naming` (the new term's name is dictated by the condition).
> - **Reviewing skill:** none is named, so I ran none.
> - **Standards the work changes:** graph-conventions.md and CONTEXT.md are among the work. The renames change what their text calls the two reports, but move no element I hold the work against.
>
> **The search the condition records**
>
> - **Clause 6:** `grep -rn "pick report" --include=*.md .claude/ CONTEXT.md` was recorded as 14 hits (8+3+2+1, all in the four files) at 106380a. It now returns 4 hits, all in `expedition-standing-yes/SKILL.md`, a place outside the condition's list. Details are under QUESTIONS.
> - **Clause 7:** `grep -rni "closing report" …` was recorded as 7 hits at 106380a. It now returns 36 lines, and I judged each one as clause 7 asks.
>
> QUESTIONS:
> - **Clause 6's enumerator.**
>   - *Instances:* clause 6 says the enumerator must "return nothing, whatever the count has become". It searches all of `.claude/`, and it returns 4 lines in `.claude/skills/expedition-standing-yes/SKILL.md` (80, 83, 86, 87). The condition's fence ("The four files, and no others") forbids the worker to edit that file, so the literal demand cannot be met without breaching the fence.
>   - *Why a question and not a FAIL:* the wording is the condition's own, so departing from it was not the worker's call. The worker read "return nothing" as scoped to the four files, which is what the recorded 14 covered, and flagged this as 137.4 for the human at the gate. I found the four files clean, so this is handed back as a question.
>   - *Form:* a `pick report` occurrence under `.claude/` or `CONTEXT.md` outside the four files.
>   - *Extent:* `grep -rn "pick report" --include=*.md .claude/ CONTEXT.md`.
> - **Integration with master (for the human, via the manager).**
>   - *Instances:* master 89135d3 adds `.claude/skills/expedition-cleanup/SKILL.md`. I read it with `git show 89135d3:<path>`, which reads the tree and not the record. It uses bare "closing report" for the effort-level report at line 45 ("would drop it from the closing report") and line 61 ("The closing report is built from its lines whose flag is not yet settled"). Under this work's new rule, a bare "closing report" means the node-level report, so after integration those two lines would name the wrong report. They are outside this node's four files.
>   - *Form:* a bare "closing report" that means the effort-level report, in a shipped file outside the four.
>   - *Extent:* `grep -rniE 'closing report' --include=*.md .claude/ | grep -viE '(node|effort|session.s) closing report'`, run on the integrated tree.
>
> NOT COVERED:
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The condition does not demand this, but the rules file makes it a bookkeeping rule. The worktree diff contains no such write, and what the main tree's record holds is outside what I was given.

*The manager's note:* the checker handed back questions beside its outcome, which the standing yes never covers, so this gate goes to the human.

### Gate — approve, 2026-09-27

The human, `verbatim`: *"ok for recommended"*. The recommendation it takes, the manager's: "approve node 137. Accept the four-file reading of clause 6. Fold the cleanup skill's two lines into node 344, which is open, unclaimed and about the same concern, as an amendment carrying its own flag. The amendment will say those two lines read "effort closing report"."
