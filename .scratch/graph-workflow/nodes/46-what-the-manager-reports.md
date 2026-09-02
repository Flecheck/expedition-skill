# What the manager reports to the human, in one place

Type: precondition
Status: resolved

## Question

Collect every duty the manager's report to the human owes, from each node that added one, into a single
statement of what that report contains. At least four are known and no file lists them:

- the line naming what a **cascade pass minted**, or that it found nothing — [Cascade pass
  mechanics](15-cascade-pass-mechanics.md), flagged there at `15.2`;
- the line naming **what waits behind the live question**, by node name and kind only — [What the manager works
  on next, and how the human redirects it](16-human-steering.md), flagged there at `16.4`;
- the **pick report**, naming the implementation being started and the open questions judged non-fatal — the
  same node;
- the three states **invisible in the graph files**, a node reading `claimed` like any other: which node awaits
  approval at a gate, whether a worker is blocked on a raise, and what is banked and waiting — the same node,
  inheriting them from [Git and code-landing policy](11-git-and-code-landing.md) and [When an AFK worker cannot
  proceed](23-worker-cannot-proceed.md).

Decides nothing and writes no product code: its output is the input to the manager's own skill.

Reported by [What the manager works on next, and how the human redirects it](16-human-steering.md)'s worker.
Its own framing of why this is a `precondition` and not the implementation itself: *"two of the duties come
from a node this worker did not read, so the enumeration cannot be written here — and an implementation node
whose condition cannot be written in full is not startable, by this node's own answer."*

So this node is the **first application of the readiness floor its own reporting node had just decided**, and
it is applied against that node itself. The floor: an implementation is startable when its acceptance condition
can be written in full, with nothing deferred to an open question.

**Blockers: none.** It reads resolved nodes and writes an enumeration; nothing it needs is open.

**Why it matters, in the reporting worker's words:** the pick report *"has grown duties from three different
nodes and nothing states its contents"*, which is the shape of the failure [What keeps the shipped files
consistent when a decision changes a term](29-shipped-file-consistency.md) exists because of — a list that was
correct about the files it knew. That node has now been recorded twice as recurring inside the graph's own
files rather than in the product.

## Answer

*Written by this node's worker on attempt 2, and pasted as it wrote it.*

**What was done.** Every duty on what the manager puts in front of the human, gathered from the whole node corpus
(01–103) and from the four shipped files that impose one, with each item traced to its source and its standing.
Coverage: nodes 01–60 from attempt 1's recovered scan, verified by spot-check (below); nodes 61–103 read in full this
attempt; plus `.claude/skills/expedition/SKILL.md`, `graph-conventions.md`, `CONTEXT.md`, and `map.md`'s Notes.
`flags.md` was left unread, per the contract — every flag cited below is read from its node.

**How the recovered material was treated.** Attempt 1's scan of nodes 01–60 was verified rather than trusted.
**Checked directly:** twelve quoted items against their files, each confirmed present, verbatim, under the heading
claimed — node 08's "told once"/"no path on which it answers anything"/"never infer whole-node scope", node 10's four
moves and "every sweep round appears in the report", node 11's uncommitted-code stop and commit-message rule, node
15's narration line, node 16's `16.4` and the three invisible states, node 20's "the diff is never rendered" and "no
acceptance condition in the payload", node 22's flag-ids instruction, node 23's pre-emption, node 26's flag-expansion
instruction, node 27's gate-payload consequence, node 34's stated gap, node 36's name-the-outcome practice, node 39's
fourth component, node 59's transcript rule. **Probed for false negatives:** ten of its "no duty found" verdicts (05,
18, 21, 37, 43, 44, 47, 48, 50, 52, 56, 60) by grepping each for manager→human language; every hit was worker→manager
reporting, so all ten hold. **Taken on trust:** the completeness of its per-node quoting within the ~35 nodes where it
*did* find duties — I confirmed each quoted item exists but did not re-read those nodes end to end looking for items
it omitted.

**The finding that reorganises the question.** There is no single report. There are **nine distinct forms** the
manager sends, each with its own duties, and one duty-bearer (flag settlement) that is not a form at all but rides
another. Node 46's `## Question` said "at least four" duties; node 75's duty 84 said "at least four … from three
nodes". Both are floors. The enumeration below holds **about ninety** items drawn from **thirty-one nodes and four
shipped files**.

---

### 1. The nine forms, and what each is called

| form | the name(s) the corpus uses | where it is defined |
| --- | --- | --- |
| **relayed question** | *relay payload*, *relayed question*, *question* (the return variant) | 08 `### The relay payload` |
| **the manager's own raise** | *the manager's raise*, *a blocking raise by the manager on its own behalf* | 28 `### The manager's raise…` |
| **gate payload** | *gate payload*, *the payload*, *the gate* | 20 `### What the manager raises` |
| **pick report** | *pick report*, *the report accompanying the pick*, *the report of a pick*, *the report that closes the node*, and — wrongly — *closing report* | 16 `### 3. The readiness floor` (first use) |
| **closing report** | *closing report*, ex-*completion report*, *the report that precedes a close* | 10 `### The completion report…` |
| **death notification** | *death notification* (16), and the unnamed *told once by node name* (08) | 08 `### When a subagent dies mid-question` |
| **narration at resolution** | *ordinary narration at resolution*, *one line rather than a channel* | 15 `### What it reports` |
| **the on-request answer** | unnamed — *"the third it answers on request"* | 16 `### 5. What the manager must be able to report` |
| **the reject one-liner** | unnamed — *"one line offering to keep"* | 20 `### The abandoned diff…`, 68 `### On reject…` |

**Flag settlement** is not a tenth form: it *rides* the human moment that already ends the node (16 `### 1. The
attention queue`) — a gate for an implementation node, a **pick report** for every other kind (99 `### The moment`).

---

### 2. Duties on every form

- **U1 — one short line at the end naming what is expected of them.** The human's standing instruction, `verbatim`:
  *"Also I want to add to the manager skill to always end with a short phrase that says what is expected of the user,
  like what you did now. So that can look at the last line and know what I need to look into. Create a node"* — node
  96 `## Question`; `map.md` `## Notes`. **In no shipped file.** Node 96 is `open`. The exemplar is a gate's own last
  line, `**Approve, correct, or reject.**` **Explicitly unsettled by node 96 itself:** whether a report that asks for
  nothing (pick, death, closing) ends with *nothing is expected of you* or with no such line; and whether the line
  names the node.
- **U2 — assembled from other people's text; the manager writes only separately-marked notes of its own.** 12 `### The
  manager is a scribe, not an author`; 20 `### The chronology is assembled, not summarized`; SKILL.md `### You write
  as a scribe`. *"Ordering pasted pieces is scribe work; rewriting them into a gloss is not."*
- **U3 — a manager note is capped at context the manager already holds.** It does not read code or run research to
  produce one. 08 `### The relay payload`; SKILL.md.
- **U4 — a note may name which question the manager thinks sharpest, and may never say what it thinks the answer is.**
  16 `### 6. Consequences`, flag `16.7`; SKILL.md.
- **U5 — exactly one question in front of the human; nothing displaces a live one; two tiers; tier 1 closed at exactly
  three (a gate, a worker's blocking raise, the manager's own raise).** Adding a fourth is the human's decision, never
  an inference. 16 `### 1. The attention queue`; SKILL.md `## What is in front of the human, and when`.
- **U6 — never render a diff into the conversation.** 20 `### What the manager raises` — and note this is **inferred,
  not instructed**, flagged on node 20: *"The human specified what the header carries and never addressed rendering."*
- **U7 — there is no path on which the manager answers anything.** 08 `### What the manager may never do`.
- **U8 — the human has read none of what the agent read.** Frame every question. 08 `### The relay payload`, on
  findings `F7`/`F8`.
- **U9 — refer to a node by name, never a bare id.** 24 finding 12.
- **U10 — the glossary's vocabulary exactly, `_Avoid_` lines included.** 14; 26; `CONTEXT.md`.
- **U11 — where the reply is a choice among named outcomes, the payload asks for the name.** 36 `### Gate — approve`,
  after node 33's gate arrived as *"you can continue"* and had to be read. The manager's words: *"please name one so I
  don't have to read it out of context like last time"*.
- **U12 — a flag reaching the human carries what was done, why, and the context needed to answer it, and answering
  never requires opening a file.** The human's binding instruction at node 26's gate, `verbatim`: *"Also for flags,
  when asking the user, please explain in more detail what was done and why and the context. Idealy I don't have to go
  into the files to find out what happened and how to respond"*. 26 / 20; SKILL.md `### A flag in a payload`.
- **U13 — a payload that omits a flag settles that flag silently, so every flag the node holds is in it.** 27
  `## Annotation: approving the node's end settles its flags`; `map.md`. Failed at node 64's gate — the human's
  correction, `verbatim`: *"you forgot to describe the flags."* Discharged at node 74's. Nil flags are stated
  explicitly too (71 `### Gate: approve`).
- **U14 — flags carry ids so each can be pointed at.** The human, `verbatim`: *"Maybe add ids to flag in the node,
  right now it is a bit hard to comment each one"* — 22.
- **U15 — the manager's own material is labelled as its own.** Recurring practice under headings of the form *"The
  manager's note at filing, not a change to the condition"* (64, 67, 70, 71, 73, 74, 81, 86, 89, 90). No node settles
  it; it is node 75 §Q2 class.
- **U16 — a fact the files can answer is not put to the human.** 69 flag `69.1`.
- **U17 — where a terse reply does not say which option it points at, record the reply and ask which.** The human,
  `verbatim`: *"If an anwser is not clear, yes ask again"* — 25 flag `25.3`.

---

### 3. Per-form duties

**3.1 Relayed question** — 08, 12, 16

- **R1.** Fixed payload: `NODE`, `ABOUT`, `SO FAR`, `ASK` (the worker's question verbatim), `RECOMMENDED`,
  `ALTERNATIVES`, optional `MANAGER NOTES`. 08 `### The relay payload` — *"This is the deliverable."*
- **R2.** `ABOUT` and `SO FAR` are written every time, the first included; the worker writes them, the manager adds
  its note and nothing else. 12 `### The handover`.
- **R3.** Names in one line whatever else is waiting — **by node name and kind only**, never restating the other
  question or its options; a `MANAGER NOTES` line. 16 `### 1. The attention queue`, flag `16.4`.
- **R4.** Downward: `HUMAN ANSWER` verbatim, `DIVERGENCE` where the answer contradicts the recommendation, `MANAGER
  NOTES` marked as the manager's. 08. *(Manager→worker; listed because `DIVERGENCE` is what stops a worker resolving
  as though it had won its point.)*
- **R5.** Extra material in a human's answer beyond the option travels to the worker rather than being read by the
  manager. 86 `### Attempt 1`.
- **R6.** The manager may correct a false premise before relaying a checker's question — done at 71, human-confirmed,
  and **in tension with U2**.

**3.2 The manager's own raise** — 28, 71, 74, 80, 81

- **M1.** The channel exists and is tier 1. *"Nothing had described that channel: everything the manager says to the
  human today is a relay, a gate, or a flag settlement."* 28, flag `28.5`.
- **M2.** Same block shape as a worker's raise — `ABOUT`, `SO FAR`, `ASK`, `RECOMMENDED`, `ALTERNATIVES`. 71
  `### Attempt 1`.
- **M3.** Attribution inside the raise: whose idea the recommendation is. 71 — *"This is not my invention — it is what
  the checker itself proposed."*
- **M4.** Where writing an artefact would require deciding an open question, the manager raises instead of writing.
  71; 16's readiness floor.
- **M5.** A known condition/work divergence is raised **before a check is spent**, naming the exact clause and the
  exact departure. 74 `### The human's ruling on the condition's two-file clause`.
- **M6.** The answer produces **two** outputs, always both: a licence for that one attempt, flagged; and a node for
  the permanent fix. 28; SKILL.md.
- **M7.** The manager may not grant a licence itself — the human's own words must be carried into the spawn. 74, 80.
- **M8.** Where a check needs a constraint the ground-rules block does not hold, that is a raise, not the manager's
  judgement. 29.
- **M9.** Where a condition cannot be written in full, what is missing goes to the human **before the node is
  claimed**. 35, 39; instances open at 87, 88, 89.

**3.3 Gate payload** — 20, 12, 11, 19, 22, 26, 27, 36, 38, 45, 64, 68, 71, 74, 76

- **G1.** Raised once the checker passes. **One exception:** a check that will not pass must still reach the human,
  raised on the failing tree with that stated in the first line. 20 `### The checker is started by the manager…`.
- **G2.** Contents, the human's own shorter list: the checker's runs laid end to end oldest first, each naming `PASS`,
  or `FAIL` and which of the two, or that it raised and issued no outcome; what the worker changed for each finding,
  in the worker's words; the flags the node holds; the node; the paths the worker **reported** touching, never
  inferred from `git status`; **where the work is and the command that shows its diff**; the proposed commit message
  with its `Node: <effort>/<NN>` trailer. 20 `### What the manager raises`; 12; 11; 76 correction round 1.
- **G3.** **The list is not closed** — a checker's `QUESTIONS:` and its `NOT COVERED:` parts ride it. 76 Run 1 finding
  5 and correction round 1; SKILL.md.
- **G4.** Two things stay out: the rendered diff (U6) and **the acceptance condition** — *"a human who has to check
  the condition themselves is doing the checker's work at the gate."* 20.
- **G5.** The diff-location item was **found by a hole between three intact nodes**, not gathered from any: the human,
  `verbatim`, *"what are the changes ? I don't see them in git ?"* — 68 annotation 1; 75's post-gather annotation. Its
  method limit is stated there: *"A gather over resolved nodes cannot find a duty that no resolved node states."*
- **G6.** Every flag in full, per U12/U13 — with what was done and why. 64 (failed), 74 (discharged).
- **G7.** Where the manager skipped a re-check, the payload says so rather than leaving it to be inferred. 71
  `### Correction round 1`.
- **G8.** An owed `NOT COVERED:` part is established **by the gate at the latest**, usually by the manager. 38, 45;
  SKILL.md.
- **G9.** Three outcomes and no fourth; approve → commit → resolve, correct → uncapped re-raise, reject → graph edit
  first, then clean. 20; SKILL.md.
- **G10.** On reject, **one line** offering to keep: *"discarding `<paths>` — say so now if you want the diff kept."*
  20 (flagged), 68.
- **G11.** A self-edit at its gate names which files it moved and which are left in the older form, and the manager
  carries that into every later spawn and re-check. 19; **unshipped** — node 41 clause 6 is `open`.
- **G12.** A flag already licensed at a raise is reported as **confirmed**, not newly discovered; and a flag settled
  as *reported and carried* is not presented as a defect repaired. 74.
- **G13.** What the approval did **not** settle is recorded so it is not read as settled. 76 `### Gate: approve` —
  agent judgement, no clause requires it.
- **G14.** A bar failure does not reach the human as a gate; the manager opens the correction round itself. 71.

**3.4 Pick report** — 16, 27, 39, 82, 93, 95, 99, 100, 103

- **P1.** **Owed the instant a node closes**, on every node of every kind. 99 `### The moment`; 27 `## Annotation: one
  of the grounds is false`.
- **P2.** It reports work **already under way** — the manager picks, spawns, then reports. 100 clauses 1 and 4;
  `map.md` `## Notes`. The human, `verbatim`: *"Also the manager should proactively start new nodes when one has
  finished."*
- **P3.** **It awaits no answer**, and the human's redirection is a correction after the fact rather than a permission
  waited for. 100 clause 2; 39 constraint 4; SKILL.md `### Picking the next node`. The manager **never asks which node
  to work** (16, human's `verbatim` *"Yes for pick and report"*).
- **P4.** Names the implementation being started and **the open questions judged non-fatal**. 16 `### 3. The readiness
  floor`.
- **P5.** Names a manager-written acceptance condition **as the manager's own**, and in a line or two what it demands.
  39 constraint 4; SKILL.md constraint 4.
- **P6.** Names a **condition amendment**: recorded beside the search that justified it, marked as the manager's own,
  carried as a flag, named in the pick report — or, where the amendment came after the claim, in that node's closing
  report instead. 82 Guard 2 and `### The two guards → Which report`; 95 clause 5.
- **P7.** Reports a **standing steering instruction** back in every pick it constrains. 16 `### 4. How the human
  overrides`; SKILL.md.
- **P8.** **Carries every flag the closing node holds, in the fuller form a gate payload uses** — what was decided,
  why, and the context needed to answer it, so answering never requires opening a file. 99 `### The duty that comes
  with it`; 103's condition. Node 99's worker, in as many words: *"Node 46 inherits it as a fifth duty to collate and
  does not get to re-decide it."*
- **P9.** Names **every** node the manager starts, so a node that ships a rule surfaces before it lands. 93 flag
  `93.4`.
- **P10.** States what bounds how much was started — the code-slot count, and the rule about the human's channel. 100
  clause 3. **Live and unsettled:** the human was uneasy at node 100's gate and supplied a third shape at its
  interview, `verbatim`: *"For 100, I would say by default 2 grilling nodes at once, and the rule is that when a node
  finishes, you start a new one (or new ones) to get back to the current amount (2 by default by the user can ask for
  more)"*. Flag `100.1` is open.
- **P11.** The settlement it carries **rides the human's next word whatever that word is about**; where the human
  never speaks again nothing settles and the flags reach the closing report; the manager never settles on its own
  judgement or on the passage of time. 99; flag `99.3` extends it across several pick reports.
- **P12. Open:** whether the pick report is a **fourth non-claimant** and the list of three should read four. Flag
  `100.2`, untouched by the human's reply.

**3.5 Closing report** — 10, 13, 16, 19, 27, 41, 86, 90, 102

- **C1.** A **delta scoped to what the human has not already seen**; a report replaying six months would be
  unreadable. 10.
- **C2.** Contents: **what landed**; **the supersession chains**; **the bar's current state**; **every outstanding
  flag** — read as `flags.md`'s unchecked lines, never reconstructed at report time; **what the sweep found**, and
  **every sweep round**. 10; `graph-conventions.md` `## The five files`; SKILL.md.
- **C3.** **The human's four moves on it: accept; settle a flag on the spot; promote, which creates a node; or reject
  what landed, which is a revision.** 10 `### The completion report…`; 75 duty 141. **This is in no shipped file** —
  the fifth duty filed onto this node at node 76's gate, found because `promote` is defined in the manager's contract
  and used nowhere in its body.
- **C4.** It ends the effort rather than taking a turn in it; not a claimant. 16.
- **C5.** It carries only the flags that never had a human moment. 27; SKILL.md. **Its scope is shrinking and node 102
  is `claimed` on it:** whether a `research` node's and an AFK `precondition` node's flags move to the pick report. If
  they do, the closing report's flag list falls to almost nothing.
- **C6.** A `FRICTION` flag is never settled as fixed on the effort that raised it — it is *refused* in place with the
  human's reason, or *outstanding*, carried and re-surfaced at that effort's close. 19; 41 clause 3; 86.
- **C7.** The manager reports that the conditions hold **and nothing more**; only the human closes. 10; `CONTEXT.md`
  **Closed**.
- **C8.** No frequency claim is made anywhere, in any wording; what stands is the conditional that a never-emptying
  frontier is a legitimate steady state rather than a stalled one — and the manager may not present a non-empty
  frontier to the human as failure. 86; 90 (`open`, the glossary still carries the rejected claim). The human,
  `verbatim`: *"For close 36, I disagree that most efforts never end."*
- **C9.** Twenty legacy flags have this as their only route to the human. 27 `### The residual`.

**3.6 Death notification and its siblings** — 08, 17, 16, 59

- **N1.** Told **once**, by node name: the agent for that node died, their answer is recorded and being replayed, and
  they will never see the same question twice. Awaits no answer; not a claimant. 08; 16; SKILL.md.
- **N2.** A **second** unfileable return gets the same single notice — the manager files what it can, leaves the node
  `open`, and tells the human once by node name. 17.
- **N3.** A **third** failure is not a crash to retry: it goes to the human as a question about the shape of the
  graph. 08; SKILL.md.
- **N4.** A run's state is reported from its transcript's size and record count, **never from the harness's summary
  line**. 59 `### Correction by the manager: a dead run is not an empty run`.

**3.7 Narration at resolution** — 06, 15

- **X1.** The manager names, in its ordinary narration at each resolution, **what the cascade pass minted, or that it
  found nothing**. 15 `### What it reports`, flag `15.2` — *"Settled by me, not asked."* **Absent from every shipped
  file**; node 87 is `open` on exactly this.
- **X2.** **Nothing reaches the human as an interrupt.** *"Its output is queued graph edits, never a human interrupt.
  Discovery is not resolution."* 06.
- **X3.** Only genuine conflicts reach a human, and they arrive **queued on a node**. 06.
- **X4.** A big decision the cascade surfaces is raised with the human **when that node is worked**, not at discovery.
  06.
- **X5.** A session about to supersede a node that is **itself a replacement** escalates to the human as a decision
  instead of revising again. 06, adopted on agent judgement. **In no shipped file** — see the new node below.
- **X6.** The pass raises no flag of its own. 15, flag `15.5`.

**3.8 The on-request answer** — 11, 16, 23

- **O1.** Three states are invisible in the graph files, a node reading `claimed` like any other: **which node awaits
  approval at a gate**, **whether a worker is blocked on a raise**, and **what is banked and waiting**. The first two
  the manager **volunteers**; the third it answers **on request**. 16 `### 5.`, inheriting from 11 and 23; SKILL.md.
- **O2.** It needs no new machinery — answered from `flags.md` and from `Status: open` with a non-empty
  `## Interview`. 16 flag `16.6`.
- **O3.** A blocking raise **pre-empts**: the manager stops filling the human's queue with grilling questions and
  asks. The human, `verbatim`: *"Block, keep the slot, the manager should priorise answering the worker instead of
  continuing working on grilling (ask the user to do it)"* — 23.

**3.9 Landing-adjacent duties that reach the human** — 11, 68

- **L1.** If the product tree holds uncommitted code the node did not write, the manager **stops and says so** rather
  than committing someone else's work under a node's name. 11.
- **L2.** The manager proposes the commit message; the human sees it before the commit happens. 11.

---

### 4. Where the shipped set already stands

`.claude/skills/expedition/SKILL.md` (node 76) already carries: U2–U8, U12, U13, R1–R4, M1, M6, M8, M9, G1–G4, G8,
G9, P3 (unnamed), P5, P7, C1, C2, C4, C5, C7, C8, N1, N3, O1. **It lists this very collation as the first of nine
duties nobody has settled.**

**Settled duties that are in no shipped file** — the gap this node exists to make visible:

1. **C3**, the human's four moves on the closing report (10 / 75 duty 141) — the fifth duty filed onto this node.
2. **X1**, the cascade narration line (15) — node 87 `open`.
3. **X5**, the second-supersession escalation (06) — nothing points at it.
4. **U1**, the closing line naming what is expected (96) — `open`, binding this effort by the map.
5. **G11**, the self-edit disclosure at a gate (19) — node 41 `open`.
6. **P1/P8**, the pick report as the settling moment and its flag duty (99) — node 103 `open`, `Blocked by: 102`.
7. **P2**, starts-rather-than-proposes (100) — `claimed`, uncommitted, at a correction round. `map.md`'s Notes already
   describe it as *"shipped into the manager's contract by [node 100]"*, which is ahead of the tree.
8. **P6**, the amendment-naming duty (82) — node 95 `open`.
9. The **pick report is not named anywhere in SKILL.md**; the section says only *"report the pick"*.

---

### 5. Naming — reported, not normalised

One collision runs through the corpus, and it has three faces:

- **`closing report`** names two different things: the once-per-effort report (`CONTEXT.md`, 10, 76, 96, 102) and a
  **per-node** close report (`map.md`, and node 95's clause 5). Flag `99.2` chose **pick report** for every per-node
  use, on the worker's own authority — *"`/naming` was not run and the human was not asked."* Node 103's condition
  repairs `map.md`; **it does not reach node 95's clause 5**, which still says *"named in that node's closing report
  instead."*
- **`report`** is refused by `CONTEXT.md`'s `Handover` entry — *"_Avoid_: report (the closing report owns that
  word)"* — while the shipped contract and the map now use **pick report** freely. Nobody has reconciled the
  reservation with the usage.
- The **relayed question** has no settled noun: *relay payload*, *relayed question*, *question*, *the return
  variant*. The **death notification** is named once (16) and left unnamed elsewhere (08: *"told once by node
  name"*). The **reject one-liner** and the **on-request answer** have no names at all.

---

### 6. Conflicts, reported unresolved

None of these is mine to settle.

1. **The scribe rule against the fuller form of a flag.** U2 forbids re-authoring; U12 requires the manager to write a
   third, expanded form for the human; node 30 would add a fourth, **stripped**, for the checker — opposites, both in
   the manager's hands. Node 20 treats the gate form as inside the scribe boundary; node 30 leaves it open. 75 §P 160;
   SKILL.md `## Where two of these pull against each other`.
2. **Arrival order against a waiting gate.** Tier 1 is ordered by arrival; a gate holds a code slot while it waits and
   a relayed question does not. Node 16's own annotation says *"This node still owes that."* 75 §P 162.
3. **Supplying what a condition omits, against authoring a whole one.** Node 33 forbids the first *on the ground that
   it makes the manager the author of the standard*; node 39 permits the second. Node 39's reconciliation — *"differ
   in visibility, not in authorship"* — is flag `39.1`, the worker's reading and not the human's. 75 §P 161.
4. **U1 against the reports that ask for nothing.** Node 96 requires every report to end naming what is expected; the
   pick report, the death notification and the closing report ask for nothing. Node 96 leaves this open by name.
5. **P10 against the map.** Node 100's clause 3 bounds starting a HITL node on the one-question rule; the map says two
   grilling nodes run at once. Flag `100.1` is live, the human is uneasy, and their answer supplies a third shape
   nobody has written down yet.
6. **P12** — whether the pick report makes the non-claimant list four. Flag `100.2`, unmentioned in the human's reply.
7. **C5 / node 102** — whether `research` and AFK `precondition` flags move to the pick report, and what that leaves
   `flags.md`'s stated purpose.
8. **Node 66** — a checker that takes a satisfiable reading of two clauses that cannot both hold hands the alternative
   back as a question; nothing says what the human must receive in order to overrule it, and *"a `PASS` under a
   reading is not the same object as a `PASS`."*
9. **Node 85** — whether the manager may ask the human what they changed in a claimed tree. It did not ask, on its own
   invented remedy; *"a diff would have cost the human nothing to describe."*
10. **Node 82 `### What this does not settle` against SKILL.md's unsettled duty 8** — nothing independent checks the
    manager's report of its own conduct; *"the party being judged and the party writing the judgement were the same,
    with no step in between."*
11. **Node 88** — a mechanical check that prints a known-false failure every run, which the manager told the human
    twice to ignore. *"A check that always reports one failure teaches its reader to skim the failures."* A
    presentation defect in a recurring report, `open`.
12. **`CONTEXT.md`'s `Closing report` entry against node 10 and SKILL.md.** The glossary says the report carries
    *"what was decided, what landed, and every flag still outstanding"* — three items where the settled list has six
    and is delta-scoped. Node 103 touches `CONTEXT.md`'s **Flag** entry only; nothing reaches this one.

### 7. Facts later nodes depend on

- The collation is organised **by form, not by source node**, because the corpus has nine forms and no single report.
  An implementation node writing from this must decide whether the shipped file states nine sections or one.
- **U1 (node 96), P1/P8 (node 103), P2 (node 100), P6 (node 95), C3, X1 (node 87) and X5 are the seven items that are
  settled-or-instructed and unshipped.** Anything writing the manager's report section must carry all seven or say
  which it left.
- **Node 102 is `claimed` and blocks node 103.** A shipped statement of the closing report's flag list cannot be final
  until 102 answers.
- **Node 100 is `claimed` at a correction round with an unanswered interview.** Its clause 3 wording, flag `100.1` and
  flag `100.2` are all live; the human's *"2 grilling nodes, top up when one finishes"* has reached the map but no
  shipped file.
- I checked the diagnostic node 46's annotation left open: **`revision` and `AFK / HITL` are, like `promote` and
  `cascade`, defined in `SKILL.md`'s `## Words used exactly` and used nowhere in its body.** `revision` does hide a
  duty — X5, node 06's second-supersession escalation. `AFK / HITL` appears to hide none on reporting; its conduct is
  carried by other entries.

> **The manager's note, filed with the answer and not a change to it.** Two of the states this answer reports as live
> resolved between the worker's last read and this filing, and the answer is left exactly as written rather than
> updated: **node 102 is now resolved** — its answer moves every kind's flags to the pick report, which settles item
> C5 and conflict 7 — and **node 100's correction round is complete and under checker run 2**, with flags `100.3` and
> `100.4` added since. The worker's own §7 predicted both as the things a later node must re-check. Node 46 is a
> precondition node, so what it hands forward is this text plus this note.

## Flags

*Each entry is the worker's own prose, pasted. The manager added the id, the marker and the state.*

`46.1` `ASSUMPTION` **settled** — **I organised the enumeration by report form rather than by source node, and read "the
manager's report" as the whole family of manager→human messages rather than one message.** Node 46's `## Question`
and node 75's duty 84 both speak of *"the report"* in the singular and list duties that in fact belong to four
different vehicles. Reading it as one message would have forced me either to merge duties that contradict each other
across forms — a gate's *never show the acceptance condition* against a pick report's *say what the manager's
condition demands* — or to drop the ones that did not fit. Nine forms is what the corpus actually holds; the
collation names them and files each duty under the one that imposed it. Whoever writes the shipped statement may
still choose to present it as one section.

`46.2` `ASSUMPTION` **settled** — **I treated shipped files as sources of duty alongside nodes, and included duties from nodes
that are `open` or `claimed`.** The spawn said each duty should trace to *"the node or shipped file that imposed
it"*, so `SKILL.md`, `graph-conventions.md`, `CONTEXT.md` and `map.md`'s Notes are cited as sources. I also included
duties whose node has not resolved — nodes 95, 96, 99–103 — because several landed today and a collation restricted
to resolved nodes would be the same confident incompleteness this node exists to prevent. Every such item is marked
with its standing, so nothing settled and nothing unsettled is presented as the other.

`46.3` `ASSUMPTION` **settled** — **The recovered scan of nodes 01–60 was verified by spot-check rather than re-derived.** I
confirmed twelve of its quoted items verbatim against their files and probed ten of its "no duty found" verdicts for
false negatives; all twenty-two held. What I did not do is re-read the ~35 nodes where it *did* find duties looking
for items it omitted, so a duty present in nodes 01–60 and missed by that scan would still be missing here. I judged
the check proportionate because the scan's twenty-two verified claims were exact, including headings and
struck-through markers, and because the spawn directed me to spot-check rather than re-run it.

## Annotation: a fifth duty for this list, found at node 76's gate

*Filed by the manager. Not a change to the question above, which already says at least four are known and no file
lists them — this is the fifth, found the same way.*

**The human's four moves on the closing report.** Duty 141 of [Gather the manager's accumulated
duties](75-gather-the-managers-duties.md), settled at [Done-ness and termination](10-done-ness.md): *"accept;
settle a flag on the spot; **promote**, which creates a node; or reject what landed, which is a revision."*

**It is in no shipped file.** [Write the first version of the manager's skill](76-write-the-manager-skill.md)
states what the closing report *contains* — what landed, the supersession chains, the state of the bar, every
outstanding flag, what the sweep found — and says nothing about what the human may do with it. That is correct
for that node: its clause 36 demanded the contents and nothing more.

**How it was found, which is the part worth keeping.** The blind checker reported that `promote` is defined under
`## Words used exactly` and used nowhere in the body, and offered it as an observation rather than a finding, the
term list being the acceptance condition's own. The human asked whether there was a plan to use it. **A defined
term with no conduct behind it is a reliable marker for a duty nobody wrote down** — the same question about
`cascade` produced [The manager's cascade duties are in neither
contract](87-managers-cascade-duties-have-no-contract.md) one message earlier.

**Two more terms have the same shape and are not filed anywhere yet**: `revision` and `AFK / HITL` each appear in
the manager's contract only inside other entries' definitions. Whether either hides a duty has not been checked.

## Annotation: attempt 1 died, and what it produced before it did

*Filed by the manager. Not a change to the question above.*

**Attempt 1 died** on a session limit rather than on anything about the node, having read the node and dispatched a
breadth scan across the node corpus. It is marked dead and replaced; the node keeps its number, its file and its
claim.

**What it produced before it died is recoverable and was not lost.** Its scan of nodes 01–60 returned to the manager
rather than to it — an enumeration of every duty on what the manager reports to the human across those sixty files,
each item quoted with its heading and its settled-or-flagged standing. The manager holds that text and carries it
into the replacement's spawn as recovered material, to be verified rather than trusted, and extended across nodes
61–103 which the scan never reached.

**Nothing of the human's was replayed**, this being an AFK node that had put nothing to them.

## Annotation: what this node's own question got wrong

*Filed by the manager from attempt 2's `INVALIDATIONS`, in the worker's own words. The `## Question` above is left
exactly as it was minted.*

> Node 46's own `## Question`, which says *"At least four are known and no file lists them."* Four was right as a
> floor and is now superseded by the enumeration above; the annotation's fifth duty is item C3 and is one of about
> ninety. Reported here because the manager files the answer, not me.

## Retrospective

*The worker's own text, pasted, handed back as the sixth handover part this effort asks for.*

**What I had to hunt for.**
*Nodes 100–103.* The spawn said nodes 61–103. `ls nodes/ | tail` showed 99 as the last file and I briefly concluded
100–103 did not exist, because `100-…` sorts before `11-…` alphabetically. Found by globbing `10[0-9]*`. Four of the
most report-relevant nodes in the corpus were one bad assumption from being missed entirely.
*The existing partial collation.* Node 75's `### H. How the manager reports to the human` is twelve of this node's
duties already gathered and cited, and it is roughly 60% of the settled half of my answer. Nothing in the spawn, the
node file or the recovered scan's node-75 entry names it. I found it by grepping node 75's headings after deciding on
my own to read that node because it was the largest file in the range. Had I split it out to a subagent like the rest,
I would have paid for the same work twice.
*The shipped state of each duty.* I looked first in `graph-conventions.md`, expecting procedures; the report duties
are in `SKILL.md`, which I reached second.

**What I read and did not use.** Node 75's sections K (code slot and worktree), L (cascade and sweep), M (acceptance
conditions) and O (housekeeping) — about 40% of what I read of that file, kept only for the two items in each that
turned out to be report duties. `wayfinder-divergences.md`, which contains no match for *report*, *human* or
*payload*. Most of `CONTEXT.md`, of which four entries mattered.

**What would have made this node easier.**
*In the spawn:* a single line saying the node corpus is 103 files and that 100–103 exist. And a pointer to node 75 §H
as the existing partial gather — the spawn told me what attempt 1 had produced but not what the corpus already held.
*In the node file:* its `## Question` lists four duties as *"at least four are known"*. Node 75, resolved before this
node was spawned, already listed twelve under one heading and cited them. A node file whose question was written
before its own best source existed makes a worker's first estimate of the job's size wrong by an order of magnitude.
*In the contract:* nothing blocked me. One observation rather than a request — the contract's `## What you read` names
three sources and says *"Do not trust any summary of them"*, and this node's whole method is reading a fourth kind of
thing (the corpus) and a fifth (the shipped files) that the spawn authorised. The contract handles that by deferring
to the spawn, which worked, but a precondition node whose work *is* reading the record is common enough that the
section could say so.

**What I read that was stale, wrong, or contradicted something else.** Six things, all reported above and none
repaired by me: `map.md` describing node 100's rule as shipped while the node is claimed and uncommitted;
`CONTEXT.md`'s **Closing report** entry three items short of the settled list; `CONTEXT.md`'s **Closed** entry still
carrying the frequency claim the human rejected (node 90 is open on it); `CONTEXT.md` reserving the word `report` to
the closing report while the shipped contract uses `pick report`; `graph-conventions.md`'s `### Settle a flag` still
resting on the ground node 99 falsified; and node 75's duty 84, whose *"from three nodes"* this node's own answer now
contradicts.

**The manager's note on the retrospective.** *Not a change to anything above.* The first of the six is the manager's
own text and **has been repaired**: `map.md`'s bullet now says node 100's work is being carried into the contract,
is under check, and has not landed, and it no longer states the superseded bound. The other five are other nodes'
work, four of them already minted. Two items under *what would have made this node easier* — a spawn that says how
large the corpus is, and a node file whose question predates its own best source — are the manager's defects rather
than any worker's, and join the promotions it owes off retrospectives.
