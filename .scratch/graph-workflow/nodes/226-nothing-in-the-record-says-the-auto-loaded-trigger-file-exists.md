# Nothing in the record says the auto-loaded trigger file exists

Type: implementation
Status: claimed

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
