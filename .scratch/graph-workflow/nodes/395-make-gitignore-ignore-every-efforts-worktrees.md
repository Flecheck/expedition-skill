# Make `.gitignore` ignore every effort's worktrees directory

Type: implementation
Status: resolved
Blocked by: 394

## Question

This lets a later effort in this repository cut implementation worktrees without first editing `.gitignore`, as the root `CLAUDE.md` describes. Today `.gitignore` ignores only `.scratch/graph-workflow/worktrees/`. Should it ignore `.scratch/*/worktrees/` instead?

*Reported by [node 394](394-a-repo-claude-md-so-the-next-effort-does-not-start-cold.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none". The manager added node 394 as a blocker, because this condition edits the `CLAUDE.md` that node 394 creates.*

## Acceptance condition

*Authored by node 394's worker and filed by the manager.*

> The work edits `.gitignore` and `CLAUDE.md` only. Scope came from no search: the named places are the work.
> 1. `.gitignore` ignores `.scratch/*/worktrees/`, and `git check-ignore .scratch/anyname/worktrees/x` prints that path.
> 2. `.gitignore` still ignores `.scratch/graph-workflow/worktrees/`.
> 3. The sentence in `CLAUDE.md`'s `## The worktree of an implementation node` that tells an effort to check `.gitignore` before its first worktree, and to add an entry where none covers it, is removed. The bullet still states that `.gitignore` ignores that path.
> 4. `CLAUDE.md` is at most 900 words by `wc -w CLAUDE.md`.
> 5. The working tree meets the bar.

## Answer

`.gitignore` replaces `.scratch/graph-workflow/worktrees/` with `.scratch/*/worktrees/`, so any effort's worktrees are ignored; CLAUDE.md drops its "check `.gitignore` before your first worktree" sentence.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `13bb6ed9c`. Flags 395.1 settle at the node closing report.

## Handover, attempt 1

*Pasted as the worker handed it back, 2026-10-07.*

`````
HANDOVER:      Make `.gitignore` ignore every effort's worktrees directory

ANSWER:        `.gitignore`'s third entry, `.scratch/graph-workflow/worktrees/`, is replaced by `.scratch/*/worktrees/`, so every effort's worktrees directory is ignored. Its comment now says "one directory per effort" and "whichever effort cut them", and it still cites `map-manager-only.md`, "How the worktree is made". The glob covers `.scratch/graph-workflow/worktrees/`, so clause 2 holds without a separate literal entry: `git check-ignore -v .scratch/graph-workflow/worktrees/` reports `.gitignore:19:.scratch/*/worktrees/`. `git check-ignore .scratch/anyname/worktrees/x` prints that path. The pattern is anchored at the repo root and `*` does not cross `/`, so the doubled path `.scratch/graph-workflow/.scratch/graph-workflow/worktrees/x` is still not ignored (checked, exit 1). This keeps true `map-manager-only.md`'s statement under *How the worktree is made* that `.gitignore` does not match the doubled path. The two older entries, `.worktrees/` and `.claude/worktrees/`, are unchanged. In root `CLAUDE.md`, under `## The worktree of an implementation node`, the bullet now reads only "`.gitignore` ignores that path." The sentence telling an effort to check `.gitignore` before its first worktree, and to add an entry where none covers it, is removed. `wc -w CLAUDE.md` = 831. Bar: the repo's root `CLAUDE.md` `## Commands` says there are no build, test, format or CI commands. That agrees with `map-implementation-rules.md`'s recorded copy, so the bar here is the standards plus the condition.

INDEX LINE:    `.gitignore` replaces `.scratch/graph-workflow/worktrees/` with `.scratch/*/worktrees/`, so any effort's worktrees are ignored; CLAUDE.md drops its "check `.gitignore` before your first worktree" sentence.

FLAGS:         ASSUMPTION — Clause 2 says `.gitignore` "still ignores" `.scratch/graph-workflow/worktrees/`. I read that as a property of what is ignored, not as a requirement to keep the literal line. So I replaced the literal entry with the glob instead of adding the glob beside it, which would have been redundant. `git check-ignore -v` shows that the glob covers the path. If the human wants the literal line kept as well, it is a one-line addition.
               Index sentence: The literal `.scratch/graph-workflow/worktrees/` ignore entry was replaced, not supplemented, by `.scratch/*/worktrees/`, which covers it.

NEW NODES:     none

INVALIDATIONS: Node 269 ("Ignore the new worktree path") is extended. The entry it added is generalised from graph-workflow's directory to every effort's. Node 394 is narrowed. Its answer says the worktree section tells an effort to check and add a `.gitignore` entry, and that sentence is now gone. Its statement that `.gitignore` "today ignores only `.scratch/graph-workflow/worktrees/`" is no longer true. Not a node, but a record copy now stale: `map-implementation-rules.md`'s bar-commands paragraph says `.gitignore` "ignores `.worktrees/`, `.claude/worktrees/` and `.scratch/graph-workflow/worktrees/`". The third item is now `.scratch/*/worktrees/`. The manager should repair that copy. I did not edit it, because the condition limits the work to `.gitignore` and `CLAUDE.md`. `map-manager-only.md`'s doubled-path statement remains true (verified above).

CONDITIONS:    Searched for `gitignore`, `worktrees/`, "covers that effort" and "add one where none". No other node is open or claimed: the status counts are 305 resolved, 72 superseded, 16 out-of-scope and 1 claimed (this one), derived 2026-10-07, for scale only. So no open condition or question is affected. For resolved nodes, I narrowed the search to `.scratch/graph-workflow/worktrees/` and "ignores only". The relevant matches are 269 and 394, reported above. Other "ignores only" hits (11, 13, 116) concern other repos or older states and are not changed.

MISSING FROM MAP: none

GATE PAYLOAD:  No checker findings yet. Paths touched, in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/395-gitignore: `.gitignore`, `CLAUDE.md`. Record file left in the older form: `.scratch/graph-workflow/map-implementation-rules.md` (bar-commands paragraph lists the old literal entry). Proposed commit message:
               "Ignore every effort's worktrees directory with .scratch/*/worktrees/ and drop CLAUDE.md's check-before-first-worktree sentence

               Node: graph-workflow/395"

RETROSPECTIVE:
1. What I had to hunt for: which nodes are open. There is no list. I first tried a status-line grep loop and got nothing, then counted `Status:` values to learn that only 395 is claimed. I also had to work out whether the glob would start matching the doubled path that map-manager-only.md says is not matched, and I settled that by running `git check-ignore`.
   - `open-node-list-re-derived-by-hand`: carried by 2 earlier retrospectives (214, 388), derived 2026-10-07, for scale only.
2. What arrived that this node did not need: almost all of map.md and map-implementation-rules.md. The node needed only the bar paragraph and the standards list. The spawn's `.gitignore` and `CLAUDE.md` pointers plus the bar line would have been enough.
   - `map-read-whole-for-a-few-items`: carried by 20 earlier retrospectives (135, 178, 185, 205, 214, 220, 284, 317, 382, 386, 387, 388, 389, 390, 391, 392, 393, 394, 40, 41), derived 2026-10-07, for scale only.
   - `rules-file-read-whole-for-one-section`: carried by 16 earlier retrospectives across 15 node files (178, 185, 214, 220, 317, 382, 386, 387, 388, 390, 391, 392, 393, 40, 41), derived 2026-10-07, for scale only.
   - `record-is-not-mechanically-scannable`: a search for `gitignore` across resolved nodes matched about 140 files, because the word appears in passing everywhere. It is carried by 6 earlier retrospectives (178, 212, 220, and others), derived 2026-10-07, for scale only.
3. What would have made this node easier: a spawn line saying "no other node is open". Also the contract could state, for a condition clause like "still ignores X", whether X must remain a literal entry.
4. Stale or contradictory reading: `map-implementation-rules.md`'s bar paragraph enumerates `.gitignore`'s entries. That copy goes stale with every `.gitignore` change, and it is stale now.
   - `record-copy-of-repo-file-goes-stale`: new name, carried by no earlier retrospective.
`````

## Flags

`395.1` `ASSUMPTION` **· settled** — The literal ignore entry was replaced, not supplemented, by the glob. *(The worker's full text is under its handover's `FLAGS`.)*

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-10-07. A fresh checker; the condition reached it as a verbatim copy in `$TMPDIR/check395.md`. The node's one flag, 395.1, reached it as text.*

> PASS
>
> Acceptance condition, one line per part:
> - Preamble (edits `.gitignore` and `CLAUDE.md` only): `git status --porcelain --untracked-files=all` in the worktree lists only ` M .gitignore` and ` M CLAUDE.md`. The diff is 7 insertions and 7 deletions across those two files. No search is recorded in the condition ("Scope came from no search"), so I had no recorded command to re-run.
> - Part 1: `.gitignore` now ends with the entry `.scratch/*/worktrees/`. `git check-ignore .scratch/anyname/worktrees/x` printed `.scratch/anyname/worktrees/x` with rc=0.
> - Part 2: `git check-ignore .scratch/graph-workflow/worktrees/x .scratch/graph-workflow/worktrees/` printed both paths with rc=0. `git check-ignore -v .scratch/graph-workflow/worktrees/395-gitignore` attributes the match to `.gitignore:19:.scratch/*/worktrees/`.
> - Part 3: `grep -n "Before an effort's first worktree\|add one where none" CLAUDE.md` matched nothing (rc=1). `grep -n "ignores that path" CLAUDE.md` matched line 48, ``- `.gitignore` ignores that path.``, which is under `## The worktree of an implementation node`. The diff shows that the bullet lost only its second and third sentences.
> - Part 4: `wc -w CLAUDE.md` gives 831, which is at most 900.
> - Part 5 (the bar): see below.
>
> The bar:
> - Commands: the root `CLAUDE.md` `## Commands` says the repo has no build, no tests, no formatter and no CI, so there is no command to run. The copy in the rules file agrees. I also ran `git diff --check`, which printed nothing (rc=0).
> - Standards: I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`, under `## What the work is held against`. They are `/coding-principles` and `/naming`, the glossary `_Avoid_` lines, the effort's ground rules and six writing rules (taken from the spawn text), `graph-conventions.md`, and `/writing-for-agents`. No reviewing skill is named, so I ran none and held the work against these standards by hand.
> - Standards that bore on this work: the glossary `_Avoid_` lines, the six writing rules / `/writing-for-agents` (for the edited `.gitignore` comment and the `CLAUDE.md` bullet), and ground rule 4. `graph-conventions.md` says nothing about `.gitignore` or worktrees, so it did not bear.
> - `_Avoid_` result: I grepped the `_Avoid_` lines for the words in the changed lines. The only hit is `review` (line 290, refused as a name for the gate). The comment's "so that a review can see the diff" already stood before this change, and it uses "review" for the human's act, which the refusal's own parenthetical allows. Not a finding.
> - Writing-rules result: the opening comment line "The current path, one directory per effort." is a label phrase. It keeps the form of the earlier "The current path." I judged it a comment label rather than a breach of "Write every sentence grammatically". Not a finding.
> - Did the work move a standard: no. Neither changed path holds a standard I hold the work against. The `CLAUDE.md` edit removes a procedural instruction and leaves the `## Standards` list and the writing rules unchanged.
>
> Under the rules file's rule, I read the changed paths as the work. Neither path is a record file, a status line, `decisions.md` or `flags.md`.
>
> Flags, checked after the outcome:
> - 395.1 is true of the work. The diff removes `-.scratch/graph-workflow/worktrees/` and adds `+.scratch/*/worktrees/`, and no literal entry for that path remains in `.gitignore`.
>
> No QUESTIONS, no NOT COVERED. I wrote no temporary files.
>
> Paths: /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/395-gitignore/.gitignore, /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/395-gitignore/CLAUDE.md

*The manager's note:* the checker handed back no question and no raise, covered every clause, and found the flag true. The gate is taken under the standing yes, below.


### Gate — approve, `standing yes`, 2026-10-07

Taken under the standing yes recorded in `map-manager-only.md`, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies. This settles none of the node's flags; they settle at the node closing report.

*The manager's note, 2026-10-07:* flags 395.1 settle at the node closing report that closes this node, which names its gate as taken under the standing yes.
