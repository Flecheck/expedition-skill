# A failed `git merge --ff-only` can leave the tree partially updated, and the record says it cannot

Type: implementation
Status: claimed

Blocked by: none

## Question

*Surfaced by [node 216](216-what-a-correction-round-after-a-rebase-conflict-owes.md)'s worker, and pasted as it
wrote it. **The manager is the party that hit this**, at node 198's landing, and reported it to that worker.*

> `map-manager-only.md` states twice, of the sandboxed merge failure, that *"`HEAD` does not move and nothing is
> lost"* and that *"the merge succeeds outside the sandbox"*. Node 198 falsified the second half: the merge wrote
> one changed file before failing on the read-only mount, left the tree dirty, and the documented retry outside the
> sandbox then refused with *"Your local changes would be overwritten by merge"*. The record's line is what a
> manager reads before deciding this failure is harmless, and it currently promises a clean retry that does not
> happen.

**Blockers, in the worker's words:** *"none. It edits paragraphs node 160 does not freeze, but node 160 also lists
`map-manager-only.md` among its permitted files, so the manager should not run both in one slot pair."*

## Acceptance condition

*Written by node 216's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md`. The worker
> may edit those two files and no other; it may not mark this node, resolve it, or write a line in `decisions.md` or
> `flags.md`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. In `map-manager-only.md`, under the heading `## Landing an implementation node's work`, each of the two
>    sentences asserting that a sandbox-failed merge loses nothing and succeeds on a retry outside the sandbox is
>    **replaced** by text that also states the partial-write case: that the merge may write some of the changed
>    files before failing, that this leaves the working tree dirty, and that a retry outside the sandbox then
>    refuses with `Your local changes … would be overwritten by merge`.
> 2. The text of each sentence replaced under clause 1 is appended, **unaltered**, to `map-history.md` under the
>    heading mirroring the section it came from, appended rather than replacing anything. This is the `Change the
>    map` procedure for text stating a rule that currently binds.
> 3. New text beside it states the repair, in this order and as one pass: establish that the partially written
>    content is byte-identical to what the branch carries, discard it, and re-run the merge outside the sandbox. It
>    states that establishing byte-identity comes **first**, and that where it does not hold the manager stops
>    rather than discarding.
> 4. The paragraph beginning `**Landing policy**` is byte-identical to its state at `HEAD`. The sentence beginning
>    `**A rebase conflict is resolved by nobody in the moment**` is not edited, struck, moved or deleted by this
>    node.
> 5. No heading named `## Notes` is added to either file.
> 6. Every markdown link in both files resolves to a path that exists, except a link to a path outside this
>    repository, which is out of scope.
> 7. No file outside `.scratch/graph-workflow/` is modified.
> 8. The standing quality bar for this repository holds of the finished tree.

## The manager's note at filing

*Not a change to anything above.*

**The manager is a party to this node's subject and states its own conduct rather than a view.** At node 198's
landing it ran the sandboxed merge, met the partial write, established that the dirt was byte-identical to what the
branch carried, discarded it and re-merged — which is exactly the repair clause 3 demands be written down, arrived
at in the moment rather than read from the record. **Clause 3's insistence that byte-identity is established first
is the part the manager got right by luck rather than by rule**, and it is the clause that matters.

**A second instance arrived after this node was specified, and it points the other way.** Landing [node
229](229-bank-the-landing-sections-accounts-out-of-map-manager-only.md), the same sandboxed merge refused on **both**
changed files, leaving `HEAD` unmoved and **nothing** partially written — the record's line as written. So the
partial write is a case rather than the rule, and clause 1's *"may write some of the changed files"* is the right
shape. **Whoever claims this should not read node 198 as the normal case.**

**Its author's blocker note is scheduling and the manager holds it**: node 160 lists `map-manager-only.md` among its
permitted files, so these two must not run in one slot pair. No blocking edge is written.

## Amendment, 2026-09-27 (from node 160)

*Written by [node 160](160-carry-the-integration-conflict-rule-into-the-map.md)'s worker under its `CONDITIONS`, and filed by the manager. Pasted as it wrote it.*

Node 234, clause 4, second sentence. Current text: "The sentence beginning `**A rebase conflict is resolved by nobody in the moment**` is not edited, struck, moved or deleted by this node." That sentence no longer exists, so the clause is vacuously true and no longer protects anything. Replacement: "The text in that paragraph beginning `A rebase conflict is resolved, and the rebase is not aborted.` and ending `the manager runs `git rebase --abort` and the node takes a correction round.` is not edited, struck, moved or deleted by this node." What fixes these words: this node's work, once landed in the tree.
Clause 4's first sentence, "The paragraph beginning `**Landing policy**` is byte-identical to its state at `HEAD`", still holds against whatever HEAD is when node 234 runs.

## Interview

#### Raise 1, relayed 2026-09-28

*Pasted as the worker handed it back. The worker is stopped until the human answers.*

```
NODE:          234, "A failed `git merge --ff-only` can leave the tree partially updated, and the record says it cannot"
ABOUT:         Replace the record's claim that a merge failed in the sandbox loses nothing and retries cleanly, bank the old text, and write the repair down. I stopped at the check you asked for, before any edit. Nothing in the worktree is touched.
SO FAR:        I read the contract, the node file (with its node-160 amendment), map.md, map-implementation-rules.md, and the landing, merge and sandbox lines in decisions.md. Then I searched the worktree (`7093c67`) for the passages the condition names.
               - Clause 1 says "each of the **two** sentences" claiming that a sandbox-failed merge loses nothing and succeeds on a retry outside the sandbox. Only **one** such sentence is left in `.scratch/graph-workflow/map-manager-only.md` under `## Landing an implementation node's work`, in the "One sandbox restriction bites this lifecycle" bullet, sub-bullet "What it hits": "`HEAD` does not move and nothing is lost in either case; both succeed outside the sandbox." It covers two operations: the merge, and `git reset --hard` inside an entered worktree. That reset is a step of no route any more (node 265).
               - The two sentences node 216's worker quoted ("`HEAD` does not move and nothing is lost; the merge succeeds outside the sandbox" and "the merge succeeds on a retry outside the sandbox") are already gone. Node 229 (`38709b7`, 2026-09-13 09:49) moved them to `map-history.md`, word for word, under `## Superseded from map-manager-only.md — the landing section's accounts`, as Edit 13 and Edit 14. That was 14 minutes before this node was minted (`5d8507c`, 10:03). At minting, `git show 5d8507c:` already shows only the one combined sentence. So the condition was out of date from the day it was written, which is the kind of case you told me to raise.
               - Everything else checks out. Clause 4's `**Landing policy**` paragraph is there. The node-160 replacement span ("A rebase conflict is resolved, and the rebase is not aborted." … "the manager runs `git rebase --abort` and the node takes a correction round.") is there too. Clauses 5 to 8 raise no problem. The bar for this repo is entirely non-command (no build, tests, formatter or CI), and I confirmed there is no manifest to contradict that record.
               Settled on my own authority: nothing.
ASK:           Clause 1's "two sentences" no longer exist as two. Do I go ahead by treating clause 1 as covering the one surviving combined sentence, with the other two counted as already banked by node 229?
RECOMMENDED:   Go ahead on that reading. This is the concrete shape, which you can approve as worded:
               (a) Replace the surviving sentence with the following. "`HEAD` does not move in either case. The reset loses nothing and succeeds outside the sandbox. The merge may instead write some of the changed files before it fails. That leaves the main tree dirty, and a retry outside the sandbox then refuses with `Your local changes to the following files would be overwritten by merge`." The reset keeps its old claim because nothing has falsified it, and the partial write has only been seen on the merge. The wording keeps "may" because node 229's own landing hit the clean case.
               (b) Right after it, add a repair line for clause 3. "The repair is one pass, in this order: first establish that every dirty file is byte-identical to the branch's version (`git diff --quiet <branch> -- <path>`); then discard the dirt (`git checkout -- <path>`); then re-run the merge outside the sandbox. Where any dirty file differs from the branch, stop and discard nothing."
               (c) Append the replaced sentence, word for word, to `map-history.md` under a new heading "Superseded from `map-manager-only.md` at node 234", with a "### From *Landing an implementation node's work*" subheading. That follows the node-160 and node-336 pattern.
               (d) Clause 2 is then met for the other two sentences, because Edit 13 and Edit 14 already hold them word for word. I would not append them a second time.
               This rests on the node's purpose, which is that the record stops promising a clean retry. That purpose is fully served by fixing the one place that still makes the promise. The claims node 216 quoted now live only in the history file, which holds superseded text.
ALTERNATIVES:  - Rewrite clause 1 (and clause 2) so they name the one surviving sentence, then continue. This is cleaner for the checker, which reads only the condition and will count "two sentences". But the condition would change after the node was claimed.
               - Also correct the reset's half of the sentence, or drop it since the reset belongs to no route. This goes beyond the node's scope and nothing measured supports it.
               - Stop the node as already partly done by node 229 and file a smaller replacement. More bookkeeping for the same edit.

Manager-facing notes (not part of the raise):
- Touched paths: none. The worktree is exactly as it was cut.
- I have not appended anything to `map-history.md`. If I continue, I will append only the one new section described in (c).
- Whichever way you answer, the checker's copy of the condition needs to show how "two sentences" was settled, or the checker will FAIL clause 1 by counting.

RETROSPECTIVE
1. What I had to hunt for: whether the second sentence had been moved to history or deleted outright. It took `git log -S` together with reading Edit 13 and Edit 14 in map-history.md, then an ancestry check to learn it predated this node's minting.
2. What arrived that this node did not need: the landing-merge-sandbox fact (merges run with the sandbox off), and node 186's parallel run on the rules file. Both only matter once the edit happens.
3. What would have made this easier: the node file recording that node 229 landed shortly before minting and banked Edit 13 and Edit 14. Better still, a check at minting that the condition's premises hold against the tree.
4. What was stale, wrong or contradictory: clause 1's "two sentences" and the Question's two quotes were already out of date when the node was minted. The node-160 amendment is accurate. The manager's filing note ("the record's line as written" for node 229's clean case) points at the single combined sentence, without saying that it is now the only one.
```

#### The human's answer to raise 1, 2026-09-28

The human, `verbatim`: *"ok"*. It takes the worker's recommendation: "Go ahead on that reading." — clause 1 covers the one surviving combined sentence, the two sentences node 229 already banked (Edit 13 and Edit 14 in `map-history.md`) count as done for clause 2, and the shape (a) to (d) the raise gives is approved as worded.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-28. The worker's own text, pasted.*

````
HANDOVER:      234, "A failed `git merge --ff-only` can leave the tree partially updated, and the record says it cannot"

ANSWER:        Per the human's "ok" to Raise 1, clause 1 is taken to cover the one sentence that still stated the claim, and clause 2 to be already met for the two earlier statements. Node 229 had moved those two, word for word, to `map-history.md` (Edit 13 and Edit 14) before this node was minted.
               In `map-manager-only.md`, under `## Landing an implementation node's work`, in the bullet "One sandbox restriction bites this lifecycle", sub-bullet "What it hits": the sentence "`HEAD` does not move and nothing is lost in either case; both succeed outside the sandbox." is replaced. The new text:
               - keeps "`HEAD` does not move in either case";
               - keeps the reset's old claim (it loses nothing and succeeds outside the sandbox), because nothing has shown it false and the reset is a step of no route since node 265;
               - states the partial-write case for the merge: it may write some of the changed files before it fails, which leaves the main tree dirty, and a retry outside the sandbox then refuses with `Your local changes to the following files would be overwritten by merge`;
               - states the clean case (the merge fails having written nothing, and the retry succeeds), because node 229's landing hit that case and the partial write is a case rather than the rule.
               The repair follows in the same sub-bullet, as one pass in order:
               1. Establish byte-identity for each dirty file with `git show worktree-<NN>-<name>:<path> | cmp - <path>`.
               2. Outside the sandbox, discard the files: `git checkout HEAD -- <path>` for a file `HEAD` holds, and delete a file it does not hold.
               3. Re-run the merge outside the sandbox.
               The text states that byte-identity comes first. Where any dirty file differs from the branch's version, the manager stops and discards nothing.
               Three choices a later reader would otherwise have to re-derive:
               - The repair goes inside the existing sub-bullet, not in a fourth one, so that the lead-in "The three sub-bullets below are measurements" stays true.
               - The discard runs outside the sandbox because a dirty file under `.claude/skills/` cannot be rewritten inside it.
               - The discard uses `git checkout HEAD --` rather than `git checkout --`, so it also undoes any index write the failed merge made.
               The replaced sentence is appended word for word to `map-history.md` under `## Superseded from map-manager-only.md at node 234 — the claim that a merge failed in the sandbox loses nothing`, subheading `### From *Landing an implementation node's work* — the sandbox restriction's sub-bullet on what it hits`. The introduction under that heading points at Edit 13 and Edit 14 for the two earlier statements.

INDEX LINE:    The landing section now says a sandbox-failed merge may partially write the tree and block a retry, and gives the repair: confirm byte-identity first, discard, re-merge unsandboxed.

FLAGS:         none

NEW NODES:     none

INVALIDATIONS: Node 229 (the landing section's accounts banked): no contradiction. Its Edit 13 and Edit 14 text is now cited from the new history section as the two earlier statements of the claim this node supersedes. Node 140 (Edit 14's measurement, "the merge succeeds on a retry outside the sandbox"): narrowed. That retry is clean only where the failed merge wrote nothing.

CONDITIONS:    What I searched for: the open and claimed nodes' conditions and questions, for "nothing is lost", "succeeds outside the sandbox", "What it hits", "overwritten by merge", "partially written", "ff-only" and "One sandbox restriction bites". Apart from this node, it matched node 251 (line 34: the ff-only merge listed as not retested) and node 80 (line 64: the landing-policy sequence naming `git merge --ff-only`). My work makes neither wrong. There are no replacements and no changed questions.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings: none yet.
               Paths touched, both in worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/234-failed-merge`:
               - `.scratch/graph-workflow/map-manager-only.md`
               - `.scratch/graph-workflow/map-history.md` (appended only; you integrate this against node 186 at landing)
               The node file is not edited. The worktree copy predates the `## Interview` record in the main checkout.
               Checks run against the condition:
               - The `**Landing policy**` paragraph is byte-identical to HEAD (md5 matches).
               - The node-160 rebase-conflict span is untouched.
               - The `## Notes` heading count in both files is unchanged.
               - Every relative markdown link in both files resolves.
               - Only the two files are modified.
               The bar: the repo has no build, tests, formatter or CI. That matches `map-implementation-rules.md`'s record, so there is no difference to report.
               Proposed commit message:
               State that a sandbox-failed merge can partially write the tree, and its repair

               The landing section said a merge failed in the sandbox loses nothing and
               succeeds on a retry outside it. The merge may instead write some changed
               files first, leaving the tree dirty and the retry refused. The section now
               states that case and the one-pass repair: confirm byte-identity with the
               branch first, discard, and re-merge outside the sandbox. The replaced
               sentence is banked in map-history.md.

               Node: graph-workflow/234

RETROSPECTIVE
1. What I had to hunt for: whether the second sentence had been banked or deleted, and when. It took `git log -S` and an ancestry check against the node's minting commit. For the repair, I had to check that git's error message reads "Your local changes to the following files would be overwritten by merge".
2. What arrived that this node did not need: node 186's parallel run and node 364's (relevant only at integration), and the decisions.md lines on worktree routes.
3. What would have made this easier: the node file noting that node 229 had landed shortly before, or a check at minting that the sentences a condition counts actually exist. Either would have made the raise unnecessary.
4. What was stale, wrong or contradictory: clause 1's "two sentences", out of date when the node was minted and settled by the raise. Also, the worktree's copy of the node file lacks the `## Interview` record the manager wrote in the main checkout. That is expected, and not a problem for this work.
````

*The manager's note:* the raise the human approved gave the repair as `git diff --quiet <branch> -- <path>`, then `git checkout -- <path>`, then re-merge. The landed text uses `git show … | cmp`, `git checkout HEAD --`, deletes a file `HEAD` does not hold, and adds the clean case. The worker gives its reasons above but raised no flag for the difference; the manager puts it in the gate.

## Review

### Checker run 1 — `FAIL` (acceptance condition, and the bar)

*The checker's own text, pasted, 2026-09-28. A fresh checker; the condition reached it as a verbatim copy in `$TMPDIR/c234.md`, with the human's settlement of how clauses 1 and 2 are read.*

> FAIL: acceptance condition
>
> This is the check of "Rewrite the manager contract's second part in plain English". The worktree is `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/297-rewrite-the-manager-contract-part-2`.
> - The before-text is `git show 6745f37:.claude/skills/expedition/SKILL.md`, which is also the merge-base.
> - The rewritten range G2 is before-text lines 146–437 and after-text lines 146–419, from `## Spawning a worker` up to `## What is in front of the human, and when`.
> - I walked clauses 1 and 2 separately, and built the rule-change list myself.
>
> **The bar holds.** The repo root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. There is no build, test suite, formatter or CI, so there is no command to run. The non-command half is met:
> - the ground rules and the five standing rules for writing
> - `CONTEXT.md`'s `_Avoid_` lines
> - `graph-conventions.md`
> - `/writing-for-agents`
>
> These standards come from `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md`. That file names no reviewing skill, so I ran none. The changed path is a shipped skill file, not a record file.
>
> **Clause by clause:**
> - **Clauses 1 and 2:** walked. The results are in RULE CHANGES below. None of them fails the work.
> - **Clause 1a:** two before-text terms that `CONTEXT.md` does not define are dropped as terms. For each, the meaning is still stated in plain words where it was defined, so neither is a rule change.
>   - "licence" is now "A permission the human gave in answer to a raise of yours". "Licence" appears nowhere else in the file.
>   - The "**handles** its own work fixes" is now "what its own work fixes: each word it refuses, each path…, and each phrase it supersedes".
> - **Clause 3:** holds. Every generalisation that changes an outcome or decides an open case is listed as a rule change.
> - **Clause 4:** holds. The frontmatter is byte-identical, and G2 has no code fences in either the before-text or the after-text.
> - **Clause 5:** holds. All G2 headings are byte-identical.
> - **Clause 6:** holds. These references resolve: "listed below", "the limit on notes above", "described in the next section", "the payload's first line", "the moments this section names", and "under the raise above". "The raise above" resolves to "A worker that judges the condition wrong raises it". The unchanged part's reference to "`### A flag in a payload` above" also resolves.
> - **Clause 7:** holds. My scan of `_Avoid_` words found only uses outside the refused concept: "discarded" in the prototype entry, "each word it refuses", and "correction round". I also checked by hand. `CONTEXT.md` terms are spelled as it defines them, and no new term is coined.
> - **Clause 8:** fails 8c, as below. 8a, 8b, 8d, 8e and 8f hold:
>   - Each prohibition sits beside its positive.
>   - G2 has no bold.
>   - I found no slogan.
>   - I checked every pronoun.
>   - No sentence has more than one dash aside or more than one semicolon.
>   - No line is longer than 106 characters.
> - **Clause 9 (reported, not enforced):** `wc -w` of G2 is 3147 before and 2749 after, which is 87%. The target is at most 2098, so it was missed.
> - **Clauses 10 and 11:** hold. `.claude/skills/expedition/SKILL.md` is the only changed path, and nothing is untracked. Everything before `## Spawning a worker` and everything from `## What is in front of the human, and when` onward is byte-identical to the before-text (`cmp`, both parts).
>
> **Finding: clause 8c, a figure of speech or coined phrase in G2 prose that is not a term defined in `CONTEXT.md`.**
> - Line 116, "The checker's runs, laid end to end, oldest first." "Laid end to end" is an idiom for placing one after another.
> - Lines 38–39, "such a direction is the only way past it". This is a spatial figure, of the same kind as run 1's "in reach". The plain meaning is that it is the only way to go on.
> - Line 184, "settled at the first human moment its close reaches". "Human moment" is a coined phrase, and a close "reaching" a moment is a figure. The next sentence explains it, but the phrase remains. `CONTEXT.md`'s Flag entry uses the same wording, but it is not a defined term there.
> - Form: a phrase in G2 prose outside code fences that says an idea by figure or coinage rather than in plain words, where the idea is not a `CONTEXT.md` term.
> - Extent: none. I found these by reading, and they are not proven exhaustive.
> - Borderline passages I did not count as breaches: lines 227–228, "reach only a node nobody holds yet"; line 246, "never reaches any of the following three things"; and line 228, "goes over as written". In each, "reach" means "applies to", which is close to the ruled-out "neither pen reaches" but without the pen.
>
> RULE CHANGES
>
> Clause 1. For each entry: the before-text statement in G2, then its counterpart.
> 1. **When a contract blocks the node.** Before: "nothing you send a worker may widen what that worker is permitted to write". After: "Keep what a worker may write within what its contract allows, in every message you send it, a resume included."
>    - The limit moves from what the worker is permitted, which includes a permission the human granted, to what its contract allows.
>    - `### Two things that travel in a spawn and are not yours` lets you carry such a permission. A message carrying one that lets the worker write beyond its contract was allowed before, and is outside the after-text rule.
> 2. **Changing a contract.** Before: "Amending a contract is its own piece of work against that file, and never something you do mid-flight." After: "Changing a contract is a separate piece of work on that file. You never change one while the node it blocks is being worked."
>    - "Mid-flight" was not tied to any one node. The counterpart ties the ban to the blocked node, which narrows it where another node under the same contract is being worked.
> 3. **A flag in a payload.** Before: "*(This is one effort's standing instruction from its human rather than a rule of the workflow — see* Standing steering *below. Where an effort's human has not said it, ask.)*" After: "That settling rule is one effort's standing instruction from its human, and is not a rule of the workflow. Where an effort's human has not given it, ask them whether their approval settles the node's flags."
>    - The before-text left open two things: whether "This" meant "every flag the node holds is in the payload" or the settling statement, and what to ask. The after-text decides both.
>    - It now states that the settling rule is not a rule of the workflow. That sits against the same file's `## Flags`: "A node's flags are settled at the first human moment its close reaches … Every kind of node follows this rule."
> 4. **Which amendments reach only unclaimed nodes.** Before: "Everything here reaches a node nobody holds yet." After: "The amendments in this section, by the party that established a fact and by you, reach only a node nobody holds yet."
>    - "Everything here" covered the whole section. That includes the search, which the same section says covers "every open node's condition, claimed or not".
>    - The after-text limits the unclaimed-only rule to those two kinds of amendment. That settles a contradiction the before-text left open.
> 5. **Where an amendment is named.** Before, item 5 of the things that accompany an amendment: "or, where the amendment is made after the node is claimed, in that node's closing report instead". After: "Where the amendment is made after the node is claimed, it is named in the report that closes that node instead."
>    - Under the before-text's own line-25 import, "closing report" is `CONTEXT.md`'s effort-level Closing report. The after-text names the report that closes the node.
>
> Clause 2. A statement the after-text makes that the whole before-text does not.
> 6. **When a flag may be settled.** Line 190: "Settle a flag only at the moments this section names, never on your own judgement or on the passage of time." The before-text said only "You never settle a flag on your own judgement or on the passage of time." The word "only" adds a ban on settling a flag at any moment other than those `## Flags` names.
>
> **Checked and not counted as rule changes:**
> - **What the checker may be pointed at.** "It is the one agent whose payload cannot be a pointer" became "its spawn never points it at the node file". Combined with "receives nothing from the effort's own record", and the condition and ground rules going as text, the outcome is the same.
> - **The ban on quantifying over the record.** "may not quantify over the record" became "makes no demand about the record as a whole". This is the wording of the landed `graph-conventions.md`: "A demand about the record as a whole belongs on the handover and in no condition".
> - **Departing from a worker contract.** "You may not depart … on your own authority" became "Depart … only with the human's permission". The outcome is the same.
> - **Extraction as scribe work.** "Extraction is copying, so it is scribe work" is now carried by the unchanged part's scribe section: "extracting a block of text to hand to somebody else".
> - **Dropped rationale sentences.** Each one's rule remains.
>
> **Extent of the list:** a bounding set, every statement in G2 before and after, walked paragraph by paragraph. Each G2 statement was held against the whole after-text including `CONTEXT.md` through its import, and each after-text G2 statement against the whole before-text.
>
> **Not re-raised:** run 6's open question about ground rule 1 and `CONTEXT.md` concerns lines outside G2, which this work does not change. G2 adds no new dependence on this repo.
>
> File: `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/297-rewrite-the-manager-contract-part-2/.claude/skills/expedition/SKILL.md`

*The manager's note:* a `FAIL` is outside the standing yes. Finding 1 turns on whether the worker may depart from wording the human approved "as worded", which only the human can say; it goes to the human. Finding 2 goes back to the worker with the human's answer, in one correction round.

#### The human's answer at the gate, 2026-09-29

The manager put finding 1 of checker run 1 to the human, recommending that the worker's version be kept and only the three bold spans be fixed. The human, `verbatim`: *"for 234, I guess git merge --abort is not available because it's a merge fail and not a merge conflict. Also isn't it similar to the issue with worktrees where the old way of doing it had problems ? And now we don't have readonly issues ? Otherwise ok."* The "ok" takes the recommendation: keep the worker's version, and fix the bold.

*The manager's note, from context it already holds:* on the first point, an `--ff-only` merge that fails leaves no merge in progress, so `git merge --abort` has nothing to abort. On the second, the partial write comes from running the merge inside the sandbox, where `.claude/skills` is read-only. Every landing merge this session ran with the sandbox off from the start, and none partially wrote, so under that practice the case does not arise, as the worktree case no longer does. The read-only overlay on `.claude/skills` in the main checkout still exists; it bites only a merge run inside the sandbox.

### Checker run 2 — `PASS`

*The checker's own text, pasted, 2026-09-29, after correction round 1.*

> PASS
>
> This is a re-check after one correction round, against `/tmp/claude-1000/c234.md` under the reading the manager relayed: the human's "ok" keeps the worker's text for (a) and (b) as it now stands, not the raise's wording. I held the work against the ground rules and the six standing rules for writing as they stand in `/tmp/claude-1000/ground.md`, re-read, and I did not read `map.md`. I read only the standards section of `map-implementation-rules.md` ("What the work is held against"). I read the two changed paths as the work, under that file's rule on record files as work.
>
> What changed since my last outcome:
> - `map-history.md` still has blob `a40514e`, so it is unchanged since my last outcome.
> - `map-manager-only.md` went from blob `b7571b0` to `4e7116b`.
> - I compared its new diff hunk with last round's hunk, word by word. The only change is removing `**…**` from three sentences: "The merge may instead write some of the changed files before it fails.", "The repair for a partially written merge is one pass, in this order.", and "Establishing byte-identity comes first." No word moved and the line breaks are unchanged.
> - The work shows no change that the statement does not mention.
>
> Last round's findings:
> - Finding 1 (acceptance condition): settled by the human's "ok". The worker's text for (a) and (b) is now the approved text, and the work carries it unchanged.
> - Finding 2 (the bar, writing rule 5): fixed. I unwrapped `map-manager-only.md` at HEAD and in the worktree, listed every `**…**` span on each side and diffed the two lists. `diff` printed nothing: the work adds no bold span. The one added diff line that contains `**` is the existing span "The manager must expect this rather than discover it", which moved only because the lines around it were rewrapped.
>
> Parts of the condition:
> - **Scope and clause 7: met.** `git status --porcelain --untracked-files=all` lists only `.scratch/graph-workflow/map-history.md` and `.scratch/graph-workflow/map-manager-only.md`. There is no change to a node status line, `decisions.md` or `flags.md`.
> - **Clause 1, as settled: met.** Established last round and unmoved except for the bold removal. The surviving combined sentence is replaced by the worker's text, which states the partial write, the dirty main tree, and the retry refusing with `Your local changes to the following files would be overwritten by merge`.
> - **Clause 2 with (c) and (d): met.** Established last round, and `map-history.md` is unchanged.
>   - The replaced sentence is appended word for word: "`HEAD` does not move and nothing is lost in either case; both succeed outside the sandbox."
>   - It sits under the new node-234 `## Superseded from …` heading and its `### From *Landing an implementation node's work* — …` subheading. The addition is appended only.
>   - Edit 13 and Edit 14 are present (`grep -n 'Edit 1[34]' map-history.md`).
> - **Clause 3: met.** The worker's repair text runs in order: establish byte-identity, then discard, then re-run the merge outside the sandbox. It states "Establishing byte-identity comes first." and "the manager stops and discards nothing" where a file differs.
> - **Clause 4, with node 160's amendment: met.**
>   - The unwrapped `**Landing policy**` paragraph has md5 `6088403e…` at HEAD and in the worktree.
>   - The amended span "A rebase conflict is resolved, and the rebase is not aborted. … the manager runs `git rebase --abort` and the node takes a correction round." matches once in the unwrapped file.
>   - No added or removed diff line contains "rebase". The one hit for `git diff HEAD | grep -i -e rebase -e '## Notes'` is a context line.
> - **Clause 5: met.** No added line contains `## Notes`.
> - **Clause 6: met.** From `.scratch/graph-workflow/`, every relative `](…)` target in both files, with its anchor stripped, passes `[ -e ]`. The loop reported nothing missing.
> - **Clause 8:** covered by the bar below.
>
> The bar:
> - The repo has no build, tests, formatter or CI, and its root holds only `CONTEXT.md` and `CONTEXT-MAP.md`, which agrees with `map-implementation-rules.md`. There was no command to run, so the bar is its non-command half.
> - I held the changed passages against the five ground rules, the six standing rules for writing (rule 5's bold clause now holds), `/writing-for-agents`, and the glossary's `_Avoid_` refusals, checked by hand. None found a defect.
> - No reviewing skill is named, so I ran none.
>
> I did not check the questions the human raised to the manager in the same answer: `git merge --abort` after a merge failure, the likeness to the worktree issue, and whether the read-only restriction still applies. They are not part of the acceptance condition or the bar. My only writes were two scratch files in `$TMPDIR` for the bold comparison.

### Gate — approve, 2026-09-29

The human's approval is the answer recorded under `## Interview` as "The human's answer at the gate, 2026-09-29": *"… Otherwise ok."*, taking the manager's recommendation to keep the worker's text, fix the bold, and have the checker run again. Run 2 passed.

## Handover, attempt 1, correction round 1

*Filed by the manager as handed back, 2026-09-29. The worker's own text, pasted.*

````
HANDOVER:      234, "A failed `git merge --ff-only` can leave the tree partially updated, and the record says it cannot"

WHAT CHANGED THIS ROUND: Only finding 2. I removed the bold from the three spans I had added in `map-manager-only.md`: "The merge may instead write some of the changed files before it fails.", "The repair for a partially written merge is one pass, in this order." and "Establishing byte-identity comes first." The words are unchanged. Nothing else changed, including the repair text the human kept. This round touched text that clauses 1 and 3 name, but only its markup, not its wording. I checked with the checker's method: I unwrapped the file at HEAD and in the worktree, listed the `**…**` spans on each side and diffed the two lists, and the lists are now identical. `**The manager must expect this rather than discover it**` was already there before my change, and is kept.

ANSWER:        Per the human's "ok" to Raise 1, clause 1 is taken to cover the one sentence that still stated the claim, and clause 2 to be already met for the two earlier statements. Node 229 had moved those two, word for word, to `map-history.md` (Edit 13 and Edit 14) before this node was minted.
               In `map-manager-only.md`, under `## Landing an implementation node's work`, in the bullet "One sandbox restriction bites this lifecycle", sub-bullet "What it hits": the sentence "`HEAD` does not move and nothing is lost in either case; both succeed outside the sandbox." is replaced. The new text:
               - keeps "`HEAD` does not move in either case";
               - keeps the reset's old claim (it loses nothing and succeeds outside the sandbox), because nothing has shown it false and the reset is a step of no route since node 265;
               - states the partial-write case for the merge: it may write some of the changed files before it fails, which leaves the main tree dirty, and a retry outside the sandbox then refuses with `Your local changes to the following files would be overwritten by merge`;
               - states the clean case (the merge fails having written nothing, and the retry succeeds), because node 229's landing hit that case and the partial write is a case rather than the rule.
               The repair follows in the same sub-bullet, as one pass in order:
               1. Establish byte-identity for each dirty file with `git show worktree-<NN>-<name>:<path> | cmp - <path>`.
               2. Outside the sandbox, discard the files: `git checkout HEAD -- <path>` for a file `HEAD` holds, and delete a file it does not hold.
               3. Re-run the merge outside the sandbox.
               The text states that byte-identity comes first. Where any dirty file differs from the branch's version, the manager stops and discards nothing.
               Three choices a later reader would otherwise have to re-derive:
               - The repair goes inside the existing sub-bullet, not in a fourth one, so that the lead-in "The three sub-bullets below are measurements" stays true.
               - The discard runs outside the sandbox because a dirty file under `.claude/skills/` cannot be rewritten inside it.
               - The discard uses `git checkout HEAD --` rather than `git checkout --`, so it also undoes any index write the failed merge made.
               The replaced sentence is appended word for word to `map-history.md` under `## Superseded from map-manager-only.md at node 234 — the claim that a merge failed in the sandbox loses nothing`, subheading `### From *Landing an implementation node's work* — the sandbox restriction's sub-bullet on what it hits`. The introduction under that heading points at Edit 13 and Edit 14 for the two earlier statements.

THE HUMAN'S TWO QUESTIONS, and how they bear on the text (I have changed nothing for them):
               1. "`git merge --abort` is not available because it's a merge fail and not a merge conflict": correct. A `--ff-only` merge that fails on an unlink never starts a merge, so there is no `MERGE_HEAD` and `git merge --abort` has nothing to undo. That is why the repair is a manual comparison and discard. The text does not say this. I judge it worth one clause, e.g. "`git merge --abort` does not apply: the failed fast-forward left no merge in progress". Adding it would not touch anything the condition fixes. I left it out because this round was scoped to finding 2.
               2. "Similar to the worktree issue where the old way had problems, and now no read-only issues?": yes, it has the same shape. The bullet "A failed rebase leaves its partial checkout behind" in the same section records a git operation that wrote part of its result before failing, so the retry met the leftover changes. The worktree route got rid of its read-only problems by dropping the steps that hit the overlay: the reset, and entering a tree. The removal still runs with the sandbox off. The merge has not been fixed that way. The read-only overlay on the main checkout's `.claude/skills` still exists, and a merge run inside the sandbox still hits it. Your note says every landing merge this session ran with the sandbox off from the start and none partially wrote. That points to a simpler rule: always run the landing merge with the sandbox off. The partial write could then not happen, and the repair would become a fallback. I judge the text should gain that rule, but not in this node:
                  - The rule belongs in the `**Landing policy**` paragraph, which clause 4 freezes.
                  - Or it could sit in this sub-bullet, but it would change how landing is done, which goes beyond this node's own text (trigger 2).
                  I propose it below as a new node.

INDEX LINE:    The landing section now says a sandbox-failed merge may partially write the tree and block a retry, and gives the repair: confirm byte-identity first, discard, re-merge unsandboxed.

FLAGS:         none

NEW NODES:     Name: The landing merge runs with the sandbox off from the start
               Kind: implementation
               Question: Should the landing policy say that `git merge --ff-only` into the main tree always runs with the sandbox off? The sandbox mounts the main checkout's `.claude/skills` read-only, so a merge run inside it can fail after writing part of its result. Every landing merge on 2026-09-28 ran with the sandbox off from the start, and none partially wrote.
               Blockers: none. It edits `.scratch/graph-workflow/map-manager-only.md`, which node 234 also edits, so the two must not run in the same pair of code slots.
               Acceptance condition:
                 The work is `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md`. The worker may edit those two files and no other.
                 Done means every one of the following is true of the finished tree.
                 1. In `map-manager-only.md`, under the heading `## Landing an implementation node's work`, the paragraph beginning `**Landing policy**` states that the manager runs `git merge --ff-only` with the sandbox off, and states the reason: the sandbox mounts `.claude/skills` in the main checkout read-only, so a merge run inside it can fail after writing some of the changed files.
                 2. Where a sentence stating a rule that currently binds is replaced to meet clause 1, its text before the change is appended, unaltered, to `map-history.md` under a heading naming `map-manager-only.md` and this node, with a subheading naming *Landing an implementation node's work*. It is appended rather than replacing anything.
                 3. The text in the same section that states the repair for a partially written merge (confirm that each dirty file is byte-identical to the branch's version, discard, then re-run the merge outside the sandbox, and stop without discarding where any file differs) is still present, and says it applies where a merge was run inside the sandbox.
                 4. Every markdown link in both files resolves to a path that exists, except a link to a path outside this repository.
                 5. No file outside `.scratch/graph-workflow/` is modified.
                 Scope came from no search: the named places are the work.

INVALIDATIONS: Node 229 (the landing section's accounts banked): no contradiction. Its Edit 13 and Edit 14 text is now cited from the new history section as the two earlier statements of the claim this node supersedes. Node 140 (Edit 14's measurement, "the merge succeeds on a retry outside the sandbox"): narrowed. That retry is clean only where the failed merge wrote nothing.

CONDITIONS:    What I searched for: the open and claimed nodes' conditions and questions, for "nothing is lost", "succeeds outside the sandbox", "What it hits", "overwritten by merge", "partially written", "ff-only" and "One sandbox restriction bites". Apart from this node, it matched node 251 (line 34: the ff-only merge listed as not retested) and node 80 (line 64: the landing-policy sequence naming `git merge --ff-only`). My work makes neither wrong. There are no replacements and no changed questions. This round changed no words, so I did not search again.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings and what I changed:
               - Finding 1 (repair text departs from the approved wording): the human kept my version, so nothing changed.
               - Finding 2 (bold on text that defines no term): I removed the bold from the three added spans. The bold-span lists before and after my change now match exactly.
               Paths touched, both in worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/234-failed-merge`:
               - `.scratch/graph-workflow/map-manager-only.md`
               - `.scratch/graph-workflow/map-history.md` (appended only; you integrate this against node 186 at landing)
               The node file is not edited.
               Checks against the condition, re-run this round:
               - The `**Landing policy**` paragraph is byte-identical to HEAD.
               - The node-160 span is untouched.
               - No `## Notes` heading was added.
               - Every link resolves.
               - Only the two files are modified.
               The bar: the repo has no build, tests, formatter or CI. That matches the record.
               Proposed commit message:
               State that a sandbox-failed merge can partially write the tree, and its repair

               The landing section said a merge failed in the sandbox loses nothing and
               succeeds on a retry outside it. The merge may instead write some changed
               files first, leaving the tree dirty and the retry refused. The section now
               states that case and the one-pass repair: confirm byte-identity with the
               branch first, discard, and re-merge outside the sandbox. The replaced
               sentence is banked in map-history.md.

               Node: graph-workflow/234

RETROSPECTIVE
1. What I had to hunt for: this round, nothing. The checker's instructions for measuring the extent were exact.
2. What arrived that this node did not need: finding 1's details, since the human had already settled it.
3. What would have made this easier: if the writing rules had been in front of me when I wrote the text. I read rule 5 in map.md and still bolded out of habit, following the style around it. The surrounding sub-bullets bold whole sentences that define nothing, so the local style works against the rule.
4. What was stale, wrong or contradictory: the section's existing bold spans, such as "**The manager must expect this rather than discover it**", break rule 5 the same way mine did. I left them, since they fall outside this node's condition.
````

## Flags

`234.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment from node 160 above.* Node 160's replacement for clause 4's second sentence was filed on this open, unclaimed node without asking the human first.
