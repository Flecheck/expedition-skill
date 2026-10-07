# Ship the FRICTION flag and the self-edit disclosure duty

Type: implementation
Status: claimed
Supersedes: 170

Blocked by: ~~56~~, ~~170~~, 392

## Question

This work lets an agent on any effort record a defect it noticed in the expedition workflow itself. It also lets the manager record a permission the human granted past a blocking contract clause. Each gets a flag marker that says what it is.

*The opening sentence above was written by [node 392](392-write-the-acceptance-conditions-for-the-five-kept-nodes.md)'s worker and filed by the manager on 2026-10-06.*

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

`41.2` `ASSUMPTION` — The disclosure duty also went into the implementation contract's GATE PAYLOAD line. *(The worker's full text is under its handover's `FLAGS`.)*

`41.3` `ASSUMPTION` — "A direction from the human" was renamed "an instruction from the human". *(The worker's full text is under its handover's `FLAGS`.)*

`41.4` `ASSUMPTION` — The glossary's and flags.md's "judgement an agent made on its own" wording was left unchanged. *(The worker's full text is under its handover's `FLAGS`.)*

`41.5` `ASSUMPTION` — The "one case only" sentence was left to node 317. *(The worker's full text is under its handover's `FLAGS`.)*

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

## Amendment, 2026-10-06 (from node 392)

*Pasted as node 392's worker wrote it. It carries the human's 2026-10-06 decision on recording a permission. Flag 392.1 records its judgement on clause 5.*

*Written by node 392's worker. The words are fixed by four sources:*
- *the condition's own clauses 1 and 5, written by node 19's worker;*
- *the human's 2026-10-06 answer on this node, which takes the recommendation to "add `PERMISSION` as a marker beside `FRICTION`, defined in one line: \"a permission the human granted for one attempt, past a contract clause that blocked the node\". It's settled like any flag. One list grows by one entry, and nothing else moves.";*
- *node 312's landed split (commit `e64b3de`): rules about the graph's files go in graph-conventions.md, and rules about the manager's choices go in SKILL.md;*
- *the shipped text of `.claude/skills/expedition/SKILL.md` under `### Two things that travel in a spawn and are not yours`.*

- **A replacement for clause 1.** Read clause 1 as: "1. `.claude/skills/expedition/graph-conventions.md`, where it lists the markers a node's `## Flags` entry may carry, lists two markers alongside `ASSUMPTION`, `CONDITION-WRONG` and `DELEGATED`, and states that the list holds five markers. One is named `FRICTION`, and its stated meaning is: a defect the agent noticed in the expedition workflow itself while using it, rather than a judgement about the work in front of it. The other is named `PERMISSION`, and its stated meaning is: a permission the human granted for one attempt, past a contract clause that blocked the node."
- **A replacement for clause 5.** Read clause 5 as: "5. `.claude/skills/expedition/SKILL.md`, under `### Two things that travel in a spawn and are not yours`, states three things: that where friction blocks a node, the way past it is an instruction from the human carried into the spawn as their own words; that where the same instruction is needed more than once, it is written into that effort's ground rules in `map.md`'s `## Notes`; and that the manager may not invent such an instruction on its own authority. Text already under that heading counts toward any of the three. `.claude/skills/expedition/graph-conventions.md` gains none of the three statements."
- **An added clause.** "11. `PERMISSION` is added to the marker list named in clause 1, and to no other file's list of markers. No sentence about how a `PERMISSION` flag settles is added anywhere. It settles under the same rules as every other flag."
- Scope of the three clauses: the scope came from no search, because the named places are the work rather than instances of a defect.

## Handover, attempt 1

*Pasted as the worker handed it back, 2026-10-06.*

`````
HANDOVER:      Ship the FRICTION flag and the self-edit disclosure duty

ANSWER:        The FRICTION and PERMISSION markers, FRICTION's settlement rule, the rule that an effort not owning the skill files never fixes them, the human's carried instruction as the way past blocking friction, and the self-edit disclosure duty are now in the shipped files. All changes are uncommitted in the worktree at 0cf4d4acf.
               - `.claude/skills/expedition/graph-conventions.md`:
                 - `### `## Flags``: "There are five markers". `FRICTION` and `PERMISSION` are added with the condition's exact meanings. The lead-in now reads "one word saying which kind of flag it is" instead of "which kind of judgement the flag records", because a permission is not a judgement.
                 - Under `flags.md`'s line form: a `FRICTION` flag uses the same form, with its marker where `ASSUMPTION` stands.
                 - `### `## Acceptance condition``: an effort whose product is not the expedition skill files never fixes them, so no acceptance condition and no condition for closing that effort may depend on a change to them.
                 - `### Settle a flag`: a `FRICTION` flag on such an effort has exactly two dispositions, refused (settled in place with the human's reason on its entry) and outstanding (left unchecked, and carried again by the effort closing report). It is never settled as fixed by an agent, for the cross-repository reason. The human may check the line by hand, and mark the entry settled, once they know the fix landed. The paragraph names the `## Flags` rule in `SKILL.md` that it changes for such a flag.
                 - A new section, `## Work that changes a file other nodes are written against`, holds the gate disclosure duty.
               - `.claude/skills/expedition/SKILL.md`, `### Two things that travel in a spawn and are not yours`: the first bullet is now "An instruction from the human" (it said "direction"). It states the three things clause 5 requires: a defect in the workflow that blocks a node is passed by the human's instruction carried as their words; an instruction needed more than once goes into the effort's ground rules in `map.md`'s `## Notes`; the manager never invents one. No `PERMISSION` text was added, and no settlement sentence for it anywhere.
               - Four worker contracts (grilling, prototype, precondition, implementation): `FRICTION` is added to "markers are yours", with the meaning "a defect in the expedition workflow itself that you noticed while using it", and to the `FLAGS:` handover line.
               - The implementation contract's `GATE PAYLOAD:` also carries the disclosure duty.
               - The checker contract, the glossary and all `.scratch/` files are untouched.

INDEX LINE:    The FRICTION and PERMISSION flag markers, FRICTION's two-disposition settlement, the carried-instruction route past blocking friction, and the gate disclosure duty for self-edits ship in the skill files.

FLAGS:
  ASSUMPTION: The disclosure duty was also put in the implementation contract's GATE PAYLOAD line. The condition places it only in graph-conventions.md, but the worker that owes it reads its contract, and on other efforts it does not read graph-conventions.md. So without this line the duty would reach nobody who owes it. Index: Node 41 added the gate disclosure duty to the implementation contract's GATE PAYLOAD line as well as graph-conventions.md, so the worker owing it reads it.
  ASSUMPTION: Renamed the first bullet under SKILL.md `### Two things that travel in a spawn and are not yours` from "A direction from the human" to "An instruction from the human". Clause 5 uses "instruction", and keeping both words for one thing would give it two names. No other shipped file used "direction" for it (grep over .claude/). Index: Node 41 renamed the spawn's "direction from the human" to "instruction from the human" so the carried-instruction rule uses one word.
  ASSUMPTION: Two places were left unchanged, following the human's "nothing else moves" on the PERMISSION decision. The glossary's `**Flag**:` entry and graph-conventions.md's description of flags.md ("every judgement an agent made on its own") still describe a flag as an agent's own judgement. A PERMISSION flag is the human's grant, and a FRICTION flag is an observation rather than a judgement. Only the marker list's lead-in was reworded ("which kind of flag it is"), because otherwise that sentence would be false next to the list it introduces. If the human wants the definitions aligned, that is a small node. Index: Node 41 left the glossary's and flags.md's "a judgement an agent made on its own" wording unchanged despite PERMISSION and FRICTION, rewording only the marker list's lead-in.
  ASSUMPTION: Did not edit SKILL.md `## Flags`'s "Flags reach the effort closing report in one case only" sentence. It becomes narrower than the outstanding-FRICTION case, but claimed node 317 replaces exactly that sentence with "every outstanding flag reaches the effort closing report", which covers it. Editing it here would collide with 317's work. graph-conventions.md's new paragraph names the SKILL.md `## Flags` rule it changes for such a flag. Index: Node 41 left SKILL.md's "one case only" closing-report sentence to node 317, which replaces it with a rule covering outstanding FRICTION flags.

NEW NODES:     none

INVALIDATIONS:
               - Node 19 (Workflow self-improvement): extended. Its settled marker, settlement rule, carried-instruction route and gate duty now ship.
               - Node 170 (merged here): answered by the PERMISSION marker.
               - Node 353: narrowed. Its answer says the markers are defined in graph-conventions.md "There are three markers: ..."; there are now five.
               - Node 312: item 17 maps "one word saying which kind of judgement the flag records", which now reads "which kind of flag it is".
               - Node 297: its recorded wording "such a direction is the only way the node can proceed" is renamed to "such an instruction".
               - Nodes 380 and 78: their answers name the spawn part "a direction from the human", now called "an instruction from the human" (rename).
               - Node 392: its note quoting "There are three markers:" is superseded as expected.

CONDITIONS:
               - Searched the conditions and questions of the open and claimed nodes (317, 393; 41 itself excluded) for "One marker is yours", "Two markers are yours", "three markers", "There are three", "FLAGS:", "prefixed ASSUMPTION", "GATE PAYLOAD", "in one case only", "direction from the human", "FRICTION", "PERMISSION", "LICENCE" and "kind of judgement".
               - Node 317 (claimed) matches on "in one case only". No clause of it is made wrong: my work leaves that sentence untouched, and 317's replacement covers outstanding FRICTION flags.
               - Node 393 is unaffected: its "all seven parts" sentences were not edited.
               - No replacement clauses.

MISSING FROM MAP: none

GATE PAYLOAD:
               - Checker: not yet run.
               - Paths touched:
                 - .claude/skills/expedition/graph-conventions.md
                 - .claude/skills/expedition/SKILL.md
                 - .claude/skills/expedition-grilling/SKILL.md
                 - .claude/skills/expedition-prototype/SKILL.md
                 - .claude/skills/expedition-precondition/SKILL.md
                 - .claude/skills/expedition-implementation/SKILL.md
               - Bar: the repo root holds no CLAUDE.md, AGENTS.md or manifest, which matches map-implementation-rules.md: no build, tests or formatter. All added lines are within the files' existing wrap width.
               - Disclosure under this node's own clause 6:
                 - Files moved: the six above. The marker list, FLAGS: lines, "markers are yours" sentences, GATE PAYLOAD line and the spawn bullet changed form.
                 - Left in the older form: every existing flag entry and flags.md line (three markers, by clause 9); the glossary `**Flag**:` entry; SKILL.md `## Flags`'s "one case only" sentence (node 317's); the precondition contract's "The flag settles at the node closing report" (not true of an outstanding FRICTION flag on a foreign effort; graph-conventions states the exception); and node answers quoting "A direction from the human" or "There are three markers".
               - Proposed commit message:
                 Ship the FRICTION and PERMISSION flag markers and the self-edit disclosure duty

                 Node: graph-workflow/41

RETROSPECTIVE:
1. What I had to hunt for:
   - Where clause 6's duty should sit in graph-conventions.md. No existing section fits a gate duty, so I added one.
   - That claimed node 317 owns the SKILL.md sentence my settlement rule makes narrow. I found it only through the CONDITIONS search, after I had already edited that sentence, and then reverted the edit.
   - `condition-collides-with-claimed-node` (new, carried by 0 earlier retrospectives): an open node's planned edit overlaps a claimed node's, and nothing in the spawn said so.
2. What arrived that the node did not need:
   - Most of map.md and map-implementation-rules.md. Only ground rules, writing rules and the bar's commands bore on the work.
   - `map-read-whole-for-a-few-items` (17 earlier retrospectives: 135, 178, 185, 205, 214, 220, 284, 317, 382, 386, 387, 388, 389, 390, 391, 392, 40).
   - `rules-file-read-whole-for-one-section` (14 earlier retrospectives: 178, 185, 214, 220, 317, 382, 386, 387, 388, 390, 391, 392, 40).
   - The node file's superseded clause text and history, read to reach the current condition.
   - `node-history-read-to-reach-current-condition` (2 earlier retrospectives: 214, 392).
3. What would have made the node easier:
   - The spawn naming node 317 as editing SKILL.md `## Flags` concurrently.
   - The condition stating the consolidated current clauses once, rather than an original plus three amendments.
4. What was stale, wrong or contradictory:
   - The node's question says it edits "the same five worker contracts as open nodes 32, 38 and 40". There are four now, and 40 is resolved.
   - `question-quotes-superseded-text` (5 earlier retrospectives: 185, 214, 317, 392, 40).
   - The manager's gap note says the FRICTION glossary entry is owed under the bar. Node 353 superseded that, as the node's own later note records.
`````

*The manager's note, 2026-10-06:* the worker is right that the spawn did not say node 317 was editing `SKILL.md`'s `## Flags` at the same time. The manager knew it and left it out.

## Amendment, 2026-10-07 (the human's answer at the gate)

*Written by the manager from the recommendation the human accepted at the gate on the checker's question. It changes one word of clause 3; every other clause stands.*

> Where clause 3 names a `FRICTION` flag's disposition "refused", read "declined". The shipped text names that disposition "declined", and says "declines" wherever it would say the human "refuses" such a flag. The words "refuse", "refused" and "refuses" do not appear in the `FRICTION` passage under `### Settle a flag`.

## Review

### Checker run 1 — `FAIL` (the bar)

*The checker's own text, pasted, 2026-10-07. A fresh checker; the condition, its amendments and the node's five flags reached it as text in `$TMPDIR/check41.md`.*

> FAIL: the bar
>
> ### Finding 1: the FRICTION settle passage changes a second SKILL.md rule without naming it (standing rule for writing 6)
> - **Instances:** In `.claude/skills/expedition/graph-conventions.md`, under `### Settle a flag`, the new passage says of an outstanding FRICTION flag: "The effort closing report of that effort carries it again."
>   - That changes a rule in `.claude/skills/expedition/SKILL.md` under `## Flags`: "Flags reach the effort closing report in one case only: a flag whose node closing report the human never answered, because they never spoke again." An outstanding FRICTION flag whose node closing report the human did answer now also reaches the effort closing report.
>   - The passage's last sentence names one SKILL.md rule it changes: "the rule under `## Flags` in `SKILL.md` that a node's flags settle at its gate or at its node closing report". It does not name the "one case only" rule, and it does not state that change.
>   - Standing rule 6 says: "A passage that changes a rule for its own case names that rule by heading and states the change in its own words."
>   - The work's wording follows the condition, so this is not a condition failure. The breach is the missing statement of the change.
>   - Found by reading the unwrapped `## Flags` section of the worktree's SKILL.md, using `awk '/^## Flags/{f=1} f&&/^## /&&!/^## Flags/{f=0} f' .claude/skills/expedition/SKILL.md | tr '\n' ' '`, and comparing it with the new passage.
> - **Form:** a sentence in the new FRICTION text of graph-conventions.md that changes, for FRICTION flags, a rule stated in another shipped file, where the passage does not name that rule by heading and state the change.
> - **Extent:** the smallest set that contains every instance is the two new FRICTION passages in graph-conventions.md. One is the paragraph after "A `FRICTION` flag raised on an effort whose product is not the expedition skill files" under `### Settle a flag`. The other is the paragraph starting "An effort whose product is not the expedition skill files never fixes those files". These are the only added text that changes how flags or conditions behave elsewhere. I checked the second one, and it changes no rule stated elsewhere. Flag 41.5 says the SKILL.md sentence was left for node 317. I did not judge that reason. The finding is only that the graph-conventions passage does not name this change.
>
> Acceptance condition (held as amended: clause 1 replaced by the 2026-10-06 text, clause 3's wording per the 2026-09-27 amendment, clause 5 replaced 2026-10-06, clause 7 replaced 2026-10-05, clause 11 added). All parts hold:
> 1. Met. The `## Flags` description in graph-conventions.md says "There are five markers". It lists ASSUMPTION, CONDITION-WRONG, DELEGATED, FRICTION (worded exactly as the clause) and PERMISSION (worded exactly as the clause). Established by `git diff` on graph-conventions.md.
> 2. Met. Directly after the `flags.md` line form: "A `FRICTION` flag uses this same form. Its marker stands where `ASSUMPTION` stands above, as every other marker does."
> 3. Met. `### Settle a flag` says there are "exactly two dispositions, and being settled as fixed is not one of them".
>    - The two dispositions are "refused", settled in place with the human's reason recorded, and "outstanding", where the line stays unchecked and "The effort closing report of that effort carries it again".
>    - It also says "No agent may mark such a flag settled as fixed", gives the reason about the repository boundary, and says the human may check the line by hand.
> 4. Met. The paragraph after the condition-scope text says "never fixes those files … no acceptance condition, and no condition for closing the effort, may be made to depend on a change to them."
> 5. Met.
>    - `.claude/skills/expedition/SKILL.md` keeps the heading `### Two things that travel in a spawn and are not yours` (`grep -n "^#"`).
>    - Its first bullet holds all three statements: the human's instruction is carried as their own words, an instruction needed more than once is written into the ground rules in `map.md`'s `## Notes`, and "Never invent such an instruction on your own authority".
>    - `grep -n "instruction\|ground rules"` over graph-conventions.md's diff shows it gained none of the three.
> 6. Met. graph-conventions.md has a new section, `## Work that changes a file other nodes are written against`, with the required duty.
> 7. Met. Each of the four files (grilling, implementation, prototype, precondition) has `FRICTION` in its `FLAGS:` line. Each one's marker paragraph says "`FRICTION`, for a defect in the expedition workflow itself that you noticed while using it". The research contract is absent from `.claude/skills/` (`ls`).
> 8. Met. `git diff --quiet HEAD -- .claude/skills/expedition-checker` exits 0.
> 9. Met. `git diff --stat HEAD -- .scratch` is empty, and `git status --porcelain --untracked-files=all` shows only the six modified paths.
> 10. Not met: see Finding 1. Under the bar there is no command to run (see below).
> 11. Met. `grep -rn PERMISSION .claude/` finds one hit, the marker list line in graph-conventions.md. No sentence about how a PERMISSION flag settles was added.
>
> The bar:
> - **No commands to run.** The worktree root has no CLAUDE.md, AGENTS.md or manifest (`ls -a`), so there is nothing to build, test or format. `git diff --check` is clean, and no added line is longer than 110 characters.
> - **Standards file.** I read only the standards in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md`.
> - **Standards that bore on this work:**
>   - graph-conventions.md
>   - the glossary's `_Avoid_` lines
>   - the ground rules
>   - the six standing rules for writing
> - **Not run:** `/coding-principles` and `/naming` (no code), and `/writing-for-agents`, which is not invocable here and which I applied through the six written rules. No reviewing skill is named, so I ran none.
> - **Where the work moved a standard:** the work changes graph-conventions.md, which is itself a standard, so I settled what moved first.
>   - The marker list, the new paragraphs and the new section are added elements, so I held them against the condition.
>   - The lead-in changing from "which kind of judgement the flag records" to "which kind of flag it is" is explanatory wording only.
>   - No element was removed.
> - **Record files:** none are among the changed paths, so the record-as-work rule did not apply.
>
> The flags, checked after the outcome:
> - 41.2 is true: the GATE PAYLOAD line has the duty.
> - 41.3 is true: `grep -rn "direction from"` over `.claude/` finds nothing.
> - 41.4 is true: "judgement an agent made on its own" is unchanged in glossary.md, in graph-conventions.md's flags.md description, and in the four contracts.
> - 41.5 is true: the "one case only" sentence is still in SKILL.md.
> - 41.1 is true as far as the work shows: the work uses "the effort closing report of that effort". Where the clause was filed is part of the record, which I can't see.
> - No flag is false.
>
> QUESTIONS:
> - One word may clash with the glossary. The condition's own disposition name "refused" (clause 3) sits beside the glossary's `**Reject**` entry, whose `_Avoid_` line lists "refuse". The work uses the condition's word as it was told to, so it was not the worker's to change. The question for the human is whether a FRICTION flag's "refused" disposition should be reworded to stay clear of the Reject entry's refused synonym. Extent: `grep -n "refused" .claude/skills/expedition/graph-conventions.md`, one hit in the new `### Settle a flag` passage.
>
> I wrote no temporary files.

*The manager's note:* under the human's ruling that a `FAIL` goes straight back to the worker for a correction round, the finding is sent to the worker. The checker's question on "refused" goes to the human at the gate.


### Correction round 1

*The worker's handover, pasted as handed back, 2026-10-07.*

`````
HANDOVER:      Ship the FRICTION flag and the self-edit disclosure duty (correction round 1)

ANSWER:        Unchanged from the first handover, except under `### Settle a flag` in `.claude/skills/expedition/graph-conventions.md`. The FRICTION passage now ends by naming both of the rules under `## Flags` in `SKILL.md` that it changes for such a flag, each with the change stated:
               - The rule that a node's flags settle at its gate or at its node closing report. Such a flag stays outstanding past both, until the human refuses it or checks it by hand.
               - The rule on which flags reach the effort closing report. Such a flag reaches that report while it is outstanding, whatever that rule says of other flags.

INDEX LINE:    The FRICTION and PERMISSION flag markers, FRICTION's two-disposition settlement, the carried-instruction route past blocking friction, and the gate disclosure duty for self-edits ship in the skill files.

FLAGS:         The four ASSUMPTION flags from the first handover stand as written. The fourth one ("Did not edit SKILL.md `## Flags`'s 'one case only' sentence ...") is still true: the sentence is untouched. graph-conventions.md now also names the rule that sentence states, as the paragraph it changes. No new flags.

NEW NODES:     none

INVALIDATIONS: unchanged from the first handover.

CONDITIONS:    Unchanged. Node 317 (passed its check, gate waiting on the human) replaces the "one case only" sentence with "Every outstanding flag reaches the effort closing report, whatever the state of its node." The new wording reads correctly against both states of the tree:
               - Against the tree this work starts from, it names the "one case only" rule and says what changes for an outstanding FRICTION flag.
               - Once 317 lands, "whatever that rule says of other flags" stays true, and nothing in the passage quotes or depends on the sentence 317 removes.

MISSING FROM MAP: none

GATE PAYLOAD:
               - Checker run 1, Finding 1 (standing rule for writing 6): fixed.
                 - The single closing sentence of the `### Settle a flag` FRICTION passage is replaced by a lead-in, "This changes, for such a flag, two rules under `## Flags` in `SKILL.md`:", followed by two bullets. Each bullet names one rule and states the change for such a flag.
                 - The second bullet is the one the checker found missing: the rule on which flags reach the effort closing report.
                 - The other FRICTION passage, under `### `## Acceptance condition``, is unchanged. As the checker found, it changes no rule stated elsewhere.
               - Does the change touch anything the acceptance condition names? Yes. It is inside the `### Settle a flag` procedure, which clause 3 names. The clause 3 content (two dispositions, never settled as fixed, the cross-repository reason, the human ticking the line by hand) is unchanged.
               - The checker's question to the human ("refused" against the glossary's Reject `_Avoid_` line): not acted on, as instructed. "refused" is the condition's own word.
               - Paths touched this round: `.claude/skills/expedition/graph-conventions.md`.
               - Paths touched overall:
                 - .claude/skills/expedition/graph-conventions.md
                 - .claude/skills/expedition/SKILL.md
                 - .claude/skills/expedition-grilling/SKILL.md
                 - .claude/skills/expedition-prototype/SKILL.md
                 - .claude/skills/expedition-precondition/SKILL.md
                 - .claude/skills/expedition-implementation/SKILL.md
               - Bar: unchanged. This repo has no build, tests or formatter, and the new lines are within the existing wrap width.
               - Clause 6 disclosure: same as the first handover. No further file moved.
               - Proposed commit message:
                 Ship the FRICTION and PERMISSION flag markers and the self-edit disclosure duty

                 Node: graph-workflow/41

RETROSPECTIVE:
- `one-rule-stated-at-several-sites`: carried by 1 earlier retrospective (node 178). Which flags reach the effort closing report is stated in SKILL.md `## Flags`, and now also implied by graph-conventions' settle procedure. I noticed the collision with node 317's sentence but treated "leave it to 317" as enough. The writing standard required the passage to name every rule elsewhere that it changes, whoever later edits that rule.
- `condition-collides-with-claimed-node`: carried by 0 earlier retrospectives; it is my own first-round name. It recurs here: a claimed node's pending change shaped what the fix had to say, so that it reads correctly both before and after 317 lands.
`````

### Checker run 2 — `PASS`

*The checker's own text, pasted, 2026-10-07. The run 1 checker, resumed for the re-check.*

> PASS
>
> This re-check comes after correction round 1, in the same worktree with the work still uncommitted.
>
> **What changed this round.**
> - The six changed paths are the same as last round (`git status --porcelain --untracked-files=all`).
> - Only graph-conventions.md was touched after SKILL.md (`find .claude -newer .claude/skills/expedition/SKILL.md -type f`).
> - I reread the full added text of graph-conventions.md and SKILL.md (`git diff HEAD | grep '^[-+]'`). The one change from last round is under `### Settle a flag`. The old closing sentence, which named only the settle-timing rule, has become a lead-in, "This changes, for such a flag, two rules under `## Flags` in `SKILL.md`:", followed by two bullets:
>   - when a node's flags settle: "Such a flag stays outstanding past both, until the human refuses it or checks it by hand."
>   - which flags reach the effort closing report: "Such a flag reaches that report while it is outstanding, whatever that rule says of other flags."
> - This matches the worker's statement, and nothing else moved.
>
> **Last round's Finding 1 (writing rule 6) is repaired.** The passage now names both `SKILL.md` `## Flags` rules it changes, and states the change for each.
>
> The condition, as amended:
> 1. Met, and the text is unmoved. graph-conventions.md says "There are five markers". `FRICTION` and `PERMISSION` are listed with the meanings the clause gives.
> 2. Met, and the text is unmoved. The sentence "A `FRICTION` flag uses this same form…" follows the `flags.md` line form.
> 3. Re-established, because this round edited the passage. The passage still holds:
>    - "exactly two dispositions, and being settled as fixed is not one of them";
>    - refused, settled in place by steps 1 and 2 with the human's reason recorded;
>    - outstanding, left unchecked and carried again in "The effort closing report of that effort";
>    - "No agent may mark such a flag settled as fixed", with the reason about the repository boundary;
>    - the human checking the flag's line by hand once the fix landed.
>
>    The new bullets add to this and contradict nothing in the clause.
> 4. Met, and the text is unmoved. The paragraph "An effort whose product is not the expedition skill files never fixes those files…" is unchanged.
> 5. Met, and the text is unmoved. `SKILL.md` under `### Two things that travel in a spawn and are not yours` holds all three statements, and graph-conventions.md gains none of them (from the diff).
> 6. Met, and the text is unmoved. The section `## Work that changes a file other nodes are written against` is unchanged.
> 7. Met, and the diff for these files is the same size as last round. The four contracts each list `FRICTION` in their marker paragraph and their `FLAGS:` line, with the meaning required.
> 8. Met. `git diff --quiet HEAD -- .claude/skills/expedition-checker .scratch` exits 0.
> 9. Met, by the same command.
> 10. Met. See the bar below.
> 11. Met. `grep -rn PERMISSION .claude/` gives one hit, the marker-list line. The new bullets say nothing about how a `PERMISSION` flag settles.
>
> The bar, re-run in full:
> - **Commands:** the repo has no build, test or format commands, since the root has no CLAUDE.md, AGENTS.md or manifest. `git diff --check` is clean, and no added line is over 110 characters.
> - **Standards:** I read only the standards in `map-implementation-rules.md`. The ones that bear on this work:
>   - graph-conventions.md;
>   - the glossary's `_Avoid_` lines;
>   - the ground rules;
>   - the six standing rules for writing.
> - **The edited standard:** graph-conventions.md is both changed by this work and one of the standards. This round's edit only adds elements, so the analysis from last round stands.
> - **Breaches:** none found.
> - **Record files:** none are among the changed paths.
>
> **Flags.** The flags are unchanged, and none is false. 41.5 is still true: the "one case only" sentence is unchanged in SKILL.md, and graph-conventions.md now names its change for `FRICTION` flags.
>
> My question about "refused" stands as handed back last round. My view of it has not changed.
>
> I wrote no temporary files.

*The manager's note:* the checker's run 1 question on "refused" still stands beside this outcome, so the standing yes does not cover this gate. It goes to the human.

### Gate — sent back, 2026-10-07

`verbatim`: *"ok"*

*The manager's note:* the manager's message ended "Please answer: \"ok for recommended\" sends node 41 back for that rename, or say approve as is." The recommendation was to rename "refused" to "declined" in the new passage, including "until the human refuses it", so the gate word "reject" stays unambiguous. The reply takes it, and the amendment above records it.

