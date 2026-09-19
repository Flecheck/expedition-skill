# Where the harness-worktree standing instruction lives, now that the landing policy has left `map.md`

Type: implementation
Status: open

Blocked by: 140

## Question

*Surfaced by [Move the implementer's and checker's material out of the map](140-move-the-implementers-and-checkers-material-out-of-the-map.md)'s worker, and pasted as it wrote it.*

> `master` gained a paragraph beginning `**A worktree is created by the harness, never by hand.**`, written to sit
> *"immediately below"* the landing policy, which node 140 has just moved into `map-implementation-rules.md`. The
> landing policy's own struck clause points at it by position. It is implementer-and-checker material by kind and by
> node 138's own test, but it is not among the four bodies node 140's condition names, so it stays in `map.md` while
> the paragraph it belongs beside is elsewhere, and the cross-reference no longer resolves.

**Blockers, in the worker's words:** *"node 140 landing."*

## Acceptance condition

*Written by node 140's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/`. The worker may edit `map.md` and `map-implementation-rules.md` and no other
> file; it may not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`. Done means: the
> paragraph beginning `**A worktree is created by the harness, never by hand.**` is in
> `map-implementation-rules.md`, in the section holding the paragraph beginning `**Landing policy**`, and immediately
> after it; its text is byte-identical to what `map.md` held, nothing in it reworded or shortened; it is no longer in
> `map.md`, and `map.md` restates none of it; the landing policy's own phrase `see the standing instruction
> immediately below` resolves to that paragraph's new position; `map.md` gains no second markdown link to
> `map-implementation-rules.md` and holds no more than the pointer it already holds; `map.md` holds exactly these
> `##` headings and no other at `##` level: `## Destination`, `## Notes`, `## Decisions so far`;
> `map-implementation-rules.md` gains no heading named `## Notes`; and every markdown link in both files resolves to
> a path that exists, except any link to a path outside this repository, which is out of this node's scope.

## The manager's note at filing

*Not a change to anything above.*

**The paragraph this node moves is the manager's own**, written into `map.md` on the human's worktree instruction
while node 140 was claimed and its subject was `map.md`. That is the two-writers collision [node
115](115-two-writers-edit-the-map-at-once.md) names, and it is what produced this node.

**Its condition's last clause already excepts the out-of-repository link** that defeats node 140's clause 14 and node
144's clause 6 — see [node 154](154-the-dogfood-link-names-a-path-on-another-machine.md).

## Annotation: node 188 has landed, and this condition is unsatisfiable as written

*Filed by the manager from [node 188](188-move-the-landing-section-out-of-the-workers-file.md)'s worker, in its own
words. Nothing above is changed, and **the condition is not amended** — a condition is not the manager's to rewrite,
and this node is unclaimed, so the repair is the human's or a fresh writer's.*

> **Node 152** (*Where the harness worktree instruction lives*) — **unsatisfiable as written.** It requires the
> `**A worktree is created by the harness, never by hand.**` paragraph to land in `map-implementation-rules.md` *"in
> the section holding the paragraph beginning `**Landing policy**`, and immediately after it"*, and it permits
> editing only `map.md` and `map-implementation-rules.md`. That section is now in a third file its worker may not
> touch. Its clause that *"the landing policy's own phrase `see the standing instruction immediately below` resolves
> to that paragraph's new position"* names a phrase that also moved. The natural repair points the whole node at
> `map-manager-only.md`, which is a change of place rather than an addition, so it likely exceeds node 82's
> manager-amendment authority.

**The manager agrees it exceeds that authority and has not exercised it.** Node 82 lets the manager widen a
condition's scope where the scope was too narrow for the work it names; this is a different file being named as the
destination, which changes what the node does rather than how much of the tree it may touch.

## Annotation: the manager's position above is now false in its first limb

*Filed by the manager on 2026-09-19, carrying [node
252](252-may-an-unclaimed-nodes-acceptance-condition-be-amended.md)'s worker's words rather than the manager's.*

> It records the manager's position that *"a condition is not the manager's to rewrite, and this node is unclaimed,
> so the repair is the human's or a fresh writer's."* Under node 252 the repair is the manager's, the falsifying
> party — node 188's worker — having finished. The annotation is the manager's own text on an open node.

***The manager's own note, beside that text.*** The struck-through limb is **not** struck above, because the never-
delete rule marks record text where it stands and this annotation is that mark. **The repair itself is not made
here.** This node's condition is also the one [node
250](250-state-how-an-implementation-worker-reaches-its-worktree.md) was told to preserve the exact phrases of, and
node 250's work is uncommitted at a gate; whoever amends this condition must quote the section's form **after** that
gate settles, not before.
