# Ship an `expedition-stop` skill that closes a management session

Type: implementation
Status: open

Blocked by: none

## Question

*Minted by the manager on the human's direction. The question below is the manager's own.*

Closing a management session has been described to the manager in prose each time it happens. The human wants it
invocable instead.

**Their words**, `verbatim`:

> We'll also add a new skill: expedition-stop that can be called in the manager to do that: stops starting work on
> new nodes and just completes the ones that are in-flight, then stop (so I don't have to re-describe it every time).
> Add that note that we don't need a handoff document there, since expedition is designed such that the map holds all
> the information needed for restarting work.

**The second half is a finding this session established rather than a design intention.** A fresh manager ran this
effort's graph cold at the start of the session and reconstructed it from the files; at the session's close it
verified against three live nodes that the three states the manager's contract calls invisible are in fact derivable
from the record. That verification is written into
[map-manager-only.md](../map-manager-only.md)'s `Resume and recovery` item, and its prior text is banked in
[map-history.md](../map-history.md).

## Acceptance condition

***Written by the manager***, this node having been minted by the manager and having no spawning node. **Read back
against the two rules that bind every condition and found to meet both**: it is **self-contained text** — every
demand is in its own words, and the two derivations it requires are written out here rather than pointed at; and it
**does not quantify over the record**, every clause being answerable from the new file and the diff.

The work is a new skill under `.claude/skills/`. Done means every one of the following is true of the finished tree.

1. A file `.claude/skills/expedition-stop/SKILL.md` exists, with the frontmatter shape the sibling
   `expedition-*` skills use, and a description saying it is invoked in an expedition's manager thread to close a
   management session.
2. It states that on invocation the manager **starts no new node** — it claims nothing, spawns no worker for a node
   not already under way, and does not fill a slot a finishing node leaves empty.
3. It states what **finishing the work in flight** means, and it distinguishes the two cases rather than leaving them
   to judgement:
   - work the manager can complete alone — filing a handover that has arrived, resolving a node on it, spawning a
     checker for finished work, and landing work the human has already approved — **is completed**;
   - work that cannot complete without the human — a node at a gate, and a worker holding an unanswered question —
     **is left where it stands**, recorded, and named in the closing report.
4. It states that **no handoff document is written**, and gives the reason as a property rather than an assertion:
   the record already carries what a fresh manager needs. It states the three derivations that make that true —
   a node at a gate is `claimed` with a checker's outcome recorded and no gate outcome; a worker holding an
   unanswered question is `claimed` with a question recorded and no answer under it; a parked node is `open` with a
   non-empty interview — and that a live worktree is discovered from the version control system rather than recorded.
5. It states that whatever routes a manager to its running agents **does not survive the session**, that this costs
   nothing, and that a fresh manager replaces an unresumable attempt by the ordinary route, replaying what the human
   has already said and marking it settled so they are never asked twice.
6. It states what the closing report carries: what landed, what resolved, what is in flight and in which of the two
   states of clause 3, and what is outstanding for the human.
7. **It assumes no particular repository, machine, or toolchain**, names no plugin, requires no skill to be
   invocable, and names no command. Where it must refer to discovering a worktree or a commit it states the property
   and not the command.
8. It addresses the manager throughout and never the human, and nothing in it tells any agent to address the human.
9. It is at most 4,000 bytes.
10. No file outside `.claude/skills/expedition-stop/` is created or modified.
11. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**The manager did not write the skill itself, though the human asked for it during a session it had been told to
close.** A shipped file lands through an implementation node with a checker and a gate; a manager writing one
directly is the failure this workflow exists to prevent. **Minting is not starting**, so filing this node does not
breach the instruction to start no new work. If the human would rather have it immediately, that is one word and this
node is where the record of the departure would go.

**Clause 4's three derivations are the manager's own text and are the one part of this condition a later reader
should check hardest**, since they assert a property of every node file rather than of this one.
