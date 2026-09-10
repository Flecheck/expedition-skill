# Whether adding a standard is a case of `### Where the work moved one of them`

Type: grilling
Status: resolved
Supersedes: 207

Blocked by: none

## Question

*Surfaced by [Carry the record-node reading rule into the implementation-rules file](171-carry-the-record-node-reading-rule-into-the-rules-file.md)'s worker, and pasted as it wrote it.*

> The checker contract tells a checker that when an element of a standard it holds work
> against was added, removed or altered, it has nothing unmoved left to hold the rest of the
> work against and must raise. On this effort the standards file is itself frequently the
> work — nodes 140, 144, 169 and 171 all edit it — and every such node *adds* an element by
> construction. Does a pure addition, which leaves every pre-existing element unmoved, fall
> under that bullet, or does the bullet reach only a standard rewritten in place? If it
> reaches additions, every node that extends this file deadlocks its own check.

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**This is [flag `171.1`](171-carry-the-record-node-reading-rule-into-the-rules-file.md)'s subject**, and the two are
the halves of one thing: the flag records that the worker judged a check still possible and shipped, and this node is
where that judgement gets tested by the party that can settle it.

**It has already been met once, from the other side.** [Node 144](144-make-the-rules-file-stand-alone.md)'s checker
hit the same bullet, described it as *"a bright line"*, and **declined to cross it** — it proceeded and reported
rather than raising, on the ground that the bullet's own stated reason (*"nothing unmoved left to hold the rest of the
work against"*) did not obtain when seven of eight elements were unmoved. That checker asked in as many words whether
*"the contract wants a middle branch for a list that loses an entry"*. **The human saw that question at node 144's
gate and approved without answering it.** So two agents have now improvised past this bullet in the same direction,
neither with authority to.

**Node 171's own check is live as this is filed**, and the manager spawned it without pre-authorising anything, so a
raise on this bullet is a possible outcome rather than one that has been ruled out.

## Annotation: two further arrivals, and a duplicate node retired into this one

*Filed by the manager. Nothing above is changed.*

**The count is higher than this node's filing note says.** It recorded two agents improvising past the bullet; two
more did so in one session, both checkers, both on shipped files that the rules file also names as standards.

- **[Node 197](197-ship-what-a-file-of-the-map-admits.md)'s checker**, alongside its `PASS`, in its own words:
  *"Read literally, that forces a raise on any purely additive edit to a shipped file that the rules file also names
  as a standard — which is precisely what this node's condition demands, so the branch would make this class of work
  permanently uncheckable."* It declined the literal reading because the branch's own stated ground — *"you have
  nothing unmoved left to hold the rest of the work against"* — was false there.
- **[Node 204](204-demote-the-recorded-bar-commands-to-a-copy.md)'s checker** settled a reading of its condition's
  clause 6 and disclosed the stakes rather than raising: *"Under the other reading, the work would FAIL clause 6."*
- **[Node 200](200-collapse-the-rules-files-two-map-history-statements.md)'s checker** settled the same branch twice,
  once per run, each time on operative content, and passed.

~~**So four agents have now improvised past this bullet in the same direction, none with authority to.** Every one
reached the same answer, which is evidence about the bullet rather than about any of them.~~ **Struck by the manager
on this node's own worker's finding.** The count was wrong and one of the three arrivals above is misattributed:
**node 204's checker's remark that *"under the other reading, the work would FAIL clause 6"* is about a different
subject** — whether a shipped file may name the file a repo states its commands in — and not about this branch. The
manager conflated two disclosures from the same run. **The count as of this node's claiming was three**, and two
further checkers settled the branch while its worker was working: node 188's in a preamble before passing, and node
215's before failing the work on an unrelated clause. **The number and its instances are this node's answer to
state**, and the manager restates none of them here.

**A duplicate of this node was minted and has been retired into it.** [Node
207](207-the-checkers-raise-branch-fires-on-a-purely-additive-edit.md) was minted at node 197's gate for exactly
this question, the manager not having looked at the frontier for a node already holding it; it is marked superseded
with a forward pointer here and nothing was blocked on it.

**Its near neighbour pulls the other way and should be held with it.** [Node
214](214-a-condition-that-contradicts-a-standard-is-a-raise.md) exists because on the one case that mattered,
**nothing raised at all** — the human's words, `verbatim`: *"If both the checker and implementer knew it, I would
have expeted a raise at least."* This node asks whether the branch fires too often; that one asks why it did not
fire when it should. **Same clause, same contract, opposite failures.**

## Interview

### Attempt 1 — two questions, banked and not yet relayed

*The worker's payload, pasted as it wrote it. **It has not been put to the human**: node 213's two questions were
in front of them when this arrived, and the manager keeps one thing in front of them at a time. It is written here
so that a death loses nothing.*

```
NODE:          Whether adding a standard is a case of `### Where the work moved one of them`

ABOUT:         The checker contract has a branch that tells a checker to **stop and ask you** whenever the work it is checking has edited one of the documents that hold the rules the work is measured against. It is being decided now because four checkers have hit that branch, all four judged it wrong, and all four proceeded anyway without authority to — and roughly a quarter of this effort's landed work is edits to exactly such a document, so a fifth will hit it shortly.

SO FAR:
**What the branch says.** When a rule-document is among the changed files, the checker compares the rules on each side element by element. If the elements are identical and only the explanation changed, it carries on. If *"an element was added, removed or altered"*, then — in the contract's own words — *"you have nothing unmoved left to hold the rest of the work against, and no reading of the work can produce an outcome. Raise it."* A raise hands back **no outcome at all** and stops the check.

**Why that reason is false.** The branch treats any change to the rule-set as if it displaced the whole rule-set. It does not. Adding a rule leaves every pre-existing rule exactly where it was. Even removing one of forty leaves thirty-nine unmoved. The branch's stated ground — nothing unmoved left — is true only when the whole document is replaced or gone, and the branch fires far wider than that.

**Where it came from.** It was written from one real case (node 31): a checker whose work had edited the glossary's list of refused words. That checker invented the element-by-element test itself, found the refused set unchanged, and carried on. It then guessed at its own stopping condition — *"had the edit added or removed a refused word… I would have raised"* — and that guess was written into the contract as a rule. The guess generalised from "the set changed" to "nothing unmoved left", which does not follow.

**The four arrivals, each independent, all the same direction.** Node 144's checker called the branch *"a bright line"* and declined to cross it, on the ground that its stated reason did not hold when seven of eight elements were unmoved; it asked whether the contract *"wants a middle branch for a list that loses an entry"* — you saw that question at node 144's gate and approved without answering it. Node 197's checker: *"Read literally, that forces a raise on any purely additive edit to a shipped file that the rules file also names as a standard — which is precisely what this node's condition demands, so the branch would make this class of work permanently uncheckable."* Nodes 200 and 204's checkers settled the same branch and disclosed the stakes alongside a `PASS` rather than stopping. None had authority; all reached the same answer, which is evidence about the branch rather than about any of them.

**What I measured, rather than taking on trust.** 220 node files; 106 on the frontier; 37 of this effort's 161 commits (23%) touched a document that the rules file names as a rule the work is held against; 56 frontier nodes name one. So the literal branch would have stopped roughly one landed commit in four.

**What the cost of stopping is, stated by a checker.** A raise *"hands back no outcome and stops the check"* — so it withholds an outcome the checker was able to give on work nobody disputes.

**One thing I settled myself.** The contract's method compares *"the set of things the standard requires or refuses"* — the rules, not the file's text. So an edit to a rule-document moves a rule only where it changes that rule's own content; adding an unrelated paragraph to the glossary does not touch its list of refused words at all. All four checkers described the trigger as *"a file that is also a standard"*, which is wider than what the contract actually says. I am treating the narrower reading as correct and recommending it be said out loud, since four readers in a row got it wrong.

**Its opposite number.** Node 214 exists because on the one case that mattered, nothing stopped at all, and your instruction there was *"If both the checker and implementer knew it, I would have expeted a raise at least."* Same contract, same machinery, opposite failure. I do not think the two conflict: one test governs both — *is there anything unmoved left to hold the work against* — and the contract already says that test governs its other stopping grounds. This branch applies it too loosely; node 214's case is one the contract never applied it to.

---

Q1. What the branch actually reaches
ASK:           Should the branch be narrowed so it stops the check only where a rule the work must actually be judged by has itself been changed and no unchanged version of it survives — meaning a pure addition never stops a check, and changing or deleting one rule out of many stops the check only for that rule rather than for all of them?
RECOMMENDED:   Yes, in three parts. (a) **The rule is not the file**: editing a document that holds rules moves a rule only where the rule's own content changed. (b) **A rule the work itself added is work, not a rule** — every pre-existing rule is untouched, so the check survives; and holding work against a rule that same work authored is circular anyway, which is why the acceptance condition governs it instead. (c) **Deletion and alteration are handled one rule at a time**: the surviving rules still bind and the work is held against them; the checker stops only where the changed rule is one *this* work must be judged by and no unchanged statement of it remains. That last case is the one the branch was built for and it keeps firing — e.g. work that rewrites the rule *"prefer short, simple prose"* while itself being prose judged by that rule. This rests on the branch's own stated reason: it justifies stopping by *nothing unmoved left*, so it should fire exactly where that is true and nowhere else.
ALTERNATIVES:
- **Fix only the additive case**, leaving deletion and alteration to stop the check as today — smaller change, but it leaves the same false reason biting when one rule of forty is removed, where thirty-nine are plainly still standing.
- **Leave it as written and accept the stops** — makes this whole class of work permanently uncheckable and would have stopped ~23% of landed commits; it also means the four checkers were wrong and their `PASS`es were given without authority.
- **Exempt efforts whose subject is their own rules** — wrong shape: node 197's and 204's cases were ordinary shipped documents, and any repo whose coding standards live inside it hits this.
- **Delete the branch entirely** — loses the real case, where the work alters the very rule it must be judged by, which is the case the branch was written from.

---

Q2. What an agent does until the fix lands
ASK:           Until the contract is actually repaired, should a checker that hits this branch keep doing what the four did — carry on, give its outcome, and say plainly that it settled the branch and how — or must it stop and ask you every time, because the file on disk still says so?
RECOMMENDED:   Carry on and disclose. Four independent agents reached the same reading, the branch's stated reason is verifiably false in these cases, and stopping withholds an outcome the checker can give on work nobody disputes. The disclosure is the safeguard: it reaches you at the node's gate either way, without a stopped check. 56 frontier nodes name one of these documents, so the difference is not hypothetical.
ALTERNATIVES:
- **Require the stop until the file is fixed** — consistent with the file on disk winning and with your instruction at node 214, but pays one stopped check per node across a large share of the frontier for a question you are answering here.
- **Have the manager pre-authorise it in each spawn** — this is the manager departing from a shipped contract on its own authority, which node 28 settled that it may not do.
- **Say nothing and let each agent decide** — this is the status quo, and it is what produced four unauthorised improvisations and one retired duplicate node.
```

**The answers: not yet asked.** Numbered `Q1.` and `Q2.` for this attempt, and the numbers are fixed for it.

**Why its `Q2.` is the time-sensitive half.** It asks what a checker does *until* the contract is repaired, and
**two checks are live as this is filed** — node 188's and node 215's, both on work that edits a file the rules file
names as a standard. Whatever the human answers reaches those two only if it arrives before they finish; if it does
not, each will have settled the branch on its own reading, which is the fifth and sixth arrival.

### The answers — `Q1.` and `Q2.`, both taken

**The human's words, `verbatim`.**

> Q1 ok Q2 ok

*The manager read these as this node's two questions, node 178's being the only `Q1.`/`Q2.` pair outstanding when
they spoke — node 213's had been answered in an earlier message and what else stood in front of them was a gate.*

**What each answers, quoted from the option its author wrote** — this node's own worker, not the manager:

- `Q1.` *"Yes, in three parts. (a) **The rule is not the file**: editing a document that holds rules moves a rule
  only where the rule's own content changed. (b) **A rule the work itself added is work, not a rule** […] (c)
  **Deletion and alteration are handled one rule at a time**: the surviving rules still bind and the work is held
  against them; the checker stops only where the changed rule is one *this* work must be judged by and no unchanged
  statement of it remains."*
- `Q2.` *"Carry on and disclose."*

**Not a divergence.** Both take the worker's own recommendation.

**`Q2.` is a licence and the manager has recorded it as one.** It authorises every checker on this effort to depart
from a shipped contract's literal branch until the repair lands — wider than the one-attempt licence the manager's
contract describes, because the human granted it as standing rather than per attempt. It is written into `map.md`
as standing steering in the same turn, so that it reaches a checker by the route a ground rule does rather than by
the manager's memory. **The permanent fix is `Q1.`'s answer**, and the node that carries it is this node's worker's
to mint.

## Flags

*All three are the worker's own text, pasted. The ids are the manager's bookkeeping and nothing else.*

**All three are settled by the human's `ok` at this node's interview**, that being the human moment this node's
close reached — except that the second and third were settled *after* the reply, on the worker's own reading, and it
says so in each. The manager records that rather than smoothing it.

`178.1` **· settled** `ASSUMPTION` — **What the branch's method actually compares.** Before putting anything to the human I settled that the section's element-by-element comparison runs over what the standard requires or refuses, not over the text of the file holding it — so an edit to a standards-bearing file reaches the standard only where the standard's own content changes. I settled it from the section's own words (*"the set of things the standard requires or refuses"*) against the arrivals' uniform description of the trigger as *a file that is also a standard*. It is recorded as mine because it was made before the reply and became part (a) of a recommendation the human then took whole; it is the part every reader before me got wrong.

`178.2` **· settled** `ASSUMPTION` — **The arrival count, settled against four wrong statements of it.** The node file and the manager's notes recorded four agents improvising, then two further arrivals. Reading each cited agent's own text, I put the true count at three — nodes 144's and 197's checkers and node 171's worker — and established that nodes 188, 200, 204 and 215 either applied the identical-sets case correctly or never met the branch, and that one quotation attributed to node 204 concerns a different subject. I wrote the answer to three and named every instance so the number cannot drift again. Settled on my own reading after the human's reply, so never put to them.

`178.3` **· settled** `ASSUMPTION` — **That the repair is one node over one file.** I searched every shipped file and every record rule for restatements of the branch and found it in `.claude/skills/expedition-checker/SKILL.md` alone, at three sites, and confirmed the implementation contract carries no moved-standard text at all. I wrote a single acceptance condition on that basis. Had a fourth site existed outside that file, the condition's scope clause would be wrong.

## Answer

*Pasted as the worker wrote it, with the worker's own three corrections applied by it before filing.*

**No. A pure addition is not a case of `### Where the work moved one of them`, and the branch as written fires far wider than its own stated ground.** The human settled both questions this node put, `verbatim`: *"Q1 ok Q2 ok"* — taking the recommendation in each.

### The defect is the branch's own reason

The branch justifies stopping a check by a consequence: *"you have nothing unmoved left to hold the rest of the work against, and no reading of the work can produce an outcome."* That consequence holds only where the whole standard is displaced. Adding an element leaves every pre-existing element exactly where it was; removing one of forty leaves thirty-nine unmoved. So the trigger — *"an element was added, removed or altered"* — is wider than the ground it rests on, and that gap is where every agent that met the branch found itself.

**Where it came from.** The test was invented mid-check by [node 31](31-checker-contract-owes.md)'s checker, which compared the glossary's refused set, found it unchanged, and carried on. It then guessed at its own stopping condition — *"had the edit added or removed a refused word … that I would have raised rather than resolved"* — and the guess was written into the contract as a rule. The guess generalises from *the set changed* to *nothing unmoved left*, which does not follow. **The method that checker invented is sound and survives; only the threshold it guessed at is wrong.**

### What the branch now reaches, in three parts

1. **A standard is not the file that holds it.** An edit to a file containing a standard reaches that standard only where it changes what the standard itself requires or refuses. The comparison the section prescribes is over what the standard requires or refuses, never over the file's text, so adding an unrelated paragraph to a file that holds a standard does not touch the standard at all. **This part is stated because readers kept missing it**: the arrivals described the trigger as *a file that is also a standard*, which is wider than what the contract says, and independent readers converging on a wider reading than the text supports is a defect in the text. Node 144's checker had already drawn this distinction unaided — *"a standard the bar carries being one of the standards named, not the list itself"*.
2. **An element the work itself added is work, not a standard the work is held against.** Every pre-existing element is unmoved, so the check survives; and holding work against an element that same work introduced is circular. The added element is held against the acceptance condition, as work, like any other changed text. Node 197's checker reached this and added the reach test — *"the added element therefore does not reach the work"*.
3. **A removed or altered element is handled one element at a time.** The elements that did not move still bind and the work is held against them. The raise fires only where an element that moved is one *this* work must be held against and no unmoved statement of it survives. Where that reaches only part of what the checker must establish and the rest stands, the existing `NOT COVERED:` route applies instead. This is the *"middle branch for a list that loses an entry"* node 144's checker asked for in as many words and did not get.

**The branch still fires, and on the case it was built for**: work that rewrites the very rule it must itself be judged by — rewriting *"prefer short, simple prose"* while being prose held against it.

### How often it would have fired

Nothing in the record held this, so it was derived (2026-09-10; not authoritative). Of this effort's 161 commits, **20 touched `CONTEXT.md` or `graph-conventions.md`**, standards throughout; **37 touched one of those or `map-implementation-rules.md`**, a standards container since node 140 — 12% and 23%. There are 220 node files and 106 nodes on the frontier, 56 of which name such a document. Read literally, the branch would have stopped roughly one landed commit in four.

### The interim licence, and when it ends

Until the repair lands, **a checker that meets this branch carries on, gives its outcome, and discloses that it settled the branch and how.** Granted by the human at this node, `verbatim`: *"Q2 ok"*; it stands in `map.md` as standing steering in their words and the manager carries it in every checker's spawn while it stands. **It expires when this node's repair lands**, the narrowed branch then saying what the licence stood in for.

### The arrival count, settled with its instances

**Three agents met a branch that fired and proceeded anyway.** Five numbers have been offered on this — four, then three, then a fifth and sixth arrival — so the instances are named here and the number is not to be restated without them.

- **Node 144's checker.** An entry was removed from the standards list. It named the broad reading under which the branch fires, proceeded on the ground that its stated reason *"plainly does not obtain, since seven of eight elements are unmoved"*, and asked for a middle branch. **A genuine improvisation.**
- **Node 197's checker.** A pure addition to a standard that was itself the path under check, confirmed by SHA-256 that nothing was removed or altered. The branch fires literally; it proceeded. **A genuine improvisation, and decisive on its own.**
- **Node 171's worker** — an implementer, not a checker. It added operative content to the standards file, judged a check still possible because *"the added element is the work itself"*, and shipped. **A genuine improvisation.**

**Four further agents met the branch and correctly found it did not fire**, which is evidence *for* this answer: the contract's identical-sets case works, and only the added-removed-altered threshold is wrong. Node 31's checker (the origin, refused set unchanged). Node 188's checker, which removed 128 lines from the standards-bearing file and established by SHA-256 that the standards section was byte-identical, the removed section *"requires and refuses nothing of an implementation node's deliverable"* — **which is part (a) of this answer applied correctly before it was written.** Node 200's checker, identical sets, settled twice, once per run. Node 204's checker, no standard among the changed paths at all.

**Two agents were credited with arrivals they never made.** Node 215's checker never met the branch — its standards file was untouched and its outcome does not mention it. And node 204's quoted settlement of *"clause 6"* concerns a filename refusal in its own acceptance condition, not this branch.

### Where the repair goes

The branch is stated at **three sites in `.claude/skills/expedition-checker/SKILL.md` and in no other shipped file**. One node, one file: a repair to one site leaves the file contradicting itself, which is the defect node 222 is open for.

**What the worker reported its work invalidates**, pasted as it wrote it:

**Node 31's `## Answer`** states the rule this node narrows — *"An element added, removed or altered: raise"* — and is superseded on that point alone. Its method survives untouched: the operative-content-versus-rationale split, the element-by-element set comparison, the unwrapping instruction, and the identical-sets case. What falls is the threshold its checker guessed at, and the answer's own account shows it was a guess.
- **The shipped checker contract at three sites**, listed in the acceptance condition above. Live rule text, replaced by the repair node rather than struck, this being a file the workflow ships.
- **Flag `171.1` is discharged rather than overturned.** Its `ASSUMPTION` — *"the pre-existing standards are element-for-element unmoved and the added element is the work itself, so a check is still possible"* — is now the settled rule, in almost the words the answer uses. Its judgement is ratified and the work it shipped stands.
- **Node 144's checker's proceed-and-report is ratified, and its open question is answered.** It asked *"does the contract want a middle branch for a list that loses an entry, as against a standard whose content changed?"*; the answer is yes, and part (c) is that branch. The human saw that question at node 144's gate and approved without answering it, so this is where it gets answered. Its `PASS` stands.
- **Node 197's checker's refusal of the literal reading is ratified**, on the ground it gave.
- **Nodes 188, 200 and 204's settlements are confirmed, not overturned.** Each established that no operative element moved, or that no standard was among the changed paths, and proceeded correctly. Node 188's is the strongest: it removed 128 lines from the standards-bearing file and proved by SHA-256 that the standards themselves were byte-identical, which is part (a) of this answer applied before it existed.
- **Node 220's acceptance condition is wrong on the number it exists to protect.** It names **five** retrospective heading forms "as of 2026-09-09", written expressly so its worker would not undercount by searching one form. There are **six**: it misses node 70's `## Annotation: this node's retrospective claim is refined, and its own number has moved`, which landed in commit `8bb5d02` *before* node 212 resolved in `54d03b3` the same day. Node 212's answer carries the same five. A worker following that clause reproduces the bug the node exists to fix, so it needs amending before the node is claimed — and amending a condition is not mine.
- **Nothing about node 214 is invalidated.** The two do not conflict, for the reasons under `NEW NODES`.

## Retrospective

*Filed by the manager in the same edit that writes this node's answer, its flags and its line in
`decisions.md`. Pasted as the worker wrote it, in its reissued form — its first version's counts were provisional and
it replaced them with mechanically derived ones before filing.*

**The items I report, named under node 212's rule, with the count of earlier retrospectives carrying each.** The corpus is **35 filings under six heading forms**, 33 of them full four-question retrospectives. **Naming is absent from 34 of the 35**: node 212 is the only retrospective that carries names, so its four names are the whole registry and each stands at exactly one carrier. The duty has not landed in the map — [node 219](nodes/219-replace-the-mint-on-second-report-rule-in-the-map.md) is open and `map.md` still carries the old mint-on-second-report bullet with no naming clause — which is why three of my six items must mint a name for a heavily-reported item.

1. `stale-number-in-the-record` — **16 prior reports**; mine is the 17th, and it is the heaviest instance the item has had. My spawn's *"roughly 216 node files and a frontier near 104"* against a measured 220 and 106, hedged and re-derived. The heading-form count, given as six against node 212's five — six is right. And **the arrival count, stated to me four times and wrong every time**: four in the annotation, then two further arrivals mid-node, of which node 215 never met the branch and node 204's cited quotation is about a different subject. It is now three with every instance named, which is the only form that stops it drifting. The record also disagrees with itself on the unfiled-retrospective tally, node 183 saying eleven against node 221's and node 212's ten.
2. `one-rule-stated-at-several-sites` — **new name; 8 prior reports** (nodes 46, 102, 116, 117, 126, 144, 163, 175; sharpest is node 175's *"two live descriptions of the same decision in two files, and the index is the one a later worker greps"*). Mine is the 9th, and it is this node's central structural finding: the branch is stated three times in one shipped file, nothing says so, and a repair to one site leaves the file self-contradicting. **Eight reports and no name is why my acceptance condition had to enumerate the sites itself.**
3. `map-read-whole-for-a-few-items` — **new name; 26 prior reports**; mine is the 27th. **This is the largest standing item on the effort and it has no name.** Only nodes 46, 75, 98, 138, 139, 183 and 204 fail to report it. I used four of roughly thirty standing items; the worktree, `EnterWorktree`, sandbox-mount and landing material bore on nothing, this being a grilling node with no code path.
4. `rules-file-read-whole-for-one-section` — **new name; 6 prior reports** (nodes 126, 144, 163, 167, 200, 204); mine is the 7th, and **node 126 already self-numbered as the third**. I went to `map-implementation-rules.md` for `## What the work is held against` and took 197 lines, roughly 130 of which are worktree and sandbox forensics addressed to the manager. Node 167 reported it in my own words a session ago: *"Where I went for one fact and took the whole file."*
5. `nothing-pointed-me-at-it` — **new name, and the phrase is the corpus's own; 13 prior reports** (10 verbatim: nodes 59, 94, 116, 117, 122, 136, 138, 139, 144, 183; 3 as *"nothing indexes"*: 163, 167, 204). Mine is the 14th. My node file names four arrivals downstream of the clause and never links node 31, where the clause was authored and where its author's reasoning — the whole basis of the answer — is recorded.
6. `record-is-not-mechanically-scannable` — **4 prior reports** (nodes 114, 117, 163, 212), 5 counting node 136; mine is the 5th. **New count owed: six heading forms, not five** — and the instance above, that node 220's condition and node 212's answer both carry the stale five, so the two artifacts that exist to fix this item reproduce it.

**(1) What I had to hunt for.** The clause's origin, node 31 — found by grepping `decisions.md` for *"operative content"*, one hit; I looked first at my node file and then at the contract, neither of which points there. The frequency numbers, which nothing in the record holds and which are the most load-bearing facts in the payload; derived from `git log` over the three standards paths and from status greps. That the branch is restated at three sites, found only by grepping the file for its own phrases. And the arrival count, which took reading five checkers' outcomes because every stated version of it was wrong. **The highest-value line in my spawn** was the warning that the manager's summary of the raise mechanics could not be trusted and that I should read both contracts — it was right, and node 200's checker had caught the same gloss.

**(2) What arrived that this node did not need.** Items 3 and 4 above. Beyond them, my spawn's dated counts carried no information, arriving with an instruction to re-derive: a number I am told not to trust costs what one I am told nothing about costs. Everything else in the spawn bore on the work, the pointers to nodes 214 and 222 included — the second decided my disjointness claim.

**(3) What would have made this node easier.** In the node file: a link to node 31. In the record: something saying this branch appears three times in one file, which is item 2 at nine reports; and an index of which agents have settled a given clause, which is what four wrong arrival counts cost. In the spawn: nothing; it hedged where it should have and was right to. In the contract: nothing.

**(4) What I read that was stale, wrong, or contradicted something else.** The arrival count, four times over, reported under item 1 — including two arrivals offered mid-node that turned out to be a correct application of the branch and a checker that never met it. Node 212's and node 220's five heading forms, which are six. My spawn's node and frontier counts, low by four and two, hedged. And the convergent error in the record itself: every genuine arrival described the trigger as *a file that is also a standard*, where the contract's own method compares what a standard requires or refuses — three independent readers reading the text wider than written, which is why part (a) of the answer states it rather than leaving it implied.

## The manager's note at resolution

*Not a change to anything above.*

**This node corrected the manager four times on one number**, and the last two corrections landed after the manager
had already told the human the wrong figure twice. The arrival count was stated as four in a manager's annotation,
then as *"the fifth and sixth arrivals"* when node 188's and node 215's checks finished. **Both were wrong**: node
188's checker established by SHA-256 that the standards section was byte-identical and proceeded — which is this
answer's part (a) applied correctly before it was written — and node 215's checker never met the branch at all.
**The count is three, and this node's answer names every instance so it cannot drift again**, which is the form the
manager should have used from the start.

**One thing the manager acted on before this node resolved**, and it is this node's own subject seen from the
record side: node 207 carried `Status: superseded` with no `Superseded by:` field and node 178 carried no
`Supersedes:`. Both edges are now written, per the field forms in `graph-conventions.md`. That was caught by [node
213](213-nothing-triggers-the-ten-mechanical-checks.md)'s first-ever live run of the mechanical checks, not by this
node.
