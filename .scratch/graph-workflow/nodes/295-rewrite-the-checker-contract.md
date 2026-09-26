# Rewrite the checker contract in plain English

Type: implementation
Status: resolved
Blocked by: 290

## Question

Rewrite `.claude/skills/expedition-checker/SKILL.md` in plain English and shorter, under the pass [node 289](289-a-plain-english-and-compaction-pass-over-the-shipped-files.md) settled.

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

11. **Scope.** The work changes `.claude/skills/expedition-checker/SKILL.md` and no other path. The rewritten range is the whole file.

## Amendment by the human, 2026-09-24

*The human approved the manager's proposal, `verbatim`: "ok". The proposal and the answer to A that prompted it are recorded on [node 290](290-rewrite-the-research-contract-as-the-pilot.md). The manager drafted the wording below, and the human amended the condition with it. The original clauses above are left as they were. The clauses below take the place of clauses 1 and 2, add clause 1a, and add a sentence to clause 3.*

1. **Lost or changed statements are rule changes.** The binding statements are: every rule, meaning every instruction, permission, prohibition or duty, and whose it is; every condition or exception attached to a rule; every fixed template; every term the text defines, and its definition; every word the text refuses; and the members and stated count of every closed list. A binding statement of the before-text that has no counterpart anywhere in the whole after-text, or whose counterpart changes the outcome for any case, is a rule change. The checker lists every rule change it finds, each with the before-text statement and its after-text counterpart, or "removed". A rule change does not fail the work.
1a. **Terms `CONTEXT.md` does not define.** A term the before-text defines that `CONTEXT.md` does not define may be dropped as a term, where its meaning is still stated in plain words at the place it was defined. Dropping a term that way is not a rule change.
2. **Added statements are rule changes.** A rule, permission, duty, exception, defined term or refused word that the after-text states and the before-text does not is a rule change. The checker lists it the same way as under clause 1. It does not fail the work.
3. *(added sentence)* A generalisation that changes an outcome, or decides a case the before-text left undecided, is a rule change under clause 1 or clause 2.

## Answer

The checker contract is rewritten in plain English at 85% of its size, every rule kept. Fences and cross-file headings are byte-identical, and the labels CONTEXT.md lacks are said in plain words.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`, as changed by correction round 1, which brought the file to 86% (4,132 words). The human approved the one listed rule change, and the checker's independent list is under `### Checker run 2`. The work landed as commit `76e66e3`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-25. The worker's own text, pasted. The attempt was resumed once after a rate-limit stop. The flags are raised under `## Flags` at the gate.*

HANDOVER:      Rewrite the checker contract in plain English

ANSWER:        `.claude/skills/expedition-checker/SKILL.md` is rewritten in plain English at 4,093 words, down from 4,798 (85%). The two-thirds target of 3,199 words is missed. That is reported, and it does not fail the work. I made no deliberate rule change under ruling A (details below). The frontmatter and all six code fences are byte-identical. Every heading whose exact text appears in another file named by clause 5 is kept: `Words used exactly`, `Hard rules`, `What you hand back`, `PASS` and `FAIL`. The `NOT COVERED:` and `QUESTIONS:` shapes are unchanged.

What was done:
- **Bold** is now used only on the seven defined terms under `## Words used exactly`. Bolded leads and bolded case labels were removed.
- **Dashes:** every em-dash aside in the prose is gone. The only dashes left are the ones in the definition list's format and in one heading.
- **Semicolons:** none are left outside the fences.
- **Prohibitions** are restated as what to do, with the prohibition kept beside the positive where it is needed. For example, hard rule 3 now reads "Leave the acceptance condition as written. Never rewrite it…".
- **Slogans and figures of speech are gone:** "A line is not a unit of meaning", "A standard is not the file that holds it", "blindness wins", "not decoration", "in as many words", "the whole of the looking", "The bound is on the sentence and not on the report", "Do not inherit your own conclusion".
- **Labels dropped under clause 1a**, each with its meaning still stated in plain words where it was defined: "implementation-rules file" (now the filename `map-implementation-rules.md`), "operative content" and "rationale" (now "what the standard requires or refuses" and "the wording that says why the standard holds"), "enumerator" (now "a command that lists the form's candidates…" or "the command"), and "bounding set" (the text itself is kept).
- **Repetition cut, with no outcome changed:**
  - The unwrap rule is stated once, in general, in `## What you are given`. The copy in the standards section is removed, and the moved-standard section keeps a one-word "unwrapped".
  - The moved-standard rule is stated in full once, under `### Where the work moved one of them`. The not-covered section and the raise section now point at it instead of restating it.
  - "Check as written, it is not a raise" and "met-and-wrong is a question" now stand only in the routing table.
  - "Where the skill cannot go on without an answer, raise" now stands only in the reviewing-skill limits.
- **Two headings renamed** (neither text appears in any other file): `### What a skill delegates is not blind` → `### When a skill hands part of its work to another agent`, and `### The enumerator a condition records` → `### The search a condition records`.
- **Existing defects carried over unchanged:**
  - Given 2 still offers the spawn a choice between the bar's commands and the properties alone (node 173).
  - The contract still says the checker cannot establish growth of scope (node 125).
  - There is still no `## How you check` section (node 151).

INDEX LINE:    The checker contract is rewritten in plain English at 85% of its size, every rule kept. Fences and cross-file headings are byte-identical, and the labels CONTEXT.md lacks are said in plain words.

FLAGS:         ASSUMPTION: The contract keeps its own `## Words used exactly` list instead of pointing at `CONTEXT.md`, as the manager contract's first part did. The checker is kept blind, and only `map-implementation-rules.md` is an allowed read. On an effort in another repo, the root `CONTEXT.md` is that host repo's own glossary (the concern the human raised at node 56). Pointing a checker at it would add a read the contract otherwise forbids, and in a foreign repo it could send the checker to the wrong file. So this ruling-A cut does not make sense in this file. / The checker contract keeps its own term list, because pointing a blind checker at `CONTEXT.md` would add a forbidden read and could hit a foreign repo's glossary.
ASSUMPTION: "finding" and "the human" stay defined terms, although `CONTEXT.md` defines neither. Clause 1a permits dropping such a term but does not require it. Both are plain English and not coined phrases. "finding" is used throughout, so dropping it would force a wordier phrase at every use. / The checker contract keeps "finding" and "the human" as defined terms, because both are plain words and clause 1a only permits dropping.

NEW NODES:     none

INVALIDATIONS: none. The contract's rules are unchanged, so no resolved node's answer changes meaning. One wording change is worth a sweep: hard rule 5's "the worker holding the code" is now "the implementer". The same party is meant, but it bears on the open question in node 56's annotation (see RULE CHANGES, item 3).

GATE PAYLOAD:
  Checker findings: none yet, this is before the first check.
  Paths touched: `.claude/skills/expedition-checker/SKILL.md` only (in the worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/295-rewrite-the-checker-contract`), uncommitted.
  Bar: the repo has no build, no tests, no formatter and no CI. The worktree root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`, which matches the record in `map-implementation-rules.md`. `git diff --check` is clean.
  Structural checks I ran:
  - Fences diffed against the before-text: identical.
  - Frontmatter: identical.
  - Heading diff: only the two renames.
  - The refused-word grep from the spawn, plus `task`, `item`, `the whole of` and `in as many words`: no hits.
  - Semicolons outside fences: 0.
  - Lines over 106 characters outside tables: 0.
  Proposed commit message:
    Rewrite the checker contract in plain English

    Node: graph-workflow/295

RULE CHANGES:
I made no deliberate rule change. Every item below is borderline, and I list it so the checker's independent list can be matched against mine.
1. Before: "You are read-only. You do not fix what you find." After: "You are read-only. Report what you find, and fix none of it." Why: clause 8a asks for the positive form. Handing back findings is already the checker's whole output, so "report" adds no new duty.
2. Before: given 4 "It is a name, not somewhere to go and read." After: removed. What remains is "The name of the work, which you use only to address a raise", and the record paragraph still says "Leave the record unread, and do not go looking for it." Why: slogan-shaped, and the outcome is already fixed by "only" and by the record rule.
3. Before: hard rule 5 "sends it to the worker holding the code". After: "sends it to the implementer". The search section's "a worker who met the scope as written" is likewise now "an implementer who met the scope as written". Why: it is the same party, and the file already used "the implementer" elsewhere. This settles nothing for the checker file, but node 56's annotation leaves open whether "implementer" or "the worker holding the code" survives across the files.
4. Before: "This duty holds whoever wrote the enumerator." After: "The duties in this section hold whoever wrote the command." Why: "This duty" pointed back past the sentence before it, which clause 8e forbids. The section has only the recorded-command duties, so the reach is the same. It is also listed as a generalisation below.
5. Before: "It is the same file the implementer works from, so the two of you hold the work to one set of rules rather than two", preceded by the reason about changeability ("a rule written in a file can be changed by whoever owns it, where a rule a checker finds for itself cannot"). After: "The implementer works from the same file, so the two of you hold the work to one set of standards." The changeability reason is removed. Why: this is explanation and not a rule, and the fact that the implementer works from the same file is kept. The change of "rules" to "standards" does the narrowing node 173's clause 6 asks for.
6. Before: the fifth raise ground's explanation, "Such a demand is not incoherent, not self-contradicting, not unmeasurable, and what it names can be observed perfectly well by whoever holds the material — so none of the four fits". After: "Nothing is wrong with such a demand, but you cannot check it." Why: this is explanation. The ground, its "fifth beside those four" count, and its whole-or-part routing are all kept.
7. Before: "whom this contract forbids to repair a condition". After: "who may not repair a condition". Why: the checker contract forbids nothing to the implementer, so the before-text named the wrong contract. The fact stated is the same.
8. Removed as repetition, each still covered elsewhere in the after-text:
   a. The paragraph after the table, "An element the work itself added is in none of these rows…". It is covered by the "An element was added" case.
   b. The raise section's list of edits that are "not this ground" (a rationale reworded, an element this work added, an element that moved but is not held against). These are covered by the four moved-standard cases.
   c. The raise section's "Where it reaches only part … hand that part back as not covered". It is covered by the last moved-standard case and by table row 6.
   d. Both copies of "A condition you can check but disagree with is not a raise / check it as written", in the Questions section and the raise section. This is covered by table row 1.
   e. The Questions section's "Where the skill cannot go on at all without an answer, this is not the route: raise it". It is covered by the third reviewing-skill limit.
   f. The standards section's "Search unwrapped text when you read inside one". It is covered by the general unwrap rule, which names "the standards you read".
   g. The standards section's "a property nobody stated is not a finding". It is covered by hard rule 2.
9. Before: given 5 "which every other worker reads … so they are copied into the spawn rather than pointed at". After: "which you do not read, so anything in the map that bears on your check reaches you only as words in the spawn." Why: the fact about other workers is dropped, and the rule is kept.
10. Before: the "Supplying the extent costs you almost nothing — you built the enumerator in order to find the instances…" reason, and the delegation section's "a part run by an agent handed everything you hold is worth more than a part not run at all". After: removed. What remains is "The extent lets the implementer repair every instance…" and "Prefer supplying the givens, because then the part actually runs." Why: explanation of why, cut to one clause.
The `CONTEXT.md` terms I walked in the after-text are manager, checker, acceptance condition, the bar, raise, worker, node, effort, map and record. Each is spelled as `CONTEXT.md` has it, and no term list was replaced by a pointer.

RE-POINTING SEARCH:
Where I searched: the `## Acceptance condition` section, and everything after it up to the next stop heading, of every node whose status is `open` or `claimed`, excluding 295. Each condition was normalised and joined into one string. I adapted `/tmp/claude-1000/n297/search.py`, and my copy is at `$TMPDIR/n295/search.py` (`/tmp/claude-1000/n295/`).
What I searched for:
- (a) every 6-word sequence of the before-text, with each hit classified as KEPT or GONE against the after-text;
- (b) all 19 before-text headings;
- (c) the strings `expedition-checker`, `checker contract` and `checker's contract`;
- (d) these removed or replaced phrases: blindness wins, not decoration, the whole of the looking, instinct is to go looking, operative content, rationale, implementation-rules file, enumerator, bounding set, in as many words, A line is not a unit of meaning, Do not inherit your own conclusion, A standard is not the file that holds it, What a skill delegates is not blind, The enumerator a condition records, the worker holding the code, whole of what you hold, Find these before, one set of rules, Three reasons, six things, The bound is on the sentence, moved-standard, The instances, The form, The extent, extent, not somewhere to go, ordinary case rather than a defect, purely additive, second opinion, Never say, never address, read cold, fifth ground, complete bar, deficient, has no extent, not exhaustive, modification times, reflow, and the kept headings.
Only three nodes quote this file in a way that needs action:
- **Node 173.**
  - Clause 1: replace "the item in the list of what the checker is given that begins `**The bar**`" with "the item in the list of what the checker is given that begins `The bar:`".
  - Clause 4: replace "and that this is a complete bar and not a deficient one" with "and that this is, in the file's words, "the complete bar for such a repo"". The after-text reads: "A repo with no build, no tests and no formatter meets the bar on its remaining half, which is the complete bar for such a repo."
  - Clause 6: replace the quoted sentence with `The implementer works from the same file, so the two of you hold the work to one set of standards`. This sentence already claims only the standards and keeps the ground that the implementer works from the same file. So clause 6 is now met by the rewrite. The manager may keep it, stated as "is kept so that…", or drop it.
  - Clause 8: replace "the given-list item beginning `**The bar**`" with "the given-list item beginning `The bar:`".
  - Clause 5: no change needed. The count sentence now reads "You are given six things. The spawn carries the first five, and you read the sixth for yourself from one file this contract names." It is still arithmetically correct.
- **Node 164.**
  - Clause 4: replace "The file's existing statement of what may be copied to the checker as a ground rule and what may not" with "The file's statement beginning "A ground rule is a standing constraint on the effort that is true of any node's work"". The bold lead it pointed at is gone.
  - Clause 5: it describes rather than quotes, and still matches the after-text "Leave the record unread, and do not go looking for it." No change.
  - Clause 1: the list "the reasoning that led to it, the effort it belongs to, … the rest of the work around it" is kept word for word.
  - Separately, clause 3's "the two routes by which they reach it" was already stale before this rewrite, since there is one route. I did not repair it.
- **Node 151.** Its clause 1 headings `## Hard rules` and `## What you hand back`, and its clause 10 shapes `PASS`, `FAIL: acceptance condition`, `FAIL: the bar` and `NOT COVERED`, are all kept. No change needed.
No action needed for the rest:
- Node 56's annotation quotes "the part of the work the implementer may edit" (kept) and "the condition's own and so was not the worker's to depart from" (kept). It also notes that the checker file uses "the worker holding the code". That phrase is now "the implementer" (RULE CHANGES, item 3). The annotation's open question now reads with the checker file on the "implementer" side. This is not a condition clause.
- Node 49's annotation cites four unwrap sites in the checker contract by line number. There are now fewer sites: the general rule, the moved-standard section and the reflow bullet. This is also not a condition clause.
- These nodes name the file only to exclude it or to say "in the voice of", so nothing changes: 41, 43, 44, 55, 73, 79, 155, 279.
- Nodes 109, 111, 137, 148, 247 and 304 use "enumerator" or "bounding set" as their own vocabulary for other files, not as quotes of this file. Once node 109 lands, those words will be defined in other files while the checker file says them in plain words. That is worth knowing, and it breaks no condition.
- Nodes 80, 81, 90, 205, 271 and 284 use "complete bar … not a deficient one" about `map-implementation-rules.md` or their own bar, not about this file.
- Nodes 190 and 276 matched only the generic phrase "an implementation node's work is held". Node 60 matched only "not wait for an answer and", in its own clause.
- The rewrite nodes 291–302 list this file in their clause 5. The headings that clause protects are all kept, and the two renamed headings appear in no other file.
- Nodes 72 and 125 quote this file in their `## Question` only, not in a condition.

GENERALISATIONS:
1. "The duties in this section hold whoever wrote the command." It replaces "This duty holds whoever wrote the enumerator." The section's duties are all the recorded-command duties, so every case comes out the same.
2. One general unwrap rule ("Unwrap text into unbroken lines before you search it, wherever you search: the work, the standards you read, or a change nobody told you about") now carries three before-text statements: the given-section rule, the standards section's "Search unwrapped text when you read inside one", and the reason in the moved-standard section's "Unwrap both sides first — a standard rewritten in place is usually rewrapped too". The reflow bullet is kept, because it adds a procedure.
3. The not-covered section's "second cause" and the raise section's "standard the work moved" ground now point at `### Where the work moved one of them` ("falls under the last case of…", "in the case … sends here") instead of restating it. The outcomes are unchanged.
None of these changes an outcome, and none decides a case the before-text left open.

RETROSPECTIVE:
(1) What I had to hunt for:
- What ruling B means for ordinary-English terms like "finding". It is in node 290's gate section, where the pilot's flag 290.1 dealt only with a coined label. I looked in the spawn first. I settled it as flag 2.
- Whether any other file references this file's sections. A grep over the shipped files found only `NOT COVERED:` in graph-conventions.
- Which headings clause 5 protects. I had to compute this by grepping each heading against the 16 listed files. The spawn could name the protected headings, since the manager or an earlier worker has probably computed them already.
(2) What arrived that this node did not need:
- The whole of `map.md`, apart from the worktree paragraph and the pointer to the rules file.
- The whole of `map-implementation-rules.md`'s review-route prose, where only the writing rules and the ground rules bore on the work.
- Full condition dumps for nodes 41, 43, 44, 55, 73, 79, 111, 61 and 81, which name the file only to exclude it. A search mode that prints only the clause containing the hit would have avoided about 40KB.
(3) What would have made this node easier:
- A list of the heading texts protected in this file, and of the open nodes that quote it, precomputed in the spawn (this node's list: 151, 164, 173).
- Stating in the spawn that ruling B applies to coined labels, not to plain defined words.
- A shared, maintained search script in the record rather than per-node copies under /tmp.
(4) What was stale, wrong or contradictory:
- The before-text said "whom this contract forbids to repair a condition", which is wrong for the checker contract (RULE CHANGES, item 7).
- Node 164's clause 3 says "the two routes by which they reach it", but the file has had one route since the standards moved into a file.
- `map.md` says `CONTEXT.md` holds 51 entries, a figure it dates itself.
- My run was also interrupted once by a rate limit. The file I had written before the stop was intact on disk, and I resumed from it.

## Review

### Checker run 1 — `FAIL`, acceptance condition (as amended by the human)

*The checker's own text, pasted, 2026-09-25. The checker was resumed from node 290's check.*

> FAIL: acceptance condition
>
> The work fails on clause 8c only: five passages still say an idea with a figure of speech or an idiom. Every other clause is met, and the bar holds. The fixes are small; most need only a word or phrase changed. All line numbers below refer to the after-text in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/295-rewrite-the-checker-contract/.claude/skills/expedition-checker/SKILL.md`.
>
> My contract is the master copy of `expedition-checker/SKILL.md`. It is byte-identical to the before-text at merge-base `527596c`, so the work did not change the file I checked under. I read the changed path only as the work.
>
> **Finding: clause 8c, figures of speech (5 instances)**
> - **Instances:**
>   - Line 338, "the acceptance condition itself, read cold, with none of the reasoning behind it". "Read cold" is an idiom. The plain gloss follows in the same sentence, so deleting "read cold," is enough.
>   - Line 342, "A fifth ground sits beside those four and looks nothing like them". The grounds are made to sit and to look.
>   - Line 102, "so that the standard moves under your check", and line 216, "the work has moved the listed files under you". "Under you" is an idiom.
>   - Line 175, "whichever route it travels". A finding is made to travel. This is lighter than the ones above.
>   - Line 312, "The same route takes a second case". A route is made to take a case. Also lighter.
> - **Form:** a phrase outside a code fence that carries an idea `CONTEXT.md` does not define by means of a non-literal verb or an idiom, where a literal wording exists.
> - **Extent (bounding set):** every prose sentence of the after-text, read by hand. A starting list comes from `awk '/^```/{f=!f;next} !f' .claude/skills/expedition-checker/SKILL.md | grep -n -i -E 'cold|nothing like|under you|under your|travels|takes a|sits|carries|survive|blind|moved'`. The words that grep also returns and that I judged acceptable are listed under clause 8c below.
>
> **Clause by clause**
> 1. **Rule changes: met.** Under the amendment, a rule change does not fail the work. They are listed under RULE CHANGES below.
>    - Dropping these terms is allowed by clause 1a, because each meaning is still stated in plain words where it was defined, so none is a rule change: *implementation-rules file*, *enumerator*, *bounding set*, *operative content*, *rationale*, and the definition of *reviewing skill*. None of them is defined in `CONTEXT.md`.
>    - Not a finding, but worth fixing: line 269, "Each row takes a different shape", is untrue. The two raise rows hand back the same shape, and so do the two not-covered rows. It binds nothing.
> 2. **Added statements: met.** They are listed under RULE CHANGES.
> 3. **Generalisation: met.** Before-text line 266 said "This duty holds whoever wrote the enumerator". The after-text widens it to "The duties in this section hold whoever wrote the command". No outcome changes, because the other duties in that section already applied whoever wrote the command. The table now carries the before-text's closing lines that routed a condition you disagree with and a condition met and wrong anyway. The "where the work moved" bullets now carry the raise section's three edits that are not a ground to raise. Both moves give the same outcomes.
> 4. **Fixed text: met.** I extracted the frontmatter and all code fences from both versions and diffed them. They are identical.
> 5. **Headings: met.** Two headings were renamed: "### What a skill delegates is not blind" and "### The enumerator a condition records". I searched the 15 listed files (unwrapped) for both texts, in the worktree and in the main tree, and neither appears in any of them. All other headings are identical.
> 6. **References inside the file: met.** Each one resolves:
>    - "`## What you hand back`" and "the file `## The standards you hold the work against` names"
>    - "the list that follows", "the three below", "the table below" and "Everything below"
>    - "under `NOT COVERED:` below" and "under `QUESTIONS:` below"
>    - "`### What every finding carries`"
>    - "the last case of `### Where the work moved one of them`", which is the final bullet of that section
>    - "The six givens above"
> 7. **Terms: met.** Terms from `CONTEXT.md` are spelled as it defines them. "The worker holding the code" became "the implementer". Both the before-text and `CONTEXT.md` itself already use "implementer", so I judged that acceptable. I checked the refused words by hand: report, run, question, done, complete, review and reject. Each is used for a concept other than the one refused, and "reject" is only mentioned as the human's word. No new term is coined, since "givens" was already in the before-text.
> 8. **Plain English: fails on 8c**, as above. The other five properties hold:
>    - 8a: every prohibition sits beside its positive statement.
>    - 8b: bold appears only on the seven terms in the word list.
>    - 8d: no slogan-shaped sentence, and "the whole of what" does not appear.
>    - 8e: I read every it, this, that, they, these, those and them. Each has one clear referent in its own sentence or the one before. "This contract", "this section" and "this route" refer to the text they stand in.
>    - 8f: no semicolons. Every dash is a separator in the word list, apart from one in a heading.
>    - Words I judged acceptable under 8c:
>      - "moved/unmoved/survives": the fixed `NOT COVERED:` template, which clause 4 freezes, uses "unmoved", so the prose has to use the same word.
>      - "blind to the record": this is the standard technical sense of "blind", and the implementation-rules file uses it too.
>      - "carries": used in its plain sense.
> 9. **Size (reported, not enforced):** the rewritten range is the whole file. `wc -w` gives 4798 before and 4093 after, which is 85% of the before-text. The target of at most 3199 is missed, which does not fail the work.
> 10. and 11. **Scope: met.** `git status --porcelain --untracked-files=all` shows only `.claude/skills/expedition-checker/SKILL.md` modified.
>
> **RULE CHANGES**
> 1. **Added duty.** Before (intro): "You are read-only. You do not fix what you find." After (intro): "You are read-only. Report what you find, and fix none of it." The new "Report what you find" has no limit on it. The before-text never required reporting everything you find, and it says elsewhere that a property nobody stated is not a finding. The after-text keeps "Hand back only findings that touch the acceptance condition or the bar" under `### Running a reviewing skill`. Outside a skill run, though, the new duty can decide a case the before-text did not.
> 2. **Narrowed exception (borderline reading).** The before-text covers two cases: the implementation-rules file does not exist, or it exists and states no standards. It says: "An effort that has never written one is the ordinary case rather than a defect … so this is a route the contract expects you to take, not a fault to report." I read "this is a route" as covering both cases. After: "A missing file is the ordinary case for an effort that has never written one … so it is not a fault to report." For a file that exists but states no standards, the after-text no longer says it is not a fault.
>
> How far the list reaches: I compared every statement of the before-text, from the intro through `## When you are handed the same work again`, with its counterpart in the whole after-text. I covered every rule, condition, closed list and count, template, defined term and refused word. Beyond the two above I found no rule change. That includes the three items in the three limits on running a skill, the two ways to meet the rule for a skill that spawns an agent, the three extents, the three reasons, the six givens, the two kinds of question, the four grounds plus the fifth, and the six table rows.
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`, which matches the rules file. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md`, the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:**
>   - Standing rule 5 (plain English), which is the same property as clause 8.
>   - Standing rules 1 and 3, which are met.
>   - `CONTEXT.md`'s `_Avoid_` lines.
>   - `graph-conventions.md`'s account of the `## Review` section, which is consistent with the rewrite.
>   - `/writing-for-agents` (on stating the positive), read from the installed plugin.
>   - All five ground rules, which are met. Nothing tells the checker to address the human.
> - `/coding-principles` and `/naming` had no bearing on this prose. No reviewing skill is named, so I ran none.
>
> **Disclosure:** a search I ran across `.claude` for the term "enumerator" also matched record files under the main tree's `.claude/worktrees/250-…/.scratch/graph-workflow/`: `decisions.md`, `flags.md` and some node files. I used nothing from those lines and reasoned from none of them. For clause 5, I searched `map.md` and `map-manager-only.md` for the two old heading texts and read nothing else in them, because the condition names both files.

*The manager's note, matching the two lists:* the checker's rule change 1 is the worker's 1. The checker's rule change 2, the narrowed exception for a rules file that exists but states no standards, is not on the worker's list. Under the amended pass, an unlisted change goes back as a correction, together with the 8c finding.

### Correction round 1 — the worker's changes for checker run 1

*The worker's own text, pasted, 2026-09-25.*

CORRECTION ROUND 1 — Rewrite the checker contract in plain English

The checker's clause 8c finding is fixed, and so is the rule change it found that I had not listed. The file now restores the before-text's outcome for both no-standards cases, so that change is gone rather than added to my list. I also fixed the untrue sentence the checker noted and 14 more phrases of the same kind as its finding. Nothing I changed touches what the condition names beyond clause 8c. Fences, frontmatter and headings are unchanged. The file is now 4,132 words, 86% of the before-text's 4,798; it was 4,093.

WHAT CHANGED, for each thing the checker found. Quotes are from the after-text.

Clause 8c, its five instances:
- "read cold": removed. The sentence now reads "The first is the acceptance condition itself, read with none of the reasoning behind it."
- "A fifth ground sits beside those four and looks nothing like them:" now reads "There is also a fifth ground, unlike those four:".
- "so that the standard moves under your check" now reads "so the work under check may have changed the standard itself."
- "the work has moved the listed files under you" now reads "the work has changed the listed files since then".
- "whichever route it travels" now reads "whether it is an entry under a `FAIL` or something handed back alongside an outcome."
- "The same route takes a second case" now reads "This section also covers a second case". In the same sentence, "it falls under the last case of …" now reads "the last case of `### Where the work moved one of them` applies to it".

I then read every prose sentence for the checker's form, a non-literal verb or an idiom where a literal wording exists. I changed these too:
- "The file sits beside the record" now reads "The file is in the same directory as the record".
- "can sit in one of the paths" now reads "can be in one of the paths".
- "whether you raise or carry on" now reads "whether you raise or continue the check".
- "would take you into the record" now reads "would have you read the record".
- "may also take it into the record first" now reads "may also have it read the record first".
- "Either of two things puts you there." now reads "Two things can cause a raise."
- "in the case `### Where the work moved one of them` sends here:" now reads "in the last case of `### Where the work moved one of them`:".
- "that bears on your check" now reads "that matters to your check".
- "An edit reaches a standard" now reads "An edit affects a standard".
- "a return that reaches a place" now reads "a return that includes a place".
- "the condition's command reaches material you are blind to" now reads "the condition's command searches material you are blind to".
- "sends the work back to the feature … to the build" now reads "sends the work back for changes to the feature … for changes to the build".
- "Where the part reaches the whole condition" now reads "Where the part covers the whole condition".
- "Raise where it reaches the whole condition" now reads "Raise where it applies to the whole condition".
- "the change reaches", "the amendment reaches" and "does not reach" now read "affects", "affects" and "does not affect".
- "reach the human by this route" now reads "reach the human this way".

The checker's note on line 269 ("Each row takes a different shape" is untrue): the sentence now reads "Where what you check against is itself the problem, find the row for what you can still establish in the table below, and hand back what that row names. The routes are not interchangeable." The second sentence keeps the before-text's "they are not interchangeable" without claiming that each row has its own shape.

The checker's rule change 2 (the no-standards exception had been narrowed): I restored the before-text's outcome for both cases, so there is no rule change to list. The paragraph now reads: "Where the file does not exist, or states no standards, hold the work against the acceptance condition and the bar alone, and say so in your outcome. Look for no other standards. In either case, holding the work against the condition and the bar alone is a route the contract expects you to take, so it is not a fault to report. An effort that has never written the file, as in any fresh repository, is the ordinary case."

DID THE CHANGE TOUCH WHAT THE CONDITION NAMES: yes, but only clause 8c, and clause 1 through the restored exception. The fences are still byte-identical to the before-text, and so is the frontmatter. The heading list is identical to run 1. The refused-word grep finds nothing. There are still no semicolons outside fences and no lines over 106 characters outside the table. `git diff --check` is clean. The only path changed is still `.claude/skills/expedition-checker/SKILL.md`.

RULE CHANGES: as first returned, items 1 to 10. The checker's rule change 2 is not added, because the change is undone. The checker's rule change 1 matches my item 1. Two rewordings this round might be read as borderline:
- "reaches the whole condition" became "covers" or "applies to the whole condition". The before-text's "reaches" means the same extent.
- "a return reaching a place the condition's list does not name" became "a return that includes a place …". The before-text meant a result of the command naming such a place.
Neither changes any outcome.

RE-POINTING SEARCH, for this round's changed wording: I searched the open and claimed conditions for read cold, route it travels, route the finding travels, under you, under the check, carry on, back to the feature, the change reaches, the amendment reaches, sits beside, moves under, moved under, puts you there, looks nothing like, fifth ground, not interchangeable, shapes below, reaching a place, material you are blind to, bears on your check, route the contract expects, ordinary case, and not a fault to report. The script was the same one as before. The only hit is node 120's "no standard moved under the check", and it is a demand on the manager contract, not a quote of this file. No new replacement clause is needed. The earlier replacements for nodes 173 and 164 still stand as first returned, because none of the wording they quote changed this round.

FLAGS: every flag as first returned.

GATE PAYLOAD: I changed what each checker finding above says. Paths touched: `.claude/skills/expedition-checker/SKILL.md` only. The commit message is as first returned.

Every other part is as first returned.

### Checker run 2 — `PASS`, under the amended condition

*The checker's own text, pasted, 2026-09-25.*

> PASS
>
> This is check 2 of node 295. The five 8c passages from run 1 are fixed, and so is the untrue sentence about the table. The corrections add no new breach, and the bar still holds. One rule change remains ("Report what you find"), which does not fail the work under the amendment.
>
> My contract is the master copy in the main tree. I read the changed path only as the work.
>
> **What changed since run 1.** No statement of changes came with this check, so I compared the current file paragraph by paragraph against the run-1 text I read in full. The word count went from 4093 to 4132. These are all the edits I found:
> - Line 49: "that bears on your check" became "that matters to your check".
> - Line 90: "The file sits beside the record" became "The file is in the same directory as the record".
> - Lines 94–97: rewritten, so the rule that this is not a fault now covers both a missing file and a file with no standards (run-1 rule change 2).
> - Line 103: "so that the standard moves under your check" became "so the work under check may have changed the standard itself". Line 104's "An edit reaches a standard" became "affects".
> - Line 108: "raise or carry on" became "raise or continue the check".
> - Line 142: "would take you into the record" became "would have you read the record". Line 153 has the same edit.
> - Line 176: "whichever route it travels" became "whether it is an entry under a `FAIL` or something handed back alongside an outcome".
> - Line 218: "moved the listed files under you" became "changed the listed files since then".
> - Line 221: "reaches a place" became "includes a place". Line 235: "reaches material" became "searches material".
> - Line 266: the feature and the build now each say "for changes to …".
> - Lines 270–271: "Each row takes a different shape…" became "find the row for what you can still establish in the table below, and hand back what that row names. The routes are not interchangeable."
> - Line 284: "by this route" became "this way".
> - Lines 314–315: "The same route takes a second case" became "This section also covers a second case", with "the last case of `### Where the work moved one of them` applies to it".
> - Line 333: "reaches the whole condition" became "covers". Line 345: "applies to".
> - Line 338: "Either of two things puts you there" became "Two things can cause a raise".
> - Line 340: "read cold," removed.
> - Line 344: "A fifth ground sits beside those four and looks nothing like them" became "There is also a fifth ground, unlike those four".
> - Line 349: "in the case `### Where the work moved one of them` sends here" became "in the last case of `### Where the work moved one of them`".
> - Lines 372, 388 and 392: "reaches" became "affects".
>
> **Clause by clause**
> 1. **Lost or changed statements: met.** The rule change is listed below. The rewritten no-standards paragraph now matches my reading of the before-text: "this is a route the contract expects you to take, not a fault to report", covering both cases. So run-1 rule change 2 is gone. The clause 1a term drops stand as in run 1.
> 1a. **Terms `CONTEXT.md` does not define: met**, unchanged from run 1.
> 2. **Added statements: met.** None of the new edits adds a rule.
> 3. **Generalisation: met.** Only one reading matters here. If the before-text's "this is a route" is read as covering only a missing file, then "In either case" decides a case the before-text left open, and that would be a rule change under this clause. I read it as covering both, as in run 1.
> 4. **Fixed text: met.** Re-run: the frontmatter and all code fences are byte-identical to the before-text.
> 5. **Headings: met.** The headings are unchanged since run 1. The only two renamed headings still appear in none of the listed files, as established in run 1.
> 6. **References inside the file: met.** The new "the last case of `### Where the work moved one of them`" (twice) points at that section's final bullet. "the table below" resolves. All other references stand as in run 1.
> 7. **Terms: met.** The new edits introduce no refused word and no new term.
> 8. **Plain English: met.**
>    - 8c: each run-1 passage is replaced by a literal wording, and I found no new figure of speech. My run-1 judgements on "moved/unmoved", "blind" and "carries" stand.
>    - 8e: I read every new pronoun. Each has one clear referent in its own sentence or the one before:
>      - "so it is not a fault to report" refers to holding the work against the condition and the bar alone.
>      - "since then" refers to when the condition was written.
>      - "what that row names" refers to the row in the same sentence.
>      - "applies to it" refers to the part.
>      - "those four" refers to the four grounds in the sentence before.
>    - 8a, 8b, 8d and 8f: re-run. There are no semicolons, and the only dashes are the 7 word-list separators and 1 heading. Bold is only on the 7 terms in the word list. "The whole of what" does not appear.
> 9. **Size (reported, not enforced):** the rewritten range is the whole file. `wc -w` gives 4798 before and 4132 after, which is 86% of the before-text. The target of at most 3199 is missed, which does not fail the work.
> 10. and 11. **Scope: met.** `git status --porcelain --untracked-files=all` shows only `.claude/skills/expedition-checker/SKILL.md` modified.
>
> **RULE CHANGES** (for the file as it now stands)
> 1. **Added duty.** Before (intro): "You are read-only. You do not fix what you find." After (line 15): "You are read-only. Report what you find, and fix none of it." "Report what you find" has no limit on it. The before-text never required reporting everything you find, and it says a property nobody stated is not a finding. Line 141, under `### Running a reviewing skill`, still says "Hand back only findings that touch the acceptance condition or the bar". Outside a skill run, though, the new duty can decide a case the before-text did not.
>
> How far the list reaches: the whole before-text, compared statement by statement against the whole after-text. I covered every rule, condition, closed list and count, template, defined term and refused word. Run 1 was a full comparison, and I re-read every edit listed above against the before-text. None of those edits adds, loses or changes an outcome, beyond resolving run-1 rule change 2. The list above is complete as far as I can establish.
>
> **The bar, re-run in full**
> - The repo has no build, tests, formatter or CI, and `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md`, unchanged since run 1: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:**
>   - Standing rule 5 (plain English), which is the same property as clause 8.
>   - `CONTEXT.md`'s `_Avoid_` lines.
>   - `/writing-for-agents`.
>   - All five ground rules, which are met.
> - No reviewing skill is named, so I ran none.

*The manager's note, matching the two lists:* the checker's one rule change is the worker's item 1. The worker's items 2 to 10 the checker judged to keep their outcomes. Nothing on the checker's list is missing from the worker's.


### Gate — approve, 2026-09-25

The human, `verbatim`: *"approve"*

## Flags

`295.1` **· settled** `ASSUMPTION` — The contract keeps its own `## Words used exactly` list instead of pointing at `CONTEXT.md`, as the manager contract's first part did. The checker is kept blind, and only `map-implementation-rules.md` is an allowed read. On an effort in another repo, the root `CONTEXT.md` is that host repo's own glossary (the concern the human raised at node 56). Pointing a checker at it would add a read the contract otherwise forbids, and in a foreign repo it could send the checker to the wrong file. So this ruling-A cut does not make sense in this file.

`295.2` **· settled** `ASSUMPTION` — "finding" and "the human" stay defined terms, although `CONTEXT.md` defines neither. Clause 1a permits dropping such a term but does not require it. Both are plain English and not coined phrases. "finding" is used throughout, so dropping it would force a wordier phrase at every use.
