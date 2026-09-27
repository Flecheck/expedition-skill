# Write the cascade pass's worker contract

Type: implementation
Status: resolved

## Question

The pass now has a design and no contract. Write the standalone skill file its two roles are dispatched to,
in the shape of the six contracts already shipped.

Reported by [Cascade pass mechanics](15-cascade-pass-mechanics.md)'s worker, which wrote the acceptance
condition below. It is the second of the two nodes that node's answer required, and it is the one that makes
the design executable rather than recorded.

**Blockers: none. Sequencing only** — it creates a new directory under `.claude/skills/` and touches no
existing file, so it collides with nothing, but the code slot is exclusive.

## Acceptance condition

One new file exists — `.claude/skills/expedition-cascade/SKILL.md` — carrying YAML frontmatter with
`name: expedition-cascade` and a one-line `description`, in the same frontmatter shape as the sibling
files already under `.claude/skills/expedition-*/SKILL.md`. No existing file in the repository changes,
and no file under `.scratch/` changes.

The file is a worker contract: instructions addressed to the agent that will follow it, in the voice of
`.claude/skills/expedition-checker/SKILL.md`, carrying no reasoning about why it says what it says and no
history of how it was decided. It stands alone as a file and does not depend on any other skill being
invoked. It covers two roles of one pass and states which role a given spawn is dispatching. It contains
all of the following:

1. **Its own vocabulary, defined in the file.** At minimum: node, manager, worker, handover, flag,
   resolve, supersede, acceptance condition, code slot. It states that a node's identity is a sequential
   number that never changes and its name is free-form.
2. **The triage role.** Its input is one resolved node's answer plus an inventory of every node in the
   effort that has landed code — one line each carrying that node's number, its name, and the paths its
   commit touched. Its job is to decide which of those landed nodes that answer may have made stale. It
   reads no product code. Its output is a list of node numbers, and the file states that the empty list is
   the ordinary result and a success rather than a failure to find something.
3. **The per-candidate role.** Its input is one landed node — its answer, its commits, and its files. Its
   job is to judge whether that node's landed code still agrees with that node's own answer. It reads
   product code and modifies none.
4. **Neither role edits product code, and neither writes any file.** The file says this in as many words
   for both roles, and says that what the agent returns is text the manager writes.
5. **What it returns when it finds something is a node to be created**, described so its reader can write
   one: a name, a kind, the question, the blocking edges, and — where the kind is `implementation` — an
   acceptance condition the agent writes itself. The file states that the agent reports an
   `implementation` node where what the fix must be is determined, and a `grilling` or `research` node
   where it is not yet clear what the fix should be.
6. **The exact shape of what it returns**, with every part named, and a statement that a part it has
   nothing for is written `none` in full rather than left off.
7. **The self-containment rule for any acceptance condition it writes, written into this file rather than
   pointed at.** Everything needed to judge whether the work is done is in the condition, and the
   condition's reader never goes anywhere else to find out what it demands; that reader is a second,
   independent, read-only agent handed the condition as text, which has not read the node and does not
   read the effort's record at all. A path may say where the work must land. What may never sit outside
   the text is the demand itself — *as decided at node NN*, *the wording agreed earlier* — because each
   sends its reader away to learn what is being asked. Material genuinely held elsewhere is copied into
   the condition. A demand that quantifies over the whole record — that the work contradicts no decision,
   that everything in it traces back to one — belongs in no condition at all, there being no bounded
   material to bring inside the text. The file also tells its reader to read what it wrote back against
   those four points before handing it over.
8. **The code slot.** The file states that the per-candidate role does not run while another agent is
   modifying product code, that occupancy is discovered from the working tree, and that waiting costs
   nothing because what the pass produces is a queued node rather than an edit. It states that the triage
   role reads no product code and never waits.
9. **It raises no flag**, and where it cannot judge — a tree in flux, a file it cannot read — it says so
   in what it returns and reports no node.
10. The tree meets the bar.

*The manager's note, 2026-09-27:* [node 109](109-carry-the-extent-rule-into-the-shipped-files.md)'s worker reports that this node's clause 7 builds the cascade contract to read back against "those four points", while the five worker contracts now carry a fifth point, the extent rule, and read back against "the five points above". Adding the fifth point here is a new demand, so it was not filed as an amendment; it goes to the human when this node is next taken up.

## Interview

### The manager's question on the fifth point, 2026-09-27

*The manager's own raise, put to the human.* ASK: "Should node 44's condition gain the fifth point, stated in the new contract's own text as the five contracts now carry it, with its read-back count becoming five?" RECOMMENDED: "Yes. Add it as one clause beside clause 7, worded after the bullet the five contracts now carry, and have the read-back say "the five points". I'll write it as an amendment carrying its own flag, and every word will come from the landed text of node 109 (`8c1053b`)."

The human, `verbatim`: *"ok"*. The manager reads it as taking the recommendation, the only option the question asked them to confirm.

## Amendment by the human, 2026-09-27

*Written by the manager on the human's "ok" above. Every word is fixed by the five worker contracts as landed by [node 109](109-carry-the-extent-rule-into-the-shipped-files.md) at `8c1053b`; the new clause quotes the grilling contract's bullet, which is identical in all five.*

- **A new clause, 7a, beside clause 7.** "The extent rule for any acceptance condition it writes, written into this file rather than pointed at, carrying the content of this bullet from the five worker contracts: "Where the condition's scope came from a search, state that search beside the list of files, and never in place of it. State exactly one of three: the command and what it returned when you ran it; where no command fits, the smallest set that provably contains every instance, and how you computed it; or that the scope came from no search, because the work creates a file or the named places are the work rather than instances of a defect. A condition addressing a defect with instances that states none of the three is malformed. Run the command over the working tree, and never over the effort's own record. Write into the condition that an instance the search reaches outside the list is reported and not edited. The condition's readers cannot go and look at how its scope was found, so the condition tells them.""
- **Clause 7's read-back.** Where clause 7 has the contract read back against "those four points", read "the five points", the fifth being clause 7a.

## Answer

The cascade pass ships as `expedition-cascade`: triage returns candidate landed nodes, empty being ordinary; per-candidate compares landed code with its answer and hands back nodes to mint.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker failed it on run 1 on the bar and passed it on run 2 after one correction round. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `c64a0e3`. Flags 44.1, 44.2, 44.3 settle at the node closing report.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      Write the cascade pass's worker contract

ANSWER:        The cascade pass's worker contract ships as `.claude/skills/expedition-cascade/SKILL.md`. It uses the sibling contracts' frontmatter shape (`name: expedition-cascade`, and a one-line description that follows the siblings' "…worker contract for an expedition. Read it when a spawn names it."). It is written in the checker contract's voice and wrapped at 105 columns like its siblings. It stands alone and invokes no other skill. Its sections, in order:
               - An opening that names the two roles, **triage** and **per-candidate**. The spawn names the role. A spawn that names neither or both gets back the single line `ROLE: not named`.
               - `## Words used exactly`: node (its identity is a sequential number that never changes, and its name is free-form), manager, worker, handover, flag, resolve, supersede, landed node, acceptance condition, the bar, checker and code slot.
               - `## Hard rules`, which apply to both roles: edit no product code, write no file, the handover is text that the manager writes, every act on the graph belongs to the manager, raise no flag (where it cannot judge, say so and report no node), no contact with the human, and output written for the manager.
               - `## Triage`. It is given one resolved answer and the landed-code inventory (number, name and paths touched for each landed node). It reads no product code and never waits for a slot. It hands back `ROLE`, `RESOLVED`, `CANDIDATES` and `CANNOT JUDGE`. The empty list, `CANDIDATES: none`, is stated to be the ordinary result and a success.
               - `## Per-candidate`. It is given one landed node: its answer as the node now holds it, annotations included; its commits by `git log --grep '^Node: <effort>/<NN>$'`, with the reason for the anchors; and its files. It reads product code in the main checkout and modifies none. It hands back `ROLE`, `CANDIDATE`, `AGREES`, `DEPARTURES`, `NEW NODES` and `CANNOT JUDGE`. A node block has `NAME`, `KIND`, `QUESTION`, `BLOCKED BY` and `ACCEPTANCE CONDITION`. The kind is `implementation`, with a condition it writes itself, where the fix is determined. Where the fix is not yet clear it is `grilling` for a decision only the human can make, or `research` for a fact from outside the working directory.
               - `### The code slot`. Before reading any product code, the agent counts the live worktrees, one per claimed implementation node. If any slot is occupied it reads nothing and hands back `CANNOT JUDGE` with "a code slot is occupied" and every other part `none`. The section says waiting costs nothing because the pass produces a queued node rather than an edit.
               - `### The acceptance condition you write`. It carries the self-containment rule and the five points, copied from the worker contracts' bullets. The pointer examples are *as decided at node NN* and *the wording agreed earlier*. A demand about the whole record is left out of the condition, because the cascade handover has no `INVALIDATIONS` part. The extent rule is the fifth point, word for word. Then the read-back "against the five points above".
               Calls a later reader would otherwise have to re-derive:
               - The noun is "handover" and the verb "hand back", never "return", because the glossary's `Handover` entry refuses "return".
               - Occupancy follows the glossary (count the live worktrees), not the condition's older "from the working tree".
               - "Waiting" is carried out as an immediate `CANNOT JUDGE` handover, since an agent cannot usefully sleep.
               - Joining a defect to an open node is left out, because the per-candidate agent's input does not include the open nodes.
               No existing file changed.

INDEX LINE:    The cascade pass ships as `expedition-cascade`: triage returns candidate landed nodes, empty being ordinary; per-candidate compares landed code with its answer and hands back nodes to mint.

FLAGS:         ASSUMPTION: Clause 8 asks the file to say occupancy "is discovered from the working tree". The glossary's `Code slot` entry now says occupancy is found "by counting the live worktrees, one per claimed implementation node, rather than by inspecting the working tree for uncommitted changes". I wrote "count the live worktrees … That count is how occupancy is discovered from the working trees", which meets the clause without contradicting the glossary, as the manager's note directed (work to what the tree says). Also, because implementation workers now write only their own worktrees and the per-candidate agent reads the main checkout, the clause's premise that the tree is "in flux" while a slot is held no longer holds. The wait rule is kept because the condition demands it, but it only adds delay. "Waiting" is carried out as an immediate `CANNOT JUDGE: a code slot is occupied` handover.
               Index: The cascade contract discovers slot occupancy by counting live worktrees, as the glossary now says, and turns clause 8's wait into an immediate cannot-judge handover.
               ASSUMPTION: The glossary's `Handover` entry refuses "return", so the contract calls both roles' output a handover and uses "hand back", although the condition says "returns". It keeps the condition's own words "queued node", since the refused "queue" is refused for the frontier concept. It gives the per-candidate agent the landed node's answer "as the node now holds it, with any annotation on it", so that a change a later resolution annotated onto that answer is visible. It defines three terms beyond clause 1's minimum (landed node, the bar, checker), because the text uses them.
               Index: The cascade contract says handover and hand back, not the glossary-refused "return", and hands the per-candidate agent the landed answer with its annotations.

NEW NODES:     none

INVALIDATIONS: [Cascade pass mechanics](15-cascade-pass-mechanics.md), narrowing. Its "The code slot" paragraph says occupancy is "discovered from the working tree, as it already is". The shipped contract counts live worktrees, following the glossary as it now stands. It also carries "does not run" as an immediate cannot-judge handover rather than an agent that waits.

CONDITIONS:    I searched the `## Acceptance condition` sections of every open or claimed node for `expedition-cascade`, `cascade`, `triage`, `per-candidate`, `expedition-*`, `skills/*`, "six contracts" / "six worker contracts" and "every (shipped) (worker) contract". The only match is this node's own condition. No replacements written.

MISSING FROM MAP: The map does not say whether any node owns the manager's side of the cascade: who spawns triage, what the manager does with a `CANNOT JUDGE: a code slot is occupied` handover, and when per-candidate is run again. I found node 87, "The manager's cascade duties are in neither contract" (open), by searching the node files for "cascade". I went on without it: the contract makes no claim about what the manager does next.

GATE PAYLOAD:  Checker findings: none yet (no check has run).
               Paths touched: `.claude/skills/expedition-cascade/SKILL.md` (new). Nothing else. `graph-conventions.md` and the node-346 sentence were not touched.
               Bar: I confirmed the repo against the rules file. It has no build, no tests, no formatter and no CI (root: `.claude/`, `CONTEXT.md`, `.gitignore`, `.scratch/`, and no manifest or `.github`). `.gitignore` lists the three worktree paths the record names. So the bar is its non-command half. I checked that no line in the new file exceeds 105 columns (awk: none), and grepped the text by hand against `CONTEXT.md`'s `_Avoid_` lines ("return" was found and removed). I found no difference from the recorded commands.
               Method skills: none invoked, so nothing skipped.
               Proposed commit message:
                 Ship the cascade pass's worker contract

                 Add .claude/skills/expedition-cascade/SKILL.md: the triage and
                 per-candidate roles, their handover shapes, the code-slot check by
                 live worktrees, and the self-containment rule with the extent rule
                 for any acceptance condition the pass writes.

                 Node: graph-workflow/44

RETROSPECTIVE:
1. What I had to hunt for. Whether any shipped file already dispatches to the cascade. A grep of `.claude` for "cascade" returned nothing, so nothing does. Whether a node owns the manager's side: node 87, found by grep over `nodes/`. Node 15's design, including the anchored `git log` query, the "goes and looks" and "raises no flag" grounds, and the code-slot paragraph: I first looked in decisions.md, which has only one line, and then read node 15's `## Answer`. The glossary's `Handover` _Avoid_ line refusing "return" I found only by grepping the `_Avoid_` lines after drafting. I would have missed it if I had trusted the condition's wording.
2. What arrived that this node did not need. Most of map.md (standing preferences on payloads, gates, retrospectives, worktrees, token priority): about 110 lines, of which I used the ground rules pointer and the glossary line. From the rules file I used the bar paragraph and the two rule blocks, and not the record-as-work paragraph. From the spawn, the list of recent nodes (97, 137, 327, 342, 124, 337, 343, 333) bore on nothing except 109 and the "seven parts" note. The implementation contract's gate, correction and raise sections I read only to follow them.
3. What would have made this easier. The spawn or node file could point at node 15's `## Answer` sections "Landed code is the spawned pass", "The code slot" and "Who writes, and who reads" as the design source. It could name node 87 as the manager-side counterpart. It could note that clause 8 conflicts with the glossary's `Code slot` entry, which the manager already suspected. A note that "return" is refused for "handover" would have saved one rewrite pass.
4. What was stale, wrong or contradictory. Clause 8 says "discovered from the working tree", but the glossary says count live worktrees rather than inspect the working tree. The premise of clause 8 ("a tree … in flux") no longer holds, because implementation workers write only their own worktrees and the manager contract says every non-implementation worker reads a consistent snapshot of the main checkout. The condition's "returns" collides with the glossary's refusal of "return". The node's Question says "in the shape of the six contracts already shipped", but there are now five worker contracts plus the checker, with other skills beside them. Node 15's answer says the triage agent "goes and looks", but its only named inputs are the answer and the inventory. I wrote it to work from those two alone.

## Review

### Checker run 1 — `FAIL`, the bar

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 346's check, and resumed again after it stopped on the session's usage limit; the condition reached it as a verbatim copy in `$TMPDIR/c44.md`.*

> FAIL: the bar
>
> This is the check of node 44, "Write the cascade pass's worker contract". The work is the untracked file `.claude/skills/expedition-cascade/SKILL.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/44-cascade`, on base 353689f. I read the whole condition in `/tmp/claude-1000/c44.md`, with the human's 2026-09-27 amendment (clause 7a, and the read-back against "the five points"). I read the file with `cat -n`. It meets every part of the acceptance condition. It fails the bar on one finding against ground rule 1.
>
> ### Finding 1 (the bar: ground rule 1, "Nothing in the shipped files may assume this repo, this machine, or a toolchain. Prefer properties that are discovered over commands that are declared.")
>
> - **Instances.** Found with `grep -rnE '`git [a-z]' --include=*.md .claude/skills/`. It returns exactly two lines, both in this file:
>   - Line 96: "its commits, found by `git log --grep '^Node: <effort>/<NN>$'`, anchored at both ends because an unanchored `Node: <effort>/4` also matches 40 to 49 and 400 upward".
>   - Line 102: "count the live worktrees, for instance with `git worktree list`".
>   - Both declare a command for a particular version-control tool. No other shipped file under `.claude/skills/` names a `git` command. The manager contract and graph-conventions state the commit trailer `Node: <effort>/<NN>` as a property only.
>   - The condition does not demand either command. Clause 8 asks only that occupancy "is discovered from the working tree".
>   - Both properties can be stated without a command. For line 96: the commits whose message carries the line `Node: <effort>/<NN>`, matched as a whole line, so that `4` does not also match 40–49 or 400 upward. For line 102: count the live worktrees beside the main checkout.
> - **Form.** A command declared for a particular tool (here `git …`) in this shipped contract, where a stated property would do.
> - **Extent.** `grep -nE '`git [a-z]' .claude/skills/expedition-cascade/SKILL.md`, which lists 2 lines.
>
> ### The acceptance condition: all met
>
> - **Scope and frontmatter.** Met.
>   - `git status --short --untracked-files=all` shows only `?? .claude/skills/expedition-cascade/SKILL.md`. No existing file changed, and nothing under `.scratch/` changed.
>   - The frontmatter is `name: expedition-cascade` plus a one-line `description`, the same shape as `expedition-checker/SKILL.md`.
> - **Worker contract, voice, stands alone, names the role.** Met.
>   - It addresses its reader as "you", as the checker contract does.
>   - It has no history of how anything was decided. Its few "because" clauses are rules or triggers that other parts of the condition demand, or that it shares with the sibling contracts. I read "no reasoning about why it says what it says" as ruling out design rationale, since the checker contract's own voice also gives reasons.
>   - It depends on no other skill.
>   - "Your spawn names the role you are in." Where the spawn names neither role or both, the worker hands back `ROLE: not named`.
> - **Clause 1, vocabulary.** Met. `## Words used exactly` defines node, manager, worker, handover, flag, resolve, supersede, acceptance condition and code slot. It also defines landed node, the bar and checker. The node entry says "Its identity is a sequential number that never changes, and its name is free-form."
> - **Clause 2, triage.** Met.
>   - Input: one resolved node's answer, and an inventory with one line per landed node giving number, name and paths.
>   - Job: decide which landed nodes the answer may have made stale.
>   - "Read no product code".
>   - `CANDIDATES` lists node numbers, with names and a reason.
>   - "The empty list, `CANDIDATES: none`, is the ordinary result. It is a success, and not a failure to find something."
> - **Clause 3, per-candidate.** Met. Input: one landed node's answer, its commits and its files. It judges whether the landed code agrees with the answer, reads product code, and says "Modify none of it".
> - **Clause 4.** Met. Hard rules 1 and 2 say "Edit no product code, in either role" and "Write no file, in either role. Your whole output is the handover, which is text, and the manager writes it onto the graph." Each role's section repeats both.
> - **Clause 5.** Met.
>   - `### A node you report` gives NAME, KIND, QUESTION, BLOCKED BY, and an ACCEPTANCE CONDITION for implementation nodes, written by the worker.
>   - It says to report "an `implementation` node where what the fix must be is determined … Either of those two kinds [grilling, research] fits wherever it is not yet clear what the fix should be."
> - **Clause 6.** Met. Both handover blocks name every part and say "Write every part, with `none` in full for a part you have nothing for."
> - **Clause 7, self-containment written in.** Met.
>   - It defines the checker as the reader, handed the condition as text, which has not read the node or the record.
>   - It says a path may say where the work lands.
>   - It says the demand itself stays in the text, never behind *as decided at node NN* or *the wording agreed earlier*, "Each such pointer sends its reader away".
>   - Material held elsewhere is copied in, and only the bar is exempt.
>   - A record-wide demand is kept out, "No bounded material exists to bring inside the text".
>   - The read-back is "against the five points above".
> - **Clause 7a.** Met. Using the same awk range to extract the extent bullet from `expedition-grilling/SKILL.md` and from this file, `cmp` reports them byte-identical.
> - **Clause 8, code slot.** Met.
>   - The per-candidate role reads no product code while any slot is occupied.
>   - Occupancy is found by counting live worktrees: "That count is how occupancy is discovered from the working trees".
>   - "Waiting costs nothing: what this pass produces is a queued node rather than an edit".
>   - The triage role: "Never wait for the code slot. You read no product code".
>   - The condition says "from the working tree". The file counts worktrees, which matches the glossary's **Code slot** entry ("counting the live worktrees … rather than by inspecting the working tree for uncommitted changes"). I read that as meeting the clause.
> - **Clause 9.** Met. Hard rule 4 says "Raise no flag. Where you cannot judge, say so in your handover, and report no node". The per-candidate role repeats this for "the tree is in flux or a file will not read".
> - **Clause 10, the bar.** Fails on Finding 1, as reported above.
>
> ### The bar
>
> - The repo has no build, tests, formatter or CI, so there are no commands to run.
> - The file has no trailing whitespace. Its only lines over 105 characters are in its fenced handover shapes, as in the sibling contracts.
>
> ### Standards
>
> As in my earlier checks, I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`.
>
> - **Bore on the work:**
>   - Ground rule 1: breached, Finding 1.
>   - Ground rules 2 and 3: met. The contract stands alone, and it tells the worker to reach the human only through the manager.
>   - `CONTEXT.md` `_Avoid_` lines: nothing found, and the file uses the glossary's terms.
>   - The writing rules: bold only where terms are defined, and prohibitions stand beside their positives.
>   - `/writing-for-agents`: the roles are split by branch, and nothing else found.
> - **Did not bear:** `/coding-principles` and `/naming`.
> - **Reviewing skill:** none is named, so I ran none.
>
> NOT COVERED:
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The worktree shows no `.scratch/` change. What the main tree's record holds is outside what I was given.

*The manager's note:* a `FAIL` on the bar sends the work back to the build; the worker is resumed for a correction round with the finding pasted.

### Correction round 1, 2026-09-27

*The worker's own text, pasted as handed back.*

CORRECTION ROUND 1 — node 44, "Write the cascade pass's worker contract"

WHAT I CHANGED (for Finding 1, the bar: ground rule 1). Both git commands are gone and each is now stated as a property. The only file edited is `.claude/skills/expedition-cascade/SKILL.md`, under `## Per-candidate`:
- `### What you are given`, the commits bullet. It no longer contains `git log --grep '^Node: <effort>/<NN>$'`. It now reads: "its commits, which are the commits whose message carries the line `Node: <effort>/<NN>`, matched as a whole line so that `Node: <effort>/4` does not also match 40 to 49 or 400 upward".
- `### The code slot`, first sentence. It no longer contains "for instance with `git worktree list`". It now reads: "count the live worktrees beside the main checkout. Each such worktree is one claimed implementation node, and one occupied code slot." I rewrapped the rest of that paragraph to the 105-column width. Its words did not change.

Checks after the edit:
- The checker's extent command, `grep -nE '`git [a-z]' .claude/skills/expedition-cascade/SKILL.md`, returns nothing.
- Over all of `.claude/skills/`, `grep -rnE '`git [a-z]' --include=*.md .claude/skills/` returns nothing.
- No line is longer than 105 columns.

DOES IT TOUCH ANYTHING THE ACCEPTANCE CONDITION NAMES. Yes, in wording only, in two places:
- Clause 3, the per-candidate role's input ("its commits"). The input is unchanged, and only the way it is identified is now stated as a property.
- Clause 8, the code slot. The file still says that the per-candidate role does not run while another agent is modifying product code, that occupancy is discovered from the working trees by counting live worktrees, and that waiting costs nothing because what the pass produces is a queued node rather than an edit. It still says triage never waits.
Nothing else changed.

EFFECT ON THE HANDOVER I ALREADY GAVE. Two parts are affected, and the rest stands as handed back:
- In `ANSWER`, the per-candidate commits clause should read "its commits, being those whose message carries the line `Node: <effort>/<NN>`, matched as a whole line, with the reason for matching whole lines". It should replace "its commits by `git log --grep '^Node: <effort>/<NN>$'`, with the reason for the anchors".
- In `FLAGS`, the first ASSUMPTION's wording about counting live worktrees still holds, and no longer names a command.

GATE PAYLOAD:
- Checker findings and what I changed: Finding 1, both instances replaced by stated properties, as above.
- Paths touched: `.claude/skills/expedition-cascade/SKILL.md` (new, uncommitted). No other path.
- Proposed commit message, the same as before:

  Ship the cascade pass's worker contract

  Add .claude/skills/expedition-cascade/SKILL.md: the triage and
  per-candidate roles, their handover shapes, the code-slot check by
  live worktrees, and the self-containment rule with the extent rule
  for any acceptance condition the pass writes.

  Node: graph-workflow/44

### Checker run 2 — `PASS`

*The checker's own text, pasted, 2026-09-27. The same checker, resumed for the re-check.*

> PASS
>
> This is the re-check of node 44, "Write the cascade pass's worker contract", after correction round 1. The work is still the untracked file `.claude/skills/expedition-cascade/SKILL.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/44-cascade`, on base 353689f. The condition is the same text, in `/tmp/claude-1000/c44.md`.
>
> **No standard moved.**
> - The only path in the work is still that one file (`git status --short --untracked-files=all` shows only it), and it is not a standard.
> - The standards file `.scratch/graph-workflow/map-implementation-rules.md` was last modified at 20:12:14. The work was last modified at 21:02:02. My first check read the standards file as it stands, with the same five ground rules.
>
> **What changed, and how I established it.**
> - The file is still 180 lines. Comparing it against my first reading, only `## Per-candidate` → `### What you are given` and `### The code slot` differ. Every other line is unchanged.
> - The commits bullet now reads: "its commits, which are the commits whose message carries the line `Node: <effort>/<NN>`, matched as a whole line so that `Node: <effort>/4` does not also match 40 to 49 or 400 upward".
> - The code-slot paragraph now reads: "count the live worktrees beside the main checkout. Each such worktree is one claimed implementation node, and one occupied code slot." The rest of that paragraph has the same words, rewrapped.
> - This matches what the worker reports.
>
> **Finding 1 (the bar, ground rule 1): resolved.**
> - `grep -nE '`git [a-z]|\bgit\b'` over the file finds nothing.
> - `grep -rnE '`git [a-z]' --include=*.md .claude/skills/` finds nothing.
> - Both properties are now stated as properties, with no tool named.
>
> **Re-established parts of the condition.**
> - **Clause 3:** met. The per-candidate input is still one landed node's answer, its commits and its files.
> - **Clause 8:** met. The per-candidate role still reads no product code while any slot is occupied. "That count is how occupancy is discovered from the working trees" is kept, as is "Waiting costs nothing: what this pass produces is a queued node rather than an edit". The triage role's "Never wait for the code slot" is unchanged.
> - **Every other part:** it stands as I established it in my first check, because the text it rests on is unchanged. That covers scope, frontmatter, voice, stands-alone, role naming, and clauses 1, 2, 4–7, 7a and 9.
>
> **The bar, re-run in full.**
> - The repo has no build, tests, formatter or CI, so there are no commands to run.
> - `git status` shows only the one file, so no other file changed.
> - The file has no trailing whitespace.
> - `awk 'length>105'` prints nothing.
>
> **Standards.** As in my earlier checks, I read only the standards in `map-implementation-rules.md`.
> - Ground rule 1 is now met, and ground rules 2 and 3 still hold.
> - The `CONTEXT.md` `_Avoid_` lines: nothing found in the changed text.
> - The writing rules and `/writing-for-agents`: nothing found.
> - `/coding-principles` and `/naming` did not bear on the work.
> - No reviewing skill is named, so I ran none.
>
> NOT COVERED:
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The worktree shows no `.scratch/` change. What the main tree's record holds is outside what I was given.

### Gate — approve, `standing yes`, 2026-09-27

Taken under the standing yes recorded in `map.md`'s `## Notes` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 2 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and its one NOT COVERED item is the worker's bookkeeping. This settles none of the node's flags; they settle at the node closing report.

## Flags

`44.1` `ASSUMPTION` **· settled** — *The manager's own entry.* The human's terse "ok" to the manager's question on the fifth point was read as taking its recommendation, and the extent rule was added to this node's condition as clause 7a with a five-point read-back.

`44.2` `ASSUMPTION` **· settled** — *From attempt 1's handover.* Clause 8 asks the file to say occupancy "is discovered from the working tree". The glossary's `Code slot` entry now says occupancy is found "by counting the live worktrees, one per claimed implementation node, rather than by inspecting the working tree for uncommitted changes". I wrote "count the live worktrees … That count is how occupancy is discovered from the working trees", which meets the clause without contradicting the glossary, as the manager's note directed (work to what the tree says). Also, because implementation workers now write only their own worktrees and the per-candidate agent reads the main checkout, the clause's premise that the tree is "in flux" while a slot is held no longer holds. The wait rule is kept because the condition demands it, but it only adds delay. "Waiting" is carried out as an immediate `CANNOT JUDGE: a code slot is occupied` handover. — The cascade contract discovers slot occupancy by counting live worktrees, as the glossary now says, and turns clause 8's wait into an immediate cannot-judge handover.

`44.3` `ASSUMPTION` **· settled** — *From attempt 1's handover.* The glossary's `Handover` entry refuses "return", so the contract calls both roles' output a handover and uses "hand back", although the condition says "returns". It keeps the condition's own words "queued node", since the refused "queue" is refused for the frontier concept. It gives the per-candidate agent the landed node's answer "as the node now holds it, with any annotation on it", so that a change a later resolution annotated onto that answer is visible. It defines three terms beyond clause 1's minimum (landed node, the bar, checker), because the text uses them. — The cascade contract says handover and hand back, not the glossary-refused "return", and hands the per-candidate agent the landed answer with its annotations.

*The manager's note, 2026-09-27:* flags 44.1, 44.2, 44.3 settle at the node closing report that closes this node, which names its gate as taken under the standing yes.
