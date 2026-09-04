# What to do about the record's token cost, given what `qmd` turns out to be

Type: grilling
Status: claimed

Blocked by: none — [node 128](128-whether-qmd-lowers-this-workflows-token-cost.md) resolved

## Question

*Minted by the manager from the human's own request that the research be followed by a grilling node. Their words,
`verbatim`:*

> Maybe create a research node and then grilling

**The decision this node holds.** Given what [node
128](128-whether-qmd-lowers-this-workflows-token-cost.md) establishes: does this workflow adopt `qmd`, change how the
record is written so that less of it must be read, do both, or neither? And where a change is adopted, does it reach
the **shipped files** — which ground rule 1 forbids to assume a toolchain — or only this effort's own record, which
is not shipped?

**One thing the human said and hedged, which belongs to this node rather than to the research:** *"I don't know if it
is nessesary ?"* — their own uncertainty about whether the record needs to be easier to grep and traverse at all. So
**neither** is a live answer here and not a formality.

## The manager's note at filing

*Not a change to anything above.*

**This node is blocked and will stay blocked until node 128 hands back**, because every option it chooses between
turns on a fact nobody has: what the tool is. The manager minted it now rather than later only because the human
asked for it in the same message.

## Interview

### Attempt 1

*The attempt's routing key is held in the manager's session and does not survive it. Banked at hand-back, before
being relayed: this question queues behind node 145's, which was live when it arrived.*

**The worker's question, pasted as it wrote it.**

> **ASK:** Do we take package A below — no qmd anywhere for now, and one shipped change to how the record is *read*
> rather than how it is written — or one of the alternatives?
>
> Package A, in three parts:
> (i) One instruction in each worker contract: the record is searched before it is read whole. Phrased as a property
>     ("search the record"), never as a command ("run grep"), so ground rule 1 holds and nothing is installed.
> (ii) `decisions.md` moves off every worker's read-whole list onto that search list. `map.md` and the worker's own
>     node file stay read whole, because a worker cannot know which of their constraints it needs until it has read
>     them. Saving: ~6,000 tokens per worker per node, measured.
> (iii) The index's one-line cap stays as it is. Once workers search the nodes rather than the index, the cap costs
>     nothing and widening it would make a file every worker touches bigger to serve a retrieval the corpus already
>     serves.
>
> One boundary I would write into it explicitly: this does not touch your direction that a checker must not go and
> find its own rules. Rules an agent is *held to* are given to it, so they can be changed in a file. Facts in the
> record are found, because nobody knows in advance which one a worker will need.
>
> **RECOMMENDED:** Package A, reaching the shipped files.
>
> It rests on three measurements rather than on a prediction. The saving is measured (~6,000 tokens/node from (ii),
> ~12x on a targeted fact from (i)); it is free, so it competes with nothing; and it is the only lever here that does
> not decay, which points 2 and 3 above make a measured claim rather than an intuition. It also closes the hole the
> map split just opened, which is a correctness point and not a saving: after node 140 lands, a grilling or research
> worker needing the bar's commands has no pointer to them at all, and search is the only route back.
>
> One honest caveat I would write into the instruction: search is only cheap when it is narrow. Searching this record
> for "code slot" returns 33,215 bytes — more than reading `decisions.md` whole. Listing the matching files first
> returns 2,651, and a narrowed phrase 483. So the instruction is two-step: list, narrow, then read.
>
> On qmd specifically: I am recommending we refuse it *for now* and name the trigger that would bring it back. Its
> one real advantage over search is genuine — it finds a fact phrased differently from your query, which is exactly
> the position every cold worker is in. But its saving over plain search is unmeasured, and it would be replacing a
> free alternative that has never once been instructed. Adopting it today is the failure your own token-priority rule
> warns against: ranking by predicted saving. The trigger is concrete — if (i) lands and workers start reporting that
> they could not find a fact because they did not know its wording, that is the measurement, and qmd becomes worth
> its 2 GB in this effort's notes.
>
> **ALTERNATIVES:** B — Package A *and* install qmd for this effort's notes now, to get the number that decides it.
> Costs ~119 MiB of install plus ~2 GB of models, re-indexing on every node edit since this record never deletes, and
> ~2,800 tokens of skill text per spawn that loads it. Buys the one comparison nobody can make today.
>
> C — qmd only, no contract change. Refused: it cannot touch the mandatory read at all (you cannot query for rules
> you do not know exist), so it leaves the largest measured cost untouched and adds a dependency.
>
> D — Neither; the hedge you raised. I set it aside only because the measurement removes it: (ii) alone is ~6,000
> tokens per worker per node for one sentence of contract text, which is a cost we are currently paying for nothing.
>
> E — Package A, but this effort's notes only, changing no shipped file. Cheaper and reversible, but it would leave
> the workflow's own cost unchanged on every future effort, which is what your token-priority instruction ranks
> first.

**The measurements the question rests on**, pasted as the worker wrote them:

> 1. qmd needs Node 22, Bun, a compiled SQLite extension and ~2 GB of downloaded models, and it ships *as a Claude
> Code plugin*. So in the shipped files it is barred twice over: by ground rule 1, and by the standing direction that
> the skill not depend on a plugin — qmd would be a strictly harder version of the dependency just asked to be
> removed. In this effort's own notes, which ship nothing, it is permitted.
>
> 2. Splitting files is a lever that decays. `map.md` was cut to 26,971 bytes by node 59, grew back to 43,847, was
> cut to 31,481 by node 139 two hours ago, and is 33,007 bytes now. Twice cut, twice regrowing.
>
> 3. The read discipline is a lever that does not decay, and it has never been pulled. Nothing in any shipped
> contract tells a worker to search the record before reading a file whole. Measured: the fact a worker wanted from
> node 52 costs 25,295 bytes read whole, or 2,180 bytes of search output — about 12x cheaper, free, and working on
> any machine.
>
> 4. `decisions.md` is the single largest uncontested waste on the table. It is 24,345 bytes (~6,000 tokens), 42% of
> the two files every worker reads whole, and seven retrospectives now name it: not one worker used more than about
> four of its 74 entries, and the three who searched it instead of reading it reported that it worked and cost almost
> nothing.
>
> 5. Its one-line cap is provably lossy — the fact three workers went looking for appears zero times in the file. No
> search engine repairs that; the fact is in node 52, where searching the *nodes* finds it.
>
> 6. Splitting the map has created a new hole that only search closes. Node 139 moved material into a file `map.md`
> says no worker reads, and node 140 is moving more out now. It has already bitten once: a worker on node 132 needed
> a standard, found it in the manager-only file, and had to decide on its own authority whether it was allowed to
> read it.

**The human's answer**, `verbatim`:

> yes package A

**The option it takes, in the worker's own words** — quoted because the reply is unreadable without it and the prose
is the worker's:

> **RECOMMENDED:** Package A, reaching the shipped files.

***The manager's note.*** **Not a divergence**: the answer takes the worker's own recommendation. **The manager
considered and did not treat the reply as ambiguous.** Alternative E was *"Package A, but this effort's notes only,
changing no shipped file"* — a Package A variant — so a bare *"package A"* could in principle have meant either. The
manager's relayed question ended *"package A as recommended, or one of B through E"*, the reply opens with *"yes"*,
and E was not named; on this effort the human's two preceding answers took recommendations in the same form
(*"yes recommended"*, *"recommended ship it"*). So the reply is read as the recommendation, which reaches the shipped
files. Recorded here rather than left to inference, because the difference between the recommendation and E is
whether the change reaches the shipped worker contracts at all.

**The human's correction**, `verbatim`, sent immediately after the answer above and while the worker was writing its
handover:

> wait revert: leave decisions in read-whole - it's small enough

**`DIVERGENCE`.** The recommendation was package A entire, and part (ii) was *"`decisions.md` moves off every
worker's read-whole list onto that search list"*. The human keeps (i) and (iii) and reverts (ii), so the answer now
departs from the worker's recommendation on the part carrying its largest measured saving.

***The manager's note.*** **The measurement the reverted part rested on stands in the record and is not withdrawn**,
so a later reader does not mistake the revert for the measurement being wrong: the worker measured `decisions.md` at
24,345 bytes (~6,000 tokens), 42% of the two files every worker reads whole, with seven retrospectives reporting that
no worker used more than about four of its 74 entries and three reporting that searching it instead worked and cost
almost nothing. The human's stated ground is *"it's small enough"*. The manager put nothing to them about it and
relayed the correction to the worker unaltered.

**The human's ground for the revert**, `verbatim`, given unprompted after it:

> the rationale for decisions being kept fed is that LLMs will otherwise hardly proactively search for decisions,
> whereas if it's fed to context, the LLM's engine will take it into account naturally - and it's small enough.

***The manager's note.*** **This meets the worker's measurement rather than overriding it.** The worker's evidence was
that no worker *used* more than about four of `decisions.md`'s 74 entries; the human's ground is that entries in
context are taken into account without being cited, so a count of explicit uses does not measure the file's effect.
It also names the failure the search instruction would cause — that a worker told it may search will mostly not — which
is a claim about part (i)'s reliability and not only about (ii). The manager relayed it to the worker unaltered and
put nothing to the human about it.

***The manager's note on the first handover.*** **It arrived carrying part (ii) as landing, and was sent back once.**
Its answer read *"(ii) `decisions.md` leaves every worker's read-whole list and becomes a searched pointer"*, and
clause 1 of its surfaced acceptance condition read *"The effort's index of decisions is no longer an item of the read
list"* — both of which the human had reverted before the handover was written. The two corrections had been relayed
to the worker and are recorded above; whether they reached it before it finished is not something the manager can
establish, the worker having reported no acknowledgement of either. **Nothing from that handover was written onto
this node**, per the rule that a handover sent back is not recorded, and it was sent back naming exactly what was
wrong.
