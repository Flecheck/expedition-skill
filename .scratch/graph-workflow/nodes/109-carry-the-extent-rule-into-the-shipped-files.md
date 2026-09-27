# Carry node 94's extent rule into the seven shipped files that state what a condition must be

Type: implementation
Status: resolved
Blocked by: [95](95-carry-the-widening-rule-into-the-shipped-files.md), [103](103-carry-the-pick-report-settling-moment.md)

## Question

*Surfaced by [Whether a condition's scope stops being a list of files](94-condition-scope-as-a-predicate.md)'s
worker, and pasted as it wrote it.*

> Make every shipped file that states what an acceptance condition must carry state the extent rule, so that no file
> still presents self-containment as the whole of what a condition owes its reader.

**Blockers, in the worker's words:** *"[node 95](95-carry-the-widening-rule-into-the-shipped-files.md), which edits
the same two sections of the same two files and whose own scope this node's `INVALIDATIONS` reports as short; and
[node 103](103-carry-the-pick-report-settling-moment.md), which edits `expedition/SKILL.md`. Claiming this before
both land would put three workers in one file."*

## Acceptance condition

*Written by node 94's worker. Pasted as it wrote it, and not the manager's. It is the first condition on this graph
written under its own node's rule, and it carries its enumerator accordingly.*

> **Scope, and the search that produced it.** The seven files below are edited and no other file is.
>
> `.claude/skills/expedition/graph-conventions.md`, `.claude/skills/expedition/SKILL.md`, and the five worker
> contracts `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`,
> `.claude/skills/expedition-precondition/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`,
> `.claude/skills/expedition-research/SKILL.md`.
>
> **The enumerator, so the scope is measured rather than asserted.**
> `grep -rln "self-contained" --include="*.md" .claude/ CONTEXT.md` returns exactly those seven paths and nothing
> else, `CONTEXT.md` among the searched files and not among the hits. Each of the five worker contracts additionally
> contains the phrase *"against those four"*, confirmed by `grep -rln "against those four" --include="*.md" .claude/`
> returning those five paths and no others. **Where the work turns up a statement of what an acceptance condition
> must carry in some other file, it is reported and not edited** — reporting it is the whole of what this condition
> asks for it.
>
> **1. The rule to state, copied here in full rather than pointed at.** Where an acceptance condition's scope was
> derived from a search, that search is stated in the condition. The list of files stays and so does the exclusion
> clause; the search is written beside the list as the thing that produced it and never in place of it. The
> condition's author owes exactly one of three, and a condition addressing a defect with instances that carries none
> of the three is **malformed**:
>   1. an **enumerator** — the command, and what it returned when run;
>   2. a **bounding set**, where no command fits — the smallest set that provably contains every instance, together
>      with how that set was computed;
>   3. an explicit statement that **the scope came from no search** — the work creates a file, or the named places
>      are the work rather than instances of a defect.
>
> **2. The enumerator's domain is the working tree and never the effort's record.** The files state this as a limit
> on rung 1: a search over the effort's own node files or its indexes is the quantification a condition may not make,
> and no copy repairs it.
>
> **3. The residual clause, stated as a duty of the worker.** An instance the search reaches outside the condition's
> list is **reported and not edited**. A worker whose search matches somewhere unlisted gains a duty to report and
> never a permission to edit, and a false positive costs one line in a handover.
>
> **4. The reason travels with the rule, in each document's own voice.** A condition's scope is a finding stated in
> advance, and its readers — the blind checker, and the worker before it — cannot go and look, which is why they are
> owed the same extent statement a checker's finding already owes. Stated as what the rule protects and not as why it
> was chosen.
>
> **5. `graph-conventions.md`'s `### Acceptance condition` and `SKILL.md`'s `## Acceptance conditions`** each carry
> clauses 1 through 4. In `SKILL.md` they are stated as the manager's duties: it files a condition carrying none of
> the three rungs as malformed rather than claiming the node on it, and where a condition records its enumerator,
> re-deriving the scope is running that recorded command rather than reconstructing one.
>
> **6. Each of the five worker contracts' section on reporting an implementation node** gains the extent statement as
> a fifth thing its author owes, beside the self-containment bullets already there, and gains the residual clause as
> a duty the reporting worker writes into the condition it writes. **The read-back sentence's count is corrected**:
> each contract today says the author reads what it wrote back *"against those four"*, and after this change the
> stated count matches the number of properties that section actually lists.
>
> **7. Nothing already in these files is removed, renumbered, or changed in meaning** beyond what clauses 1 to 6
> name. In particular the self-containment rule, the ban on a demand held elsewhere, the path permit, the bar's
> exemption from the copy rule, and the prohibition on the manager authoring a condition for an agent-minted node all
> stand exactly as they stand today.
>
> **8. `CONTEXT.md` is changed only if a term genuinely moves**, and where one does, it is reported in the handover
> rather than assumed to travel. No file under `.scratch/` is changed.
>
> **9. The bar.** The standing bar applies: the tree builds, warns about nothing, is formatted, and passes the tests
> relevant to the change. This repository has no build, no tests and no formatter, which is a complete bar on its
> remaining half rather than a deficient one — so what remains is `/coding-principles`, `/naming`, and each file's
> own form: it addresses its reader as *you*, states rules rather than explaining them, and a new rule joins an
> existing section rather than sitting beside it.

## Amendment, 2026-09-24

*Written by [node 290](290-rewrite-the-research-contract-as-the-pilot.md)'s worker and filed by the manager, after that node's work landed as commit `4068519`. Every word of each replacement is fixed by that commit: it quotes the research contract's after-text. The minting author's condition above is left as it was, and these replacements take the place of the clauses they name.*

Node 290's worker searched every open node's `## Acceptance condition` for quoted spans of the research contract's before-text, for mentions of the file, and for each piece of wording its rewrite removed or replaced. The full list of handles is on node 290 under `### Re-pointing duty` and `### Correction round 1`.

- **The enumerator paragraph.** Replace it with: "Each of the five worker contracts additionally contains the read-back sentence, which reads *"against those four"* in a contract not yet rewritten and *"against the four points above"* in `.claude/skills/expedition-research/SKILL.md`. It is confirmed by `grep -rlnE "against (those four|the four points above)" --include="*.md" .claude/` returning those five paths and no others."
- **Clause 6.** Replace "each contract today says the author reads what it wrote back *"against those four"*" with "each contract's read-back sentence (*"against those four"*, or in the research contract *"check what you wrote against the four points above"*)". The rest of the clause is unchanged. After nodes 291 to 294 land, only the second form remains.

## Flags

`109.1` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 290](290-rewrite-the-research-contract-as-the-pilot.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `4068519`.

## Amendment, 2026-09-25 (from node 294)

*Written by [node 294](294-rewrite-the-implementation-contract.md)'s worker and filed by the manager, after that node's work landed as commit `724c361`. Every word of the replacement is fixed by that commit: it quotes `expedition-implementation/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 294's worker's search is on node 294 under `RE-POINTING SEARCH`.*

- **The enumerator paragraph**, as amended by node 290. Replace "and *"against the four points above"* in `.claude/skills/expedition-research/SKILL.md`" with "and *"against the four points above"* in `.claude/skills/expedition-research/SKILL.md` and `.claude/skills/expedition-implementation/SKILL.md`".
- **Clause 6**, as amended by node 290. Replace "or in the research contract" with "or in the research and implementation contracts". The rest is unchanged.

`109.2` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 294](294-rewrite-the-implementation-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `724c361`.

## Amendment, 2026-09-25 (from node 291)

*Written by [node 291](291-rewrite-the-grilling-contract.md)'s worker and filed by the manager, after that node's work landed as commit `0a3e68b`. Every word of the replacement is fixed by that commit: it quotes `expedition-grilling/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 291's worker's search is on node 291 under `RE-POINTING SEARCH`.*

- **The enumerator paragraph**, as amended by nodes 290 and 294. Replace "in `.claude/skills/expedition-research/SKILL.md` and `.claude/skills/expedition-implementation/SKILL.md`" with "in `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md` and `.claude/skills/expedition-grilling/SKILL.md`".
- **Clause 6**, as amended by node 294. Replace "or in the research and implementation contracts" with "or in the research, implementation and grilling contracts". The rest is unchanged.

`109.3` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 291](291-rewrite-the-grilling-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `0a3e68b`.

## Amendment by the human, 2026-09-25

*The manager's question, carrying node 312's worker's recommendation from node 312's `RE-POINTING SEARCH:`:* "Do you agree to amend node 109's clause 5 this way, or keep it as written?" The way proposed: `graph-conventions.md`'s `### Acceptance condition` states the rule itself (clauses 1 to 4), and the manager contract's `## Acceptance conditions` states only the manager's duties under it, pointing at `graph-conventions.md` in one sentence. The reason given: clause 5 as written would re-create a rule stated in both files, which the split the human approved at node 312 rules out.

The human, `verbatim`: *"I agree"*

*The manager drafted the wording below, and the human amended the condition with it. The condition above and its earlier amendments are left as they were. The clause below takes the place of clause 5.*

5. **`graph-conventions.md`'s `### Acceptance condition` carries clauses 1 through 4.** `SKILL.md`'s `## Acceptance conditions` states the manager's duties under that rule: it files a condition carrying none of the three rungs as malformed rather than claiming the node on it, and where a condition records its enumerator, re-deriving the scope is running that recorded command rather than reconstructing one. `SKILL.md` does not restate clauses 1 through 4. It points at `graph-conventions.md`'s `### Acceptance condition` for them in one sentence.

## Amendment, 2026-09-25 (from node 292)

*Written by [node 292](292-rewrite-the-precondition-contract.md)'s worker and filed by the manager, after that node's work landed as commit `ede2c76`. Every word of the replacement is fixed by that commit: it quotes `expedition-precondition/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 292's worker's search is on node 292 under `RE-POINTING SEARCH` and its addendum.*

- **The enumerator paragraph**, as amended by node 291. In the list of files that hold *"against the four points above"*, add `.claude/skills/expedition-precondition/SKILL.md`.
- **Clause 6**, as amended by node 291. In the list of contracts whose read-back sentence reads *"check what you wrote against the four points above"*, add the precondition contract. The rest is unchanged.

`109.4` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 292](292-rewrite-the-precondition-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `ede2c76`.

## Amendment, 2026-09-25 (from node 293)

*Written by [node 293](293-rewrite-the-prototype-contract.md)'s worker and filed by the manager, after that node's work landed as commit `6d26be1`. Every word of the replacement is fixed by that commit: it quotes `expedition-prototype/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 293's worker's search is on node 293 under `RE-POINTING SEARCH`.*

- **The enumerator paragraph**, as amended by nodes 290, 294 and 291. In the list of files that hold *"against the four points above"*, add `.claude/skills/expedition-prototype/SKILL.md`.
- **Clause 6**, as amended by node 291. In the list of contracts whose read-back sentence is *"check what you wrote against the four points above"*, add the prototype contract. The rest is unchanged.

*The manager's note:* the worker reported that `grep -rlnE "against (those four|the four points above)" --include="*.md" .claude/` still returns the five worker contracts and no others, and that the `self-contained` grep still returns the same seven paths.

`109.5` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 293](293-rewrite-the-prototype-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `6d26be1`.

`109.6` `ASSUMPTION` **· settled** — *From attempt 1's handover.* Constraint 2 of the manager contract's `### The four constraints on a condition you write yourself` said the manager reads its own condition back against "the two rules that bind every condition". Once the extent rule binds every condition, that sentence would have been false. I changed it to three rules and named the extent rule as the third. I read this as one of the manager's duties under the rule, which clause 5 asks `SKILL.md` to state, and not as a meaning change that clause 7 forbids. If the checker or the human reads clause 7 more strictly, reverting that one numbered item is the fix. — The manager contract's read-back of its own condition now names three binding rules rather than two, the third being the extent rule, taken as a duty under clause 5.

*The manager's note, 2026-09-27:* [node 327](327-a-related-defect-joins-an-open-node-instead-of-becoming-a-new-one.md)'s worker reports that this node's clause 6 quotes the worker contracts as saying "against those four", where they now say "against the four points above". Node 327 also appends a paragraph to that section which says "the same points", with no count.

## Answer

graph-conventions.md now states the extent rule for a condition: an enumerator, a bounding set or no-search, working-tree only, out-of-list instances reported. The manager contract adds the duties, and the five worker contracts a fifth point.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `8c1053b`. Flags 109.1 to 109.6 settle at the node closing report. Node 44's four-point read-back is noted on node 44.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      Carry node 94's extent rule into the seven shipped files that state what a condition must be

ANSWER:        The extent rule from node 94 is now in the seven shipped files. The work is uncommitted in `.scratch/graph-workflow/worktrees/109-extent`, based on `e4beb1d`.

  - **`.claude/skills/expedition/graph-conventions.md`, `### `## Acceptance condition``.** It carries clauses 1 to 4 as four new paragraphs. They sit after the paragraph on demands about the record as a whole and before the pointer to `SKILL.md`'s `## The checker`, so the new rule is part of the existing section. The paragraphs are:
    1. The rule. Where a scope came from a search, the condition states that search beside the list of files and never in place of it, and the list and the exclusion clause stay. The author owes exactly one of three: an **enumerator** (the command and what it returned), a **bounding set** (the smallest set that provably contains every instance, and how it was computed), or a statement that the scope came from no search. A condition about a defect with instances that carries none of the three is malformed.
    2. The domain limit. An enumerator searches the working tree, never the record, and no copy repairs a search over the record.
    3. The residual clause. An out-of-list instance is reported and not edited. It gives the worker a duty to report and never a permission to edit, and a false positive costs one line.
    4. The reason. A scope is a finding stated in advance, and its readers cannot go and look, so they are owed the same extent a checker's finding owes.
  - **`.claude/skills/expedition/SKILL.md`, `## Acceptance conditions`**, following the human's amended clause 5:
    - One sentence was added to the opening paragraph. It points at graph-conventions' description for what a condition owes about the search behind its scope, and for when a condition is malformed for lacking it. Clauses 1 to 4 are not restated.
    - One manager duty was added after "you file it": a condition that carries none of the three and is malformed for it is filed as malformed rather than claimed on.
    - A sentence was appended to the re-derivation paragraph in `### Changing one after it is written`. Where a condition records the command that produced its scope, re-deriving the scope means running that recorded command rather than reconstructing one.
    - Constraint 2 of `### The four constraints on a condition you write yourself` now reads the condition back against "the three rules that bind every condition", naming the extent rule as the third. This is the call recorded as flag 1 below.
  - **The five worker contracts, `## When a node you report is an implementation node`.** Each gets a fifth bullet stating the extent rule in the worker's voice:
    - where the scope came from a search, state that search beside the list and never in place of it
    - exactly one of the three, described in plain words without the two coined names
    - a condition about a defect with instances that states none of them is malformed
    - run the command over the working tree and never over the record
    - write into the condition that an out-of-list instance is reported and not edited (the residual clause, as a duty the reporting worker writes into its condition)
    - the reason: the condition's readers cannot go and look at how its scope was found
    
    Both counts changed from four to five: "So write the condition to the five points that follow" and "check what you wrote against the five points above". The section is byte-identical across all five contracts. Node 327's related-defect paragraph says "the same points" with no count and is unchanged.
  - **How I read the amendments.** For the enumerator paragraph and clause 6, the chain 290, 294, 291, 292, 293 ends with all five contracts reading "against the four points above". The manager's note of 2026-09-27 confirms this. That matches `e4beb1d`: the grep `grep -rlnE "against (those four|the four points above)" --include="*.md" .claude/` returned the five contracts and nothing else before the work. The `self-contained` grep returned exactly the seven paths, with `CONTEXT.md` searched but not a hit. For clause 5 I worked to the human's amendment of 2026-09-25, which replaces the original clause 5.
  - **Clause 7 (nothing else changes in meaning).** Nothing was removed or renumbered. The self-containment rule, the ban on a pointer to a demand held elsewhere, the path permit, the bar's exemption from the copy rule, and the rule that an agent-minted node's condition is written by that agent all stand as before. The one change beyond clauses 1 to 6 is the count in constraint 2 (flag 1 below).
  - **Clause 8.** `CONTEXT.md` was not changed, because no term moves. "Enumerator" and "bounding set" are new names, bolded where graph-conventions defines them, and are not glossary entries. The contracts avoid both names. No file under `.scratch/` was changed.
  - **Out-of-list instance, reported and not edited.** `.claude/skills/expedition-checker/SKILL.md`, `### The search a condition records`, already says how a checker treats a recorded command and refers to "the condition's own residual clause". It agrees with the new text, so nothing needed to change there.

INDEX LINE:    graph-conventions.md now states the extent rule for a condition: an enumerator, a bounding set or no-search, working-tree only, out-of-list instances reported. The manager contract adds the duties, and the five worker contracts a fifth point.

FLAGS:
  ASSUMPTION: Constraint 2 of the manager contract's `### The four constraints on a condition you write yourself` said the manager reads its own condition back against "the two rules that bind every condition". Once the extent rule binds every condition, that sentence would have been false. I changed it to three rules and named the extent rule as the third. I read this as one of the manager's duties under the rule, which clause 5 asks `SKILL.md` to state, and not as a meaning change that clause 7 forbids. If the checker or the human reads clause 7 more strictly, reverting that one numbered item is the fix.
  Index: The manager contract's read-back of its own condition now names three binding rules rather than two, the third being the extent rule, taken as a duty under clause 5.

NEW NODES:     none

INVALIDATIONS:
  - Node 94 (whether a condition's scope stops being a list of files): extension. Its answer is now stated in the shipped files.
  - Node 39 (condition for a manager-minted node): extension. The manager's read-back against "two rules" is now against three.
  - Node 312 (cutting rules both the manager contract and graph-conventions state): consistent. The rule itself sits only in graph-conventions, and `SKILL.md` holds only the duties plus a one-sentence pointer.
  - Node 110 (whether the checker re-runs the enumerator): consistent. The residual clause it relies on now exists in the files that tell authors what a condition must carry.

CONDITIONS:
  - **What I searched for.** Every open or claimed node's `## Acceptance condition` for "four points", "points that follow", "two rules", "those four", "bind every condition", "Re-derive an enumerated", "short version", "reconstruct", and for the section headings I edited (`When a node you report is an implementation`, `Acceptance conditions`, `Changing one after`).
  - **What matched.** Only this node and node 44 ("Write the cascade pass's worker contract", open, unclaimed). Node 44's clause 7 tells its new cascade contract to state the self-containment rule and to read back against "those four points". Nothing I changed makes that clause wrong, because the count and the points are that new file's own. It does mean a cascade contract built to it would lack the extent point the five contracts now carry. Adding one is a new demand, which an amendment by a party that established a fact cannot carry, so I wrote no replacement. The manager may want to put it to the human or fold it into node 44.
  - **This node's own enumerator.** After the work, the `against (those four|the four points above)` grep returns nothing. The work changed every read-back to "the five points above", as clause 6 requires.

MISSING FROM MAP: none

GATE PAYLOAD:
  - Checker findings: none yet (first run).
  - Paths touched:
    - `.claude/skills/expedition/graph-conventions.md`
    - `.claude/skills/expedition/SKILL.md`
    - `.claude/skills/expedition-grilling/SKILL.md`
    - `.claude/skills/expedition-implementation/SKILL.md`
    - `.claude/skills/expedition-precondition/SKILL.md`
    - `.claude/skills/expedition-prototype/SKILL.md`
    - `.claude/skills/expedition-research/SKILL.md`
    
    Nothing else. `## Starting an effort` in `SKILL.md` is untouched.
  - The bar, confirmed against the repo: there is no manifest, build, tests, formatter or CI, only `CONTEXT.md`, `.claude/`, `.scratch/` and `.gitignore`. This matches the recorded bar, so only the non-command half applies. Every new line wraps at 104 columns or less, the same as the surrounding text.
  - Proposed commit message:

    Carry the extent rule into the files that state what a condition must carry

    graph-conventions.md's acceptance-condition section now states that a
    condition whose scope came from a search records it as an enumerator, a
    bounding set or a statement of no search. It also states that an
    enumerator searches the working tree only, that an out-of-list instance
    is reported and not edited, and why. The manager contract points there
    and adds the duties to file a malformed condition rather than claim it
    and to re-run a recorded command. The five worker contracts gain the
    rule as a fifth point, and their read-back counts become five.

    Node: graph-workflow/109

RETROSPECTIVE
1. **What I had to hunt for.** Whether "malformed" and "extent" already had a shipped use. The checker contract's `### What every finding carries` has the pattern clause 4 alludes to, and I found it by grepping `.claude/`. I also had to find which node set constraint 2's "two rules", to fill in INVALIDATIONS. A grep of the node files pointed to node 39.
2. **What arrived that this node did not need.**
   - Most of `map.md`: about 41KB, of which only the worktree paragraph and the plain-English rule in the rules file bore on this node.
   - The manager's notes on nodes 137, 342, 340, 124, 337, 343 and 333. They were useful only as a warning that quotes might have moved. In fact the only quotes that mattered (the two greps) matched the amendment chain exactly.
   - `decisions.md`: the grep for acceptance-condition lines returned about 20 lines, of which 94, 110, 39-related and 312 mattered.
3. **What would have made this easier.**
   - A single consolidated condition on the node, rather than a base text plus five chained amendments that replace fragments of each other. The chain for the enumerator paragraph has to be applied in order in my head.
   - A note in the spawn that constraint 2's "two rules" count exists and would be falsified. That is where clause 7 and clause 5 pull against each other.
4. **What was stale, wrong or contradictory.**
   - The node's clause 6 base text ("against those four") is stale, but the amendments fix it, as the manager noted.
   - The spawn's list of amendments omits node 290's, which is the first in the chain. The node file has it.
   - Clause 7 (no change in meaning beyond clauses 1 to 6) sits against the fact that adding a binding rule makes "the two rules that bind every condition" false. I resolved this with flag 1.
   - Node 44's open condition still builds a cascade contract to the old four-point set.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 97's check; the condition reached it as a verbatim copy in `$TMPDIR/c109.md`, assembled from the condition and its amendment sections.*

> PASS
>
> Node 109, "Carry node 94's extent rule into the seven shipped files that state what a condition must carry". The work is the uncommitted diff in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/109-extent`, on base e4beb1d. I read the whole condition in `/tmp/claude-1000/c109.md`, with each clause as its latest amendment reads it. Clause 5 is the human's 2026-09-25 wording. The enumerator paragraph and clause 6 are the versions amended by nodes 290, 294, 291, 292 and 293.
>
> **Parts of the condition**
>
> - **Scope (the seven files and no other):** met.
>   - `git status --short --untracked-files=all` shows exactly these files: graph-conventions.md, expedition/SKILL.md, and the grilling, implementation, precondition, prototype and research contracts.
>   - Nothing under `.scratch/` changed, and `CONTEXT.md` is unchanged.
> - **1:** met. graph-conventions.md's `` ### `## Acceptance condition` `` gains the rule:
>   - "the condition states that search. The list of files stays, and so does the clause that excludes every other file. The search is written beside the list … never in place of it."
>   - "owes exactly one of the three", listed as **enumerator**, **bounding set** and no-search statement, each in the clause's content.
>   - "A condition addressing a defect with instances that carries none of the three is malformed."
> - **2:** met. "An enumerator searches the working tree and never the effort's record. A search over the effort's own node files or its indexes quantifies over the record, which a condition may not do, and no copy repairs it."
> - **3:** met. "An instance the search reaches outside the condition's list is reported and not edited. A worker whose search matches a place the list does not name gains a duty to report it, and never a permission to edit it. A false positive costs one line in a handover."
> - **4:** met. The reason is stated as what the rule protects: "A condition's scope is a finding stated in advance. Its readers, the checker and the worker before it, cannot go and look at how the scope was found, so a condition owes them the same extent that a checker's finding owes."
> - **5 (the human's wording):** met.
>   - graph-conventions.md carries clauses 1–4, as above.
>   - SKILL.md's `## Acceptance conditions` states the two duties. The first is "Where a condition carries none of the three things it owes about its scope and is malformed for it, file it as malformed rather than claim the node on it." The second is "Where the condition records the command that produced its scope, re-deriving the scope is running that recorded command, rather than reconstructing one."
>   - SKILL.md does not restate clauses 1–4. It points to them in one sentence ("That description also states what a condition owes about the search that produced its scope, and when a condition is malformed for lacking it"). "That description" is the description of `## Acceptance condition` under `## The node file` in graph-conventions.md, named in the sentence before it.
> - **6 (as amended):** met in all five worker contracts.
>   - Each gains a fifth bullet beside the self-containment bullets: "Where the condition's scope came from a search, state that search beside the list of files … State exactly one of three … malformed … Run the command over the working tree, and never over the effort's own record."
>   - Each bullet also carries the residual duty: "Write into the condition that an instance the search reaches outside the list is reported and not edited."
>   - The count is corrected in both places. "So write the condition to the five points that follow" and "check what you wrote against the five points above" now match the five bullets the section lists.
> - **7:** met. `git diff --numstat` shows graph-conventions.md with 24 lines added and 0 removed. Each contract has 12 added and 3 removed, and all 3 removed lines are the two count sentences plus a blank line.
>   - The self-containment rule, the rule against a demand about the record as a whole, the path rule, the bar's exemption from the copy rule, and the row forbidding the manager to author a condition for an agent-minted node are all unchanged.
>   - In SKILL.md, constraint 2 of `### The four constraints on a condition you write yourself` now reads "the three rules that bind every condition" and names the extent rule as the third. The condition's own flag 109.6 records this change. Once clause 1 makes the extent rule bind every condition, "the two rules that bind every condition" would be false. I read the change as clause 1's own consequence, not a meaning change beyond what clauses 1–6 name. The flag already puts the stricter reading to the human.
> - **8:** met. `CONTEXT.md` is unchanged, and no `.scratch/` file changed.
> - **9:** met. See the bar below.
>   - Each file keeps its form. The contracts' new bullet addresses the worker as *you*. The graph-conventions addition is impersonal, like that file.
>   - Each new rule joins its existing section: `` ### `## Acceptance condition` ``, the contracts' list of points, and `## Acceptance conditions`.
>
> **The searches the condition records**
>
> - `grep -rln "self-contained" --include="*.md" .claude/ CONTEXT.md` returns exactly the seven paths, with `CONTEXT.md` not among them. That matches the recorded return.
> - The amended read-back enumerator, `grep -rlnE "against (those four|the four points above)" --include="*.md" .claude/`, returns nothing on the worked tree (exit 1). On HEAD, `git grep` returns the five contracts, which matches the recorded return.
>   - The empty result on the worked tree is expected, because clause 6 demands exactly this count correction.
>   - `grep -rln "against the five points above"` now returns the same five contracts.
> - Whether the worker reported any other file that states what a condition must carry is its handover's business (see NOT COVERED).
>
> **The bar**
>
> - The repo has no build, tests, formatter or CI, so there are no commands to run.
> - `git diff --check` is clean (exit 0).
> - No added line exceeds the files' wrap width.
>
> **Standards**
>
> As in my earlier checks, I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`.
>
> - **CONTEXT.md `_Avoid_` lines:** checked by hand against the added text. Nothing found.
> - **The writing rules:** bold only on the two defined rung names, and citations by heading. Each "never" stands beside its positive.
> - **`/writing-for-agents`:** the rule has one home, graph-conventions.md. SKILL.md points to it rather than repeating it. Each contract carries the rule in its own words, as ground rule 2 requires. Nothing else found.
> - **The ground rules:** nothing assumes a repo, machine or toolchain.
> - **`/coding-principles` and `/naming`:** these do not bear on prose beyond the file-form points above.
> - **graph-conventions.md:** it is part of the work, and the addition moves no element I hold the work against.
> - **Reviewing skill:** none is named, so I ran none.
>
> NOT COVERED:
> - "Where the work turns up a statement of what an acceptance condition must carry in some other file, it is reported and not edited." That report is in the worker's handover, not in the working tree, so it is outside what I was given. The diff edits no file outside the seven.
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The worktree shows no `.scratch/` change. What the main tree's record holds is outside what I was given.

*The manager's note:* the first NOT COVERED item, the report owed of any other file stating what a condition must carry, is established from the worker's handover: its ANSWER reports `.claude/skills/expedition-checker/SKILL.md`'s `### The search a condition records` as the one such place, found agreeing and left unedited.

### Gate — approve, `standing yes`, 2026-09-27

Taken under the standing yes recorded in `map.md`'s `## Notes` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise; the one owed part it could not cover is established from the handover, as the note above says; the other NOT COVERED item is the worker's bookkeeping. This settles none of the node's flags; they settle at the node closing report.

*The manager's note, 2026-09-27:* flags 109.1, 109.2, 109.3, 109.4, 109.5, 109.6 settle at the node closing report that closes this node, which names its gate as taken under the standing yes.
