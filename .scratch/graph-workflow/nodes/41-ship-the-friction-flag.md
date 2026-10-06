# Ship the FRICTION flag and the self-edit disclosure duty

Type: implementation
Status: claimed
Supersedes: 170

Blocked by: ~~56~~, ~~170~~

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

## Amendment, 2026-09-27 (from node 137)

*Written by [node 137](137-rename-the-two-reports-and-repair-the-avoid-line.md)'s worker under its `CONDITIONS`, and filed by the manager after that node landed as commit `fe2610b`, whose `**Effort closing report**:` entry in `CONTEXT.md` fixes every word of it. Under node 137's rule a bare "closing report" means the node closing report, and "that effort's" is a possessive, not the `effort` prefix.*

- **A replacement.** Where this condition reads "outstanding — left unchecked, meaning carried, and re-surfaced in that effort's closing report", read "outstanding — left unchecked, meaning carried, and re-surfaced in the effort closing report of that effort."

## Flags

`41.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above.* Node 137's worker's replacement clause was filed on this open, unclaimed node without asking the human first, under the rule node 327 landed.

*The manager's note, 2026-09-27:* [node 56](56-ship-the-glossary-into-the-skill-set.md)'s worker reports this node's question is changed, once node 56 lands. Its words, pasted: Node 41 (open), question changed: the entry for `FRICTION` that its worker owes under the bar now goes in `.claude/skills/expedition/glossary.md`. The completeness paragraph node 29 designed is now in place, so node 41 is the mechanism's first test as planned. Its manager-note link `[CONTEXT.md](../../../CONTEXT.md)` now reaches the superseded pointer. Its condition clause "written into that effort's ground rules in `map.md`'s `## Notes`" agrees with the new `Ground rules` entry.

*The manager's note, 2026-09-28:* [node 353](353-whether-implementer-becomes-a-glossary-headword.md)'s worker reports this node's question changed. Its words, pasted: Node 41 (open, implementation): the question changes, but no clause does. The manager's 2026-09-27 note, relaying node 56's worker, says the `FRICTION` entry its worker owes "now goes in `.claude/skills/expedition/glossary.md`". Under this answer, `FRICTION` is a flag marker and owes no glossary entry. So that obligation, and the manager's filing note that `UPSTREAM` belongs in the glossary as its refused alternative, no longer hold. The marker is defined where its shape is defined, which clauses 1 and 7 already require. Its condition does not mention the glossary, so no replacement clause is needed. Clause 8 ("the checker contract is not changed by this work") limits that node's own work and does not conflict with the new rename node, which changes that file.

## Edge, 2026-09-29 (from node 366)

*The manager's note:* node 41 gains `Blocked by: 170`, carrying out the human's answer to [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q3 (`verbatim`: *"ok"*) as node 366's worker proposed: 41 and 170 edit the same closed list of flag markers, and 170 still waits on a human choice. See flag 366.3. Node 56, its earlier blocker, is resolved.

*The manager's note, 2026-10-05:* [node 385](385-whether-the-rarely-used-node-kinds-should-stay.md)'s worker reported under its `CONDITIONS` that this condition's file list includes `.claude/skills/expedition-research/SKILL.md`, which becomes wrong once [node 388](388-merge-research-into-precondition-and-remove-the-cascade-pass.md) lands: "When the new node lands, the replacement is the same list without that path, fixed by that landed work. The manager amends it then, node 41 being unclaimed."

## Amendment, 2026-10-05 (from node 388's landing)

*Replacement for clause 7, written by [node 388](388-merge-research-into-precondition-and-remove-the-cascade-pass.md)'s worker under its `CONDITIONS`, and filed by the manager now that node 388 has landed (commit `5f8c85480`) and deleted the research contract. Node 41 is open and unclaimed. Its words are the clause's own minus that path.*

> 7. Each of these four files lists `FRICTION` among the markers its worker may use, and includes it in that file's `FLAGS:` handover line, with its meaning stated as a defect in the expedition workflow itself that this worker noticed while using it: `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md`

## Amendment, 2026-10-06 (node 170 merged in at the triage)

Node 170's question is merged into this node: both change the closed list of flag markers under `graph-conventions.md`'s `### `## Flags``. Node 170 had no acceptance condition, so no clause moves. Its question, pasted as it stands on node 170:

> *Surfaced by the manager while filing [flag `144.5`](144-make-the-rules-file-stand-alone.md). The manager's own text,
> and marked as the manager's.*
>
> The manager's contract says that where a clause of a worker contract blocks the node in front of it, the manager
> raises it, and the human's answer produces **two things, always both**: *"a licence for that one attempt, recorded as
> a flag on the node"*, and a node for the permanent fix.
>
> `graph-conventions.md`'s `## Flags` section defines **three** markers and closes the list: `ASSUMPTION` — the worker
> decided a small ambiguity itself; `CONDITION-WRONG` — the manager's, after a worker raised its condition as wrong and
> the human said ship it anyway; and `DELEGATED` — the human said *"you decide"* and the worker answered.
>
> **A licence is none of the three.** It is not a judgement an agent made on its own, which is what the glossary says a
> flag records; it is the human's own grant, made in answer to a raise, and it binds one attempt. Recording it under
> any of the three states something false about who judged what. The manager wrote `LICENCE` on flag `144.5` for that
> reason, which is a marker no file defines.
>
> **Two settled rules produce a duty neither states**, which is the shape this effort's own contract names as a node
> rather than something to settle in the moment.

Before a worker starts this node, the human chooses how a permission the human grants is recorded (a fourth marker, an open-ended marker list, or somewhere other than `## Flags`), and that choice becomes a clause here. The term in `SKILL.md` is now "permission", not "licence".

*The human's answer to the triage proposal, `verbatim`, 2026-10-06:* *"ok"*. The manager's proposal ended "Please answer Q1 to Q4. \"ok for all\" approves each as proposed."


## Interview

#### The human's answer on recording a permission, 2026-10-06

*The manager put node 170's question, merged here, directly after the 2026-10-06 triage. The manager's recommendation, as sent:* "add `PERMISSION` as a marker beside `FRICTION`, defined in one line: \"a permission the human granted for one attempt, past a contract clause that blocked the node\". It's settled like any flag. One list grows by one entry, and nothing else moves." *Alternatives offered: declare the marker list open-ended; record permissions outside `## Flags`, in the node's interview. The message ended:* "Please answer. \"ok for recommended\" takes the `PERMISSION` marker."

`verbatim`: *"ok"*

*The manager's note:* the reply takes the recommendation. It is still to become an amendment clause on this node's condition.
