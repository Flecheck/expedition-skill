# Rewrite the implementation contract in plain English

Type: implementation
Status: resolved
Blocked by: 290

## Question

Rewrite `.claude/skills/expedition-implementation/SKILL.md` in plain English and shorter, under the pass [node 289](289-a-plain-english-and-compaction-pass-over-the-shipped-files.md) settled.

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

11. **Scope.** The work changes `.claude/skills/expedition-implementation/SKILL.md` and no other path. The rewritten range is the whole file.
12. **The two shared sections are copies.** The after-text's sections headed `## When you raise a flag` and `## When a node you report is an implementation node` are byte-identical to the sections of the same headings in `.claude/skills/expedition-research/SKILL.md` as it stands at the commit this work's branch was created from. For those two sections, this identity takes the place of clauses 1 to 3 and 8. For the rest of the file, clauses 1 to 10 apply as written.

## Amendment by the human, 2026-09-24

*The human approved the manager's proposal, `verbatim`: "ok". The proposal and the answer to A that prompted it are recorded on [node 290](290-rewrite-the-research-contract-as-the-pilot.md). The manager drafted the wording below, and the human amended the condition with it. The original clauses above are left as they were. The clauses below take the place of clauses 1 and 2, add clause 1a, and add a sentence to clause 3.*

1. **Lost or changed statements are rule changes.** The binding statements are: every rule, meaning every instruction, permission, prohibition or duty, and whose it is; every condition or exception attached to a rule; every fixed template; every term the text defines, and its definition; every word the text refuses; and the members and stated count of every closed list. A binding statement of the before-text that has no counterpart anywhere in the whole after-text, or whose counterpart changes the outcome for any case, is a rule change. The checker lists every rule change it finds, each with the before-text statement and its after-text counterpart, or "removed". A rule change does not fail the work.
1a. **Terms `CONTEXT.md` does not define.** A term the before-text defines that `CONTEXT.md` does not define may be dropped as a term, where its meaning is still stated in plain words at the place it was defined. Dropping a term that way is not a rule change.
2. **Added statements are rule changes.** A rule, permission, duty, exception, defined term or refused word that the after-text states and the before-text does not is a rule change. The checker lists it the same way as under clause 1. It does not fail the work.
3. *(added sentence)* A generalisation that changes an outcome, or decides a case the before-text left undecided, is a rule change under clause 1 or clause 2.

## Answer

The implementation contract is rewritten in plain English at 87% of its length, with fences and headings kept, both shared sections copied byte-for-byte from the research contract, and no deliberate rule change.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`, as changed by correction round 1, which brought the file to 88% (2,604 words) and added the one rule change the checker listed. The human approved it, and the checker's independent list is under `### Checker run 2`. The work landed as commit `724c361`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-25. The worker's own text, pasted. The flags are raised under `## Flags` at the gate.*

HANDOVER:      Rewrite the implementation contract in plain English

ANSWER:
`.claude/skills/expedition-implementation/SKILL.md` has been rewritten in plain English in the worktree `.scratch/graph-workflow/worktrees/294-rewrite-the-implementation-contract`, based on `76e66e3`. The changes are uncommitted.

- **Size.** `wc -w` went from 2,970 to 2,594, which is 87%. The two-thirds target (1,980) is missed. About 810 words are fixed text: the fences are 231 words and the two shared sections are 576. That leaves too little other prose to reach two thirds without dropping `CONTEXT.md` terms from the term list. The pilot landed at 87% (1,517 to 1,317) and the checker contract at 86%, so this matches them.
- **Fixed text.** The frontmatter and all four fences are byte-identical to the before-text.
- **Shared sections (clause 12).** `## When you raise a flag` and `## When a node you report is an implementation node` are byte-identical copies of the research contract's sections at `76e66e3`. I checked that this file's before-text of those two sections was identical to the research contract's own before-text at `4068519^`. So every difference in them is one node 290 made and the human approved at its gate.
- **Headings (clause 5).** Every before-text heading is kept exactly, including the six that other shipped files also use.
- **Term list.** Every term in the list is defined in `CONTEXT.md`, so clause 1a let me drop none. I kept the file's own list rather than pointing at `CONTEXT.md`, as node 295 did. Definitions were shortened where the same fact is stated elsewhere in the file:
  - gate: that the manager raises your work there is now in the diagram.
  - resolve: "never yours" is now in hard rule 2.
  - code slot: that the effort sets the slot count is now in the opening.
- **Labels and idioms.** "standing over sources" is written out as the plain description the pilot used, and the label is gone. These idioms were replaced:
  - "reaches past" became "affects more than"
  - "upstream of yours" became "your node depends on"
  - "a genuine fork" became "the choice is genuinely open"
  - "on the way in", "Below all three", "outlets" and "not going anywhere from here" were reworded plainly
  - "orientation, not permission" became "neither permit nor forbid an edit"
  - "The graph-file ban is about recording, not about files" is now stated directly as hard rules 1 and 2
- **Numbered triggers.** The trigger table's rows are now numbered "1." to "3.", so the file's references to "trigger 1" point at something the file holds.
- **Other clauses.** The refused-word grep returns nothing. The repo has no build, tests, formatter or CI (only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch` at the root), so the bar is its non-command half. No method skill was run, so no part of one was skipped.

INDEX LINE:    The implementation contract is rewritten in plain English at 87% of its length, with fences and headings kept, both shared sections copied byte-for-byte from the research contract, and no deliberate rule change.

FLAGS:
ASSUMPTION: I read "Those paths are orientation, not permission" together with the sentence after it ("Where the work takes you outside them, go"). I wrote it as "The paths the spawn expects you to touch neither permit nor forbid an edit. Where the work needs changes outside those paths, make them." I judged that the "forbid" half is what the second sentence already said. *Index:* "orientation, not permission" in the implementation contract was reworded as paths that "neither permit nor forbid an edit", on the reading that the next sentence already allowed going outside them.

NEW NODES:     none

INVALIDATIONS: none. Node 74's shipped code-slot wording ("One worker to a slot; how many slots an effort runs is that effort's own setting") is reworded but keeps its content. The new wording is "the right to modify product code, held by one worker" and "Each effort sets how many code slots it runs."

GATE PAYLOAD:
- Checker findings: none yet.
- Paths touched: `.claude/skills/expedition-implementation/SKILL.md` only. My scratch copies and search scripts are outside the repo in `/tmp/claude-1000/n294/`.
- Bar: the repo has no commands. `map-implementation-rules.md` records none, and the repo agrees.
- Proposed commit message:
  ```
  Rewrite the implementation contract in plain English

  Node: graph-workflow/294
  ```

RULE CHANGES

I made no deliberate rule change. Each entry below is borderline: I judge that it keeps every outcome, and I list it so the checker's list can be matched against mine.

1. **Only on a trigger.**
   - Before: "you reach for them only on the three triggers below" (opening), plus "Raise when any one of these holds" and "One trigger is enough."
   - After: "raise if any one of the three triggers in the table below holds, and raise on no other ground."
   - Why: "reach for" was figurative, and the "only" is now stated where the triggers are.
2. **Paths.**
   - Before: "Those paths are orientation, not permission. Where the work takes you outside them, go, and report what you touched."
   - After: "The paths the spawn expects you to touch neither permit nor forbid an edit. Where the work needs changes outside those paths, make them." Reporting moved to hard rule 5.
   - Why: "orientation" was dropped as the non-binding half. This is also my one flag.
3. **raise definition.**
   - Before: "whether it waits is the channel's property rather than the word's"
   - After: removed. Both cases are kept: "Where this contract says *raise* alone, it means the kind that stops your work until the human acts" and "A flag waits for the gate."
4. **The tree.**
   - Before: "every file you edit is inside it" (worded as a description)
   - After: "Edit only files inside it."
5. **Hard rule 3.** Added the positive form "Leave your work uncommitted, on the branch it is on." It sits before the unchanged list of prohibitions, which it only restates.
6. **Hard rule 4.**
   - Before: "You have no human-facing tool. Do not call one. Your two outlets are a flag and a raise."
   - After: "Contact the human only by a flag or a raise, and call no tool that addresses the human."
   - Why: the claim of fact "you have no human-facing tool" is removed. The rule stays.
7. **Hard rule 5.**
   - Before: "Report the paths you touched. Never leave them to be found in `git status`."
   - After: "Report every path you touched."
8. **Hard rules 1 and 2.**
   - Before: "The graph-file ban is about recording, not about files … never record it when you finish … Marking your node, resolving it, and its lines in decisions.md and flags.md stay the manager's", and "You never resolve your node and never mark it. You hand your answer back and the manager writes it."
   - After: "Write product code. Write a graph file only where your node's own work is a change to that file." and "Leave all recording on the graph to the manager, whatever your node's work is. The manager writes your answer onto your node, marks and resolves the node, and writes its lines in `decisions.md` and `flags.md`."
9. **Standards.**
   - Removed the reason "A rule written in a file can be changed by whoever owns it; a rule an agent finds for itself cannot." It is not stated anywhere else in the file.
   - Before: "which is why neither of you goes looking". After: "Your checker reads the same file and looks nowhere else either."
10. **Flags.**
    - Before: "read by the human at the gate, hours away — not at the end of the effort"
    - After: "The human reads your flags at the gate."
    - Why: "hours away" and "not at the end of the effort" were explanation.
11. **Stop.**
    - Before: "what you built is not going anywhere from here" and "Do not tidy it, do not make it build, and do not bring it to the bar."
    - After: the first clause is removed. The second became "leave what you built as it is, even where it does not build or meet the bar."
    - I checked all three cases against the before-text.
12. **How you implement.**
    - Removed the reason "Such a skill was written for an agent working alone."
    - "Leave the conflicting part unrun" became "Skip the conflicting part", which is the pilot's wording.
    - "The bar, the standards, and the acceptance condition are what bind you" became "What binds your work is the bar, the standards and the acceptance condition."
13. **The bar.**
    - Before: "These are properties, not commands", "the repo's statement wins" and "the record … stands as it is, unconfirmed".
    - After: the first is carried by the definition and "these properties". The second is carried by "authoritative" and "run the repo's commands". The third became "use the recorded ones unconfirmed."
14. **Diff.**
    - Before: "Never render a diff into your output. The manager lays your text end to end with the checker's own"
    - After: "Leave the diff in the working tree and out of your output. The manager joins your text to the checker's"
15. **Checker finding that is a piece of work.**
    - Before: "do not carry the finding past the gate unfixed on your own authority"
    - After: "Never leave the finding unfixed at the gate on your own authority."
16. **Replacement attempt.**
    - Before: "Everything in that record is a settled fact. Never put one of those questions back to them."
    - After: "Treat everything in that record as settled, and never ask the human again a question that record answers."
17. **Shared sections.** Replaced by the research contract's copies. Under clause 12 these are not rule changes. Examples of what changed: "Its cap is stated here so you need not open the file" is gone, and "report-shaped" became "one sentence that reports your judgement". These are exactly node 290's changes, which the human approved.

Exception cases I checked against the before-text, all kept in full:
- continue: 2 cases
- stop: 3 things not to do
- hard rule 6: replacement node or split
- method-skill conflicts: 3
- a wrong acceptance condition: 4 kinds
- things not to touch when raising: discard, tidy, revert
- git operations: 5
- bar properties: 5
- the manager's bookkeeping acts: 4

RE-POINTING SEARCH

**How I searched:**
- All 93 `## Acceptance condition` sections of open or claimed nodes, together with every `## Amendment…` section. My script is `/tmp/claude-1000/n294/search2.py`.
- (a) Every quoted span of 12 characters or more (backticks, `*…*`, straight or curly double quotes), normalised, found in the before-text, and checked for whether it survives in the after-text.
- (b) Six-word shingles shared between the before-text and each condition (`/tmp/claude-1000/n294/search.py ngram`).
- (c) Mentions: `expedition-implementation`, "implementation contract", "five worker contracts", "five files", "six files", "each of the five".
- (d) Removed or replaced wording: every before-text heading, orientation not permission, reaches past, upstream of yours, genuine fork, hours away, Below all three, One trigger is enough, trigger 1, on the way in, not going anywhere, graph-file ban, about recording not about files, outlets, human-facing tool, git status, standing over sources, one known file, look nowhere else, live statement, properties not commands, Nobody hands them to you, hunt for none, a rule an agent finds for itself, neither of you goes looking, end to end, render a diff, Discard nothing, written for an agent working alone, collide with the rules above, unrun, are what bind you, reach for them, every file you edit is inside it, Report the paths you touched, never both at once, never leave a part off, an instruction not an answer, Rounds are uncapped, a piece of work rather than a repair, past the gate unfixed, put one of those questions back, settled fact, Read each of these, ordinary case rather than a defect, three triggers, the channel's property, a copy of an earlier discovery, the only statement there is, remaining half, complete bar and not a deficient one, is not what this rule reaches, Saving what you built, You keep the code slot, half-written code, test yourself, It did not read your node, One worker to a slot, Six parts every time, none in full, Marking your node resolving it, the size of your own node is not yours to change.

**Replacement clauses:**
- **Node 148, clause 1**, as amended by node 290. Replace it with: "the bullet beginning `A path may say where, because the checker has the repo` in `.claude/skills/expedition-research/SKILL.md` and `.claude/skills/expedition-implementation/SKILL.md`, and in any of the five not yet rewritten, the bullet beginning `a **path** may say where`".
- **Node 155, the sentence before its clauses**, as amended by node 290. Replace it with: "Each carries a `## What you read` section opening `Read each of these. Do not trust any summary of them.`, or, in `.claude/skills/expedition-research/SKILL.md` and `.claude/skills/expedition-implementation/SKILL.md`, `Read each of the following. Do not trust any summary of them.`, followed by a bulleted list of pointers and then a line stating that `flags.md` is not the worker's." In the implementation file the `flags.md` line ("Leave `flags.md` unread. It is not yours.") follows the list directly. The decisions bullet ("`decisions.md` — the sections the spawn names") is byte-identical, so clauses 1, 3 and 4 still hold.
- **Node 109, the enumerator paragraph**, as amended by node 290. Replace "and *"against the four points above"* in `.claude/skills/expedition-research/SKILL.md`" with "and *"against the four points above"* in `.claude/skills/expedition-research/SKILL.md` and `.claude/skills/expedition-implementation/SKILL.md`". The recorded grep `grep -rlnE "against (those four|the four points above)" --include="*.md" .claude/` still returns the five worker contracts and no others. I ran it in the worktree. The `self-contained` grep also still returns the same seven paths.
- **Node 109, clause 6**, as amended by node 290. Replace "or in the research contract" with "or in the research and implementation contracts". The rest is unchanged.

**Matched, needing no change:**
- 279: the amended clauses 1 and 3 quote the research after-text, which this file now holds byte-for-byte. Clause 2's conflict with the byte-for-byte copying is still the manager's open item.
- 43: "Report `NEW NODES` and `INVALIDATIONS` yourself. Nothing else reports them." is kept word for word, and the quantify rule is kept in meaning, as in the research copy. `your work contradicts` sits inside the fence.
- 41: the `FLAGS:` line is inside the fence, and "One marker is yours" is kept.
- 60: "Write all six parts of the handover every time" still states the count.
- 61: the opening and the handover paragraph still spell out the manager passing text along unaltered.
- 55: "written by the node that spawned it" is kept.
- 81: entry 3 describes node 74's wording by its content, not by quotation. Both facts are still in the file, but no longer as one sentence to copy.
- 97 and 111: "standing over sources" was already re-pointed by node 299, with the wording this file now uses.
- 304: it excludes this file.
- 291 to 293, 298, 301 and 302: they quote "the ban is about recording, not about files" only as an example in their own clause 8d.
- 173, 149, 205, 206, 190 and 276: hits on other files.

GENERALISATIONS
1. "Report every path you touched." (hard rule 5) replaces both hard rule 5's before-text ("Report the paths you touched. Never leave them to be found in `git status`.") and "and report what you touched" in `## What you read`.
2. Hard rules 1 and 2 are merged into "Leave all recording on the graph to the manager, whatever your node's work is …". It replaces the before-text's hard rule 1 sentences on bookkeeping and marking, and hard rule 2's "You never resolve your node and never mark it. You hand your answer back and the manager writes it".
3. "Read them there yourself, and look for none anywhere else." replaces "you read that file, and you look nowhere else", "Nobody hands them to you" and "you hunt for none of your own".
4. The trigger sentence replaces the opening's "you reach for them only on the three triggers below", "Raise when any one of these holds" and "One trigger is enough".
5. Trigger 1's row now carries "the size of your own node is not yours to change" alone. It replaces the copies in hard rule 6 and in the paragraph on checker findings.

RETROSPECTIVE
1. **What I had to hunt for.**
   - Which before-text headings other files use. I computed it with a grep over clause 5's file list.
   - Whether nodes 148, 155, 109, 279 and 57 already had amendments. I found them by listing each node's `##` headings.
   - What node 290 had already re-pointed. It is in node 290's `### Re-pointing duty`, which I found only after reading the amendments.
   - Whether the implementation file's shared sections matched the research file's before-text. I checked with `git show 4068519^`.
2. **What arrived that this node did not need.**
   - The node-297 direction in the spawn, about what a message to a worker may permit and about approval settling flags. This contract states neither rule.
   - Most of `map.md` (its long standing preferences) and the review-route paragraphs of `map-implementation-rules.md`. I needed one pointer and rule 5.
   - `CONTEXT.md` read in bulk, where I needed only the entries and `_Avoid_` lines for this file's thirteen terms.
   - A list of the open nodes whose conditions name this file, with their amendments, would have replaced most of my search.
3. **What would have made it easier.**
   - One shared search script that collects amendment sections. This is node 313.
   - A note in the spawn that fences plus shared sections are about 810 of 2,970 words, so two thirds is out of reach without dropping terms.
   - The prior rewrites' ratios (86 to 87%), given as the benchmark.
4. **What was stale, wrong or contradictory.**
   - `/tmp/claude-1000/n295/search.py` stops collecting at any `## The manager…` heading, so it misses every `## Amendment` filed after a manager's note. That affects nodes 148, 155, 279, 109, 111 and 61.
   - Node 298's flag `298.1` credits "They are in one known file, you read that file, and you look nowhere else." to the checker contract's `## The standards you hold the work against`. That sentence was this file's, under `## The standards your work is held to`.
   - `map.md` still says `CONTEXT.md` is "moving" into `.claude/skills/expedition/`. It is still at the root.

## Review

### Checker run 1 — `FAIL`, acceptance condition (as amended by the human)

*The checker's own text, pasted, 2026-09-25. The checker was resumed from node 295's check.*

> FAIL: acceptance condition
>
> Node 294, "Rewrite the implementation contract in plain English". The work fails on two clauses: one refused word under clause 7, and two rules stated only as prohibitions under clause 8a. All three are one-line fixes. Everything else is met: the two shared sections are byte-identical copies, I found no rule changes, and the bar holds.
>
> I read my contract again from the main tree, as it stands after node 295 landed (`76e66e3`). The work is `.claude/skills/expedition-implementation/SKILL.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/294-rewrite-the-implementation-contract`. The branch base is `76e66e3`. I read the changed path only as the work. Line numbers below are the after-text's.
>
> **Finding 1: clause 7, a refused word (1 instance)**
> - **Instance:** line 267–268, in `## If you are a replacement attempt`: "never ask the human again a question that record answers". The `_Avoid_` line under **Raise** in `CONTEXT.md` refuses *ask* for a worker meant to work mostly by itself putting something to the human. That is a raise, and an implementation worker's only way to put a question to the human is a raise. The before-text had "Never put one of those questions back to them", with no refused word. Wording such as "never put to the human again a question that record answers" would meet the clause.
> - **Form:** "ask" in prose outside a code fence, naming a worker putting a question to the human. The `ASK:` field inside the raise template is fixed text under clause 4 and is not an instance.
> - **Extent (enumerator):** `awk '/^```/{f=!f;next} !f{print NR": "$0}' .claude/skills/expedition-implementation/SKILL.md | grep -i -w -E 'ask|asks|asked|asking'`. It returns this one line.
>
> **Finding 2: clause 8a, a rule stated only as a prohibition (2 instances)**
> - **Instances:**
>   - Line 28, in the word list's **acceptance condition** entry: "You may not rewrite it." Nothing beside it says what to do, such as leaving the condition as written.
>   - Line 167, under `## After the code is written`: "You never start the checker." The sentences beside it ("You also never see it start. You receive what it found. Fix all of it before the gate.") state other things. None is the positive form of this rule, such as that the manager starts the checker.
> - **Form:** a sentence outside the two shared sections and outside code fences that states a rule for the reader only in the negative, with no positive form of the same rule in that sentence or the one next to it.
> - **Extent (bounding set):** every hit of `awk '/^```/{f=!f;next} !f{print NR": "$0}' .claude/skills/expedition-implementation/SKILL.md | grep -i -w -E 'no|not|never|nothing|none|neither|nor|do not|may not'` outside lines 214–262, which are the two shared sections. I read each hit by hand. Every other negative rule has its positive form beside it.
>
> **Clause by clause**
> 1. **Lost or changed statements: met.** No rule change is found, and the list below says how far that reaches. Dropping the term *standing over sources* is allowed by clause 1a: its meaning is still stated in plain words where it was defined ("by path or glob, which sources are authoritative, which are evidence only, and which hold statements known to be false"), and `CONTEXT.md` does not define it.
> 2. **Added statements: met.** Nothing is added. "Raise on no other ground" restates the before-text's "you reach for them only on the three triggers below". "Leave your work uncommitted, on the branch it is on" restates "never commit, never branch, never switch branches".
> 3. **Generalisation: met.** Two changes merge or narrow statements, and I judged both to give the same outcome in every case:
>    - Hard rule 6 went from an unconditional "never create the node that would replace your own … never split your own node" to "Where the work needs … raise, and do neither yourself". A worker creating or splitting nodes when the work does not need it is still ruled out: hard rule 2 leaves all recording to the manager and says to "create no file for it".
>    - The **gate** definition lost "The manager raises your work". The fixed diagram still says "→ the manager raises the gate".
> 4. **Fixed text: met.** The frontmatter and all code fences are byte-identical to the before-text. That covers the raise template, the flow diagram and the handover template.
> 5. **Headings: met.** Every heading is identical to the before-text.
> 6. **References inside the file: met.** Each one resolves: "listed under `## What you hand back`", "trigger 1 in `## Flag, or raise`" (the table rows are now numbered), "the table below", "the raise under `### The raise`", "the handover below", and "the four points that follow" and "the four points above" in the shared section.
> 7. **Terms: fails** on "ask", as above. Otherwise the terms from `CONTEXT.md` are spelled as it defines them: code slot, gate, correction round, raise, flag, handover, resolve, acceptance condition, the bar and checker. The before-text's "Discard nothing" is gone. That was a word refused for the reject concept, and the after-text says "deleted" instead. "Return one `ASSUMPTION` flag" became "hand back". No new term is coined.
> 8. **Plain English (outside the shared sections): fails on 8a**, as above. The other five properties hold:
>    - 8b: bold appears only on "implementation" at its definition and on the word-list terms.
>    - 8c: I found no figure of speech or coined phrase. "Lands in the repo" and "the code path" are `CONTEXT.md`'s own wording of defined terms.
>    - 8d: I found no slogan-shaped sentence, and "the whole of what" does not appear.
>    - 8e: I read every it, this, that, they, these, those and them. Each has one clear referent in its own sentence or the one before.
>    - 8f: no semicolons outside the fences. The only dashes are one separator per list line.
> 9. **Size (reported, not enforced):** the rewritten range is the whole file. `wc -w` gives 2970 before and 2594 after, which is 87% of the before-text. The target of at most 1980 is missed, which does not fail the work.
> 10. and 11. **Scope: met.** `git status --porcelain --untracked-files=all` shows only `.claude/skills/expedition-implementation/SKILL.md` modified.
> 12. **The shared sections are copies: met.**
>    - `## When you raise a flag` is byte-identical (`cmp`) to the section of that heading in `expedition-research/SKILL.md` at base `76e66e3`.
>    - `## When a node you report is an implementation node` is byte-identical to the research section up to that file's end. The only extra byte is the blank line separating it from the next heading, `## If you are a replacement attempt`, which the research file does not have because the section ends it.
>    - Clause 7 still applies to these sections, and "a `## Review` round" is the heading name, not the refused use.
>
> **RULE CHANGES**
>
> None found.
>
> How far the list reaches: I compared every statement of the before-text outside the two shared sections against the whole after-text. The two shared sections are excluded because clause 12 replaces clauses 1 to 3 for them. The comparison covered every rule and whose it is, every condition and exception, the three fixed templates, the defined terms, the refused words, and the closed lists with their counts:
> - the three triggers
> - the two answers, continue and stop
> - the two things handed back
> - the six handover parts
> - the three conflicting skill instructions
> - the five things you read
> - the two ways to reach the human, a flag and a raise
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, the bar, the review route, the five ground rules and the five standing rules for writing. That file has one uncommitted edit on disk: a note on `.gitignore` in the bar paragraph. It does not change what the bar requires.
> - **Standards that bore on this work:**
>   - Standing rule 5 (plain English), which is the same property as clause 8.
>   - `CONTEXT.md`'s `_Avoid_` lines, where the "ask" finding comes from.
>   - `/writing-for-agents` (on stating the positive), which bears on the 8a finding.
>   - All five ground rules, which are met.
> - On ground rule 3: "Contact the human only by a flag or a raise" names the two channels that go through the manager, and the intro says "Everything the human receives goes through the manager". So it does not tell the worker to address the human directly.
> - No reviewing skill is named, so I ran none.

*The manager's note, matching the two lists:* the checker found no rule change, and every entry on the worker's list is one the checker judged to keep its outcome. What goes back is the clause 7 and clause 8a findings.

### Correction round 1 — the worker's changes for checker run 1

*The worker's own text, pasted, 2026-09-25.*

CORRECTION ROUND 1 — node 294, Rewrite the implementation contract in plain English

WHAT I CHANGED

All three instances are fixed in `.claude/skills/expedition-implementation/SKILL.md` in the worktree. The changes are uncommitted.

1. **Finding 1, clause 7** (`## If you are a replacement attempt`).
   - Before: "never ask the human again a question that record answers."
   - After: "never put to the human again a question that record answers."
   - The sentence now reads: "Treat everything in that record as settled, and never put to the human again a question that record answers."
   - The checker's awk and grep for `ask|asks|asked|asking` outside code fences now returns nothing.
2. **Finding 2, clause 8a, word list** (the **acceptance condition** entry).
   - Before: "You may not rewrite it."
   - After: "Leave it as written. You may not rewrite it."
3. **Finding 2, clause 8a, `## After the code is written`.**
   - Before: "You never start the checker. You also never see it start."
   - After: "The manager starts the checker, and you never start it. You also never see it start."

**Checks after the change:**
- I rewrapped the two edited paragraphs to the file's line width.
- The code fences are still byte-identical to the before-text.
- The two shared sections are still byte-identical to the research contract's at `76e66e3`.
- Every heading is unchanged.
- The refused-word grep returns nothing.
- `wc -w` went from 2,594 to 2,604. The before-text is 2,970 words, so the after-text is about 88% of it.

**Did the change touch what the condition names?** Yes. All three edits are inside the rewritten range, which is the whole file and the only path clause 11 names. They answer clause 7 (finding 1) and clause 8a (finding 2). No other path changed.

RULE CHANGES (differences from the first return)

- **New borderline entry 18: "The manager starts the checker."**
  - Before: "You never start the checker and you never see it start." The before-text never says who starts it.
  - After: "The manager starts the checker, and you never start it."
  - Why it makes sense in the file: clause 8a needs the positive form beside the prohibition. The sentence names the manager, which `CONTEXT.md`'s **Checker** entry already says: "Started by the manager and never by the implementer". This is an added statement about whose act it is. I judge that it changes no outcome for the worker. I list it because under clause 2 it may count as an added statement.
- **New borderline entry 19: "Leave it as written."**
  - Before: "You may not rewrite it."
  - After: "Leave it as written. You may not rewrite it."
  - This is the positive form of the same rule, with the same outcome.
- **Entry 16 is updated.** Its after-text is now "Treat everything in that record as settled, and never put to the human again a question that record answers." The outcome is the same as the before-text's "Never put one of those questions back to them."
- Every other rule-change entry is as first returned.

RE-POINTING SEARCH (for the changed wording)

- **Handles searched:** "You may not rewrite it", "may not rewrite", "never start the checker", "You never start the checker", "never see it start", "never ask the human again", "put one of those questions back", "Leave it as written", "The manager starts the checker".
- **Where:** all 93 `## Acceptance condition` sections of open or claimed nodes, with their `## Amendment` sections, normalised.
- **Result:** one hit. Node 55, clause 5, says "that its worker may not rewrite it". That clause is about another file, which node 55's own work changes, and it quotes no text from this file. This file also still says "You may not rewrite it." So node 55 needs no change.
- The replacement clauses for nodes 148, 155 and 109 are as first returned.

FLAGS: as first returned (one `ASSUMPTION`, on "neither permit nor forbid an edit").

GATE PAYLOAD:
- **Checker findings and what I changed:**
  - Finding 1, clause 7, refused word "ask": reworded to "never put to the human again a question that record answers".
  - Finding 2, clause 8a, two prohibitions with no positive form: added "Leave it as written." to the acceptance condition entry, and "The manager starts the checker, and" before "you never start it".
- **Paths touched:** `.claude/skills/expedition-implementation/SKILL.md` only.
- **Bar:** the repo has no build, test or format commands, so the bar is its non-command half.
- **Proposed commit message:** as first returned.

Every other part as first returned: ANSWER (apart from the word count, now 2,604), INDEX LINE, NEW NODES, INVALIDATIONS, GENERALISATIONS and RETROSPECTIVE.

### Checker run 2 — `PASS`, under the amended condition

*The checker's own text, pasted, 2026-09-25.*

> PASS
>
> This is check 2 of node 294, "Rewrite the implementation contract in plain English". All three run-1 findings are fixed and the corrections break nothing else, so the work now meets the amended acceptance condition and the bar. One edit adds a statement the before-text did not make, and I list it as a rule change. Under the amendment a rule change does not fail the work.
>
> My contract is the main-tree checker contract, unchanged since run 1. The work is `.claude/skills/expedition-implementation/SKILL.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/294-rewrite-the-implementation-contract`, branch base `76e66e3`. I read the changed path only as the work. Line numbers are the after-text's.
>
> **What changed since run 1.** No statement of changes came with this check, so I compared the whole file against the run-1 text I read in full. I found exactly three edits and nothing else. The word count went from 2594 to 2604, which matches the three edits.
> 1. Line 28, the **acceptance condition** entry: "You may not rewrite it." became "Leave it as written. You may not rewrite it."
> 2. Line 167: "You never start the checker." became "The manager starts the checker, and you never start it."
> 3. Lines 267–268: "never ask the human again a question that record answers" became "never put to the human again a question that record answers".
>
> **Clause by clause**
> 1. **Lost or changed statements: met.** The rule change is listed below. Edit 1 gives the same outcome as the before-text's "You may not rewrite it", which the after-text still holds. My run-1 comparison stands for the rest of the file.
> 1a. **Terms `CONTEXT.md` does not define: met**, as in run 1. The term *standing over sources* was dropped, and its meaning is still stated in plain words where it was defined.
> 2. **Added statements: met.** Edit 2 adds the manager's duty to start the checker, which is listed below.
> 3. **Generalisation: met.** The edits don't affect it, so my run-1 findings stand: hard rule 6 and the gate definition give the same outcomes.
> 4. **Fixed text: met.** Re-run: the frontmatter and every code fence are byte-identical to the before-text.
> 5. **Headings: met.** Re-run: every heading is identical to the before-text.
> 6. **References inside the file: met.** The edits add no reference, and every reference from run 1 still resolves.
> 7. **Terms: met.** "Ask" is gone from the prose. `grep -i -w -E 'ask|asks|asked|asking'` outside the code fences returns nothing. The `ASK:` field in the raise template is fixed text. "The manager" and "checker" are spelled as `CONTEXT.md` defines them.
> 8. **Plain English (outside the shared sections): met.**
>    - 8a: both run-1 instances now have their positive form beside them: "Leave it as written." and "The manager starts the checker". I re-read the negations in the edited sentences, and every other negative rule already had its positive form beside it in run 1.
>    - 8e: in "Leave it as written", the "it" refers to the acceptance condition the entry defines. In "you never start it" and "You also never see it start", the "it" refers to the checker.
>    - 8b, 8c, 8d and 8f are unaffected by the edits. Re-run: there are no semicolons outside the fences, bold still appears on the same 19 terms, and the edits add no dash, figure of speech or slogan-shaped sentence.
> 9. **Size (reported, not enforced):** the rewritten range is the whole file. `wc -w` gives 2970 before and 2604 after, which is 88% of the before-text. The target of at most 1980 is missed, which does not fail the work.
> 10. and 11. **Scope: met.** `git status --porcelain --untracked-files=all` shows only `.claude/skills/expedition-implementation/SKILL.md` modified.
> 12. **The two shared sections are copies: met.** Re-run against `expedition-research/SKILL.md` at `76e66e3`. `## When you raise a flag` is byte-identical. `## When a node you report is an implementation node` is byte-identical except for the blank line before the heading that follows it, as in run 1. The edits are outside both sections.
>
> **RULE CHANGES** (for the file as it now stands)
> 1. **Added duty (the manager's).** Before: "You never start the checker and you never see it start." The before-text says nowhere who starts the checker. After, at line 167: "The manager starts the checker, and you never start it." The new statement gives the manager the duty of starting the checker. `CONTEXT.md`'s **Checker** entry says the same ("Started by the manager and never by the implementer"). The worker's outcome is unchanged.
>
> How far the list reaches: every statement of the before-text outside the two shared sections, compared against the whole after-text. Clause 12 replaces clauses 1 to 3 for those two sections, so they are excluded. The comparison covers rules and whose they are, conditions and exceptions, the three templates, defined terms, refused words, and every closed list with its count. It is the full run-1 comparison, together with the three edits above, each read against the before-text. Beyond the one change listed, I found no rule change.
>
> **The bar, re-run in full**
> - The repo has no build, tests, formatter or CI, and `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md`, unchanged since run 1: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:** standing rule 5, `CONTEXT.md`'s `_Avoid_` lines, `/writing-for-agents`, and all five ground rules, which are met.
> - No reviewing skill is named, so I ran none.

*The manager's note, matching the two lists:* the checker's one rule change is the worker's entry 18, added in correction round 1. Every other entry on the worker's list the checker judged to keep its outcome.


### Gate — approve, 2026-09-25

The human, `verbatim`: *"approve"*

## Flags

`294.1` **· settled** `ASSUMPTION` — I read "Those paths are orientation, not permission" together with the sentence after it ("Where the work takes you outside them, go"). I wrote it as "The paths the spawn expects you to touch neither permit nor forbid an edit. Where the work needs changes outside those paths, make them." I judged that the "forbid" half is what the second sentence already said.
