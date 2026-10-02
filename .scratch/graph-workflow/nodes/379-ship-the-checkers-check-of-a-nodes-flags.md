# Ship the checker's check of a node's flags

Type: implementation
Status: claimed
Blocked by: none

## Question

Carry node 30's answer into the checker contract and the manager contract.

*Reported by [node 30](30-checking-a-flag-before-the-human.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none"*

## Acceptance condition

*Authored by node 30's worker and filed by the manager.*

> The work is `.claude/skills/expedition-checker/SKILL.md` and `.claude/skills/expedition/SKILL.md`, and no other file may be edited. These are files the workflow ships, so superseded wording is removed rather than struck, and nothing is moved to any history file. The worker may not mark this node, resolve it, or write a line in any index file.
>
> Done means all of the following are true of the finished tree.
>
> In `.claude/skills/expedition-checker/SKILL.md`:
>
> 1. Under `## What you are given`, the numbered list gains a seventh item: the flags the work's node holds, each as one sentence with its id, given as text by the spawn. The item says that a flag is a judgement another agent recorded about this work, and that this given is absent where the node holds no flags. The sentence introducing the list states the new count, and states correctly which givens the spawn carries and which one the checker reads for itself.
> 2. The paragraph beginning "The six givens above are everything you are given" no longer says "six". It states its closure as protection of the record: the record stays unread, and a flag given under item 7 is a claim about the work, not part of the record. The paragraph's other sentences keep their words. That includes "The one exception is `map-implementation-rules.md`, and only for the standards in it." and "A path you were given as the work is the work wherever it sits, and you read it."
> 3. A section headed `### The flags, after your outcome` is added under `## What you hand back`. It states all of the following:
>    (a) Check the flags only after reaching your `PASS` or `FAIL`, and change no outcome because of them.
>    (b) For each flag, establish one of three things: what it says was done is true of the work, it is false, or it makes no claim the work can make true or false.
>    (c) Judge only whether what the flag says was done is true of the work, never whether the judgement was right, and ignore any reason the flag gives.
>    (d) Report a false flag, and only a false flag, under `QUESTIONS:`, naming the flag's id and the search that showed it false.
> 4. In `### Questions, alongside a \`PASS\` or a \`FAIL\``, the sentence that counts the kinds of question states the new count, and a false flag is described there as one kind. The section points at `### The flags, after your outcome` rather than restating it.
> 5. No heading of the file is renamed. No sentence outside clauses 1 to 4 changes in content. The table under `### When what you check against is itself the problem` is not changed by this work.
>
> In `.claude/skills/expedition/SKILL.md`:
>
> 6. In `## The checker`, the list after "The checker receives the following:" gains one item: on the check of an implementation node, every run, the flags the node holds, each as its sentence from `flags.md` with its id and without the link to its node.
> 7. The sentence "The checker receives nothing from the effort's own record, so its spawn never points it at the node file." is changed so that it makes the flag sentences of clause 6 its only exception, and it still says that the spawn never points the checker at the node file.
> 8. In `## What nothing here settles`, the item beginning "Does anything check a flag before the human settles it?" is removed, and the items after it are renumbered in their existing order. The bullet "The scribe rule against the fuller form of a flag." under `## Conflicts this contract leaves open` is not changed.
>
> Both files:
>
> 9. Compared with the commit the work starts from, `.claude/skills/expedition-checker/SKILL.md` grows by no more than 15 lines, and `.claude/skills/expedition/SKILL.md` does not grow. Line counts are those printed by `wc -l`.
> 10. Every markdown link in both files resolves to a path that exists.
> 11. The working tree meets the bar.
>
> Scope: the places named are the work, not instances of a defect. One search was run to find the count words a seventh given would make wrong: `grep -n -w -i 'six\|five' .claude/skills/expedition-checker/SKILL.md` returned two lines, "You are given six things. The spawn carries the first five, and you read the sixth for yourself from one" and "The six givens above are everything you are given.", which clauses 1 and 2 cover. A count word that this search reaches outside those two lines is reported, not edited.

## Attempts

*The manager's note, 2026-10-02:* attempt 1 was stopped by the manager seconds after its spawn, because the spawn was malformed: it went out without the acceptance condition's text. The worktree was still clean when it stopped. Attempt 2 is a fresh spawn in the same worktree.

## Handover, attempt 2

*Pasted as the worker handed it back.*

`````
HANDOVER:      Ship the checker's check of a node's flags (node 379)
ANSWER:        Node 30's answer is now in the checker contract and the manager contract. Two files changed, and no other file was touched.

               `.claude/skills/expedition-checker/SKILL.md` (422 lines before, 436 after by `wc -l`, so 14 lines added against a cap of 15):
               - `## What you are given` has a seventh item. It gives the flags the work's node holds, as text, each as one sentence with its id. It says that a flag is a judgement another agent recorded about this work, and that this given is absent where the node holds no flags. The sentence that opens the list now reads "You are given seven things. The spawn carries all of them except the sixth, which you read for yourself from one file this contract names." Only the sixth given, the standards, is read by the checker itself.
               - The paragraph after the list now opens "The givens above are everything you are given, so that the record behind the work stays unread." One sentence is added after the sentence that defines the record: "A flag given under item 7 is a claim about the work, and not part of the record." The new sentence goes after that definition so that the record is defined before the flag is set apart from it. Every other sentence of the paragraph keeps its words. The paragraph was rewrapped, and no word in it moved.
               - The counting sentence in `### Questions, alongside a `PASS` or a `FAIL`` now reads "Three kinds of question reach the human this way, and none of them stops your check." A paragraph is added after "The second is…": "The third is a false flag, meaning that what a flag says was done is not true of the work. `### The flags, after your outcome` says when and how you check the flags."
               - A new section, `### The flags, after your outcome`, comes right after `### Questions…` and before `### A part you could not establish…`. It is one paragraph and says five things. Check the flags only after reaching `PASS` or `FAIL`, and change no outcome because of them. For each flag, establish one of three things: true of the work, false, or no claim the work can make true or false. Judge only whether what the flag says was done is true. Never judge whether the flag's judgement was right, and ignore any reason the flag gives. Report only a false flag, under `QUESTIONS:`, naming its id and the search that showed it false.
               - No heading was renamed. The table under `### When what you check against is itself the problem` is unchanged.

               `.claude/skills/expedition/SKILL.md` (826 lines before, 824 after):
               - The list after "The checker receives the following:" in `## The checker` has a new item: "On the check of an implementation node, on every run, the flags the node holds: each as its sentence from `flags.md`, with its id and without the link to its node."
               - The sentence about the record now reads "The checker receives nothing from the effort's own record except those flag sentences, so its spawn never points it at the node file."
               - In `## What nothing here settles`, the item "Does anything check a flag before the human settles it?" is gone, and the old items 3, 4 and 5 are now 2, 3 and 4 in the same order. The scribe-rule bullet under `## Conflicts this contract leaves open` is unchanged.

               Neither file contains a markdown link, so clause 10 holds with nothing to resolve.
INDEX LINE:    The checker contract gains a seventh given, the node's flags as id-tagged sentences, and checks them after its outcome. The manager's checker spawn carries them, and the open question is removed.
FLAGS:         ASSUMPTION: Where the new section and sentence go. The condition says where each piece goes only as "under `## What you hand back`" and "the paragraph". I put `### The flags, after your outcome` right after `### Questions, alongside a `PASS` or a `FAIL``, because a false flag is reported as a question. In the closing paragraph of the givens I replaced only the first sentence. I added the item-7 sentence after the sentence that defines the record rather than at the start, so the record is defined before the flag is set apart from it. Index: The new flags section follows the Questions section, and the closing paragraph's new flag sentence follows the record's definition so the term is defined first.
               ASSUMPTION: The pointer in `### Questions…` gives the false flag a definition of one clause ("what a flag says was done is not true of the work") as well as pointing at the new section. Clause 4 asks for a false flag to be described there as a kind, and also asks for no restatement. I read the clause as a definition of the kind and the section as the procedure. "neither stops your check" became "none of them stops your check", which is the wording node 66's pending clauses for node 214 already use. Index: The Questions section defines a false flag in one clause and points at the flags section for how to check one, and its counting sentence uses node 66's "none of them" wording.
NEW NODES:     none
INVALIDATIONS: none beyond what node 30 already reported. This work ships node 30's answer: node 26 narrowed, node 42 extended, and node 28's flag 28.3 carried out by the new closing paragraph of the givens. Node 34's rule is used unchanged for a false flag.
CONDITIONS:    I listed the open and claimed nodes with `grep -l -E '^Status: (open|claimed)' nodes/*.md`, which found 21 nodes. In those files I searched for: "six givens", "six things", "first five", "everything you are given", "check a flag", "nothing from the effort", "Two kinds of question", "neither stops", "What nothing here settles", "May you file a flag", "What limits what a spawn", "Does anything tell a worker", "The checker receives", "What you are given", "Questions, alongside", "The flags, after", "## The checker", "flags the node holds", "node file" and `expedition-checker/SKILL.md`. Two nodes besides 379 are affected.

               Node 214 (open and unclaimed, with no acceptance condition yet). The clauses its 2026-10-02 amendment from node 66 queues for addition are wrong once this work lands. Clause 2 quotes "Two kinds of question reach the human this way, and neither stops your check.", and that sentence will no longer exist. It also places its paragraph straight after the "The second is…" paragraph, where this work's "The third is a false flag…" paragraph now sits. Replacement for that clause 2:
               "2. In the same file, under `### Questions, alongside a \`PASS\` or a \`FAIL\``, the sentence "Three kinds of question reach the human this way, and none of them stops your check." becomes "Four kinds of question reach the human this way, and none of them stops your check." After the paragraph that begins "The third is a false flag", and before the paragraph that begins "Hand each question back under your outcome", one paragraph is added, word for word: "The fourth is two parts of the condition that cannot both hold on one reading of their words, where every part holds on another reading. Check the work under the reading on which every part holds. Taking that reading is not a repair of the condition. In the question, name the reading you took, the reading you set aside, and each part the work would fail under the reading you set aside. Where no reading lets every part hold, the condition is self-contradicting, so raise.""
               What fixes the words: the quoted sentence and the "The third is a false flag" paragraph are this node's work once it lands in the tree. The rest is node 66's resolved text word for word. Only two words change: "Three" becomes "Four" in the new sentence, and "third" becomes "fourth" at the start of the paragraph. Both follow from the order of the paragraphs as landed, and no new judgement is made. This replacement holds only if this node lands before node 214 is worked. Clauses 1 and 3 of node 66's block are unaffected, since this work leaves the table alone.

               Node 37 (claimed, grilling). Its attempt's text calls the manager contract's `## What nothing here settles` "item 3" ("Does anything tell a worker to look at the record…") and proposes "Remove item 3". After this work that item is item 2. The node is claimed, so this goes to the manager under the raise route, and I edited nothing.

               Nodes 41 and 380 matched only on the path `.claude/skills/expedition-checker/SKILL.md`. Both conditions say that file is not changed by their own work, so they do not conflict with this work. No open node's question changes.
MISSING FROM MAP: none
GATE PAYLOAD:  Checker findings: none yet, because no checker has run.
               Paths touched: `.claude/skills/expedition-checker/SKILL.md` and `.claude/skills/expedition/SKILL.md`, both in the worktree `.scratch/graph-workflow/worktrees/379-flag-check`. Both are uncommitted.
               Checks run:
               - The condition's recorded search `grep -n -w -i 'six\|five' .claude/skills/expedition-checker/SKILL.md`, run before the edit, returned exactly the two recorded lines (36 and 56). Run after the edit with 'seven' and 'seventh' added, it returns only line 36, "You are given seven things…", which matches through the word "sixth".
               - `wc -l`: 422 to 436 for the checker contract, and 826 to 824 for the manager contract.
               - The list of `#` headings is identical before and after in both files, apart from the one added heading.
               - `git diff --check` is clean.
               - Neither file contains a markdown link.
               - Before removing the item, I searched the shipped files with `grep -rn -E 'What nothing here settles|item [0-9]' .claude/` for citations of those items by number, and found none.
               Bar: the repo states no commands of its own. Its root holds `.claude`, `CONTEXT-MAP.md`, `CONTEXT.md`, `.gitignore` and `.scratch`, with no manifest, no task runner, no CI and no agent-instruction file that gives commands. That matches the record in `map-implementation-rules.md`, so the command half of the bar is empty and complete.
               Standards: I wrote to the standards that file lists, including the six rules for writing in map.md and the glossary's `_Avoid_` lines. "item 7" is used only for a numbered entry in a list, as the condition demands and as the existing text already does. I loaded the `/writing-for-agents` skill as a standard and skipped no part of it. It is reference text, and none of it conflicts with the contract.
               Proposed commit message:
               Ship the checker's check of a node's flags

               The checker contract gains a seventh given, the node's flags as id-tagged
               sentences, and a section on checking them after its outcome, reporting a
               false flag as a question. The manager contract's checker spawn carries the
               flag sentences, and the settled open question is removed.

               Node: graph-workflow/379

RETROSPECTIVE:
1. What I had to hunt for: whether any shipped file cites the items of `## What nothing here settles` by number (none does). I also had to find which open nodes quote the sentences this work rewrites. Node 214's queued clauses from node 66 quote the "Two kinds of question" sentence. Nothing in the spawn or in node 30's CONDITIONS flagged that, because node 66's amendment was added after node 30 searched.
2. What arrived that this node did not need: most of map.md (the heterogeneous-model note, the never-delete boundaries, the glossary counts), and in map-implementation-rules.md the worktree, record-as-work and trigger-file paragraphs. The decisions lines for nodes 26, 28 and 34 were not needed either, since the condition is self-contained.
3. What would have made this easier: the manager's notes saying that node 214 carries pending clauses on the same counting sentence. Two nodes are now in line to edit one sentence in the checker contract.
4. What was stale, wrong or contradictory: node 30's CONDITIONS search said node 214 changes only the table. That is now stale: node 214's 2026-10-02 amendment from node 66 also rewrites the "Two kinds of question" sentence that this node rewrites. The manager's numbers checked out: 826 and 422 lines at 937fe6c9b. The note about the backslashes in clause 4 was accurate.
`````

*The manager's note:* the replacement clause for node 214 under `CONDITIONS` is filed on node 214 when this work lands. The point about node 37 goes to node 37's worker when it is next resumed.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-10-02. A fresh checker; the condition reached it as a verbatim copy in `$TMPDIR/c379.md`.*

> PASS
> Work under check: uncommitted changes in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/379-flag-check (base 937fe6c9b). I compared the diff with `git diff`, and for clauses 2 and 5 I compared the files sentence by sentence. For that comparison I unwrapped each paragraph, split it into sentences, and set-diffed the sentences of the base (`git show 937fe6c9b:<path>`) against the work. I read the changed paths as the work under the rule in map-implementation-rules.md.
>
> Preamble. `git status --porcelain --untracked-files=all` lists only ` M .claude/skills/expedition-checker/SKILL.md` and ` M .claude/skills/expedition/SKILL.md`. No other file is edited, and nothing is untracked. In the work tree, no node file, `decisions.md`, `flags.md` or `map-history.md` changed. The diff contains no `~~` strike-through. (The part about the main checkout is under NOT COVERED.)
>
> 1. Item 7 is present: "The flags the work's node holds, as text: each one sentence, with its id. A flag is a judgement another agent recorded about this work. Where the node holds no flags, this given is absent." The intro now reads "You are given seven things. The spawn carries all of them except the sixth, which you read for yourself from one file this contract names." Both parts of that are correct: the spawn carries 1–5 and 7, and the checker reads 6. Established from the sentence set-diff.
> 2. "six" is gone from the paragraph. The new first sentence is "The givens above are everything you are given, so that the record behind the work stays unread." It adds "A flag given under item 7 is a claim about the work, and not part of the record." Every other sentence of the paragraph appears unchanged in the set-diff, including the two quoted in the clause. The set-diff lists only the old "The six givens above are everything you are given." as removed.
> 3. `### The flags, after your outcome` sits between `### Questions…` and `### A part you could not establish…`, under `## What you hand back`. Each sub-clause has its own sentence:
>    - (a) "Check the flags only after reaching your `PASS` or `FAIL`, and change no outcome because of them."
>    - (b) "establish one of three things: … true of the work, it is false, or it makes no claim the work can make true or false."
>    - (c) "Judge only whether … Never judge whether the flag's judgement was right, and ignore any reason the flag gives."
>    - (d) "Report only a false flag, under `QUESTIONS:`, naming the flag's id and the search that showed it false."
>    Established from the set-diff and the headings diff.
> 4. The count sentence reads "Three kinds of question reach the human this way, and none of them stops your check." It adds "The third is a false flag, …" and then points at the new section with "`### The flags, after your outcome` says when and how you check the flags." Established from the set-diff.
> 5. Headings: `diff` of `grep '^#'` between base and work shows a single added line, `### The flags, after your outcome`, in the checker file and nothing in the expedition file. The set-diff shows no sentence changed outside clauses 1–4. The table under `### When what you check against is itself the problem` is byte-identical: I extracted it with `sed -n '/^| what you find/,/^$/p'` on both sides and diffed.
> 6. `## The checker` gains "On the check of an implementation node, on every run, the flags the node holds: each as its sentence from `flags.md`, with its id and without the link to its node." Established by reading the section with `sed -n 220,250p` and from the set-diff.
> 7. The sentence now reads "The checker receives nothing from the effort's own record except those flag sentences, so its spawn never points it at the node file." Established from the set-diff.
> 8. The item "Does anything check a flag before the human settles it?" and its three following sentences are removed. The remaining items are numbered 1–4 in their existing order (`sed -n 780,824p`). The scribe-rule bullet under `## Conflicts this contract leaves open` does not appear in the diff.
> 9. `wc -l`:
>    - expedition-checker/SKILL.md went from 422 to 436 (+14, within the limit of 15).
>    - expedition/SKILL.md went from 826 to 824 (no growth).
> 10. A script extracted every `](…)` target in both files and found 0 markdown links in either. `grep -c ']('` also returns 0 for both, so no link can fail to resolve.
> 11. The bar is met (see below).
>
> Recorded search: I ran `grep -n -w -i 'six\|five' .claude/skills/expedition-checker/SKILL.md` as written.
> - On the finished tree it returns nothing.
> - On the base (`git show 937fe6c9b:…`) it returns exactly the two lines the condition records, at lines 36 and 56. That matches the recorded return.
> - The search reaches no count word outside those two lines.
>
> Bar: the repo has no agent-instruction file at its root (no CLAUDE.md or AGENTS.md; the root holds only CONTEXT.md, CONTEXT-MAP.md, .gitignore, .claude and .scratch). map-implementation-rules.md states that graph-agent has no build, no tests, no formatter and no CI. So no command was run for the command half of the bar, and the bar rests on its non-command half.
> - `git diff --check` is clean.
> - No trailing whitespace.
> - Added lines are at most 106 columns, which matches the existing wrap width of non-table lines in both files.
>
> Standards: I read only the standards in .scratch/graph-workflow/map-implementation-rules.md. The main checkout's copy and the worktree's copy are byte-identical (cmp).
> - Bore on this work: the glossary's `_Avoid_` lines, the ground rules, the six standing rules for writing, graph-conventions.md and `/writing-for-agents`.
>   - `_Avoid_` lines: none of the new text uses a refused word for its refused concept. "Report" is used as a verb for handing back, as the existing "Report what you find" already does.
>   - Writing rules: the prohibitions ("Never judge…", "change no outcome…") stand beside their positives. The Questions section points at the new heading rather than restating it. No line numbers are cited, and nothing is bolded.
>   - `/writing-for-agents`: the new section is short and puts the positive instruction first.
> - Barely touched: `/coding-principles` and `/naming`.
> - No reviewing skill is named for this repo, so I ran none.
> - No flags were given to me, so I checked none.
>
> NOT COVERED:
> - "The worker may not mark this node, resolve it, or write a line in any index file." I established it for the work tree I was given: no node file or index file changed there. Whether anything was written to the record in the main checkout is outside the paths I was given.
>
> QUESTIONS:
> - The work complies with clauses 2 and 7, and complying is what produces this defect. The wording is the condition's own, so departing from it was not the worker's call. The two shipped files now disagree about whether a flag is part of the record.
>   - Instances:
>     - expedition-checker/SKILL.md, `## What you are given`, as clause 2 dictates: "A flag given under item 7 is a claim about the work, and not part of the record."
>     - expedition/SKILL.md, `## The checker`, as clause 7 dictates: "The checker receives nothing from the effort's own record except those flag sentences", which treats the flag sentences as record.
>     - Outside the work, these sentences agree with the second reading:
>       - glossary.md **Manager**: "The record is every answer, status, index line and flag".
>       - graph-conventions.md `## The seven files`: "Text that records what happened, such as a line in `decisions.md` or an entry in `flags.md`".
>       - The unchanged checker paragraph on ground rules: "An account of what happened, on this work or anywhere in the record, … is part of the record you are kept blind to".
>   - Form: a sentence in a shipped file that places a flag, or a `flags.md` line, inside or outside the effort's record, where another shipped sentence places it on the other side.
>   - Extent: unwrap each file under `.claude/` and list the sentences matching both `\bflag` and `\brecord\b`. I ran this as a perl one-liner over `git ls-files .claude`, splitting on sentence ends. It returns 6 sentences. Within the two editable files the candidates are exactly the two sentences quoted above. The graph-conventions instance uses "records", so it falls outside that pattern and is listed by hand.
>   - A reader of both files gets opposite answers. The human might pick one reading, for example "a flag is part of the record, and given under item 7 it is the one exception to the checker's blindness".
>
> Temporary files were written only under $TMPDIR/chk379 and have been removed.

*The manager's note on the part under `NOT COVERED`:* the manager established it. Between the cut at `937fe6c9b` and this run, master changed neither `decisions.md` nor `flags.md`. The only commits touching this node's file are the manager's own two, recording the stopped attempt and filing the handover. *The manager's note on the gate:* the checker handed back a question beside its outcome, so the standing yes does not cover this gate. It goes to the human.
