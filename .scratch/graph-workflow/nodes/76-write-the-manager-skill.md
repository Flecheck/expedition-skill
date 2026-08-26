# Write the first version of the manager's skill

Type: implementation
Status: open

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
