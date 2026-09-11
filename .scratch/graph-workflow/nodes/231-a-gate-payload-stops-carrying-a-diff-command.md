# A gate payload stops carrying a command that prints a diff

Type: implementation
Status: open

Blocked by: 229

## Question

*Minted by the manager from the human's own instruction, given while answering [node
216](216-what-a-correction-round-after-a-rebase-conflict-owes.md)'s `Q2.`*

**Their words, `verbatim`:**

> On another notes, the current diff command is not useful, I am using vscode, not looking at the diff in the
> terminal, it can be removed.

And, on the same subject one clause earlier: *"don't give the diff, If I want the diff, I can get it."*

**What currently says otherwise, and it is their own earlier instruction.** `map-manager-only.md`'s landing policy
states: *"**The gate payload names the worktree's path and the command that shows its diff**, because an
implementation node's work is uncommitted in a checkout outside the repository and `git diff` where the human is
standing does not show it"* — added after a gate reached them with neither and they asked, `verbatim`: *"what are
the changes ? I don't see them in git ?"*. The shipped manager contract carries the same demand in its gate-payload
list.

**What changed is not the need but the reader.** The 2026 instruction was about being unable to **find** the work at
all. The work is still in a worktree outside where they are standing, so **the path is still needed**; what is not
needed is a `git -C <path> diff` line, because they read the diff in an editor rather than in the terminal.

## Acceptance condition

**None yet, and the manager has not written one.** This node reaches **a shipped file and a record file**, and the
record file is `map-manager-only.md`, whose landing policy states the rule — the same file [node
229](229-bank-the-landing-sections-accounts-out-of-map-manager-only.md) is holding under a condition that demands
byte-identity outside its own fourteen spans. **A condition written now would be written against text about to
move.**

Whoever writes it owes, at minimum: that the worktree's path survives in the gate payload; that the diff command
does not; that the human's `verbatim` words on both sides are kept, since the rule being reversed is their own; and
that the shipped manager contract and the landing policy agree afterwards.

## The manager's note at filing

*Not a change to anything above.*

**The blocking edge is scheduling rather than logic.** Nothing this node does needs node 229's output — it is
blocked because two writers must not hold `map-manager-only.md` at once, and node 229's condition would be broken by
an edit landing under it.

**The manager has already stopped emitting the command**, which needs no node and no landing: it is a change to what
the manager does. This node is for the two files that still say otherwise.

**One thing worth stating because it will recur.** This is the second time today a rule of the human's own has been
reversed by the human — the first being node 218's `## What this file is`, which a clause of the manager's demanded
and which they removed. **The map's standing preference that a decision of theirs may be proposed for change on the
same footing as one the workflow made is doing real work**, and neither reversal needed a supersession argument.
