# An acceptance condition demands facts about files the checker is told it does not read

Type: grilling
Status: resolved

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

## Answer

*Attempt 2's, pasted as it wrote it.*

**The worker's own preamble, standing before its handover block.**

> The human's answer sends this to the map rather than to the shipped contract. That is a divergence from my
> recommendation, and one of my own two objections to that placement is now mine to carry. I worked it rather than
> re-asking, and the placement inside the map is settled by rules already written.
>
> **What resolved the objection.** I claimed the checker would skip a permission placed in
> `map-implementation-rules.md`, because its contract says to read that file *for its standards* and "leave the rest
> of that file unread". Checking the file itself, that objection fails: the `## What the work is held against`
> section **already carries checker-conduct rules** — the review-route paragraph tells the checker which standards to
> hold work against and that "a checker does not go looking for" a reviewing skill — and node 143's shipped contract
> explicitly expects to read conduct out of there ("A reviewing skill is one the standards name"). So a rule about
> how the checker reads the work, placed in that section, is read. The human's placement works.
>
> **And the second objection dissolves too.** Re-reading the shipped sentence in its own section, "read nothing else
> in the effort's directory … open no other file beside it" sits entirely within `## The standards you hold the work
> against`. It governs **the route by which standards reach the checker**, not given 3, which hands it the changed
> paths. So this is an *ambiguity* a cold checker hits on a record node, not an override the map would have to
> perform — which is why an effort-local rule can legitimately settle it and node 28 is not engaged.

**The answer.**

> **Yes to the first two questions, and the permission becomes a written rule of this
> effort's map rather than of the shipped contract.**
>
> **An acceptance condition may demand a change to the effort's own record.** Nodes 140
> and 147 both did it and both landed, and seven open implementation nodes — 80, 88,
> 144, 149, 152, 156, 160 — are shaped the same way. [Node
> 36](36-resolved-node-clause-cannot-be-self-contained.md) is not touched by this: it
> refuses a condition that *quantifies over* the record — *the work contradicts no
> decision* — where a record node's condition names bounded paths, which is exactly what
> [node 33](33-condition-is-self-contained.md) permits a condition to do. A path is
> where, and a record file is a path like any other.
>
> **The checker is permitted to read those files as the work under check**, and takes no
> statement of intent from them. The manager improvised this twice, at nodes 147 and
> 140, flagging itself at `147.3` and `140.9`; the improvisation is now a rule. It
> survived measurement: across both runs, node 140's checker FAILed the work on a clause
> its own worker had pre-excused in the record and refused to read the human's *"so that
> the checker then passes"* as a verdict, and independently found the defect node 153
> was minted for; node 147's checker contradicted the condition's own author and
> established its two central clauses byte-wise. Six signs of preserved independence,
> none against.
>
> **Where it is written, and the human's ground.** Their words, `verbatim`: *"I would say
> add it to the rules in the map somewhere, not the skill at it is relevant only for
> this project"*. This is a **divergence**: the worker recommended the shipped
> `expedition-checker/SKILL.md` and the human declined it, on scope. Under [node
> 93](93-effort-scoped-custom-rules.md) map-only is the ordinary case, and the rule
> lives here and nowhere else.
>
> **Which map file, settled by the worker on the rules already written:**
> `map-implementation-rules.md`, under its existing `## What the work is held against`
> heading, beside the review route. It is the only map file the checker reads — [node
> 143](143-rules-arrive-by-the-spawn-never-by-a-search.md)'s landed contract sends it
> there by name — its declared readers are exactly an implementation node's worker and
> its checker, and `map.md`'s own stated principle keeps out what not every worker can
> act on. That section already carries checker-conduct rules, so a rule about how the
> checker reads the work is read there rather than skipped.
>
> **What the rule has to do is disambiguate, not override.** Node 143 landed two
> sentences that read, on a record node, as a directory ban: *"The implementation-rules
> file is the single exception, and only for the standards in it"*, and *"Read that file
> for its standards and read nothing else in the effort's directory … open no other file
> beside it."* Both sit inside `## The standards you hold the work against`, so both
> govern **the route by which standards reach the checker**. The changed paths reach it
> by a different route — given 3, *"The work — the paths that changed"* — which those
> sentences do not touch. A checker whose whole diff sits in the effort's directory
> cannot see that from the section it is reading, so this effort states it. **Nothing in
> the shipped contract is overridden**, which is why [node
> 28](28-spawn-overriding-a-contract.md) is not engaged and no licence is being spent.
>
> **The guard binds at check time rather than on the condition's writer.** The earlier
> attempt found three guards in force on both runs *by accident*: the condition excluded
> the node's own status line, `decisions.md` and `flags.md`; the checker took the paths
> from `git status --porcelain -uall`; and both conditions were answerable mechanically.
> Making the first a duty on whoever writes such a condition puts it in front of the
> wrong reader — a condition is written by a worker of any kind, and no worker but the
> implementer reads `map-implementation-rules.md`. So the rule states the exclusion
> itself: a change to the node's own status line, to `decisions.md` or to `flags.md` is
> bookkeeping reserved to the manager, and the checker `FAIL`s it wherever it appears in
> the work, whether or not the condition excluded it. That binds without a second
> reader, and it repairs **nodes 80 and 156**, which are open, edit record files, and
> name no such exclusion — node 156's deliverable being `decisions.md` itself.
>
> **What this does not reach.** Both measured runs were on conditions answerable by
> bytes, greps and counts. Neither asked a checker to judge whether newly-written record
> prose was *correct*, so nothing here is evidence about a semantic condition on a record
> node. And the ambiguity in the shipped sentence survives for any effort in another repo
> that has no such map rule — surfaced below rather than settled here, the human having
> decided the permission itself is this project's alone.

**What the worker reported its work invalidates, pasted as it wrote it.**

> none. My answer contradicts no resolved node.
>
> Three near misses the manager should have, none of which is a contradiction. **Node
> 143** is the node whose landed wording this reads against — its decision (the standards
> come from one known file) stands untouched, and what this effort adds is a reading of
> one sentence it shipped. **Node 36** is not contradicted: it refuses a condition that
> quantifies over the record, where this permits one that names bounded record paths.
> **Flags `147.3` and `140.9`** are endorsed rather than overturned; the manager's own
> note on my node file already corrects their framing, and nothing here disturbs that.
>
> One thing that is not an invalidation but is a live inconsistency in unresolved
> material: **nodes 80 and 156** are open implementation nodes on record files whose
> conditions do not exclude the node's own status line, `decisions.md` or `flags.md`. New
> node 1 above repairs them at check time without either condition being edited.

## Flags

*All three are the worker's own text, pasted. The ids and the links are the manager's bookkeeping and nothing else.
The round that produced them is `## Interview`, attempt 2.*

`163.1` `ASSUMPTION` — **which map file carries the rule.** The human said *"the rules in the map
somewhere"* and left the file open; the map is more than one file. I settled it as
`map-implementation-rules.md` rather than `map.md` or its ground-rules block, on three
things already written: it is the one map file node 143's contract sends the checker
to by name, its own first sentence declares its readers to be exactly an implementation
node's worker and its checker, and `map.md` states that it holds only what *every*
worker can act on. The ground-rules block was the other candidate and I refused it —
it is copied into every checker spawn on every node, so a rule needed by record nodes
only would be paid for by all of them, and node 42's test for that route is a standing
constraint on *the work*, which this is not.

`163.2` `ASSUMPTION` — **the shipped "open no other file beside it" reads as governing the
standards route only.** Node 143 landed that sentence inside `## The standards you hold
the work against`, while given 3 hands the checker the changed paths by a separate
route. I read the sentence as bounded by its section, which makes this effort's rule a
disambiguation rather than an override, and so keeps node 28's raise-per-departure out
of it. Read the other way — as a genuine ban on opening any file in the effort's
directory — the map could not lift it and every record node would owe a raise. I
believe the bounded reading and I have not put it to the human.

`163.3` `ASSUMPTION` — **the guard became a check-time rule instead of a duty on the condition's
writer.** My question to the human recommended requiring every writer of such a
condition to exclude the node's status line, `decisions.md` and `flags.md` in the
condition's own text. A condition is written by a worker of any kind, and none but the
implementer reads `map-implementation-rules.md`, so that duty would have landed in
front of nobody. I inverted it into a rule the checker enforces from the standards
regardless of what the condition says. The human endorsed the placement, not this
inversion.

## Interview

### Attempt 1 — dead

*Banked at hand-back, before being relayed: this question queues behind node 141's, which was live when it arrived.*

***The manager's note.*** **This attempt is dead, and its question was never relayed.** The manager session that
spawned it ended before the queue reached this node, and resumability dies with the manager's session — the boundary
recorded in `map.md`'s resume rule. So the human has said **nothing** on this node, and everything below is the
worker's own text with no answer under it.

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

### Attempt 2

*The attempt's routing key does not survive the manager's session, so it is not recorded here: a fresh manager thread
cannot resume this attempt and runs the replacement procedure instead.*

*Banked at hand-back: this question queued behind [node 167](167-the-checkers-bar-commands-route.md)'s, which was live
when it arrived, and then behind the manager's own raise on [node 144](144-make-the-rules-file-stand-alone.md)'s
checker. Relayed once both cleared.*

**The worker's question, pasted as it wrote it.**

> ```
> NODE:          An acceptance condition demands facts about files the checker is told it does not read (node 163)
>
> ABOUT:         Some of this effort's implementation nodes have the effort's own record as their
>                product — moving text between `map.md` and its siblings, repairing `decisions.md`.
>                Their checker is told it does not read the record. So the one thing it must open to
>                check the work is the one thing its contract forbids. This is being decided now
>                because node 143 landed two hours' worth of new wording that turned that tension into
>                a flat contradiction, and because a node in exactly this shape is claimed right now.
>
> SO FAR:        **What the earlier, dead attempt on this node established, which I have re-checked and
>                kept.** The manager has already improvised this permission twice on its own authority
>                — once at node 147, once at node 140 — instructing the checker to read the changed
>                graph files as *the work under check* and to take no statement of intent from them,
>                and flagging itself both times (`147.3`, `140.9`). Both flags were settled at their
>                gates. That attempt then measured whether the improvisation actually blinded anything,
>                across both runs: six independent signs that it did not, none that it did. Node 140's
>                checker FAILed the work on a clause its own worker had pre-excused in the record — the
>                excuse was sitting there and it did not pick it up; on the re-run it refused to read
>                the human's "so that the checker then passes" as a verdict; it independently found the
>                defect node 153 was later minted for. Node 147's checker handed back a finding that
>                contradicted the condition's own author. So on the evidence the permission is safe.
>                Three guards were in force both times — the condition excluded the node's own status
>                line, `decisions.md` and `flags.md`; the checker took the changed paths from `git
>                status` rather than from the record; and both conditions were answerable by bytes,
>                greps and counts rather than by reading for meaning. That attempt noted those guards
>                held **by accident, not by rule**, and that the evidence reaches no further than
>                mechanically-answerable conditions.
>
>                **What has changed since, and it changes the answer.** That attempt's central finding
>                was that the blindfold was "against a second statement of intent, not against a
>                directory" — the contract said *there is a record behind this work, you do not read
>                it*, and separately named `map.md` as a standard every checker already reads, so
>                reading a graph file was never actually banned. **Commit `7b5bcf0` (node 143) landed
>                after that attempt handed back and made it a directory ban.** The shipped checker
>                contract now says, in new text: *"You do not read it, and you do not go looking for
>                it. The implementation-rules file is the single exception, and only for the standards
>                in it"*, and *"Read that file for its standards and read nothing else in the effort's
>                directory … open no other file beside it."* Meanwhile the same file still hands the
>                checker, as given 3, *"The work — the paths that changed."* On a record node every one
>                of those paths sits in the effort's directory. The contradiction is now **inside one
>                shipped file**, between given 3 and the standards section, rather than between a
>                contract and a manager's habit.
>
>                **Which kills the earlier attempt's own recommendation.** It wanted the permission
>                written into this effort's `map-implementation-rules.md`. Post-143 that placement
>                fails twice over: the checker is told to read that file *for its standards* and to
>                "leave the rest of that file unread", and a permission about what the checker may open
>                is not a standard the work is held against — so the one reader it binds is instructed
>                to skip it. And an effort's map file cannot countermand a sentence in a shipped
>                contract; node 93 says a rule reaches a shipped file only where you say so.
>
>                **How much this bites, measured just now.** Seven open or claimed implementation nodes
>                have record files as their work: 80, 88, 144, 149, 152, 156, 160. **Node 144 is
>                claimed and running**, and its condition names only files inside
>                `.scratch/graph-workflow/` — its checker, under the contract as it now stands, is
>                handed a set of paths it is told not to open. Of those seven, **two do not carry the
>                guard the earlier attempt found holding by luck**: node 80 and node 156 never exclude
>                the node's own status line, `decisions.md` or `flags.md` by name, relying only on a
>                catch-all "no other file changes". Node 156's deliverable *is* `decisions.md`.
>
>                **One thing I have not settled and am not asking you to.** Node 164 is open, is an
>                implementation node on `.claude/skills/expedition-checker/SKILL.md`, and its condition
>                edits the same section — what a path handed to the checker as a *standard* may hold.
>                If your answer sends work at that file, that work and node 164 collide on the same
>                heading, and I will report the sequencing on my handover rather than guess it here.
>
> ASK:           Should this permission stop being an improvisation and be written down — and be
>                written into the **shipped** checker contract `.claude/skills/expedition-checker/SKILL.md`,
>                rather than into this effort's `map-implementation-rules.md`?
>
> RECOMMENDED:   Yes, and into the shipped contract. Three things, about fifteen lines.
>
>                **(1) State the blindfold by what it guards, not by a directory.** The checker is
>                blind to *statements of intent and decision* — node files, `decisions.md`, `flags.md`
>                — and it reads whatever it was handed as a changed path as **the work**, whatever
>                directory that path sits in, saying so in its outcome. That is one sentence, and it
>                repairs the given-3-versus-standards-section contradiction where the contradiction
>                actually lives.
>
>                **(2) Put it in the shipped file, not the map sibling.** The contradiction is between
>                two sentences of one shipped file, so only that file can resolve it; the map sibling
>                is a file the checker is explicitly told to read selectively and leave the rest of
>                unread; and the next effort, in another repo, gets a record-editing node with no
>                `map-implementation-rules.md` at all and no permission anywhere. This is the option
>                the earlier attempt wanted and set aside for one reason only — node 143 was claimed on
>                that exact file and it refused to collide. 143 has landed. That reason is gone.
>
>                **(3) Make the accidental guard a written duty on whoever writes such a condition.**
>                A condition whose work is the record must exclude, *in the condition's own text*, the
>                node's own status line, `decisions.md` and `flags.md` from what the worker may edit —
>                so the checker can see the guard instead of trusting a manager instruction it cannot
>                read. This is the part I would not have recommended on the earlier attempt's evidence
>                and do recommend on today's: the guard is already missing from two of the seven live
>                nodes.
>
>                What this rests on: measurement rather than argument — two runs, six independence
>                checks, none failed; node 28's rule that an improvised departure owes both a licence
>                and a node for the permanent fix, this having had two licences and, until now, no
>                node; and node 93, which makes the shipped-file destination yours to grant and not the
>                manager's to take.
>
> ALTERNATIVES:  Write it into `map-implementation-rules.md` instead — the earlier attempt's own pick,
>                and cheaper, but the checker is told to read that file only for standards and leave
>                the rest unread, and it cannot override a sentence in the shipped contract.
>
>                Leave it as a per-node manager instruction, flagged each time — cheapest today, but
>                post-143 the instruction now contradicts shipped text rather than merely going beyond
>                it, which under node 28 makes it a raise every single time rather than a judgement the
>                manager may make; and it re-improvises on every one of the seven live record nodes.
>
>                No checker at all on a record-editing node: it goes straight to your gate and your
>                diff read is the check — honest to the contract as written, and it drops the second
>                pair of eyes on exactly the nodes that rewrite the effort's own rules.
>
>                Narrow the permission to conditions answerable without reading for meaning — this is
>                what the evidence actually covers and nothing more, but nothing today separates a
>                structural clause from a semantic one, so it needs a test I cannot write.
>
>                Answer the node's first question the other way: an acceptance condition may **not**
>                demand a change to the effort's record at all. This is the "no" that unwinds the most
>                — nodes 140 and 147 have already landed this way, and seven open nodes are shaped
>                like it — so I do not recommend it, but it is the question the node asks first and it
>                is yours to say.
> ```

**The human's reply, `verbatim`. `DIVERGENCE`.**

> I would say add it to the rules in the map somewhere, not the skill at it is relevant only for this project

**The option it takes**, quoted from the worker's own `ALTERNATIVES` and attributed to the worker:

> Write it into `map-implementation-rules.md` instead — the earlier attempt's own pick,
> and cheaper, but the checker is told to read that file only for standards and leave
> the rest unread, and it cannot override a sentence in the shipped contract.

***The manager's note.*** **Marked a divergence because it contradicts the worker's `RECOMMENDED`**, which was the
shipped contract and which argued that placement in the map fails twice over. Without the mark the worker would read
a bare answer as agreement and resolve as though it had won its point. The reply's *"somewhere"* leaves the placement
inside the map open; the manager has not narrowed it, and it is the worker's to work out or to put back.

## Retrospective

*Attempt 2's, pasted as it wrote it. Filed by the manager as an annotation; this effort asks every worker for one,
and the worker's own contract forbids it to write a graph file.*

**(1) What I had to hunt for.** Three things. *Whether node 143's landing changed the text the previous attempt's findings were measured against* — found with `git show 7b5bcf0` on the checker skill. I looked first at the current `SKILL.md`, which showed me the new sentences but could not tell me they were new; only the diff established that attempt 1 could not have seen them, which is the fact the whole node turned on. *The live blast radius* — which open implementation nodes edit record files. Nothing indexes that; I had a subagent read every node file. *Whether `map-implementation-rules.md` already carries checker-conduct rules*, which is what made the human's placement workable after I had argued against it — found in that file's review-route paragraph. I looked first at the checker contract, which describes the file abstractly and never says what a real one contains.

**(2) What arrived that this node did not need.** The spawn's line that the effort declares no label vocabulary "so it is unscoped" bore on nothing — I wrote one index line and grouping never arose. `decisions.md` is a mandatory whole read and I used about six of its ninety-odd entries; it has no headings and no grouping, so there is no way to read only the part bearing on the checker. Even a subject grouping would have let me read a fifth of it. In `map.md` I used the ground rules, standing rules 2 and 4, the never-delete rule, the retrospective item and node 93; the worktree and sandbox material, the token-cost items, the resume rule, the dogfood material and `## Destination` bore on nothing — and `## Notes` is one flat list of very long items with no sub-headings, so the map's own standing rule 3 ("a long answer is navigable by heading") is not met by the map's biggest section. In `map-implementation-rules.md` I went for one thing, what the standards section holds, and took a file whose majority is `## Landing an implementation node's work` — worktrees, rebases, sandbox mounts, all irrelevant here; a spawn pointer to `## What the work is held against` would have avoided it. I read the whole implementation contract to check its graph-file ban and its standards section; its raise, flag and gate machinery bore on nothing. I read node 164's full nine-clause condition when I needed only the two sentences saying it does not overlap with mine.

**(3) What would have made this easier.** *In the spawn:* the manager's note said node 143 had landed and framed that as removing a **collision** on a file. Its real effect was to **falsify the previous attempt's central finding** — that the blindfold was "against a second statement of intent, not a directory". A note that says what a landing changed in the text this node reasons about is worth much more than one saying a file is now free. *In the node file:* attempt 1's banked block is presented as durable measurement with no marker of when it was measured. A banked block from a dead attempt should carry the commit or date it was taken at, so the next attempt knows what to re-verify rather than having to suspect all of it. *In the record:* there is no index of the open frontier. `decisions.md` indexes what is resolved; nothing indexes what is open, so "how many live nodes does this bite" costs a read of the whole nodes directory — and that question is asked by every node whose subject is a rule. *In the contract:* the "If you are a replacement attempt" section says every question answered in the earlier record is a settled fact. Attempt 1 had no answered questions, only unverified findings, and the contract says nothing about how far to trust a dead attempt's *measurements*. One line distinguishing a settled answer from a banked finding would have told me directly what I spent the first third of this node working out.

**(4) Stale, wrong, or contradictory.** Attempt 1's headline finding — "the blindfold is already narrower than it reads … not against a directory" — was true when written and is **false of the shipped text today**; node 143 made it a directory ban, and it sits on the node file unqualified. The node file's manager note asserts that 163 and 164 "do not overlap"; that was contingent on an answer nobody had — while my recommendation stood they would have collided on the same heading of the same file, and it is the human's answer that made the note true. Inside the shipped checker contract, given 3 ("the paths that changed") and "open no other file beside it" contradict each other on a record node; that is this node's whole subject, but it is a live contradiction in a shipped file right now. And `map-implementation-rules.md` warns that a paragraph saying *below* may point into `map.md`, then does exactly that in its review-route paragraph — "the human's standing direction below" resolves nowhere in the file node 143 now sends the checker to. I checked before surfacing it: node 144 is claimed and is that repair, so I raised no node for it.
