# Carry the search-the-record instruction into the five worker contracts

Type: implementation
Status: superseded
Superseded by: 333

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

## Amendment, 2026-09-24

*Written by [node 290](290-rewrite-the-research-contract-as-the-pilot.md)'s worker and filed by the manager, after that node's work landed as commit `4068519`. Every word of each replacement is fixed by that commit: it quotes the research contract's after-text. The minting author's condition above is left as it was, and these replacements take the place of the clauses they name.*

Node 290's worker searched every open node's `## Acceptance condition` for quoted spans of the research contract's before-text, for mentions of the file, and for each piece of wording its rewrite removed or replaced. The full list of handles is on node 290 under `### Re-pointing duty` and `### Correction round 1`.

- **The sentence before its clauses.** Replace it with: "Each carries a `## What you read` section opening `Read each of these. Do not trust any summary of them.`, or, in `.claude/skills/expedition-research/SKILL.md`, `Read each of the following. Do not trust any summary of them.`, followed by a bulleted list of pointers and then a line stating that `flags.md` is not the worker's." Between the list and the `flags.md` line, the research file also holds "You may read outside the working directory." The before-text had the same shape. Clauses 1, 3 and 4 still hold as written. The decisions bullet and the `flags.md` statement are still there.

## Flags

`155.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 290](290-rewrite-the-research-contract-as-the-pilot.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `4068519`.

## Amendment, 2026-09-25 (from node 294)

*Written by [node 294](294-rewrite-the-implementation-contract.md)'s worker and filed by the manager, after that node's work landed as commit `724c361`. Every word of the replacement is fixed by that commit: it quotes `expedition-implementation/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 294's worker's search is on node 294 under `RE-POINTING SEARCH`.*

- **The sentence before its clauses**, as amended by node 290. Replace it with: "Each carries a `## What you read` section opening `Read each of these. Do not trust any summary of them.`, or, in `.claude/skills/expedition-research/SKILL.md` and `.claude/skills/expedition-implementation/SKILL.md`, `Read each of the following. Do not trust any summary of them.`, followed by a bulleted list of pointers and then a line stating that `flags.md` is not the worker's."

*The manager's note:* the worker reported that in the implementation file the `flags.md` line ("Leave `flags.md` unread. It is not yours.") follows the list directly, and that the decisions bullet is byte-identical, so clauses 1, 3 and 4 still hold.

`155.2` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 294](294-rewrite-the-implementation-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `724c361`.

## Amendment, 2026-09-25 (from node 291)

*Written by [node 291](291-rewrite-the-grilling-contract.md)'s worker and filed by the manager, after that node's work landed as commit `0a3e68b`. Every word of the replacement is fixed by that commit: it quotes `expedition-grilling/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 291's worker's search is on node 291 under `RE-POINTING SEARCH`.*

- **The sentence before its clauses**, as amended by node 294. Replace it with: "Each carries a `## What you read` section opening `Read each of these. Do not trust any summary of them.`, or, in `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md` and `.claude/skills/expedition-grilling/SKILL.md`, `Read each of the following. Do not trust any summary of them.`, followed by a bulleted list of pointers and then a line stating that `flags.md` is not the worker's."

`155.3` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 291](291-rewrite-the-grilling-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `0a3e68b`.

## Amendment, 2026-09-25 (from node 292)

*Written by [node 292](292-rewrite-the-precondition-contract.md)'s worker and filed by the manager, after that node's work landed as commit `ede2c76`. Every word of the replacement is fixed by that commit: it quotes `expedition-precondition/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 292's worker's search is on node 292 under `RE-POINTING SEARCH` and its addendum.*

- **The sentence before its clauses**, as amended by node 291. In the list of files whose `## What you read` section opens `Read each of the following. Do not trust any summary of them.`, add `.claude/skills/expedition-precondition/SKILL.md`.

*The manager's note:* the worker reported that in the precondition file the `flags.md` line follows the list directly, that the list now has four bullets because the node-file bullet was split in two, and that the decisions bullet is byte-identical, so clauses 1, 3 and 4 still hold.

`155.4` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 292](292-rewrite-the-precondition-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `ede2c76`.

## Amendment, 2026-09-25 (from node 293)

*Written by [node 293](293-rewrite-the-prototype-contract.md)'s worker and filed by the manager, after that node's work landed as commit `6d26be1`. Every word of the replacement is fixed by that commit: it quotes `expedition-prototype/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 293's worker's search is on node 293 under `RE-POINTING SEARCH`.*

- **The sentence before its clauses**, as amended by node 291. In the list of files whose `## What you read` section opens `Read each of the following. Do not trust any summary of them.`, add `.claude/skills/expedition-prototype/SKILL.md`.

*The manager's note:* the worker reported that in the prototype file the `flags.md` line ("Leave `flags.md` unread. It is not yours.") follows the list directly, and that the decisions bullet ("`decisions.md` — the sections the spawn names") is byte-identical, so clauses 1, 3 and 4 still hold.

`155.5` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 293](293-rewrite-the-prototype-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `6d26be1`.

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 333](333-land-the-open-repairs-to-the-five-worker-contracts-in-one-change.md), the merge [node 329](329-group-the-open-nodes-against-the-worker-contracts.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole.
