# The manager's own uncommitted record edits collide with a landing branch

Type: grilling
Status: open

Blocked by: none

## Question

*The manager's own, minted after the collision below. Marked as the manager's.*

**The landing policy has no procedure for the case where the manager's own uncommitted edits sit on the files a
landing branch changes.** It met that case at [node 144](144-make-the-rules-file-stand-alone.md): the branch changed
`map.md` and `map-implementation-rules.md`, and the main checkout held uncommitted manager edits to both — two count
settings written there minutes earlier. `git merge --ff-only` cannot write a file with local modifications, so an
approved node could not land.

**Why the case is structural rather than unlucky.** The policy says the graph's own files *"are **not** committed per
node; they are committed periodically by the human"*. So the record accumulates uncommitted edits for long stretches
by design — while implementation nodes whose work **is** the record land by fast-forwarding over those same files.
The two rules guarantee the collision; nothing in the policy names it.

**What makes it worse than an ordinary conflict:** the manager's edits exist in no commit anywhere. A wrong move
loses the human's own recorded words, which is the one thing the never-delete rule exists to protect.

**What is open:**

1. Does the manager commit the record before a landing, and if so does that survive the human's standing instruction
   that they review a diff before a commit is made?
2. Or does the manager stash and restore, accepting a window where the edits live only in a stash?
3. Or does the record stop being edited at all while a record-editing node is in flight — which serialises the
   manager against its own workers?
4. Is this the same question as [node 115](115-two-writers-edit-the-map-at-once.md)'s, or a different one? Node 115
   is a *worker's* map change against the manager's; this is the manager against itself, and its open carriers are
   [node 160](160-carry-the-integration-conflict-rule-into-the-map.md) and [node
   162](162-how-much-of-the-integration-rule-ships.md).

## The manager's note at filing

*Not a change to anything above.*

**The manager has taken no route.** The collision is live and unresolved at this node's filing: node 144's work is
committed on its branch and not merged, and the manager put the sequence to the human rather than running it.

**The human's words that prompted it**, `verbatim`: *"we should make it so that there isn't issues like that later"*.

**Not started, and the reason is a count rather than a judgement.** This effort runs two nodes needing the human at
once, and both places are held by [node 165](165-measure-whether-a-fed-file-earns-its-place.md) and [node
50](50-shared-blocks-stay-duplicated.md), each holding a banked question.
