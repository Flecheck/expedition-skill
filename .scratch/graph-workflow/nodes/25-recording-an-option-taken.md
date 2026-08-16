# What is recorded when the human takes an option as offered

Type: grilling
Status: resolved

## Question

When the human answers by taking one of the options they were offered, exactly as written, what goes onto
the node — the option's text standing as the human's own, or the manager's rendering marked `paraphrase`?

Reported by [Off-contract subagent output](17-off-contract-output.md)'s worker, which hit it as the stated
limit of the check that node built.

It is unsettled rather than obvious: [Subagent context contract](12-subagent-context-contract.md)'s
`## Interview` marks three such answers **`verbatim` (option chosen as written)**, while [Off-contract
subagent output](17-off-contract-output.md)'s marks all three of its own **`paraphrase`**. Same act, two
markers, on the same map, four nodes apart.

It matters more than it did when [Relay protocol](08-relay-protocol.md) accepted the marker as the remedy
for `F6`, because [Off-contract subagent output](17-off-contract-output.md)'s check now makes the recorded
answer **the baseline something reads against**: a check that catches a worker inventing the human's words
cannot catch a manager having supplied them, and afterwards the two look alike on the page.

The third option — the manager echoes the answer back and the human confirms it — costs a round trip on the
resource this map calls scarce, and is the one to beat.

## Answer

**The manager pastes what the human wrote. Whatever they wrote is the answer, however short, and it
is marked `verbatim`.**

This node was written as a choice between two markers for one act. It is not one. Both markers were
labels for something that should not have happened: in [Subagent context
contract](12-subagent-context-contract.md) and [Off-contract subagent
output](17-off-contract-output.md) alike, the text recorded as the human's answer is *the option's*
text, and the human's own reply was kept in neither. `verbatim` and `paraphrase` were two honest
descriptions of the same substitution — node 12 calling the option exact, node 17 calling it a
rendering — and the disagreement between them is the symptom rather than the thing to fix.

### What goes onto the node

One entry, holding two texts, attributed:

- **the human's reply, as they wrote it**, marked `verbatim` — the whole of it, however terse. *"ok
  for recommended"* is a complete answer and is recorded as one.
- **the option it points at, quoted and attributed to the worker that wrote it.** It is on the page
  because the reply is unreadable without it, and it is attributed because it is not the human's
  prose.

Nothing is rendered, so nothing is marked `paraphrase`. The label keeps both its values and
`paraphrase` keeps the meaning it was given — a rendering the manager could not avoid — which after
this decision is rare and always deliberate.

### Why this, and not either marker

**The relay already required it.** [Relay protocol](08-relay-protocol.md) fixes the downward payload
as `HUMAN ANSWER: <the human's own words, verbatim>`, and [Subagent context
contract](12-subagent-context-contract.md) makes the manager a **scribe** that pastes and never
re-authors. Substituting the option's text for the human's reply is re-authoring, in the one place
two sessions of the manager did not notice it was re-authoring. So this answer adds no rule. It
removes an exception that had grown under two names.

**The marker stops being a judgement.** It is written at relay time, in the turn the manager resumes
the worker, and the record shows that a marker needing a judgement gets got wrong — twice, by the
same manager, in opposite directions, neither time noticed. Copying is the manager's cheapest act and
it yields `verbatim` every time, so the correct marker is now a consequence of the default behaviour
rather than something the manager has to be paying attention to. That was the binding constraint on
this node: whatever it decided had to be followable by a manager not attending to the distinction.

**It repairs [Off-contract subagent output](17-off-contract-output.md)'s check at the source.** That
node holds a handover's `ANSWER` against the `## Interview` the manager wrote itself, and stated its
own limit: the baseline can be one remove from the human, so the check catches a worker inventing the
human's words and cannot catch a manager having supplied them. With the human's reply on the page the
baseline *is* the human, and *resting on words the human did not say* becomes decidable. That limit
is now closed rather than merely stated — and closed without the echo-and-confirm round trip this
node named as the option to beat. The reply is already in the manager's context; copying it costs
nothing.

**`F6` is the case this restores.** [Relay protocol](08-relay-protocol.md)'s `F6` — a worker quoting
*"the human's exact answer"* while actually holding the manager's paraphrase of an **option label** —
is precisely this act, and the verbatim rule was written for it. Marking an option `verbatim` would
have made `F6` policy.

### The terse reply, and what it costs elsewhere

A four-word reply is a complete `verbatim` answer. Two places that changes something.

**A worker resumed with a terse assent must reason from the option it offered.** The shipped
`expedition-grilling` and `expedition-prototype` contracts both say `HUMAN ANSWER` *"holds their
words, not a rendering of them"* and then instruct the worker to *"reason from what they wrote rather
than from the option you offered"*. That sentence was written against a rendering and is wrong
against an assent: where the human's words *are* an assent to a named option, the option is what they
endorsed and the worker reads it as theirs. It needs a carve-out and does not have one.
`expedition-precondition` and `expedition-implementation` carry the `HUMAN ANSWER` block without that
sentence and need nothing. Verified on disk: the sentence lives in exactly those two contracts, both
at line 98.

**The same rule governs `## Review`.** An approval at the gate is the same act — the human taking an
offered outcome as written — and [Subagent context contract](12-subagent-context-contract.md)'s
ordering rule already covers both logs in one sentence. *"ok, ship it"* is recorded as written,
`verbatim`, beside what it approves.

Both are edits to files that have shipped, so both belong to an implementation node against those
files rather than to the manager mid-flight, per [Off-contract subagent
output](17-off-contract-output.md).

### The six entries already on this map

Not recoverable: the human's words for those exchanges were never kept, and the sessions holding them
are gone. What reaches those two nodes is honesty about what their entries are.

- **[Subagent context contract](12-subagent-context-contract.md)'s three `verbatim` markers are wrong
  under this answer.** They claim the human's own words for text the human did not write, which is
  the one direction that fails unsafely. Struck through in place, corrected to `paraphrase`, pointing
  here. Marking superseded text and writing the new text beside it is the standing in-place-update
  rule, and neither node's `## Answer` is touched — so this is an annotation, not a supersession.
- **[Off-contract subagent output](17-off-contract-output.md)'s three `paraphrase` markers stand.**
  They were accurate about the text they carried, and those entries already say in prose what the
  text is. They gain the same forward pointer and nothing else.

### This node's own first entry

Node 25's `## Interview` is the first record made under this rule: a four-word reply marked
`verbatim`, with the recommendation it points at quoted beside it and attributed to the worker. It is
also the first instance of the terse-assent case, which is what surfaced the contract sentence above.

## Flags

`25.1` **· settled** `ASSUMPTION` — decided alone that [Subagent context contract](12-subagent-context-contract.md)'s
three `verbatim` markers are corrected in place — struck through, `paraphrase` written beside them,
pointing here — rather than left with only a forward note. Read the map's never-delete rule as
prescribing exactly that for text that is now clearly wrong, and read an `## Interview` marker as an
annotation rather than a change to the node's answer, so no supersession. **The human was not asked
whether a resolved node's record may be edited at all.**

`25.2` **· settled** `ASSUMPTION` — decided alone that this rule governs `## Review` as well as `## Interview`, on the
ground that [Subagent context contract](12-subagent-context-contract.md)'s ordering rule already covers
both logs in one sentence and that an approval at the gate is the same act as taking an option. Not put
to the human.

`25.3` **· settled** `ASSUMPTION` — decided alone that where a terse reply does not make clear which
option it points at, the manager records the reply and asks which, rather than choosing one and quoting
it. This is the only case left that costs a round trip, and it is a genuine ambiguity rather than a
rendering. Settled in the human's own words, which state it as a rule rather than as an exception:
*"If an anwser is not clear, yes ask again"*.

`25.4` **· settled** `ASSUMPTION` — **filed by the manager, by running [Off-contract subagent
output](17-off-contract-output.md)'s check on this node's own handover.** Two of the answer's sections
entered from the manager's own notes rather than from the human or from the worker's reading: *The six
entries already on this map*, which produced `25.1`, followed a manager note observing that the
worker's finding reached two resolved nodes; and *This node's own first entry* followed a manager note
about the rule applying to itself. Neither rests on words the human said. **This is the second
consecutive node where that check has fired and the party it caught was the manager** — the first time
for words put into the human's mouth, this time for scope the human did not open.

## Interview

### Attempt 1 — routing key `graph-workflow/25/a1`

Chosen off the frontier at the human's direction, in their words: *"Do 25 first, it's better to close it if
it is a live inconsistency"*.

**Q1** — When you take one of the options exactly as offered, what should land in the node's `## Interview`
as your answer: your own reply as you actually typed it, with the option quoted beside it and attributed to
the worker that wrote it? Or the option's text standing alone as the answer, in which case we must pick
which of the two markers it carries?

The worker recommended **your own reply, as you typed it, marked `verbatim`** — with the option text quoted
in the same entry and attributed to the worker. Its grounds: [Relay protocol](08-relay-protocol.md) already
fixes the downward payload as the human's own words and [Subagent context
contract](12-subagent-context-contract.md) already makes the manager a scribe, so this is the existing rule
being followed in the one place both nodes stopped following it; the marker becomes mechanical, since copy
always yields `verbatim`; and it fixes [Off-contract subagent output](17-off-contract-output.md)'s check at
the source, the baseline no longer being one remove from the human. Set aside: `paraphrase` on the option
text always, `verbatim` on the option text, a third marker value, and echo-and-confirm.

**A1** — `verbatim`

> ok for recommended

The option that phrase points at is the worker's `RECOMMENDED` block, quoted in full above and **written by
the worker, not by the human**.

This entry is the first record made under the rule the node decides, and it is deliberately shaped by it:
four words of the human's, and the option kept beside them under someone else's name. Under the practice of
[Subagent context contract](12-subagent-context-contract.md) it would have read *"your own reply, as you
typed it, marked `verbatim`"* marked `verbatim`; under [Off-contract subagent
output](17-off-contract-output.md)'s, the same sentence marked `paraphrase`. In neither would the words *ok
for recommended* appear anywhere on the map.

### Settling the flags

Put to the human as the node closed, per the practice set at [Write the worker contract
skills](22-worker-contract-skills.md)'s gate. The manager recommended settling all four, and recommended
against making `25.4` a node of its own on the ground that [Human-initiated
steering](16-human-steering.md) is the natural home for the same question with the human steering.

**A** — `verbatim`

> 25.1 ok 25.2 ok 25.3 If an anwser is not clear, yes ask again

`25.3` is the one of the three that is not a bare assent. The flag as the worker wrote it treats an
unclear reply as a residual case that costs a round trip; the human's words state it as a rule, and it is
recorded on the flag as they wrote it.

**Q** — `25.4` was not understood on first reading, so the manager restated it: two of the answer's
sections, including the one that produced `25.1`, exist because the manager's own notes pointed the worker
at them, and neither came from the human or from the worker's reading. The manager offered settle, leave
outstanding, or promote to a node, recommended settling, and stated one thing against its own
recommendation — that this was the second consecutive node where the check fired and caught the manager.

**A** — `verbatim`

> ok for 25.4, we will see when we do the manager skill

The second clause is a routing instruction rather than part of the settlement: the question of how far a
manager's notes may steer a worker is deferred to the writing of the manager's skill, and is not promoted
to a node here.
