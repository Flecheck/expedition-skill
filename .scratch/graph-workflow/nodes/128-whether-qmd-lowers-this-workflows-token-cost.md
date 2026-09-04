# Whether `qmd` lowers this workflow's token cost, and what it would cost to adopt

Type: research
Status: claimed

Blocked by: none

## Question

*The human's own request, `verbatim`. **Minted by the manager from their message and not surfaced by any worker.***

> Would it be interesting to add https://github.com/tobi/qmd to lower token usage, to help with all the issues ?
> Maybe create a research node and then grilling

**What to establish**, written by the manager under the constraint that a research node's question fixes what is read
and never what is concluded:

1. **What `qmd` is and what it actually does**, from its own repository rather than from any description of it. Its
   licence, its dependencies, what it needs installed, and whether it runs on this machine.
2. **Where in this workflow it could bear**, against the measured costs this effort already holds rather than against
   a guess: `map.md` at ~19,840 tokens read cold by every worker once per node; `decisions.md` read whole by several
   workers to use four lines; node files that workers report reading in full to use fifteen lines; and the
   five-minute prompt-cache TTL fixed at [node 52](52-token-cost-of-a-workflow.md).
3. **What adopting it would cost**, including the thing that decides it under this effort's own ground rules: whether
   it makes any shipped file depend on a tool being installed. **Ground rule 1 forbids a shipped file assuming this
   repo, this machine, or a toolchain**, and the human has separately directed that the skill not depend on an
   external plugin — recorded on [node 113](113-whether-the-method-skill-instruction-does-any-work.md). A tool the
   workflow requires is a harder dependency than a skill it invokes.
4. **Whether the alternative the human named in the same breath is the same problem or a different one.** Their
   words, `verbatim`: *"Or maybe make the nodes easier to grep, traverse. I don't know if it is nessesary ?"* Establish
   whether these are two routes to one end — less context read per node — or two different problems. That comparison
   is what [node 129](129-what-to-do-about-the-records-token-cost.md) decides on.

**It may read outside the working directory**, and it must: the repository at the URL above, and the record's own
files.

## The manager's note at filing

*Not a change to anything above.*

**The human framed this as *"to help with all the issues"***, and the manager has not read that as naming a
particular set. **What the record actually holds** is a repeated, measured complaint from workers rather than a
suspicion: seven consecutive retrospectives report reading `map.md` whole to act on a handful of lines, and three
report that `decisions.md`'s one-line cap hid the fact that made a node relevant. **That is the evidence this node
has**, and whether `qmd` touches it is exactly what is unestablished.

**The manager has not looked at the URL.** Reading it is this node's work, and a manager's note is capped at context
it already holds.

## What the human added after this node was minted

**Their words, `verbatim`:**

> (qmd is a local seach engine)

***The manager's note.*** This is the only description of the tool anywhere on the graph, and it is **theirs rather
than the repository's** — clause 1 above still asks that what `qmd` is be established from its own repository, and
this line is now the expectation that establishing it should either confirm or correct. **If the repository says
something other than a local search engine, that is a finding rather than a discrepancy to smooth over.**

**What it does to clause 4.** Their alternative — *"make the nodes easier to grep, traverse"* — reads differently
against a search engine than against a compression tool: a search engine and a more greppable record are two ways of
doing the same thing rather than two different problems. **The manager has not concluded that**, and clause 4's
comparison is still what node 129 decides on; the reading is offered as the human's description and not as a result.
