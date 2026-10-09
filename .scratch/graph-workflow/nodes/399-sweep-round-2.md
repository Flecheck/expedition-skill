# Sweep round 2, after the round 1 repairs

Type: precondition
Status: resolved
Blocked by: none

## Answer

The second sweep, on 2026-10-09, found nothing new. Checks 1, 2, 3, 4, 7, 8, 9 and 11 pass. Check 10 reports the same 32 oversized items. The remaining failures under checks 5 and 6 are all older records that the human chose, at [node 396](396-sweep-round-1.md), to leave as records of what happened.

*The manager's note:* minted by the manager to hold the sweep round's report, which the effort closing report carries. The round ran after nodes [397](397-make-the-check-reading-rules-match-the-record-as-written.md) and [398](398-fix-the-small-graph-defects-the-first-sweep-found.md) landed.

## Question

Does a second whole-graph run of the mechanical checks find anything new after round 1's repairs?

## The sweep agent's report

*Pasted as the read-only agent handed it back, 2026-10-09.*

`````
## Sweep round 2: `.scratch/graph-workflow/`, all 11 mechanical checks

I wrote nothing in the repo, and the working tree is clean. My scripts were in `$TMPDIR/sweep2` and I have removed them. I read the files by the current `### How a check reads the files` rules. Fields come only from the header block. Fenced blocks are skipped. `Blocked by:`, `Supersedes:` and `Superseded by:` numbers are taken from outside code spans, strikethrough and link targets. Paragraphs and list items are unwrapped before matching. A flag's node, and a `decisions.md` entry's node, is the first link on the line. A flag counts as settled only where `**· settled**` stands directly after the kind marker or directly after the id.

The graph has 397 node files, numbered 1–398 with 187 skipped. Their statuses are 309 `resolved`, 72 `superseded` and 16 `out-of-scope`. None is open or claimed, so the frontier is empty.

### Check 1: PASSED
- **New:** none.
- **Left by the human:** none.
- **Round 1 items that now pass:** node 164 now reads `Blocked by: 143, ~~151~~ 334`, which gives 143 and 334, and both are resolved.

### Check 2: PASSED
- **New:** none.
- **Left by the human:** none.
- **Round 1 items that now pass:** all 5. Nodes 76, 143, 100 and 311 now carry `Supersedes: 61`, `72`, `192` and `279`. Node 332 now reads `Supersedes: 90, 92, 134, 247, 81`. Every `Superseded by:` has its back-edge, and every `Supersedes:` has its forward edge.

### Check 3: PASSED
- **New:** none.
- **Left by the human:** none.
- **Round 1 items that now pass:** id 187. No file numbered 187 exists in git history on any ref, so it is a skipped number under node 397's reading rule. Ids 1–398 are each used once, with no duplicates.

### Check 4: PASSED
No node carries `Labels:` in its header, and `map-manager-only.md` reads "Label vocabulary for this effort: none declared." The only `Labels: EFF, REG` line is in node 13's body, which is not a header.

### Check 5: FAIL, 14, plus 1 borderline
- **New:** none.
- **Left by the human (no `## Answer` heading), 14 resolved nodes:** 95, 166, 218, 242, 244, 249, 255, 260, 267, 268, 269, 274, 277, 281.
  - Nine of them carry their answer under `## What the work states`: 95, 255, 260, 267, 268, 269, 274, 277, 281.
  - Five have no answer-like section: 166, 218, 242, 244, 249.
  - To pass: an `## Answer` section on each.
- **Borderline, as in round 1, and not counted:** node 13 has two unstruck `decisions.md` units whose first link is node 13.
  - One is its real entry at line 34.
  - The other is the preamble paragraph at lines 9–11, which ends "…capped by [Graph file format](nodes/13-graph-file-format.md)." Once unwrapped, its first link is node 13.
  - To pass: rule that only list-item lines are entries, or move the citation so it is not the paragraph's first link.
- **Round 1 items that now pass:** all three `decisions.md` counts.
  - Node 131: line 220 is struck, and line 219 is its one unstruck line.
  - Nodes 218 and 243: each has one unstruck line (335 and 336) beside its struck one.
  - The new nodes 397 and 398 each have an `## Answer` and exactly one line.

### Check 6: FAIL, 173 (20 + 1 + 104 + 48)
`flags.md` has no unchecked line outside its fenced format example, so every one of the 173 sits on a `- [x]` line.
- **New:** none. Flags 397.1 and 398.1–398.6 pass.
- **Left by the human (older flag drift):**
  - **a. 20 lines with no id**, `flags.md:43`–`62` (the legacy lines for nodes 12, 14, 20, 21, 23 and 24). Example, line 43: `- [x] ASSUMPTION · [Naming the workflow and its vocabulary](nodes/14-naming.md) — wrote `CONTEXT.md` …`. To pass: give each line, and its node entry, an id.
  - **b. 1 duplicate id**, `190.1`, at `flags.md:367` and `:714`. To pass: re-id one of them.
  - **d. 1 index line with no entry anywhere.** `flags.md:363`, `- [x] 160.1 CONDITION-WRONG · …`; node 160's `## Flags` starts at 160.2. To pass: file the 160.1 entry under node 160's `## Flags`.
  - **e. 103 index lines whose entry is not a `## Flags` entry.** The list is identical to round 1's. To pass: put each entry under `## Flags`, at the start of its own paragraph.
    - Under `## Amendment …`: 296.4, 148.2–6, 258.1, 120.1–2, 155.2–5, 109.2–6, 43.2, 61.2, 81.2–3, 137.2–7, 57.2, 247.2.
    - Under `## Flags this node raised`: 128.1, 107.1–3, 133.1–4, 136.1–2, 139.1–3, 138.1–7.
    - Under `## Answer`: 216.2–6, 248.2–5.
    - Under `## Annotation…`: 103.2–6, 242.3, 95.1.
    - Under `## Review`: 143.6–8, 166.4, 268.3.
    - Under other headings:
      - 213.1–4 under `## The manager's own flag, against itself`.
      - 103.7–9 under `## The checker`.
      - 267.4 and 283.5 under `## The manager's disposal`.
      - 150.5, 200.3, 192.1, 215.3, 218.3, 218.4, 248.6, 166.5 and 220.4, one each under its own heading.
      - 207.1, which sits on node 178.
    - Prefixed with `- `: 26.1–26.9.
    - Prefixed with `~~`: 299.1, 299.3, 296.3.
    - Mid-paragraph: 140.9.
  - **f/g. 48 `- [x]` lines whose entry has no recognised settled marker:**
    - **38 written `**settled**`, without the `·`.** Example, node 100:86: `` `100.1` `ASSUMPTION` **settled** — … ``. The ids are 46.1–3, 91.1–3, 94.1–5, 98.1–2, 100.1–5, 102.1–3, 103.1, 114.1, 116.1, 117.1–7, 119.1–4 and 122.1–3. These are the remnant of round 1's group f.
    - **1 with extra words:** 27.2, `` `27.2` **· settled, and overruled** `ASSUMPTION` ``, also from group f.
    - **9 with no settled marker** (round 1's group g): 184.1–3, 193.1–2 and 194.1–2. 220.1 and 359.2 read `**· withdrawn by … in correction round 1**`.
    - To pass: mark each entry `**· settled**` after the kind marker.
- **Round 1 items that now pass:**
  - **Group c:** 265.2, 265.3, 265.4 and 283.1 now have `flags.md` lines 859–862 and settled marks on their entries.
  - **Group f:** 348 of its 387 now pass, because the reading rule accepts the marker after the kind marker.

### Check 7: PASSED
- **New:** none.
- **Left by the human:** none.
- **Round 1 items that now pass:** node 140's suffixed headings (`## Acceptance condition — written in part…` and `— completed…`) now count, under node 397's rule.
- **Not a failure:** nine implementation nodes have no condition: 32, 72, 170, 192, 238, 239, 240, 303 and 308. As round 1 established from git, none was ever claimed. None of their files changed since round 1.
- Nodes 397 and 398 both have conditions.

### Check 8: PASSED
No node has more than two distinct attempt numbers under `## Interview`.

### Check 9: PASSED
- **New:** none.
- **Left by the human:** none.
- **Not a failure:** only two `NOT COVERED:` labels stand alone outside a blockquote and outside a fence, at node 296:518 and 296:594. Both items open `- ESTABLISHED BY the manager · …`.
- **Round 1 items that now pass:** all 50 of round 1's blockquoted `> NOT COVERED:` labels, which are now quoted text under node 397's rule.
- There are now 51 blockquoted labels. The new one is node 398's pasted checker run 1. Its three parts are recorded as established by the manager in the gate note's prose, which no check reads.

### Check 10: report, 32 items over 500 bytes (unchanged from round 1)
I ran the `derivations.md` (h) script over `map.md`, `map-manager-only.md` and `map-implementation-rules.md`. The last has no `## Notes`. No map file has changed since round 1, and every size and line is identical to round 1's tables.

`map.md` (17):

| Bytes | Line |
|---|---|
| 1043 | 28 |
| 1078 | 36 |
| 1778 | 37 |
| 1203 | 38 |
| 871 | 39 |
| 804 | 41 |
| 1116 | 42 |
| 618 | 44 |
| 1234 | 46 |
| 1218 | 47 |
| 531 | 51 |
| 1038 | 53 |
| 971 | 55 |
| 1232 | 57 |
| 1085 | 59 |
| 526 | 75 |
| 773 | 76 |

`map-manager-only.md` (15):

| Bytes | Line |
|---|---|
| 746 | 17 |
| 790 | 19 |
| 1038 | 51 |
| 524 | 57 |
| 1682 | 59 |
| 591 | 61 |
| 858 | 63 |
| 1191 | 74 |
| 1642 | 78 |
| 4946 | 80 |
| 935 | 82 |
| 599 | 84 |
| 1799 | 86 |
| 808 | 88 |
| 595 | 96 |

### Check 11: PASSED for the commits since round 1
- Thirteen commits follow 62fba95a2, from 34414fd04 to cc25a35f8. None touches `map.md`, `map-manager-only.md`, `map-implementation-rules.md` or `map-history.md`, so neither half can fail. The working tree is clean.
- **Earlier commits, carried by the human's decision without a node:** round 1 found half 1 breached in 2 commits (6fb738bfe and 2c690542f). It found half 2 breached, approximately, in 24 commits: 4 before `map-history.md` existed and 20 after. I did not re-examine them.

### Summary

| Check | Result | New | Left by the human | Round 1 items now passing |
|---|---|---|---|---|
| 1 | PASSED | 0 | 0 | 1 (node 164) |
| 2 | PASSED | 0 | 0 | 5 back-edges |
| 3 | PASSED | 0 | 0 | 1 (id 187, skipped) |
| 4 | PASSED | 0 | 0 | — |
| 5 | FAIL, 14 (+1 borderline, node 13) | 0 | 14 missing `## Answer` | 3 (`decisions.md` counts for 131, 218, 243) |
| 6 | FAIL, 173 | 0 | 20 id-less, 1 duplicate id, 1 line with no entry, 103 not `## Flags` entries, 48 no recognised settled marker | 4 (group c) + 348 of group f |
| 7 | PASSED | 0 | 0 | 1 borderline (node 140) |
| 8 | PASSED | 0 | 0 | — |
| 9 | PASSED | 0 | 0 | 50 blockquoted labels |
| 10 | 32 reported (17 in `map.md`, 15 in `map-manager-only.md`), unchanged | — | — | — |
| 11 | PASSED (no commit since 62fba95a2 touches a map file) | 0 | earlier: half 1 in 2 commits, half 2 in 24 commits | — |

Round 2 found nothing new. Every remaining failure is one the human chose at node 396 to leave as a record: the old flag drift under check 6, and the missing `## Answer` headings under check 5.
`````
