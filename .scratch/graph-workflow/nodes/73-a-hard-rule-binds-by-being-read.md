# State in a shipped file that a hard rule binds by being read

Type: implementation
Status: superseded
Superseded by: 340

## Question

The shipped files nowhere say **what kind of thing a hard rule is.** [Whether the workflow ships explicit subagent
definitions](69-explicit-subagent-definitions.md) established the distinction — a contract states what a worker
**may** do and is honoured by an agent that reads it, where what a worker **can** do is a property of the harness
that ran it — and today it lives only inside that node's answer, reachable only by a reader who already knows to
look.

**Why it matters rather than being theory.** Two agents have read a hard rule down ([Whether a checker may write
scratch files outside the work](67-whether-a-checker-may-write-scratch.md)), and **a later author who assumes a rule
is enforced will write a weaker one.** Node 69 measured the gap: of the hard rules these six contracts state, the
one a capability could reach is already free, and every rule that has actually been broken is defeated by Bash.

Reported by node 69's worker, which wrote the acceptance condition below and scoped it deliberately: **one short
passage in `graph-conventions.md`, and not six edits to the six contracts** — a worker does not need the theory of
the rule binding it, and whether shared text is duplicated across contracts is [Whether the contracts' shared blocks
stay duplicated](50-shared-blocks-stay-duplicated.md)'s question.

**Blockers: none.** It edits `.claude/skills/expedition/graph-conventions.md` and so contends for the code slot with
[Say in the conventions document how the map and its history are written](64-conventions-say-how-the-map-is-written.md),
which is claimed, and with several others.

## Acceptance condition

*Written by node 69's worker.*

`.claude/skills/expedition/graph-conventions.md` gains one new section, under a heading of the author's choosing,
holding all four of the following. It is at most 200 words.

1. It states that a hard rule in a worker contract binds by being read by the agent the contract was given to, and
   that no mechanism in the shipped workflow enforces one.
2. It states the distinction in both directions: a contract says what a worker **may** do, and what a worker
   **can** do is a property of the harness that ran it — and that a clause of the first kind survives a change of
   harness while one of the second kind does not.
3. It states the consequence for anyone writing or editing a contract: a rule that would be false on a harness
   unable to enforce it does not belong in a shipped file, and the remedy for a rule agents read down is a
   better-written rule or a granted exception, never an assumed capability.
4. It cites `nodes/69-explicit-subagent-definitions.md` by name as where the distinction was established.

No file under `.claude/skills/expedition-checker/`, `expedition-grilling/`, `expedition-implementation/`,
`expedition-precondition/`, `expedition-prototype/` or `expedition-research/` is changed by this node — `git diff`
over those six directories comes back empty.

The section is added, and nothing existing in `graph-conventions.md` is deleted or reworded: the file's existing
headings, listed by `grep -n '^#\{1,3\} '`, are all still present afterwards in the same order.

The standing bar for this repo applies as it reaches the checker by its own route.

### The manager's note at filing, not a change to the condition

**Clause 4 asks for a citation by path into `nodes/`, and this document ships in `.claude/skills/expedition/`.**
Node 64's worker established that **no relative markdown link between the two resolves**, and added none for that
reason. The clause says *"cites by name"* rather than *by link*, so it is satisfiable — but whoever claims this
should expect to name the file in backticks rather than link it, and a checker reading it as a link requirement
would be reading in more than the clause says.

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 340](340-add-the-annotation-section-and-what-a-hard-rule-is.md), the merge [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole.
