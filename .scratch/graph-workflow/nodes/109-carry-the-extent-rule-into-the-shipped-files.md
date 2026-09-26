# Carry node 94's extent rule into the seven shipped files that state what a condition must be

Type: implementation
Status: open
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

`109.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 290](290-rewrite-the-research-contract-as-the-pilot.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `4068519`.

## Amendment, 2026-09-25 (from node 294)

*Written by [node 294](294-rewrite-the-implementation-contract.md)'s worker and filed by the manager, after that node's work landed as commit `724c361`. Every word of the replacement is fixed by that commit: it quotes `expedition-implementation/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 294's worker's search is on node 294 under `RE-POINTING SEARCH`.*

- **The enumerator paragraph**, as amended by node 290. Replace "and *"against the four points above"* in `.claude/skills/expedition-research/SKILL.md`" with "and *"against the four points above"* in `.claude/skills/expedition-research/SKILL.md` and `.claude/skills/expedition-implementation/SKILL.md`".
- **Clause 6**, as amended by node 290. Replace "or in the research contract" with "or in the research and implementation contracts". The rest is unchanged.

`109.2` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 294](294-rewrite-the-implementation-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `724c361`.

## Amendment, 2026-09-25 (from node 291)

*Written by [node 291](291-rewrite-the-grilling-contract.md)'s worker and filed by the manager, after that node's work landed as commit `0a3e68b`. Every word of the replacement is fixed by that commit: it quotes `expedition-grilling/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 291's worker's search is on node 291 under `RE-POINTING SEARCH`.*

- **The enumerator paragraph**, as amended by nodes 290 and 294. Replace "in `.claude/skills/expedition-research/SKILL.md` and `.claude/skills/expedition-implementation/SKILL.md`" with "in `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md` and `.claude/skills/expedition-grilling/SKILL.md`".
- **Clause 6**, as amended by node 294. Replace "or in the research and implementation contracts" with "or in the research, implementation and grilling contracts". The rest is unchanged.

`109.3` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 291](291-rewrite-the-grilling-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `0a3e68b`.

## Amendment by the human, 2026-09-25

*The manager's question, carrying node 312's worker's recommendation from node 312's `RE-POINTING SEARCH:`:* "Do you agree to amend node 109's clause 5 this way, or keep it as written?" The way proposed: `graph-conventions.md`'s `### Acceptance condition` states the rule itself (clauses 1 to 4), and the manager contract's `## Acceptance conditions` states only the manager's duties under it, pointing at `graph-conventions.md` in one sentence. The reason given: clause 5 as written would re-create a rule stated in both files, which the split the human approved at node 312 rules out.

The human, `verbatim`: *"I agree"*

*The manager drafted the wording below, and the human amended the condition with it. The condition above and its earlier amendments are left as they were. The clause below takes the place of clause 5.*

5. **`graph-conventions.md`'s `### Acceptance condition` carries clauses 1 through 4.** `SKILL.md`'s `## Acceptance conditions` states the manager's duties under that rule: it files a condition carrying none of the three rungs as malformed rather than claiming the node on it, and where a condition records its enumerator, re-deriving the scope is running that recorded command rather than reconstructing one. `SKILL.md` does not restate clauses 1 through 4. It points at `graph-conventions.md`'s `### Acceptance condition` for them in one sentence.

## Amendment, 2026-09-25 (from node 292)

*Written by [node 292](292-rewrite-the-precondition-contract.md)'s worker and filed by the manager, after that node's work landed as commit `ede2c76`. Every word of the replacement is fixed by that commit: it quotes `expedition-precondition/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 292's worker's search is on node 292 under `RE-POINTING SEARCH` and its addendum.*

- **The enumerator paragraph**, as amended by node 291. In the list of files that hold *"against the four points above"*, add `.claude/skills/expedition-precondition/SKILL.md`.
- **Clause 6**, as amended by node 291. In the list of contracts whose read-back sentence reads *"check what you wrote against the four points above"*, add the precondition contract. The rest is unchanged.

`109.4` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 292](292-rewrite-the-precondition-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `ede2c76`.

## Amendment, 2026-09-25 (from node 293)

*Written by [node 293](293-rewrite-the-prototype-contract.md)'s worker and filed by the manager, after that node's work landed as commit `6d26be1`. Every word of the replacement is fixed by that commit: it quotes `expedition-prototype/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 293's worker's search is on node 293 under `RE-POINTING SEARCH`.*

- **The enumerator paragraph**, as amended by nodes 290, 294 and 291. In the list of files that hold *"against the four points above"*, add `.claude/skills/expedition-prototype/SKILL.md`.
- **Clause 6**, as amended by node 291. In the list of contracts whose read-back sentence is *"check what you wrote against the four points above"*, add the prototype contract. The rest is unchanged.

*The manager's note:* the worker reported that `grep -rlnE "against (those four|the four points above)" --include="*.md" .claude/` still returns the five worker contracts and no others, and that the `self-contained` grep still returns the same seven paths.

`109.5` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 293](293-rewrite-the-prototype-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `6d26be1`.
