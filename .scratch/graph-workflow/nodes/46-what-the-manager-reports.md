# What the manager reports to the human, in one place

Type: precondition
Status: open

## Question

Collect every duty the manager's report to the human owes, from each node that added one, into a single
statement of what that report contains. At least four are known and no file lists them:

- the line naming what a **cascade pass minted**, or that it found nothing — [Cascade pass
  mechanics](15-cascade-pass-mechanics.md), flagged there at `15.2`;
- the line naming **what waits behind the live question**, by node name and kind only — [What the manager works
  on next, and how the human redirects it](16-human-steering.md), flagged there at `16.4`;
- the **pick report**, naming the implementation being started and the open questions judged non-fatal — the
  same node;
- the three states **invisible in the graph files**, a node reading `claimed` like any other: which node awaits
  approval at a gate, whether a worker is blocked on a raise, and what is banked and waiting — the same node,
  inheriting them from [Git and code-landing policy](11-git-and-code-landing.md) and [When an AFK worker cannot
  proceed](23-worker-cannot-proceed.md).

Decides nothing and writes no product code: its output is the input to the manager's own skill.

Reported by [What the manager works on next, and how the human redirects it](16-human-steering.md)'s worker.
Its own framing of why this is a `precondition` and not the implementation itself: *"two of the duties come
from a node this worker did not read, so the enumeration cannot be written here — and an implementation node
whose condition cannot be written in full is not startable, by this node's own answer."*

So this node is the **first application of the readiness floor its own reporting node had just decided**, and
it is applied against that node itself. The floor: an implementation is startable when its acceptance condition
can be written in full, with nothing deferred to an open question.

**Blockers: none.** It reads resolved nodes and writes an enumeration; nothing it needs is open.

**Why it matters, in the reporting worker's words:** the pick report *"has grown duties from three different
nodes and nothing states its contents"*, which is the shape of the failure [What keeps the shipped files
consistent when a decision changes a term](29-shipped-file-consistency.md) exists because of — a list that was
correct about the files it knew. That node has now been recorded twice as recurring inside the graph's own
files rather than in the product.

## Annotation: a fifth duty for this list, found at node 76's gate

*Filed by the manager. Not a change to the question above, which already says at least four are known and no file
lists them — this is the fifth, found the same way.*

**The human's four moves on the closing report.** Duty 141 of [Gather the manager's accumulated
duties](75-gather-the-managers-duties.md), settled at [Done-ness and termination](10-done-ness.md): *"accept;
settle a flag on the spot; **promote**, which creates a node; or reject what landed, which is a revision."*

**It is in no shipped file.** [Write the first version of the manager's skill](76-write-the-manager-skill.md)
states what the closing report *contains* — what landed, the supersession chains, the state of the bar, every
outstanding flag, what the sweep found — and says nothing about what the human may do with it. That is correct
for that node: its clause 36 demanded the contents and nothing more.

**How it was found, which is the part worth keeping.** The blind checker reported that `promote` is defined under
`## Words used exactly` and used nowhere in the body, and offered it as an observation rather than a finding, the
term list being the acceptance condition's own. The human asked whether there was a plan to use it. **A defined
term with no conduct behind it is a reliable marker for a duty nobody wrote down** — the same question about
`cascade` produced [The manager's cascade duties are in neither
contract](87-managers-cascade-duties-have-no-contract.md) one message earlier.

**Two more terms have the same shape and are not filed anywhere yet**: `revision` and `AFK / HITL` each appear in
the manager's contract only inside other entries' definitions. Whether either hides a duty has not been checked.
