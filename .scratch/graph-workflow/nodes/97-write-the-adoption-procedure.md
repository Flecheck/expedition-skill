# Write the adoption procedure

Type: implementation
Status: resolved

Blocked by: ~~18~~

## Question

*Surfaced by [Adopting an in-flight effort](18-adopting-in-flight-effort.md)'s worker, and pasted as it wrote it.*

> Write the file that tells a manager how to start an effort from a directory of work that already exists. This is
> the second of the two pieces the map's fog item *"The implementation nodes that write the actual skill files"*
> names, and the one it says waits on node 18.

**Blockers, in the worker's words:** *"58. Node 58 qualifies the graph-file ban so that a worker whose own node's
work is a change to a graph file makes that change itself. The procedure this node writes hands the bulk import to
workers, so if 58 does not land the procedure has no performer to name."*

**The manager's note at filing:** [node 58](58-qualify-the-graph-file-ban.md) has since been approved and landed as
commit `392e0ae`, so that blocker is discharged and is not carried in the header. What remains is `Blocked by: 18`,
this node's source, which is `resolved`.

## Acceptance condition

*Written by node 18's worker. Pasted as it wrote it, and not the manager's.*

> A file exists at `.claude/skills/expedition/adoption.md`. It is instructions to a manager starting an effort from a
> directory of work that already exists, and it states all of the following. Each is judged as a property of what the
> text says, never as particular wording.
>
> 1. That adoption is a mode of starting an effort rather than a kind of node, and that the manager performs it
>    before the graph exists.
> 2. That the manager's own act is bounded and ends by minting the bulk import as the graph's first nodes, whose kind
>    is `precondition` — rather than the manager writing the imported node files itself.
> 3. The steps of the manager's own act, in order: taking the effort's name from the directory that already exists;
>    resolving any of the reserved graph names (`map.md`, `map-history.md`, `decisions.md`, `flags.md`, `nodes/`)
>    that the directory is already using for something else; writing `map.md` with its destination, its notes, the
>    effort's ground rules and its standing over sources copied from what the effort already wrote rather than
>    invented; declaring the label vocabulary from the foreign label families; appending the expedition section to
>    the target repository's tracker doc where it has one; creating the remaining graph files empty; and minting the
>    import nodes.
> 4. The rule for a reserved name already in use: the existing file's content moves verbatim into the node files that
>    now hold it, and the reserved name is then rewritten to its expedition meaning. Nothing is summarised, shortened
>    or discarded on the way.
> 5. That the import transcribes the foreign corpus as it stands and reconciles nothing, and that a question the
>    foreign record has already answered is imported as an ordinary node and resolved afterwards by ordinary graph
>    work.
> 6. That the bulk import runs in two passes — one minting every node file, splittable and parallel; a second wiring
>    the blocking edges from the foreign prose, which is single because inverting an edge needs the whole
>    foreign-label-to-number mapping at once.
> 7. That a foreign identifier survives in the node's free-form filename and never as a field, and that foreign prose
>    moved into a node keeps its own words while newly written prose does not adopt them.
> 8. The rule for which foreign files import as nodes and which are linked from the map: a file holding questions or
>    decisions imports, a file holding research output is linked, and a file that is genuinely either gets a node of
>    its own rather than being decided by the import.
> 9. That a foreign status maps onto an expedition status, and that where the foreign record already names one thing
>    as superseding another, both directions of the supersession edge are written so the pair is complete.
> 10. That adoption changes nothing about the target repository's git history, and that no existing commit is
>     attributed to an imported node.
> 11. That citations inside imported material are repointed by a lookup table the manager builds once before the
>     import and the import applies mechanically, and that building the table is part of the manager's own act.
>
> The file is instructions and not an account: it narrates no particular effort's adoption, and it contains no
> passage that only makes sense to a reader who already knows the `Lang` repository.
>
> Nothing outside `.claude/skills/expedition/` changes. Within it, only the new file, plus optionally a pointer to it
> added to `SKILL.md` and to the closing section of `wayfinder-divergences.md`. No file under `.scratch/` changes.
>
> The work leaves the tree meeting the bar.

## Amendment, 2026-09-24

*Written by [node 299](299-rewrite-graph-conventions-part-1.md)'s worker and filed by the manager, after that node's work landed as commit `0d406b7`. Every word of the replacement is fixed by that commit: it quotes `graph-conventions.md`'s after-text. The minting author's condition above is left as it was. The replacement takes the place of the clause it names. Node 299's worker searched every open node's `## Acceptance condition` for quoted spans of its before-range, matched literally and normalised with each condition joined into one string, and for each phrase its rewrite removed or replaced. The full list of handles is on node 299 under `### Re-pointing duty` and correction rounds 1 to 3.*

- **Clause 3.** It says "the effort's ground rules and its standing over sources copied from …". Replace "its standing over sources" with "its declaration of which sources are authoritative, which are evidence only, and which hold statements known to be false".

## Flags

`97.1` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 299](299-rewrite-graph-conventions-part-1.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `0d406b7`.

`97.2` `ASSUMPTION` **· settled** — *From attempt 1's handover.* The condition lists five reserved names, taken from node 18, and I listed all seven. Since node 139, `graph-conventions.md`'s `## The seven files` also reserves `map-manager-only.md` and `map-implementation-rules.md`, and a foreign file on either would collide in exactly the same way. — `adoption.md` reserves all seven graph file names, not the five its condition listed, because two map files were added after node 18.

`97.3` `ASSUMPTION` **· settled** — *From attempt 1's handover.* Node 18 says a reserved-name file "moves" but never says how, when the manager must resolve the collision before any node file exists. I decided that the manager renames the file to a free name, pass one transcribes it, and pass two removes it, since at that point every entry is in a node file. The never-delete rule covers only the graph's own files, and the text is not lost because it moved verbatim. — A foreign file on a reserved graph name is renamed by the manager, transcribed by pass one and removed by pass two.

`97.4` `ASSUMPTION` **· settled** — *From attempt 1's handover.* Node 18 was silent on three mechanics that parallel pass-one nodes and a correct frontier need, and I decided all three. Each pass-one node gets a number range that overlaps no other, and later nodes are numbered above the highest range. Pass two sets `superseded` together with its edges. No imported node is started before the pass-two node resolves. — Parallel pass-one import nodes get disjoint number ranges, and no imported node starts until the pass-two edge-wiring node resolves.

`97.5` `ASSUMPTION` **· settled** — *From attempt 1's handover.* The kind of an imported node is the foreign kind where that is one of the five, and otherwise `grilling`, on the ground that a question the foreign record holds open is one the human decides. A file that could either import or be linked gets a `grilling` node, and its question is which. — An imported node without a matching foreign kind is `grilling`, and so is the node that decides whether an ambiguous foreign file imports.

`97.6` `ASSUMPTION` **· settled** — *From attempt 1's handover.* The worker contracts' hard rule 2 ends "create no node yourself". An import worker could read that as forbidding the very files it exists to write. I resolved it inside `adoption.md`, not in the contracts: the import node's question names the node files it writes as its own node's work and not nodes it found, so hard rule 1's graph-file clause covers them. If a real import worker still stops on this, the repair belongs in the five worker contracts. — `adoption.md` casts the import's node files as the node's own work, so the contracts' "create no node yourself" does not block the import.

`97.7` `ASSUMPTION` **· settled** — *From attempt 1's handover.* Node 18's step 5 said the `wayfinder-divergences.md` block needs one more line saying the effort was adopted and where its nodes are. I put that line in `adoption.md`'s step 5, not in the block, which keeps `wayfinder-divergences.md` to a pointer as the condition allows. A tracker doc of another scheme gets that one line only. — The line saying an effort was adopted and where its nodes are is specified in `adoption.md`, not added to the wayfinder block.

## Answer

`adoption.md` ships the manager's seven adoption steps, the two-pass `precondition` import, reserved-name renaming, status mapping, the citation table and git non-interference, with pointers from `SKILL.md` and `wayfinder-divergences.md`.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `c3f99d1`. Flags 97.1 to 97.7 settle at the node closing report. The worker's related defect for node 56 is filed there as clause 6a.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      Write the adoption procedure

ANSWER:
**`.claude/skills/expedition/adoption.md` now exists.** It tells the manager how to start an effort from a directory of work that already exists. It holds only the steps adoption adds to `## Starting an effort` in `SKILL.md` and `### Start an effort` in `graph-conventions.md`, and it refers the reader to both. Two pointers were added: one sentence at the end of `SKILL.md`'s `## Starting an effort`, and a rewrite of `wayfinder-divergences.md`'s `## Not covered here`. The old text there used "Importing an effort" as the name of the whole act, which the glossary refuses.

The file's sections:
- The intro. Adoption is a way of starting an effort and not a kind of node. The manager performs it before the graph exists, and the manager's part is bounded. That part ends when the manager mints the bulk import as `precondition` nodes. The manager writes no imported node file.
- `## Your steps, in order`. Seven steps, in the condition's order:
  1. Take the name from the directory.
  2. Rename away any foreign file on a reserved name.
  3. Write `map.md` from what the effort already wrote. Ground rules are copied verbatim. The source declaration is built from the record's own statements about its sources, using the three terms. Where the record is silent, the manager asks the human.
  4. Declare the label families in `map-manager-only.md`.
  5. Append the `wayfinder-divergences.md` block to the tracker doc, plus one line saying the effort was adopted and where its nodes are.
  6. Create the remaining files empty.
  7. Mint the import nodes. Four sub-steps: sort the foreign files, build the citation table, mint the pass-one and pass-two nodes, and run checks 1, 3 and 4.
- `## A reserved name already in use`.
- `## The bulk import`, with `### What an imported node looks like`.
- `## Which foreign files import`.
- `## Citations inside imported material`.
- `## Git history`.

Calls a later reader would otherwise have to re-derive:
- **The reserved names are all seven graph files.** The list is `map.md`, `map-history.md`, `map-manager-only.md`, `map-implementation-rules.md`, `decisions.md`, `flags.md` and `nodes/`. The condition listed five because it predates the split into seven files.
- **A reserved-name collision is resolved by renaming.** The manager renames the foreign file to a name the graph does not use. Pass one transcribes it into node files verbatim. Pass two then removes the renamed file, because by then every entry of it is in a node file.
- **Pass-one nodes get number ranges.** Each gets a range no other range overlaps, larger than its share. A node added after the import takes a number above the highest range. Pass two builds the foreign-identifier-to-number mapping from the node filenames.
- **Pass two writes every edge that names another node.** That is `Blocked by:`, `Supersedes:` and `Superseded by:`. It also sets `superseded` statuses, so a replaced entry is `open` until pass two runs.
- **No imported node is started until the pass-two node resolves.**
- **An imported node's kind** is the foreign kind where that is one of the five, and `grilling` otherwise. A file that could either import or be linked gets a `grilling` node of its own.
- **Status mapping:**
  - decided → `resolved`, with the entry's text as `## Answer` and a line in `decisions.md`;
  - replaced by another entry → `superseded`, with both edge directions;
  - ruled beyond the effort → `out-of-scope`, with a line in `## Out of scope`;
  - set aside to return to → `open`, with `## Interview`;
  - anything else → `open`.
- **Each import node's `## Question` carries three things:** its files or entries, its number range, and the lookup table. It also says that the node files it writes are its own node's work, and not nodes it found.

INDEX LINE:    `adoption.md` ships the manager's seven adoption steps, the two-pass `precondition` import, reserved-name renaming, status mapping, the citation table and git non-interference, with pointers from `SKILL.md` and `wayfinder-divergences.md`.

FLAGS:
ASSUMPTION: The condition lists five reserved names, taken from node 18, and I listed all seven. Since node 139, `graph-conventions.md`'s `## The seven files` also reserves `map-manager-only.md` and `map-implementation-rules.md`, and a foreign file on either would collide in exactly the same way. — Index: `adoption.md` reserves all seven graph file names, not the five its condition listed, because two map files were added after node 18.
ASSUMPTION: Node 18 says a reserved-name file "moves" but never says how, when the manager must resolve the collision before any node file exists. I decided that the manager renames the file to a free name, pass one transcribes it, and pass two removes it, since at that point every entry is in a node file. The never-delete rule covers only the graph's own files, and the text is not lost because it moved verbatim. — Index: A foreign file on a reserved graph name is renamed by the manager, transcribed by pass one and removed by pass two.
ASSUMPTION: Node 18 was silent on three mechanics that parallel pass-one nodes and a correct frontier need, and I decided all three. Each pass-one node gets a number range that overlaps no other, and later nodes are numbered above the highest range. Pass two sets `superseded` together with its edges. No imported node is started before the pass-two node resolves. — Index: Parallel pass-one import nodes get disjoint number ranges, and no imported node starts until the pass-two edge-wiring node resolves.
ASSUMPTION: The kind of an imported node is the foreign kind where that is one of the five, and otherwise `grilling`, on the ground that a question the foreign record holds open is one the human decides. A file that could either import or be linked gets a `grilling` node, and its question is which. — Index: An imported node without a matching foreign kind is `grilling`, and so is the node that decides whether an ambiguous foreign file imports.
ASSUMPTION: The worker contracts' hard rule 2 ends "create no node yourself". An import worker could read that as forbidding the very files it exists to write. I resolved it inside `adoption.md`, not in the contracts: the import node's question names the node files it writes as its own node's work and not nodes it found, so hard rule 1's graph-file clause covers them. If a real import worker still stops on this, the repair belongs in the five worker contracts. — Index: `adoption.md` casts the import's node files as the node's own work, so the contracts' "create no node yourself" does not block the import.
ASSUMPTION: Node 18's step 5 said the `wayfinder-divergences.md` block needs one more line saying the effort was adopted and where its nodes are. I put that line in `adoption.md`'s step 5, not in the block, which keeps `wayfinder-divergences.md` to a pointer as the condition allows. A tracker doc of another scheme gets that one line only. — Index: The line saying an effort was adopted and where its nodes are is specified in `adoption.md`, not added to the wayfinder block.

NEW NODES:
Join to open node 56, "Ship the glossary inside the skill directory and make it state its own completeness" (unclaimed). The new `.claude/skills/expedition/adoption.md` names the glossary as `CONTEXT.md`. Clause 6 of node 56's condition repoints only `graph-conventions.md`, so after node 56 lands this new file would point at the old name. Clause to add, read under node 56's existing amendment that substitutes `glossary.md`:
> 6a. Wherever `.claude/skills/expedition/adoption.md` names the glossary, it names `glossary.md`, the file beside it in `.claude/skills/expedition/`.
Words fixed by: node 56's own amendment (the human's choice of `glossary.md`, 2026-09-25) and this work landed in the tree.

INVALIDATIONS:
- Node 18, "Adopting an in-flight effort", is extended and narrowed in two ways. First, its "Five names are the graph's" is now seven (see the first flag). Second, its "a question marked superseded ... becomes a `superseded` node" is carried out in two steps: `open` in pass one, then `superseded` in pass two. Its example "a retired one becomes `out-of-scope`" is written as "ruled beyond the effort", because the glossary uses "retired" to name supersession.
- `wayfinder-divergences.md`'s old `## Not covered here` sentence, "Importing an effort ... is a separate procedure", is replaced by a pointer to `adoption.md`. This is a rename away from a use of "import" that the glossary refuses.
- No contradiction of any resolved node.

CONDITIONS: I searched every open and claimed node's `## Acceptance condition` for: `adopt`, `adoption`, `adoption.md`, `wayfinder-divergences`, `Starting an effort`, `Start an effort`, `charting`, `migration`, `onboarding`, `separate procedure`, `Not covered here`, `import(ing|ed) an effort`, `reserved name`, `foreign label`, `expedition-precondition`. The only matches outside node 97 were:
- node 137 (claimed; its matches are the precondition contract and `graph-conventions.md`, which I did not touch);
- nodes 109 and 41 (the precondition contract, a different concern);
- node 80 ("unadopted", unrelated);
- node 56's clause 6, a glossary-path clause, handled under NEW NODES as an addition.
No replacement clause is written.

MISSING FROM MAP: `map.md` does not say where an adopted effort's lookup table or number ranges should live, or how an import worker's node-file writes square with "create no node yourself". I went on without it and settled all of it inside `adoption.md` (see flags). I used node 18's `## Answer` for the mechanics the condition compresses. I opened that file because it is this node's resolved source.

GATE PAYLOAD:
- Checker findings: none yet (first run).
- Bar: the repo has no build, tests, formatter or CI, confirmed by the worktree root holding only `CONTEXT.md` and `.claude/` with no manifest. That matches `map-implementation-rules.md`. The bar is therefore its non-command half. The work was checked against the rules file's standards:
  - `CONTEXT.md` `_Avoid_` words: scanned by hand and by grep. I dropped "complete" and "retired".
  - Plain English and one idea per sentence.
  - Citation by heading.
  - Wrap width 104, matching the siblings; no new line exceeds it.
- Paths touched (worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/97-adoption`):
  - `.claude/skills/expedition/adoption.md` (new)
  - `.claude/skills/expedition/SKILL.md` (one sentence at the end of `## Starting an effort`)
  - `.claude/skills/expedition/wayfinder-divergences.md` (`## Not covered here` rewritten to a pointer)
  - Nothing under `.scratch/` in the tree was changed. `CONTEXT.md` and `graph-conventions.md` were not touched.
- Method-skill parts skipped: none invoked.
- Proposed commit message:
```
Ship adoption.md: how the manager starts an effort from existing work

Adds the manager's seven adoption steps, the two-pass precondition
import, the reserved-name rule, the status mapping, the citation table
and git non-interference, with pointers from SKILL.md's Starting an
effort section and wayfinder-divergences.md's closing section.

Node: graph-workflow/97
```

RETROSPECTIVE
1. **What I had to hunt for.**
   - The mechanics behind the condition's compressed clauses: how a reserved-name file "moves" before node files exist, whether decided entries import as `resolved`, and where the tracker-doc line goes. I found them in node 18's `## Answer` (lines 76-201), after looking first in the condition and in `graph-conventions.md`.
   - Whether the precondition contract lets a worker mint nodes. I grepped the five contracts for "create no node".
   - Which open conditions name the glossary path. Found in node 56's clause 6 by search.
2. **What arrived that this node did not need.**
   - `map.md` read whole: about 41 KB, of which roughly the Destination, the Notes' graph-files and vocabulary paragraphs, and the worktree paragraph bore on this node. The standing-preference bullets (gate payload, standing yes, retrospective, token priority, resume) bore on nothing here.
   - `map-implementation-rules.md`'s long paragraphs on record files and supersession of rules bore on nothing.
   - The spawn's note on node 137's report renaming did not apply, since I named neither report. It was cheap.
3. **What would have made this easier.**
   - A line in the node file, or the spawn, saying that node 18's `## Answer`, sections "What the manager itself does" through "Two things adoption deliberately does not do", is the source of the condition's mechanics.
   - A note that the reserved-name list in clause 3 predates the seven-file split.
4. **What was stale, wrong or contradictory.**
   - Clause 3's five reserved names are stale against `graph-conventions.md`'s seven files.
   - Node 18's "a retired one becomes `out-of-scope`" clashes with the glossary, whose `Out of scope` entry refuses "retired" as naming supersession.
   - `wayfinder-divergences.md` used "Importing an effort" as the name of the whole act, which `CONTEXT.md`'s Adoption entry refuses. Now fixed.
   - The contracts' "create no node yourself" is ambiguous against a worker whose own work is minting nodes (see flags).

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 344's check; the condition reached it as a verbatim copy in `$TMPDIR/c97.md`.*

> PASS
>
> This is the check of node 97, "Write the adoption procedure". The work is in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/97-adoption`, on base 89135d3:
> - the new untracked file `.claude/skills/expedition/adoption.md`, which I read in full with `cat -n`;
> - uncommitted diffs to `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition/wayfinder-divergences.md`.
>
> I read the whole condition in `/tmp/claude-1000/c97.md`, with clause 3 as the 2026-09-24 amendment reads it.
>
> **The acceptance condition**
> - **The file exists and is instructions to a manager adopting an existing directory:** met. It opens "This file tells the manager how to start an effort from a directory of work that already exists" and addresses the manager as "you" throughout.
> - **1:** met. "Adoption is a way of starting an effort, and not a kind of node. You perform it, before the graph exists."
> - **2:** met. "Your part ends when you mint the bulk import as the graph's first nodes. Their kind is `precondition`. Workers write the imported node files, and you write none of them yourself."
> - **3 (as amended):** met. `## Your steps, in order` gives, in the demanded order:
>   1. the name comes from the directory;
>   2. reserved names are resolved. It lists the five names the clause gives, plus `map-manager-only.md` and `map-implementation-rules.md`;
>   3. `map.md` is written, taking the destination, the notes, the ground rules copied verbatim and the three-term source declaration from what the effort already wrote, and inventing none of it;
>   4. the label vocabulary is declared from the foreign families;
>   5. the expedition section is appended to the tracker doc where there is one;
>   6. the remaining files are created empty;
>   7. the import nodes are minted.
> - **4:** met. `## A reserved name already in use` says the content "moves verbatim into the node files that now hold it. The reserved name is then rewritten to its expedition meaning. Nothing is summarised, shortened or discarded on the way."
> - **5:** met. `## The bulk import` says the import "transcribes the foreign record as it stands. It reconciles nothing." A question the record has already answered "is imported as an ordinary node… resolved afterwards by ordinary graph work."
> - **6:** met. Pass one mints every node file and "can be split… into several nodes that run in parallel". Pass two is "one node… because inverting an edge needs the whole mapping from foreign identifier to node number at once."
> - **7:** met. Under `### What an imported node looks like`, the foreign identifier "survives in the node's free-form filename… It is never written as a field." Foreign prose "keeps its own words", and new prose "does not adopt the foreign ones".
> - **8:** met. `## Which foreign files import` sends questions and decisions to import, research output to a link, and a file that is genuinely either to "a `grilling` node of its own… The import does not decide it."
> - **9:** met. It gives a mapping from foreign status to expedition status. Where the record names a supersession, "pass two writes both directions of the edge… so the pair has both of its halves."
> - **10:** met. `## Git history` says "Adoption changes nothing about the target repository's git history… No existing commit is attributed to an imported node."
> - **11:** met. `## Citations inside imported material` has the table built before the import, as "part of your own act", and applied "mechanically to every citation it moves". Step 7.2 places building it inside the manager's steps.
> - **Instructions, not an account; nothing that needs knowledge of `Lang`:** met. `grep -niE 'lang\b|Lang '` finds nothing, and the file narrates no effort.
> - **Scope:** met.
>   - `git status --short --untracked-files=all` shows only the new file and the two named files, all inside `.claude/skills/expedition/`. Nothing under `.scratch/` changes.
>   - The `SKILL.md` change adds one sentence at the end of `## Starting an effort`: "Adoption adds steps of its own, which are in `adoption.md`, beside this file."
>   - The `wayfinder-divergences.md` change is confined to its closing section, `## Not covered here`. It replaces "Importing an effort that is already under way is a separate procedure…" with a pointer to `adoption.md` and a one-line summary of what adoption does. I read that as the pointer the condition permits: the old sentence spoke of a separate procedure, and the pointer now names it.
> - **The bar:** met. See below.
>
> **Cross-references I checked resolve:**
> - `wayfinder-divergences.md` has `## Changed` with the block to append.
> - `graph-conventions.md`'s `### Start an effort` has step 9, which runs checks 1, 3 and 4.
> - `expedition-precondition/SKILL.md` has the rule "Write a graph file only where your node's own work is a change to that file", which is the rule step 7 and `## The bulk import` rely on.
>
> **The bar**
> - The repo has no build, tests, formatter or CI, so there are no commands to run.
> - `git diff --check` is clean (exit 0).
> - The new file has no trailing whitespace and no line over 105 characters. It is 8551 bytes; the condition sets no size limit.
>
> **Standards.** As in my earlier checks, I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`.
> - **Bore on the work:**
>   - `CONTEXT.md` `_Avoid_` lines. `grep -noiE` for the distinctive refusals (done, complete, close, finish, ticket, issue, backlog, task, retry, session, migration, onboarding, kickoff, setup, bootstrap, tags, categories, revise, obsolete, retired, wontfix, cancelled, decision) finds nothing in `adoption.md`. The file uses "import" only for the step inside adoption, as the glossary's Adoption entry allows.
>   - The writing rules. Citations are by heading. Bold is used on step leads and bullet leads in the style of the file's siblings. Every "never" has its positive beside it.
>   - `/writing-for-agents`. The file discloses behind a pointer from `SKILL.md`, which keeps the manager contract's top short. Nothing else found.
>   - The ground rules. Git is named only because clause 10 demands it. The file names no command and assumes no machine. Where the manager must ask the human, it is the manager who asks.
> - **Did not bear:** `/coding-principles` and `/naming`.
> - No reviewing skill is named, so I ran none.
>
> NOT COVERED:
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The condition's fence covers `.scratch/`, and the worktree shows no change there. What the main tree's record holds is outside what I was given.

### Gate — approve, `standing yes`, 2026-09-27

Taken under the standing yes recorded in `map.md`'s `## Notes` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and its one NOT COVERED item is the worker's bookkeeping. This settles none of the node's flags; they settle at the node closing report.

*The manager's note, 2026-09-27:* flags 97.1 to 97.7 settle at the node closing report that closes this node, which names its gate as taken under the standing yes.
