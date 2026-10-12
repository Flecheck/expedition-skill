---
name: expedition-standing-yes
description: Give a standing yes in an expedition's manager thread. The human invokes it with a scope, and the manager then takes the worker's recommendation, or the checker's PASS at a gate, as the human's reply on items inside that scope. It may also cover a push of a deliverable's branch.
---

# A standing yes

You are the manager of an expedition, and the human has invoked this skill with a scope. A **standing
yes** is a yes the human gives in advance, for a scope they state. You take it in place of the human's
reply on the items inside that scope. It changes who gives that one reply, and nothing else: the graph,
the kinds of node and the workers' own work stay as they are.

## The scope

The human writes the scope in any words. A scope may name a part of the effort, such as a refactor or
part of a feature. It may instead name a type of demand, such as gates where the human trusts the
checker. Take the scope as the human wrote it, and never ask for a particular form.

## Recording the invocation

Write the invocation into the effort's map when the human makes it, as the human's standing steering,
in the human's own words. `### Standing steering, and standing instructions of one effort` in your
contract governs the invocation as it governs any standing rule. The invocation stays in force until
the human changes it.

More than one standing yes may be in force at once. Each is its own entry in the map, holding its own
scope text.

## What a standing yes covers

A standing yes covers four kinds of item, and no other:

- A worker's question. The worker's `RECOMMENDED` is taken as the human's *"ok for recommended"*.
- A worker's raise. The worker's `RECOMMENDED` is taken as the human's *"ok for recommended"*.
- A gate. The checker's `PASS` is taken as the human's approval, and you then commit as on an approval.
- A push of a deliverable's branch, which you would otherwise offer the human as your own raise. The
  standing yes is taken as the human's yes to that one push.

You decide whether an item is inside a scope, at the moment you would otherwise put the item to the
human. Where you cannot tell, put the item to the human as usual.

A payload holding several questions is covered only when every question in it is inside a scope.
Otherwise send the whole payload to the human, unchanged.

## What a standing yes never covers

Each of the following goes to the human as usual, whatever the scope says:

- a question or raise with no recommendation the worker believes
- a checker's `FAIL`
- a checker's raise, which includes a question a checker hands back beside its outcome
- a gate whose check will not pass
- a gate holding a part of its condition that the checker could not cover, that is still owed, and
  that you cannot establish
- a reject
- an acceptance condition judged wrong
- closing the effort

Anything outside the four kinds above is not covered either. That includes every raise of your own
other than the offer of a push.

## Taking a covered item

Your contract's `## What is in front of the human, and when` says what happens to a covered item. Take
the item in the same turn you would otherwise have queued it.

1. For a question, a raise or a gate, record the item on the node. A question or a raise goes under
   `## Interview`. A gate goes under `## Review`. `### Recording the human's words` in
   `graph-conventions.md` holds the entry's form.
2. For a question or a raise, resume the worker with this line in place of `HUMAN ANSWER`:

   ```
   STANDING YES:  <the scope text, verbatim>
   ```

   The rest of the worker's resume shape is unchanged. `DIVERGENCE` is never present, because a standing
   yes always takes the recommendation.
3. For a gate, commit as on an approval. The node then resolves.
4. For a push, push the deliverable's branch. A push belongs to no node, so nothing is recorded on
   one. Say in your next report to the human which branch you pushed, and quote the scope text of the
   standing yes that covered it.

## Flags, and the node closing report

`## Flags` in your contract says when a node's flags settle where its gate was taken under a standing
yes.

The node closing report names every item on the node taken under a standing yes, each with its scope.
It states that the human may take any listed item back by naming it in a reply. An item taken back is
a revision of its node, handled like any other.
