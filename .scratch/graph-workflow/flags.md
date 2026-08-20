# Flags

Every flag in the graph, one capped line each, with its state. The **only** file the sweep reads to
build the completion report: the report is the unchecked lines. Specified by
[Graph file format](nodes/13-graph-file-format.md).

- `[ ]` outstanding · `[x]` settled by the human
- ~~The checkbox lives **only here**. The flag's text and reasoning live in its node's `## Flags`
  section, so the two can never disagree and settling a flag never touches a node file.~~
  **Overruled by the human** at [Write the worker contract skills](nodes/22-worker-contract-skills.md)'s
  gate: a settled flag is marked `settled` in its node's `## Flags` section too, so someone reading a node
  can see which of its judgements are still live without opening this file. The state is genuinely in two
  places now — **this file wins** where they disagree, since the report is built from it. The flag's text
  and reasoning still live on the node.
- **The manager aims to settle a node's flags as it closes that node**, putting them to the human then
  rather than leaving them here for the report. The human's instruction at the same gate: while the node is
  still open the work is still there, so acting on a flag is cheap. Eleven of eleven were settled that way
  on that node.
- Three kinds, from [Node type taxonomy](nodes/07-node-type-taxonomy.md) and
  [Relay protocol](nodes/08-relay-protocol.md): `ASSUMPTION` (an implementer decided a small
  ambiguity itself), `CONDITION-WRONG` (~~an implementer judged its acceptance condition wrong but may
  not rewrite it~~ **the human answered a raise about a wrong acceptance condition with *carry on, ship it
  anyway*; the judgement is no longer the worker's alone**, changed by [When an AFK worker cannot
  proceed](nodes/23-worker-cannot-proceed.md)), `DELEGATED` (the human said "you decide" and the subagent
  answered).
- **Append-only.** A settled flag is checked, never removed.

Format:

```
- [ ] NN.k ASSUMPTION · [<node name>](nodes/NN-<name>.md) — <one line>
```

**`NN.k` is the flag's id**, added at the same gate: the node's own number, then a sequence
within that node, allocated in write order and never reused. It is what lets a human name one flag out of
eleven, and it turns mechanical check 6 into an exact join rather than a match on prose. The twenty lines
below predate it and carry none.

## Outstanding and settled

~~*(none yet — no implementation node has run on this map)*~~

- [ ] ASSUMPTION · [Naming the workflow and its vocabulary](nodes/14-naming.md) — wrote `CONTEXT.md` into the product tree from a grilling node, so the glossary passed no checker and no gate.
- [ ] CONDITION-WRONG · [Write the graph conventions document](nodes/21-conventions-document.md) — acceptance condition 4's first clause is false: Naming's renames break three lines of the target's tracker doc, so all three ship as divergences instead.
- [ ] ASSUMPTION · [Write the graph conventions document](nodes/21-conventions-document.md) — wrote the document to `.claude/skills/expedition/`, pinning the skill's install location inside live fog.
- [ ] ASSUMPTION · [Write the graph conventions document](nodes/21-conventions-document.md) — ships no frontier ordering rule, since [Human-initiated steering](nodes/16-human-steering.md) is open and owns it.
- [ ] ASSUMPTION · [Write the graph conventions document](nodes/21-conventions-document.md) — resolved on a truncated checker run: Phase 1 passed condition 6, phases 2–4 never ran and no overall verdict was issued.
- [ ] ASSUMPTION · [Subagent context contract](nodes/12-subagent-context-contract.md) — read "invocable by name" as six sibling skill directories, since a supporting file cannot be invoked; layout left to node 22.
- [ ] ASSUMPTION · [Subagent context contract](nodes/12-subagent-context-contract.md) — the method skills the contracts name are per-install, not per-repo; each names them *invoke if present*, unverified on a machine without them.
- [ ] ASSUMPTION · [Subagent context contract](nodes/12-subagent-context-contract.md) — resolved with no worker and no relay: the manager grilled directly, so the contract routed none of its own interview.
- [ ] ASSUMPTION · [Human review of landed code](nodes/20-human-code-review.md) — the code travels as a pointer and the diff is never rendered; inferred from the human's answer rather than stated by them.
- [ ] ASSUMPTION · [Human review of landed code](nodes/20-human-code-review.md) — a rejected diff is discarded with one line offering to keep it; the human defined reject's meaning but not the work's fate.
- [ ] ASSUMPTION · [Human review of landed code](nodes/20-human-code-review.md) — a checker that will not pass still reaches the gate, qualifying the human's statement that its findings are fixed first.
- [ ] ASSUMPTION · [Human review of landed code](nodes/20-human-code-review.md) — renamed the checker's `REJECT` to `FAIL` to free the word for the gate, correcting a token node 12 fixed.
- [ ] ASSUMPTION · [Human review of landed code](nodes/20-human-code-review.md) — depth of review is never measured, leaving node 10's accepted residual risk unquantified by construction.
- [ ] ASSUMPTION · [Friction from running this map by hand](nodes/24-self-hosted-friction.md) — resolved as a second node in one session, which the inherited one-node-per-session rhythm forbids.
- [ ] ASSUMPTION · [Friction from running this map by hand](nodes/24-self-hosted-friction.md) — written retrospectively from a manager's memory across compacted sessions; the transcripts were not re-read.
- [ ] ASSUMPTION · [When an AFK worker cannot proceed](nodes/23-worker-cannot-proceed.md) — the salvage's form and place are chosen here: an unread path-limited diff at `<effort>/salvage/NN-<attempt>.patch`, with new files marked intent-to-add.
- [ ] ASSUMPTION · [When an AFK worker cannot proceed](nodes/23-worker-cannot-proceed.md) — corrected node 07's "never asks live" by annotation and redefined `AFK` to absorb it; second settled clause corrected this way.
- [ ] ASSUMPTION · [When an AFK worker cannot proceed](nodes/23-worker-cannot-proceed.md) — read the three triggers as disjunctive and ungated, so a worker that could pick must still raise; the reading most likely to produce noise.
- [ ] ASSUMPTION · [When an AFK worker cannot proceed](nodes/23-worker-cannot-proceed.md) — let the human rewrite an acceptance condition in place on a claimed node, a third revision case node 06 does not name.
- [ ] ASSUMPTION · [When an AFK worker cannot proceed](nodes/23-worker-cannot-proceed.md) — resolved with no worker and no relay: a node about the worker's channel to the human routed nothing through it.
- [x] 22.1 ASSUMPTION · [Write the worker contract skills](nodes/22-worker-contract-skills.md) — six sibling skill directories at `.claude/skills/expedition-<type>/SKILL.md`, inheriting node 21's install-location assumption.
- [x] 22.2 ASSUMPTION · [Write the worker contract skills](nodes/22-worker-contract-skills.md) — the raise reaches implementer, checker and precondition; `research` alone is flag-only, on the glossary rather than on a stated scope.
- [x] 22.3 ASSUMPTION · [Write the worker contract skills](nodes/22-worker-contract-skills.md) — the code reaches the checker as changed paths in the working tree rather than as rendered text.
- [x] 22.4 ASSUMPTION · [Write the worker contract skills](nodes/22-worker-contract-skills.md) — the checker is given the node's name to address a raise, on the reading that a name is not part of the node file.
- [x] 22.5 ASSUMPTION · [Write the worker contract skills](nodes/22-worker-contract-skills.md) — each contract carries the glossary subset its own text uses, so the vocabulary now lives in seven places.
- [x] 22.6 ASSUMPTION · [Write the worker contract skills](nodes/22-worker-contract-skills.md) — written by the manager rather than by a worker, so none of the six has been run by the agent it is written for.
- [x] 22.7 ASSUMPTION · [Write the worker contract skills](nodes/22-worker-contract-skills.md) — the checker's contract uses `code-review`, a word the glossary refuses for the agent, as the name of a thing a repo may carry.
- [x] 22.8 ASSUMPTION · [Write the worker contract skills](nodes/22-worker-contract-skills.md) — the checker's blindness outranks a method skill's procedure, written from what a checker did unprompted mid-run.
- [x] 22.9 ASSUMPTION · [Write the worker contract skills](nodes/22-worker-contract-skills.md) — the checker finds the standards it holds work against rather than being handed them, loosening *checks against something stated*.
- [x] 22.10 ASSUMPTION · [Write the worker contract skills](nodes/22-worker-contract-skills.md) — a method skill's question to the human is non-blocking, carried alongside the outcome rather than waited on.
- [x] 22.11 ASSUMPTION · [Write the worker contract skills](nodes/22-worker-contract-skills.md) — a re-checking checker distrusts the manager's statement of what changed, finding omissions by modification time.
- [x] 17.1 ASSUMPTION · [Off-contract subagent output](nodes/17-off-contract-output.md) — an implementer whose code fails its acceptance condition was ruled outside this node alone; the human was never asked whether the two are one mechanism.
- [x] 17.2 ASSUMPTION · [Off-contract subagent output](nodes/17-off-contract-output.md) — an unfileable return is never written onto the node, reading never-delete as governing what is in the graph's files rather than what must enter them.
- [x] 17.3 ASSUMPTION · [Off-contract subagent output](nodes/17-off-contract-output.md) — declined the human's own word `reject` for an unfileable handover, changing their wording rather than following it.
- [x] 17.4 ASSUMPTION · [Off-contract subagent output](nodes/17-off-contract-output.md) — filed by the manager running this node's own check: a paragraph of the answer rests on a manager note rather than on anything the human said.
- [x] 25.1 ASSUMPTION · [What is recorded when the human takes an option as offered](nodes/25-recording-an-option-taken.md) — corrects a resolved node's `## Interview` markers in place, without the human having been asked whether a resolved node's record may be edited at all.
- [x] 25.2 ASSUMPTION · [What is recorded when the human takes an option as offered](nodes/25-recording-an-option-taken.md) — extended the rule to `## Review` as well as `## Interview`, on the ground that a gate approval is the same act as taking an option.
- [x] 25.3 ASSUMPTION · [What is recorded when the human takes an option as offered](nodes/25-recording-an-option-taken.md) — an unclear terse reply is recorded and asked about rather than resolved by the manager, the one case left that costs a round trip.
- [x] 27.1 ASSUMPTION · [Whether flags.md survives the settle-at-close practice](nodes/27-does-flags-file-survive.md) — read the nineteen-of-nineteen settle rate from the record as a calibrated marker rather than a gate that stopped filtering, without asking the human.
- [x] 27.2 ASSUMPTION · [Whether flags.md survives the settle-at-close practice](nodes/27-does-flags-file-survive.md) — left mechanical check 6 an existence join, so nothing detects a node marked `settled` whose line here is still unchecked. **Overruled**: the check is extended.
- [x] 27.3 ASSUMPTION · [Whether flags.md survives the settle-at-close practice](nodes/27-does-flags-file-survive.md) — filed by the manager: the answer replaces the *ground* of a resolved node's rule in the shipped document, on a manager note rather than on the human's words.
- [x] 25.4 ASSUMPTION · [What is recorded when the human takes an option as offered](nodes/25-recording-an-option-taken.md) — filed by the manager: two of the answer's sections, including the one that produced `25.1`, entered from manager notes rather than from the human or the worker's reading.
- [x] 26.1 ASSUMPTION · [Carry the recorded deltas into the shipped skill files](nodes/26-carry-deltas-into-shipped-files.md) — stated the option-taken and ordering rules once in a shared subsection naming both logs, satisfying "for both" by reference rather than by duplication.
- [x] 26.2 ASSUMPTION · [Carry the recorded deltas into the shipped skill files](nodes/26-carry-deltas-into-shipped-files.md) — chose the punctuation for a flag id in this file's own line form while leaving this file unread, as the contract requires; the guess matches what is already here.
- [x] 26.3 ASSUMPTION · [Carry the recorded deltas into the shipped skill files](nodes/26-carry-deltas-into-shipped-files.md) — made two edits no delta required, both grounded in node 20: `### Review` no longer says "landed", and the three reject routes are named inline.
- [x] 26.4 ASSUMPTION · [Carry the recorded deltas into the shipped skill files](nodes/26-carry-deltas-into-shipped-files.md) — filed by the manager: two of this node's conditions point into the record, which a blind checker may not read, so the manager dereferenced one and passed the other through.
- [x] 26.5 ASSUMPTION · [Carry the recorded deltas into the shipped skill files](nodes/26-carry-deltas-into-shipped-files.md) — corrected the glossary's `Flag` entry on *who* leaves a flag as well as on `CONDITION-WRONG`, the record already carrying four manager-filed flags.
- [x] 26.6 ASSUMPTION · [Carry the recorded deltas into the shipped skill files](nodes/26-carry-deltas-into-shipped-files.md) — replaced a glossary sentence no delta names, going beyond the human's `fix`; it was stale on the record too, in a node the worker never read.
- [x] 26.7 ASSUMPTION · [Carry the recorded deltas into the shipped skill files](nodes/26-carry-deltas-into-shipped-files.md) — filed by the manager: the human extended this node's scope by instruction without rewriting its acceptance condition, so one product file is covered by no condition at all.
- [x] 26.8 ASSUMPTION · [Carry the recorded deltas into the shipped skill files](nodes/26-carry-deltas-into-shipped-files.md) — filed by the manager: shipped with `raise` carrying two senses in adjacent glossary entries, the fix that would settle it being out of an implementation node's reach. **Overruled**: the word was generalised instead.
- [x] 26.9 ASSUMPTION · [Carry the recorded deltas into the shipped skill files](nodes/26-carry-deltas-into-shipped-files.md) — re-grounded the `_Avoid_` clause refusing `ask`, there being no *Ask* entry to check; without it the widened `raise` swallows a grilling node's interview. **Settled by the human supplying a different ground**: what the worker is built for, not what the turn is.
- [x] 28.1 ASSUMPTION · [Whether a spawn may override a shipped worker contract](nodes/28-spawn-overriding-a-contract.md) — the three-route triage is the worker's own; the human assented only to the clause that the manager may not depart on its own authority.
- [x] 28.2 ASSUMPTION · [Whether a spawn may override a shipped worker contract](nodes/28-spawn-overriding-a-contract.md) — wrote the rule over anything the manager sends a worker, spawn or resume, rather than over the spawn; not put to the human.
- [x] 28.3 ASSUMPTION · [Whether a spawn may override a shipped worker contract](nodes/28-spawn-overriding-a-contract.md) — judged the checker contract's closed list load-bearing but mis-grounded, and proposed re-grounding rather than removal, from the file rather than by asking.
- [x] 28.4 ASSUMPTION · [Whether a spawn may override a shipped worker contract](nodes/28-spawn-overriding-a-contract.md) — ruled the dereferenced acceptance condition not an override at all and placed its defect upstream, in how a condition is written; decided alone.
- [x] 28.5 ASSUMPTION · [Whether a spawn may override a shipped worker contract](nodes/28-spawn-overriding-a-contract.md) — named the manager's own question a `raise` under the glossary's generalised sense, describing a channel the design never had, on a reading of an existing term.
- [x] 28.6 ASSUMPTION · [Whether a spawn may override a shipped worker contract](nodes/28-spawn-overriding-a-contract.md) — filed by the worker about the manager: the raise-firing-rate clause came from a manager note and entered the node's permanent text, the fifth node in a row.
- [x] 33.1 ASSUMPTION · [An acceptance condition is self-contained text](nodes/33-condition-is-self-contained.md) — read node 21's "no reasoning" clause as refusing the record behind a decision, not an operative statement of what a rule protects, from five such clauses already shipped.
- [x] 33.2 ASSUMPTION · [An acceptance condition is self-contained text](nodes/33-condition-is-self-contained.md) — exempted the bar from the copy rule, decided alone; without it every condition would have to inline the whole bar and three of four audited fail on that clause.
- [x] 33.3 ASSUMPTION · [An acceptance condition is self-contained text](nodes/33-condition-is-self-contained.md) — extended node 28's manager raise to a malformed acceptance condition, so the manager may raise before spending a check it knows will only raise.
- [x] 33.4 ASSUMPTION · [An acceptance condition is self-contained text](nodes/33-condition-is-self-contained.md) — filed by the manager: the handover asks for one flag line where a flag lands in two places under two caps, so the manager authored all four index lines here.
- [x] 36.1 ASSUMPTION · [The clause that says no resolved node changes cannot be self-contained](nodes/36-resolved-node-clause-cannot-be-self-contained.md) — decided the fork alone rather than raising it, the second branch needing a checking party that does not exist and the condition itself saying to raise rather than invent one.
- [x] 36.2 ASSUMPTION · [The clause that says no resolved node changes cannot be self-contained](nodes/36-resolved-node-clause-cannot-be-self-contained.md) — added a carve-out no node asked for, permitting a demand about what changed in the tree, to stop the new prohibition catching file-scoped clauses.
- [x] 31.1 ASSUMPTION · [What the checker contract owes to having been run](nodes/31-checker-contract-owes.md) — split the two improvised riders rather than merging them, and treated neither as a fourth return shape, so the reserved raise never fired.
- [x] 31.2 ASSUMPTION · [What the checker contract owes to having been run](nodes/31-checker-contract-owes.md) — filed by the manager about itself: the check ran under the contract the work had just rewritten, and the manager proceeded rather than raising the circularity.
- [x] 35.1 ASSUMPTION · [A worker's handover carries no acceptance condition for the node it mints](nodes/35-handover-mints-no-condition.md) — left graph-conventions.md unedited because its flags.md clause and its silence on conditions agree with the answer rather than standing against it, so condition 6's allowance went unused.
- [x] 35.2 ASSUMPTION · [A worker's handover carries no acceptance condition for the node it mints](nodes/35-handover-mints-no-condition.md) — wrote the route for a worker that cannot state what done means: write what you can, say what is missing, the manager takes it to the human; no resolved node covering it.
- [x] 35.3 ASSUMPTION · [A worker's handover carries no acceptance condition for the node it mints](nodes/35-handover-mints-no-condition.md) — wrote the two new sections byte-identical in all five contracts, accepting a five-way edit and one restatement, to buy exact agreement across the five.
- [x] 35.4 ASSUMPTION · [A worker's handover carries no acceptance condition for the node it mints](nodes/35-handover-mints-no-condition.md) — phrased the no-round flag exception over the node — no exchange with the human, no gate — rather than naming research and AFK precondition, checked against all five kinds.
