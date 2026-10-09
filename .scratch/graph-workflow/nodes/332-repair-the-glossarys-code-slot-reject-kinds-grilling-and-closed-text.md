# Repair the glossary's code-slot, reject, kinds-of-node, grilling and closed text, and add its starting-an-effort section

Type: implementation
Status: resolved
Supersedes: 90, 92, 134, 247, 81
Blocked by: none

## Question

Four open nodes each change a few lines of `CONTEXT.md`: 90 (the Closed entry), 92 (the Code slot entry), 134 (the kinds-of-node paragraph and the grilling entry) and 247 (a new starting-an-effort section). Do all four in one piece of work. Supersedes 90, 92, 134 and 247.

*Proposed by [node 328](328-group-the-open-nodes-against-the-glossary.md)'s worker and filed by the manager, on the human's "ok" to node 328's merge, its conflicts' recommendations and the manager's picks. Node 81's glossary part (its entries 1 and 2) joins this node under C1(a); its prototype-contract line goes to the worker-contracts merge. Sequencing, in the worker's words: "claim it after node 106 lands and before node 56." Node 106 has landed (`64db5aa`).*

## Acceptance condition

*Written by node 328's worker. The manager applied the two amendments that worker wrote for the human's options C1(a) and C2(a), as its note directs ("C1(a) inserts the text given there and widens clause 13's list to include the Reject definition. C2(a) replaces clause 4's second bullet."); each is tagged where it lands. The manager numbered the Reject clause `1a` so the worker's numbering stands.*

> **Which file.** Exactly one file changes: `CONTEXT.md` at the repository root. No other file changes, and no file under `.scratch/` changes. Where this work finds something outside that file that needs changing, it reports it in the handover and does not edit it. *(90, 92, 134, 247)*
>
> **Baselines, to be re-run and reported.**
> - At commit `64db5aa`, `grep -c '^\*\*.*\*\*:$' CONTEXT.md` returns 51 and `grep -c '^_Avoid_' CONTEXT.md` returns 41. This work raises each count by exactly two. Where either count has moved before the work starts, report the starting count. *(247)*
> - At that commit, `grep -rn -i "chart" .claude/skills/ CONTEXT.md` returns nothing. *(247)*
>
> 1. **Code slot.** The entry headed `**Code slot**:` under `## Working a node` currently reads: "The right to modify product code, held by one worker at a time. Occupancy is discovered from the working tree rather than recorded, so a dying worker leaves nothing behind to clean up."
>    - After the work it no longer says the right is held "by one worker at a time", and no longer says occupancy is discovered from the working tree.
>    - It states that how many code slots an effort runs is that effort's own setting, one worker to a slot.
>    - It states that a slot's occupancy is discovered by counting the live worktrees, one per claimed implementation node, rather than by inspecting the working tree for uncommitted changes.
>    - It also states that the number of slots may be more than one. The current second sentence's claim that a dying worker leaves nothing behind to clean up does not survive. *(81, entry 1, by C1(a))*
>    - Its `_Avoid_` line, "write lock, code lock — there is no lock", is left exactly as it stands. *(92)*
> 1a. **Reject.** **Reject** (`## Landing code`) currently contains the sentences 'On a reject the node does not resolve, and the working tree is cleaned. What is kept is the discovery.' After the work, the entry no longer says the working tree is cleaned. It says that on a reject the manager removes that node's worktree and deletes its branch, and that where the human asks for the work to be kept, it is committed onto that branch before the directory is removed. It still says that the node does not resolve and that what is kept is the discovery. 'The human's finding at the gate that implementing the node revealed that its code should not exist.', 'A reject is not a verdict on quality: a node whose code is merely wrong takes a correction round.', 'The word is the human's alone; the checker's outcomes are `PASS` and `FAIL`.' and `_Avoid_: refuse, discard, abandon (which names losing the code, not learning why)` are left exactly as they stand. *(81, entry 2, as amended from node 302, by C1(a))*
> 2. **The kinds of node.** Under `## The five kinds of node`, the paragraph before the first entry reads: "Each kind names what its worker does. Three of the kinds name a skill the worker invokes."
>    - After the work, nothing in that paragraph claims that any number of the kinds names a skill the worker invokes. Whatever replaces the second sentence, if anything, is true of the shipped contracts as they stand when the work is done.
>    - That state is tested by a scan of `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md` and `.claude/skills/expedition-checker/SKILL.md` for the strings `/grilling`, `/domain-modeling`, `/coding-principles`, `/naming`, `/research`, `/prototype` and `mattpocock`. It returned nothing at `64db5aa`. Re-run it and report what it returns.
>    - The paragraph's first sentence is left as it stands. *(134, both conditions)*
> 3. **grilling.** The entry headed `**grilling**:` currently reads: "A decision only the human can make, reached by interviewing them. Its worker may put several of its questions in one payload. Only questions that are independent of each other share a payload."
>    - Its definition may be reworded. After the work it states all four of these:
>      - a decision only the human can make, reached by interviewing them;
>      - its worker may put several of its own questions in one payload;
>      - two questions share a payload only where neither's answer depends on the other's;
>      - a question whose answer depends on another question in that payload is held for a later payload.
>    - It does not say the human is interviewed one question at a time.
>    - Its `_Avoid_` line, "decision, question, interview", is left exactly as it stands. *(134, both conditions)*
> 4. **Closed.** The entry headed `**Closed**:` under `## Closing an effort` currently reads: "The human's declaration that an effort is over. Only the human closes one; the manager reports that the conditions hold and nothing more. Most efforts are never closed, and that is a legitimate steady state."
>    - Its third sentence is replaced. The replacement makes no claim, in any wording, about how often efforts are closed: not that most are, not that most are not, and not that the proportion is unknown.
>    - In its place, it states that an effort whose destination says it is not expected to end, and whose frontier never empties, is in a legitimate steady state rather than a stalled one, and is not to be treated as a defect. *(90, as amended by C2(a))*
>    - The first two sentences and the `_Avoid_` line, "done, finished, complete", are left exactly as they stand. *(90)*
> 5. **A new section.** The file gains one new section headed `## Starting an effort`, placed immediately before the existing section headed `## Closing an effort`. No other section moves. *(247)*
> 6. That section holds exactly two term entries and nothing else. Each is written in the same shape as the entries already in the file: a line holding only the headword in bold followed by a colon, then the definition, then a line beginning `_Avoid_:`. *(247)*
> 7. **Starting an effort.** The first entry's headword is `Starting an effort`. Its definition states all of the following:
>    - it is the act that creates an effort;
>    - the manager performs it, and it happens before the graph exists;
>    - it produces the effort's files and its first nodes;
>    - it has two inputs, a conversation with the human or a directory of work that already exists, and the input is the only thing the two ways of starting differ in. *(247)*
> 8. That entry's `_Avoid_` line refuses `charting`, `kickoff`, `onboarding`, `bootstrap`, `setup` and `init`. Against `charting` it gives a reason with both of these halves:
>    - this workflow's cartographic metaphor stops at the map, and every act beneath it is described plainly;
>    - the act the word names is what the file's existing `Expedition` entry says the workflow's ancestor does, "works out what the work is", rather than anything this workflow performs. *(247)*
> 9. **Adoption.** The second entry's headword is `Adoption`. Its definition states all of the following:
>    - it is starting an effort from a directory of work that already exists;
>    - it is a way of starting an effort, not a kind of node;
>    - it carries steps the other input does not, naming at least these five: taking the effort's name from the directory that already exists; resolving any reserved graph name the directory already uses for something else; deriving the map from the record the effort already wrote, rather than from a conversation; declaring the label vocabulary from the foreign label families; and minting the bulk import as `precondition` nodes. *(247)*
> 10. That entry's `_Avoid_` line refuses `migration`, `import`, `onboarding` and `port`. Against `migration` it gives the reason that the word names moving data rather than taking on an effort. Against `import` it gives the reason that importing is one step inside adoption rather than the act itself. *(247)*
> 11. No entry anywhere in the file gives a name to the way of starting whose input is a conversation. That way is referred to by its input, and never by a word of its own, in the new section and everywhere else in the file. *(247)*
> 12. The word `charting` appears in the file in exactly one place, the `_Avoid_` line of clause 8. No other form of the word *chart* appears anywhere in the file. *(247)*
> 13. **Nothing else changes.** Only these may change: the definition lines of **Code slot** (clause 1), the paragraph under `## The five kinds of node` (clause 2), the definition lines of **grilling** (clause 3), the third sentence of **Closed** (clause 4) and the definition lines of **Reject** (clause 1a). The only addition is the new section (clauses 5 to 12). Every other line is byte-identical to the file as it stood when the work was claimed. In particular:
>     - the `Expedition` entry is unchanged;
>     - no entry is removed and no `_Avoid_` line is removed or changed;
>     - no section other than the new one is added or moved.
>
>     *(90, 92 clause 3, 134, 247 clauses 1 and 8)*
> 14. The work leaves the tree meeting the bar. *(90, 92, 134, 247)*

## Answer

The glossary's Code slot, Reject, kinds-of-node paragraph, grilling and Closed entries now match the settled rules, and a new Starting an effort section defines the plain act and Adoption.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The human approved. The work landed as commit `c365a75`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      Repair the glossary's code-slot, reject, kinds-of-node, grilling and closed text, and add its starting-an-effort section

ANSWER:        `CONTEXT.md` at the repo root is the only file changed, uncommitted in worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/332-glossary-merge`. The existing wrap width is kept: greedy wrapping, no line over 102 characters, which is the file's own maximum.
- **Code slot** (clause 1). The definition now says the slot is the right to modify product code. How many slots an effort runs is that effort's own setting, one worker to a slot, and the number may be more than one. Occupancy is found by counting the live worktrees, one per claimed implementation node, not by inspecting the working tree for uncommitted changes. The dying-worker sentence is gone. The `_Avoid_` line is unchanged.
- **Reject** (clause 1a). "the working tree is cleaned" is replaced. The entry now says the manager removes that node's worktree and deletes its branch, and that where the human asks for the work to be kept, it is committed onto that branch before the directory is removed. The first line ("The human's finding…"), "A reject is not a verdict on quality…", "What is kept is the discovery.", "The word is the human's alone…" and the `_Avoid_` line are unchanged in text. Where a line changed, it is only because the text was rewrapped.
- **The five kinds of node** (clause 2). The second sentence, "Three of the kinds name a skill the worker invokes.", is deleted and nothing replaces it. So the paragraph makes no claim about the contracts. The first sentence is unchanged.
- **grilling** (clause 3). The first line is unchanged. It now says: the worker may put several of its own questions in one payload; two questions share a payload only where neither's answer depends on the other's; and a question whose answer depends on another question in that payload is held for a later payload. It does not say one question at a time. The `_Avoid_` line is unchanged.
- **Closed** (clause 4). "Most efforts are never closed…" is replaced with this: an effort whose destination says it is not expected to end, and whose frontier never empties, is in a legitimate steady state rather than a stalled one, and is not to be treated as a defect. The replacement makes no claim about how often efforts close. Sentences 1 and 2 and the `_Avoid_` line are unchanged in text, though line 2 was rewrapped.
- **`## Starting an effort`** (clauses 5–12). This is a new section placed immediately before `## Closing an effort`. It holds exactly two entries in the file's shape (bold headword with a colon, then the definition, then `_Avoid_:`) and nothing else.
  - `Starting an effort`: the act that creates an effort. The manager performs it before the graph exists. It produces the effort's files and first nodes. It has two inputs, a conversation with the human or a directory of work that already exists, and the input is the only thing the two ways differ in.
  - Its `_Avoid_` line refuses charting, kickoff, onboarding, bootstrap, setup and init. The reason against charting has two halves: the cartographic metaphor stops at the map and every act beneath it is described plainly; and the word names what the ancestor does when it "works out what the work is" (the phrase is quoted from the `Expedition` entry), not anything this workflow performs.
  - `Adoption`: starting an effort from a directory of work that already exists. It is a way of starting an effort, not a kind of node. It lists the five steps the conversation input does not have.
  - Its `_Avoid_` line refuses migration (it names moving data, not taking on an effort), import (importing is one step inside adoption, not the act itself), onboarding and port.
  - The conversation input has no name of its own anywhere. It is always called "starting from a conversation" or "a conversation with the human".
- **Measurements after the work.**
  - Term entries (`grep -c '^\*\*.*\*\*:$'`): 51 before, 53 after.
  - `_Avoid_` lines (`grep -c '^_Avoid_'`): 41 before, 43 after.
  - The `chart` grep over `.claude/skills/` and `CONTEXT.md` returned nothing before the work. After it, it returns one match: `CONTEXT.md` line 321, the `_Avoid_: charting` line. No other form of *chart* appears.
  - Clause 2's scan of the six worker and checker contracts for `/grilling`, `/domain-modeling`, `/coding-principles`, `/naming`, `/research`, `/prototype` and `mattpocock` returned nothing (grep exit 1), both at the start and at the end.
  - The section order is unchanged apart from the one insertion. `git diff --stat`: 1 file, +36 −8.
- **The bar.** I confirmed against the worktree that the repo has no build, no tests, no formatter and no CI. The tracked files are `.claude/`, `CONTEXT.md` and `.gitignore`, and there is no manifest or task runner. This matches `map-implementation-rules.md`, so no command was run. The remaining half was checked by hand:
  - no word refused by an `_Avoid_` line is used for its refused concept;
  - bold appears only on the new headwords;
  - the plain-English rule was applied.

INDEX LINE:    The glossary's Code slot, Reject, kinds-of-node paragraph, grilling and Closed entries now match the settled rules, and a new Starting an effort section defines the plain act and Adoption.

FLAGS:         ASSUMPTION: Reject's kept-work sentence carries an ambiguity from its source. The condition, and the landing policy in `map-manager-only.md` it was drawn from ("On reject the worktree is removed and its branch deleted; where the human asks for the work to be kept, the manager commits it onto that branch before removing the directory"), say both that the branch is deleted and that kept work is committed onto that branch. Neither says whether the branch survives in the kept case. Read literally, the commit would then be lost. I wrote the entry the way the landing policy says it, with the deletion as the ordinary case and keeping as the exception. I added no claim that the branch survives, because that is a landing-policy decision and not the glossary's. The manager may want the landing policy to say it explicitly.
               Index: The glossary's Reject entry repeats the landing policy's reject wording, which says the branch is deleted and does not say whether it survives when the human asks for the work to be kept.

NEW NODES:     none

INVALIDATIONS: none. Related staleness in this file that the condition put out of scope (clause 13), reported rather than edited:
- The **Salvage** entry still says "before the working tree is cleaned", which the new Reject wording no longer matches. Node 81 already records this as deliberately left out, pending what salvage becomes on a per-node branch, with the annotation on node 23. So this is not a new defect.
- The **Attempt** entry's "a worker that dies is replaced" contradicts the map's standing resume rule. The map already names this.

GATE PAYLOAD:  Checker findings: none yet (no checker run has reached me).
               Paths touched: `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/332-glossary-merge/CONTEXT.md` only.
               Proposed commit message:
               ```
               Repair five glossary entries and add its Starting an effort section

               Code slot states a per-effort slot count and occupancy counted from live
               worktrees. Reject says the worktree is removed and the branch deleted, with
               kept work committed onto the branch first. The kinds-of-node paragraph drops
               its claim that three kinds name a skill. grilling states when questions share
               a payload. Closed replaces its claim about how often efforts close with the
               steady state of an effort not expected to end. A new Starting an effort
               section defines the act and Adoption.

               Node: graph-workflow/332
               ```

RETROSPECTIVE:
1. **What I had to hunt for.**
   - The source for Reject's kept-work wording. I went to `map-manager-only.md` (grep "reject") to check that the condition matched the landing policy, and it did, ambiguity included.
   - Whether Salvage's staleness was already known. I grepped the nodes for "salvage" and found node 81's note.
   - The file's wrap width. I measured it with awk, because "keep the existing wrap width" named no number.
2. **What arrived that this node did not need.** Most of `map.md`. I used only the `## Notes` line on grouping related defects and the fact that the glossary is authoritative. The long standing-preferences bullets on questions, payload timing, retrospectives, token priority and resuming bore on nothing here. Of `map-implementation-rules.md`, only the bar paragraph and the five writing rules mattered. The spawn's decisions.md filter ("only the lines about the glossary") helped, and a grep was enough.
3. **What would have made this easier.**
   - Saying the wrap width as a number (102, greedy).
   - Noting in the condition, next to clause 1a, whether the branch survives when work is kept, or at least that the landing policy leaves this open.
   - Noting beside clause 13 that rewrapping a changed paragraph may alter the line of an adjacent unchanged sentence. The Closed entry's line 2 carries sentence 2's text unchanged but as a changed line. I read "byte-identical" as applying to the other entries and sentences, not to rewrapped lines inside a paragraph the clause allows to change.
4. **What was stale, wrong or contradictory.**
   - The landing policy and clause 1a both say "deletes its branch" and "committed onto that branch" without resolving the two (flagged above).
   - The Salvage and Attempt entries in `CONTEXT.md` are stale against the worktree route and the resume rule. Both are already known.
   - The map's `## Notes` still says `CONTEXT.md` holds "51 term entries and 41 `_Avoid_` lines". After this node lands that is 53 and 43, and the figure is marked dated.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-26. The checker was resumed from node 106's check.*

> PASS
>
> Node 332, "Repair the glossary's code-slot, reject, kinds-of-node, grilling and closed text, and add its starting-an-effort section", meets every clause of its acceptance condition, and the bar holds. The work rewrites five existing passages in `CONTEXT.md` and adds one new section, and nothing else changed.
>
> My contract is the main-tree checker contract, unchanged since my last check: its last commit is `76e66e3` and it has no uncommitted edits. The work is `CONTEXT.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/332-glossary-merge`, on branch `worktree-332-glossary-merge`, with HEAD and merge-base both at `64db5aa`. I read the changed path only as the work.
>
> **The work changed one of the standards, so I checked that first.** `CONTEXT.md`'s `_Avoid_` lines are one of the standards the work is held against. The edit changes none of the existing 41 `_Avoid_` lines and adds two new ones. The added lines are part of the work, so I held them against the condition, not the work against them. Every earlier `_Avoid_` line is unchanged, so the standard still stands.
>
> **Baselines, re-run as written**
> - `grep -c '^\*\*.*\*\*:$' CONTEXT.md` at `64db5aa` returns 51, and `grep -c '^_Avoid_' CONTEXT.md` returns 41. Neither had moved before the work started. Now they return 53 and 43, each up by exactly two.
> - `grep -rn -i "chart" .claude/skills/ CONTEXT.md` at `64db5aa` returns nothing, which matches the recorded return. Now it returns only the `_Avoid_` line in clause 8.
> - The skill-name scan: I searched the six named contracts for `/grilling`, `/domain-modeling`, `/coding-principles`, `/naming`, `/research`, `/prototype` and `mattpocock`. It returns nothing at `64db5aa`, which matches the recorded return, and it returns nothing now.
>
> **Clause by clause**
> - **Which file: met.** `git status --porcelain --untracked-files=all` shows only `CONTEXT.md` modified. Nothing under `.scratch/` or `.claude/` changed, which matches the worker's report.
> 1. **Code slot: met.**
>    - The definition now reads: "The right to modify product code. How many code slots an effort runs is that effort's own setting, one worker to a slot, and the number may be more than one. A slot's occupancy is discovered by counting the live worktrees, one per claimed implementation node, rather than by inspecting the working tree for uncommitted changes."
>    - "By one worker at a time" and "a dying worker leaves nothing behind to clean up" are gone.
>    - The `_Avoid_` line, "write lock, code lock — there is no lock", is unchanged.
> 1a. **Reject: met.**
>    - "The working tree is cleaned" is gone. The entry now says "the manager removes that node's worktree and deletes its branch", and "Where the human asks for the work to be kept, it is committed onto that branch before the directory is removed."
>    - It still says "the node does not resolve" and "What is kept is the discovery."
>    - The three sentences that had to stay are present word for word, as is the `_Avoid_` line. I checked them unwrapped.
> 2. **The kinds of node: met.**
>    - The paragraph is now only "Each kind names what its worker does." That keeps the first sentence, and nothing claims a number of kinds name a skill.
>    - The scan is re-run above and returns nothing, so the removal is true of the shipped contracts.
> 3. **grilling: met.** All four required statements are present:
>    - "A decision only the human can make, reached by interviewing them."
>    - "Its worker may put several of its own questions in one payload."
>    - "Two questions share a payload only where neither's answer depends on the other's."
>    - "A question whose answer depends on another question in that payload is held for a later payload."
>
>    Nothing says the human is interviewed one question at a time. The `_Avoid_` line, "decision, question, interview", is unchanged.
> 4. **Closed: met.**
>    - The third sentence now reads: "An effort whose destination says it is not expected to end, and whose frontier never empties, is in a legitimate steady state rather than a stalled one, and is not to be treated as a defect."
>    - The file makes no claim about how often efforts are closed. A search for "most efforts", "never closed", "how often" and "proportion" returns nothing.
>    - The first two sentences and the `_Avoid_` line, "done, finished, complete", are word for word as they were.
> 5. **A new section: met.** `## Starting an effort` is the only new heading. It sits immediately before `## Closing an effort`, and all other headings keep their order.
> 6. **Two entries in the section's shape: met.** The section holds exactly two headword lines and two `_Avoid_` lines, and nothing else. Each entry is a bold headword line with a colon, then the definition, then its `_Avoid_:` line.
> 7. **Starting an effort: met.** The definition states each required point:
>    - "The act that creates an effort."
>    - "The manager performs it, and it happens before the graph exists."
>    - "It produces the effort's files and its first nodes."
>    - "It has two inputs: a conversation with the human, or a directory of work that already exists. The input is the only thing the two ways of starting differ in."
> 8. **Its `_Avoid_` line: met.** It refuses charting, kickoff, onboarding, bootstrap, setup and init. The reason against charting has both halves:
>    - "this workflow's cartographic metaphor stops at the map, and every act beneath it is described plainly".
>    - "the word names what the workflow's ancestor does when it "works out what the work is", rather than anything this workflow performs". This quotes the Expedition entry's own wording.
> 9. **Adoption: met.**
>    - It is defined as "Starting an effort from a directory of work that already exists", and "a way of starting an effort, not a kind of node".
>    - It names all five steps: taking the effort's name from the directory, resolving any reserved graph name the directory already uses for something else, deriving the map from the record rather than from a conversation, declaring the label vocabulary from the foreign label families, and minting the bulk import as `precondition` nodes.
> 10. **Its `_Avoid_` line: met.** It refuses migration, import, onboarding and port. It gives "migration (which names moving data, not taking on an effort)" and "import (importing is one step inside adoption, not the act itself)".
> 11. **No name for starting from a conversation: met.** Every mention of that way refers to it by its input, as "a conversation with the human" or "starting from a conversation". The only other "conversation" in the file is Gate's "render the diff into the conversation".
> 12. **`charting` in exactly one place: met.** `grep -o -i 'chart[a-z]*' CONTEXT.md` returns one match, "charting", in that `_Avoid_` line. "Cartographic" is not a form of *chart*.
> 13. **Nothing else changes: met.**
>    - `git diff` has 36 lines added and 8 removed. Its hunks touch only the kinds-of-node paragraph, the grilling definition, the Code slot definition, the Reject definition, the new section and the Closed entry's last sentence.
>    - The Closed line that also holds the end of the second sentence changed only because the third sentence starts on it. The second sentence's text is unchanged.
>    - The Expedition entry is unchanged. No entry or `_Avoid_` line was removed or changed, and no section other than the new one was added or moved.
> 14. **The bar: met**, as below.
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, in the same state as at my last check: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:**
>   - Standing rule 5 (plain English): the new definitions are plain.
>   - `CONTEXT.md`'s `_Avoid_` lines, settled first above.
>   - All five ground rules, which are met.
> - No reviewing skill is named, so I ran none.

### Gate — approve, 2026-09-26

The human, `verbatim`: *"approve. I think we should also commit the graph state as there is a lot of stuff, maybe once the groups are made ? I don't know if it was finished."*

## Flags

`332.1` **· settled** `ASSUMPTION` — Reject's kept-work sentence carries an ambiguity from its source. The condition, and the landing policy in `map-manager-only.md` it was drawn from ("On reject the worktree is removed and its branch deleted; where the human asks for the work to be kept, the manager commits it onto that branch before removing the directory"), say both that the branch is deleted and that kept work is committed onto that branch. Neither says whether the branch survives in the kept case. Read literally, the commit would then be lost. I wrote the entry the way the landing policy says it, with the deletion as the ordinary case and keeping as the exception. I added no claim that the branch survives, because that is a landing-policy decision and not the glossary's. The manager may want the landing policy to say it explicitly.
