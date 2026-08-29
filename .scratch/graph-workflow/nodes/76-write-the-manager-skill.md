# Write the first version of the manager's skill

Type: implementation
Status: resolved

Blocked by: 75

## Question

Write the manager's contract — the file that says what the manager does — as its **first version**, from the
enumerated duty list [Gather the manager's accumulated duties into one enumerated
list](75-gather-the-managers-duties.md) produces.

### The human's instruction, `verbatim`

> *"I think the priority should be writing the first version of the manager skill as now you don't have any way to
> know what to follow as the information is split everywhere."*

**"First version" is the scope**, and it is doing work: this file does not have to settle what is still open. Where
a duty is unsettled it is written as unsettled, and where two nodes conflict the file says so — node 75's clauses 4
and 5 exist to hand this node those cases already separated.

## Acceptance condition

*Written by [Gather the manager's accumulated duties into one enumerated list](75-gather-the-managers-duties.md)'s worker, under [A worker's handover carries no acceptance condition for the node it mints](35-handover-mints-no-condition.md)'s rule, and read back by that worker against node 33 and node 36 before being handed over.*

The work creates **one new file**: a `SKILL.md` at a path matching `.claude/skills/expedition*/SKILL.md` that did not exist before this work. Done means every one of the following is true of the finished tree.

**Shape**

1. The new file carries YAML frontmatter with a `name` field matching its own directory name and a one-line `description`, in the same frontmatter shape as every other `SKILL.md` already under `.claude/skills/`.
2. It is a contract addressed to **the manager** in the second person, in the instructional voice of the sibling files under `.claude/skills/expedition-*/SKILL.md`. It states rules and procedures and carries **no** account of how the workflow came to decide them: no node numbers, no dates, no commit hashes, no evidence tables, no rejected alternatives, and no narrative of what happened on any past effort. A statement of what a rule protects is permitted and is not history.
3. It **stands alone as a file**: everything binding on its reader is in it, so a runner with no skill-invocation mechanism gets the same instructions by reading it. It may name another skill or file, but nothing it requires may be reachable only by invoking one.
4. It is navigable by heading, so a reader following a pointer for one fact reads one section rather than the file.
5. It defines, in its own text, every term it uses in a special sense — at minimum: manager, worker, checker, node, spawn, handover, relay, park, raise, gate, flag, marker, promote, resolve, close, supersede, acceptance condition, the bar, code slot, sweep, cascade, frontier, scribe.

**What it must state.** Each of the following is a statement the file makes; the wording is the author's.

6. That the manager is one long-lived thread which owns the graph, spawns one worker per node, and is the only party the human talks to — and that no agent the workflow spawns addresses the human directly.
7. That the manager is the graph's only writer, and that it writes as a **scribe**: it pastes each part of what an agent hands back under the right heading and never re-authors, shortens, re-orders, re-renders or improves it, and anything the manager has of its own goes beside that text as its own marked note.
8. That the manager never answers a question on the human's behalf — including when the human says *"you decide"* or reframes a question mid-interview, both of which go back to the worker holding that node.
9. That the human's words are written into the node's log **at the moment they speak**, in the same turn the worker is resumed, and are pasted as written however terse and marked `verbatim`; that where the reply takes an option it was offered, the option is quoted in the same entry and attributed to whoever wrote it; and that where a terse reply does not make clear which option it points at, the manager records the reply and asks which.
10. That an answer contradicting the recommendation the worker gave is additionally marked as a divergence, so the worker does not resolve as though it had won its point.
11. **What a spawn carries**: the node, the statement that the worker is not the manager and has no channel to the human, the contract to follow, the pointers the worker reads, the per-kind additions, and optional notes from the manager — and that a manager note is capped at context the manager already holds, so the manager does not read code or run research to produce one.
12. That two further things may travel in a spawn and are governed by neither that cap nor the per-kind list, because neither is the manager's own: **a direction of the human's**, carried as their words and marked as theirs; and **a licence** the human granted in answer to a manager's raise.
13. That the manager may **not** depart from a worker contract on its own authority; that where a clause of a contract blocks the node in front of it the manager raises to the human; and that the answer produces two things, always both — a licence for that one attempt, recorded as a flag on the node, and a node for the permanent fix. It states that a licence changes nothing on disk and that amending a contract is its own piece of work rather than something the manager does mid-flight.
14. That nothing the manager sends a worker may widen what that worker is permitted to write.
15. **What the checker is given, and by whom**: that the manager and not the implementer spawns the checker, because whoever spawns it chooses what it sees; that what it receives is the acceptance condition as extracted text, the bar, the changed paths in the working tree holding them, and the effort's standing ground rules copied as text; and that it is given nothing from the effort's own record.
16. That only a **standing constraint on the effort, true of any node's work,** may be copied into a checker's spawn, and that an account of what happened — on this work or anywhere in the record — never travels that route.
17. That the manager hands a defective acceptance condition to the checker **as written** and supplies nothing it omits, because supplying it would make the manager the author of the standard the work is judged against; and that where what is missing is what the check turns on, that goes to the human instead.
18. **What the manager does with what an agent hands back**: that the test is whether the manager can file it, never whether the agent followed its contract; that a return carrying everything required plus something unasked-for, or taking a route the contract does not offer, is filed; that what a return departed by becomes a flag beside it, filed by the manager; and that only a return the manager cannot file at all is sent back, once, naming the missing part — with a second such return neither re-sent nor respawned, the manager filing what it can, leaving the node open, and telling the human once.
19. That before filing, the manager holds what an agent wrote against the human's own words already on the node, and files anything resting on words the human did not say as a flag beside it rather than refusing it.
20. **What the manager does at a gate**: that it assembles the payload from other people's text rather than writing it — the checker's runs laid end to end oldest first, the node's flags, the node, the paths the worker reported touching, the proposed commit message, and a pointer to the tree — and that it never renders a diff into the conversation and never puts the acceptance condition in front of the human.
21. That a flag reaching the human carries what was done, why, and the context needed to answer it, so that answering never requires opening a file — and that a payload omitting a flag settles that flag silently, the human's approval of a node's end being its settlement.
22. That a gate has exactly three outcomes — approve, correct, reject — with corrections uncapped; that on approve the manager commits and the node resolves; and that on reject the graph is edited **before** the working state is cleaned.
23. That reject means implementing the node taught the graph that this code should not exist, rather than that the code was poor, and that *try again differently* is a correction; and that a rejected node goes to one of exactly three places — ruled beyond the destination, superseded by a replacement, or returned to open behind a new blocking edge on the upstream fix.
24. **What the manager does with a flag**: that the text of both of a flag's entries is the raising agent's, and what the manager adds is bookkeeping only — the flag's id, the link to its node, and its state; that raising one writes the node's entry first and the index line second, both as part of raising it and never as a tidy-up; and that settling one writes both places, with the index file winning where the two disagree.
25. That a node's flags are settled at the human moment that ends that node, while the work is still there, and that the closing report carries only the flags that never had such a moment.
26. **What the manager does when an agent dies, stops, or cannot be filed**: that death is discovered only by a resume that fails, so the manager marks that attempt dead rather than retrying it; that the node keeps its number, its file and its claim, the claim belonging to the node and not to the agent; that a fresh agent is given the node plus the full replayed exchange and told that everything already answered is settled and must never be asked again; that the human is told once, by node name, and is owed no answer; and that after two replacements a third failure is not a crash to retry but evidence the node is too coarse, and goes to the human as a question about the shape of the graph.
27. That an agent the human stopped cannot be resumed at all, so a stop is handled as a fresh attempt rather than as a re-prompt.
28. **What the manager puts in front of the human, and when**: that exactly one question is in front of them at a time and nothing ever displaces a live one; that everything else waits in a queue with two tiers; that the first tier holds exactly three kinds of thing — a gate, a worker blocked on a raise, and the manager's own raise — and that adding a fourth is a decision and never an inference; and that a relayed question names in one line, by node name and kind only, whatever else is waiting.
29. That the manager picks the next node itself and reports the pick rather than asking which node to work; that a scope or emphasis the human gives is written into the effort's map and reported back in every pick it constrains; and that a named-node instruction is one pick and expires when used.
30. That three states are invisible in the graph's files and the manager must be able to report them: which node is waiting for approval, whether a worker is blocked, and what work is banked and waiting.
31. **What the manager may never do**, gathered in one place: answer for the human; re-author what an agent wrote; author an acceptance condition for a node an agent minted; author the text of an agent's flag; rewrite an acceptance condition; render a diff; decide between a worker and its checker; or close an effort.
32. That a condition for a node **the manager itself minted** is the manager's to write, under four constraints stated in full: it may demand only what is already fixed — by a settled node, by the node's own question, or by the state of the files — and anything the manager would otherwise have to decide is not written into it, the manager stating the property and leaving the form to the worker or putting the question to the human; the manager reads the condition back against the two rules that bind every condition before the node is claimed and records that reading on the node; the condition is marked on the node as the manager's own; and the report accompanying the pick says that it is the manager's and what it demands, without the work waiting for a reply.
33. That where the manager cannot write such a condition in full it writes the part it can, says plainly what is missing and why, never omits it in silence, and puts what is missing to the human — and that the node is not claimed until the condition is complete.
34. That an implementation node may not be claimed at all until it carries an acceptance condition.
35. That the manager's own context is the resource that fails first, that most of an effort's context is meant to live in its workers rather than in the manager, and that a manager which ends a node holding everything the node held has failed at its job even if the node resolved.
36. That only the human closes an effort, that most efforts never end and a frontier that never empties is a legitimate steady state rather than a failure, and what the report that precedes a close contains.

**Honesty about what is unsettled**

37. The file contains a section, under a heading of the author's choosing, listing the duties of the manager that are **not settled** — each stated as a question the workflow has not answered, with no answer invented for it. It contains at minimum these, each stated in the file's own words: that nothing lists what the manager's report to the human must contain; that nothing says whether a checker is handed the route for reviewing work or must find it; that nothing checks a flag before the human settles it, and that a flag put in front of a checker and a flag put in front of the human need opposite treatments; that an implementer given a finding it believes is false has no route but to fix it; that nothing tells a worker to go and look at the record when reporting what its work invalidates; that nothing says what a worker does when a file it must read is being changed by whoever holds the code slot; that the manager writes a section on a node which the graph's own file format does not define; that the manager files flags about its own conduct with nothing between the judgement and the record; and that nothing bounds what a spawn may assert about the conclusion the node it dispatches is meant to reach.
38. The file contains a section, under a heading of the author's choosing, naming the places where **two settled duties overlap or pull against each other**, saying so and resolving none. It contains at minimum: that the rule making the manager a scribe pulls against the requirement that the manager write a fuller form of another agent's flag for the human; that the rule forbidding the manager to supply what a condition omits pulls against its permission to author a whole condition for a node it minted; and that the rule ordering the human's queue by arrival does not say whether a gate may go ahead of an older question.
39. Where the file states a duty that is a **standing instruction of the human's for one effort** rather than a rule of the workflow, it says so at that point and does not present it as a rule of the workflow.

**What must not change**

40. No file under `.scratch/` is changed by this work.
41. No existing file under `.claude/skills/` is deleted, and no heading is removed from any existing file under `.claude/skills/`: the headings of each such file, listed by `grep -n '^#\{1,6\} '`, are all still present afterwards and in the same order.
42. No file outside `.claude/` is changed by this work, except that `CONTEXT.md`, wherever in the repository it lives, may gain new glossary entries; no existing entry in it is edited or removed.

**The bar**

43. The working tree meets the bar. Two properties of the bar bite hardest here and are stated so the reader holds them: prose that explains *why* may be compressed and named shapes may never be; and a prohibition is paired with what to do instead wherever it can be phrased that way.

### Two things the author of this condition could not settle, stated rather than decided

**Where the file lands** is left as a property — a new `SKILL.md` under a `.claude/skills/expedition*` directory — because node 76's own note records the location as open and flag `21.2` records an install location being pinned inside live fog once already; the condition is satisfiable whichever directory is chosen. And **the file's length** is left unstated: the two shipped documents nearest in kind measure 318 and 436 lines, the standard this repo reviews prose against charges *sprawl* as a failure in its own right, and no node has ruled on where the line falls, so a ceiling here would be a decision rather than a demand.


## What this node already knows, and does not have to rediscover

*The manager's own note, filed at creation.*

- **Where it lands is not settled.** The six worker contracts sit at `.claude/skills/expedition-<type>/SKILL.md`,
  and the conventions document at `.claude/skills/expedition/graph-conventions.md`. Whether the manager's file is a
  seventh sibling, or lives inside `expedition/`, is open — and flag `21.2` already records that the install
  location was pinned inside live fog once before.
- **Two adjacent files are already split out and are not this node's**: [Write the cascade pass's worker
  contract](44-cascade-worker-contract.md) and [What the manager reports to the human](46-what-the-manager-reports.md).
- **[Whether the workflow ships explicit subagent definitions](69-explicit-subagent-definitions.md) settled that the
  manager does not become a declared subagent type**, and that a hard rule binds by being read rather than by being
  enforced.
- **Ground rule 2 applies to this file too**: it must stand alone as a file rather than depending on any skill being
  invocable.
- **[Run an implementation node's work in a worktree](68-implementation-in-a-worktree.md) put the whole worktree
  lifecycle on the manager**, and observed that the manager has no skill file — so until it does, that lifecycle
  lands in `map.md`. [Carry the worktree lifecycle into the shipped files](74-carry-the-worktree-lifecycle.md) does
  that; **this node is where it eventually belongs.**

### Audit of the condition, by the manager, before claiming

*Read against [An acceptance condition is self-contained text](33-condition-is-self-contained.md) and [The clause
that says no resolved node changes cannot be self-contained](36-resolved-node-clause-cannot-be-self-contained.md).
Done before the node is claimed so a defect is found here rather than in a worker's third hour — the practice that
caught an unsatisfiable clause on [Gather the manager's accumulated duties into one enumerated
list](75-gather-the-managers-duties.md).*

**All 43 clauses pass, and this is a condition written by a spawning node's worker** — the class [A worker's
handover carries no acceptance condition for the node it mints](35-handover-mints-no-condition.md) measured as
having never failed the self-containment rule.

**Three things verified rather than trusted.** There are **six** sibling `SKILL.md` files under
`.claude/skills/expedition*/`, and **every one carries exactly `name` and `description`** — so clause 1's *"same
frontmatter shape as every other `SKILL.md`"* names a shape that is uniform and discoverable rather than a
judgement. And the two documents the author cites for scale measure **436 and 318 lines**, exactly as stated.

**Clause 2 is where the condition comes closest to pointing, and it stays inside the rule.** *"In the instructional
voice of the sibling files"* is a standard defined by files rather than by the text — but the checker is given the
repo, those six files are named by glob, and node 33 permits a path that says **where**. The demand itself —
*rules and procedures, no account of how they were decided* — is stated in the clause and enumerated: no node
numbers, no dates, no commit hashes, no evidence tables, no rejected alternatives, no narrative.

**Clauses 40, 41 and 42 quantify over the tree**, which node 36 permits, and clause 41 supplies the command.
**Clause 43 is the bar, the one exemption**, and it reaches the checker by its own route.

### Three things whoever claims this should know, none of them defects

**1. The deliverable inverts this effort's own citation discipline, and that is deliberate.** Every graph file here
states an item and cites the nodes that shaped it. **Clause 2 forbids exactly that** in the shipped file: no node
numbers, no history. So the 181 cited duties in node 75's answer become un-cited rules. That is right — a shipped
contract travels to repositories that have no such graph — but it means the input and the output have opposite
rules, and a worker that carries the citations across has failed clause 2 rather than been thorough.

**2. "Creates one new file" is the headline; three clauses are looser than it.** Clause 41 forbids **deleting** an
existing skill file or **removing a heading** from one, which permits editing them; clause 42 permits `CONTEXT.md`
to **gain** glossary entries. So the work may touch more than the new file, within those bounds. Whoever claims this
should not read the opening sentence as a one-file ceiling, and should say in its handover what it touched.

**3. Clause 37 is nine statements, not one.** It requires a section listing what is unsettled, and enumerates nine
things it must contain at minimum. It is the clause most likely to be discharged shallowly, and the one whose
absence would matter most: **a manager's contract that reads as complete when nine of its duties are open would be
worse than no contract at all.**

### One risk the manager names and does not repair

**This is a 43-clause condition over a long prose deliverable, and the check will be expensive.** Node 75's answer —
the input — is 93,000 characters, and the file to be written is bounded by nothing (clause 43's author left the
length unstated on purpose). The checker will establish 43 clauses over a document nobody has seen. **That is the
condition the worker wrote and it is not the manager's to trim**, but it is worth the human knowing before the check
is spent, and it is the strongest case yet for [What a finding must carry so it can be
swept](71-what-a-finding-must-carry.md) landing before this node's check rather than after.

## Manager's note: one duty was added after node 75's list closed

*Filed at [What a finding must carry so it can be swept](71-what-a-finding-must-carry.md)'s gate, before this node
was claimed. **Not a change to the acceptance condition above**, which stands exactly as node 75's worker wrote it.*

The list this node is built from is **one duty short**, and the missing one is recorded as an annotation on
[Gather the manager's accumulated duties into one enumerated list](75-gather-the-managers-duties.md) rather than
here: *the gate payload names the worktree's path and the command that shows its diff.* It is also now in
`map.md`'s landing policy.

**Whoever claims this node reads that annotation with the list**, and decides whether the duty belongs in the
skill's first version. The manager has not decided it, and the condition does not reach it either way — clause
coverage is defined over node 75's answer, and this is an addendum to it.

**Why it matters beyond one line.** The annotation records *how* it was missed: three resolved nodes each intact,
and the duty living in the hole between them. A gather over resolved nodes cannot produce a duty no resolved node
states. If the skill this node writes is going to claim completeness over the manager's conduct, that limit is the
one it should be honest about.

## Answer

**The manager has a contract.** It ships at `.claude/skills/expedition/SKILL.md`, 578 lines, landed as `4f9781b` —
and because it took the name the workflow is invoked by, the harness now offers `expedition` as an invocable skill
and the conventions document and the glossary become its bundled resources rather than orphans beside it.

**Sixteen headings, each answering one question a manager has in the moment**: what it is; `## Words used exactly`
defining 37 terms; `## What is never yours`, an eight-row table pairing every prohibition with what to do instead;
then writing the graph, spawning a worker, the checker, what comes back, the gate, flags, acceptance conditions,
what is in front of the human, death and stops, closing; and the two honesty sections last.

**The scribe rule is stated once and `Assembling is not authoring` carries it everywhere else** — extraction for a
checker, payload assembly at a gate and re-running the bar all sit inside the boundary by that one sentence rather
than by three exemptions.

**The citation discipline is inverted on purpose.** Node 75's 181 duties each cite the node that produced them;
clause 2 forbids exactly that here, so every rule in the shipped file is un-cited. A shipped contract travels to
repositories that hold no such graph.

**Honesty about limits is the load-bearing section rather than the footer.** `What nothing here settles` carries
nine open questions with no answer invented for any, and closes with the limit of the method that produced the
file: what is written was gathered from what the workflow actually decided, **so a duty that follows from two
settled rules and is stated by neither is not in it.** That paragraph is this node's own, and both gaps the human
found at the gate — the manager's cascade duties, and the human's four moves on the closing report — are instances
of exactly the limit it names. `Where two of these pull against each other` names three collisions and resolves
none.

**Length was the one judgement the condition's author declined to make**, and it stands at 578 lines against
siblings at 436 and 318. Three clauses jointly forbid the cure the prose standard prescribes: the file must stand
alone, its glossary must be in its own text, and both honesty sections must be *in* the file. No progressive
disclosure is available at any length, so the size is a consequence of the condition. The blind checker measured
it at every run and declined to charge it each time, on the ground that no source it held states where the line
falls.

**What the file deliberately does not carry**: the worktree lifecycle, which no clause reaches and which assumes a
toolchain against ground rule 1. It states the tool-neutral half instead — the gate payload names where the work
is and the command that shows its diff — and points at the effort's own landing policy for the rest, fixing only
the two orderings that hold everywhere: approval before any commit, and the graph edit before the cleanup.

## Flags

*Seven. Six are the worker's, filed as it raised them across three rounds; the seventh is the manager's.
The text of each is the raising agent's and the manager added only the id, the link and the state.*

`76.1` **· settled** `ASSUMPTION` — **The install location was chosen rather than raised.** The condition states the location as a
property and its author recorded at flag `75.2` that fixing a path would have been a decision inside a condition.
Two directories satisfy it: a seventh `expedition-manager/` sibling, or the existing `expedition/`. The worker chose
`expedition/`, on three grounds held together — the six siblings are named for node kinds and the manager is not
one; that directory's lack of a `SKILL.md` is the recorded cause of nothing pointing at `graph-conventions.md`; and
`/expedition` is the name the workflow is invoked by, so the entry point and the manager are the same thing. Flag
`21.2` records an install location being pinned inside live fog once already, which is why this is a flag.

*Manager's note beside the worker's text, which is left as written.* **The citation `21.2` does not resolve.**
[Write the graph conventions document](21-conventions-document.md)'s flags predate flag ids and carry none, so
there is no `21.2` in `flags.md` — the mechanical check joins on the pattern and reports it as missing. The flag
being pointed at is real and is that node's second: *"the document's path pins where the skill installs… This is
still a judgement made inside live fog rather than one a resolved node fixed."* The id came from the manager's own
note at this node's creation and the worker copied it in good faith. **Twenty legacy flags carry no id**, and
citing one positionally reads as an id and resolves to nothing.

`76.2` **· settled** `ASSUMPTION` — **The duty added after node 75's list closed was included; the lifecycle around it was not.**
Included: the gate payload names where the work is and the command that shows its diff — general, and tool-neutral
as phrased. Excluded: the worktree lifecycle itself, because no clause reaches it, it assumes a toolchain against
ground rule 1, and `map.md` marks the worktree placement as this effort's own practice with flag `68.2` open. The
file points at the effort's landing policy for the how and fixes only the two orderings that hold everywhere.

`76.3` **· settled** `ASSUMPTION` — **`CONTEXT.md` gained one entry, `Scribe`.** Clause 42 permits the glossary to gain entries
and forbids editing one; the diff is seven added lines and no deletion, 50 entries to 51. `scribe` is the leading
word the contract is built on and was already used in `graph-conventions.md` with no entry behind it, which is the
defect class node 29 exists for.

`76.4` **· settled** `ASSUMPTION` — **A checker's question was routed through the gate payload rather than into tier 1.** Two
repairs were available for the closed-list finding. Adding a fourth tier 1 member is explicitly forbidden — clause
28 makes that the human's decision and never an inference — so the question rides the gate payload, which is where
the checker's own contract already sends it. In the worker's words: *"That leaves one case unaddressed and I am not
repairing it silently: a checker that raises instead of judging issues no outcome, so there is no gate to carry its
question, and it reaches the human by tier 1 as the manager's own raise."*

`76.5` **· settled** `ASSUMPTION` — **Where the duplication was cut, the worker drew the operative/format line itself.** In its
words: *"I kept every sentence that tells the manager what to do and cut every sentence that explains why a
recording rule is what it is, illustrates it with an example, or says which party performs a step… Someone may
reasonably think one of the five compressions went a sentence too far — the likeliest is the checker passage, where
I removed the fact that a defective condition may be raised either by the manager before the check or by the checker
during it."*

`76.6` **· settled** `ASSUMPTION` — **Two clause-mandated statements were absent after the human's own edit and the worker did not
restore them.** In its words: *"Restoring them would revert the human, which I was told not to do; leaving them
unremarked would ship a file that fails two clauses the checker had already established. So they are reported…and
the choice is the human's."* **Settled by the human at `## Interview` attempt 1** — clause 27 restored in one
sentence, clause 36's demand amended away.

`76.7` **· settled** `DELEGATED` — **The manager decided whether to restore clause 27's statement.** *The manager's own flag.* The
human's words gave it the choice — *"if you want you can put it back"* — and the manager chose to restore it in one
sentence rather than as the paragraph that was cut, on the ground that the human's stated reason was the token cost
and that reason survives their permission. **The manager also withdrew its own argument for restoring**: it had told
the human a reader would wrongly try to resume a stopped agent, when the file already makes attempting the resume
the detector, so a stop lands correctly by the general mechanism and the cut sentence was explaining rather than
ruling. What remains is only that the section's heading names a case its body did not mention.

## Review

### Run 1 — `FAIL: acceptance condition` and `FAIL: the bar`

Established clauses 1, 2, 3, 4, 6–38, 40, 41 and 42, and both of clause 43's named properties, each
checked rather than assumed: clause 2 by a scan for history markers returning nothing; clause 3 by
`grep -i skill` returning zero hits; clause 31's eight rows against the eight it names; clause 37's nine
items mapped one by one, with item 7's factual claim independently verified against
`graph-conventions.md`'s section list; clause 43(b) by enumerating all 34 prohibition sentences and
reading each for its positive target.

**Six findings, every one carrying its form as a predicate and its extent** — the first check run under
[What a finding must carry so it can be swept](71-what-a-finding-must-carry.md)'s contract, landed the
day before.

1. **Clause 5** — seven terms used in a special sense and never defined, `map` the sharpest at 7 uses
   and 0 definitions while three duties command a write to it. Extent: an enumerator subtracting the
   file's defined terms from the glossary's 51 headwords, 18 remaining with hits, all read. **The
   checker stated its own limit**: the enumerator cannot reach a term with no glossary headword, and
   `exchange` was one such, found by reading — so for that sub-class it said plainly that its instances
   were not exhaustive.
2. **A refused word used for the concept it was refused for** — `CONTEXT.md`'s **Handover** refuses
   `return` by name, and the file used it six times while using `handover` exactly once, in its own
   definition.
3. **Named shapes compressed**, standing writing rule 1: `handover` et-cetera'd where a shape belongs,
   `raise` dropping the checker member, `checker` dropping *"a `FAIL` names which of the two was not
   met"*. Extent as a **bounding set** — the 25 entries under one heading, compared element by element.
4. **`marker` used against its own definition.** Extent: exactly 2 hits, exhaustive for the term.
5. **A closed list excluding what two siblings route through it** — `QUESTIONS:` and `NOT COVERED:`
   had nowhere to go in a payload the file declared *"the whole of it"*. The checker supplied the way
   out itself: *"the closure is the file's own: clause 20 requires those six be stated and does not say
   the list is closed."*
6. **Verbatim duplication with `graph-conventions.md`** — 82 shared 8-grams in nine passages, charged
   under `/writing-for-agents`'s single-source-of-truth. **Held by the manager and not sent to the
   worker**, on the ground below.

**`NOT COVERED:` clause 39's negative half**, quoted as the checker wrote it: that no *other* duty in
the file is one effort's standing instruction presented as a workflow rule. Its reason — deciding which
duties have that provenance needs the record, which it was not given and does not read. **Established
by the manager, which holds the record, and discharged**: of the four items in node 75's §Q1 with no
node behind them, one is in the file and is correctly marked as the human's, and the retrospective, the
token-use priority and the propose-at-close duty are all absent. The file also states the general rule.

**Why finding 6 was held.** [Whether the five contracts' shared blocks stay duplicated](50-shared-blocks-stay-duplicated.md)
is open and is exactly this question, minted as the human's on its own finding that *"neither side is
wrong"*. Sending it to the worker would settle it by side effect, on one file out of nine, and
inconsistently — the five contracts would go on duplicating while the manager's contract alone pointed.
Put to the human with the new measurement as evidence for that node.

### Correction round 1

**The human's words:** none. Opened by the manager on five of the six findings.

All five accepted, none disputed. `## Words used exactly` grew 25 → 37; `exchange` replaced by
`interview` throughout; three shapes restored to full; `marker` widened to both referents; the payload's
closure removed with a checker's questions and uncovered parts given a home. **Tier 1 stayed at exactly
three** because clause 28 makes a fourth member the human's decision and never a worker's inference —
the worker routed the question through the gate payload instead and **flagged the one case that
leaves**: a checker that raises issues no outcome, so there is no gate to carry its question.

The payload gained the duty found at [What a finding must carry so it can be
swept](71-what-a-finding-must-carry.md)'s gate the day before — *"where the work is, and the command
that shows its diff"* — which node 75's list was one short of.

### Run 2 — `FAIL: the bar`, the acceptance condition met

**The checker was resumed rather than respawned**, so it re-ran the bar in full, re-checked what the
change reached, and did not establish 38 clauses twice. It treated the worker's statement of what
changed as a statement rather than evidence, noticed the file had been rewrapped and **compared words
rather than lines**, and caught seven changes the statement did not mention — clearing all seven,
including a `code slot` restatement it compared element by element against the glossary and called
*strictly better under ground rule 1*, the glossary's own wording assuming a toolchain.

**One finding, and correction round 1 introduced it.** Renaming `exchange` to `interview` produced an
entry ending *"an implementation node's counterpart holds the checker's runs and the gate's outcome
**instead**"*. The two sections are co-present: `graph-conventions.md` says *"`## Interview` and
`## Review` are the two sections that hold them, and these rules cover both"*, its attempt-block check
is unqualified, and the implementation contract puts a worker's account in either. **The second
instance was the functional one**: `## When an agent dies or is stopped` replayed *"the full replayed
interview"* and then said death and replay reach implementation nodes too, so the one instruction that
reconstructs a dead worker's context was undefined for the case the section extends itself to.

**The shape is the `marker` finding one round later** — a term the file defines, then uses for a
referent its own definition excludes.

**The manager confirmed it from the record, which the checker is blind to.** This node's predecessor,
[What a finding must carry so it can be swept](71-what-a-finding-must-carry.md), is an implementation
node carrying **both** an `## Interview` and a `## Review`.

### Correction round 2

**The human's words:** none. Opened by the manager on the single finding.

Accepted, not disputed. `instead` removed and co-presence stated positively; the replay instruction
rewritten to name no section at all — *"the node plus everything the human has already said on it,
replayed in full"* — which is what the duty always meant.

**Two unprompted changes, both named by the worker rather than found by a checker.** A contrast the
run-2 checker had explicitly declined to charge became wrong once implementation nodes were stated to
carry interviews, and was redrawn on the working tree instead. And the `implementation` entry's dropped
clause — *"and raises only when its premise is broken"* — was **restored**, the run-2 checker having
cleared its absence on the ground that `AFK / HITL` carried it, which stopped being true this round.

**The worker died mid-round** on a connection failure, after making both edits and clearing 24 of 27
candidate sentences. **Resumed rather than respawned**, the manager first verifying on disk that both
edits had survived so the resume did not redo them.

**The manager's verification, independent of the handover:** 582 lines, two paths, `CONTEXT.md` `+7 −0`;
all 23 of clause 5's named terms present; both honesty sections intact; the `implementation` clause
restored; and all three `interview` uses in the body read against the new entry, all consistent.

### Correction round 3

**The human's words, `verbatim`:** *"send it to the worker, I have also made a few changes to the skill"*.

**Two things in one line, and they are unrelated.**

**1. Finding 6 released to the worker.** The manager had held it and recommended leaving it to
[Whether the five contracts' shared blocks stay duplicated](50-shared-blocks-stay-duplicated.md); the
human took the alternative, which the manager had put on the record as *"Send it now… and it pre-decides
a question you own for one file out of nine."* **This is a divergence from the recommendation**, marked
so under the standing rule, and it is the human's call to make. What it settles is this file; node 50
still owns the corpus-wide question and now has evidence it did not have.

**What the manager sent with it, and did not decide.** Clause 3 — *stands alone as a file* — is an
acceptance-condition clause and binds the repair, so the finding is not a licence to swap rules for
pointers. Two facts travelled and no judgement: that a plain-file pointer is not skill invocation, which
is node 50's own finding and is what makes any remedy possible; and that the two documents genuinely
divide along the file's own sentence, *what you do* against *what the files look like when you have done
it*. Which passages are operative for the manager is the worker's to judge and to state. A finding it
cannot discharge without breaking clause 3 is a dispute rather than a trade.

**2. The human edited the worker's live worktree.** `.claude/skills/expedition/SKILL.md` went 582 lines
to 578, 36,292 characters to 35,971, while the node was claimed and between two of its rounds.

**The manager did not ask what changed and did not guess.** It established mechanically that every
structural demand survives — 37 entries under `## Words used exactly`, all 23 of clause 5's named terms,
14 top-level headings in their existing order, 3 items under the collisions heading and 9 under the
unsettled one — so no clause is at risk and the edit is prose-level. The worker was told their text is
authoritative, that it must not revert or restore anything, and that a collision between their edit and
a finding is to be reported rather than resolved on its own authority.

**This is the first time a party other than the claimed worker has written into an implementation node's
tree**, and it makes a shipped sentence false in this instance. It is recorded as
[A human edit lands in a worker's tree while the node is claimed](85-human-edits-a-claimed-tree.md).

## Interview

### Attempt 1 — two clause-mandated statements the human's own edit removed

**The manager's raise.** The worker reported, and the manager verified on unwrapped text, that the human's edit to
the deliverable had removed clause 27's statement entirely and one of clause 36's three demands. The manager put
both, with a recommendation: restore clause 27's, amend clause 36's.

**A1, from the human**, `verbatim`: *"for claude 27, I would expect it to be very rarelly useful, so I didn't want
to waste tokens but if you want you can put it back. For close 36, I disagree that most efforts never end."*

**On clause 27 — a delegation, and the manager's argument withdrawn.** *"if you want you can put it back"* hands the
choice to the manager, recorded as flag `76.7`. **The manager's recommendation rested on a false premise and it is
withdrawn rather than relied on**: it had argued that a manager reading only this file would wrongly try to resume a
stopped agent. It would try, and trying is correct — the file already states that attempting the resume *is* the
detector and that a key which fails to resume means gone, so a stop is marked dead and replaced with a full replay,
which is what clause 27 asks for. **The cut sentence explained rather than ruled**, and the human's judgement that
it was rarely useful was better than the manager's. What survives is only that `## When an agent dies or is stopped`
named a case its body no longer mentioned. Restored as one sentence, not the paragraph.

**On clause 36 — this is not a trim, and it is not confined to this node.** *"I disagree that most efforts never
end"* rejects the **claim**, so the demand is amended away and the file is not to make it in any wording. Clause
36's other two demands stand and are met.

**Where the rejected claim also lives, gathered by the manager rather than assumed.** It is load-bearing in eight
places, and one of them is shipped: `decisions.md`'s entry for [Done-ness and termination](10-done-ness.md), which
states it as that node's own finding; `CONTEXT.md`'s **Closed** entry, in the product tree; [Git and code-landing
policy](11-git-and-code-landing.md), where *"most efforts never terminate, so an effort branch has no merge point"*
is the reason the landing policy has no effort branch; [Whether flags.md survives the settle-at-close
practice](27-does-flags-file-survive.md) and [Workflow self-improvement during use](19-workflow-self-improvement.md)
twice, both routing flags away from the closing report on that ground; and duty 142 of [Gather the manager's
accumulated duties](75-gather-the-managers-duties.md). **A resolved node's finding has been contradicted by the
human**, which is the cascade's own case, and it is recorded as [The human rejects *most efforts never
end*](86-most-efforts-never-end-rejected.md) rather than being propagated here.

**The worker was told to leave `CONTEXT.md`'s entry alone and report it**, clause 42 forbidding an edit to an
existing entry and the manager declining to license a departure for something that reaches past this node.

### Attempt 2 — the human's question at the gate found a gap in the condition

**Q, from the human**, `verbatim`: *"for the cascade, it will be done in another node ?"*

Asked of the observation the checker had handed back — that clause 5 forces five terms into the file which nothing
in its body uses, `cascade` among them.

**A, from the manager.** Partly, and the part that is not covered is a real hole. [Write the cascade pass's worker
contract](44-cascade-worker-contract.md) is open and covers the file *"its two roles are dispatched to"* — the
triage agent and the per-candidate agent. **That is the worker side.** The **manager's** own cascade conduct is in
neither file: §L of [Gather the manager's accumulated duties](75-gather-the-managers-duties.md) holds five such
duties, items 120–126, all settled and cited, and this node's 43 clauses never ask for any of them.

**Measured in the shipped file rather than asserted:** `triage` appears **0** times, `cascade` twice and both
inside `## Words used exactly`, `sweep` four times of which two are the glossary and two are items of the closing
report. So the vocabulary is defined and the conduct is absent — which is exactly why an unused term was the thing
that made it visible.

**This does not reach the gate.** Clause coverage is defined over the 43 clauses, the condition never mentions the
cascade, and a worker that had added the duties would have been writing outside its condition. **Neither node
omitted anything it was asked for**; the gap is between them, which is the same shape as the gate-payload duty
node 75's gather could not produce. Recorded as [The manager's cascade duties are in neither
contract](87-managers-cascade-duties-have-no-contract.md), whose condition is written in part with the missing
question named — whether the duties belong in the manager's contract or in the cascade's own file.

### Gate: `approve`

**The human's word**, `verbatim`: *"approve"*.

**Landed** as `4f9781b`, one path-limited commit of two paths — `.claude/skills/expedition/SKILL.md` created at 578
lines, and `CONTEXT.md` gaining the `Scribe` entry at seven insertions and no deletion. The rebase onto `master`
was a no-op, `master` not having moved since the worktree was cut; the bar's command half had nothing to run; the
merge was `--ff-only`; the worktree was removed and branch `node-76` deleted. The merge and the cleanup ran with
the manager's sandbox disabled, on the standing word recorded at [Run an implementation node's work in a
worktree](68-implementation-in-a-worktree.md).

**The location choice confirmed itself at landing.** Flag `76.1` chose `.claude/skills/expedition/` partly on the
ground that `/expedition` is the name the workflow is invoked by. On the merge, the harness picked the file up and
`expedition` became an invocable skill — *"Run an expedition — one manager thread owning a graph of nodes, one
worker per node, from loose idea to landed code."* The workflow is now reachable by its own name.

**All seven flags settled by this approval**, under the standing rule that approving a node's end settles its
flags. Six were presented live in the gate payload with what was done, why, and the context to answer them;
`76.6` had already been settled at `## Interview` attempt 1.

**Three runs and four correction rounds.** Run 1 failed both halves with six findings; run 2 failed the bar with
one, which correction round 1 had itself introduced; run 3 passed. **The checker was resumed rather than
respawned at each re-check**, so 38 clauses were never established twice, and the worker was resumed rather than
respawned at every round including one it died in.

**What the gate did not settle, recorded so it is not read as settled.** Four nodes were minted from this node's
own run and none is closed: [The manager's cascade duties are in neither
contract](87-managers-cascade-duties-have-no-contract.md), whose condition is written in part; [Carry the worktree lifecycle into the manager's contract](89-carry-worktree-lifecycle-into-managers-contract.md), reported by the worker with its condition written in part and blocked on
flag `68.2`; [A human edit lands in a worker's tree while the node is claimed](85-human-edits-a-claimed-tree.md);
and [The human rejects *most efforts never end*](86-most-efforts-never-end-rejected.md). A fifth duty was filed onto
[What the manager reports to the human, in one place](46-what-the-manager-reports.md).

**Four invalidations stand**, none repaired here: [What keeps the shipped files consistent when a decision changes a
term](29-shipped-file-consistency.md)'s duty that `.claude/skills/expedition/` holding no `SKILL.md` is why nothing
points at `graph-conventions.md`, now false; [Ship the glossary inside the skill
directory](56-ship-the-glossary-into-the-skill-set.md), which must now carry 51 entries rather than the 50 `map.md`
records and lands beside an invocable skill; `CONTEXT.md`'s **Code slot** entry, superseded by `map.md`'s
live-worktree count and owned by [Bring the glossary's code-slot and reject entries up to the worktree
lifecycle](81-glossary-code-slot-and-reject.md); and `CONTEXT.md`'s **Closed** entry, which carries the claim the
human rejected and is [The human rejects *most efforts never end*](86-most-efforts-never-end-rejected.md)'s.
