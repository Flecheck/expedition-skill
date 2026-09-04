# `CONTEXT.md` reserves the word `report` to the closing report, and the shipped contract now uses `pick report`

Type: grilling
Status: claimed

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
