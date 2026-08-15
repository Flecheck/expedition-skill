# Write the worker contract skills

Type: implementation
Status: resolved
Blocked by: 12, 20, 23

## Question

Write the six worker contracts as skills: one per node type, plus the checker.

Graduated from the map's fog by [Subagent context contract](12-subagent-context-contract.md), which
fixed what a contract contains — the spawn's shape, the pointer set and its per-type delta, the
handover's five parts and its three variants, and the scribe rule the manager holds up on its side.
This node writes those decisions down as instructions a worker actually receives.

Each contract is invoked by name from the spawn, rather than copied into it, so each must be
independently invocable — a supporting file under another skill cannot be. The glossary travels inside
these files, because the vocabulary is the workflow's and has to reach a machine that has never seen
this repo.

~~Blocked on [Human review of landed code](20-human-code-review.md) for one row of one contract: the
implementation worker's handover carries the gate payload, and that node owns its shape.~~

## Annotation: unblocked, and two of the six contracts changed

Added by [Human review of landed code](20-human-code-review.md). ~~**Both blockers are now resolved, so
this node is on the frontier** — the map's second implementation node, and the first one written after
the gate it will pass through was specified.~~ **A third blocker arrived within the hour:** [When an AFK
worker cannot proceed](23-worker-cannot-proceed.md), from the human's steering. Two of the six contracts
cannot be written until it resolves, because condition 2 requires every return variant a worker may use
and condition 3 forbids a rule no node decided — and that node may give both the implementer and the
checker a variant they do not have today.

The acceptance condition is **not** touched: it was written by [Subagent context
contract](12-subagent-context-contract.md) and only the spawning node writes one. What that node fixed
generically, this one now fixes concretely:

- **The implementation contract's gate payload has a shape.** Condition 2's *"shape of every return
  variant"* now has a referent for this row: a chronology of the checker assembled from others' text, the
  worker's flags, the node, the paths actually touched, the proposed commit message with its trailer, and
  a pointer to the tree — never a rendered diff. Plus the correction-round rule the worker has to obey:
  it reports whether its correction touched something a condition names, because that is what decides
  whether the acceptance condition is re-checked.
- **The checker contract says `FAIL`, not `REJECT`.** The word `reject` now belongs to the human at the
  gate. Condition 5 binds on the glossary, which now refuses `reject` for the agent by name — so a
  contract written with the old token fails that condition rather than merely reading oddly.
- **The gate is raised even when the checker will not pass**, so the implementation contract cannot treat
  a passing check as a precondition of finishing.

## Annotation: the third blocker resolved, and both affected contracts have their answers

Added by [When an AFK worker cannot proceed](23-worker-cannot-proceed.md). **All three blockers are resolved
and this node is on the frontier** — the map's second implementation node. The `Blocked by:` line keeps all
three, because unblockedness is computed rather than recorded.

- **The implementation contract gains a `raise` as a return variant** (condition 2), with the threshold
  stated as three triggers a worker can test on itself, and the rule that a raise **blocks while keeping the
  code slot** rather than parking.
- **The checker contract gains a third outcome, not a third value.** `PASS`, `FAIL`, or a raise that issues
  no verdict at all. Its characteristic case is an acceptance condition that is incoherent or unmeasurable,
  since it is the only party that reads one cold.
- **Both must say what happens on a stop.** The worker writes nothing and is dropped; the manager saves the
  salvage and cleans the tree. Condition 8 is untouched — a worker still writes no graph file, and the
  salvage is the manager's to write.
- **One rule to trace for condition 3**: `AFK` now means *does not need the human in order to proceed*.
  That is [Node type taxonomy](07-node-type-taxonomy.md)'s clause as corrected there, not a new rule
  invented in a contract.

## Acceptance condition

1. Six contracts exist and each is independently invocable by name from a spawn prompt: one per node
   type — grilling, research, prototype, implementation, precondition — plus the checker.
2. Each contract states, for its own type: the worker's identity and that it has no channel to the
   human; its hard rules; the shape of every return variant it may use; and the method skills it
   invokes, named as *invoke if present*.
3. Every rule in every contract traces to a resolved node. No contract introduces a rule that no node
   decided.
4. Instructions only — no reasoning, no rejected alternatives, no history. The same bar [Write the
   graph conventions document](21-conventions-document.md) was held to.
5. The vocabulary is the glossary's, and no `_Avoid_` word appears in any of the six.
6. The grilling contract is diffable against the relay prototype's [run-1
   contract](../prototypes/08-relay-protocol/run-1.md): everything that contract carried is either
   present or deliberately absent, and `CONTEXT-PROOF` is absent.
7. The checker's contract names neither the node file nor any part of it except the acceptance
   condition, which reaches the checker as extracted text.
8. A worker following any of the six writes no graph file.
9. Each contract's text stands alone as a file: everything binding on the worker is *in* the file, so a
   runner with no skill-invocation mechanism gets the same instructions by reading it. The skill is the
   wrapper, never the content. Added after the contracts were specified, because the human intends to
   run workers on other models and harnesses later and this is the whole cost of keeping that open.

## Answer

**Six contracts at `.claude/skills/expedition-<type>/SKILL.md`, one `SKILL.md` each, landed as commit
`e72f444` — 907 lines.** One per node kind, plus the checker.

Every one carries the same six things: who the worker is and that it never addresses the human; the subset
of the glossary its own text uses; what to read, with `flags.md` withheld and the map's optional ground
rules and source standing named; its hard rules; its method discipline, restated in full so the file stands
without the skills it names; and the shape of every return variant it may use.

| kind | what it may hand back | method skills |
| --- | --- | --- |
| grilling | question, handover, park | `/grilling`, `/domain-modeling` |
| research | handover | `/research` |
| prototype | question, handover, park | `/prototype` |
| implementation | raise, or handover with a sixth part | `/coding-principles`, `/naming` |
| precondition | question, handover, park, raise | none |
| checker | `PASS`, `FAIL`, raise — plus questions alongside either outcome | **discovered, never named** |

### What this node settled that no node had

- **The raise's scope by kind.** [When an AFK worker cannot proceed](23-worker-cannot-proceed.md) wrote it
  for the implementer and the checker; [Subagent context contract](12-subagent-context-contract.md)'s
  annotation generalised it to *"AFK workers"*. Settled at the gate: `precondition` has it too, and
  **`research` alone is flag-only**, on the glossary's *"never involves the human"*.
- **The gate payload splits along the scribe rule**, which neither node that owns half of it had written
  down. The worker supplies its own account of what it changed per checker finding, the paths it touched,
  and a proposed commit message; the manager lays that against the checker's own words and points at the
  working tree.
- **The checker's row, which node 12 left empty in every column.** It discovers the standards it holds work
  against rather than being handed them, preferring the repo's own to the machine's; its blindness outranks
  any method skill's procedure; a reviewing skill is for code standards and never for intent; a skill's
  question rides back alongside the outcome and costs no verdict; and it re-checks only what a change
  reaches, finding undisclosed changes by modification time rather than by re-reading.
- **`CONDITION-WRONG` is the manager's to file**, not the worker's, following node 23's change of its
  origin. The worker's own markers are `ASSUMPTION` and `DELEGATED`.
- **Flag ids, `NN.k`**, and a flag marked `settled` on the node as well as in `flags.md`. Both are the
  human's instruction at this gate, and both are deltas the shipped conventions document now owes.

### What it found, which is worth more than the files

- **An acceptance condition can contain a clause its own checker structurally cannot check.** Condition 3 —
  *every rule traces to a resolved node* — was declared unestablishable by **four** independent blind
  checkers, each reaching it alone. The condition is not wrong; it is addressed to the wrong party. Nothing
  today makes a spawning node ask whether the party that will read its condition can.
- **A condition can also unblind its own checker**, by naming a path inside the effort. Conditions 5 and 6
  do.
- **Workers finish the contracts they run under.** Three rules in the shipped files came from a checker's
  unprompted judgement mid-run rather than from a node: blindness outranking a skill's procedure, leaving a
  spec axis unrun, and distrusting the manager's statement of what changed. A map cannot reason its way to
  those.
- **A stop is more destructive than a death.** The harness refuses to resume an agent a user stopped —
  *"treat its work as cancelled"* — while [Relay protocol](08-relay-protocol.md)'s whole recovery story is
  respawn-and-replay after a death. A mis-click costs a whole check.
- **A contract edited mid-session does not reach a worker spawned afterwards.** The harness serves the body
  it loaded. Every spawn since names the contract's path and says the file on disk wins.
- **A cheaper model does not do less work; it does the same work at a lower rate.** Six checker attempts:
  100.3k, 101.3k, 81.8k worker tokens on Opus, 87.6k and 60.9k on Sonnet. The one real saving came from a
  *rule* — the modification-time re-check — not from a model: 87.6k to 60.9k while checking more.

## Flags

Eleven, all settled. Each carries an id of the form `NN.k` — this node's number, then a sequence within it, allocated in
write order and never reused. When each was raised, and what the human said about it, is in `## Review`
below, under the round that raised it.

~~**State is not here**: a flag's checkbox lives in [flags.md](../flags.md) and nowhere else.~~ **Overruled
by the human at the gate:** a flag they have confirmed is marked **settled** here as well, so someone
reading the node can see which judgements are still live without opening a second file. This is a real
duplication — [Graph file format](13-graph-file-format.md) put the checkbox in one place precisely so the
two could never disagree — and it is the seventh delta the shipped conventions document owes. The word is
`settled` rather than `resolved` because the glossary gives `resolve` to a node and leaves `settle` for a
flag.

`22.1` **· settled** `ASSUMPTION` — six sibling skill directories at `.claude/skills/expedition-<type>/SKILL.md`, one
`SKILL.md` in each. This is the layout call [Subagent context contract](12-subagent-context-contract.md)
left to this node, and it inherits [Write the graph conventions document](21-conventions-document.md)'s
install-location assumption whole.

`22.2` **· settled** `ASSUMPTION` — ~~the raise is given to the implementer and the checker only; research and
precondition keep the flag alone, against node 12's annotation reading *"AFK workers"* without
qualification.~~ **Amended at the gate:** `precondition` has the raise too, on the human's instruction, so
`research` is the only kind left with the flag alone. What is still assumed is the ground for that
exception — [`CONTEXT.md`](../../../CONTEXT.md)'s *"never involves the human"* — rather than [When an AFK
worker cannot proceed](23-worker-cannot-proceed.md) having stated the scope.

`22.3` **· settled** `ASSUMPTION` — the code reaches the checker as the changed paths in the working tree rather than as
rendered text, applying the gate's pointer-not-render rule to a party [Human review of landed
code](20-human-code-review.md) did not discuss.

`22.4` **· settled** `ASSUMPTION` — ~~a checker's raise carries no address and the manager supplies one, which no node
states.~~ **Answered at the gate:** the checker is given the node's **name**, for addressing a raise and
nothing else. What is assumed is the reading of acceptance condition 7 that lets it — that a name is not
*part of* the node file — which the human gave rather than the condition stating.

`22.5` **· settled** `ASSUMPTION` — each contract carries the subset of the glossary its own text uses, six to eleven
terms, rather than all fifty. Acceptance condition 9 forces the duplication; the cost is that a term which
drifts is a correction in up to seven places.

`22.6` **· settled** `ASSUMPTION` — written by the manager rather than by a worker under a contract, so none of the six
has been run by the agent it is written for. The same gap every node since [Dogfood
target](09-dogfood-target.md) carries, and the last node on which it is structural rather than incidental.

`22.7` **· settled** `ASSUMPTION` — the checker's contract uses the word **code-review**, which the glossary refuses for
the agent. It stands as the name of a thing a repo may carry, not as a name for checking, which is a
reading of acceptance condition 5 rather than compliance with it.

`22.8` **· settled** `ASSUMPTION` — the checker's blindness is given precedence over a method skill's own procedure, a
priority rule no node states. Written from what the checker did unprompted when a plugin skill's origin
axis would have unblinded it.

`22.9` **· settled** `ASSUMPTION` — the checker **finds** the standards it holds work against rather than being handed
them, which loosens the property that it checks against something stated. Bounded two ways: the repo's own
standards outrank the machine's, and a finding touching neither the acceptance condition nor the bar is not
its to hand back.

`22.10` **· settled** `ASSUMPTION` — a question a method skill wants to put to the human is **non-blocking by default**,
carried alongside the outcome rather than waited on. The human said such a question should be able to reach
them and did not say whether the check stops for it; the blocking form exists as the raise.

`22.11` **· settled** `ASSUMPTION` — a re-checking checker is told to distrust the manager's statement of
what changed, and to check anything the work shows that the statement does not mention. No node decided it;
it strengthens the human's own re-check rule against the failure mode attempt 4 demonstrated, at the cost of
some of the cheapness that rule exists for. Settled on the ground that finding those changes is a
modification-time comparison rather than a re-read, which round 9 writes into the rule.

**This entry was added late**, and its lateness is the human's own finding arriving a second time: it was
raised in round 8, after this section had been gathered, so for two rounds it lived only in the round that
created it. A flag section assembled once does not stay assembled. Whatever writes the manager's skill has
to make gathering a step of raising a flag rather than a tidy-up.

## Review

**The six contracts are written and the node stays `claimed`.** The checker has not run: spawning another
agent was not authorised in this session, and a self-check dressed as an independent one is the thing
[Node type taxonomy](07-node-type-taxonomy.md) refuses. The work stands at the gate, holding the code
slot, exactly as [Write the graph conventions document](21-conventions-document.md) stood.

Six sibling directories, each with one `SKILL.md`:

```
.claude/skills/expedition-grilling/SKILL.md         148 lines
.claude/skills/expedition-research/SKILL.md          79
.claude/skills/expedition-prototype/SKILL.md        152
.claude/skills/expedition-implementation/SKILL.md   189
.claude/skills/expedition-precondition/SKILL.md     146
.claude/skills/expedition-checker/SKILL.md          106
```

| Condition | State |
| --- | --- |
| 1 — six contracts, each independently invocable by name | **Checked, and observed rather than inferred.** Each carries a `name:` field matching its directory. The harness registered `expedition-grilling`, `expedition-prototype` and `expedition-research` as available skills mid-session, before the other three were written. |
| 2 — identity and no channel to the human; hard rules; the shape of every return variant; method skills as *invoke if present* | **Checked.** Every file opens on identity and the no-direct-channel rule, and carries a numbered hard-rules list. Return variants: grilling, prototype and precondition three each (question, handover, park); research one; implementation two (handover with a sixth part, raise); the checker three outcomes and no handover. Four name their method skills *if they are present* and restate the discipline for a machine holding none of them; precondition and the checker say in as many words that they have none. |
| 3 — every rule traces to a resolved node | **Checked by hand, per rule.** The trace is below. |
| 4 — instructions only | **Checked.** Greps for `because`, `the reason`, `rejected`, `in order to`, `trade-off` and `justif` return two hits, both the noun *reasoning* in the checker's contract naming the record it must not read. |
| 5 — the glossary's vocabulary, no `_Avoid_` word | **Checked against all fifty entries.** One knowing use: *"Do not trust any summary of them"*, which is [Subagent context contract](12-subagent-context-contract.md)'s own spawn wording, and a different sense from the closing report's refused synonym. `issue` appeared once as a verb and was removed. `reject` appears twice: once as the gate's outcome, once where the checker is forbidden the word. |
| 6 — the grilling contract diffable against the [run-1 contract](../prototypes/08-relay-protocol/run-1.md), `CONTEXT-PROOF` absent | **Checked line by line.** Table below. `CONTEXT-PROOF` is absent, and one other clause is deliberately absent. |
| 7 — the checker's contract names neither the node file nor any part of it except the acceptance condition, as extracted text | **Checked.** Greps for `node`, `map.md`, `decisions.md`, `flags.md`, every field name and every section heading return nothing in that file. The word *question* survives once, as the relay's `ASK` field. The condition arrives as *"the words themselves, not somewhere to go and read them."* |
| 8 — a worker following any of the six writes no graph file | **Checked.** Stated in the hard rules of all six and in the `worker` glossary line of five. |
| 9 — each file stands alone | **Checked.** No file points at another, at `CONTEXT.md`, or at `graph-conventions.md` for anything binding. Each carries the subset of the glossary its own text uses — six to eleven terms. |

**What only the checker can do**: conditions 3 and 6 rest on a reading of six resolved nodes against 820
lines, which is judgement rather than grep, and both are the kind of thing the writer of a document is
worst placed to check on itself. Condition 5 rests on the writer's own grep list being complete.

### Where each rule comes from

- **The spawn's shape, the three graph pointers, `flags.md` withheld, source standing in the map's
  `## Notes`, the glossary shipping inside the contract, the five-part handover with explicit `none`, the
  per-type method skills, paths as orientation, the path list reported rather than inferred** — [Subagent
  context contract](12-subagent-context-contract.md).
- **The question and answer shapes, `ABOUT` and `SO FAR`, verbatim words, `DIVERGENCE`, capped manager
  notes, the four redirects, per-question versus whole-node delegation, park, replay of a dead attempt's
  record as settled fact** — [Relay protocol](08-relay-protocol.md).
- **The five kinds and what each produces, prototype artifacts outside the product tree, the acceptance
  condition written by the spawning node and not rewritable, `ASSUMPTION` for a small ambiguity, the
  checker as a second independent agent checking against something stated** — [Node type
  taxonomy](07-node-type-taxonomy.md).
- **The bar as properties with commands discovered per repo, and a repo with no toolchain meeting a
  complete bar** — [Done-ness and termination](10-done-ness.md), with this repo's own discovery recorded in
  the map's `## Notes`.
- **One path-limited commit made by the manager after approval; no branch, no push, no history rewrite;
  the worker resumable through correction rounds** — [Git and code-landing policy](11-git-and-code-landing.md).
- **The lifecycle after the code is written, `PASS` / `FAIL` naming which of the two failed, the manager
  starting the checker, the implementer fixing every finding before the gate, uncapped rounds, the
  human's words as an instruction, reporting whether a correction touched something a condition names, the
  gate payload's contents, never rendering a diff, a flag disagreed with becoming a correction round** —
  [Human review of landed code](20-human-code-review.md).
- **The three triggers and the flag route below them, the raise blocking while keeping the code slot,
  discarding nothing on the way in, the two answer shapes, the human rewriting a condition the worker may
  not, `CONDITION-WRONG` filed by the manager after a raise, a stopped worker doing nothing further, the
  checker's third outcome and its characteristic case, `AFK` as *needs no live answer*, the worker never
  minting the node that replaces its own** — [When an AFK worker cannot proceed](23-worker-cannot-proceed.md).
- **Field and section names, statuses, the flag markers, the four files** — [Graph file
  format](13-graph-file-format.md) as shipped in
  [`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md).
- **Every term in every `Words used exactly` block** — [`CONTEXT.md`](../../../CONTEXT.md), condensed and
  never restated with a different meaning.

Three rules are thinner than the rest and are flagged below: the raise's availability per kind, the form
the code reaches the checker in, and who addresses a checker's raise.

### Condition 6: the grilling contract against the run-1 contract

| the run-1 contract carried | where it is now |
| --- | --- |
| identity, not the manager, no channel to the human | present, as **worker** |
| the node's name and its question, inlined | present as the first pointer — the node's own file, `## Question` first |
| context to read, *"do not trust any summary of them"* | present, and now the fixed set of three |
| grill to a decision under `/grilling`: one question at a time, always recommend, look facts up | present under *How you grill*, restated so it stands without the skill |
| hard rule 1 — never answer your own question | present, rule 1, with the delegation redirect named so the two cannot be read as contradicting |
| hard rule 2 — no human-facing tool; end the turn; the question is the whole output | present, rule 2 |
| hard rule 3 — strictly read-only | present, rule 3, widened from *no file in the graph* to *no file at all* |
| hard rule 4 — the final output is a machine-consumed value | present, rule 5 |
| the pausing shape: `QUESTION FOR` / `ASK` / `RECOMMENDED` / `ALTERNATIVES` | present and grown by `NODE`, `ABOUT`, `SO FAR` |
| *"you will then be resumed with the human's answer, with your context intact"* | present, with the downward shape stated |
| the finishing shape: `ANSWER FOR` / `DECISION` | present as `HANDOVER` / `ANSWER` |
| `NEW-NODES`, with an explicit `none` | present as part 4; the explicit `none` now binds all five parts |
| `CONTEXT-PROOF` | **absent**, as this condition requires |
| *"ask at most two questions in total"* | **deliberately absent.** Instrumentation for one prototype attempt; nothing in [Relay protocol](08-relay-protocol.md) caps an exchange, and the manager's own cap is three attempts per node. |

Added beyond that contract: the index line, flags with their markers, invalidations, the park variant, the
four redirects, source standing, and the replacement-attempt rule.

### What writing the six found

- **The shipped conventions document owes a fifth delta.** It says *"Its worker may raise a
  `CONDITION-WRONG` flag against it and may not rewrite it"* and *"`CONDITION-WRONG` — the worker judged
  its acceptance condition wrong."* Both are now stale: under [When an AFK worker cannot
  proceed](23-worker-cannot-proceed.md) a wrong condition trips trigger 1, so the worker raises and the
  **manager** files that flag once the human says ship anyway. Recorded in the map's `## Notes` with the
  other four.
- **The raise belongs to the implementer and the checker, and to nothing else.** [Subagent context
  contract](12-subagent-context-contract.md)'s annotation generalises it to *"AFK workers"*, which would
  reach `research` and an AFK `precondition` too. `CONTEXT.md` settles it against that reading for
  research — *"Never involves the human"* — and [When an AFK worker cannot
  proceed](23-worker-cannot-proceed.md) names both kinds only to say their flags wait for the closing
  report. So the literal reading is the coherent one, and the generalisation was wrong. Flagged.
- **The gate payload splits cleanly along the scribe rule, and the split had not been written down.** The
  worker supplies its own account of what it changed for each checker finding, the paths it touched, and a
  proposed commit message; the manager lays that end to end with the checker's own words and points at the
  working tree. Neither node's text divides the payload that way, and both are satisfied by it.
- **A checker's raise cannot carry an address.** [Relay protocol](08-relay-protocol.md) makes the node
  name the human's only address for a thread, and condition 7 forbids this contract from naming it. The
  manager supplies it, which it can: it knows what it spawned. Flagged.
- **Condition 9 makes the glossary a duplicated file rather than a shared one.** Each contract carries only
  the terms it uses, six to eleven of the fifty. A term that drifts is now a correction in up to six
  places.
- **`.claude/skills/expedition/` carries no `SKILL.md`.** [Write the graph conventions
  document](21-conventions-document.md) shipped two files there and no entry point, so `graph-conventions.md`
  is a file the manager reads rather than a skill anything invokes. The six contracts are the first
  invocable thing the workflow ships. Nothing is broken by it; the manager's own skill is where an entry
  point would go.

### Judgement calls, to be filed as flags on resolution

~~Held here rather than in [flags.md](../flags.md) until the work is final, so no line has to be struck
through if the gate changes it.~~ **Moved to `## Flags` above**, which is where the format has always put
them, on the human's finding at the gate: *"right now the flags are spread out in the node, it is a bit
hard to find."* Holding them under `## Review` was this node's own call, and it is what scattered them —
each landed in whichever round found it. The list below is left where it is as the record of where they
were first written. **Each carries an id, `NN.k`,** added at the human's request at the gate — see below.

- `22.1` `ASSUMPTION` — six sibling skill directories at `.claude/skills/expedition-<type>/SKILL.md`,
  inheriting node 21's install-location assumption and the layout call node 12 left here.
- `22.2` `ASSUMPTION` — the raise is given to the implementer and the checker only; research and
  precondition keep the flag alone, against node 12's annotation reading *"AFK workers"* without
  qualification.
- `22.3` `ASSUMPTION` — the code reaches the checker as the changed paths in the working tree rather than
  as rendered text, applying the gate's pointer-not-render rule to a party that node did not discuss.
- `22.4` `ASSUMPTION` — a checker's raise carries no address and the manager supplies one, which no node
  states.
- `22.5` `ASSUMPTION` — each contract carries a subset of the glossary rather than all fifty terms, so the
  vocabulary now lives in seven places.
- `22.6` `ASSUMPTION` — written by the manager rather than by a worker under a contract, so none of the six
  has been run by the agent it is written for. The same gap every node since [Dogfood
  target](09-dogfood-target.md) carries, and the last node on which it is structural rather than
  incidental.
- `22.7` `ASSUMPTION` — the checker's contract names a **code-review** skill, using a word
  [`CONTEXT.md`](../../../CONTEXT.md) refuses for the agent. It stands as the name of a skill a repo may
  carry, not as a name for checking, which is a reading of acceptance condition 5 rather than a compliance
  with it. Added in correction round 2 at the human's instruction.

### The gate, round 1 — five flags settled, one question, one change

The manager raised the work with the checker's absence stated in the first line, per [Human review of
landed code](20-human-code-review.md)'s escape hatch, and the six judgement calls above as the flags.
The human's answer, verbatim:

> *"Maybe add ids to flag in the node, right now it is a bit hard to comment each one. six sibling
> directory is fine. 2nd one: ok, they are supposed to do the best they can, there will be a grilling
> after if they couldn't do eveything. 3rd: yes it reads what he neeeds 4th: I am not sure I undersand
> what is address here. 5th: ok 6th: ok. You can run the checker, both for feedback and to see if it
> works well"*

| flag | the human | state |
| --- | --- | --- |
| `22.1` | *"six sibling directory is fine"* | settled at the gate |
| `22.2` | *"ok, they are supposed to do the best they can, there will be a grilling after if they couldn't do eveything"* | settled, and it added a rule — see below |
| `22.3` | *"yes it reads what he neeeds"* | settled at the gate |
| `22.4` | *"I am not sure I undersand what is address here"* | **outstanding** — a question, not a settling. Answered in the conversation: `NODE:` is the first line of every relayed question and the human's only address for a thread, per [Relay protocol](08-relay-protocol.md)'s `F1`, and condition 7 forbids the checker's contract from naming it. |
| `22.5` | *"ok"* | settled at the gate |
| `22.6` | *"ok"* | settled at the gate |

**Five flags settled in one message, which is the first time this map has settled any.** [Human review of
landed code](20-human-code-review.md) predicted exactly this — the gate is the only place acting on a flag
is free, because the worker is still alive and still holding the code slot — and [Friction from running
this map by hand](24-self-hosted-friction.md)'s finding 5 measured the opposite as the standing state:
fifteen outstanding, zero settled. The prediction held on its first real trial.

**Flag ids are a format change, and the sixth delta on the shipped conventions document.** The human's
first sentence is a change to how flags are written rather than to this node's product: without an id a
flag can only be pointed at by its position in a list, which is what made this exchange awkward. The
scheme is `NN.k` — the node's own number, then a sequence within that node, allocated in the order the
flags are written and never reused. It costs no lookup, it sorts, and it stays stable under append-only.
Both places a flag lives need it: the node's `## Flags` entry and its [flags.md](../flags.md) line.
Applied to this node's six immediately; the twenty flags already in `flags.md` are un-id'd until someone
retro-fits them, which is mechanical, since that file is already in node order.

### Correction round 1 — what a worker could not do is part of its answer

The human's reasoning on `22.2`, verbatim: *"they are supposed to do the best they can, there will be a
grilling after if they couldn't do eveything."* This confirms the narrow reading — research and
precondition get the flag and no raise — and adds the rule that makes the narrow reading survivable: a
worker's shortfall has to be visible, or nothing downstream knows a grilling node is wanted.

The research contract already carried it as a hard rule: *"A fact you could not establish is a result.
Report it as one, and never fill the space with a plausible answer."* The precondition contract did not,
and now does, in its handover:

> Do the best you can with what you have. Where something could not be done at all, `ANSWER` says what and
> how far you got, and leaves the shortfall visible rather than tidy.

One line, in the file the human's answer was about. No flag: a correction at the gate is the human's
instruction, and flags record the worker's judgement.

### The checker was authorised, and its own contract is what it runs under

*"You can run the checker, both for feedback and to see if it works well."* Two purposes in one agent: the
verdict on nine conditions, and the first live use of `/expedition-checker` by the party it was written
for. Spawned blind, per [Subagent context contract](12-subagent-context-contract.md) — the acceptance
condition as extracted text, the bar as discovered for this repo, and the six changed paths.

**Its spawn found something about acceptance conditions in general.** Two of the nine conditions name a
file the checker must read to check them at all: condition 5 names the glossary, and condition 6 names a
prototype asset **inside the effort's own directory**. So a condition can unblind its own checker by
citing the graph, and blindness is a property of the condition's wording rather than of the contract that
keeps it. Nothing to fix here — the checker follows the condition it is given — but the next node that
writes an acceptance condition should know that a path in one is a hole in the blindfold.

### Attempt 1 died on the clock rather than on the work

It stopped on a session limit — an account wall with a stated reset time — partway through, having reached
the point it named in its last words: *"Now the bolded-term inventory against the glossary, plus conditions
7 and 9."* **No outcome was handed back, so under its own contract there is nothing to read.** `PASS`,
`FAIL` and a raise are the three things it may hand back; a death is none of them, and its absence is not
a pass.

**This is the second checker this map has lost, and both died the same way.** [Write the graph conventions
document](21-conventions-document.md)'s died on a session limit after one of four phases. The checker is
the only kind of worker this map has ever lost, neither loss was caused by the work, and both times the
condition left unchecked was one only the checker can check.

**It also draws a distinction [Relay protocol](08-relay-protocol.md) did not.** That node's two-respawn cap
rests on the reasoning that *"replay re-inflates exactly the context that killed the previous attempt"*,
which is true of context exhaustion and false of an account limit. A session-limit death re-inflates
nothing, so it should not spend an attempt against a cap whose premise is context. Recorded rather than
decided — the cap belongs to that node.

### Correction round 2 — the raise reaches precondition, and the checker gains a method skill

The human's words, verbatim:

> *"I guess precondition could raise, as it is more reseach that is supposed to be fully autonomous. 4. I
> guess we could give the node to the checker, it is not the one who did the implementation so there
> should 4. ok, we might want to add to the checker to see if the repo as a review skill and to use it ?"*

Three things: two acted on, one put back to them.

- **`precondition` gains the raise.** This amends flag `22.2`'s settlement rather than reversing it — the
  narrow reading holds for `research`, and the human has named that kind as the one meant to need nobody at
  all. The contract now carries the three triggers, the two answer shapes, and the rule that a raise reuses
  the question shape rather than adding a fourth thing to hand back. A precondition's raise holds no code
  slot and has no salvage, since it writes no product code. Annotated on [When an AFK worker cannot
  proceed](23-worker-cannot-proceed.md), which owns the mechanism.
- **The checker gains its first method skill.** Where the repo or the harness carries a code-review skill
  of its own, the checker invokes it and holds what it finds against **the bar**, whose own wording is
  *whatever else the repo itself demands*. A finding touching neither the condition nor the bar is not the
  checker's to hand back. This is the first entry in [Subagent context
  contract](12-subagent-context-contract.md)'s method-skill column for the checker, which that node left
  empty, and it carries flag `22.7` for the word it spends.
- **The middle sentence is put back to them.** It reads *"we could give the node to the checker"* and stops
  mid-clause. `node` there could mean the node's **name** — which is all flag `22.4` is about, and which
  costs nothing — or the node's **file**, which reverses the blindness the human chose themselves at
  [Subagent context contract](12-subagent-context-contract.md) (*"Blind — condition, bar, diff"*, taken as
  offered) and rewrites acceptance condition 7. Those differ by far more than a line, so nothing was
  assumed.

### Correction round 3 — the checker gets a name, and nothing else

Put back as three options; the human took the first, as offered: **the node's name only.** Flag `22.4`
moves from outstanding to **settled at the gate**, which makes six of the seven settled before the work
has landed.

- **The contract gains a fourth thing it is given**, and one sentence keeping it a name rather than an
  address to read: *"The name of the work, for one purpose: addressing a raise. It is a name, not
  somewhere to go and read."*
- **Its raise gains `NODE:` back**, so a checker's raise is now shaped identically to every other relayed
  question rather than being the one payload the manager has to complete. The manager only carries it.
- **Acceptance condition 7 stands as written and was not rewritten**, on the human's reading that a name is
  not *part of* the node file. The contract still names no file, no section, and no path into the graph:
  what it can do with the name is stated in the same sentence that grants it.
- **Blindness survives intact**, which is what the other two options cost. It is the property [Human review
  of landed code](20-human-code-review.md) leans on when it takes the checker's spawn away from the
  implementer, and the one [Write the graph conventions document](21-conventions-document.md)'s four-phase
  protocol was built out of.

**Attempt 2 spawned** against the final six files, carrying the name and the note that its predecessor
handed nothing back to inherit.

### `22.7` settled, and a fourth round queued behind the running check

The human on `22.7`: *"22.7 seems good"* — **settled at the gate**, which makes all seven settled before
the work has landed. Their instruction in the same message, verbatim:

> *"in my global context, I have stuff about coding principles that the checker should check, I don't know
> if there is something for it right now. Using them if there is no code-review skill. (don't take my
> principle in put them in the checker but add something about using them). What do you think about it ?"*

**Held rather than applied, because a checker is running on these files.** Editing the work under a live
check would leave its outcome standing against a file that no longer exists. This lands as correction round
4 alongside whatever attempt 2 hands back, and the pair is re-checked once rather than twice.

What it will say when it lands, and one place it departs from their words:

- **The standing principles are already part of the bar, not a new thing.** [Done-ness and
  termination](10-done-ness.md) put *"whatever the repo itself demands"* in the bar and had its contents
  discovered per repo and recorded in the map's `## Notes` — which for this repo already reads *"the project
  criteria (the human's global coding principles and `/naming`)"*. So the hole is not in what the bar
  contains; it is that nothing points the checker at it.
- **Two halves, and only one of them is this node's.** The contract gains an *invoke if present* line for
  the discipline an install carries, exactly as the code-review skill got. The other half is the **manager's
  spawn**, which must hand over the bar's non-command half as the map records it rather than as a phrase —
  the improvised spawn for attempt 2 said *"the repo's own coding principles and naming discipline"* and
  pointed at nothing. That belongs to the manager's own skill, which is still in the fog.
- **Not a fallback, against their literal words.** They wrote *"using them if there is no code-review
  skill"*; the recommendation is to use whichever are present, both where both are. A code-review skill is a
  procedure for looking and a principles skill is the standard being held to, so one does not substitute for
  the other. One sentence to overturn.
- **The limit to hold.** A checker that goes looking for its own standard stops checking against something
  stated, which is the whole of what separates it from a second opinion. Naming a discipline to invoke keeps
  it stated; *read the repo and form a view* would not, and is not what lands.
- **It raises no new flag.** Method skills being per-install rather than per-repo is the `ASSUMPTION`
  [Subagent context contract](12-subagent-context-contract.md) already carries, and this line inherits it.
  On this machine all three exist — `coding-principles` and `naming` as the human's own, `code-review` as a
  plugin — and none of them is per-repo.

### The checker ran, and it failed the work on one line

**Attempt 2, outcome `FAIL: the bar`, one entry.** The checker's contract opened *"Three things, in the
spawn:"* over a list of **four** items — the fourth being the name added in correction round 3 an hour
earlier. It found it by reading the file, established it as the only count error in the six by checking
every other count word against its own list, and placed it on the bar's non-command half under the naming
discipline: *"the heading asserts a count its own list falsifies."* Fixed in round 4 below. **It breaches
none of the nine conditions**, which is the checker doing exactly the thing it was split from the human
for — the gate would have been spent on a typo.

**Eight conditions established, and one that cannot be.** Conditions 1, 2, 4, 5, 6, 7, 8 and 9 were each
established with the evidence named. Four things it did that no self-check could have:

- **Condition 1 was confirmed live by an independent party.** It found all six in the harness listing and
  invoked `expedition-checker` by name to get its body — invocability observed from outside rather than
  asserted from the frontmatter.
- **Condition 5's literal reading is unsatisfiable, and it reached that alone.** Its words: the glossary
  *"lists `correction`, `revision`, `reject` and `done` as `_Avoid_` words for one term while making them
  the names of others"*, so it read the clause as the negative half of *the vocabulary is the glossary's*.
  That is the same reading this node made while writing, arrived at blind. It then listed sixty-odd avoided
  synonyms verified absent, and every appearing word with the sense that licenses it.
- **Condition 6 has three deliberate absences, not one.** This node's own record named the two-question
  budget. The checker found two more — `RECOMMENDED`'s *max 2 sentences* cap and `ALTERNATIVES`' *1-3*
  cap — read all three as prototype instrumentation rather than protocol, and noted that *deliberately*
  absent is not observable and rests on judgement. All three are hereby recorded as deliberate: none is in
  [Relay protocol](08-relay-protocol.md)'s payload, and a cap on how much a worker may say to the human is
  the opposite of `SO FAR`'s *summarized if long*.
- **Condition 7 is met and the seam is exactly where it looks.** Its words: *"A node's name is a part of the
  node. What saves it under the condition as written is that the condition's own exception clause identifies
  extracted text as the acceptable mechanism, and item 4 uses precisely it."* It also noticed that reading
  *any part of it* strictly would delete item 4 — **which would have fixed the bar failure too**, since item
  4 is what makes the count wrong. The human settled that reading one round earlier.

**Condition 3 cannot be checked by a blind checker, and the checker did something better than its contract
allows.** Verifying that every rule traces to a resolved node requires the record it is barred from
reading. Under its contract that is trigger 1 — an unmeasurable condition — and a raise, which **issues no
outcome at all**. It instead handed back a legal `FAIL` on the bar, marked condition 3 *not established and
not establishable*, and listed the six rules it could not map to the glossary as a residual for the manager:
the `## Notes` ground rules and source standing, `flags.md is not yours`, `/coding-principles` and `/naming`
on the implementer, `/domain-modeling` on the griller, the checker's own method-skill section, and item 4.
Every one of those traces — to [Subagent context contract](12-subagent-context-contract.md)'s table and
pointer set, and to this node's own gate — which is the point: **it was right that it could not tell.**

That is a real hole in [When an AFK worker cannot proceed](23-worker-cannot-proceed.md)'s design, found by
running it: **a raise costs the whole verdict, so a checker holding one unmeasurable condition out of nine
must choose between losing eight established verdicts and issuing one with a silent gap.** It took a third
route that node does not name — a verdict plus a stated residual — and the third route is better than either
option it was given. Recorded here; the mechanism belongs to that node, and
[Off-contract subagent output](17-off-contract-output.md) is the open node that owns *a worker doing
something its contract does not name*.

**It protected its own blindness against a method skill, unprompted.** The plugin code-review skill it found
has an axis that sends workers after the origin of a change; running it would have walked straight into the
record. It left that axis unrun, said so, and ran the standards axis itself. Round 4 writes that back into
the contract as a rule.

**A runtime finding the design has to know about.** Its closing note: the body the harness served when it
invoked `expedition-checker` **differed from the file on disk** — no item 4, no `NODE:` line — with the
file's mtime six minutes before it read it, after skills were loaded for that attempt. **A contract edited
mid-session does not reach a worker spawned afterwards.** The whole design ships worker contracts as skills,
so a stale body in circulation is a correctness problem rather than an inconvenience, and it lands on
[Runtime that hosts the manager and its subagents](02-runtime-host.md) and the map's *whether the Claude
Code subagent runtime proves too simple* fog. The workaround costs one line in the spawn: name the
contract's path and say the file on disk wins.

### Correction round 4 — the count, the standards, and the blindfold

Three edits, all to the checker's contract.

1. **`Three things` → `Four things`.** The checker's finding, applied.
2. **Its method skills, which [Subagent context contract](12-subagent-context-contract.md) left empty.**
   `/code-review`, `/coding-principles` and `/naming`, *if they are present*, with what they find held
   against the bar. **This deviates from the human's words in one place** — they wrote *"using them if there
   is no code-review skill"*, and the line says to run whichever exist, since a code-review skill is a
   procedure for looking and the other two are the standard being held to. One sentence to overturn.
3. **Blindness outranks a method skill's procedure.** Where a skill wants the work's origin, that part goes
   unrun and the checker says it left it. The checker did this on its own judgement; now it is written down.

The human's constraint held: *"don't take my principle in put them in the checker but add something about
using them."* No principle is copied into the contract. What it carries is three names and a rule about what
to do with what they say.

**The acceptance condition must be re-checked, and this node reports why**, per [Human review of landed
code](20-human-code-review.md): edit 1 touches nothing a condition names, but edits 2 and 3 touch conditions
2, 3, 5 and 9. The bar re-runs either way.

- `22.8` `ASSUMPTION` — the checker's blindness is given precedence over a method skill's own procedure, a
  priority rule no node states.

  **What produced it, since a flag is worth nothing without this.** Attempt 2 found the plugin's code-review
  skill and declined to run it whole. Its own words: *"its Spec axis would have sent a subagent into the
  record I am barred from reading, so I did not run it, and ran its Standards axis myself against the repo's
  only standards document (`CONTEXT.md`) plus the `coding-principles` and `naming` skills."* Nothing told it
  to do that. Its contract told it to invoke the skill, and separately told it not to read the record; it
  worked out unprompted that one axis of that skill made the two instructions contradict, chose the one that
  protects the check, ran the rest of the skill anyway rather than dropping it, and **reported the choice
  instead of making it silently**. The flag exists because that choice now binds every checker after it, and
  it was made by a worker in the middle of a run rather than decided by a node.

### Correction round 5 — four decisions, and only three of them fit in a contract

The human's words, verbatim:

> *"When the checker find something, I belive it should not always be fixed by the implementer if the
> changes would be too big, it should be raised to the user to see what should be done. The code review
> skill could also want to ask the human. I feel that it should not name "/code-review"
> "/conding-principles" adn "/naming" directly but should ask the agent to find them, if there is a code
> review skill or similar, it should use it, prioritazing one on the project, otherwise verify the rules
> that are available. Also for the checker, if only part of the code was changed since last run, it should
> not rerun everything, maybe keeping the checker alive and saying what has changed ?"*

1. **A checker finding whose fix is a piece of work rather than a repair is a raise.** Written into the
   implementation contract, under trigger 1 — the size of the node is not the worker's to change — with the
   two things it must not do instead: start the large fix, or carry the finding past the gate on its own
   authority. **This qualifies a plain statement of the human's** at [Human review of landed
   code](20-human-code-review.md), *"the issues raised by the checker should be already fixed by the
   impementor"*, which that node already carries an `ASSUMPTION` against for a different reason. Second
   qualification of the same sentence, this one from its author.
2. **A method skill's wish to ask the human creates no channel.** The checker raises where the question
   meets the threshold and answers it itself otherwise, saying so in its outcome. Its one route out stays
   its raise.
3. **Skills are discovered, not named.** The three names went in one round ago and come out again: the
   contract now says to go and find a reviewing skill or anything doing that job, the stated coding
   principles and naming discipline wherever they are written, and any standards document the repo keeps —
   **the repo's own beating the machine's general one** where both exist. This is the map's own portability
   rule reaching a place it had not — *prefer properties that are discovered over commands that are
   declared* — and it is the first real answer to [Subagent context
   contract](12-subagent-context-contract.md)'s standing `ASSUMPTION` that method skills are per-install
   rather than per-repo. **It reopens that question for the other five contracts, and this node does not
   touch them**: their skill names are in that node's resolved table, and changing them is a revision of it
   rather than a correction here. Recorded for whoever takes it.
4. **The checker may be resumed rather than respawned**, which splits in two. The contract's half is
   written: handed the same work again with a statement of what changed, it re-runs the bar in full,
   re-checks the parts of the condition the change reaches plus anything it failed last time, and does not
   establish twice what it already established. **The manager's half is not this node's** — resuming a live
   checker instead of spawning a fresh one is the manager's act, and its skill is still in the fog. The
   worker's own duty to report what it touched, which is what feeds the statement, was already fixed by
   [Human review of landed code](20-human-code-review.md).

**Nothing here is a new accepted risk.** *"Do not establish it twice"* is that node's re-check rule stated
from the checker's side rather than the implementer's, and the residual — a fix that breaks something
already passed — is the one it already accepted.

- `22.9` `ASSUMPTION` — the checker now **finds** the standards it holds work against rather than being
  handed them, which loosens the property that it checks against something stated. Bounded two ways: the
  repo's own standards outrank the machine's, and a finding touching neither the acceptance condition nor
  the bar is not its to hand back.

  **What produced it.** The human's instruction in this round, replacing the three skill names written into
  the contract one round earlier: *"it should not name `/code-review` `/coding-principles` and `/naming`
  directly but should ask the agent to find them."* The looseness is the price of portability — a contract
  that names skills is wrong on a machine carrying none, and a contract that names none leaves the checker
  choosing what to be judged by. The two bounds above are what keeps that choice narrow.

### Correction round 6 — a skill's question reaches the human, and it costs no verdict

The human, overturning round 5's second item one message after it landed: *"A skill wanting to ask the
human should be able to do it"*.

Round 5 had the checker swallow such a question or spend a raise on it. Both are wrong for the same
reason, and it is the hole **the checker itself found** an hour earlier: **a raise issues no outcome at
all**, so routing a review skill's question through one throws away nine conditions' work to ask something
that was never blocking.

- **A `PASS` or a `FAIL` may now carry questions alongside it.** The checker hands each one back under
  `QUESTIONS:`, does not wait, and its outcome never depends on an answer. The manager carries them to the
  human with the rest of what it puts in front of them at the gate.
- **Nothing new was invented to do it.** [Human review of landed code](20-human-code-review.md) already
  makes the gate the place the human reads *"things to be looked at"* — the human's own phrase, about
  flags. A question from a skill the checker ran is that same kind of object arriving by a different
  route, and it lands where they are already looking.
- **The blocking case stays a raise**, and is named as the exception: where the skill cannot go on at all
  without an answer, the check genuinely stops, which is what a raise is for.
- **This routes around node 23's hole rather than fixing it.** A raise still costs the whole verdict. What
  changed is that fewer things now have to be one.
- **Two lines elsewhere in the file had to move with it**, both found by counting the file against itself
  the way attempt 2 did: the `human` entry said *only by a raise*, and hard rule 5 said the checker's work
  does not reach the human at all.

- `22.10` `ASSUMPTION` — a skill's question is **non-blocking by default**, carried with the outcome rather
  than waited on. The human said such a question should be able to reach them and did not say whether the
  check stops for it; the blocking form exists as the raise, and one sentence swaps the default.

### Attempt 3 — the acceptance condition is met, and the bar fails twice

**`FAIL: the bar`, two entries, and `Acceptance condition: met`.** Both entries are in the checker's own
contract and both are the class it caught last round: a statement the file makes about itself that its own
text contradicts.

1. **The opening foreclosed the route the file's own new mechanism opens.** *"A raise is your only route to
   them"* against three passages added in round 6 giving a second. Its words: *"A checker reading top-down
   concludes it must suppress `QUESTIONS`."* Round 6 edited three places and missed the fourth.
2. **`raise` was counted as an outcome and then declared not to be one.** *"Exactly one of the three
   outcomes"* against *"you hand back no outcome at all"* and hard rule 4. It settled which side is right
   from the glossary rather than by preference — `Checker`'s entry has `PASS` and `FAIL` as the outcomes and
   a raise issuing no verdict — and noted it had missed this last round, surfacing now **because the bar is
   re-run in full**. Which is the re-check rule the human decided one round earlier, paying for itself
   immediately.

Both fixed in round 7 below.

**The condition is met on everything a blind party can establish.** Conditions 1, 2, 4, 5, 7, 8 and 9
re-checked where the change reaches; 6 stands from attempt 2, the grilling contract being untouched. Two
readings it stated rather than assumed:

- **Condition 2's *"named as invoke if present"* fixes the modality, not the names.** The discovery section
  names no skill, and it read the clause as satisfied by the stated null case — the same way
  `expedition-precondition` satisfies it by saying it has none. That is the reading round 5 needed and did
  not get to state, arrived at independently.
- **Condition 5's `_Avoid_` words are concept-scoped, and it proved it rather than asserting it**: the
  glossary itself writes *"deferring"* under `Park` while listing *"defer"* under `Promote`. That is a
  better proof than the one this node wrote, and it settles the reading both checkers reached alone.

**Condition 3 is not observable from inside its blindness**, stated again and in sharper terms: *"The
clause itself is checkable only by whoever holds the record."* Two independent checkers, the same verdict,
which is now the strongest evidence on this map that **an acceptance condition can contain a clause its own
checker structurally cannot check.**

**It defended its blindness mechanically this time, not just procedurally.** It ran the plugin skill's
standards axis **in a worker barred from `.scratch/`**, and left the spec axis unrun for two reasons rather
than one: that axis walks into the record, and its setup step writes files, which hard rule 1 forbids. It
then listed five judgements that axis raised and dismissed each with a reason — including *"Five parts"*
over six fenced lines, read as `HANDOVER:` being the block's label and never a part anyone would write
`none` for. **That reading was taken and the ambiguity deliberately left alone**: an independent party
examined it and passed it with grounds, and re-opening it would have spread round 7 across five files and
cost the cheap re-check below.

### Correction round 7, and the first real resume

Two edits, both to the checker's contract, both wording. **They touch nothing any condition names**, so per
[Human review of landed code](20-human-code-review.md) only the bar is re-checked — which this node reports
rather than leaves to inference, as that node requires.

**The checker was resumed rather than respawned.** The human's decision from round 5, used for the first
time: attempt 3's own agent was handed a statement of what changed, told to re-run the bar in full and
re-check only what those two edits reach, and told that everything else it established stands. It was also
told which of its own judgements was taken and left unchanged, so an unfixed ambiguity does not read as a
miss. This is the same attempt, not attempt 4 — the checker keeps its number and its context, exactly as
[Relay protocol](08-relay-protocol.md)'s claim belongs to the node rather than to the agent instance.

**A question came back with the outcome, and the mechanism worked end to end on its first run.** Under
`QUESTIONS:`, from the plugin's code-review skill: it wants to be told where the originating specification
is so its spec axis can run, and the checker could neither answer it nor go looking, since the answer is the
record. Its own words: *"Whether that axis should be run at all, and by whom, is not mine to decide."*
Relayed to the human. The route the human opened one round earlier carried a real question on the very next
run, and it cost no verdict.

**The resume was stopped, by accident, before it handed anything back** — the human's own word for it. And
the accident produced a finding worth more than the run would have: **the harness refuses to resume an agent
a user stopped.** *"Was stopped by the user and won't be resumed. Treat its work as cancelled."* A second
attempt to continue it failed outright.

**That is a failure mode [Relay protocol](08-relay-protocol.md) does not have.** Its whole recovery story is
lazy detection then replay: a dead attempt is respawned with the record and carries on, and the human is
told once. A **stopped** attempt cannot be respawned into the same agent at all, the manager cannot read its
transcript, and no on-disk record of a checker's partial work exists — a checker writes no graph file and
hands nothing back until it has an outcome. So a stop is more destructive than a death, which is the reverse
of what that node's machinery assumes, and it means **a mis-click costs a whole check**. Recorded here; the
mechanism belongs to that node.

**Attempt 4 was spawned fresh, carrying what attempt 3 established rather than its context.** That is the
re-check rule working through a colder channel than the one the human designed it for: the statement of what
changed is the same, but *"everything else you already established stands"* now arrives as text from the
manager rather than as the agent's own memory. The independence of those carried parts rests on attempt 3's
work, not on attempt 4's, and this node says so rather than letting the distinction disappear into a `PASS`.

What no run has produced is the measurement the resume was supposed to give: whether a resumed check costs a
fraction of a fresh one. Still unknown, and it is what this node could have contributed to the map's
*whether the Claude Code subagent runtime proves too simple* fog.

### Round 8, queued behind attempt 4 — order, and what a reviewing skill is for

The human's words, verbatim:

> *"The code checker should first read the rules and skills and then read the code, as the skills might want
> to spawn a subagent for review. The skill for review should only be used to review the code standards, not
> the spec, (there is a small issue, with mattpocock code review skill, it is designed to review both the
> standards and the spec but the spec is not a matt pockock spec so it shouldn't run)"*

Held rather than applied, for the reason round 4 was held: a check is running on these files, and editing
under it leaves its outcome standing against a file that no longer exists. Two rules, both for the checker's
contract:

1. **Order is fixed: find the standards first, then read the work.** The reason is mechanical rather than
   tidy — a reviewing skill may run the reviewing in a **worker of its own**, and that worker is spawned
   rather than handed what the checker has already read. A checker that reads the code first has paid for
   reading it twice, in two contexts.
2. **A reviewing skill is for code standards and never for intent.** The acceptance condition is the only
   statement of what the work was meant to be. Where such a skill also checks work against a specification,
   a requirement document or an originating request, that part goes unrun — there is no document of that
   kind here, and what it would go looking for is the record.

**This makes a rule of what a worker did on its own.** Attempt 3 left the plugin's spec axis unrun,
unprompted, and gave two grounds for it. The human has now made the first ground general and named the
second concretely: that skill's spec axis wants a specification of a shape this workflow does not produce.
**Second time this session** that a worker's unprompted judgement has become a written rule — the first
became flag `22.8` — and it is what a dogfood is supposed to produce: the contracts are being finished by
the workers running under them.

**The existing limit is not replaced by this.** *"Run no part of one that would take you into the record"*
stands on blindness; the new rule stands on where intent lives, and it would bind even for a spec axis that
never touched the record.

### Attempt 4 — `PASS`, and it refused to take the manager's word for what changed

Both entries of attempt 3's `FAIL` cleared, the bar re-run in full and clean, no questions handed back. It
re-checked conditions 2, 4, 5, 7 and 9 on the edited file, let 1, 6 and 8 stand, and reported condition 3
**not establishable** — *"not as met and not as failed"* — which is the **third independent checker in a row
to say so.**

**The finding worth more than the verdict: a statement of change is the manager's word, not evidence.** The
spawn told it only the checker's contract had moved. It noticed `expedition-implementation/SKILL.md` had an
mtime it could not place against the earlier outcome, declined to *"rest the result on the statement of
change being exact"*, and applied the whole condition to that file too — where it held. That is the
re-check rule's one soft spot, found on its second use: **a checker that trusts the statement inherits the
manager's errors**, and the manager is the party least able to notice its own omission. Written into the
contract in round 8 below.

It also read *"Exactly one of the three below"* sitting above four `###` blocks and cleared it on the same
label-versus-part reading it had taken for *"Five parts"* — the count discipline that failed twice now
holding by a stated rule rather than by luck.

### Correction round 8 — order, scope, and one line the checker earned

Three edits, all to the checker's contract.

1. **Find the standards before you read the work.** A reviewing skill may run the reviewing in a worker of
   its own, and that worker is spawned rather than handed what the checker has read.
2. **A reviewing skill is for code standards and never for intent.** The acceptance condition is the only
   statement of what the work was meant to be; where such a skill also holds work against a requirements
   document, a product brief or an originating request, that part goes unrun. The word *specification* is
   deliberately not used — `spec` is an `_Avoid_` word, and both checkers swept for it.
3. **The statement of what changed is not evidence.** Where the work shows a change the statement does not
   mention, the checker checks it and says so. This is attempt 4's own behaviour written down, and it is
   the **third time this session** a worker's unprompted judgement has become a rule.

Edits 1 and 2 touch conditions 2, 4, 5 and 9; edit 3 touches 2 and 9. **The acceptance condition needs one
more check**, and this node reports that rather than leaving it to inference.

- `22.11` `ASSUMPTION` — a re-checking checker is told to distrust the manager's statement of change where
  the work contradicts it, which no node decided. It strengthens the human's own re-check rule from round 5
  against the failure mode attempt 4 demonstrated, and it costs the cheapness that rule was for.

  **Settled at the gate**, on a ground the human supplied and the rule did not carry: *"it seems good if he
  find what was changed?, since it is cheap (modification time)."* Their acceptance rests on the mechanism
  being a modification-time comparison rather than a re-read, so round 9 writes that mechanism into the rule
  — a settlement that depends on a method the text does not name is settled on luck.

### Three checkers, one unanswerable condition

Acceptance condition 3 — *every rule in every contract traces to a resolved node* — has now been declared
uncheckable by three independent blind agents, in three different sessions, each reaching it alone. The
condition is not wrong; it is **addressed to the wrong party.** Only whoever holds the record can check it,
and the checker is defined as the party without the record.

That is a lesson for whoever writes the next acceptance condition, and it belongs upstream of this node: a
condition is written by the spawning node, and nothing today makes a spawner ask whether the party that will
read it can. Recorded here rather than turned into a node, since minting one is the human's call.

### Attempt 5 — `PASS`, on a cheaper model, and the cost finding is not the expected one

**Run on Sonnet rather than Opus**, deliberately, because the human raised token cost in the same message
that authorised the round: a re-check of three small edits, with everything else already established by two
independent Opus-level runs, is the cheapest place on this map to buy that evidence.

**`PASS`.** Bar re-run in full, conditions 2, 4, 5, 7 re-checked where the edits reach, 1, 6, 8, 9 standing,
3 not establishable — the **fourth** independent checker to say so.

**The rule written one round earlier worked on its first run.** Told the statement of change is not
evidence, it compared mtimes across all six contracts and the glossary, **found three files the statement
did not mention** — `map.md`, and the node files for this node and for [When an AFK worker cannot
proceed](23-worker-cannot-proceed.md) — identified them as record files, declined to read them on its own
blindness, and said it had declined. That is the failure mode attempt 4 demonstrated, caught by the rule
that came out of it, one round later, by a different agent on a different model.

**One judgement worth recording.** The reviewing skill's smell baseline flagged **duplicated code** across
the six contracts — the shared blocks are real and large. It suppressed the finding against acceptance
condition 9, which requires each file to stand alone, and cited that baseline's own override rule. That is
the correct call and it is not a mechanical one: the duplication is a decision this node made and flagged
as `22.5`, not an accident.

**The cost finding, which is the opposite of the intuition it was testing.** Worker tokens by attempt:
attempt 1 died on an account limit and reported none; then **100.3k, 101.3k, 81.8k** on Opus, and **87.6k**
on Sonnet — the Sonnet run being the **second smallest, not the smallest**, and larger than the last Opus
run before it. A
cheaper model did not do less work; it did the same work at a lower rate. So the spend-per-kind table this
map and [Dogfood target](09-dogfood-target.md) ask the dogfood to carry back must be **tokens × rate**, and
a design that only counts tokens will read a model switch as having changed nothing.

**What this run is not.** It is not evidence that a cheap checker is as rigorous as an expensive one.
Nothing was planted for it to find, and round 8's edits were three careful sentences. The two failures this
map's checkers have caught were both found by Opus runs on freshly-written material. What it does show is
that a Sonnet checker followed a 160-line contract exactly, including a rule added an hour earlier, and made
one non-mechanical judgement correctly.

### Correction round 9 — the mechanism the settlement rests on

One edit, to the checker's contract. `22.11`'s rule gains the method the human accepted it on: *"Comparing
modification times against your last outcome is enough to find them. You are not re-reading the work to go
looking."*

**Written because a settlement that depends on a method the text does not name is settled on luck.** The
human agreed to the rule *"since it is cheap (modification time)"*. The rule as written said only to check
what the statement omits, and left a checker free to satisfy it by re-reading all six files — which is the
expensive reading, and the one the re-check rule exists to prevent. Attempt 5 chose the cheap method on its
own; the next checker would have been choosing again.

**It also puts a number on why this was worth another check rather than a delta.** The shipped conventions
document is carrying **seven** deltas for exactly this — small corrections that arrived after the node
resolved, each waiting on some future node to touch that file. A second product file starting its own delta
list, on its first day, over one sentence, is the more expensive option even at the price of a checker run.

Touches conditions 4 and 9. One more check.

### Attempt 6 — `PASS`, the cheapest run, and the rule paying for itself

Sonnet, **60.9k worker tokens** — the smallest of the six attempts, against 100.3k / 101.3k / 81.8k on Opus
and 87.6k on the first Sonnet run. It is cheapest **because** round 9's method landed: modification times
told it four contracts were untouched since 2026-08-14, so it stood them from the earlier outcome and read
only the two that had moved. It did *more* checking than the run before it for two thirds of the tokens.
That is the first measurement on this map where a rule's value shows up as a number.

**The undisclosed-change rule fired again, correctly and for the second time.** The statement named only the
checker's contract; mtimes showed `expedition-implementation/SKILL.md` also carried a same-day time, so it
read that file in full against conditions 1, 2, 4, 5, 8 and 9 *"as if for the first time"* and found it
compliant.

**And that exposes the rule's one limit, which is not worth another round.** A checker has no timestamp for
its own previous outcome, so a modification time newer than *some* unknown moment reads as suspicious
forever: this file was last edited in round 5 and has now been re-read from scratch by three consecutive
checkers. The fix is not in the contract — it is the **manager** handing the time of the previous outcome
alongside the statement of change, since the manager is the only party that knows it. Recorded for the
manager's skill rather than corrected here, and the cost until then is one file re-read per round.

**All eleven flags are settled.** The acceptance condition is met on everything a blind party can establish,
condition 3 remains not establishable by construction, and the bar is clean.

### What six rounds at one gate mean

[Human review of landed code](20-human-code-review.md) fixed that *"a chronology long enough to want
shortening is a signal, not a formatting problem"* and pointed it at node-too-coarse. **The signal is
firing and it is pointing somewhere else.** Five of the six contracts have taken no correction at all; every
round has landed on the **checker**, which is the one row [Subagent context
contract](12-subagent-context-contract.md) left with no method skills, no discovered standards, no re-check
behaviour and a return set of two values. This node is not too coarse — the checker's row was
under-specified, and each round has been the human filling it in against a live example. Worth knowing
before the same diagnostic fires on a node where it does mean what it says.
