# The worktree route's create command names a relative path and never says from where

Type: implementation
Status: resolved

Blocked by: none

## Answer

The worktree route's create command now runs as `git -C <repo root> worktree add …`, so it gives the same ignored path from any working directory; the writability check is anchored the same way.

*The manager's note:* landed as commit `3679741c0`. The gate was put to the human once and answered with a correction round fixing two factual sentences; run 2's `PASS` was taken under the standing yes. Flags 284.1 to 284.4 settled at the human's gate.

## Question

*Surfaced by [node 281](281-map-repeats-the-false-no-override-claim-about-the-worktree-route.md)'s worker, and
pasted as it wrote it.*

> The Create bullet of `map-manager-only.md`'s *How the worktree is made* gives `git worktree add -b
> worktree-<NN>-<name> .scratch/graph-workflow/worktrees/<NN>-<name>` and says the manager works *"from the main
> tree"*. **"From the main tree" names the tree, not the working directory** — so a manager whose cwd is
> `.scratch/graph-workflow/` is still in the main tree and gets a **doubled** path. That is what happened for this
> node and for node 267: both worktrees are at
> `.scratch/graph-workflow/.scratch/graph-workflow/worktrees/<NN>-<name>`. **The doubled path escapes
> `.gitignore`** — the rule node 269 landed is anchored at the repo root and does not match it — so `git status` at
> the root shows `?? .scratch/graph-workflow/.scratch/`, measured, and `git check-ignore` returns non-matching. **Two
> entire worktrees are currently sitting untracked-and-unignored in the repository.** Should the bullet state an
> absolute path, or state the directory the command is run from?

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 281's worker. Pasted as it wrote it, and not the manager's.*

> Done when all four hold.
>
> **1.** `map-manager-only.md`'s *How the worktree is made* Create bullet states the worktree path in a form that
> resolves to `<repo root>/.scratch/graph-workflow/worktrees/<NN>-<name>` **whatever working directory the command
> is issued from** — either by giving an absolute path or by naming the working directory the command must be run
> from as part of the command.
>
> **2.** Whatever it now states, `git check-ignore` matches the resulting path against the repository's
> `.gitignore` — that is, **the created worktree is ignored**.
>
> **3.** Any wording the change displaces that states a rule currently binding is **replaced**, not struck in place,
> and its existing text is appended verbatim to `.scratch/graph-workflow/map-history.md` under a heading mirroring
> the section it came from, struck-through text staying struck through; `map-history.md` gains text and loses none.
>
> **4.** No file outside `map-manager-only.md` and `map-history.md` is modified; nothing is written in
> `decisions.md` or `flags.md`; no node's status line is touched. The bar applies: this repository has no build, no
> tests, no formatter and no CI, which is a complete bar on its remaining half, so what binds is the project
> criteria, `CONTEXT.md`'s `_Avoid_` lines, `graph-conventions.md`, `/writing-for-agents`, `/coding-principles`,
> `/naming`, and this effort's ground rules and four standing rules for writing.

## The manager's note at filing

*Not a change to anything above.*

**The manager caused this and it was live in the repository when the worker found it.** Flag `281.2` holds the
manager's half: it ran `git worktree add` with a relative path from a cwd that was not the repository root, then
wrote the non-existent path into the spawn, costing that worker two tool calls before `git worktree list` told it
where it actually was.

**One consequence the worker could not see, measured by the manager after the report.** The manager's periodic
record-state commit is `git add .scratch/graph-workflow`, **and the doubled path is underneath it** — `git add
--dry-run` staged both worktrees. **The manager would have committed two entire working trees into the record.**
That is closed for now by a local-only `.git/info/exclude` entry, which touches no tracked file; **this node is what
stops it recurring.**

**Clause 2 is the load-bearing one and it is testable rather than arguable**: whatever the bullet says, the path it
produces must be one `git check-ignore` matches. A claiming worker should run that command rather than reason about
the anchor.

**The manager's own conduct has changed already** — it creates worktrees with an absolute path — which is the
ordinary order on this effort and is also the thing that makes a node like this feel like ceremony. That tension is
[node 283](283-what-makes-a-change-to-a-record-file-a-node-rather-than-bookkeeping.md)'s subject and is in front of
the human.

## A second author's condition for the same defect

***Filed by the manager, not merged.*** [Node
267](267-the-priority-list-does-not-say-the-human-must-always-have-something-to-do.md)'s worker found this
independently, an hour after node 281's worker, and wrote its own condition. **The manager has not folded the two
together** — that would be authoring a condition out of two agents' text — but this one **adds two demands the
condition above lacks**, and whoever claims this node should have them:

> **1.** … `map.md`'s paragraph beginning *"An implementation node's worktree is made with plain git"* states the
> same path in the same form.
>
> **2.** `.gitignore` ignores the path any worktree created by that route occupies. … Verified by `git check-ignore
> -v` against a path under the route's location, **which must report `.gitignore` and not `.git/info/exclude`.**
>
> **3.** Nothing in the work depends on `.git/info/exclude`, and the work neither reads nor writes that file.
>
> **4.** No existing git worktree is moved, removed or renamed, and no branch is created, deleted or checked out.

**Clause 2's second half is the sharper demand and it is aimed at the manager's own containment.** The local
exclude the manager added closes the hole on this machine only; **it is untracked and does not survive a clone.**
Node 281's worker's condition would be satisfied by a path the local exclude happens to cover; this one would not.

**Clause 4 matters because two live worktrees sit at the doubled path right now**, one of them holding finished work
at a gate. A worker repairing the *rule* must not try to repair the *directories*.

**The scope differs too**: the condition above is two files, this one is three — it adds `.gitignore`. **Whoever
claims this node picks, and says which it took.**

## The manager's note, 2026-09-23

*The manager's own note, not an amendment.* This node's `## Acceptance condition` quotes the words "four standing rules for writing". Since [node 289](289-a-plain-english-and-compaction-pass-over-the-shipped-files.md), `map-implementation-rules.md` holds five standing rules for writing and says "five" where it said "four". Found by the manager's search of the open conditions for "four standing rules". The clause must be re-pointed before this node is claimed.

## Amendment, 2026-09-27 (from node 56)

*Written by [node 56](56-ship-the-glossary-into-the-skill-set.md)'s worker under its `CONDITIONS`, and filed by the manager. Pasted as it wrote it.*

- Node 284 (open, unclaimed): in its bar sentence, "`CONTEXT.md`'s `_Avoid_` lines" should read "`.claude/skills/expedition/glossary.md`'s `_Avoid_` lines". Same source for the path.

## Amendment, 2026-09-28 (from node 354)

*Written by [node 354](354-add-the-sixth-standing-rule-for-writing.md)'s worker under its `CONDITIONS`, and filed by the manager. Pasted as it wrote it. It binds once node 354 lands.*

- Node 284 (open, unclaimed). Clause 4's bar sentence says "this effort's ground rules and four standing rules for writing". The manager's note of 2026-09-23 on that node already records that this is stale. Replacement for that phrase: "this effort's ground rules and six standing rules for writing". It is fixed by the same landed work.

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      The worktree route's create command names a relative path and never says from where

CONDITION TAKEN: the first one, node 281's worker's, with the two filed amendments applied to clause 4's bar sentence (node 56's amendment and node 354's amendment). I did not take node 267's worker's condition. Its clause 1 requires "`map.md`'s paragraph beginning *"An implementation node's worktree is made with plain git"*" to state the path. `map.md` no longer holds that paragraph. Node 345 moved it verbatim to `map-implementation-rules.md`, and `map.md` now only points there ("how an implementation node's worktree is made and reached is in map-implementation-rules.md"). So that clause cannot be met as written, and taking that condition would have meant a trigger-1 raise. Its other demands are met by this work anyway, and the evidence is in the GATE PAYLOAD. Clause 2: `git check-ignore -v` reports `.gitignore:19`, not `.git/info/exclude`. Clause 4: no worktree or branch was moved, created, deleted or checked out. On clause 3: the work does not depend on `.git/info/exclude` and wrote nothing to it. I did read it once, read-only, while checking the manager's notes. It now holds only git's default comment lines, and the manager's doubled-path entry is gone.

The clause text I worked to, with both amendments applied. Hand the checker this:

> Done when all four hold.
>
> **1.** `map-manager-only.md`'s *How the worktree is made* Create bullet states the worktree path in a form that resolves to `<repo root>/.scratch/graph-workflow/worktrees/<NN>-<name>` **whatever working directory the command is issued from** — either by giving an absolute path or by naming the working directory the command must be run from as part of the command.
>
> **2.** Whatever it now states, `git check-ignore` matches the resulting path against the repository's `.gitignore` — that is, **the created worktree is ignored**.
>
> **3.** Any wording the change displaces that states a rule currently binding is **replaced**, not struck in place, and its existing text is appended verbatim to `.scratch/graph-workflow/map-history.md` under a heading mirroring the section it came from, struck-through text staying struck through; `map-history.md` gains text and loses none.
>
> **4.** No file outside `map-manager-only.md` and `map-history.md` is modified; nothing is written in `decisions.md` or `flags.md`; no node's status line is touched. The bar applies: this repository has no build, no tests, no formatter and no CI, which is a complete bar on its remaining half, so what binds is the project criteria, `.claude/skills/expedition/glossary.md`'s `_Avoid_` lines, `graph-conventions.md`, `/writing-for-agents`, `/coding-principles`, `/naming`, and this effort's ground rules and six standing rules for writing.

ANSWER:
The Create bullet under *How the worktree is made* in `map-manager-only.md` now gives the command as `git -C <repo root> worktree add -b worktree-<NN>-<name> .scratch/graph-workflow/worktrees/<NN>-<name>`. `<repo root>` is defined there as the main tree's absolute path, which is the first path `git worktree list` prints. Git resolves the relative path argument against the `-C` directory. So the command creates the worktree at `<repo root>/.scratch/graph-workflow/worktrees/<NN>-<name>` whatever the shell's working directory is. I chose `-C` over an absolute path argument because `-C` also pins the HEAD the worktree lands on to the main tree's HEAD. A cwd inside a linked worktree would otherwise change both the path and the base. The old bullet's "from the main tree" was dropped, because it named the tree and not the directory. The bullet keeps the trigger as part of the rule, as the map's admission test allows. Without `-C`, a cwd below the repository root produces a doubled path such as `.scratch/graph-workflow/.scratch/graph-workflow/worktrees/<NN>-<name>`. `.gitignore` does not match that path, so the manager's commit of `.scratch/graph-workflow` would stage the whole worktree.

The same section's writability check had the same defect, so it also changed: `test -w .scratch/graph-workflow` became `test -w <repo root>/.scratch/graph-workflow`. From the wrong cwd, the relative form would report a false failure and send a needless raise to the human.

Both displaced passages are appended byte-identical to `map-history.md` under a new section, "Superseded from `map-manager-only.md` at node 284 — the create command's relative path, and the writability check's". Each passage has its own `### From *How the worktree is made* — …` heading.

`.gitignore` is unchanged. Its anchored rule `.scratch/graph-workflow/worktrees/` already matches the path the new command produces. `git check-ignore -v` reports `.gitignore:19` for that path, and returns no match for the doubled path. Making `.gitignore` also catch doubled paths would be a separate, defensive change that neither condition requires.

Left unchanged: the paragraph in `map-implementation-rules.md` beginning "An implementation node's worktree is made with plain git". It still says the manager creates the worktree "from the main tree with `git worktree add`, at `.scratch/graph-workflow/worktrees/<NN>-<name>`". That is a true statement of where the worktree goes, read by workers and not used as a command, and it points at the manager's file for the full route. Clause 4 also bars touching it. Also left unchanged: the Base bullet's "the manager's current `HEAD`". With `-C <repo root>` the base is the main tree's HEAD, which is the manager's HEAD as long as the manager stands in the main tree, as the landing policy assumes.

INDEX LINE:    The worktree route's create command now runs as `git -C <repo root> worktree add …`, so it gives the same ignored path from any working directory; the writability check is anchored the same way.

FLAGS:
ASSUMPTION: Node prose: The node held two conditions and left the pick to its worker. I took node 281's worker's condition, two files, with the amendments from nodes 56 and 354 applied to its bar sentence. Node 267's worker's clause 1 names a paragraph in `map.md` that node 345 moved to `map-implementation-rules.md`, so it cannot be met as written. Its `.gitignore` demand (check-ignore reports `.gitignore`, not `.git/info/exclude`) and its no-worktree-touched demand both hold for this work anyway, and I verified both. Index: Node 284 took node 281's worker's condition over node 267's, whose clause 1 names a `map.md` paragraph that node 345 moved to the rules file.
ASSUMPTION: Node prose: Beyond the Create bullet the condition names, I also anchored the same section's `test -w .scratch/graph-workflow` check at `<repo root>`. It is the same defect in the same section, a relative path with no stated cwd. From the wrong directory it gives a false failure that the bullet says to raise to the human. Its old text went to `map-history.md` under clause 3's procedure. Index: Node 284 also anchored the worktree route's `test -w` writability check at `<repo root>`, the same relative-path defect one bullet below the Create command.

NEW NODES:     none

INVALIDATIONS: Node 265 (extension): its route's create command `git worktree add -b worktree-<NN>-<name> .scratch/graph-workflow/worktrees/<NN>-<name>` now carries `-C <repo root>`. Its `decisions.md` line stays true as a statement of location. Node 281: none. Its `map.md` sentence is untouched.

CONDITIONS:    The 18 open or claimed node files (counted 2026-10-04, not authoritative, for scale only) were searched, conditions and questions, for: "from the main tree", "git worktree add", "test -w", "worktrees/<NN>", "How the worktree is made", "Create bullet", "relative path", "doubled". Only node 284 itself matched, plus node 384 on "relative path", where it is about repo-relative paths in conditions and unrelated. No replacements, and no open question changed.

MISSING FROM MAP: The second condition and the spawn both point at a `map.md` paragraph about the worktree. `map.md` now only points at `map-implementation-rules.md` for it. I found that from `map.md`'s own pointer line ("how an implementation node's worktree is made and reached is in map-implementation-rules.md"). Otherwise none.

GATE PAYLOAD:
Checker findings: none yet (first run).
Bar: the repo has no build, tests, formatter or CI. I looked for a manifest, task runner or CI config and found none, which matches `map-implementation-rules.md`'s record of the bar's commands. No difference to report. Graph-conventions check 11 run over the touched files: the pre-change `map-history.md` is a byte-exact prefix of the new one, and all 8 removed lines of `map-manager-only.md` appear byte-identically in the appended text. Check 10 is not applicable, since the passage is not under a `## Notes`.
Verification:
- `git -C /home/mathieu/projects/graph-agent check-ignore -v .scratch/graph-workflow/worktrees/999-example` gives `.gitignore:19:.scratch/graph-workflow/worktrees/` (also for `284-worktree-path`, and the same inside this worktree). The doubled path gives no match, exit 1.
- In a scratch repo under `$TMPDIR` with this repo's `.gitignore`, run from cwd `.scratch/graph-workflow`: `git -C "$(git worktree list | head -1 | awk '{print $1}')" worktree add -b worktree-1-x .scratch/graph-workflow/worktrees/1-x` created `<root>/.scratch/graph-workflow/worktrees/1-x`, and check-ignore reported `.gitignore:19`. The scratch repo was then deleted.
- No worktree or branch was created in this repository.
- `git worktree list` (2026-10-04): main, `220-retro-derivation`, `284-worktree-path`. The doubled worktrees no longer exist, which confirms the manager's note.
Paths touched:
- /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/284-worktree-path/.scratch/graph-workflow/map-manager-only.md
- /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/284-worktree-path/.scratch/graph-workflow/map-history.md
Proposed commit message:
```
Worktree route: run the create command with git -C <repo root>

The Create bullet gave a path relative to the shell's working directory, so a
manager whose cwd was below the repository root created worktrees at a doubled
path that .gitignore does not match. The command now runs as
git -C <repo root> worktree add ..., and the writability check is anchored
the same way. The displaced text is appended to map-history.md.

Node: graph-workflow/284
```
Method-skill parts skipped: none. `/writing-for-agents` was read and applied, and it has no conflicting part here.

Manager's notes checked:
- Node 270 resolved "no script" on 2026-10-04: confirmed in `decisions.md` and in the node's interview dates.
- This worktree was made at an absolute path: confirmed by `git worktree list`.
- The doubled worktrees are gone: confirmed, and `.scratch/graph-workflow/.scratch` does not exist.

RETROSPECTIVE:
1. What I had to hunt for: where the second condition's "`map.md` paragraph" now lives. I found it in `map-implementation-rules.md` through `map.md`'s pointer line. I also had to find the shape of a `map-history.md` entry, which I got by grepping its headings and copying node 277's and node 281's entries. The effort name for the commit trailer came from `git log`. Short names: "moved-paragraph pointer stale in a condition"; "history-entry shape found by example". I did not search earlier retrospectives for name counts.
2. What arrived that this node did not need: most of `map.md`'s Notes, and most of `map-manager-only.md` beyond the landing section (the priority list, the retrospective bullet, fog, out of scope), about 55 KB read whole when the work needed one section. A narrower mandatory read, "the section *How the worktree is made*", would have been enough. Short name: "whole manager file read for one section".
3. What would have made this easier: the spawn noting that node 267's clause 1 targets a paragraph node 345 moved. That one fact decided the pick.
4. What was stale, wrong or contradictory: node 267's worker's clause 1 (the `map.md` paragraph no longer exists there). The node's manager note says the doubled worktrees and the local exclude are live, and both are now gone, which the spawn already flagged. The manager's note "absolute path, `"$PWD/..."` from the repo root" still depends on the cwd being the root, which is the same failure mode in a different spelling. The new bullet removes that dependence.
`````

## Flags

`284.1` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment from node 56 above.* Node 56's replacement naming `.claude/skills/expedition/glossary.md` in place of `CONTEXT.md` was filed on this open, unclaimed node without asking the human first.

`284.2` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment from node 354 above.* Node 354's replacement of "five" (or "four") with "six" standing rules for writing was filed on this open, unclaimed node without asking the human first.

`284.3` `ASSUMPTION` **· settled** — Node 284 took node 281's worker's condition over node 267's, whose clause 1 names a `map.md` paragraph that node 345 moved to the rules file. *(The worker's full text is under its handover's `FLAGS`.)*

`284.4` `ASSUMPTION` **· settled** — Node 284 also anchored the worktree route's `test -w` writability check at `<repo root>`, the same relative-path defect one bullet below the Create command. *(The worker's full text is under its handover's `FLAGS`.)*

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-10-04. A fresh checker; the condition reached it as a verbatim copy of the node's condition and its two clause-4 amendments in `$TMPDIR/c284.md`, and the node's four flags as their `flags.md` sentences with ids.*

> PASS
>
> Scope: the work is the uncommitted diff in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/284-worktree-path, which touches .scratch/graph-workflow/map-manager-only.md and .scratch/graph-workflow/map-history.md. Under the rules file's paragraph beginning "An implementation node's work on this effort may be the effort's own record", I read the changed paths as the work. I took no statement of intent from them. I held the condition as amended, with both clause-4 amendments in force: the glossary is `.claude/skills/expedition/glossary.md`, and there are six standing rules for writing.
>
> 1. **Clause 1, the path resolves from any working directory: met.**
>    - The Create bullet now reads `git -C <repo root> worktree add -b worktree-<NN>-<name> .scratch/graph-workflow/worktrees/<NN>-<name>`, and it defines `<repo root>` as the main tree's absolute path, "the first path `git worktree list` prints".
>    - I tested this in a scratch repo carrying a copy of this repo's .gitignore. Running `git -C $R worktree add ...` from `$R/.scratch/graph-workflow` and from the parent of `$R` both created `$R/.scratch/graph-workflow/worktrees/<NN>-<name>`, as `git worktree list` showed.
>    - `git worktree list` run from inside a linked worktree also printed the main tree first.
>
> 2. **Clause 2, the created worktree is ignored: met.**
>    - In the real repo, `git check-ignore -v .scratch/graph-workflow/worktrees/284-worktree-path .scratch/graph-workflow/worktrees/12-some-name` matched `.gitignore:19:.scratch/graph-workflow/worktrees/` for both paths.
>    - The same command matched in the scratch repo for the worktree the command actually created.
>
> 3. **Clause 3, displaced wording replaced and banked verbatim: met.**
>    - Map-history only gains text: `git diff --numstat` gives 33 lines added and 0 removed. The file's committed content (`git show HEAD:...`) is a byte-identical prefix of the new file, which I confirmed with `diff` against `head -n <old line count>`.
>    - Both bullets the change displaced (Create, and "The route's one failure mode") were taken out with awk from `git show HEAD:.scratch/graph-workflow/map-manager-only.md`. `cmp` finds each byte-identical to its block appended in map-history.
>    - The headings follow the file's existing pattern, "## Superseded from `map-manager-only.md` at node 284 — ..." / "### From *How the worktree is made* — ...", the same shape as the node 234 and node 276 entries.
>    - Both bullets were replaced in map-manager-only.md, not struck where they stood. Neither original held any struck text.
>    - This also meets graph-conventions check 11 on both of its halves.
>
> 4. **Clause 4, only the two files touched: met.**
>    - `git status --porcelain --untracked-files=all` lists only the two files, and there are no new commits (HEAD is still 16ac40915).
>    - So no node file, `decisions.md` or `flags.md` was touched, and no status line.
>    - The three links added under `nodes/` (189, 265, 284) all resolve to files that exist.
>
> **The bar.**
> - Commands: no CLAUDE.md or AGENTS.md at the repo root. The rules file records that the repo has no build, no tests, no formatter and no CI, so the command half is empty and the bar is its non-command half.
> - Standards: I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`, mainly its `## What the work is held against` list. The work does not touch that file, so no standard moved.
> - What bore on this work:
>   - **Glossary `_Avoid_` lines.** I scanned the added lines, unwrapped, for every refused word. The only hits are "run(s)" (running a command), "tree" (git's main tree or working tree, not the graph) and "session". "session" sits inside text reproduced verbatim, so it was not introduced. None is a breach.
>   - **graph-conventions.md**: `## Writing the map`, `### Change the map` and check 11 are all met. Check 10 does not apply, because the edit is outside `## Notes`.
>   - **The six standing rules for writing**: no line-number citations were added, and the cross-reference "as in the *Create* bullet" points at its target by name.
>   - **/writing-for-agents**: read from the mattpocock-skills plugin's SKILL.md. It raised no defect.
>   - **/coding-principles and /naming**: little to apply to prose.
> - No reviewing skill is named for this repo, so I ran none.
> - Considered and not counted as a breach of rule 5 ("Bold a term only where it is defined"): the edited failure-mode bullet keeps three bold spans that are not terms. They are on "So the manager runs `test -w ...` before creating a worktree", "neither created nor written" and "raised to the human". All three were already in the text before this work. The work added no new bold.
>
> **Findings handed back alongside the PASS (none is a FAIL on the condition or on a stated standard):**
>
> - **Finding A: a false claim about git in the new Create bullet.**
>   - Instance: the bullet says "The repository's `.gitignore` does not match that path, so the manager's commit of `.scratch/graph-workflow` would stage the whole worktree."
>   - What git actually does: in the scratch repo, running without `-C` from `.scratch/graph-workflow` did create the doubled path, and `check-ignore` did not match it (exit 1). Both of those claims are true. But `git add .scratch/graph-workflow` then staged one gitlink entry (mode 160000, `git ls-files -s` shows `160000 <sha> 0 .scratch/graph-workflow/.scratch/graph-workflow/worktrees/97-z`) and warned "adding embedded git repository". It did not stage the worktree's files.
>   - Form: a sentence in the changed text that says what a git command does, where git does something else.
>   - Extent: none. The instances listed are not exhaustive. Only this sentence was tested against git.
>
> - **Finding B: an inaccurate sentence in the new map-history intro paragraph.**
>   - Instance: the paragraph says "Each passage gave a path relative to the shell's working directory and said only that the manager works from the main tree". The banked failure-mode bullet does not say "main tree" (`grep -c 'main tree'` counts 0 there and 1 in the banked Create bullet).
>   - Form: a statement in the appended intro about what the banked passages say that is false of one of them.
>   - Extent: the smallest set that contains every instance is the italic intro paragraph under "## Superseded from `map-manager-only.md` at node 284", compared against the two banked blocks under it.
>
> **Not checked:** whether the new Create bullet restates what node 284 holds (writing rule 2). Checking that would mean reading the node, which is outside what I was given.
>
> **Flags (no question needed, since none is false):**
> - 284.1, 284.2 and 284.3: claims about the record that the work cannot make true or false.
> - 284.4: true. The bullet now reads `test -w <repo root>/.scratch/graph-workflow`.
>
> The temporary directory under $TMPDIR has been removed, and the working tree is as I found it.

*The manager's note:* the checker handed back two findings beside its outcome, so the standing yes does not cover this gate. It goes to the human.

### The gate, 2026-10-04

`verbatim`: *"ok"*

The manager had offered "Recommended: a short correction round to fix both sentences, and the same checker re-checks." and the alternative "approve as is", closing with "Please answer: "ok for recommended", or "approve as is"." The reply takes the correction round. Flags `284.1` to `284.4` were in the payload and settle here.

## Handover, correction round 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      The worktree route's create command names a relative path and never says from where (correction round 1)

ROUND CHANGES: I fixed both forms the checker found. Each change touches text the acceptance condition names. Finding A changes a sentence in the Create bullet (clause 1), but the command and the path form are unchanged. Finding B changes the appended `map-history.md` intro (clause 3), and the banked passages stay byte-identical. The condition I worked to is unchanged from round 0: node 281's worker's condition, with the amendments from nodes 56 and 354 applied to clause 4's bar sentence, as quoted in the round-0 handover.

ANSWER:
The Create bullet under *How the worktree is made* in `map-manager-only.md` now gives the command as `git -C <repo root> worktree add -b worktree-<NN>-<name> .scratch/graph-workflow/worktrees/<NN>-<name>`. `<repo root>` is defined there as the main tree's absolute path, which is the first path `git worktree list` prints. Git resolves the relative path argument against the `-C` directory. So the command creates the worktree at `<repo root>/.scratch/graph-workflow/worktrees/<NN>-<name>` whatever the shell's working directory is. I chose `-C` over an absolute path argument because `-C` also pins the HEAD the worktree lands on to the main tree's HEAD. A cwd inside a linked worktree would otherwise change both the path and the base. The old bullet's "from the main tree" was dropped, because it named the tree and not the directory.

The bullet keeps the trigger as part of the rule, as the map's admission test allows. Without `-C`, a cwd below the repository root produces a doubled path such as `.scratch/graph-workflow/.scratch/graph-workflow/worktrees/<NN>-<name>`. `.gitignore` does not match that path. So `git add .scratch/graph-workflow` stages the worktree as one embedded repository entry, a gitlink with mode 160000, and warns `adding embedded git repository`. This was measured in a scratch repo. It does not stage the worktree's files.

The same section's writability check had the same defect, so it also changed: `test -w .scratch/graph-workflow` became `test -w <repo root>/.scratch/graph-workflow`. From the wrong cwd, the relative form would report a false failure and send a needless raise to the human.

Both displaced passages are appended byte-identical to `map-history.md` under a new section, "Superseded from `map-manager-only.md` at node 284 — the create command's relative path, and the writability check's". Each passage has its own `### From *How the worktree is made* — …` heading. The section's intro states what each passage said. Both gave a path relative to the shell's working directory. The create bullet said only "from the main tree", and the writability check named no directory.

`.gitignore` is unchanged. Its anchored rule `.scratch/graph-workflow/worktrees/` already matches the path the new command produces. `git check-ignore -v` reports `.gitignore:19` for that path, and returns no match for the doubled path.

Left unchanged: the paragraph in `map-implementation-rules.md` beginning "An implementation node's worktree is made with plain git". It is a true statement of where the worktree goes, read by workers and not used as a command, and clause 4 bars touching it. Also left unchanged: the Base bullet's "the manager's current `HEAD`". With `-C <repo root>` the base is the main tree's HEAD, which is the manager's HEAD as long as the manager stands in the main tree, as the landing policy assumes.

INDEX LINE:    The worktree route's create command now runs as `git -C <repo root> worktree add …`, so it gives the same ignored path from any working directory; the writability check is anchored the same way.

FLAGS:
ASSUMPTION: Node prose: The node held two conditions and left the pick to its worker. I took node 281's worker's condition, two files, with the amendments from nodes 56 and 354 applied to its bar sentence. Node 267's worker's clause 1 names a paragraph in `map.md` that node 345 moved to `map-implementation-rules.md`, so it cannot be met as written. Its `.gitignore` demand (check-ignore reports `.gitignore`, not `.git/info/exclude`) and its no-worktree-touched demand both hold for this work anyway, and I verified both. Index: Node 284 took node 281's worker's condition over node 267's, whose clause 1 names a `map.md` paragraph that node 345 moved to the rules file.
ASSUMPTION: Node prose: Beyond the Create bullet the condition names, I also anchored the same section's `test -w .scratch/graph-workflow` check at `<repo root>`. It is the same defect in the same section, a relative path with no stated cwd. From the wrong directory it gives a false failure that the bullet says to raise to the human. Its old text went to `map-history.md` under clause 3's procedure. Index: Node 284 also anchored the worktree route's `test -w` writability check at `<repo root>`, the same relative-path defect one bullet below the Create command.

NEW NODES:     none

INVALIDATIONS: Node 265 (extension): its route's create command now carries `-C <repo root>`. Its `decisions.md` line stays true as a statement of location. Node 281: none.

CONDITIONS:    Unchanged from round 0. The 18 open or claimed node files (counted 2026-10-04, not authoritative, for scale only) were searched, conditions and questions, for: "from the main tree", "git worktree add", "test -w", "worktrees/<NN>", "How the worktree is made", "Create bullet", "relative path", "doubled". Only node 284 matched, plus node 384 on "relative path", which is unrelated. This round's new wording ("embedded git repository") changes no open node's condition or question. No replacements.

MISSING FROM MAP: Node 267's condition and the spawn both point at a `map.md` paragraph that now lives in `map-implementation-rules.md`. I found it through `map.md`'s pointer line. Otherwise none.

GATE PAYLOAD:
Checker findings, and what changed:
- Finding A (false claim about git in the Create bullet): fixed. I checked the claim first. In a scratch repo with this repo's `.gitignore`, the worktree was created without `-C` from `.scratch/graph-workflow`, and then `git add .scratch/graph-workflow` was run from the root. `git diff --cached --name-status` showed one `A` entry for the doubled path, `git ls-files -s` showed mode `160000`, and git warned `adding embedded git repository`. "would stage the whole worktree" is replaced by "`git add .scratch/graph-workflow` stages the worktree as one embedded repository entry and warns `adding embedded git repository`". I checked the other statements about git in the changed text for the same form, and each holds by measurement:
  - "Git resolves the relative path against `<repo root>`" (scratch-repo test, round 0);
  - "the first path `git worktree list` prints" is the main tree (measured here and in scratch);
  - the doubled path without `-C` (measured by the checker and in node 284's question);
  - `.gitignore` not matching the doubled path (`check-ignore` exit 1).
- Finding B (history intro misstates one banked passage): fixed. The intro now reads: "Each passage gave a path relative to the shell's working directory. The create bullet said only that the manager works from the main tree, which names the tree and not the directory, and the writability check named no directory at all." I compared the intro's other statements against the two banked blocks: byte-identical reproduction, the route taken, and what replaces each passage. Each holds. The banked passages are untouched, and the paragraph was rewrapped to the file's width.
Re-checks run: graph-conventions check 11 against HEAD. The committed `map-history.md` is a byte-exact prefix of the new one, and all 8 lines removed from `map-manager-only.md` appear byte-identically in the appended text. No added line is longer than 120 characters. Only the two paths are modified. Bar: the repo has no build, tests, formatter or CI, as recorded.
Paths touched:
- /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/284-worktree-path/.scratch/graph-workflow/map-manager-only.md
- /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/284-worktree-path/.scratch/graph-workflow/map-history.md
Proposed commit message:
```
Worktree route: run the create command with git -C <repo root>

The Create bullet gave a path relative to the shell's working directory, so a
manager whose cwd was below the repository root created worktrees at a doubled
path that .gitignore does not match, and git add then staged it as an embedded
repository. The command now runs as git -C <repo root> worktree add ..., and
the writability check is anchored the same way. The displaced text is appended
to map-history.md.

Node: graph-workflow/284
```
Claims in the correction message checked: Finding A was reproduced as described. Finding B holds, since the banked failure-mode bullet does not contain "main tree". I could not check "Checker run 1 PASSED every clause" and did not rely on it.

RETROSPECTIVE:
Names were found by searching the `## Retrospective` sections, and any heading containing "retrospective", of the files under `.scratch/graph-workflow/nodes/` in this worktree on 2026-10-04. Counts are as derived then.
1. What I had to hunt for:
   - `condition-cites-moved-paragraph`: node 267's worker's condition names a `map.md` paragraph that node 345 moved. I found it through `map.md`'s pointer line, after first looking in `map.md` itself. New name, 0 earlier.
   - `history-entry-shape-by-example`: the form of a `map-history.md` entry. I found it by grepping that file's headings and copying the node 277 and node 281 entries; `graph-conventions.md`'s *Change the map* gives only the rule. New name, 0 earlier.
   - This round: the existing retrospective names. I found them by the search above, which needed three regex passes because names are not marked uniformly (backticks, bold, plain). `record-is-not-mechanically-scannable` fits, 2 earlier: 178, 212.
2. What arrived that this node did not need:
   - `map-read-whole-for-a-few-items`: `map-manager-only.md` was read whole (about 55 KB) for one section, *How the worktree is made*, and most of `map.md`'s Notes bore on nothing here. A mandatory read naming the section, or a pointer to the heading, would have avoided it. 2 earlier: 178, 243.
   - This round's message carried exactly what the round needed.
3. What would have made this node easier:
   - `condition-cites-moved-paragraph` again: one line in the spawn saying node 267's clause 1 targets moved text would have settled the pick at once.
   - `tool-behaviour-stated-unmeasured`: Finding A came from my stating what `git add` does by inference while measuring everything else. A habit or rule of measuring every sentence that says what a tool does, before handover, would have caught it. New name, 0 earlier.
   - `summary-generalised-from-one-instance`: Finding B came from my writing an intro over two banked passages from the memory of one. Comparing each sentence of the summary against each passage would have caught it. New name, 0 earlier.
4. What was stale, wrong or contradictory:
   - `condition-cites-moved-paragraph`, as above.
   - The node's filing note describes the doubled worktrees and the local exclude as live, and both are gone, as the spawn said.
   - `absolute-path-form-still-cwd-dependent`: the manager's note gives the absolute form `"$PWD/..."` "from the repo root", which still depends on the cwd being the root, the same defect in a different spelling. New name, 0 earlier.
   - My own round-0 text: the `git add` claim and the history-intro sentence, which the checker found and this round fixed.
`````

### Checker run 2 — `PASS`

*The checker's own text, pasted, 2026-10-04. The run 1 checker, resumed for this node's re-check.*

> PASS
>
> Re-check after the correction round on run 1's findings A and B. No statement came with the round naming exactly what changed, so I checked the whole condition and the whole bar again as written. Comparing the new diff with the run-1 diff, word for word with the text unwrapped, shows two passages changed:
> - The last sentence before "Settled at" in the Create bullet of map-manager-only.md. It now reads "so `git add .scratch/graph-workflow` stages the worktree as one embedded repository entry and warns `adding embedded git repository`". In run 1 it read "would stage the whole worktree".
> - The italic intro paragraph in map-history.md. It now reads "The create bullet said only that the manager works from the main tree, which names the tree and not the directory, and the writability check named no directory at all". In run 1 it read "Each passage ... said only that the manager works from the main tree".
>
> I found no other changed words. The failure-mode bullet and both banked blocks are unchanged from run 1. As before, I read the changed paths as the work, under the rules file's paragraph that begins "An implementation node's work on this effort may be the effort's own record". The condition I held is the one with both clause-4 amendments: the glossary is at `.claude/skills/expedition/glossary.md`, and there are six standing rules for writing.
>
> 1. **Clause 1 (the path resolves the same from any working directory): met.**
>    - The Create bullet gives `git -C <repo root> worktree add -b worktree-<NN>-<name> .scratch/graph-workflow/worktrees/<NN>-<name>`, where `<repo root>` is "the first path `git worktree list` prints".
>    - I re-ran it in a scratch repo that carries this repo's .gitignore. From `$R/.scratch/graph-workflow` and from the parent directory of `$R`, both runs created `$R/.scratch/graph-workflow/worktrees/<NN>-<name>`, as `git worktree list` showed.
>    - Run inside a linked worktree, `git worktree list` printed the main tree first.
>
> 2. **Clause 2 (the created path is ignored): met.**
>    - In the real repo, `git check-ignore -v .scratch/graph-workflow/worktrees/284-worktree-path .scratch/graph-workflow/worktrees/12-some-name` matched `.gitignore:19:.scratch/graph-workflow/worktrees/` for both paths.
>    - In the scratch repo it matched both worktrees the command created.
>
> 3. **Clause 3 (displaced text replaced, and banked verbatim): met.**
>    - `git diff -- map-history.md` shows 0 removed lines.
>    - `git show HEAD:` of map-history.md is a byte-identical prefix of the current file, checked with `diff` against `head -n <old line count>`.
>    - Both displaced bullets, the Create bullet and "The route's one failure mode", were extracted with awk from `git show HEAD:.scratch/graph-workflow/map-manager-only.md`. `cmp` against the matching banked blocks reports create-identical and fail-identical.
>    - The headings mirror the section's existing pattern. Both bullets were replaced, not struck in place. Graph-conventions check 11 holds on both of its halves.
>
> 4. **Clause 4 (only the two files are touched): met.**
>    - `git status --porcelain --untracked-files=all` lists only the two files, and HEAD is still 16ac40915.
>    - No node file, `decisions.md` or `flags.md` was touched, and no node's status line.
>    - All three `nodes/` links in the added lines (189, 265 and 284) resolve to existing files.
>
> **The bar**
> - The repo states no commands: there is no CLAUDE.md or AGENTS.md at its root. The rules file records no build, no tests, no formatter and no CI. So the bar is its non-command half, and that is the complete bar.
> - I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`, under `## What the work is held against`. The work does not touch that file, so no standard moved.
> - Standards that bore on this work:
>   - **Glossary `_Avoid_` lines.** I re-scanned the added lines, unwrapped. The hits are "run(s)" (running a command), "tree" (git's main or working tree), "session" (inside text reproduced verbatim) and the new "warns". "warns" describes git's own output, not the flag concept that "warning" is refused for. None is a breach.
>   - **graph-conventions.md**: `## Writing the map`, `### Change the map` and check 11 are all met.
>   - **Six standing rules for writing**: the added lines cite no line numbers.
>   - **/writing-for-agents**: no defect.
>   - **/coding-principles** and **/naming** apply little to prose.
> - No reviewing skill is named for this repo, so I ran none.
>
> **Run 1's findings, re-established**
> - **Finding A is repaired.** In the scratch repo, running without `-C` from `.scratch/graph-workflow` created `.scratch/graph-workflow/.scratch/graph-workflow/worktrees/97-z`. `git check-ignore` did not match it (exit 1). Then `git add .scratch/graph-workflow` at the repo root exited 0 and warned "warning: adding embedded git repository: ...". `git ls-files -s` shows exactly one `160000` entry for that path, and `git ls-files | grep -c '97-z/'` gives 0. So the bullet's new sentence is true as written.
>   - Note: one intermediate run piped `git add` into `| head -1`, and SIGPIPE killed git before it wrote the index. The result above comes from a run without the pipe.
> - **Finding B is repaired.** The intro no longer says that both passages mention the main tree. It attributes "said only that the manager works from the main tree" to the create bullet alone, which matches the banked text (`grep -c 'main tree'`: 1 in the create bullet, 0 in the failure-mode bullet). It says the writability check "named no directory at all". From the clause before it, "directory" there means the working directory, and the banked `test -w .scratch/graph-workflow` names none, so I do not count this as a defect.
>
> Not checked, as in run 1: whether the Create bullet restates what node 284 holds (writing rule 2). Checking it would mean reading the node, which is outside what I was given.
>
> **Flags** (none is false, so I have no question to hand back):
> - 284.1, 284.2 and 284.3 are claims about the record, and the work can make none of them true or false.
> - 284.4 is true. The bullet reads `test -w <repo root>/.scratch/graph-workflow`, "with `<repo root>` as in the *Create* bullet".
>
> I removed the temporary directory under $TMPDIR. The worktree is as I found it, and the repo's worktree list is unchanged at three entries.

*The manager's note on what the checker did not check:* writing rule 2 is a standard, not a part of the condition. The manager read the new Create bullet in the worktree: it states the command, its trigger and a "Settled at" citation, and restates no reasoning of node 284's.

### The gate, second time, 2026-10-04 — standing yes

`standing yes`. The scope, word for word: *"Approve all gates automatically"*. The checker's `PASS` (run 2) is taken as the human's approval. The run covered every part of the condition and handed back no question. Flags 284.1 to 284.4 were settled at the human's gate.
