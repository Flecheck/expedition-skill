# `graph-conventions.md`'s seven-files block says `map.md` is read once per session

Type: implementation
Status: open
Blocked by: 300

## Question

In `.claude/skills/expedition/graph-conventions.md`, the fenced block under `## The seven files` describes `map.md` as "Read once per session." The prose of the same file says every worker reads all of `map.md` once per node. The plain-English pass keeps code fences byte-identical, so node 299's worker carried the mismatch over. Reported in node 299's retrospective: *"Inside the file itself, the fixed fence says `map.md` is "Read once per session", while the prose says once per node. The fence is fixed text, so I carried the mismatch over."*

*Manager's note: minted from node 299's retrospective. Its acceptance condition is the manager's to write, and is not written yet.*
