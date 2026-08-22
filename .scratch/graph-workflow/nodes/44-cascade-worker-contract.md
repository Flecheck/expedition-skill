# Write the cascade pass's worker contract

Type: implementation
Status: open

## Question

The pass now has a design and no contract. Write the standalone skill file its two roles are dispatched to,
in the shape of the six contracts already shipped.

Reported by [Cascade pass mechanics](15-cascade-pass-mechanics.md)'s worker, which wrote the acceptance
condition below. It is the second of the two nodes that node's answer required, and it is the one that makes
the design executable rather than recorded.

**Blockers: none. Sequencing only** — it creates a new directory under `.claude/skills/` and touches no
existing file, so it collides with nothing, but the code slot is exclusive.

## Acceptance condition

One new file exists — `.claude/skills/expedition-cascade/SKILL.md` — carrying YAML frontmatter with
`name: expedition-cascade` and a one-line `description`, in the same frontmatter shape as the sibling
files already under `.claude/skills/expedition-*/SKILL.md`. No existing file in the repository changes,
and no file under `.scratch/` changes.

The file is a worker contract: instructions addressed to the agent that will follow it, in the voice of
`.claude/skills/expedition-checker/SKILL.md`, carrying no reasoning about why it says what it says and no
history of how it was decided. It stands alone as a file and does not depend on any other skill being
invoked. It covers two roles of one pass and states which role a given spawn is dispatching. It contains
all of the following:

1. **Its own vocabulary, defined in the file.** At minimum: node, manager, worker, handover, flag,
   resolve, supersede, acceptance condition, code slot. It states that a node's identity is a sequential
   number that never changes and its name is free-form.
2. **The triage role.** Its input is one resolved node's answer plus an inventory of every node in the
   effort that has landed code — one line each carrying that node's number, its name, and the paths its
   commit touched. Its job is to decide which of those landed nodes that answer may have made stale. It
   reads no product code. Its output is a list of node numbers, and the file states that the empty list is
   the ordinary result and a success rather than a failure to find something.
3. **The per-candidate role.** Its input is one landed node — its answer, its commits, and its files. Its
   job is to judge whether that node's landed code still agrees with that node's own answer. It reads
   product code and modifies none.
4. **Neither role edits product code, and neither writes any file.** The file says this in as many words
   for both roles, and says that what the agent returns is text the manager writes.
5. **What it returns when it finds something is a node to be created**, described so its reader can write
   one: a name, a kind, the question, the blocking edges, and — where the kind is `implementation` — an
   acceptance condition the agent writes itself. The file states that the agent reports an
   `implementation` node where what the fix must be is determined, and a `grilling` or `research` node
   where it is not yet clear what the fix should be.
6. **The exact shape of what it returns**, with every part named, and a statement that a part it has
   nothing for is written `none` in full rather than left off.
7. **The self-containment rule for any acceptance condition it writes, written into this file rather than
   pointed at.** Everything needed to judge whether the work is done is in the condition, and the
   condition's reader never goes anywhere else to find out what it demands; that reader is a second,
   independent, read-only agent handed the condition as text, which has not read the node and does not
   read the effort's record at all. A path may say where the work must land. What may never sit outside
   the text is the demand itself — *as decided at node NN*, *the wording agreed earlier* — because each
   sends its reader away to learn what is being asked. Material genuinely held elsewhere is copied into
   the condition. A demand that quantifies over the whole record — that the work contradicts no decision,
   that everything in it traces back to one — belongs in no condition at all, there being no bounded
   material to bring inside the text. The file also tells its reader to read what it wrote back against
   those four points before handing it over.
8. **The code slot.** The file states that the per-candidate role does not run while another agent is
   modifying product code, that occupancy is discovered from the working tree, and that waiting costs
   nothing because what the pass produces is a queued node rather than an edit. It states that the triage
   role reads no product code and never waits.
9. **It raises no flag**, and where it cannot judge — a tree in flux, a file it cannot read — it says so
   in what it returns and reports no node.
10. The tree meets the bar.
