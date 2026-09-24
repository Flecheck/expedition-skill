# Rewrite the research contract in plain English, as the pass's pilot

Type: implementation
Status: resolved

## Question

Rewrite `.claude/skills/expedition-research/SKILL.md` in plain English and shorter, under the pass [node 289](289-a-plain-english-and-compaction-pass-over-the-shipped-files.md) settled.

> Beside the work, the handover carries three things. (1) For every open node whose `## Acceptance condition` quotes text or a heading from the before-text of what this node rewrites: either a replacement for each affected clause, quoting the after-text, or a proposal that the node be superseded as unnecessary, with the reason. Name the search you ran. (2) Every generalisation made, naming the statements it replaced. (3) Any rule judged dead or a default behaviour, reported as a new node and left in the text.

## Acceptance condition

*Authored by node 289's worker and filed by the manager. Written out whole by node 289's worker, because the pilot is claimed first.*

**Terms.** *The before-text* of a file is that file as it stands at the commit this work's branch was created from, read with `git show $(git merge-base HEAD master):<path>` in the worktree. *The after-text* is the file in the worktree. *The rewritten range* is the whole of `.claude/skills/expedition-research/SKILL.md`.

1. **Nothing binding is lost.** Every binding statement in the before-text has a counterpart somewhere in the whole after-text that gives the same outcome in every case. The binding statements are: every rule, meaning every instruction, permission, prohibition or duty, and whose it is; every condition or exception attached to a rule; every fixed template; every term the text defines, and its definition; every word the text refuses; and the members and stated count of every closed list. A binding statement with no counterpart, or whose counterpart changes the outcome for any case, fails this clause.
2. **Nothing binding is added.** The after-text states no rule, permission, duty, exception, defined term or refused word that the before-text does not.
3. **Generalisation.** Several before-text statements may be replaced by one general statement only where every case each of them decided comes out the same under it, and it decides no case the before-text left undecided.
4. **Fixed text.** Everything inside code fences, and the frontmatter block at the top of the file, is byte-identical to the before-text.
5. **Headings.** A heading of the before-text whose exact text appears in any other of the following files keeps that exact text in the after-text: `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/graph-conventions.md`, `.claude/skills/expedition/wayfinder-divergences.md`, `.claude/skills/expedition-checker/SKILL.md`, `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition-stop/SKILL.md`, `CONTEXT.md`, `.claude/rules/expedition-triggers.md`, `.scratch/graph-workflow/map.md`, `.scratch/graph-workflow/map-manager-only.md`, `.scratch/graph-workflow/map-implementation-rules.md`, `.gitignore`. Any other heading may be reworded, merged or removed, provided clause 1 holds.
6. **References inside the file.** Every reference the after-text makes to another part of the same file, such as "below", "above" or "under *X*", points at something the after-text holds.
7. **Terms.** Where the before-text uses a term defined in `CONTEXT.md`, the after-text spells that term as `CONTEXT.md` defines it wherever the idea recurs. The after-text uses no word that a `CONTEXT.md` `_Avoid_` line refuses, for the concept that line refuses it for, and coins no new term.
8. **Plain English.** Prose outside code fences has these six properties. The checker names each passage it judges to breach one, and which property it breaches.
   a. A rule is stated as what to do. A prohibition appears only where the rule cannot be stated as what to do, and then beside the positive statement.
   b. Bold appears only on a term at the place where it is defined. No clause or sentence is bolded for emphasis.
   c. An idea that is not a term defined in `CONTEXT.md` is said in plain words, with no figure of speech and no coined phrase. The following, from the shipped files, are the kind ruled out: "neither pen reaches", "rides a moment that already exists", "claimants", "in as many words".
   d. Statements are direct. No sentence is a slogan-shaped contrast or reversal, of the kind "the ban is about recording, not about files" or "amending is never authoring". No sentence uses "the whole of what".
   e. Every sentence is grammatical, and each "it", "this", "that", "they", "these" or "those" has one clear referent in the same sentence or the one before. The following is the kind ruled out: "Two things that is not, and neither is loosened by it."
   f. One idea per sentence. No sentence holds more than one dash-delimited aside, or more than one semicolon.
9. **Size, reported and not enforced.** The checker reports the `wc -w` count of the file's before-text and after-text. The target is an after-text of at most two thirds of the before-text. Missing the target does not fail the work.
10. **Scope.** The work changes `.claude/skills/expedition-research/SKILL.md` and no other path.
11. **The two shared sections.** The after-text holds a section headed exactly `## When you raise a flag` and a section headed exactly `## When a node you report is an implementation node`, each a `##` section of its own, and clauses 1 to 8 hold for each of them. Four later nodes copy these two sections byte for byte into the other worker contracts.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-23. The worker's own text, pasted. The flags are raised under `## Flags` at the gate.*

### Answer

I rewrote `.claude/skills/expedition-research/SKILL.md` in plain English under standing writing rule 5, as the pilot of the pass node 289 settled. The frontmatter and the handover code fence are byte-identical to the before-text. Every heading that other files cite keeps its exact text: `## Words used exactly`, `## What you read`, `## Hard rules`, `## What you hand back`, `## When you raise a flag` and `## When a node you report is an implementation node`. The two uncited headings, `# Research worker contract` and `## How you research`, are also unchanged. The seven hard rules keep their numbers, because other text refers to them by number: "hard rules 4 to 6" in this file, and node 57's "hard rule 3".

*Size.* The file went from 1,517 to 1,306 words by `wc -w`, 86% of the before-text. Three things kept it large:
- About 105 words are fixed text: the frontmatter and the code fence.
- The six defined terms in `## Words used exactly` (117 words) keep their definitions.
- Splitting stacked sentences into one idea each added words back.

*What was cut:*
- **Reasons not needed to apply a rule:** "That is what this kind of node is for" · "Such a skill was written for an agent working alone" · "because then nothing else records what produced the flag" · "Its cap is stated here so you need not open the file" · "You are the party that holds what it takes … nobody holds that again until a worker claims the node" · "each sends its reader away to learn what is being asked of them" · "there being no bounded material to bring inside the text"
- **Repetition:** "you have no channel to the human" in the opening, which hard rule 3 already says · "handed you one node" · "never as a tidy-up afterwards", which "write both when you raise the flag" already covers · "It never writes your sentence for you", which "the manager adds only bookkeeping" and "you write both" already cover.
- **Slogans and figures of speech:** "The graph-file ban is about recording, not about files": the rule is now carried by hard rules 1 and 2 · "the whole of the discipline" became "your entire method" (I avoided "complete" because `CONTEXT.md` refuses it for *resolve*) · "paid for there" became "So any loose wording you write here can stop that node." · "report-shaped", "read cold" and "hold what it takes" are gone.

*What was kept word for word*, so that open acceptance conditions still match: "Read each of these. Do not trust any summary of them." and the four pointer bullets (node 155) · Hard rule 3 (node 57) · "Report `NEW NODES` and `INVALIDATIONS` yourself. Nothing else reports them." (node 43) · The phrases "against those four" and "self-contained" (node 109's enumerators) · "written by the node that spawned it" (node 55).

*Bold* now appears only where a term is defined: research, the six listed terms, entry, acceptance condition, self-contained, checker, the bar.

*Carried over unchanged, as node 289 requires:* the pointer bullet saying `map.md` holds "the fog". It is stale, and I report it under `NEW NODES`.

*The two shared sections* are written for any contract, and nothing in them is specific to research. The four later nodes can copy them byte for byte.

**Generalisations made:**
1. **The account of what produced a flag.** Before (the `## Flags` bullet): "Except where your node holds no round at all — no exchange with the human, and no gate — … this entry carries that account itself: what you actually did, in your words." Before (the last paragraph): "What produced the flag is a different artifact: the round that created it … carries that account, and where your node has no round the `## Flags` entry above carries it instead." After: "The round that created the flag, an `## Interview` attempt or a `## Review` round, holds the account of what produced the flag. If your node holds no round at all, meaning no exchange with the human and no gate, your `## Flags` entry holds that account instead: what you actually did, in your words." Every case comes out the same.
2. **Recording on the graph.** Three statements became hard rule 2, "Leave all recording on the graph to the manager, whatever your node's work is. The manager writes your answer onto your node, marks it, resolves it, and writes its lines in `decisions.md` and `flags.md`." It replaces: from hard rule 1, "Bookkeeping on the graph is the manager's job; yours is to do your own work and never record it when you finish." · from hard rule 1, "Marking your node, resolving it, and its lines in `decisions.md` and `flags.md` stay the manager's whatever your node's work is." · from hard rule 2, "You never resolve your node, never mark it … You hand your answer back and the manager writes it." All of these applied in every case, and the merged rule does too.
3. **The source declarations.** "a **standing over sources** by path or glob: which sources are authoritative, …" became "It may also declare, by path or glob, which sources are authoritative, which are evidence only, and which hold statements known to be false." The label is used nowhere else in this file, so no case changes. This is flag 1.

**Rules judged dead or default behaviour:** none. I suspected the method-skill conflict paragraph was dead, because no contract tells a worker to invoke a method skill any more. Node 113's Answer, under "What is deliberately not removed", keeps it on purpose: a worker may still invoke one on its own initiative.

### Index line

The research contract is rewritten in plain English at 86% of its size, every rule kept, fences and cited headings byte-identical, and its two shared sections ready to copy.

### Flags, as handed back

`ASSUMPTION` 1: `standing over sources` is said in plain words. *For the node:* Clause 1 of the condition keeps every term the text defines. Clause 8c rules out coined phrases for ideas that `CONTEXT.md` does not define. "standing over sources" is both, so I described what the declaration says (which sources are authoritative, which are evidence only, which hold statements known to be false) and dropped the label. The label is not used again in this file, so no case changes. `map.md`, the manager contract and `graph-conventions.md` still use the label. *For the index:* The pilot says the source declaration in plain words and drops the undefined label "standing over sources", which other shipped files still use.

`ASSUMPTION` 2: some passages were left word for word so that fewer conditions need re-pointing. *For the node:* Where a passage was already plain enough, I kept its exact words so that open acceptance conditions keep matching. These are the opening sentence and bullets of `## What you read` (node 155), hard rule 3 (node 57), the `NEW NODES`/`INVALIDATIONS` sentence (node 43), and "against those four" and "self-contained" (node 109). I chose stable text over a fuller rewrite. *For the index:* The pilot keeps several plain-enough passages word for word so that open conditions quoting them need no re-pointing.

### New nodes

Filed as [node 304](304-four-worker-contracts-say-map-md-holds-the-fog.md) and [node 305](305-whether-standing-over-sources-becomes-a-glossary-term.md), each carrying the worker's text.

### Invalidations

none. Node 50's duplication, node 58's recording-not-files meaning and node 113's kept method-skill paragraph are all preserved.

### Gate payload

- *Checker findings:* none received yet.
- *Paths touched:* `.claude/skills/expedition-research/SKILL.md` only, uncommitted in the worktree. My scratch files are under `$TMPDIR/n290`, outside the repo.
- *The bar:* the repo states no build, test or format commands (no manifest, no agent instructions file at the root). That matches `map-implementation-rules.md`, so the bar is its non-command half.
- *Proposed commit message:* `Rewrite the research contract in plain English` / blank / `Node: graph-workflow/290`

### Re-pointing duty

*What I searched:* all 145 open or claimed nodes, and their 96 `## Acceptance condition` sections. (a) Quotes: every span in double quotes, curly quotes, `*…*`, backticks, or single quotes of at least 12 characters, normalised and checked as a substring of the before-text. (b) Mentions: `expedition-research`, "research contract", "five worker contracts" and similar. (c) The removed and replaced wording: graph-file ban, about recording, not about files, no channel to the human, whole of the discipline, Rules 4 to 6, standing over sources, never becomes authority, what this kind of node is for, hard rules govern, unrun, five parts, never leave a part off, onto the graph unaltered, two caps, report-shaped, read cold, tidy-up, cap is stated here, never writes your sentence, flag's entry, different artifact, cannot be claimed until, holds what it takes, holds that again, in silence, self-contained text, may say where, the demand itself, copy into, one exemption, quantif, bounded material, against those four, worker's to fix, paid for there, loosely, carries where you read it, fill the space, plausible answer, consumed by the manager, no way to reach the human, waits on them, Do not trust any summary, is not yours, Leave it unread.

*Two nodes need a replacement clause:*
- **Node 148, clause 1.** It points at "the bullet beginning `a **path** may say where`". Replacement: "the bullet beginning `A path may say where, because the checker has the repo` in `.claude/skills/expedition-research/SKILL.md`, and in any of the five not yet rewritten, the bullet beginning `a **path** may say where`". Once nodes 291 to 294 land, all five start with the after-text form.
- **Node 279, clause 1.** The quoted sentence is gone. Replacement: "the passage *"The worker that claims the node may not fix a condition it judges wrong. That node stops instead, and the condition goes to the human. So any loose wording you write here can stop that node."* states in addition …", with the rest of the clause unchanged.
- **Node 279, clause 3.** Replace "that what the reporting worker writes loosely is paid for by a later worker" with "that loose wording by the reporting worker can stop the node it reports".
- **Node 279, clause 2**, which says the five files are "not unified onto one sentence", already contradicted node 50 before this work. Now it contradicts the byte-for-byte copying as well. Changing that demand is for the manager or the human, not me.

*Matched but needing no change:* 155, 57 and 43: the text they quote is kept word for word; node 43's quantify rule is kept in meaning · 109: "against those four" is kept · 41: the `FLAGS:` line is inside the fence · 60: "five parts" is still stated · 61: the heading is kept, and the handover paragraph still spells out the idea; its premise about the opening paragraph was already false for this file · 55: "written by the node that spawned it" is kept · 73 and 79: they only say their own work does not change this file · 291 to 294: they copy the two sections · the rest are hits on other files' `## Notes` or `## Flags` headings.

### Trade-offs for the human to settle at the gate

1. **How deep to cut.** Some short reasons are still in the file, about 50 words: "because the checker has the repo" · "because it reaches the checker by its own route" · "because a node reported without one cannot be worked at all" · "No copy can repair such a demand" · "So any loose wording you write here can stop that node". I kept them because each helps a reader apply the rule, and node 279 treats the last as content to keep. Getting near two thirds would mean cutting these and shortening the defined-term list, which overlaps `CONTEXT.md`.
2. **Label versus plain words** for `standing over sources` (flag 1).
3. **Stable text versus a fuller rewrite** for the passages open conditions quote (flag 2).

### Retrospective

1. **What I had to hunt for:** Which headings other files cite: I grepped the 15 files clause 5 lists · Which open conditions quote the before-text: I extracted every open condition and wrote a script to match their quoted spans; the spawn gave me the duty but no enumerator; I first tried a plain grep for the path · Whether the shared sections really are byte-identical today: I diffed them; they are, apart from one trailing blank line · Whether the method-skill paragraph is dead: I looked first at `decisions.md`, whose line on node 113 is ambiguous; the answer was in node 113's Answer, under "What is deliberately not removed" · Where the fog lives: in `graph-conventions.md`'s map-shape passage.
2. **What arrived that this node did not need:** `decisions.md` whole (about 7,000 words): I used three lines of it (nodes 50, 113 and 289) · `map.md` whole: I used only the pointer to the fifth writing rule · The implementation contract's sections on the gate, correction rounds and the checker: none of them bear on a prose rewrite · Node 289's "Which files it covers" and "The nodes". A pass node whose condition is self-contained could skip `decisions.md`. The spawn could instead name the few resolved nodes the rewrite touches: 50, 58 and 113.
3. **What would have made this easier:** The spawn could carry a ready-made enumerator for the re-pointing search, such as the quote-matching script · The condition could say whether a stated consequence ("paid for there") counts as binding · The condition could say how clause 1 and clause 8c resolve for a term the file defines that `CONTEXT.md` does not · The spawn could note that the shared sections are byte-identical today.
4. **What was stale, wrong or contradictory:** The "`map.md` — … the fog" bullet in four contracts is stale · Node 61's premise is false for this file: the research contract's opening never spelled out the scribe idea · Node 279's clause 2 contradicts node 50 · Node 148's clause 7 still counts the map's standing preferences as part of the bar, which nodes 169 and 184 struck.

## Review

### Checker run 1 — `FAIL`, acceptance condition

*The checker's own text, pasted, 2026-09-23.*

> **FAIL: acceptance condition**
>
> The bar holds. Clauses 1 to 7, 9 and 10 are met. The work fails on clause 8, properties a and e, and those breaches also reach clause 11. All the failing text is short and cheap to fix, but it matters most in the two shared sections, because four later nodes copy them byte for byte.
>
> **Finding 1: clause 8a, a rule stated only as a prohibition (1 instance)**
> - **Instance:** Hard rule 3 reads "You have no way to reach the human, and nothing you hand back waits on them." It is a rule stated entirely in the negative, and no positive statement sits beside it. The wording is unchanged from the before-text. Every other negative in the file sits beside a positive.
> - **Form:** a sentence stating a rule for the reader (a duty or prohibition) only in the negative, with no positive statement of the rule in the same sentence or the one next to it.
> - **Extent (bounding set):** every sentence outside the code fence that contains a negation, read by hand. I listed them with `awk '/^```/{f=!f;next} !f' .claude/skills/expedition-research/SKILL.md | grep -n -i -w -E 'no|not|never|nothing|none|may not|do not'`. This is the only one I judged a breach.
>
> **Finding 2: clause 8e, "these"/"those" with no referent in the same sentence or the one before (3 instances)**
> - "Read each of these." under `## What you read`. It points at the list that follows. The wording is unchanged from the before-text.
> - "So write the condition to these four points." under `## When a node you report is an implementation node`, one of the shared sections. It also points forward, at the list that follows.
> - "check what you wrote against those four." in the same shared section. It points at four bullets, but the sentence before it is only the last bullet.
> - **Form:** a "this", "that", "these" or "those" whose referent is neither in its own sentence nor in the sentence immediately before it. That includes a referent that comes after it.
> - **Extent (bounding set):** every hit of `awk '/^```/{f=!f;next} !f' .claude/skills/expedition-research/SKILL.md | grep -n -i -w -E 'it|this|that|they|these|those'`, each read by hand. These three are the only instances.
> - **Note:** this applies the window exactly as clause 8e words it. A reader might find a forward-pointing "these" before a list clear enough. Wording like "the following" and "the four points above" would meet the clause.
>
> **What passed, clause by clause**
> 1. **Nothing binding lost: met.** I compared every rule, condition, fixed template and defined term side by side. Closed lists keep their counts and members: the three conflicting skill instructions, the five handover parts, the three bookkeeping items, and the four condition points. The only things dropped are sentences explaining why ("That is what this kind of node is for", "You are the party that holds what it takes", and similar).
> 2. **Nothing binding added: met.** The new "Put all your work in your handover" is the positive half of "write no file", which clause 8a demands. The before-text already implied it, since the handover is the worker's only output.
> 3. **Generalisation: met.** The no-round exception that the before-text stated twice is merged into one statement with the same outcome.
> 4. **Fixed text: met.** The frontmatter and the code fence are byte-identical, checked by extracting both from each version and diffing them.
> 5. **Headings: met.** Every heading is kept verbatim, checked by diffing the headings of both versions.
> 6. **References inside the file: met.** "Hard rules 4 to 6 above" still points at the same three rules. "this contract's hard rules" resolves.
> 7. **Terms: met.** Terms from `CONTEXT.md` are spelled as it defines them. I checked the refused words by hand. The candidates (report, run, tree, index, summary, done, question, decision, interview, `## Review` round) are all used for other concepts, and the before-text used each the same way. No new term is coined.
> 8. **Plain English: fails on a and e**, as above. The other four properties hold: 8b: bold appears only at the place a term is defined. 8c: none of the figures of speech I found in the before-text survive ("paid for there", "read cold", "the whole of the discipline"). 8d: I found no slogan-shaped sentence, and "the whole of what" does not appear. 8f: no semicolons, and every dash is a list-term separator, one per line. I judged "one idea per sentence" through the clause's own test. The closest case is "Write both when you raise the flag, while you still have the context, and give each the flag's marker."
> 9. **Size (reported, not enforced):** `wc -w` gives 1517 before and 1306 after, which is 86% of the before-text. The target was at most 1011, so it is missed, but this does not fail the work.
> 10. **Scope: met.** `git status --porcelain --untracked-files=all` shows only `.claude/skills/expedition-research/SKILL.md` modified.
> 11. **The two shared sections: both present** as `##` sections of their own. The implementation-node section carries two of the Finding 2 instances. The flag section has no breaches.
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`, which matches the rules file. `git diff --check` is clean.
> - **Standards read:** from `map-implementation-rules.md`, the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:** `CONTEXT.md`'s `_Avoid_` lines · the flag-raising and `## Notes` passages of `graph-conventions.md`, which the after-text agrees with · `/writing-for-agents` (on prompting the positive rather than the negative), read from the installed plugin · standing rule 5, which is the same property as clause 8 · all five ground rules, which are all met; no shipped text tells an agent to address the human.
> - `/coding-principles` and `/naming` did not bear on this work. No reviewing skill is named, so I ran none. The changed path is not a record file, so the rule for record files did not apply.
>
> **QUESTIONS**
> - Clause 1 counts every term the file defines as binding, while clause 8c rules out coined phrases that `CONTEXT.md` does not define. For a term this file defined but `CONTEXT.md` does not, the two clauses pull opposite ways. The rewrite dropped the names "standing over sources" and "quantifies over the record" and kept their meaning in plain words. I counted clause 1 as met, because each name was used only where it was defined and no outcome changes. Two other files keep the names, though: `graph-conventions.md` tells the manager to write a "standing over sources" block into the map's `## Notes`; `expedition/SKILL.md` says a condition "may not quantify over the record". Should the four later passes resolve this tension the same way, or keep these names as defined terms?

### Correction round 1 — the worker's changes for checker run 1

*The worker's own text, pasted. The worker returned its full handover again. The parts that differ from `## Handover, attempt 1` are pasted here, and the rest is unchanged from that section.*

**What I changed for each checker finding (run 1):**
- **Finding 1 (8a), hard rule 3.** I added a positive opening sentence to the rule. It now reads "3. Do your work without the human. You have no way to reach the human, and nothing you hand back waits on them." The second sentence is unchanged, so node 57's quote still appears inside it. The new sentence adds no rule: the before-text already says a research node "never involves the human".
- **Finding 2 (8e), three instances:** "Read each of these." became "Read each of the following." The next sentence's "them" now refers back to it. · "So write the condition to these four points." became "So write the condition to the four points that follow." · "check what you wrote against those four." became "check what you wrote against the four points above."
- **Did the corrections touch what the condition names?** Yes. All four edits are prose that clause 8 governs, and two of them are in the shared section that clause 11 names. Nothing inside the code fences or the frontmatter changed (clause 4), and no heading changed (clause 5). The two new internal references point at bullets the section holds (clause 6).

**Changed parts of the handover:**
- *Size:* 1,517 to 1,317 words by `wc -w`, 87% of the before-text.
- *Index line:* The research contract is rewritten in plain English at 87% of its size, every rule kept, fences and cited headings byte-identical, and its two shared sections ready to copy.
- *Pronouns:* A "these" or "those" never points forward, and never reaches back past the sentence before it. The text says "Read each of the following", "the four points that follow" and "the four points above" instead.
- *Kept word for word, revised:* the four pointer bullets under `## What you read` (node 155) · the sentence "You have no way to reach the human, and nothing you hand back waits on them.", now inside hard rule 3 after a new positive opening sentence · "Report `NEW NODES` and `INVALIDATIONS` yourself. Nothing else reports them." (node 43) · "self-contained" (node 109's enumerator) · "written by the node that spawned it" (node 55).
- *Flag 2, revised for the node:* Where a passage was already plain enough, I kept its exact words so that open acceptance conditions keep matching. These are the pointer bullets (node 155), the sentence inside hard rule 3 (node 57), the `NEW NODES`/`INVALIDATIONS` sentence (node 43), and "self-contained" (node 109). Two passages I had first kept word for word failed clause 8e and were reworded: "Read each of these" and "against those four".

**Re-pointing, added this round.** The checker round added three more pieces of wording to the list: "Read each of these", "against those four" and hard rule 3's text. Among open conditions, each is quoted only by the nodes below.
- **Node 155, the sentence before its clauses.** Replace it with: "Each carries a `## What you read` section opening `Read each of these. Do not trust any summary of them.`, or, in `.claude/skills/expedition-research/SKILL.md`, `Read each of the following. Do not trust any summary of them.`, followed by a bulleted list of pointers and then a line stating that `flags.md` is not the worker's." Between the list and the `flags.md` line, the research file also holds "You may read outside the working directory." The before-text had the same shape. Clauses 1, 3 and 4 still hold as written. The decisions bullet and the `flags.md` statement are still there.
- **Node 109, the enumerator paragraph.** Replace it with: "Each of the five worker contracts additionally contains the read-back sentence, which reads *"against those four"* in a contract not yet rewritten and *"against the four points above"* in `.claude/skills/expedition-research/SKILL.md`. It is confirmed by `grep -rlnE "against (those four|the four points above)" --include="*.md" .claude/` returning those five paths and no others."
- **Node 109, clause 6.** Replace "each contract today says the author reads what it wrote back *"against those four"*" with "each contract's read-back sentence (*"against those four"*, or in the research contract *"check what you wrote against the four points above"*)". The rest of the clause is unchanged. After nodes 291 to 294 land, only the second form remains.
- **Node 57, clause 2.** Replace "which today reads *"You have no way to reach the human, and nothing you hand back waits on them"*" with "which today reads *"Do your work without the human. You have no way to reach the human, and nothing you hand back waits on them."*". The rest of the clause is unchanged.
- The node 148 and node 279 replacements stand as in attempt 1.

**Trade-off added:** 4. **Hard rule 3 now says "the human" twice.** I did that to keep node 57's quote intact. Changing the second to "them" reads better but means re-pointing node 57 again.

**Retrospective, added:** (3) The checker's two breaches came from passages I kept word for word to protect other conditions. Both goals held at once is the harder bar, and the spawn could say which one wins. I read clause 8e loosely for a list-introducing "these", and the checker read it strictly. The strict reading is the right one. (4) The before-text's "Read each of these" and "against those four" breach the fifth rule's pronoun test in all five contracts. So the conditions for 291 to 294 will hit the same instances, unless they copy the pilot's wording.

### Checker run 2 — `PASS`

*The checker's own text, pasted, 2026-09-23.*

> **PASS**
>
> This is a re-check. The work changed, and the acceptance condition did not. Both run-1 findings are repaired, the corrections add no new breach, and the bar still holds. The run-1 question stands unchanged, and nothing I found this round changes it.
>
> **What changed since run 1.** I re-read the whole file and compared it word by word against the text I checked in run 1. The work shows exactly the four edits the worker described and nothing else: the first sentence of hard rule 3 is new, and the rule is rewrapped around it · "Read each of the following." replaces "Read each of these." · "the four points that follow" replaces "these four points" · "the four points above" replaces "those four", and the last paragraph is rewrapped around it. The word count confirms it. The four edits add 11 words, which matches the move from 1306 to 1317. No other path changed.
>
> **Clause by clause**
> 1. **Nothing binding lost: met.** The edits remove nothing. My run-1 comparison stands for everything else.
> 2. **Nothing binding added: met.** "Do your work without the human" restates what the before-text already binds: the research node "never involves the human", and "nothing you hand back waits on them". No case comes out differently.
> 3. **Generalisation: met.** The edits don't reach it, so run 1 stands.
> 4. **Fixed text: met.** Re-run: the frontmatter and the code fence are still byte-identical to the before-text.
> 5. **Headings: met.** Re-run: all headings are still identical to the before-text.
> 6. **References inside the file: met.** The two new references resolve. "the four points that follow" points at the four bullets directly after it, and "the four points above" points at the same four bullets. "Hard rules 4 to 6 above" still resolves.
> 7. **Terms: met.** The edits introduce no refused word and no new term.
> 8. **Plain English: met.** 8a: hard rule 3 now opens with the positive "Do your work without the human", and the negative statement sits beside it. 8e: I re-ran the scan for this, that, they, these and those, and read every hit. Each remaining one is a relative "that" or has its referent in its own sentence or the one before. The "them" in "Do not trust any summary of them" refers back to "the following". 8b: the bold words are the same 12 as in run 1, each where its term is defined. 8c, 8d and 8f: the new text adds no figure of speech, no slogan-shaped sentence, no semicolon and no dash.
> 9. **Size (reported, not enforced):** `wc -w` gives 1517 before and 1317 after, which is 87% of the before-text. The target of at most 1011 is missed, which does not fail the work.
> 10. **Scope: met.** `git status --porcelain --untracked-files=all` shows only `.claude/skills/expedition-research/SKILL.md` modified.
> 11. **The two shared sections: met.** Both are still `##` sections of their own under their exact headings. The implementation-node section now meets 8e, and clauses 1 to 8 hold for both.
>
> **The bar, re-run in full.** The repo still has no build, tests, formatter or CI, and `git diff --check` prints nothing. I held the work against the same standards as run 1: the ground rules and the five standing rules for writing, from `map-implementation-rules.md` · `CONTEXT.md`'s `_Avoid_` lines · `graph-conventions.md` · `/writing-for-agents`. All are met. No reviewing skill is named, so I ran none. I read the changed path as the work under check, and it is not a record file.

### Gate — approve

*The human, 2026-09-24,* `verbatim`: *"it seems ok approve"*. The gate payload also asked three questions (A: how deep to cut, B: names the file defines that `CONTEXT.md` does not, C: stable text or a fuller rewrite). The reply does not say which way those go, so the manager asks them separately.

Landed as `4068519`, a fast-forward of `master`. The merge failed inside the sandbox with `unable to unlink old '.claude/skills/expedition-research/SKILL.md': Read-only file system` and left the tree clean. It succeeded with the sandbox off. The worktree and its branch were removed with the sandbox off.

### The gate's three questions, answered 2026-09-24

The human, `verbatim`: *"A ok B like the pilot C you can update"*

- **A** (how deep to cut) — the reply is "ok". A offered two options, so the manager asks which: keep the current depth (a plain-English rewrite at about 85–95% of the original), or allow rule changes such as pointing the manager contract's term list at `CONTEXT.md`, each listed at the gate for approval. The second option was framed in the manager's report after nodes 296 and 299 handed back, from node 296's worker's text: *"let the Words list point at `CONTEXT.md` instead of restating it; drop the `## What is never yours` table …; merge `### Item 5, the check you stop on` into item 5"*.
- **B** (names a file defines that `CONTEXT.md` does not) — "like the pilot": the pilot said "standing over sources" in plain words and dropped the label (this node's flag 1, the worker's text).
- **C** (keep quoted passages word for word, or rewrite freely) — "you can update": rewrite freely and update the conditions that quote the old text.

**A, answered 2026-09-24**, `verbatim`: *"A. we can do 2 if it make sense in the file"*. Option 2 as the manager put it: *"Cut deeper by changing rules. For example, point the manager's term list at `CONTEXT.md` instead of restating it, drop the "What is never yours" table, and fold item 5's check into item 5. Each change would be listed at its gate for you to approve."*

**The condition question, answered 2026-09-24**, `verbatim`: *"ok"*, to the manager's proposal: *"Clause 1: a binding statement that is missing, or whose outcome changed, is a rule change. The checker lists every rule change it finds, with the old statement and its replacement (or "removed"). A rule change doesn't fail the work. Clause 2: the same for anything added. B: a term the file defines that `CONTEXT.md` doesn't may be dropped as a term if its meaning stays in plain words where it stood. That isn't a rule change. At the gate you see two lists side by side: the worker's own list of rule changes with its reasons, and the checker's independent list. A change the checker found that the worker didn't list goes back as a correction. You approve or strike each listed change."* Filed on nodes 291 to 302.

## Flags

`290.1` **· settled** `ASSUMPTION` — `standing over sources` is said in plain words. Clause 1 of the condition keeps every term the text defines. Clause 8c rules out coined phrases for ideas that `CONTEXT.md` does not define. "standing over sources" is both, so I described what the declaration says (which sources are authoritative, which are evidence only, which hold statements known to be false) and dropped the label. The label is not used again in this file, so no case changes. `map.md`, the manager contract and `graph-conventions.md` still use the label.

`290.2` **· settled** `ASSUMPTION` — some passages were left word for word so that fewer conditions need re-pointing. Where a passage was already plain enough, I kept its exact words so that open acceptance conditions keep matching. These are the pointer bullets (node 155), the sentence inside hard rule 3 (node 57), the `NEW NODES`/`INVALIDATIONS` sentence (node 43), and "self-contained" (node 109). Two passages I had first kept word for word failed clause 8e and were reworded: "Read each of these" and "against those four".

## Answer

The research contract is rewritten in plain English at 87% of its size, every rule kept, fences and cited headings byte-identical, and its two shared sections ready to copy.

*The manager's note:* the worker's full answer is under `## Handover, attempt 1`, as corrected in `### Correction round 1`. It landed as commit `4068519`.
