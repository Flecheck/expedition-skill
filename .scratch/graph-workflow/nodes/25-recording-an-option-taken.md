# What is recorded when the human takes an option as offered

Type: grilling
Status: open

## Question

When the human answers by taking one of the options they were offered, exactly as written, what goes onto
the node — the option's text standing as the human's own, or the manager's rendering marked `paraphrase`?

Reported by [Off-contract subagent output](17-off-contract-output.md)'s worker, which hit it as the stated
limit of the check that node built.

It is unsettled rather than obvious: [Subagent context contract](12-subagent-context-contract.md)'s
`## Interview` marks three such answers **`verbatim` (option chosen as written)**, while [Off-contract
subagent output](17-off-contract-output.md)'s marks all three of its own **`paraphrase`**. Same act, two
markers, on the same map, four nodes apart.

It matters more than it did when [Relay protocol](08-relay-protocol.md) accepted the marker as the remedy
for `F6`, because [Off-contract subagent output](17-off-contract-output.md)'s check now makes the recorded
answer **the baseline something reads against**: a check that catches a worker inventing the human's words
cannot catch a manager having supplied them, and afterwards the two look alike on the page.

The third option — the manager echoes the answer back and the human confirms it — costs a round trip on the
resource this map calls scarce, and is the one to beat.
