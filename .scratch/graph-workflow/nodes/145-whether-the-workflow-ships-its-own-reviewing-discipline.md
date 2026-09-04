# Whether the workflow ships its own reviewing discipline, now that a checker may not find one

Type: grilling
Status: resolved

Blocked by: none

## Question

*Surfaced by [Where the rules a checker is held to live](138-where-the-rules-a-checker-is-held-to-live.md)'s worker,
and pasted as it wrote it.*

> Removing discovery from the checker's contract removes a procedure as well as a list — the checker is left with
> sources and no discipline for reviewing against them. Does the workflow ship one of its own, or is a list of
> standards the whole of what a checker gets? Shipping one mints a second shipped-discipline deliverable beside node
> 130's, and the human's packaging direction — *"so that the skill can be used without it or the doc by itself"* —
> would then bind it too. Node 132's earlier worker named this cost and did not ask it.

## The manager's note at filing

*Not a change to anything above.*

**This is the one part of node 138's third section its worker refused to settle**, and it said why: the rest followed
from the human's direction or from a resolved node, where this *"mints a deliverable"*. Everything else about what a
checker is given is settled and is [node 143](143-rules-arrive-by-the-spawn-never-by-a-search.md)'s work.

**It meets [node 130](130-the-docs-discipline-this-workflow-ships.md) at exactly one point**, in node 138's words:
both are *"the same shape — a named thing handed over, rather than a thing discovered"*, and if the workflow ships a
reviewing discipline it is a second shipped-discipline deliverable beside node 130's, which the human's packaging
direction would bind. **Under node 138's answer that direction now binds node 130's output**, which is flag `138.5`.

**Node 132 is where this cost was first named and not asked.** Its worker wrote that replacing `/writing-for-agents`
*"would mint a third shipped-discipline deliverable on top of node 130's"* — so this node, node 130 and node 132 are
three views of one count, and the manager has not weighed whether they should be one node.

## Answer

*The worker's own text, pasted. Written by attempt 2, which rests on attempt 1's evidence and attributes it.*

**The workflow ships its own checking discipline, as a short section of the shipped checker contract. A list of
standards is not the whole of what a checker gets.**

The human's word, `verbatim`: *"recommended ship it"*. It takes attempt 1's recommendation, quoted in full and
attributed to that worker rather than to the manager:

> **Ship it, as a section of the checker's contract**, roughly fifteen lines, with an effort's own rules file free to
> add method specific to that effort on top — which yours already does. Concretely: read the acceptance condition and
> split it into its parts before you read the work, because your `PASS` owes one line per part; keep the three axes
> separate and never merge or rerank them — the condition, the bar, and the standards, which report under the bar —
> so passing one cannot mask failing another; establish each part by a search you can name and hand back rather than
> by reading through; say plainly what you did not check. Nothing is taken from the barred skill.

No divergence.

### 1. What ships, and where it sits

A section headed `## How you check` in `.claude/skills/expedition-checker/SKILL.md`, after `## Hard rules` and before
`## What you hand back` — the position the four contracts that already carry a method section put theirs in. It
carries four moves and one routing rule: split the condition into parts before reading the work; keep the condition,
the bar and the standards separate and never merge or rerank them; establish each part by a named search rather than
by reading through; say plainly what was not checked; and the standards report **under the bar**, so a standards
breach is `FAIL: the bar` and never `FAIL: acceptance condition`. Roughly fifteen lines. It is written by the node
reported below, not here.

### 2. What it mints, which is the whole of why this node was held back

**Nothing separately installable, so the packaging direction does not bind it.** The human's direction that the docs
discipline be packaged *"so that the skill can be used without it or the doc by itself"* is about a thing someone
could install on its own. A section inside a contract that already ships is not that. The cost [node
138](138-where-the-rules-a-checker-is-held-to-live.md) named — that shipping a reviewing discipline mints a second
shipped-discipline deliverable beside [node 130](130-the-docs-discipline-this-workflow-ships.md)'s — was real, and it
bites only under the option set aside. **The count of separately-packaged discipline deliverables on this effort stays
at one, and it is node 130's.** [Node 132](132-does-the-plugin-direction-reach-the-efforts-own-bar.md)'s third view of
that count is likewise untouched.

### 3. What the evidence rests on, and one correction it owes

The five grounds are attempt 1's and are on this node in full: the checker was the contract left without a method
because its method *was* the skill it was told to find; the human had already made this call once at *"For 113 ok"*,
and the checker is the contract it did not reach; a method each effort must write itself is no method on a repo the
workflow has never seen; fifteen deletable lines cost almost nothing to be wrong; and the record measures the
shipped-method option as the winning one, at roughly twenty to one against the found skill's standards pass, with four
separate places saying the checker's row was under-specified.

**One correction this node owes the record, verified rather than assumed.** Attempt 1's evidence point 1 says the
checker is *"the only contract with no method section"*. `grep -n "^## " .claude/skills/expedition-*/SKILL.md` returns
`## How you research`, `## How you prototype`, `## How you grill` and `## How you implement` — four — and **the
precondition contract has none either**. The recommendation's shape claim ("the same shape the other four contracts
have") is exact; the word *only* is not. Nothing in the answer turns on it.

### 4. What was set aside

- **Standards and no method**, the status quo after node 143's deletion — no checker would ever report it thin,
  because a checker that improvises does not know it was owed a method.
- **The method in this effort's rules file rather than the shipped contract** — every future effort would write its
  own from scratch and a fresh repo's checker would get nothing. What survives of this option is that an effort's
  rules file may still add method **on top**.
- **A separately-installable checking discipline beside node 130's** — the option this node existed to stop being
  chosen by accident.
- **Vendoring the twelve code smells** — object-oriented smells against a prose deliverable, against a contract rule
  that a property nobody stated is not a finding, and measured at two surviving findings across twenty runs, one of
  them suppressed.

### 5. What this leaves for the two nodes beside it

**Node 143 keeps its clause 5 machinery, as its manager note anticipated.** *"If the human says yes, this file gains
something later"* — they said yes, and what the file gains is the section reported below, which is blocked on node 143
rather than folded into it.

**[Node 132](132-does-the-plugin-direction-reach-the-efforts-own-bar.md) and this node do not overlap in what they
produce, and this node agrees with node 132's worker.** Node 132's output — through [node
149](149-state-the-prose-standards-demands-in-the-rules-file.md) — is a never-shipped section of the effort's own
rules file saying what this effort's **prose standards demand**. This node's output is a shipped, effort-agnostic
section of a contract saying **how a checker proceeds**. Different file, different reader, different kind of content;
they touch only in that a checker on this effort reads both, where the shipped section says the standards report under
the bar and the rules file says what those standards are. The new node's condition forbids restating any standard, so
they cannot contend.

**[Node 129](129-what-to-do-about-the-records-token-cost.md) and this node do not want the same sentence in the same
file.** Node 129's package A instructs a worker to search **the record** before reading it whole; this node's method
has a checker establish a part of the condition by a search over **the work**. The objects differ, and node 129's own
payload draws the boundary in as many words — *"Rules an agent is held to are given to it… Facts in the record are
found"*. The checker reads no record at all, so node 129's `decisions.md` half cannot reach its contract. Whichever
lands second should cite the other rather than restate it; neither should be merged into the other.


## Flags

*Each entry is the worker's own prose, pasted. The manager added the id and the marker and nothing else.*

`145.1` **· settled** `ASSUMPTION` — **The shipped thing is called *checking*, and the section is `## How you check`.** Not *reviewing*, and not `## How you review`. Decided from `CONTEXT.md`, which is authoritative on this effort's vocabulary and refuses the word twice: the **Checker** entry's `_Avoid_` line reads *"reviewer, verifier, auditor — reviewing is the human's"*, and the **Gate** entry's reads *"review (that is what the human does at the gate)"*. The human's answer settles that it ships and says nothing about what it is called, and this node's own title and interview say *reviewing discipline* throughout — that is the pre-glossary word, and this node does not carry it into a shipped file the glossary governs. The reading set aside: naming the section for the word the record discusses, which would put a refused word into the shipped corpus and cost a later consistency node.

`145.2` **· settled** `ASSUMPTION` — **Method specific to this effort stays in the effort's own rules file and is not shipped.** Concretely that is the measured trap in the review-route paragraph — that `CONTEXT.md`'s refused words are largely unusable as a grep list, about a third being ordinary English refused only for one concept, so the distinctive refusals are checked by hand instead — which sits in `map-manager-only.md` today and which [node 140](140-move-the-implementers-and-checkers-material-out-of-the-map.md) is moving into the file the checker and implementer read. It is a fact about this repo's glossary rather than a property of checking, so ground rule 1 bars it from a shipped file. The shipped section says only that an effort's rules may add method on top and that its own demands still hold where they do. The reading set aside: hoisting the trap into the contract as a worked example, which would assume this repo.

`145.3` **· settled** `ASSUMPTION` — **The `FAIL: the bar` routing rides the new node rather than getting one of its own.** Attempt 1's point 4 named a live defect: the sentence telling a checker that the standards are held under the bar sits inside the section node 143 deletes, and node 143's replacement does not carry it forward. It is verified on disk as *"Everything you find is held against **the bar**, whose own wording is whatever else the repo itself demands"*, inside `## The standards this repo and this machine carry`. I put it in the new node's condition rather than minting a second node, for three reasons: the option the human took already states it in as many words (*"the standards, which report under the bar"*), so a separate node would write the same sentence twice into the same file; two nodes editing `.claude/skills/expedition-checker/SKILL.md` would contend for one code slot; and a defect whose repair is one clause does not need a node of its own. **The consequence I am accepting and naming:** between node 143 landing and the new node landing, the shipped contract states the standards as a given and nowhere says which of its two verdicts they report under. The repair I did not take is amending node 143's clause 2 to preserve the sentence — that adds a demand to a written condition, which under [node 82](82-amending-a-condition-whose-scope-was-too-narrow.md) is the human's act and not the manager's, since only a scope widening that adds no demand is the manager's. Sequencing the two nodes back to back closes the window without anyone amending anything.

## Interview

### Attempt 1 — **dead**

*The attempt died. Discovered by a resume that failed with `No transcript found`, which is the only way a
death is discoverable: a running agent's transcript cannot be read and a dead one cannot be inspected, so attempting
the resume is the detector. It died **after** the human's answer below had been written onto this node, so nothing
the human said was lost. The claim stays with the node, which keeps its number and its file.*

*The attempt's routing key is held in the manager's session and does not survive it. Banked at hand-back, before
being relayed: this question queues behind node 147's raise and node 132's question.*

**The worker's note to the manager, pasted as it wrote it.** Its first payload was re-issued after a survey it had
commissioned returned; it is one question rather than two.

> **TO THE MANAGER, before the payload:** this is the **same question, same number, same recommendation, same four
> alternatives** — Q1 of attempt 1, not a second question. Only the evidence under `SO FAR` gains one item (point 6)
> and `RECOMMENDED` gains one ground (e). **If Q1 has already been put in front of the human, do not deliver this:
> their answer to it answers this node in full, and this text is for the record.** Nothing displaces a live
> question, and this graph has twice paid for a second payload arriving behind a first.

*Q1 had not been put to the human when this arrived, so this text is the payload rather than a record of a
superseded one.*

**The worker's question, pasted as it wrote it.**

> **ASK:** Does the checker's contract get its own short `## How you check` section — a shipped method, the same
> shape the other four contracts have — or does a list of standards stay the whole of what a checker is given?
>
> **RECOMMENDED:** **Ship it, as a section of the checker's contract**, roughly fifteen lines, with an effort's own
> rules file free to add method specific to that effort on top — which yours already does. Concretely: read the
> acceptance condition and split it into its parts before you read the work, because your `PASS` owes one line per
> part; keep the three axes separate and never merge or rerank them — the condition, the bar, and the standards,
> which report under the bar — so passing one cannot mask failing another; establish each part by a search you can
> name and hand back rather than by reading through; say plainly what you did not check. Nothing is taken from the
> barred skill.
>
> It rests on five things rather than on preference.
>
> **(a) It mints nothing, which is the whole of what this node was held back for.** Your direction that the docs
> discipline be packaged *"so that the skill can be used without it or the doc by itself"* is about a thing someone
> could install separately. A section inside a contract is not that. The worry that answering this creates a second
> separately-shipped discipline is real, but it only bites under the option I am setting aside.
>
> **(b) You have already made this exact call once**, at *"For 113 ok"*, and the checker is the one contract it did
> not reach.
>
> **(c) A method the effort must write itself is no method on a repo the workflow has never seen** — which your map
> names as the constraint to design for now rather than port to later.
>
> **(d) It costs almost nothing to be wrong.** Fifteen lines, deletable. Against your preference for short prose
> over machinery for predicted needs: this is not a predicted need, it is the hole the deletion leaves.
>
> **(e) It is the option your own record already measures as the winning one** — twenty-to-one, point 6 below. Your
> checkers have been improvising this method for a year of nodes; four separate places in the record say so in as
> many words, and one node's diagnosis of six consecutive correction rounds was that *"the checker's row was
> under-specified, and each round has been the human filling it in against a live example."* This is that row,
> still unfilled.
>
> **ALTERNATIVES:**
> — **Standards and no method — the status quo after the deletion.** Cheapest, and defensible on your preference
> for waiting until something is reported thin. Against it: no checker will report it, because a checker that
> improvises does not know it was owed a method, and the bar/condition routing defect ships regardless.
> — **Put the method in your effort's rules file instead of the shipped contract.** Closest to your earlier words —
> *"put it in the map"* — one file beside the standards, editable in one place. Against it: every future effort
> writes its own from scratch, and a fresh repo's checker gets nothing.
> — **Ship it as its own separately-installable checking discipline, beside the docs one.** The option this node
> exists to stop you choosing by accident; your packaging direction would bind it, and it is machinery for a need
> nothing has demonstrated.
> — **Vendor the twelve code smells so the checker keeps a substantive list.** I recommend against it, now on
> measurement rather than argument: object-oriented smells against a prose deliverable, your checker's own rule
> forbids faulting work for a property nobody stated, and across twenty runs that list produced two surviving
> findings, one of which your own checker suppressed.

**The evidence the recommendation rests on**, pasted as the worker wrote it:

> **1. THE CHECKER IS THE ONLY CONTRACT WITH NO METHOD SECTION.** Grilling has `## How you grill`, and
> implementation, research and prototype each have their own. The checker has none — because its method *was* the
> skill you told it to go and find.
>
> **4. THE THING GENUINELY LOST IS SMALLER, AND ONE PIECE OF IT IS A LIVE DEFECT.** The sentence telling a checker
> that the standards are held **under the bar** — so a standards breach reports as `FAIL: the bar` and not `FAIL:
> acceptance condition` — sits inside the section being deleted, and the replacement text does not carry it
> forward. A checker will have standards and no idea which of its two verdicts they belong to.
>
> **5. A HALF OF YOUR OWN EARLIER INSTRUCTION WAS NEVER DONE.** Your words then, `verbatim`: *"For the checker, it
> need to find how to review, we should put it in the map with the list of stuff to follow and then give it to him
> when we spawn it so that it doesn't have to find it."* That names **two** things going into the map — *how to
> review*, and *the list of stuff to follow*. Only the list was ever written.
>
> **6. AND HERE IS THE MEASUREMENT.** Across about twenty checker runs that actually ran the found skill's
> standards pass, **exactly two of its findings survive anywhere in your record — and one of those was
> suppressed.** Against that, the highest-yield checks you have ever had ran on a **written-down** discipline and no
> skill at all. **A method in a file has outperformed a found skill by roughly twenty to one here.** And two
> checkers spent their single largest cost on the discovery step, and one died having produced nothing but that
> step.

**The human's answer**, `verbatim`:

> recommended ship it

**The option it takes, in the worker's own words** — quoted here because the reply is unreadable without it and the
prose is the worker's rather than the human's:

> **Ship it, as a section of the checker's contract**, roughly fifteen lines, with an effort's own rules file free to
> add method specific to that effort on top — which yours already does. Concretely: read the acceptance condition and
> split it into its parts before you read the work, because your `PASS` owes one line per part; keep the three axes
> separate and never merge or rerank them — the condition, the bar, and the standards, which report under the bar —
> so passing one cannot mask failing another; establish each part by a search you can name and hand back rather than
> by reading through; say plainly what you did not check. Nothing is taken from the barred skill.

***The manager's note.*** **Not a divergence**: the answer takes the worker's own recommendation. The reply reached
the payload as the worker wrote it, this node's question having been relayed unaltered.

### Attempt 2

*A fresh worker, given this node plus everything the human has already said on it, replayed in full and marked
settled. The human is not asked anything twice.*
