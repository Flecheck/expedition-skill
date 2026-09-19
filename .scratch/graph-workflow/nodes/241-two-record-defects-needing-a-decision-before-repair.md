# Two record defects the first run of the checks found, each needing a decision before it can be repaired

Type: grilling
Status: resolved

Blocked by: none

## Question

*Surfaced by [node 213](213-nothing-triggers-the-ten-mechanical-checks.md)'s worker, and pasted as it wrote
it. **Its acceptance condition below is that worker's own**, written in the same handover.*

**4. Two record defects the first run of the checks found, each needing a decision before it can be
worked**
Kind: grilling
Blockers: none
Question: Running the mechanical checks for the first time returned two failures whose repair is a
decision rather than work. (a) `nodes/207-the-checkers-raise-branch-fires-on-a-purely-additive-edit.md`
is `Status: superseded` and carries no `Superseded by:`, and no node in the record carries a
`Supersedes:` field — so either a replacement exists and both edges are missing, or the status is wrong.
(b) Node 150 is `resolved` and has three entry lines in `decisions.md`, all struck through and none
live — so either it owes a current line, or a resolved node may legitimately have none. Which is it in
each case?

**Acceptance condition: none, and none is owed** — this is a grilling node.

**What I could not write, and why**, stated rather than left out: I deliberately did not mint these as
implementation nodes. For 207 I do not know whether a replacement node exists, and naming one would be
authoring a supersession. For 150 the text of a replacement index line is a statement of what that node
decided, which is not a worker's to write. Both need the human before either can be work.

## The manager's note at filing

*Not a change to anything above.*

**This node was specified in a handover the manager left unfiled for a session**, and is minted late for that
reason rather than any other — flag `213.4` records the delay against the manager. Nothing in the text above
was re-authored on the way here; it is the worker's own, recovered verbatim from the session record.

## Annotation: one of the two defects is already repaired, the other still stands

*Filed by the manager, from the tree rather than from memory, on the day this node was minted.*

**(a) is discharged.** The condition names
`nodes/207-the-checkers-raise-branch-fires-on-a-purely-additive-edit.md` as `Status: superseded` with no
`Superseded by:` and no node anywhere carrying `Supersedes:`. **Both edges now exist**: node 207 carries
`Superseded by: 178`, and node 178 carries `Supersedes: 207`. The manager wrote both after node 213's worker made
its observation and before this node was minted — the same unfiled-handover delay flag `213.4` records.

**(b) still stands, exactly as described.** [Node 150](150-which-harness-route-creates-a-worktree.md) is
`Status: resolved` and **all three** of its lines in `decisions.md` are struck through, so it has **zero live index
lines**. That is a live failure of mechanical check 5 — *"Every `resolved` node has an `## Answer` and exactly one
line in `decisions.md`"* — and it is the failure this node exists to decide, because the repair is a choice between
unstriking one, writing a fourth, and something else again.

**So this node's subject is now one defect rather than two**, and the manager has neither narrowed its question nor
touched its wording: **the question is its author's**, and whoever answers it should know that half of it has
answered itself.

## Interview

### Attempt 1 — the question put to the human

*Pasted as the worker wrote it, in its own order and its own words. **No answer has arrived**; the payload is banked
here so that a death leaves the worker's work on disk rather than losing it. The attempt's routing key does not
survive the manager's session.*

**ABOUT:** Node 213's worker ran the ten mechanical checks for the first time and found two record defects whose
repair is a decision rather than work. Defect (a) — node 207's missing supersession edges — was repaired by the
manager before this node was minted, so one defect is left: node 150 is `Status: resolved` and has three lines in
`decisions.md`, every one of them struck through and none live. That is a live failure of mechanical check 5, and it
is being decided now because the repair is a choice between three incompatible routes and nobody may pick one on
your behalf.

**SO FAR:** I read my node file, `map.md` whole, `decisions.md` whole, `CONTEXT.md`, node 150's file whole, node
156, node 213's answer, and node 238's acceptance condition, and I swept every node file in the effort.

**What the three lines actually are.** Node 150 decided which harness route creates an implementation node's
worktree. Its worker wrote an index line, then reissued it, and later the route itself was superseded when you named
a fourth route — the manager calls `EnterWorktree` with a node-tied name and resets to `HEAD`. Each supersession
struck a line and none of them appended a replacement. So `decisions.md` now holds: the original line struck with
the node-175 note; the same original line struck again with a "superseded by the reissued line below" note; and the
reissued line struck with the node-175 note. Zero live.

**`decisions.md` states the rule it broke, in its own header**: *"A superseded node's line is struck through in
place and its replacement gets a new line of its own. Nothing is ever deleted or rewritten."* The striking half was
done three times and the replacement half was never done once. On that reading this is not a question about what
check 5 should permit — it is one half of the file's own procedure left undone.

**Node 150 is the only case in the whole effort.** I swept every `Status: resolved` node against `decisions.md`:
five have no live line, and four of those (103, 114, 116, 133) have no line at all and are already node 156's
subject, which is open. Node 150 is the only node with lines where all of them are struck, so whatever you decide
governs one node today and a shape that will recur every time a resolved node's answer is superseded in place.

**Node 150 does have an `## Answer`**, so check 5's other half is satisfied.

**Check 5's wording is already being repaired and is not in scope here.** Node 238 is open and its acceptance
condition, clause 4, already rewords check 5 to *"exactly one line in `decisions.md` that is not struck through,
struck-through lines being permitted in any number"*. Under that wording node 150 fails on zero rather than on
three, which is the same failure. I did not re-report it.

**Two small things I settled myself**, coming back as flags. First, the duplicated pair of struck lines — the same
original line struck twice with two different notes — stays exactly as it is: never-delete forbids removing either,
both are struck, both point forward, and neither misleads. Second, both struck notes say the replacement content
lives in `map-implementation-rules.md`, which stopped being true when node 188 moved the landing section to
`map-manager-only.md`. I am leaving those notes alone, because struck text records what was true when it was written
and correcting it would be rewriting recorded text; the live line I recommend below carries the current location
instead. That matters, because node 175's worker said of exactly these lines that they are *"the one a later worker
greps"* and reported one live worker already misled by them.

I also found a separate defect I am reporting as a new node rather than asking about: `map.md` still says this route
question *"is open and is node 150"*, and names two routes when the one in force is a third.

**ASK:** Does node 150 owe a live line in `decisions.md` — so a resolved node whose answer was superseded in place
still owes exactly one unstruck line, and the fourth line below is appended with your approval of its text — or may
a resolved node legitimately have none, its struck lines and their forward pointers being enough?

**RECOMMENDED:** It owes a live line, and here is the text I propose:

`- [Which harness route creates an implementation node's worktree](nodes/150-which-harness-route-creates-a-worktree.md) — Revised to the human's route, now stated in [map-manager-only.md](map-manager-only.md): the manager calls `EnterWorktree` with a node-tied name, checks the base it landed on and resets.`

Three things it rests on. **The file's own header already demands it** — a struck line's replacement gets a new line
of its own, and that half was skipped three times, so this is finishing a procedure rather than adding a rule. **The
index is what every worker is fed**: your stated ground for keeping `decisions.md` read whole is that a fed entry is
taken into account naturally, and today node 150 is fed to nobody as anything that currently holds — a worker
reading the index cold sees three struck lines about a route that lost and learns nothing about the route that won.
**It costs no node.** Node 213's answer says a missing index line is the act's own bookkeeping, repaired inside the
act and not mentioned, and sends to you only a repair that would rewrite recorded text or reverse a status.
Appending does neither. The one thing that was not the manager's to decide is what the line *says*, and approving
the text above settles that — so the manager pastes it and nothing else has to happen.

If you want the wording different, say so and that is what gets written; I am not attached to my sentence, only to
there being one.

**ALTERNATIVES:**

- **A resolved node may legitimately have no live line**, check 5 being narrowed to permit it where every line is
  struck and each carries a forward pointer. Set aside: it makes a resolved decision invisible to the one file every
  worker reads whole, and it also forces node 238's already-written condition to change, since its clause 4 demands
  exactly one unstruck line.
- **Unstrike the third line**, the reissued one. Set aside: it is genuinely superseded on the route, so unstriking
  asserts something false, and `decisions.md`'s header forbids rewriting a line outright.
- **Mint a replacement node for 150, mark 150 `superseded` with a forward pointer, and give the replacement the live
  line.** This is the route the glossary prescribes for a node that holds work and turns out wrong, and it is the
  only option I did not dismiss easily. Set aside because the revision was already filed in place on node 150's own
  file and accepted there, node 199 settled that a node file archives its own subject, and it would mint a node for
  a decision you have already made and which is already written into `map-manager-only.md` — while reversing a
  status, which is precisely the case node 213 says must come to you anyway.

**The human's answer**, `verbatim`: *"for the question ok"*

It takes the worker's `RECOMMENDED`, which the worker wrote as: *"It owes a live line, and here is the text I
propose"*, followed by the proposed `decisions.md` line for node 150. The option quoted here is the worker's own
text and not the human's. No divergence: the answer agrees with the recommendation.

## Answer

*The worker's own text, pasted.*

**Node 150 owes a live line in `decisions.md`, and a resolved node whose answer was superseded in place still owes
exactly one line that is not struck through.** The human's words settling it, `verbatim`: *"for the question ok"*,
taking the recommendation as offered and approving the line's text as written. No divergence.

**The line, approved as written**, appended to `decisions.md` at the end of the list:

> `- [Which harness route creates an implementation node's worktree](nodes/150-which-harness-route-creates-a-worktree.md) — Revised to the human's route, now stated in [map-manager-only.md](map-manager-only.md): the manager calls `EnterWorktree` with a node-tied name, checks the base it landed on and resets.`

Appending it is the manager's bookkeeping and needs no node: under [Nothing triggers the ten mechanical
checks](213-nothing-triggers-the-ten-mechanical-checks.md) a missing index line is the act's own bookkeeping,
repaired inside the act and not mentioned, and only a repair that rewrites recorded text or reverses a status comes
to the human. Appending does neither. The one part that was never the manager's — what the line *says* — is what the
human approved here.

### Why it is owed rather than excused

**`decisions.md` states the rule it broke, in its own header:** *"A superseded node's line is struck through in
place and its replacement gets a new line of its own. Nothing is ever deleted or rewritten."* Node 150's line was
struck three times and its replacement was never appended once. This is one half of the file's own procedure left
undone, not a question about what a check should tolerate.

**The index is what every worker is fed.** The ground for keeping `decisions.md` read whole, fixed at [What to do
about the record's token cost](129-what-to-do-about-the-records-token-cost.md), is that a fed entry is taken into
account naturally. Until this line is appended, node 150 is fed to nobody as anything that currently holds: a worker
reading the index cold sees three struck lines about a route that lost and learns nothing about the route in force.

**The line carries the current location deliberately.** [What the harness worktree cycle does to the manager's
writable region](175-what-the-worktree-cycle-does-to-the-sandbox.md)'s worker said of these exact lines that they
are *"the one a later worker greps"*, and reported a live worker already misled by them. A greping worker now finds
a live line beside the struck ones and is sent to the file that holds the route today.

### The scope of the failure, re-derived rather than taken from the question

Every `Status: resolved` node in the effort was swept against `decisions.md`. **Five have no live line.** Four of
them — 103, 114, 116 and 133 — have no line at all and are already the subject of [Four resolved nodes have no line
in the effort's index of decisions](156-four-resolved-nodes-have-no-index-line.md), which is open. **Node 150 is the
only node in the effort whose lines all exist and are all struck**, so the rule above governs one node today and a
shape that recurs whenever a resolved node's answer is superseded in place.

Node 150 does have an `## Answer`, so check 5's other half was never in question.

### What was set aside

- **Narrowing check 5 to permit zero live lines** where every line is struck and each carries a forward pointer. It
  makes a resolved decision invisible to the one file every worker reads whole, and it would force [Add each check
  to the procedure that can falsify it](238-add-each-check-to-the-procedure-that-can-falsify-it.md)'s
  already-written condition to change, its clause 4 demanding exactly one unstruck line.
- **Unstriking the reissued line.** It is genuinely superseded on the route, so unstriking asserts something false,
  and the file's header forbids rewriting a line outright.
- **Minting a replacement node for 150 and marking 150 `superseded`.** This is the route the glossary prescribes for
  a node that holds work and turns out wrong, and it was the only alternative that was not easy to dismiss. Set
  aside because the revision was already filed in place on node 150's own file and accepted there; because [Whether
  an acceptance condition is a rule statement or a record](199-is-an-acceptance-condition-a-rule-or-a-record.md)
  settled that a node file archives its own subject; and because it would mint a node for a decision the human has
  already made and which is already written into `map-manager-only.md`, while reversing a status — the case node 213
  says must come to the human anyway.

### Defect (a) needed no decision

The node's other defect — node 207 `Status: superseded` with no `Superseded by:` and no `Supersedes:` anywhere — was
discharged by the manager before this node was minted, both edges now existing between nodes 207 and 178. Confirmed,
not re-verified from scratch: the manager's annotation at filing states it from the tree, and nothing in this node's
work touched it.

## Flags

`241.1` `ASSUMPTION` — **The duplicated pair of struck lines in `decisions.md` stays exactly as it is.** Node 150's
original index line appears struck twice, once carrying the node-175 supersession note and once carrying a
*"superseded by the worker's reissued index line, immediately below"* note — the same sentence recorded twice with
two different accounts of what replaced it. I settled this rather than asking. Never-delete forbids removing either;
both are struck; both point forward; and the live line this node adds is what a reader now finds. Correcting it
would be rewriting recorded text for no gain to any reader.

`241.2` `ASSUMPTION` — **The two struck notes naming `map-implementation-rules.md` as where the replacement route
lives are left uncorrected.** That file held it when node 175's worker wrote the note; [Move the landing section out
of the file an implementation worker reads](188-move-the-landing-section-out-of-the-workers-file.md) moved it to
`map-manager-only.md` afterwards, so the pointer inside struck text now resolves to a file that no longer holds the
route. I settled this rather than asking, on the ground that struck text records what was true when it was written
and correcting it would be rewriting recorded text — which node 213's answer sends to the human. The misleading this
creates is real and documented, so I neutralised it the other way: the live line approved in the answer names
`map-manager-only.md`, which is what a greping worker now finds.

## Retrospective

*This effort's own standing instruction, carried in the spawn and shipped nowhere. Pasted as the worker wrote it.*

**1. What I had to hunt for.**

- *Whether node 150 was the only instance of this defect.* Nothing states it. I derived it by sweeping every `Status: resolved` node file against `decisions.md` in one shell loop. I looked first in the node file and in `decisions.md`, neither of which answers it. This was the single most load-bearing fact in the answer and the cheapest to compute — about one command.
- *Why the three lines were struck, and in what order.* `decisions.md` shows three strikes and two different supersession notes but not the sequence that produced them. Reconstructible only from node 150's own 497-line file, whose `## Revision` section at the very end is where the route's supersession actually lives. I read the whole file to find it.
- *Where the replacement route content lives now.* Both struck notes say `map-implementation-rules.md`. I looked there first and found nothing; it is in `map-manager-only.md`, moved by node 188. Found by grepping `EnterWorktree` across the three map files. This cost two searches and became a flag.
- *Check 5's exact wording, and whether it was already being repaired.* I looked in `map.md` first, which does not hold the checks. It is at `.claude/skills/expedition/graph-conventions.md:487` and `nodes/13-graph-file-format.md:180`, and its repair is already specified in node 238's condition. One grep for `exactly one line in` found all of it, including the node-156 precedent, in one call.

**2. What arrived that this node did not need.**

- *From the spawn:* the note that a second grilling node runs beside me and that questions are relayed one at a time bore on nothing — I end my turn when a payload is ready either way. The note naming the two implementation nodes in flight was useful once, accidentally, when I wanted to know whether node 238 was claimed; a spawn cannot know that in advance and I would keep it.
- *From the mandatory reads:* `map.md` is the largest thing in my context and I acted on three items in it — never-delete and its two boundaries, the existence of the `Change the map` procedure, and the retrospective questions. The standing preferences on concurrency, model heterogeneity, resume, token priority, the gate payload's diff command, the grilling-node target and the payload trigger bore on nothing here. **This is at least the second report of this item**: node 144's worker wrote in its own retrospective that *"`map.md`'s `## Notes` is about 5,000 words of which I acted on four items … while the standing preferences on concurrency, model heterogeneity, resume, token priority, worktree creation and one-question-at-a-time bore on nothing here"*. Two workers, different node kinds, the same six or seven bullets. `CONTEXT.md` I used four entries of — `Node`, `Resolve`, `Supersede`, `Revision` — out of 51; the landing-code and closing-an-effort sections and the five node-kind entries bore on nothing.
- *Where I went to a file for one fact and took the whole file:* **node 150, 497 lines, read whole for two facts** — what its answer currently stands for, and why its index lines were struck. Both live in two places: the `## Answer`'s opening paragraph and the final `## Revision` section, together about 60 lines. The ~250 lines of `## Interview` between them — two complete question texts, eight measurements, four manager notes on a contradiction about `EBUSY` — bore on nothing I decided. **The arrangement that would have avoided it:** a node file whose current standing position is findable without reading to the end. Today a revision filed in place lands as a new `##` section appended after the interview, so the newest and most authoritative text is the furthest from the top, and a reader cannot know whether the `## Answer` still holds without reading everything after it. A one-line pointer under the `## Answer` heading — *superseded on X at node NN, see `## Revision` below* — would make the whole middle skippable. `decisions.md` read whole is the one large read that earned its place: the sweep needed all of it.

**3. What would have made this node easier.**

- *The single highest-value thing in my context was the manager's annotation on my own node file*, which established from the tree that defect (a) was already repaired and that (b) still stood exactly as described. It removed half the node before I started and it was verifiable prose rather than a summary. Worth naming as a pattern: a node minted late is worth re-checking against the tree at minting time, and saying so on the file.
- *What the node file did not carry, and cheaply could have:* why node 150's lines were struck, and where the replacement content lives. Two sentences in the annotation would have saved the 497-line read and the wrong-file chase that became a flag. The manager had both facts — it wrote the annotation from the tree.
- *In the record:* nothing tells a reader where a node's current position lives once its answer has been revised in place. `decisions.md` is the natural place to look and, for node 150, was precisely the place that had been left silent — which is this node's own subject, so the gap is self-illustrating.

**4. What was stale, wrong, or contradicted something else.**

- **`map.md`'s worktree paragraph is stale three ways** — says node 150 is open, names two routes when a third is in force, and states a constraint the landed practice contradicts. Reported as new node 1. It is live text in the one file every worker reads cold, which is the worst place in the record for a stale line.
- **`decisions.md`'s two struck notes point at `map-implementation-rules.md`** for content node 188 moved to `map-manager-only.md`. Flagged and neutralised by the new live line, not corrected.
- **Check 5's pre-repair wording survives in two places**, `graph-conventions.md:487` and `nodes/13-graph-file-format.md:180`. Node 238 owns the first; the second is on `INVALIDATIONS`.
- **`decisions.md` holds the same original node-150 line struck twice**, with two different accounts of what superseded it. Flagged.
- **One low-confidence observation, reported as such:** `map-manager-only.md` says the worktree route was added beside the landing policy rather than rewritten into it *"because node 152 and node 144 hold conditions quoting that paragraph's exact phrases"*. Node 152's condition does quote them. I grepped node 144's condition and could not find any phrase from that paragraph in it — its quoted material is `.gitignore` and rules-file text. I did not chase this to the bottom, so it may be that node 144's condition once quoted it or that I searched too narrowly; recorded because a reader relying on that sentence to know which conditions constrain the paragraph would be over-constrained by it.

## The manager's disposal of the retrospective's record items

*Not the worker's text. Each item naming the record, and what the manager did with it.*

- **`map.md`'s stale worktree paragraph** → minted as [node 244](244-map-says-the-worktree-route-question-is-open.md).
- **Node 156's condition being weaker than this node's rule** → minted as [node 245](245-node-156s-condition-re-derives-a-weaker-property.md).
- **`map.md`'s `## Notes` read whole for three items, reported at least twice** → minted as [node 246](246-map-notes-mixes-what-a-worker-acts-on-with-what-a-manager-acts-on.md), under this effort's rule that a second report of a standing item mints a node. Two further reports of the same item arrived in the same session, from nodes 235 and 166; all four are quoted on node 246.
- **Node 13's copy of check 5's wording** → annotated onto node 13 rather than minted, node 238 already owning the shipped statement. The manager's reasoning is on that annotation.
- **A node file's current position not being findable without reading to the end** → **not minted, and this is why**: it restates the open fog item *"What never-delete costs the reader of a node file"* in `map-manager-only.md`, which already names the same cost and says what would settle it. The manager has added nothing to that item, an unresolved fog item not being a node.
- **`map-manager-only.md` saying node 144's condition quotes the worktree paragraph** → **not minted.** The worker reported it as low-confidence and did not chase it. The manager has not verified it either and is not minting a node on an unverified premise; it is recorded here so the next reader of that sentence knows it is doubted.
