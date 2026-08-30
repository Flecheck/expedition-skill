# Whether a condition's scope stops being a list of files

Type: grilling
Status: open

## Question

*Surfaced by [How a condition's scope is amended](82-amending-a-condition-whose-scope-was-too-narrow.md)'s worker,
and pasted as it wrote it.*

> Node 82's guard 1 re-derives a condition's file enumeration before the claim, which repairs an ageing list rather
> than removing it. The alternative is that a condition addressing a defect with instances states the defect as a
> predicate over a named search domain — "every place under `.claude/skills/**/*.md` where X" — and gives any file
> list as illustration rather than as the bound. That shape is already self-contained text a checker can run against
> the repo, it is the shape [What a finding must carry so it can be swept](71-what-a-finding-must-carry.md) already
> makes a checker hand back, and it would have reached all four recorded shortfalls with no amendment at all,
> including the file that did not exist when node 58's condition was written.
>
> What is genuinely at stake against it: a scope clause has one load-bearing job, which is stopping a worker
> wandering into unrelated work, and a predicate is a weaker fence than a list. A predicate scope also moves the
> moment of judgement — who decides whether a given place matches, and what a worker does when it thinks the
> predicate reaches somewhere the author did not intend.
>
> So: should a condition addressing a defect with instances be written as a predicate over a search domain rather
> than as a list of files — always, never, or on a stated trigger — and if so, what keeps the fence doing its job?

**Blockers, in the worker's words:** *"none. Node 82 is resolved and node 71 has shipped."*
