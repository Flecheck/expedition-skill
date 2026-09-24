# Drop the closing report's case for flags raised before settle-at-close existed

Type: implementation
Status: open
Blocked by: 300

## Question

`### Settle a flag` says flags reach the closing report in two cases. One is "a flag raised before this settling rule existed, on a node already resolved". No effort started after the rule shipped can hold such a flag. Should the shipped file drop that case?

*Reported by [node 300](300-rewrite-graph-conventions-part-2.md)'s worker.*

## Acceptance condition

*Authored by node 300's worker and filed by the manager.*

In `.claude/skills/expedition/graph-conventions.md`, under `### Settle a flag`, the paragraph beginning "Flags reach the closing report" states one case only: a flag whose pick report the human never answered, because they never spoke again. It no longer states the case of a flag raised before the settling rule existed. No other sentence in the file changes, and no other path changes. The working tree meets the bar.
