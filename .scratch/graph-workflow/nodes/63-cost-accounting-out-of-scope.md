# Whether the out-of-scope line on cost accounting still holds

Type: grilling
Status: open

## Question

`map.md`'s `## Out of scope` rules out *"Cost and token accounting, dashboards, fleet telemetry"*, while two of
its fog items require the dogfood to carry back a **measured** spend per node type, and the human's standing
instruction prioritising token-use improvement forbids ranking candidates by **predicted** saving — which cannot
be obeyed without measuring.

Meanwhile the harness already **prints** what those ask for: `/usage` attributes recent usage to skills,
subagents, plugins and individual MCP servers, reports cache read against cache write per model, and raises
behavior flags when one accounts for 10% or more of recent usage. **Reading numbers the harness already prints is
not building accounting** — but as written the line reads as forbidding the measurement the fog demands and the
new instruction requires. Does the line narrow, and to what?

Reported by [What the token findings change in the workflow and its
skills](53-what-token-findings-change.md)'s worker, from facts established at [How an agent workflow and its
skills reduce their own token cost](52-token-cost-of-a-workflow.md).

**Blockers: none.**

**Why it is a node rather than settled at node 53 with the human present**, in that worker's words: *"narrowing
an out-of-scope line is a scoping act, and that section's own rule is that nothing in it becomes fog without the
destination being redrawn. So it is not this node's even with the human present."*
