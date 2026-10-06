# Narrow the flags.md clause in the worker contracts

Type: implementation
Status: out-of-scope

## Question

*"`flags.md` is not yours. Leave it unread"* stands unchanged in **five** shipped contracts —
[`expedition-grilling`](../../../.claude/skills/expedition-grilling/SKILL.md) line 41,
[`expedition-implementation`](../../../.claude/skills/expedition-implementation/SKILL.md) line 54,
[`expedition-research`](../../../.claude/skills/expedition-research/SKILL.md) line 37,
[`expedition-prototype`](../../../.claude/skills/expedition-prototype/SKILL.md) line 43, and
[`expedition-precondition`](../../../.claude/skills/expedition-precondition/SKILL.md) line 45.

The clause exists to keep a worker's read small and to stop it second-guessing decisions outside its own
node. A node **about** that file is a case it did not consider. Give it the carve-out it lacks.

One thing to decide while doing so, and the answer must state which it chose: is the carve-out **a
conditional pointer the spawn names** — which keeps a worker's behaviour readable from its own file and keeps
the authority explicit — or **a condition the worker judges for itself**? Under [Node type
taxonomy](07-node-type-taxonomy.md) a small ambiguity is decided and flagged while a genuine fork becomes a
grilling node; if the implementer judges this one a genuine fork, that is the route.

### Why it is worth a node

**The clause has cost twice, and only one of the two was a suspension.**

- [Whether flags.md survives the settle-at-close practice](27-does-flags-file-survive.md)'s spawn
  **suspended** it, because that node's whole subject was the file. Well-grounded, plainly stated, and the
  node could not have been worked otherwise.
- [Carry the recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md)'s worker
  **complied** with it while writing that same file's own conventions, and so had to guess a punctuation
  detail blind — flag `26.2`, whose manager note records that the guess happened to match what was already
  in the file. **Compliance was as expensive as the departure**, and only luck kept it from being worse.

Created by [Whether a spawn may override a shipped worker contract](28-spawn-overriding-a-contract.md), which
is also the node that says why this repair is a node at all rather than something the manager does in
passing: node 27's departure produced no node, and a session later the clause was still unchanged in all five
files while node 28 was still carrying the narrowing as an open question. **This node is the repair that got
lost**, minted late and on the record.

### The acceptance condition is owed

Written by whoever spawns this, per [Node type taxonomy](07-node-type-taxonomy.md), and it may not be claimed
without one. Deliberately **not** written by node 28's manager, on [What the checker contract owes to having
been run](31-checker-contract-owes.md)'s warning: node 26's condition was the first written by a manager
rather than by a spawning node or its worker, and it had to be amended twice.

## Annotation: the sentence that made this node unclaimable is superseded, and the node is now startable

*Filed by the manager.* This node's `### Why it is worth a node` records that its condition was *"Deliberately
**not** written by node 28's manager, on [What the checker contract owes to having been
run](31-checker-contract-owes.md)'s warning: node 26's condition was the first written by a manager rather than
by a spawning node or its worker, and it had to be amended twice."*

**That sentence is superseded** by [Who writes the acceptance condition for an implementation node the manager
mints itself](39-condition-for-a-manager-minted-node.md), decided by the human on 2026-08-22 with the words
*"ok for recommendation"*. The manager may write this node's condition, under four constraints: it may demand
only what is already fixed by a resolved node, this node's own `## Question`, or the state of the files; the
manager reads it back against the self-containment rule and the no-quantifying-over-the-record rule before the
claim and records that reading here; the condition is marked as the manager's own; and the pick report names
that it is the manager's and what it demands, without the work waiting for a reply.

**The cost of the refusal, measured on this node.** It has been unclaimable since 2026-08-19 — ten node
resolutions and seven landed commits — and the node 39 worker's summary of the outcome is *"Two nodes stopped,
no defect avoided."* The other is [Nothing carries a flag's account of what produced it out of a
worker](40-flag-account-has-no-handover-part.md).

**One thing whoever writes this condition must not do.** This node's `## Question` holds a live fork — whether
the carve-out is *a conditional pointer the spawn names* or *a condition the worker judges for itself* — and
constraint 1 forbids the condition from deciding it. Under [Node type taxonomy](07-node-type-taxonomy.md) that
is either a small ambiguity the implementer decides and flags, or a genuine fork that becomes a grilling node,
and the node already says the implementer's judgement decides which. So the condition states the property and
leaves the form, or the fork goes to the human as a raise. **A condition made writable by deciding that fork
does not pass the readiness floor.**

A second thing that has arrived since: [Review every shipped file against
`/writing-great-skills`](47-review-shipped-skills.md) found *"`flags.md` is not yours. Leave it unread"* to be a
**bare prohibition with no positive target beside it**, and assigned that repair here rather than to
[Reconcile a method skill's instructions with the contract's hard rules](48-method-skill-conflicts-hard-rules.md),
whose clause 2 names two other sentences. So this node now carries two changes to the same clause in the same
five files: the carve-out it was minted for, and a stated positive beside the prohibition.

*The manager's note, 2026-10-05:* the question changed, as reported by [node 385](385-whether-the-rarely-used-node-kinds-should-stay.md)'s worker under its `CONDITIONS`: "It names the flags.md clause in \"five shipped contracts\", the research contract among them. After the new node lands there are four, and the research link is dead." The new node is [node 388](388-merge-research-into-precondition-and-remove-the-cascade-pass.md).

## Ruled out of scope, 2026-10-06

Dropped at the triage the human invoked on 2026-10-06: only this self-hosting effort hits the clause, the per-attempt permission route already covers it, and its other half (wording the rule as what to do) is already met by the current "Leave `flags.md` unread. It is not yours.". A read-only agent checked the node against the current files.

*The human's answer to the triage proposal, `verbatim`, 2026-10-06:* *"ok"*. The manager's proposal ended "Please answer Q1 to Q4. \"ok for all\" approves each as proposed."

