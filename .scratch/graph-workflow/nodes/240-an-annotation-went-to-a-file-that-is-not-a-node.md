# An annotation was written to a file that is not a node, under an id already in use

Type: implementation
Status: resolved

Blocked by: none

## Question

*Surfaced by [node 213](213-nothing-triggers-the-ten-mechanical-checks.md)'s worker, and pasted as it wrote
it. **Its acceptance condition below is that worker's own**, written in the same handover.*

**3. An annotation was written to a file that is not a node, under an id already in use**
Kind: implementation
Blockers: none
Question: A checker's findings on node 188 were filed to a new file sharing node 198's id, carrying no
node fields and untracked by git, and node 198's own file never received them. Put the annotation where
it belongs and leave one file per id.

Acceptance condition:

&gt; The work is confined to `.scratch/graph-workflow/nodes/`. The worker may not mark this node, resolve
&gt; it, or write a line in `decisions.md` or `flags.md`. **This work changes the effort's own record, so
&gt; the never-delete rule binds it: no text is removed, and text that moves moves verbatim, struck-through
&gt; text staying struck through.**
&gt;
&gt; Two files under `.scratch/graph-workflow/nodes/` begin with `198-`:
&gt; (A) `198-two-files-describe-the-rules-file-by-contents-node-188-removes.md`, which has a title line, a
&gt; `Type:` field, a `Status:` field, and sections `## Question`, `## Acceptance condition` and `## The
&gt; manager's note at filing`; and
&gt; (B) `198-two-shipped-descriptions-of-the-rules-file-are-stale.md`, which is untracked by git, has no
&gt; title line, no `Type:` field and no `Status:` field, and whose entire content is one section headed
&gt; `## Annotation: a third site, and a bounding set that is provably complete outside the record`.
&gt; File (A) does not contain that annotation.
&gt;
&gt; Done means every one of the following is true of the finished tree.
&gt;
&gt; 1. Exactly one file under `.scratch/graph-workflow/nodes/` has a name beginning `198-`, and it is file
&gt;    (A) under its existing name.
&gt; 2. Every byte of file (B)'s content, its heading included, appears in file (A), verbatim and
&gt;    unshortened, as a section of file (A) placed after its last existing section.
&gt; 3. File (B) no longer exists.
&gt; 4. File (A)'s title line, `Type:` field, `Status:` field, `## Question`, `## Acceptance condition` and
&gt;    `## The manager's note at filing` are byte-identical to what they were before this work.
&gt; 5. No file outside `.scratch/graph-workflow/nodes/` is modified, and no file under
&gt;    `.scratch/graph-workflow/nodes/` other than (A) and (B) is modified.
&gt; 6. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This node was specified in a handover the manager left unfiled for a session**, and is minted late for that
reason rather than any other — flag `213.4` records the delay against the manager. Nothing in the text above
was re-authored on the way here; it is the worker's own, recovered verbatim from the session record.

## Answer

**The repair this node specifies was already performed, before the node existed.** The manager made the defect and
the manager repaired it, both within the session in which node 213's worker found it — and node 213's handover then
sat unfiled long enough that the node describing the repair was minted after the repair had landed.

**Established from the tree rather than from memory**, today:

- Exactly one file under `nodes/` begins with `198-`, and it is
  `198-two-files-describe-the-rules-file-by-contents-node-188-removes.md`, the real node. **The stray file carrying
  a duplicate id is gone.**
- That node carries the checker's findings, in the annotation headed `## Annotation: a third site, and a bounding
  set that is provably complete outside the record`, pasted verbatim as the checker wrote them.
- Node 198 has since been claimed, worked, checked, approved and **landed** — which it could not have been while its
  file was missing the findings its own condition's extent turned on.

**So the condition's demand — put the annotation where it belongs and leave one file per id — holds of the tree, and
no work is owed.**

**What the manager is disclosing rather than hiding.** This is an implementation node resolved **without a gate**,
and a gate is where an implementation node is meant to become visible to the human. **There is nothing to approve**:
no branch, no worktree, no diff, and the change it would have carried is already on `master` in a commit made for a
different reason. The manager is recording that departure here rather than quietly resolving, because the honest
description is *this node was minted after its own work had landed*, and the reason it was minted late is flag
`213.4` against the manager.

**What the node still bought.** Its acceptance condition is the only written statement of what a correct repair
looked like, and it was written by a party that had found the defect independently. **It agrees with what was
done**, which is worth more as a check than as an instruction.
