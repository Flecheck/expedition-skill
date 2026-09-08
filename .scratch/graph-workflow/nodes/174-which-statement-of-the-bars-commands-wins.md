# Which statement of the bar's commands wins where a recorded copy and the repo's own instructions disagree

Type: grilling
Status: resolved

Blocked by: none

## Question

*Surfaced by [The checker's bar-commands route](167-the-checkers-bar-commands-route.md)'s worker, and pasted as it wrote it.*

> The implementation contract tells its worker to *"use whatever
> `map-implementation-rules.md` records for this repo"* and to discover the commands only where it
> records none; the checker discovers them from the repo. Where an effort's rules file records commands
> **and** the repo's own agent instructions state different ones, the two agents run different
> commands — which is the drift node 167 was minted about, surviving in one narrowed case. Which is
> authoritative? And does the rules file's record become a cache that is checked against the repo
> rather than trusted, given that a recorded copy of a discovery goes stale while the repo's own
> statement does not?

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**This node exists over the human's silence rather than their instruction**, which is [flag
`167.3`](167-the-checkers-bar-commands-route.md): node 167's question offered to report this separately *if they said
so*, and their `ok` answered the yes/no without taking the offer. Its author minted it anyway, judging it node 167's
own subject surviving in a narrowed case, and said it is cheap to kill if unwanted.

**On this effort the question is inert**, node 167's answer having established that this repo has no build, no tests
and no formatter and no agent-instruction file at all. It bites on another repo.

## Interview

### Attempt 1

**The worker's payload carried one question** rather than a batch, having found that the state reduced to a single
choice. Its `SO FAR` established that **three shipped files state where the bar's commands come from and they do
not agree** — `CONTEXT.md`'s *"Properties rather than commands: the commands are discovered per repo"*, the
checker's contract saying discover from the repo, and the implementation contract saying *"use whatever
`map-implementation-rules.md` records for this repo"* — so **the implementation contract is the single outlier
against the other two**, which reframes the node from a standoff into a repair. It also verified this repo's root
itself: no `CLAUDE.md`, no `AGENTS.md`, no manifest, so the recorded copy records an absence and nobody has yet run
a wrong command.

**The human's reply, `verbatim`.**

> ok

**The option it takes**, quoted from the worker's own payload and attributed to the worker:

> **ASK:** Does the repo's own live statement of its commands always win — with the rules file's record demoted from
> something an agent trusts to something it confirms against the repo before using, running the repo's commands and
> reporting the disagreement where the two differ, and never failing the work over it?
>
> **RECOMMENDED:** Yes.

***The manager's note.*** **Not a divergence**, and it takes none of the four alternatives — not *the record wins*,
not *a disagreement stops the work and comes to the human*, not *leave it asymmetric*, and not *delete the record
entirely*. **The bare `ok` is unambiguous here because the payload carried exactly one question**, so there is no
option to pick between; the manager records that rather than inferring which of several it meant.

**Three things the worker settled on its own authority before asking**, in its words: that any wording names the
repo's own instruction file **by role** and never as `CLAUDE.md`, under ground rule 1 and the phrasing [node
167](167-the-checkers-bar-commands-route.md) already fixed; that the shipped wording will not introduce *cache* as a
term, `CONTEXT.md` already refusing `cached` for a different thing; and that the same contradiction sitting inside
`graph-conventions.md` is [node 153](153-graph-conventions-notes-bullet-is-false.md)'s rather than this node's.

## Answer

*Pasted as the worker wrote it.*

> **The repo's own live statement of its commands wins, always. The recorded copy is demoted from something an agent
> trusts to something it confirms against the repo before using.**
>
> **The rule, as it now stands:**
>
> > A repo's own live statement of its build, test and format commands is authoritative. Where an effort's
> > implementation-rules file records those commands, that record is a copy of an earlier discovery: an agent
> > confirms it against what the repo itself says before using it, rather than trusting it. Where the two differ the
> > repo's statement wins, the agent runs the repo's commands, and it reports the difference so the record can be
> > repaired — the difference is never a reason to judge the work defective, the work not being the thing that is
> > wrong. Where the repo states no commands of its own, the record is the only statement there is and stands as it
> > is, unconfirmed.
>
> **Both halves of this node's question are answered, and the second half is the one that does the work.** *Which
> wins* is settled by the first sentence. But either answer to *which wins* leaves the losing copy sitting there
> going stale, and only the cache reading says what becomes of it: a record that keeps winning goes stale in
> silence, where a record confirmed on every use cannot.
>
> **This is a repair rather than a new rule, and that is what made it cheap.** Three shipped files state where the
> bar's commands come from, and two already said *discover*: [`CONTEXT.md`](../../CONTEXT.md), the glossary this
> effort declares authoritative — *"Properties rather than commands: the commands are discovered per repo"*, which
> mentions no recorded copy at all and **needs no change**; the **checker's** contract, which discovers them from
> the repo and **needs no further change from this node**; and the **implementer's** contract — *"use whatever
> `map-implementation-rules.md` records for this repo. Where it records none, discover them from the repo"* — **the
> single outlier**, and the site of the repair.
>
> **It closes the case [node 167](167-the-checkers-bar-commands-route.md) named and left open.** That node carried
> the human's own reframing — build instructions live in the repo's own instructions to an agent, which the agent
> already holds — to the checker and not to the implementer, and said so: *"On a repo whose rules file records
> commands **and** whose own instructions state different ones, the two agents run different commands."*
>
> **On this effort the rule is inert, and measurably so.** This repo's root holds no `CLAUDE.md`, no `AGENTS.md` and
> no manifest. The record therefore records an *absence*, there is no repo statement to confirm it against, and it
> stands unconfirmed. **One consequence worth having:** three checkers this session re-checked that absence against
> the tree rather than taking the record's word, and under this rule they need not have. So the rule **removes** a
> small repeated cost here rather than adding one.
>
> **A fourth site was found that no node in the record connects to this question**, and it is the manager's own
> contract. `.claude/skills/expedition/SKILL.md` holds the trusted-copy model twice — its `map` glossary entry,
> where the bar's commands *"live there and nowhere else"*, and its `the bar` entry, *"discovered per repo and
> written once into the effort's map"* — and holds the checker-spawn mirror of the very given node 173 was minted to
> delete: *"the bar — its commands where the effort's map records them for this repo, its properties otherwise"*.
> Node 173's condition is confined to the checker's file and reaches none of it. All three also name `map.md` as the
> home of the commands, which node 140 made false. The repair below covers all four sites in one node, on the ground
> that the defect being fixed *is* an inconsistency between shipped files and landing half of it would recreate one.
>
> **Where any wording names the file a repo states its commands in, it names it by role and position and never by
> filename.** `CLAUDE.md` is one harness's convention and ground rule 1 forbids a shipped contract assuming it.

**What the worker reported its work invalidates**, pasted as it wrote it:

> **[Node 10](10-done-ness.md) — *Done-ness and termination* — is contradicted in one clause of its `## Answer`, and
> it is the clause the rules file's bar paragraph cites.** Node 10 wrote: *"the properties are fixed and shipped,
> the commands are discovered per repo on first use, and then **written once into the map's Notes** — so the next
> node does not re-derive them, and so the human can see and edit what is actually being run."* Three parts, and
> they do not fare alike:
>
> - ***"discovered per repo on first use"*** — stands, and is the ground this node's answer rests on.
> - ***"written once into the map's Notes"*** — already false on location, node 140 having moved the record to
>   `map-implementation-rules.md`; and now false on standing, *once* having become *once, and confirmed against the
>   repo on each use*.
> - ***"so the next node does not re-derive them"*** — **narrowed rather than reversed.** No later agent re-derives
>   the commands from scratch. But where the repo states its own commands the later agent uses the repo's statement
>   and the record is only confirmed against it. Where the repo states nothing — this effort's case — node 10's
>   clause holds exactly as written.
> - ***"so the human can see and edit what is actually being run"*** — stands, and is now the record's main job.
>
> **No other resolved node is contradicted.** In particular **node 167 is completed, not contradicted**: it
> explicitly declined to fold this case in and reported it as a node, and this answer settles it the way that node's
> own reasoning pointed. **Node 143 stands untouched.**

## Flags

*All four are the worker's own text, pasted. The ids are the manager's bookkeeping and nothing else.*

`174.1` **· settled** `ASSUMPTION` — **I settled that the shipped wording names the file a repo states its commands
in by role and position only, never as `CLAUDE.md`, and put that in the question as settled rather than asking it.**
Ground rule 1 bars a shipped contract from assuming one harness's file convention, and the map records that a worker
will eventually not be a Claude subagent at all. This merely re-applies what node 167 already fixed at flag
`167.1`, so it is cheap to accept; the literal reading was available and I did not take it.

`174.2` **· settled** `ASSUMPTION` — **I settled that no shipped file will introduce *cache* as a term, although
the node's own question and my recommendation both use the word.** `CONTEXT.md` already refuses `cached` as a name
for a **banked answer**, and a second use of the word for a second concept would blur a fifty-entry glossary the
shipped files declare authoritative. So the rule is written as *confirmed against the repo before use* and the word
*cache* stays in this node's prose and out of the deliverables.

`174.3` **· settled** `ASSUMPTION` — **I settled that the self-contradiction inside `graph-conventions.md` is a
neighbouring question rather than this node's, and did not put it to the human.** That file's `## Notes` bullet
names `map.md` as the home of the bar's commands where an earlier paragraph names the rules file. The false half is
node 153's and its condition repairs it; the earlier paragraph makes a containment claim rather than an authority
claim, so this node's answer leaves it true and demands no change to a file five other nodes are queued on.

`174.4` **· settled** `ASSUMPTION` — **I settled that the shipped repair is one node over two files rather than two
nodes, and that no blocking edge is needed.** One rule stated inconsistently across shipped files is the defect
itself, and splitting the repair would leave a window where the contracts disagree again — which is how node 167
came to exist, node 143's amendment having covered one agent and not the other. On edges: fifteen open nodes target
`.claude/skills/expedition/SKILL.md`, and I read each one's acceptance condition for a claim over the bar's-commands
passages or the checker-spawn given list. None holds one — every hit was the routine *the tree meets the bar*
clause — so any order works and I left the sequencing to the manager rather than spending an edge.

***The manager's note.*** **All four are settled by the human's `ok` at this node's own interview**, that being the
first human moment this node's close reached. **`174.4` is the most expensive judgement any worker has made cheaply
this session**: it read fifteen open acceptance conditions to establish that no edge was owed, and reported that
nothing indexes which open conditions touch which paths — which its retrospective calls the third report of that
item.
