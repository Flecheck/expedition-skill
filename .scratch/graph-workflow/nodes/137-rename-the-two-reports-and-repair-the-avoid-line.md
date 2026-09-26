# Rename the two reports and repair the `_Avoid_` line that reserved the word

Type: implementation
Status: open

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

`137.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from node 297's re-pointing list, on the ground that every word of the replacement is fixed by commit `e6c43fb`.

## Amendment, 2026-09-25 (from node 292)

*Written by [node 292](292-rewrite-the-precondition-contract.md)'s worker and filed by the manager, after that node's work landed as commit `ede2c76`. Every word of the replacement is fixed by that commit: it quotes `expedition-precondition/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 292's worker's search is on node 292 under `RE-POINTING SEARCH` and its addendum.*

- **Clause 6.** After clause 6's last sentence, add: "`.claude/skills/expedition-precondition/SKILL.md` no longer says `pick report`. It reads *"The flag settles at the report the manager sends the human when your node closes."* That phrase names the node-level report, and it is replaced by the node-level term." The file stays in this node's scope list, so no other clause changes.

`137.2` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 292](292-rewrite-the-precondition-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `ede2c76`.

## Amendment, 2026-09-26 (from node 302)

*Written by [node 302](302-rewrite-the-glossary.md)'s worker and filed by the manager, after that node's work landed as commit `de347dc`. Every word of the replacement is fixed by that commit: it quotes `CONTEXT.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 302's worker's search is on node 302 under `RE-POINTING SEARCH`.*

- **Clause 5.** "`CONTEXT.md`'s `**Handover**:` entry ends today with `_Avoid_: report (the closing report owns that word), return, payload, deliverable`." becomes "`CONTEXT.md`'s `**Handover**:` entry ends today with `_Avoid_: report (the closing report uses that word), return, payload, deliverable`." The rest of clause 5 is unchanged.

*The manager's note:* the worker reported that clause 6's recorded count, "2 in `CONTEXT.md`" for `pick report`, and clause 7's `closing report` occurrences in `CONTEXT.md` (3) are the same before and after.

`137.3` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 302](302-rewrite-the-glossary.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `de347dc`.

*The manager's note, 2026-09-26:* [node 106](106-context-closing-report-entry-lists-three.md)'s worker reports, under its `INVALIDATIONS`, that clause 1 of this node's condition defines the effort closing report as "what was decided, what landed, and every flag still outstanding", and clause 2 says the renamed entry's meaning is unchanged. Node 106 replaces that three-item list with the manager contract's six items. Once 106 lands, a worker following clause 1 would put the three-item list back. Repairing this condition goes to the human; this node is not started until they answer.

*The manager's note, 2026-09-26:* the human's "ok" to [node 328](328-group-the-open-nodes-against-the-glossary.md)'s C6, on the manager's pick, settles that clause 1 of this node's condition is amended to define the effort closing report by node 106's six items rather than by "what was decided, what landed, and every flag still outstanding". Node 106's landed text (`64db5aa`): "What the manager hands the human once the frontier empties. It covers only what the human has not already seen. It carries what landed, the supersession chains, the state of the bar, every flag still outstanding, what the sweep found, and every sweep round."
