# Rewrite the manager contract's third part in plain English

Type: implementation
Status: resolved
Blocked by: 297

## Question

Rewrite the third part of `.claude/skills/expedition/SKILL.md` in plain English and shorter, under the pass [node 289](289-a-plain-english-and-compaction-pass-over-the-shipped-files.md) settled.

> Beside the work, the handover carries three things. (1) For every open node whose `## Acceptance condition` quotes text or a heading from the before-text of what this node rewrites: either a replacement for each affected clause, quoting the after-text, or a proposal that the node be superseded as unnecessary, with the reason. Name the search you ran. (2) Every generalisation made, naming the statements it replaced. (3) Any rule judged dead or a default behaviour, reported as a new node and left in the text.

## Acceptance condition

*Authored by node 289's worker and filed by the manager. Node 289's worker's COMMON CLAUSES block, copied in full, then this node's own clauses, verbatim.*

**Terms.** *The before-text* of a file is that file as it stands at the commit this work's branch was created from, read with `git show $(git merge-base HEAD master):<path>` in the worktree. *The after-text* is the file in the worktree. *The rewritten range* is the part of the file this condition's own clauses name, or the whole file where they name no part.

1. **Nothing binding is lost.** Every binding statement in the before-text has a counterpart somewhere in the whole after-text that gives the same outcome in every case. The binding statements are: every rule, meaning every instruction, permission, prohibition or duty, and whose it is; every condition or exception attached to a rule; every fixed template; every term the text defines, and its definition; every word the text refuses; and the members and stated count of every closed list. A binding statement with no counterpart, or whose counterpart changes the outcome for any case, fails this clause.
2. **Nothing binding is added.** The after-text states no rule, permission, duty, exception, defined term or refused word that the before-text does not.
3. **Generalisation.** Several before-text statements may be replaced by one general statement only where every case each of them decided comes out the same under it, and it decides no case the before-text left undecided.
4. **Fixed text.** Everything inside code fences, and the frontmatter block at the top of the file where there is one, is byte-identical to the before-text.
5. **Headings.** A heading of the before-text whose exact text appears in any other of the following files keeps that exact text in the after-text: `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/graph-conventions.md`, `.claude/skills/expedition/wayfinder-divergences.md`, `.claude/skills/expedition-checker/SKILL.md`, `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-stop/SKILL.md`, `CONTEXT.md`, `.claude/rules/expedition-triggers.md`, `.scratch/graph-workflow/map.md`, `.scratch/graph-workflow/map-manager-only.md`, `.scratch/graph-workflow/map-implementation-rules.md`, `.gitignore`. Any other heading may be reworded, merged or removed, provided clause 1 holds.
6. **References inside the file.** Every reference the after-text makes to another part of the same file, such as "below", "above" or "under *X*", points at something the after-text holds.
7. **Terms.** Where the before-text uses a term defined in `CONTEXT.md`, the after-text spells that term as `CONTEXT.md` defines it wherever the idea recurs. The after-text uses no word that a `CONTEXT.md` `_Avoid_` line refuses, for the concept that line refuses it for, and coins no new term.
8. **Plain English.** Within the rewritten range, prose outside code fences has these six properties. The checker names each passage it judges to breach one, and which property it breaches.
   a. A rule is stated as what to do. A prohibition appears only where the rule cannot be stated as what to do, and then beside the positive statement.
   b. Bold appears only on a term at the place where it is defined. No clause or sentence is bolded for emphasis.
   c. An idea that is not a term defined in `CONTEXT.md` is said in plain words, with no figure of speech and no coined phrase. The following, from the shipped files, are the kind ruled out: "neither pen reaches", "rides a moment that already exists", "claimants", "in as many words".
   d. Statements are direct. No sentence is a slogan-shaped contrast or reversal, of the kind "the ban is about recording, not about files" or "amending is never authoring". No sentence uses "the whole of what".
   e. Every sentence is grammatical, and each "it", "this", "that", "they", "these" or "those" has one clear referent in the same sentence or the one before. The following is the kind ruled out: "Two things that is not, and neither is loosened by it."
   f. One idea per sentence. No sentence holds more than one dash-delimited aside, or more than one semicolon.
9. **Size, reported and not enforced.** The checker reports the `wc -w` count of the rewritten range in the before-text and in the after-text. The target is an after-text of at most two thirds of the before-text. Missing the target does not fail the work.
10. **Scope.** The work changes no path except those this condition's own clauses name, and within a named file, no text outside the rewritten range: that text is byte-identical to the before-text.

11. **Scope.** The work changes `.claude/skills/expedition/SKILL.md` and no other path. The rewritten range is:
    - G3: from the heading `## What is in front of the human, and when` to the end of the file.
    Clause 1's walk covers the binding statements in the before-text of the rewritten range. Their counterparts may be anywhere in the whole after-text.

## Amendment by the human, 2026-09-24

*The human approved the manager's proposal, `verbatim`: "ok". The proposal and the answer to A that prompted it are recorded on [node 290](290-rewrite-the-research-contract-as-the-pilot.md). The manager drafted the wording below, and the human amended the condition with it. The original clauses above are left as they were. The clauses below take the place of clauses 1 and 2, add clause 1a, and add a sentence to clause 3.*

1. **Lost or changed statements are rule changes.** The binding statements are: every rule, meaning every instruction, permission, prohibition or duty, and whose it is; every condition or exception attached to a rule; every fixed template; every term the text defines, and its definition; every word the text refuses; and the members and stated count of every closed list. A binding statement of the before-text that has no counterpart anywhere in the whole after-text, or whose counterpart changes the outcome for any case, is a rule change. The checker lists every rule change it finds, each with the before-text statement and its after-text counterpart, or "removed". A rule change does not fail the work.
1a. **Terms `CONTEXT.md` does not define.** A term the before-text defines that `CONTEXT.md` does not define may be dropped as a term, where its meaning is still stated in plain words at the place it was defined. Dropping a term that way is not a rule change.
2. **Added statements are rule changes.** A rule, permission, duty, exception, defined term or refused word that the after-text states and the before-text does not is a rule change. The checker lists it the same way as under clause 1. It does not fail the work.
3. *(added sentence)* A generalisation that changes an outcome, or decides a case the before-text left undecided, is a rule change under clause 1 or clause 2.

## Answer

Rewrote the manager contract's third part (What is in front of the human to the end) in plain English, 2,369 to 1,880 words; one answered open question removed.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The human approved the listed rule changes, and the checker's independent list is under `### Checker run 1`. The work landed as commit `9d8044c`. With nodes 296 and 297, the whole manager contract is now rewritten.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-25. The worker's own text, pasted. The flags are raised under `## Flags` at the gate.*

HANDOVER:      Rewrite the manager contract's third part in plain English

ANSWER:
I rewrote `.claude/skills/expedition/SKILL.md` from `## What is in front of the human, and when` to the end of the file, under the pass node 289 settled. The work is in worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/298-rewrite-the-manager-contract-part-3` and is uncommitted.

- Size (clause 9): the range went from 2,369 to 1,880 words by `wc -w`, which is 79%. The two-thirds target (about 1,579) was missed. What remains is mostly closed lists and rules with conditions attached.
- Scope (clauses 4, 5, 10, 11): lines 1–419 are byte-identical to `e6c43fb` (checked with `cmp`). The range has no code fences. `.claude/skills/expedition/SKILL.md` is the only changed path.
- Headings: the three that clause 5 protects keep their exact text. They are `## What is in front of the human, and when` (cited in `map.md`), `## When an agent dies or is stopped` (cited in `expedition-stop/SKILL.md`) and `## Closing an effort` (a heading in `CONTEXT.md`). `### Picking the next node`, `### Standing steering, and standing instructions of one effort`, `### Three states nothing in the files shows` and `## What nothing here settles` are also unchanged. One heading was renamed: `## Where two of these pull against each other` became `## Conflicts this contract leaves open`. No file cites it.
- Links with the rest of the file still work:
  - The pending queue still has the four members that item 5 of `## The order you act in` lists: three in tier 1 and the relayed question in tier 2.
  - "`### A flag in a payload` above" is kept.
  - The pick report is still defined in `### Picking the next node`, as "The pick report states the pick as work already under way. It names the node that just closed, and the node and kind you started."
- Style: the range has no bold, no dashes and no semicolons. The list items that used to end in ";" are now sentences. No line is over 104 characters. The spawn's refused-word grep finds nothing in the range.
- Clause 1a: I dropped the label "claimant", which `CONTEXT.md` does not define. Its meaning is now said in plain words: "Three things never enter the queue" and "A checker's question never enters the queue either."
- The rule that the human's approval settles a node's flags (the human's point 3): nothing in the range says it is one effort's instruction. `### Standing steering, and standing instructions of one effort` still states only the general duty to record an effort's own instructions as theirs.
- One rule change was made under ruling A: open question 2 was removed. It is listed under RULE CHANGES.

INDEX LINE:    Rewrote the manager contract's third part (What is in front of the human to the end) in plain English, 2,369 to 1,880 words; one answered open question removed.

FLAGS:
- ASSUMPTION: I judged that the shipped checker contract answers the manager contract's open question "Is a checker handed the route for holding work against this repo's standards, or does it go and find them?". The answer is in `## The standards you hold the work against`: "They are in one known file, you read that file, and you look nowhere else." The implementation contract says the same. So I removed the question and renumbered the list from nine items to eight. *Index:* The manager contract's open question on whether a checker finds its standards was judged answered by the checker contract, and removed.

NEW NODES:
- Name: The manager contract says three node states show in no file, while the stop skill derives each from the node's file
  Kind: implementation
  Question: `SKILL.md`'s `### Three states nothing in the files shows` tells the manager to keep track of three states itself, because the files show them only as `claimed` or `open`. `expedition-stop/SKILL.md`'s `## Write no handoff document` says each of the three is derivable from the node's own file. Should the manager contract state the derivations?
  Blockers: none
  Acceptance condition: In `.claude/skills/expedition/SKILL.md`, the section headed `### Three states nothing in the files shows` no longer states or implies that the three states cannot be read from the files. It states that each reads as `claimed` or `open` on the node's status line, and that each can be derived from the node's own file, as follows. Waiting at a gate: `claimed`, with a checker's outcome recorded and no gate outcome under it. A worker blocked on a raise: `claimed`, with a question recorded and no answer under it. Banked and waiting: `open`, with a non-empty interview. The section still tells the manager to report the first two without being asked, and the third when the human asks. The heading may be reworded. No other path changes. The working tree meets the bar.

INVALIDATIONS: none. Node 76's answer records "the nine nobody has settled" as what that node shipped. That is an account of the time, and it is not contradicted. The removed question was settled by the human's standing direction in `map.md` ("the rules a checker holds work against are given to it, never found by it"), which the checker contract carries.

GATE PAYLOAD:
- Checker findings: none yet, because no checker has run.
- Paths touched: `.claude/skills/expedition/SKILL.md` in the worktree. Scratch files outside the repo are in `/tmp/claude-1000/n298/`: `search.py` (node 297's copy, with 297 swapped for 298), `dump.py`, `wrap.py`, `handles.txt`, `hits5.txt`, `hits6.txt`, `draft.md`, `before_range.md`, `before_full.md`, `after_range.md`.
- The bar: the repo root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`, so there is no build, no tests, no formatter and no CI. The bar is its non-command half. The record matches: `map-implementation-rules.md` now lists the third `.gitignore` entry.
- Method skills: none invoked.
- Proposed commit message: `Rewrite the manager contract's third part in plain English` / blank / `Node: graph-workflow/298`

RULE CHANGES

Made under ruling A:
1. Open question 2 is removed. Before: "2. **Is a checker handed the route for holding work against this repo's standards, or does it go and find them?** The two are not equivalent: … so handing the route over narrows what a checker may fault work for. Nothing has priced that." After: removed, and items 3–9 are renumbered 2–8. Why it makes sense in the file: the file listed as unanswered a question the shipped checker contract answers ("They are in one known file, you read that file, and you look nowhere else."). The human settled it as a standing direction. Restoring it is one list item.

Borderline, listed so the checker's list can be matched. I judge each to keep its outcome unless the entry says otherwise.

2. Tier order. The after-text adds "tier 1 goes ahead of tier 2". The before-text implied this through the numbering and "The two tiers and arrival order have already chosen it", and `CONTEXT.md`'s Raise entry says a blocking raise "pre-empts grilling work in the manager's queue".
3. Parking. Before: "the human holds the release valve: parking the live question moves the queue on immediately" (a description). After: "When the human parks the live question, send the next thing in the queue at once." (a duty on the manager).
4. Asking which. Before: "Never ask the human which of the waiting things to take next.", then "Listing what is waiting and inviting them to pick hands them a choice the ordering has already made…" as a reason. After, one prohibition: "Never ask the human which waiting thing to take next, whether by a question or by listing what is waiting and inviting them to pick."
5. What the ask-which rule covers. Before: "a worker's question that genuinely offers options is that worker's question, relayed whole: this binds the reports you write yourself, never a payload you are carrying." After: "Relay a worker's question that offers options whole, as that worker's question. The rule against asking which thing to take applies only to the reports you write yourself." The word "genuinely" is dropped.
6. The relayed-question line. Before: "It is drawn from context you already hold" (a description). After: "Write it from context you already hold." It was stated twice before ("Naming in one line what else is waiting stays", and the separate paragraph). It is now stated once.
7. Flags in a pick report. Before, the contents of the fuller form were listed: "what was decided, why, and the context needed to answer without opening a file". After, the text only points at `### A flag in a payload` above, which says "what was done, why, and the context needed to answer it". "Decided" becomes "done".
8. Removed: "Having started it was not a mistake." Its duty stays as "Start a pick without waiting for permission." (before: "you were never holding the pick open waiting for permission to begin").
9. Code slots. Before: "One worker to a slot, and no free slot means no start." After: "A slot holds one worker. Where no slot is free, start no implementation node." This narrows the unspecified "no start" to implementation nodes, which is the bullet's subject.
10. Filling the counts. Before: "A count is a target to reach rather than a ceiling to stay under. When a node finishes you start enough work to fill every gap it leaves". After: "Each count is a number to reach. When a node finishes, start enough work to bring every count back up to its number". This also covers gaps the finishing node did not leave, which "target to reach" already implied.
11. Removed: "You cannot read a running agent's transcript or inspect a dead one". Before, this was the reason why "attempting the resume is the detector". Node 120's open condition treats reading a dead run's transcript as possible, so the claim is doubtful as well as not binding.
12. Third failure. Before: "a third failure is not a crash to retry … evidence the node is too coarse". After: "treat a third failure as evidence that the node is too large. Do not start another replacement."
13. Before: "A frontier that never empties is a legitimate steady state rather than a stalled one." After: "…is a legitimate steady state." "Rather than a stalled one" is dropped.
14. The closing report's flags. Before: "never reconstructed by you at report time". After: "never reconstructed by you".
15. Removed from the open question about checking flags: "And note the shape of the problem before you improvise:". The intro's "Do not invent an answer to one when you meet it" covers it.
16. Final paragraph. Before: "Where you find one, that is a node rather than something to settle in the moment." After: "Where you find one, mint a node for it. Do not settle it yourself."
17. The first conflict no longer restates "You never re-author what an agent wrote". Its counterpart is `### You write as a scribe`.
18. Standing steering: the reasons are cut ("which is its only durable home — steering held only in your context dies with your thread", "so an emphasis nobody remembers setting cannot be silently forgotten"). The counterpart for "only home" is `## Words used exactly`: the steering lives in the map "and nowhere else".
19. A stopped agent. Before: "a stop is handled as a fresh attempt rather than as a re-prompt". After: "Handle a stop by starting a fresh attempt, never by re-prompting the stopped agent."
20. The heading `## Where two of these pull against each other` is renamed `## Conflicts this contract leaves open`.

Reasons cut, none of them binding:
- "The cost is bounded to one answer's latency"
- "a name and a kind invite nothing"
- "keeping it to a name and a kind is what keeps a terse reply attributable to exactly one thing"
- the which-node reasons: it occupies the channel, a pick is cheap to undo, the override is one line
- "the forbidden question in the shape of a statement" (kept as the duty "Continue without waiting for a reply.")
- why the report goes out at the start (kept as the duty "send the pick report as you start it")
- "The duty bites hardest on a node the human never met…"
- "Their questions do not collide…"
- "Replay re-inflates exactly the context that killed the previous attempt"
- "on an open-ended effort, a report replaying everything would be unreadable"
- "The channel exists" in the open question about invalidations
- "Nothing does today" becomes "Nothing does".

RE-POINTING SEARCH
Method: I extracted the `## Acceptance condition` section, amendments included, of every node whose status is `open` or `claimed`, leaving out node 298. I normalised the text and matched (a) every 6-word run and then every 5-word run of the normalised before-range, and (b) 150 handles in `/tmp/claude-1000/n298/handles.txt`. The handles are all eight headings of the range, plus the words and phrases my work removes or replaces. Among them: claimant(s), release valve, not an extensible rule, Two things that is not, genuinely offers options, rides a moment, terse reply attributable, forbidden question, cheap to undo, was not a mistake, target to reach, ceiling, fill every gap, only durable home, dies with your thread, volunteer, Death is discovered, detector, A key that fails, re-prompt, agent instance, re-inflates, too coarse, recoverable state, delta scoped, stalled one, at report time, Named rather than resolved, scribe boundary, pull against, handed the route, priced, unblind, before you improvise, hardens there, where the hole is, One limit of this contract, three things are not, not claimants, nine, item 2 to item 9, how many implementation nodes run at once, whoever holds the code slot, Some of what binds you, pick report, the report that precedes a close. Scripts: `/tmp/claude-1000/n298/search.py` and `dump.py`.

Replacement clauses (every word is fixed by this node's after-text):
- Node 101: replace "The existing paragraph beginning *"Some of what binds you on a given effort is a **standing instruction of that effort's human**"* is kept" with "The existing paragraph beginning *"Some of what binds you on a given effort is a standing instruction of that effort's human, and not a rule of this workflow."* is kept". The rest of that sentence is unchanged.
- Node 105: replace "its two tiers and its list of things that are not claimants are unchanged" with "its two tiers and its list beginning *"Three things never enter the queue:"* are unchanged". Its "the file's list of duties nobody has settled is not reduced" binds only its own work. That list now holds eight items.
- Node 118, clause 6: replace "the sentence beginning *"Three things are not claimants at all"* together with the three things it names" with "the sentence *"Three things never enter the queue:"* together with the three things it lists". The manager's note under that condition ("the sentence that lists three non-claimants") needs the same wording change, but it is the manager's text, not a clause.
- Node 161, clause 1: replace "The bullet beginning `**how many implementation nodes run at once**`" with "The bullet beginning `How many implementation nodes run at once.`".
- Node 161, clause 2: replace "reading `**What does a worker do when a file it must read is being changed by whoever holds the code slot?**`, together with the two sentences under it" with "reading `What does a worker do when a file it must read is being changed by whoever holds the code slot?` (now item 5), together with the two sentences after it". Its clause 5 holds as written.
- Node 280, clause 1: replace "`## What nothing here settles` item 5" with "`## What nothing here settles` item 4, the item reading *"Does anything tell a worker to look at the record when it reports what its work invalidates?"*". The rest of the clause is unchanged, and so is clause 2.
- Node 96, clause 6: replace "the nine duties listed as unsettled are not reduced to eight" with "the eight duties listed as unsettled are not reduced to seven". The manager's read-back under it says "the nine unsettled duties", which is the manager's text.

Matches that need nothing:
- Node 111: "the report that precedes a close" and `## Closing an effort` are kept word for word. Its "fourteen headings" is a dated enumerator. The file still has 15 `## ` headings.
- Node 120: its heading is kept. The after-text still says "An agent the human stopped cannot be resumed either", so its clause 3 still applies as written.
- Node 127: clause 4 forbids the "terse reply attributable" reason, which is now gone. Clause 6 already allows the non-claimants to be renamed.
- Node 137: its clauses 6 and 7 say to re-run their enumerators. The range now has 6 occurrences of "pick report" (5 before), and 1 of "closing report" (1 before).
- Node 285: `### Picking the next node` is kept.
- Node 160: the match is in an annotation, not a clause. The annotation question is still open, as item 6.
- Nodes 106, 90 and 247 target `CONTEXT.md`. Nodes 41, 208, 214, 312, 81, 92, 155, 211 and 256 match on shared phrasing only. Nodes 210, 221, 288 and 49 match only on "nine". Rewrite nodes 291–302 match only because their common clauses quote the ruled-out examples.
- Not a condition, for node 301: `expedition-stop/SKILL.md` says "tier 1 claimants in your contract's `What is in front of the human, and when`". "Tier 1" still exists there, but "claimant" no longer appears in the manager contract.

GENERALISATIONS
- Rule change 10: "fill every gap it leaves" became "bring every count back up to its number".
- Rule change 4: the ask-which prohibition and the listing-and-inviting sentence became one prohibition.
- No others. The two statements of the relayed-question line were merged into one, which removes a repeat without generalising.

RETROSPECTIVE
(1) What I had to hunt for:
- Which open conditions quote the range. The script at `/tmp/claude-1000/n297/search.py` worked once I swapped 297 for 298.
- Which of the range's headings other files cite. I grepped the 16 files.
- Whether open question 2 is still open. The answer was in the checker contract's `## The standards you hold the work against`.
- That the stop skill uses "tier 1 claimants" and states the three states differently. I found both by grepping for "tier".
- That nodes 96 and 280 depend on the numbering of the open questions. The handle search found them only after I added "nine" and "item N".

(2) What arrived that this node did not need:
- `map.md`, read whole. Only the worktree paragraph and the pointer to the writing rules mattered.
- Node 297's file, read for style. Its handover's RULE CHANGES, its checker run 1 and its gate correction were the useful parts. The spawn could have named those headings.
- The spawn's point 1, about what a worker may write. It bears on nothing in this range.
- Nearly all of `map-implementation-rules.md` beyond writing rule 5.

(3) What would have made this node easier:
- A spawn listing the open nodes whose conditions quote the range, since the manager can run the shared script (node 313).
- A script that skips the ruled-out examples in the common clauses of 291–302, which match in every search.
- A note that a numbered list's positions are cited by other conditions (96, 280, 161).

(4) What was stale, wrong or contradictory:
- Open question 2 was already answered by the checker contract.
- The stop skill says the three states are "derivable from the node's own file", against this contract's "Three states nothing in the files shows" (NEW NODES above).
- The before-text's "You cannot read a running agent's transcript" is against node 120's condition, which reads transcript record counts.
- Node 101's condition asks for strike-in-place in a shipped file, which `map.md` says the never-delete rule does not cover.
- Node 96's "nine duties" and node 118's manager note were already fragile against any renumbering or renaming.

## Review

### Checker run 1 — `PASS`, under the amended condition

*The checker's own text, pasted, 2026-09-25. The checker was resumed from node 297's check.*

> PASS
>
> This is node 298, "Rewrite the manager contract's third part in plain English". I started from the givens only and carried over nothing from nodes 296 or 297. I re-read the checker contract as it now stands.
> - The worktree is `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/298-rewrite-the-manager-contract-part-3`.
> - The before-text is `git show e6c43fb:.claude/skills/expedition/SKILL.md`, which is the merge-base.
> - The rewritten range G3 is before-text lines 420–628 and after-text lines 420–601, from `## What is in front of the human, and when` to the end of the file.
> - I walked clauses 1 and 2 separately.
>
> **Clause by clause:**
> - **Clauses 1 and 2:** walked. The results are under RULE CHANGES below. None of them fails the work.
> - **Clause 1a:** one before-text term is dropped. "Claimants" is not a `CONTEXT.md` term. Its meaning is stated in plain words where it was used: "Three things never enter the queue" and "A checker's question never enters the queue either". It is not a rule change.
> - **Clause 3:** holds. The generalisations that change an outcome or decide an open case are listed as rule changes.
> - **Clause 4:** holds. The frontmatter is byte-identical, and G3 has no code fences in either the before-text or the after-text.
> - **Clause 5:** holds.
>   - `## Where two of these pull against each other` became `## Conflicts this contract leaves open`. That exact text appears in none of the other listed files. I grepped both the worktree and the main tree. The main tree's only hit is its own copy of this same file, which clause 5 excludes.
>   - Every other G3 heading is byte-identical.
> - **Clause 6:** holds.
>   - Each reference resolves: "the queue above", "under `### A flag in a payload` above" (a heading at after-text line 283), "the three states below", "Each conflict below" and "Each item below".
>   - "Where two of these pull against each other" resolves to nothing in the after-text, so no reference is left pointing at the renamed heading.
> - **Clause 7:** holds.
>   - The `_Avoid_` scan found only uses outside the refused concept: "blocked", "retry the resume" (a repeated resume, not a name for an attempt), and "not complete".
>   - I also checked by hand. `CONTEXT.md` terms are spelled as it defines them, and no new term is coined.
> - **Clause 8:** holds.
>   - 8a: each prohibition sits beside its positive statement.
>   - 8b: G3 has no bold.
>   - 8c: the before-text's figures are gone, including "release valve", "bites hardest", "hardens there", "claimants" and "stands where the hole is".
>   - 8d: no slogan remains.
>   - 8e: I checked every pronoun, and each has one clear referent.
>   - 8f: no sentence has more than one dash aside or more than one semicolon.
>   - No line is longer than 106 characters.
>   - Borderline, not counted: line 30–31, "It happens at a moment that already exists", which keeps the ruled-out example without the figurative "rides". Line 33, "takes no turn in it". Line 103, "The claim belongs to the node, not to the agent", which is a contrast but a direct one.
> - **Clause 9 (reported, not enforced):** `wc -w` of G3 is 2369 before and 1880 after, which is 79%. The target is at most 1579, so it was missed.
> - **Clauses 10 and 11:** hold. `.claude/skills/expedition/SKILL.md` is the only changed path, and nothing is untracked. Everything before `## What is in front of the human, and when` is byte-identical to the before-text (`cmp`). G3 runs to the end of the file, so nothing follows it.
>
> **The bar.** The repo root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. It has no manifest, task runner, formatter or CI, so there is no command to run and nothing was printed. The non-command half is met.
> - The standards I read are in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md`. They are the ground rules, the five standing rules for writing, `/coding-principles` and `/naming`, `CONTEXT.md`'s `_Avoid_` lines, `graph-conventions.md` and `/writing-for-agents`.
> - Those that bore on this work are the ground rules, writing rules 1 and 5, the `_Avoid_` lines and `/writing-for-agents`.
> - G3 adds nothing that assumes this repo, this machine or a toolchain.
> - The file names no reviewing skill, so I ran none. The changed path is a shipped skill file, not a record file.
>
> RULE CHANGES
>
> Clause 1. For each entry: the before-text statement in G3, then its counterpart.
> 1. **How much to start when a node finishes.** Before: "When a node finishes you start enough work to fill every gap it leaves, which is sometimes more than one node." After: "When a node finishes, start enough work to bring every count back up to its number, which is sometimes more than one node."
>    - The before-text filled the gaps that node leaves. The after-text fills every gap, including one that was already open before the node finished.
> 2. **What nothing here settles, item 2.** Before: "**Is a checker handed the route for holding work against this repo's standards, or does it go and find them?** … Nothing has priced that." After: removed.
>    - It goes with the section's "Do not invent an answer for one in the moment" as it applied to this question. The list drops from nine items to eight.
> 3. **What a flag at the pick report carries.** Before: the pick report carries flags "in the fuller form under `### A flag in a payload` above — what was decided, why, and the context needed to answer without opening a file". After: "in the fuller form under `### A flag in a payload` above", with no restatement.
>    - That section says "what was done, why, and the context needed to answer it". So the pick-report form now reads "what was done" where G3 said "what was decided". The difference is small, and I list it for completeness.
> 4. **A duty that no rule states.** Before: "Where you find one, that is a node rather than something to settle in the moment." After: "Where you find one, mint a node for it. Do not settle it yourself."
>    - The before-text barred settling it in the moment. The after-text bars you from settling it at any time.
>
> Clause 2. For each entry: a statement the after-text makes that the whole before-text does not.
> 5. **Tier order.** Line 7: "The queue has two tiers, and tier 1 goes ahead of tier 2."
>    - The before-text numbered the tiers and said "The two tiers and arrival order have already chosen it". It never stated which tier goes first.
>
> **Checked and not counted as rule changes:**
> - **Parking.** "parking the live question moves the queue on immediately" became "When the human parks the live question, send the next thing in the queue at once". The outcome is the same.
> - **Relaying a question with options whole.** "this binds the reports you write yourself, never a payload you are carrying" became "applies only to the reports you write yourself". The outcome is the same.
> - **Death.** "a third failure is not a crash to retry" became "Do not start another replacement". The outcome is the same.
> - **Standing steering.** The map as its "only durable home" became "Write it into the effort's map". The Words list already says steering lives in the map "and nowhere else".
> - **Outstanding flags.** "never reconstructed by you at report time" became "never reconstructed by you". The outcome is the same in every case that arises.
> - Every dropped rationale sentence leaves its rule standing.
>
> **Extent of the list:** a bounding set. It is every G3 statement before and after, walked paragraph by paragraph. I held each before-text statement against the whole after-text, including `CONTEXT.md` through the "Every term in this contract means what the glossary, `CONTEXT.md`, defines it to mean" line before G3. I held each G3 statement of the after-text against the whole before-text.
>
> File: `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/298-rewrite-the-manager-contract-part-3/.claude/skills/expedition/SKILL.md`

*The manager's note, matching the two lists:* the checker's rule changes 1–5 are the worker's 10, 1, 7, 16 and 2. Every one is on the worker's list.


### Gate — approve, 2026-09-25

The human, `verbatim`: *"approve"*. *The manager's note:* given after the manager corrected the gate payload's attribution of the sentence behind rule change 1 (see the note under `298.1`).

## Flags

`298.1` **· settled** `ASSUMPTION` — I judged that the shipped checker contract answers the manager contract's open question "Is a checker handed the route for holding work against this repo's standards, or does it go and find them?". The answer is in `## The standards you hold the work against`: "They are in one known file, you read that file, and you look nowhere else." The implementation contract says the same. So I removed the question and renumbered the list from nine items to eight.
*The manager's note:* node 294's worker reported that the quoted sentence is the implementation contract's, under `## The standards your work is held to`, not the checker contract's. The manager checked: the landed checker contract's `## The standards you hold the work against` says instead "The standards are in `.scratch/<effort>/map-implementation-rules.md` … List `.scratch/` once to resolve the path, and do no other looking." The manager's gate payload repeated the wrong attribution, and the human was told.
