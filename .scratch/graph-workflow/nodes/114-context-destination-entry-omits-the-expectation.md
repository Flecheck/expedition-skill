# `CONTEXT.md`'s `Destination` entry does not say the destination states whether the effort is expected to end

Type: implementation
Status: claimed

## Question

*Reported as an invalidation by [Whether charting an effort establishes and records that it is expected to
end](91-charting-records-whether-an-effort-ends.md)'s worker, and pasted as it wrote it. Minted by the manager
because no node reached it.*

> `CONTEXT.md`'s `Destination` entry reads *"What reaching the end of an effort looks like. It fixes the scope, which
> is what makes work beyond it out of scope rather than fog."* It is now short by this answer: the destination also
> states whether the effort is expected to reach it. Contradicted by omission rather than by statement, so the
> disposition is an extension of the entry, not a replacement. **No open node reaches it** — nodes 90, 106 and 107
> each repair a different `CONTEXT.md` entry (`Closed`, `Closing report`, the reservation of the word `report`), and
> none touches `Destination`.

**Blockers:** none.

## Acceptance condition

***Written by the manager, for a node the manager minted itself*** because the node that found the defect surfaced it
as an invalidation rather than as a node, and no other node reaches the entry. Marked as the manager's own under
[Who writes the acceptance condition for an implementation node the manager mints
itself](39-condition-for-a-manager-minted-node.md), whose constraint 1 confines it to what is already fixed. **What
is fixed is node 91's resolved answer**; the entry's wording and the shape of the addition are not, so this condition
states the property and leaves the form.

> **Scope, and the search that produced it**, under [node 94](94-condition-scope-as-a-predicate.md)'s rung 1.
> `CONTEXT.md` is edited and no other file is.
>
> ~~The enumerator, run while this condition was written: `grep -rn "Destination" CONTEXT.md` returns two lines — the
> entry's own heading `**Destination**:` and the `_Avoid_` line of another entry that refuses the word — and
> `grep -rln "Destination" .claude/skills` returns no file, so the term is stated in the glossary and nowhere in the
> shipped skills.~~
>
> **Struck and replaced. Both recorded returns were false when the manager wrote them**, found by [Whether the
> checker re-runs a condition's own enumerator](110-does-the-checker-rerun-the-enumerator.md)'s worker and re-run by
> the manager before this correction. What the commands actually return:
>
> - `grep -rn "Destination" CONTEXT.md` returns **one** line, `CONTEXT.md:39:**Destination**:`. The command is
>   case-sensitive and the `_Avoid_` line the manager had in mind is lowercase, so it never matched.
> - `grep -rln "Destination" .claude/skills` returns **one** file, `.claude/skills/expedition/graph-conventions.md`.
>   That hit is the description of `map.md`'s `## Destination` section under `## The five files` — **the exact line
>   [node 111](111-write-the-starting-an-effort-section.md)'s clause 10 is open to edit**. So this node stays out of
>   it, and the two conditions do not collide: node 111 edits that line, this node edits `CONTEXT.md`'s entry.
>
> A place this work finds stating what the destination holds, outside `CONTEXT.md`, is **reported and not edited**;
> reporting it is the whole of what this condition asks for it.
>
> 1. `CONTEXT.md`'s **Destination** entry states that the destination also says, in one line, whether the effort is
>    expected to reach it.
> 2. It states that where the effort is not expected to reach it, this is where a manager reads that a non-empty
>    frontier is that effort's steady state rather than a defect.
> 3. The entry's existing two sentences are kept, the addition being an extension rather than a replacement, and its
>    `_Avoid_` line is unchanged.
> 4. The entry states nothing, in any wording, about how often efforts end or fail to end.
> 5. No other entry in `CONTEXT.md` changes. In particular the **Closed**, **Closing report**, **Flag** and
>    **Handover** entries are untouched, those being nodes 90, 106, 103 and 107's work.
> 6. No file under `.claude/skills/` changes and no file under `.scratch/` changes.
> 7. The working tree meets the bar.

### The manager's read-back, recorded before any claim

*[Node 39](39-condition-for-a-manager-minted-node.md)'s constraint 2 requires the condition to be read back against
the two rules that bind every condition, and that reading recorded on the node.*

- **Self-contained text.** It passes. Each demanded property is written out here rather than pointed at; the file is
  named by path and the checker has the repo; the enumerator is a command the checker can run.
- **It does not quantify over the record.** It passes. Every clause is a demand about the state of one file, and the
  enumerator's domain is the tree rather than `nodes/` — which is what flag `94.2` requires.

## The manager's note at filing

*Not a change to anything above.*

**Node 111 could not absorb this**, its own clause 12 confining it to `.claude/skills/expedition/`. That is why this
is a node rather than a widening.

## Annotation: the condition's enumerator was corrected in place before any claim

*Filed by the manager against its own text. The node is open and holds no work, so [Revision
semantics](06-revision-semantics.md)'s in-place route applies rather than supersession.*

**What was wrong and who found it.** Both recorded returns in the scope clause were false at the moment the manager
wrote them — not stale, false. Node 110's worker ran the two commands as part of its own node and reported them; the
manager re-ran both before correcting, and both of the worker's findings hold exactly. The struck text and its
replacement are in the condition above.

**Why this matters beyond one node.** The manager wrote the first condition on this graph to carry an enumerator
under [node 94](94-condition-scope-as-a-predicate.md)'s rung 1, and got the enumerator wrong — which is the precise
failure node 110 is asking whether the checker should catch. **The instance is the manager's own and is recorded as
evidence for that node rather than as an argument in it.** Node 110's worker put it more sharply than the manager
would: on the two live false instances, *"the author is the manager."*
