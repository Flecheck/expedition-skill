# Workflow self-improvement during use

Type: grilling
Status: resolved

## Question

When using the workflow reveals that the **workflow itself** is wrong, where does that go?

Surfaced by [Dogfood target](09-dogfood-target.md). The human's expectation is explicit: *"The workflow is bound to evolve and improve anyway as I find new things by using it"*. So this is not an edge case to handle once — it is the expected steady state, and the dogfood run's most valuable output is the friction it exposes. Without a place to put that, it evaporates into a transcript.

The awkwardness is that the friction is discovered on one graph and has to be fixed on another:

- A subagent grilling a Lang spec gap notices the relay payload is missing something. That is not a Lang node — Lang's graph is about a programming language. Does it become a node on **this** map, which may by then be closed? A node on Lang's graph tagged as not-about-Lang? A separate log?
- **Who is allowed to notice?** Subagents are read-only and stay off the graph, per [Relay protocol](08-relay-protocol.md). If only the manager may record friction, everything a subagent noticed has to survive its return value. If subagents may record it, the single-writer rule needs an exception.
- **What granularity?** A one-line "this was annoying" is cheap and gets written; a properly-framed node is useful and does not get written. These may want to be two different things, with a promotion step.
- Does friction **interrupt** the run or queue? [Revision semantics](06-revision-semantics.md) chose queued graph edits over human interrupts for cascades; the same reasoning may apply, but a workflow bug can also be blocking the very run that found it — the workflow cannot always defer fixing itself the way it can defer a decision.
- **When may the workflow be changed mid-run?** Editing the skill files while a graph is live means later nodes ran under different rules than earlier ones, so the dogfood stops being one experiment. Freezing until the run ends is cleaner but wastes what was just learned. Is there a distinction between a fix that unblocks the run and an improvement that can wait?
- Does this map's own destination move? The destination is *dogfooded once*. If a friction fix is required to *finish* the dogfood, the map has to accept new implementation nodes after it thought it was nearly done — which is [Done-ness](10-done-ness.md)'s oscillation question wearing a different hat.

Added by [Done-ness and termination](10-done-ness.md), which widens where friction comes from and answers the last bullet:

- **Some of it will be found on machines and repositories this graph can never see.** The human will also run the workflow on work projects elsewhere — and those are the runs *most* likely to break the design, because a bounded effort that actually terminates exercises the parts Lang never will. A channel that works only by an agent reading files in this repo misses exactly those.
- So friction from there arrives as **the human's own words to the manager** — a third possible noticer alongside the manager and the subagent, and the one the *who is allowed to notice* bullet did not consider. It also puts a floor under the granularity question: whatever the mechanism is, the human has to be able to dictate a one-liner from memory, days later, about a repository that is not even open.
- **The destination bullet above now has a mechanical answer.** Done-ness settled that only the human closes an effort, and that a fix landing as a new node simply keeps the frontier non-empty. So this map's destination does not need to move: the map cannot close while friction nodes are open, and the human decides when to stop accepting them.

- **How a self-edit lands is settled, and it is not special.** [Git and code-landing policy](11-git-and-code-landing.md) rules that an effort's graph lives in the repo the effort changes and that each repo's effort follows the same policy — so a friction fix to the skill files is an implementation node on *this* map, landing in `graph-agent` by the same gate as anything else: reviewer, human approval, one path-limited commit. Nothing cross-repo is coordinated. What stays this node's question is **when** the workflow may edit itself — mid-run, between efforts, or only when the human says so — not how the edit lands.
- One consequence worth noticing: a self-edit during the dogfood takes the **exclusive code slot in `graph-agent`** while Lang's own implementation nodes hold Lang's. Two independent slots in two repositories is not something the concurrency model has been asked about, and it is the first case where the workflow improving itself competes with the workflow doing its job.

Not blocked: answerable now, and worth answering before the dogfood starts rather than during it, since the run is where the friction arrives.

### What the record now holds, gathered by the manager before this node was claimed

*The manager's own note, not a decision.* This node was written when the graph held twenty nodes and had
shipped nothing. It now holds forty, has landed nine commits into the workflow's own files, and has changed
those files five times while workers were reading them. So most of the bullets above have **measurements**
rather than only arguments, and a worker that re-derives them spends the human's time on facts. Facts and
where to check them follow; no conclusion is drawn, and every question above is still open.

**The caveat that bounds all of it.** This map's product *is* the workflow, so here a friction fix and the
work are the same act — every instance below is the **degenerate** case. The question as written is about the
other one: friction found on an effort whose product is something else, which is Lang and the work projects,
and neither has started. Facts 1–6 measure how friction behaves when the noticer and the fix live in one
repo. Nothing on the record measures the crossing.

**Fact 1 — the mechanism has been running unnamed, seventeen times, and every instance is traceable.** Each
row is stated on the named node, in its own provenance line.

| node | who noticed | how it reached the graph |
| --- | --- | --- |
| [23](23-worker-cannot-proceed.md) when an AFK worker cannot proceed | the human, steering mid-session | dictated, verbatim on the node |
| [24](24-self-hosted-friction.md) friction from running this map by hand | the human, steering | a `precondition` node whose answer is fourteen findings |
| [25](25-recording-an-option-taken.md) recording an option taken | node 17's **worker**, as the stated limit of the check it built | handover |
| [26](26-carry-deltas-into-shipped-files.md) carry the recorded deltas | the map's **delta list**, promoted | nine `## Notes` appends, then one implementation node |
| [27](27-does-flags-file-survive.md) does `flags.md` survive | the human, reading node 25's settled flags | dictated |
| [28](28-spawn-overriding-a-contract.md) spawn overriding a contract | node 26's **worker**, told the override had happened | handover |
| [29](29-shipped-file-consistency.md) shipped-file consistency | the delta list's **own failure** | node minted instead of a tenth line on the list |
| [31](31-checker-contract-owes.md) what the checker contract owes | node 33's **blind checker**, reserving a clause it could not establish | node minted at the gate |
| [32](32-narrow-flags-file-clause.md) narrow the `flags.md` clause | node 28 — a repair left to the manager's judgement and lost | node |
| [33](33-condition-is-self-contained.md) a condition is self-contained | node 28 — the same repair, the part that was not lost | node |
| [34](34-implementer-disputes-a-finding.md) implementer disputes a finding | the human at node 28's gate | dictated |
| [35](35-handover-mints-no-condition.md) handover mints no condition | node 33's **worker** | handover |
| [36](36-resolved-node-clause-cannot-be-self-contained.md) the record-wide clause | node 33's **worker** | handover |
| [37](37-invalidations-is-not-a-check.md) `INVALIDATIONS` is not a check | node 36's **worker** at that node's gate, as the honest cost of the answer it had just shipped | handover |
| [38](38-recording-a-not-covered-part.md) recording a not-covered part | node 31's **worker** | handover |
| [39](39-condition-for-a-manager-minted-node.md) condition for a manager-minted node | node 35's **worker** | handover |
| [40](40-flag-account-has-no-handover-part.md) flag account has no handover part | node 35's **blind checker** | a note attached to a check, then the human's word, then a node |

By noticer: **seven** a worker, **two** a blind checker, **four** the human dictating, **four** a resolved
node's own answer or a mechanism. By route: **seven** a handover part, **four** the human's words in chat,
**four** a node minted by the manager from a finding it held, **one** promoted from a running list, **one** a
checker's note promoted by the human.

**Fact 2 — the two-level shape the third bullet asks for exists, and has been run end to end exactly once.**
The map's `## Notes` carried a **delta list** — *"nine deltas the shipped `graph-conventions.md` does not yet
carry"* — grown one line at a time by nine different nodes across several sessions, then **promoted** into
[Carry the recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md), which
discharged all nine and landed as commit `0cec4e7`. Cheap line, then promotion, and it worked. It also failed
once, measurably: node 25's delta landed on two of the six worker contracts, which the list did not track, so
that fix *"had nowhere to be recorded at all"* — the map's own lesson being *"a delta list works until a delta
lands on a file the list does not track."* [What keeps the shipped files consistent when a decision changes a
term](29-shipped-file-consistency.md) holds that failure and two further levels of it.

**Fact 3 — a subagent's noticing already survives its return value, and the single-writer rule needed no
exception.** Two of the five mandatory handover parts are `NEW NODES` and `FLAGS`. A worker that notices
friction reports it there, the manager files it, and the worker still writes nothing — so the second bullet's
fork resolved to its first branch at no cost. Seven of the seventeen rows arrived exactly that way, and two
more came from a **blind checker**, which reads neither its node nor the record and still produced two
requirements on the workflow.

**Fact 4 — queue-versus-interrupt already has a two-tier answer.** All seventeen **queued**: not one
interrupted the node it was found on. The interrupt exists separately, as node 28's **manager's blocking
raise** — where a shipped clause blocks the node in front of the manager it raises, and the human's answer
yields both a licence for that one attempt and a node for the permanent fix. Measured rate: two firings in
thirty-one nodes, with the map recording that a materially higher rate reports the contracts are wrong rather
than anything about the node in front of the manager.

**Fact 5 — the workflow has been edited mid-effort five times, and the hazard measured the opposite way round
from the guess.** After the first contracts shipped at `e72f444`, five commits changed workflow files while
this graph was live and spawning workers: `0cec4e7`, `51f281d`, `6c7d409`, `f2fc81c`, `ad06086`. Three things
were measured rather than argued.

- [What the checker contract owes to having been run](31-checker-contract-owes.md) rewrote the **checker's own
  contract** and then spawned its checker, which reported *"my instructions match the post-change text"*. So a
  contract edited mid-session **does** reach a worker spawned afterwards, and the recorded hazard inverted:
  what it guards against is that a node editing a contract silently changes the contract of every worker
  spawned after it, its own checker included. That is flag `31.2`, filed by the manager about itself.
- The *"earlier and later nodes ran under different rules"* cost in the fifth bullet is real and was paid, on a
  graph-file form rather than a contract: node 26 writes a flag's `settled` marker after the type marker and
  node 27 before it, so **22 entries follow the shipped form and 9 did not**, and the divergence survived a
  session because nothing among the eight checks verifies conformance to a form the conventions document
  fixes.
- The vocabulary case the `## Annotation` below calls the worst-behaved self-edit has also already happened:
  [Naming](14-naming.md) changed four settled words under previously-resolved nodes and moved the node
  directory, and the map's standing note is that prose written before that point still says the old words —
  *"that is the never-delete rule, not drift, and the glossary is authoritative."*

**Fact 6 — the human's dictated one-liner has fired at least four times, and the map absorbed it every time
with nothing routing it.** The floor the annotation from [Done-ness and termination](10-done-ness.md) put
under granularity — the human dictating a one-liner from memory, days later, about a repository that is not
even open — has already been exercised on this repo, in their own words: *"You should write your findings down
somewhere, I don't know if it is worth it"* became node 24; *"maybe first restart the worker and then write the
file, it might gain a bit of parralellism"* became the eighth delta, and the map records it as the first
correction to `graph-conventions.md` that came from the human watching the manager work rather than from a node
deciding something; *"using opus for everything is running through my tokens quite fast"* became an append to a
fog item, parked at their word *"also for later"*; and their judgement on `flags.md` became node 27. Two landed
as nodes, one as a `## Notes` delta, one as a fog append — and the manager placed each by judgement.

**What none of the seventeen touches, and it is where the answer has to work.** Two gaps.

- **The crossing.** Every instance was noticed inside the one repo holding both the graph and the workflow.
  Nothing has yet had to get a node onto a graph the noticing agent cannot see: an agent working a Lang node,
  or an effort on a work project on another machine, noticing something about expedition. [Git and code-landing
  policy](11-git-and-code-landing.md) settled how such a fix **lands** — an implementation node here, ordinary
  policy, nothing cross-repo coordinated — and left how it **gets** here to this node.
- **What happens once this effort closes.** [Done-ness and termination](10-done-ness.md) settled that only the
  human closes an effort and that this map cannot close while friction nodes are open. It does not say where
  friction from a work-project run arrives after the human has closed this one — a fresh effort in
  `graph-agent`, a standing map that never closes, or something else. That is the human's time and so their
  call.

### Standing instructions for this node's worker

Written here because the manager holds them and the files cannot tell you.

- **The human has read none of the above.** Write `ABOUT` and `SO FAR` on every question, the first included.
  The map's fog items are single paragraphs carrying appends from many nodes, so read whole paragraphs rather
  than sentences, and expect the same on node files.
- **Spend no question on anything in Facts 1–6.** Verify by the paths given if you doubt one. Say in `SO FAR`
  what you are taking as settled, so the human can contradict it rather than have to confirm it.
- **Five bullets is more than one decision.** Expect several rounds, take the sharpest fork first, and do not
  bundle two decisions into one question — a bundled question comes back answered on one of them.
- **Do not assume the answer is a new file.** The graph is four files, fixed by [Graph file
  format](13-graph-file-format.md), and this effort has never added a fifth. A mechanism that fits an existing
  file — a fog item, a `## Notes` block, a node, a flag — costs nothing to ship. That is a bias to state and
  defend if you keep it, not a rule you inherit.
- **Where your answer needs a shipped file changed** — a worker contract, `graph-conventions.md`, or the
  manager's own skill, which is still fog on the map — that is an implementation node you report, and its
  acceptance condition is yours to write.
- **Where something already works, say so plainly rather than designing beside it.** The map's standing
  preference is short simple prose that can be changed later over machinery built for predicted needs, and
  Fact 1 is a mechanism that has run seventeen times unnamed. Naming it, and fixing the two gaps above, may be
  most of the answer.

## Annotation

Added by [Naming](14-naming.md).

- **The promotion step this node asked for exists, and it is called `promote`.** Derived for flags in [Done-ness](10-done-ness.md), it is the same act: turn a one-line note of friction, or a flag, into a node. So the granularity question keeps both levels — a cheap line that actually gets written, and a node it can be promoted into — under one verb.
- **A vocabulary change is a self-edit like any other, and the worst-behaved one.** [`CONTEXT.md`](../../../CONTEXT.md) is a product-tree file in `graph-agent`, so changing a settled term lands through the gate here like anything else. But it is the one kind of self-edit that makes earlier and later nodes of a live effort read differently, which is this node's *may the workflow change mid-run* question at its highest stakes.

## Answer

Friction with the workflow itself travels as a **`FRICTION` flag**, raised on the graph where it was
noticed and discharged only in the repository that holds the expedition skill files. Six things were
settled, in six rounds.

**1. A self-edit may land mid-effort, on the ordinary gate and nothing more.** No freeze and no new
permission rule: every implementation node already ends at the human's gate, so a freeze would only
remove their ability to say yes. The guessed hazard was measured and came out inverted — [What the
checker contract owes to having been run](31-checker-contract-owes.md) rewrote the checker's own
contract and the checker spawned afterwards reported that its instructions matched the post-change
text, so a contract edited mid-session *does* reach a worker spawned after it. What that actually
costs is the reverse of the fear: a node that edits a contract silently changes the contract of every
worker spawned after it, its own checker included. Five such edits had already landed while this graph
was live and spawning workers — `0cec4e7`, `51f281d`, `6c7d409`, `f2fc81c`, `ad06086` — verified in
git at this node.

One duty is attached. An implementation node that changes a file which other nodes of the same effort
are written against must, at its gate, name which files it moved and which existing files are left in
the older form. The manager carries that statement into every later spawn and re-check, which extends
the requirement already recorded on **the manager's own skill** that a statement of what changed must
cover commits and not only the working tree.

**2. Form changes are not carved out, and the duty's limit is known and unrepaired.** The one cost
actually paid was a divergence in a *form* rather than in prose: deltas six and seven fixed a new shape
for a flag entry, that shape shipped mid-effort in `0cec4e7`, and 22 entries then conformed while 9 did
not, silent for a session until a loosened scanner found them and [Whether a spawn may override a
shipped worker contract](28-spawn-overriding-a-contract.md) normalised them by hand. The never-delete
rule does not cover that case; it covers older prose keeping older words.

The duty in 1 does not cover it either, and this was checked rather than assumed: node 26 holds exactly
nine flags and node 26 *is* the node that shipped the form, so the nine nonconforming entries were its
own, written after its own change. It was not leaving files in the old form — it was writing the new
form wrong. What covers that case is conformance checking of a shipped form, which is [What keeps the
shipped files consistent when a decision changes a term](29-shipped-file-consistency.md)'s question,
open with nobody on it and load-bearing for the permission granted in 1. Recorded here rather than
repaired, and not made a blocker of anything.

**3. Friction noticed on another effort is a flag on that effort's graph, never a node there.** The
flag is the only existing mechanism whose reader is already this problem's reader: [Whether flags.md
survives the settle-at-close practice](27-does-flags-file-survive.md) settled that `flags.md` is not a
queue but the capped index of every judgement an agent made on its own, one sentence written to be read
cold by someone who has not read the node — which is the human, days later, on a repository that is not
open. It is already harvested by the sweep and the closing report, and `promote` is already defined in
the glossary over *"a flag, or a one-line note of friction"*. Every noticer reaches it with no change:
a worker's handover has a `FLAGS` part, the manager files its own.

A node on that graph is not merely worse but wrong: it could never be resolved there, since the fix
lands in the skill's own repository by [Git and code-landing policy](11-git-and-code-landing.md), so it
would sit on that effort's frontier permanently and make the effort uncloseable when an empty frontier
is a condition of closing.

The marker earns its own word because a flag's ordinary disposition is to be **settled in place** and
this one's is to be **exported**; mixing them in one index means the human settles half a list and
carries the other half.

**4. No standing graph in this repository; a fresh bounded effort each time.** The durable store is
already the flag on the graph where it was noticed, so an inbox here would be a *second* copy of items
whose first copy is authoritative — and a second list somebody must remember to extend is the pattern
that failed three times on [What keeps the shipped files consistent when a decision changes a
term](29-shipped-file-consistency.md)'s record. Discharging a batch of carried friction is a bounded
destination; *"expedition keeps working"* is not a destination at all, and `Destination` is the term
that fixes scope. Charting an effort is what settling a `FRICTION` flag does when nothing is live here.
This applies the map's own rule already applied once, that a redrawn destination is a fresh effort
inheriting v1's contracts rather than a resumption.

**5. A `FRICTION` flag is never settled as fixed on the effort that raised it.** The human's words,
`verbatim`: *"The effort, if not in this project can't fix the skill. The effort in another project
will never fix the skill"*. Two dispositions and no third:

- **refused** — the human judges it not worth carrying, settled in place with their reason recorded;
- **outstanding** — left unchecked, meaning carried, and re-surfaced at that effort's close.

Settled-as-fixed is unavailable. That is node 28's measured failure forbidden at its one move: what
lost the repair there was a licence marked settled with nothing behind it. No agent can ever tick the
line, because no agent crosses a repository boundary and the machine may not be the same one; the human
owns graph commits and may tick it by hand once they know the fix landed. An outstanding line reading
*still not fixed* is the honest state.

Because nothing can be lost while the flag stays outstanding, **no batch trigger is needed** and the
human batches at whatever size they like.

Two consequences. Nothing on such an effort may be made to wait on the skill being fixed — no
acceptance condition and no closing condition — because that effort could never close. And [Done-ness
and termination](10-done-ness.md)'s promote route mints its node in the skill's own repository, in a
session there, never on the graph that raised the flag: it is the human's act, not the foreign
manager's.

**6. Blocking friction is passed by the human's own instruction, carried.** Their words, `verbatim`:
friction *"will be used to add custom instruction for the task if nessesary and then I will take
fraction flags and try to improve the workflow so that it doesn't happen often"*. Since a foreign
effort never fixes the skill, that instruction is the *only* route past friction that blocks, rather
than one option among several — *"if nessesary"* reads as *if it blocks*.

Needed once, it is the human's carried direction in that one spawn, marked as their words. Needed more
than once, it becomes a line in that effort's **ground rules** in `map.md`'s `## Notes` — already
optional prose, already declared per effort, already a pointer every worker receives, so making it
durable costs one paragraph and no new file. That promotion is the local form of what the human
described globally: reducing how often the friction happens, one repository at a time.

It is never the manager's to invent. Node 28 settled that a spawn may not depart from a shipped
contract on the manager's authority; the manager **raises**, and the human's answer supplies the
licence. And in a foreign repository node 28's second output — a node for the permanent fix — is
impossible by the human's own words, so there the `FRICTION` flag **takes the node's place**: raise,
licence, flag.

The harvest's purpose is the human's own and it is aggregate: *"try to improve the workflow so that it
doesn't happen often"* rather than items discharged one at a time. That is what makes a batch genuinely
a batch, and it is why the absence of a trigger costs nothing.

**One thing the blind checker needs, endorsed separately.** An effort's ground rules reach every worker
except the **checker**, which reads no map — so a workaround written as a ground rule would not reach
the party whose own contract is a measured source of friction. The remedy takes an existing precedent
rather than inventing a channel: the manager already copies the bar's non-command half into the
checker's spawn as text, precisely because the checker cannot be pointed at the map, and a ground rule
travels the same way. It does not unblind anything, provided the boundary holds — what may be copied is
a **standing constraint** on the effort, true of any node's work, and never an account of what happened
on this node or elsewhere in the record, which is what the checker is kept blind to.

**What this node does not settle.** A checker's own route to raising a `FRICTION` flag: it writes no
flag, and what it hands back alongside its outcome belongs to [Recording a not-covered
part](38-recording-a-not-covered-part.md) and [A flag's account has no handover
part](40-flag-account-has-no-handover-part.md). And conformance checking of a shipped form, which is
node 29's.

## Flags

`19.1` **· settled** `ASSUMPTION` — **the marker's name.** Took `FRICTION` over the runner-up `UPSTREAM` on my own
authority. I offered the name as a one-word overrule and the human's reply named the mechanism and not the
word, so this is a reading of an absence rather than an assent. Chosen because `FRICTION` is already this
effort's own word for the thing — node 24 is titled with it and the dogfood already owes a record of it —
rather than a coinage; `UPSTREAM` names the disposition instead and generalises past expedition. Cheap to
overrule at the implementation node's gate, where the word first reaches a shipped file.

`19.2` **· settled** `ASSUMPTION` — **the disclosure duty's limit routed to node 29 rather than reopened.** I established
that node 26 holds exactly nine flags and shipped the form those nine diverged from, so the duty the human
endorsed would not have surfaced them. I neither reopened the mid-effort permission nor minted a node for it,
on the ground that map.md already assigns *a shipped form that nothing checks* to node 29 — leaving node 29
load-bearing for a permission now granted, and open with nobody on it. Stated in the answer rather than made a
blocker of anything.

`19.3` **· settled** `ASSUMPTION` — **the remedy for the blind checker not seeing ground rules.** The human endorsed the
manager's observation — *"fair point from the manager"* — and named no remedy, so I wrote one: copy the ground
rules into the checker's spawn as text, on the existing precedent of the bar's non-command half travelling
that way. I also drew the boundary that keeps it from unblinding the check — standing constraints only, never
an account of what happened — which nobody asked for and which is the part most likely to be wrong.

`19.4` **· settled** `ASSUMPTION` — **the two dispositions carried through an answer that neither took nor rejected them.**
I offered *refused or outstanding* as a recommendation, the human's next answer was substantive on a different
point, and I restated the dispositions for contradiction in the round after. None came. I am treating
silence-after-explicit-restatement as enough, on the ground that *"the effort in another project will never
fix the skill"* is consistent with them and rules out the only alternative disposition, settled-as-fixed.

## Interview

### Attempt 1 — routing key `graph-workflow/19/a1`

Spawned against [`expedition-grilling/SKILL.md`](../../../.claude/skills/expedition-grilling/SKILL.md), over
the three standard pointers and no per-type addition, after the manager's fact-gathering block above was
written and the node was claimed.

**The worker declared five of this node's questions settled before asking anything**, and put them in `SO FAR`
for the human to contradict rather than confirm: *who may notice* (four parties, seventeen traceable
instances), *granularity* (the two levels exist and the verb is `promote`), *queue-versus-interrupt* (all
seventeen queued; the interrupt is the manager's raise), *how a fix lands* (node 11's ordinary gate), and
*whether this map's destination moves* (it does not). It named what it judged genuinely left as three things,
and its own ordering of them: **(A)** whether the workflow may be edited while an effort using it is live,
**(B)** how friction noticed on another repo or machine gets here at all, **(C)** where it goes once the human
closes this effort — taking (A) first on the ground that it constrains the other two, since *"if edits must
wait for a window, arriving friction needs somewhere to sit until the window opens."*

**Q1** — *the worker's words:* May a friction fix to expedition's own files land while an effort using those
files is live — on the ordinary implementation gate and nothing more?

It recommended **yes, on the ordinary gate and nothing more** — no freeze, no new permission rule, and one
duty added — on four measured grounds rather than argued ones: that it has already happened five times on this
graph while nodes were being spawned (`0cec4e7`, `51f281d`, `6c7d409`, `f2fc81c`, `ad06086`, verified in git by
the worker itself); that the feared hazard is inverted, node 31 having rewritten the checker's own contract and
its checker reporting its instructions matched the post-change text, so the real hazard is a node silently
changing the contract of every worker spawned after it; that no new permission is needed because every
implementation node already ends at the human's gate, so *"a freeze rule would only remove your ability to say
yes"*; and that the one cost actually paid was a silent divergence rather than a broken worker — the 22-versus-9
flag marker split. Hence the duty, *"where the cost lands rather than a rule against editing"*: a node that
changes a shipped workflow file states at its gate which files moved, and the manager carries that statement
into every later spawn and re-check, covering commits and not only the dirty working tree.

Four alternatives set aside, each with its reason: **freeze per effort** (Lang is not expected to terminate, so
the window never opens); **explicit say-so per self-edit** (identical to the gate that already exists, so
ceremony without protection); **two tiers, unblocking fixes now and improvements queued** (needs a judgement
call per fix, and frontier order already lets the human prefer the unblocking one); and **freeze only a
vocabulary change**, which it named as the nearest thing to a real objection it found and set aside on the
never-delete rule — older prose keeps the old words and the glossary is authoritative.

**A1** — the human, `verbatim`: *"yes"*.

Taken against the recommendation it was offered, which was the worker's: **"Yes, on the ordinary gate and
nothing more — no freeze, no new permission rule, and one duty added."** No `DIVERGENCE`.

One thing the record should carry about the shape of that answer. The manager put a push of its own to the
human in the same message as the question — that the vocabulary carve-out may be stronger than the worker
credited it, because the 22-versus-9 marker divergence the worker cites as *the one cost actually paid* is
precisely the case the never-delete rule does **not** clean up: a divergence in a **form**, not older prose
keeping older words, and it survived a session because nothing checks conformance. It is [What keeps the
shipped files consistent when a decision changes a term](29-shipped-file-consistency.md)'s open territory. The
human answered *"yes"* with that note in front of them and said nothing about it, which is neither an
endorsement of it nor a rejection: it stays the manager's note, unanswered, and was carried to the worker as
one.

**Q2** — *the worker's words:* Does a self-edit that changes a **form** the graph files are written in need
carving out of the permission you just gave — frozen until between efforts — or is the disclosure duty enough,
extended to cover it?

**The worker withdrew one of Q1's four grounds before asking.** In its words: *"one of my four grounds was the
wrong ground. I claimed the never-delete rule already covers the worst case. It does not."* Never-delete
covers older **prose** keeping older words, which is the case [Naming](14-naming.md) created; it does not
cover a divergence in a **form**, and that is the case that actually happened. It then established the fact
that closes the loop, having read both files: they conform today because [Whether a spawn may override a
shipped worker contract](28-spawn-overriding-a-contract.md) **normalised the nine by hand**, after a scanner
it had to loosen found them. So the cost was real, silent for a session, and cleaned up by a person noticing
rather than by any rule. Its conclusion did not move; the ground under it did.

It recommended **no carve-out, extend the duty instead**: a form-changing self-edit says at its gate which
existing files are left in the old form, with conformance checking staying [What keeps the shipped files
consistent when a decision changes a term](29-shipped-file-consistency.md)'s. Three grounds. **The freeze aims
at the wrong thing** — what cost a session was not the edit but the **silence**, and node 26 shipping the new
flag form while recording that the twenty pre-existing flags predate it and stay un-id'd is the disclosure
already working. **A freeze does not remove the split it aims at**: a form landing between efforts still
leaves the previous effort's files in the old form, so pre-form and post-form files coexist either way and the
freeze only moves the seam. **And the measured price of not freezing was one hand normalisation of nine
entries**, against having ids and settled markers on the 22 written in between — which is what turned
mechanical check 6 from a prose match into an exact join.

Four alternatives set aside: **freeze form and vocabulary changes to between efforts**, named as the strongest
version of the manager's push and set aside for the reasons above; **plain no carve-out with the duty
unchanged**, cheapest, set aside only because the one thing that actually went wrong was invisible under it;
**require the form-changing node to normalise the existing files** rather than name them, aimed at the right
target but a bigger instrument than the evidence supports, node 26 having declined to retro-fit twenty flags
and been right to; and **no form change until node 29 settles what checks conformance**, rejected because that
would let an unstarted node block work already permitted.

**The manager put a second note to the human alongside this question, and it is a defect in the recommended
remedy rather than in the reasoning.** The extended duty addresses **legacy** files — which existing files are
left in the old form — and the failure it is derived from was not in a legacy file. The nine nonconforming
entries were written **after** the form shipped, by node 26, which is the node that shipped it: the form was
new, the writing was new, and it was the new form done two ways. Node 26 *did* disclose the legacy twenty, in
its own answer — *"The twenty un-id'd flags in `flags.md` were not retrofitted"* — and that disclosure worked
exactly as the worker says. So the remedy and the evidence do not line up: no statement at a gate would have
surfaced this, which leaves conformance checking as the only thing that reaches it, and that is node 29's. The
note does not argue for the carve-out; it argues that the case against the carve-out rests on node 29 rather
than on the duty.

**A2** — the human, `verbatim`: *"ok"*.

Taken against the recommendation it was offered, which was the worker's: **"No carve-out; extend the duty
instead. A form-changing self-edit must say, at its gate, which existing files are left in the old form — and
that is the whole remedy here, with conformance checking staying node 29's."** No `DIVERGENCE`.

The manager's second note went unanswered in the same way as the first — the human replied with it in front of
them and said nothing about it, which is neither endorsement nor rejection. What the note establishes stands on
its own facts either way: node 29 is load-bearing for a permission now granted, and it is open with nobody on
it.

**Q3** — *the worker's words:* When an agent working an effort in another repo notices something wrong with
expedition itself, where does that get recorded on that effort's own graph?

**Two things the worker settled on its own authority first.** It verified the manager's second note and
sharpened it: **node 26 has exactly nine flags**, and node 26 is the node that shipped the form — so the nine
nonconforming entries were its own, written after its own change, and the duty the human endorsed *"would not
have surfaced them, because the node was not leaving files in the old form, it was writing the new form
wrong."* It kept the duty as endorsed and recorded the limit in the answer plus one flag rather than reopening
it. And on (B) it established that **the carrier across the boundary can only be the human**: multi-repo and
cross-machine dispatch are out of scope on [map.md](../map.md), [Git and code-landing
policy](11-git-and-code-landing.md) coordinates nothing cross-repo, so no file channel between machines exists
by design. What is undecided is the step **before** the human: where a foreign effort writes the thing down so
it survives the session it was noticed in.

It recommended a **flag on that effort's graph under a marker of its own, `FRICTION`, and never a node there.**
Its grounds: a flag is the only existing mechanism whose reader is already this problem's reader — [Whether
flags.md survives the settle-at-close practice](27-does-flags-file-survive.md) fixed `flags.md` as the capped
index of every judgement an agent made on its own, one sentence written to be read cold by someone who has not
read the node, *"which is exactly you, days later, on a repo that is not open"*; it is already harvested, the
sweep collecting every outstanding flag before an effort closes, so on a work project — the kind of effort that
actually terminates — the carry moment is scheduled rather than left to memory; `promote` is already defined in
the glossary over *"a flag, or a one-line note of friction"*, so the input is named already; and every noticer
has a route to it with no change, a worker's handover having a `FLAGS` part.

**Why not a node on the foreign graph**, which it called the one candidate actively wrong rather than merely
worse: a friction node there can never be resolved there, the fix landing in `graph-agent` by node 11's
policy, so it would sit open on that effort's frontier permanently and make the effort uncloseable — against
an empty frontier being a condition of closing. **Why its own marker:** a flag's disposition is to be
**settled in place** and this one's is to be **exported**, and mixing them in one index means the human settles
half a list and carries the other half. Two riders it offered as cheap to overrule: the manager narrates a
`FRICTION` flag when it is raised, because most efforts never close and the closing report would then never
fire; and shipping it needs one paragraph in `graph-conventions.md` and one glossary entry, which it will
report as an implementation node.

Five alternatives set aside: a **`## Friction` section or `## Notes` block on the foreign map**, the delta-list
shape and the only two-level mechanism that has run end to end here, set aside because nothing harvests it and
the map records that the human's view is the manager's narration plus code review; an **`## Out of scope` entry
there**, tempting since the status keeps it off the frontier, but the glossary says out-of-scope work never
graduates and this must; **nothing written down**, the manager raising the line in chat, which is what has
actually happened four times and worked *"because you remembered, and that is not a mechanism"*; **a file under
`.claude/skills/expedition/` in the foreign repo**, rejected as putting expedition's notes in someone else's
product tree; and the marker named **`UPSTREAM`** rather than `FRICTION`, named as the runner-up and a one-word
overrule.

**The manager put a third note to the human alongside this question: the export has no verification, and the
precedent says an unverified export is lost.** A `FRICTION` flag's `- [x]` would mean *carried*, and nothing
anywhere checks that the carry produced a node here — the foreign graph cannot see this one, and this one never
sees that flag. That is the failure [Whether a spawn may override a shipped worker
contract](28-spawn-overriding-a-contract.md) measured and answered: a repair left to judgement produced *"no
node was ever minted, the clause is still on disk in five contracts unchanged"*, and its rule was **two
outputs, always both**. The same discipline here would be that settling a `FRICTION` flag names the node it
produced, or records the decision not to make one. Alongside it, one framing point: because a foreign effort
may never close, the sweep may never fire, so the worker's first rider — the manager narrating at raise time —
is not a rider but the actual carrier, and the file is durability behind it.

**A3** — the human, `verbatim`: *"ok for an flag"*.

Taken against the recommendation it was offered, which was the worker's: **"As a flag on that effort's graph,
under a marker of its own — `FRICTION` — and never a node there."** No `DIVERGENCE`. The reply names the
mechanism and not the marker, and the marker was offered as *"a one-word overrule"* against `UPSTREAM`; no word
came, so the recommendation stands as offered rather than the runner-up.

The manager's third note went unanswered like the first two. It differs from them in one way worth recording:
the first two were corrections to the reasoning, and this one proposes an **addition to the mechanism** — that
settling a `FRICTION` flag name the node it produced. A reply on the flag-versus-node fork neither endorses nor
rejects it, so it stayed the manager's note and went back to the worker as one.

**Q4** — *the worker's words:* After you close this effort, where does carried friction about expedition land —
a standing graph in this repo that is never closed, or a fresh bounded effort each time?

**Two carry-overs it named first.** On the marker, it is taking `FRICTION` as it stood *"because the word has to
be a word — it goes into `graph-conventions.md`, the glossary, and the acceptance condition of the
implementation node I will report"*, with `UPSTREAM` remaining a one-word overrule now or at that node's gate,
at no cost. On the manager's third note, it is neither dropping nor folding: *"It turns out to depend on your
answer to this question... If there is no graph in this repo to put a node on, 'name the node it produced' has
no referent, which is why this fork comes first."* So the note becomes the question after this one.

It recommended **a fresh bounded effort each time, and no standing graph** — charting one being what settling a
`FRICTION` flag does when nothing is live here. Three grounds. **The durable store is already decided and it is
not in this repo**: the flag lives on the graph where it was noticed, and that effort's sweep and closing report
already collect it, so a standing inbox here would be a second copy of items whose first copy is authoritative
— *"and a second list that someone must remember to extend is precisely the thing that has failed three times
on this effort"*, recorded on [What keeps the shipped files consistent when a decision changes a
term](29-shipped-file-consistency.md), each failure being *"a list that was correct about the files it knew"*.
**It matches this map's own rule, already applied once**: the heterogeneous-fleet work is recorded as *"a fresh
effort inheriting v1's contracts, not a resumption of this one"*, and *"discharging five carried frictions is a
bounded destination; 'expedition keeps working' is not a destination at all"*. **And it needs no machinery** —
a fresh effort is a map, a destination and some nodes, with nothing existing between batches.

It stated the hole in its own recommendation rather than leaving it: *"on its own this leans on you remembering
to chart one, which is the same weakness I rejected in the last round. It is closed by the settlement rule
rather than by a standing graph."*

Three alternatives set aside: a **standing graph never closed** in this repo, legitimate under
[Done-ness](10-done-ness.md)'s *most efforts never close* and giving one place to look, set aside as a duplicate
store with no destination to fix its scope; **never closing this effort**, rejected on this map's own evidence
that never-delete is beating load-once-cheaply — `## Notes` at fifteen paragraphs, single fog items carrying
eight appends — so *"a map that never closes would be lying about its own scope"* once *dogfooded once* is
reached; and **a file in the product tree**, rejected as a graph-shaped thing living outside the graph.

**The manager put a fourth note to the human alongside this question: the missing referent is not new, and it
already afflicts a rule this effort shipped.** [Done-ness and termination](10-done-ness.md) settled that at the
closing report the human settles each flag or **postpones** one, *which creates a node*. On a foreign effort
whose flag is about expedition, that node has no graph to live on either — so whatever answers this question
has to serve node 10's postpone route as well as the new marker, and the two should not get different answers.
Beside it, the cost that drives the choice: if charting an effort is the price of settling one flag, the human
will rationally **batch**, nothing defines the batch trigger, and between a foreign effort's close and the batch
the item's only home is a closed effort's closing report — which is this node's own *evaporates into a
transcript* failure moved one hop out.

**A4** — the human, `verbatim`: *"ok"*.

Taken against the recommendation it was offered, which was the worker's: **"A fresh bounded effort each time,
and no standing graph. Charting one is what settling a FRICTION flag does when nothing is live here."** No
`DIVERGENCE`.

The manager's fourth note went unanswered like the three before it. It bears on the question the worker had
already queued behind this one, so both were carried into that question rather than left as two separate
notes.

**Q5** — *the worker's words:* When a `FRICTION` flag comes up for settlement on the effort that raised it, may
the human settle it without a node existing here — and if so, on what?

**It folded in both parts of the manager's fourth note and corrected one of them on a fact it looked up.** The
correction: a flag is not normally settled at the closing report at all. Node 27 and the glossary put settlement
at *"the human moment that ends its node"*, with the closing report as the exception path for flags whose moment
never came — so a `FRICTION` flag reaches the human early and locally, at the end of the node that raised it,
and again at that effort's close if still outstanding. *"Two scheduled surfacings, neither relying on memory."*
It also corrected the manager's word: node 10's `postpone` was retired by [Naming](14-naming.md) in favour of
`promote`, which the glossary already defines over *"a flag, or a one-line note of friction"*. It agreed the
missing referent is shared and gave both routes the same answer, and it recorded the batching objection as the
thing that *"killed the strict reading of node 28's rule for me"*.

It recommended **exactly two dispositions and no third**: **refused**, settled in place with the human's
reason, or **outstanding**, left as it is and re-surfaced at that effort's close. *"What is not available is
settling it as done on the strength of having carried it."* Its ground is node 28's rule aimed where it was
measured rather than read literally — what node 28 measured was a flag marked settled with nothing behind it,
*"the repair was lost along with the record"*, so forbidding that one move is the whole remedy, while requiring
a node be named *"would force you to charter an effort in another repo in order to tick a line in this one."*

Three consequences it drew rather than asked about. **The batch trigger stops being needed**: an outstanding
`FRICTION` flag is itself the durable record, node 27 having settled that `flags.md` keeps flags nobody can
settle — twenty today — and is an index rather than a queue, so *"the item's home is never a closed report; it
is an outstanding line in a live file that gets read cold."* **No agent can ever mark one settled-as-fixed**,
no agent crossing the repo boundary, so ticking it once the fix has landed is the human's own act by hand or
the line keeps showing up — *"honest either way: the line says still not fixed, which is true."* **And the
`promote` route gets the identical answer**: promoting a `FRICTION` flag mints its node **here**, in a
`graph-agent` session, never on the graph that raised it.

Four alternatives set aside: the **strict reading** of node 28, faithful to its sentence and set aside because
it prices the cheap disposition at the cost of charting an effort; a third disposition **`carried`**, rejected
outright as *"the evaporation this whole node exists to prevent"*; **the foreign manager writing the node into
this repo directly**, rejected on node 11 coordinating nothing cross-repo and the machine possibly not being
the same one; and **no settlement rule at all**, rejected because an ordinary flag's settlement means the
judgement was accepted, and accepting a friction report is not discharging it.

**The manager put a fifth note to the human alongside this question, in two parts.** First, and load-bearing:
**does an outstanding `FRICTION` flag block the effort that raised it from closing?** [Done-ness and
termination](10-done-ness.md) makes closing require the human to have dealt with every flag, so if it does
block, the human must charter an effort in this repo in order to close a work project — which is the coercion
this recommendation exists to avoid, arriving by the other door. If it does not, done-ness needs to say so
explicitly. Second, cheaper: **the pointer only runs reliably one way.** A flag cannot point at the node it
produced — wrong repo, wrong time, and often no node yet — but the node minted here can always name the
foreign flag it came from, being written afterwards by the party holding the carried item. That is the same
discipline as node 28's, reversed, and it puts the record on the side that will still be live.

**A5** — the human, `verbatim`: *"friction will be used to add custom instruction for the task if nessesary and
then I will take fraction flags and try to improve the workflow so that it doesn't happen often. The effort, if
not in this project can't fix the skill. The effort in another project will never fix the skill"*.

The first substantive answer on this node rather than an assent to an option, so no option is quoted beside it
and **the manager did not mark it against the recommendation either way**. Three things in it that the question
did not ask about, recorded as the manager's reading and not as theirs: it names an **immediate local response**
— a custom instruction for the task — which is neither settling nor a node and which the five questions never
reached; it fixes the **harvest's purpose** as reducing how often friction happens rather than fixing items one
by one; and it states as fact, twice, that an effort outside this project **cannot and will never** fix the
skill. Whether that endorses, modifies or displaces the two dispositions the question offered is not something
the manager can establish from the words, so it was carried to the worker unresolved and unmarked.

**Q6** — *the worker's words:* When friction blocks a node on a foreign effort, whose instruction is the local
workaround and where does it live?

**Why it asked rather than inferred**, in its words: *"where that instruction lives is constrained by a rule
already settled: node 28 forbids the manager departing from a shipped contract on its own authority. So I
cannot infer this one, and a guess here would be the manager inventing the licence it is forbidden to
invent."*

**What it read the human's answer as settling**, put up to be contradicted rather than confirmed: that a
foreign effort never fixes the skill, *"said twice, and I am treating it as fixed, not as emphasis"*; that
therefore nothing on a foreign effort may be made to wait on the skill being fixed — no acceptance condition,
no closing condition — since such an effort could never close, which makes the local instruction *"the only
route past blocking friction rather than one option among several"*, and reads *"if nessesary"* as *if it
blocks*; that the harvest is the human's, in this project, in aggregate, aimed at frequency, which
*"retroactively justifies having no batch trigger — you need several items before a pattern is visible"*; and
that its two dispositions survive renamed, a `FRICTION` flag being either settled as **not worth carrying** or
left **outstanding**, meaning carried, with none ever settled as fixed on the effort that raised it — named as
*"the one part of my last recommendation your answer neither took nor rejected."*

It recommended the instruction is **the human's, carried**, living in two places by how often it is needed:
**once**, as the human's carried direction in that one spawn; **more than once**, as a line in that effort's
**ground rules** in `map.md`'s `## Notes`. Why not the manager's: [Whether a spawn may override a shipped
worker contract](28-spawn-overriding-a-contract.md) settled that a spawn may not depart from a shipped contract
on the manager's authority, and *"a custom instruction that works around a defect in a shipped contract is
exactly such a departure"* — so the sequence is the one already designed, the manager raises, the human's
answer supplies the licence, and it travels as their words. Why the ground rules: the block already exists, is
optional prose, is declared per effort, and is a pointer every worker already receives, so a recurring
instruction costs one paragraph and no new file — and *"promoting an instruction from one-attempt to
whole-effort is reducing how often the friction happens, one repo at a time, while the aggregate harvest
reduces it everywhere."*

**And the half the human's answer forced it to state.** Node 28's rule is *two outputs, always both* — a
licence for the attempt and a node for the permanent fix — and in a foreign repo the second is impossible by
the human's own words. So there *"the `FRICTION` flag **takes the node's place**: raise, licence, flag, and the
flag is what the rule's second output degrades to when the repo cannot hold the fix."* Node 28's measured
failure was a licence recorded with nothing behind it, and this keeps something behind it.

Four alternatives set aside: **the manager writing the instruction itself and flagging it**, cheapest and
forbidden by node 28 on its own measured evidence; **the instruction living only on the node it was needed
for**, set aside because a recurring friction then costs a raise every time, *"which is the frequency cost you
named, paid one node at a time"*; **straight into the ground rules the first time**, simpler by one step and
set aside because the first occurrence is also when one learns whether it recurs, and a standing rule from one
instance is the machinery-for-predicted-needs this map prefers not to build; and **a per-repo override file
patching expedition locally**, rejected because *"it forks the skill per repo, and the fork is what would then
never come back."*

**The manager put a sixth note to the human alongside this question: the ground rules do not reach the
checker, and the checker is a measured source of friction.** `expedition-checker/SKILL.md` says under
`## What you are given`: *"Four things, in the spawn"* — the acceptance condition as text, the bar, the work
paths, and the name of the work. It never reads `map.md`, by design, because a pointer into the graph would
unblind it, which [Subagent context contract](12-subagent-context-contract.md) fixed as the one worker whose
payload cannot be a pointer. So a standing instruction in an effort's ground rules reaches every worker except
the checker, and friction with the checker's contract is not hypothetical — [What the checker contract owes to
having been run](31-checker-contract-owes.md) is a whole node of it. On a foreign effort the recommended
mechanism therefore has no route to the blind agent, and the only thing that reaches it is the acceptance
condition, which is the spawning node's text rather than a standing rule.

**A6** — the human, `verbatim`: *"ok for recommended, fair point from the manager"*.

Taken against the recommendation it was offered, which was the worker's: **"It is your instruction, carried,
and it lives in two places by how often it is needed: once, as the human's carried direction in that one
spawn; more than once, as a line in that effort's ground rules in `map.md`'s `## Notes`."** No `DIVERGENCE`.

**The second clause is the first time a manager's note on this node was answered at all**, five having gone
unanswered before it, and it endorses the sixth: that an effort's ground rules reach every worker except the
blind checker, and that the checker's contract is a measured source of friction. It endorses the
**observation** and names no remedy, so what to do about it is the worker's to write or to ask.

## Annotation: both citations of the frequency claim are withdrawn, and both conclusions stand

*Filed by the manager from [The human rejects *most efforts never end*](86-most-efforts-never-end-rejected.md)'s
`INVALIDATIONS`, sites 6 and 7. Corrects two cited grounds rather than superseding the answer; the disposition is
flag `86.1`.*

**Site 6.** The answer says a `FRICTION` flag is raised where noticed *"because most efforts never close and the
closing report would then never fire."* The frequency is withdrawn. **The conclusion stands on this node's own other
wording**, three lines away: *"because a foreign effort may never close."* Node 86's worker recorded that this node
*"states its point both ways within twenty-two lines"*, and that the possibility form was the best evidence the
frequency was never carrying the argument.

**Site 7.** An alternative was set aside as *"legitimate under [Done-ness]'s *most efforts never close*"*. **That
citation is withdrawn.** The alternative was set aside on other grounds and stays set aside.

**And this node's deeper ground is not about closing at all**: a friction node on a foreign graph *"can never be
resolved there, the fix landing in `graph-agent` by node 11's policy"*. Untouched.
