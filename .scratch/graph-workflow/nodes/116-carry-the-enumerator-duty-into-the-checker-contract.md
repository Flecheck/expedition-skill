# Carry the checker's enumerator duty into the checker's contract

Type: implementation
Status: claimed

## Question

*Surfaced by [Whether the checker re-runs a condition's own enumerator](110-does-the-checker-rerun-the-enumerator.md)'s
worker, and pasted as it wrote it.*

> Make the checker's contract state that where an acceptance condition records the search that produced its scope,
> the checker runs that command as written, reports what it returned against what the condition records, and never
> `FAIL`s the work on that comparison alone. Nothing states this today: `scope` appears in that file zero times, and
> node 109 ships node 94's rule into seven files that do not include it.

**Blockers, in the worker's words:** *"none. Node 110 resolves with this handover, node 94 is resolved, and this node
shares no file with nodes 95, 103, 109, 111 or 114."*

## Acceptance condition

*Written by node 110's worker. Pasted as it wrote it, and not the manager's. It carries its scope's enumerator under
[node 94](94-condition-scope-as-a-predicate.md)'s rung 1.*

> **Scope, and the search that produced it.** `.claude/skills/expedition-checker/SKILL.md` is edited and no other
> file is.
>
> **The enumerator, run while this condition was written.** `grep -rln "enumerator" --include="*.md" .claude/
> CONTEXT.md` returns exactly that one path, and `grep -rln "extent" --include="*.md" .claude/ CONTEXT.md` returns
> exactly that same one path — so that file is the only shipped file naming either, and it names them only about the
> checker's own findings. Beside them, `grep -c "scope" .claude/skills/expedition-checker/SKILL.md` returns **0**:
> the contract does not use the word at all, so this work adds a duty rather than repairing instances of a defect
> spread across the tree. **A place this work finds stating what a checker establishes about a condition's scope,
> outside the file above, is reported and not edited**; reporting it is the whole of what this condition asks for it.
>
> **One expected movement in that enumerator, stated so it is not read as a discrepancy.** [Node
> 109](109-carry-the-extent-rule-into-the-shipped-files.md) is open and will add the word *enumerator* to seven other
> shipped files. Where it has landed before this node is checked, the first command above returns eight paths rather
> than one, and the seven additions are node 109's work and not this node's scope.
>
> 1. **The duty, copied here in full rather than pointed at.** The contract states that where the acceptance
>    condition records the search that produced its scope, the checker **runs that command as written** and states in
>    its outcome what the command returned and whether that matches the return the condition records.
>
> 2. **What the comparison is against.** The contract states that the comparison is against the **return the
>    condition records**, and not against the condition's list of places. It states that the two may legitimately
>    differ — a condition may exclude part of its scope from the enumerator's domain and say so — and that where the
>    condition states the reason, the difference is not a discrepancy.
>
> 3. **What the comparison is not.** The contract states that the checker is not asked whether the scope has grown
>    since the condition was written, and cannot establish it: it holds no before-state, the work has moved the
>    listed files under it, and other work may have landed in them. What it establishes is whether a recorded claim
>    is false.
>
> 4. **The outcome.** The contract states that a mismatch, or a return reaching a place the condition's list does not
>    name, is handed back **alongside** the outcome and is **never on its own a `FAIL`**. It states all three
>    reasons: a property nobody demanded of the work is not a finding, the enumerator being a statement of how the
>    list was got rather than a demand on the work; a `FAIL` sends the work back to a worker who met the scope as
>    written and whom this contract forbids to repair a condition; and the condition's own residual clause already
>    routes an out-of-list instance to being reported and not edited.
>
> 5. **What stays a `FAIL`.** The contract states that the work editing a file outside the condition's list remains a
>    `FAIL` on the condition, established from the diff and not from the enumerator.
>
> 6. **A record-reaching domain.** The contract states that where the recorded command's domain reaches the effort's
>    record rather than the working tree, the checker runs it as written, reports that the condition's enumerator
>    reaches material the checker is blind to, and does **not** silently narrow the command to the tree.
>
> 7. **Authorship is not a factor.** The contract states that this duty holds whoever wrote the enumerator, and that
>    the checker is not told and does not ask.
>
> 8. **The surplus travels as a finding.** The contract states that what is handed back under clause 4 is a finding,
>    so it carries the three things `### What every finding carries` already requires of one — the instances, the
>    form as a predicate, and one of the three extents.
>
> 9. **Nothing already in the file is removed, renumbered, or changed in meaning** beyond what clauses 1 to 8 name.
>    In particular hard rules 1 to 6, `### What every finding carries`, `### What you can establish, and what you
>    cannot`, the `PASS`, `FAIL` and raise shapes, the `QUESTIONS:` and `NOT COVERED:` routes, and the five raise
>    grounds all stand exactly as they stand today. **Where in the file the new material goes is not dictated**, that
>    being a form the worker settles.
>
> 10. **`CONTEXT.md` is changed only if a term genuinely moves**, and where one does, it is reported in the handover
>     rather than assumed to travel. No file under `.scratch/` is changed.
>
> 11. **The bar.** The standing bar applies: the tree builds, warns about nothing, is formatted, and passes the tests
>     relevant to the change. This repository has no build, no tests and no formatter, which is a complete bar on its
>     remaining half rather than a deficient one — so what remains is `/coding-principles`, `/naming`, and the file's
>     own form: it addresses the checker as *you*, states rules rather than explaining them, and a new rule joins an
>     existing section rather than sitting beside it.

## The manager's note at filing

*Not a change to anything above.*

**This is the first node whose acceptance condition anticipates its own enumerator moving**, in the paragraph headed
*"One expected movement"*. Node 110's answer makes a checker compare the recorded return against what the command
returns now; this condition pre-empts the false positive that node 109 landing first would otherwise produce. Whether
that is a shape other conditions should copy is nobody's node yet.
