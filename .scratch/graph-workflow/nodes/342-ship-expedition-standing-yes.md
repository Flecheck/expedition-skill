# Ship `/expedition-standing-yes`

Type: implementation
Status: resolved
Blocked by: none

## Question

Ship the standing yes, as decided at node 131, into the workflow's skill files and glossary.

*Reported by [node 131](131-a-just-do-it-mode-that-skips-grilling.md)'s worker, which gave it no blockers.*

## Acceptance condition

*Authored by node 131's worker and filed by the manager.*

The work leaves the tree meeting all of the following. Every file named is under the repo root.
1. A new skill file exists at `.claude/skills/expedition-standing-yes/SKILL.md`. Its frontmatter `name` is `expedition-standing-yes`, and its description says the human invokes it, with a scope, in an expedition's manager thread. Its body tells the manager all of the following:
   a. The human invokes it with a scope written in any words. A scope may name a part of the effort (for example a refactor, or part of a feature) or a type of demand (for example gates where the human trusts the checker).
   b. The manager records the invocation in the effort's map, as the human's standing steering, in the human's own words. It stays in force until the human changes it, and the next effort starts without it.
   c. For an item inside a scope, the worker's `RECOMMENDED` is taken as the human's "ok for recommended" on a worker's question or raise. On a gate, the checker's `PASS` is taken as the human's approval, and the manager then commits as on an approval.
   d. The manager decides whether an item is inside a scope, at the moment it would otherwise put the item to the human. Where it cannot tell, it puts the item to the human as usual.
   e. A standing yes never covers any of the following: a question or raise with no recommendation the worker believes; a checker's `FAIL`; a checker's raise; a gate whose check will not pass; a gate holding a part of its condition that the checker could not cover, that is still owed, and that the manager cannot establish; a reject; an acceptance condition judged wrong; closing the effort.
   f. A payload holding several questions is covered only when every question in it is inside a scope. Otherwise the whole payload goes to the human, unchanged.
   g. An item covered by a standing yes never enters the pending queue.
   h. The manager records each covered item on the node, under `## Interview` for a question or raise and under `## Review` for a gate, with the mark `standing yes`. The entry quotes the scope text word for word and says which standing yes was applied. It never marks such an entry `verbatim`.
   i. The pick report that closes a node names every item on that node taken under a standing yes, with its scope, and carries every flag the node holds, as for any closing pick report. It states that the human may take any listed item back by naming it in a reply.
   j. A worker whose question or raise is covered is resumed with a line `STANDING YES: <the scope text, verbatim>` in place of `HUMAN ANSWER`.
2. `.claude/skills/expedition/SKILL.md` (the manager contract):
   - points at `expedition-standing-yes` from `## The gate` and from `## What is in front of the human, and when`, stating in each place that an item covered by a standing yes is handled by that skill and not put to the human;
   - no longer says, anywhere, without qualification, that answering on the human's behalf is never the manager's, or that only the human's own approval permits a commit. Each such statement names the standing yes as the case it does not cover.
3. `.claude/skills/expedition/graph-conventions.md`, under `### Recording the human's words`, names three markers instead of two: `verbatim`, `paraphrase`, and `standing yes`. It states that a `standing yes` entry quotes the scope text word for word and is not the human's words about that item.
4. Each of `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md` and `.claude/skills/expedition-precondition/SKILL.md` states, beside its `HUMAN ANSWER` resume shape, that the worker may instead be resumed with `STANDING YES: <the scope text, verbatim>`, and that it reads this as assent to the recommendation of every question in that payload. `.claude/skills/expedition-implementation/SKILL.md` states the same beside its description of how the human answers a raise, reading it as "continue" on the raise's recommendation.
5. The glossary (`CONTEXT.md` at the repo root, or `.claude/skills/expedition/glossary.md` if the glossary has moved there) has an entry **Standing yes**: a yes the human gives in advance, for a scope they state, which the manager takes in place of the human's reply on items inside that scope. Its `_Avoid_` line refuses `auto-approve` and gives the reason: in Claude Code the word means approving tool-permission prompts. The glossary's **Approval** entry no longer says, without qualification, that approval is the human's yes at the gate and the only thing permitting a code commit. It names a standing yes covering that gate as the other thing that permits one.
6. No file in the tree names the skill `/expedition-auto-approve` except as a refused word.

## Answer

`/expedition-standing-yes` ships as a manager skill, with pointers from the manager contract, a third recording mark `standing yes`, a `STANDING YES:` resume line in four worker contracts, and glossary entries.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The human approved. The work landed as commit `eb3b217`. Flags 342.1 to 342.5 are settled at this gate. The worker's replacement clause for node 56 is filed on node 56.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      Ship `/expedition-standing-yes`

ANSWER:
**The standing yes ships.** A new skill, `.claude/skills/expedition-standing-yes/SKILL.md`, tells the manager what to do once the human invokes it with a scope. The manager contract, `graph-conventions.md`, four worker contracts, the triggers file and the glossary now point at the skill or make room for it.

1. **The skill.** Its frontmatter `name` is `expedition-standing-yes`. Its description says the human invokes it, with a scope, in an expedition's manager thread. It has these sections:
   - `## The scope`: the scope is written in any words, either a part of the effort or a type of demand.
   - `## Recording the invocation`: the manager writes the invocation into the effort's map as the human's standing steering, in their own words. This follows the contract's `### Standing steering, and standing instructions of one effort`, in the wording node 337 landed: it binds only once written into the map, stays in force until the human changes it, and belongs to this effort alone. More than one standing yes may be in force, each as its own map entry.
   - `## What a standing yes covers`: exactly three kinds of item. On a worker's question or raise, the worker's `RECOMMENDED` is taken as *"ok for recommended"*. On a gate, the checker's `PASS` is taken as approval and the manager commits. The manager judges scope at the moment it would otherwise put the item to the human, and where it cannot tell, the item goes to the human. A payload with several questions is covered only when every question is in scope; otherwise it goes whole and unchanged.
   - `## What a standing yes never covers`: the eight exclusions from the condition. A checker's raise is read as including a question a checker hands back beside its outcome. Anything outside the three kinds is not covered either, the manager's own raise included.
   - `## Taking a covered item`: the item never enters the pending queue. The manager records it (a question or raise under `## Interview`, a gate under `## Review` as the gate's outcome), marks it `standing yes` and never `verbatim`, quotes the scope text word for word, says which standing yes was applied, and quotes what was taken. A covered question or raise resumes the worker with `STANDING YES:  <the scope text, verbatim>` in place of `HUMAN ANSWER`, with no `DIVERGENCE`. A covered gate is committed as on an approval.
   - `## Flags, and the pick report`: a covered gate settles no flag, so the node's flags settle at the pick report that closes it. That pick report names every covered item with its scope and carries every flag the node holds. It also says the human may take any listed item back by naming it in a reply. An item taken back is a revision of its node.
2. **`.claude/skills/expedition/SKILL.md`**:
   - `## The gate` and `## What is in front of the human, and when` each gain a paragraph: a covered item is handled by `expedition-standing-yes` and is not put to the human. In the second, it also never enters the queue.
   - The `## What is never yours` row on answering on the human's behalf now names the standing yes as its exception.
   - `### Three outcomes, and no fourth` ("approval before any commit") names a covered gate as the one other thing that permits a commit.
   - `### The human's words` names three marks instead of two.
   - `### A flag in a payload` and `## Flags` say a covered gate settles no flag and the node's flags settle at its pick report.
   - `### Picking the next node` says a closing pick report also carries what the skill requires.
   - Nothing in `## What nothing here settles` was touched, so node 340's edit there stays clear.
3. **`graph-conventions.md` `### Recording the human's words`** names three markers: `verbatim`, `paraphrase`, `standing yes`. A new paragraph says a `standing yes` entry quotes the scope text word for word, is not the human's words about that item, is never marked `verbatim`, and under `## Review` is the gate's outcome, an approval. No procedure was added, so no check step is owed. The `## Interview` subsection, where 340 lands, is untouched.
4. **Worker contracts.** Grilling, prototype and precondition each say, beside their `HUMAN ANSWER` resume shape, that the worker may instead get `STANDING YES: <the scope text, verbatim>` and reads it as assent to the recommendation of every question in that payload. Implementation says the same beside how the human answers a raise, read as "continue" on the raise's `RECOMMENDED`.
5. **Glossary (`CONTEXT.md`, still at the root).**
   - A new **Standing yes** entry at the end of `## Talking to the human`, with `_Avoid_: auto-approve (in Claude Code the word means approving tool-permission prompts)`.
   - **Approval** now names a standing yes covering the gate as the one other thing that permits a code commit.
   - Qualified for consistency, beyond the condition: **Manager** (never answers on the human's behalf, except for a standing yes), **Verbatim / paraphrase** and **Interview** (both mention the `standing yes` mark).
6. **`.claude/rules/expedition-triggers.md`**: the second trigger gains "Where a standing yes covers it, take it as `/expedition-standing-yes` says instead."
7. **Left as written, on purpose.** None of these covers a standing yes as a false statement:
   - the **Relay** entry and the four worker contracts' opening "answers nothing itself";
   - the implementation contract's "after the human has approved it", which a `PASS` taken as approval satisfies;
   - item 3 of `## What nothing here settles` ("answer nothing"), which is about a dispute between implementer and checker, a case no standing yes covers.
8. **Clause 6.** The worktree has no mention of `expedition-auto-approve`, and `auto-approve` appears only in the refused word.

INDEX LINE:    `/expedition-standing-yes` ships as a manager skill, with pointers from the manager contract, a third recording mark `standing yes`, a `STANDING YES:` resume line in four worker contracts, and glossary entries.

FLAGS:
- ASSUMPTION: I read "a checker's raise" to include a question a checker hands back beside its outcome. So a gate whose payload carries a checker's question is not covered. Ground: the glossary's **Raise** entry names a checker's question as a raise, and nothing would answer that question if the manager took the `PASS`.
  (index) A gate whose checker handed back a question beside its outcome is not taken under a standing yes; the question counts as a checker's raise.
- ASSUMPTION: A gate taken under a standing yes settles none of the node's flags. They settle at the pick report that closes the node. Ground: node 131's Q4 recommendation, which the human accepted ("Its flags settle on whatever you say next, under the existing rule"). The condition's clause 1i requires that pick report to carry every flag, and a gate no human saw cannot settle flags.
  (index) A gate taken under a standing yes settles no flag; the node's flags settle at its closing pick report instead.
- ASSUMPTION: The skill says an item the human takes back is a revision of its node, handled like any other. Ground: the pick report goes out once the node has closed, so any taken-back item sits on a settled node, which is what the glossary's **Revision** covers. The condition only requires stating that the human may take an item back.
  (index) An item the human takes back from a standing yes is treated as a revision of its already-closed node.
- ASSUMPTION: I qualified four statements outside the condition's named places: the glossary's **Manager**, **Verbatim / paraphrase** and **Interview** entries, and `.claude/rules/expedition-triggers.md`'s second trigger. Left unqualified, each would contradict the landed skill. I left the Relay entry, the worker contracts' "answers nothing itself", the implementation contract's approval wording and item 3 of `## What nothing here settles` as written, on the grounds given in ANSWER point 7.
  (index) The standing yes was carried into three more glossary entries and the triggers file; four statements it does not falsify were left as written.
- ASSUMPTION: The skill states two things the condition does not spell out: more than one standing yes may be in force at once, and anything outside a worker's question, a worker's raise or a gate is not covered, the manager's own raise included. Ground: clause 1h's "which standing yes was applied" implies more than one, and clause 1c lists only those three kinds.
  (index) Several standing yeses may be in force at once, and only a worker's question, a worker's raise or a gate can be covered.

NEW NODES:     none

INVALIDATIONS:
- [Human review of landed code](nodes/20-human-code-review.md) and the glossary's **Approval**: extended. The human's approval is no longer the only thing that permits a commit, because a standing yes covering the gate also does.
- [Relay protocol](nodes/08-relay-protocol.md), the manager's "answers nothing": narrowed. A standing yes lets the manager take the human's advance yes in place of their reply, marked `standing yes`.
- The flag-settling rule of nodes 99, 102 and 310 (settle at the gate where there is one): narrowed. A gate taken under a standing yes settles nothing, and that node's flags settle at its pick report.
- Recording marks (`verbatim` / `paraphrase`, two values): extended to three.

CONDITIONS:    I searched every open and claimed node's `## Acceptance condition` for: two marks / two markers, `verbatim`/`paraphrase`, "only thing that permits", `Approval**`, "on the human's behalf", `HUMAN ANSWER`, "Recording the human's words", "answers nothing", auto-approve, standing yes, `expedition-triggers`, "pick report that closes". I also checked the glossary term counts in node 56. What matched:
- Node 226, clause 5 ("`.claude/rules/expedition-triggers.md` is byte-identical to its state before this work"). Its baseline is its own start, so there is no conflict. I note it because I touched that file.
- Node 56, clause 1 ("**51** term entries … **at least 40** lines beginning `_Avoid_`") was already wrong before this work: master `d3b1a14` holds 55 entries and 44 `_Avoid_` lines. After this work there are 56 and 45. Replacement, fixed by work landed in the tree (the count of `CONTEXT.md` once this node lands) plus node 56's own clause 4 entry: "`.claude/skills/expedition/CONTEXT.md` exists and is the glossary: **57** term entries, each written as a line holding only the term in bold followed by a colon, and **at least 45** lines beginning `_Avoid_`." Node 56's path (`CONTEXT.md` against the map's `glossary.md`) also looks stale, but no replacement for that is fixed by my work.
- Node 80 matched only on "paraphrased", which is unrelated.

MISSING FROM MAP: none

GATE PAYLOAD:
- Checker findings: none yet (no run so far).
- Paths touched:
  - `.claude/skills/expedition-standing-yes/SKILL.md` (new)
  - `.claude/skills/expedition/SKILL.md`
  - `.claude/skills/expedition/graph-conventions.md`
  - `.claude/skills/expedition-grilling/SKILL.md`
  - `.claude/skills/expedition-prototype/SKILL.md`
  - `.claude/skills/expedition-precondition/SKILL.md`
  - `.claude/skills/expedition-implementation/SKILL.md`
  - `CONTEXT.md`
  - `.claude/rules/expedition-triggers.md` (outside the expected paths)
- Bar: the repo has no build, tests, formatter or CI, which matches `map-implementation-rules.md`, so there were no commands to run. The prose half was held against `/writing-for-agents`, the five writing rules, the ground rules and the `_Avoid_` lines. Each file's wrap width is kept, apart from the one table row in `SKILL.md`, since table rows there are already long. Method-skill parts skipped: none.
- Proposed commit message:
  ```
  Ship /expedition-standing-yes: a yes the human gives in advance for a scope

  The manager takes the worker's RECOMMENDED, or the checker's PASS at a gate,
  as the human's reply on items inside the scope, with listed exclusions. The
  manager contract points at the skill, recording gains a third mark
  `standing yes`, four worker contracts accept a STANDING YES resume line, and
  the glossary gains the term and qualifies Approval.

  Node: graph-workflow/342
  ```

RETROSPECTIVE
1. What I had to hunt for.
   - Every statement in `SKILL.md` that says only approval permits a commit. The condition names none. Grepping "approv" found "approval before any commit" in `### Three outcomes, and no fourth`.
   - How flags settle on a covered gate. It is in node 131's Q4 recommendation, not in the condition.
   - The glossary's current counts, needed for node 56's clause.
2. What arrived that this node did not need.
   - Most of `map.md`: the worktree route, the retrospective rule's history and the never-delete scope. Only the standing-rule line (node 93/337) bore on the work.
   - The `decisions.md` grep brought back the pick-report retirement line (node 107), which turned out not to hold, so it was a false lead.
   - I read `graph-conventions.md` whole when I needed only `### Recording the human's words`, `## Review` and the procedures, the last to confirm I was adding none.
3. What would have made this easier.
   - A condition clause listing the known sites of "approval permits a commit" and "never answers on the human's behalf", including the glossary's Manager and Relay entries and the triggers file. Then the scope of clause 2 would not be a judgement.
   - A line in the spawn that `.scratch/` in the worktree sits at master, so clause 6 cannot see node 131's quotes of the human's words. Once the record is committed, those quotes name `/expedition-auto-approve` as the human's own words, not as a refused word. That may matter if a later checker reads clause 6 over the whole tree.
4. What was stale, wrong or contradictory.
   - Node 56's condition counts (51 / 40) are wrong against master (55 / 44), and its path `.claude/skills/expedition/CONTEXT.md` disagrees with the map's `glossary.md`.
   - `decisions.md` says `pick report` is retired (node 107), but the shipped files use it throughout.
   - The quotes your notes flagged as possibly moved still matched after 337, 124, 343 and 333. I found no mismatch.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 340's check; the condition reached it as a verbatim copy in `$TMPDIR/m342.md`, which the message told it to read whole.*

> PASS
>
> This is the check of node 342, "Ship `/expedition-standing-yes`". The work is the uncommitted diff in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/342-standing-yes` (base d3b1a14), plus the untracked `.claude/skills/expedition-standing-yes/SKILL.md`. `git status --short --untracked-files=all` shows these files:
> - the new skill;
> - `.claude/skills/expedition/SKILL.md` and `graph-conventions.md`;
> - the grilling, implementation, precondition and prototype contracts;
> - `CONTEXT.md`;
> - `.claude/rules/expedition-triggers.md`.
>
> The condition sets no file fence, and the diff contains no file under `.scratch/`, no `decisions.md` and no `flags.md`.
>
> **Clause 1: the new skill file.** I read the whole file with `cat -n`. Frontmatter: `name: expedition-standing-yes`. The description says "Give a standing yes in an expedition's manager thread. The human invokes it with a scope…". Each sub-clause is met:
> - (a) `## The scope`: the scope is written in any words, and may name a part of the effort ("a refactor or part of a feature") or a type of demand ("gates where the human trusts the checker").
> - (b) `## Recording the invocation`: the invocation is written into the effort's map as the human's standing steering, in their own words. It stays in force until the human changes it, "so the next effort starts without it".
> - (c) `## What a standing yes covers`: `RECOMMENDED` counts as *"ok for recommended"* on a question or raise. On a gate, the checker's `PASS` counts as approval, "and you then commit as on an approval".
> - (d) "You decide whether an item is inside a scope, at the moment you would otherwise put the item to the human. Where you cannot tell, put the item to the human as usual."
> - (e) `## What a standing yes never covers` lists all eight exclusions the condition names, in its words.
> - (f) "A payload holding several questions is covered only when every question in it is inside a scope. Otherwise send the whole payload to the human, unchanged."
> - (g) "A covered item never enters the pending queue".
> - (h) Step 1 records the item under `## Interview` for a question or raise, or under `## Review` for a gate. It marks the entry `standing yes` "and never `verbatim`", quotes the scope text word for word, and says which standing yes was applied.
> - (i) The pick report "names every item on that node taken under a standing yes, each with its scope", "carries every flag the node holds", and says the human may take any listed item back by naming it in a reply.
> - (j) Step 2 resumes the worker with `STANDING YES:  <the scope text, verbatim>` in place of `HUMAN ANSWER`. The two spaces after the colon align it with the other resume-shape labels.
>
> **Clause 2: the manager contract.** Met.
> - `## The gate` gains "A gate that a standing yes covers is handled by the skill `expedition-standing-yes`, and you do not put it to the human." This sits in the section's own body, before `### The payload`.
> - `## What is in front of the human, and when` gains "An item that a standing yes covers is handled by the skill `expedition-standing-yes`, and you do not put it to the human. Such an item never enters the queue."
> - I ran `grep -noiE 'behalf|answer (nothing|anything|one)|never answer|human.s to answer|only the human|approv|permit|commit'` over the paragraph-unwrapped SKILL.md:
>   - The table row now reads "answering anything on the human's behalf, except by taking a standing yes…".
>   - "approval before any commit" is followed by "The one other thing that permits a commit is a standing yes covering the gate".
>   - One remaining hit is "You cannot settle the dispute, because you are a scribe and answer nothing", in `## What nothing here settles` item 3. It is about deciding a dispute between an implementer and its checker. It does not say answering on the human's behalf is never the manager's, and no standing yes covers a checker's `FAIL` in any case. So I do not count it as an unqualified statement of the kind clause 2 names.
>   - No other statement claims the manager never answers or that only the human's approval permits a commit.
>
> **Clause 3: graph-conventions.md.** Met. Under `### Recording the human's words`, the text now says "Every recorded answer carries one of three markers: `verbatim`, `paraphrase` or `standing yes`." A new paragraph says the entry quotes the scope text word for word, and "The scope text is not the human's words about that item, so such an entry is never marked `verbatim`."
>
> **Clause 4: the worker contracts.** Met.
> - Grilling, prototype and precondition each add, directly after their `HUMAN ANSWER` resume text, "You may instead be resumed with `STANDING YES: <the scope text, verbatim>` in place of `HUMAN ANSWER`… Read it as assent to the recommendation of every question in that payload."
> - Implementation adds the same right after "The human answers in one of two ways", ending "Read it as "continue", on your raise's `RECOMMENDED`."
>
> **Clause 5: the glossary.** Met.
> - `CONTEXT.md` gains `**Standing yes**:` with the demanded definition.
> - Its `_Avoid_` line reads "auto-approve (in Claude Code the word means approving tool-permission prompts)".
> - `**Approval**:` now reads "It permits a code commit. The one other thing that permits one is a standing yes covering that gate."
>
> **Clause 6: no file names the old skill.** Met. `grep -rln 'expedition-auto-approve' .` over the worktree returns nothing. `grep -rn -i 'auto-approve'` finds only the glossary's `_Avoid_` line.
>
> **Consistency across the files.** Every place in the diff says the same thing:
> - A gate taken under a standing yes settles no flag, and its flags settle at the pick report. The skill, the manager contract's `## The gate` and its `## Flags` all agree.
> - graph-conventions says an `## Review` standing-yes entry "is the gate's outcome, an approval", which fits that section's three kinds of entry.
> - The triggers rule and the Manager and Interview glossary entries carry the same exception.
>
> **The bar.**
> - The repo has no build, tests, formatter or CI, so there are no commands to run.
> - `git diff --check` is clean (exit 0), and the new file has no trailing whitespace.
> - Two lines are wider than the files' usual width: the frontmatter description (240) and the changed table row. Both match existing practice: the expedition-stop frontmatter description is 174 wide, and the table's other rows are long too.
>
> **Standards.** As in my earlier checks, I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`.
> - Bore on the work:
>   - `CONTEXT.md` `_Avoid_` lines, checked by hand on the added text. The new term "standing yes" avoids "auto-approve", and nothing refused appears.
>   - The writing rules: bold only where "standing yes" is defined, citations by heading, and every "never" stands beside its positive.
>   - `/writing-for-agents`: the description front-loads its trigger, and nothing else found.
>   - The ground rules. Each worker contract explains `STANDING YES` in its own text, without depending on the skill being invocable. Nothing tells a spawned agent to address the human. The Claude Code mention in the `_Avoid_` line is the condition's own wording.
> - `/coding-principles` and `/naming` did not bear on the work, since it is prose. The skill's name is dictated by the condition.
> - No reviewing skill is named, so I ran none. graph-conventions.md is part of the work, and the change adds a third marker without moving any element I hold the work against.
>
> The condition records no search command.
>
> NOT COVERED:
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The condition does not demand this; the rules file makes it a bookkeeping rule. The worktree diff contains no such write, and what the main tree's record holds is outside what I was given.

### Gate — approve, 2026-09-27

The human, `verbatim`: *"approve"*

## Flags

`342.1` `ASSUMPTION` **· settled** — I read "a checker's raise" to include a question a checker hands back beside its outcome. So a gate whose payload carries a checker's question is not covered. Ground: the glossary's **Raise** entry names a checker's question as a raise, and nothing would answer that question if the manager took the `PASS`. — A gate whose checker handed back a question beside its outcome is not taken under a standing yes; the question counts as a checker's raise.

`342.2` `ASSUMPTION` **· settled** — A gate taken under a standing yes settles none of the node's flags. They settle at the pick report that closes the node. Ground: node 131's Q4 recommendation, which the human accepted ("Its flags settle on whatever you say next, under the existing rule"). The condition's clause 1i requires that pick report to carry every flag, and a gate no human saw cannot settle flags. — A gate taken under a standing yes settles no flag; the node's flags settle at its closing pick report instead.

`342.3` `ASSUMPTION` **· settled** — The skill says an item the human takes back is a revision of its node, handled like any other. Ground: the pick report goes out once the node has closed, so any taken-back item sits on a settled node, which is what the glossary's **Revision** covers. The condition only requires stating that the human may take an item back. — An item the human takes back from a standing yes is treated as a revision of its already-closed node.

`342.4` `ASSUMPTION` **· settled** — I qualified four statements outside the condition's named places: the glossary's **Manager**, **Verbatim / paraphrase** and **Interview** entries, and `.claude/rules/expedition-triggers.md`'s second trigger. Left unqualified, each would contradict the landed skill. I left the Relay entry, the worker contracts' "answers nothing itself", the implementation contract's approval wording and item 3 of `## What nothing here settles` as written, on the grounds given in ANSWER point 7. — The standing yes was carried into three more glossary entries and the triggers file; four statements it does not falsify were left as written.

`342.5` `ASSUMPTION` **· settled** — The skill states two things the condition does not spell out: more than one standing yes may be in force at once, and anything outside a worker's question, a worker's raise or a gate is not covered, the manager's own raise included. Ground: clause 1h's "which standing yes was applied" implies more than one, and clause 1c lists only those three kinds. — Several standing yeses may be in force at once, and only a worker's question, a worker's raise or a gate can be covered.
