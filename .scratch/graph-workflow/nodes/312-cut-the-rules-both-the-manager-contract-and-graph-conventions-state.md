# Cut the rules that both the manager contract and `graph-conventions.md` state

Type: implementation
Status: open
Blocked by: 297, 298

## Question

The human, `verbatim`, after approving node 300: *"wait for 300, we should also cut the duplicate rules, I don't know if they need to be cut in the manager contract or the graph-convention"*. It answers node 300's flag `300.2`, whose worker kept rules that `graph-conventions.md` shares with `.claude/skills/expedition/SKILL.md`, such as when flags settle and the order for recording the human's answers. Node 300 had already landed as `527596c` when this arrived.

Each rule that both files state should be stated in one of them, with the other pointing at it where a reader needs it. Which file keeps each rule is being put to the human. The acceptance condition waits on that answer, and so does node 298, the last rewrite of the manager contract.

*Manager's note: minted by the manager. The condition is the manager's to write once the human has answered.*
