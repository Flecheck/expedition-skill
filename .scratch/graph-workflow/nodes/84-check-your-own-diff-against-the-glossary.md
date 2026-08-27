# Whether a worker checks its own prose against the glossary's headwords before handing back

Type: grilling
Status: open

## Question

The glossary refuses words with `_Avoid_` lines and **defines** words as headwords, and those are two different
tests. An `_Avoid_` line refuses a word outright, so scanning for refused words catches its own class. A headword
**permits** the word and fixes its meaning — so a break is a word used in its ordinary sense, invisible to anyone
scanning for refusals, and visible only by holding each defined term against the text.

**Nothing tells anyone to run the second test**, and the effort's own guidance points only at the first: `map.md`'s
review route says *"the distinctive refusals are checked by hand"* and says nothing about the headwords.

**It cost a correction round the same day it was noticed.** At [What a finding must carry so it can be
swept](71-what-a-finding-must-carry.md) the worker checked its prose against the `_Avoid_` lines, passed, and shipped
`sweep` in its ordinary-English sense — a headword meaning an effort-level pass over the graph. The blind checker
built the missing test, found it, and the round cost a full worker resume for one clause. In the worker's own words:

> I read `CONTEXT.md` for its **`_Avoid_` lines**, which is what `map.md` says the refusals are for, and I checked
> my text against them. I did not check my text against the **headwords**, which is a different and stricter test…
> `map.md` warns that the `_Avoid_` list is a poor grep target and says nothing about the headwords being a good
> one — but they are: 50 terms, word-boundary matched against the diff, two hits, both dispositionable in seconds.
> **A worker writing prose into the shipped corpus should run the headword enumerator over its own diff before
> handing back**, and that is cheap enough to be a rule rather than a habit.

### What makes this a decision rather than a wording job

**Ground rule 1 stands against the obvious form.** The enumerator is a shell pipeline over `grep`, and nothing in
the shipped files may assume a toolchain. So either the rule is stated as a property — *hold your prose against
every term the glossary defines, not only the ones it refuses* — with the pipeline as an illustration that is
allowed to be absent, or it is not shipped at all and lives in this effort's own map.

**Who it binds is not obvious either.** Only some workers write prose into the shipped corpus. Putting it in all
five contracts costs four irrelevant paragraphs; putting it in one leaves the next kind of worker uncovered; putting
it in the bar makes it the checker's test rather than the worker's, which is where it already effectively is —
and the whole point is that the *worker* running it is what saves the round.

**And the cheaper half may not need a node at all.** `map.md`'s review route note is the manager's own file and
already carries the measured trap about the refusals being a poor grep list. Adding the headword enumerator beside
it helps checkers, who caught this one anyway. The node is about the half that helps the worker.

### What the answer has to fix

- Whether it is shipped or effort-local.
- If shipped, which contracts carry it and in what form, given ground rule 1.
- Whether it is stated as a duty before handing back, or as one more item under the bar.

## Priority

**Token-use work**, so it rides [What the manager works on next](16-human-steering.md)'s standing bump: its whole
value is a correction round not spent, and the one instance is measured rather than predicted — one worker resume,
for one clause.

## Where it came from

Node 71's worker, in the retrospective it returned after the correction round that this would have prevented. Filed
by the manager, that retrospective being effort-scoped and returning no `NEW NODES` of its own.
