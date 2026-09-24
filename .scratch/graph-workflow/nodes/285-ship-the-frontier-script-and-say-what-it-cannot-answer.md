# Ship the frontier script and say what it cannot answer

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [node 273](273-a-script-that-answers-what-can-be-started.md)'s worker, and pasted as it wrote it.*

> Write and ship the read-only frontier script node 273 decided on, and state in the manager's contract that it
> exists and where it is partial.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 273's worker. Pasted as it wrote it, and not the manager's.*

> A script exists at `.claude/skills/expedition/scripts/frontier.sh` and is executable. It is written in POSIX shell
> and awk only: no bash-only syntax, and no dependency on python, perl, node, jq or any other interpreter.
>
> Its first argument is the path to an expedition's graph directory — the directory holding `map.md` and a `nodes/`
> subdirectory of `NN-<name>.md` files. It optionally takes two further integers: the target number of concurrently
> running nodes that need the human, and the target number of implementation nodes, each defaulting to 2 when not
> given. **It hardcodes no path; in particular the strings `.scratch` and `graph-workflow` appear nowhere in it.**
>
> It writes no file and modifies nothing. Running it leaves the tree byte-identical.
>
> From each `nodes/NN-<name>.md` it reads only the header block — every line above the first line beginning with
> `## ` — and takes three fields from it: `Type:`, `Status:` and `Blocked by:`. It reads no field from below the
> first `## ` heading, and treats no text inside a fenced code block as a field.
>
> From the `Blocked by:` field it takes a node number only where that number lies outside every backtick-delimited
> code span, outside every `~~...~~` strikethrough, and outside the parenthesised target of every markdown link.
> **Four worked examples it must satisfy**, each written as the field's literal content followed by what must be
> taken from it:
>
> ```
> `123, 120`                                                       -> 123 and 120
> `[node 269](269-ignore-the-new-worktree-path.md)`                -> 269 only
> `none — [node 139](139-move-the-managers-material.md) landed as `4e38c11`` -> 139 only
> `~~95~~ **none — node 95 resolved and landed at `b095bb6`.**`    -> nothing
> ```
>
> An empty field, and the literal `none`, mean no blocker.
>
> It reports a node as startable when its `Status:` is `open`, it is not `claimed`, and every blocker taken from its
> `Blocked by:` field names a node whose own `Status:` is `resolved`. **No other status value satisfies a blocker.**
>
> Its output carries three things, in this order, each labelled in plain words:
>
> 1. for each of `grilling` and `implementation`, how many nodes hold `Status: claimed`, shown against the
>    corresponding target passed in or defaulted;
> 2. how many nodes are startable in total, and how many of each `Type:`;
> 3. the startable nodes themselves, grouped by `Type:`, one per line, each line carrying the node's number and its
>    name.
>
> It orders the startable nodes by nothing beyond that grouping, and it performs no check of the graph's internal
> consistency — no dangling-edge, back-edge, reused-number, label, index or flag check.
>
> Its opening comment states, in two sentences, that it reads only the expedition's own graph files and assumes
> nothing about the repository the expedition is being run on.
>
> `.claude/skills/expedition/SKILL.md`, under its existing `### Picking the next node` heading, gains a short
> passage that: names the script by its path relative to the skill directory; says the manager runs it when a node
> finishes, to see what is startable and whether a slot has emptied; and states in one sentence each that **the
> script cannot tell whether two startable nodes would edit the same file**, because no field records which files a
> node touches, so the manager applies that filter itself before filling a second implementation slot — and that
> **two grilling nodes can never collide**, a grilling worker writing no file.
>
> **Verification the checker performs:** run the script against the graph directory at `.scratch/graph-workflow` in
> this repository. It exits 0, writes nothing, and prints the three labelled sections above. The checker then picks
> **ten** `nodes/NN-<name>.md` files at random, reads each one's `Status:` and `Blocked by:` fields and the
> `Status:` of each node those fields name, works out by hand whether each of the ten is startable, and confirms the
> script's output agrees on all ten. The checker also confirms the four `Blocked by:` examples above are handled as
> stated, by reading the parsing code where no node in the tree exercises a case.
>
> No file other than the two named above changes.

## The manager's note at filing

*Not a change to anything above.*

**This is the first executable this effort ships**, and every ground rule on it was written for markdown
deliverables. **The argument for why ground rule 1 does not reach it is in [node
273](273-a-script-that-answers-what-can-be-started.md)'s answer and is load-bearing** — the rule guards the *host
project's* stack, and this script reads only the expedition's own markdown in a format the workflow itself creates.
**A worker on this node should carry that argument rather than re-derive it**, and a checker should hold the script
against it.

**The condition's verification clause is unusually strong and that is deliberate.** It makes the checker compute ten
nodes' startability by hand and compare, and read the parsing code for the cases no live node exercises. **That is
the only part of this node a `PASS` cannot be reached on by inspection.**

**The manager is the party the script exists to correct**, having reported *"nothing is waiting on you"* three times
in one session with slots free and work startable. It is worth a claiming worker knowing that the failure is
measured rather than supposed.
