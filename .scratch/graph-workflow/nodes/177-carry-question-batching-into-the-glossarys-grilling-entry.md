# Carry intra-node question batching into the glossary's grilling entry

Type: implementation
Status: resolved

Blocked by: none

## Question

*Surfaced by [Carry intra-node question batching into the grilling worker contract](126-carry-question-batching-into-the-grilling-contract.md)'s worker, and pasted as it wrote it.*

> `CONTEXT.md` defines the node kind **grilling** as *"A decision only the human can make, reached by interviewing them
> one question at a time"*, and its **Relay** entry as the payload carrying *"a worker's question"* in the singular.
> Node 126 has removed both claims from the grilling worker contract, so the glossary — which the map declares
> authoritative for a term — now contradicts the shipped contract. Neither node 126's condition nor node 127's reaches
> this file.

**Blockers, in the worker's words:** *"none. Its subject exists only once node 126's change lands, so it is worked
after that gate rather than blocked by an edge."*

## Acceptance condition

*Written by node 126's worker. Pasted as it wrote it, and not the manager's.*

> 1. `CONTEXT.md`'s entry for the node kind **grilling** does not say the decision is reached one question at a time,
>    and nothing in that entry limits a worker to putting one question to the human at once.
> 2. `CONTEXT.md`'s **Relay** entry states that what a relay carries may hold more than one of one worker's questions,
>    rather than describing a worker's question in the singular only.
> 3. Both entries keep their existing `_Avoid_` and `_Note_` lines, and no other entry in the file is required to
>    change by this condition.
> 4. No other line in `CONTEXT.md` states that a worker puts one question at a time to the human, or that exactly one
>    *question* is in front of them. A statement that exactly one *thing awaiting a reply* is in front of them is
>    permitted and is not what this forbids.

## The manager's note at filing

*Not a change to anything above.*

**Its blocker is discharged: [node 126](126-carry-question-batching-into-the-grilling-contract.md) landed as
`8cc9b79`.** Its author wrote no edge and said why; the manager has added none.

**Two agents found this independently.** Node 126's worker reported it on its handover, and node 126's **checker** —
blind to the record and to that handover — reached `CONTEXT.md:114` from the other side and asked whether the human
wanted it amended. The checker also ran an enumerator over the shipped files and cleared two further hits as
non-defects, naming them so nobody re-derives them: `expedition-prototype/SKILL.md`'s own one-at-a-time rule, which is
a different node kind's scope decision, and `expedition/SKILL.md`'s line about concurrent nodes queueing, which stays
true. Its `CONTEXT.md:29` hit is a false positive. **The manager records those three as the checker's findings and
asserts nothing about them**; clause 4 of the condition above is what reaches them, and it is the condition's author's
wording rather than the manager's.

**The human saw the checker's question at node 126's gate and answered it in neither direction**, approving the node.
The manager records the question rather than reading approval as an answer to it.

## Flags

*All three are the worker's own text, pasted. The ids and links are the manager's bookkeeping and nothing else.*

`177.1` **· settled** `ASSUMPTION` — **The entries state the batching rule positively rather than merely dropping the old claim.** Clause 1 demands only that the `grilling` entry not say *one question at a time* and not limit a worker to one question at once, which deleting six words would have satisfied. I wrote the rule in instead. Ground: `CONTEXT.md`'s stated job is stopping a settled term from drifting back, which is what its `_Avoid_` lines do, and a silence records nothing for the next reader. Nobody was asked.

`177.2` **· settled** `ASSUMPTION` — **`Relay` also states that a payload never carries a second worker's questions.** The condition asks only that the entry admit more than one of *one worker's* questions. I added the cross-node refusal, which is the other half of node 117's answer — batching adopted inside a node, refused across them — because an entry saying a payload may hold several questions and stopping there invites the reading that two nodes' questions may share one. Nobody was asked.

`177.3` **· settled** `ASSUMPTION` — **Superseded text was deleted rather than marked superseded.** The map's never-delete rule names files *in the graph*; `CONTEXT.md` is shipped. Nothing states in one place that the rule stops at shipped files, so I settled it from precedent — node 133's commit `4000830` and node 126's commit `8cc9b79` both delete plainly from shipped contracts — and from the file's purpose, a glossary of current meanings. Nobody was asked.

## Review

### Checker run 1 — `PASS`

*Pasted as the checker wrote it, ordered under its own headings; every sentence is the checker's.*

> **What I read as the work.** Only `CONTEXT.md` at the root of the worktree. `git status --porcelain -uall` returns exactly ` M CONTEXT.md` — no node file, no `decisions.md`, no `flags.md`, so no manager bookkeeping appears among the work. **I read the changed path given to me as the work under the implementation-rules file's rule for that** ("An implementation node's work on this effort may be the effort's own record"), and derived no statement of intent from anything but the acceptance condition.
>
> **How I established each part.** Because every claim clause 4 is about wraps across lines, **I did not settle any of it line-wise.** I unwrapped both sides — `git show HEAD:CONTEXT.md` and the working file — into unbroken paragraphs and diffed those; the whole change is two paragraphs, and I then searched the unwrapped text and the sentence split of it.
>
> 1. **Met.** The grilling entry now reads: *"A decision only the human can make, reached by interviewing them. Its worker may put several of its questions in one payload, independence being what decides which of them share one."* The phrase *one question at a time* is gone, and the remaining text grants rather than limits.
> 2. **Met.** The Relay entry now reads: *"…carrying a worker's questions to the human and the answers back. One payload holds one of that worker's questions or several of them, and either way it is one thing in front of the human; it never carries a second worker's."* The head sentence is plural in both directions.
> 3. **Met.** Both `_Avoid_` and `_Note_` lines are byte-identical to `HEAD`. The unwrapped paragraph diff shows exactly two changed paragraphs and no others.
> 4. **Met.** I enumerated every occurrence of `question` in the unwrapped text, plus `at a time`, `one at a time`, `single`, `one thing`, `in front of` and `ask`, and read every sentence in the file mentioning the human. Outside the two entries, `question` appears in **Node**, **Fog**, **Manager**, **Resolve**, **Raise**, **Manager note** and **Park**. The last two are the nearest candidates: each is an indefinite singular naming one instance of a thing, and neither asserts that a worker puts one at a time or that exactly one is in front of the human. `at a time` appears once, in **Code slot**, about workers holding a slot. The only statement of the form clause 4 discusses is the Relay entry's own *"either way it is one thing in front of the human"*, **which is the wording clause 4 expressly permits.**
>
> **The bar.** Nothing to run, verified rather than assumed. Under the *"if relevant"* clause it is a complete bar. The non-command half held by hand.
>
> **`_Avoid_` lines bore hardest.** Checked by hand rather than by grep, per that file's own recorded trap about ordinary-English refusals. The new text's only loaded word is *payload*, refused under **Handover** — but it is used here in the sense the **Relay** entry itself establishes and already used before the change, not as a name for a handover, so it is the file's own vocabulary.
>
> **Ground rule 3 bore, and holds:** the grilling entry describes a worker filling a payload, and the Relay entry keeps the manager as the party that passes it along.
>
> **Reviewing skills.** The implementation-rules file names none for this repo, and states plainly that a checker does not go looking for one. So no reviewing skill was run. I invoked `/writing-for-agents` only to read the standard into this thread and applied it myself; **nothing was delegated to an agent that would have been handed less than I was.**

*No `NOT COVERED`. No questions raised.*

***The manager's note.*** **The third consecutive check to use [node 171](171-carry-the-record-node-reading-rule-into-the-rules-file.md)'s rule and say so, and the third to need no licence.** This one applied it to a *shipped* file rather than a record file, reading it as the general permission it is written as.

### Gate — `approve`

**The human's word, `verbatim`.**

> approve

*No correction round; run 1's `PASS` is the only run. All three flags are settled by the approval.*

## Answer

*Pasted as the worker wrote it.*

> **`CONTEXT.md` now states node 117's adopted rule in the two entries the condition names**, and neither says a worker puts one question to the human at a time. One file changed; nothing else was touched.
>
> ### 1. The `grilling` entry
>
> The trailing *"one question at a time"* is gone, and the entry does not merely fall silent — it states the rule positively, so the removed claim cannot drift back:
>
> > **grilling**: A decision only the human can make, reached by interviewing them. Its worker may put several of its questions in one payload, independence being what decides which of them share one.
> > `_Avoid_`: decision, question, interview
>
> *Independence* is the membership test node 126 shipped into the grilling contract; the glossary states it in one clause and does not restate what that contract holds.
>
> ### 2. The `Relay` entry
>
> > **Relay**: The channel and the payload carrying a worker's questions to the human and the answers back. One payload holds one of that worker's questions or several of them, and either way it is one thing in front of the human; it never carries a second worker's. The manager passes both along unaltered and answers nothing itself.
>
> **The wording *"one thing in front of the human"* is deliberate and is the condition's clause 4 exemption used on purpose.** What the workflow still holds is that exactly one *thing awaiting a reply* faces the human; what it no longer holds is that exactly one *question* does. The same distinction is already load-bearing in the shipped grilling contract. *"It never carries a second worker's"* is node 117's other half — batching adopted inside a node and refused across them.
>
> ### 3. How clause 4 was established across the rest of the file
>
> Every claim at issue wraps across lines, so a line-wise `grep` cannot settle it. The file was searched with paragraphs joined into single unbroken lines. Three hits survive, and none is what clause 4 forbids: **`Node`** — *"a single question to decide"*, a node's own subject; **`Worker`** — *"work exactly one node"*; **`Code slot`** — *"held by one worker at a time"*.
>
> ### 4. The edit deletes rather than strikes, and that is a call
>
> `CONTEXT.md` is a **shipped** file, not a graph file, so the map's never-delete rule does not reach it — the rule's own words are *"when any file in the graph is edited"*. The precedent is node 133, which plainly deleted a preface and every method-skill name from a shipped contract at `4000830`, and node 126, which plainly deleted the same sentence from the grilling contract. A glossary carrying struck superseded definitions would also defeat its own purpose, being the file the shipped set declares authoritative for a term's *current* meaning.

**What the worker reported its work invalidates:** `none`. In its words: *"The change carries out node 117's answer into the file node 126 could not reach and contradicts no resolved node. Node 14 fixed this vocabulary and is extended rather than contradicted: the terms `grilling` and `Relay` are unchanged, only what they are defined to permit."*
