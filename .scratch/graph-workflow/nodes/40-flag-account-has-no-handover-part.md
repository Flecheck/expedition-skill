# Nothing carries a flag's account of what produced it out of a worker

Type: implementation
Status: claimed
Blocked by: 392

## Question

This work lets the human see what the worker actually did, in the worker's own words, when they come back to a flag on a node that had an interview or a review. It does this by giving that account a route from the worker to the place where it is filed.

*The opening sentence above was written by [node 392](392-write-the-acceptance-conditions-for-the-five-kept-nodes.md)'s worker and filed by the manager on 2026-10-06.*

[`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md)'s `### Raise a flag`
procedure requires a **third** piece of writing for every flag, beyond the two [A worker's handover carries
no acceptance condition for the node it mints](35-handover-mints-no-condition.md) just fixed:

> The round that raised the flag — an `## Interview` attempt or a `## Review` round — says **what produced
> it**, and for a flag written from a worker's own unprompted judgement that means what the worker actually
> did, in its words. A one-line summary is enough under `## Flags`; it is not enough in the round that
> created it. Where there is no round at all — a `research` node, an AFK `precondition` node — the
> `## Flags` entry carries that account itself.

**No handover part carries that text out of any worker.** After node 35 the five contracts ask for the
`## Flags` prose and the `flags.md` sentence, and nothing else. So the account — *what the worker actually
did*, explicitly *in its words* — has no route from the party that holds it to the file that requires it.

### This is the same defect a third time, which is why it is a node and not a clause

Node 35's subject was a handover part naming fewer artifacts than the graph needs: `NEW NODES` naming four
elements where an implementation node needs five, and `FLAGS` naming one artifact where a flag entry lands
in two. This is the third instance and the one that node could not reach — its acceptance condition named
two places, so a worker complying with it produced a section that says two.

Found by that node's **blind checker**, as a note attached to the question that opened its correction round.
Promoted to a node by the human, whose words on being shown it were *"we will need to do something"* against
the manager's proposal to mint rather than fix in place.

### What the answer has to decide, and one thing it must not assume

**Where the account goes when there is a round, versus when there is not.** The clause splits: with a round,
the account belongs to the `## Interview` attempt or the `## Review` round; with no round — `research`, AFK
`precondition` — it belongs to the `## Flags` entry, which node 35's correction round taught those two
contracts. So the no-round half is now covered and **the round half is not**: for a grilling, prototype or
implementation worker, nothing carries the account to the round that created it.

**Not to assume: that this is a sixth handover part.** Two cheaper shapes exist. The `FLAGS` part could ask
for the account as a third element beside the prose and the sentence, since it is flag text and travels with
the flag. Or the account may already be reaching the round by another route — a raise's `SO FAR`, a
correction round's report of what changed — in which case what is missing is the instruction to file it
there rather than the text itself. Establish which before adding a part: [Off-contract subagent
output](17-off-contract-output.md) settled that the manager files what it can paste, and a part that
duplicates text already arriving is cost with no gain.

**One asymmetry worth checking rather than assuming.** The requirement says *in its words*, which is the
scribe rule biting: the manager may not write this account, and the two measured instances of the manager
authoring flag text — nodes 33 and 36, flag `33.4` — are the same failure this one would produce.

### The acceptance condition is owed

Written by whoever spawns this. Note that it may not be claimed without one, and that node 35's evidence
says the writer should read it back against the self-containment rule before handing it over — a duty the
five worker contracts now carry and the manager's own skill does not.

### What the answer touches

The five `.claude/skills/expedition-<type>/SKILL.md` contracts, and `graph-conventions.md` only if the clause
above turns out to be the thing that is wrong rather than the contracts.

**Sequencing, not a blocker.** Those five files are also the live territory of [Checking a flag before the
human sees it](30-checking-a-flag-before-the-human.md), [Narrow the flags.md clause in the worker
contracts](32-narrow-flags-file-clause.md) and [Nothing tells a worker to hold its work against the
record](37-invalidations-is-not-a-check.md). The landing policy forbids a second commit against one **node**,
not against one **file**, so these may run in any order — but not concurrently, the code slot being
exclusive.

## Acceptance condition

*Authored by [node 392](392-write-the-acceptance-conditions-for-the-five-kept-nodes.md)'s worker, from the human's 2026-10-06 decision where the node has one, and filed by the manager.*

> Done when all of the following hold. In this condition, a *round* is an `## Interview` attempt or a round in `## Review` on a node file. A flag's *account* is the full account of what produced the flag. For a flag from a worker's own unprompted judgement, the account is what the worker actually did, told in the worker's words.
>
> 1. `.claude/skills/expedition/graph-conventions.md` states, for every node, which section of the node file holds a flag's account. Before this work, that statement is this paragraph under `### Raise a flag`: "The round that raised the flag, an `## Interview` attempt or a round in `## Review`, says what produced it. For a flag from a worker's own unprompted judgement, what produced it is what the worker actually did, told in the worker's words. A one-line summary is enough under `## Flags`. The round needs the full account. Where a node has no round at all, as with an AFK `precondition` node, the `## Flags` entry carries that account itself." The work may change where the statement places the account. After the work, the statement still places the account in some section of the node file, on every kind of node.
> 2. Every section that clause 1's statement names as holding the account admits it in graph-conventions.md's own description of that section, under `## The node file`. Where the statement names `## Review`, that section's description lists the account among the kinds of entry it holds. Before this work, that description lists three kinds of entry "and nothing else": a checker run, a correction round, and the gate's outcome. Where the statement names `## Interview`, that section's description lists the account among what an attempt's block holds.
> 3. Each of these four files states in which part of which of its hand-back shapes its worker hands back the account, for every section where clause 1's statement places the account on that worker's kind of node:
>    - `.claude/skills/expedition-grilling/SKILL.md`
>    - `.claude/skills/expedition-prototype/SKILL.md`
>    - `.claude/skills/expedition-precondition/SKILL.md`
>    - `.claude/skills/expedition-implementation/SKILL.md`
> 4. The account may travel inside a part whose other text is filed under a different section of the node file. An example is the `FLAGS` part, whose prose is filed under `## Flags`. In that case, `.claude/skills/expedition/SKILL.md` or `.claude/skills/expedition/graph-conventions.md` states that the account is filed under the section clause 1's statement names.
> 5. Where each of the four files in clause 3 states where the account is held, that statement agrees with clause 1's statement. Before this work, the four files' statement is this paragraph of `## When you raise a flag`: "The round that created the flag, an `## Interview` attempt or a `## Review` round, holds the account of what produced the flag. If your node holds no round at all, meaning no exchange with the human and no gate, your `## Flags` entry holds that account instead: what you actually did, in your words."
> 6. The sections headed `## When you raise a flag` and `## When a node you report is an implementation node` are byte-identical across the four files of clause 3 before this work, and are byte-identical across them after it.
> 7. This condition fixes no form. Any of the following meets it, provided clauses 1 to 6 hold:
>    - the account travels as a new part of a hand-back shape;
>    - the account travels as a further element of an existing part, such as `FLAGS`;
>    - the account travels inside text a shape already carries, such as a question's `SO FAR` or a correction round's report of what changed;
>    - clause 1's statement moves the account to a section that an existing route already reaches.
> 8. The working tree meets the bar.
>
> Scope: the scope came from no search, because the named places are the work rather than instances of a defect.

## Annotation: this node is now startable, on the same decision that unstuck node 32

*Filed by the manager.* This node has been unclaimable since 2026-08-20 for one reason only — no acceptance
condition, and nobody assigned to write one, this node having been **promoted by the human** from a checker's
note rather than reported by any worker. [Who writes the acceptance condition for an implementation node the
manager mints itself](39-condition-for-a-manager-minted-node.md) settles it: the manager writes it, under the
four constraints recorded there, and this node is the **first route** that node named — the human's steering —
rather than the manager's own reading of the graph, which was node 32's.

**The constraint that bites hardest here.** Constraint 1 permits the condition to demand only what is already
fixed. What is fixed for this node is the requirement in `graph-conventions.md`'s `### Raise a flag` procedure,
quoted in full in the `## Question` above, and the shape of the five contracts' handover sections as node 35
left them. What is **not** fixed is which handover part carries the account and whether it is a new part or a
widening of `FLAGS` — so the condition states the property and leaves the form, or that choice goes to the human
as a raise.

Beside it, and not this node's to fix: [Widen the invalidation channel](43-widen-the-invalidation-channel.md)
already widens a different handover part, so the two touch the same sections of the same five files and are not
concurrently claimable.

*The manager's note, 2026-10-05:* the question changed, as reported by [node 385](385-whether-the-rarely-used-node-kinds-should-stay.md)'s worker under its `CONDITIONS`: "It quotes graph-conventions' \"a `research` node, an AFK `precondition` node\", which after the new node reads \"an AFK `precondition` node\"." The new node is [node 388](388-merge-research-into-precondition-and-remove-the-cascade-pass.md).

*The manager's note, 2026-10-06:* kept at the triage the human invoked and approved (`verbatim` *"ok"*). A read-only agent checked it against the current files and found it still live; it has no acceptance condition yet.

## Handover, attempt 1

*Pasted as the worker handed it back, 2026-10-06.*

`````
HANDOVER:      Nothing carries a flag's account of what produced it out of a worker

ANSWER:        The account of what produced a flag is now held in the flag's `## Flags` entry on every kind of node. That replaces the earlier split, where the round (an `## Interview` attempt or a `## Review` round) held the full account and `## Flags` needed only a one-line summary, except on a node with no round. The account reaches that entry by a route that already existed: the handover's `FLAGS` part, whose prose for the node is filed under `## Flags`. So no new handover part was built, and no round needs a filing instruction. This is the fourth form clause 7 of the condition permits: clause 1's statement moves the account to a section an existing route already reaches.

               What changed:
               - `.claude/skills/expedition/graph-conventions.md`, `### Raise a flag`: the paragraph now reads: "The flag's entry under `## Flags` holds the full account of what produced the flag, on every kind of node. For a flag from a worker's own unprompted judgement, that account is what the worker actually did, told in the worker's words. The entry holds the account whether or not the node has an `## Interview` attempt or a round in `## Review`. A worker hands the account back as part of its handover's `FLAGS` part, which is filed under `## Flags`." This covers clauses 1 and 4. Clause 4 is met trivially, because the part and the account file under the same section.
               - The same file, the `### `## Flags`` description under `## The node file`: it now says that each entry holds the full account of what produced its flag, pointing at `### Raise a flag` (clause 2). The `## Review` and `## Interview` descriptions are unchanged, because the statement no longer names them.
               - The four contracts (grilling, prototype, precondition, implementation), `## When you raise a flag`:
                 - The `## Flags` bullet loses "A one-line summary is enough, and you may write more" and now asks for the full account of what produced the flag.
                 - The closing paragraph now says the `## Flags` entry holds the account on every kind of node, whether or not the node has a round. It says that for an unprompted judgement the account is what the worker actually did, in its words. It also names the route: hand the account back in the handover's `FLAGS` part, inside the flag's prose for the node (clauses 3 and 5).
               - Clause 6: `## When you raise a flag` and `## When a node you report is an implementation node` are byte-identical across the four files after the change, checked by md5 over each section.
               - Untouched: the `FLAGS:` template lines in the handover shapes, which node 41 also edits, and `.claude/skills/expedition/SKILL.md`. Its `## Flags` section already points at graph-conventions for the form of each entry.

               Bar: the repo states no build, test or format command. The root holds `CONTEXT.md` and `CONTEXT-MAP.md` but no `CLAUDE.md`, `AGENTS.md` or manifest. So the record in map-implementation-rules.md (none) stands unconfirmed. The bar is its non-command half, and the new lines wrap within the files' width.

INDEX LINE:    A flag's full account of what produced it now lives in its `## Flags` entry on every node, carried out of a worker by the existing `FLAGS` part.

FLAGS:         ASSUMPTION: I chose where the account lives rather than raising it. The condition leaves the form open (clause 7) and lists moving the account to a section an existing route reaches as one permitted form. I picked that form: the `## Flags` entry, which the `FLAGS` part already reaches, on every kind of node.
               What I did: I read node 26's answer (item 7) and node 35's answer and review, the only places that give a reason for the round holding the account. The only reason I found is that the no-round case needed somewhere to put it. I found no reason for preferring the round when there is one.
               I set aside two alternatives:
               - A new handover part, or a third element of `FLAGS`, aimed at the round. This keeps two places for one thing and would need a filing instruction in SKILL.md under clause 4.
               - Telling the worker to put the account in `SO FAR` or in its correction-round report. That fails for flags raised in a handover, and the implementation contract has no separate correction-round shape to carry it.
               Moving the account also puts it beside the flag, where the human looks when they return to it, which is what the node's question asks for.
               What it costs: `## Flags` entries get longer, and the earlier "one-line summary is enough" allowance is gone. It also reverses the placement that node 26 shipped and node 35 kept (see INVALIDATIONS).
               Index sentence: Node 40's worker moved a flag's full account from the round that produced it into its `## Flags` entry on every node, reusing the `FLAGS` route rather than adding a handover part.

NEW NODES:     Name: Three worker contracts say "all seven parts" over a handover of eight
               Kind: implementation
               Question: This lets a grilling, prototype or precondition worker count its handover's parts correctly, so that a part is not dropped because the count is wrong. `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md` and `.claude/skills/expedition-precondition/SKILL.md` each say "Hand back all seven parts every time." Each lists eight parts in its handover shape: HANDOVER, ANSWER, INDEX LINE, FLAGS, NEW NODES, INVALIDATIONS, CONDITIONS and MISSING FROM MAP. The implementation contract already says "all eight parts".
               Blockers: none. It touches the same files as node 41, so it cannot run at the same time as node 41.
               Acceptance condition: Done when all of the following hold.
               1. In each of `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md` and `.claude/skills/expedition-precondition/SKILL.md`, the sentence that says how many parts the handover has states the number of parts that the file's handover shape lists.
               2. No other text in those three files changes.
               3. The working tree meets the bar.
               Scope: `grep -n "parts every time" .claude/skills/expedition-*/SKILL.md` over the working tree on 2026-10-06 returned four lines. The three files above say "seven" and `expedition-implementation/SKILL.md` says "eight". The implementation line is already correct and is not part of this work. An instance the search reaches outside this list is reported and not edited.

INVALIDATIONS:
               - Node 26 (Carry the recorded deltas into the shipped files), answer item 7. It shipped "the round which raised a flag says what produced it … a one-line summary being enough under `## Flags` and not enough in the round". This is a contradiction: the account now lives in `## Flags` on every node, and the one-line allowance is gone.
               - Node 35 (A worker's handover carries no acceptance condition for the node it mints), answer. Its closing paragraph names the account as a different artifact, "carried by the round that created it, or by the `## Flags` entry itself where there is no round", and it deliberately built no part for the round case. This is a narrowing: the no-round branch now covers every node, and the round branch is gone.

CONDITIONS:    Searched for: "what produced", "one-line summary", "holds the account", "carries that account", "round that created", "round that raised", "round needs the full", "When you raise a flag", "Raise a flag" and "seven parts". I searched the `## Acceptance condition` and `## Question` sections of every open or claimed node (4 at the time), and the resolved nodes' `## Answer` and `## Acceptance condition` sections.
               - Open or claimed nodes: only this node matched. Node 41's condition edits the `FLAGS:` line and the marker list, and nothing in my change affects its clauses.
               - Something seen, but not caused by my work: node 41's clause 7 lists `.claude/skills/expedition-research/SKILL.md`, which does not exist in the tree, because node 388 merged research into precondition. The amendment on node 41 does not replace that clause.
               - I wrote no replacement clause, and no open node's question changes.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings: none yet.
               Paths touched (all under /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/40-flag-account):
                 .claude/skills/expedition/graph-conventions.md
                 .claude/skills/expedition-grilling/SKILL.md
                 .claude/skills/expedition-prototype/SKILL.md
                 .claude/skills/expedition-precondition/SKILL.md
                 .claude/skills/expedition-implementation/SKILL.md
               Proposed commit message:
                 A flag's account of what produced it lives in its `## Flags` entry

                 graph-conventions.md places the full account in the flag's `## Flags` entry on
                 every kind of node, and its `## Flags` description admits it. The four worker
                 contracts hand the account back inside the `FLAGS` part's prose for the node,
                 which already reaches that section, so no handover part is added.

                 Node: graph-workflow/40

RETROSPECTIVE:
(1) What I had to hunt for: why the round, and not `## Flags`, was chosen to hold the account. I looked first in decisions.md, where my search was too broad (my own error) and found nothing on point. The reason was in node 26's answer item 7 and node 35's review. I reached both by grepping every node file for "what produced" and "one-line summary".
 - `nothing-pointed-me-at-it` — the reason for a shipped rule sat only in resolved node bodies, with no index line naming it. Carried by 4 earlier retrospectives: 135, 178, 385, 389.
(2) What I did not need:
 - `map-read-whole-for-a-few-items` — I used only the ground rules and the writing rules from map.md. Carried by 16 earlier retrospectives: 135, 178, 185, 205, 214, 220, 284, 317, 382, 386, 387, 388, 389, 390, 391, 392.
 - `rules-file-read-whole-for-one-section` — from map-implementation-rules.md I used only the standards list and the bar paragraph. Carried by 13 earlier retrospectives: 178, 185, 214, 220, 317, 382, 386, 387, 388, 390, 391, 392.
(3) What would have made this easier: a spawn note naming nodes 26 and 35 as the source of the round placement.
 - `question-quotes-superseded-text` — the node's question quotes the old em-dash wording of the rule, and a `research` node that no longer exists. Carried by 4 earlier retrospectives: 185, 214, 317, 392.
(4) What was stale or wrong:
 - `count-wrong-when-written` — three contracts say "all seven parts" over an eight-part handover, reported in NEW NODES. Carried by 1 earlier retrospective: 135.
 - `stale-status-quoted-in-a-question` — node 40's question still speaks of "five contracts" and a `research` node. Node 41's clause 7 names `.claude/skills/expedition-research/SKILL.md`, which is gone. Carried by 1 earlier retrospective: 388.
`````

## Flags

`40.1` `ASSUMPTION` — The worker moved a flag's full account into its `## Flags` entry on every node. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-10-06:* the worker's `CONDITIONS` says node 41's clause 7 still lists the research contract. That clause was replaced by node 41's `## Amendment, 2026-10-05 (from node 388's landing)`, which drops the path. The worker read the clause as first filed.
