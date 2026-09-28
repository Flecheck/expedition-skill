# Nothing in the record says the auto-loaded trigger file exists

Type: implementation
Status: resolved

Blocked by: none

## Question

*Surfaced by [node 218](218-put-the-managers-trigger-duties-where-a-compaction-re-injects-them.md)'s worker, and
pasted as it wrote it.*

> The four trigger-duties now exist in two places: as standing preferences in `map.md`, and as triggers in
> `.claude/rules/expedition-triggers.md`, which the harness loads without anything pointing at it. The new file
> states its own precedence — it holds triggers only and overrides nothing in the map — so which governs is settled.
> What is not settled is the other direction: nothing in the effort's record names the file, so somebody editing the
> map's statement of a duty has no way to know a second statement of it exists, and the two can diverge with nothing
> reporting it. This effort's record keeps an in-place-update discipline precisely to stop that. The work is a
> pointer in the record; where it goes is the open part, `map.md` being read by every worker while the file is a
> manager's concern.

**Blockers, in the worker's words:** *"none. It could not be done inside node 218, whose scope clause closed
`.scratch/` entirely."*

## Acceptance condition

*Written by node 218's worker. Pasted as it wrote it, and not the manager's.*

> The work edits files under `.scratch/graph-workflow/` only, and no file under `.claude/` is created or modified.
> The worker may not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. Exactly one file under `.scratch/graph-workflow/` names the path `.claude/rules/expedition-triggers.md`, and it
>    states three things about it: ~~that the harness loads it into every agent in this repository without any spawn
>    or hook~~ **that the harness loads it, without any spawn or hook, into an agent whose work touches an effort's
>    record and not into any other**, that it holds the trigger form of duties stated elsewhere in the map, and that
>    it overrides nothing in the map.
> 2. That same statement says that whoever edits the map's statement of one of those duties edits that file in the
>    same edit, or says plainly why not.
> 3. The statement contains no account of what happened — no count of missed duties and no story of a failure — and
>    cites by heading or by a quoted phrase, never by line number.
> 4. No text in any file under `.scratch/graph-workflow/` is deleted or rewritten; text that is superseded is
>    handled by the procedure the file it sits in states for supersession.
> 5. `.claude/rules/expedition-triggers.md` is byte-identical to its state before this work.
> 6. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This node cannot be claimed until node 218 lands**, and the manager has written no blocking edge because the
worker wrote none: its clause 5 demands a file that exists only in node 218's uncommitted worktree, so the condition
is unsatisfiable until that work is on `master`. **The manager is holding the scheduling rather than the graph**, as
it did for node 223 against node 214.

**One thing the manager notes about clause 1's "exactly one file".** The manager has twice today corrected a
statement that existed at more than one site, and this clause is the discipline stated as a demand rather than
learned afterwards. It is the worker's own wording, not the manager's.

**What made this node necessary is a property of the destination the human chose.** A file under `.claude/rules/` is
loaded by the harness rather than by anything the effort controls, so the record cannot discover it by reading a
spawn or a contract. That is the same property flag `218.2` turns on, and it is the cost side of the mechanism —
recorded here so the trade is visible rather than only its benefit.

## Annotation: clause 1 corrected, on its own author's report

*Filed by the manager. **The correction is the author's, not the manager's** — node 218's worker wrote this
condition, and in its next handover it reported that its own clause had been falsified by the clause the human
added to node 218. The manager has struck the false wording in place and written the author's own replacement.*

**What the author said, `verbatim`:**

> The node minted from the previous round — the one whose condition requires the record to say that the harness
> loads this file — carries, in the condition I wrote for it and which the manager has adopted, the clause *"the
> harness loads it into every agent in this repository without any spawn or hook"*. **Clause 8 has made that
> false.** The harness now loads it only into an agent working under `.scratch/**`. That node's condition needs the
> clause corrected before it is claimed, and the correction is the manager's: the record should say the file loads
> for work touching an effort's record, not for every agent.

**One thing the manager corrects in that, about whose the correction is.** A condition is not the manager's to
rewrite, and this one is not the manager's — the worker's own last sentence assigns to the manager something the
contract keeps away from it. **What the manager did instead is transcribe**: the replacement wording says what the
author said it should say, and nothing more. Had the author named no substance, this would have gone to the human.

**Why the clause was false rather than merely imprecise.** Node 218's own worker established that the narrowing is
real but partial: *"a checker or an implementation worker whose work under check is a record file is inside the
`.scratch/**` glob"*. So the record must not say *every agent*, and must not say *only the manager* either. The
replacement says **an agent whose work touches an effort's record**, which is what the glob actually does.

*The manager's note, 2026-09-25:* [node 301](301-rewrite-the-stop-skill-wayfinder-divergences-and-the-triggers-rule.md)'s worker reported, in its re-pointing search: "226 clause 1 describes the file as holding "the trigger form of duties stated elsewhere in the map", but both before-text and after-text say the governing statement is in the `/expedition` skill." The condition is not the manager's to change. Whoever claims this node raises it if it blocks the work.

## Amendment by the human, 2026-09-27 (from raise 1)

*The worker's recommended wording, taken by the human's "ok" to raise 1, recorded under `## Interview`. Filed by the manager. It replaces clauses 1 and 2.*

1. "Among `map.md`, `map-manager-only.md` and `map-implementation-rules.md` under `.scratch/graph-workflow/`, exactly one carries a statement about `.claude/rules/expedition-triggers.md` that says three things. First, the harness loads the file, without any spawn or hook, into an agent that reads a file matching its `paths:` frontmatter, meaning an effort's `map-manager-only.md` or the shipped `/expedition` skill's `SKILL.md`, and into no other agent. Second, the file holds a copy of the manager's trigger-duties and of the priority that orders them, and the governing statement of both is in `.claude/skills/expedition/SKILL.md`. Third, where the file and the map differ, the map is followed. Other files that merely name the path, such as node files, `decisions.md`, `flags.md`, `map-history.md` or the existing mention in `map-manager-only.md`, do not count against 'exactly one'."
2. "That same statement says that whoever edits the governing statement in `.claude/skills/expedition/SKILL.md` of one of those duties, or of the priority, edits `.claude/rules/expedition-triggers.md` in the same edit, or says plainly why not."

## Interview

#### Raise 1, relayed 2026-09-27

*Pasted as the worker handed it back. The worker is stopped until the human answers.*

```
NODE:          226, "Nothing in the record says the auto-loaded trigger file exists"
ABOUT:         This node writes one statement in the effort's record that names `.claude/rules/expedition-triggers.md`, says when the harness loads it, says what it holds and what it overrides, and says that it is edited together with the governing statement. I stopped before making any edit, because three of its clauses are false or cannot be met in the tree as it is now.
SO FAR:        I read the node file, map.md, map-implementation-rules.md, decisions.md line 142 (the only line naming the triggers file), and the triggers file at worktree HEAD `b775f2a`. I also read `git show` of the file at 4598672, db81330, e5c03a5, 02bdd3b and eb3b217. I searched `.scratch/graph-workflow/` (without `worktrees/`) for `expedition-triggers`, and searched `.claude/skills/` for `expedition-triggers` and `rules/`. I have edited nothing, and the worktree is clean. The bar for this repo: there is no build, no test and no formatter, which agrees with the rules file, so the bar is its non-command half. These are the facts that break the condition:
               (a) Clause 1 says "Exactly one file under `.scratch/graph-workflow/` names the path". About 33 files there already name it, among them `map-manager-only.md` (the passage "the third trigger in `.claude/rules/expedition-triggers.md`"), `map-history.md`, `decisions.md`, `flags.md` and many node files. Clause 4 forbids deleting or rewriting text, so clause 1 cannot be met as written.
               (b) The corrected wording of clause 1 is false again. It says the file loads "into an agent whose work touches an effort's record and not into any other". Since 4598672 (node 255), and still at HEAD, the frontmatter is `paths: [".scratch/**/map-manager-only.md", "**/expedition/SKILL.md"]`. So the file loads for an agent that reads an effort's `map-manager-only.md` or the shipped manager contract. It does not load for any other record file, and it does load for a file that is not part of the record. decisions.md line 142, as the manager repaired it, already says this: "scoped by `paths:` frontmatter naming both an effort's record and the shipped manager contract".
               (c) Clause 1 says the file "holds the trigger form of duties stated elsewhere in the map", and clause 2 says "whoever edits the map's statement of one of those duties". Neither is true now. The file says "The `/expedition` skill holds the governing statement of both, and this copy stays in context after a compaction. Where this file and the map differ, follow the map." The governing statements are in `.claude/skills/expedition/SKILL.md` (for example `## The order you act in`), and the map only points there (map-manager-only.md: "Where giving a question stands among the manager's acts is stated in `.claude/skills/expedition/SKILL.md`"). Node 301's worker already reported this, and the manager's 2026-09-25 note on this node says that whoever claims the node raises it if it blocks the work. It does block the work.
               Clauses 3 to 6 stand. Clause 3 bans an account of what happened. Clause 4 bans deletion and asks each file's own supersession procedure. Clause 5 keeps the triggers file byte-identical. Clause 6 is the bar. "Overrides nothing in the map" is still true.
               What I have already decided myself: the statement does not go in `map-manager-only.md` or `map-history.md`, so it stays clear of node 160. `.claude/skills/expedition/SKILL.md` does not mention the triggers file at all. That is a gap in a shipped file, and it is outside this node's scope (the condition closes `.claude/`).
ASK:           Will you replace clause 1 and clause 2 with the wording under RECOMMENDED, and then let this node continue?
RECOMMENDED:   Replace both clauses with the text below. Every fact in it is already fixed by the triggers file at HEAD, by `.claude/skills/expedition/SKILL.md`, or by decisions.md line 142.
               1. "Among `map.md`, `map-manager-only.md` and `map-implementation-rules.md` under `.scratch/graph-workflow/`, exactly one carries a statement about `.claude/rules/expedition-triggers.md` that says three things. First, the harness loads the file, without any spawn or hook, into an agent that reads a file matching its `paths:` frontmatter, meaning an effort's `map-manager-only.md` or the shipped `/expedition` skill's `SKILL.md`, and into no other agent. Second, the file holds a copy of the manager's trigger-duties and of the priority that orders them, and the governing statement of both is in `.claude/skills/expedition/SKILL.md`. Third, where the file and the map differ, the map is followed. Other files that merely name the path, such as node files, `decisions.md`, `flags.md`, `map-history.md` or the existing mention in `map-manager-only.md`, do not count against 'exactly one'."
               2. "That same statement says that whoever edits the governing statement in `.claude/skills/expedition/SKILL.md` of one of those duties, or of the priority, edits `.claude/rules/expedition-triggers.md` in the same edit, or says plainly why not."
               I would put the statement in `map-implementation-rules.md`, under `## What the work is held against`. Whoever edits `SKILL.md` is an implementation worker, and that file is the one such a worker and its checker hold the work to, so a checker would catch a missed paired edit. It also keeps this diff apart from node 160's two files.
ALTERNATIVES:  - Put the statement in `map.md`. Every worker reads it, but only a manager or an implementation worker acts on it, which goes against map.md's rule of holding "only what every worker can act on".
               - Put the statement in `map-manager-only.md`, next to its existing mention of the file. That is the natural place, but it collides with node 160, and no implementation worker or checker reads it.
               - Keep the "map's statement" wording in clause 2 and have the record declare that the map holds the duties. That would make the record false about where the duties are governed.
               - Close this node, and open a node that adds the pointer inside `.claude/skills/expedition/SKILL.md` instead. The shipped skill would then carry its own statement that the two must be edited together, but that is a change to a shipped file and needs the human's say-so.

RETROSPECTIVE
1. What I had to hunt for. How the triggers file's frontmatter changed over time: whether the `.scratch/**` scope from node 218 still held, and at which commit it narrowed. I found it with `git log` / `git show` on the file, not from the record. I also had to find where the duties are actually governed, from the file itself and node 301's notes.
2. What arrived that this node did not need. The manager's note about node 160, because I raised before choosing a file. The node's filing note about the "cost side of the mechanism".
3. What would have made this easier. A spawn line saying the file's frontmatter was narrowed at 4598672 (node 255). Also a check, before the claim, of whether this condition still matched the tree: the node sat unclaimed through nodes 255 and 301, both of which changed the file and one of which reported the defect.
4. What was stale, wrong or contradictory. The corrected clause 1, as described in (b). "Exactly one file ... names the path", which was already false when filed and is false by about 33 files now. "Stated elsewhere in the map" and "the map's statement", as described in (c). The spawn told me to hand back the handover and a gate payload, but the contract allows a raise in place of the handover, and this is a raise. The node's question also assumes the duties are stated in `map.md` ("as standing preferences in `map.md`"), and they are not stated there now.
```

#### The human's answer to raise 1, 2026-09-27

The human, `verbatim`: *"ok"*. It takes the worker's recommendation: "Replace both clauses with the text below." The replacement clauses are filed under `## Amendment by the human, 2026-09-27 (from raise 1)`.

## Answer

`map-implementation-rules.md` now states when the harness loads `.claude/rules/expedition-triggers.md` and what it holds. It says the governing statement is in `/expedition`'s `SKILL.md`, the map wins where they differ, and editing either duty's statement means editing both.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `4ef7f95`. Flags 226.1 settle at the node closing report.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

````
HANDOVER:      226, "Nothing in the record says the auto-loaded trigger file exists"

ANSWER:        The record now has one statement about `.claude/rules/expedition-triggers.md`. It is a new paragraph of 8 lines in `.scratch/graph-workflow/map-implementation-rules.md`, under `## What the work is held against`, placed right before the paragraph that begins "**An implementation node's work on this effort may be the effort's own record**". It says four things, which are the four demands of the amended clauses 1 and 2:
               - The harness loads the file into an agent that reads a file matching its `paths:` frontmatter, meaning an effort's `map-manager-only.md` or the shipped `/expedition` skill's `SKILL.md`, and into no other agent. No spawn or hook is involved.
               - The file holds a copy of the manager's trigger-duties and of the priority that orders them. The governing statement of both is in `.claude/skills/expedition/SKILL.md`, under `## The order you act in` and `## What is in front of the human, and when`.
               - Where the file and the map differ, the map is followed.
               - Whoever edits the governing statement in `SKILL.md` of a duty or of the priority edits the triggers file in the same edit, or says plainly why not.
               Why this file: whoever edits `SKILL.md` is an implementation worker, and this is the file that worker and its checker hold the work to, so the checker enforces the paired edit. The human accepted this placement with the "ok" to raise 1.
               What the other map files say: `map.md` does not name the triggers file. `map-manager-only.md` names it only in the passage "the third trigger in `.claude/rules/expedition-triggers.md`", which the amended clause 1 excludes from "exactly one".
               What the statement leaves out: it gives no account of how the file came to exist, and it cites headings rather than line numbers.
               What was not changed: no text was deleted or reworded, and `.claude/` is untouched, so the triggers file is byte-identical to `b775f2a`. The shipped `SKILL.md` still does not name the triggers file, and it is outside this node's scope.

INDEX LINE:    `map-implementation-rules.md` now states when the harness loads `.claude/rules/expedition-triggers.md` and what it holds. It says the governing statement is in `/expedition`'s `SKILL.md`, the map wins where they differ, and editing either duty's statement means editing both.

FLAGS:         ASSUMPTION: I placed the paragraph right before the "effort's own record" paragraph, so the one paragraph that node 352 leaves alone sits between it and node 352's edits. Node 352 rewords the review-route paragraph just above, with an unchanged blank line between, and removes the writing-rules block below the record paragraph. I also cited `SKILL.md` under two headings, `## The order you act in` for the priority and `## What is in front of the human, and when` for the never-ask trigger. The clause names only the file, and the headings were picked by reading the headings of `SKILL.md` and `map-manager-only.md`'s pointers to it. Index sentence: Node 226 put its triggers-file statement just before the rules file's "effort's own record" paragraph, away from node 352's edits, and cited two `SKILL.md` headings as where the duties are governed.

NEW NODES:     none. One gap for you to weigh, not reported as a node: `.claude/skills/expedition/SKILL.md` does not name `.claude/rules/expedition-triggers.md`, so a reader of the shipped skill alone still cannot find the copy. Fixing that is a change to a shipped file and needs the human's say-so.

INVALIDATIONS: This narrows node 218's answer where it says the file loads for "work touching an effort's record" (decisions.md line 142 was already repaired to the narrower scope). The record now states the narrower scope, from the frontmatter set at `4598672` by node 255. It also narrows this node's own question, which assumes the duties are stated as standing preferences in `map.md`: the record now says their governing statement is in `SKILL.md`. Nothing is contradicted.

CONDITIONS:    Searched with `scripts/search-conditions.py 226 b775f2a:.scratch/graph-workflow/map-implementation-rules.md <worktree copy>` and the phrases `expedition-triggers`, `trigger-duties`, `trigger-duty` and `map-implementation-rules.md`. It covered 31 open or claimed conditions. Nothing quoted from the file or shared as a 6-gram is gone. The phrase hits are nodes 152, 190, 271, 352 and 354, and they match only because they name the file. I read their scope clauses, and none forbids a new paragraph or conflicts with this one. I also grepped the open and claimed node files for `expedition-triggers` and `trigger-dut`, and only node 226 matched. No replacement clauses. No open node's question changes.

MISSING FROM MAP: The map does not say where the manager's trigger-duties are governed, or that the triggers file's `paths:` scope was narrowed at node 255. I got both from the triggers file itself, `git show` of its history, and node 301's reports. Now that the statement exists, a later reader has it.

GATE PAYLOAD:  Checker findings: none received yet.
               Paths touched: `.scratch/graph-workflow/map-implementation-rules.md` only, 9 lines added and none removed. Not touched: the node file (the worktree copy predates the amendment, and its recording is yours), `map-history.md`, `map-manager-only.md`, and everything under `.claude/`.
               The bar: the repo has no build, no test, no formatter and no CI, which agrees with the rules file, so the bar is its non-command half. I checked the paragraph against the five writing rules, `/naming` and the ground rules. It is plain sentences, with no bold, no line numbers and no account of what happened.
               Proposed commit message:
               "State in the rules file when the harness loads the triggers rule and that it is edited with SKILL.md

               Node: graph-workflow/226"

RETROSPECTIVE
1. What I had to hunt for. The history of the triggers file's frontmatter and where the duties are governed (both before the raise). After it, which `SKILL.md` headings hold the duties.
2. What arrived that this node did not need. The node's filing note on the "cost side of the mechanism". The note on node 160 turned out to be moot, because the placement was settled in the raise.
3. What would have made this easier. A resumption that also said the worktree's node file is stale and not mine to update. I inferred that and left it alone. Node 352's conflict zones were given in the message, which helped.
4. What was stale, wrong or contradictory. The worktree's copy of this node file predates the amendment, as the message said. Nothing else.
````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 352's check; the condition reached it as a verbatim copy in `$TMPDIR/c226.md`.*

> PASS
>
> This is the check of node 226, "Nothing in the record says the auto-loaded trigger file exists". The work is the uncommitted diff to `.scratch/graph-workflow/map-implementation-rules.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/226-triggers`, on base b775f2a. Under the rules file, I read that record file as the work. I read the whole condition in `/tmp/claude-1000/c226.md`, with the human's 2026-09-27 amendment as clauses 1 and 2, and clauses 3 to 6 as written.
>
> **Parts of the condition**
>
> - **Scope.** Met.
>   - `git status --short --untracked-files=all` shows only `M .scratch/graph-workflow/map-implementation-rules.md`.
>   - No file under `.claude/` changed, and neither did any node file, `decisions.md` or `flags.md`.
> - **1 (amended).** Met.
>   - Among the three map files, `grep -n 'expedition-triggers'` finds the new paragraph in `map-implementation-rules.md`. It also finds `map-manager-only.md` line 94, the existing mention that the amendment excludes from the count. `map.md` has none. So exactly one file carries the statement.
>   - The paragraph says the three things:
>     - The harness loads the file "without any spawn or hook, into an agent that reads a file matching its `paths:` frontmatter, meaning an effort's `map-manager-only.md` or the shipped `/expedition` skill's `SKILL.md`, and into no other agent". That matches the file's actual frontmatter: `paths: ".scratch/**/map-manager-only.md"` and `"**/expedition/SKILL.md"`.
>     - "The file holds a copy of the manager's trigger-duties and of the priority that orders them. The governing statement of both is in `.claude/skills/expedition/SKILL.md`". The two headings it cites, `## The order you act in` and `## What is in front of the human, and when`, exist in that file.
>     - "Where the file and the map differ, the map is followed."
> - **2 (amended).** Met. The same paragraph says "Whoever edits the governing statement in `SKILL.md` of one of those duties, or of the priority, edits `.claude/rules/expedition-triggers.md` in the same edit, or says plainly why not."
> - **3.** Met. The paragraph gives no account of what happened, no count and no story. It cites by heading and by path, never by line number, and ends with a link to the node that settled it.
> - **4.** Met. The diff removes 0 lines. The paragraph is inserted between two paragraphs that are unchanged, so no text is deleted or rewritten and nothing needs a history entry.
> - **5.** Met. `.claude/rules/expedition-triggers.md` does not appear in the status, so it is byte-identical.
> - **6.** Met. See the bar below.
>
> **The bar**
> - The rules file records no build, tests, formatter or CI, and the repo confirms that.
> - `git diff --check` is clean (exit 0).
> - The added paragraph is wrapped like the file's other wrapped paragraphs. Its longest line is 119 characters, against a file that already has unwrapped lines longer than that.
>
> **Standards.** I read the standards in `map-implementation-rules.md`, together with the ground rules given as text.
>
> - These bore on the work, and I found nothing against them:
>   - `## Writing the map`'s admission test. The duty to edit the trigger file with `SKILL.md` binds any implementation worker who changes `SKILL.md`.
>   - The writing rules. Citations are by heading, and there is one idea per sentence.
>   - `CONTEXT.md` `_Avoid_` lines.
>   - `/writing-for-agents`.
>   - The ground rules. This is a record file, not a shipped one.
> - The addition changes none of the standards I hold the work against.
> - No reviewing skill is named, so I ran none.
>
> NOT COVERED:
> - None of the condition's parts is uncovered. The ban on node, `decisions.md` and `flags.md` writes is established from the worktree diff.

### Gate — approve, `standing yes`, 2026-09-27

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and its one NOT COVERED item is the worker's bookkeeping. This settles none of the node's flags; they settle at the node closing report.

## Flags

`226.1` `ASSUMPTION` **· settled** — I placed the paragraph right before the "effort's own record" paragraph, so the one paragraph that node 352 leaves alone sits between it and node 352's edits. Node 352 rewords the review-route paragraph just above, with an unchanged blank line between, and removes the writing-rules block below the record paragraph. I also cited `SKILL.md` under two headings, `## The order you act in` for the priority and `## What is in front of the human, and when` for the never-ask trigger. The clause names only the file, and the headings were picked by reading the headings of `SKILL.md` and `map-manager-only.md`'s pointers to it.

*The manager's note, 2026-09-27:* flags 226.1 settle at the node closing report that closes this node, which names its gate as taken under the standing yes.
