# The removal step of the worktree route does not work as written

Type: implementation
Status: resolved

Blocked by: none

## Question

*Minted by the manager, from a failure it caused and measured at [node
268](268-carry-the-plain-git-worktree-route-into-the-map.md)'s landing.*

**`map-manager-only.md`'s `How the worktree is made` states the removal step as `git worktree remove --force <path>`
followed by `git branch -D worktree-<NN>-<name>`, and says of the whole route that no step needs a sandbox
override.** That is false of the removal step, and it was false when it was written.

**Measured at node 268's own landing, minutes after it landed.** `git worktree remove` returned `error: failed to
delete '.git/worktrees/268-plain-git-route-into-map': Device or resource busy`. The working directory went; the
admin directory under `.git/worktrees/` stayed, leaving the entry `prunable`, the branch undeletable — *"cannot
delete branch … used by worktree at …"* — and `git worktree list` reporting a tree that no longer exists. `git
worktree prune` failed identically. **`git worktree prune` with the sandbox off succeeded at once**, freeing the
branch.

**The cause is a sandbox bind mount and it is not specific to this route.** `/proc/mounts` carries two entries per
live worktree — `.git/worktrees/<name>` read-write and `.git/worktrees/<name>/commondir` read-only — and **a mount
point cannot be unlinked.**

## Acceptance condition

***Written by the manager.*** Minted by the manager from its own measurement; there is no agent whose condition this
displaces. Every demand is fixed by the measurement recorded above and by nothing else.

Done when all five hold.

**1.** `.scratch/graph-workflow/map-manager-only.md`'s `How the worktree is made` no longer states, of the route as
a whole, that no step needs a sandbox override; and its removal bullet states that **the removal runs with the
sandbox off**, that attempting it inside the sandbox fails on `.git/worktrees/<name>` with `Device or resource
busy`, and that the failure leaves a prunable entry and an undeletable branch rather than a clean tree.

**2.** That bullet states the trigger by which a reader knows the rule fires — the sandbox holds two bind mounts per
live worktree, on `.git/worktrees/<name>` and its `commondir`, and a mount point cannot be unlinked — and states
the recovery for an entry already left stale: `git worktree prune` with the sandbox off, after which the branch can
be deleted.

**3.** The creation, writing and base statements in that section are unchanged: the route still creates with plain
`git worktree add` at `.scratch/graph-workflow/worktrees/<NN>-<name>`, still lands on `HEAD` with no reset, and a
worker still writes by absolute path calling no tool and owing no cleanup. **The claim that those steps need no
override is true and stays.**

**4.** Every displaced statement whose job is to state a rule that currently binds is **replaced** rather than
struck in place, and its existing wording appended **verbatim** to `.scratch/graph-workflow/map-history.md` under a
heading mirroring the section it came from. `map-history.md` gains text and loses none. Every new statement cites by
markdown link the node that shaped it, and none recounts attempt counts, costs, or who was wrong.

**5.** No file outside `map-manager-only.md` and `map-history.md` is modified; `.gitignore` is not edited; no file
under `.claude/skills/` is changed; nothing is written in `decisions.md` or `flags.md`. The `## Landing an
implementation node's work` heading and the quoted phrase `How the worktree is made` both still occur in
`map-manager-only.md` — three `.gitignore` pointers cite them. The bar applies.

## The manager's note at filing

*Not a change to anything above.*

**The manager is the party that got this wrong and it got it wrong twice.** It told the human the `EBUSY` failure
had stopped reproducing — once as *"three times"*, once as *"four"* — and node 268's condition, which the manager
did not write, took that as settled. Flag `268.3` holds it.

**What the measurements actually support is narrower than either claim.** [Node
265](265-should-the-worktree-route-drop-enterworktree-for-git.md)'s worker created **and removed** a probe worktree
inside one session, so the mounts never existed for it. [Node 269](269-ignore-the-new-worktree-path.md)'s removal
succeeded sandboxed **for a reason nobody has established**, and that gap is real: a claiming worker should not
write that the failure is universal, because one counter-instance is on the record.

**Why this is an implementation node rather than the manager's bookkeeping**: the text is a rule that currently
binds, in a file the never-delete rule governs, and the repair is a `Change the map` with banking. **The manager has
already changed its own conduct** — removals now run with the sandbox off — and this node is what puts it on disk.

## Interview

### Attempt 1 — the raise put to the human

*Pasted as the worker wrote it. Banked here so that a death leaves the worker's work on disk. **The worker has
written no file.** It stopped under this effort's standing rule that a condition forcing a contradiction is a raise
and not a flag.*

**ABOUT:** Node 277 rewrites `map-manager-only.md`'s `How the worktree is made` so the removal step says it runs
with the sandbox off, states its trigger and its recovery, and banks the displaced rule text verbatim into
`map-history.md`. I have done all the reading and the measurement, and have written nothing yet.

**SO FAR — the plan I had settled.** Two bullets are displaced and both state currently-binding rules, so both are
replaced and banked verbatim under a new `## Superseded from map-manager-only.md at node 277 — …` heading in node
268's shape: (a) *"**No step of the route needs a harness tool call or a sandbox override**, by the manager or by
the worker"*, narrowed to the create, base and write steps that clause 3 says are true and stay; (b) the **Remove**
bullet, rewritten to carry the sandbox-off rule, the symptom, the trigger and the recovery. Nothing else moves; the
three `.gitignore` pointers hold.

**THE MEASUREMENT, WHICH IS WHY I AM STOPPING.** You asked me to establish the difference between node 268's
sandboxed removal failing and node 269's succeeding if it was cheap. **It was cheap, and it came out against the
condition.** Three worktrees are live: 250 (created by `EnterWorktree`, under `.claude/worktrees/`) and 274 and 277
(both plain `git worktree add`, under `.scratch/graph-workflow/worktrees/`). Two read-only probes, inside my
sandbox:

- `grep -i worktree /proc/mounts` returns entries for **250 only** — its admin dir `rw`, its `commondir` `ro`, plus
  `.git/worktrees` itself `rw`. **No entry of any kind for 274 or 277.**
- `rmdir` against each admin directory — safe, every one is non-empty and `rmdir` never removes a non-empty
  directory, so the errno is a pure mount-point test: **250 → `Device or resource busy` (a mount point); 274 →
  `Directory not empty`; 277 → `Directory not empty` (neither is).**

So **"the sandbox holds two bind mounts per live worktree" is false as written.** What carries the mounts here is
the harness-created worktree, not liveness: the two live plain-git worktrees — the route this node documents — have
no mounts on their admin directories at all, and those directories are unlinkable right now. Neither was created or
entered by a harness tool, and 250 has no live session in it, so the discriminator is not *"a session is in it"*
either.

**WHAT THIS DOES AND DOES NOT SETTLE.** It explains node 269's sandboxed success cleanly: a plain-git worktree, no
mount, nothing to be busy. **It leaves node 268's failure unexplained** — 268's worktree was plain-git too, made by
the route it was writing down. **So the counter-instance has not closed; it has swapped ends.** The mechanism in the
node file predicts failure for 269, 274 and 277 as much as for 268, and it is contradicted for three of the four.

**WHAT I DID NOT DO, DELIBERATELY.** The one test that would settle 268 is creating a throwaway plain-git worktree
and removing it sandboxed. I did not run it: if the removal failed it would leave exactly the stale entry this node
is about, in a repo where `git worktree list` is how a code slot's occupancy is counted, and I can neither disable
the sandbox nor prune. **Say the word and I will run it.**

**ALSO REPORTED, NOT TOUCHED.** `map.md`'s own worktree paragraph carries the same false sentence and clause 5
scopes me out of that file. **Node 263's search duty**: I searched the open nodes' `## Acceptance condition`
sections for `map-manager-only.md`, `How the worktree is made`, `commondir`, `bind mount`, `resource busy`,
`worktree remove` and `prune`. **Sequencing only, no breakage** — node 250's condition (parked) governs the same
section but demands six `EnterWorktree` statements node 265 already retired, and nodes 234, 236 and 276 hold the
landing policy above my bullets rather than the bullets.

**ASK:** Clause 2 requires the new bullet to state, as the trigger by which a reader knows the rule fires, that the
sandbox holds two bind mounts per live worktree — which I have just measured to be false of both live plain-git
worktrees. **Do I write that wording as the condition gives it, or do I write the trigger as measured?**

**RECOMMENDED:** Write the trigger as measured. Clauses 1, 3, 4 and 5 are untouched and I meet them exactly as
written; only clause 2's em-dash gloss changes. The bullet would state the sandbox-off rule, the symptom, and the
recovery — that half of clause 2 stands untouched, measured and true. **In place of the false mechanism it would
state what is measured**: a mount point cannot be unlinked; the sandbox does place two such mounts on a worktree's
admin directory and its `commondir`; this was observed on the harness-created worktree and not on the plain-git
ones; and **why one plain-git removal failed and another succeeded is not established** — so the removal runs with
the sandbox off unconditionally, which costs one override and is the only rule the evidence supports.

**ALTERNATIVES:** Write clause 2's wording as given and hand back an `ASSUMPTION` flag — rejected: it ships a
statement I have measured false into a binding rules file, and the effort's own rule makes that a raise rather than
a flag. Write only the symptom and the recovery, naming no mechanism — honest, but it throws away the one
discriminator anyone has. Run the throwaway-worktree probe first — the most informative, and the only option that
can leave the repo dirtier than it found it.

***The manager's note, filed beside the raise and not inside it.*** **The manager holds a measurement that
contradicts the worker's own generalisation and sent it back rather than relaying the raise.** Before node 268's
removal, the manager ran `grep -c "268-plain-git" /proc/mounts` and got **2** — that worktree, created by plain git,
**did** carry the two mounts at that moment. So *"the harness route carries the mounts and the plain-git route does
not"* is as untrue as the condition's own wording, and something that varies over time is the real discriminator.
This is the human's standing instruction — *"you should give the information you have to the worker if it changes
something"* — and it changes something.

### Attempt 1, second raise — and the one command that answered it

*The worker ran two probes, withdrew its own mechanism, narrowed the field to two candidates, and asked the manager
for **one read-only command in the manager's own session** that separates them — saying in as many words that this
was not a question for the human. **The manager ran it before relaying anything.***

**The worker's two probes, both plain `git worktree add --detach` so no branch was created, both removed sandboxed,
both leaving `git worktree list` and `git branch` byte-identical to before:**

- **probe277a** — created and removed inside one tool call. No mount; removal exit 0. *"This case cannot fail by
  construction: the call's namespace was computed before the worktree existed."*
- **probe277b** — created in one call, measured in a second, removed in a third. No mount in the fresh call, removal
  exit 0. **So a tool-call boundary is not the variable.**

**What the seven instances now say**, in the worker's own table: node 265's probe, node 269, probe277a and probe277b
all succeeded sandboxed and were all removed by the session that made them; **node 268 failed, and had crossed a
session boundary**; node 250 is harness-made and many sessions old and carries two mounts; nodes 274 and 277 are
same-session and carry none.

**What died:** the worker's own mechanism (refuted by the manager's `grep -c` of 2 on node 268's plain-git tree, and
withdrawn by its author), the call boundary (refuted by probe277b), and the condition's *"per live worktree"*
(refuted by 274, 277 and probe277b).

**The manager's measurement, run in its own session on 2026-09-20:**

```
277-removal-step:          0
274-widened-supersession:  0
250 (harness):             2
```

**That kills candidate (b).** *"Which session is looking"* is dead: the manager's session sees exactly what the
worker's sees — zero mounts on both live plain-git trees, two on the harness one.

**Candidate (a) stands alone: a worktree that outlives the session that created it.** It fits all seven instances,
its competitor is now refuted by measurement rather than by argument, and **it is a trigger a manager can act on**,
which the others were not. **It remains a fit over seven instances rather than a demonstrated mechanism**, and the
manager is recording that limit rather than letting the fit read as a proof.

## What the work states

*The worker's `ANSWER`, pasted as it wrote it.*

> `map-manager-only.md`'s `How the worktree is made` no longer claims of the route as a whole that no step needs a
> sandbox override, and its removal bullet now carries the rule, the symptom, the trigger and the recovery. Two
> bullets were displaced; both stated rules that currently bind, so both were replaced and banked verbatim.
>
> **What the route now says.** Creating the worktree, putting it on its base, and the worker writing it need no
> harness tool call and no sandbox override — that claim is true and it stays, **narrowed to those three steps**.
> **The removal is the exception, and it runs with the sandbox off.** `git worktree remove --force <path>` then `git
> branch -D worktree-<NN>-<name>`; attempted inside the sandbox it can fail on `.git/worktrees/<name>` with `Device
> or resource busy`, and what it leaves is not a clean tree — the working directory goes, the admin directory stays,
> the entry turns `prunable`, `git worktree list` keeps naming a tree that is gone, and the branch will not delete.
> The recovery for an entry already stale is `git worktree prune` with the sandbox off, after which `git branch -D`
> succeeds.
>
> **The trigger, and what it is not.** What fails is the unlink of a mount point: the sandbox places two bind mounts
> on some worktrees, `.git/worktrees/<name>` read-write and its `commondir` read-only, and a mount point cannot be
> unlinked. **Which worktrees carry them is a fit over seven observations and not a demonstrated mechanism.** Every
> worktree removed by the session that created it carried neither mount and came away clean; the one removal that
> failed, and the only other tree found carrying the mounts, had each outlived the session that created it. So the
> trigger is a worktree outliving its creating session — and **why that is what does it is unestablished**. Nobody
> has shown how the mounts come to be there, and the text says so rather than asserting a third mechanism after two
> were refuted.
>
> **The rule is unconditional even though the trigger is known**, and the text states that as its own clause: the
> trigger is there so a reader knows the rule is not paranoia, not as a condition on when to obey it. A live tree
> shows no mount to inspect beforehand, the manager cannot always tell which case it is in, the override costs one
> call, and the failure costs a stale entry in the very thing a code slot's occupancy is counted from.
>
> **How the mechanism was reached, since the call is not re-derivable from the text.** Three mechanisms were
> proposed and two died by measurement. The condition's own — two bind mounts per *live* worktree — is refuted by
> three live worktrees carrying none. The worker's first replacement — that the harness route carries the mounts and
> the plain-git route does not — is refuted by the manager's `grep -c "268-plain-git" /proc/mounts` returning 2
> before that removal. *"Which session is looking"* is refuted by the manager running the same grep in its own
> session and seeing 0 on both live plain-git trees, the same as the worker saw. **What survives is the session
> boundary, and it was reached by elimination rather than by demonstration, which is why the text says fit and not
> cause.**
>
> **The measurements, none of which left anything behind.** `rmdir` against a non-empty admin directory is a **pure
> mount-point test** — it can never delete, and the errno separates the cases: `Device or resource busy` for a mount
> point, `Directory not empty` for anything else. It returned busy for the harness-made tree at node 250 and
> not-empty for both live plain-git trees, repeatedly and across separate calls. `/proc/mounts` agreed. Two throwaway
> worktrees were made with `git worktree add --detach` — detached so no branch was created, hard rule 3 forbidding
> branching — one created and removed inside one tool call and one left across two calls before removal. Both removed
> cleanly with the sandbox on, **which kills the tool-call boundary as the variable**. `git worktree list` and `git
> branch` are byte-identical to what they were before the node started.
>
> **The limit, and it is real.** A worker cannot start a session and cannot read another session's mount namespace,
> so the surviving candidate was confirmed by elimination from the manager's own session rather than by crossing a
> boundary directly. **Nothing anyone can run from inside one session settles *why* the mounts appear.**

**The index line the worker wrote**, held here until the node resolves:

> The worktree route's removal step now states that it runs with the sandbox off, with its `Device or resource busy`
> symptom, the session-boundary trigger named as an unexplained fit, and the prune recovery.

## Flags

`277.1` `ASSUMPTION` — *The worker's own text, pasted.*

> The acceptance condition's clause 2 fixes the rule's trigger as *"the sandbox holds two bind mounts per live
> worktree"*. Three live worktrees and two throwaway probes measured that claim false, so the bullet states the
> trigger that survived elimination — a worktree outliving the session that created it — and names it as a fit over
> seven observations rather than a mechanism. **This was raised rather than decided, twice**; the manager answered
> both times and directed the wording, and the departure from clause 2 is filed against the condition rather than
> against the work. Every other clause is met as written.

`277.2` `CONDITION-WRONG` — ***Filed by the manager against its own condition, as it told the worker it would.***
**Clause 2 of this condition asserts a mechanism the manager had measured badly and stated as fact.** The worker
refuted it, raised rather than shipping it, and was right both times. **The manager's own note at filing already
held the doubt** — it recorded that node 269's removal succeeded sandboxed *"for a reason nobody has established"*
— **in a section marked *"not a change to anything above"*, so the doubt and the clause sat in one file disagreeing,
with the clause winning by position.** The worker's generalisation is the repair and the manager is carrying it:
**a condition whose author already doubts one of its clauses should carry that doubt in the clause.**

## Invalidations

*The worker's own text, pasted.*

> `map.md`'s worktree paragraph still says **"No step of the route needs a harness tool call or a sandbox override,
> by the manager or by the worker"** — the same sentence removed from `map-manager-only.md` here, and false for the
> same reason. Clause 5 confines this node to two files, so it is reported and not touched. **Every worker on this
> effort reads `map.md` whole, so this is the more widely read of the two copies.**
>
> Node 268's banked block in `map-history.md` states, in the text it moved, that the sandbox *"makes
> `.git/worktrees/<name>` its own mountpoint, so `git worktree remove` and `git worktree prune` both return
> `EBUSY`"* as a property of worktrees generally. That is the same over-general claim, inside a banked passage that
> **must not be altered**. Nothing is owed on it — banked text is a record of what was said — but a reader of that
> block meets the refuted mechanism with nothing marking it.

## Retrospective

*The worker's own text, pasted.*

> **(1) What I had to hunt for.** Nothing in the record, and that is unusual — the spawn named every file and every
> section, and each was where it said. What I hunted for was *physical*: which worktrees carry the mounts. I looked
> first at `/proc/mounts`, the spawn's own suggestion, which gave a clean but incomplete answer. **The technique that
> actually settled it — `rmdir` against a non-empty directory as a pure mount-point test, safe because rmdir cannot
> delete a non-empty directory — I reached for only after deciding the probe was too risky.** It is cheap, read-only
> in effect, and decisive, and **it is worth writing down somewhere a later node can find it, because `/proc/mounts`
> alone would have left me asserting the wrong mechanism.**
>
> **(2) What arrived that this node did not need.** `map.md` read whole, cold: of its ~115 lines, one paragraph bore
> on my work, and it bore on it only as something to report and not touch. The spawn warned me eight workers had
> said this, **which did not reduce what it cost to read**. `map-implementation-rules.md`'s review-route paragraph is
> the checker's and I acted on none of it — the spawn said five workers had reported that too. **The pattern is that
> the *warning* is now cheaper to write than the fix**: both files would be improved by a one-line reader marker at
> the top of the paragraph (`— the checker acts on this; an implementer does not`) rather than by a line in every
> spawn saying it bore on nothing. `map-manager-only.md` I read whole for one section; the fog and out-of-scope items
> are about half the file and bore on nothing.
>
> **(3) What would have made this node easier.** **The condition asserted a mechanism as established fact inside a
> clause I was required to reproduce.** Had clause 2 said *state the trigger you can establish, and name what is
> unestablished*, both raises would have been unnecessary and the outcome identical — the manager's own note already
> held the doubt, in a section explicitly marked *"not a change to anything above"*. The doubt and the clause were in
> the same file, disagreeing, with the clause winning by position. **A condition whose author already doubts one of
> its clauses should carry that doubt in the clause.**
>
> What worked, and it is the reason this settled rather than hedged: **the manager held a refuting measurement and
> sent it *before* relaying my raise, and then ran the one read-only command that separated the last two candidates
> instead of forwarding a hedged question. Two rounds of that cost less than one human turn would have.**
>
> **(4) What was stale, wrong, or self-contradicting.** The node file's stated cause is false and is the thing this
> node repaired. `map.md`'s worktree paragraph carries the same false sentence. **Node 250's acceptance condition,
> which governs the same section, still demands six statements about `EnterWorktree` that node 265 retired**; it is
> parked, so this is sequencing, but a worker claiming it would write a section that contradicts the one I just
> wrote. Node 268's banked block states the refuted mechanism inside text that may not be altered.
>
> **Node 263's search duty.** I searched every open and claimed node's `## Acceptance condition` for the handles
> `map-manager-only.md`, `How the worktree is made`, `commondir`, `bind mount`, `resource busy`, `worktree remove`
> and `prune`. **Sequencing only, no breakage**: node 250 governs the same section but names only retired
> `EnterWorktree` statements; nodes 234, 236 and 276 hold the landing policy *above* my bullets; node 262's "first
> act" test is unaffected. **One integration note rather than a breakage: nodes 276 and 234 both expect to append to
> `map-history.md`, which I have appended to at its end — whichever lands second meets a moved tail.**

## The manager's disposal of the retrospective's record items

*Not the worker's text.*

- **`map.md` carrying the same false no-override sentence** → **minted as [node
  281](281-map-repeats-the-false-no-override-claim-about-the-worktree-route.md)**. It is the more widely read of the
  two copies and every worker on this effort reads it whole.
- **The `rmdir`-against-a-non-empty-directory mount-point test** → **carried into node 281's condition as the
  technique that established the claim**, so it is written somewhere a later node finds it rather than living only
  in this retrospective. The worker is right that `/proc/mounts` alone would have produced the wrong answer.
- **Node 268's banked block carrying the refuted mechanism, unalterable** → **nothing owed and nothing done.**
  Banked text records what was said. The manager notes only that this is the first time on this effort that the
  never-delete rule has preserved a statement now known false, and that no reader of `map-history.md` is warned.
- **A condition whose author doubts a clause should carry that doubt in the clause** → **flag `277.2`**, and it is
  the generalisable half rather than the correction.
- **The review-route paragraph, sixth report, and `map.md`'s `## Notes`, ninth** → the worker's point is new and
  sharper than the previous five: **the warning is now cheaper to write than the fix**, and a one-line reader marker
  at the head of the paragraph would end it. **Named for the human**, and the manager has now named it six times.
- **Nodes 276 and 234 both expecting to append to `map-history.md`** → **sequencing the manager holds.** Recorded
  here so the second to land is not surprised by a moved tail.

## Review

### Run 1 — `PASS`

*The checker's own text, pasted. Spawned by the manager, given the acceptance condition as extracted text **with
clause 2's false gloss included and unmarked**, the bar as properties, the two changed paths, the record-as-work
rule, and this effort's ground rules and four standing writing rules. It was given nothing from this node or from
the effort's record, and was told nothing about the raises.*

> **I read the two changed paths as the work under check**, under the rule that an implementation node's work on
> this effort may be the effort's own record. I derived no statement of intent from them. **No node status line, no
> `decisions.md` and no `flags.md` change appears among the work.** The rules file states no reviewing skill is
> named for this repo, so I ran none. **None of the standards moved under this check.**
>
> **PASS**
>
> **Clause 1 — MET.** An unwrapped whole-file search shows *"No step of the route"* now has **0 hits**, and the
> single surviving override claim is the narrowed one. The new *Remove* bullet states the sandbox-off rule, the
> literal `error: failed to delete '.git/worktrees/<name>': Device or resource busy`, and what the failure leaves —
> working directory gone, admin directory left, entry `prunable`, `git worktree list` still reporting the tree,
> branch will not delete — explicitly *"not a clean tree"*.
>
> **Clause 2 — MET.** Trigger, both bind mounts, the unlinkability and the recovery are all in the one bullet. **The
> bullet's scope qualifier diverges from the condition's own gloss — I did not fail on it because I disproved the
> gloss with a read-only observation.** See the questions.
>
> **Clause 3 — MET, programmatically.** I extracted the Create, Base and worker-writes bullets and tested each as a
> contiguous substring of both `git show b095bb6:…map-manager-only.md` and the current file: **all three present in
> both, byte-identical.** The section's header paragraph likewise.
>
> **Clause 4 — MET, verbatim half established programmatically, sort half by judgement.** Base `map-history.md` is a
> **byte-exact prefix** of the current one (141,318 → 142,827 bytes), so the file gains text and loses none and the
> added block is exactly the tail. I parsed that tail into its two banked passages and tested each as a contiguous
> substring of the base `map-manager-only.md`: **both True, and both False against the current file** (also False
> unwrapped) — banked byte-identical and gone from source. `~~` count is **0 → 0** in `map-manager-only.md` and **66
> → 66** in `map-history.md`, so nothing was struck in place anywhere. **The sort half:** I split the base
> `map-manager-only.md` on the two banked passages and searched the three remaining chunks, in order, in the current
> file — **all found, so the only text removed from the binding file is those two passages and nothing else.** Both
> are rule-stating and both bound at `b095bb6`, so both correctly took replace-and-bank. **Nothing whose job is to
> record what happened was banked, and nothing rule-stating was left struck or left stale.** Citations resolve; node
> 277's own file exists in the main tree and not at base, which is expected. **I checked existence only and read no
> node file.**
>
> **Clause 5 — MET.** Exactly the two paths; `.gitignore` untouched; nothing under `.claude/skills/`; the heading
> present and the quoted phrase occurring three times; **`.gitignore`'s three pointer comments cite those two,
> matching the condition's recital of three.**
>
> **THE BAR — HOLDS.** Discovered from the repo: no manifest of any kind, no `.github/`. No build, no tests, no
> formatter, no CI, **so the command half is empty and nothing was run** — a complete bar on its remaining half.
> `CONTEXT.md`'s `_Avoid_` lines scanned over the added text for every distinctive refusal — **zero hits** — with
> the ordinary-English refusals checked by hand as the rules file directs: *session* here means the harness process
> lifetime, matching the file's own pre-existing usage. Ground rules 1, 3 and 4 hold; **rule 1 does not bite,
> `map-manager-only.md` being this effort's own practice and explicitly not a shipped file.** Standing rules 2 and 4
> hold. **`/writing-for-agents`:** the bullet is long but *"it caches exactly what that standard says to cache, the
> gotcha no config confesses"*, and it leads positively rather than by prohibition.
>
> ```
> QUESTIONS:
>
> - Clause 2's parenthetical gloss — "the sandbox holds two bind mounts per live worktree" — is false on
>   this machine, and the work states a narrower, truer form instead. I checked it read-only:
>   `git worktree list` shows three live worktrees, and the /proc/mounts probe shows the two bind
>   mounts on exactly ONE of them — the tree that outlived the session that made it — and none on the
>   two created by the live session. So the work's "two bind mounts on some worktrees" and its trigger
>   "a worktree outliving the session that made it" hold where the condition's "per live worktree" does
>   not. I marked clause 2 met on its operative demand, because failing it would send the work back to
>   write a statement I have just disproved. Flagging it because the departure is from the condition's
>   own wording and only the human can settle whether the condition should be amended.
>
> - The bullet's measurement tally may belong in `map-history.md` rather than in a binding map file,
>   and complying with clause 2 is what put it there. Instance: the new Remove bullet's sentence
>   "Which worktrees carry them is a fit over seven observations rather than a demonstrated mechanism:
>   every worktree removed by the session that created it carried neither mount and came away clean,
>   while the one removal that failed and the only other tree found carrying them had each outlived the
>   session that created it." Form, as a predicate: a sentence in a binding map file whose content is
>   the measurement from which a rule was derived, rather than the rule, its trigger or its symptom.
>   Extent — a bounding set, since no grep characterises the form: the text this change added to a
>   binding map file, which is the two new bullets and nothing else. Within that set this is the single
>   instance. Why this is a question and not a FAIL: the same standard says "A trigger is part of a rule
>   and stays", and clause 2 positively demanded the trigger be stated in that bullet; the condition's
>   own prohibition list names attempt counts, costs and who was wrong, none of which this is. Drawing a
>   tighter line than the condition drew would be checking the work against my own repair of it.
> ```

**The manager's disposal of run 1.** *Not the checker's text.*

- **The checker independently reproduced the measurement and reached the same trigger**, blind, from a condition
  whose gloss said the opposite. **That is a third party on the session-boundary finding** — the worker, the
  manager, and now a reader told nothing about either. It is the strongest support the claim has, and it still is
  not a demonstrated mechanism.
- **It declined to fail on clause 2 and gave the ground**: *"failing it would send the work back to write a
  statement I have just disproved."* The manager did not tell it the clause was known false; it established that
  itself and then reasoned about what a `FAIL` would cost.
- **Its second question is the sharper one and it declined that too, on a principle worth keeping**: *"Drawing a
  tighter line than the condition drew would be checking the work against my own repair of it."* **The manager
  agrees and is not acting on it**: whether the seven-observation tally belongs in `map-history.md` rather than
  beside the rule is a real question about where a *fit* sits, and it goes to the human at the gate rather than
  being settled by the party whose condition put it there.
- **Both questions are about clause 2, which is flag `277.2`'s subject.** The condition is not amended: this node is
  claimed, and node 252's pen reaches unclaimed nodes only.

### Gate — `approve`

**The human's answer**, `verbatim`: *"approve, I am a bit confused that it's an implementation node, I would have
kinda expected it to be the manager ? Since it is only writing findings ?"*

**The approval is unambiguous and the question is not a condition on it**, so the work landed. **The question is not
answered by the approval and is not treated as closed**: it asks where the line sits between the manager's own
bookkeeping and an implementation node, on a file that is the effort's own record. The manager has been making that
call node by node without a rule to point at, and said so rather than supplying one after the fact.

**Landed under the effort's landing policy.** One path-limited commit of the two record files; rebase; the bar's
command half empty; `git merge --ff-only`; worktree removed and branch deleted **with the sandbox off, per this
node's own finding**. Commit recorded in the gate line below.

**Neither of the checker's two questions is settled by the approval**, and both stay open: whether clause 2's
condition wording should be amended, and whether a seven-observation tally belongs in a binding map file or in
`map-history.md`.
