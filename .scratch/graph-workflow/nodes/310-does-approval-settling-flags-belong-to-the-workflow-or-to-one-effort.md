# Does the human's approval settling flags belong to the workflow or to one effort?

Type: grilling
Status: resolved

## Question

`## Flags` in the manager contract and `CONTEXT.md`'s Flag entry state that a node's flags settle at its gate or pick report as a rule, with no kind of node exempt. `### A flag in a payload`, in the same file, says the same settlement is "one effort's standing instruction from its human, and is not a rule of the workflow", and tells the manager to ask. Which is it?

*Reported by [node 297](297-rewrite-the-manager-contract-part-2.md)'s worker.*

## Answer

It is a rule of the workflow. The human answered this node's question directly, at [node 297](297-rewrite-the-manager-contract-part-2.md)'s gate, `verbatim`: *"for 1 I agree, it the user wants something, at the end it should do what the user wants (the workflow should still use the best tool he has) . for 3, its a workflow rule"*. Their "3" is the manager's gate item: *"The rule that your approval settles a node's flags is now stated as one effort's instruction, not a workflow rule … That contradiction is node 310's question."* No worker was spawned for this node. Node 297's correction round carries the fix into the manager contract.
