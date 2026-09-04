# `map.md` has grown back most of what node 59's restructure saved

Type: grilling
Status: claimed

Blocked by: none

## Question

*Surfaced by [Whether the contracts' instruction to invoke a method skill is doing any
work](113-whether-the-method-skill-instruction-does-any-work.md)'s worker, and pasted as it wrote it.*

> `map.md` is **40,344 bytes** today against the **26,971** node 59's restructure landed it at, so append-in-place
> has given back 13,373 bytes — roughly 3,340 tokens on every worker's uncached opening payload — eroding that node's
> measured 71% cut to 56%. The map's standing preference ranks a measured token saving above the rest, and this is
> measured rather than predicted. What, if anything, bounds the map's growth?

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**The manager is the map's only writer, so this is a question about the manager's own conduct**, and most of the
13,373 bytes were added by the manager in this session — every standing direction of the human's written in under
node 93, every correction archived under the `Change the map` procedure, and every superseded item's replacement.
**The manager has not weighed whether any of that was avoidable** and has added nothing to the question.

**One tension the answer will meet, named because the manager holds both halves.** The never-delete rule and the
`Change the map` procedure between them mean a correction **adds** text rather than replacing it: the new wording, a
pointer to `map-history.md`, and often a sentence saying what was wrong. So the mechanism that keeps the map true is
the mechanism that grows it. **Three corrections landed in this session alone** by that route.

**Two figures the manager can supply and has verified**, since a grilling worker should not have to derive them: the
map is read cold, in full, by **every worker on every node**, and node 52's ratio for this repository is exactly 4
bytes per token, which is the rule of thumb rather than a tokenizer count.

## Interview

### Attempt 1, questions 1 and 2 — delivered

*Pasted as the worker wrote it. The manager authored none of it and has taken no view on either question.*

> **NODE:** `map.md` has grown back most of what node 59's restructure saved
>
> **ABOUT:** The effort's map is the one file every worker reads whole, cold, before doing anything. Node 59 cut it
> by 71%; it has since grown 58% back. This node decides what, if anything, bounds that growth — and it is being
> decided now because the growth is measured rather than predicted, which is the only kind of token finding this
> effort's own rules let you prioritise.
>
> **SO FAR:**
>
> I read the map, the node behind it (59), the token research it rests on (52), the four decision-index lines, the
> shipped conventions document's rules for writing the map, and the "read and did not use" answer of all 19
> retrospectives on the record. Then I measured. Byte counts are exact; token figures are nominal at this repo's
> 4-bytes-per-token rule of thumb, which is not a tokenizer count.
>
> **1. THE GROWTH, AND WHERE IT WENT.** Node 59 landed the map at 26,971 bytes. It is 42,566 today — +15,595, a 58%
> regrowth. (It was 40,344 when this node was filed: it grew a further 2,222 bytes while the node about its growth
> sat open.) Node 59's 71% cut is now a 54% cut. A worker's map read is ~10,600 nominal tokens, up from ~6,700.
> Where the 15,595 went: the standing-preference bullets +8,779 (56%); the landing/worktree policy and the code-slot
> count +2,734 (18%); the "review route" and "bar's commands" records +2,186 (14%); the four writing rules promoted
> out of node 53 +762; the Destination's new expected-to-end paragraph +617; the fog +469. The bullet list went 11 ->
> 16 bullets and its mean bullet went 548 -> 924 bytes.
>
> **2. THE TENSION I WAS HANDED IS MEASURABLY FALSE, AND I AM CONFIDENT OF THIS.** The manager's note says the
> never-delete rule and the `Change the map` procedure mean a correction adds text rather than replacing it, so "the
> mechanism that keeps the map true is the mechanism that grows it." I measured the whole correction apparatus in the
> file: two "Corrected at node 114's check..." clauses at 128 and 129 bytes, and ten sentences pointing at
> `map-history.md` totalling 900 bytes. So the entire never-delete-plus-correction machinery costs about 1,150 bytes
> of 42,566, and of the +15,595 of growth it accounts for at most ~500 (3%). The shipped procedure is not
> append-anyway either: `graph-conventions.md`'s `Change the map` step 2 says *replace* it with the new statement.
> Three corrections in a session cost ~400 bytes. This is node 52's finding 11 recurring in a new place — there it
> was struck-through text misidentified as the cost (2.1%) when live append-in-place was the cost. Same shape here:
> the truth-keeping mechanism is a rounding error, and something else is doing the growing.
>
> **3. WHAT IS ACTUALLY DOING THE GROWING: TWO THINGS, BOTH ALREADY GOVERNED BY A RULE NOBODY ENFORCES.**
> (a) The shipped conventions document already states the bound. `## Writing the map`: every map item is "a
> **current statement**: what holds now, citing by markdown link the nodes that shaped it and **never restating what
> those nodes hold**. The **account** behind it — how it came to say that, what was measured, what it used to say —
> belongs in `map-history.md`." The map's own fourth writing rule says the same. The map today does not obey it: the
> four largest bullets (1,864 / 1,765 / 1,680 / 1,572 bytes) each carry the account — what the rule reverses, what it
> does not license, what ground the human gave, which nodes refined it — beside the rule itself. The rule is true,
> shipped, and enforced by nothing, because "does this restate what a node holds" is not mechanically checkable.
> (b) There is a natural experiment inside the file. Node 59's condition put a hard 900-byte cap on each fog item and
> no cap on anything else. Since then the capped section grew 6.4% and stayed at 9 items; the uncapped bullet list
> grew 145%. The one enforced cap is the one thing that held. (One fog item has since drifted to 1,343 bytes, so even
> that cap now has a breach nothing caught.)
>
> **4. THE SECOND LEVER, AND THE MEASUREMENT NODE 59 PROMISED TURNS OUT TO EXIST.** Node 59 said the split between
> the map and its history would be "settled by measurement rather than argument", and pointed at node 60 — *a worker
> reports what the map did not tell it* — as the instrument. I checked: node 60 is still `open` and unbuilt, so the
> promised instrument was never made. But the opposite instrument was built by accident and has been running for
> weeks: the retrospective's second question, "what did you read and did not use". It has produced 19
> retrospectives, 13 of which name map sections. Unprompted and independently, they converge: the landing/worktree
> policy and code-slot count named unused by 11; the dogfood target by 11; the fog by 11; out-of-scope by 10; the
> review route by 7; the bar's commands by 7; the label vocabulary by 5. Against that, the only parts any
> retrospective reports *acting on* are the standing preferences, the ground rules, the four writing rules, the
> Destination and the bar line. Node 60 was to detect shortfall; the surfeit instrument arrived first, unplanned, and
> nothing sweeps it.
> The reason those sections read as dead weight is that they are not universal — they are per-kind. The review route
> is material the *manager* reads to compose a checker's spawn (the checker never reads the map). The landing policy,
> the worktree lifecycle and the bar's commands are for an implementation worker and its checker. The code-slot
> count, the fog, the dogfood target and out-of-scope are the manager's. On the section-level reading the
> retrospectives directly name, that is 17,619 bytes — 41% of the file. Adding the standing-preference bullets that
> are manager-only in substance (report-ends-with-one-line, manager-never-idles, flags-settle-at-close,
> resume-wherever, and the copy-the-block paragraph) brings it to ~24,100 bytes, 57% of what every worker on every
> node pays for.
> And the map's own governing first sentence is what admits all of it: "it holds only what **a** worker can act on."
> Every byte above passes that test, because some worker can act on each of them. The test that would bound the file
> is "what **every** worker can act on" — a one-word difference between the sentence the map states and the sentence
> its own cost model implies.
>
> **5. WHAT I SETTLED MYSELF (returning as ASSUMPTION flags).** That "read and did not use" is legitimate evidence of
> surfeit rather than a worker's complaint; the per-kind/universal boundary calls on individual sections, drawn from
> what the retrospectives name rather than from my own judgement wherever they name it; and that all token figures
> are nominal per flag 52.1.
>
> Two questions follow. Neither one's answer depends on the other's: Q1 decides which material is in the file at all,
> Q2 decides what each surviving item may cost. They compose without double-counting — the bullets Q1 moves out are
> not the ones Q2's cap would then be trimming.
>
> **ASK:**
>
> **Q1** — Does the map's admission test become "what EVERY worker can act on", with per-kind material moved to a
> sibling file its actual reader is pointed at?
>
> **Q2** — Is a map item's size capped by a number a mechanical check can enforce, since the shipped rule that
> already forbids the account cannot be checked?
>
> **RECOMMENDED:**
>
> **Q1** — Yes. Change the map's first sentence to "only what **every** worker can act on", and move the per-kind
> material out of the file every worker reads into siblings named for their reader, with the map keeping a one-line
> pointer to each. Concretely: the landing policy, the worktree lifecycle, the code-slot count and the bar's commands
> to a file the implementation and checker spawns point at; the review route, the dogfood target, the label
> vocabulary, the fog and out-of-scope to a file the manager reads. Pointer, not copy — copying into spawns would
> move the cost into the manager's context, which is this effort's first-failing resource and which the "most of the
> context lives in the workers" preference forbids.
> This rests on: node 52's mechanic (every worker pays its whole opening payload uncached, so the map's size
> multiplies by the node count, 179 at the dogfood target); 13 independent unprompted reports converging on the same
> sections; 41% of the file measured; and the precedent inside this effort, since `map-history.md` is exactly this
> move made once already, along a different axis. It also does what node 59 said would happen — the split gets
> settled by measurement — and the measurement is now in hand from the instrument nobody planned.
>
> **Q2** — Yes: cap each item in `## Notes` at 500 bytes of prose, excluding the human's own verbatim quote, with the
> remainder moving to `map-history.md` under the existing `Change the map` procedure, and add the cap to
> `graph-conventions.md`'s numbered mechanical checks as check 10. Excluding the quote because shortening the human's
> words is paraphrase, which never-delete forbids. 500 because it is not a number I invented: 8 of the 16 current
> bullets already meet it, including three of the oldest and most load-bearing — "most of the context lives in the
> workers" at 411 bytes, "an in-place update never deletes" at 349, "the human is the scarce resource" at 445. So the
> cap is set at what this map's own best-behaved rules already cost, and the seven bullets that breach it are the
> seven filed in one session. Measured effect: the bullet block falls 14,797 -> 8,385, saving 6,412 bytes on every
> worker's read on every node. The cap goes in the mechanical checks because the record shows why: the shipped rule
> that says the same thing in prose has been in force throughout the 145% growth, and the one cap that was mechanical
> is the one section that held.
>
> **ALTERNATIVES:**
>
> **Q1** — Keep one file and put a whole-file byte ceiling on it (node 59's condition used 32,000): cheap and
> checkable, but it names no principle, so when it binds, the choice of what gives way lands on the manager
> mid-session — and it is the manager's filing that grew the file.
> — Keep one file with per-kind headings and tell each worker to read only its own: rejected because node 52's cost
> is the payload, not the worker's attention. A worker is handed the file and pays for all of it whether it reads it
> or not.
> — Accept the growth, and let nothing bound it: defensible on the ground that every byte is either a standing
> direction of yours or a fact recorded so no later agent re-derives it, and that a worker acting on a stale map
> costs more than a large one. I set it aside because the map's own standing preference ranks a measured saving above
> the rest and this saving is measured, and because 41% of the file is being paid for by workers who report it bore
> on nothing.
>
> **Q2** — No cap; restate or sharpen the shipped rule instead. Set aside because that is the status quo and the
> status quo is the 145%.
> — Cap the item count rather than the bytes: set aside because the count is set by how many standing directions you
> give, which is not the workflow's to ration.
> — A tighter cap, 300 bytes excluding quotes, saving 8,714: set aside as the point where a rule can no longer state
> its own scope — several of these bullets do operative work in their second half by naming what the rule does *not*
> license, and losing that is how a rule gets over-applied.
> — A looser cap, 900, matching the fog's: saves only 3,146, because the current mean is already 924. The number and
> the saving are the same decision here, which is why I put a defended number in the recommendation rather than a
> range.

***The manager's note beside it, and not the worker's.***

**Its section 2 is a correction of the manager's own note at filing, and the manager accepts it.** The note above
claims the never-delete rule and the `Change the map` procedure make a correction add text rather than replace it, so
that *"the mechanism that keeps the map true is the mechanism that grows it."* The worker measured that mechanism at
about 1,150 bytes of 42,566 and at most ~500 of the 15,595 of growth, and read the shipped procedure's step 2 as
saying *replace*. **The manager wrote the tension from belief rather than from measurement**, and it is the shape node
52's own annotation names — an unestablished claim offered as context. It stands struck by the worker's measurement
rather than removed, the never-delete rule holding.

**The manager takes no view on either question**, and has not weighed the recommendations. Both bear directly on the
manager's own conduct, which is what the node was minted about.

**One fact the manager holds and the worker could not.** Its section 4 says node 60 is *"still `open` and unbuilt"*,
which the manager confirms. So the instrument node 59 named was never made, and the instrument the worker used —
the retrospective's second question — was fixed by a different node and never intended as a measurement of the map.

### Attempt 1, answers to Q1 and Q2 — Q1 taken, Q2 a divergence

**The human's word, `verbatim`**, written at the moment they spoke:

> Q1 ok Q2 I am not a fan of a hard cap but maybe a soft capto try to meet it. You don't want a rule that forces to
> remove critical information.

**Q1 is taken.** The recommendation it settles, quoted in full and attributed to this node's worker rather than to
the manager:

> Yes. Change the map's first sentence to "only what **every** worker can act on", and move the per-kind material
> out of the file every worker reads into siblings named for their reader, with the map keeping a one-line pointer to
> each. Concretely: the landing policy, the worktree lifecycle, the code-slot count and the bar's commands to a file
> the implementation and checker spawns point at; the review route, the dogfood target, the label vocabulary, the fog
> and out-of-scope to a file the manager reads. Pointer, not copy — copying into spawns would move the cost into the
> manager's context, which is this effort's first-failing resource and which the "most of the context lives in the
> workers" preference forbids.

**`DIVERGENCE` on Q2.** The worker recommended **a hard 500-byte cap enforced as a mechanical check**, its whole
ground being that the prose rule already forbidding the account *"is true, shipped, and enforced by nothing"* and that
*"the one cap that was mechanical is the one section that held"*. **The human refuses the hard cap** and offers a soft
one in its place, with a reason the worker's payload did not raise on either side: *"You don't want a rule that forces
to remove critical information."*

***The manager's note, and not the human's words. Three facts recorded rather than decided.***

1. **Their reason is not among the alternatives the worker offered.** The worker set aside a 300-byte cap on a
   related but distinct ground — that a rule too short to state what it does *not* license gets over-applied. The
   human's objection is to the **hardness** rather than to the number: a cap that binds mechanically forces a
   deletion at the moment it binds, whoever is filing and whatever is being filed. **That is a new argument on this
   node**, and the manager has not weighed it.
2. **"Soft cap" is not defined anywhere on this graph, and the manager has not defined it.** *"maybe a soft cap to
   try to meet it"* fixes the direction and leaves the mechanism open. Whether a soft cap is a target the manager
   aims at, a number the mechanical checks report without failing, or something else is the worker's to put back —
   it holds the interview.
3. **The worker's ground for hardness is untouched by their answer and still stands on the record.** The 145% growth
   happened with a prose rule in force saying the same thing. A soft cap has to answer that measurement or accept
   it; nothing in the human's reply does either, and it was not asked to.
