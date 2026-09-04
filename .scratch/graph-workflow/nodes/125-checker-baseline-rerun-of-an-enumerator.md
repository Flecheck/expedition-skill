# Whether a checker's baseline re-run of an enumerator belongs in its contract

Type: grilling
Status: open

Blocked by: none

## Question

*Surfaced by [Carry the checker's enumerator duty into the checker's
contract](116-carry-the-enumerator-duty-into-the-checker-contract.md)'s worker, and pasted as it wrote it.*

> The checker contract now says the checker is not asked whether a condition's scope has grown and cannot establish
> it, because it was given no before-state. A checker can reach one anyway: node 103's attempt 2 re-ran the recorded
> enumerator against commit `47703bb`, confirmed the recorded four exactly, and established that the 4→3 divergence
> was the work repairing the fourth file — turning a bare mismatch into a diagnosis, on the rule's first live outing,
> with nothing telling it to. So: does the contract name that re-run as something the checker may do, and how is it
> squared with blindness to the record — the baseline being reachable from git while the commit the condition was
> written against is not? And if it is named, does the checker still say it cannot establish growth, or does it say
> what it can and cannot separate?

**Blockers, in the worker's words:** *"none. Node 110 is resolved, node 116 has landed the rule it decided, and this
node shares its file with no open node except node 109, which does not touch the checker contract."*

## The manager's note at filing

*Not a change to anything above.*

**One correction to the blocker line, and it does not change the answer.** Node 116 has **not** landed — its work is
uncommitted and its check is running as this node is filed. The rest of the line holds, and the node is unblocked
either way, being a grilling node that decides rather than edits. **If node 116's check or gate changes the sentence
this node is about**, whoever takes this node reads the file as it then stands rather than as quoted here.

**A fact this node's answer will need and which is not in the question.** The sentence at issue is the worker's own
wording rather than the condition's: the condition mandated *"it holds no before-state"* and the worker wrote *"you
were given no before-state"*, recorded as flag `116.1`. So the thing this node asks about is already a live
disagreement between a condition and the work that met it.
