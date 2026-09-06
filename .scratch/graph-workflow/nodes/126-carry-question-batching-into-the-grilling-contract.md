# Carry intra-node question batching into the grilling worker contract

Type: implementation
Status: resolved

Blocked by: none

## Question

*Surfaced by [Whether the manager sends the human questions in batches](117-questions-sent-in-batches.md)'s worker,
and pasted as it wrote it.*

> The grilling worker contract still says one question at a time, its question shape admits one question, and its
> discipline list is prefaced so that the bullet does not bind when the invoked skill is present — while that skill
> now instructs the opposite. Make the file state the adopted rule in its own text.

**Blockers, in the worker's words:** *"none."*

**The worker's note on why this is two nodes rather than one**, pasted: *"I split these by file rather than by
sentence as the manager proposed, because the two manager-contract sentences are one edit to one section while the
worker contract is a different file with a different reader, and a code slot of one serialises them either way."*

## Acceptance condition

*Written by node 117's worker. Pasted as it wrote it, and not the manager's.*

> `.claude/skills/expedition-grilling/SKILL.md` states all of the following in its own text, and nothing in that file
> contradicts any of them.
>
> 1. A worker may put more than one of its own questions to the human in a single payload. Two questions may share a
>    payload only where neither's answer depends on the other's; a question whose answer depends on another in the
>    same payload is held for a later payload.
> 2. Where a payload carries more than one question, each question is numbered, carries a short title, carries its
>    own recommendation and the alternatives it sets aside, and is visibly separated from the next. Where a payload
>    carries exactly one question, that question is not numbered.
> 3. A question's number is fixed for the life of the attempt. Numbers are never reused and never renumbered: a
>    payload re-asking a question asked earlier in the same attempt uses that question's original number, and a
>    question asked for the first time takes the next number not yet used in that attempt.
> 4. A reply naming a question or naming an option settles what it names. A reply that assents to the recommendation
>    without naming any question — *"ok for recommended"* and forms like it — settles every question's recommendation
>    in that payload, and settles nothing in that payload which is not a recommendation.
> 5. A question the reply does not name is unanswered rather than deferred. It goes out in a later payload. The
>    worker never reads an unnamed question as assent and never answers one itself.
> 6. The human deferring is something they state. Nothing in the file treats a question the reply failed to name as a
>    request to defer.
> 7. The file places no requirement on the form of the human's reply, requires no numbered reply, and makes no claim
>    about what form a reply will take.
> 8. The file does not use the word "frontier" for the questions carried in a payload.
> 9. Every one of items 1 to 8 is stated in this file's own text. None of them is left to be supplied by any skill
>    the file instructs the worker to invoke, and the file does not make any of them conditional on such a skill
>    being present or absent.

## The manager's note at filing

*Not a change to anything above.*

**This condition carries no enumerator and states no scope beyond one file**, which is [node
94](94-condition-scope-as-a-predicate.md)'s rung 3 case rather than a malformation: its scope is one named file and
was not derived from a search. Clause 9's *"in this file's own text"* is a demand on that file rather than a
quantifier over the tree. **The manager has not amended it.**

**One fact the worker established that this condition does not name, and that its worker will meet.** The file
contradicts itself today: its discipline list is prefaced *"Where they are not present, this is the whole of the
discipline"*, so its *"One question at a time"* bullet does not formally bind while `/grilling` is present, and
`/grilling` now instructs the opposite. Clause 9 reaches that preface; nothing else does.

***The manager's later note: the paragraph above is stale, and its worker corrected it.*** [Node
133](133-carry-the-method-skill-deletion-into-the-contracts.md) had already deleted that preface and every method-skill
name from this contract, landed as commit `4000830`, one day before this node ran. So the bullet **did** formally bind
when the worker arrived and the file named no skill. The rest of the premise held. Left in place under the
never-delete rule and corrected here rather than over there.

## Flags

*All three are the worker's own text, pasted. The ids and the links are the manager's bookkeeping and nothing else.
The account of what produced them is the worker's handover, which reached the manager as one document.*

`126.1` **· settled** `ASSUMPTION` — **What a multi-question payload does to *When the answer is not an answer*, and to park.** The condition says what an unnamed question means and says nothing about a reply that applies one of the table's four moves to one question of several. I settled it: each row governs the question the reply applied it to, and every other question in the payload is read under the reply rules. That reaches the *"ask me later"* row, which previously stopped the node outright and now holds that question for a later payload, parking only where what they defer is the payload itself or where nothing is left to carry on with. Ground: park banks the node and stops it, which would throw away the questions they did answer in the same payload, and node 117's answer already treats an unsettled question as one that goes out later. I also added the unanswered questions to the park shape's `WHERE IT STOOD`, so a parked node's next attempt inherits them. Nobody was asked.

`126.2` **· settled** `ASSUMPTION` — **The glyphs of a batched payload: `Q1.` plus a short title, and `---` between questions.** The condition demands numbering, a title and visible separation, and names no glyphs. I took `Q1`/`Q2` and the `---` rule from the external skill node 117 read, recorded in that node's first queued payload, because the human's own predicted reply form is *"Q1 ok Q2 ok Q3 .."* — so the number they will type is the number the payload shows. The alternative was a markdown heading per question, which reads better on screen and gives them nothing short to type back.

`126.3` **· settled** `ASSUMPTION` — **Two words added to the contract's `## Words used exactly`: payload and attempt.** The condition's rules are stated over a payload and over the life of an attempt, and the contract used both words without defining either — **attempt** appeared only in bold inside the park entry. I defined both from `CONTEXT.md`'s own entries rather than coining anything: **payload** as what a relay carries, which `CONTEXT.md`'s `Relay` entry already uses in those words, and **attempt** as one worker instance on one node, which is `CONTEXT.md`'s `Attempt` entry. `CONTEXT.md`'s `_Avoid_` line under `Handover` refuses `payload` as a name for a handover; that is a different concept and the refusal does not reach this use, which is the measured `_Avoid_`-as-greplist trap the rules file already names.

## Review

### Checker run 1 — `PASS`

*Pasted as the checker wrote it, condensed to its own section headings by ordering rather than rewriting; every
sentence below is the checker's.*

> **Standards read.** `.scratch/graph-workflow/map-implementation-rules.md` (resolved from a single listing of `.scratch/`, which holds one effort, `graph-workflow`). Its `## What the work is held against` names the standards: `/coding-principles`, `/naming`, `CONTEXT.md`'s `_Avoid_` lines, the map's standing preferences / ground rules / four standing rules, `.claude/skills/expedition/graph-conventions.md`, and `/writing-for-agents`. It also records that **no reviewing skill is named for this repo**, so none was run and none was looked for. I read that file for its standards and opened nothing else in `.scratch/`.
>
> **No standard moved under the check.** The single changed path is not one of the standards above, so `### Where the work moved one of them` never engaged. The condition records no enumerator, so there was none to run.
>
> ### The acceptance condition, part by part
>
> Established by reading the file whole, and by searching it **unwrapped into paragraph-length unbroken lines** (a Python pass that joins each paragraph before matching), since every rule at issue wraps.
>
> 1. **Multiple questions per payload, independence the test.** Stated at the discipline bullet: *"One payload may carry more than one of your questions. Two questions may share a payload only where neither's answer depends on the other's; one whose answer depends on another in the same payload is held for a later payload."*
> 2. **Numbering, title, own recommendation, visible separation; a lone question unnumbered.** Both halves present. The two code blocks match: the single shape carries no `Q1.`, the multi shape carries `Q1.`/`Q2.` split by `---`.
> 3. **Numbers fixed for the attempt, never reused, never renumbered.** Stated in full, including both sub-clauses. `attempt` is newly defined in *Words used exactly*, so "for the life of your attempt" is anchored in the file's own text.
> 4. **What a reply settles.** Both bullets present verbatim in substance, including *"settles nothing in that payload which is not a recommendation."*
> 5. **Unnamed is unanswered, not deferred.** Present, with both prohibitions.
> 6. **Parking is stated.** The `park` glossary entry was amended to *"the human deferring, in as many words."* I checked the one place that could contradict it — the `ask me later` row — and it routes on what the human states, not on what they omit.
> 7. **No requirement on the reply's form.** Present. The two appearances of *"ok for recommended"* and the one of *"Q1 ok"* are illustrations of what a reply would **mean**, and the condition itself cites the first of those forms.
> 8. **No "frontier" for a payload's questions.** The unwrapped search returns nothing.
> 9. **All of 1–8 in the file's own text, none deferred to a skill.** Stated directly, and independently each of items 1–8 is present as the file's own prose.
>
> **Nothing in the file contradicts any of them.** The unwrapped search for `one at a time` / `one question at a time` returns nothing — both prior instances were removed.
>
> ### The bar
>
> Nothing to run, and I ran nothing. No manifest, no task runner, no CI config, confirmed by listing and by a `find`. So the bar is entirely its non-command half, which is a complete bar here. `/writing-for-agents` holds — `payload` earns its place as a leading word, the added prohibitions are each paired with the positive target the standard asks for, and the second shape block defers to the first with `<as above, written once for the payload>` rather than restating it. `CONTEXT.md`'s `_Avoid_` lines checked by hand: **Handover**'s refusal of *payload* does not bite, being concept-scoped to a handover, and `CONTEXT.md`'s own **Relay** entry already uses *payload* for precisely this concept. `graph-conventions.md`'s `## Interview` already reads *"each relayed question and each human answer"*, which accommodates a multi-question payload. Ground rules 1–5 all hold.

```
NOT COVERED:
- ESTABLISHED BY the human, at the gate · read the part as the gate presented it — as owed,
  unestablished, and as the gap node 144 had just closed for every worktree cut after
  `37a3d28` — and approved the node with it in front of them. Their word, `verbatim`:
  "approve". The manager did not establish it: doing so meant holding the work against a
  standard itself, which is the checker's office.
  — "this map's standing preferences, ground rules and four standing rules" as
  standards. Those live in `map.md`, which my contract forbids me to open. The **ground
  rules** reached me as text in the spawn and I checked against them; the **standing
  preferences** and the **four standing rules** I could not read. Whoever holds `map.md`
  is the only party that can settle that slice.
```

***The manager's note on the owed part.*** **This is the exact gap [node 144](144-make-the-rules-file-stand-alone.md)
exists to close**, and it is owed here only because node 144's work has not merged: this worktree is based on
`8340e18`, where the four standing rules still sit in `map.md`. Once 144 lands, a checker reads both blocks in the
rules file it is already sent to, and this class of `NOT COVERED` stops arising.

**The question it raised alongside its outcome, pasted as it wrote it.** It issues no verdict and did not stop the
`PASS`; it travels to the human in the gate payload.

> **`CONTEXT.md`'s glossary still asserts the discipline this work removed.** The condition demands *"one question at a time"* be gone from the grilling contract, and the work removed it. But `CONTEXT.md` — which opens by declaring itself *"the vocabulary the skill files are written in"* — still says, under **grilling**: *"A decision only the human can make, reached by interviewing them one question at a time."* Complying with the condition is what produced the disagreement: the wording is the condition's own and the file is outside the condition's single path, so departing from it or editing `CONTEXT.md` was not the worker's to do. Under `/writing-for-agents`' single-source-of-truth rule this is a live duplication gone stale. Does the human want `CONTEXT.md`'s **grilling** entry amended, as its own node or as an extension of this one?
>
> **Instances.** `CONTEXT.md:114`.
>
> **Form, as a predicate.** A line in a shipped file, outside the condition's one path, that asserts a grilling worker puts questions to the human one at a time.
>
> **Extent.** Enumerator, over the shipped files:
>
> ```
> grep -rniE 'one (question )?at a time|a single question|one question only' \
>   --include='*.md' . --exclude-dir=.git --exclude-dir=.scratch --exclude-dir=.worktrees
> ```
>
> Run in the worktree, it returns four hits. One, `CONTEXT.md:29`, is a false positive (*"a single question to decide"*, the **Node** definition). One is the instance above. The remaining two are **not** defects I assert, and I name them so nobody has to re-derive them:
>
> - `.claude/skills/expedition-prototype/SKILL.md:80` — *"One question at a time. Wait for the answer before asking the next."* A different node kind's contract. Whether the prototype worker should follow grilling is a scope decision for the effort, not a contradiction of the file under check.
> - `.claude/skills/expedition/SKILL.md:482` — *"Their questions do not collide, because what reaches the human is still one at a time."* Read in context this is about concurrent HITL **nodes** queueing one payload at a time in front of the human, which the change leaves true. The wording is now a little loose, and that is an observation rather than a finding.
>
> I am blind to the effort's record, so each of these is bounded by the files I hold: *nothing in the shipped files I may read reconciles `CONTEXT.md:114` with the amended contract*, not *nothing does*. The party holding the record settles whether the other two hits are already spoken for.

***The manager's note on that question.*** **The checker found independently what the node's own worker reported**, from
the other side of a blindfold: the worker minted a node for `CONTEXT.md`'s `grilling` entry, and the checker reached the
same line without seeing that. The manager records the agreement and reads nothing further into it.

### Gate — `approve`

**The human's word, `verbatim`.**

> approve

*No correction round; run 1's `PASS` is the only run. The three flags are settled by the approval. The checker's
question was in the payload and the human answered it in neither direction; the manager records the question rather
than reading approval as an answer, and its subject already has a node.*

**Landed as `8cc9b79`**, rebased onto `37a3d28` and fast-forwarded onto `master`; worktree removed, branch deleted.
**The merge required the sandbox off**, which is the case `map-implementation-rules.md` already records: a branch
changing a file under `.claude/skills/` cannot be merged into that read-only bind mount. The rebase was clean.

## Answer

*Pasted as the worker wrote it.*

> **`.claude/skills/expedition-grilling/SKILL.md` now states node 117's adopted rule in its own text**, and the *"One question at a time"* bullet is gone. One file changed; nothing else was touched.
>
> ### 1. What the file now says, and where each piece sits
>
> - **Opening line.** The kind is *"a decision only the human can make, reached by interviewing them"* — the trailing *"one question at a time"* is removed.
> - **`## Words used exactly`** gains **payload** (one relayed message of yours, awaiting one reply, carrying one question or several, and one thing in front of the human either way) and **attempt** (one worker instance on one node). Both are taken from `CONTEXT.md`'s existing `Relay` and `Attempt` entries rather than coined. **relay** is pluralised; **park** is redefined as *"the human deferring, in as many words"*, which is where the file's park rule is anchored.
> - **The discipline** carries the batching rule itself: a payload may carry more than one of your questions; two may share one only where neither's answer depends on the other's, and one that depends on another in the same payload is held for a later payload; no cap, independence being the whole of what decides membership; and each question in a multi-question payload carries its own recommendation and alternatives.
> - **The `question` shape is now two shapes.** One question, unnumbered, in the shape the file already had — with a line saying that numbering is itself the signal that a payload holds more than one. More than one question: `NODE`, `ABOUT`, `SO FAR` once, then each question headed `Q1. <short title>`, carrying its own `ASK`, `RECOMMENDED` and `ALTERNATIVES`, separated by `---`. Beneath both, the number rule: fixed for the life of the attempt, never reused, never renumbered, a re-ask keeping its original number and a new question taking the next number not yet used.
> - **What a reply settles** sits beside the resumed `HUMAN ANSWER` block, where a worker reads it at the moment it reads the answer: naming a question or an option settles what it names; a bare assent to the recommendation settles every recommendation in that payload and nothing in it that is not a recommendation; an unnamed question is unanswered rather than deferred and goes out in a later payload, never read as assent and never answered by the worker; parking is something the human states, and a question their reply failed to name is not a request to defer.
> - **The form of the reply is left to the human**, in the file's own words: no numbered reply is asked for, no shape is prescribed, and no claim is made about what shape one will take — numbering your own questions is the whole of what the worker does about it.
> - **The word `frontier` does not appear in the file** and none was introduced.
>
> ### 2. The one thing added that the condition did not name, and why
>
> **The unconditionality sentence.** Clause 9 forbids any of the rules being left to a skill or made conditional on one. The file's `## How you grill` opens with the paragraph saying the hard rules govern a method skill's conflicting instructions — which left the *discipline* formally unguarded against a skill instructing the opposite, since only the hard rules were said to govern. One sentence now closes it: the discipline and the shapes are the whole of what binds the worker and bind whether or not any such skill is invoked, no part of them supplied by a skill or changing with one's presence.
>
> ### 3. What the node file's premise got wrong, stated so a later reader does not re-derive it
>
> **The preface the node file and the manager's note both quote — *"Where they are not present, this is the whole of the discipline"* — was already gone when this node started.** [Node 133](133-carry-the-method-skill-deletion-into-the-contracts.md) removed it, landed as commit `4000830`, and the list has read *"This is the whole of the discipline:"* since; the contract also names no method skill any more. So the *"One question at a time"* bullet **did** formally bind when this worker arrived, and the self-contradiction the manager's note records had already been half-repaired. What remained true is the rest of the premise: the bullet said one at a time, and the `ASK` field admitted one.
>
> ### 4. Two other shipped files carry the same sentence, and only one has a node
>
> `.claude/skills/expedition/SKILL.md`'s *"Exactly one question is in front of the human at a time"* is inside `## What is in front of the human, and when`, which is [node 127](127-manager-contract-one-payload-several-questions.md)'s section and was not touched. **`CONTEXT.md`'s `grilling` entry — *"reached by interviewing them one question at a time"* — belongs to neither node**, and is reported on `NEW NODES`.

**What the worker reported its work invalidates, pasted as it wrote it.**

> none. My change carries out node 117's answer and contradicts no resolved node beyond what that node already filed on its own `## Invalidations` — node 16's *"Question batching is dead"* and its two companion sentences. The `CONTEXT.md` contradiction above is between two shipped files rather than with a decision, which is why it is on `NEW NODES` and not here.

## Retrospective

*Pasted as the worker wrote it. Filed by the manager as an annotation.*

**1. What I had to hunt for.**

- **The preface my own node file quotes.** I opened the contract expecting *"Where they are not present, this is the whole of the discipline"* and it was not there. `git log --oneline -- <the file>` found commit `4000830`, node 133, which deleted it on 2026-09-04 — one day before this node ran. I looked first at the file, which is right; what was missing was any statement of *when* the condition's author read it.
- **Which other shipped files repeat the sentence.** One `grep -rn "one question at a time"` over `.claude/` and `CONTEXT.md` returned two hits. Cheap, but nothing told me to run it and the answer produced this node's only new node.
- **Whether node 127 already covers `CONTEXT.md`.** My spawn said 127 holds *"the manager-contract half"* without its scope, so I opened node 127 to read its condition and learn it names one file and one section. One file read to avoid minting a duplicate.
- **The glyphs for numbering and separation.** Node 117's `## Answer` states numbering, titles and separation but names no glyphs; `Q1`/`Q2` and `---` are in that node's **first queued interview payload**, 200 lines above the answer. The operative fact for the shape I was to write was in the working-out rather than in the conclusion.

**2. What arrived in my context that this node did not need.**

- **`map-implementation-rules.md`'s `## Landing an implementation node's work`** — roughly sixty lines of worktree, rebase and sandbox forensics, which is most of the file, against the two paragraphs under `## What the work is held against` that I actually used. My spawn warned me and I still took it whole, because `Read` on a file is whole-file: the warning cannot fix this, and the arrangement can. That section is by its own words *"the manager's lifecycle material"*, and it would cost a worker nothing if it lived in `map-manager-only.md` with the worker/checker file holding only what is held against. **This is the third report of it.**
- **`map.md`'s retrospective bullet, quoted in full in my spawn as well.** Roughly 400 words of identical text arrived twice. The spawn's copy is the operative one; the map's copy is what every worker on every node pays for again.
- **`map.md` more broadly:** what bore on my work was the never-delete rule (and it turned out **not** to reach shipped files, which I had to establish from commit `4000830`'s plain deletion), the four standing rules of writing, ground rules 2 and 5, and the no-mattpocock-dependency direction. The landing policy, the `EnterWorktree` route, the resume rule, the flags-settle-at-close rule, the code-slot count and the dogfood material bore on nothing I did.
- **Node 117's file: 537 lines, of which about forty were operative** — the answer's §4, §5, §8 and §9, plus the glyph fact noted above. Its two full interview payloads, both manager notes, the worker's correction of a manager note, seven flags and its own retrospective told me why the rule is what it is, which made me confident but changed no word I wrote. **A node implementing a grilling node's answer wants that answer's operative sections quoted in the spawn**, the way my acceptance condition was quoted, rather than a pointer to the node.
- **The spawn's note that node 144 is at its gate elsewhere** bore on nothing: it told me there was no collision, which I could not have derived, but no collision was possible from one file under `.claude/skills/`.

**3. What would have made this node easier.**

- **A condition that quotes a file should carry the commit it read.** Clause 9 and the manager's note at filing were both written against a state of the file that had already been repaired, one commit earlier. Nothing in the node, the spawn or the record says at what point the file was read, so I had to reconstruct it from `git log`.
- **The node that split 126 from 127 should have run the grep.** It knew the sentence and split by file; a thirty-second search over `.claude/` and `CONTEXT.md` would have found the third file and minted its node at splitting time, instead of my finding it at handover after both siblings were already scoped.
- **In the record:** node 117's answer is this node's specification and it is buried in a 537-line file whose interview is four times the size of its conclusion. The convention that puts the answer last is what makes the specification expensive to reach; a spawn quoting the answer's operative sections costs the manager nothing and would have saved me most of that read.

**4. What was stale, wrong, or contradicted something else.**

- **My node file's `## Question` and the manager's note at filing are both stale on the same fact.** Both say the discipline list is prefaced so the *"One question at a time"* bullet does not formally bind, and that the file names a skill instructing the opposite. Node 133 deleted the preface and every skill name from this contract, landed as `4000830`. The bullet bound unconditionally when I arrived, and the file named no skill. The rest of the premise held, and clause 9 still had work to do — but for a different reason than the one recorded, which is why I wrote the unconditionality sentence rather than deleting a preface.
- **`CONTEXT.md` contradicts the shipped contract** as of my change, in the `grilling` entry and weakly in `Relay`. Reported as a new node.
- **`CONTEXT.md`'s `_Avoid_` line under `Handover` refuses `payload`**, while its own `Relay` entry uses `payload` for what a relay carries, and the map, the rules file and every gate say *"gate payload"*. Not a defect I acted on — it is exactly the *"ordinary English refused only for one concept"* trap `map-implementation-rules.md` records — but it is the second word after `where` that a checker grepping that list will hit.
