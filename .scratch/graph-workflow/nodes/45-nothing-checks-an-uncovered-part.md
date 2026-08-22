# Nothing checks that a part a checker left uncovered was ever established

Type: implementation
Status: resolved

Blocked by: 38

## Question

`## Review` now records a part a checker run did not cover and, beside it, who established it. Nothing detects
the case the form exists for: an entry where the part was named and nobody ever established it. The form's
whole guarantee is that such a part is **visible**, which relies on someone looking — and the eight mechanical
checks do not reach it. A check that did would have to match prose inside `## Review`, which is the class of
scan [map.md](../map.md) records eleven false results against; the repair is the same move the sixth delta made
for flags with `NN.k` — fix an anchor first, then the join is exact.

Reported by [Record a checker's not-covered part on `## Review`](38-recording-a-not-covered-part.md)'s worker,
which wrote the acceptance condition below. In its own words, it reported it *"because my own change creates an
obligation that can be left open with nothing to detect it"*, and it named it an instance of *a shipped form
that nothing checks* — which is [What keeps the shipped files consistent when a decision changes a
term](29-shipped-file-consistency.md)'s recurring problem, arriving this time inside a form that had just been
designed rather than one that had drifted.

## Acceptance condition

1. The section of `.claude/skills/expedition/graph-conventions.md` that documents a node's `## Review` fixes
   how two things are written: a part of the acceptance condition that a checker run named as not covered, and
   the statement of who later established that part. It fixes them such that whether a named part has an
   establisher beside it is decidable by reading the file and matching what that section fixes, without judging
   the prose around it.
2. That file's `## Mechanical checks` section gains one check: every part named on a checker run's entry as not
   covered carries, beside it, who established it, before that node's `Status:` is `resolved`. It is stated so
   as to be decidable by reading the files, that section's opening sentence being *"Every one of these is
   decidable by reading the files."*
3. The checks already in that section — numbered 1 to 8, covering: every `Blocked by:` target exists and is not
   `superseded` or `out-of-scope`; every `Superseded by:` has a matching `Supersedes:`, both directions present;
   no `NN` used twice and no gap indicating a reused number; every `Labels:` entry appears in the map's declared
   vocabulary; every `resolved` node has an `## Answer` and exactly one line in `decisions.md`; every
   `## Flags` entry has a line in `flags.md` carrying the same id and none the other way, the two agreeing on
   state; every `implementation` node has an `## Acceptance condition` before it is `claimed`; and no node has
   more than three `## Interview` attempt blocks — are all still present after this work and none has lost
   anything it required.
4. That same `## Review` section still states three things and nothing beyond them: the checker's chronology,
   one entry per run; each correction round, numbered; and the gate's outcome, named as one of approve /
   correct / reject. Where the count word or the phrase *"and nothing beyond them"* is no longer true of the
   section, it is made true in the same change.
5. No file outside `.claude/skills/expedition/` is changed by this work.
6. The working tree meets the bar.

### Audit at claim time, by the manager

*The manager's own note, not a change to the condition above.* Read against [An acceptance condition is
self-contained text](33-condition-is-self-contained.md) and [The clause that says no resolved node changes
cannot be self-contained](36-resolved-node-clause-cannot-be-self-contained.md).

**All six clauses pass.** Clause 3 copies the eight existing checks in full rather than sending the checker to
read them, which is the one place this condition would otherwise have pointed. Clause 5 quantifies over the
**tree** and not the record, which node 36 permits. Clause 6 is the bar, the one exemption.

**The two factual claims the condition rests on were verified rather than trusted.**
`.claude/skills/expedition/graph-conventions.md` does carry a `## Mechanical checks` section, at line 371; its
opening sentence is exactly *"Every one of these is decidable by reading the files."* as clause 2 quotes it;
and it lists exactly **eight** numbered checks, as clause 3 asserts.

**One thing worth naming, and it is the node's own design rather than a defect.** Clause 2 demands a ninth
check that is *decidable by reading the files*, while this node's own `## Question` says such a check *"would
have to match prose inside `## Review`, which is the class of scan `map.md` records eleven false results
against"*. So the condition asks for something whose decidability is exactly what is in doubt — and clause 1
is the repair, fixing how the two things are written **first** so the join is exact afterwards. The order is
load-bearing: if clause 1 is done loosely, clause 2 is unsatisfiable rather than merely hard. Whoever works
this node should treat clause 1 as the work and clause 2 as its consequence.

## Answer

`.claude/skills/expedition/graph-conventions.md`'s `## Review` section now fixes a **form** for the two things
node 38 introduced, and `## Mechanical checks` gains a ninth check that reads it.

The form, under the run's entry:

```
NOT COVERED:
- OWED — "<the part, as the checker wrote it>"
- ESTABLISHED BY <who> · <what they read or ran> — "<the part, as the checker wrote it>"
```

Four calls make it decidable, and each answers one of the false-result classes `map.md` records:

1. **The state opens the item, and there are only two openings.** Whether a named part has an establisher is
   read off the item's first word — `OWED` or `ESTABLISHED BY` — and never judged from the prose after it. The
   two tokens share no prefix, so a substring scan for one cannot match the other; `UNESTABLISHED` was rejected
   for exactly that (it contains `ESTABLISHED`).
2. **The marker opens the *item*, not the line.** The part is a quote that will wrap at ~100 columns, and the
   map records that a line-based grep misses any phrase that wraps. A marker at the item's head can never be
   carried onto a continuation line, so the check needs no unwrapping at all.
3. **The label stands alone on its own line, and one item is one part.** This is the gap the map records
   against check 6 — *"every `## Flags` entry"* without saying an entry is line-anchored — closed here before it
   can be paid for. Measured rather than assumed: the string `NOT COVERED:` already occurs **six times** in this
   effort's graph files (nodes 31, 35, 38, in `## Question`, `## Answer`, `## Flags` and `## Acceptance
   condition`), every one of them prose, none line-anchored and none in a `## Review`. A scan matching the bare
   label would report six parts where there are none.
4. **The open state is written, not inferred from an absence.** `OWED` is the document's own word for it (*"the
   part is still owed"*). A form where the establisher is merely appended would make "nobody established it" and
   "the manager forgot the form" the same reading; with a positive token, an item carrying neither marker is
   malformed and visible.

Check 9 reads that form: *every item under a `NOT COVERED:` label in a `## Review` opens with `OWED` or with
`ESTABLISHED BY`, and no `resolved` node still carries one opening with `OWED`.* Two halves on purpose — the
first is the form check that makes the second exact, the second is the obligation the node exists for, and it is
a single token scan over resolved nodes with no cross-file join.

Separators are the document's existing grammar rather than new punctuation: `·` between bookkeeping tokens and
` — ` before free prose, as `flags.md`'s line already does. Measured before adopting: `·` occurs on 16 lines
across the graph corpus and in a marker position every time — zero loose prose uses. The part is quoted, so its
boundary is the quotation and not a dash the checker's own prose may contain.

**Deliberately not done: a not-covered part carries no id.** The flags precedent that this move copies came
with `NN.k`, but an id there buys a cross-file join (`## Flags` ↔ `flags.md`) and a way to point at one entry in
a list. Neither exists here: establishing is written into the same item, nothing joins across files, and the
check reads one token. Flagged as `45.1`.

Three sentences of node 38's prose moved to match the form: the entry now *quotes* each part as one item under
the label, establishing is recorded *on that same item*, a full-coverage entry carries *no label, no item and no
marker*, and an unestablished part is *"legible there as an item still opening `OWED`"* where it read *"a part
with nothing beside it"*. The section still states three things and nothing beyond them — this is entry kind 1's
form, and the sentence saying so is untouched.

## Flags

`45.1` **· settled** `ASSUMPTION` — **A not-covered part carries no id**, where the sixth delta gave every flag `NN.k` on the
human's own instruction that a flag with no id can only be pointed at by its position in a list. In the
worker's words: *"I decided the analogy does not carry: a flag's id serves a join between two files and a
pointer into a list, while a part's establisher is written into the part's own item, nothing joins across files,
and check 9 reads a token rather than an identity. So an id would be allocation bookkeeping — next unused, never
reused — for a join nothing performs, against the map's preference for short prose over machinery built for
predicted needs. Revisit if anything ever needs to cite one part among several on a run."*

`45.2` **· settled** `ASSUMPTION` — **The form's reading rules are stated locally inside `## Review` rather than as a general
rule under `## Reading the graph`**, where they would also have closed the line-anchoring gap the map records
against check 6 and `## Flags`. In the worker's words: *"My condition asks for a form decidable by matching what
that section fixes, check 6 and `## Flags` are not mine to change, and node 29 is live on precisely the class of
problem a general rule would touch. So the rules are local and check 6 is untouched."*

## Review

**Checker, run 1 — dead.** Spawned with the five givens node 42 fixed and terminated by the harness before it
took a single turn: *"Agent terminated early due to an API error: You've hit your session limit."* It
established nothing, judged nothing and raised nothing. Recorded because the record of a check is the run and
not only its verdict, and because this is the **third** dead checker run in this effort — the second inside one
day.

**Checker, run 2 — spawned fresh**, with the same five givens and **no statement of what changed**, run 1 having
established nothing at all. Telling it that a predecessor existed would be the account of what happened that
[The checker's spawn carries the effort's ground rules](42-checker-spawn-carries-ground-rules.md) forbids
travelling by the ground-rules route.

**Outcome of run 2: `PASS`. Nothing reserved, no questions, nothing handed back as not covered** — the third
consecutive check in this effort with no residual for the manager to hold, and the first run under the
`NOT COVERED:` form this very work introduced, which had nothing to record.

It established all six clauses by reading rather than by inference, and two of its methods are worth keeping.
For clause 3 it **unwrapped the whole `## Mechanical checks` section on both sides into unbroken text and
compared**, finding the two byte-identical through check 8 with check 9 the only addition — the unwrap rule
applied unprompted, from its own contract, in the file that does not state it, which is exactly [Co-locate the
scan rules with the mechanical checks](49-colocate-scan-rules.md)'s subject. For clause 4 it found the count
*"remains true rather than needing repair"*, because the new material lives inside entry kind 1 and the retained
sentence *"This is not a fourth thing on the log"* binds it there.

It disposed of the operative-content hazard itself, unprompted and correctly: *"`graph-conventions.md` is a
conventions document the repo keeps for itself, and it is the path that changed — but its operative content
governs how an effort's **graph** files are written, and the work under check is a **product** file under
`.claude/skills/`."*

**One close call, reported rather than failed, and the manager judges the checker right.** A reviewing skill it
found on the machine called the work a hard violation for coining **`item`**, which sits on a `CONTEXT.md`
`_Avoid_` line — refused as a synonym for **node**. The checker overruled it on two grounds: the bar's own
wording is *"text that uses a refused word instead of the settled one"*, and `item` never stands for a node nor
displaces `entry`, a run's entry now containing several items. And decisively, on the repo's own practice —
*"`run` is refused by name twice (under Effort and under Attempt), and the shipped, unchanged text of this very
section coins it as format vocabulary — 'the checker's chronology, one entry per run'. Failing `item` would fail
the work for a property of its own baseline."* That is a correct reading of how this effort applies its
glossary, and it is the first time a checker has **overruled a reviewing skill's hard verdict** rather than
adopting or discarding a soft finding.

One thing it named that is not a failure and not a finding: within eight lines the same token is described as
its *state*, its *opening*, its *first word* and the *marker* — *"each facet is load-bearing, but a reader holds
three words for one thing."*

**Gate: awaiting the human.**

**Gate: `approve`.** The human's words, `verbatim`: *"approve for gate 45"*. They name the outcome themselves,
which is the clause node 33's gate added to the payload doing its job for the third time.

**Both flags settled by that approval, with no separate assent asked for**, under the standing instruction filed
at [Whether flags.md survives the settle-at-close practice](27-does-flags-file-survive.md) — *"when I approve the
end of the node, the flags should be considered ok"*. The payload presented `45.1` and `45.2` in full, which is
what the instruction requires of every gate: approval discharges them, so a payload that omits one settles it
silently.
