# `map.md` repeats the false no-override claim about the worktree route

Type: implementation
Status: resolved

Blocked by: ~~277~~ **none — node 277 resolved and landed at `b94104a`.**

## Question

*Surfaced by [node 277](277-the-removal-step-of-the-worktree-route-does-not-work-as-written.md)'s worker in its
`INVALIDATIONS`, and pasted as it wrote it.*

> `map.md`'s worktree paragraph still says **"No step of the route needs a harness tool call or a sandbox override,
> by the manager or by the worker"** — the same sentence removed from `map-manager-only.md` here, and false for the
> same reason. Clause 5 confines this node to two files, so it is reported and not touched. **Every worker on this
> effort reads `map.md` whole, so this is the more widely read of the two copies.**

**Blockers:** node 277, whose landing is what makes the replacement text true and which holds `map-history.md`.

## Acceptance condition

***Written by the manager.*** Minted by the manager from its worker's report; there is no agent whose condition this
displaces. Every demand is fixed by node 277's measurements and by nothing else.

Done when all five hold.

**1.** `.scratch/graph-workflow/map.md`'s worktree paragraph no longer states that no step of the route needs a
harness tool call or a sandbox override. It states instead that **creating the worktree, putting it on its base and
a worker writing it** need neither, and that **the removal is the exception and runs with the sandbox off** — and it
points at `map-manager-only.md`'s `How the worktree is made` by that quoted phrase for the symptom, the trigger and
the recovery, rather than restating them.

**2.** The rest of that paragraph is unchanged: it still states the path, the branch name, and that **a worker
writes its tree by absolute path, calls no tool to reach or leave it, and owes no cleanup** — that half is true and
is what every worker reads the paragraph for.

**3.** The displaced wording states a rule that currently binds, so it is **replaced** rather than struck in place,
and its existing text is appended **verbatim** to `.scratch/graph-workflow/map-history.md` under a heading mirroring
the section it came from. `map-history.md` gains text and loses none. **Append at the file's end**; two other open
nodes expect to append there and the manager holds that sequencing.

**4.** Every new statement cites by markdown link the node that shaped it, and none recounts attempt counts, costs,
or who was wrong.

**5.** No file outside `map.md` and `map-history.md` is modified; nothing is written in `decisions.md` or
`flags.md`; no node's status line is touched. The bar applies.

## The manager's note at filing

*Not a change to anything above.*

**The technique that established the underlying claim is recorded here so a later node can find it**, its author
having said that `/proc/mounts` alone would have produced the wrong answer: **`rmdir` against a non-empty directory
is a pure mount-point test.** It can never delete — `rmdir` refuses a non-empty directory — so the errno is the
whole result: `Device or resource busy` means a mount point, `Directory not empty` means anything else. Node 277's
worker reached for it only after judging a destructive probe too risky, and it is what separated the cases that
`/proc/mounts` left ambiguous.

**What node 277 established, and its stated limit**, so this node's worker does not overclaim: the removal fails on
the unlink of a mount point; the sandbox places two such mounts on **some** worktrees; **which ones is a fit over
seven observations and not a demonstrated mechanism** — every tree removed by the session that made it came away
clean, and both trees found carrying mounts had outlived their creating session. **Why that is what does it is
unestablished.** Three mechanisms were proposed and two died by measurement, one of them the manager's.

**The rule is unconditional even though the trigger is known**, and clause 1 should not be read as inviting a
condition on it: a live tree shows no mount to inspect beforehand, and the failure costs a stale entry in the thing
a code slot's occupancy is counted from.

## What the work states

*The worker's `ANSWER`, pasted as it wrote it.*

> `map.md`'s worktree paragraph no longer claims that no step of the route needs a harness tool call or a sandbox
> override. The one sentence carrying that claim was replaced, in place, by two: that **creating the worktree,
> putting it on its base, and a worker writing it** need neither; and that **the removal is the exception and runs
> with the sandbox off**. The replacement points at `map-manager-only.md`'s *How the worktree is made* for the
> removal's symptom, its trigger and its recovery rather than restating any of them, and cites node 277 as what
> narrowed the claim.
>
> The replacement was written to agree with node 277's landed text at `b94104a` rather than re-derived. **Node 277's
> landed text and the acceptance condition did not disagree** — clause 1 is a faithful paraphrase of the landed
> bullet — so nothing was raised on that ground.
>
> One call a later reader would otherwise re-derive: **the paragraph now points at *How the worktree is made*
> twice**, once in the new text and once in the pre-existing sentence. **That redundancy was left deliberately.**
> Clause 2 holds the rest of the paragraph unchanged, and that sentence is part of the rest; removing or folding it
> would have been a clause-2 breach to buy a stylistic gain. The two pointers do different jobs — mine names *what*
> is over there, the older one says the route is there whole.
>
> A second call, on the reader question the manager put open: **the split does not leave a worker unable to act, and
> the pointer is correctly the manager's half.** A worker never removes a worktree — this same paragraph tells it it
> owes no cleanup, and removal sits in the landing policy, which is the manager's. So no failure a worker can cause
> or meet is behind the pointer. To make that visible rather than leave the worker guessing whether it must go and
> read a file it is told elsewhere it does not read, the new text says in its own words that the removal *"is the
> manager's step and no worker's — the cleanup a worker owes is still none"*. **That is the one sentence added
> beyond what the condition demanded, and it exists so a worker can stop reading at that point.**
>
> Nothing was written firmer than the landed text. **The trigger is not stated in `map.md` at all** — only pointed
> at — so there was no opportunity to overclaim the seven-observation fit as a mechanism.

**The index line the worker wrote**, held here until the node resolves:

> `map.md`'s worktree paragraph drops the false no-override claim, narrows it to creation, base and writing, and
> points at the manager's file for the removal exception.

## Flags

`281.1` `ASSUMPTION` **· settled** — *The worker's own text, pasted.*

> The condition's clause 2 protects *"the rest of that paragraph"*, and the pre-existing sentence *"The route is
> stated in full in `map-manager-only.md` under `How the worktree is made`"* falls inside that protection while now
> duplicating the pointer the new text adds. **I left it untouched and accepted the redundancy** rather than fold the
> two pointers into one, on the reading that clause 2's headline demand governs and its three-item enumeration
> illustrates rather than bounds. The narrower reading — that only the path, the branch name and the worker half are
> protected — would have licensed the tidier edit, and I did not take it.

`281.2` `MANAGER-WRONG` **· settled** — ***Filed by the manager against itself, and it was live in the repository when the worker
found it.*** **The manager created this node's worktree, and node 267's, at a doubled path** —
`.scratch/graph-workflow/.scratch/graph-workflow/worktrees/<NN>-<name>` — by running `git worktree add` with a
**relative** path from a working directory that was not the repository root. **The spawn then named a path that did
not exist**, and the worker lost two tool calls looking where it was told to look.

**The consequence the worker named, and one it could not see.** It measured that the doubled path **escapes
`.gitignore`**, whose rule is anchored at the root, so two whole working trees sat untracked and unignored. What it
could not know is that **the manager's own periodic record-state commit is `git add .scratch/graph-workflow`, and
the doubled path is underneath it** — measured with `git add --dry-run`, which staged both worktrees. **The manager
would have committed two entire working trees into the record.**

**What the manager did, immediately and non-destructively.** It added `.scratch/graph-workflow/.scratch/` to
`.git/info/exclude` — **local-only, not a tracked file, so no shipped or record file changed and no node's work was
pre-empted** — and verified both that `git check-ignore` now matches and that `git add --dry-run` stages none of it.
**Neither live worktree was moved or removed**: node 267's worker is still in one of them. The exclude carries a
comment saying why it is there and that it goes when those worktrees land. **The route repair is [node
284](284-the-worktree-create-command-names-a-relative-path.md).**

`281.3` `MANAGER-WRONG` **· settled** — ***Filed by the manager against itself.*** The condition's clause 3 and the spawn both
said **two** other open nodes expect to append to `map-history.md`, naming 234 and 276. **The worker measured at
least fourteen** — 80, 97, 160, 190, 203, 211, 219, 232, 233, 234, 236, 237, 254, 256, 271, 276. **It did not break
the work**, every one keying on a heading name rather than a position. **This is the fourth count in three days the
manager has passed on without re-deriving**, after `263.4`, `95.6` and `283.1`.

## Invalidations

*The worker's text: `none`.*

## Retrospective

*The worker's own text, pasted.*

> **1. What I had to hunt for.** **The worktree.** The spawn named a path that does not exist; I lost two tool calls
> before `git worktree list` gave me the real one. I looked first where I was told to look. **Nothing in the record
> would have told me** — the doubled path is an artifact of how the command was run, and **this is the one fact a
> spawn is the only possible source for.**
>
> **2. What arrived that this node did not need.** **`map.md` read whole** — of ~90 lines I acted on **one** and
> consulted two others. **But the file is read whole by contract and by its own first line, so this is not waste to
> be trimmed by a worker**; the arrangement that would fix it is node 246's, already open. **Tenth report.**
> **`map-implementation-rules.md`** — the review-route paragraph is the checker's and I acted on none of it,
> **seventh report**; what I did need was the bar's recorded commands and the four writing rules, both short. **The
> whole file is ~12KB and I used perhaps 15% of it.** **The contract's `## When a node you report is an
> implementation node` section turned out to be the highest-value thing I read and I nearly skimmed it**, since I did
> not know at the start that I would report an implementation node.
>
> **3. What would have made this node easier.** **In the spawn: the worktree path, correct. That is the whole of
> it.** Everything else was load-bearing and well-aimed — particularly naming node 277's landed text as the
> authority and telling me to make `map.md` agree rather than re-derive, which saved me reconstructing the
> mount-point argument. **In the record: nothing. The record served this node well.** **A note on the manager's own
> count** — it said two nodes expect to append to `map-history.md`; I measured at least fourteen. **The manager
> asked to be tested on exactly this and the test fails.** It did not break my work, but **node 236 is worth
> holding**: its condition says its text goes *"inside its existing final section or a new `##` section of its
> own"*, and after my append **the existing final section is mine**. A worker claiming node 236 later could bank
> `map-manager-only.md`'s reset text under my node-281 heading and satisfy its condition while corrupting the file's
> meaning. **That is sequencing the manager holds, and it is now a real hazard rather than a theoretical one.**
>
> **4. What I read that was stale, wrong, or contradicted something else.** **Node 152's acceptance condition is
> stale**, found only through the node-263/95 search duty: it demands a paragraph be moved out of `map.md` that
> **node 268 already replaced and banked**, and demands `map.md` gain *"no second markdown link to
> `map-implementation-rules.md`"* where it currently holds **three**. Node 152 is open and unclaimed, so a worker
> claiming it would meet an unsatisfiable condition. **Node 237 has no acceptance condition by design**, and its
> author left a fork for the human turning on whether node 152's condition quotes a particular path phrase — **it
> does not, I read it. That fork is answerable now, and cheaply.** **`.gitignore` really does hold three patterns**,
> confirming node 271 independently.
>
> **Handles I searched**, per the duty: `map.md`, `map-history.md`, `sandbox override`, `no-override`, `worktree
> paragraph`, `How the worktree is made`. Run against the `## Acceptance condition` section of **every open node —
> 135 of them, mechanically filtered by status line** — reading the eleven that matched non-generically, and
> additionally grepping the whole record for the exact sentence removed: **it appears nowhere outside `map.md`,
> `map-history.md`, and nodes 277 and 281 themselves**, so no open condition quotes it.

## The manager's disposal

*Not the worker's text.*

- **The second node it surfaced — *"Two worktrees sit untracked and unignored inside the repository"*, a
  precondition asking whether to remove them now or finish the cycle first** → **not minted, because the manager
  answered it by acting in the same turn it was reported.** The trap is closed by a local-only exclude, neither
  worktree was disturbed, and both go at landing. **Recorded here so the question is visibly answered rather than
  dropped.**
- **The route repair** → **minted as [node 284](284-the-worktree-create-command-names-a-relative-path.md)**,
  carrying the worker's own condition.
- **Node 236's hazard after this append** → **sequencing the manager holds, and it is now recorded on this node
  rather than only in a retrospective.** A worker claiming node 236 must be told its *"existing final section"* is
  node 281's and not the one its author meant.
- **Node 152's condition unsatisfiable, and node 237's fork answerable** → **both are the manager's to act on under
  node 252 and neither is done.** Node 152's replacement is fixed by node 268's landing; node 237's fork the worker
  has just settled by reading. **Named as owed**, and the manager is not amending two conditions in the same breath
  as filing a handover — that haste is what flag `95.5` records.

## Review

### Run 1 — `PASS`

*The checker's own text, pasted. Spawned by the manager, given the condition as extracted text, the bar as
properties, the two changed paths at the doubled worktree path, the record-as-work rule, and this effort's standing
rules. Given nothing from this node or the effort's record. Told clause 2 was where the work is and that a word-stream
diff is what establishes an "unchanged" claim over hand-wrapped prose.*

> **PASS**
>
> **How I read the work.** Both changed paths are record files. I read them as the work under check, held them
> against the condition and the standards as I would product code, and derived no statement of intent from them.
> `git status --porcelain` returns exactly two modified paths and no untracked entries; `git diff --numstat` gives
> `18/0` on `map-history.md` and `1/1` on `map.md`.
>
> **Clause 1 — MET.** The old sentence is absent from the new `map.md`, **checked by exact substring against the
> file, not by eye.** What stands in its place narrows the claim to creation, base and writing, states the removal as
> the exception running with the sandbox off, and says its symptom, trigger and recovery are stated in
> `map-manager-only.md` *"rather than restated here"*. **The pointer resolves** — I confirmed that file's `Remove`
> bullet holds the symptom, the error string, the trigger and the recovery — **and neither symptom nor error string
> nor recovery is restated in `map.md`.**
>
> **Clause 2 — MET, established programmatically.** I extracted the paragraph from base and from the tree, collapsed
> all whitespace in both into a single word stream, and computed the longest common prefix and suffix on characters.
> **The result is a single contiguous substitution: 424 characters identical before it and 542 identical after it.**
> The surviving prefix carries byte-for-byte the path, the branch name, and *"a worker writes that tree by absolute
> path, calls no tool to reach or leave it, and owes no cleanup"*. **Nothing else in the paragraph moved, and since
> `map.md` shows `1/1`, nothing elsewhere in the file moved either.**
>
> **Clause 3 — MET.** Verbatim-ness verified against the base rather than by reading: the banked string is an exact
> substring of the base `map.md` and of the appended tail. **`map-history.md`'s base content is a strict byte prefix
> of the new file** (`+1421` bytes of tail), so it gained text, lost none, and the append is at the file's end. The
> heading mirrors the section and matches the file's existing entries for nodes 244, 260 and 268.
>
> **Clause 4 — MET.** No attempt count, no cost, no attribution of error in either file. The nearest thing sits in
> `map-history.md` and is **provenance of scope rather than an account of who was wrong — and it is in the file that
> exists to hold accounts.**
>
> **Clause 5 — MET.** Only the two named paths; no node file, no status line, `decisions.md` and `flags.md`
> untouched. **The bookkeeping rule that would force a `FAIL` does not fire.**
>
> **No standard moved under the check.** The implementation-rules file states that `map.md`'s standing preferences
> are not among the standards, and `map-history.md` holds superseded text only, **so `### Where the work moved one of
> them` did not fire.**
>
> **The bar — holds.** Discovered from the repo: no manifest of any kind, no `.github/`. No build, no tests, no
> formatter, no CI — a complete bar rather than a deficient one, **and nothing printed because there was nothing to
> run.** `CONTEXT.md`'s `_Avoid_` lines: the only hit is *report* used as a plain verb, which the implementation-rules
> file names explicitly among the ordinary-English false positives.
>
> **One observation that is not a finding.** Mechanical check 10 reports `## Notes` items over the 500-byte target.
> **This item went from 1071 to 1686 bytes and does not say why it exceeds.** The standard states the check *"reports
> and never fails"* and that the target *"is never a rule that forces text out"*, and **the item was already over
> before this work**, so it is a number to look at rather than a defect.
>
> ```
> QUESTION:
> - Complying with clauses 1 and 2 together leaves the map.md worktree paragraph carrying the pointer to
>   map-manager-only.md under "How the worktree is made" TWICE — once in the new sentence clause 1
>   dictates, and once in the pre-existing closing sentence that clause 2 requires be left unchanged.
>   /writing-for-agents' pruning lever counts a meaning stated twice as duplication. The worker could not
>   have merged them: clause 1 dictates the new pointer's wording and clause 2 forbids touching the
>   sentence that already carried one, so this is the condition's own wording and was not the worker's to
>   depart from. Worth a decision on whether a later node collapses the two pointers into one.
> ```

**The manager's disposal of run 1.** *Not the checker's text.*

- **`PASS`, first run, no repair owed**, and the checker established both *"unchanged"* claims by word-stream diff
  rather than by reading — **424 characters identical before the substitution and 542 after** is the kind of finding
  a line diff cannot produce.
- **Its question and the worker's flag `281.1` are the same finding, reached independently and from opposite
  sides.** The worker judged clause 2's protection to bind beyond its three enumerated items and left the redundant
  pointer; the checker, blind to that, found the redundancy and concluded **the worker could not have merged them
  because the condition forbids it.** Two parties agreeing that a condition forced a defect is the strongest
  evidence available that the condition did.
- **The condition is the manager's own**, so the defect is too. **It is not amended** — this node is claimed — and
  it goes to the human at the gate.
- **The 500-byte observation is carried and not acted on.** The item was over before this work and the convention
  says the check never fails; **collapsing the two pointers would fix both that and the duplication in one edit**,
  which is what the checker's question is really proposing.

### Gate — `approve`

**The human's answer**, `verbatim`: *"1 approve"* — the first of four given in one message.

No divergence: the payload carried a `PASS` and no recommendation against landing.

**Landed under the effort's landing policy.** One path-limited commit of the two record files; rebased from
`0e82353` onto `df22fef`'s parent with no conflict; the bar's command half empty; `git merge --ff-only`; worktree
removed and branch deleted **with the sandbox off**, per node 277's finding. **Commit `df22fef`**, trailer
`Node: graph-workflow/281`.

**The duplicated pointer is not repaired by this landing.** Flag `281.1` and the checker's question both name it,
both independently, and **the condition that forced it is the manager's own.** It ships as it stands.

**The worktree this node was worked in was at the doubled path and is now gone**, and with it the last of the two
the manager created wrongly. The local `.git/info/exclude` entry that contained them **was removed in the same
turn**, its own comment having said it goes when those worktrees land. **Node 284 is still the route repair and is
still open.**

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
