# Carry the method-skill deletion into the four worker contracts

Type: implementation
Status: claimed

Blocked by: none

## Question

*Surfaced by [Whether the contracts' instruction to invoke a method skill is doing any
work](113-whether-the-method-skill-instruction-does-any-work.md)'s worker, and pasted as it wrote it.*

> Make the four contracts state their discipline unconditionally and name no method skill.

**Blockers, in the worker's words:** *"none; composes with node 126 in either order."*

## Acceptance condition

*Written by node 113's worker. Pasted as it wrote it, and not the manager's.*

> All four of the following files, and nothing else, are changed:
> `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`,
> `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`.
>
> 1. In each of the four, the sentence instructing the worker to invoke a method skill is gone. Those sentences are,
>    one per file: *"Invoke `/grilling` and `/domain-modeling` if they are present."*; *"Invoke `/coding-principles`
>    and `/naming` if they are present."*; *"Invoke `/research` if it is present."*; *"Invoke `/prototype` if it is
>    present."*
> 2. In each of the four, the sentence making the discipline conditional on the skill's absence is gone. Those
>    sentences are: *"Where they are not present, this is the whole of the discipline:"* (grilling); *"Where they are
>    not present, the bar and the acceptance condition are what bind you."* (implementation); *"Where it is not
>    present, rules 4 to 6 above are the whole of the discipline."* (research); *"Where it is not present, this is
>    the whole of the discipline:"* (prototype). Where the surrounding text needs a lead-in so the list or clause
>    still reads, it is written unconditionally — stating that this is the discipline, not that it is the discipline
>    in some circumstance.
> 3. No file among the four contains the string `/grilling`, `/domain-modeling`, `/coding-principles`, `/naming`,
>    `/research`, `/prototype`, `mattpocock`, or any other name of an external skill, in any sentence telling the
>    worker to invoke, consult, load or read one.
> 4. The paragraph beginning *"Where a method skill's instructions and this contract's hard rules conflict, the hard
>    rules govern."* is **retained unchanged** in all four files, including its list of three colliding instructions
>    and its instruction to leave the conflicting part unrun and report it.
> 5. `.claude/skills/expedition-grilling/SKILL.md` states both of the following in its own text, as items in its
>    discipline: that the worker works the decisions in dependency order, a decision branching into the decisions
>    that hang off it, so that a question whose answer depends on one not yet asked waits for it; and that finding
>    facts is the worker's own job and never the human's, so where a question needs a fact from the tree or the
>    environment the worker reads it or dispatches a subagent for it, and does not hold up its other questions while
>    that search runs. Neither item uses the word "frontier". Where the file already states an item in its own text,
>    that item counts as met and is not duplicated.
> 6. Nothing in any of the four files makes any part of its discipline conditional on any skill being present or
>    absent.
> 7. No file outside the four listed above is changed.
>
> Held against the bar.

## The manager's note at filing

*Not a change to anything above.*

**This condition names its scope as four files and quotes the exact sentence to remove from each**, which is [node
94](94-condition-scope-as-a-predicate.md)'s rung 3 case — a scope not derived from a search — even though clause 3 is
a whole-file predicate over those same four. The manager has **not** amended it and reads clause 3's domain as the
four named files rather than the tree, which is what makes it well-formed; **that reading is the manager's** and is
correctable.

**One collision the manager sequences rather than the worker.** [Node
126](126-carry-question-batching-into-the-grilling-contract.md) edits the same grilling contract, and its clause 9
already forbids the construction clause 2 here removes. The surfacing worker judged that they *"compose in either
order"*. With a code slot of one they serialise, and whichever runs second reads a file the other moved.

## Answer

*Attempt 1's handover, pasted as its worker wrote it. The manager authored none of it.*

> The four `Invoke <skill> if it is present` lines and the four conditional prefaces are out of
> `expedition-grilling`, `expedition-implementation`, `expedition-research` and `expedition-prototype`. Each
> contract's stated discipline is now its whole discipline, unconditionally, and no shipped contract names a method
> skill. Ground rule 2 — *"each shipped worker contract stands alone as a file, rather than depending on any skill
> being invocable"* — is true of the corpus for the first time rather than aspirational.
>
> **The premise was re-checked before any edit and held.** All eight sentences node 113's worker quoted match
> byte-for-byte, each exactly once, each in the file its clause names: `grep -F` on each of the eight returned one hit
> and no misses. A wider scan for `/grilling`, `/domain-modeling`, `/coding-principles`, `/naming`, `/research`,
> `/prototype`, `mattpocock`, `/writing-for-agents` and `/wayfinder` across the four files returned **only** those
> four `Invoke` lines, and a scan for `present|absent|invocable|invoke` returned only the eight target sentences plus
> four unrelated `DIVERGENCE` lines. So clauses 3 and 6 needed no edit beyond clauses 1 and 2 — there was no second
> conditional construction and no second skill name hiding anywhere in the four.
>
> **How each lead-in was rewritten unconditionally**, per clause 2's *"stating that this is the discipline, not that
> it is the discipline in some circumstance"*. Grilling and prototype: *"Where they/it are/is not present, this is the
> whole of the discipline:"* → **"This is the whole of the discipline:"**. Research: → **"Rules 4 to 6 above are the
> whole of the discipline."** Implementation: → **"The bar and the acceptance condition are what bind you."** In each
> case the sentence's content is the discipline statement and only its conditionality was removed; nothing was
> dropped.
>
> **The node-48 paragraph is byte-identical in all four and was not moved.** Clause 4 is a keep, so the paragraph was
> left exactly where it stood, which after the `Invoke` line's deletion makes it the first thing under each `## How
> you` heading. It keeps its subject: it says *"a method skill"* generically, names none, and `map.md`'s `## Notes`
> still lists all six skills as ones a session should consult — so a worker may still invoke one on its own
> initiative and the reconciliation rule still has something to reconcile. Node 48 is not contradicted. Node 50
> (shared blocks stay duplicated) is likewise satisfied: the paragraph stays duplicated four times and was not
> factored out.
>
> **The grilling contract's two new bullets, and the one call inside them.** Clause 5's item A — dependency order —
> was not stated anywhere in the file and was added as a new bullet: *"Work the decisions in dependency order, a
> decision branching into the decisions that hang off it. So a question whose answer depends on one not yet asked
> waits for it."* Item B was **partially** stated: the existing bullet *"Any fact the files can tell you, read. Ask
> only what they cannot."* carried item B's core (facts are the worker's job, not the human's) but neither the
> dispatch nor the non-blocking half. Clause 5 exempts an item *already stated* from duplication; a partially stated
> item is neither exempt nor honestly met by a second near-duplicate bullet, so that bullet was **completed in
> place** rather than joined by a sibling: *"Finding facts is your own job and never the human's. Where a question
> needs a fact from the tree or the environment, read it or dispatch an agent of your own for it, and keep your other
> questions moving while that search runs. Ask only what no source can tell you."* One item, one bullet, no
> duplication. Neither bullet uses **frontier**.
>
> **Two wording calls inside those bullets.** Clause 5's phrase *"dispatches a subagent"* was written as **"dispatch
> an agent of your own"**, because `CONTEXT.md`'s **Worker** entry refuses `subagent` by name and the glossary is
> declared authoritative; *"an agent of its own"* is the phrasing `map.md`'s review route already uses for exactly
> this object. And clause 5's *"does not hold up its other questions"* was written positively as **"keep your other
> questions moving"**, under `/writing-for-agents`'s negation lever — a prohibition drags the forbidden behaviour into
> context. Clause 5 demands what the file states, not the words it states it in, and its one wording constraint (no
> *"frontier"*) is met.
>
> **`tree` was kept and is not a glossary breach.** `CONTEXT.md` refuses `tree` under **Graph** — as a name for the
> graph, alongside `plan` and `backlog` — not as a name for the checkout, which every contract already calls *"the
> working tree"* or *"the tree"*. Clause 5's own words were kept for that reason.
>
> **The dependency-order bullet is placed first**, ahead of *"One question at a time"*, because it orders the work
> while the rest order the asking. It is a position rather than a demand and reversible in one line.
>
> **Node 126 was read and nothing of it was pre-empted.** Its eight items are all batching, numbering and
> reply-reading; none touches the fact bullet or work ordering, and its *"One question at a time"* bullet was left
> untouched for it. Its clause 9 — *"None of them is left to be supplied by any skill the file instructs the worker
> to invoke, and the file does not make any of them conditional on such a skill being present or absent"* — is now
> **trivially true** of the file it will inherit, since the file instructs the worker to invoke nothing. Its manager's
> note observes the same self-contradiction this node removed. One overlap worth naming rather than a collision:
> clause 9 here and node 126's item 1 both speak of a question whose answer depends on another, but 126's is about
> sharing a payload and this one is about the order work is taken in; they compose.
>
> **Node 51 is open and this work leaves it with no instance.** *"What a contract may name as a method skill"* asks
> how a skill is addressed; after this change no shipped contract addresses one at all. Its premise, not its answer,
> is what moved, and it is reported rather than judged.

## Flags this node raised

*Each in the worker's own words.*

`133.1` — `ASSUMPTION`:

> **Clause 5's item B was completed in place rather than added as a second bullet.** The existing bullet *"Any fact
> the files can tell you, read. Ask only what they cannot."* stated item B's core but not its dispatch or
> non-blocking halves, so it was neither already-stated (clause 5's no-duplication exemption) nor absent. I rewrote
> that one bullet to carry the whole item rather than leaving a thin bullet beside a fuller near-duplicate. The
> alternative reading — add a new bullet and leave the old one — is defensible and produces two overlapping bullets.
> This node had no gate or exchange when the judgement was made, so the account is here.

`133.2` — `ASSUMPTION`:

> **Clause 5's word `subagent` was not used, the glossary refusing it.** `CONTEXT.md`'s **Worker** entry lists
> `_Avoid_: subagent`, and the glossary is authoritative under the map. I wrote *"dispatch an agent of your own"*,
> matching the phrasing `map.md`'s review route uses for the same object, on the reading that clause 5 fixes the
> demand and not its wording. If the condition's literal string was intended, this is the one place the file departs
> from it.

`133.3` — `ASSUMPTION`:

> **`/coding-principles` and `/naming` were not invoked; `/writing-for-agents` was.** The contract line naming the
> first two is what this node deletes, and node 113 measured them as near-no-ops on prose three times. They still
> reach me through `map.md`'s bar as the project criteria, so I held the deliverable against them in substance
> instead: it is prose, coins no term, and introduces no identifier. Ground rule 5's `/writing-for-agents` I did
> invoke, and it changed the deliverable once — the negation in clause 5's item B became a positive instruction.

`133.4` — `ASSUMPTION`:

> **I read one line of `flags.md`, which my contract tells me to leave unread.** Checking whether node 113's
> `CONTEXT.md` findings were still outstanding before reporting a node for them, I grepped `flags.md` for two flag
> ids and got one line back (flag `113.4`). My contract says *"`flags.md` is not yours. Leave it unread."* I stopped
> there and read nothing further. Reported rather than left to be found; the fact it gave me (that `113.4` is
> outstanding) supports the new node below but the node stands without it.

## Nodes this node surfaced

**One, and it duplicates a node that already exists.** The worker proposed *"Bring CONTEXT.md's node-kind entries in
line with the contracts as they now read"*, an implementation node covering `CONTEXT.md`'s skill-count sentence and
its stale `grilling` entry. That is [node 134](134-repair-two-context-defects-node-113-found.md), minted from node
113's handover before this worker was spawned. **No new node is minted.**

***The manager's note.*** **The worker's version of the condition carries something node 134's does not**, and it is
carried onto node 134 rather than lost: an **enumerator with a domain**, naming six contract files and seven strings
and demanding the scan return nothing. Node 134's clause 1 states the same demand as a property with no enumerator.
Under [node 94](94-condition-scope-as-a-predicate.md)'s rungs that is the difference between rung 2 and rung 1.
**The manager has not substituted one for the other** — node 134's condition was written by node 113's worker and is
not the manager's to rewrite — and has filed the offered text beside it for whoever holds node 134 to raise.

## What this node's work invalidates

*Pasted as the worker wrote it.*

> none. Node 48 was checked directly: its paragraph is byte-identical in all four files, keeps its generic subject,
> and `map.md`'s `## Notes` still names the six skills, so a worker may invoke one on its own initiative and the rule
> still has an object. Node 50 is satisfied rather than contradicted — the paragraph stays duplicated four times and
> was not factored into a shared file. Two things moved that are not invalidations because their nodes are open:
> **node 51**'s premise, which now has no instance in the shipped corpus, and **node 126**'s clause 9, which is now
> trivially true of the file it inherits. And one recorded expiry is one step closer without firing: node 113's own
> answer notes that `map.md`'s `## Notes` entries for `/grilling` and `/domain-modeling` stop being correct when
> nodes 126 and 130 land; both are still open, so the clause is correct today.

## The checker's runs

### Run 1 — `PASS`

*Spawned by the manager, given the condition as extracted text, the bar, the paths, the worktree and the effort's
ground rules copied as text, and nothing from this record.*

**It died once and was resumed rather than replaced**, under [node
119](119-dead-attempt-respawned-rather-than-resumed.md)'s rule. The death was an API session limit at **118 records,
572,259 bytes**, read from its transcript rather than from the harness summary. Its own first line on resuming:
*"The tree is exactly as I left it — worktree HEAD `9c9e23d`, master `d6dd13f`, the same four modified files, nothing
staged or untracked, the same diff shape, and nothing dirty outside `.scratch/` in the main checkout. My outcome rests
on that re-observation."*

**Outcome: `PASS`**, covering the seven clauses and the bar's non-command half. Its clause-by-clause finding, pasted:

> 1. Met. All four invoke sentences gone; zero occurrences of `invoke`/`Invoke` and zero slash-tokens remain in the
>    four.
> 2. Met. All four lead-ins now unconditional and reading correctly in context; research's "Rules 4 to 6 above"
>    resolves to three rules that exist.
> 3. Met. Over unwrapped paragraphs, none of the six skill names, `mattpocock`, `consult`, `load` or `plugin` appears
>    in any of the four; `skill` survives only inside the clause-4 paragraph. No "What you read" list names a skill.
>    Across the whole shipped surface post-change, the only slash-token anywhere is `/wayfinder` in
>    `wayfinder-divergences.md` — the ancestor workflow, named in CONTEXT.md's **Expedition** entry, not a method
>    skill.
> 4. Met. I reconstructed the paragraph from `HEAD` and compared unwrapped text: byte-identical in all four, list of
>    three and the leave-unrun instruction intact.
> 5. Met. Both items present as discipline bullets, all three parts of each. Neither uses "frontier". The worker
>    rendered the condition's "dispatches a subagent" as "dispatch an agent of your own" — correct, since `subagent`
>    is on **Worker**'s `_Avoid_` list and the glossary is authoritative over these files' words.
> 6. Met. No `if it/they is/are present`, no `where it/they is/are not present`; `present` survives only in the
>    `DIVERGENCE` sense. The retained paragraph is conditional on a *conflict*, not on presence or absence.
> 7. Met over the worktree holding the work, re-observed: exactly the four modified, nothing staged, nothing
>    untracked, nothing new-and-ignored. Across both worktrees nothing is modified outside the four except files
>    under `.scratch/`.

**On the bar:** *"Command half vacuous, and I found nothing contradicting the map's record: the repo is ten tracked
non-record files, all markdown plus `.gitignore`; no manifest, no task runner, no CI directory, no repo-level
settings or hooks, nothing tracked carrying an executable bit, one ignore file invoking nothing. No command to run,
so nothing printed."*

**On the enumerator duty:** *"This condition records no enumerator and no return, so there is nothing here to run in
its name and no mismatch to report."*

**Three `_Avoid_` hits it cleared rather than raised**, in its words: *"`tree` (**Graph**), and `decision`/`question`
(**grilling**). CONTEXT.md itself uses "tree" five times in the working-tree sense inside the same glossary that lists
it, and the **grilling** entry's own gloss reads "A decision only the human can make, reached by interviewing them one
question at a time" while listing all three words. So `_Avoid_` bans a term as a *name for that concept*, not the
English word."*

#### What it handed back alongside its outcome — five questions

*Its own framing:* **"All five are the same shape: the condition is met, the work complied, and complying is what
produced the effect. Each wording is the condition's own and so was not the worker's to depart from."**

> - **Two sentences outside the four now contradict the shipped state.** CONTEXT.md `## The five kinds of node`:
>   *"Each names what its worker does, and three of them name a skill the worker invokes."* — no worker invokes one
>   now. And `.claude/skills/expedition-precondition/SKILL.md`: *"There is no method skill for this kind of node."* —
>   a distinction that no longer distinguishes. Form: a sentence in a shipped file outside the four asserting or
>   presupposing that some worker invokes a method skill. Extent: an unwrapped-paragraph search for `method
>   skill|invokes? a skill|names a skill` across all nine shipped files plus CONTEXT.md returns exactly these two
>   outside the four, plus the clause-4 paragraph inside each of five contracts. Clause 7 forbade the worker either
>   file.
> - **grilling's and prototype's shared bullet now diverges.** Both carried *"Any fact the files can tell you, read.
>   Ask only what they cannot."*; clause 5 sharpened grilling's copy only, so prototype — which runs the same
>   one-question-at-a-time exchange — now states the weaker discipline. Extent (bounding set): the discipline lists
>   of the four, five bullets each in grilling and prototype and none in the other two; comparing them bullet by
>   bullet, this is the one divergence, and the two files' other shared bullets are still identical.
> - **The clause-4 paragraph now opens on an unintroduced referent.** It is the first thing under each `## How you
>   ...`, and "a method skill" is a definite noun phrase nothing in the file introduces; "Leave the conflicting part
>   unrun, run the rest" presupposes an invocation no file instructs. Not a no-op — a model-invoked method skill can
>   still fire on its own, so the guard still changes behaviour — but a co-location cost clause 4 mandated. Extent:
>   the five shipped contracts carrying `method skill`, enumerated above.
> - **Three wordings clause 5 dictates read ambiguously in this file.** "Work the decisions in dependency order" can
>   read as ordering grilling *nodes*, which the file's own hard rule 4 forbids; "a fact from the tree" is ambiguous
>   in a contract whose named sources are `map.md`, `decisions.md` and node files; and "keep your other questions
>   moving while that search runs" sits two bullets below "One question at a time. Wait for the answer before asking
>   the next." and can read as licensing parallel questions. Extent (bounding set): the two items clause 5 adds are
>   the only text it dictates, and I read both against the file's hard rules and its other four bullets.
> - **The new item licenses an agent nothing binds.** "read it or dispatch an agent of your own for it" — the
>   contract's hard rules bind "you" (writes no file, has no human-facing tool), and nothing carries them onto the
>   dispatched agent. Ground rule 3's second half is not breached, since nothing tells that agent to address the
>   human. Extent: an unwrapped search for `dispatch|spawn|agent of your own|subagent` across the four returns this as
>   the only dispatch licence; every other hit is the manager spawning the worker.

#### The part of the condition it could not cover

> - "No file outside the four listed above is changed." I establish this over the worktree that holds the work, and
>   over the repository's shipped surface. What I cannot establish is the residue: the main checkout carries
>   modifications to six files and one untracked file, all under `.scratch/graph-workflow/`, which is the effort's
>   record. I did not read them, and whether any is part of this work is settleable only by the party holding the
>   record.

***The manager establishes this part, which is the one party who can.*** **Every modified and untracked file under
`.scratch/graph-workflow/` at that moment was the manager's own graph writing for other nodes** — nodes 107, 128,
136, 137 and 138, filed while this check ran — and **none of it is node 133's work**. The manager holds the record and
is its only writer; no worker on this node ever writes there. The `.scratch/` tree ships nothing and is committed
separately from any node's code, so clause 7's demand is met over everything clause 7 can reach.

## The manager's own failure during this check, recorded against itself

**The manager told this checker that no standard had moved, minutes after receiving a standing direction that moves
exactly the standards it was using.** The resume message said *"No standard moved. The acceptance condition in your
first message is unchanged and unamended, the ground rules are unchanged, and the bar is unchanged."* The human's
direction — that a checker must not go and find the skill or the rules, and that `mattpocock-skills:code-review` is
not to be used because it is too generic — had arrived before that message was sent, and the manager had already
superseded the map's review route on the strength of it.

**What the checker then did, in its own words:** *"The reviewing skill. `code-review`, in the same plugin. I ran its
**Standards** axis with the givens supplied … I left its **Spec** axis and its step 2 (identify the spec source)
unrun."* So it ran the skill the direction bars, and it found it by the discovery route the direction bars, because
the manager told it nothing had changed.

**This is the sixth time this session the manager has put into an agent's context something the record did not
support**, and the first where the false statement was about a rule the human had just given.

**What the manager has not decided, and will not:** whether this `PASS` stands. The direction was not in force when
the check began, the standards the skill's axis was run against were supplied by hand rather than discovered, and the
checker triaged the skill's findings itself. Whether that is enough is the human's call at the gate below, and the
manager states the fact rather than the verdict.
