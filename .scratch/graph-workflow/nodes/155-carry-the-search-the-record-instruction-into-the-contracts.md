# Carry the search-the-record instruction into the five worker contracts

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [What to do about the record's token cost, given what `qmd` turns out to
be](129-what-to-do-about-the-records-token-cost.md)'s worker, and pasted as it wrote it.*

> Add to each worker contract the instruction that the effort's record is searched before any file beyond the
> worker's pointer list is read whole — phrased as a property rather than as a command, so it assumes no toolchain.

**Blockers, in the worker's words:** *"none. The condition below deliberately names no file that does not exist
today, so it does not wait on node 140."*

## Acceptance condition

*Written by node 129's worker. Pasted as it wrote it, and not the manager's.*

> Five files are in scope and no others:
>
> - `.claude/skills/expedition-grilling/SKILL.md`
> - `.claude/skills/expedition-research/SKILL.md`
> - `.claude/skills/expedition-prototype/SKILL.md`
> - `.claude/skills/expedition-precondition/SKILL.md`
> - `.claude/skills/expedition-implementation/SKILL.md`
>
> Each carries a `## What you read` section opening `Read each of these. Do not trust any summary of them.`, followed
> by a bulleted list of pointers and then a line stating that `flags.md` is not the worker's.
>
> 1. **Each of the five gains one passage inside `## What you read`, placed after that bulleted list**, stating all
>    four of the following:
>    a. the bulleted pointer list is what the worker reads whole, and the rest of the effort's record is searched
>       rather than read;
>    b. a worker that needs a fact it cannot place searches the record for it before opening any file whole, and a
>       file of the record that is not on the pointer list is opened because a search led to it;
>    c. the search is narrowed before anything is read — establish which files match, narrow the phrase, then read
>       what matched — because a broad term can return more text than the file it was meant to spare;
>    d. this governs facts held in the record and never the rules the worker is held to: those arrive in the spawn
>       and in the files the pointer list names, and a worker never goes looking for a standard it is to be judged
>       against.
> 2. **The passage names a property and never a command.** The added text contains no occurrence of `grep`, `rg`,
>    `ripgrep`, `ls`, `find`, `awk`, `sed`, or any other executable name, names no tool as required, and describes
>    searching as something the worker's environment provides.
> 3. **Nothing is removed from any of the five pointer lists, and no existing bullet is reworded.** In particular
>    each of the five retains its bullet naming the effort's index of decisions, byte-identical to its current text,
>    and that index remains a file the worker reads whole.
> 4. **The `flags.md` exclusion is untouched and is not reopened.** Each file retains its existing statement that
>    `flags.md` is not the worker's, and the added passage neither licenses searching `flags.md` nor mentions it.
> 5. **`.claude/skills/expedition-checker/SKILL.md` is not modified.** That file instructs its own reader to search
>    the work under review; the added passage must not duplicate, restate or contradict that instruction, and where
>    it needs to relate the two it cites that file by path instead of repeating what it says.
> 6. **The added passage is at most 1,200 bytes in each of the five files.** The five may share wording verbatim.
> 7. **No file outside the five listed in clause 1 is modified.**
>
> The work is also held against the bar.

**The worker's note on its size, in its words:** *"this is a small node. The whole change is one passage of at most
1,200 bytes repeated across five files, and clauses 3 to 7 exist to stop it doing more than that. Its smallness is
the point — it was the cheap half of the package, and it is the half that survived."*

## The manager's note at filing

*Not a change to anything above.*

**Clause 3 is where the human's revert lands.** It requires the index-of-decisions bullet to stay byte-identical and
the index to stay read whole, which is the opposite of what this node's parent originally recommended. The
`DIVERGENCE` and the human's ground for it are on [node 129](129-what-to-do-about-the-records-token-cost.md).
