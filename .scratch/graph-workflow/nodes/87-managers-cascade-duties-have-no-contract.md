# The manager's cascade duties are in neither contract

Type: implementation
Status: open

## Question

**The cascade has a design, a worker contract coming, and nothing that says what the *manager* does.**

[Write the cascade pass's worker contract](44-cascade-worker-contract.md) is open and writes *"the standalone skill
file its two roles are dispatched to"* — the **triage agent** and the **per-candidate agent**. That is the worker
side. It is not the manager's side, and nothing else is.

[Write the first version of the manager's skill](76-write-the-manager-skill.md) shipped without them, correctly:
its 43-clause acceptance condition never mentions the cascade, so a worker that had added the duties would have
been writing outside its condition. **Measured in the shipped file:** `triage` appears **0** times; `cascade`
appears twice and both are inside `## Words used exactly`; `sweep` appears four times, twice in the glossary and
twice as an item of the closing report. So the term is defined and the conduct is absent.

### The duties that are in neither file

All of them are settled, cited, and already gathered as §L of [Gather the manager's accumulated
duties](75-gather-the-managers-duties.md), items 120–126. They are the manager's own conduct rather than the pass's
internals:

- **The manager spawns a triage agent at every resolution.** Its whole input is the answer that just resolved plus
  the landed-code inventory, one line per node that ever landed code, from `git log --grep '^Node: <effort>/'`. It
  reads no product code, and **the empty result is the ordinary one**.
- **Each survivor gets its own agent**, handed that node's answer, its commits from the *anchored*
  `git log --grep '^Node: <effort>/<NN>$'`, and its files. The anchors are load-bearing: unanchored,
  `Node: <effort>/4` matches 4, 40–49 and 400 upward.
- **The per-candidate agent does not run while the code slot is occupied; triage reads no product code and never
  waits.**
- **Open-node targets stay manual** — the manager keeps reading its own answers and appending the marked note by
  hand, and sharpening an unstarted node's acceptance condition is an open-node edit that stays with it.
- **The sweep is the same machinery with the bound taken off** — triage with every resolved answer as its input,
  fanning out identically, plus a single read of the index of flags, and it runs only on an empty frontier.

### Why this is not a defect in either node

Node 44's scope is the file the pass's two roles read. Node 76's scope is its 43 clauses. **Neither omitted
anything it was asked for**, and the gap is between them rather than inside either — the same shape as the
gate-payload duty that node 75's gather could not produce, recorded on that node.

**Found by the human**, in one line, asking whether the cascade was going to be done in another node. The term being
defined and unused in the manager's contract is what made it visible.

### What has to be settled by whoever claims this

- **Whether these duties go in the manager's contract or in the cascade's own file.** Both are defensible: they are
  the manager's conduct, which argues for the manager's contract; but they are meaningless without the pass, which
  argues for keeping the whole mechanism in one place and having the manager's contract point at it.
- **Whether this waits on node 44.** If the duties land in the cascade file, this node collapses into that one. If
  they land in the manager's contract, the two can run in either order, and this one is a wording job over duties
  already enumerated.
- **What the manager's contract says about the trigger either way.** *Spawn a triage agent at every resolution* is
  a duty that fires on every node this workflow ever closes, and a manager reading only its own contract currently
  has no idea it exists.

## Acceptance condition

*Written in part by the manager, for a node it minted itself. **What is missing, and why:** the condition turns on
which file the duties land in, which is the first bullet above and which no resolved node settles. Choosing it here
would be the manager deciding inside a condition, which the readiness floor forbids. **That question goes to the
human before this node is claimed.***

**The part that can be written.** After this work, whichever file the duties land in states each of the five duties
above; the manager's contract either states them or names the file that does, so a manager reading only its own
contract learns that a resolution triggers a pass and where to read about it. Every `git log` pattern that appears
is anchored at both ends. No file under `.scratch/` is changed. The headings of every existing file under
`.claude/skills/`, listed by `grep -n '^#\{1,6\} '`, are all still present afterwards and in the same order. The
working tree meets the bar.

## Where it came from

The human's question at node 76's gate, `verbatim`: *"for the cascade, it will be done in another node ?"*
