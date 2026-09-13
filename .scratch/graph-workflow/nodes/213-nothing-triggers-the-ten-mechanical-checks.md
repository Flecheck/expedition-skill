# Nothing triggers the ten mechanical checks

Type: grilling
Status: resolved

Blocked by: none

## Question

*Surfaced by [Nothing measures the record about itself](183-nothing-measures-the-record-about-itself.md)'s
worker, and pasted as it wrote it.*

> `graph-conventions.md` lists ten mechanical checks and the string *"Mechanical checks"*
>   appears nowhere else under `.claude/`; no worker contract and no part of the manager's contract names
>   a moment at which any of them runs. The cost is not hypothetical: check 3 covers a gap in node
>   numbering and one is live today — 202 node files spanning ids 01–203 with 187 absent. Check 10 is
>   already the reporting instrument this effort's retrospectives asked for six times, landed by node 136
>   and never fired. Node 183 settled the trigger for *measurements* — on demand, by whoever needs the
>   number — but checks 1–9 return verdicts rather than numbers, and a verdict nobody asks for is never
>   produced, so the same trigger cannot serve them. Who runs a verdict check, and when? The manager's
>   own contract already records that it holds no statement of what a complete report contains, which is
>   one candidate home.

**Blockers, in the worker's words:** none.

## Acceptance condition

**None, and none is owed.** This is a grilling node: what done means is the human's answer, and no
acceptance condition is written for one.

## The manager's note at filing

*Not a change to anything above.*

**Its cost is live rather than hypothetical.** Check 3 covers a gap in node numbering and node id 187 has no
file. The manager has separately established from the whole of git history that **id 187 never existed** — an id was
skipped rather than a node lost — which is exactly the verdict check 3 would have returned the day it happened, for
nothing, had anything run it.

**Check 10 is the instrument six retrospectives asked for.** It measures byte sizes and *"reports and never
fails"*, landed at node 136 and never fired. Node 183's answer covers it under the derivations; checks 1 to 9
return verdicts rather than numbers, which is why that answer does not reach them.

## Interview

### Attempt 1 — two questions, relayed unaltered

*The worker's payload, pasted as it wrote it. The manager relayed it and answered nothing.*

Its own framing above the payload, in its words:

> I have what I need. Ending my turn with one payload carrying two independent questions.

```
NODE:          Nothing triggers the ten mechanical checks

ABOUT:         The workflow's conventions file lists ten "mechanical checks" — cheap yes/no
               invariants over the graph's own files, like "every resolved node has an answer and
               exactly one line in the decisions index". Nothing in the workflow ever runs them.
               This node decides who runs one and at what moment. It is being decided now because
               a sister node settled the same question for *measurements* (numbers, derived by
               whoever needs one) and its answer explicitly does not reach these nine, which
               return verdicts rather than numbers — and a verdict nobody asks for is never
               produced.

SO FAR:        What I read: my node, the effort's map, the decisions index (searched, not read
               whole), the ten checks themselves, the conventions file's procedures, and the
               manager's contract.

               Four things I established rather than took on trust.

               (1) The checks are referenced nowhere. Across every shipped skill file, the string
               "echanical" occurs exactly once: the heading "## Mechanical checks" itself. No
               worker contract, no checker contract and no line of the manager's contract mentions
               them. The only two things that point at a check are two sentences *inside the same
               file*, and both are written as if the checks already run — "check 9 below reads that
               marker" and "check 1 below reports it". The file assumes an instrument that does
               not exist.

               (2) I re-derived the numbers my spawn gave me and two were wrong. The effort holds
               220 node files, not ~215, with ids 1–221, no duplicate, and 187 the only gap. The
               frontier is 104, which was right. (Derived today, and not to be relied on later.)

               (3) The structural finding, which nothing in the record states and which I think
               decides the node: the checks are, almost item for item, the *read-back of the
               procedures the workflow already has*. The conventions file lists eight numbered
               procedures — claim, resolve, supersede, rule out of scope, park, raise a flag,
               settle a flag, change the map — plus adding a node, and each one opens by listing
               every file it changes. Check 5 is exactly what "resolve" steps 1 and 3 must leave
               true. Check 2 is "supersede" steps 1 and 3. Check 6 is "raise a flag" and "settle
               a flag", both steps. Check 7 is already written into "claim" as a precondition.
               Check 3 is the "allocate the next unused number" line of adding a node. Seven of
               the nine verdict checks are falsifiable *only* by an act that already carries a
               numbered procedure. Nothing ever ran them because they were written as a separate
               audit list at the end of the file instead of as each procedure's last step — so
               they restate the procedures' own content in a place no procedure points at.

               (4) The two exceptions are informative. Checks 8 and 9 hang off the two graph
               writes that have *no* procedure at all — writing an interview attempt, and
               recording a checker's review round. Those are the two most frequent writes on the
               graph, and the procedures section claims to list every file that changes.

               What I settled on my own: that check 10 is out of scope here (it measures and never
               fails, and the sister node's answer already covers it); and that the cost is real
               but small — the one live instance, a missing node 187, was separately established
               to be an id skipped rather than a node lost, so it misled nobody.

Q1. What triggers a verdict check
ASK:           Who runs checks 1 to 9, and at what moment?
RECOMMENDED:   The act runs its own check. Each procedure gains a final numbered step naming the
               check its own writes can falsify, run by whoever performed the act, over the
               material that act just touched. That party is always the manager. No schedule, no
               new pass, no extra agent.
               What it rests on: (a) finding (3) above — for seven of the nine this is not new
               work, it is reading back the step list you just executed; (b) the cost is a re-read
               of what you just wrote rather than a scan of 220 files, and the scan form of these
               checks is precisely what the record has 12 false results against across seven
               sessions, plus a 13th last week — the whole-graph form is both unreliable and the
               one nobody ever ran; (c) the live 187 case is caught by this trigger and by no
               other, because the manager reads the directory listing to allocate the next id, so
               the gap is in front of its eyes at exactly that moment, for free; (d) it is the
               same repair two other nodes reached independently — move the act to the party
               already holding the material, and let repairs ride invoked work rather than a
               sweep.
               Two riders I would state plainly rather than hide: checks 8 and 9 need two
               procedures that do not exist yet, which I am reporting as separate work rather than
               inventing here; and the existing end-of-effort sweep keeps its job unchanged as the
               whole-graph backstop, gaining nothing new.
ALTERNATIVES:  The manager's report to you carries them. It is the candidate my node's own question
               names, and the manager's contract already records that it has no statement of what
               a complete report contains. Set aside: it defers the verdict past the act that
               caused it, and loads the one party measured as the first to run out of context — on
               the 187 case the verdict would have arrived weeks late or never.
               A read-only agent spawned to run all ten, periodically or at each code gate. Set
               aside: a spawn and a context rebuild each time, to re-derive what the manager was
               already holding.
               The sweep on an empty frontier. Set aside: the frontier is 104 and a long-running
               effort has no close, so this is indistinguishable from never.
               Nobody — delete checks 1 to 9 from the shipped file. An honest option: nine
               verdicts that have never run, and the only live instance was harmless. Set aside
               because those ten items are the only written statement of what each procedure must
               leave true, so deleting them deletes the procedures' post-conditions.
               A duty on every worker. Set aside: it charges every worker for verdicts almost none
               of them are positioned to produce, the falsifying acts all being the manager's.

---

Q2. What a failing check produces
ASK:           When a check comes back failed, what happens to that failure — repaired on the spot
               and never mentioned, recorded as a flag for you to settle later, or put in front of
               you?
RECOMMENDED:   Repaired inside the same act and not mentioned, where what failed is the act's own
               bookkeeping — a missing index line, a missing back-edge, a checkbox left unticked.
               It comes to you only where the repair would touch something *you* decided or
               something the never-delete rule protects: a numbering gap that means a node was
               genuinely lost rather than skipped, an index line that would have to be rewritten,
               a status that would have to be reversed.
               What it rests on: the manager is the graph's scribe, so finishing a write it had
               already half-made is inside that role rather than a judgement; you are the scarce
               resource and exactly one thing sits in front of you at a time; and the rule for
               when an agent must interrupt you is a contradiction it can name, which "I missed
               step 3" is not. No flag in either branch — a flag records a judgement an agent made
               on its own, and completing your own write is not one.
ALTERNATIVES:  Every failure becomes a flag. Set aside: the flag index is the capped record of
               agent judgements, and this would fill it with the manager's own typos.
               Every failure reaches you. Set aside: it spends your one channel on bookkeeping.
               Repaired silently in all cases, with no route to you at all. Set aside: that lets
               the manager quietly rewrite a record you decided, which is the exact thing the
               never-delete rule exists to stop.
               Repaired, plus one line in the report that closes that node. Closest to the
               recommendation and defensible; set aside only because it makes every act owe a
               report line whose ordinary content is "nothing happened".
```

**The answers: awaited.** Numbered `Q1.` and `Q2.` for this attempt, and the numbers are fixed for it.

**One thing the manager notes about its own spawn**: the spawn handed this worker *"roughly 216 node files and a
frontier near 104"*, marked dated and not authoritative, and told it to re-derive. It re-derived **220 node files,
ids 1–221 with 187 the only gap**, and the frontier at 104. **The hedge worked as node 183 said it would** — the
number was wrong and misled nobody, because it arrived marked as not to be relied on.

### The answers — `Q1.` and `Q2.`, both taken

**The human's words, `verbatim`.** Their message also carried evidence for a different node, which is filed there
and not here.

> There is an example for the PreCompact: https://github.com/mvara-ai/precompact-hook/blob/main/pre-compact.sh ,
> it seems that the output of the script is added after compaction. Q1 ok Q2 ok

**What each answers, quoted from the option its author wrote** — this node's own worker, not the manager:

- `Q1.` *"The act runs its own check. Each procedure gains a final numbered step naming the check its own writes can
  falsify, run by whoever performed the act, over the material that act just touched. That party is always the
  manager. No schedule, no new pass, no extra agent."*
- `Q2.` *"Repaired inside the same act and not mentioned, where what failed is the act's own bookkeeping… It comes
  to you only where the repair would touch something you decided or something the never-delete rule protects."*

**Not a divergence.** Both take the worker's own recommendation.

**The two riders its `Q1.` stated rather than hid travel with the answer**: checks 8 and 9 hang off the two graph
writes that have no procedure at all — writing an interview attempt, and recording a checker's review round — so
they need two procedures that do not exist yet, reported as separate work; and the end-of-effort sweep keeps its job
unchanged as the whole-graph backstop.


## The handover, filed late and pasted whole

*This node's worker handed back its five parts and its retrospective, and **the manager did not file them**. The
delay is the manager's alone and is recorded at flag `213.4` below. What follows is the worker's own text,
recovered verbatim from the session record and pasted under the headings the graph's format gives it — nothing
re-authored, nothing summarised.*

## Answer

*Pasted as the worker wrote it.*

*Pasted as the worker wrote it. Both questions were answered `ok` on the worker's own
recommendation, and neither is a divergence.*

**The act runs its own check.** Each procedure gains a final numbered step naming the checks its own
writes can make false, run by the party performing the act, over the material that act touched. That
party is always the manager, every one of these acts being its own. No schedule, no periodic pass, no
separate agent, and no new whole-graph run.

### Why nothing ever ran them, which is what decides the trigger

**The checks are the procedures' own post-conditions, filed away from the procedures.**
`graph-conventions.md` holds eight numbered procedures under `## Procedures` — claim, resolve,
supersede, rule out of scope, park, raise a flag, settle a flag, change the map — plus `## Adding a
node`, and the section opens *"Each lists every file that changes, in order."* Read against that list,
the ten checks are almost item for item the read-back of a step list that already exists:

- check 5 is what `### Resolve` steps 1 and 3 must leave true;
- check 2 is `### Supersede` steps 1 and 3;
- check 6 is `### Raise a flag` steps 1–2 and `### Settle a flag` steps 1–2;
- check 1 is `### Supersede` step 4, `### Rule out of scope`'s stated consequence, and `## Adding a
  node`'s second pass;
- check 7 is already written into `### Claim` as a precondition;
- check 3 is `## Adding a node`'s *"allocate the next unused `NN`"*;
- check 4 is the `Labels:` field written at `## Adding a node` and the vocabulary edited by
  `### Change the map`;
- check 10 is the `## Notes` item written by `### Change the map`.

**Seven of the nine verdict checks are falsifiable only by an act that already carries a numbered
procedure.** So the checks were never an audit that nothing scheduled; they were each procedure's last
step, written at the far end of the file where no procedure points at them. Across the whole of
`.claude/skills/`, the string `echanical` occurs exactly once — the heading `## Mechanical checks`
itself. No worker contract, no checker contract and no line of the manager's contract mentions them.
The only two things that reach for a check are two sentences inside that same file, and both are
written as though the checks already run: *"which is what check 9 below reads"*, and *"until then
check 1 below reports it"*. The file has been assuming an instrument that does not exist.

### The trigger, per act

| act | checks it runs |
| --- | --- |
| `### Claim` | 7 |
| `### Resolve` | 5, 9 |
| `### Supersede` | 1, 2 |
| `### Rule out of scope` | 1 |
| `### Park` | 8 |
| `### Raise a flag` | 6 |
| `### Settle a flag` | 6 |
| `### Change the map` | 4, 10 |
| `## Adding a node` | 1, 3, 4 |

**The cost is a re-read of what you just wrote, not a scan.** That distinction is the whole of why this
trigger is affordable where the audit form never was. The whole-graph form of these checks is what the
record has twelve false results against across seven sessions, plus a thirteenth at node 183 — and is
also the form nobody ever ran. Reading back the two files an act just touched needs no scan rules at
all.

**The live numbering gap is caught by this trigger and by no other.** The manager reads the node
directory to allocate the next id, so a gap or a collision is already in front of its eyes at exactly
that moment, for nothing.

### What a failing check produces

**Repaired inside the same act and not mentioned**, where what failed is that act's own bookkeeping — a
missing index line, a missing edge, a flag left unmarked. The manager is the graph's scribe, and
finishing a write it had already half-made is inside that role rather than a judgement, so **no flag is
raised either way**: a flag records a judgement an agent made on its own.

**It reaches the human** where the repair would change something the human decided, would rewrite or
remove text already recorded, or would reverse a status. Those are the cases where a silent repair is
the manager quietly editing a record that is not its to edit, which is what the never-delete rule
exists to stop.

### Two riders that travel with the trigger

**Checks 8 and 9 hang off the only two graph writes that have no procedure at all** — appending a
checker's run to `## Review`, and appending a relayed question or answer to `## Interview`. These are
among the most frequent writes on the graph, and `## Procedures` claims to list every file that
changes. Until those two subsections exist, checks 8 and 9 have no act to attach to. That is
[the two missing procedures](#) node below, and it is why the trigger lands on nine sections rather
than eleven.

**The whole-graph run keeps its job unchanged.** The sweep at an empty frontier remains available as
the one run not tied to an act, and gains nothing new. It is not the trigger: this effort has 103 open
nodes, and node 183 established that a long-running effort has no close, so attaching the checks there
would be indistinguishable from never.

**Check 10 is not displaced.** Node 183's answer and node 210's condition give the *derivation* — how
to compute the `## Notes` item sizes. This gives the *trigger* — the act that can change them. They are
complementary, and check 10 still reports and never fails.

### What running them once found

**Run on 2026-09-10, and these numbers are dated and not authoritative — re-derive before relying on
one.** The tree holds 222 node files, 221 distinct ids, max id 222; 113 resolved, 103 open, 4 claimed,
1 superseded.

- **Check 3 — FAIL, twice.** Id **187** has no file, separately established to be an id skipped rather
  than a node lost. And **id 198 is used twice**: `198-two-files-describe-the-rules-file-by-contents-
  node-188-removes.md`, and `198-two-shipped-descriptions-of-the-rules-file-are-stale.md`, the second
  untracked by git, carrying no title line, no `Type:` and no `Status:`, and holding nothing but a
  2,017-byte annotation filed from node 188's checker — which node 198's real file does not contain.
  **The manager wrote a checker's findings to a file that is not a node and is not in version control,
  and the annotation has reached nobody.** Nothing in the record references it.
- **Check 2 — FAIL.** `nodes/207-the-checkers-raise-branch-fires-on-a-purely-additive-edit.md` is
  `Status: superseded` and carries no `Superseded by:`, which the same file calls *"mandatory the moment
  it becomes `superseded`"*. No node anywhere carries a `Supersedes:` field, so both directions are
  absent.
- **Check 5 — FAIL, five times.** Nodes 103, 114, 116 and 133 are resolved with no entry line in
  `decisions.md` — which independently reproduces exactly the four that node 156 was minted for. The
  fifth is new: node **150** is resolved and has three entry lines, **all struck through and none
  live**.
- **Check 5's wording is itself falsified by this effort's never-delete rule.** *"Exactly one line in
  `decisions.md`"* cannot be satisfied by any node whose index line was superseded, since a superseded
  line is struck in place and stays. It must read *exactly one line not struck through*.
- **Check 1 — PASSes on its own terms**, no `Blocked by:` target being absent, superseded or
  out-of-scope. But **seven nodes carry a `Blocked by:` value that is not the declared bare form** —
  markdown links instead of numbers on node 109, and `none` followed by prose on nodes 129, 140, 146,
  171 and 201. Nothing checks a field's form, and this is the direct cause of false results in any
  scan.
- **Checks 4, 7 and 8 — PASS.** No node carries `Labels:` and this effort declares no vocabulary; no
  implementation node is claimed or resolved without an `## Acceptance condition`; no node has more than
  two `## Interview` attempt blocks.
- **Check 6 — 27 candidate mismatches, deliberately not asserted as defects.** 351 id'd lines in
  `flags.md` against 326 line-anchored `## Flags` entries. The largest cluster is flags `103.2`–`103.9`,
  which are present on node 103 but outside its `## Flags` section. I am not calling this a verdict,
  because the join needs the entry-anchoring rule that node 49 exists to supply and which the file does
  not state.

**Three of my own scans in this one session produced false results before I corrected them** — check 1
on the `Blocked by:` field form, check 5 on which line is an entry, check 6 on what a `## Flags` entry
looks like — and a fourth was avoided only because I inspected the heading forms first: a loose scan
reported four check-8 failures where the true answer is none. That is fresh, dated evidence for node
49, and it adds two rules its clause list does not have: that a `Blocked by:` value in this record is
not reliably the bare declared form, and that a `decisions.md` entry counts only when not struck
through. **It is also the strongest argument for this trigger**: a read-back over what an act just
touched needs none of those rules, and a whole-graph scan needs all of them.

INDEX LINE:    The act runs its own check: each procedure gains a final step naming the checks its
               writes can falsify; a failure is repaired inside the act, and reaches the human only
               where the repair would touch the record.

## Flags

*Pasted as the worker wrote it.*

ASSUMPTION — **I ran the ten checks live, which nothing asked for, and I bounded one result rather than
asserting it.** My node asked who runs a verdict check and when, not what a run would find. I ran them
anyway, because the answer's whole weight rests on whether these checks catch real things, and it was
cheap. Five checks returned failures and three of my own scans returned false results first. On check 6
I stopped at 27 candidate mismatches and refused to call them defects, because the join needs the
entry-anchoring rule node 49 exists to supply; a different worker would have reported 27 findings, or
none.
  *Index sentence:* Node 213's worker ran the ten mechanical checks for the first time in the effort's
  history, unasked, and chose to report check 6's 27 candidate mismatches as unverified rather than as
  defects because the rule the join needs is not written down.

ASSUMPTION — **I treated check 10 as already covered and attached a trigger to it anyway.** Node 183's
answer covers check 10 under the derivations and my node's own question set it aside, so I could have
left it out of the per-act table. I put it on `### Change the map` on the ground that a derivation and a
trigger are different things and neither supplies the other, and that omitting the one check that
reports rather than fails would leave the map's growth still unobserved at the moment it happens.
  *Index sentence:* Node 213's worker gave check 10 an act-attached trigger although node 183's answer
  already covers it as a derivation, judging that a derivation says how to compute a number and a
  trigger says when, and that neither supplies the other.

ASSUMPTION — **I split the work into four nodes rather than one or two, and added no blocking edge
between the two that edit the same file.** The two shipped-file nodes both edit `## Procedures` in
`graph-conventions.md`, which with two code slots could put two workers in one file — a hazard the
manager's own contract lists as unsettled. I made their conditions disjoint by region instead of
serialising them, because neither needs anything the other produces.
  *Index sentence:* Node 213's worker left two implementation nodes editing the same section of
  `graph-conventions.md` unblocked on each other, relying on conditions disjoint by file region rather
  than on a blocking edge, with the concurrent-edit hazard named for the manager to schedule around.

### The nodes this worker surfaced

*Pasted as the worker wrote it.*

**Four, and here is plainly which is which:** one carries the trigger the human approved; one writes the
two procedures the trigger cannot attach to until they exist; one repairs a record defect I can specify
completely; one names two record defects I cannot, and says why.

---

**1. Add each check to the procedure whose writes can make it false**
Kind: implementation
Blockers: none
Question: The ten mechanical checks in `graph-conventions.md` are the read-back of the procedures in
the same file, filed where no procedure points at them, and nothing has ever run one. Put each check on
the last step of the act that can make it false.

Acceptance condition:

&gt; The work is one edited file, `.claude/skills/expedition/graph-conventions.md`, and no other file may
&gt; be edited. The worker may not mark this node, resolve it, or write a line in `decisions.md` or
&gt; `flags.md`.
&gt;
&gt; That file holds a section headed `## Procedures` whose opening line reads *"Each lists every file that
&gt; changes, in order"*, containing subsections `### Claim`, `### Resolve`, `### Supersede`, `### Rule out
&gt; of scope`, `### Park`, `### Raise a flag`, `### Settle a flag` and `### Change the map`, each a
&gt; numbered list; a separate section headed `## Adding a node`; and a section headed `## Mechanical
&gt; checks` holding a numbered list of ten checks.
&gt;
&gt; Done means every one of the following is true of the finished tree.
&gt;
&gt; 1. Each of the nine sections below ends with one added numbered step — continuing that section's
&gt;    existing numbering where it has one — which names by number the checks it must run, and states that
&gt;    the party performing the act runs them itself, at that act, over the material that act touched. The
&gt;    sections and the numbers each must name:
&gt;    (a) `### Claim` — 7; (b) `### Resolve` — 5 and 9; (c) `### Supersede` — 1 and 2; (d) `### Rule out
&gt;    of scope` — 1; (e) `### Park` — 8; (f) `### Raise a flag` — 6; (g) `### Settle a flag` — 6;
&gt;    (h) `### Change the map` — 4 and 10; (i) `## Adding a node` — 1, 3 and 4.
&gt; 2. The `## Mechanical checks` section states, in wording the implementer chooses, all three of: that
&gt;    every check is run by the party performing the act that can make it false, at that act, over the
&gt;    material that act touched; that no schedule, no periodic pass and no separately spawned agent runs
&gt;    any of them; and that a whole-graph run of all ten remains available at an empty frontier and is the
&gt;    only run not tied to an act.
&gt; 3. That same section states what a failure produces: the party repairs it inside the same act and
&gt;    reports nothing, where what failed is that act's own bookkeeping — a missing index line, a missing
&gt;    edge, a flag left unmarked; and puts it to the human instead where the repair would change something
&gt;    the human decided, would rewrite or remove text already recorded, or would reverse a status. It
&gt;    states that no flag is raised in either case.
&gt; 4. Check 5 in the numbered list is worded so that it is satisfied by a node having exactly one line in
&gt;    `decisions.md` **that is not struck through**, struck-through lines being permitted in any number.
&gt;    Its wording before this work is *"Every `resolved` node has an `## Answer` and exactly one line in
&gt;    `decisions.md`"*, which no node whose earlier line was struck through and replaced can satisfy.
&gt; 5. The numbered list under `## Mechanical checks` still holds exactly ten items, numbered 1 to 10 in
&gt;    order. No check is added and none is removed, and clause 4 is the only change any item's text
&gt;    receives.
&gt; 6. No existing numbered step in any subsection under `## Procedures` is reworded, renumbered or
&gt;    removed, and `## Adding a node`'s existing prose is unchanged apart from the step clause 1 adds.
&gt; 7. No file other than `.claude/skills/expedition/graph-conventions.md` is modified, and no file under
&gt;    `.scratch/` is modified.
&gt; 8. The working tree meets the bar.

---

**2. Write the two graph writes that have no procedure**
Kind: implementation
Blockers: none
Question: `## Procedures` says each of its entries lists every file that changes, and two of the
graph's most frequent writes have no entry — appending a checker's run to a node's `## Review`, and
appending a relayed question or a human answer to a node's `## Interview`. Checks 8 and 9 hang off
exactly those two writes and so have no act to attach to. Write both procedures.

Acceptance condition:

&gt; The work is one edited file, `.claude/skills/expedition/graph-conventions.md`, and no other file may
&gt; be edited. The worker may not mark this node, resolve it, or write a line in `decisions.md` or
&gt; `flags.md`.
&gt;
&gt; That file holds a section headed `## Procedures` whose opening line reads *"Each lists every file that
&gt; changes, in order"*, containing eight subsections: `### Claim`, `### Resolve`, `### Supersede`,
&gt; `### Rule out of scope`, `### Park`, `### Raise a flag`, `### Settle a flag` and `### Change the map`.
&gt; The same file describes the shape of a node's `## Review` section and of its `## Interview` section
&gt; under their own headings, and no subsection of `## Procedures` covers the write into either.
&gt;
&gt; Done means every one of the following is true of the finished tree.
&gt;
&gt; 1. `## Procedures` gains exactly two new subsections and no others: one for appending a checker's run
&gt;    to a node's `## Review` section, and one for appending a relayed question or a human answer to a
&gt;    node's `## Interview` section. Each is a numbered list naming every file that changes, in order, in
&gt;    the form the eight existing subsections use.
&gt; 2. The `## Review` subsection ends with a numbered step naming check 9 in that file's `## Mechanical
&gt;    checks` list; the `## Interview` subsection ends with a numbered step naming check 8. Each says the
&gt;    party performing the act runs the named check itself, over the material that act touched.
&gt; 3. Neither new subsection restates the shape of `## Review` or of `## Interview`. Where a shape is
&gt;    needed, the subsection cites the section of the same file that holds it, by that section's heading.
&gt; 4. No existing subsection under `## Procedures` is reworded, renumbered or removed, and no item in the
&gt;    numbered list under `## Mechanical checks` is added, removed or changed.
&gt; 5. No file other than `.claude/skills/expedition/graph-conventions.md` is modified, and no file under
&gt;    `.scratch/` is modified.
&gt; 6. The working tree meets the bar.

---

**3. An annotation was written to a file that is not a node, under an id already in use**
Kind: implementation
Blockers: none
Question: A checker's findings on node 188 were filed to a new file sharing node 198's id, carrying no
node fields and untracked by git, and node 198's own file never received them. Put the annotation where
it belongs and leave one file per id.

Acceptance condition:

&gt; The work is confined to `.scratch/graph-workflow/nodes/`. The worker may not mark this node, resolve
&gt; it, or write a line in `decisions.md` or `flags.md`. **This work changes the effort's own record, so
&gt; the never-delete rule binds it: no text is removed, and text that moves moves verbatim, struck-through
&gt; text staying struck through.**
&gt;
&gt; Two files under `.scratch/graph-workflow/nodes/` begin with `198-`:
&gt; (A) `198-two-files-describe-the-rules-file-by-contents-node-188-removes.md`, which has a title line, a
&gt; `Type:` field, a `Status:` field, and sections `## Question`, `## Acceptance condition` and `## The
&gt; manager's note at filing`; and
&gt; (B) `198-two-shipped-descriptions-of-the-rules-file-are-stale.md`, which is untracked by git, has no
&gt; title line, no `Type:` field and no `Status:` field, and whose entire content is one section headed
&gt; `## Annotation: a third site, and a bounding set that is provably complete outside the record`.
&gt; File (A) does not contain that annotation.
&gt;
&gt; Done means every one of the following is true of the finished tree.
&gt;
&gt; 1. Exactly one file under `.scratch/graph-workflow/nodes/` has a name beginning `198-`, and it is file
&gt;    (A) under its existing name.
&gt; 2. Every byte of file (B)'s content, its heading included, appears in file (A), verbatim and
&gt;    unshortened, as a section of file (A) placed after its last existing section.
&gt; 3. File (B) no longer exists.
&gt; 4. File (A)'s title line, `Type:` field, `Status:` field, `## Question`, `## Acceptance condition` and
&gt;    `## The manager's note at filing` are byte-identical to what they were before this work.
&gt; 5. No file outside `.scratch/graph-workflow/nodes/` is modified, and no file under
&gt;    `.scratch/graph-workflow/nodes/` other than (A) and (B) is modified.
&gt; 6. The working tree meets the bar.

---

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

### What this work invalidates

*Pasted as the worker wrote it.*

**Check 5's own wording, in the shipped `graph-conventions.md`.** *"Exactly one line in
`decisions.md`"* is contradicted by this effort's never-delete rule, under which a superseded index
line is struck in place and stays. Any node whose line was ever superseded fails the check as written
while being perfectly correct. Node 150 is the live instance. New node 1's clause 4 repairs it.

**Node 29's part 3, which the human assented to: *"nothing is added to the mechanical checks and
nothing to any acceptance condition."*** My answer adds no check, and new node 1's clause 5 holds the
list at exactly ten. But two things are worth the manager's eye. First, that clause is **already
overtaken in fact and unmarked**: the list stood at eight when node 29 answered, a ninth arrived by node
45, and a tenth by nodes 136 and 139 — so the record carries a settled *nothing is added* beside two
additions. Second, new node 1 rewords check 5, and whether an amendment is an addition is a distinction
node 29 never had to draw. Neither is mine to settle.

**Nothing else.** In particular node 10's decision — *"the bar, the mechanical edge check, and the
human's own reading of the changes are the backstops"* — is **confirmed rather than contradicted**: it
assigned check 1 the role of backstop for cascade misses, and until now nothing ran it. And node 183's
answer is untouched: it settled the trigger for measurements and said in as many words that it does not
reach the verdict checks, which is why this node existed.

## The manager's own flag, against itself

`213.4` `MANAGER-WRONG` — **This node's handover sat unfiled for the length of the session.** Its worker handed
back all five parts and a retrospective; the manager filed nothing, left the node `claimed`, and carried on
starting and landing other nodes — eight of them. **The node was finished work the whole time**, so it also read as
an occupied grilling slot that the manager was counting against its own target. The handover was recovered verbatim
from the session record and filed above; nothing was lost, and nothing was re-authored. **What it cost was the four
nodes this worker specified going unminted while the manager minted others**, and one of those four is a repair to a
record defect the manager itself created.

*This flag is the manager's about the manager, and is outstanding.*
