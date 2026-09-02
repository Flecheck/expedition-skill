# Carry node 82's widening rule into the two shipped files that state the old one

Type: implementation
Status: open

Blocked by: 58

## Question

*Reported by [How a condition's scope is amended](82-amending-a-condition-whose-scope-was-too-narrow.md)'s worker in
its `INVALIDATIONS`, and pasted as it wrote it. Whether it became one node or rode an existing one was left to the
manager; this is that node.*

> Two shipped statements go stale with it, and both are downstream of that node rather than resolved nodes of their
> own: `graph-conventions.md`'s `### Acceptance condition` — *"its worker may not rewrite it"*, with no word on who
> may widen its scope — and `.claude/skills/expedition/SKILL.md`'s `## Acceptance conditions`, *"Where a node was
> minted by an agent, that agent wrote the condition and you file it"*, which now needs the widening carve-out and
> guard 1's re-derivation. Reported here because nothing else reports them; whether they become one implementation
> node or ride an existing one is the manager's.

**Why it is blocked by [node 58](58-qualify-the-graph-file-ban.md).** Both files are in node 58's own change and its
work is uncommitted at a gate. Claiming this before that lands would put two workers in the same two files.

## Acceptance condition

***Written by the manager, for a node the manager minted itself.*** Marked as the manager's own under [Who writes the
acceptance condition for an implementation node the manager mints
itself](39-condition-for-a-manager-minted-node.md), whose constraint 1 confines it to what is already fixed. **What
it demands was fixed by node 82 and by nothing of the manager's**; its wording is not, so the condition states the
properties and leaves the form.

1. `.claude/skills/expedition/graph-conventions.md`'s `### Acceptance condition` states who may change a condition
   after it is written, and distinguishes three parties: **the condition's own worker**, which may not rewrite it and
   raises instead where it judges it wrong — unchanged from what that section says today; **the manager**, which may
   extend the condition's scope to further instances of a defect the condition already describes, provided the
   amendment writes no requirement that was not already fixed; and **the human**, to whom anything else goes.
2. The same section states the three things that extension does **not** reach, and states them as properties rather
   than as examples: a new demand at any place; an ambiguous demand at a place the condition already lists, which
   stays the worker's to decide-and-flag or to raise; and a defect the condition does not describe, which is a new
   node.
3. `.claude/skills/expedition/SKILL.md`'s `## Acceptance conditions` — which today says *"Where a node was minted by
   an agent, that agent wrote the condition and you file it"* — carries the same permission and the same three
   limits, stated as duties of the manager rather than as a description of the rule.
4. That same section states the manager's duty to **re-derive an enumerated scope before the node is claimed**: where
   a condition's scope is a list of files, the manager re-runs the search that produced that list, and where the list
   has grown, widens it before the node is claimed rather than after a worker has read the short version.
5. That same section states what accompanies an amendment: it is recorded on the node beside the search that
   justified it, marked as the manager's own and distinguished from the minting author's text, carried as a flag, and
   named in the report accompanying the pick — or, where the amendment is made after the node is claimed, named in
   that node's closing report instead.
6. Neither file states that the manager may **author** a condition for a node an agent minted. That prohibition is
   untouched by this work, and where either file states it today, it still stands after.
7. `CONTEXT.md` is not changed, and no file under `.scratch/` is changed.
8. No rule in either file is removed or renumbered, and no rule other than the ones clauses 1–5 name changes its
   meaning.
9. The working tree meets the bar.

### The manager's read-back, recorded before the claim

*[Node 39](39-condition-for-a-manager-minted-node.md)'s constraint 2 requires the condition to be read back against
the two rules that bind every condition, and that reading recorded on the node.*

- **Self-contained text.** It passes. Every demand is stated in the condition's own words rather than by pointing at
  node 82 — the permission, the three limits, the re-derivation duty and the five things that accompany an amendment
  are all written out here. The two existing sentences it changes are quoted. The checker has both files.
- **It does not quantify over the record.** It passes. Clauses 6 and 8 are demands about **what changed in the two
  files**, answerable from the diff, which `graph-conventions.md` permits by name. No clause holds the work against
  the effort's resolved nodes.

## Annotation: this condition's scope is short by measurement — five worker contracts it does not name

*Filed by the manager from [Whether a condition's scope stops being a list of
files](94-condition-scope-as-a-predicate.md)'s `INVALIDATIONS`, in that node's own words. **The condition above is
not amended by this annotation**; amending it is a separate act under [How a condition's scope is
amended](82-amending-a-condition-whose-scope-was-too-narrow.md)'s guard 2, and the manager has not performed it.*

> **This one is the sharper finding, because node 95 is node 82's own carrier.** Its scope names two files. Its
> subject is *who may change a condition after it is written*, and `grep -rn "not that worker's to fix"` over
> `.claude/` returns that sentence **verbatim in all five worker contracts**, none of which the condition names: *"A
> condition its worker judges wrong is not that worker's to fix: it stops that node and goes to the human."* That
> sentence states the worker's half of exactly the three-party distinction node 95's clauses 1 and 2 exist to write,
> and node 82 falsified its routing — a short scope now goes to the **manager** and never spends a human turn. So a
> worker reading its contract after node 95 lands would still be told to stop the node and go to the human, which is
> the wasted turn node 82 exists to prevent. **Node 82's carrier reproduces node 82's defect, five files over.** The
> demand at the five new places is fixed by node 82's resolved answer, so this is a widening node 82 licenses
> cleanly.

**Why nobody reported it earlier**, in node 94's words: *"its scope came from a worker's `INVALIDATIONS` rather than
from a search, which is the exact case rung 3 exists to expose."*
