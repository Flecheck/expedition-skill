# `CONTEXT.md` reserves the word `report` to the closing report, and the shipped contract now uses `pick report`

Type: grilling
Status: resolved

## Question

*Surfaced by [What the manager reports to the human, in one place](46-what-the-manager-reports.md)'s worker, and
pasted as it wrote it.*

> `CONTEXT.md`'s **Handover** entry carries `_Avoid_: report (the closing report owns that word)`, while
> `.claude/skills/expedition/SKILL.md` and this effort's map now use **pick report** as a settled name, chosen on a
> worker's own authority at flag `99.2` with `/naming` never run and the human never asked. Node 103 repairs the
> map's per-node uses and reaches neither the reservation nor node 95's clause 5, which still says *"named in that
> node's closing report instead."* Does `report` stay reserved, and if so what is the per-node message called? If it
> does not, what does the `_Avoid_` line become, and which sites change?

**Blockers, in the worker's words:** *"node 102 — its answer decides whether the pick report also carries a
`research` node's and an AFK `precondition` node's flags, which is part of what the name has to cover."*

## The manager's note at filing

*Not a change to anything above.*

**The blocker was satisfied before this node was written.** [Whether a research node's and an AFK precondition
node's flags settle at the pick report too](102-do-afk-nodes-flags-settle-at-the-pick-report.md) resolved between
node 46's worker writing this and the manager filing it: every kind's flags now settle at the first human moment its
close reaches, which for every kind but implementation is the pick report. So the name has to cover all of them, and
this node is open and unblocked.

## Interview

### Attempt 1, question 1 — written and queued, not yet put to the human

***Recorded by the manager as a queued payload, not as a question the human has been asked.*** Node 103's gate held
the channel when this arrived, and node 117's question was already queued ahead of it. **Pasted as the worker wrote
it**; the manager authored none of it and has taken no view on it.

> **The line in dispute.** `CONTEXT.md`'s **Handover** entry ends `_Avoid_: report (the closing report owns that
> word), return, payload, deliverable`. Every `_Avoid_` line in that file lists words not to be used *for that
> entry's own term*, so read by its placement this forbids calling a **handover** a report. Nothing in node 103's
> work does that; the prohibition is unbreached. What is inexact is the parenthetical's reason.
>
> **It was already inexact before node 103.** `CONTEXT.md` has carried a `Closing report` entry all along, and the
> shipped `expedition/SKILL.md` in the main checkout already says *"report the pick"* and *"the report accompanying
> the pick"*. So the word was in use for the manager's per-node message before this work named it.
>
> **Which tree holds what.** The main checkout's `.claude/` and `CONTEXT.md` contain no occurrence of "pick report"
> at all. The term lives in node 103's worktree, in four files: `CONTEXT.md` (the `Flag` and `Raise` entries),
> `expedition/SKILL.md` (six uses), `expedition/graph-conventions.md` (three), and `expedition-precondition/SKILL.md`
> (one). Separately, this effort's own `map.md` already uses it in the main checkout, because graph files are not
> committed per node. The two trees genuinely disagree right now.
>
> **Nothing defines it.** `CONTEXT.md` opens *"This glossary is the vocabulary the skill files are written in"*, and
> *pick report* is bolded as exact vocabulary in three shipped files with no entry anywhere — not in `CONTEXT.md`,
> not in `expedition/SKILL.md`'s `## Words used exactly`.
>
> **Two sites nobody has named yet, both outside node 103's change.** First, `expedition/SKILL.md` line 417 still
> reads *"Say in the report accompanying the pick…"* after node 103's edits, so the shipped file will hold two forms
> for one thing. Second, node 95 — an implementation node still `open` and unclaimed — has a clause 5 in its
> acceptance condition reading *"named in the report accompanying the pick — or, where the amendment is made after
> the node is claimed, named in that node's closing report instead."* That clause uses *closing report* for a
> **per-node** report, which directly contradicts `CONTEXT.md`'s `Closing report` entry. It changes under either
> answer here, and the node being unclaimed means it can still be fixed in place.
>
> **I ran `/naming` on the term, which had never been run.** Deriving the sentence from what the thing does rather
> than from its name: *the message the manager owes the human whenever a node closes, naming what closed, carrying
> every flag that node holds — it is where those flags settle — and naming whatever was started in response,
> expecting no answer.* "Pick report" round-trips to "a report about a pick", which is the contingent half.
> `SKILL.md` itself has cases where a node closes and no pick is reported (*"a pick that would exceed one is not
> started — it waits, and you say what it is waiting for"*), and cases where several are (*"you start enough work to
> fill every gap it leaves, which is sometimes more than one node"*). The tell is in
> `expedition-precondition/SKILL.md`, which cannot use the term without a relative clause: *"the **pick report** the
> manager sends when your node closes"*. That finding is the substance of the second question, not this one.
>
> **Settled on my own authority, invariant across both branches:** `CONTEXT.md` is owed an entry for the per-node
> message whatever it ends up called, placed under `## Talking to the human` alongside `Relay` and `Raise` rather
> than under `## Closing an effort` where `Closing report` sits. Also that node files and `map-history.md` are not
> repair sites — under the never-delete rule, prose written before a word changed keeps the old word.
>
> **Method skills:** I ran `/naming`, `/grilling` and `/domain-modeling`, leaving unrun the parts the hard rules
> override — `/grilling`'s "ask the whole frontier in one round" and its wait-for-the-user loop, and
> `/domain-modeling`'s instruction to edit `CONTEXT.md` inline and to offer an ADR.
>
> **ASK:** Does the word `report` stay reserved to the once-per-effort closing report across the whole vocabulary —
> so the per-node message must be renamed and lose the word entirely — or is the reservation only what its placement
> says, a ban on calling a **handover** a report, leaving two named reports to coexist?
>
> **RECOMMENDED:** The second: `report` is not reserved as a word, and never was. It rests on four things. The
> placement — every other `_Avoid_` line in the file scopes to its own entry, and reading this one as a global claim
> makes it the only exception. The history — `Closing report` and *"report the pick"* already shared the word before
> this work, so the parenthetical was overreaching when it was written rather than falsified by node 103. The shape
> of a glossary — two qualified compounds off one head noun is how a vocabulary distinguishes, not how it collides,
> and the same file already does this with `Code commit` and `Graph commit`. And the cost of the alternative —
> reserving the word would leave one report in a workflow whose manager's entire output to the human is reports.
>
> The repair, then, is two edits and no rename: narrow the parenthetical to state the constraint that is actually
> operative, which is direction of travel — a report goes to the human, a handover goes to the manager — so it reads
> something like `_Avoid_: report (a report goes to the human; a handover goes to the manager), return, payload,
> deliverable`; and add the missing glossary entry. That parenthetical is truer than the one it replaces, holds for
> both reports, and keeps the ban doing its work.
>
> **ALTERNATIVES:** Reserve `report` as a word and rename the per-node message — costs a rename across eight live
> sites and still leaves `closing report` holding the word, so it buys consistency it cannot deliver.
> Delete the parenthetical, leaving a bare `_Avoid_: report, return, payload, deliverable` — smallest possible edit,
> but `CONTEXT.md`'s refusals carry their reasons and this one's reason is worth stating correctly rather than
> dropping.
> Leave `CONTEXT.md` untouched and treat the parenthetical as harmless local prose — rejected because the map calls
> the glossary authoritative and its `_Avoid_` lines "the part that does the work", so a false reason there is a
> defect rather than stale prose the never-delete rule protects.

***The manager's note beside it, and not the worker's.*** **It found a live defect on an unclaimed node's acceptance
condition** — node 95's clause 5 uses *closing report* for a per-node report, contradicting `CONTEXT.md`'s own entry.
The manager has **not** touched node 95: amending a condition is node 82's act with its two guards, and this one is
not the manager's to make on a worker's report while the question that decides it is unanswered.

### Attempt 1, answer 1

**The human's word, `verbatim`**, written at the moment they spoke:

> ok for 107

**The option it takes, quoted in full and attributed to the worker who wrote it**, not to the manager:

> The second: `report` is not reserved as a word, and never was. It rests on four things. The placement — every other
> `_Avoid_` line in the file scopes to its own entry, and reading this one as a global claim makes it the only
> exception. The history — `Closing report` and *"report the pick"* already shared the word before this work, so the
> parenthetical was overreaching when it was written rather than falsified by node 103. The shape of a glossary — two
> qualified compounds off one head noun is how a vocabulary distinguishes, not how it collides, and the same file
> already does this with `Code commit` and `Graph commit`. And the cost of the alternative — reserving the word would
> leave one report in a workflow whose manager's entire output to the human is reports.
>
> The repair, then, is two edits and no rename: narrow the parenthetical to state the constraint that is actually
> operative, which is direction of travel — a report goes to the human, a handover goes to the manager — so it reads
> something like `_Avoid_: report (a report goes to the human; a handover goes to the manager), return, payload,
> deliverable`; and add the missing glossary entry.

**It agrees with the worker's recommendation**, so it is not a divergence. **The reply names the node**, which is the
fifth recorded instance of the human volunteering a scope where a bare assent would have been ambiguous — a fact node
117's worker measured and built its own recommendation on.

***The manager's note, and not the human's words.*** **What the manager did not read into it.** The reply is to the
question as asked — whether the word stays reserved — and the recommendation it assents to carries a *proposed
repair* alongside its answer, including one wording (*"a report goes to the human; a handover goes to the manager"*)
offered with *"something like"* by its own author. **The manager does not read the assent as fixing that exact
wording**, and marks that as the manager's reading rather than theirs. **Also not settled by this word:** the second
question the worker said it holds — whether *pick report* is the right name, its `/naming` run having found the term
round-trips to *"a report about a pick"* while the thing is neither always about a pick nor about only one — and the
node-95 clause-5 defect the worker found, which no word of theirs has reached.

### Attempt 1, question 2 — written, queued, and its premise stale

***Recorded by the manager as a queued payload, not as a question the human has been asked.*** Node 117's second
question was already queued ahead of it. **Pasted as the worker wrote it**; the manager authored none of it.

> **What your "ok for 107" settled.** `report` is not reserved as a word. The `_Avoid_` line under `CONTEXT.md`'s
> **Handover** entry is scoped to that entry and bans calling a *handover* a report, nothing more; two named reports
> may coexist. The repair that follows is a narrowed parenthetical plus the missing glossary entry.
>
> **I am not treating my proposed wording as fixed by that assent.** I offered *"a report goes to the human; a
> handover goes to the manager"* hedged with "something like", and I read your answer the same way the manager does —
> as taking the position, not the sentence. So what I hand back demands of the parenthetical only that it stop
> claiming one term exclusively owns the word and state the distinction that actually holds, with my wording carried
> as a recommendation the repair's worker may improve on.
>
> **What `/naming` found, which is this question.** Deriving the sentence from what the thing does rather than from
> its name: *the message the manager owes the human the instant a node closes, naming the node that closed, carrying
> every flag it holds — it is where those flags settle — and naming whatever was started in response; it awaits no
> answer.* "Pick report" round-trips to "a report about a pick", and the necessary subject of that sentence is the
> **close**, not the pick.
>
> **Two of my three objections weakened when I read the shipped text again**, and I am reporting that rather than
> pressing them. The case where nothing is started — *"a pick that would exceed one is not started — it waits, and
> you say what it is waiting for"* — still has a pick in it; it is the start that waits, not the pick. And the
> frontier-empty case is a different report altogether, the map routing it to the sweep and the report preceding a
> close.
>
> **What survives is one real defect, in the contract whose reader it hurts most.**
> `expedition-precondition/SKILL.md` cannot use the term without glossing it: *"the **pick report** the manager sends
> when your node closes"*. For that worker, "pick" refers to a **different node** than the one it just worked — the
> next one — while the thing being described is its own node's close and its own flags settling. A name needing a
> relative clause to say what it is about is the naming smell. Alongside it, a smaller one: the report may name
> several picks (*"you start enough work to fill every gap it leaves, which is sometimes more than one node"*), so
> the singular is loose.
>
> **Every alternative I generated is worse, and I want to be plain about why**, since that is what makes "keep it" a
> recommendation rather than inertia. `close report` sits one letter from `closing report` in the same glossary,
> where the two would mean per-node and per-effort — a trap, and `Closing report` already refuses its own
> near-synonyms. `node report` is near-contentless in a workflow where everything is a node. Dropping "report" for
> another head noun runs into terms already taken: `Manager note` is a different thing, and `handover` is the
> worker's word.
>
> **Settled on my own authority, by the rules rather than by preference:** the repair cannot ride node 103. Its
> acceptance condition names `CONTEXT.md`'s `Flag` entry only, and both of node 103's checkers reported the `_Avoid_`
> line and the missing entry as outside it — and node 82's widening rule, as node 95's clause 2 states it, explicitly
> does not reach "a new demand at any place". So the repair is its own implementation node, which I hand back on
> `NEW NODES`.
>
> **Also settled: node 95's clause 5 is a site, and not the repair node's to touch.** That clause says an amendment
> is *"named in that node's closing report instead"*, using `closing report` for a per-node report — which your
> answer makes unambiguously the wrong term, `Closing report` being the per-effort one. Node 95 is open and
> unclaimed, so under `CONTEXT.md`'s `Revision` entry it is fixed in place, and amending a condition is the manager's
> act. I record it as a site with that owner rather than writing it into a node's condition.
>
> **ASK:** Does the per-node message keep the name **pick report**, or is it renamed — and if renamed, to what?
>
> **RECOMMENDED:** Keep **pick report**, and fix the one sentence rather than the name. Four grounds. The objection
> that would have forced a rename dissolved on re-reading: there is no case where the report carries no pick at all.
> The defect that survives is a clarity problem in a single sentence of one contract, and is cheaper to fix there —
> that contract can say the report closes the worker's node and also names what the manager started, so "pick" stops
> looking like the subject. Every candidate is worse, for the reasons above. And the name has a virtue nobody has
> stated: the shipped instruction is already *"Pick it yourself and report the pick"*, so the term and the act it
> names share a root, which is what makes it findable.
>
> Two things I would rather accept out loud than leave silent. The singular understates a report naming several
> picks. And the name names the trigger while the duty three nodes have now hung on it — flags settling — attaches to
> the close. I am recommending you take both knowingly, as the price of not renaming eleven occurrences and forcing a
> correction round on work already at your gate.
>
> One bonus if it stays: `CONTEXT.md` has no entry for **pick** either, so the glossary entry the repair adds can
> define the act and the report together, in one place.
>
> **ALTERNATIVES:** `close report` — round-trips correctly, and disqualified by sitting one letter from `closing
> report` for a different scope.
> `node report` — no collision, but says almost nothing in a graph workflow.
> A non-report head noun such as `pick note` or `close note` — sidesteps the word entirely, and collides with
> `Manager note`, which is already something else.
> Rename and re-open node 103 — the only option that gets a fully clean name into the shipped files in one pass, at
> the cost of a correction round on work you are about to approve.

***The manager's note, and not the worker's: this payload was not relayed as written, because one of its premises
went stale while it was being composed.*** It says the price of renaming is *"forcing a correction round on work
already at your gate"* and offers *"Rename and re-open node 103"* as an alternative. **Node 103 is resolved and
landed as commit `106380a`.** There is no gate to force a round on and nothing to re-open; a rename would be an edit
in a new node against landed files. That changes the cost the recommendation is priced against, and it is a cost the
human was going to be asked to weigh. **The manager corrected the fact to the worker rather than correcting the
question**, which is the worker's to revise or to stand by.

#### The revised second question, superseding the one above

***The worker was given the fact that node 103 had landed and revised its own payload. The version above is not
deleted; this one supersedes it.*** The worker's framing of what it did, in its own words: *"Node 103 landing removes
a price my recommendation partly rested on. That obliges me to re-decide rather than restate, so I have re-run the
candidates with cost nearly out of the comparison — and one alternative gets stronger, not weaker, when cost falls.
The recommendation survives, on narrower grounds."*

**Pasted as it wrote it. Only the parts that changed are reproduced; the unchanged parts of the payload above stand.**

> **ABOUT:** Whether *pick report* is the right name for the manager's per-node message, now that it is allowed to
> keep the word "report". It is decided now because the name was chosen on a worker's own authority at flag `99.2`,
> `/naming` had never been run on it, and the term is live in four shipped files — so a rename gets cheaper the
> sooner it happens and dearer every time the term is used again.
>
> **My first version of this question was priced against a gate that no longer exists.** Node 103 landed as commit
> `106380a` while I was writing, so there is no correction round to force and nothing to re-open; a rename would now
> be one more mechanical edit inside the repair node I am handing back either way. I have re-run the comparison with
> that cost removed rather than restating the old answer.
>
> **And the rename's true footprint is smaller than the raw count suggests** — which cuts against what I am about to
> recommend, so you should have it. Eleven occurrences sit in four shipped files. `map.md` and `decisions.md` would
> **not** be touched: the map states that prose written before a word changed keeps the old word and the glossary is
> authoritative. Node 95's clause 5 needs correcting under either answer and is the manager's act, not this node's.
> So the rename is four files.
>
> **ASK: Q1.** Does the per-node message keep the name **pick report**, or is it renamed — and if renamed, to what?
>
> **RECOMMENDED:** Keep **pick report**. With cost nearly out of the comparison the recommendation now rests on one
> thing only, and I would rather state it that narrowly than dress it up: **no better name exists among the
> candidates.** `close report` round-trips correctly and sits one letter from `closing report`, where the two would
> mean per-node and per-effort — the worst kind of collision, between two terms a reader meets in the same glossary.
> `node report` collides with nothing and says almost nothing in a workflow where everything is a node. The note
> family — `pick note`, `close note` — is blocked by `Manager note`, already something else.
>
> Two lesser things support it. The shipped instruction is already *"Pick it yourself and report the pick"*, so the
> term shares a root with the act it names, which is what makes it findable. And `CONTEXT.md` has no entry for
> **pick** either, so the entry the repair adds can define the act and the report together.
>
> What I am asking you to accept knowingly, no longer as a price but as a residue: the singular understates a report
> naming several picks, and the name names the trigger while the duty three nodes have hung on it — flags settling —
> attaches to the close. The `expedition-precondition` sentence is fixable in place, by having it say the report
> closes the worker's own node *and* names what the manager started, so "pick" stops reading as the subject.
>
> **ALTERNATIVES: Rename `closing report`, then take `close report` for this one.** The only path to a fully clean
> pair — `close report` per node, and something like *final report* or *effort report* per effort — and the one
> option that gets *better* now that node 103 has landed, since nothing is mid-flight to disturb. I set it aside
> rather than recommend it because it reaches beyond what this node asks: `Closing report` is settled vocabulary with
> its own refusals, and renaming the effort-level report to fix the node-level one is a larger act than the defect
> warrants. It is here because it is genuinely available and you may want it.
> `close report` alone — blocked by that same near-collision unless the above is done.
> `node report` — no collision, near-contentless.
> `pick note` / `close note` — blocked by `Manager note`.

***The manager's note beside it, and not the worker's.*** **The correction did what a correction should and the
manager records it as evidence rather than as praise.** Given one stale fact, the worker did not defend its answer:
it re-ran the comparison with the cost removed, reported that the footprint is **smaller** than it had implied —
against its own recommendation — and promoted an alternative it had previously not stated at all, on the ground that
removing the cost makes that alternative *stronger*. The recommendation survived on one narrower ground.

**One small inconsistency between two workers, recorded and not resolved.** This payload numbers its single ask
`Q1`. Node 117's worker settled on its own authority, in the same hour, that *"no number on a lone question: the
presence of numbering is itself the signal that the payload holds more than one."* Neither reading has reached the
human, node 117's second question — what a bare assent means against a numbered round — being the live one. **The
manager relayed neither convention as a rule and takes no view.**

### Attempt 1, answer 1 to Q1 — a divergence

**The human's word, `verbatim`**, written at the moment they spoke:

> We can rename the closing report to effort closing report and use closing report or close report for the node
> report. The effort closing report is rarely done in practice compared to the node one, so we can do effort closing
> report and node closing report, shortened to closing report as it is the one used the most and should be
> understandable in the context where it is used ?

**`DIVERGENCE`. This does not take the recommendation.** The worker recommended *"Keep **pick report**"* on the
stated ground that **no better name exists among the candidates**, and it disqualified `close report` specifically
because it *"sits one letter from `closing report`, where the two would mean per-node and per-effort — the worst kind
of collision, between two terms a reader meets in the same glossary"*. **The human has taken the alternative the
worker set aside**, which the worker described as *"the only path to a fully clean pair"* and *"the one option that
gets better now that node 103 has landed"*, and offered *"because it is genuinely available and you may want it"*.

**The option they took, quoted in full and attributed to the worker who wrote it**, not to the manager:

> **Rename `closing report`, then take `close report` for this one.** The only path to a fully clean pair — `close
> report` per node, and something like *final report* or *effort report* per effort — and the one option that gets
> *better* now that node 103 has landed, since nothing is mid-flight to disturb. I set it aside rather than recommend
> it because it reaches beyond what this node asks: `Closing report` is settled vocabulary with its own refusals, and
> renaming the effort-level report to fix the node-level one is a larger act than the defect warrants. It is here
> because it is genuinely available and you may want it.

**But their proposal is not that alternative as written**, and the difference is the whole of what is left to decide.
The worker's version renames the effort-level report to something *distinct* — *"final report or effort report"* — so
the two names share no head. **Theirs keeps a shared head and disambiguates by prefix**: `effort closing report` and
`node closing report`, and then proposes that the node one **shortens to `closing report`** on the ground that it is
the more frequent and that context will carry it.

***The manager's note, and not the human's words. Three facts the manager holds and is recording rather than
deciding.***

1. **Their reply is not fully determinate.** It offers *"closing report or close report"* for the node-level term and
   does not choose, then converges on `node closing report` shortened to `closing report`. Under [node
   117](117-questions-sent-in-batches.md)'s rule a reply settles what it names, and this names two candidates. The
   manager has **not** picked between them.
2. **Their shortening proposal inverts a term already in use rather than introducing a new one.** `closing report`
   currently denotes the once-per-effort report — in `CONTEXT.md`'s own entry, in the manager's contract, in
   `graph-conventions.md`, in `map.md`, and in this effort's record. Under their proposal the unqualified form comes
   to denote the **node-level** one. So every unqualified existing use would either need a prefix or would silently
   change meaning, and the never-delete rule means the record keeps its old uses unaltered. **That is a cost the
   worker's version does not have**, and it is the exact hazard the worker was avoiding by refusing a shared head —
   arrived at from the other direction.
3. **Their reply ends in a question mark.** The manager reads that as inviting a view rather than as issuing a
   decree, and **that view is the worker's to give, not the manager's** — the worker holds the interview. It has been
   put back to the worker with the three facts above and no manager position.

### Attempt 1, question 2 — written and queued, not yet put to the human

***Recorded by the manager as a queued payload.*** Node 116's gate held the channel and node 113's first question was
already queued ahead of it. **Pasted as the worker wrote it**; the manager authored none of it and has taken no view.

> **ABOUT:** One thing is left: whether an unqualified **closing report** is allowed to change meaning. Your answer
> renames the pair, which makes the bare form the node-level report where today it is the effort-level one
> everywhere. That is the last decision in this node; everything else your answer settled or I have.
>
> **Your answer is taken, and my recommendation lost.** The pair is **effort closing report** and **node closing
> report**, sharing a head and disambiguated by prefix. *pick report* disappears — it lived for one commit, so that
> costs nothing.
>
> **How I read the part that offered two candidates**, so you can correct it: your reply floats "closing report or
> close report" and then concludes *"so we can do effort closing report and node closing report, shortened to closing
> report"*. I read the conclusion as superseding the list, and `close report` as raw material you set aside — because
> "shortened to closing report" only parses under the shared head; `close report` does not shorten to `closing
> report`. So I did not spend a question confirming it. If that reading is wrong, it is the one thing to correct.
>
> **The repair, measured on master now that node 103 has landed.** *pick report*: 14 occurrences in 4 files —
> `expedition/SKILL.md` (8), `graph-conventions.md` (3), `CONTEXT.md` (2), `expedition-precondition/SKILL.md` (1).
> Effort-level *closing report*: 6 more in the same 3 files, needing the prefix. Plus one entry renamed and one
> added. About 21 mechanical edits in 4 files, one node, no ambiguity in any of them.
>
> **The flip's blast radius, which is the question.** "closing report" appears **197 times across 35 files** in this
> effort's record — `map.md`, `decisions.md`, `map-history.md` and 32 node files — and every one means the
> effort-level report. The never-delete rule keeps all 197 unaltered. The map's standing answer covers this: *"Prose
> written before a word changed still says the old word: that is the never-delete rule rather than drift, and the
> glossary is authoritative."*
>
> **But that rule was written for a rename, and this is a flip**, which is the one distinction I want to put in front
> of you. After a rename, stale prose says a word that is no longer vocabulary — visibly old, and a reader checks the
> glossary. After a flip, stale prose says a word that is *current* vocabulary and means the opposite thing —
> invisibly old, and a reader has no cue to check anything. 197 sites is the largest stale set this effort has
> created in one decision.
>
> **Your reason for the flip holds up on measurement, and I checked it because it is the thing that decides this.**
> You said the node-level one is used most. That is true of the act, and it is also true of the word in the shipped
> files: 14 node-level against 6 effort-level. So the short form does go to the commoner term.
>
> **Which `CONTEXT.md` entries the repair node needs to own**, since node 113 found that file has a separate stale
> entry and someone else will be editing it: the `Handover` entry's `_Avoid_` line; the `Closing report` entry,
> renamed; a new entry for the node-level report under `## Talking to the human`; and the `Flag` and `Raise` entries,
> which both name these reports in prose. It does **not** touch the `grilling` entry — node 113's "one question at a
> time" staleness is not mine and my repair should not silently absorb it.
>
> **ASK: Q2.** May an unqualified **closing report** mean the node-level one, as you proposed — accepting that 197
> existing uses meaning the effort-level one become invisibly stale? Or must the shipped files always carry the
> prefix, so the bare form is never written again and nothing flips?
>
> **RECOMMENDED:** Take the flip as you wrote it, and disarm it with one sentence in the glossary: the `Effort
> closing report` entry states that an unqualified "closing report" means the node-level one, and that prose written
> before this change means the effort-level one. That puts the cue in the one file the map already declares
> authoritative and that every worker is required to read before writing anything — which is the exact mechanism this
> effort already relies on for stale vocabulary, used here for a case it was not written for. Cost: one sentence. It
> keeps your shortening, keeps the commoner term short, and gives the 197 the cue they would otherwise lack.
>
> I am recommending your option rather than mine, and not merely deferring to it: the flip's cost turned out to be
> one sentence rather than a hazard, and the measurement backs your frequency reason.
>
> **ALTERNATIVES:** Mandate the prefix in the shipped files, bare form never written — nothing flips and the 197 stay
> correct by construction, at the cost of the shortening you asked for and of two three-word terms in files that use
> them 20 times.
> Flip it and say nothing — saves one sentence, and leaves the largest invisible stale set this effort has made with
> no cue anywhere.

***The manager's note beside it, and not the worker's.***

**The indeterminacy the manager flagged is resolved, by the worker and on a textual ground rather than by
preference.** The manager recorded that the human's reply named two candidates and did not choose. The worker read
the conclusion as superseding the list, on the ground that *"shortened to closing report" only parses under the
shared head; `close report` does not shorten to `closing report`* — and marked the reading as its own, correctable in
one line, rather than spending a question on it. **The manager accepts that this is the worker's reading to make**,
having put the fact to it without a position.

**The distinction the worker drew is new to this graph and the manager had not seen it.** The map's standing answer
for stale vocabulary — *"prose written before a word changed still says the old word … and the glossary is
authoritative"* — was written for a **rename**, where stale prose uses a word that is no longer vocabulary and so
reads as visibly old. **This is a flip**, where stale prose uses a word that *is* current vocabulary and means the
opposite. The manager's own note had named the flip as a cost; it had not seen that the effort's existing mitigation
does not reach it.

**One number the manager records because it bears on more than this node.** *"closing report"* appears **197 times
across 35 files** in the record. Whatever is decided here, that is the largest population of text this effort has put
at risk of meaning something else, and nothing on the graph watches for it.

### Attempt 1, answer 1 to Q2

**The human's word, `verbatim`**, written at the moment they spoke:

> ok for 107

**A bare assent, and it takes the recommendation.** Under [node 117](117-questions-sent-in-batches.md)'s settled rule
a bare assent settles **every recommendation in that payload and nothing that is not a recommendation**. This payload
held one ask and one `RECOMMENDED`, so what is settled is the worker's own recommendation in the worker's own words:

> Take the flip as you wrote it, and disarm it with one sentence in the glossary: the `Effort closing report` entry
> states that an unqualified "closing report" means the node-level one, and that prose written before this change
> means the effort-level one.

**No divergence.** The worker recommended the human's option rather than its own, and the human's word takes it.

***The manager's note, and not the human's words. Two facts recorded rather than decided.***

1. **The assent is determinate even though it names the node rather than the number.** Node 117's rule makes an
   unnamed question unanswered rather than parked — but only one number was in flight on this node, so naming the
   node reaches exactly one ask and nothing is left unnamed. Had a second question been queued behind it, this reply
   would not have been readable.
2. **The worker's *reading* of the two-candidate reply is not covered by what the human just said, and the manager
   takes no view on it.** The worker set out how it read *"closing report or close report"* — the conclusion
   superseding the list — and offered it as *"the one thing to correct"* rather than as an ask or a recommendation.
   The human corrected nothing. **Whether an uncorrected stated reading counts as confirmed is governed by nothing on
   the graph**: node 117's rule speaks of recommendations, and this is neither a recommendation nor a question. The
   worker holds the interview and may spend a question on it. Recorded here because it is a **gap in the batching
   rule node 117 has just landed**, and not a fact about this node.

***The manager's later note, added when the handover arrived.*** **The worker did not proceed on "uncorrected", and
said so.** Its words: *"I proceed on my reading, and on stronger ground than 'uncorrected' — the recommendation they
assented to is only coherent under the shared-head pair, so the reading is entailed by it rather than merely
unchallenged."* It carried the judgement as flag `107.2` so it can be overturned cheaply. **The gap in node 117's
rule that the manager named above is untouched by that** — the worker got past it on this node's particular facts
rather than by settling the general question.

## Answer

*Attempt 1's handover, pasted as its worker wrote it. The manager authored none of it.*

**`report` is not reserved as a word, and never was.** `CONTEXT.md`'s `_Avoid_` lines are each scoped to their own
entry, and the one under **Handover** — `_Avoid_: report (the closing report owns that word), return, payload,
deliverable` — forbids calling a *handover* a report. Nothing breached it. What overreaches is the parenthetical: it
asserts that one term exclusively owns the word, and that assertion was already untrue when written, `CONTEXT.md`
having carried a `Closing report` entry all along and `expedition/SKILL.md` having said *"report the pick"* and *"the
report accompanying the pick"*. It is repaired rather than obeyed, and the ban it justifies stands untouched. The
distinction that actually holds is **direction of travel — a report goes to the human, a handover goes to the
manager** — which is true of every report the workflow has.

**The vocabulary gains a pair, and `pick report` is retired.** The human's words, `verbatim`: *"We can rename the
closing report to effort closing report and use closing report or close report for the node report. The effort
closing report is rarely done in practice compared to the node one, so we can do effort closing report and node
closing report, shortened to closing report as it is the one used the most and should be understandable in the
context where it is used?"*

- **effort closing report** — what the manager hands the human once the frontier empties: what was decided, what
  landed, and every flag still outstanding. Once per effort.
- **node closing report** — the message the manager sends the instant a node closes: the node that closed, every flag
  that node holds carried in full (this being where those flags settle), and whatever work the manager started in
  response. It awaits no answer and takes no place in the human's question queue.
- **An unqualified `closing report` means the node-level one**, that being the one used most — a frequency claim
  confirmed on measurement, the shipped files using the node-level term 14 times against the effort-level term 7.

**`pick report` was wrong for a reason worth recording, since it cost a commit.** `/naming` had never been run on it;
it was chosen at flag `99.2` on a worker's own authority. Run here, the method derives the sentence from what the
thing does — *the message the manager owes the human when a node closes* — while "pick report" round-trips to *"a
report about a pick"*, naming the consequence rather than the subject. The tell was in
`expedition-precondition/SKILL.md`, which could not use the term without glossing it: *"the **pick report** the
manager sends when your node closes"*, where "pick" names a **different node** than the one that worker just worked.
The new name dissolves that defect rather than patching the sentence.

**The flip is accepted, and disarmed by one sentence in the glossary.** The bare form means the node-level report
from now on, where today it means the effort-level one in all 197 of its occurrences across 35 files of this effort's
record. The never-delete rule keeps every one of them unaltered, and the map's standing answer — *"Prose written
before a word changed still says the old word: that is the never-delete rule rather than drift, and the glossary is
authoritative"* — was written for a **rename**, where stale prose says a word that is no longer vocabulary and is
visibly old. **This is a flip**, where stale prose says a word that is current vocabulary and means the opposite
thing, and is invisibly old. So the glossary states the cue explicitly: the unqualified form means the node-level
report, and prose written before this change uses it for the effort-level one. One sentence in the file every worker
must read before writing anything, which is the mechanism this effort already relies on, applied to a case it was not
written for.

**How the two-candidate reply was read, recorded because a later reader cannot otherwise tell.** The reply floats
*"closing report or close report"* and then concludes *"so we can do effort closing report and node closing report"*.
This node proceeds on the conclusion superseding the list, and on `close report` being raw material set aside. The
ground is not that the reading went uncorrected but that it is **entailed** by the recommendation the human then
assented to: an `effort closing report` entry and an unqualified `closing report` meaning the node one are coherent
only under the shared-head pair, and `close report` neither shortens to `closing report` nor leaves the bare form
meaningful. Carried as flag `107.2` so it can be overturned cheaply if the entailment is rejected.

**The repair sites, all four files, measured on master at commit `106380a`.** `CONTEXT.md`;
`.claude/skills/expedition/SKILL.md`; `.claude/skills/expedition/graph-conventions.md`;
`.claude/skills/expedition-precondition/SKILL.md`. Fourteen occurrences of `pick report` become the node-level term;
five occurrences of `closing report` take the `effort` prefix; the `Closing report` entry is renamed; one entry is
added; the `Handover` `_Avoid_` parenthetical is rewritten; and `expedition/SKILL.md`'s surviving periphrasis *"the
report accompanying the pick"* becomes the term. That is one implementation node, reported below.

**Three things are not this node's, and are named so they are not lost.**

- **Node 95's clause 5**, on an `open` and unclaimed acceptance condition, reads *"named in the report accompanying
  the pick — or, where the amendment is made after the node is claimed, named in that node's closing report
  instead."* It uses a periphrasis for the term and, worse, `closing report` for a **per-node** report. Under this
  answer the bare form does now mean the node-level one, so the second half accidentally becomes correct and the
  clause is still wrong in wording. Amending a condition is the manager's act, and `CONTEXT.md`'s `Revision` entry
  puts an unstarted node's repair in place, so this is the manager's to fix before node 95 is claimed.
- **`map.md`, `decisions.md`, `map-history.md` and the node files are not repair sites.** The map's own rule keeps
  their old words, and the glossary is authoritative over them.
- **`CONTEXT.md`'s `grilling` entry**, whose *"one question at a time"* node 113 superseded, is node 113's and is
  deliberately not absorbed by this repair.

## Flags this node raised

`107.1` — `ASSUMPTION`, in the worker's own words:

> Settled before the first question, and invariant across every branch it could have taken, that `CONTEXT.md` is owed
> an entry for the per-node report whatever it ended up called, and that the entry belongs under `## Talking to the
> human` beside `Relay` and `Raise` rather than under `## Closing an effort`. Ground: the file's own preamble says
> *"This glossary is the vocabulary the skill files are written in"*, and the term was bolded exact vocabulary in
> three shipped files with no entry anywhere. Both of node 103's checkers reported the gap independently and neither
> could act on it. The human was never asked, this being a consequence of the file's stated role rather than a
> choice.

`107.2` — `ASSUMPTION`, in the worker's own words:

> The human's answer to Q1 named two candidates for the node-level term and then converged on one. This node
> proceeded on the converging clause rather than spending a question, on the ground that the pair is entailed by the
> Q2 recommendation the human then assented to — `close report` does not shorten to `closing report`, and an
> unqualified `closing report` meaning the node one presupposes the shared head. Recorded because node 117's rule
> speaks of recommendations and says nothing about a stated reading left uncorrected, so nothing on the graph makes
> this confirmed.

`107.3` — `ASSUMPTION`, in the worker's own words:

> The `_Avoid_` parenthetical's replacement wording is held as recommended rather than fixed. The human's *"ok for
> 107"* was assent to a recommendation offered with "something like", so the repair node's condition demands the
> **properties** the parenthetical must have — that it stop claiming exclusive ownership of the word and state the
> human/manager direction of travel — and carries the wording as a recommendation its worker may improve on. The
> manager proposed this reading first and this worker agrees with it.

## Nodes this node surfaced

One, minted as [node 137](137-rename-the-two-reports-and-repair-the-avoid-line.md). Its name, kind, blockers,
question and acceptance condition were all written by this node's worker and are pasted there.

## What this node's work invalidates

*Pasted as the worker wrote it.*

- **[Node 103](103-carry-the-pick-report-settling-moment.md)** — resolved and landed as commit `106380a`. Its answer
  stands entirely; its **vocabulary does not**. The four files it shipped name the per-node message `pick report`,
  which this node retires. Node 103's worker predicted this exactly, reporting the collision at its gate and
  declining to act on it because node 107 was open.
- **[Node 102](102-do-afk-nodes-flags-settle-at-the-pick-report.md)** — resolved. Its answer routes every kind's
  flags to *"the pick report that closes it"*. The routing is untouched; the term in it is superseded.
- **[Node 99](99-flags-arrive-after-the-node-s-human-moment.md)** — resolved, and **flag `99.2` is overturned**. That
  flag records the name `pick report` chosen on a worker's own judgement; the human has now named the thing itself,
  so the judgement it flagged has been taken out of the worker's hands rather than confirmed.
- **[Node 14](14-naming.md)** — resolved. It fixed the vocabulary and the map records `CONTEXT.md` as holding *"50
  term entries and 40 `_Avoid_` lines"*. Both counts move: one entry is added and one `_Avoid_` line's text changes.
- **Not invalidations, said explicitly so a reader does not think they were missed:** the 197 occurrences of `closing
  report` meaning the effort-level report across 35 files of this effort's record, on nodes 10, 19, 23, 27, 46, 75,
  76, 91 and others. The never-delete rule keeps them, the glossary is authoritative over them, and clause 4 above is
  what makes their staleness visible.

***The manager's note.*** **Two of these are the manager's own work rather than a later node's.** Node 99's flag
`99.2` is settled and marked, so overturning it is a graph edit; and the map's *"50 term entries and 40 `_Avoid_`
lines"* count moves when node 137 lands rather than now. **Node 95's clause 5 is the third**, named in the answer
above rather than here.

## Retrospective — attempt 1

*Pasted as the worker wrote it.*

**What I had to hunt for that the node or the spawn could have told me.** Three things, and one of them decided the
node.

*Which tree holds what.* The spawn warned me the two trees disagreed and told me to say which one I read a claim from
— that warning was worth its length and I used it. But the actual state took four greps to establish, and one of them
lied to me: my first repo-wide `grep | head -60` silently truncated before reaching `.claude/` and `.worktrees/`, and
I nearly concluded the shipped files were clean when I had simply not seen them. I caught it only because the
manager's note said four files carried the term and my grep showed none. **A spawn that hands a worker the term's
occurrence counts per file, per tree, would have removed the whole hunt and the near-miss with it.** That data is one
command the manager could run once.

*Whether node 95's clause 5 still said what it was quoted as saying.* The spawn flagged this as unverified and
unasserted, which was exactly right and exactly useful. Verifying it cost one grep and one read. Worth keeping as a
pattern — a named unverified claim is much cheaper to check than an unnamed assumption is to discover.

*Whether the report is owed when no pick happens.* Nothing told me; I had to read `### Picking the next node` whole.
This was the load-bearing fact of my first recommendation and **re-reading it is what dissolved two of my three
objections** — the pick is still made when the start waits. I would have shipped a worse question without it, so the
hunt earned its cost.

**What I read and did not use.** The map, in the main: I read all 107 lines cold as the contract requires, and used
the never-delete rule, the glossary-is-authoritative line, the flag-settling bullet, the four writing rules and the
bar. The landing policy, the dogfood target, the code-slot count, the firstmate fog, the out-of-scope section and
most of `## Not yet specified` bore on nothing here. That is the map doing its job for other nodes, not waste — but a
**grilling node about a word** needs perhaps a fifth of it. `decisions.md` I scoped by grep as instructed and used
two lines of the ten it returned. `/domain-modeling` returned almost nothing I could act on: its whole method is to
edit `CONTEXT.md` inline and offer ADRs, both of which my hard rules forbid, so I invoked it, found one usable
instruction ("challenge against the glossary", which I was already doing), and left the rest unrun. `/grilling` gave
me one genuinely useful idea — the frontier, which is what told me the reservation question gates the name question —
and its round format and wait-for-the-user loop are overridden by the hard rules, so I ran neither. `/naming` was the
one that paid: it produced the finding, and it is the skill the map names for terminology and that nobody had run.

**What would have made this node easier.** Four things.

1. **The occurrence counts, per file per tree, in the spawn.** As above. This is the single biggest saving available
   and it is mechanical.
2. **Knowing node 103 was about to land.** I priced a recommendation against a gate twice, in a payload that then had
   to be revised because the gate closed while I composed it. The manager caught it, which is the system working —
   but a spawn line saying *"node 103 is at its gate and may land at any moment"* would have stopped me leaning on a
   transient fact at all. **A worker cannot tell which of the facts it is handed are about to expire, and only the
   manager can.**
3. **The rules changed under me twice mid-node** — node 117 on multi-question payloads, node 113 on the method-skill
   lines in my own contract. Both arrived as manager notes, which worked. But I was invoking `/grilling` and
   `/domain-modeling` under a contract clause that node 113 was in the process of deleting, and I spent tokens on
   `/domain-modeling` for one usable line. **A worker working the contract that is itself being edited is a hazard
   specific to this effort**, and it would be cheaper if a spawn said which of the contract's own instructions are in
   flight.
4. **Nothing told me `flags.md` was off-limits until my contract did, after I had already seen seven of its lines**
   in the incidental output of a repo-wide grep. I did not open the file and did not use those lines as sites. But
   **a worker forbidden to read a file will hit it by grep**, and the ban is stated as "leave it unread" rather than
   "do not rely on its contents", which is the rule I actually needed.

**What I found stale, wrong, or contradicting something else.** Five things, in descending order of consequence.

1. **`CONTEXT.md`'s `_Avoid_` parenthetical was already false when it was written**, not falsified by node 103 as all
   three agents at node 103's gate believed. `Closing report` and *"report the pick"* predate the collision. Both
   checkers described it as *"the reason inside one going stale"* and it never was current.
2. **`expedition/SKILL.md` will hold two names for one thing until the repair lands** — *"the report accompanying the
   pick"* at the acceptance-conditions material, along `pick report` eight times. Node 103's diff did not reach it
   and nobody reported it; I found it only by grepping for periphrases rather than for the term.
3. **Node 95's clause 5** uses `closing report` for a per-node report, contradicting `CONTEXT.md`'s entry. Reported
   by node 46's worker as a quote and, as far as I can tell, never checked against the file until now.
4. **My own count was off by one in a payload the human read.** I told them 6 occurrences of `closing report` would
   take the `effort` prefix; it is 5, the sixth being the `_Avoid_` line that clause 5 rewrites separately. Corrected
   in the condition. It did not change the decision, and I record it because a number in front of the human should be
   right.
5. **`decisions.md`'s node 10 entry uses the word `completion report`**, which `CONTEXT.md`'s `Closing report` entry
   explicitly refuses by name. Old prose under never-delete, so not a defect — but it is a live example of why clause
   4's cue matters: a reader cannot tell a refused word from a current one without the glossary, and after a **flip**
   they cannot tell a current word from an inverted one either.

***The manager's note on the retrospective, and not the worker's.*** **Its item 4 corrects a number the manager
relayed.** The manager put *"6 more in the same 3 files"* in front of the human, taken from this worker's own earlier
payload; the true figure is 5. The worker found and corrected it unprompted. **Its "occurrence counts in the spawn"
ask is now the third such ask on the record** — node 128's worker and node 133's worker made the same one in the same
hour, each about a different mechanical fact. **The manager has still not minted a node for it.**
