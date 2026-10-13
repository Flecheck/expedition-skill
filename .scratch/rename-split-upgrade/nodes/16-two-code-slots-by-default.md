# Two code slots by default

Type: implementation
Status: resolved
Blocked by: ~~14~~

## Question

*Written by the manager.* This lets an effort that says nothing about its code slots run two implementation nodes at once, as the human wants by default. The human said, `verbatim`: *"You can run 2 code slot, I think it should be the default."* Today the manager contract gives the count of nodes that need the human a default of two, and gives the count of code slots no default: it is "the effort's number of code slots, recorded in its map".

## Acceptance condition

*Written by the manager.* Scope: the named place is the work, and the scope came from no search. The file this work may change is `.claude/skills/expedition/SKILL.md`. Any other file found to need a change is reported, not edited.

1. In `.claude/skills/expedition/SKILL.md`, the bullet that begins "How many implementation nodes run at once" says that the count is two, unless the effort's map sets another number. ~~It still says that a slot holds one worker, that where no slot is free no implementation node is started, the trade that raising the count buys, that the human sets the number, and that the manager names the trade when the human moves the count.~~ *(superseded by amendment 1 below)*
2. No other sentence of `.claude/skills/expedition/SKILL.md` changes in meaning.
3. `.claude/rules/expedition-triggers.md` changes only where this work edits, in `.claude/skills/expedition/SKILL.md`, the governing statement of one of the manager's trigger-duties or of the priority that orders them. In that case it changes to match.

*Manager's note, reading the condition back against `### Acceptance condition` under `## The node file` in `graph-conventions.md`:* it is self-contained and states what must be true in its own words; its paths are relative to the repository root; it states that its scope came from no search, because the named place is the work; it makes no demand about the record as a whole; and every demand is fixed by the human's words above or by the state of the files: the bullet's other properties are copied from its text at `cf5984eadc`. It is blocked by node 14 only because both edit `.claude/skills/expedition/SKILL.md`.

*Manager's note:* the worker of [node 14](14-ship-the-rule-for-widening-scope.md) wrote a replacement for clause 1's second sentence, to be filed once node 14 lands, since its words are fixed by that landed work. As it wrote it: "It still says that a slot holds one worker, that a paused node holds no slot while it is blocked, as `## A paused implementation node` says, that where no slot is free no implementation node is started, the trade that raising the count buys, that the human sets the number, and that the manager names the trade when the human moves the count."

### Amendment 1 — by the worker of node 14, filed by the manager

What fixed the words: node 14's work, landed as `47beb1c218`, which added to this bullet of `.claude/skills/expedition/SKILL.md` the sentence "A paused node holds no slot while it is blocked, as `## A paused implementation node` says." Clause 1's second sentence now reads, as that worker wrote it:

It still says that a slot holds one worker, that a paused node holds no slot while it is blocked, as `## A paused implementation node` says, that where no slot is free no implementation node is started, the trade that raising the count buys, that the human sets the number, and that the manager names the trade when the human moves the count.

*Manager's note, before the claim:* read everything after the condition. The bullet beginning "How many implementation nodes run at once" is present at `47beb1c218`. Its scope came from no search. Node 14 resolved, so the blocker is struck.

## Answer

In `.claude/skills/expedition/SKILL.md`, the bullet that begins "How many implementation nodes run at once" now says: "The count is the effort's number of code slots. It is two, unless the effort's map sets another number." That replaces "The count is the effort's number of code slots, recorded in its map." The new wording follows the sibling bullet on nodes that need the human ("The count is two, unless the effort's map sets another number"), so the two counts now default the same way. Every other sentence of the bullet is unchanged in meaning: a slot holds one worker; a paused node holds no slot while it is blocked, as `## A paused implementation node` says; where no slot is free, no implementation node is started; the trade that raising the count buys; the human sets the number; the manager names the trade when the human moves the count. The only other change is that the lines after the edit were rewrapped. `.claude/rules/expedition-triggers.md` is unchanged, because this bullet is not the governing statement of a trigger-duty or of the priority. The priority's "within the limits" names no count.

**MISSING FROM MAP, as the worker wrote it:** Same gap as node 14 reported: `map.md` does not say that the effort runs two code slots. I took that from the spawn, and from `map-manager-only.md`'s Counts note, which a search reached.

*Manager's note:* landed as `5dc2681779` on `master`, after the human's approval: the node's commit was put on top of `master` (node 18 had landed in another file) and then fast-forwarded; the worktree and branch are removed.

## Flags

`16.1` `ASSUMPTION` **· settled** — Amendment 1 to clause 1, written by node 14's worker and filed by the manager after node 14 landed. The worker handed no flag sentence for the amendment itself.

## Review

### Checker run 1 — `PASS`

The checker's entry, as it wrote it:

PASS

Node: 16-two-slots-default. Work: the uncommitted change to `.claude/skills/expedition/SKILL.md` in /home/mathieu/projects/graph-agent/.scratch/rename-split-upgrade/worktrees/16-two-slots-default. `git status --short --untracked-files=all` shows that file as the only changed path.

Scope: no search was recorded, because the condition says its scope came from no search. The diff touches only the listed file, so nothing was edited outside the list.

1. Clause 1 holds. I unwrapped the bullet with `awk 'BEGIN{RS=""} /How many implementation nodes run at once/{gsub(/\n */," ");print}'`. It now reads: "The count is the effort's number of code slots. It is two, unless the effort's map sets another number." Every required element is still in the bullet:
   - "A slot holds one worker."
   - "A paused node holds no slot while it is blocked, as `## A paused implementation node` says." That heading exists in the file (`grep -n '^## A paused implementation node'`).
   - "Where no slot is free, start no implementation node."
   - The trade: "Raising the count buys parallel implementation at the price of conflicts to resolve when the work is integrated."
   - "The human sets the number."
   - "When the human moves the count, name this trade to them."
   - The default of two agrees with `scripts/frontier.sh`, whose `implementation_target=${3:-2}` is described as "Each target defaults to 2". So the change makes no other place in the file wrong.
2. Clause 2 holds. `git diff --word-diff=plain` shows a single change: "slots, recorded in its map." became "slots. It is two, unless the effort's map sets another number." That change is the clause-1 sentence itself. Every other difference in the diff is line re-wrapping with identical words.
3. Clause 3 holds. `git diff --stat -- .claude/rules` is empty. `grep -niE 'count|two|slot|at once' .claude/rules/expedition-triggers.md` returns nothing, so this bullet is not the governing statement of any trigger-duty or of the priority. No change to the trigger file was owed.

The bar:
- The root `CLAUDE.md`, under `## Commands`, says the repository has no build, no tests, no formatter and no CI. I confirmed this: there is no `.editorconfig` or prettier configuration, and `git diff --check` is clean. No commands exist to run.
- I held the standards by hand:
  - The rules for writing in `CLAUDE.md`: the new sentences are plain, hold one idea each, and "It" has one referent, the count. The new sentence also matches the wording of the sibling bullet.
  - The glossary's `_Avoid_` lines: the new text adds only "two", "unless" and "the effort's map sets another number". None of these is a refused term, and "code slot" is the glossary's own term.
  - `graph-conventions.md`, `/coding-principles` and `/naming`: none of them bears on this one-sentence prose change.
- I ran no reviewing skill. The standards name none as a reviewer, so I applied them by hand.

Standards read: I read only the standards in `.scratch/rename-split-upgrade/map-implementation-rules.md` and opened no other file in the effort's directory. That file sends the reader to:
- the bar's commands in `CLAUDE.md` (bore on this work: none exist);
- `/coding-principles` and `/naming` (did not bear);
- the glossary's `_Avoid_` lines (bore);
- `graph-conventions.md` (did not bear);
- `/writing-for-agents` and the rules for writing in `CLAUDE.md` (bore);
- the trigger-file rule (bore, and is clause 3).

A note that is not a finding: the re-wrapped paragraph leaves line 744 at 123 characters. Every other prose line in the file is 105 characters or fewer; only the frontmatter and table rows are longer. No stated standard or formatter sets a line width, so this is not a finding. It is cosmetic and can be re-wrapped if wanted.

Flags: 16.1 records where the amended clause 1 came from. It makes no claim about the work that the work could make true or false.

I wrote no files.

### Gate outcome — approve

The human's words, `verbatim`:

> apprpve
