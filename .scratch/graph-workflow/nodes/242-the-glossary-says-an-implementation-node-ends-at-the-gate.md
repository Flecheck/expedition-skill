# The glossary says an implementation node ends at the gate, and it does not

Type: implementation
Status: resolved

Blocked by: none

## Question

*Surfaced by [node 235](235-graph-conventions-says-a-node-resolves-at-its-gate.md)'s worker, and pasted as it wrote
it.*

> `CONTEXT.md`'s `implementation` entry ends *"Its worker needs no live answer in order to proceed and raises only
> when its premise is broken, and the node ends at the gate."* The node does not end at the gate: the landing policy
> commits, rebases, re-runs the bar and merges after it, and node 216's answer makes a second approval reachable
> after the first. This is the same false claim node 235 removed from `graph-conventions.md`, in the file the
> shipped documents declare authoritative over every term. Clause 6 of node 235's condition put `CONTEXT.md` out of
> that node's reach. Note that the glossary is moving into `.claude/skills/expedition/CONTEXT.md` under node 56, so
> whichever path holds it when this node is claimed is the one to edit.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 235's worker. Pasted as it wrote it, and not the manager's.*

> The work is the glossary file: `CONTEXT.md` at the repository root, or
> `.claude/skills/expedition/CONTEXT.md` where the glossary has moved there before this work
> starts. The worker may edit whichever of those two holds the glossary and no other file; it may
> not mark this node, resolve it, or write a line in `.scratch/graph-workflow/decisions.md` or
> `.scratch/graph-workflow/flags.md`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. The glossary's `implementation` entry no longer asserts that the node ends at the gate. The
>    clause to remove is *"and the node ends at the gate"*, closing the sentence that reads *"Its
>    worker needs no live answer in order to proceed and raises only when its premise is broken,
>    and the node ends at the gate."*
> 2. Whatever stands in its place is true of the workflow: the gate is the one point on the code
>    path where work stops until the human acts, and it is neither where the node ends nor where
>    it resolves — after approval the manager commits the work and lands it, and the node resolves
>    after that.
> 3. The rest of the `implementation` entry is unchanged in what it says, and no other term entry
>    in the file changes what it says.
> 4. No `_Avoid_` line is added, removed or changed, in that entry or anywhere else.
> 5. The file's existing entry order, section order and heading names are unchanged.
> 6. No file outside the one glossary file named above is modified.
> 7. The standing quality bar for this repository holds of the finished tree.

## The manager's note at filing

*Not a change to anything above.*

**This node and [node 56](56-ship-the-glossary-into-the-skill-set.md) both edit the glossary, and node 56 moves
it.** The condition above already anticipates that by naming both paths. The manager holds the sequencing and has
written no blocking edge: whichever runs first, the other edits the file where it then stands.

**The glossary is also edited by [node 112](112-what-the-glossary-calls-starting-an-effort.md)**, which is claimed
and whose worker is holding an unanswered question. Node 112 adds a `## Starting an effort` section and touches no
existing entry, so the two do not collide — but **two workers must not hold that file at once**, and the manager is
the party sequencing them.

## Flags

`242.1` **· settled** `ASSUMPTION` — Clause 2 of the acceptance condition names three things true of the workflow, the first being
that the gate is the one point on the code path where work stops until the human acts. That first element is
verbatim the opening of this same file's **Gate** entry. I read clause 2 as a truth test on the replacement wording
rather than as a demand that all three be transcribed into the `implementation` entry, and so the replacement uses
the defined term `gate` in place of its definition. Ground: `/writing-for-agents`, named in
`map-implementation-rules.md` as the standard that bites on prose deliverables, holds each meaning to a single
source of truth and treats a restated definition as duplication that inflates its rank; and the sibling wording node
235 landed in `graph-conventions.md` makes the same choice. The two elements clause 2 asserts about the
implementation node itself are both stated in full. Not raised as a condition-versus-standard contradiction because
under this reading there is none — a wording exists that satisfies both, and it is the one that landed.

`242.2` **· settled** `MANAGER-WRONG` — ***Filed by the manager against itself.*** This node's `## The manager's note at filing`
says the glossary is also edited by **node 112**, *"which is claimed and whose worker is holding an unanswered
question"*. **That was already false when it reached this worker**: node 112 resolved, and the node that adds the
`## Starting an effort` section is [node 247](247-write-the-glossarys-starting-an-effort-entries.md), which the
spawn named correctly. So the node file and the spawn disagreed, and the worker had to decide which to believe. Its
words, `verbatim`: *"It bore on nothing I did — either way I held the file alone — but a worker that believed the
node file would have believed a second worker was live on this file."* **The manager wrote the stale note and did
not revise it when node 112 resolved**, which is the general failure rather than this instance: a manager note
naming another node's status is a fact with a shelf life, and nothing re-reads one.

## Retrospective

*This effort's own standing instruction, carried in the spawn and shipped nowhere. Pasted as the worker wrote it.*

1. **What I had to hunt for.** One fact, and it was cheap: whether the glossary had moved under node 56. Neither the spawn nor the node file could say, both correctly deferring to what is on disk, so I resolved it with a single `ls` of the two candidate paths plus `CONTEXT-MAP.md` before reading anything. That is the right shape for a worker, but **the manager knows the answer at spawn time for the same one `ls`**, and stating it in the spawn would remove the branch from the worker entirely. The second hunt was node 235's landed wording in `graph-conventions.md`; the spawn had already quoted it accurately and my `grep` only confirmed it, so that lookup was avoidable and I would skip it next time. Nothing else had to be found — `map-implementation-rules.md` held the bar's commands exactly as the repo states them, and confirming them took one `ls`.

2. **What arrived that this node did not need.** The dominant item is `map.md`, read whole as the contract requires. This node acted on **two** of its lines: the sentence recording that `CONTEXT.md` is the glossary and is moving to the skill directory, and the retrospective instruction — which the spawn also carried verbatim, so even that was a second copy. Everything else in that file is the manager's operating rules: the one-question-at-a-time count, the payload-release trigger, the resume-wherever-resumable rule, the worktree-creation route, the spent moved-standard licence, the concurrency targets, the token-priority ordering. None of it could change what a worker does inside a node, and a worker editing one sentence of prose pays for all of it. **The arrangement that would avoid it already exists in this effort and has not been applied here**: `map-manager-only.md` and `map-implementation-rules.md` split two audiences out of this file, and the residue is still largely manager-facing. `map.md` says of itself that it holds *"only what every worker can act on"*; measured against this node, that is not true of most of its `## Notes`. A third sibling holding the standing preferences a worker can act on would leave `map.md` short enough to keep its own promise.
   Smaller items: the `decisions.md` grep for `gate` returned seven lines, of which one (node 235) bore on the work and the spawn had already told me its content — so the grep confirmed rather than informed. The spawn's paragraph on nodes 56 and 247 carried one operative fact (I hold the file alone); the rest of it bore on nothing I did. **Not waste, despite being large:** reading `CONTEXT.md` whole. Clauses 3, 4 and 5 of the condition are assertions about the *rest* of the file, so the whole file was the surface I had to check against, not merely the entry I edited.

3. **What would have made this node easier.** (a) The spawn resolving which path holds the glossary, as above. (b) Clause 2 of the condition being explicit about whether it demands the three elements be transcribed or the replacement merely be true — that ambiguity is this node's only judgement call and its only flag, and one clarifying half-sentence at node 235 would have removed both. The contract's own guidance for writing a condition warns that *"what you write loosely here is paid for there"*, and this is a small, clean instance of exactly that. (c) The node file and the spawn could have agreed about the record — see 4.

4. **What was stale, wrong, or contradictory.** The node file's manager note says the glossary is also edited by **node 112**, *"which is claimed and whose worker is holding an unanswered question"*; my spawn says that node is **247**, and that neither it nor node 56 is claimed or being worked. Both cannot be current. It bore on nothing I did — either way I held the file alone — but a worker that believed the node file would have believed a second worker was live on this file. The likely reading is that the note is stale and node 247 superseded or replaced node 112; the manager holds that.
   Second, `map.md` states the glossary *"is **moving** into `.claude/skills/expedition/CONTEXT.md`, with a `CONTEXT-MAP.md` at the root"*. Neither path exists. The sentence is forward-looking rather than stale, but it reads as an accomplished fact on a first pass and is the reason I checked disk before believing anything; naming node 56 as still open in that sentence would settle it. Its neighbouring counts — 51 entries, 41 `_Avoid_` lines — I confirmed live and both are accurate.
   Nothing else conflicted. `map-implementation-rules.md`'s record of the bar matched the repo exactly, and `graph-conventions.md` and the glossary now agree.

## The manager's disposal of the retrospective's record items

*Not the worker's text. Each item naming the record, and what the manager did with it.*

- **The node file's stale claim that node 112 is live on the glossary** → **acted on, and filed as flag `242.2`
  against the manager.** The general failure it names — a manager note asserting another node's status is a fact
  with a shelf life, and nothing re-reads one — is **not minted**, because the manager cannot tell whether the
  remedy is a rule about what a note may assert or simply the manager re-reading its own notes. **Named for the
  human.**
- **`map.md` reading as though the glossary has already moved** → **not minted.** [Node
  56](56-ship-the-glossary-into-the-skill-set.md) is the move and is open; the worker's suggested repair is to name
  node 56 in that sentence, which is a `Change the map` on a paragraph another open node's work will rewrite
  anyway. Recorded here for whoever claims node 56.
- **`map.md` still holding mostly manager-facing standing preferences** → **already minted**, as [node
  246](246-map-notes-mixes-what-a-worker-acts-on-with-what-a-manager-acts-on.md). This is the **eighth** report of
  the item, and this worker's framing is the sharpest so far: `map.md` says of itself that it holds *"only what
  every worker can act on"*, and measured against a node it is not true of most of its `## Notes`.
- **Clause 2's transcribe-or-be-true ambiguity** → **not minted.** It is an instance of [node
  252](252-may-an-unclaimed-nodes-acceptance-condition-be-amended.md)'s neighbourhood rather than a new subject, and
  the worker resolved it without a raise. The flag records the reading taken.
- **The spawn not resolving which path holds the glossary** → **acted on, not minted.** One `ls` the manager can run
  at spawn time; a change to the manager's conduct that reaches no file.
- **The glossary's counts, 51 and 41, confirmed live** → **nothing owed.** They match `map.md`'s figure from node
  224's count, so that line needs no repair.

## Review

### Run 1 — `PASS`

*The checker's own text, pasted. It was spawned by the manager, was given the acceptance condition as extracted
text, the bar as properties, the changed path, and this effort's ground rules and four standing rules for writing
copied as text, and was given nothing from this node or from the effort's record. It was told that clause 2's two
readings were **its to test rather than to inherit**, and that if the readings gave different outcomes it should say
so and say which it applied.*

PASS

**Working directory:** the worktree, entered via `EnterWorktree` with the absolute path from
`.scratch/graph-workflow/nodes`; never exited, sandbox never disabled, nothing written.

**Standards.** I read `map-implementation-rules.md` and nothing else in that directory. The standards it states: `/coding-principles` and `/naming`; `CONTEXT.md`'s `_Avoid_` lines; the effort's ground rules and its four standing rules for writing; `graph-conventions.md`; and `/writing-for-agents`. It states explicitly that **no reviewing skill is named for this repo**, so I ran none and went looking for none. Of those, the ones that bore on this work were `/writing-for-agents`, the `_Avoid_` lines, `graph-conventions.md`, and both rule blocks; `/coding-principles` and `/naming` do not bite on a three-sentence prose edit that introduces no name. The work under check is a shipped product file, not the effort's record, so the record-as-work rule did not apply — but I confirmed no node status line, `decisions.md` or `flags.md` change is present. No standard moved under the check.

**How each part was established** (from `git diff`, `git diff --word-diff`, and reads of the file):

1. *Clause removed.* `git diff --word-diff` shows `broken,` → `broken.` and the phrase `and the node ends at the gate` gone. Met.
2. *The replacement is true of the workflow.* The replacement reads: *"Its gate is the last point at which the human can act on it, and is neither where the node ends nor where it resolves: after approval the manager commits the work and lands it, and the node resolves after that."* Checked against the shipped product, not the record: `.claude/skills/expedition/SKILL.md`'s `## The gate` says *"approve → you make the commit, and the node resolves"* and *"the gate is the only place an implementation node ever becomes visible to them"*, and the gate's only three outcomes are approve/correct/reject, so nothing puts the human on the node after it. Both the neither-ends-nor-resolves clause and the after-approval clause are transcribed and true; the last-point clause is true (weaker than `SKILL.md`'s *only* place, but nothing stated demands the stronger form). Met — see the reading note below.
3. *Rest of the entry, and every other entry, unchanged.* One hunk, 3 insertions / 1 deletion, entirely inside the `implementation` entry. The preceding two sentences are word-identical.
4. *`_Avoid_` lines untouched.* `diff` of all `_Avoid_`/`_Note_` lines between `HEAD` and the tree: identical. The entry had none before and has none now.
5. *Order unchanged.* `diff` of all headings and bolded entry keys between `HEAD` and the tree: identical.
6. *No other file modified.* `git status --porcelain --untracked-files=all` returns `M CONTEXT.md` and nothing else. The glossary has not moved to `.claude/skills/expedition/`, so the root `CONTEXT.md` is the right one of the two named.
7. *The bar.* Confirmed from the repository rather than assumed: the tree holds only `CONTEXT.md`, `.gitignore`, `.claude/` and `.scratch/`; a `find` for `package.json`, `Cargo.toml`, `pyproject.toml`, `Makefile`, `justfile`, `*.nix`, `*.toml`, `*.yml`/`*.yaml` returns nothing; there is no `.github/`; `.gitignore` lists `.worktrees/` and `.claude/worktrees/` and invokes nothing. So there is no build, no test, no formatter and no CI to run, and nothing was run — a complete bar on its command half, matching what the rules file records. The non-command half holds: no `_Avoid_` word is used against its refusal (the text says *gate*, *approval*, *resolves*, not *review*, *sign-off*, *close* or *done*); ground rules 1–5 are unoffended; `graph-conventions.md` requires shipped files to be edited plainly with superseded wording removed, which is what was done; `/writing-for-agents` favours the edit, since transcribing the `Gate` definition into this entry would duplicate a meaning that already has a single source of truth two sections down, and the one negation present is paired with the positive statement that follows it.

**On clause 2 and the two readings — this is the part you asked me to settle myself.** The two readings give different outcomes, and I say which I applied.

- I applied the **truth-and-consistency** reading. Clause 2's own grammar carries it: it demands that *"whatever stands in its place **is true of the workflow**"*, and the colon then supplies the workflow facts it must be true of. A transcription demand would have read *states that*. Two standards point the same way: `graph-conventions.md` fixes that *"terms are used exactly as the glossary defines them"*, so the token `gate` carries the `Gate` entry's *"one point on the code path where work stops until the human acts"* without restating it; and `/writing-for-agents` treats one meaning written in two places as a defect. On that reading the clause is met.
- Under the **transcription** reading it would not be. The entry transcribes two of the three named facts and replaces the first with a different property — *"the last point at which the human can act on it"* rather than *"the one point on the code path where work stops until the human acts"*. Those are distinct propositions, both true, and only the second is in the entry. A checker applying that reading would return `FAIL: acceptance condition` on clause 2 alone.

**Nothing is uncovered, and I have no question to hand back.** The condition carries no recorded enumerator, so there was none to run.

### Gate — `approve`

**The human's answer**, `verbatim`: *"approve for the gate"*

Landed under the effort's landing policy: one path-limited commit of `CONTEXT.md` in the node's worktree, no rebase
needed (the worktree's base and the manager's `HEAD` were both `19df459`), the bar's command half empty so nothing
to re-run, `git merge --ff-only` onto `master`, worktree removed and branch deleted. Commit `f6aee57`, carrying the
trailer `Node: graph-workflow/242`.

**The two flags this node held are settled by this approval.**

**Fourth landing, same pattern.** The path-limited commit succeeded sandboxed; `git merge --ff-only` failed
sandboxed with `unable to unlink old 'CONTEXT.md': Read-only file system` and **failed atomically**, `HEAD` not
moving, then succeeded with the sandbox off. Four landings, four different target paths, one constant cause. For
[node 251](251-the-managers-own-session-cannot-write-parts-of-the-record.md).

## Annotation: the manager gave the human a question while this node's gate was live

*Written by the manager. Not a change to anything above, and recorded here because this is the node it was done to.*

**This gate was raised, and then a worker's raise from [node
248](248-review-the-priority-list-and-decide-how-much-ships.md) was put in front of the human while it was still
unanswered.** The manager sent it. The human then answered node 248 rather than this gate, and so this node's
approval arrived one exchange later than it would have.

**The rule broken has no ambiguity behind it**: exactly one question is in front of the human at a time and nothing
displaces a live one, a worker's raise queues, and within tier 1 the order is arrival. The manager had run that
queue correctly twice immediately before — it held this gate while node 248's first payload was live, and said so —
and then stopped running it.

**What is genuinely unsettled is the reverse case and was not this one.** The shipped contract names, as an open
collision, that a gate holds a code slot while it waits and a relayed question does not, so whether a newly ready
**gate** may go ahead of an **older question** is unstated. Here a newer question went ahead of an older gate, which
nothing leaves open.

Filed as flag `242.3`.

`242.3` `MANAGER-WRONG` — ***Filed by the manager against itself, after the human asked whether it had done this.***
The manager put node 248's worker's raise in front of the human while this node's gate was live and unanswered,
giving the human two open things at once. The gate had arrived first, and a gate holds a code slot while it waits.
The human noticed and asked; the manager had not reported it. **This is the second time this session the manager
stated its own conduct rather than checking it** — the first being flag `250.1`, where it told the human twice it
had changed the spawn's working directory when it had not. Raised after this node's approval, so it is **not**
settled by that approval and stands open.
