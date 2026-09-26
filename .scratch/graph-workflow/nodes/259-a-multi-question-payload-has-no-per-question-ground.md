# A multi-question payload has no per-question place for what the question rests on

Type: grilling
Status: resolved

Blocked by: none

## Question

*Surfaced by [node 248](248-review-the-priority-list-and-decide-how-much-ships.md)'s worker, and pasted as it wrote
it.*

> The grilling contract's multi-question shape gives each question `ASK`, `RECOMMENDED` and `ALTERNATIVES`, and
> `SO FAR` is written once for the whole payload. A question resting on findings of its own has nowhere to put them,
> so they go into `ASK` and bury the question. This cost a measured human turn on node 248: the human read a long
> `ASK` and replied *"what do you propose ?"* when a recommendation was already written below it. Decide whether the
> shape gains a per-question field, or whether `ASK` is instructed to hold the question only.

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**The measured turn is real and the manager watched it happen.** The human's reply was `verbatim` *"Q1. … What do
you think about it ? For the rest ok Q2. what do you propose ?"*, and the worker's own next payload opens by naming
the cause: *"you asked 'what do you propose?' and I had already written a recommendation, which means it was not
findable. That is my error and worth naming: I put five paragraphs of findings inside the ASK field instead of
keeping it to the question, so the proposal sat behind a wall."*

**The manager relayed that payload unaltered, as it must**, so the burial reached the human through a channel that
cannot repair it. That is what makes this the contract's problem rather than one worker's.

## Answer

A multi-question payload gives each question an optional `CONTEXT` line for why it is asked, keeps a recommendation's grounds in `RECOMMENDED`, and limits `ASK` to the question itself.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The human's answer is under `## Interview`. The node the worker surfaced is [node 331](331-give-each-question-in-a-multi-question-payload-a-context-line.md).

## Interview

### Attempt 1

**Q1, from the worker**, pasted as it wrote it, 2026-09-26. **Held, not yet put to the human**: it arrived while node 319's gate was in front of the human, with node 302's gate and [node 123](123-who-performs-a-stop.md)'s questions queued ahead of it.

```
NODE:          A multi-question payload has no per-question place for what the question rests on (node 259)
ABOUT:         When a worker puts several questions in one payload, the grilling contract gives each question only ASK, RECOMMENDED and ALTERNATIVES, and SO FAR is shared by all of them. This node decides where a finding that belongs to only one question goes. It is decided now because the gap already cost you one turn, at node 248.
SO FAR:        What I read: this node, the grilling contract as it stands and its git history, node 248's interview and retrospective, node 117's answer (where batching was decided), node 123's pending payload, the external /grilling skill, and the other four worker contracts' question shapes.
               - What happened at node 248. Q2's ASK held about five paragraphs of findings, and the recommendation came after them. You replied "Q2. what do you propose ?", although RECOMMENDED was written right below. The worker's next payload named the cause itself: "I put five paragraphs of findings inside the ASK field instead of keeping it to the question, so the proposal sat behind a wall."
               - The contract already has part of the answer. Each question's RECOMMENDED has read "<your recommendation, and what it rests on>" since the multi-question shape was added on 2026-09-06, before node 248. So a question's own grounds already had a place. What the contract never says is that ASK holds only the question. The external /grilling skill that batching was adopted from says the opposite: its question body "might be multiple paragraphs".
               - One worker has already done it the other way without being told. Node 123's worker, working under the current contract, wrote a three-question payload. It has not reached you yet. Each ASK is one sentence, each question's findings sit in its RECOMMENDED after "Grounds:", and the facts all three questions share are in SO FAR. To me it reads cleanly. That is my judgement, not a measurement.
               - Only the grilling contract has the multi-question shape. The other four worker contracts ask one question per payload, each with its own SO FAR, so nothing else would change.
               - Node 322 will edit a different part of the same contract ("What a reply settles"). This change would touch only the payload shape.
               - Settled on my own authority: I read "what the question rests on" in this node's title as the findings specific to one question, as opposed to the facts several questions share.
ASK:           Where should a finding that belongs to one question go: into a new field of its own, or into that question's RECOMMENDED, with the contract telling ASK to hold only the question?
RECOMMENDED:   No new field. Add two sentences to the contract. In both shapes, ASK holds only the question, in a sentence or two. In the multi-question shape, a finding that one question rests on goes in that question's RECOMMENDED, after the recommendation itself, so the proposal is the first thing under the question; a finding that several questions rest on goes in SO FAR. Grounds: the place already exists and the field's own text names it. What failed is that nothing kept findings out of ASK, and one sentence fixes exactly that. Node 123 shows how the result reads. A new field would appear on every question and be empty on most. Its position also costs something wherever it goes: before ASK it pushes the question down, and between ASK and RECOMMENDED it rebuilds the wall that hid the proposal at node 248.
ALTERNATIVES:  - A new field for each question, e.g. `CONTEXT:`, placed after ALTERNATIVES so that the question, recommendation and alternatives stay together at the top and the detail comes last. It gives findings a home of their own, at the cost of a fifth line on every question.
               - Change nothing, and treat node 248 as one worker's slip. Against it: the manager relays a payload unaltered, so a buried question reaches you with nothing able to repair it, and the upstream skill actively invites long question bodies.
```

*The manager put Q1 to the human on 2026-09-26, after node 106's gate.*

**Q1, the human's answer**, 2026-09-26, `verbatim`: *"CONTEXT makes more sense if its really context, if it explains why the questions are asked. If it's explaining why the recommended was recommended, putting it in the RECOMMENDED makes a lot of sense"*

*The manager's note:* **a divergence in part.** The worker recommended "No new field"; the human keeps a finding that explains the recommendation in RECOMMENDED, as the worker proposed, and gives a finding that explains why the question is asked to a `CONTEXT` field, which the worker offered only as an alternative ("A new field for each question, e.g. `CONTEXT:`, placed after ALTERNATIVES").

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      A multi-question payload has no per-question place for what the question rests on

ANSWER:        **A question in a multi-question payload gains an optional `CONTEXT` line for why that question is asked. What explains the recommendation stays in `RECOMMENDED`, and `ASK` holds only the question.** The human's words, `verbatim`: *"CONTEXT makes more sense if its really context, if it explains why the questions are asked. If it's explaining why the recommended was recommended, putting it in the RECOMMENDED makes a lot of sense"*.

               **This diverges in part from the worker's recommendation.** The worker recommended no new field, with every finding specific to one question going into its `RECOMMENDED`. The human kept that half for findings that explain the recommendation. For material that explains why the question is asked, they chose the `CONTEXT` field, which the worker had offered only as an alternative.

               **The rules that now hold, in the grilling contract's payload shape:**
               1. In both shapes, `ASK` holds only the question, in a sentence or two. At node 248, five paragraphs of findings inside a question's `ASK` hid the recommendation below them, and the human replied *"what do you propose ?"*. That cost a human turn.
               2. In the multi-question shape, each question may carry a `CONTEXT` line holding why that one question is asked. It sits between the question's numbered title and its `ASK`, and it is left out when the question needs none.
               3. A finding that explains why the recommendation is recommended goes in that question's `RECOMMENDED`, after the recommendation itself, so the proposal is the first thing under the question. The field's placeholder already said *"your recommendation, and what it rests on"* before node 248. The gap was never a home for grounds. It was a home for why a question is asked, and a rule keeping findings out of `ASK`.
               4. A fact that more than one question in the payload rests on goes in `SO FAR`, as before.

               **The single-question shape gains no `CONTEXT`.** There, `ABOUT` and `SO FAR` already belong to the one question. Only the grilling contract has a multi-question shape, since the other four worker contracts ask one question per payload. No other shipped file names these fields.

INDEX LINE:    A multi-question payload gives each question an optional `CONTEXT` line for why it is asked, keeps a recommendation's grounds in `RECOMMENDED`, and limits `ASK` to the question itself.

FLAGS:         ASSUMPTION — **`CONTEXT` sits between the question's numbered title and `ASK`, not after `ALTERNATIVES`, which is where the worker's own alternative had put it.** The human chose the field but did not say where it goes. Three grounds. First, the human defined it as explaining why the question is asked, and a reader needs that before the question, not after it. Second, the failure at node 248 was material sitting between `ASK` and `RECOMMENDED`, and this placement keeps `ASK`, `RECOMMENDED` and `ALTERNATIVES` together. Third, `ASK` stays a short labelled line, so a reader who skips the context still finds the question at once. The cost, which the worker itself named in its payload, is that a long `CONTEXT` pushes the question down. The rule that `CONTEXT` holds only why the question is asked is what keeps that cost small.
               Index: The per-question `CONTEXT` line sits between the question's title and `ASK`, so why a question is asked is read first and the question stays next to its recommendation.

               ASSUMPTION — **`CONTEXT` is optional, left out when a question needs none, and exists only in the multi-question shape.** The worker's payload objected that a new field would sit empty on most questions. The human's *"if its really context"* reads as a line used when there is context to give, not a slot to fill every time. In the single-question shape, `ABOUT` and `SO FAR` already belong to the one question, so a `CONTEXT` line there would duplicate them.
               Index: `CONTEXT` is an optional line of the multi-question shape only, left out when a question needs no explanation of why it is asked.

NEW NODES:     **Name:** Give each question in a multi-question payload a context line
               **Kind:** implementation
               **Question:** Carry the payload-shape rules decided at node 259 into the grilling worker contract.
               **Blockers:** none. Node 322 edits the "What a reply settles" bullets of the same file, a different part of it. The manager sequences the two edits.
               **Acceptance condition:**
               In `.claude/skills/expedition-grilling/SKILL.md`, under the heading `### question — you need the human`:
               1. In the fenced block that shows the shape for more than one question, each of the two example questions (Q1 and Q2) has a line beginning `CONTEXT:`, with the field name padded to the same column as the other field names. The line is placed after that question's `Q<n>. <short title>` line and before its `ASK:` line. Its placeholder says that the line holds why this one question is asked, and that the line is left out when the question needs none.
               2. The fenced block that shows the shape for one question contains no `CONTEXT:` line and is otherwise unchanged.
               3. The prose of that section states each of the following:
                  a. In both shapes, `ASK` holds only the question, in a sentence or two.
                  b. `CONTEXT` belongs to the multi-question shape only. It holds why its question is asked, and it is left out when there is nothing of that kind to say.
                  c. A finding that explains why the recommendation is recommended goes in that question's `RECOMMENDED`, after the recommendation itself.
                  d. A fact that more than one question in the payload rests on goes in `SO FAR`.
               4. The sentence that lists what each question in the multi-question shape carries (today: a number, a short title, its own recommendation, and the alternatives it sets aside) also names the optional context line.
               5. No other part of the file changes what it requires, and no other file under `.claude/` is changed.

INVALIDATIONS: none. Nodes 117 and 126 fixed the multi-question shape as numbered, titled questions, each with its own recommendation and alternatives. An optional extra line extends that shape and contradicts none of it.

RETROSPECTIVE:
1. **What I had to hunt for.** (a) Whether `RECOMMENDED`'s "and what it rests on" existed before node 248, which decides whether the node's premise ("nowhere to put them") was true. I looked first at the current contract, which could not tell me. I found it with `git log -S` and `git show 8cc9b79` on the contract: the text was there from 2026-09-06, before 248. (b) Whether any other contract shares the multi-question shape. I grepped `.claude/` for `ASK:` and the other field names, and none does. (c) The upstream `/grilling` skill's round format. `~/.claude/plugins` held nothing, and I found it in the nix store. Its "question body, might be multiple paragraphs" is the invitation that caused the 248 failure.
2. **What arrived that this node did not need.** Almost all of `map.md`. Its very long `## Notes` lines had nothing to act on here except the one-question and scarce-human preferences, which I already knew. Node 248's 612 lines, when I needed only the first payload, the reply and the retrospective paragraph (about lines 71–230 and 563). Better arrangement: the spawn, or this node's file, could give the line range of the offending payload, or quote it.
3. **What would have made this easier.** This node's file could have quoted the Q2 `ASK` that caused the turn, and noted that `RECOMMENDED` already asked for grounds. That fact reframes the question from "where do grounds go" to "where does why-asked go". The human's answer drew exactly that distinction, which I had not offered as a split. The spawn's pointer to node 123's payload was the most useful single item: it gave a working example under the current contract.
4. **Stale, wrong or contradicting.** This node's `## Question`, pasted from node 248's worker, says a question's own findings have "nowhere to put them". That was partly wrong when written: `RECOMMENDED`'s placeholder already named "what it rests on". What lacked a home was material explaining why a question is asked. Minor: the node's title says "per-question place" and its filename says "per-question ground". Also minor: node 248's Q1 had the same fault (findings inside `ASK`) and cost no turn, so a long `ASK` does not reliably cost a turn. Node 248's own retrospective does not overstate this.

## Flags

`259.1` `ASSUMPTION` — **`CONTEXT` sits between the question's numbered title and `ASK`, not after `ALTERNATIVES`, which is where the worker's own alternative had put it.** The human chose the field but did not say where it goes. Three grounds. First, the human defined it as explaining why the question is asked, and a reader needs that before the question, not after it. Second, the failure at node 248 was material sitting between `ASK` and `RECOMMENDED`, and this placement keeps `ASK`, `RECOMMENDED` and `ALTERNATIVES` together. Third, `ASK` stays a short labelled line, so a reader who skips the context still finds the question at once. The cost, which the worker itself named in its payload, is that a long `CONTEXT` pushes the question down. The rule that `CONTEXT` holds only why the question is asked is what keeps that cost small.

`259.2` `ASSUMPTION` — **`CONTEXT` is optional, left out when a question needs none, and exists only in the multi-question shape.** The worker's payload objected that a new field would sit empty on most questions. The human's *"if its really context"* reads as a line used when there is context to give, not a slot to fill every time. In the single-question shape, `ABOUT` and `SO FAR` already belong to the one question, so a `CONTEXT` line there would duplicate them.
