# Sweep round 1, at the first empty frontier

Type: precondition
Status: resolved
Blocked by: none

## Answer

The first sweep ran every check under `graph-conventions.md`'s `## Mechanical checks` over the whole graph on 2026-10-07. Checks 4 and 8 passed. Check 10 reported 32 items. Every other check failed, almost entirely on older records written before the current conventions. What becomes of the failures is the human's to decide, and that decision is recorded under `## Interview` once it is given.

*The manager's note:* minted by the manager to hold the sweep round's report, which `SKILL.md`'s `## Closing an effort` says the effort closing report carries. The sweep ran under the rule [node 390](390-state-the-sweep-as-a-whole-graph-run-of-the-mechanical-checks.md) shipped, as one read-only agent.

## Question

What does a whole-graph run of the mechanical checks find at the effort's first empty frontier?

## The sweep agent's report

*Pasted as the read-only agent handed it back, 2026-10-07.*

`````
## Sweep report: `.scratch/graph-workflow/`, all 11 mechanical checks

I wrote nothing in the repo and the working tree is clean. My scripts were under `$TMPDIR` and I removed them; the other files in `/tmp/claude-1000` were already there and I left them alone. I read the files by the rules in `### How a check reads the files`: fields come only from the header block, fenced blocks are skipped, `Blocked by:` numbers are taken outside code spans, strikethrough and link targets, and a flag's node is the first link on its line. The frontier script reports 0 claimed and 0 startable nodes. All 392 node files are `resolved` (304), `superseded` (72) or `out-of-scope` (16).

### Check 1: FAIL (1)
- `nodes/164-what-a-standards-path-may-hold.md` (superseded) has `Blocked by: 143, 151`, and node 151 is `superseded` (`Superseded by: 334`). To pass: replace 151 with 334, as step 4 of Supersede says, or strike it.

### Check 2: FAIL (5)
Each replacement node lacks the matching `Supersedes:`.
- `61-collapse-onto-scribe.md` has `Superseded by: 76`, but node 76 has no `Supersedes:`. To pass: add `Supersedes: 61` to node 76.
- `72-checker-is-given-the-review-route.md` has `Superseded by: 143`, but node 143 has none. To pass: add `Supersedes: 72` to node 143.
- `81-glossary-code-slot-and-reject.md` has `Superseded by: 332, 333`, but node 332's field reads `Supersedes: 90, 92, 134, 247`. To pass: add 81 to node 332's `Supersedes:`. Node 333 already matches.
- `192-the-top-up-trigger-is-a-node-finishing.md` has `Superseded by: 100`, but node 100 has no `Supersedes:`. To pass: add `Supersedes: 192` to node 100.
- `279-five-worker-contracts-route-a-scope-raise-to-the-human.md` has `Superseded by: 311`, but node 311 has none. To pass: add `Supersedes: 279` to node 311.

### Check 3: FAIL as stated (1)
- Id 187 has no node file. The ids run 01–393 with no duplicates. Git history (all refs) shows no file numbered 187 under `nodes/` or `issues/` ever existed, so the gap is a skipped number, not a reused one. From the files alone I cannot tell whether a gap "indicates a reused number", so I report it. Node 213 recorded the same item as a check 3 FAIL. To pass: rule that a skipped id is not a gap that indicates reuse, or record 187 as never allocated.

### Check 4: PASSED
No node carries `Labels:`, and `map-manager-only.md` declares no vocabulary.

### Check 5: FAIL (17)
14 resolved nodes have no `## Answer` heading:
- 95, 166, 218, 242, 244, 249, 255, 260, 267, 268, 269, 274, 277, 281.
- Nine of them (95, 255, 260, 267, 268, 269, 274, 277, 281) carry their answer under `## What the work states`. Nodes 166, 218, 242, 244 and 249 have no answer-like section at all.
- To pass: an `## Answer` section on each.

Three nodes have the wrong number of unstruck lines in `decisions.md`:
- Node 131 has two identical unstruck lines, `decisions.md:219` and `:220` (*"- [A "just do it" mode that skips grilling…](nodes/131-…) — `/expedition-standing-yes` ships: …"*). To pass: strike one.
- Node 218 has only a struck line (`decisions.md:142`, `- ~~[Put the manager's trigger-duties…](nodes/218-…)`) and no unstruck line. To pass: add one current line.
- Node 243 has only a struck line (`decisions.md:152`, `- ~~[A worker cannot enter its worktree…](nodes/243-…)`). To pass: add one current line.

A borderline case I did not count: node 13 has two unstruck lines whose first link is node 13 — its real entry at line 34, and the preamble prose at `decisions.md:11`, `[Graph file format](nodes/13-graph-file-format.md).` The first-link rule counts the preamble line too. To pass: rule that only list-item lines are entries, or move the preamble's citation off the start.

### Check 6: FAIL (about 525 items in 7 groups)
`flags.md` has no unchecked line outside its fenced format example. Every one of its 815 lines is `- [x]`.

**a. 20 lines with no id.** These are `flags.md:43`–`62`, the legacy lines for nodes 12, 14, 20, 21, 23 and 24, for example `:43` *"- [x] ASSUMPTION · [Naming the workflow and its vocabulary](nodes/14-naming.md) — wrote `CONTEXT.md` …"*. With no id, no entry can match them. To pass: give each line and its node entry an id.

**b. A duplicate id.** `190.1` appears at `flags.md:367` (CONDITION-WRONG) and `:714` (ASSUMPTION). Node 190 notes the duplicate itself. To pass: re-id one of them.

**c. Outstanding entries with no index line (4).**
- `265-should-the-worktree-route-drop-enterworktree-for-git.md:428/440/451`: ``265.2` `ASSUMPTION` — *The worker's own text, pasted.*`` and likewise `265.3` and `265.4`.
- `283-what-makes-a-change-to-a-record-file-a-node-rather-than-bookkeeping.md:55`: ``283.1` `MANAGER-WRONG` — …``.
- None of these is marked settled, so a missing line is a mismatch. To pass: append the `flags.md` lines, or settle the entries.

**d. An index line with no entry anywhere (1).** `flags.md:363` is `- [x] 160.1 CONDITION-WRONG · [Carry the integration-conflict rule…](nodes/160-…)`. Node 160's `## Flags` starts at `160.2`. To pass: file the `160.1` entry on node 160.

**e. Index lines whose entry is not a `## Flags` entry (103).** The entry exists on the node but sits under another heading, is prefixed, or begins mid-paragraph, so it does not count. To pass: put each entry under `## Flags`, at the start of its own paragraph.
- Under `## Amendment …` (30): 296.4, 148.2–6, 258.1, 120.1–2, 155.2–5, 109.2–6, 43.2, 61.2, 81.2–3, 137.2–7, 57.2, 247.2.
- Under `## Flags this node raised` (20): 128.1, 107.1–3, 133.1–4, 136.1–2, 139.1–3, 138.1–7.
- Under `## Answer` (9): 216.2–6, 248.2–5.
- Under `## Annotation…` (7): 103.2–6, 242.3, 95.1.
- Under `## Review` (5): 143.6–8, 166.4, 268.3.
- Under `## The manager's own flag, against itself` (4): 213.1–4.
- Under `## The checker` (3): 103.7–9.
- Under `## The manager's disposal` (2): 267.4, 283.5.
- One each:
  - `## The worker reissued its handover…`: 150.5
  - `## Flag \`200.3\`…`: 200.3
  - `## Superseded, 2026-09-26`: 192.1
  - `## Retrospective…`: 215.3
  - `## Flags — after the correction round`: 218.3 (also mid-paragraph) and 218.4
  - `## The manager's disposal of the retrospective's record items`: 248.6
  - `## Second amendment to the acceptance condition…`: 166.5
  - `## Flags, correction round 1`: 220.4
  - `## The manager's note at resolution` on node 178: 207.1
- Prefixed `- ` (9): 26.1–26.9; 26.2, 26.3, 26.4, 26.6 and 26.7 are also mid-paragraph list items.
- Prefixed `~~` (3): 299.1, 299.3, 296.3, for example ``~~`299.1` `ASSUMPTION`~~ **· settled** …``.
- Mid-paragraph (1): 140.9 (`140-…md:224`).

**f. Index `[x]` but the entry's marker sits after the kind marker, not directly after the id (387).** The usual form is ``NN.k` `ASSUMPTION` **· settled** …` (also ``**settled**``), where the reading rule requires ``NN.k` **· settled** `ASSUMPTION``. So by the rule these entries are not settled. To pass: move `**· settled**` to directly after the id. The ids:
27.2, 29.1–3, 30.1–4, 34.1, 37.1–3, 39.1–2, 40.1, 41.1–5, 43.1, 44.1–3, 46.1–3, 47.1–2, 50.1–3, 52.1–2, 53.1–6, 54.1–2, 56.1–4, 57.1, 61.1, 67.1–3, 68.1–4, 69.1–3, 78.1–3, 80.1–2, 81.1, 87.1, 89.1, 91.1–3, 94.1–5, 95.2–6, 96.1, 97.1–7, 98.1–2, 100.1–5, 101.1, 102.1–3, 103.1, 105.1, 108.1–3, 109.1, 110.1–3, 111.1, 112.1–3, 113.1–5, 114.1, 115.1–3, 116.1, 117.1–7, 118.1, 119.1–4, 122.1–3, 124.1–3, 129.1–4, 130.1–4, 135.1, 137.1, 141.1–4, 148.1, 149.1, 150.1–4, 155.1, 160.2–5, 161.1, 162.1–2, 163.1–3, 164.1, 165.1–5, 167.1–3, 168.1–2, 172.1, 173.1, 176.1–4, 179.1–2, 181.1–2, 185.1–2, 190.1–8, 195.1, 199.1–3, 202.1–3, 205.1–2, 206.1, 210.1–3, 211.1, 214.1–2, 216.1, 219.1–2, 220.2–3, 225.1–4, 226.1, 228.1, 230.1–2, 233.1, 234.1, 241.1–2, 243.1–4, 247.1, 248.1, 250.1–5, 252.1–2, 253.1–2, 255.1–2, 259.1–2, 260.1, 263.1–4, 264.1–4, 265.1, 266.1–2, 267.1–3, 268.1–2, 269.1, 270.1–2, 272.1–2, 273.1–3, 274.1–2, 275.1–2, 276.1, 277.1–2, 279.1, 280.1, 281.1–3, 283.2–4, 284.1–4, 285.1–4, 309.1, 317.1, 327.1–5, 335.1, 337.1–5, 340.1–2, 342.1–5, 344.1, 345.1–2, 346.1, 347.1, 348.1, 349.1–2, 350.1–2, 351.1–2, 353.1, 355.1–2, 356.1, 357.1, 358.1, 359.1, 360.1–3, 361.1, 362.1–3, 364.1, 365.1–3, 366.1–5, 368.1, 369.1, 370.1–2, 372.1–2, 373.1, 375.1, 377.1, 379.1–3, 380.1, 381.1, 383.1–2, 384.1–3, 385.1–5, 389.1–2, 391.1–2, 392.1–3.

**g. Index `[x]` with no settled marker on the entry at all (9).** The ids are 184.1–3, 193.1–2, 194.1–2, 220.1 and 359.2, for example ``184.1` `ASSUMPTION` — I judged the divergence…``. 220.1 and 359.2 read `**· withdrawn by …**`. To pass: mark each entry ``**· settled**``.

**Not failures under check 6:**
- `144.5` reads `` `144.5` **· settled** `LICENCE` `` and its line is `[x]`. It passes check 6; no check tests marker vocabulary.
- `MANAGER-WRONG` and `SPAWN-WRONG` markers also appear.
- `207.1`'s index line links node 178 rather than node 207. Its entry sits on node 178. Check 6 compares ids only.
- Id-less legacy entries on nodes cannot be detected as entries by the line-anchored rule, so only their index lines (group a) show up.

### Check 7: FAIL as stated (1 borderline); otherwise passed
- `140-move-the-implementers-and-checkers-material-out-of-the-map.md` (resolved, so it was claimed) has its condition under `## Acceptance condition — written in part, deliberately…` and `## Acceptance condition — completed, and superseding the partial one above`. There is no bare `## Acceptance condition` heading, but the content is present. To pass: a heading reading exactly `## Acceptance condition`.
- Eight implementation nodes have no condition: 32, 72, 170, 192, 238, 239, 240, 303 and 308. Their states are superseded/out-of-scope, plus 240 resolved. Git history shows no `Status: claimed` was ever written in any of them, so they pass. Node 240 was resolved without a claim.

### Check 8: PASSED
No node has more than two `### Attempt N` blocks under `## Interview`. Node 22's Attempts 4–6 sit under `## Review`.

### Check 9: no failure under the strict line reading; 43 failures under the blockquote reading
- Only two labels stand alone on their own line: `296-…md:518` and `:594`, both with `- ESTABLISHED BY the manager · …`, so both pass. The labels on nodes 126 and 144 are inside fenced blocks and are skipped by the rule.
- 50 labels are blockquoted pasted checker output, `> NOT COVERED:`. Their items open with neither `OWED` nor `ESTABLISHED BY`, and every one is on a resolved node.
- 43 of them are in `## Review` / `## Review, continued`: nodes 109:320, 124:481, 137:367, 156:218, 156:334, 160:331, 190:197, 198:226, 202:212, 226:229, 230:180, 260:296, 269:265, 285:354, 327:173, 333:281, 335:127, 336:227, 337:303, 338:230, 339:260, 340:171, 342:224, 343:91, 344:116, 346:147, 347:127, 348:171, 350:182, 351:120, 352:168, 354:142, 357:142, 364:169, 364:230, 370:173, 370:219, 379:172, 379:437, 44:228, 44:312, 56:310, 97:272.
  - Example, `342:225`: `> - Whether the worker marked the node or wrote to \`decisions.md\` or \`flags.md\`. …`
  - Five of them (160, 226, 230, 352, 354) hold the single item *"None of the condition's parts is uncovered."*
- 7 more are outside a `## Review` section: 103:432 and 103:656 (`## The checker`), 218:416, 333:431, 336:302, 336:375 and 379:306.
- To pass: open each item with `ESTABLISHED BY <who> · <what>`, or rule that a blockquoted label is quoted checker text and not a label.

### Check 10: report (32 items over 500 bytes)
Sizes come from the `derivations.md` (h) script, which removes `*"…"*` human quotations. I ran it unchanged over `map.md`, and over `map-manager-only.md` by swapping only the file name. `map-implementation-rules.md` has no `## Notes`.

`map.md` (17 items):

| Bytes | Line | Opening |
|---|---|---|
| 1043 | 28 | Skills every session should consult |
| 1078 | 36 | The node files are written for agents |
| 1778 | 37 | An in-place update never deletes |
| 1203 | 38 | The shipped files should not depend on the `mattpocock-s…` |
| 871 | 39 | The rules a checker holds work against are given to it |
| 804 | 41 | A standing rule binds this effort only once it is written |
| 1116 | 42 | Nodes are grouped by file |
| 618 | 44 | A decision of the human's own may be proposed for change |
| 1234 | 46 | Where an implementation worker sees that its acceptance… |
| 1218 | 47 | A fact about the record is derived rather than stored |
| 531 | 51 | The workflow will also be run on repositories this machine… |
| 1038 | 53 | Claude tokens are scarce |
| 971 | 55 | The graph is ~~six~~ seven files |
| 1232 | 57 | The workflow is named `/expedition` |
| 1085 | 59 | This `## Notes` section also carries two optional blocks |
| 526 | 75 | 5. Write plain English |
| 773 | 76 | 6. Point at a heading of another shipped file |

`map-manager-only.md` (15 items):

| Bytes | Line | Opening |
|---|---|---|
| 746 | 17 | The dogfood target is Lang |
| 790 | 19 | The order the manager works the frontier in |
| 1038 | 51 | Two rulings the human gave at the pilot's gate |
| 524 | 57 | *Moved verbatim from `map.md`'s `## Notes`* |
| 1682 | 59 | The human is asked one question at a time |
| 591 | 61 | A payload goes over as soon as it is ready |
| 858 | 63 | A gate payload does not carry a command that prints a diff |
| 1191 | 74 | The manager never idles |
| 1642 | 78 | Approving a node's end settles that node's flags |
| 4946 | 80 | Every worker returns a retrospective as the last handover part |
| 935 | 82 | Token-use improvement is prioritised |
| 599 | 84 | A standing yes is in force |
| 1799 | 86 | An agent is resumed wherever it can be resumed |
| 808 | 88 | The moved-standard licence is spent |
| 595 | 96 | The steering that the manager never asks the human which w… |

### Check 11: concerns changes, so I checked it over git history
The working tree is clean, so no change is pending. I compared parent and commit for all 94 non-root commits on HEAD that touch `map.md`, `map-manager-only.md`, `map-implementation-rules.md` or `map-history.md`.

**Half 1 (history only grows): decided exactly. FAIL in 2 commits.**
- `6fb738bfe` ("Graph state: nodes 59, 64, 68 and 69 resolved") rewrote `map-history.md:97`, the line *"- **The implementation nodes that write the actual skill files** — …"*, in place.
- `2c690542f` ("Carry the worktree lifecycle into the implementation contract…") inserted a block at line 60 (`### The landing policy in the form it had before worktrees`) instead of appending it.
- These are past commits and cannot be made to pass now. The remedy is to record the breach.

**Half 2 (removed text appears in what the commit appended): approximate.** The check does not define a "passage", so I diffed word by word and tested each removed span for an exact substring match against the appended text. A small span (a single word) can match by chance. Results:
- 61 spans are "nowhere": not in the appended text and not anywhere in the map files afterwards. 3 more are only in older `map-history.md` text.
- 1 span matches the appended text only after re-wrapping.
- 192 spans were moved to another map file rather than to history. Read literally, the check fails these too.
- Commits with spans that are nowhere or only in older history:
  - Before `map-history.md` existed, so they could not comply: `f5712bfd2`, `4bcd34131`, `0a813b273`, `49e77f2d9`.
  - Since then: `8a39024ec`, `f10d8ca9f`, `85e2fc293`, `68ec79172`, `4e38c11e7`, `9c0695556`, `37a3d288a`, `8bb5d0223`, `c6b61fc2b`, `b4595b323`, `3729849bf`, `38709b791`, `8933f1d65`, `084aae906`, `175c4ebae`, `a66424328`.
  - The most recent is `a66424328` (2026-10-02, "State the implementation standards once in the rules file"). It removed the span `` `/writing-for-agents`; and the node's acceptance condition — the last two added at [node 184](…) `` from `map-implementation-rules.md:39`.
  - `3729849bf` removed the "**Banked questions are handed over as they arrive…**" bullet at `map.md:37`–`43`, and its words are not in that commit's appended text.

**What I could not establish:** which spans are true "passages" and which are in-place word edits; whether a move between map files counts as a removal; and whether the check should apply to commits made before it existed. Each half-2 item above needs a human reading before it becomes a node.

### Summary
| Check | Result |
|---|---|
| 1 | FAIL, 1 |
| 2 | FAIL, 5 |
| 3 | FAIL as stated, 1 (id 187; history shows it was skipped, not reused) |
| 4 | PASSED |
| 5 | FAIL, 17 (14 missing `## Answer`, 3 `decisions.md` counts), plus 1 borderline (node 13) |
| 6 | FAIL, about 525 |
| 7 | 1 borderline (node 140's heading form); otherwise PASSED |
| 8 | PASSED |
| 9 | 0 strictly; 43 (+7 outside `## Review`) under the blockquote reading |
| 10 | 32 items reported (17 in `map.md`, 15 in `map-manager-only.md`) |
| 11 | Half 1 FAIL in 2 commits; half 2 approximate, 20 commits with spans found nowhere, plus 192 spans moved within the map |

Check 6 breaks down as:
- 20 id-less lines
- 1 duplicate id
- 4 outstanding entries with no line
- 1 line with no entry
- 103 entries that are not `## Flags` entries
- 387 settled markers in the wrong position
- 9 entries with no settled marker
`````
