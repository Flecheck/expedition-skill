# Reword `implementer` to "the worker" in the shipped files

Type: implementation
Status: resolved
Blocked by: none

## Question

Carry node 353's answer into the shipped files: the 9 uses of `implementer` become "the worker"/"a worker" (or "the implementation worker" where a sentence needs it), with no glossary headword.

*Reported by [node 353](353-whether-implementer-becomes-a-glossary-headword.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Acceptance condition

*Authored by node 353's worker and filed by the manager.*

> Done when all of the following hold.
> 1. Running `grep -rn -i "implementer" --exclude-dir=.scratch --exclude-dir=.git .` from the repository root returns nothing. Run over the working tree when this condition was written, it returned exactly these 9 lines, which are the whole scope of the work:
>      `.claude/skills/expedition/glossary.md:134` — "The manager starts it, and the implementer never does, because whoever spawns it"
>      `.claude/skills/expedition/SKILL.md:830` — "3. What does an implementer do with a finding it believes is false? It has no route except fixing it."
>      `.claude/skills/expedition-checker/SKILL.md:79` — "5. Your outcome goes to the manager, which sends it to the implementer."
>      `.claude/skills/expedition-checker/SKILL.md:88` — "The implementer works from the same file, so the two of you"
>      `.claude/skills/expedition-checker/SKILL.md:208` — "over the part of the work the implementer may edit."
>      `.claude/skills/expedition-checker/SKILL.md:209` — "command whose hits are mostly text the implementer may not touch"
>      `.claude/skills/expedition-checker/SKILL.md:210` — "command to text the implementer may edit is part of supplying one."
>      `.claude/skills/expedition-checker/SKILL.md:215` — "The extent lets the implementer repair every instance"
>      `.claude/skills/expedition-checker/SKILL.md:250` — "A `FAIL` sends the work back to an implementer who met the scope as written"
>    An instance the grep reaches outside this list is reported and not edited.
> 2. At each of the 9 sites, the party is now named "the worker" or "a worker", with the article adjusted to the sentence. "The implementation worker" is allowed instead where the sentence would otherwise not say which worker. No other word or coined phrase names this party at these sites.
> 3. Apart from the rename and the article changes it forces, the sentences at these sites say what they said before. No rule is added, removed or narrowed, and lines are re-wrapped only as far as the rename requires.
> 4. `.claude/skills/expedition/glossary.md` gains no headword and no `_Avoid_` line, and its entry and `_Avoid_` counts are unchanged by this work.
> 5. No file other than `.claude/skills/expedition/glossary.md`, `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition-checker/SKILL.md` is changed, and nothing under `.scratch/` is changed.
> 6. The working tree meets the bar.

## Answer

The 9 shipped uses of `implementer` now read "the worker" or "a worker", with no re-wrap and no glossary headword or `_Avoid_` line added.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `d1e6c52`. Flags 357.1 settle at the node closing report.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-28. The worker's own text, pasted.*

````
HANDOVER:      Reword `implementer` to "the worker" in the shipped files

ANSWER:        `implementer` is gone from the shipped files. All 9 sites the condition lists now say "the worker", or "a worker" where the original had "an implementer". No site needed "the implementation worker". The calls made:
               - `.claude/skills/expedition/glossary.md`, `**Checker**` entry: "The manager starts it, and the worker never does". I chose "the worker" over "the implementation worker" for two reasons. The entry's first sentence already says the checker checks "a finished implementation", so it is clear which worker is meant. And the longer phrase would have pushed the line past the file's 102-column width and forced a re-wrap.
               - `.claude/skills/expedition/SKILL.md`, the numbered question 3: "What does a worker do with a finding it believes is false?" The next sentence already says "a worker sure that a finding is wrong", so the two sentences now use the same word.
               - `.claude/skills/expedition-checker/SKILL.md`, 7 sites (rule 5; the `## The standards you hold the work against` paragraph; the three lines of extent 1; "The extent lets the worker repair"; the `FAIL` bullet): "the worker" each time, and "a worker who met the scope" where the original had "an implementer". The contract is addressed to the checker as "you", and it already uses "the worker" for the other party at its line 318, so nothing there is ambiguous.
               Every replacement is shorter than the word it replaces, so no line was re-wrapped. The glossary is unchanged apart from the one word: 58 headword lines (`^\*\*`) and 45 `_Avoid_` lines, both before and after.

INDEX LINE:    The 9 shipped uses of `implementer` now read "the worker" or "a worker", with no re-wrap and no glossary headword or `_Avoid_` line added.

FLAGS:         ASSUMPTION: The condition's grep still returns one line in the worktree: `.git:1:gitdir: /home/mathieu/projects/graph-agent/.git/worktrees/357-implementer`. That line is not shipped text. In a linked worktree `.git` is a file, not a directory, so `--exclude-dir=.git` does not exclude it. It matches only because this node's worktree name contains "implementer". In the main checkout `.git` is a directory, so the grep there returns nothing. Clause 1 routes an instance outside its list to being reported and not edited, so I reported it, did not edit it, and judged clause 1 met on the shipped files. I did not raise, because nothing in the shipped files is affected and the line goes away when the worktree is removed.
               Index sentence: In node 357's worktree, the condition's `implementer` grep still matched the worktree's own `.git` pointer file, whose path contains the node's name; it was reported, not edited, and clause 1 was judged met on the shipped files.

NEW NODES:     none

INVALIDATIONS: none. This carries out node 353's answer and extends no resolved node. Resolved record text that says "implementer" (for example node 13, node 140's title) keeps the word under the never-delete rule.

CONDITIONS:    I searched the `## Acceptance condition` and `## Question` sections of every open, claimed and blocked node for four things: `implementer` (case-insensitive); the changed paths with their old line numbers (`expedition/SKILL.md:830`, `expedition-checker/SKILL.md:79|88|208|209|210|215|250`, `glossary.md:134`); and the old phrases ("sends it to the implementer", "implementer works from", "implementer may edit/not touch", "lets the implementer", "to an implementer who", "implementer never does", "What does an implementer").
               - Old phrases: no hits outside node 357.
               - `implementer`: hits in open nodes 32, 34, 149, 152, 154, 157 and 214. Each one uses the word as record prose, in a link title or a quote, for the party now called the worker. None of them makes a claim about the shipped text that this work falsifies. The glossary gains no `_Avoid_` line, so the word is not refused, and no clause needs replacing.
               - Node 34 (open, grilling), "What an implementer does with a checker finding it believes is false": its question concerns the shipped line `.claude/skills/expedition/SKILL.md` question 3, which now reads "What does a worker do with a finding...". This renames a term in the question and answers no part of it. Node 353's worker already reported this, and the manager's note on node 34 records it.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings: none yet.
               Bar: I checked the repo and it matches the rules file's record. There is no manifest, build, test, formatter or CI. The root holds `.claude/`, `CONTEXT-MAP.md`, `CONTEXT.md`, `.gitignore` and `.scratch/`, and `.gitignore` invokes nothing. So the bar here is its non-command half: the condition, the ground rules, the writing rules, the glossary's `_Avoid_` lines, `graph-conventions.md` and `/writing-for-agents`. `git diff --check` is clean. Each file keeps its wrap width.
               Paths touched (all in worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/357-implementer`, uncommitted, on branch `worktree-357-implementer`):
                 .claude/skills/expedition/glossary.md (1 line)
                 .claude/skills/expedition/SKILL.md (1 line)
                 .claude/skills/expedition-checker/SKILL.md (7 lines)
               Nothing under `.scratch/` changed.
               Proposed commit message:
                 Reword `implementer` to "the worker" in the shipped files

                 The 9 shipped uses of `implementer` now read "the worker" or
                 "a worker". The glossary gains no headword and no `_Avoid_` line.

                 Node: graph-workflow/357

Method skills: none invoked, so nothing was skipped.

RETROSPECTIVE
1. What I had to hunt for: which nodes are open, for the CONDITIONS search. There is no index of statuses, so I grepped `^Status:` across every node file. I also had to work out why the grep still hit something after the edit (the worktree's `.git` pointer file).
2. What arrived that this node did not need: most of `map.md` and `map-implementation-rules.md`. This node needed the destination, writing rule 5 and the bar paragraph. The worktree, never-delete, record-as-work and trigger-file paragraphs had nothing to act on here. Node 353's `## Answer` was one line pointing at its handover, which I did not need either, because the condition is self-contained.
3. What would have made this easier: a condition whose grep works inside the worktree it will be run in, for example by adding `--exclude=.git` or by naming the worktree without the searched word. The worktree name `357-implementer` makes the condition's own check fail by construction. A one-line list of open node ids in the spawn would have saved the status sweep.
4. What was stale, wrong or contradictory: the condition's grep command reaches the worktree's `.git` file, as described above, so it cannot literally "return nothing" in this worktree. The listed line numbers were exact. The glossary counts in `map.md` (58/45) are still accurate.
````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 354's check; the condition reached it as a verbatim copy in `$TMPDIR/c357.md`.*

> PASS
>
> This is the check of node 357, "Reword `implementer` to "the worker" in the shipped files". The work is the uncommitted diff to `.claude/skills/expedition/glossary.md`, `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition-checker/SKILL.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/357-implementer`, on base 51e4a9a. I read the whole condition in `/tmp/claude-1000/c357.md`.
>
> **Parts of the condition**
>
> - **1: met.**
>   - `git grep -n -i implementer HEAD -- . ':!.scratch'` returns 9 lines at the base, which matches the recorded scope.
>   - In the worktree, running the recorded command (`grep -rn -i "implementer" --exclude-dir=.scratch --exclude-dir=.git .`) returns one line: `.git:1:gitdir: /home/mathieu/projects/graph-agent/.git/worktrees/357-implementer`.
>   - That hit is the worktree's own `.git` pointer file. It exists only because the manager named the worktree after the word, and it is neither tracked nor shipped. `--exclude-dir=.git` misses it only because `.git` is a file in a worktree and a directory in the main checkout, where the condition was written.
>   - None of the 9 listed sites still contains the word, and no other file does either.
> - **2: met.** All 9 sites now use "the worker" or "a worker", with the article adjusted:
>   - `glossary.md` **Checker**: "The manager starts it, and the worker never does";
>   - `SKILL.md` item 3: "What does a worker do with a finding it believes is false?";
>   - checker hard rule 5: "which sends it to the worker";
>   - the standards paragraph: "The worker works from the same file";
>   - extent rung 1, three times: "the worker may edit", "the worker may not touch", "the worker may edit";
>   - "The extent lets the worker repair every instance";
>   - "A `FAIL` sends the work back to a worker who met the scope as written".
>   
>   No other name for this party appears at these sites.
> - **3: met.** Each changed line differs from its old version only by the rename and the article it forces. No other word moved, and no line was re-wrapped. The diff is 9 lines removed and 9 added, one for one. Each sentence says what it said before.
> - **4: met.** The `glossary.md` hunk changes one line inside the **Checker** entry. It adds no `**…**:` headword line and no `_Avoid_` line, so both counts are unchanged.
> - **5: met.** `git status --short --untracked-files=all` shows only the three files. Nothing under `.scratch/` changed.
> - **6: met.** See the bar below.
>
> **The bar**
>
> - The rules file records no build, tests, formatter or CI, and the repo confirms that.
> - `git diff --check` is clean (exit 0).
> - No changed line exceeds the files' wrap width.
>
> **Standards.** As in my earlier checks, I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`, together with the ground rules and the six writing rules.
>
> - These bore on the work, and I found nothing against them:
>   - The glossary's `_Avoid_` lines. The change removes a word that had no headword.
>   - Writing rule 5: no coined term, and one clear referent for each pronoun.
>   - `/writing-for-agents`.
>   - Ground rules 2 and 3. The checker contract still stands alone.
> - The checker contract is one of the files changed. The rename moves no element of what it requires, so my check is untouched.
> - No reviewing skill is named, so I ran none.
>
> NOT COVERED:
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The condition does not demand this; the rules file makes it a bookkeeping rule. The worktree shows no `.scratch/` change, and what the main tree's record holds is outside what I was given.

### Gate — approve, `standing yes`, 2026-09-27

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and its one NOT COVERED item is the worker's bookkeeping. This settles none of the node's flags; they settle at the node closing report.

## Flags

`357.1` `ASSUMPTION` **· settled** — The condition's grep still returns one line in the worktree: `.git:1:gitdir: /home/mathieu/projects/graph-agent/.git/worktrees/357-implementer`. That line is not shipped text. In a linked worktree `.git` is a file, not a directory, so `--exclude-dir=.git` does not exclude it. It matches only because this node's worktree name contains "implementer". In the main checkout `.git` is a directory, so the grep there returns nothing. Clause 1 routes an instance outside its list to being reported and not edited, so I reported it, did not edit it, and judged clause 1 met on the shipped files. I did not raise, because nothing in the shipped files is affected and the line goes away when the worktree is removed.

*The manager's note, 2026-09-28:* the stray match is the manager's doing: it named the worktree `357-implementer`, after the very word the condition's grep refuses.

*The manager's note, 2026-09-27:* flags 357.1 settle at the node closing report that closes this node, which names its gate as taken under the standing yes.
