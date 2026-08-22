# Ship the FRICTION flag and the self-edit disclosure duty

Type: implementation
Status: open

Blocked by: 56

## Question

Land in the shipped files what node 19 settled: the `FRICTION` marker, its settlement rule, the fact that an
effort not owning the skill never fixes it, the human's carried instruction as the way past blocking friction,
and the gate-disclosure duty on a self-edit.

Two things whoever claims this should know. It edits the same five worker contracts as open nodes 32, 38 and
40, and the code slot is exclusive, so whichever lands first moves text the others were written against —
which is this node's own subject arriving on schedule. And a checker's route to raising a `FRICTION` flag is
deliberately out of scope here: a checker writes no flag, and what it hands back belongs to nodes 38 and 40.

Reported by [Workflow self-improvement during use](19-workflow-self-improvement.md)'s worker, which wrote the
acceptance condition below.

## Acceptance condition

Done when all of the following hold.

1. `.claude/skills/expedition/graph-conventions.md`, where it lists the markers a node's `## Flags` entry may
   carry, lists a fourth alongside `ASSUMPTION`, `CONDITION-WRONG` and `DELEGATED`. It is named `FRICTION` and
   its stated meaning is: a defect the agent noticed in the expedition workflow itself while using it, rather
   than a judgement about the work in front of it.
2. The same document, where it gives `flags.md`'s line form, states that a `FRICTION` flag uses that same form
   and carries that marker in the same position as the others.
3. The same document's *Settle a flag* procedure states that a `FRICTION` flag raised on an effort whose
   product is not the expedition skill files has exactly two dispositions, and that being settled as fixed is
   not one of them:
     - refused — the human judges it not worth carrying, and it is settled in place with their reason
       recorded;
     - outstanding — left unchecked, meaning carried, and re-surfaced in that effort's closing report.
   It further states that no agent may mark such a flag settled-as-fixed, because the fix lands only in the
   repository holding the expedition skill files and no agent crosses a repository boundary; and that the
   human may check the line by hand once they know the fix landed.
4. The same document states that an effort whose product is not the expedition skill files never fixes those
   files, and that therefore no acceptance condition and no closing condition on such an effort may be made to
   depend on a change to them.
5. The same document states that where friction blocks a node, the way past it is an instruction from the
   human carried into the spawn as their own words; that where the same instruction is needed more than once
   it is written into that effort's ground rules in `map.md`'s `## Notes`; and that the manager may not invent
   such an instruction on its own authority.
6. The same document states that an implementation node which changes a file that other nodes of the same
   effort are written against must, at its gate, name which files it moved and which existing files are left
   in the older form.
7. Each of these five files lists `FRICTION` among the markers its worker may use, and includes it in that
   file's `FLAGS:` handover line, with its meaning stated as a defect in the expedition workflow itself that
   this worker noticed while using it:
     `.claude/skills/expedition-grilling/SKILL.md`
     `.claude/skills/expedition-implementation/SKILL.md`
     `.claude/skills/expedition-prototype/SKILL.md`
     `.claude/skills/expedition-precondition/SKILL.md`
     `.claude/skills/expedition-research/SKILL.md`
8. `.claude/skills/expedition-checker/SKILL.md` is not changed by this work.
9. No existing flag entry in any file under `.scratch/graph-workflow/` has its marker or its settled state
   changed: the marker is added to the shipped documents only.
10. The working tree meets the bar.

### One gap the manager found in this condition while filing it, and did not repair

*The manager's own note, not a change to the condition above.* The condition never reaches
[`CONTEXT.md`](../../../CONTEXT.md), and `FRICTION` is a new term in the workflow's vocabulary. The precedent
is [Carry the recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md), where the
glossary followed on three entries in the same commit, and the map records forty terms living there with their
rejected synonyms attached — which is where `UPSTREAM` would belong as this marker's refused alternative. The
worker's own words at the round that proposed the marker were that shipping it needs *"one paragraph in
`graph-conventions.md` and one glossary entry"*, so the omission is against its own stated plan rather than
against a rule it never saw.

Left unrepaired because the condition is the minting worker's text and supplying what it omits would make the
manager the author of part of the standard, which [An acceptance condition is self-contained
text](33-condition-is-self-contained.md) forbids for the same reason. It is recorded here so that the audit at
claim time meets it rather than has to find it, and so that whoever claims this node knows the question is
live rather than settled. Note also that this is [What keeps the shipped files consistent when a decision
changes a term](29-shipped-file-consistency.md)'s problem recurring inside a condition: a list of files a
decision is owed to, correct about the files it knew.

## Annotation: now blocked, and it is the deliberate first test of node 29's mechanism

*Filed by the manager at [What keeps the shipped files consistent when a decision changes a
term](29-shipped-file-consistency.md)'s resolution, in that worker's own words:*

> [Ship the FRICTION flag and the self-edit disclosure duty](41-ship-the-friction-flag.md) gains `Blocked by:`
> that node. It coins `FRICTION` and its condition never reaches the glossary; landing it second means its
> worker owes the entry under the bar, without the condition being amended and without the manager writing it.
> That is this answer's first real test, and it is the case the manager recorded twice and left alone.

**So this node's `Blocked by:` gains 56** — not because its work depends on the glossary's location, but because
it is the case node 29's mechanism was designed to catch, and running it first would waste the only clean test
available. `FRICTION` is one of the two terms this effort has shipped with no glossary entry; the other,
`ground rules`, is written by node 56 itself. **Under the mechanism, this node's worker owes the `FRICTION`
entry by way of the bar, with nothing in its acceptance condition saying so** — and if it does not deliver it,
the blind checker should fault the work for it. Either outcome is informative.

The manager notes against its own past practice: this is the case it met twice while filing conditions and left
unrepaired both times, on the ground that supplying what a condition omits makes the manager the author of the
standard. Node 29's answer is what makes that refusal correct rather than merely principled.
