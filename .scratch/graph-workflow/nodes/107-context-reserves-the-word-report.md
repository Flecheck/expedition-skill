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
