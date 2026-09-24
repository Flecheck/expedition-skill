# A plain-English and compaction pass over the shipped files

Type: grilling
Status: resolved

## Question

The human, `verbatim`, opening a management session on 2026-09-23: *"Continue working on the project. All the
current stuff was written by opus 5, we might want to at some point do a full pass over the skills as opus 5 writes
in a weird english. We might also want to compact things a bit as I feel the skills are quite long."*

What does that pass consist of, precisely enough that implementation nodes carrying it out can be given
self-contained acceptance conditions? Among what the interview has to settle:

- **Which files it reaches** — the skill files under `.claude/skills/expedition*/`, `graph-conventions.md`,
  `wayfinder-divergences.md`, `CONTEXT.md`, `.claude/rules/expedition-triggers.md`; and whether the effort's own
  record (the map files, the node files) is inside it or outside it.
- **What "weird English" is**, in terms a checker can hold a rewrite against — with examples the human points at.
- **What "compact" means** — a target, and what may be cut: explanation of why, repetition across files,
  rules themselves.
- **How a rewrite is checked for losing nothing that binds** — what a checker is handed so that "no rule was
  dropped or changed" is judgeable from text it was given.
- **When it runs relative to the open backlog.** At the time of writing about 130 nodes are open, many of them
  wording repairs to the same shipped files. Whether the pass runs first, runs last, or runs alongside, and what
  happens to the open nodes whose work it overtakes, is the human's to decide.
- **How it is cut into implementation nodes** — per file, per concern, or otherwise — given two code slots.

## Interview

### Attempt 1 — routing key `abd5f65b4d8ffac2e` (does not survive the manager's session)

**Payload 1, relayed 2026-09-23** — the worker's own text, pasted:

> NODE: A plain-English and compaction pass over the shipped files
>
> ABOUT: You asked for a pass over the skills, because Opus 5 "writes in a weird english" and the skills "are quite long". This node pins down what that pass is, precisely enough that implementation nodes can carry it out and a checker can judge each one. This payload holds the four questions that don't depend on each other. How a rewrite is checked for dropped rules, and how the pass is split into nodes, come in a later payload, because they depend on these answers.
>
> SO FAR: I measured the shipped files on 2026-09-23. These are working figures, so re-derive them rather than trust them. There are 12 files: the 10 under `.claude/skills/expedition*/`, plus `CONTEXT.md` and `.claude/rules/expedition-triggers.md`. Together they are 3,370 lines and about 34,400 words. The manager contract alone is 8,445 words, `graph-conventions.md` is 5,718 and the checker contract is 4,798.
> - **No history to cut.** The shipped files contain almost no citations of nodes (one in total), so compacting them can't mean cutting provenance. It has to cut explanation, repetition or phrasing.
> - **Two decisions already bear on this.** Node 50 records your *"keep them duplicated"*: two sections are word-for-word the same in each of the five worker contracts, about 684 words each. Standing writing rule 1 says: compress the prose that explains why, and never compress the shapes, meaning the fixed handover templates.
> - **The backlog is large.** 131 nodes are open. 91 of them are implementation nodes, and 57 of those have acceptance conditions that name a shipped file. All 57 quote text, 266 quoted passages in total. A rewrite breaks those quotations.
> - **The existing mechanisms cover it.** A rewrite worker must already search open conditions for text its own work changes (node 263). A node that becomes unnecessary can now be closed as `superseded` (node 264).
> - **A reference point exists.** The prose standard this effort already uses, `/writing-for-agents`, rejects steering by prohibition and rejects saying the same thing in several places. Your own lines in `expedition-triggers.md` read quite differently from the lines around them. For example: *"if the human has nothing to do and there is a question/gate, give it to him."*
>
> Q1. Which files the pass covers
> ASK: Does the pass cover exactly the 12 shipped files above, and leave out the effort's own record (`map.md` and its sibling files, `decisions.md`, `flags.md`, the node files)?
> RECOMMENDED: Yes, the 12 shipped files and nothing else. You said "the skills", and the record serves a different purpose. It follows the never-delete rule and quotes your words verbatim, so rewriting it would mean banking every changed line in `map-history.md`. `map.md` is also long and in the same style, so it could be its own later node if you want that. In `expedition-triggers.md`, the lines you wrote yourself keep their meaning, and only their grammar gets touched.
> ALTERNATIVES: Include `map.md` and the other map files too (every worker reads `map.md`, so it costs as much as a skill) · Only the skill files, leaving out `CONTEXT.md` and the triggers file · Everything, node files included
>
> Q2. What "weird English" means
> ASK: Is this what you mean by weird English, and which examples hit or miss? Six features, with real instances from the files:
> 1. **Rules stated as negatives.** "never" appears 185 times and "rather than" 110 times. *"Exactly one of three, and never two at once."*
> 2. **Bold scattered mid-sentence.** There are about 700 bold spans in 34k words.
> 3. **Figures of speech or invented terms for plain ideas.** *"Three things neither pen reaches"*, *"settling a flag, which rides a moment that already exists"*, *"claimants"*, *"in as many words"*.
> 4. **Slogan-like reversals.** *"The graph-file ban is about recording, not about files."* *"Amending is never authoring."* *"the whole of what binds you"*.
> 5. **Broken or unclear references.** *"**Two things that is not**, and neither is loosened by it."*
> 6. **Long sentences** that stack clauses with dashes and semicolons.
> RECOMMENDED: Adopt these six as the definition, plus anything you point at that I missed. The fix for each: state the rule positively, keep bold only for a term where it is defined, use plain words, write direct statements with clear referents, and put one idea in each sentence. Also add it to `map-implementation-rules.md` as a fifth standing writing rule. The open backlog will otherwise keep writing in the old style, and I write in it too. That makes it binding on this effort only; it reaches the shipped files only if you say so.
> ALTERNATIVES: Point at your own examples and I derive the definition from them · Make it a one-off standard for the pass only, not a standing rule · No fixed definition: a reviewer judges "plain English" case by case (a checker can't hold a rewrite to that)
>
> Q3. What "compact" may cut, and how far
> ASK: What may the pass remove, and should it have a size target?
> RECOMMENDED: It may cut three things. (a) Explanations of why, down to a clause wherever the reason isn't needed to apply the rule. (b) Repetition inside a file: the manager contract repeats several rules across its sections. (c) Words, through the rewrite in Q2. It may not cut any rule, any fixed template, or any refused word in the glossary. Where a worker thinks a rule is dead, or is something the model does anyway, it reports it as a new node for you to decide. Node 50 stands, so the shared sections in the five worker contracts stay duplicated. The reason is that each contract must stand alone, and those sections are read at the moment of writing a handover. The target: roughly one third fewer words in each file, as a soft figure. The checker reports it, and missing it raises a flag rather than failing the work. I can't measure in advance what is achievable without cutting rules, so a hard number would be a guess.
> ALTERNATIVES: Hard target, such as halving each file (forces rule cuts or a fail) · No target, just the categories (the worker doesn't know how hard to cut) · Also remove the cross-file duplication, reversing node 50 · Rules may be cut too, when the worker judges them no-ops (this changes behaviour without a decision from you)
>
> Q4. When the pass runs relative to the backlog
> ASK: Does the pass run before the open backlog of wording repairs to these files, after it, or alongside it?
> RECOMMENDED: Before, one file at a time. While a file's rewrite is in progress, no other implementation node on that file starts. Shorter files make every later worker and checker cheaper to run, which is the token priority you set. The backlog would also land in the new style instead of adding more of the old one. The cost is the 266 broken quotations. Each file's rewrite worker already has to search for them (node 263). For every open node whose condition quotes that file, it hands back one of two things. Either a re-pointed condition that quotes the new text, which is allowed because the words are then fixed by the landed rewrite. Or a stand-down as `superseded`, for a repair the rewrite made unnecessary. A rewrite preserves meaning, so it carries existing defects over unchanged, and the open nodes that repair rules still apply afterwards.
> ALTERNATIVES: After: no condition churn, but the pass waits behind about 90 implementation nodes while the files keep growing in the current style · One file at a time, the other way round: clear a file's open repairs first, then rewrite it (fewer broken quotations, but the pass barely starts) · Alongside without freezing: rewrites and repairs to the same file collide at landing

**The human's answer to payload 1, 2026-09-23**, `verbatim`:

> 1. The important part are the shipped files but it might be good to do it also on some stuff in the map I don't know, you decide 2. ok for your proposition. I don't have a specific rule in mind but yes, using plain words, make thing clear is good. Right now it is quite hard to understand. 3. ok. I also think by simplifying the text it might be possible to make it smaller maybe finding some generalisation/simplification of some existing stuff 4. ok

- **Q1** — a *"you decide"* on Q1 alone, after naming the shipped files as the important part; goes back to the worker. The worker's recommendation it was offered: *"Yes, the 12 shipped files and nothing else."*
- **Q2** — takes the worker's recommendation: *"Adopt these six as the definition, plus anything you point at that I missed. […] Also add it to `map-implementation-rules.md` as a fifth standing writing rule."* (worker's text, quoted).
- **Q3** — takes the worker's recommendation: *"It may cut three things. (a) Explanations of why […] (b) Repetition inside a file […] (c) Words, through the rewrite in Q2. It may not cut any rule, any fixed template, or any refused word in the glossary. […] The target: roughly one third fewer words in each file, as a soft figure."* (worker's text, quoted) — with an addition of the human's own, above: generalising or simplifying existing material.
- **Q4** — takes the worker's recommendation: *"Before, one file at a time. While a file's rewrite is in progress, no other implementation node on that file starts."* (worker's text, quoted).

**Payload 2, relayed 2026-09-23** — the worker's own text, pasted:

> NODE: A plain-English and compaction pass over the shipped files
>
> ABOUT: You asked for a pass over the skills in plainer and shorter English. This node defines that pass precisely enough that implementation nodes can carry it out and a checker can judge them. This payload holds the last two open points: how a checker confirms a rewrite dropped no rule, and how the pass is split into nodes.
>
> SO FAR: **What you settled last round:**
> - **Q2 (what "weird English" is):** my six-feature definition. It also becomes a fifth standing writing rule for this effort.
> - **Q3 (what may be cut):** why-explanations, repetition inside a file, and wording. No rule, template or refused word is cut. There is a soft target of about a third fewer words per file. You added: look for generalisations and simplifications of existing material.
> - **Q4 (when it runs):** before the backlog, one file at a time, with that file frozen while its rewrite is in progress. Each rewrite worker re-points or stands down the open conditions that quote its file.
>
> **What I decided on your "you decide" (Q1):** the pass covers the 12 shipped files. After them, a follow-on node applies the same rule to `map.md` and `map-implementation-rules.md`, because workers read those two. That node rewrites only the rule statements that are currently live. Your verbatim words stay as they are, and replaced text is saved word for word in `map-history.md`, as the map's usual procedure requires. `map-manager-only.md`, `map-history.md`, `decisions.md`, `flags.md` and the node files stay out.
>
> **Two points I settled from your answers, and will flag:**
> - **Generalisations must not change any outcome.** A generalisation may replace several specific rules only where every case they covered comes out the same under it. One that would change an outcome is a rule change, which Q3 already excludes, so it is reported as a new node for you. Each generalisation is listed in the worker's handover, so you see it at the gate.
> - **Glossary terms stay.** The plain-words fix applies to figures of speech that aren't defined terms, like "pen" and "rides a moment". Terms defined in `CONTEXT.md` (`scribe`, `gate`, `park`, `raise` and so on) remain. Renaming one is a vocabulary decision, so it would be a new node.
>
> **Facts for the two questions below:**
> - A checker is handed exactly the condition, the bar, the changed paths, the work's name and the ground rules. It is never handed the worker's handover, and a spawn can't add to that list (node 28). So whatever the checker needs to judge "nothing dropped" must be in the condition or in the tree.
> - Node 50 keeps two sections word-for-word identical across the five worker contracts. Rewriting those contracts separately would make the copies drift apart.
> - There are two code slots. The files range from 330 words (`wayfinder-divergences.md`) to 8,445 (manager contract).
>
> Q5. How a rewrite is checked for dropped rules
> ASK: How does the checker establish that no rule was dropped or changed?
> RECOMMENDED: The checker compares the file before and after, itself, without a list from the worker. Each condition lists what counts as binding: every rule · every fixed template and field name · every defined term · every refused word · the members and number of every closed list, such as "exactly three kinds" · every stated exception. The checker diffs the file against the worktree's base and goes through the old text section by section. For each binding statement it finds the new form. A statement that is missing, or whose outcome changed, fails the check. A generalisation passes only where every case it absorbs keeps its outcome. The checker also reports the word count against the one-third target, and checks the new text against the six weird-English features. Units of one file or one section group (Q6) keep that walk small enough to do properly.
> ALTERNATIVES: The worker writes a ledger file in the worktree mapping each old statement to its new place, and the manager deletes it before landing. The checker would still have to prove the ledger is complete, so it saves little and adds a file that never lands. · A second, independent checker on each rewrite. That doubles the cost, for a gain that section-sized units already give. · No systematic walk: the checker samples, and you catch the rest in the diff. That puts the loss-of-rules risk on your review.
>
> Q6. How the pass is split into nodes
> ASK: How is the pass split into implementation nodes, and in what order?
> RECOMMENDED: Start with a pilot, then go one file at a time. 1. **Pilot:** the research contract (1,517 words), including the two shared sections. You approve or correct it at its gate, and that fixes the style and cut depth for everything after it. 2. **The other four worker contracts** (grilling, precondition, prototype, implementation), one node each. Each copies the two shared sections unchanged from the landed pilot, which keeps node 50's copies identical. 3. **The checker contract**, as one node. 4. **The manager contract**, in three nodes by section group, run one after another. At 8,445 words it is too much for one worker to rewrite and one checker to walk. 5. **`graph-conventions.md`**, in two nodes, one after another. 6. **`CONTEXT.md`**, as one node, near the end, so its definitions can be checked against how the rewritten files use its terms. 7. **The three small files** (`expedition-stop`, `wayfinder-divergences.md`, `expedition-triggers.md`) together, as one node. 8. **The follow-on map node**, last. Once the pilot has landed, the two code slots run two different files at a time. That is 13 nodes in all.
> ALTERNATIVES: Pilot on the manager contract, which is the biggest saving, but the worst place to calibrate the style · One node per concern across all files (for example "remove negation everywhere"). Every node would touch every file, which breaks the one-file freeze and multiplies conflicts. · One node per file with no pilot. Faster, but a style you'd correct gets repeated up to twelve times before you see it.

**The human's answer to payload 2, 2026-09-23**, `verbatim`:

> Q5 ok Q6 ok

- **Q5** — takes the worker's recommendation: *"The checker compares the file before and after, itself, without a list from the worker. Each condition lists what counts as binding"* (worker's text, quoted; the full recommendation is in payload 2 above).
- **Q6** — takes the worker's recommendation: *"Start with a pilot, then go one file at a time."*, the pilot being the research contract, 13 nodes in all (worker's text, quoted; the full order is in payload 2 above).

## Answer

### The pass, as decided

The pass rewrites the files the workflow ships in plain English, and makes them shorter without dropping or changing any rule. It runs before the open backlog. It is carried out as a pilot followed by one file, or one section group, per implementation node. Thirteen implementation nodes carry it, listed under *The nodes* below. What the human said, `verbatim`:

- Payload 1: *"1. The important part are the shipped files but it might be good to do it also on some stuff in the map I don't know, you decide 2. ok for your proposition. I don't have a specific rule in mind but yes, using plain words, make thing clear is good. Right now it is quite hard to understand. 3. ok. I also think by simplifying the text it might be possible to make it smaller maybe finding some generalisation/simplification of some existing stuff 4. ok"*
- Payload 2: *"Q5 ok Q6 ok"*

Q2 to Q6 take the worker's recommendation, with nothing diverging. Q1 was delegated back to the worker (see `## Flags`). Q3 carries the human's addition: generalise or simplify existing material where possible.

### Which files it covers

The twelve shipped files:

- the ten under `.claude/skills/expedition*/`:
  - `expedition/SKILL.md`, `expedition/graph-conventions.md`, `expedition/wayfinder-divergences.md`
  - `expedition-checker/SKILL.md`, `expedition-grilling/SKILL.md`, `expedition-implementation/SKILL.md`, `expedition-precondition/SKILL.md`, `expedition-prototype/SKILL.md`, `expedition-research/SKILL.md`, `expedition-stop/SKILL.md`
- `CONTEXT.md`
- `.claude/rules/expedition-triggers.md`

After them, the same writing rule is applied to the rule statements that are currently live in `map.md` and `map-implementation-rules.md`. Every worker reads the first of these, and every implementation worker and checker reads the second. The human's verbatim words in them stay as they are. Replaced text is banked word for word in `map-history.md` under the `Change the map` procedure.

Under [node 283](283-what-makes-a-change-to-a-record-file-a-node-rather-than-bookkeeping.md) (a change confined to the effort's record is the manager's own), this map part is the manager's own act, not a node. `map-manager-only.md`, `map-history.md`, `decisions.md`, `flags.md` and the node files stay out.

### What "weird English" is, and the fifth standing writing rule

Six features, each paired with its fix:

1. Rules stated as prohibitions. Fix: state the rule as what to do.
2. Bold scattered mid-sentence. Fix: bold a term only where it is defined.
3. Figures of speech and coined phrases for plain ideas. Examples: *"neither pen reaches"*, *"rides a moment that already exists"*, *"claimants"*, *"in as many words"*. Fix: plain words.
4. Slogan-shaped contrasts and reversals. Examples: *"The graph-file ban is about recording, not about files"*, *"Amending is never authoring"*, *"the whole of what"*. Fix: direct statements.
5. Ungrammatical sentences or unclear referents. Example: *"Two things that is not, and neither is loosened by it."* Fix: grammatical sentences, with one clear referent for each pronoun.
6. Sentences that stack clauses with dashes and semicolons. Fix: one idea per sentence.

The definition becomes a **fifth standing rule for writing** in `map-implementation-rules.md`. It binds this effort only, and the human has not carried it into any shipped file. The manager writes it before the pilot is claimed, as its own edit under node 283. It also updates *"Four standing rules"* to five in that file and in `map.md`'s pointer. The rule's text:

> 5. **Write plain English.** State a rule as what to do; use a prohibition only where the rule cannot be said as what to do, and then beside the positive. Bold a term only where it is defined. Say any idea that is not a term defined in `CONTEXT.md` in plain words, with no figure of speech and no coined phrase. Make statements directly rather than as slogan-shaped contrasts. Write every sentence grammatically, with one clear referent for each pronoun. Put one idea in each sentence.

### What compaction may cut

The pass may cut three things:

- explanation of why, down to a clause wherever the reason isn't needed to apply the rule
- repetition inside a file
- words, through the plain-English rewrite.

**Generalisation is allowed where it preserves every outcome.** Several statements may become one general statement only where every case each of them decided comes out the same, and the general statement decides no case the old text left undecided. A generalisation that would change an outcome is a rule change. It is reported as a new node, and the rewrite doesn't make it. Each rewrite worker lists its generalisations on its handover, so the human sees them at the gate.

The pass does not cut or add any of these:

- rules
- fixed templates (text inside code fences stays byte-identical)
- terms defined in `CONTEXT.md`
- refused words.

Where a worker judges a rule dead, or something the model does by default anyway, it reports it as a new node.

[Node 50](50-shared-blocks-stay-duplicated.md) stands: the two shared sections of the five worker contracts stay duplicated.

The size target is soft: an after-text of at most two thirds of the before-text by `wc -w`. The checker reports the figure, and missing it does not fail the work.

### How a rewrite is checked for dropped rules

The checker walks the before-text itself. The worker hands it no list. Each condition states what counts as binding. The checker diffs against the branch's fork point and goes through the before-text section by section, finding each binding statement's counterpart in the after-text. A missing statement, or a changed outcome, fails the check. Units of one file or one section group keep that walk small enough to do properly.

### When it runs relative to the backlog

The pass runs **before** the open backlog.

**The freeze.** While a rewrite node on a file is claimed, no other implementation node naming that file is claimed. Once the rewrite has landed, an open node naming that file is claimed only after its condition has been re-pointed or the node has been superseded.

**Re-pointing.** Each rewrite worker searches the `## Acceptance condition` sections of the open nodes for quoted text and headings from its before-text. This is the duty the manager contract states under `### Changing one after it is written`; the implementation contract doesn't state it, so the spawn carries it. For every match, its handover returns one of two things:

- a replacement for each affected clause, quoting the after-text
- a proposal that the node be superseded as unnecessary, under the widened `superseded` of [node 264](264-no-status-for-a-node-whose-work-no-longer-needs-a-node.md), with the reason.

It names the search it ran. The manager files these after the rewrite lands, when the replacement's words are fixed by the landed work.

**Meaning is preserved.** A rewrite carries existing defects over unchanged, so the open repair nodes still apply to the new text.

### The nodes

Thirteen implementation nodes, listed under this node's handover as NEW NODES:

- the pilot: the research contract
- the other four worker contracts, each copying the two shared sections byte-identical from the landed pilot
- the checker contract
- the manager contract, in three section groups, one after another
- `graph-conventions.md`, in two section groups, one after another
- the three small files together, after the manager contract
- `CONTEXT.md`, last.

After the pilot has landed, the two code slots run two different files at a time. The human corrects the style and how deep to cut at the pilot's gate, before anything else is claimed.

### Search of open conditions

**Handles searched:**

- The twelve shipped paths, across the open implementation nodes' `## Acceptance condition` sections. 57 of the 91 open implementation conditions name a shipped file, and all 57 quote text, 266 quoted passages in all (counted 2026-09-23; a working figure, not authoritative).
- Conditions demanding exact wording in a shipped file. This search was a rough pattern match, so it returns candidates, not confirmed collisions. The fifth rule may collide with the wording these seven conditions demand. Whoever claims or re-points one of them checks for that, and a real collision is a raise, not a flag:
  - `155-carry-the-search-the-record-instruction-into-the-contracts`
  - `190-the-rules-file-states-one-list-twice`
  - `233-ship-the-two-never-delete-tests-into-the-conventions-document`
  - `284-the-worktree-create-command-names-a-relative-path`
  - `81-glossary-code-slot-and-reject`
  - `80-map-items-nodes-64-and-68-left-stale`
  - `97-write-the-adoption-procedure`

**Result:** this node changes no shipped text, so it falsifies no open condition itself. The falsifying facts arrive as each rewrite lands, and the re-pointing duty above covers them.

## Flags

`289.1` **· settled** `DELEGATED` — **Whether the pass reaches the map.** The human wrote *"it might be good to do it also on some stuff in the map I don't know, you decide"*. Decided: the live rule statements in `map.md` and `map-implementation-rules.md` get the same rewrite after the shipped pass lands, because workers read those files. The human's verbatim words stay as they are, and replaced text is banked in `map-history.md`. The other record files stay out. The worker first proposed this as a follow-on node. Node 283 makes a record-only change the manager's own, so it becomes a manager act, not a node. That also corrects the payload's "13 nodes in all": the thirteen rewrite nodes excluded the map node from the count.

`289.2` **· settled** `ASSUMPTION` — **What a generalisation may do.** The human added *"maybe finding some generalisation/simplification"* to a Q3 that forbids cutting rules. Read together, the two mean: a generalisation must give every case it absorbs the same outcome, and decide no case the old text left open. One that changes an outcome goes out as a new node.

`289.3` **· settled** `ASSUMPTION` — **Glossary terms, templates and frontmatter stay.** The plain-words fix reaches figures of speech that aren't defined terms. Terms defined in `CONTEXT.md` keep their spelling. Text inside code fences, and a file's frontmatter, stay byte-identical, which applies standing writing rule 1 ("never compress the shapes"). Renaming a term is a vocabulary decision and a new node.

`289.4` **· settled** `ASSUMPTION` — **Headings cited elsewhere keep their text.** Other files, and the live map files, cite shipped files by heading. So a heading whose exact text appears in any of the other shipped files, `map.md`, `map-manager-only.md`, `map-implementation-rules.md` or `.gitignore` keeps that text. Any other heading may be reworded, merged or removed.

`289.5` **· settled** `ASSUMPTION` — **The human's own sentences in the triggers file keep their meaning, and only their grammar may change.** `git show a70fb82 70ac77c` identifies them.

## Nodes surfaced

The worker's own framing, pasted; each condition is filed whole on its node.

**How the thirteen conditions are made.** Each node's `## Acceptance condition` is the **COMMON CLAUSES** block, copied in full, followed by that node's own clauses, verbatim. This is a transcription, since the common text is identical for all thirteen. The pilot's condition is also written out whole, because it is claimed first.

**How the thirteen questions are made.** Each node's `## Question` is: *"Rewrite <its files or section group> in plain English and shorter, under the pass [node 289](289-a-plain-english-and-compaction-pass-over-the-shipped-files.md) settled."* followed by this handover duty, verbatim:

> Beside the work, the handover carries three things. (1) For every open node whose `## Acceptance condition` quotes text or a heading from the before-text of what this node rewrites: either a replacement for each affected clause, quoting the after-text, or a proposal that the node be superseded as unnecessary, with the reason. Name the search you ran. (2) Every generalisation made, naming the statements it replaced. (3) Any rule judged dead or a default behaviour, reported as a new node and left in the text.

Filed as: A → [290](290-rewrite-the-research-contract-as-the-pilot.md), B–E → [291](291-rewrite-the-grilling-contract.md), [292](292-rewrite-the-precondition-contract.md), [293](293-rewrite-the-prototype-contract.md), [294](294-rewrite-the-implementation-contract.md), F → [295](295-rewrite-the-checker-contract.md), G1–G3 → [296](296-rewrite-the-manager-contract-part-1.md), [297](297-rewrite-the-manager-contract-part-2.md), [298](298-rewrite-the-manager-contract-part-3.md), H1–H2 → [299](299-rewrite-graph-conventions-part-1.md), [300](300-rewrite-graph-conventions-part-2.md), I → [301](301-rewrite-the-stop-skill-wayfinder-divergences-and-the-triggers-rule.md), J → [302](302-rewrite-the-glossary.md). *(Manager's note: the letter-to-number mapping and the file names are the manager's bookkeeping.)*

**Not minted, and the manager's own under node 283:**
- (a) the fifth standing writing rule, whose text is in `ANSWER`, before A is claimed
- (b) the plain-English rewrite of `map.md`'s and `map-implementation-rules.md`'s live rule statements, after J lands
- (c) the freeze
- (d) filing each rewrite's re-pointed conditions and stand-downs after it lands.

## Invalidations

none. The pass preserves meaning and contradicts no resolved node. Node 50's duplication is kept, node 53's "never compress the shapes" is applied, and node 283's file test places the map part. Open conditions quoting the shipped files are falsified only when each rewrite lands, which the re-pointing duty in `ANSWER` covers.

## Retrospective

(1) **What I had to hunt for.**
- What a checker is handed, which decides where a list of preserved rules could live. Found under the checker contract's `## What you are given`. I had first assumed it saw the handover.
- Whether an implementation contract carries node 263's duty to search open conditions. It doesn't: the duty is only in the manager contract, so the spawn has to carry it.
- Node 283's file test, which turned my delegated "map node" into a manager act. I found it only while writing the handover, by grepping `decisions.md` in my head. It should have come up while I was framing Q1.
- Which lines of `expedition-triggers.md` the human wrote. Found with `git log` and `git show` on the human's "Improve rule" and "Add priority to rule" commits.
- The shared-block headings, confirmed by md5 over the five contracts.

(2) **What arrived that this node didn't need.**
- `map.md`, read whole. Only three of its paragraphs bore on this node: the standing preference about document classes, never-delete, and token priority. The retrospective paragraph and the worktree paragraph carried nothing. The map is itself long and in the style under repair.
- `decisions.md`, read whole. About ten of its 170 lines mattered: 50, 53, 54, 252, 263, 264, 283. A search for "shipped", "duplicat" and "record file" would have found them.
- The grilling contract's `## When a node you report is an implementation node` section, which I did use.
- Node 54, read for one sentence, at the right offset, so a narrow read.
- **Better arrangement:** a spawn that names the resolved nodes the node's `## Question` touches. Here those would be 50, 53, 263, 264 and 283.

(3) **What would have made this node easier.**
- A node file listing the resolved nodes that bear on it, 283 above all.
- Per-file word counts, and the count of open conditions quoting each file, which I derived by hand. The frontier script (node 285, not yet shipped) doesn't cover this.
- A way to hand a checker a worker-produced ledger. Its absence narrowed Q5's options.

(4) **What was stale, wrong or contradictory.**
- Node 54's finding that *"`.claude/skills/expedition/` holds no `SKILL.md` at all"* is stale: the manager contract now exists there.
- Node 50's corpus figures (9 files, 27,735 words) are stale against today's 12 files and about 34,400 words. As dated figures they were never authoritative.
- The implementation contract doesn't state the search-the-open-conditions duty that the manager contract assigns to "the party that established" a fact, and an implementation worker is that party. This looks like a gap in node 95's carriage.
- My own payload 2 said "13 nodes in all" while listing 14 items. That is corrected in the DELEGATED flag.

## The manager's disposal

*The manager's own note.* Retrospective items naming the record:
- (4) the implementation contract missing the search duty: **minted** as [node 303](303-the-worker-contracts-do-not-state-the-search-the-open-conditions-duty.md). Until it lands, every rewrite node's spawn carries the duty, as this answer already requires.
- (4) node 54's stale finding and node 50's dated figures: no action. Both are records of what held when those nodes resolved, and neither binds anything now.
- (2) and (3) a spawn naming the resolved nodes a question touches: no action this time. A manager note is limited to context the manager already holds, so listing relevant nodes would mean researching them. If this is reported a second time, the manager mints a node.
