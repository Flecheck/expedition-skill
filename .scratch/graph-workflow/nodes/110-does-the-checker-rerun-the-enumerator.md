# Whether the checker re-runs a condition's own enumerator

Type: grilling
Status: resolved

## Question

*Surfaced by [Whether a condition's scope stops being a list of files](94-condition-scope-as-a-predicate.md)'s
worker, and pasted as it wrote it.*

> A condition now records the search that produced its scope, and four parties could run it: the author while writing
> (this node's rule), the manager at node 82's guard 1, the worker to find its instances, and the checker to verify
> the scope was met. Nothing binds the fourth. Node 82 left open that *"nothing independent checks the amendment"* —
> its guard 2 being the manager auditing its own act, which is flag `58.3`'s residual and the shipped manager
> contract's own unsettled duty 8 — and a recorded enumerator is the first thing on this graph that an independent
> party could re-run to close it. So: must a checker re-run a condition's recorded enumerator as part of establishing
> the scope, and if it must, what is the outcome when the command now returns more than the condition's list — a
> `FAIL` on a scope the worker met as written, a finding outside the outcome, or a raise?

**Blockers, in the worker's words:** *"none. Node 94 is resolved and node 71 has shipped the checker's own extent
ladder."*
## Answer

*Written by this node's worker and pasted as it wrote it.*

**Yes — the checker runs a condition's recorded enumerator, and what it returns never produces a `FAIL` on its own.**
The human, on the recommendation as offered: *"ok for recommended"* — taken whole, so everything under *The rule*,
*What the comparison is against*, and *Why not a `FAIL`* is theirs by that assent.

Their reply carried a first clause about a manager relay line naming node 108. It addresses a different thing and is
recorded there; this worker read the assent as unreserved, and agrees with the manager's reading rather than working
around it.

### The rule

Three parts, and one thing left exactly as it stands.

1. **The checker runs each recorded enumerator as written**, and its outcome states what the command returned and
   whether that matches the return the condition records. It costs one command. It is the only independent test the
   arithmetic gets: the author records it, the manager re-derives its own act at [node
   82](82-amending-a-condition-whose-scope-was-too-narrow.md)'s guard 1, and the worker uses it to find instances —
   three runs by two parties, both of which have a stake in the answer.
2. **A mismatch, or a return reaching a place the list does not name, is handed back alongside the outcome and is
   never on its own a `FAIL`.**
3. **An enumerator whose domain reaches the effort's record is reported as a defect in the condition.** The checker
   runs the command as written, notices that it walked into material it is blind to by design, and says so rather
   than quietly trimming the domain.

**Unchanged: editing outside the condition's list stays a `FAIL`** on the exclusion clause, established from the diff
and needing none of this.

### What the comparison is against

**The return the condition records, and not the condition's list of places.** The two may legitimately differ, and
[node 103](103-carry-the-pick-report-settling-moment.md) is the live instance: its condition names six places across
five files, its enumerator's recorded return is four files, and the gap is `map.md`, which the condition excludes
from the domain by name because it is the effort's record rather than the tree. A checker comparing the return
against the *place list* would report a discrepancy that the condition already explains in its own text.

So the checkable claim is narrow and exact: *this command, run now, returns X; the text beside it says it returns Y.*
The checker is not asked whether the scope **grew**, and could not establish it if it were — it holds no
before-state, the work has moved the listed files under it, and on this effort several nodes queue on the same files
with each rebasing onto the last. Growth is not diagnostic. Falsity is.

### Why not a `FAIL`

Three grounds, and the third is the condition's own.

1. **The checker's hard rule 2** — *"you check against what you were given and never against your own preference. A
   property nobody stated is not a finding."* The scope *demand* is that the listed files are edited and no others
   are. The enumerator is a statement of fact about how that list was got, prefaced in every instance on this graph
   by *"so the scope is measured rather than asserted"*. It was true or false before any worker arrived.
2. **A `FAIL` punishes the wrong party.** `FAIL: acceptance condition` *"sends the work back to the feature"*, in the
   contract's own words. The work met the scope as written; the error is the condition author's, and hard rule 3
   forbids the worker to repair a condition — so the correction round would be unactionable by the only agent it
   reaches.
3. **The condition's own residual clause already routes this to reporting.** Every condition written under [node
   94](94-condition-scope-as-a-predicate.md) carries *"an instance the search reaches outside the condition's list is
   reported and not edited — reporting it is the whole of what this condition asks for it."* A surplus is, by the
   condition's own words, a thing to report. This route has two spontaneous precedents: node 71's checker searched
   outside its scope, found two near-misses and correctly owed nothing; node 74's enumeration arrived **outside a
   `FAIL`, alongside a `PASS`**, which node 71's own audit names as the case that made the whole extent idea worth
   shipping.

### Whose enumerator this reaches

**Every one, and the checker is not told which.** Four authorship cases now exist on this graph — a minting worker's
(node 109), the manager's for a node it minted itself (nodes 71 and 114), and the manager's supplied after the fact
at guard 1 (node 103). The checker cannot distinguish them, being blind to the record, and that indifference is a
feature rather than a gap: the grounds above get **stronger** the further the enumerator's author sits from the
worker being checked, and the weakest case for a `FAIL` is the one where a manager wrote the command months after the
condition's author stopped being involved.

### What it rests on, measured rather than argued

Four recorded enumerators exist on this graph. **Two were false as recorded, and nothing on the graph had re-run any
of them.**

| condition | author | recorded | actual |
| --- | --- | --- | --- |
| node 71 | manager, own minted node | `grep -rln "one entry per failure" --include="*.md" .` returns one path | **two** — the shipped contract, and node 71's own node file |
| node 109 | minting worker | seven paths, and five for the sub-enumerator | **exact**, both halves |
| node 114 | manager, own minted node | two lines in `CONTEXT.md`; no file under `.claude/skills` | **one** line, and **one** file |
| node 103 | manager, at guard 1 | four files, zero false positives | **exact** |

**Node 71 is the sharpest of the four, because it is the exemplar.** Node 94 called its condition *"the only one on
the record that never overflowed"* and modelled the whole rule on it. Its enumerator globs `.`, so its domain
includes the effort's record — which flag `94.2` bans — and the condition, by quoting the phrase it searches for,
**made itself a hit on its own enumerator.** Git confirms the node file was committed the day before the work
landed, so this was already true when that node's checker ran; its `## Review` records that it *"established the
scope and its extent grep"*. Run verbatim at that moment, the command returned two paths. Either it was not run, or
the difference was absorbed in silence. **This is what part 3 of the rule exists for**, and it is why the checker
runs the command as written instead of narrowing it to the tree: a record-reaching enumerator is invisible until
somebody runs it and reports where it went.

**Node 114 is the one that shows the cost is not historical.** It was open, manager-written, and awaiting a claim,
and both halves of its recorded return were false — the command written is case-sensitive and the return recorded was
not, and the file it declared silent is the exact line [node 111](111-write-the-starting-an-effort-section.md)'s
clause 10 is open to edit. Two open conditions disagreed about a fact one of them had recorded a search to settle.
The manager re-ran both commands, confirmed the finding, and corrected that condition in place before any claim.

**And the contrast worth keeping:** the two that hold are the two most recently run, and the only worker-written one
is exact in both halves. The failure is not carelessness about searching. It is that **a recorded return is prose the
moment it is written down**, and nothing read it back.

### What this does not close

**Not [node 82](82-amending-a-condition-whose-scope-was-too-narrow.md)'s hole**, and this node's question expects it
to. That question says a recorded enumerator *"is the first thing on this graph that an independent party could
re-run to close"* the residual at flag `58.3` and the manager contract's unsettled duty 8. It is half right, and the
half it is right about is the smaller one. The checker can test whether the **arithmetic** is right. It cannot test
whether a widening added *places and no demands*, because that needs the condition's prior wording and what the
record already fixed — both in the record, which it is blind to by design. The mechanical half is now checked by a
party with no stake in it; the judgement half stays exactly where node 82 left it, and flag `58.3` and unsettled duty
8 stand.

**Nowhere for this to land yet.** No shipped file states it: `scope` appears in the checker contract **zero** times,
and `enumerator` and `extent` each appear in exactly **one** shipped file, that contract, and only about the
checker's *own* findings. [Node 109](109-carry-the-extent-rule-into-the-shipped-files.md) ships node 94's rule into
seven files and **the checker contract is not among them** — its own enumerator over `self-contained` returns seven
paths, and that file is not one. So this answer needs an implementation node of its own, and it is [Carry the
checker's enumerator duty into the checker's contract](116-carry-the-enumerator-duty-into-the-checker-contract.md).

## Flags

*Each entry is the worker's own prose, pasted. The manager added the id, the marker and the state.*

`110.1` `ASSUMPTION` — **The rule reaches an enumerator whoever wrote it, including one the manager supplied at guard
1.** The manager offered this as mine to say or to leave alone, and I said it rather than leaving it, because leaving
it would put the question to the first checker that meets node 103's condition. I settled it as reaching every
authorship case on three grounds: the checker is blind to the record and so cannot tell who wrote the command; the
condition it is handed carries no authorship marking that survives into the text; and my answer's own grounds for
report-not-`FAIL` strengthen rather than weaken as the author moves further from the worker, so the widest reading is
also the safest. The risk I accepted: a manager-supplied enumerator at guard 1 is the one case where the *manager* is
both the author of the command and the recipient of the checker's report about it, which is the same self-audit shape
node 82's guard 2 already leaves open — my rule puts an independent party between the command and the record, and
nothing puts one between the report and the manager's response to it.

`110.2` `ASSUMPTION` — **The comparison target is the condition's recorded return, not its list of places.** This was
forced by node 103 after the human had already answered, so they never saw it. That condition names six places across
five files while its enumerator's recorded return is four files, the gap being `map.md`, excluded from the domain by
name as the effort's record. Read the other way — return against place list — a checker would report a discrepancy
the condition explains in its own text, and the rule's first output on its first live instance would be a false
positive. I settled it on the narrower reading because it is the only comparison the checker can make exactly: it
holds no before-state, so *falsity of a recorded claim* is establishable and *growth of a scope* is not. The risk I
accepted: a condition can now record a return that is honest, current, and narrower than its own place list, and
nothing checks that the excluded places were excluded for a stated reason rather than forgotten.

`110.3` `ASSUMPTION` — **`/grilling` and `/domain-modeling` were not invoked.** My contract's `## How you grill` says
to invoke them where present, and both are present as `mattpocock-skills:grilling` and
`mattpocock-skills:domain-modeling`. I ran the discipline the contract states in full — one question, a
recommendation I believed, the alternatives named, every fact the files could give me read rather than asked — and
spent the budget on re-running four enumerators instead, which is what decided the node. This is a departure from an
instruction rather than a conflict between a method skill and a hard rule, so it is reported here and not under the
conflict clause. **This is the third consecutive grilling node to record it**, after flags `102.3` and `94.5`, and
[Whether the contracts' instruction to invoke a method skill is doing any
work](113-whether-the-method-skill-instruction-does-any-work.md) now exists to settle it — so I record the instance
for that node's evidence rather than to ask for the judgement again.

## Interview

### Attempt 1, round 1

**Asked**, in the worker's words:

> Should the checker run a condition's recorded enumerator and report what it returned against what the condition
> claims — with a mismatch or a surplus handed back **alongside** its outcome rather than as a `FAIL`?

**Answered**, `verbatim`:

> "Nothing is queued behind it; node 108's worker holds a second question of its own" doesn't this means that there
> is a question queued behind ? ok for recommended

**The option taken**, written by this node's worker and quoted here as it offered it:

> Yes to running it, and never a `FAIL` on its own. One package, three parts:
>
> 1. **The checker runs each recorded enumerator as written**, and its outcome states what the command returned and
>    whether that matches the condition's recorded return.
> 2. **A mismatch or a surplus is a finding handed back alongside `PASS`/`FAIL`, never a `FAIL`.**
> 3. **An enumerator whose domain reaches the record is reported as a defect in the condition.**
>
> Editing outside the list stays a `FAIL`, unchanged.

*Not a divergence: the reply takes the worker's own recommendation.*

**The manager's note on the first clause of the reply.** *Not a change to anything above.* The human's message opens
by querying a sentence of the **manager's**, not of this node's — a relay line reading *"Nothing is queued behind it;
node 108's worker holds a second question of its own"*. It bears on [When the human's channel is free, and whether
the manager must fill every gap in it](108-when-the-humans-channel-is-free.md) rather than on this node, and is
recorded there. It does not qualify the assent: the two clauses address different things, and *"ok for recommended"*
names this node's recommendation without reservation.

## Retrospective

*The worker's own text, pasted, handed back as the sixth handover part this effort asks for. Filed as an annotation,
which is why it sits after the node's mandatory sections.*

**What I had to hunt for.** One thing, and it decided the node: **what the recorded enumerators actually return.**
Nothing on the record had run any of them. I looked first at node 94's answer, expecting its census to be
re-runnable, because its measurement 2 states a count — 43 conditions, one recording a search — and I assumed the
returns came with it. They do not: it records that node 71's condition *has* an enumerator and never that the
enumerator is right. Four commands and a `git merge-base` produced the whole evidentiary base of this answer in about
five minutes.

Second hunt, smaller and load-bearing: **whether anything shipped already binds the checker here.** I went at it by
reading the checker contract whole, which was right, but the fact that settled it came from `grep -c "scope"`
returning 0 — a thing I could not have concluded from reading, because absence does not announce itself. The same
greps gave me the new node's scope for free.

Third: **whether the checker contract is inside node 109's seven files.** This is the fact that makes my answer need
a node rather than a widening, and I derived it by re-running node 109's own enumerator and reading the hit list.
Nothing said it.

**What I read and did not use.** `map.md` in full, and it remains the largest single read of the node: the
destination, the landing and worktree policy, the code-slot count, the dogfood target, the bar's commands, the review
route, the label vocabulary, out-of-scope and eight fog items. Four lines bore on the work — the retrospective
instruction, the one-question rule, and standing writing rules 2 and 4. `decisions.md` in full, ~65 lines, of which
about seven mattered and I opened six of those nodes anyway. Node 82 in full: I needed guard 1, guard 2 and the
`### What this does not settle` bullet on flag `58.3`; the four-instance table, the `INVALIDATIONS` and the
not-a-revision argument were context I did not draw on. Node 71 in full: I needed its condition and its `## Review`,
and the interview, the correction round and the gate were confirmation — though the `## Review` sentence about
establishing the extent grep is the one that made the node 71 finding *bite*, and I would not have found it by
reading only the answer. Node 95 and node 111, of which I used one section each — node 95's annotation and node 111's
condition block. The `mattpocock-skills` grilling and domain-modeling skills, not invoked, per the flag above.

**What would have made this node easier.**

First, and it is my own node's finding arriving in my own node file: **the question names three parties whose
enumerators exist and there were four by the time I claimed it.** Node 103's was supplied by the manager at guard 1,
which the question's framing — four parties who *could run* the search, with the author owning the writing of it —
does not anticipate. A question resting on a set of instances should carry the enumeration of that set, which is
exactly what node 94 decided and exactly what node 94's own retrospective reported about its own node file. **That is
the second consecutive node where the node file is an instance of its own finding.** Naming it at minting is cheaper
than a worker rediscovering it, and the fix is one line: the set, and the command that produced it.

Second, the spawn's manager notes were the highest-value part of the payload, as at node 94. Two specifically: that
nodes 111 and 114 gave me live material rather than hypotheticals is what turned this node from an argument into a
measurement, and the judgement that the second sub-question was the sharper one was right. Neither was reachable from
the files. What let me use them without deferring was their being marked as context rather than as steer — and the
mid-task note that node 103 was a fourth authorship case *"yours to say or to leave alone"* is the cleanest version
of that I have seen: it named the choice, named that it was mine, and took no position.

Third, a structural one, and it is the same one node 94's retrospective recorded — hit again, so it is a pattern
rather than an observation. My contract sends me to `decisions.md` as a pointer and tells me to follow the lines that
bear on my question. What I needed from nodes 111, 114 and 103 was **the text of their acceptance conditions** — not
what those nodes decided, and in two of the three cases those nodes have not decided anything, being open. No index
line will ever carry that, and open nodes have no index line at all. I found them by listing the `nodes/` directory
and guessing from filenames, which worked because the spawn named two of the three. **The general shape: a grilling
node about a rule's mechanics needs the live artifacts the rule has produced, and the graph indexes decisions rather
than artifacts.** I do not have a fix. I record it because it is now twice.

**What I read that was stale, wrong, or contradicted something else.**

- **Node 71's condition records a return that is false**, and was false when its own checker recorded establishing
  it. Reported under `INVALIDATIONS`. The class is *an enumerator whose domain includes the effort's record*, and the
  specific mechanism — a condition quoting the phrase it greps for, thereby matching itself — is one nothing on this
  graph names.
- **Node 114's condition recorded a return false in both halves**, with a case-sensitive command and a
  case-insensitive recorded result. Corrected in place by the manager after this node reported it, before any claim.
  Worth keeping as the shape: the command and the recorded return can disagree with each other, which is a defect no
  amount of re-reading the *list* would surface.
- **Node 82's guard 1 still reads as reconstruct-a-search.** Its wording is that the manager *"re-runs the search
  that produced that list"*, which node 94's annotation on that node already corrects — in 42 of 43 cases the search
  existed nowhere. The annotation is on the node; the guard's own sentence is not marked, and a reader arriving at
  `### The two guards` first meets the unqualified version.
- **The `/grilling` instruction is now three-for-three unrun** across nodes 94, 102 and this one. Node 113 exists to
  settle it, so this is evidence for that node rather than a new report — but the map's `## Notes` line naming those
  skills as *"skills every session should consult"* is currently contradicted by every grilling worker's practice,
  and nothing at the map end says so.
- **One thing that was right, and worth recording.** My spawn did not list `flags.md` among my pointers and my
  contract's `## What you read` says to leave it unread. Node 94's retrospective recorded the same, against flag
  `82.2` and the still-open node 32: the flat clause is presumably still on disk in five contracts, and the spawning
  practice has now corrected itself three nodes running. I read no `flags.md` and nothing was lost.

**The manager's note on the retrospective.** *Not a change to anything above.* Its third point is now recorded twice
by two different workers and the manager has no fix either — **the graph indexes decisions and not artifacts**, and a
node about a rule's mechanics needs the artifacts. The first point is a **minting** defect and therefore the
manager's: a question resting on a set of instances should carry the command that produced the set. That is the third
such promotion the manager owes off a retrospective and has not made. The fourth point is now carried by [Whether the
contracts' instruction to invoke a method skill is doing any
work](113-whether-the-method-skill-instruction-does-any-work.md), and the map's contradicting line is named there.
