# Nothing in the record says the auto-loaded trigger file exists

Type: implementation
Status: open

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
