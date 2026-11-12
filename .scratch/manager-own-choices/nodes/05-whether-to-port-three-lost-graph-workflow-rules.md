# Whether to port ~~three~~ four rules the closed `graph-workflow` map holds and the root `CLAUDE.md` does not

Type: grilling
Status: open
Supersedes: 04

## Question

*Written by the manager.* Settling this decides whether three rules from the closed `graph-workflow`
effort bind every later effort in this repository, or stay with that effort's record.

**Who answers.** The human, `verbatim`, 2026-11-11: *"1 2 and 3 -> not sure, add settling whether to
port those as a node in this effort, to be handled by flecheck. notably for 3 I suspect it means that
when writing skills, they should generally be written in such a way that allows a decision the human
made to be questioned (meta)"*. So this node's questions are for Flecheck, who ran the `graph-workflow`
effort.

The manager compared `.scratch/graph-workflow/map.md` and its sibling map files with the root
`CLAUDE.md`, by a read-only agent. These three rules are in that map, are not in `CLAUDE.md` or in any
shipped file, and fall outside what [node 394 of
`graph-workflow`](../../graph-workflow/nodes/394-a-repo-claude-md-so-the-next-effort-does-not-start-cold.md)
deliberately left out of `CLAUDE.md` ("landing and bookkeeping, and the 'why'"). One more reason they
may be absent: `## Standing steering, and standing instructions of one effort` in the manager contract
makes a human's standing instruction bind only its own effort, unless the human says otherwise.

1. **The shipped files should not depend on the `mattpocock-skills` plugin.** In
   `.scratch/graph-workflow/map.md` under `## Notes`, the standing preference with that bold lead. It
   quotes the human: *"I also would want the skill to not depend on mattpockock, I don't know what is
   the status of this. Add grilling directly on the skill and for the docs part we should make
   something. Inspired by "/domain-modeling" and
   https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"*. It goes further than ground
   rule 2, which `CLAUDE.md` carries. The comparing agent found no "mattpocock" under
   `.claude/skills/` on 2026-11-11, so the rule holds today, but nothing tells a later editor.
   `CLAUDE.md`'s ground rule 5 still locates `/writing-for-agents` in that plugin, as a repository
   standard that is never shipped.
2. **Consult `/repo-docs` by default, and read the glossary before writing anything.** In the same
   `## Notes`, the paragraph with the bold lead "Skills every session should consult". This was the
   manager's line. `CLAUDE.md` names the glossary's `_Avoid_` lines as a standard, but does not say to
   read the glossary first, and does not name `/repo-docs`.
3. **A decision of the human's own may be proposed for change, on the same footing as one the workflow
   made.** In the same `## Notes`, the bullet with that bold lead. It quotes the human: *"You can offer
   to change a rule I made, the rules I choose where because I though they where the best at the point
   they where chosen, but in the spirit of this skill, as we make stuff, we discover stuff and that can
   make us decide an earlier desision was wrong"*. The bullet adds that a worker still never changes a
   settled decision itself, and that a proposal reaches the human as a question with its ground stated.

For each of the three: is it ported, and where? The places are the root `CLAUDE.md`, as a rule for
work in this repository, or the shipped skill files, as a rule of the workflow itself. For rule 3, the
human above suspects a meaning about the shipped skills: that they should be written so that a decision
the human made can be questioned. Settle whether that is the meaning, and whether it is the rule to
port.

*Updated in place by the manager on 2026-11-12, when this node's question changed. Nothing above is removed: the title's "three" is struck and "four" added beside it, and rule 4 below is added.* The human, `verbatim`, at the gate of [node 04](04-port-the-rule-that-node-files-are-written-for-agents.md), which had ported the map rule numbered 4 in the manager's comparison: *"actually for the claude.md change, let's move it to the node for flecheck like the others so he can decide"*. Node 04 is superseded by this node.

4. **The node files are written for agents, and the human works from the manager's chat and from code review.** In `.scratch/graph-workflow/map.md` under `## Notes`, the bullet with that bold lead. It quotes the human: *"I expect the nodes to be mostly targeted to agents, as I will mostly work from what the manager says (questions from subagents) and with code review."* It limits itself by document class: over node files it stands as written, over the shipped worker contracts only the prose explaining why may be compressed, and it does not reach `map.md`. Node 04 drafted a port of it, which never landed. Its text, a proposed item 7 of "Rules for writing:" in the root `CLAUDE.md`, is quoted in node 04's `## Review`, with the human's correction that moved it there from a section of its own, and three checker runs that each established it against node 04's condition.

For rule 4, settle whether it is ported, and where, as for the other three.

*Updated in place by the manager on 2026-11-12, adding the human's suspicion below. Nothing above changes.* The human, `verbatim`: *"for the node to flecheck: I suspect that basically things that were meant to land as well placed instructions in the skill landed in the map instead, as instructions for the effort of building the map, and so may have been lost to the skill itself."* So for each rule, also settle whether it was meant as an instruction of the workflow, belonging in the shipped skill files, rather than as a rule of the `graph-workflow` effort.
