# An acceptance condition demands facts about files the checker is told it does not read

Type: grilling
Status: claimed

Blocked by: none

## Question

*Surfaced by [Two writers edit the map at once](115-two-writers-edit-the-map-at-once.md)'s worker, and pasted as it
wrote it.*

> The checker's contract hands it the effort's ground rules as copied text, giving as the reason that they live in
> "the effort's map, which every other worker reads and you do not", and tells it that where a condition's enumerator
> reaches the effort's record it must report that it reaches material it is blind to. Yet a node whose own work is a
> graph file gets a condition made almost entirely of claims about that record — node 140's fourteen clauses are
> nearly all facts about `map.md` and its siblings, and it went to its checker with them. So: may an acceptance
> condition demand a change to the effort's own record at all; if it may, is the checker permitted to read those
> files as *the work* rather than as *the record*; and if it is not, what establishes that such a node is done?

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**The manager has already made this judgement twice, on its own authority, and flagged itself both times** — at
`147.3` and again at `140.9`. Both flags say the same thing: the node's work *is* the record, no checker can hold it
against the condition without opening those files, and the manager instructed the checker to read them as the work
under check and derive nothing from their content. **Both were settled at their gates.** This node is whether that
instruction is right, and it was surfaced by a worker that could see the collision from outside it.

## Interview

### Attempt 1

*Banked at hand-back, before being relayed: this question queues behind node 141's, which was live when it arrived.*

**The worker's question, pasted as it wrote it.**

> **ASK:** Should the permission the manager has twice improvised — the checker reads the changed graph files as the
> work under check, and takes no statement of intent from them — become a written rule in
> `map-implementation-rules.md` now?
>
> **RECOMMENDED:** Yes, and I would write three things, about fifteen lines total. **(1)** The permission goes in
> `map-implementation-rules.md`, whose declared readers are exactly the implementation worker and its checker, so no
> other worker pays to read it, and which node 143 is already wiring to arrive through the spawn. **(2)** It is
> stated as what it guards rather than as a directory: the checker is blind to statements of intent and decision —
> node files, `decisions.md`, `flags.md` — and reads whatever it is handed as a changed path as the work, whatever
> directory that path sits in, saying so in its outcome. **(3)** The guard the two cases had by luck becomes a duty
> on whoever writes such a condition: exclude the node's own status line, `decisions.md` and `flags.md` from the
> paths the worker may edit, and say so *in the condition*, so the checker can see the guard instead of trusting the
> spawn. This rests on measurement rather than argument — two runs, six independence checks, none failed — on the
> fact that `map.md` already reaches every checker as a standard so the blindfold was never a ban on graph files, and
> on node 28's rule that an improvised departure owes two outputs, a licence and a node for the permanent fix: this
> has had two licences and, until this node, no node.
>
> **ALTERNATIVES:** Keep it as a per-node manager instruction flagged each time — cheapest today, but it
> re-improvises on every record node and leaves the reasoning nowhere a later manager finds it.
>
> No checker on a record-editing node at all: it goes straight to your gate and your diff read is the check — honest
> to the contract as written, and it drops the second pair of eyes on exactly the nodes that rewrite the effort's own
> rules.
>
> Ship it into `expedition-checker/SKILL.md` instead of the map — node 93 says a rule reaches a shipped file only
> where you say so, and node 143 is claimed on that exact file right now, so I would mint this as its own node once
> 143 lands rather than collide with it.
>
> Narrow it to conditions answerable without reading for meaning — matches the evidence exactly, but nothing today
> separates a structural clause from a semantic one, so it needs a test I cannot write.

**What it established, pasted as it wrote it.** The manager records that **the first of these corrects the manager's
own framing of its two flags**:

> **The blindfold is already narrower than it reads, and nobody wrote that down.** The checker's contract closes its
> list of givens with *"There is a record behind this work… You do not read it"*, and guards that with *"The
> acceptance condition as given to you is the only statement of intent you get."* So the blindfold is against a
> second statement of intent, not against a directory. The standards a checker on this effort holds work against
> name *"this map's standing preferences, ground rules and four standing rules"*. `map.md` is one of the seven graph
> files. **So every checker here already reads part of the record, by the bar, deliberately.** What it is actually
> blind to is the node files, `decisions.md` and `flags.md`.
>
> **Only one of the two cases was a real breach.** Node 140's five changed paths were `map.md`,
> `map-implementation-rules.md`, `graph-conventions.md`, `map-manager-only.md` and `map-history.md` — no node file,
> no `decisions.md`, no `flags.md`, and three of the five were standards it was already given. **Node 147 is the
> genuine case**: sixteen node files, seven of them resolved and carrying an `## Answer`.
>
> **Whether it unblinded the checker, measured on both runs. Six things point one way and none the other.** Node
> 140's checker `FAIL`ed the work on the one clause its own worker had already pre-excused in the node file at flag
> `140.5` — the excuse was sitting in the record and it did not adopt it; on the re-run it refused to read the
> human's *"so that the checker then passes"* as a verdict; it reached the same reading of a self-contradictory
> clause the worker had reached, separately; and it independently found the defect node 153 was minted for. Node
> 147's checker handed back a finding contradicting the condition's own author, and established the two central
> clauses byte-wise, so comprehension never entered.
>
> **Three guards were in force both times — by accident, not by rule.** Both conditions excluded the node's own
> status, `decisions.md` and `flags.md` from what the worker may touch. Both checkers took the paths from `git status
> --porcelain -uall` rather than from the record. And both conditions were answerable mechanically.
>
> **What the evidence does not reach.** Two runs, both on conditions answerable by bytes, greps and counts. Neither
> asked a checker to judge whether newly-written record prose was *correct*.
>
> **One contract clause has no determinate reading here.** *"Where the recorded command's domain reaches the
> effort's record rather than the working tree, run it as written and report that the condition's enumerator reaches
> material you are blind to"* assumes the two are disjoint. On a record node they are one directory; node 147's
> tree-wide enumerator fell in that gap and no such report was made.

***The manager's note.*** **The manager's own flags `147.3` and `140.9` overstated what it had done.** Both say the
manager unblinded a checker to the effort's record. On node 140 that is false on the worker's measurement: none of
the five changed paths is a node file, `decisions.md` or `flags.md`, and three were already standards the checker is
given. The flags are settled and are not withdrawn; this correction is recorded beside them rather than over them.
