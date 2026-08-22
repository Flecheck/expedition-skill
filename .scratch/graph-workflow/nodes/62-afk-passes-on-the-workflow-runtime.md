# Whether the AFK passes move to the dynamic-workflow runtime

Type: grilling
Status: open

## Question

Claude Code's dynamic-workflow runtime keeps intermediate results *"in script variables instead of landing in
Claude's context"*, with a JSON `schema` making a handover's shape **machine-enforced rather than
prose-enforced**, and it staggers matching agents in a fan-out so they share a tools-and-system-prompt prefix.
That addresses the **manager's context** directly — the resource [Friction from running this map by
hand](24-self-hosted-friction.md) measured as first-failing — and it carries one decisive limitation:

> *"No mid-run user input — only agent permission prompts can pause a run. For sign-off between stages, run each
> stage as its own workflow."*

**So it can host the AFK passes — checker runs, the cascade, the sweep — and cannot host an interview or a
gate.** Do those passes move, and if so which?

Reported by [What the token findings change in the workflow and its
skills](53-what-token-findings-change.md)'s worker from facts established at [How an agent workflow and its
skills reduce their own token cost](52-token-cost-of-a-workflow.md).

**Blockers: none.** It carries the prefix-condition candidate folded in, flagged as `53.4`: the five
preconditions — same model, effort level, agent type, tools, output schema, working directory — **name five
things this effort varies freely**, and whether `Agent`-tool spawns get the stagger at all is *documented neither
way*. So homogenising them is worth doing only inside this decision.

**Why it graduated from fog rather than staying there**, in that worker's words: *"the map's item on the runtime
proving too simple says it is 'only judgeable after a dogfood run'. That was true while the alternative was a
firstmate redraw. A shipping mechanism that addresses the first-failing resource today is a decidable question
with a known constraint, which is the threshold for a node."*

**If it resolves in favour, it invalidates [Cascade pass mechanics](15-cascade-pass-mechanics.md)**, whose answer
specifies a per-resolution triage agent fanning out to node-minting agents — the exact shape that runtime would
host differently.
