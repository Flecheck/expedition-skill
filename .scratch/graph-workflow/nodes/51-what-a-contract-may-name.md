# What a contract may name as a method skill

Type: grilling
Status: superseded
Superseded by: 113

## Question

*Superseded 2026-09-29: this question no longer needs doing here. See `## Superseded, 2026-09-29` below.*

The four plugin skills the contracts name by bare name — `/grilling`, `/domain-modeling`, `/prototype`,
`/research` — are registered by this harness as `mattpocock-skills:<name>`, while `/coding-principles` and
`/naming` are registered bare. **A worker told to invoke `/research` must translate the name itself, and where
it does not, the contract's fallback silently governs** — the worker follows the *"where it is not present"*
branch and nobody learns that a skill it should have used existed.

Observed by [Review every shipped file against `/writing-great-skills`](47-review-shipped-skills.md)'s worker in
its own skill listing, and consistent with the harness's documented rule that plugin skills are addressed as
`plugin:skill`.

**Three options, none free.** Naming the namespace declares a command that breaks wherever the plugin is
installed differently, against `map.md`'s *prefer properties that are discovered over commands that are
declared*. Telling the worker to go and find a skill doing the job is what `expedition-checker/SKILL.md:86`
already does for the reviewing skill — *"a skill that reviews code, or anything doing that job under another
name"* — so the precedent is in the shipped set. Keeping bare names accepts the silent fallback.

**Why this cannot be an implementation node.** The *invoke if present* form is [Subagent context
contract](12-subagent-context-contract.md)'s decision, and `map.md` already records it as *"a flag rather than
an answer."* Changing what a contract may name changes that decision.

**Adjacent and deliberately not merged:** [Reconcile a method skill's instructions with the contract's hard
rules](48-method-skill-conflicts-hard-rules.md) edits the same four sections, but decides nothing about naming —
it adds a precedence rule that holds however the skill is addressed. If this node resolves first its answer
lands in the same edit; if not, the two land separately.

**One live datum the manager adds.** The plugin this effort borrows from was **renamed and rewritten upstream
between two of this effort's sessions**: `/writing-great-skills` became `/writing-for-agents`, its disclosed
reference file was renamed, and its `disable-model-invocation` was dropped. So the fragility this node is about
is not hypothetical — a bare name pointing into that plugin went stale on a rev bump, and only the human
noticing told the workflow.

## Superseded, 2026-09-29

*The manager's note:* superseded by [node 113](113-whether-the-method-skill-instruction-does-any-work.md), under the human's answer to [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q1 (`verbatim`: *"ok"*, recorded on node 366). Node 366's worker's reason: node 113 removed every plugin skill name from the contracts.
