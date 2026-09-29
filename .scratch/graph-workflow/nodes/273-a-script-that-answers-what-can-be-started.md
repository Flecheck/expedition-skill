# A script that answers what can be started

Type: grilling
Status: resolved

Blocked by: none

## Question

*The human's own, `verbatim`, on 2026-09-19:*

> We might want to create a script that answer what can be started so that it is easy for the manager.

**What prompted it, and the manager is the one who failed rather than the graph.** In the turn before, the manager
reported *"nothing is waiting on you"* while **two slots were free and two nodes were claimable** — node 271, whose
blocker had just been satisfied by node 269 landing, and node 95, whose blocker turned out to have been resolved
long ago. Neither fact was hard to establish; both required the manager to notice that an edge had been satisfied by
something that happened elsewhere.

## The manager's note at filing

*Not a change to anything above. None of it is an answer.*

**What the frontier costs to compute today, from the manager's own experience rather than measured.** It is the set
of nodes that are `open`, unblocked and unclaimed. Three of those are cheap — status and `Blocked by:` are declared
lines in each node file. **The expensive part is none of them**: it is knowing which *file collisions* make a
claimable node unclaimable in practice. Node 271 and node 268 both edit `map-history.md`, and nothing on either node
says so; the manager holds that sequencing in its head and writes it into notes at filing. **A script reading the
declared fields would have reported both as startable.**

**So the question is not only whether to build one but what it can honestly answer.** A script can compute status,
edges and claims. It cannot compute a collision that lives only in two acceptance conditions naming the same path —
unless the conditions' file lists become machine-readable, which is a change to the node format and a different
question again.

**Adjacent and deliberately not merged: [node 270](270-whether-the-worktree-lifecycle-is-worth-a-script.md)**, the
human's other script proposal, for the worktree lifecycle. **Both run into the same wall and it is ground rule 1**:
*"Nothing in the shipped files may assume this repo, this machine, or a toolchain."* This effort has never shipped
an executable, and a script is a toolchain assumption in a way documented commands are not. The manager has not
merged them because they automate different things and one may be worth it while the other is not — **but whoever
works either should know the other exists**, and the underlying question *does this effort ship executables at all*
is common to both and is settled by neither.

**One thing the manager would rather have decided than guess**: whether such a script is for the manager's own use
during an effort, in which case it may assume this repo freely, or is a shipped artifact of the workflow, in which
case ground rule 1 binds it. Those are very different objects and the human's sentence does not choose.

## Interview

### Attempt 1 — the question put to the human

*Pasted as the worker wrote it. Banked here so that a death leaves the worker's work on disk. **The worker built the
script to find out what it costs**, and its measurements are the substance of the payload.*

**ABOUT:** Node 273 decides whether to build a script that computes what the manager can start next, and what such a
script honestly answers. It is live because the manager has now reported *"nothing is waiting on you"* three times
in one session while slots sat empty and work was startable.

**SO FAR:** I read the node, `map.md` whole, `graph-conventions.md`'s `## Statuses`, `## Edges` and `## Reading the
graph`, `SKILL.md`'s `### Picking the next node` and `## What is in front of the human, and when`, node 05 (which
chose markdown over a CLI), node 213, node 65, and node 270. **Then I stopped reading and measured**, because most
of what this turns on is a fact rather than a preference.

**I built the script, to find out what it costs.** Two shell commands, about twenty lines of awk and python, roughly
a minute. It reads each node file's header, computes `open` + every `Blocked by:` target `resolved` + not `claimed`,
and prints the result. **It works.**

**What it says right now.** The frontier is **123 startable nodes: 34 grilling, 86 implementation, 3 other.** The
settings are 2 grilling slots and 2 code slots. **So the manager has been running at roughly one grilling slot out
of two while 34 grilling nodes were available to start.**

**It catches the exact misses that prompted this node.** Node 271 reads `Blocked by: [node 269]`, node 269 is
resolved, and the script reports 271 as startable. Node 95 was the same shape. **Neither needed judgement — only a
lookup nothing was performing.**

**Four things I established that change the question as it was filed:**

1. **The duty already exists and is already shipped.** `expedition-triggers.md` says *"A node finishes, so the
   frontier is looked at"*; `SKILL.md` says *"A count is a target to reach rather than a ceiling… you start enough
   work to fill every gap it leaves"*. **Nothing is missing from the rules. What is missing is a way to perform
   them.**
2. **By hand it is not performable.** The graph is **282 node files, 4.87 MB** — well over a million tokens. The
   manager's context is budgeted at 100k and measured at 200k. **Computing this frontier by reading was never
   possible; it was being done from memory, which is why it failed.**
3. **"A slot emptied and nothing was started in it" is the same read.** Counting `claimed` nodes by kind against the
   map's counts is three more lines. I treated this as inside the question rather than an extension of it — nothing
   can be started when no slot is free.
4. **The collision problem the manager called "the hard part" does not touch the half that failed.** A script cannot
   see that two nodes edit the same file. **But a grilling worker writes no file at all, so two grilling nodes can
   never collide — and the grilling slots are what sat empty.** Collisions bite only implementation pairs competing
   for the 2 code slots, where the manager filters a list it now at least has.

**Settled on my own authority** (returned as flags): the script reports counts, slot occupancy and the list grouped
by kind, and does **not** rank or choose — the failure was never a bad pick, it was *"nothing is waiting"*; and it
does **not** bundle the ten mechanical checks, because node 213 already decided those run as each procedure's last
step over the material that act touched.

**On node 270, which I was told to judge rather than merge.** They can be decided separately, and ground rule 1
lands differently on each. **My script reads only the workflow's own markdown, in a format the workflow itself
creates on every effort** — stack-independent by construction, never touching the target project. **Node 270's
script drives `git` against the target repository**, which is where *"assume this repo, this machine, or a
toolchain"* actually bites. **A yes here does not carry a yes there.**

**ASK:** Is this script worth building — and if so, is it **for the manager's own use on this effort**, or a
**shipped part of the workflow** that travels to every effort?

**RECOMMENDED:** **Build it, and ship it** — as a small bundled script beside the skill files, written in POSIX
shell and awk so it needs no interpreter beyond what any machine running an agent already has.

- **Node 05 already authorised exactly this, and named the trigger.** The human's own decision there chose markdown
  over a CLI, but wrote the exception in: *"if a dogfood run shows the manager losing track of statuses, edges or
  the write lock, extract a **read-only** `check`/`frontier` command first — it needs only edges and statuses
  (settled) and bakes in no revision policy (unsettled)."* **That trigger has fired three times this session.** The
  reason it was deferred — unsettled revision semantics — has since gone away, and node 05's own later annotation
  says the extraction *"no longer needs designing"*.
- **Ground rule 1 does not reach it.** Its own second sentence, and `map.md`'s statement of it — *"works on an
  unknown stack"* — are about the **target project's** stack. This script reads the graph's own markdown and nothing
  else. **There is no unknown stack for it to fail on.**
- **The map already anticipates this.** Its Domain line says the artifact is *"skill files (markdown), possibly with
  bundled `scripts/`"*. **Shipping one is a thing this effort left open, not one it decided against.**
- **It costs no context until run.** Node 05 established that bundled scripts *"execute without loading"* — zero
  shipped cost until the manager runs it, then about forty lines of output in place of 4.87 MB of files.
- **Manager-only fixes this session and ships the defect.** Every effort will have the same format and the same
  growth curve. **This effort's subject *is* the workflow; a fix kept in `.scratch/` is the one place it helps
  least.**
- **Shipping it also part-settles node 65**, which is open, in the frontier, and raises the same ground rule 1 fork.

**ALTERNATIVES:**

- **Build nothing; tighten the discipline instead.** Set aside because the discipline is already written in two
  shipped files and **failed three times anyway**, and because at 282 files and 4.87 MB there is no hand route to
  tighten.
- **Build it, manager-only, in `.scratch/graph-workflow/`.** The safe answer, and it keeps the effort's
  no-executables record intact. **A real option if you would rather prove it on this effort before committing the
  workflow to shipping executables at all.**
- **Build the full `check`/`frontier` command node 05 named**, mechanical checks included. Set aside because node
  213 relocated those checks into the procedures that can falsify them.
- **Wait until node collisions are machine-readable.** Set aside as a much larger question that would hold the
  frontier computation hostage, when 34 grilling nodes are startable today and cannot collide with anything.

#### The human's answer

*Their reply on 2026-09-23, `verbatim`:*

> 3 ok

— the third of four given in one message.

**The option it takes**, quoted so the reply is attributable to exactly one thing. It is **the worker's
`RECOMMENDED`**, written by the worker and not by the manager:

> **Build it, and ship it** — as a small bundled script beside the skill files, written in POSIX shell and awk so it
> needs no interpreter beyond what any machine running an agent already has. … Node 05 already authorised exactly
> this and named the trigger … Ground rule 1 does not reach it … The map already anticipates this … It costs no
> context until run … Manager-only fixes this session and ships the defect.

**No divergence**: the answer agrees with the recommendation.

***The manager's own note, beside their words and not part of them.*** It did not ask which option the reply pointed
at, on the same ground as at nodes 252, 263, 264 and 265: **only one of the five is an assent**, and each
`ALTERNATIVE` is a named refusal of it.

**This is the first executable this effort has agreed to ship**, and the manager notes it as a threshold rather than
a detail: every ground rule and every standing preference on this effort was written for markdown deliverables.
**The worker's argument for why ground rule 1 does not reach it is the load-bearing part of the answer**, and
whoever writes the implementation node's condition should carry that argument rather than re-derive it.

**The session was ending when this was answered.** Under the manager's own stop procedure it claims nothing new and
spawns no worker for a node not already under way — **so this node's worker was resumed to write the answer, and no
worker was spawned for the script itself.** The node files it surfaced **are** minted, filing a handover being
carry-through rather than starting work.

## Answer

*Written by this node's worker and pasted as it wrote it.*

> **Build it, and ship it.** A small read-only script travels with the skill files, written in POSIX shell and awk.
> The human's assent, `verbatim`: *"3 ok"*, taking the recommendation whole.
>
> ### What it computes
>
> Three things from one read of the graph's own node files:
>
> 1. **How many nodes of each kind are `claimed`**, shown against the effort's counts. This is the *"a slot emptied
>    and nothing was started in it"* question, and it is **the same read as the frontier rather than a separate
>    job** — nothing can be started when no slot is free.
> 2. **The frontier** — every node `open`, unclaimed, and whose every `Blocked by:` target is `resolved` — as a
>    total and a count per kind.
> 3. **The frontier itself**, grouped by kind. **It ranks nothing.** The failure this answers was never a bad pick;
>    it was the manager reporting that nothing was waiting.
>
> It carries **no** consistency check. Node 05 named the extraction as a single *"read-only `check` / `frontier`
> command"*, but [node 213](213-nothing-triggers-the-ten-mechanical-checks.md) has since relocated those checks into
> the procedures that can falsify them. **Bundling them here would rebuild a thing that was deliberately taken
> apart.** Only the frontier half is taken.
>
> ### Why ground rule 1 does not reach it, which is the load-bearing part
>
> This is the first executable this effort ships, and every ground rule on it was written for markdown. The rule
> reads: *"Nothing in the shipped files may assume this repo, this machine, or a toolchain."* Its statement in the
> map names what it guards: *"works on an unknown stack"*.
>
> **The unknown stack is the host project's** — its build, its tests, its lint, the commands the bar is discovered
> against. **This script never touches the host project.** Its entire input is the expedition's own graph directory,
> in a format `graph-conventions.md` fixes and which the workflow itself creates on every effort, in every
> repository, whatever that repository is built with. **There is no stack for it to fail on, because it never reads
> one.** A script that ran `npm` or `cargo` or the project's tests would be squarely inside the rule; this one is a
> reader of the workflow's own artifact.
>
> **What it does assume is a POSIX shell and awk**, which is why the language was chosen. **That is the same
> assumption the landing policy already makes** when it tells the manager to run `git worktree add`, and the same
> one the harness makes by giving every agent a shell.
>
> Two further grounds, both already in the record: **the map already permits it** — its Domain line says the
> artifact is *"skill files (markdown), possibly with bundled `scripts/`"*, so shipping one is a thing this effort
> left open rather than decided against; and **it costs no context until it runs**, node 05 having established that
> bundled scripts *"execute without loading"*.
>
> ### Why it was built now: node 05's trigger has fired
>
> [Node 05](05-graph-state-mechanism.md) chose markdown over a CLI and wrote the exception into its own answer:
> *"if a dogfood run shows the manager losing track of statuses, edges or the write lock, extract a read-only
> `check` / `frontier` command first."* **That trigger has fired** — three times in one session — and the reason it
> was deferred is also gone, node 05's own annotation recording that the command *"no longer needs designing"*.
>
> **The duty was never missing.** The triggers file already says the frontier is looked at when a node finishes, and
> `SKILL.md` already says *"A count is a target to reach rather than a ceiling to stay under."* **What was missing
> was any means of performing them.** The manager was computing the frontier from memory because the only
> alternative was reading the graph, and the graph had outgrown a manager's context.
>
> ### What it cannot answer, stated here rather than left to be discovered
>
> **It cannot see a file collision.** `graph-conventions.md`'s `## Edges` is explicit: *"no field records which code
> a node touches."* Two startable nodes may both edit the same file — node 271 and node 268 both edited
> `map-history.md`, and nothing on either node said so.
>
> - **It does not bite the grilling half at all.** A grilling worker writes no file, so two grilling nodes can never
>   collide. **For the grilling slots the script's answer is complete, and the grilling slots are what sat empty.**
> - **It bites the implementation half**, where the list is a correct set of *candidates* and the manager still
>   applies the collision filter before filling a second code slot.
>
> ### Which claims depend on the size of the graph, and which on its shape
>
> **Shape, true at any size** — the duty exists with no means of performance; the frontier is computable from
> declared fields with no judgement; slot occupancy is the same read; no field records which files a node touches;
> a grilling worker writes no file; the script reads only the workflow's own markdown; and **`Blocked by:` is
> prose-shaped in practice**, the never-delete rule striking a satisfied blocker in place rather than removing it.
>
> **Magnitude, measured 2026-09-22 and true only then** — 282 node files, 4.87 MB; 123 startable, 34 grilling, 86
> implementation, 3 other, against settings of 2 and 2.
>
> **The threshold between them, which is the durable form:** the by-hand route fails once the graph exceeds what
> fits in a manager's context. **It is not that 282 files is too many; it is that reading the graph stopped being an
> available act at some point before 282, and nothing reported when.**
>
> ### What this settles of node 65, and what is left of it
>
> **Settled:** node 65's first item — whether the cheap route belongs in the shipped files at all, given ground rule
> 1. It does, on the reasoning above. **That precedent is set and node 65 need not re-litigate it.**
>
> **Left open, and node 65 stays open holding it:** its subject is wider — *what the graph holds* rather than *what
> can be started*; its item 4, whether a worker's route is a script or the manager stating graph facts in the spawn;
> its item 2, which shipped file tells a worker; and its item 3, whether the map should stop making statements the
> node files already answer.

**The index line the worker wrote:**

> A read-only frontier script ships with the skill files in POSIX shell and awk: ground rule 1 guards the host
> project's stack, and this reads only the expedition's own markdown.

## Flags

*All three are the worker's own text, pasted.*

`273.1` `ASSUMPTION` **· settled** — **Slot occupancy was read as inside the question rather than as an extension of it.** The
manager's spawn treated *"a slot emptied and nothing was started in it"* as a different question and asked that
coverage be established rather than assumed. **I settled it myself rather than spending a payload on it**: nothing
can be started when no slot is free, and it is three lines on the same read. I also set the default when no counts
are passed to 2 and 2, matching `SKILL.md`'s stated default, **so the script bakes in nothing of this effort's own
settings.**

`273.2` `ASSUMPTION` **· settled** — **The script ranks nothing and carries no consistency check.** Two scope choices made rather
than asked. It does not order the frontier beyond grouping by kind, the failure being *"nothing is waiting on you"*
rather than a bad pick, and ground rule 4 preferring simple prose over machinery for predicted needs. It carries
none of the ten mechanical checks, on node 213's ground.

`273.3` `ASSUMPTION` **· settled** — **Node 270 was judged separable and only this node was answered.** They can be decided apart:
**ground rule 1 lands differently on each.** This script reads only the expedition's own markdown; node 270's drives
git against the host repository, makes worktrees in it and deletes branches from it. **So the common question —
does this effort ship executables at all — is answered yes here without carrying a yes there.**

## Invalidations

*The worker's own text, pasted.*

> **Node 05 states twice that the extraction trigger has not fired, and this answer is that it has.** Its annotation
> says *"the trigger still has not fired"* and it closes *"the extraction trigger, which has still not fired."*
> **Both statements are now false.** What node 05 decided is untouched and was never contradicted — **it provided
> for this case in its own text** — but the two statements about the trigger's state need the strike-in-place
> treatment, recording that the trigger fired on 2026-09-22 and what fired it.
>
> **Node 05 names the extraction as one command and only half of it is taken.** Node 213 has since relocated the
> check half. Node 05's phrasing, and `decisions.md`'s index line for it, **both still describe a single command
> that will not be built as one.**

## Retrospective

*The worker's own text, pasted.*

> **1. What I had to hunt for.** **The frontier itself — the one fact this node is about — exists in no file.** I
> looked in `map.md` first; it holds the two slot settings and **no graph state at all**. Computing it from the node
> headers took one command. **That is precisely node 65's finding from node 59's retrospective, reported months of
> nodes ago and still unfixed.** **Ground rule 1's verbatim text** — the spawn quoted it twice and the node file
> quotes it, but `map.md` only *points* at the rules file, and **the whole answer turns on its second sentence,
> which neither copy quoted.** **Node 213's answer** — found only while checking whether the ten mechanical checks
> were still a whole-graph thing. **That fact decides the script's scope. Nothing pointed me at it.**
>
> **2. What arrived that this node did not need.** `map.md` whole, 115 lines, for four things. **I am the tenth
> worker to report this, and the repetition is now the datum rather than the finding.** The split that would
> actually pay here is **preference-from-account**, not worker-from-manager — which is adjacent to node 246 but not
> the same cut. `SKILL.md` lines 500–610: 110 read, ~15 used; the spawn named the right two headings, the sections
> are simply long.
>
> **3. What would have made this node easier.** **The spawn named node 05's trigger and did not name node 213
> beside it**, and that single fact decided the script's scope — I found it by accident. **The spawn did not mention
> node 65 at all**: it is open, in the frontier, raises the identical ground rule 1 fork, and **its own text already
> proposes the way through.** I found it while scanning a status table for another purpose. **Two open grilling
> nodes asking the same sub-question, neither linked to the other, is the shape a frontier script does not fix and a
> collision-aware one would not either.**
>
> **What made this node easy, and it was decisive: I stopped reading and measured.** Two shell commands gave me the
> frontier, the file count, the byte count, and **a working proof that the script parses the real `Blocked by:`
> forms correctly.** Every strong claim came from those rather than from a file. **The spawn explicitly invited this
> — *"treat anything shaped like an assertion about your answer as untested, and test it"* — and it was the single
> highest-return instruction in it.**
>
> **4. What was stale, wrong, or contradicted something else.** Node 05's two trigger statements. **`## Edges`
> states `Blocked by: NN, NN`; thirty-two open nodes' fields do not look like that** — markdown links,
> struck-through numbers, prose clauses, commit hashes in code spans. The document is not wrong about the canonical
> form; **it does not describe what a scanner will meet**, and its `## Reading the graph` already carries two rules
> for exactly this hazard class. **A soft one:** node 270's filing note and this node's both say *"this effort has
> never shipped an executable"*, while `map.md`'s Domain line has always said *"possibly with bundled `scripts/`"*.
> Both true, but together they **framed ground rule 1 as a harder wall than it is** — and **it took a measurement to
> see past a framing two node files shared.**

## The manager's disposal

*Not the worker's text.*

- **Both surfaced nodes minted**: [node 285](285-ship-the-frontier-script-and-say-what-it-cannot-answer.md) and
  [node 286](286-reading-the-graph-does-not-describe-the-blocked-by-field-a-scanner-meets.md), each carrying its
  author's own condition verbatim.
- **Node 05's two false trigger statements** → **the manager's bookkeeping and not done.** They need strike-in-place
  on a resolved node, and `decisions.md`'s node 05 line needs the same. **Recorded as owed**; the session is ending
  and the manager is not making record edits in its closing turn that a fresh manager cannot see are owed. **They
  are named in the closing report.**
- **The spawn naming node 05 without node 213** → the manager's, and it cost the worker its scope decision by
  accident. **Named.**
- **The spawn not mentioning node 65** → the manager's, and **the worker found it by scanning a table for another
  purpose.** Node 65 is open, in the frontier, and now partly answered by a resolved node — **the shape this effort
  has repaired four times this week.** Named in the closing report as outstanding.
- **`map.md`'s `## Notes`, tenth report**, with a sharper cut than node 246's: **preference from account.** Named.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
