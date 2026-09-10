# Nothing triggers the ten mechanical checks

Type: grilling
Status: claimed

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
