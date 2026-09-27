---
name: expedition-standing-yes
description: Give a standing yes in an expedition's manager thread. The human invokes it with a scope, and the manager then takes the worker's recommendation, or the checker's PASS at a gate, as the human's reply on items inside that scope.
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
contract governs it as it governs any standing rule. It binds only once it is written into the map. It
stays in force until the human changes it. It is this effort's alone, so the next effort starts without
it.

More than one standing yes may be in force at once. Each is its own entry in the map, holding its own
scope text.

## What a standing yes covers

A standing yes covers three kinds of item, and no other:

- A worker's question. The worker's `RECOMMENDED` is taken as the human's *"ok for recommended"*.
- A worker's raise. The worker's `RECOMMENDED` is taken as the human's *"ok for recommended"*.
- A gate. The checker's `PASS` is taken as the human's approval, and you then commit as on an approval.

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

Anything outside the three kinds above is not covered either, your own raise included.

## Taking a covered item

A covered item never enters the pending queue, and you do not put it to the human. Take it in the same
turn you would otherwise have queued it.

1. Record it on the node. A question or a raise goes under `## Interview`. A gate goes under `## Review`,
   as the gate's outcome. Mark the entry `standing yes`, and never `verbatim`. The entry quotes the scope
   text word for word, says which standing yes was applied, and quotes what was taken: the worker's
   `RECOMMENDED`, or the checker's `PASS`. `### Recording the human's words` in `graph-conventions.md`
   holds the entry's form.
2. For a question or a raise, resume the worker with this line in place of `HUMAN ANSWER`:

   ```
   STANDING YES:  <the scope text, verbatim>
   ```

   The rest of the worker's resume shape is unchanged. `DIVERGENCE` is never present, because a standing
   yes always takes the recommendation.
3. For a gate, commit as on an approval. The node then resolves.

## Flags, and the node closing report

A gate taken under a standing yes is not put in front of the human, so it settles none of the node's
flags. The node's flags settle at the node closing report, as a node's flags do where it has no gate.

The node closing report names every item on the node taken under a standing yes, each with its scope.
It carries every flag the node holds, as any node closing report does. It states that the human may
take any listed item back by naming it in a reply. An item taken back is a revision of its node,
handled like any other.
