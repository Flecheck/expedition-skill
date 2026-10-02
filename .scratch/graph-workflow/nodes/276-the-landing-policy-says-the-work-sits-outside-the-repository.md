# The landing policy says an implementation node's work sits outside the repository

Type: implementation
Status: claimed
Supersedes: 254

Blocked by: none

## Question

*Surfaced by [node 268](268-carry-the-plain-git-worktree-route-into-the-map.md)'s worker, and pasted as it wrote
it.*

> `map-manager-only.md`'s landing policy paragraph states, as the ground for the gate payload naming the worktree's
> path, *"because an implementation node's work is uncommitted in a checkout **outside** the repository and `git
> diff` where the human is standing does not show it"*. The checkout has been **inside** the repository since node
> 68, and under node 265's route it is inside the record directory itself. The clause is false and it is the stated
> reason for a rule that still binds.

**Blockers, in the worker's words:** *"none, but it sits in the same sentence [node
231](231-a-gate-payload-stops-carrying-a-diff-command.md) will rewrite when it removes the diff command from the
gate payload. **Folding this into node 231 is likely cheaper than running it alone**, and that is the manager's call
rather than this node's."*

## Acceptance condition

*Written by node 268's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md`, and no
> other file may be edited. The worker may not mark this node, resolve it, or write a line in `decisions.md` or
> `flags.md`. Done means all of the following are true of the finished tree.
>
> 1. The `## Landing an implementation node's work` section of `map-manager-only.md` no longer states, as the ground
>    for any rule, that an implementation node's work is uncommitted in a checkout outside the repository.
> 2. The rule that sentence grounds — that the gate payload names the worktree's path — is still stated, and the
>    replacement ground says instead that the work is uncommitted, so it appears in no commit the human can read,
>    and that the path is how the work is found at all.
> 3. The replacement cites by markdown link the node that placed the worktree inside the repository, [Run an
>    implementation node's work in a worktree](68-implementation-in-a-worktree.md).
> 4. The displaced wording is appended verbatim to `map-history.md` under a heading mirroring the section it came
>    from, with any struck-through text staying struck through; `map-history.md` gains text and loses none.
> 5. The `## Landing an implementation node's work` heading is still present and the quoted phrase `How the worktree
>    is made` still occurs in `map-manager-only.md` — three pointers in the repository's `.gitignore` cite them.
> 6. No file outside the two named above is modified, `.gitignore` is not edited, and no file under
>    `.claude/skills/` is changed.
> 7. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This node was filed rather than folded into [node 231](231-a-gate-payload-stops-carrying-a-diff-command.md), and
its author said the fold is likely cheaper.** The manager filed it separately for one reason and states it so the
human can reverse it in a line: **folding would widen an open node's subject, which is not the manager's to do.**
Node 231's subject is removing the diff command from the gate payload; this is a false ground clause in the same
sentence. They are two repairs that collide rather than one repair.

**The fold is the human's call**, and the manager's own view is that the author is probably right about the cost —
whichever of the two lands second meets the other's edit in the same sentence, which is exactly the collision node
249's worker flagged about this paragraph months of nodes ago.

**This is the third defect found in that one paragraph.** [Node
237](237-the-landing-policy-and-the-worktree-bullets-name-two-paths.md) holds a path contradiction in its first
sentence; [node 254](254-the-landing-policy-says-the-worktree-is-outside-and-inside-the-repository.md) holds the
inside/outside contradiction and **carries no acceptance condition**, its surfacing worker having written none and
said why. **This node is the first of the three with a complete, satisfiable condition**, its author having been
inside the file with the route in hand. **Whether it supersedes node 254 outright is the human's**, and the manager
has not done it: node 254 names the same clause, and under node 264's widened rule a node made unnecessary by
another may now be superseded — but node 254's own question is broader than this condition, and the manager will not
narrow somebody else's question by retiring it.

## Handover, attempt 1

*The worker's own text, pasted, 2026-10-02.*

````
HANDOVER:      The landing policy says an implementation node's work sits outside the repository

ANSWER:        In `.scratch/graph-workflow/map-manager-only.md`, under `## Landing an implementation node's work`, the landing policy paragraph had one sentence that grounded the gate-payload rule on a false claim: "because an implementation node's work is uncommitted in a checkout outside the repository and `git diff` where the human is standing does not show it". That sentence is replaced, and the rest of the paragraph is unchanged. The new text keeps the rule (**The gate payload names the worktree's path**) and keeps its citations of nodes 231 and 336. It now gives this ground: the work is uncommitted, so it appears in no commit the human can read, and the path is how the work is found at all. Next comes one sentence saying the worktree is inside the repository. That sentence cites [Run an implementation node's work in a worktree](nodes/68-implementation-in-a-worktree.md) by markdown link and says the worktree is ignored there, so its changes do not show in the human's `git status` or `git diff`. I confirmed the ignore with `git check-ignore`, which matches `.gitignore`'s `.scratch/graph-workflow/worktrees/` line. The human's quoted words ("what are the changes ? I don't see them in git ?") stay as the evidence. The paragraph's first sentence also contains "a worktree outside the repository". That is part of an account of what led to the human's instruction, it grounds no rule, and it was left alone. The displaced sentence was appended verbatim to the end of `.scratch/graph-workflow/map-history.md` under `## Superseded from map-manager-only.md at node 276 — the landing policy's ground for naming the worktree's path` / `### From *Landing an implementation node's work* — the landing policy's sentence on what the gate payload names`. It has no struck-through text. map-history.md only gained text. The section heading is still present, and `How the worktree is made` still occurs 3 times in map-manager-only.md.

INDEX LINE:    The landing policy now says the gate payload names the worktree's path because the work is uncommitted and the path is how it is found, not because it sits outside the repository.

FLAGS:         ASSUMPTION: Clause 3 of the condition writes the node 68 link target as `68-implementation-in-a-worktree.md`, which is relative to `nodes/`. From `map-manager-only.md` that target would not resolve, so I wrote `nodes/68-implementation-in-a-worktree.md` with the condition's link text, the same form the paragraph already uses for node 68 at its end. I made the change by direct edit, with no interview and no gate before this handover. — Index: The node-68 link in the landing policy uses the `nodes/` path that resolves from map-manager-only.md, not the bare filename the condition wrote.

NEW NODES:     none

INVALIDATIONS: none. The edit narrows no resolved node. Node 68's placement inside the repository is now stated where the false clause was.

CONDITIONS:    I searched the `## Acceptance condition` and `## Question` sections of every open and claimed node for "outside the repository", "uncommitted in a checkout", "names the worktree's path", "gate payload", "where the human is standing" and "Landing an implementation node". The only match is this node. Nodes 231, 237 and 254 also name the sentence, and all three are superseded. Node 209's question mentions "The rules file's `## Landing an implementation node's work` section", which this work does not touch, and it needs no change from this node. I wrote no replacement clauses.

MISSING FROM MAP: none. The map-history heading convention was taken from the existing entries in map-history.md.

GATE PAYLOAD:  No checker findings yet. Paths touched: `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md`, in worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/276-landing-ground. Nothing is committed. Bar: the repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT-MAP.md`, `CONTEXT.md`, `.gitignore` and `.scratch`, which matches what map-implementation-rules.md records, so the bar is its non-command half. `git diff --check` is clean. The manager's note about node 211 holds: my append goes at the very end of map-history.md, after the node 219 entry, so it will meet node 211's append there. Both sides are text held under the never-delete rule, so the merge keeps both. Proposed commit message:
  "Ground the gate payload's worktree path on the work being uncommitted

  The landing policy said the work sits in a checkout outside the repository; it has been inside since node 68. The displaced sentence is banked in map-history.md.

  Node: graph-workflow/276"

RETROSPECTIVE:
1. What I had to hunt for: where node 68 says the worktree moved inside the repository (its section `### 1. The worktree moves inside the repository`), and whether nodes 231 and 254 were still open. Both are superseded.
2. What arrived that this node did not need: most of map.md and map-implementation-rules.md. Of the decisions.md lines for nodes 68 and 265, only node 68's was used.
3. What would have made this easier: a condition that wrote the link target relative to the file being edited (`nodes/68-...`).
4. What was stale, wrong or contradictory: clause 3's link target does not resolve from map-manager-only.md, as flagged above. Node 209's question still calls the landing section part of "the rules file", but it moved to map-manager-only.md at node 188. The manager's notes checked out: the phrase was present, and the second mention of "outside" is in an account.
````

## Review

### Checker run 1 — `FAIL` (the bar)

*The checker's own text, pasted, 2026-10-02. A fresh checker; the condition reached it as a verbatim copy in `$TMPDIR/c276.md`.*

> FAIL: the bar
>
> Node 276, "The landing policy says the work sits outside the repository". Worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/276-landing-ground, base 343e0c604, diff from `git -C <worktree> diff`.
>
> ### Finding 1 (the bar: writing rules 1 and 5, and the `/writing-for-agents` rule on duplication)
>
> - Instances: the change adds this sentence to the `## Landing an implementation node's work` section of `.scratch/graph-workflow/map-manager-only.md`: "The worktree is inside the repository, placed there by [Run an implementation node's work in a worktree](nodes/68-implementation-in-a-worktree.md), and it is ignored there, so its changes do not show in the human's `git status` or `git diff`."
>   (a) It repeats a meaning the same paragraph already states in its first sentence, "placed at `.scratch/graph-workflow/worktrees/<NN>-<name>` **inside** the repository and ignored there". This breaks the `/writing-for-agents` pruning rule (keep one meaning in one place, because duplication is a defect) and writing rule 1 ("Compress the prose that explains why").
>   (b) It puts several ideas in one sentence: where the worktree is, which node placed it there, that it is ignored, and what follows from that. Writing rule 5 says "Put one idea in each sentence."
>   (c) This one is an observation and not a ground for the FAIL. The word "so" says the changes are hidden because the directory is ignored. The ignore rule only keeps the directory from showing as untracked. Uncommitted changes in a separate worktree never show in another checkout's `git diff`, whether or not anything is ignored.
>   - Found with `git diff --word-diff=plain -- .scratch/graph-workflow/map-manager-only.md`, then by comparing the added sentence with the paragraph's first sentence.
>   - The repair has a constraint. This sentence holds the only link to node 68 in the replacement, and part 3 needs that link. Whatever replaces the sentence must keep the link.
> - Form: a sentence this change added to `map-manager-only.md` that restates something the same paragraph already says, or that carries more than one idea.
> - Extent (type 2): the text this change added to `map-manager-only.md`. That is the three sentences between "([node 231]…, [node 336]…))." and "One of the human's two interfaces is the diff". The first of the three is worded by the acceptance condition itself. Run `git diff --word-diff=plain -- .scratch/graph-workflow/map-manager-only.md` and read the `{+…+}` segments to list them. The rest of the paragraph was not changed and is not part of the work.
>
> ### Acceptance condition: each part established
>
> 1. Part 1 is met. I unwrapped the section from its heading to the next `## ` and searched it for "outside the repository". There is one hit: "after a worktree outside the repository made a gate's diff invisible to them". That describes a past event and is not the ground for any rule. A search for "checkout outside" finds nothing.
> 2. Part 2 is met. The rule sentence "**The gate payload names the worktree's path**" is still present. A substring search for "uncommitted, so it appears in no commit the human can read, and the path is how the work is found at all" returns true.
> 3. Part 3 is met, with one detail. The link `[Run an implementation node's work in a worktree](nodes/68-implementation-in-a-worktree.md)` is present. The condition wrote the target without `nodes/`. The work's `nodes/…` path is the one that resolves from `map-manager-only.md`, matches how every other link in the paragraph is written, and points at the same node. `ls nodes/` confirms the file exists.
> 4. Part 4 is met.
>    - I took the removed sentence from `git show 343e0c604:…/map-manager-only.md`, from "**The gate payload names the worktree's path**" to `git ?"*.`. That sentence occurs byte-identically in `map-history.md` and ends the file.
>    - The old `map-history.md` is a byte-exact prefix of the new one, and the diff has no `-` lines. That is check 11 of graph-conventions.md, both halves.
>    - The headings "## Superseded from `map-manager-only.md` at node 276 — …" and "### From *Landing an implementation node's work* — …" follow the existing node 234 entry.
>    - No struck-through text was involved.
>    - The links in the new history entry to nodes 276 and 68 resolve to files in `nodes/`.
> 5. Part 5 is met. "## Landing an implementation node's work" and "How the worktree is made" are both present in the new file. The two `.gitignore` pointers I found cite "How the worktree is made", at lines 10 and 18.
> 6. Part 6 is met. `git status --porcelain --ignored`, leaving out the worktrees directory, shows only the two named files. `.gitignore` and `.claude/skills/` are untouched. Nothing in `decisions.md`, `flags.md` or any node file changed.
> 7. Part 7, the bar: fails, as stated above.
>
> ### The bar
>
> - Commands: the repo has no CLAUDE.md or AGENTS.md at its root. `map-implementation-rules.md` records that the repo has no build, no tests, no formatter and no CI, so the command half of the bar is empty and I ran nothing for it. The bar here is its non-command half: the standards.
> - Standards: from `.scratch/graph-workflow/map-implementation-rules.md` I read only the standards. These are `/coding-principles` and `/naming`, the glossary's `_Avoid_` lines, the ground rules, the six standing rules for writing, `graph-conventions.md`, and `/writing-for-agents`. I read the last from the mattpocock-skills plugin.
> - Which bore on this work: the writing rules, `/writing-for-agents` and `graph-conventions.md` (`Change the map`, check 11). The glossary bore too, and the new text uses none of its refused words. "Gate payload" was already in the file. The coding principles and naming rules did not apply, since this is prose.
> - Unchanged standards: the work did not change any standard.
> - Reviewing skills: the standards name none, and I ran none.
> - Record files: I read the changed paths as the work under check, following the record-files rule in `map-implementation-rules.md`. I opened no other record file, except to confirm that the cited node files exist.
>
> ### Searches the condition records
>
> The condition records no search command.
>
> ### Housekeeping
>
> I wrote two temporary comparison files directly in `$TMPDIR`, not in a new directory under it, and removed them. Nothing in the repository was written.

*The manager's note:* an unmet bar goes back to the worker, with the finding, in one correction round. The checker handed back no question.

## Handover, attempt 1, correction round 1

*The worker's own text, pasted, 2026-10-02.*

````
CORRECTION ROUND 1 (checker run 1, Finding 1). The fix rewrites the one sentence in .scratch/graph-workflow/map-manager-only.md that the finding named. Nothing else changed in this round.

Changed: in `## Landing an implementation node's work`, this sentence
  "The worktree is inside the repository, placed there by [Run an implementation node's work in a worktree](nodes/68-implementation-in-a-worktree.md), and it is ignored there, so its changes do not show in the human's `git status` or `git diff`."
is now
  "The worktree being inside the repository, where [Run an implementation node's work in a worktree](nodes/68-implementation-in-a-worktree.md) placed it, does not make its changes visible where the human is standing."
How this answers the finding:
(a) The sentence no longer repeats "and ignored there" or the location detail from the paragraph's first sentence. Its point is the one thing the first sentence does not say: being inside the repository does not let the human see the changes, which is why the path is still needed.
(b) It now carries one idea, plus the citation that clause 3 requires.
(c) The wrong cause is gone. The sentence no longer says the ignore rule hides the changes.
The node 68 link is kept, so clause 3 still holds. The edit touches clause 3's sentence and nothing that clauses 1, 2, 4, 5 or 6 name. The map-history.md append is unchanged. `git diff --check` is clean.

HANDOVER:      The landing policy says an implementation node's work sits outside the repository

ANSWER:        In `.scratch/graph-workflow/map-manager-only.md`, under `## Landing an implementation node's work`, the landing policy paragraph had one sentence that grounded the gate-payload rule on a false claim: "because an implementation node's work is uncommitted in a checkout outside the repository and `git diff` where the human is standing does not show it". That sentence is replaced, and the rest of the paragraph is unchanged. The new text keeps the rule (**The gate payload names the worktree's path**) and keeps its citations of nodes 231 and 336. It now gives this ground: the work is uncommitted, so it appears in no commit the human can read, and the path is how the work is found at all. One more sentence follows: "The worktree being inside the repository, where [Run an implementation node's work in a worktree](nodes/68-implementation-in-a-worktree.md) placed it, does not make its changes visible where the human is standing." The human's quoted words ("what are the changes ? I don't see them in git ?") stay as the evidence. The paragraph's first sentence also contains "a worktree outside the repository". That is part of an account of what led to the human's instruction, it grounds no rule, and it was left alone. The displaced sentence was appended verbatim to the end of `.scratch/graph-workflow/map-history.md` under `## Superseded from map-manager-only.md at node 276 — the landing policy's ground for naming the worktree's path` / `### From *Landing an implementation node's work* — the landing policy's sentence on what the gate payload names`. It has no struck-through text. map-history.md only gained text. The section heading is still present, and `How the worktree is made` still occurs 3 times in map-manager-only.md.

INDEX LINE:    The landing policy now says the gate payload names the worktree's path because the work is uncommitted and the path is how it is found, not because it sits outside the repository.

FLAGS:         ASSUMPTION: Clause 3 of the condition writes the node 68 link target as `68-implementation-in-a-worktree.md`, which is relative to `nodes/`. From `map-manager-only.md` that target would not resolve, so I wrote `nodes/68-implementation-in-a-worktree.md` with the condition's link text, the same form the paragraph already uses for node 68 at its end. I made the change by direct edit, with no interview, and it is now in correction round 1 after checker run 1. — Index: The node-68 link in the landing policy uses the `nodes/` path that resolves from map-manager-only.md, not the bare filename the condition wrote.

NEW NODES:     none

INVALIDATIONS: none

CONDITIONS:    I searched the `## Acceptance condition` and `## Question` sections of every open and claimed node for "outside the repository", "uncommitted in a checkout", "names the worktree's path", "gate payload", "where the human is standing" and "Landing an implementation node". The only match is this node. Nodes 231, 237 and 254 also name the sentence, and all three are superseded. Node 209's question mentions "The rules file's `## Landing an implementation node's work` section", which this work does not touch, and it needs no change from this node. I wrote no replacement clauses.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker run 1, Finding 1: fixed as described above. Paths touched: `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md`, in worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/276-landing-ground. Nothing is committed. Bar: the repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT-MAP.md`, `CONTEXT.md`, `.gitignore` and `.scratch`, which matches what map-implementation-rules.md records. `git diff --check` is clean. My append goes at the very end of map-history.md and will meet node 211's append there. Both sides are text held under the never-delete rule, so the merge keeps both. Proposed commit message:
  "Ground the gate payload's worktree path on the work being uncommitted

  The landing policy said the work sits in a checkout outside the repository; it has been inside since node 68. The displaced sentence is banked in map-history.md.

  Node: graph-workflow/276"

RETROSPECTIVE:
1. What I had to hunt for: where node 68 says the worktree moved inside the repository (its section `### 1. The worktree moves inside the repository`), and whether nodes 231 and 254 were still open. Both are superseded.
2. What arrived that this node did not need: most of map.md and map-implementation-rules.md. Of the decisions.md lines for nodes 68 and 265, only node 68's was used.
3. What would have made this easier: a condition that wrote the link target relative to the file being edited. Also knowing in advance that clause 3's citation has to sit in a sentence of its own, which led to the duplication the checker found.
4. What was stale, wrong or contradictory: clause 3's link target does not resolve from map-manager-only.md. Node 209's question still calls the landing section part of "the rules file", but it moved to map-manager-only.md at node 188. My first version also stated a wrong cause (the ignore rule hiding the changes), which the checker caught.
````

## Flags

`276.1` `ASSUMPTION` — *The worker's own text.* Clause 3 of the condition writes the node 68 link target as `68-implementation-in-a-worktree.md`, which is relative to `nodes/`. From `map-manager-only.md` that target would not resolve, so I wrote `nodes/68-implementation-in-a-worktree.md` with the condition's link text, the same form the paragraph already uses for node 68 at its end. I made the change by direct edit, with no interview and no gate before this handover.
