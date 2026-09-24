# Rewrite the manager contract's first part in plain English

Type: implementation
Status: resolved
Supersedes: 306
Blocked by: 290

## Question

Rewrite the first part of `.claude/skills/expedition/SKILL.md` in plain English and shorter, under the pass [node 289](289-a-plain-english-and-compaction-pass-over-the-shipped-files.md) settled.

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
    - G1: from the start of the file up to, but not including, the heading `## Spawning a worker`.
    Clause 1's walk covers the binding statements in the before-text of the rewritten range. Their counterparts may be anywhere in the whole after-text.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-24. The worker's own text, pasted. The flags are raised under `## Flags` at the gate.*

### Answer

#### What was built
`.claude/skills/expedition/SKILL.md`, from the start of the file up to the heading `## Spawning a worker`, is rewritten in plain English (standing writing rule 5, condition clause 8). Everything from `## Spawning a worker` to the end of the file is byte-identical to the before-text, checked with `diff`. So is the frontmatter. The range has no code fences.

- Bold now appears only on a term where it is defined. That means the `## Words used exactly` terms, plus **kind** and **fog**, which are defined inside the node and map entries.
- Prohibitions stand beside a positive statement, or were turned into one.
- Rewritten slogans and figures of speech: "That is about recording, not about files", "Assembling is not authoring", "the resource that fails first", "low resolution", "reads cold", "one referee", "starved", "in flight", "provable rather than felt", "with the bound taken off", "won its point", "picks it up".
- Sentences with more than one semicolon or dash aside were split.
- Pronouns whose referent was more than one sentence back were replaced with the noun.

#### Size
`wc -w` of the range (lines 1–237, frontmatter included): 2929 before, 2810 after. That is 95.9%, against a target of 66% that is reported but not enforced.

Why it is not shorter:
- `## Words used exactly` is 1362 words, 47% of the range. It is all definitions, and clause 1 keeps every definition. Plain English saves almost nothing there.
- The prose sections were already dense, and splitting sentences costs words.

If the human wants deeper cuts, there are three routes. Each is a rule change, not a rewrite:
- let the Words list point at `CONTEXT.md` instead of restating it;
- drop the `## What is never yours` table, whose rows restate rules found elsewhere in the file (node 278 depends on the table);
- merge `### Item 5, the check you stop on` into item 5.

#### Headings
- Every heading in the range keeps its exact text.
- Clause 5 requires three of them: `## Words used exactly`, `## What is never yours` and `### The human's words`.
- `## Writing the graph` is cited by node 287's condition.
- The number of `## ` headings is unchanged (15), because node 111's condition counts them.

#### Deduplications and merges (the generalisations made)
1. The map entry's "which an agent confirms against the repo before using" was removed. Its counterpart is in the bar entry: "the map's record of those commands is confirmed against the repo before use."
2. The handover entry's "A part it has nothing for comes back as `none` written out in full, and a part left off is a missing part." was removed. Its counterpart is in `## What comes back`, which is outside the range and unchanged: "`none`, written out in full, is load-bearing … A part left off is a missing part, and a part answered `none` is an answer." Node 297's rewrite must keep that statement, because it is now the only one.
3. The sweep entry's "the same pass with the bound taken off: looking for revisions nobody propagated. A cascade knows what changed; a sweep is looking." became one statement: "the same pass as a cascade, not bounded by a known revision: it looks for revisions nobody propagated."
4. "You do not do the work. Workers do." became "Workers do the work, and you leave it to them."

#### Explanations cut to a clause (none of them binding)
- Order section: "the one step in the order that cost does not explain, and so the one a later editor will get wrong" · "their channel takes one thing at a time regardless" · "spawns run out, and the question goes", now "The limits on spawning still keep a question from waiting for ever."
- Item 5 section: "not by taking the items out of order", and the worked example, which is shortened.
- Scribe section: the "Two things this protects" paragraph became one sentence that keeps the count of two.
- The human's words: "What that protects is" became a "so" clause.

#### Carried over unchanged
- The `worker` entry ("It is resumed in place rather than replaced.") and the `attempt` entry are byte-identical. Their contradiction, reported by node 258, stands.
- The `implementation` entry still says "The node ends at a gate". This contradicts `CONTEXT.md` as node 242 fixed it; see NEW NODES.
- Item 5 still says "the human has something to do, or provably nothing is waiting, and nothing an agent handed back is still unfiled". The before-text was ambiguous about how these conditions group, and the rewrite keeps that ambiguity rather than picking one reading.

#### Search of open acceptance conditions
**Handles searched:** (a) Every quoted string of 3 or more words in the `## Acceptance condition` sections of all open or claimed nodes, matched against the normalised before-text of the range. The script allows quotes that span lines, which the pilot's script (one line at a time) missed. (b) Every heading in the range, across clause 5's file list and the open conditions. (c) The phrases this work removes or replaces: "fails first", "low resolution", "reads cold", "about recording", "not about files", "Assembling is not", "referee", "starved", "in flight", "rather than felt", "code path", "bound taken off", "interrupting", "won its point", "picks it up", "each log", "this protects", "Properties rather than", "alongside its outcome", "channel's property", "You do not do the work", "too coarse", "end to end", "later editor", "sitting unsent", "tempted", "yours alone", "Five parts", "written out in full", "not permission", "on inference", "silence about scope", "divergence", "provably", "fifth test", "nothing is waiting". (d) Every open condition naming `expedition/SKILL.md` or "manager('s) contract": 34 nodes. Every condition not belonging to a rewrite node was read in full.

**Result: no condition needs a replacement clause, and none is proposed for supersession.**
- **120** quotes "A node outlives its attempts: a dead worker is replaced, and the replacement is a new attempt recorded after it." That sentence is unchanged in this file. (Note: clause 4 of node 120 attributes it to `CONTEXT.md`, which actually reads "…a new attempt." without "recorded after it".)
- **258**: the attempt and worker entries are unchanged.
- **278**: every row of the table keeps its first cell and its order. The `rewriting an acceptance condition` row is unchanged in both cells.
- **287**: Clause 3's sentence stands: "…every procedure in `graph-conventions.md` are yours, and no worker performs one." Clause 4 describes a statement and does not quote it. It still holds, against: "That rule covers recording only. Where a node's own work is a change to a graph file, that node's worker makes the change itself, as it would any other work."
- **111**: `## Words used exactly` is still the first `## ` heading. The count it records, "fourteen", was already wrong before this work: there are 15.
- **304**: its enumerator `grep -rln "the standing preferences, the fog" .claude/` still does not hit this file, because "the" and "**fog**" stay split across a line break and the word stays bold.
- **109**: its "self-contained" enumerator still hits this file.
- **137**: the count of "pick report" in the range is unchanged.
- **105**: the `revision` definition is kept.
- **127, 297, 298**: they quote `## What is in front of the human, and when`, which is outside the range.
- **61, 81, 57, 118**: they match text in other files or their own wording, not this range.

**Triggers file:** `.claude/rules/expedition-triggers.md`'s `## Priority` copy now differs from the governing list in wording but not in outcome. Clause 13 of node 301 asks only for the same outcome.

#### Dead or default rules
None judged.

### Index line

The manager contract's opening, glossary, never-yours table, act order and graph-writing sections are rewritten in plain English at 96% of their size, every rule and cited heading kept.

### Flags, as handed back

- ASSUMPTION: The handover entry's `none` rule was removed as a duplicate. `## What comes back` states the same rule outside the rewritten range, so the rule is kept once in the file. Node 297, which rewrites that section, must keep it. — *Index:* The manager contract's handover entry no longer restates the `none` rule; `## What comes back` now holds its only statement, which node 297's rewrite must keep.
- ASSUMPTION: Item 5's check keeps the before-text's ambiguous grouping of "has something to do, or provably nothing is waiting, and nothing … unfiled". The rewrite did not choose between the two readings, because a rewrite preserves meaning. — *Index:* Item 5 of the manager's act order keeps its original ambiguous grouping of three conditions; resolving it would be a rule change.
- ASSUMPTION: Two words that `CONTEXT.md` refuses were replaced where the before-text used them for the refused concept. "which section each log sits in" became "which section each record goes in" (`_Avoid_: log` for interview). The cascade's "interrupting the human" became "raising anything to the human" (`_Avoid_: interrupt` for raise). — *Index:* The manager contract's opening sections no longer use "log" or "interrupting" for concepts `CONTEXT.md` refuses them for.

### New nodes

Filed as [node 306](306-the-manager-contracts-implementation-entry-says-the-node-ends-at-a-gate.md), carrying the worker's text.

### Invalidations

none. The rewrite preserves meaning. It carries over, unchanged, the contradiction node 258 reports and the defect named in NEW NODES.

### Gate payload

- Checker findings: none yet (no checker run has reached me).
- Paths touched: `.claude/skills/expedition/SKILL.md`, in the worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/296-rewrite-the-manager-contract-part-1`. It is uncommitted. Scratch files outside the repo are in `/tmp/claude-1000/n296/`.
- Bar: the repo states no build, test or format commands. There is no manifest, CI or agent instruction file, which matches the record in `map-implementation-rules.md`. `git diff --check` is clean.
- Method skills: none invoked, so nothing was left unrun.
- Proposed commit message: `Rewrite the manager contract's opening sections in plain English` / blank / `Node: graph-workflow/296`

### Retrospective

(1) **What I hunted for.** Which open conditions quote the range: I looked first at the pilot's `/tmp/claude-1000/n290/q.py`. It matches one line at a time, so it missed node 120's quote, which spans lines. I wrote a version that handles multi-line quotes · Node 304's grep hazard: I found it only by reading its condition in full · The headings clause 5 protects, by grepping its 16-file list · That the `implementation` entry's "ends at a gate" was left behind by node 242: I found it by grepping the nodes.

(2) **Context this node did not need.** `map.md` read whole; only the pointer to writing rule 5 and the worktree paragraph mattered · `decisions.md` read whole; about five of its 175 lines mattered (242, 289, 290 and the related ones) · Node 289's `## Answer`: its retrospective and disposal parts carried nothing for this node · `map-implementation-rules.md`: only rule 5 and the bar paragraph mattered, and the condition's clause 8 already restates rule 5 · A better arrangement: the spawn names the open nodes whose conditions name the file under rewrite. That one grep saved me reading 34 conditions to find the 5 that mattered.

(3) **What would have made this easier.** A shared quote-matching script for the pass that handles multi-line quotes · A size target that accounts for definition lists, which clause 1 keeps whole · A note that node 242 changed only the glossary.

(4) **Stale, wrong or contradictory.** The manager contract's `implementation` entry contradicts `CONTEXT.md` (NEW NODES) · Node 120's clause 4 attributes to `CONTEXT.md` wording that only `SKILL.md` holds · Node 111's recorded count of fourteen `## ` headings was already wrong before this work: there are 15 · The triggers file calls its priority list "a copy". After this rewrite it is a copy in outcome only.

## Review

### Checker run 1 — `FAIL`, acceptance condition

*The checker's own text, pasted, 2026-09-24.*

> FAIL: acceptance condition
>
> The bar holds. The repo root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. It has no manifest, no task runner, no formatter and no CI, which matches the implementation-rules file. That means there are no commands to run, and the bar is its non-command half. I held the work against every part of that half and found nothing beyond the entries below.
>
> Standards read: `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md`, meaning the bar section, the review route, the ground rules and the five standing rules for writing. I also read `CONTEXT.md` (its `_Avoid_` lines) and `/writing-for-agents`, which I found by name in the mattpocock-skills plugin. The rules file names no reviewing skill, so I ran none. The only changed path is a shipped skill file, not an effort record file, so the record-as-work rule did not apply.
>
> How I checked: the before-text is `git show 4068519:.claude/skills/expedition/SKILL.md` (the merge-base). The after-text is the worktree file. The rewritten range G1 is before-text lines 1–237 and after-text lines 1–227, ending at `## Spawning a worker`.
>
> **Clauses that hold**
> - Clause 2: holds, except for the cascade entry in finding 1.
> - Clause 3: the generalisations I found decide every case as before. For example, "Whether a raise waits depends only on its channel", and the sweep entry.
> - Clause 4: the frontmatter is byte-identical. Neither the before-text nor the after-text of the range has a code fence.
> - Clause 5: all 9 headings in the range are byte-identical.
> - Clause 6: "every act below" points at the list that follows it. `## What is in front of the human, and when` exists at line 520 of the after-text. The unchanged part's references into the range, such as "the parts above" and "what is never yours", still resolve.
> - Clause 7: I compared the distinctive `_Avoid_` words before and after. The range adds no refused word and no new term. It drops "interrupt" and "log", both of which are refused words.
> - Clause 8a, 8b, 8d, 8e, 8f: hold. 8a: each prohibition sits beside its positive. 8b: bold appears only on the term at its own definition. 8d: "the whole of what" does not appear. 8e: I checked each pronoun. 8f: no sentence has more than one dash aside, and each table row has one semicolon.
> - Clauses 10 and 11: `.claude/skills/expedition/SKILL.md` is the only changed path, and nothing is untracked. Everything from `## Spawning a worker` to the end of the file is byte-identical (checked with `cmp`).
> - Clause 1, apart from the three entries below. Two statements were removed from the range, and each still has a counterpart elsewhere in the file: Handover's "comes back as `none` written out in full … a part left off is a missing part" is covered under `## What comes back`: "`none`, written out in full, is load-bearing … A part left off is a missing part". Map's "which an agent confirms against the repo before using" is covered by the bar entry: "the map's record of those commands is confirmed against the repo before use".
>
> **Clause 9 (reported, not enforced):** `wc -w` of the range is 2929 before and 2810 after, which is 96%. The target is at most 1953, so it was missed.
>
> **Findings**
>
> Findings 1 to 3 are all clause 1 failures and share one form. Form, as a predicate: an after-text sentence that is the only counterpart of a before-text binding statement, where the change of wording makes it cover a different set of cases. Extent: none. The instances are what my walk of G1, paragraph by paragraph, found in the files I hold. They are not proven exhaustive.
>
> 1. **Cascade entry, after line 109–110.** Before: "queueing graph edits rather than interrupting the human". This is also `CONTEXT.md`'s wording. After: "It queues graph edits rather than raising anything to the human." Why it fails: under the file's own **raise** entry, a flag is a raise that waits. So "anything" now forbids a cascade from leaving a flag, and a flag blocks nothing, so the before-text did not forbid it. The after-text also adds a prohibition, which breaches clause 2.
> 2. **Gate entry, after line 83.** Before: "the one point on the code path where work stops until the human acts". This is also `CONTEXT.md`'s and `expedition-implementation/SKILL.md`'s wording. After: "the one point before code lands where work stops…" Why it fails: "before code lands" widens the set of points the gate is claimed to be the only one of. It now includes a grilling interview or a relay, which also stop work before any code lands. "On the code path" excluded those.
> 3. **Fifth test, after line 166.** Before: "every agent in flight is still working". After: "every agent you started is still working". Why it fails: take an agent that has finished and whose handover you filed. The before-text leaves the test passing. Read literally, the after-text makes it fail. That contradicts item 5's own condition, "nothing an agent handed back is still unfiled".
> 4. **Clause 8c: a figure of speech.** Instance, after line 167: "puts item 1 or item 3 in reach". "In reach" is a spatial idiom, of the same kind as the ruled-out "in as many words". Form: an idiom or figure of speech in G1 prose that is not a `CONTEXT.md` term. Extent: none. I read by hand and found only this one, but that is not proven exhaustive.
>
> **Borderline passages I did not count as breaches**
> - Line 62–63, 8c: "sends the work back to the feature … back to the build".
> - Line 144, 8d: "Once the check passes you are waiting, and you never wait in place of running the check".
> - Line 195, 8d: "The node's formatting is not the problem."
>
> **Observations, not findings**
> - Line 214 changes "which section each log sits in" to "which section each record goes in". `graph-conventions.md` calls those sections logs ("either log"), so the pointer no longer matches that file's word. The sentence is a pointer, not a binding statement.
> - Lines 89 and 162 are 112 and 110 characters long, where the rest of the file wraps at about 106. No formatter or wrap width is stated anywhere.

### Correction round 1 — the worker's changes for checker run 1

*The worker's own text, pasted. It returned its full handover again. The parts that differ from `## Handover, attempt 1` are pasted here, and the rest is unchanged from that section.*

**What I changed for each finding:**

1. **Cascade entry.** I restored the before-text wording. The entry now reads "…over the graph's edges and over landed code, queueing graph edits rather than interrupting the human." Without "anything", the entry again states no rule about flags, so the prohibition I had added is gone. "Interrupting" stays because it is the before-text's and `CONTEXT.md`'s own word for this idea.
2. **Gate entry.** I restored "the one point on the code path where work stops until the human acts". Grilling interviews and relays are again outside the set of points it covers.
3. **Fifth test.** It now reads "every agent with work under way is still working". An agent that has finished, and whose handover you filed, is no longer caught by it, which matches the before-text's "in flight".
4. **"In reach" (clause 8c).** The sentence now reads "If an agent handed back anything you have not filed, relayed or acted on, item 1 or item 3 applies, so you were never at item 5 at all."

The two observations: I restored "which section each log sits in", so the pointer uses `graph-conventions.md`'s own word for those sections. I re-wrapped the two long lines, the bar entry and the pending-queue sentence. No line in the range now exceeds 106 characters, apart from the frontmatter and the table rows, which are unchanged.

**Did the correction touch anything the acceptance condition names?** Yes. All four fixes touch clause 1, and fix 1 also touches clause 2. Fix 4 touches clause 8c. The restored "log" bears on clause 7: I now read "log" in that sentence as naming the sections `graph-conventions.md` calls logs, not the refused sense of "interview". Every change is inside the rewritten range. The text outside the range is still byte-identical (checked with `diff`), and `git diff --check` is clean.

**Re-pointing search, updated.** I searched the open conditions again for "in flight", "in reach", "under way", "code path", "interrupting", "each log" and "every agent". The only hits are node 118 and node 226. Node 118's "a check in flight" is its own wording. Node 226's "every agent" is about the triggers file, which is a different file. No condition needs a replacement clause and none is proposed for supersession.

**Changed parts of the handover:** size is now 2929 before and 2808 after, 95.9% · "in reach" joins the list of rewritten figures · a new bullet: "Three wordings stay as the before-text had them, because a rewording changed which cases they cover: the gate's "on the code path", the cascade's "rather than interrupting the human", and "which section each log sits in"." · **the third flag of attempt 1 (replacing "log" and "interrupting") is withdrawn**, both words being restored; the two other flags stand as handed back.

**Retrospective, added:** (1) In the correction round, which before-text wordings bind which cases, such as "code path" and "in flight". The checker found these, and my own walk had not. (3) A warning in the condition, or the spawn, that a term's wording in `CONTEXT.md` and in other shipped files, such as "code path" or "interrupting", may be the safe counterpart. Rewording it for plain English can change which cases it covers. (4) `CONTEXT.md` refuses "log" for an interview, and `graph-conventions.md` calls those sections logs. The pointer here has to follow the second, so the two files pull against each other.

### Checker run 2 — `FAIL`, acceptance condition

*The checker's own text, pasted, 2026-09-24.*

> FAIL: acceptance condition
>
> This is run 2, a re-check after the worker's correction. The bar holds.
>
> **What I compared.** I did not rely on the worker's account. I diffed the corrected file against my own copy of the run-1 after-text. The diff shows exactly the six changes the worker describes and nothing else: line 83, the gate entry · lines 89–91, the bar entry, rewrapped with the same words · line 110, the cascade entry · lines 162–165, the pending-queue sentence, rewrapped with the same words · lines 167–168, the fifth test · lines 215–216, "log".
>
> **Checked again in full:** `.claude/skills/expedition/SKILL.md` is still the only changed path, and nothing is untracked · Everything from `## Spawning a worker` to the end is byte-identical to the before-text (`cmp`) · The frontmatter is byte-identical, and the range has no code fences · All 9 headings in the range are identical · `## What is in front of the human, and when` still resolves · No line in the range is longer than 106 characters, apart from the frontmatter and the table rows, which were already that long before the rewrite.
>
> **Run-1 findings, now resolved:** Finding 1, clauses 1 and 2: resolved. The cascade entry again reads "queueing graph edits rather than interrupting the human". That is the before-text's wording, so the added flag prohibition is gone · Finding 2, clause 1: resolved. The gate is "the one point on the code path…", matching the before-text and `CONTEXT.md` · Finding 3, clause 1: resolved. "every agent with work under way is still working" excludes an agent that has finished and been filed. That matches the before-text's "in flight", and it agrees with item 5 · Finding 4, clause 8c: resolved. The new sentence has no figure of speech, and it passes 8e and 8f.
>
> **Clauses that stand, with the words checked again:** 2, 3, 4, 5, 6, 8a, 8b, 8d, 8e, 8f, 10 and 11. Clause 1 also stands for the whole range.
>
> **Clause 9 (reported, not enforced):** `wc -w` of the range is 2929 before and 2808 after, which is 96%. The target is at most 1953, so it was missed.
>
> **The bar:** the repo root still holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. It has no build, tests, formatter or CI, so there is no command to run. The bar is its non-command half, which the implementation-rules file names, and nothing outside the entry below fails it.
>
> **Finding: clause 7, a refused word used for the concept it is refused for.** The correction brought back two words from the before-text. In run 1 I recorded their removal as consistent with clause 7. Clause 7 applies to the after-text whatever the before-text held.
> - Line 110: "queueing graph edits rather than interrupting the human". The `_Avoid_` line under **Raise** refuses "interrupt" for the idea of an agent putting something to the human that stops the work until the human acts. "Interrupting the human" names exactly that act.
> - Line 215: "which section each log sits in". The `_Avoid_` line under **Interview** refuses "log". In `graph-conventions.md` ("The human's words, in either log"), the sections this pointer names are `## Interview` and `## Review`, so "log" here names the interview, among others.
> - Form: a word listed on a `CONTEXT.md` `_Avoid_` line, used in the rewritten range to name the concept that line refuses it for.
> - Extent: an enumerator over the part of the file the worker may edit, `sed -n '1,/^## Spawning a worker/p' .claude/skills/expedition/SKILL.md | grep -n -i -E 'escalat|interrupt|\blog\b|provenance|orchestrator|subagent|reviewer|verifier|auditor|stash|\bWIP\b|snooze|cached|comments|discussion'`. In the corrected file it returns lines 110 and 215 only. The refusals that are ordinary English (report, run, session, index, plan, item, question) cannot be searched for with grep, so I checked them by hand and found none used in the refused sense.
> - Context for whoever settles this: the same words appear in files this work may not touch. `CONTEXT.md`'s own **Cascade** entry reads "rather than interrupting the human", and `graph-conventions.md` calls those two sections "either log". The worker kept the words for that reason, and the worker reads "log" as naming those sections rather than the refused sense. My reading of clause 7 is that it governs the after-text regardless. Wording exists that meets clauses 1 and 7 together: for line 110, "rather than stopping for the human", since a flag does not stop anything · for line 215, naming the sections by their headings, `## Interview` and `## Review`.
> - My run-1 observation about "log" was not a finding. The restoration it prompted is what this finding now reaches.

### Correction round 2 — the worker's changes for checker run 2

*The worker's own text, pasted.*

- **Line 110 (the cascade entry).** "queueing graph edits rather than interrupting the human" now reads "queueing graph edits rather than stopping for the human". The before-text refused to let a cascade stop the work for the human, and the new wording keeps that. It still does not forbid a flag, because a flag stops nothing. So the clause-1 finding from run 1 stays fixed.
- **Line 215 (the pointer to `graph-conventions.md`).** "which section each log sits in" now reads "whether an entry goes under `## Interview` or `## Review`". These are the two sections that `graph-conventions.md` ("The human's words, in either log") says hold the human's words. The pointer now names them by heading and uses no refused word.

**Did the correction touch anything the acceptance condition names?** Yes. It touches clause 7 (refused words), and clause 1 through the two statements' counterparts. Both edits are inside the rewritten range.

**Checks after the change:** The checker's own extent grep now returns nothing · Everything from `## Spawning a worker` onwards is still byte-identical to the before-text · `git diff --check` is clean · No prose line in the range is longer than 106 characters. The frontmatter and the table rows are unchanged.

**Re-pointing search for the new wording.** I searched the open acceptance conditions for "stopping for", "## Interview", "## Review" and "entry goes": Node 120 names `## Interview` and node 49 names `## Review`. Both mean sections of `graph-conventions.md` and the node files, not text in this range. "stopping for" and "entry goes" have no hits. No condition needs a replacement, and none is proposed for supersession.

**Changed parts of the handover:** size 2929 before, 2813 after, 96.0% · *What was built*: one wording stays as the before-text had it, the gate's "on the code path"; the cascade's "rather than interrupting the human" became "rather than stopping for the human", and "which section each log sits in" became "whether an entry goes under `## Interview` or `## Review`" · INDEX LINE, FLAGS, NEW NODES and INVALIDATIONS unchanged.

**Retrospective, changed:** (3) Add this: the condition or the spawn could say plainly that clause 7 applies to the after-text even where the before-text used the refused word. In round 1 I restored before-text wording as a safe counterpart for clause 1 and so broke clause 7. Running the checker's grep of refused words before handing back would have caught it. (4) Replace the last item with this: `CONTEXT.md` refuses "log" for an interview, yet `graph-conventions.md` heads a section "The human's words, in either log" and uses "log" for `## Interview` and `## Review`. That file will meet the same clause-7 collision when nodes 299 and 300 rewrite it.

### Checker run 3 — `PASS`

*The checker's own text, pasted, 2026-09-24.*

> PASS
>
> This is run 3, a re-check after the correction for run 2. I did not rely on the worker's account. I diffed the corrected file against my own copy of the run-2 after-text. The diff shows exactly the two changes the worker describes, at lines 110 and 215–216, and nothing else.
>
> **What I held the work against:** the acceptance condition and the bar. The standards are the ones named in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md`: the ground rules, the five standing rules for writing, `CONTEXT.md`'s `_Avoid_` lines, `graph-conventions.md` and `/writing-for-agents`. The rules file names no reviewing skill, so I ran none. The changed path is a shipped skill file, not an effort record file, so the rule for record files did not apply.
>
> **Clause by clause:**
> - Clause 1: holds. I walked every paragraph of the range against the before-text in runs 1 and 2, and those results stand. Line 110 now reads "queueing graph edits rather than stopping for the human". That gives the before-text's outcome, "rather than interrupting the human", in every case. A cascade does not stop work for the human, and a flag, which stops nothing, is not forbidden. Line 215 now reads "whether an entry goes under `## Interview` or `## Review`". It still points at the same content in `graph-conventions.md`, which states "`## Interview` and `## Review` are the two sections that hold them". Both headings exist in `graph-conventions.md`. Two statements are covered outside the range: handover's `none` rule is covered under `## What comes back`, and the map's commands record is covered by the bar entry.
> - Clause 2: holds. Neither changed line adds a rule, permission, defined term or refused word.
> - Clause 3: holds. The generalisations decide every case as before and leave no new case decided.
> - Clause 4: the frontmatter is byte-identical, and the range has no code fences.
> - Clause 5: all 9 headings in the range are byte-identical.
> - Clause 6: "every act below" points at the list that follows it, and `## What is in front of the human, and when` exists in this file. The `## Interview` and `## Review` on line 215 are headings in `graph-conventions.md`, which the sentence names, so they are not references inside this file.
> - Clause 7: holds. The run-2 enumerator returns nothing (exit 1). I checked the ordinary-English refusals by hand and found none used in the refused sense. Every `CONTEXT.md` term is spelled as `CONTEXT.md` defines it, "Interview" included, and no new term is coined.
> - Clause 8 (plain English), a to f: holds. The two new phrasings are plain, grammatical, and one idea each. Earlier runs judged three passages borderline and did not count them as breaches, and they are unchanged: "back to the feature / back to the build" · "you never wait in place of running the check" · "The node's formatting is not the problem."
> - Clause 9 (reported, not enforced): `wc -w` of the range is 2929 before and 2813 after, which is 96%. The target is at most 1953, so it was missed. That does not fail the work.
> - Clauses 10 and 11: `.claude/skills/expedition/SKILL.md` is the only changed path, and nothing is untracked. Everything from `## Spawning a worker` to the end of the file is byte-identical to the before-text (`cmp`).
>
> **The bar.** The repo root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. It has no build, tests, formatter or CI, so there is no command to run and nothing printed. The bar's non-command half is met. No line in the range is longer than 106 characters, apart from the frontmatter description and the table rows, which were already that long in the before-text.

### Gate — approve

*The human, 2026-09-24,* `verbatim`: *"approve, we will fix the glossary issuea after, I think we need to rename the file in node 56"*. This takes the manager's recommendation, *"approve 296 now and fix the glossary at node 56"*. No rule change struck. The direction on node 56 is recorded there. Landed as `6745f37`, rebased onto `0d406b7` and fast-forwarded with the sandbox off. The worktree and its branch were removed with the sandbox off.

## Flags

`296.1` **· settled** `ASSUMPTION` — The handover entry's `none` rule was removed as a duplicate. `## What comes back` states the same rule outside the rewritten range, so the rule is kept once in the file. Node 297, which rewrites that section, must keep it.

`296.2` **· settled** `ASSUMPTION` — Item 5's check keeps the before-text's ambiguous grouping of "has something to do, or provably nothing is waiting, and nothing … unfiled". The rewrite did not choose between the two readings, because a rewrite preserves meaning.

### Correction round 3 — the human's answers B and C

*The human's words at node 290's gate, `verbatim`: "A ok B like the pilot C you can update", passed to the worker after checker run 3 passed. The worker's own text, pasted.*

**B: names G1 defined that `CONTEXT.md` does not define.** Everything else G1 defines is a `CONTEXT.md` term. G1 also only refers to "pending queue", "pick report" and "gate payload", which are defined outside the range. I found six names and changed each:

1. **`spawn`** (a Words entry). I removed the entry. G1's own noun uses now say it in plain words: "spawning needs its node found first" and "spawning late delays parallel work". The verb "spawn" stays as ordinary English. The definition's counterpart is outside the range, unchanged, under `## Spawning a worker`: "A spawn is a dispatch rather than a briefing. It carries: …" The noun "a spawn" is still used outside G1: "Keep a spawn focused", `### Two things that travel in a spawn…`, "what the spawn conveys", open question 9. Nodes 297 and 298 hold those, and they apply B there.
2. **`marker`** (a Words entry). I removed the entry and moved its two halves into plain words. The word "marker" stays only as an ordinary noun. The flag half is now in the `flag` entry: "It carries a marker, one word saying which kind of judgement it was." The recorded-answer half is now in `### The human's words`: "That mark says the answer is the human's own words rather than your rendering of them. You never render a reply, so the mark never depends on your judgement." The pointer to `graph-conventions.md` now reads "the two marks a recorded answer can carry" in place of "the two markers". No text outside G1 uses "marker".
3. **`kind`** (bold, and defined inside the `node` entry). I removed the bold, so it is no longer a label. The sentence stays as plain words: "Its kind names what its worker does, and there are five kinds."
4. **"*Something to do*"** (an italic label defined in the Item 5 section). It now reads "The human has something to do only when there is something they must act on: …"
5. **"*Provably nothing*" / "the *provably nothing* list"**. These now read: "Checking that nothing is waiting means running a list, and you can say which parts of it you checked." · "…so the list is closed and you can prove that nothing is waiting." · "run the list of what may be waiting".
6. **"The fifth test"**. It now reads "The last check sits outside the pending queue: …" and "The last check looks at what has come back, and never at whether each agent is alive." The number of checks is still readable from item 5, which names the four queue members plus the unfiled test.

**C: passages kept word for word only for a quoting condition.** I checked all of them and changed none, because each is already plain English: the `attempt` entry, quoted by node 120 and also kept for node 258's contradiction, which a rewrite preserves in meaning · the table's first cells, which node 278 depends on · the `## Writing the graph` sentence node 287 names. The headings are kept for clause 5 of the condition, not for a quoting condition.

**Did this touch anything the acceptance condition names?** Clause 1 and clause 8: removing two defined terms, `spawn` and `marker`, meets clause 1's list, which includes "every term the text defines, and its definition". I moved each definition's content to a counterpart, as listed above. But a strict reading of clause 1 still counts a dropped defined term as lost. **The checker's spawn needs the human's answer B, or the condition amended to match it.** Otherwise the checker's walk will report both terms under clause 1. Clause 8b: unbolding `kind` bears on it. Clause 6: no in-file reference is broken. Checks after the change: text outside G1 is byte-identical · the number of `## ` headings is still 15 · `git diff --check` is clean · no G1 prose line is longer than 106 characters · the checker's refused-word grep returns nothing.

**Re-pointing search for the changed wording.** I searched open conditions for "spawn —", "**spawn**", "marker", "provably nothing", "something to do", "fifth test", "**kind**", "last check" and "two marks". Nodes 41 and 49 match "marker", but they mean flag markers in `graph-conventions.md`, the worker contracts and the record, not G1. Nothing else matches. No condition needs a replacement and none is proposed for supersession.

**Handover parts that differ:** size 2929 before, 2799 after, 95.6% · generalisations 5 and 6 added (the `spawn` entry's counterpart under `## Spawning a worker`; the `marker` entry split into the `flag` entry and `### The human's words`) · search handles as above · INDEX LINE, NEW NODES and INVALIDATIONS unchanged · a new flag, filed as `296.3`.

**Retrospective, added to (3):** answer B conflicts with clause 1's "every term the text defines, and its definition". If the answer had arrived with the amended clause text, this round would not need the checker to be told about B separately.

*The manager's note:* the checker is re-run against the condition as written, and is not handed the human's answer B. The pilot's checker already read clause 1 as met where a dropped name's meaning was kept in plain words. If this checker reads it the other way, the conflict between B and clause 1 goes to the human as a question about the condition.

~~`296.3` `ASSUMPTION`~~ **· settled** *withdrawn by the worker at correction round 5, amended clause 1a covering it* — Under the human's answer B, I removed the manager contract's Words entries `spawn` and `marker` and moved their content into plain statements. Clause 1 of node 296's condition, read strictly, counts a dropped defined term as lost, so the checker needs B, or an amended clause, to pass this. The noun "a spawn" is still used outside G1, for nodes 297 and 298 to handle.

### Checker run 4 — `FAIL`, acceptance condition

*The checker's own text, pasted, 2026-09-24.*

> FAIL: acceptance condition
>
> This is run 4, a re-check after the worker changed the work again following my run-3 PASS. The bar holds.
>
> **What I compared.** I did not rely on the worker's account. I diffed the file against my own copy of the run-3 after-text. The diff shows exactly the six changes the worker describes and nothing else: `**kind**` is unbolded · The `spawn` and `marker` entries are gone from `## Words used exactly` · The flag entry gains its marker sentence · The item-5 paragraphs are reworded · `### The human's words` gains its mark sentence · The pointer to `graph-conventions.md` is reworded.
>
> **Checked again in full:** `.claude/skills/expedition/SKILL.md` is still the only changed path, and nothing is untracked · Everything from `## Spawning a worker` to the end is byte-identical to the before-text (`cmp`) · The frontmatter is byte-identical, and the range has no code fences · All 9 headings in the range are byte-identical · The refused-word enumerator from run 2 returns nothing · The range has 36 bold spans, and each is a term at its definition · No sentence has more than one dash aside or more than one semicolon · No line is longer than 106 characters, apart from the frontmatter and the table rows, which were already that long in the before-text.
>
> **Parts that hold (clause 1 and clause 8b):** `spawn`: the removed definition, "the dispatch that starts a worker, and everything it carries", has a counterpart in the unchanged part of the file under `## Spawning a worker`: "A spawn is a dispatch rather than a briefing. It carries: …" · `marker`, flag half: the counterpart is the flag entry, "It carries a marker, one word saying which kind of judgement it was". No line in the unchanged part of the file uses "marker", so no use is left without a definition · `marker`, recorded-answer half: the counterpart is "That mark says the answer is the human's own words rather than your rendering of them". Read together with "You never render a reply", I judge that this gives the before-text's outcome · `kind`: it is still defined in the node entry, "Its kind names what its worker does". Removing the bold is allowed under 8b · *Something to do*: the counterpart is "The human has something to do only when there is something they must act on: a question of theirs still unanswered, or one you send as you stop." I read the colon list as saying what counts, so both directions of the before-text's "means" survive · *Provably nothing*: the counterparts are "Checking that nothing is waiting means running a list…", "you can prove that nothing is waiting" and "run the list of what may be waiting". Item 5 still says "provably nothing is waiting", which connects them · "spawning needs its node found first" and "spawning late delays parallel work" give the before-text's outcome.
>
> **Clause 9 (reported, not enforced):** `wc -w` of the range is 2929 before and 2799 after, which is 96%. The target is at most 1953, so it was missed.
>
> **The bar:** the repo root still holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. It has no build, tests, formatter or CI, so there is no command to run. The non-command half is met apart from the entries below.
>
> **Findings**
>
> 1. **Clause 6, a reference inside the file that does not pick out what it means. This also affects clause 1.** Line 164: "The last check sits outside the pending queue: every agent with work under way is still working." Line 166: "The last check looks at what has come back, and never at whether each agent is alive." Why it fails: this range uses "check" for item 5 as a whole: "run a check", "The check passes when…", "only a check at the end of the order catches it", and the heading "the check you stop on". Read that way, "the last check" is item 5 itself, the check at the end of the order, and line 164 then says item 5 sits outside the pending queue. That contradicts "The four things item 5 names are the whole membership of the pending queue". The before-text's "the fifth test" picked out one thing: the test that follows the four named things, "nothing an agent handed back is still unfiled". The after-text holds nothing unambiguously called "the last check". Form: a phrase in G1 that refers to a part of item 5's check and, given how "check" is used elsewhere in the range, can resolve to more than one thing the after-text holds. Extent: `sed -n '1,/^## Spawning a worker/p' .claude/skills/expedition/SKILL.md | grep -n -i 'last check'` returns lines 164 and 166. A fix that keeps clause 1 would name the test by what it checks, for example "The test that nothing an agent handed back is still unfiled sits outside the pending queue".
> 2. **Clause 2, a closed count that the before-text does not state and that the same section contradicts.** Line 213: "the two marks a recorded answer can carry". Why it fails: line 210 of the same section tells you to "mark it a divergence" for a recorded answer. `graph-conventions.md` says "Every recorded answer carries one of two markers, `verbatim` or `paraphrase`", and that an answer contradicting the recommendation "is additionally marked `DIVERGENCE`". So a recorded answer can carry a third mark. The before-text said "the two markers", matching `graph-conventions.md`'s "one of two markers". It did not say that these are all the marks a recorded answer can carry. Form: a sentence in G1 that states how many marks a recorded answer can carry. Extent: `sed -n '1,/^## Spawning a worker/p' .claude/skills/expedition/SKILL.md | grep -n -i -E '\b(two|three) marks?\b'` returns line 213 only. A fix: "the two marks `verbatim` and `paraphrase`", or the before-text's "the two markers".
>
> **Observation, not a finding:** the flag entry's "which kind of judgement it was" leaves "it" meaning either the flag or the judgement. Both readings give the same meaning, so I did not count it under 8e.

### Correction round 4 — the worker's changes for checker run 4

*The worker's own text, pasted.*

1. **Finding 1 (clause 6, "the last check").** The paragraph now names the test by what it checks, and "the last check" no longer appears: "The test that nothing an agent handed back is still unfiled sits outside the pending queue. It looks at what has come back, and never at whether each agent is alive. It passes when every agent with work under way is still working. If an agent handed back anything you have not filed, relayed or acted on, item 1 or item 3 applies, so you were never at item 5 at all." I moved the "looks at what has come back" sentence up to second place, so that each "It" refers back to the sentence just before it. This fixes the reading in which item 5 itself sat outside the pending queue.
2. **Finding 2 (clause 2, "the two marks a recorded answer can carry").** It now reads "the two marks `verbatim` and `paraphrase`". These are the two that `graph-conventions.md` names. The count no longer excludes `DIVERGENCE`, and I added no closed count.
3. **Observation (the flag entry's "it").** It now reads "one word saying which kind of judgement the flag records", so the sentence has only one possible referent.

**Did this touch what the condition names?** Yes: clauses 6 and 1 (finding 1); clause 2 (finding 2); clause 8e (the observation). All three edits are inside G1. Text outside G1 is byte-identical to the before-text. `git diff --check` is clean. No G1 prose line is longer than 106 characters, apart from the frontmatter, which is unchanged.

**Re-pointing search for the new wording.** I searched the open conditions for "test that nothing", "unfiled", "paraphrase" and "two marks". The only hit is node 80, where "paraphrased" is about moving map text and has nothing to do with G1. No condition needs a replacement, and none is proposed for supersession.

**Handover parts that differ:** size 2929 before, 2807 after (95.8%) · "the fifth test" is now "The test that nothing an agent handed back is still unfiled" · the pointer names "the two marks `verbatim` and `paraphrase`" · the flag half of the `marker` split reads "It carries a marker, one word saying which kind of judgement the flag records." · FLAGS, INDEX LINE, NEW NODES and INVALIDATIONS unchanged.

**Retrospective, added to (4):** the range uses "check" for item 5 as a whole, and for the tests inside it too. Any label for one of those tests has to name what the test checks, or it will be read as item 5 itself.

### Checker run 5 — `PASS`

*The checker's own text, pasted, 2026-09-24.*

> PASS
>
> This is run 5, a re-check after the correction for run 4.
>
> **What I compared.** I did not rely on the worker's account. I diffed the file against my own copy of the run-4 after-text. The diff shows exactly the three changes the worker describes and nothing else: the flag entry, lines 95–96 · the fifth-test paragraph, lines 165–168 · the pointer to `graph-conventions.md`, lines 214–215.
>
> **Checked again in full:** `.claude/skills/expedition/SKILL.md` is still the only changed path, and nothing is untracked · Everything from `## Spawning a worker` to the end is byte-identical to the before-text (`cmp`) · The frontmatter is byte-identical, and the range has no code fences · All 9 headings in the range are byte-identical · No sentence has more than one dash aside or more than one semicolon · No line is longer than 106 characters, apart from the frontmatter and the table rows, which were already that long in the before-text.
>
> **Clause by clause:**
> - Clause 1: holds. The fifth test: "The test that nothing an agent handed back is still unfiled sits outside the pending queue. It looks at what has come back, and never at whether each agent is alive. It passes when every agent with work under way is still working." This gives the before-text's outcome in every case: "The fifth test stands outside that queue — every agent in flight is still working … What you check there is what has come back, never whether each agent is alive." An agent that has finished and been filed has no work under way, so the test still passes for it, as before. The flag entry: "one word saying which kind of judgement the flag records" is the counterpart of the before-text's "on a flag, which kind of judgement it was". The paragraph-by-paragraph walk from runs 1 to 4 stands for everything else. That includes the counterparts for `spawn`, `marker`, *something to do* and *provably nothing* that I established in run 4.
> - Clause 2: holds. "the two marks `verbatim` and `paraphrase`" names two marks. It no longer states how many marks a recorded answer can carry, so it does not contradict "mark it a divergence" on line 211 or `graph-conventions.md`'s "additionally marked `DIVERGENCE`". It matches `graph-conventions.md`'s "one of two markers, `verbatim` or `paraphrase`". The other two changes add no rule.
> - Clause 3: holds, unchanged from earlier runs.
> - Clause 4: holds, as above.
> - Clause 5: holds, as above.
> - Clause 6: holds. "the last check" no longer appears (the grep returns nothing). The new paragraph names the test by what it checks, which picks out the one test the after-text holds. "The pending queue" and `## What is in front of the human, and when` still resolve.
> - Clause 7: holds. The run-2 refused-word enumerator returns nothing. I checked the ordinary-English refusals by hand, and none is used in the refused sense. No new term is coined.
> - Clause 8 (plain English), a to f: holds. In the new paragraph, each "It" refers to "The test that nothing an agent handed back is still unfiled", which is the subject of the paragraph's first sentence and of each sentence in between. The flag entry now names "the flag", so the run-4 ambiguity is gone. The three passages I judged borderline in earlier runs are unchanged and not counted.
> - Clause 9 (reported, not enforced): `wc -w` of the range is 2929 before and 2807 after, which is 96%. The target is at most 1953, so it was missed. That does not fail the work.
> - Clauses 10 and 11: hold, as above.
>
> **The bar.** The repo root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. It has no build, tests, formatter or CI, so there is no command to run and nothing printed. The non-command half is met: the ground rules, the five standing rules for writing, `CONTEXT.md`'s `_Avoid_` lines, `graph-conventions.md` and `/writing-for-agents`, all from `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md`. That file names no reviewing skill, so I ran none. The changed path is a shipped skill file, not an effort record file, so the rule for record files did not apply.

## Amendment by the human, 2026-09-24

*The human approved the manager's proposal, `verbatim`: "ok". The proposal and the answer to A that prompted it are recorded on [node 290](290-rewrite-the-research-contract-as-the-pilot.md). The manager drafted the wording below, and the human amended the condition with it. The original clauses above are left as they were. The clauses below take the place of clauses 1 and 2, add clause 1a, and add a sentence to clause 3.*

1. **Lost or changed statements are rule changes.** The binding statements are: every rule, meaning every instruction, permission, prohibition or duty, and whose it is; every condition or exception attached to a rule; every fixed template; every term the text defines, and its definition; every word the text refuses; and the members and stated count of every closed list. A binding statement of the before-text that has no counterpart anywhere in the whole after-text, or whose counterpart changes the outcome for any case, is a rule change. The checker lists every rule change it finds, each with the before-text statement and its after-text counterpart, or "removed". A rule change does not fail the work.
1a. **Terms `CONTEXT.md` does not define.** A term the before-text defines that `CONTEXT.md` does not define may be dropped as a term, where its meaning is still stated in plain words at the place it was defined. Dropping a term that way is not a rule change.
2. **Added statements are rule changes.** A rule, permission, duty, exception, defined term or refused word that the after-text states and the before-text does not is a rule change. The checker lists it the same way as under clause 1. It does not fail the work.
3. *(added sentence)* A generalisation that changes an outcome, or decides a case the before-text left undecided, is a rule change under clause 1 or clause 2.

### Correction round 5 — the human's answer A and the amended condition

*The human's words, `verbatim`: "A. we can do 2 if it make sense in the file", and the amendment filed at the end of this node, passed to the worker after checker run 5. The worker's own text, pasted.*

#### What I changed, route by route

**Route 1: point the term list at `CONTEXT.md`. Taken.** `## Words used exactly` no longer restates definitions. It opens: "Every term in this contract means what the glossary, `CONTEXT.md`, defines it to mean. The statements below add what those terms demand of you in particular." Seven short statements follow. They keep the parts of the old entries that are duties of the manager and have no other home, in this file or in `CONTEXT.md`: you own and write the graph's files · you own the map, which is the only home of the ground rules and the standing steering, and which holds the bar-commands record, confirmed against the repo · a worker is resumed in place rather than replaced · a handover has five parts, plus a sixth (the gate payload) for an implementation worker · every node that put something to the human carries an interview, implementation nodes included · a flag carries a marker · a sweep runs only on an empty frontier. The opening's read instruction now reads "Read it and the glossary, `CONTEXT.md`, before you touch an effort's files." Why this makes sense in the file: 30-odd of the entries were copies of `CONTEXT.md` terms · At least three copies had already drifted from the glossary: `grilling`, `relay` and `implementation` · `graph-conventions.md`, beside this file, already says "Terms are used exactly as the glossary (`CONTEXT.md`) defines them." The heading `## Words used exactly` keeps its exact text (clause 5) and is still the first `## ` heading (node 111).

**Route 3: fold item 5's section into item 5. Taken.** I removed `### Item 5, the check you stop on`. No other file and no open condition cites that heading. Its binding content is now three sub-bullets under item 5: what "something to do" means, what "nothing is waiting" means, and the test that nothing is unfiled. One paragraph after the list keeps the last-line duty. The intro now says the order runs in one turn and that taking a higher item leaves every lower one owed. The explanation of how the order gets broken is removed. Why this makes sense in the file: the section restated item 5's own terms and explained them. Folding it puts the check in one place, which is also the shape the triggers file copies.

**Route 2: drop the `## What is never yours` table. Not taken.** It does not make sense in this file, for four reasons: Clause 5 requires the heading `## What is never yours` to keep its exact text, because `.claude/skills/expedition-stop/SKILL.md` cites it · The stop skill names that section as one of the three that "govern how they travel and what an answer does" · Three rows have no other statement in the file: answering on the human's behalf, where "where it wrote none, say so to the human" applies to an agent-minted condition; the disagreement between a worker and its checker going to the human; and closing an effort. The closing row is partly covered elsewhere · Node 278 exists to repair one of its rows.

**Size.** Measured with `wc -w` over G1 (lines 1–237 before, frontmatter included): 2929 before, 1601 after, which is 54.7% and inside the two-thirds target. Text outside G1 is byte-identical to the before-text. There are still 15 `## ` headings. `git diff --check` is clean. The refused-word grep returns nothing.

**Did the correction touch what the condition names?** Yes: amended clauses 1 and 2 (rule changes, listed below) · clause 1a (terms `CONTEXT.md` does not define) · clause 3 (generalisation) · clause 5 (headings: all kept except `### Item 5, the check you stop on`, which no listed file cites) · clause 6 (in-file references: "item 5's check" and the `## What is in front of the human, and when` pointer both resolve) · clause 8.

#### RULE CHANGES

**Route 1: the definitions now come from `CONTEXT.md`. Each item is before-text → after-text, then why.**

1. **The term list.** Before: 36 entries defined in this file. After: "Every term in this contract means what the glossary, `CONTEXT.md`, defines it to mean", plus the seven statements above. Why: this removes the duplicate copy that had drifted, and `graph-conventions.md` already says the same.
2. **grilling.** Before: "reached by interviewing them one question at a time". After: `CONTEXT.md`'s "reached by interviewing them. Its worker may put several of its questions in one payload…". Why: node 117 adopted batching inside a node, so the contract's copy was stale. The out-of-range "Exactly one question is in front of the human" is node 127's to change.
3. **relay.** Before: "carrying a worker's question to the human and the answer back". After: `CONTEXT.md`'s "questions … One payload holds one of that worker's questions or several of them … it never carries a second worker's". Why: the same as item 2.
4. **implementation.** Before: "and the node ends at a gate". After: `CONTEXT.md`'s "Its gate is the last point at which the human can act on it, and is neither where the node ends nor where it resolves: after approval the manager commits the work and lands it, and the node resolves after that." Why: node 242 settled this. It also makes my earlier NEW NODE unnecessary, so I withdraw that node below.
5. **attempt.** Before: "the replacement is a new attempt recorded after it". After: `CONTEXT.md`'s "the replacement is a new attempt"; "recorded after it" is removed. Why: this comes with pointing. The contradiction node 258 reports is still there: the kept statement "A worker is resumed in place rather than replaced" against `CONTEXT.md`'s "a dead worker is replaced".
6. **checker.** Before: "checks a finished implementation". After: `CONTEXT.md`'s "checks a landed implementation … before the human sees it". `CONTEXT.md`'s "landed" is wrong, because the checker runs before landing; see NEW NODES. · Before: "an unmet condition sends the work back to the feature, an unmet bar back to the build". After: removed. Why: the gate section sends every finding back to the worker whichever half was unmet, so no manager act turns on this. · Added from `CONTEXT.md`: "not a second opinion", and "its characteristic case is an acceptance condition that is incoherent or unmeasurable, which it alone ever reads cold".
7. **effort.** Before: "Its files live together in one directory". After: `CONTEXT.md`'s "Its files live in `.scratch/<effort>/`". Why: this is the workflow's own path convention, not the host repo's.
8. **raise (added from `CONTEXT.md`).** The three triggers for a worker's unscheduled raise: the thing is not the worker's to change, the decision changes a lot, or it is too hard to decide alone · "Below that line it decides and leaves a flag instead." · "A blocking raise holds the code slot while it waits, it pre-empts grilling work in the manager's queue, and its answer either continues that worker or stops it." · The refused word *ask*. · Why: all of this is consistent with the tier order outside G1.
9. **acceptance condition (added from `CONTEXT.md`).** "written by the node that spawned it"; "a condition it judges wrong is a raise rather than a flag of its own"; "the `CONDITION-WRONG` flag is the manager's to file, and only where the human's answer to that raise was to carry on and ship it anyway". "Self-contained text" keeps its counterpart in `## Acceptance conditions`.
10. **flag (added from `CONTEXT.md`).** "usually a worker's, and the manager's where a judgement of its own reached the graph". This partly answers this file's open question 8 ("May you file a flag about your own conduct…"). Strike it if question 8 should stay fully open. The settlement timing that also comes with it already stands in `## Flags`.
11. **code slot.** Before: "Occupancy is discovered from the state of the work in flight". After: `CONTEXT.md`'s "from the working tree". Nodes 81 and 92 are open on this entry.
12. **close (added from `CONTEXT.md`).** "Most efforts are never closed, and that is a legitimate steady state." This is the frequency claim node 86 rejected. Node 90 is open to remove it from `CONTEXT.md`. Strike it, or accept it pending node 90. See INVALIDATIONS.
13. **sweep.** Before: "the same pass with the bound taken off … A cascade knows what changed; a sweep is looking." After: `CONTEXT.md`'s "The same work as a cascade in the opposite direction: a cascade knows what changed, and a sweep is looking." "It runs only on an empty frontier" is kept as a statement in the Words section.
14. **interview (small).** The base definition becomes `CONTEXT.md`'s "The record of a HITL exchange". The kept statement restores the case of implementation nodes.
15. **map (small, no change of outcome).** "the standing preferences" becomes `CONTEXT.md`'s "the standing notes". "cold" returns through `CONTEXT.md`'s "reads cold once per node".
16. **Refused words (added).** `CONTEXT.md`'s `_Avoid_` lines now reach this contract's vocabulary through the pointer. The file was already held to them under clause 7.
17. **Read instruction (added).** "Read it and the glossary, `CONTEXT.md`, before you touch an effort's files." Why: the terms are now defined there.

**Route 3: item 5 folded.**

18. **Heading.** `### Item 5, the check you stop on` is removed.
19. **Why the order breaks.** Before: "The usual breach is taking a high item and then stopping … Stopping is not an act, so only a check at the end of the order catches it." After: removed. It was explanation. The rule it motivated, taking a lower item later in the same turn, stands in the intro.
20. **The unfiled test.** Before: "It passes when every agent with work under way is still working." After: removed, because it restated the test that nothing handed back is unfiled.
21. **Running the list.** Before: "Before you write that nothing is expected of the human, run the list of what may be waiting. If it finds anything, that is your next act, and the turn does not end." After: "…and run item 5's check before you write that nothing is expected of them." A failed check already sends you to what the order gives.

**Not rule changes, recorded for completeness.** These old entry statements are dropped from the term list, and each keeps a counterpart elsewhere in the file: "yours alone to perform" (resolve): kept in `## Writing the graph` · "You spawn it, never the worker" (checker): kept in `## The checker` · "Only they close one": kept in `## Closing an effort` · the code-slot count as a setting: kept in `### Picking the next node` · "a death never releases one" (claim): kept in `## When an agent dies or is stopped` · "yours alone" and the relay's "answer nothing yourself": kept in `CONTEXT.md` and in "Every agent … reaches the human only through you".

#### Re-pointing search

**Handles searched.** The earlier lists (a)–(d). For this round: "Item 5, the check", "grilling", "one question at a time", "ends at a gate", "recorded after it", "back to the feature", "back to the build", "vocabulary entry", "Words used exactly", "work in flight", "every agent with work", "attempt". The open conditions naming `expedition/SKILL.md` were re-read for anything that depends on an entry of the old term list.

**Replacement clauses.**
- **Node 258, clause 1.** Its target, "the vocabulary entry for `attempt`" in `SKILL.md`, no longer exists. Proposed replacement: "**1.** In `.claude/skills/expedition/SKILL.md`, the `## Words used exactly` section, which today states *"A worker is resumed in place rather than replaced."*, states instead that a dead attempt is resumed where the harness allows and replaced only where it does not, and that a replacement is a new attempt recorded after the one it replaces." Clauses 2 and 3 are unchanged. Clause 2 is now where most of the fix lands, because `SKILL.md` takes its `attempt` definition from `CONTEXT.md`.
- **Node 120, clause 4.** It quotes the `CONTEXT.md` `attempt` entry as "…a new attempt recorded after it." That wording was only `SKILL.md`'s, and this work removes it. Proposed replacement for the quoted sentence: "`CONTEXT.md`: the `attempt` entry reads "A node outlives its attempts: a dead worker is replaced, and the replacement is a new attempt."" The rest of clause 4 is unchanged.

**Checked, no change needed.** 278: the table is untouched · 111: the first `## ` heading is unchanged · 105: "the term `revision` is used in the body of the file" can still be met. The file no longer holds its own `revision` definition · 109: its "self-contained" enumerator still hits `SKILL.md`, in `## Acceptance conditions` · 137: there is one fewer "pick report" in G1, and its enumerator is re-run by design · 304: no hit · 134: about `CONTEXT.md` only · Nothing cites `### Item 5, the check you stop on`. No node is proposed for supersession.

#### Handover parts that differ

*Size:* measured with `wc -w` over G1: 2929 words before, 1601 after (54.7%). This round's cuts are rule changes under the human's answer A (option 2) and the amended condition. Each is listed under RULE CHANGES for the gate. *Deeper cuts:* `## Words used exactly` now points at `CONTEXT.md`, followed by seven statements of the manager's own duties · `### Item 5, the check you stop on` is folded into item 5 · The `## What is never yours` table is kept, for the reasons under Route 2 above.

*INDEX LINE:* The manager contract's opening sections are rewritten in plain English at 55% of their size, the term list pointing at `CONTEXT.md` and item 5's check folded into item 5.

*FLAGS:* the flag on the handover's `none` rule: unchanged · the flag on item 5's grouping: unchanged · the flag on dropping `spawn` and `marker`: withdrawn, because amended clause 1a covers it · new, filed as `296.4`.

*NEW NODES:* **Withdrawn:** "The manager contract's `implementation` entry says the node ends at a gate". The entry no longer exists, and the pointer gives the file `CONTEXT.md`'s corrected definition (rule change 4). **New:** filed as [node 307](307-context-mds-checker-entry-says-the-checker-checks-a-landed-implementation.md).

*INVALIDATIONS:* Node 86 (no claim anywhere about how often efforts end or close). Through the pointer, `CONTEXT.md`'s "Most efforts are never closed" now reaches the manager contract. The repair is open node 90. If the human strikes rule change 12, this invalidation goes away with it.

*GATE PAYLOAD:* runs 1, 2 and 4 as reported earlier; runs 3 and 5 passed · round 3: answers B and C · round 5: this round, Routes 1 and 3; the 21 rule changes are listed under RULE CHANGES · paths touched: `.claude/skills/expedition/SKILL.md` in the worktree, uncommitted · bar: unchanged · proposed commit message: `Rewrite the manager contract's opening sections in plain English` / blank / `Point the term list at CONTEXT.md and fold item 5's check into item 5.` / blank / `Node: graph-workflow/296`.

*RETROSPECTIVE, addition to (4):* pointing the term list at `CONTEXT.md` shows that the glossary itself holds three statements the record has since rejected or corrected: the checker entry's "landed" · the Closed entry's frequency claim (node 90 is open) · the Flag entry's manager-flag clause, against open question 8. A contract that takes its definitions from the glossary inherits each of these defects.

`296.4` **· settled** `ASSUMPTION` — Of the three deeper cuts the human allowed, I kept the `## What is never yours` table. Clause 5 keeps its heading, the stop skill names the section as governing, three rows have no other home in the file, and node 278 repairs one of its rows.

### Checker run 6 — `PASS`, under the amended condition, with a list of rule changes

*The checker's own text, pasted, 2026-09-24.*

> PASS
>
> This is run 6. I checked against the amended condition: the new clauses 1, 1a and 2, the sentence added to clause 3, and the other clauses as before. I re-read the work in full, because the rewritten range is new: 1601 words where run 5 had 2807. I walked clauses 1 and 2 separately and built the rule-change list below myself.
>
> **The bar holds.** The repo root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. There is no build, test suite, formatter or CI, so there is no command to run. The non-command half is met apart from the part named under NOT COVERED. Its standards come from `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md`: the ground rules, the five standing rules for writing, `CONTEXT.md`'s `_Avoid_` lines, `graph-conventions.md`, and `/writing-for-agents`. That file names no reviewing skill, so I ran none. The changed path is a shipped skill file, not a record file.
>
> **Clause by clause**
> - **1 and 2:** walked. Every finding is listed under RULE CHANGES, and none fails the work.
> - **1a:** applied to four before-text terms that `CONTEXT.md` does not define: *Something to do* and *Provably nothing*: each meaning is still stated in plain words in item 5's sub-bullets, which is where they were defined. `marker`: the flag half is in the Words list ("A flag carries a marker…"). The recorded-answer half is in `### The human's words` and in `CONTEXT.md`'s Verbatim / paraphrase entry. `spawn`: its meaning is not restated at the place it was defined, so 1a does not apply. Clause 1 is still met, because the unchanged section under `## Spawning a worker` says "A spawn is a dispatch rather than a briefing. It carries: …" None of these four counts as a rule change.
> - **3:** holds. "Every term in this contract means what the glossary, `CONTEXT.md`, defines it to mean" generalises over about 35 definitions. Where it changes an outcome or decides a new case, I listed that as a rule change under clause 1 or 2, as the added sentence directs.
> - **4:** holds. The frontmatter is byte-identical, and neither the before-text nor the after-text of the range has a code fence.
> - **5:** holds. The heading `### Item 5, the check you stop on` was removed. Its exact text appears in none of the other listed files. I grepped both the worktree and the main checkout; its only hit was the main checkout's own copy of this same file, which clause 5 excludes. The other 8 headings are byte-identical.
> - **6:** holds. These references inside the range resolve: "every act below", "The statements below", "Those four", "item 5's check", and `## What is in front of the human, and when`. The unchanged part's references into the range also resolve, including "the parts above missing", which points at the handover parts still in the Words list.
> - **7:** holds. The run-2 refused-word enumerator returns nothing. I checked the ordinary-English refusals by hand. The range coins no new term.
> - **8:** holds. The range has no bold. No sentence has more than one dash aside or more than one semicolon. Each pronoun has a clear referent, and I found no figure of speech or slogan. The three passages I judged borderline in earlier runs are unchanged and not counted.
> - **9:** `wc -w` of the range is 2929 before and 1601 after, 55%. The target of at most 1953 is met.
> - **10 and 11:** hold. `.claude/skills/expedition/SKILL.md` is the only changed path, and nothing is untracked. Everything from `## Spawning a worker` to the end is byte-identical to the before-text (`cmp`).
>
> RULE CHANGES
>
> Clause 1. A before-text statement in the range, then its counterpart, which now often comes from `CONTEXT.md` through the line-25 import.
> 1. **grilling.** Before: "reached by interviewing them one question at a time". After (`CONTEXT.md` grilling): "reached by interviewing them. Its worker may put several of its questions in one payload, independence being what decides which of them share one." Two independent questions may now go in one payload.
> 2. **implementation.** Before: "and the node ends at a gate". After (`CONTEXT.md` implementation): "Its gate … is neither where the node ends nor where it resolves: after approval the manager commits the work and lands it, and the node resolves after that." The after-text contradicts the before-text.
> 3. **attempt.** Before: "the replacement is a new attempt recorded after it". After (`CONTEXT.md`): "the replacement is a new attempt." The words "recorded after it" are removed.
> 4. **checker, what it checks.** Before: "checks a finished implementation". After (`CONTEXT.md`): "checks a landed implementation … before the human sees it". "Finished" became "landed".
> 5. **checker, where a FAIL sends the work.** Before: "an unmet condition sends the work back to the feature, an unmet bar back to the build". After: removed. It has no counterpart in the range, the unchanged part, or `CONTEXT.md`.
> 6. **code slot.** Before: "Occupancy is discovered from the state of the work in flight rather than recorded". After (`CONTEXT.md`): "Occupancy is discovered from the working tree rather than recorded". The outcome differs for a claimed implementation node whose worker has not yet written to the tree.
> 7. **effort.** Before: "Its files live together in one directory". After (`CONTEXT.md`): "Its files live in `.scratch/<effort>/`". The directory is now fixed. `graph-conventions.md` already states `.scratch/<effort>/`.
>
> Clause 2. Statements the after-text makes that the before-text of the whole file does not.
> 8. Line 21: "Read it and the glossary, `CONTEXT.md`, before you touch an effort's files." This adds a duty to read `CONTEXT.md`.
> 9. Line 25: "Every term in this contract means what the glossary, `CONTEXT.md`, defines it to mean." This makes every `CONTEXT.md` definition binding on this contract. Beyond items 1–7, it brings in these statements the before-text did not make:
>    - a. **relay:** "One payload holds one of that worker's questions or several of them … it never carries a second worker's."
>    - b. **raise:** a worker opens an unscheduled raise when "the thing that is wrong is not the worker's to change, the decision changes a lot, or the choice is genuinely too hard to make alone. Below that line it decides and leaves a flag instead", and "its answer either continues that worker or stops it".
>    - c. **acceptance condition:** "written by the node that spawned it". This conflicts with the unchanged part's "Where **you** minted the node, the condition is yours to write". Also: "the `CONDITION-WRONG` flag is the manager's to file, and only where the human's answer to that raise was to carry on and ship it anyway."
>    - d. **out of scope:** "Both a node status and a section of the map, and it never graduates into fog."
>    - e. **labels:** "A filter and never structure: no order may be inferred from a label, and a label is never a node's identity."
>    - f. **destination:** a new defined term. It "says, in one line, whether the effort is expected to reach it", and "that line is where a manager reads that a non-empty frontier is that effort's steady state". The unchanged part calls a frontier that never empties a steady state with no condition attached.
>    - g. **closing report:** "What the manager hands the human once the frontier empties: what was decided, what landed, and every flag still outstanding". This adds a timing and a "what was decided" item beyond the unchanged part's list for the report that precedes a close.
>    - h. **correction round:** "while the node stays claimed … neither a revision nor a check".
>
> **Extent of this list:** for clause 1, a bounding set: every statement in the before-text range, walked paragraph by paragraph against the after-text range, the unchanged part, and `CONTEXT.md`. For clause 2, a bounding set: the two new sentences in the range, plus every `CONTEXT.md` headword the contract uses, each held against the whole before-text. Terms `CONTEXT.md` defines but this contract never uses are not counted: salvage, code commit, graph commit, manager note. Descriptive additions that state no rule are not counted either, for example map's "no reader reads all of it" and closed's "Most efforts are never closed".

NOT COVERED:
- ESTABLISHED BY the manager · `map.md`'s glossary note, which says the glossary "is **moving** into `.claude/skills/expedition/CONTEXT.md`" under [node 56](56-ship-the-glossary-into-the-skill-set.md); node 56's `Status: open`; and `ls .claude/skills/expedition/`, which holds no `CONTEXT.md`. So today the glossary sits at the repo root and does not ship with the skill files, and `graph-conventions.md` already depends on it the same way. Whether the new dependence is acceptable goes to the human at the gate. — "Ground rule 1 ("Nothing in the shipped files may assume this repo…") as it applies to lines 21 and 25. They make the manager contract depend on a file named `CONTEXT.md` for every term it uses. Whether that file ships with the workflow is outside what I was given. If it does not ship, a repo holding its own, unrelated `CONTEXT.md` would supply this contract's definitions. The shipped `graph-conventions.md` already says "Terms are used exactly as the glossary (`CONTEXT.md`) defines them", so the dependence is not new to the shipped files. This PASS covers the rest of the bar and all of the condition, and not this part."

*The manager's note, matching the two lists:* the checker's clause-1 items 1–7 and clause-2 items 8, 9a, 9b and 9c are on the worker's list (its items 2, 4, 5, 6, 11, 7, 17, 3, 8, 9). The checker's items **9d (out of scope), 9e (labels), 9f (destination), 9g (closing report) and 9h (correction round)** are on no list of the worker's. The worker counted the `CONTEXT.md` pointer as bringing in the definitions it listed. Under the human's approved process, those five go back as a correction.

### Correction round 6 — the five unlisted rule changes and the item-9 conflict

*The worker's own text, pasted.*

**Text change: one sentence added to `## Words used exactly`**, directly after the pointer:
> "Where a section of this contract states a rule about one of those terms, and the rule differs from the glossary, follow the section."

This settles the item-9 conflict, and where findings f and g conflict with the rest of the file, the file's own section now wins. The sentence is itself a rule change, listed as 22 below. Why this, and not narrowing the pointer to a list of the old terms: A pointer that covers every term is how `graph-conventions.md` already points at the glossary · Listing about 34 term names would cost more words than the sentence · A list would not remove the conflict for terms such as `acceptance condition`, which were on the old list anyway.

**d–h: kept, and added to RULE CHANGES.** They come in through the pointer, and each is consistent with how the rest of the file uses the term.

**How the two item-9 statements now stand together:** `CONTEXT.md` says an acceptance condition is "written by the node that spawned it". `## Acceptance conditions` says "Where **you** minted the node, the condition is yours to write." Under the new sentence, the section governs the case of a node the manager minted itself, which has no spawning node. The glossary's wording covers every other case. The glossary's gap is already an open node: node 55 carries the manager-minted case into `CONTEXT.md` and `graph-conventions.md`. Once node 55 lands, the two statements agree without the precedence sentence.

**Terms I checked for the same effect that the checker did not list.** These are glossary terms that the rest of the file uses but that G1's before-text never defined: `approval`, `reject`, `divergence`, `verbatim / paraphrase` and `node trailer` each agree with the file's own statements. No outcome changes. `banked answer` adds "held on a parked node … Paid for once". G1's "stay banked if the attempt dies" uses the word for a dead attempt rather than a parked node. I judge this no change of outcome, because both mean the answer is on disk for the next worker. Listed as 28 for the human to see.

**Did this touch what the condition names?** Yes: amended clause 2 (an added rule: the precedence sentence); amended clause 1 (d–h, and how item 9 stands); clause 8 (the new sentence has one clear referent: "the rule"). Size: 1625 of 2929 words, 55.5%. Text outside G1 is byte-identical to the before-text. `git diff --check` is clean.

**Re-pointing search** for "follow the section", "differs from the glossary" and "node that spawned it": the only hit is node 55. Its condition targets `CONTEXT.md` and `graph-conventions.md`, not G1. No replacement and no supersession is needed.

**RULE CHANGES, added after item 21:**

22. **Precedence (added).** Before: none; the old term list defined every term in the file itself. After: "Where a section of this contract states a rule about one of those terms, and the rule differs from the glossary, follow the section." Why: once the definitions come from `CONTEXT.md`, the file needs a rule for where the glossary and a section differ. The section is the more specific statement of the manager's conduct. It settles item 9 against `## Acceptance conditions` (node 55 is the open repair on the glossary's side), and f and g below.
23. **out of scope (added).** From `CONTEXT.md`: "Both a node status and a section of the map, and it never graduates into fog." Why it makes sense: `### What reject means` rules a node out of scope, and the glossary's statement agrees with that use.
24. **labels (added).** From `CONTEXT.md`: "A filter and never structure: no order may be inferred from a label, and a label is never a node's identity." Why it makes sense: `## Spawning a worker` uses labels only to scope the index of decisions, which is a filter, so the rule agrees with the only use.
25. **destination (added).** From `CONTEXT.md`: it "says, in one line, whether the effort is expected to reach it", and for an effort not expected to reach it "that line is where a manager reads that a non-empty frontier is that effort's steady state rather than a defect". Why it makes sense: node 91 settled that the destination records this expectation. How it stands with `## Closing an effort`'s unconditioned "A frontier that never empties is a legitimate steady state rather than a stalled one": the section's statement still holds for every effort, under rule 22. What the glossary adds is where the manager reads whether that steady state is expected.
26. **closing report (added).** From `CONTEXT.md`: "What the manager hands the human once the frontier empties: what was decided, what landed, and every flag still outstanding." It adds a timing, once the frontier empties. This agrees with the sweep running only on an empty frontier and the report preceding a close. It adds a "what was decided" item beyond the section's list. The section's list is not stated as closed, so this is an added item. Where the two differ, the section's delta scoping ("scoped to what the human has not already seen") governs, under rule 22. Node 137 is open to rename this term.
27. **correction round (added).** From `CONTEXT.md`: "while the node stays claimed. Uncapped, and neither a revision nor a check." Why it makes sense: `### Three outcomes, and no fourth` already says a correction round is uncapped, and the node stays claimed through it. "Neither a revision nor a check" keeps the term apart from two others the file uses.
28. **banked answer (small, no change of outcome).** From `CONTEXT.md`: "held on a parked node and waiting for a fresh worker. Paid for once." G1 also uses "banked" for words kept after an attempt dies. Both mean the answer is on disk for the next worker.

Item 9, amended text: "…added from `CONTEXT.md`: 'written by the node that spawned it' … For a node the manager minted itself, `## Acceptance conditions`' 'the condition is yours to write' governs under rule 22. Node 55 is the open repair to the glossary."

**Other changed parts:** Size: 2929 before, 1625 after (55.5%) · Deeper cuts: the pointer is followed by one precedence sentence: where a section of this contract states a rule that differs from the glossary, the section governs · Gate payload: run 6 passed, and this round adds d–h (23–27), the precedence sentence (22), how item 9 stands, and 28 · Paths touched, bar and commit message unchanged.

**Retrospective, addition to (3):** A pointer to a glossary brings in every term the rest of the file uses, not only the terms the replaced list defined. The walk for such a change has to cover all glossary terms used anywhere in the file. My list was built from the old entries only, which is why d–h were missing from it.

### Checker run 7 — `PASS`, under the amended condition, with a list of rule changes

*The checker's own text, pasted, 2026-09-24.*

> PASS
>
> This is run 7, a re-check after the worker changed the work following run 6. I did not rely on the worker's account. I diffed the file against my own copy of the run-6 after-text. The only change is one sentence added at lines 25–27 of `## Words used exactly`: "Where a section of this contract states a rule about one of those terms, and the rule differs from the glossary, follow the section."
>
> **Checked again in full:** `.claude/skills/expedition/SKILL.md` is still the only changed path, and nothing is untracked · Everything from `## Spawning a worker` to the end is byte-identical to the before-text (`cmp`) · The frontmatter is byte-identical, and the range has no code fences · The headings are as in run 6: `### Item 5, the check you stop on` is removed, which clause 5 allows, and the other 8 are byte-identical · The refused-word enumerator returns nothing · No line is longer than 106 characters, apart from the frontmatter and the table rows, which were already that long in the before-text.
>
> **Clause by clause:** Clauses 1 and 2: walked again with the new sentence in place. The results are in RULE CHANGES below. None of them fails the work · Clause 1a: as in run 6. *Something to do*, *Provably nothing* and `marker` are dropped as terms under 1a, with their meaning still stated where they were defined. `spawn` has its counterpart under `## Spawning a worker`. None is a rule change · Clause 3: holds. Each outcome change that comes from the generalisation is listed as a rule change, as the added sentence directs · Clauses 4, 5, 10 and 11: hold, as above · Clause 6: holds. "those terms" and "a section of this contract" resolve, and the references from run 6 still resolve · Clause 7: holds. The range coins no new term · Clause 8 (plain English): holds for the new sentence. It states a rule as what to do. It has no bold. It uses plain words. "those terms" refers to the terms of the sentence before, which the glossary defines. It holds one idea, with no dash aside and no semicolon · Clause 9: `wc -w` of the range is 2929 before and 1625 after, which is 55%. The target is at most 1953, so it is met.
>
> **The bar.** The repo still has no build, tests, formatter or CI, so there is no command to run. The non-command half is met, except for the part under NOT COVERED. Its standards come from `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md`. That file names no reviewing skill, so I ran none.
>
> RULE CHANGES
>
> The new sentence resolves some run-6 entries, because it makes a rule stated in this contract's sections outrank `CONTEXT.md`. I list only what still stands, and then what it resolved.
>
> Clause 1. For each entry: the before-text statement in the range, then its counterpart.
> 1. **grilling.** Before: "reached by interviewing them one question at a time". After (`CONTEXT.md`): "Its worker may put several of its questions in one payload, independence being what decides which of them share one." No section of the contract states a rule about how a grilling worker batches its questions.
> 2. **implementation.** Before: "and the node ends at a gate". After (`CONTEXT.md`): the gate "is neither where the node ends nor where it resolves". No section says the node ends at the gate. `### Three outcomes, and no fourth` ("approve → you make the commit, and the node resolves") agrees with `CONTEXT.md`, so the section rule does not bring the before-text back.
> 3. **attempt.** Before: "the replacement is a new attempt recorded after it". After: "recorded after it" is removed.
> 4. **checker.** Before: "an unmet condition sends the work back to the feature, an unmet bar back to the build". After: removed.
> 5. **code slot.** Before: "Occupancy is discovered from the state of the work in flight rather than recorded". After (`CONTEXT.md`): "discovered from the working tree". No section states how occupancy is discovered.
> 6. **effort.** Before: "Its files live together in one directory". After (`CONTEXT.md`): "Its files live in `.scratch/<effort>/`". `graph-conventions.md` already states `.scratch/<effort>/`.
>
> Clause 2. For each entry: a statement the after-text makes that the whole before-text does not.
> 7. Line 21: "Read it and the glossary, `CONTEXT.md`, before you touch an effort's files." This is a new duty.
> 8. Line 25: "Every term in this contract means what the glossary, `CONTEXT.md`, defines it to mean." This is a new rule.
> 9. Lines 25–27, new in this run: "Where a section of this contract states a rule about one of those terms, and the rule differs from the glossary, follow the section." This is a new rule that decides which source wins.
> 10. Imported through item 8, where no section states a differing rule: a. **relay:** "One payload holds one of that worker's questions or several of them … it never carries a second worker's." b. **raise:** the three conditions under which a worker opens an unscheduled raise, "Below that line it decides and leaves a flag instead", and "its answer either continues that worker or stops it". c. **acceptance condition:** "the `CONDITION-WRONG` flag is the manager's to file, and only where the human's answer to that raise was to carry on and ship it anyway." d. **out of scope:** "it never graduates into fog." e. **labels:** "no order may be inferred from a label, and a label is never a node's identity." f. **destination:** a new defined term, which "says, in one line, whether the effort is expected to reach it". g. **closing report:** "what was decided", as an item the report carries. The list under `## Closing an effort` does not say it is exhaustive, so this item adds to it rather than differing from it. h. **correction round:** "while the node stays claimed … neither a revision nor a check".
>
> Resolved by the new sentence, and no longer rule changes: **Checker, what it checks** (run-6 item 4, "landed implementation"). The sections say "Raise the gate once the checker passes", and that the work "sits uncommitted" at the gate. So the section rule is that the checker checks unlanded work, and that rule now wins. The before-text's "finished implementation" gives the same outcome · **Acceptance condition, who writes it** ("written by the node that spawned it", part of run-6 item 9c). The section's "Where **you** minted the node, the condition is yours to write" now wins · **Destination and steady state** (part of run-6 item 9f). The section's unconditional "A frontier that never empties is a legitimate steady state" now wins over `CONTEXT.md`'s conditional reading. The defined term and its one-line rule still stand, as item 10f · **Closing report, when it is sent** (part of run-6 item 9g). The section's "The report that precedes a close" now wins over "once the frontier empties". The added item still stands, as item 10g.
>
> **Extent:** a bounding set, the same as run 6. For clause 1, every statement in the before-text range. For clause 2, the new sentences in the range plus every `CONTEXT.md` headword this contract uses. Each was held against the whole before-text, and now also against the unchanged part's section rules under the new precedence sentence. Headwords this contract does not use are not counted, and neither are descriptive statements.

NOT COVERED:
- ESTABLISHED BY the manager · as for run 6: `map.md`'s glossary note, node 56's `Status: open`, and `ls .claude/skills/expedition/`. The glossary does not ship with the skill files until node 56 lands. Whether the dependence is acceptable goes to the human at the gate. — "Ground rule 1 ("Nothing in the shipped files may assume this repo…"), as it applies to lines 21 and 25. This is unchanged from run 6. Those lines make the manager contract take every definition from a file named `CONTEXT.md`. Whether that file ships with the workflow is outside what I was given. If it does not ship, a repo holding its own, unrelated `CONTEXT.md` would supply this contract's definitions. The new precedence sentence narrows the risk to terms no section states a rule about, but it does not remove it. The shipped `graph-conventions.md` already defers to `CONTEXT.md` in the same way. This PASS covers all of the condition and the rest of the bar, but not this part."

*The manager's note, matching the two lists:* every item on the checker's run-7 list is on the worker's list (its items 1–17 and 22–28).

## Answer

The manager contract's opening sections are rewritten in plain English at 55% of their size, the term list pointing at `CONTEXT.md` and item 5's check folded into item 5.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`, as changed by correction rounds 1 to 6. The human approved every listed rule change, and the checker's independent list is under `### Checker run 7`. The work landed as commit `6745f37`.
