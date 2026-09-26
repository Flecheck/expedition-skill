# Co-locate the scan rules with the mechanical checks

Type: implementation
Status: superseded
Superseded by: 339

## Question

Twelve false results across seven sessions came from running `graph-conventions.md`'s eight mechanical checks
without rules the file states elsewhere or not at all. Put every rule a check needs where the checks are.

Reported by [Review every shipped file against `/writing-great-skills`](47-review-shipped-skills.md)'s worker,
which wrote the acceptance condition below. Its measurement: present today are header-block fields (`:83`,
`:282`), skip fenced blocks (`:283`), `flags.md`'s first-link rule (`:67`) and the `**· settled**` marker form
(`:165`); **absent entirely** are the unwrap rule, `decisions.md` entry identity, and `## Flags` entry
line-anchoring.

**The inversion it found is the sharp part:** the unwrap rule is stated **four times** in the checker contract
(`:63`, `:92`, `:111`, `:304`) and **zero times** in the file whose checks it protects.

## Acceptance condition

`.claude/skills/expedition/graph-conventions.md` is left in a state where every rule needed to run its
mechanical checks without a false result is reachable from the section stating those checks. This work edits a
skill file rather than a graph file, so text it removes is removed outright and is not marked in place.

1. The section headed `## Mechanical checks` states all seven rules below, or points to the section of the same
   file that holds one, naming that section. Wording is the implementer's; content is not.
   a. Fields are read only from the header block — everything above the first `##` heading.
   b. Fenced code blocks are skipped.
   c. Text is unwrapped into unbroken lines before any phrase is matched, a phrase that wraps being invisible to
      a search over lines.
   d. In `flags.md`, the flag's node is the first link on the line.
   e. In `decisions.md`, a resolved node's entry is identified by the first link on its line, so an entry whose
      text cites another node is not counted as an entry for that node.
   f. A `## Flags` entry is line-anchored: an entry begins at the start of a line with the flag's id, so a flag
      id appearing mid-sentence inside another entry's prose is not itself an entry.
   g. A flag counts as `settled` on its node only where the marker `**· settled**` stands in an entry's marker
      position; the bare word `settled` in an entry's prose does not settle it.
2. Four of the seven are new to this file. Before this work it states a, b, d and the `**· settled**` form, and
   states nothing about unwrapping, about `decisions.md` entry identity, about `## Flags` entry anchoring, or
   about where the `settled` marker must stand to count. Afterwards all seven are present.
3. The eight mechanical checks keep their current meaning and their current numbering; none is added, removed,
   renumbered or redefined.

### Two things the manager owes whoever claims this

*Not changes to the condition above.*

**The check count will be nine, not eight, by the time this is claimed.** [Nothing checks that a part a checker
left uncovered was ever established](45-nothing-checks-an-uncovered-part.md) adds check 9 and is at its checker
now. Clause 3 says the existing checks keep their meaning and numbering and adds nothing — it does not say
*eight*, so it survives; but clause 2's list of what is present is measured against the pre-node-45 file, and
node 45's own work states some of its scanning rules locally inside `## Review`, flagged there as `45.2`
precisely because a general rule was this node's to write. **Whoever claims this reads node 45's landed change
first**, and clause 1f is the rule node 45 declined to generalise.

**The standard this was written against was superseded upstream the same day.** The lever survives: co-location
is still a named principle in the new text — *"reading one part brings its neighbours with it"* — with a test
added, *"the document should read like documentation written for the agent."* So this node is **not** blocked on
the re-review.

## Annotation: the check count is nine, and the inversion has a second name

*Filed by the manager from [Re-review the shipped files against
`/writing-for-agents`](54-review-against-writing-for-agents.md).* `graph-conventions.md` is now **402 lines with
nine mechanical checks**, not 384 with eight — [Nothing checks that a part a checker left uncovered was ever
established](45-nothing-checks-an-uncovered-part.md)'s change, in the working tree at the time of writing.
Clause 3 above says the existing checks keep their meaning and numbering and does not say *eight*, so it
survives; clause 2's inventory of what is present was measured against the pre-node-45 file.

**The ninth check ships with its own anchoring rules inline**, which is the sharp part: *"The marker opens the
**item**, so a quote that wraps over several lines cannot carry it away… The label stands alone on its own line,
so prose that mentions the words names no part at all."* So the file's newest check carries exactly the
discipline the older eight lack — **evidence that the gap is known locally and unrepaired globally.**

**A second lever for the same finding.** The scattering is also a **leading-word** failure: the standard's
*"Repeated as a token, never as a sentence"* against `unwrap`, which is stated as a sentence at four sites in the
checker contract (`:64-66`, `:92-93`, `:110-111`, `:301-305`) and appears in **no other shipped file at all**.

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 339](339-tie-graph-conventions-mds-mechanical-checks-to-the-writes-that.md), the merge [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole.
