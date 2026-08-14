# Flags

Every flag in the graph, one capped line each, with its state. The **only** file the sweep reads to
build the completion report: the report is the unchecked lines. Specified by
[Graph file format](nodes/13-graph-file-format.md).

- `[ ]` outstanding · `[x]` settled by the human
- The checkbox lives **only here**. The flag's text and reasoning live in its node's `## Flags`
  section, so the two can never disagree and settling a flag never touches a node file.
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
- [ ] ASSUMPTION · [<node name>](nodes/NN-<name>.md) — <one line>
```

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
