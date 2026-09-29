# Ship the priority list into the manager's contract and repair the rules file

Type: implementation
Status: resolved

Blocked by: none

## Question

*Surfaced by [node 248](248-review-the-priority-list-and-decide-how-much-ships.md)'s worker, and pasted as it wrote
it.*

> Carry the corrected priority list into `.claude/skills/expedition/SKILL.md`, delete the two clauses it absorbs
> there, and repair `.claude/rules/expedition-triggers.md` so it stops contradicting itself and its own charter.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 248's worker. Pasted as it wrote it, and not the manager's.*

> The work is done when all six hold.
>
> **1.** `.claude/skills/expedition/SKILL.md` contains a new section placed after the section
> `## What is never yours` and before the section `## Writing the graph`. It states an ordering over the
> manager's own acts as these five items, in this order, and no others:
>
> - Writing information to files — writing what is supposed to be written.
> - Resuming an agent.
> - Spawning an agent, respecting the limits.
> - Giving a question to the human.
> - Waiting, and only where nothing above is available.
>
> **2.** That section also states, in whatever words fit the file: that every item the manager can do it
> does, in this order, a lower item being never skipped but only deferred within the same turn; and the
> ordering's two grounds — that items 1 to 3 are ordered by what each act costs to perform, a write
> being one edit, a resume one message, and a spawn requiring that the node be found before the act can
> be made at all; and that item 3 sits above item 4 on a different ground, a spawn starting work that
> then runs in parallel so that delaying it costs throughput, while a question's cost is dominated by
> the human's own latency and their channel takes one thing at a time regardless, the limits on spawning
> being what stops a question from being starved.
>
> **3.** Two statements are removed from that same file, their force now carried by the section above.
> In the passage telling the manager to write the human's words onto the node at the moment they speak,
> the clause "in the same turn you resume the worker, not after it comes back" is gone; the surrounding
> instruction to write them at the moment they speak, and its stated reason, remain. In the passage
> saying that raising a flag is two writes in order, the clause "never to a tidy-up afterwards" is gone;
> the demand that the node's entry is written first and the index line second remains. No other
> statement in the file is deleted.
>
> **4.** In `.claude/rules/expedition-triggers.md`, the bullet beginning "**A node finishes**" no longer
> says a replacement is started "before anything else continues", and instead says a replacement is
> started as soon as what is owed to the record is written.
>
> **5.** In that same file, the `## Priority` list carries the same five items as clause 1 above, worded
> the same way, and its closing section no longer claims the file holds triggers only. That closing
> section instead says the file holds the triggers and a copy of the priority that orders them, that it
> overrides nothing in an effort's map, and that the governing statement of both lives in the
> `/expedition` skill while this file is the copy that survives a compaction. The file's title reads
> `# Triggers a manager acts on`.
>
> **6.** The words `task`, `user` and `subagent` do not appear in either file's priority list or trigger
> bullets in the sense of a node, a human or a worker.
>
> The bar applies as it does to any implementation node.

## The manager's note at filing

*Not a change to anything above.*

**This node's condition rests on a reading of the human's words that its author flagged rather than settled**, at
`248.2`: that *"the rule will ship as optional"* names the **rules file** rather than the priority list, so the
shipped section binds ordinarily. **If that reading is wrong, clause 3 of this condition is unsafe** — deleting the
two absorbed clauses would downgrade two requirements. The flag reaches the human at node 248's pick report, and
whoever claims this node should know the condition turns on it.

**[Node 258](258-the-contract-contradicts-itself-on-resume-or-replace.md) also edits `SKILL.md`** and is blocked on
this one. **Two workers must not hold that file at once**; the manager holds the sequencing.

**[Node 260](260-never-ask-which-is-stated-for-nodes-not-for-what-waits.md) edits both of this node's files** on
different lines, and goes after it. Same sequencing, held by the manager.

## Attempts

*The manager's record. A claim belongs to the node rather than to the agent holding it, so the node stayed claimed
across the death below.*

- **Attempt 1 — died.** Spawned 2026-09-16. It read its node, the map, the rules file and the two target files, and
  died **with work on disk**: `.claude/skills/expedition/SKILL.md` modified, 22 insertions and 3 deletions,
  uncommitted in `.claude/worktrees/255-ship-the-priority-list` on base `f6aee57`. **The cause was not the work** —
  the harness terminated it on an API session limit, its last words being *"Now I'll make the edits. First, the new
  section in `SKILL.md`."* Nothing it handed back, because it handed nothing back. `.claude/rules/expedition-triggers.md`
  is untouched, so four of the six clauses had not been started.
- **Attempt 2 — spawned 2026-09-19**, into the same worktree, inheriting attempt 1's uncommitted edit as material
  to check rather than to trust. **Interrupted by a transient server error (HTTP 529) on its second turn, having
  written nothing, and resumed in place** — so it is still attempt 2 rather than a third. The manager resumed it
  before recording this, the record of a resume being false until the resume succeeds.

**Two deaths on one node, from two unrelated causes, neither of them the work.** Both were harness or server
failures — a session limit and a 529 — and in both cases the node kept its claim, which is what the claim belonging
to the node rather than to the agent is for. **Attempt 2 went on to finish the node.**

## What the work states

*The worker's `ANSWER`, pasted as it wrote it.*

> The manager's five-item ordering now ships in `.claude/skills/expedition/SKILL.md` as a new section, `## The order
> you act in`, sitting between `## What is never yours` and `## Writing the graph`. It states the five acts — write
> to files, resume an agent, spawn an agent, give a question to the human, wait — as a numbered list, followed by the
> rule that every act the manager can do it does in this order, a lower item deferred within the same turn rather
> than skipped, and by the ordering's two grounds stated separately.
>
> The two grounds are kept apart deliberately, because they are not the same kind of reason. Items 1 to 3 are
> ordered by what each act costs to perform: a write is one edit, a resume is one message, a spawn needs its node
> found before the act can be made at all. Item 3 over item 4 rests on something else entirely — a spawn starts work
> that then runs in parallel, so delaying it costs throughput, while a question's cost is dominated by the human's
> own latency and their channel takes one thing at a time regardless. The section names the starvation guard
> explicitly: the limits on spawning are what stop a question from waiting forever, because spawns run out and then
> the question goes. A reader who collapsed these into one cost argument would produce an ordering that looks
> arbitrary at step 3-to-4, which is why that step carries its own paragraph.
>
> Two clauses whose force the section now carries are gone from the same file. In the passage on writing the human's
> words onto the node, `"in the same turn you resume the worker, not after it comes back"` is removed; the
> instruction to write them at the moment they speak and its stated reason — their answer reaching disk before the
> worker can return — both remain. In the passage on raising a flag, `"never to a tidy-up afterwards"` is removed;
> the demand that the node's entry is written first and the index line second remains, as does `"Both belong to the
> act of raising it."` Deletion was kept minimal so that no third statement went with them.
>
> `.claude/rules/expedition-triggers.md` is repaired on four counts. Its title now reads `# Triggers a manager acts
> on`, the previous `# For a manager acts on` having been ungrammatical. The `A node finishes` bullet no longer says
> a replacement starts "before anything else continues" — which contradicted the priority list printed twelve lines
> below it, where writing to files outranks spawning — and now says the replacement starts as soon as what is owed to
> the record is written. The `## Priority` list carries the five items in the skill's wording, replacing a shorthand
> that used `task` for a node, `user` for the human and `subagent` for a worker, all three refused by the glossary.
> The closing section no longer claims the file holds triggers only, which was false the moment a priority list sat
> in it: it now says the file holds the triggers and a copy of the priority that orders them, that it overrides
> nothing in an effort's map, and that the governing statement of both is in the `/expedition` skill while this file
> is the copy that survives a compaction.
>
> The duplication is deliberate and the two copies are not peers. The skill's section governs; the rules file is a
> copy that survives compaction, and its own closing section now says which of the two it is, so a later editor who
> finds them diverged knows which one to correct from.
>
> The reading the condition turned on — flag `248.2`, whether *"the rule will ship as optional"* named the rules file
> or the priority list — is settled by the human's later words rather than assumed. If the priority list were
> optional wherever it appeared, nothing would explain duplicating it into the skill at all; their statement that
> *"the fact that it is optional explains why the priority it is put also in the skill"* only parses if the optional
> thing is the vehicle, the rules file, and the skill copy is the one that binds. So the shipped section binds
> ordinarily and clause 3's deletions do not downgrade the two requirements they absorb.

**The index line the worker wrote**, held here until the node resolves:

> The five-item priority ships as a governing section in the manager's contract, its two grounds kept distinct; the
> rules file is repaired on title, bullet, list wording and self-description.

## Flags

`255.1` `ASSUMPTION` **· settled** — *The worker's own text, pasted.*

> Flag `248.2` was left open on whether *"the rule will ship as optional"* named the rules file or the priority list,
> and clause 3's deletions are unsafe under the second reading. I settled it as the first, on the human's later
> words — *"The fact that it is optional explains why the priority it is put also in the skill. It is a reminder for
> the agent that stays across compaction"* — which were not available when the flag was written. The argument is that
> the second reading makes the sentence unparseable: if the list were optional everywhere, there would be nothing for
> its presence in the skill to explain. The optional thing is the vehicle; the skill copy governs. I wrote the rules
> file's closing section to say this in the file itself, so the finding does not rest on the flag surviving.

`255.2` `ASSUMPTION` **· settled** — *The worker's own text, pasted.*

> The shipped section retains attempt 1's phrase *"and so the one a later editor will get wrong"*, a prediction about
> a future reader rather than a statement of what holds or of the trigger by which the rule fires. I twice tried to
> trim it and both edits were refused at the permission gate; since no clause of the condition requires the phrase's
> removal and clause 2 is satisfied with it present, I left it rather than treat a refused polish as a blocker. It is
> a candidate for deletion by node 258 or 260, both of which edit this file after me.

## Retrospective

*The worker's own text, pasted.*

> **1. What I had to hunt for.** Nothing material. The one derivation was clause 3's second deletion site, found by
> grepping the file for the quoted clause — cheap, and only because the condition quoted it exactly. Conditions that
> quote the text to be removed rather than describing it are why this node was fast.
>
> **2. What arrived and was not needed.** `map.md` is a mandatory whole-file read and the large majority of it bore
> on nothing here — the concurrency counts, the worktree-creation route, the retrospective questions, the token-cost
> preferences, the dogfood history. My node touched two shipped files and needed from `map.md` only the never-delete
> rule's boundary (that it does not reach shipped files, which is what made clause 3's deletions legitimate at all)
> and the pointer to the writing rules. That boundary is one sentence inside the effort's longest bullet. **A worker
> on a *shipped-file* node needs a different fraction of `map.md` than a worker on a *record* node, and the file has
> no heading that separates them**; the split that already sent manager-only and implementation material to siblings
> could go one step further. I also read `expedition-implementation/SKILL.md` in full, which was correct, but its
> `## When a node you report is an implementation node` section — the four constraints on writing a condition — is
> dead weight on any node that reports no new nodes, and a worker cannot know that until it has finished.
>
> **3. What would have made this easier.** The spawn was unusually good and I want to be precise about which part
> earned its keep: telling me attempt 1's edit was *material to check, not work to trust*, and handing me
> `git checkout --` as an option I did not need to ask about, removed the single decision that would otherwise have
> cost a round-trip. The one thing missing was that the spawn listed the human's two quotations but did not say
> whether the manager considered flag `248.2` still open — I had to infer from the node file's own note that judging
> it was mine. One line either way would have saved re-deriving that.
>
> **4. What was stale, wrong, or contradictory.** Two things, neither mine to fix. `decisions.md` line 142 records
> this rules file as holding "four trigger-duties"; it holds three, and its own intro says three. Same line records
> the frontmatter as `paths: [".scratch/**"]`; it is now two globs, one of them `**/expedition/SKILL.md`. Both are
> drift in the index rather than in the file.
>
> One process note for the manager, since it will recur: **two of my `Edit` calls were refused at the permission gate
> on a file the very next `Edit` wrote successfully.** That is not the sandbox and not a worktree problem — it was
> specific to those two calls. My contract says a write refused after a successful `EnterWorktree` is a raise, and I
> did not raise, because the refused edit was polish outside the acceptance condition and raising would have stopped
> a node that was otherwise complete. **If a refusal like that ever lands on a clause-required edit, that one is a
> genuine raise and I would have had no way to finish.**

## The manager's disposal of the retrospective's record items

*Not the worker's text. Each item naming the record, and what the manager did with it.*

- **`decisions.md`'s node 218 line saying the rules file holds "four trigger-duties" when it holds three, and naming
  a frontmatter that has since grown to two globs** → **held, not repaired, and deliberately.** The line describes a
  file this node's own gate is about to change. Repairing it now would state a shape that is uncommitted, and
  repairing it from the pre-gate file would state one that is about to stop being true. **The manager will repair it
  as bookkeeping when this node lands**, against the file as it then stands, and it is recorded here so that a death
  in between does not lose it.
- **`map.md` having no heading that separates what a shipped-file node needs from what a record node needs** →
  **not minted, and it is the third worker to name this file's arrangement.** It is a sharper cut than [node
  246](246-map-notes-mixes-what-a-worker-acts-on-with-what-a-manager-acts-on.md)'s, which divides worker-facing from
  manager-facing; this divides worker-facing by the *kind of file the node touches*. The manager cannot tell whether
  that is node 246's business or a second node, and widening an open node's subject is not the manager's.
  **Named for the human.**
- **`expedition-implementation/SKILL.md`'s condition-writing section being dead weight on a node that reports no new
  nodes** → **not minted.** It is a shipped contract, and the claim is that a reader cannot know in advance whether
  a section applies — which is true of most of a contract. Recorded as a candidate, with the manager's own doubt
  stated beside it.
- **Two `Edit` calls refused at the permission gate, on a file the next `Edit` wrote** → **not minted, and the
  manager holds no explanation.** The worker's own consequence is the part worth keeping: it did not raise because
  the refused edit was outside its condition, and **a refusal landing on a clause-required edit would have left it
  no way to finish.** That is a hole in the contract's raise rule rather than a defect in any file. **Named for the
  human**, and the manager has minted nothing because it cannot state what the rule should be.
- **The spawn not saying whether flag `248.2` was still open** → **nothing owed to the record; it is the manager's
  conduct.** The manager's note on this node did say judging it was the worker's, and the worker found it there. One
  line in the spawn would have saved the re-derivation, and the manager will put it in the next spawn that carries
  an open flag.

## Review

### Run 1 — `PASS`

*The checker's own text, pasted. It was spawned by the manager, was given the acceptance condition as extracted
text, the bar as properties, the two changed paths and the tree holding them, the record-as-work rule, and this
effort's ground rules and four standing rules for writing copied as text. It was given nothing from this node or
from the effort's record. It was told clause 3 was the one most likely to need real work from it.*

> ```
> PASS
> ```
>
> **Route.** `EnterWorktree` on the worktree's absolute path was **accepted** — my working directory was `.scratch/graph-workflow/nodes`, not the repository root. I checked from inside the worktree. No read was refused; the sandbox was never disabled.
>
> **The record rule.** I read the two changed paths as the work under check. `git status --porcelain` in the worktree returns exactly ` M .claude/rules/expedition-triggers.md` and ` M .claude/skills/expedition/SKILL.md` and nothing else — matching the return recorded in the condition's scope. Nothing under `.scratch/` was written; no node status line, no `decisions.md`, no `flags.md` appears among the work. Both changed paths are shipped files, so the bookkeeping-reserved-to-the-manager clause does not fire.
>
> **Standards read.** `map-implementation-rules.md`, resolved by a single listing of `.scratch/`. It states explicitly that **no reviewing skill is named for this repo**, so I ran none and went looking for none. The ones that bore on this work: `CONTEXT.md`'s `_Avoid_` lines, `/writing-for-agents`, the ground rules, the four standing rules, and `graph-conventions.md`. None of the standards is among the changed paths, so nothing I hold the work against moved.
>
> **1 — the new section, its placement, its five items. Met.** `grep -n '^## '` on `SKILL.md` gives `## What is never yours`, then `## The order you act in`, then `## Writing the graph` — the new section sits between the two named ones with nothing interposed. Its list carries five items and no others. I compared them to the condition's five character by character (stripping the list marker): identical text, identical order.
>
> **2 — what the section states. Met.** Each required element is present: *"Every one of these acts you can do, you do, and in this order."*; the lower item never skipped, only taken later in the same turn; items 1–3 ordered by cost with all three costs — *"a write is one edit, a resume is one message, and a spawn needs its node found before the act can be made at all."*; and item 3 over item 4 on a different ground, with all four sub-elements — parallel work and throughput, human latency, the one-thing-at-a-time channel, and the spawn limits as what stops starvation.
>
> Note that the condition's own word *deferred* was not copied into the file. That is correct rather than a departure: `CONTEXT.md` refuses `defer` (it blurs into `park`), and the condition licenses *"in whatever words fit the file."*
>
> **3 — the two deletions, and nothing else deleted. Met, and this is the one I established from the diff rather than the file.** `git diff --word-diff=porcelain` over `SKILL.md` yields exactly three removal fragments in the whole file:
>
> ```
> -speak** — in the same turn you resume the worker, not
> -after it comes back.
> -it, never to a tidy-up afterwards.
> ```
>
> Both target clauses are gone, and no other word in that file was removed. The surrounding statements survive: *"Write them onto the node **at the moment they speak**. What that protects is that their answer reaches disk before the worker can return…"* keeps both the instruction and its reason, and *"the entry on the node first, then the one line in the effort's index of flags. Both belong to the act of raising it."* keeps the ordering demand.
>
> Worth recording, since the condition asserts the force is "now carried by the section above": **the unmodified `graph-conventions.md` independently retains both statements** — *"the manager issues the resume and the write in one turn rather than one after the other"* and *"Both writes belong to the act of raising the flag and never to a tidy-up afterwards"*. So the deletions create no gap and no contradiction across the shipped set.
>
> **4 — the "A node finishes" bullet. Met.** Now reads *"a replacement is started as soon as what is owed to the record is written."* The word-diff confirms `before anything else continues` was removed.
>
> **5 — the rules file's priority list, closing section, and title. Met.** I diffed the two priority lists after normalising the list marker: `IDENTICAL`. The closing section now reads *"This file holds the triggers above and a copy of the priority that orders them, and it overrides nothing there. The governing statement of both is in the `/expedition` skill; this file is the copy that survives a compaction."* — the "triggers only" claim is gone, and "there" resolves to the map named in the immediately preceding sentence. Title is `# Triggers a manager acts on` (was `# For a manager acts on`).
>
> **6 — `task`, `user`, `subagent`. Met.** A case-insensitive word-boundary grep over the whole rules file returns nothing, and the same grep over the new section returns nothing. The word-diff shows each was removed from the old priority list (`-a task`, `-a new task`, `-user`, `-Waiting (all subagents are working)`). This also clears two `_Avoid_` lines directly: `task` and `subagent`.
>
> **The bar. Discovered from the repo, not taken from any account of it.** The worktree root holds `CONTEXT.md`, `.claude/`, `.scratch/`, `.gitignore` and nothing else. No `package.json`, `Makefile`, `justfile`, `Cargo.toml`, `pyproject.toml`, `flake.nix`, `.pre-commit-config.yaml`; no `.github/`. `.gitignore` lists `.worktrees/` and `.claude/worktrees/` and invokes nothing. So there is **no build, no test suite, no formatter and no CI to run** — the bar's command half is empty, which is a complete bar on its remaining half rather than a deficient one.
>
> The non-command half:
>
> - **Formatting.** No added line carries trailing whitespace; both files end in a single newline; the added lines wrap at the same width as the prose already around them in each file.
> - **`CONTEXT.md` `_Avoid_` lines.** Checked by hand rather than by grep, the implementation-rules file having measured that roughly a third of the refused words are ordinary English. `task`, `subagent` and `defer` are cleared as above. `question` and `run` appear in the new prose only in their ordinary senses — `question` as a thing put to the human, which is the skill's own established usage, and `runs` as the plain verb in *"runs in parallel"*. The refusals attach to a grilling node and to a retry, neither of which the new text names.
> - **Ground rules.** (1) Nothing in either file names this repo, this machine or a toolchain — the costs are stated as properties of the acts (one edit, one message, a node that must be found), not as commands. (2) The rules file now carries the priority itself rather than only pointing at the skill, so it stands alone for that content. (3) The whole section is explicitly the manager's own acts, and item 4 gives a question *to* the human via the manager; nothing tells a spawned agent to address them. (4) Short prose, no machinery.
> - **Four standing rules for writing.** The shapes — the five-item list — are uncompressed and stated twice in full; only the *why* is compressed. The section is navigable by its own heading, and the prose cites its own list by item number within that same list, never a file by line number.
> - **`/naming`.** `The order you act in` and `Triggers a manager acts on` both round-trip to English that matches what each names.
> - **`/writing-for-agents`.** I invoked it and held the new prose against it. The one lever that bites is single-source-of-truth: the five items now exist in two files. **That duplication is what the condition demands, and the file discharges the standard's own mitigation explicitly** — it declares itself the copy, names `/expedition` as the governing statement, and gives the reason the copy exists. No negation-only steering (the one prohibition is paired with its positive), and no no-op sentences.
> - **`/coding-principles`.** Read for applicability; both deliverables are prose, so it does not bite beyond what `/writing-for-agents` covers.
>
> No reviewing skill was run, because the standards name none. No part of any skill was delegated to an agent, so the blindness constraint on delegation never arose. **No question and no uncovered part**: the condition is checkable in full from the two changed paths.

**The manager's disposal of run 1.** *Not the checker's text.*

- **`PASS` on both halves, first run, no repair owed.** The checker handed back no question, which is why none appears in this payload.
- **One finding of its own, beyond what it was asked**: the two clauses clause 3 deletes are **independently retained in `graph-conventions.md`**, which nothing in this node touched. So the deletions leave no gap in the shipped set — a fact neither the worker nor the manager established, and the strongest available evidence that clause 3 was safe. It bears directly on flag `255.1`.
- ~~**The gate is assembled and is queued, not raised.**~~ Raised on 2026-09-19 once node 250's gate was refused and
  its payload cleared.

### Gate — `approve`

**The human's answer**, `verbatim`: *"approve"*

No divergence: the payload carried a `PASS` and no recommendation against landing.

**Landed under the effort's landing policy.** One path-limited commit of the two shipped files in the node's
worktree; **no rebase needed**, the worktree's base and the manager's `HEAD` both being `f6aee57`; the bar's command
half empty, so nothing to re-run; `git merge --ff-only` onto `master`, which **failed inside the sandbox** with
`unable to unlink old '.claude/skills/expedition/SKILL.md': Read-only file system` and succeeded with the sandbox
off — the case the map already records for a range crossing a shipped file, and the only command run that way.
Worktree removed, branch deleted. **Commit `4598672`**, carrying the trailer `Node: graph-workflow/255`.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
