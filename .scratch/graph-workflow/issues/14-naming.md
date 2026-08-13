# Naming the workflow and its vocabulary

Type: grilling
Status: open
Blocked by: 07

## Question

What is this workflow called, and what are its core terms?

Use the `/naming` skill. Terms in play, currently used loosely and inconsistently:

- The **workflow** itself — invoked as a slash command, so the name is user-facing. The repo is `graph-agent`, which may or may not be the name.
- The **graph**, and a single element of it: node? issue? ticket? Wayfinder says ticket; the user has said issue and node interchangeably.
- The **manager thread** — the user's phrase was "management main ai thread". Firstmate calls its equivalent the first mate, and the human the captain.
- The **subagent** working one element — the user said subtask, which conflates the work with the worker. Firstmate says crewmate.
- The **revision** relationship, whatever [Revision semantics](06-revision-semantics.md) decides it is.
- The **write lock** on code modification.

Now unblocked. [Node type taxonomy](07-node-type-taxonomy.md) fixed the kinds but deliberately did not fix their labels, so the terms it hands over are:

- The five kinds: `research`, `prototype`, `grilling`, `task`, `implementation` — four inherited from wayfinder, one new. Whether `implementation` is the right user-facing word is open.
- The **reviewer** — the independent agent that checks an implementation before it resolves. Not a node type, so it needs a word that does not read like one.
- The **acceptance condition** on an implementation node.
- The **flagged assumption** an implementer leaves behind when it decides a small ambiguity itself.

Added by [Relay protocol](08-relay-protocol.md), which named several things provisionally while resolving and deliberately did not settle any of them:

- The **relay** itself — the channel between subagent and human, and the payload that travels on it. "Relay" is inherited from firstmate, where it meant something else entirely (external channels like X and Discord), which this effort has ruled out of scope. Reusing the word may be a mistake.
- **Park** — a node the human deferred, which has stored its progress and gone back to `open` carrying banked answers.
- **Attempt** — one spawned agent instance working a node, of which there may be up to three before escalation. Distinct from the node, which outlives it.
- **Banked answer** — a human answer already paid for and stored, awaiting a fresh agent.
- **Delegated flag** — the record that the human said "you decide" and the subagent answered instead.
- **Manager note** — the manager's own annotation on a relayed question, drawn only from context it already holds.
- **Provenance** — whether a recorded answer is the human's verbatim words or a manager paraphrase.

Blocked on the taxonomy: naming the node types before knowing what the types are would be backwards.

Deliberately not started yet: no `CONTEXT.md` glossary exists for this repo. Per the domain-modeling skill, create it lazily when the first term is genuinely resolved — which is this issue. Writing it earlier would only have to be rewritten.
