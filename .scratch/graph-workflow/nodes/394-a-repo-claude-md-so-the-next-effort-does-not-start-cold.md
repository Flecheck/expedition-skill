# A repo `CLAUDE.md` so the next effort in this repo does not start cold

Type: implementation
Status: claimed
Blocked by: none

## Question

This work lets every agent that starts in this repository, on any later effort, learn at once what the repository is, what its work is held to, and how its worktrees are made, without reading this effort's map. That map and its rules file belong to `.scratch/graph-workflow/`, and they stop binding when this effort closes.

*Minted by the manager from the human's request, 2026-10-07, `verbatim`:* *"Can you create a CLAUDE.md withe the information in map-implementation-rules.md and other usefull information so that next effort in this repo doesn't start from scratch"*

*The manager then proposed a scope. It listed what the file would hold: what the repo is, the bar, the standards, the ground rules and writing rules, the worktree route, the trigger file, two traps, and pointers. It listed what stays out: landing and bookkeeping, and the "why". It would be short, around a page, pointing at files instead of restating them. The message ended "Please answer: \"ok for recommended\" mints the node with that scope, or tell me what to add or drop." The human's answer, `verbatim`, 2026-10-07:* *"ok"*

## Acceptance condition

*Written by the manager, who minted the node.*

> The work is one new file, `CLAUDE.md`, at the repository root. No other file may be edited.
>
> Scope: the file is new and the named place is the work, so the scope came from no search.
>
> Done when all of the following hold.
>
> 1. `CLAUDE.md` exists at the repository root, and `git status` shows it as the only change.
> 2. It says what the repository is: the `/expedition` workflow's skill files under `.claude/skills/`, the auto-loaded `.claude/rules/expedition-triggers.md`, and per-effort records under `.scratch/<effort>/`. It says an effort's map is the file `map.md` in that effort's directory.
> 3. It states the bar for this repository. The repository has no build, no tests, no formatter and no CI. So the bar is the standards in clause 4 plus the node's acceptance condition. It states this as the repository's own statement of its commands.
> 4. It lists the standards that work in this repository is held to: `/coding-principles` and `/naming`; the `_Avoid_` lines of `.claude/skills/expedition/glossary.md`; `.claude/skills/expedition/graph-conventions.md`; and `/writing-for-agents`.
> 5. It states, as rules for the files under `.claude/skills/`, the content of the five ground rules and the six standing rules for writing held in `.scratch/graph-workflow/map.md`'s `## Notes`, in the blocks headed "Ground rules for this effort." and "This effort's standing rules for writing". It may reword them so that they read as repository rules rather than this effort's. It keeps every demand they make, drops their node citations, and adds no new demand.
> 6. It states the worktree route an implementation node uses here:
>    - the worktree is made with plain `git worktree add` at `.scratch/<effort>/worktrees/<NN>-<name>` on a branch `worktree-<NN>-<name>`;
>    - that path is ignored by `.gitignore`;
>    - a worker writes the tree by absolute path and owes no cleanup;
>    - the fast-forward merge into the main checkout and the worktree's removal run with the sandbox off.
>
>    It may point at an effort's `map-manager-only.md` for the full steps, rather than restating them.
> 7. It states that whoever edits, in `.claude/skills/expedition/SKILL.md`, the governing statement of a duty copied into `.claude/rules/expedition-triggers.md`, or of the priority that orders them, edits that file in the same change or says plainly why not.
> 8. It states the two traps:
>    - many refused words in the glossary's `_Avoid_` lines are ordinary English refused only for one concept, so a grep for them gives false positives, and the distinctive refusals are checked by hand;
>    - a number about an effort's record that is handed to another agent, or written into a condition, carries the date it was derived and says it is for scale only.
> 9. It says nothing is ever pushed without the human's word.
> 10. It holds no account of how any rule was learned, no node citation, and no rule that binds only `.scratch/graph-workflow/`'s effort, such as its landing steps, its record bookkeeping, its slot counts or its standing yes.
> 11. It is at most 900 words as counted by `wc -w CLAUDE.md`. It points at a file by path or heading wherever the reader can read that file, rather than restating it.
> 12. The working tree meets the bar.

## Handover, attempt 1

*Pasted as the worker handed it back, 2026-10-07.*

`````
HANDOVER:      A repo `CLAUDE.md` so the next effort in this repo does not start cold

ANSWER:        A new `CLAUDE.md` now sits at the repository root. It is 852 words by `wc -w` (counted 2026-10-07, for scale only), and it is the only change in the tree. It has these sections, in this order:
               - `## What this repository holds`: the skill files under `.claude/skills/`, the glossary path, the auto-loaded `.claude/rules/expedition-triggers.md`, and `.scratch/<effort>/`. It also says an effort's map is `map.md` in that directory.
               - `## Commands`: the repository's own statement that it has no build, no tests, no formatter and no CI. So the bar is the standards plus the node's acceptance condition.
               - `## Standards`: the four standards from clause 4.
               - `## Rules for the files under .claude/skills/`: the five ground rules and the six rules for writing. They are reworded only so that they read as repository rules, with every demand kept and the node citations dropped. Two small wording changes:
                 - "shipped file" became "file under `.claude/skills/`".
                 - Writing rule 2's "item" became "entry", because the glossary refuses `item` for a node.
               - `## The trigger file`: the same-change duty for `SKILL.md` against `expedition-triggers.md`.
               - `## The worktree of an implementation node`: the four route facts. The full steps are pointed at in `.scratch/graph-workflow/map-manager-only.md`, under `## Landing an implementation node's work`, in the passage *How the worktree is made*.
               - `## Two traps`.
               - `## Pushing`: nothing is pushed without the human's word.
               One call a later reader would otherwise have to re-derive: `.gitignore` today ignores only `.scratch/graph-workflow/worktrees/`, not `.scratch/<effort>/worktrees/` in general. So the worktree section states that `.gitignore` ignores the path, and adds that before an effort's first worktree you check that an entry covers that effort's directory and add one where none does (see the ASSUMPTION flag).

INDEX LINE:    A root `CLAUDE.md` now states what the repo is, its commandless bar, its standards, the skill-file ground and writing rules, the worktree route, the trigger-file duty, two traps, and no-push.

FLAGS:         ASSUMPTION — Clause 6 asks the file to state that `.scratch/<effort>/worktrees/<NN>-<name>` "is ignored by `.gitignore`". In fact `.gitignore` covers only `.scratch/graph-workflow/worktrees/`, so for any other effort that statement would be false. No other file could be edited, so I stated the fact and added one sentence: before an effort's first worktree, check that a `.gitignore` entry covers that effort's directory, and add one where none does. Grounds: this keeps the clause's demand true for a later effort instead of writing a false sentence. The decision is contained in this one file, so it is not a raise. The alternative is a `.gitignore` glob (see NEW NODES), which would make that sentence unnecessary.
               Index sentence: CLAUDE.md tells a new effort to check that .gitignore covers its own worktrees directory, since .gitignore today ignores only graph-workflow's.

NEW NODES:     Name: Make `.gitignore` ignore every effort's worktrees directory. Kind: implementation. Blockers: none.
               Question: This lets a later effort in this repository cut implementation worktrees without first editing `.gitignore`, as the root `CLAUDE.md` describes. Today `.gitignore` ignores only `.scratch/graph-workflow/worktrees/`. Should it ignore `.scratch/*/worktrees/` instead?
               Acceptance condition:
               > The work edits `.gitignore` and `CLAUDE.md` only. Scope came from no search: the named places are the work.
               > 1. `.gitignore` ignores `.scratch/*/worktrees/`, and `git check-ignore .scratch/anyname/worktrees/x` prints that path.
               > 2. `.gitignore` still ignores `.scratch/graph-workflow/worktrees/`.
               > 3. The sentence in `CLAUDE.md`'s `## The worktree of an implementation node` that tells an effort to check `.gitignore` before its first worktree, and to add an entry where none covers it, is removed. The bullet still states that `.gitignore` ignores that path.
               > 4. `CLAUDE.md` is at most 900 words by `wc -w CLAUDE.md`.
               > 5. The working tree meets the bar.

INVALIDATIONS: - `map-implementation-rules.md`, paragraph "The bar's commands for this repo": two of its statements are now false. It says "This repo states no commands of its own", and it says the root "holds no agent-instruction file such as `CLAUDE.md` or `AGENTS.md`". The repository now states its commands, which are none, in `CLAUDE.md`. That statement agrees with the recorded copy, so the copy now has something to confirm against, and it confirms. This needs a narrowing edit, done by the manager or a new node.
               - Node 205 ("this repo's recorded commands have nothing to confirm against"): this work contradicts its answer's premise, that there is nothing to confirm against and that one look at the root finds no agent-instruction file. Its conclusion about which commands to run, which is none, stands.
               - Node 174 ("which statement of the bar's commands wins"): it says that on this effort the rule is inert because the root holds no `CLAUDE.md`. That is now narrowed: the rule now applies here, and the two statements agree.
               Many resolved handovers (for example 371-391 and 40/41) state as a then-current observation that the root holds no CLAUDE.md. These are records of what happened, and nothing in them needs changing.

CONDITIONS:    I searched the `## Acceptance condition` and `## Question` sections of open and claimed nodes for `CLAUDE.md`, `AGENTS.md`, "states no commands", "agent-instruction file" and "commands of its own". The only match was node 394 itself. I searched resolved nodes for the same phrases, which turned up the invalidations above. No replacement clauses and no changed questions.

MISSING FROM MAP: none. Everything I needed was in `map.md`'s `## Notes`, in `map-implementation-rules.md` and in `map-manager-only.md`'s worktree passage, where the spawn pointed.

GATE PAYLOAD:  The checker has not run yet.
               Path touched: `CLAUDE.md`, which is new, in worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/394-claude-md`.
               Bar: the repo states no build, test or format commands, and `CLAUDE.md` now says so itself. `git status --short` shows only `?? CLAUDE.md`, and `git diff --check` is clean. The bar is the standards plus the acceptance condition.
               Skipped from a method skill: nothing. `/writing-for-agents` was read from `/nix/store/shg018ki8icxyv5n3flxakvnpqqygw7l-claude-code-mattpocock-skills-patched/skills/productivity/writing-for-agents/SKILL.md`.
               Files other nodes are written against: none moved.
               Proposed commit message:
                 Add a repo CLAUDE.md stating what the repo is, its bar, standards, rules for skill files, worktree route and traps

                 Node: graph-workflow/394

RETROSPECTIVE:
(1) What I had to hunt for:
- The heading for the full worktree steps. I first used the phrase *Landing policy*, then found that the section heading is `## Landing an implementation node's work`, and that *How the worktree is made* is a passage inside it. I found this by grepping `map-manager-only.md`.
- Where `/writing-for-agents` lives. I found it by running `find` over the filesystem, in the nix store.
- `nothing-pointed-me-at-it`: per the (j) derivation run 2026-10-07 (for scale only), 4 earlier retrospectives carry this item: 135, 178, 385, 389, 40.

(2) What arrived that I did not need:
- `map-read-whole-for-a-few-items`: I read `map.md` (about 4,000 words, 2026-10-07, for scale only) for two blocks in `## Notes`. Per (j), 19 earlier retrospectives carry this item, including 205, 214, 386-393, 40 and 41.
- The contract's long handover-search instructions cost little here.

(3) What would have made this node easier:
- A spawn line saying that `.gitignore` covers only graph-workflow's worktrees. Clause 6 assumed otherwise.

(4) What was stale, wrong or contradicted:
- `condition-states-effort-fact-as-general` (new): clause 6 states that `.scratch/<effort>/worktrees/...` is ignored, but only graph-workflow's is.
- `.gitignore`'s first comment cites `map-manager-only.md`, "Landing an implementation node's work". That is still a valid heading, so this is not stale.
- The rules file's bar paragraph is now stale, as reported under INVALIDATIONS.
`````

## Flags

`394.1` `ASSUMPTION` — CLAUDE.md tells a new effort to check that `.gitignore` covers its worktrees directory. *(The worker's full text is under its handover's `FLAGS`.)*
