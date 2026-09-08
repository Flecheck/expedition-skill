# Which statement of the bar's commands wins where a recorded copy and the repo's own instructions disagree

Type: grilling
Status: claimed

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
