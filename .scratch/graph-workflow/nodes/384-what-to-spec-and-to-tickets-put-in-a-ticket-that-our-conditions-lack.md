# What `/to-spec` and `/to-tickets` put in a ticket that this workflow's nodes lack

Type: grilling
Status: claimed
Blocked by: none

## Question

*The human's own question, `verbatim`, 2026-10-04, asked while node 380's gate was in front of them. **Minted by the manager and not surfaced by any worker.***

> I have a question in matt pockock skills /to-spec and /to-tickets I feel that they generate a ticket that is much bigger that what was generated for 383, it there some stuff that we should take ?

"383" is [node 383](383-ship-the-repo-docs-skill.md), whose node file holds the question and acceptance condition node 130's worker wrote for it. The two skills are installed with the `mattpocock-skills` plugin. On this machine, on 2026-10-04, a copy sits under `/nix/store/*-claude-code-mattpocock-skills-patched/skills/engineering/to-spec` and `.../to-tickets` (the store path is this machine's, and may change).

The answer decides what, if anything, from those skills' tickets this workflow's implementation nodes should take: in the question, the acceptance condition, or what a spawn carries. It also decides where the change would land.
