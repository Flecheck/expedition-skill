# Whether the workflow ships explicit subagent definitions

Type: grilling
Status: resolved

## Question

Every worker in this effort is spawned as a **generic subagent told to read its contract from a path**. The harness
also supports **declared subagent types** — a definition file naming a system prompt, a model, and a tool set — and
the human has asked whether the six contracts should become six of those instead.

### The human's question, `verbatim`

> *"Should we create explicit subagents for the different types of tasks instead of spawning a subagent using the
> skill"*

### What is actually being traded

Today a spawn says *read your contract at `.claude/skills/expedition-checker/SKILL.md`*, and the worker's first act
is a file read. Under declared subagent types the contract would be the agent's own system prompt, arriving without
a read.

**The token difference is close to nothing and is not the reason to do this.** A subagent pays its whole opening
payload uncached either way ([What one node actually costs](52-token-cost-of-a-workflow.md)); moving the same text
from a tool result into the system prompt saves one round trip.

**The real prize is that a hard rule could stop being an instruction and become a fact.** The checker's hard rule 1
is *"write no file"*, and every worker contract forbids writing a graph file. Those are honour-system rules today,
and this effort has already watched two agents read one of them down in the same node — see [Whether a checker may
write scratch files outside the work](67-whether-a-checker-may-write-scratch.md), where a checker and a worker each
wrote scratch outside the tree, unasked, and disclosed it. **A declared type can withhold the write tools
entirely.** No other mechanism in the design can do that.

### Three costs, and the second is the one that would bite this effort today

1. **Ground rules 1 and 2 both point the other way.** Rule 1: *nothing in the shipped files may assume this repo,
   this machine, or a toolchain.* Rule 2: *each shipped worker contract stands alone as a file, rather than
   depending on any skill being invocable.* A declared subagent type is a harness feature and a **stronger**
   dependency than a skill — the contract would no longer stand alone, it would have to be registered.
2. **It may forfeit a property this effort measured and relies on.** [What the checker contract owes to having been
   run](31-checker-contract-owes.md) established, against the prediction on record, that **a contract edited
   mid-session does reach a worker spawned afterwards** when the spawn names it and the worker invokes it by name.
   Declared types are loaded when the session starts. **This effort edits its own contracts constantly and spawns
   workers against them in the same session** — six contracts changed at node 48 alone — so a definition that goes
   stale at session start would be a regression on exactly the workflow that is being dogfooded.
3. **The dogfood target is another repository.** Whatever the contracts become has to arrive in Lang's repo too.

### The manager's recommendation, marked as the manager's own and not a decision

**Not a swap — both, with the split on a seam that already exists.** Keep the six contracts as standalone files:
they are portable, they are what ground rule 2 demands, and they reach a worker spawned after they are edited. Then
ship, *optionally*, six thin declared types whose body does nothing but point at its contract, and whose only real
content is **the tool set**. The contract text never moves, so cost 2 does not arise — a thin wrapper has nothing
to go stale — and the enforcement that motivates the question is bought anyway.

That also gives node 67 a second answer to weigh: a checker denied the write tools cannot quietly take scratch, and
a checker **granted** a scratch directory and nothing else has its permission expressed as a fact rather than a
sentence.

## What has to be decided

1. Whether declared types are adopted at all, and whether as wrappers or as the contracts themselves.
2. **Whether a tool set is part of a contract.** This is the question underneath the question: today a contract
   describes what a worker may do, and this would make part of it describe what a worker *can* do. Those are
   different kinds of statement and the effort has never mixed them.
3. What happens on a harness that has no such feature, given ground rule 1.
4. Whether the manager itself becomes one.

## Where it came from

The human's own question, unprompted, alongside [Run an implementation node's work in a
worktree](68-implementation-in-a-worktree.md) and [Pruning a long-running effort's
map](70-pruning-a-long-running-map.md).

### Claimed by the manager

Picked as one of two grilling nodes, on the human's instruction to choose. **It is the human's own question, asked
directly**, and it is cheap to settle relative to its consequence: a declared subagent type can withhold the write
tools, which would turn a hard rule from an instruction into a fact. That is the only mechanism in the design that
can do it, and [Whether a checker may write scratch files outside the work](67-whether-a-checker-may-write-scratch.md)
records two agents on one node reading such a rule down.

## Answer

**No. The six contracts stay as they are** — standalone skill files, named by a spawn, read from a path by a
generic subagent. No declared subagent types: not as a swap, and not as thin wrappers. The human's words,
`verbatim`: *"for 69 leave them"*.

**The manager's own recommendation in the spawn — keep the contracts as files and ship six thin declared types
carrying only a tool set — is refused along with the full swap**, and refused on its own terms rather than on cost:
the tool set is the part that turns out to be worth nearly nothing, so the wrapper pays the portability costs to
buy something that does not work.

### Why the enforcement prize does not exist

Taking the six contracts' hard rules one at a time, withholding tools is **false for every rule that has actually
been broken and redundant for the one it could reach.**

1. **"You have no human-facing tool"**, in four of the six contracts, is **already a harness fact, for free.** No
   subagent in this harness has one; the worker confirmed it by inspecting its own tool list while running as one.
2. **"Write no file", "write no graph file", "never commit, never branch, never push"** are all **defeated by
   Bash**, and every one of these workers needs Bash — the checker runs the repo's own commands, the implementer
   builds and tests, and this harness's own standing instruction to workers is to *prefer* Bash for editing files.
   A `tools:` allowlist cannot say *Bash, but no redirection and no `git commit`*. **Decisively: both violations
   [Whether a checker may write scratch files outside the work](67-whether-a-checker-may-write-scratch.md) records
   went through Bash. The proposed mechanism would have caught neither of the two cases that motivated it.**
3. **The rules that matter most are path-scoped** — *nothing you build enters the product tree*, *everything lives
   in `prototypes/NN-<name>/`*, *you write no graph file*. **A tool set cannot express a path at all.**

Only **grilling** and **research** could run read-only, and neither is a kind where a violation has ever been
observed — so it would enforce exactly where enforcement is not needed.

**What would actually enforce these rules is not a tool set**: a PreToolUse hook or a permission deny rule. Those
exist, and they are heavier harness-specific machinery, squarely against ground rules 1 and 4. **Recorded so the
route is visibly declined rather than overlooked.**

### The distinction underneath, which is the durable part of this node

**A contract states what a worker *may* do, and it is honoured by an agent that reads it. What a worker *can* do is
a property of the harness that ran it.** They fail differently: a contract clause survives a change of harness, a
capability does not. Mixing them puts a claim in the shipped files that is **false on any harness that cannot
enforce it** — the exact failure ground rule 1 exists to prevent.

So *is a tool set part of a contract?* **No**, independently of whether declared types are adopted. **A hard rule in
this workflow binds by being read, and never by being enforced.** Two agents have already read one down; the remedy
is a better-written rule or a granted exception, not a capability the shipped files cannot guarantee.

### The four supporting grounds

- **`.claude/agents/` is a second shipping surface.** The workflow is one directory tree today and reaching Lang is
  a copy. Declared types add a second location that must be **registered**, with project/user/plugin precedence and
  collision rules — a stronger dependency than a skill, and a direct hit on **ground rule 2**.
- **Ground rule 1.** The map's stated insurance for a future non-Claude worker is precisely *"a worker contract that
  stands alone as a file."*
- **It reopens a decision the human already made.** [Subagent context contract](12-subagent-context-contract.md)
  fixed, on the human's call, that the contract travels as a skill invocation rather than as prompt text.
- **The one motive that would survive is parked, at the human's own word.** A declared type's real content is
  **model and effort per node kind** — the single declared type on this machine, `~/.claude/agents/opus-high.md`,
  sets exactly `model` and `effort` and **declares no tool set at all**. `map.md` parks *"what model the manager
  itself needs, and where a kind-to-model mapping lives"*. **That is the door to come back through, and this node
  is not it.**

### Decisions 3 and 4, closed

**Decision 4 — whether the manager becomes one: no.** The human talks only to the manager thread and a subagent has
no channel to a human, so a manager that were one could not do its job. **Decision 3** — behaviour on a harness
without the feature — is moot, nothing being adopted.

### One limit kept deliberately

**Whether a definition edited mid-session reaches a subagent spawned afterwards is undocumented, and this node did
not establish it.** The direct test needs a file written, which hard rule 3 forbids — node 67's wall, met live on a
grilling node. What *was* observed: the agent-type roster, with each type's tool set resolved into prose, is
injected at session start. **The decision does not rest on this**, and the limit is recorded rather than dropped
*"because an unestablished claim hardens into a fact once nothing depends on it"* — which is, verbatim, the shape
[What the checker contract owes to having been run](31-checker-contract-owes.md) records this effort getting wrong
once already.

### Consequences for two open nodes

[Whether a checker may write scratch files outside the work](67-whether-a-checker-may-write-scratch.md) **loses the
capability-based option** the manager's spawn offered it: its permission has to be prose in the contract, because
the checker needs Bash, so a tool set neither stops it writing scratch nor confines where it writes. And [Run an
implementation node's work in a worktree](68-implementation-in-a-worktree.md) is **not** pre-empted — `isolation:
worktree` is an agent-definition field, and if that node wants the mechanism it must make the case on its own
grounds.

## Flags

`69.1` `ASSUMPTION` **· settled** — **Decision 4 was settled by the worker without asking.** Whether the manager itself becomes a
declared type was closed from `map.md` alone. In the worker's words: *"Filed rather than asked because the grilling
contract requires any fact the files can tell to be read rather than put to the human, and this one is stated in the
map's standing preferences."*

`69.2` `ASSUMPTION` **· settled** — **The worker recommended, and the human decided, without the spawn's stated crux ever being
established.** The manager's spawn named the mid-session-reload question as the crux and asked for it to be
verified. It is undocumented; the direct test requires writing a file, and an attempt to read the harness's own
loading behaviour failed because the CLI ships as a compiled binary. In the worker's words: *"The enforcement motive
fails upstream of the reload question, and every supporting ground is independent of it. Worth the human's eye
because a crux the spawn named was left unestablished."*

`69.3` `ASSUMPTION` **· settled** — **The worker did not invoke the two method skills its contract names, and this is [What a
contract may name as a method skill](51-what-a-contract-may-name.md)'s predicted failure observed live.** The
grilling contract says *"Invoke `/grilling` and `/domain-modeling` if they are present."* Both are present but
registered as `mattpocock-skills:grilling` and `mattpocock-skills:domain-modeling`, not under the bare names. The
worker ran the contract's inline fallback discipline and did not translate the names. **Offered to node 51 as
evidence rather than argument.**

## Retrospective

**1. What it had to hunt for.** *Where the one declared type lives* — the manager's spawn said `.claude/agents/`,
which it read as repo-relative and **which does not exist in this repo**; it is at
`/home/mathieu/.claude/agents/opus-high.md`, user-level. Two calls lost. *Whether a `tools:` restriction is
enforced and whether Bash defeats it* — no file in this tree holds it; it came from the harness's own agent-type
roster, which lists `Explore` as *"All tools except Agent, Artifact, ExitPlanMode, Edit, Write, NotebookEdit"* — **a
live instance of the exact proposed design, with Bash granted.** *Whether a definition is re-read at spawn* — never
found; the CLI ships as a compiled binary with the JS bundled inside. Three calls, dead end.

**2. What it read and did not use.** Node 31 in full for one paragraph of flag `31.2`. `map.md`'s `## Out of scope`
and most of `## Not yet specified`. The six contracts' handover shapes and `## Flags`/`## Review` sections, needing
only frontmatter and hard rules. `decisions.md`, grepped and almost entirely unused.

**3. What would have made it easier — three criticisms of the manager's spawn, all upheld.** The `.claude/agents/`
path was wrong. The spawn **framed the crux one level too low**: it named the reload question, where the decisive
question was upstream — *does withholding tools stop any behaviour these workers have actually exhibited?* — and
*"once I asked that, the node was over."* And the spawn **asserted the prize as settled**: *"A declared type can
withhold the write tools. No other mechanism in this design can."* In the worker's words: **"Both halves are
misleading: withholding write tools does not stop Bash, and hooks and permission rules are other mechanisms. A spawn
that hands a worker the conclusion it is meant to test costs the worker the work of unpicking it."**

**4. What was stale or wrong.** The spawn's path. The spawn's and the node file's **shared premise that the tool set
is the cheap, obviously-worth-buying part** — the one declared type on this machine declares no tool set at all and
exists purely for `model` and `effort`, the use the node text treats as incidental and which turns out to be the
only durable motive. And `map.md` names `/grilling` and `/domain-modeling` as skills every session should consult
while both are registered under `mattpocock-skills:`, so **both the map and the contract read as though node 51 were
settled.**

### What the manager takes from it

*The manager's own note.* **The third criticism is the sharpest received in this effort and it is upheld without
qualification.** The manager wrote a conclusion into a spawn and asked the worker to test the question the
conclusion had already closed. The worker had to unpick it before it could work, and the two costs it names — three
calls on a compiled binary, and a crux framed one level too low — both descend from that one move. **The rule the
manager takes: a spawn states what is at stake and what is known; it does not state what the node is for deciding.**
The two are easy to confuse when the manager has a view, and the manager had one.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
