# The checker's bar-commands route, left asymmetric by node 143's amendment

Type: grilling
Status: resolved

Blocked by: none

## Question

*Surfaced by [node 143](143-rules-arrive-by-the-spawn-never-by-a-search.md)'s checker, alongside its `PASS`, and
pasted as it wrote it.*

> The bar's commands are now routed **asymmetrically** between the two agents, and this is a consequence of the
> amendment's scope rather than the worker's choice. The implementer reads them from `map-implementation-rules.md`;
> the checker's given 2 still says *"Where you are given properties and no commands, discover the commands from the
> repo"*, so the checker gets them by spawn or by its own discovery. The checker's own new section asserts *"It is
> the same file the implementer works from, so the two of you hold the work to one set of rules rather than two"* —
> true now for the standards, not for the bar's commands, which can drift between the spawn copy and the file. The
> wording of given 2 is the condition's own territory (the amendment named only the standards for the checker), so
> departing from it was not the worker's to do. **Should the checker's bar-commands route follow the standards into
> the same file?**

## The manager's note at filing

*Not a change to anything above.*

**It was in node 143's gate payload and the human approved without answering it.** That is their choice rather than
an omission, and the manager records the question rather than reading approval as an answer to it.

**A second thing the same payload carried and the human did not answer**: the checker's reading of clause 5, which
under the amendment denotes nothing on its literal wording. That one is spent — node 143 has resolved — and is
recorded on its gate rather than here.

## Answer

*Pasted as the worker wrote it.*

> **No route change. The repo's own instructions are the common source, and what gets repaired is a
> leftover feed route and one sentence that overclaims.**
>
> **The human reframed the question before answering it**, `verbatim`: *"I kinda expect that the build
> instruction are in the CLAUDE.md of the project so they should already have the information in their
> context ?"* — and then assented to the recommendation built on it, `verbatim`: *"ok"*.
>
> **The reframing was checked rather than taken on trust, and it holds.** Three facts:
>
> 1. **The dogfood target states its bar's commands in its own agent-instruction file.** Lang's
>    `CLAUDE.md`: *"No custom build/test scripts exist — use plain `cargo build` / `cargo run --
>    <file>.lang`. Lint with `cargo clippy`."* [Done-ness and termination](10-done-ness.md) already
>    recorded that Lang's bar was read partly off that file; no rule generalised it.
> 2. **The mechanism reaches a worker.** A subagent does receive the project's instruction block —
>    this node's own worker received one in its spawn.
> 3. **This repo has no such file at all**, and no build, no tests and no formatter. So on this effort
>    there are no commands to route and the asymmetry is inert here, rather than harmful.
>
> **So the drift argument for moving the checker's commands into `map-implementation-rules.md` fails,
> and that option was withdrawn by its own proposer.** The common source is the project's own live
> statement of how it is built. The rules file's record is a *copy* of a discovery, and copies go
> stale — a failure mode this record has already met once, an external standard having moved under a
> resolved node within the hour of it resolving. Routing the checker to the copy as well would have
> doubled down on the stale thing.
>
> **What the checker's contract already says is therefore right**: discover the commands from the
> repo. Two things around it are not.
>
> - **Given 2 still offers a spawn route** — *"either its commands for this repo, or the properties
>   alone… Where you are given properties and no commands, discover the commands from the repo."*
>   That is manager-typed text bearing on a check, and it is the one route that can drift from
>   anything the repo itself says. It also contradicts what the human settled at [node
>   143](143-rules-arrive-by-the-spawn-never-by-a-search.md)'s gate: nothing is fed.
> - **The contract overclaims what the two agents share** — *"It is the same file the implementer
>   works from, so the two of you hold the work to one set of rules rather than two."* True of the
>   standards, false of the bar's commands however they are routed.
>
> Both repairs are in `.claude/skills/expedition-checker/SKILL.md` and nowhere else. **They touch no
> file [node 144](144-make-the-rules-file-stand-alone.md)'s worker is holding**, that node's condition
> being confined to `map.md` and the rules file.
>
> **Where the wording names the repo's own instructions, it names them by role and never by filename.**
> `CLAUDE.md` is a convention of one harness; ground rule 1 forbids a shipped contract assuming it.
> This is the same constraint the manager applied at node 143 to naming this effort's directory
> literally.
>
> **What this answer does not close.** The asymmetry survives in one narrowed case, and it is the case
> the human was offered and did not take. The implementer is told to *"use whatever
> `map-implementation-rules.md` records for this repo"* and to discover only where it records none; the
> checker discovers from the repo. On a repo whose rules file records commands **and** whose own
> instructions state different ones, the two agents run different commands. Reported as a node below
> rather than folded in here.

**What the worker reported its work invalidates, pasted as it wrote it.**

> **No resolved node is contradicted.** One needs saying anyway: the repair edits text [node
> 143](143-rules-arrive-by-the-spawn-never-by-a-search.md) landed as commit `7b5bcf0`, whose answer
> records *"Items 1 to 5 are the original five at their original numbers — nothing about the spawn
> changed."* After this repair, something about the spawn has changed. That is not a contradiction of
> node 143's decision, which was about the standards and left given 2 explicitly outside its amendment's
> scope — this node exists because it did — but a reader comparing the two will meet it, and node 143's
> answer is not amended by this node's resolution.

## Flags

*All three are the worker's own text, pasted. The ids and the links are the manager's bookkeeping and nothing else.
The round that produced them is `## Interview`, attempt 1.*

`167.1` `ASSUMPTION` **· settled** — **I fixed that the repair names the repo's own instruction file by role and never as
`CLAUDE.md`, and the human's `ok` covered a recommendation carrying that constraint rather than
stating it as the question.** The human's own words named `CLAUDE.md` literally. Ground rule 1 bars a
shipped contract from assuming a file convention of one harness, and the map records that a worker
will eventually not be a Claude subagent at all — so the contract says *the repo's own instructions
to an agent* and the checker finds whatever the repo has. The literal reading was available and I did
not take it.

`167.2` `ASSUMPTION` **· settled** — **I reported the repair with no blocking edge on nodes 151 and 164, both of which
edit the same file.** I read both conditions: neither quotes nor protects the two sentences this
repair changes, node 151's clause 12 forbids its own worker to reword anything outside its new
section, and node 164's protective clauses name two different statements. So either order works, and
I left the sequencing to the manager rather than spending an edge on it.

`167.3` `ASSUMPTION` **· settled** — **I reported the residual as a node although the human declined the invitation to ask
for it.** My question offered to report the rules-file-versus-repo precedence question separately if
they said so; they answered the yes/no and said nothing about it. I judged that the residual is this
node's own subject surviving in a narrowed case rather than a new topic, so leaving it unreported
would close node 167 on a question it did not finish. It is cheap to kill if unwanted.

## Interview

### Attempt 1

*The attempt's routing key does not survive the manager's session, so it is not recorded here: a fresh manager thread
cannot resume this attempt and runs the replacement procedure instead.*

**The worker's question, pasted as it wrote it.**

> ```
> NODE:          The checker's bar-commands route, left asymmetric by node 143's amendment (node 167)
>
> ABOUT:         Node 143 stopped the checker and the implementer hunting for the standards and sent
>                both to one known file, `map-implementation-rules.md`. That amendment covered the
>                standards only. **The bar's commands** — the concrete build/test/format commands for
>                a repo — were left on the old route for the checker, and its own checker noticed on
>                the way out. You approved node 143 without answering it, so it is a node now.
>
> SO FAR:        I read the two shipped contracts, the rules file, node 143 and its gate, and nodes
>                138/140/144/151/164. The state today:
>
>                - The **implementer** is told: the bar is properties, and "the commands are where
>                  the standards are: use whatever `map-implementation-rules.md` records for this
>                  repo. Where it records none, discover them from the repo."
>                - The **checker** is told (given 2): the bar reaches it "either its commands for
>                  this repo, or the properties alone… Where you are given properties and no
>                  commands, discover the commands from the repo." So it gets them by spawn or by
>                  its own discovery, and never from the file — the contract sends it into that file
>                  for the standards and tells it in as many words to leave the rest unread.
>                - So two agents can end up running different commands for the same bar, and the
>                  checker's new section already claims otherwise: "It is the same file the
>                  implementer works from, so the two of you hold the work to one set of rules
>                  rather than two." That is true of the standards and false of the bar's commands.
>                - `map-implementation-rules.md` **already holds the commands for this repo**, in the
>                  paragraph directly above the standards, in the same section, and that paragraph
>                  says it was recorded "so no later node re-derives them". The same section records
>                  that two checker runs spent their largest single cost rediscovering the route.
>
>                Settled on my own authority: this is one question, not several. Whether the
>                discovery fallback survives, and whether the "one set of rules" sentence gets
>                repaired, both follow from the answer rather than being separate calls.
>
> ASK:           Should the checker's bar-commands route follow the standards into the same file —
>                the checker reads the commands from `map-implementation-rules.md`, and the spawn
>                stops carrying them?
>
> RECOMMENDED:   Yes: make it symmetric. The checker's given 2 becomes "the bar is these properties;
>                its commands for this repo are in the implementation-rules file you already read for
>                the standards; where it records none, discover them from the repo" — word for word
>                the implementer's route. Four grounds:
>                (1) The file's own line says the commands are recorded there so no later node
>                    re-derives them, and the checker re-deriving them is exactly what that line
>                    exists to prevent.
>                (2) Your stated ground for the standards route was changeability — a rule in a file
>                    can be edited, one an agent finds for itself cannot. A build command has the
>                    same property: when it changes, editing one file should reach both agents.
>                (3) It makes the contract's "one set of rules rather than two" sentence true instead
>                    of needing a repair.
>                (4) It costs nothing to run: the checker already opens that file, and the commands
>                    are the paragraph immediately above the standards in the same section.
>                What it costs: it widens what a blind checker reads in a file that also holds the
>                record — which is node 164's open subject. I judge the commands safe by the test
>                node 42 fixed for that, since a build command is true of any node's work and tells
>                the checker nothing about this work in particular. The work is one edit to
>                `expedition-checker/SKILL.md`; it touches no file node 144's worker is editing.
>
> ALTERNATIVES:  - Yes, but the spawn keeps priority (spawn beats file beats discovery): preserves
>                  the drift you'd be fixing, and leaves manager-typed text bearing on the check.
>                - No: leave the route asymmetric, and instead narrow the "one set of rules" sentence
>                  to the standards so the contract stops asserting something false. Cheaper, keeps
>                  the checker's blindness boundary exactly where node 143 drew it, and accepts the
>                  two agents can run different commands.
>                - Symmetry the other way — both discover for themselves: rejected outright, it is
>                  the rediscovery cost your standing direction is against.
> ```

*Relayed.*

**The human's reply, `verbatim`.**

> I kinda expect that the build instruction are in the CLAUDE.md of the project so they should already have the information in their context ?

***The manager's note.*** **This is a reframing of the question rather than an answer to it**, so it was passed back
to the worker holding the interview rather than read as picking any of the options offered. It takes neither
`RECOMMENDED` nor any `ALTERNATIVE`, and it is not marked `DIVERGENCE`: it puts the premise in question rather than
contradicting the recommendation. No option is quoted beside it, none having been taken.

**The worker's second question, pasted as it wrote it.**

*Banked at hand-back: it queued behind the manager's own raise on [node
144](144-make-the-rules-file-stand-alone.md)'s checker, and behind [node
163](163-a-condition-demands-facts-the-checker-does-not-read.md)'s, which arrived earlier in the same tier. Relayed
once both cleared.*

> ```
> NODE:          The checker's bar-commands route, left asymmetric by node 143's amendment (node 167)
>
> ABOUT:         You reframed rather than picked: build instructions live in the project's CLAUDE.md,
>                so both agents already hold them. I went and checked that instead of arguing it, and
>                it changes what I recommend.
>
> SO FAR:        Three things I established, none of which I had before:
>
>                1. **You are right about the dogfood target.** Lang's `CLAUDE.md` states the bar's
>                   commands outright: *"No custom build/test scripts exist — use plain `cargo build`
>                   / `cargo run -- <file>.lang`. Lint with `cargo clippy`."* Node 10 already read
>                   the bar there partly off that file.
>                2. **You are right about the mechanism.** A subagent does receive the project's
>                   instruction block — I got one in this very spawn.
>                3. **This repo has no `CLAUDE.md` at all**, and no build, tests or formatter either.
>                   So on this effort there are no commands to route, and the asymmetry is inert here
>                   rather than harmful.
>
>                What that does to my Q1 recommendation: it kills it. I argued the file route stops
>                the two agents drifting. But under your framing the common source is the project's
>                own live statement, and the rules file's record is a *copy* of a discovery — copies
>                go stale, and this record has already met that failure once, when an external
>                standard moved under a resolved node within the hour. Making the checker read the
>                copy too would double down on the stale thing.
>
>                What your framing does **not** dispose of, and why I am back rather than done:
>
>                - The checker's given 2 still offers a **spawn** route — *"either its commands for
>                  this repo, or the properties alone"*. That is manager-typed text bearing on the
>                  check, and it is the one route that can drift from anything the repo says. It also
>                  contradicts what you settled at node 143's gate: nothing is fed.
>                - The checker's contract still asserts *"It is the same file the implementer works
>                  from, so the two of you hold the work to one set of rules rather than two."* True
>                  of the standards, false of the commands, however they are routed.
>
>                Settled on my own authority: any wording names the repo's own instructions **by
>                role**, never as `CLAUDE.md` — ground rule 1, and the same constraint the manager
>                applied at node 143 to naming this effort's directory literally.
>
> ASK:           So is the answer "no route change — the repo's own instructions are the common source
>                and the contracts already say discover from the repo", with the work cut down to two
>                repairs: delete the spawn-carries-commands half of the checker's given 2, and bound
>                that "one set of rules" sentence to the standards?
>
> RECOMMENDED:   Yes, that. It takes your reframing as the answer rather than working around it: the
>                route is already right, and what is wrong is a leftover feed route and one sentence
>                that overclaims. It is a small edit to `expedition-checker/SKILL.md` only, it touches
>                no file node 144's worker is holding, and it leaves the checker discovering commands
>                from the repo — which is what reads the project's instructions in the first place.
>
> ALTERNATIVES:  - My Q1 recommendation, the checker reading commands from the rules file too:
>                  withdrawn, for the staleness reason above.
>                - Change nothing at all: cheapest, but ships a contract stating something untrue,
>                  and leaves the manager able to type commands into a check.
>                - Go further and demote the rules file's record to a cache for the **implementer**
>                  too, so the project's own statement wins where the two disagree. I am not
>                  recommending it here — it edits text node 143 landed a day ago, and your remark
>                  does not ask for it. If you want it, say so and I will report it as its own node
>                  rather than fold it into this one.
> ```

**The human's reply, `verbatim`.**

> ok

**The option it takes**, quoted from the worker's own `ASK` and `RECOMMENDED` and attributed to the worker:

> **ASK:** So is the answer "no route change — the repo's own instructions are the common source
> and the contracts already say discover from the repo", with the work cut down to two
> repairs: delete the spawn-carries-commands half of the checker's given 2, and bound
> that "one set of rules" sentence to the standards?
>
> **RECOMMENDED:** Yes, that.

***The manager's note.*** **Not a divergence**: the `ASK` is a yes/no whose `RECOMMENDED` is *"Yes, that"*, so the
reply assents rather than contradicting. **It takes none of the three `ALTERNATIVES`** — in particular the third,
which asked the human to *"say so"* if they wanted the implementer's route demoted as well, and which a bare `ok` does
not say. The manager records that rather than deciding it.

## Retrospective

*Pasted as the worker wrote it. Filed by the manager as an annotation; this effort asks every worker for one, and the
worker's own contract forbids it to write a graph file.*

**(1) What I had to hunt for.**
- *Whether the human's `CLAUDE.md` claim holds.* I looked first in the graph, grepping for `CLAUDE.md`, and that half-answered it: node 10 already records that Lang's `CLAUDE.md` states *"no tests exist"* and supplies its bar. The other half I got from the filesystem — a root listing of this repo (no `CLAUDE.md`, and no build to have one for) and Lang's `CLAUDE.md` itself. The decisive fact for the answer was **this repo having none**, and nothing in the record says it.
- *Where the bar's commands are recorded.* `map.md`'s line 7 pointer took me straight to `map-implementation-rules.md`. That worked, and is the one pointer in the map that saved me a search.
- *Whether the node I mint collides with nodes 144, 151 and 164.* Three whole node files read for what amounts to four clauses. There is no index of which open conditions touch which paths, so the only way to answer "who else is editing this file" is to open every candidate node.

**(2) What arrived that this node did not need.**
- *From `map.md`, my mandatory read:* the items on **manager conduct** — one question at a time and the queue target, the manager never idling and starting the next node, every report ending with what is expected of the human, flags settling at the close, and the `EnterWorktree` instruction. A worker cannot act on any of them. Node 139 built `map-manager-only.md` for exactly this and these items did not go; finishing that move is the arrangement that would have avoided it. What I did use from the map was small and specific: ground rule 1, the never-delete rule, the note that a worker will not always be a Claude subagent, and the retrospective spec.
- *Where I went for one fact and took the whole file:* `map-implementation-rules.md`. I needed the bar's-commands paragraph in `## What the work is held against`; I also got the entire landing policy — the worktree lifecycle, four struck accounts of a sandbox restriction, and the forensics of a failed rebase. Roughly sixty lines of git diagnostics bearing on nothing a grilling worker does. The file has exactly two `##` sections and everything any non-implementation reader wants is in the second, so a pointer addressed to the heading rather than the file would have avoided all of it. This is the same file, and nearly the same complaint, that node 164 is open about from the checker's side.
- Same shape, smaller: `expedition-implementation/SKILL.md` read whole for one paragraph, and node 143's 415-line file read whole for its amendment section and its checker's question. Node 143's case I would not change — the flags turned out to bear on my wording — but the read was long and I could not know that in advance.
- *From the spawn:* nothing bore on nothing. The manager's node-144 warning was the right shape — a location claim, asserting nothing about content — and it was load-bearing, since checking the collision is what let me report the repair unblocked.

**(3) What would have made this node easier.**
- **The node file omits the two facts that decide the question.** It quotes the checker's question in full but does not say that `map-implementation-rules.md` already holds a bar's-commands paragraph, nor that this repo has no build commands at all. The second makes the asymmetry inert on this effort, which reframes the whole node from *a defect to fix* to *a rule to state before it bites elsewhere*. One line each.
- **The record does not generalise what node 10 observed.** Node 10 read Lang's bar partly off its `CLAUDE.md` and no rule anywhere says a repo's own agent instructions are a source for the bar. Had `map-implementation-rules.md`'s bar's-commands paragraph said where commands come from in general, the human's reframing would have been anticipated by the question instead of arriving as a correction to it — and this node would have been one round rather than two.
- **Nothing indexes which open acceptance conditions touch which paths.** Every node minting work in a busy file pays the same three-file read to answer "who else is holding this".

**(4) What I read that was stale, wrong, or contradicted something else.**
- **Two open implementation conditions describe a mechanism node 143's amendment abolished.** Node 151's clause 4 speaks of *"the standards the spawn gives the checker"*; node 164's clause 3 requires its statements sit *"beside the two routes by which they reach it"*, and its clause 2 of *"a path it was given as a standard"*. Under the amendment nothing is fed and there is one route, which the landed contract states. Both workers will meet a condition naming something that does not exist. This is precisely the defect node 143's own file had to be repaired for at its gate — its checker's words, *"A later checker handed this node cold would read the file and fail work that meets the condition in force"* — and the repair was applied to node 143's file and not to the two downstream conditions that inherited the assumption.
- **Node 164 may be substantially discharged already by node 143's landed text.** Its clauses 1 and 2 ask the contract to state what a standards path may hold and what the checker does where such a path also holds record material; the landed `## The standards you hold the work against` already says the file *"may itself carry material that is record rather than standard… Read the standards; leave the rest of that file unread, and open no other file beside it."* Its outcome-reporting half looks like the part still outstanding. Worth checking before that node is claimed as written.
- Nothing I read was wrong on its facts.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
