# Ship the `Deliverable:` field on every node kind, and reading deliverable code without a checkout

Type: implementation
Status: resolved
Labels: SPLIT
Blocked by: ~~07~~

## Question

This lets a grilling, precondition or prototype worker see the code of the deliverables its node serves. That code never reaches the main checkout before the deliverable's pull request merges. It also keeps such a node in the record until every deliverable it serves has merged. The shipped files are to say that any node may carry `Deliverable:`, how a non-implementation worker reads a deliverable's code, and how cleanup treats a node that lists several deliverables.

*Manager's note:* minted by the worker of [node 06](06-which-checkout-a-non-implementation-worker-reads.md) on its `NEW NODES` part, with the question and condition below as it wrote them. It gave the blocker as "07 (it also edits `.claude/skills/expedition/SKILL.md`)".

## Acceptance condition

Scope: the files this work may change are named below. For clauses 1 to 5 the named places are the work. For clauses 8 and 9, the scope came from these searches, run from the repository root over the working tree on 2026-10-12 at commit `7a86d138e0` (counts for scale only, not authoritative):
- `grep -rn "Deliverable:" .claude` returned 8 lines: 5 in `.claude/skills/expedition/graph-conventions.md` and 1 each in `.claude/skills/expedition/wayfinder-divergences.md`, `.claude/skills/expedition/glossary.md` and `.claude/skills/expedition-cleanup/SKILL.md`.
- `grep -rn "Run the command over the working tree" .claude` returned 4 lines, one in each of `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md` and `.claude/skills/expedition-prototype/SKILL.md`.
~~- `grep -rn "main checkout" .claude` returned 3 lines, all in `.claude/skills/expedition/SKILL.md`.~~ *(superseded by amendment 1 below)*
An instance any of these searches finds outside the files named in this condition is reported and not edited.

1. `.claude/skills/expedition/graph-conventions.md`, `## The node file`: the paragraph about `Deliverable:` says three things. An `implementation` node carries the field only where its code lands on a deliverable's branch, and then it holds exactly one name. A `grilling`, `precondition` or `prototype` node may carry it, listing one or more names separated by commas, one for each deliverable the node serves. A node that serves no deliverable carries no `Deliverable:` field. It no longer says the field is carried only by an implementation node.
2. The same file, `## Mechanical checks`, check 12, says: every name in a `Deliverable:` field is the name of an entry under `## Deliverables` in `map-manager-only.md`, and an `implementation` node's field holds exactly one name. It no longer says only implementation nodes carry the field.
3. `.claude/skills/expedition/glossary.md`, the entry **Deliverable**, says an implementation node belongs to at most one deliverable, and any other node may name, in its `Deliverable:` field, every deliverable it serves. Its `_Avoid_` line is unchanged.
4. `.claude/skills/expedition/wayfinder-divergences.md`, `## Added`, lists the `Deliverable:` field as carried by any node and holding one name on an `implementation` node. It no longer says "on an `implementation` node only".
5. `.claude/skills/expedition/SKILL.md`, `## Spawning a worker`, says this about a `grilling`, `precondition` or `prototype` node whose `Deliverable:` field names deliverables:
   - The spawn gives each such deliverable's branch and the commit at that branch's tip when the spawn is written.
   - The worker reads each such deliverable's files at that commit through git, without checking it out.
   - The same commit holds for the whole attempt, a resume included.
   - No worktree is made for this reading.
6. `.claude/skills/expedition/SKILL.md`, the paragraph beginning "Every worker reads a consistent snapshot", says three things. An implementation worker reads its own working tree. Every other worker reads the main checkout, and reads each deliverable its node names at the commit its spawn gives. So no worker reads a file while it is being changed.
7. `.claude/skills/expedition/SKILL.md`, `### A deliverable whose base is another deliverable`, says a node belongs to every deliverable its `Deliverable:` field names. It also says a node may be blocked on a node belonging to any deliverable it names, or to such a deliverable's base, and on no other deliverable's node. It still says a node that names no deliverable is not limited by this rule.
8. `.claude/skills/expedition-cleanup/SKILL.md`, `### A merged deliverable as the region`: the first item of the proposed set holds every node whose `Deliverable:` field names that deliverable and whose every named deliverable has merged. The section says that a node that also names a deliverable not yet merged stays out of the set. It says that the merged deliverable then keeps its entry and its local branch, as the passage beginning "A deliverable that a remaining node still names" already says.
9. In each of `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md` and `.claude/skills/expedition-prototype/SKILL.md`, the sentence "Run the command over the working tree, and never over the effort's own record." is changed or followed so that it says this: for a node that will name a deliverable, the command runs over that deliverable's code at the commit the spawn gives for it, or at the tip of that deliverable's branch where the spawn gives none. It still says the command never runs over the effort's own record.
10. In each of `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md` and `.claude/skills/expedition-prototype/SKILL.md`, `## What you read` says:
    - Where the spawn gives a deliverable's branch and a commit, read that deliverable's files at that commit through git, without checking it out.
    - Read the effort's record, the map and the contract as before.
    The prototype contract also says: where you need to build on that code, copy the files you need from that commit into `prototypes/NN-<name>/`. Each contract states this in its own words, without pointing to another skill file.
11. `.claude/skills/expedition-triage/SKILL.md`, `## Check each open node`, says that an open node whose `Deliverable:` field names deliverables is also checked against the tip of each named deliverable's branch, read through git without checking it out.
12. `.claude/rules/expedition-triggers.md` changes only where this work edits, in `.claude/skills/expedition/SKILL.md`, the governing statement of one of the manager's trigger-duties or of the priority that orders them. In that case it changes to match.

### Amendment 1 — by the manager, before the claim

The fact that justified it: re-running the condition's three recorded searches from the repository root on 2026-10-12 at commit `9c0083ffbd`, after node 07 landed. `grep -rn "Deliverable:" .claude` returned 8 lines in the same four files. `grep -rn "Run the command over the working tree" .claude` returned the same 4 lines. `grep -rn "main checkout" .claude` returned 4 lines, the source of this amendment, which replaces that search's line in the scope:

- `grep -rn "main checkout" .claude` returned 4 lines: 3 in `.claude/skills/expedition/SKILL.md` and 1 in `.claude/skills/expedition-upgrade/SKILL.md` (counts for scale only, not authoritative).

The added line is in `.claude/skills/expedition-upgrade/SKILL.md`, about a promoted branch not being checked out in the main checkout. No clause of this condition names that file, so under the condition's own scope clause the instance is reported and not edited. This amendment writes no new requirement.

*Manager's note, before the claim:* read everything after the condition. The passages the condition names are present at `9c0083ffbd`: "Every worker reads a consistent snapshot", `### A deliverable whose base is another deliverable`, `### A merged deliverable as the region` with "A deliverable that a remaining node still names", `## Check each open node` in `expedition-triage`, and `## What you read` in the three worker contracts. Node 07 resolved, so the blocker is struck.

## Answer

The shipped files now say that any node may carry `Deliverable:`. They say how a grilling, precondition or prototype worker reads a deliverable's code without a checkout, and how cleanup treats a node that lists several deliverables. This implements the answer of node 06.
- `graph-conventions.md`, `## The node file`: `Deliverable:` names the deliverables a node serves. An implementation node carries it only where its code lands on a deliverable's branch, and then it holds exactly one name. A grilling, precondition or prototype node may list one or more names, separated by commas. A node that serves no deliverable carries no field. The template line is now `Deliverable: <name>, <name>`. Check 12 says every name is an entry under `## Deliverables`, and an implementation node's field holds exactly one name.
- The same file, under the enumerator rule beginning "An enumerator searches the working tree": for a node that names a deliverable, the tree searched is that deliverable's code. That is the commit the spawn gave, or the branch tip where the spawn gave none. The condition does not name this sentence. It was edited because it is in a named file and would otherwise contradict clause 9 (see flag).
- `glossary.md` **Deliverable**: an implementation node belongs to at most one deliverable. Any other node may name every deliverable it serves. The `_Avoid_` line is unchanged.
- `wayfinder-divergences.md` `## Added`: the field is listed as carried by any node and holding one name on an implementation node.
- `expedition/SKILL.md`:
  - `## Spawning a worker` has a new paragraph and list. For each deliverable such a node names, the spawn gives the branch and the tip commit at spawn time. The worker reads the files at that commit through git without checking it out. The commit holds for the whole attempt, a resume included. No worktree is made.
  - The paragraph "Every worker reads a consistent snapshot" now says that non-implementation workers also read each named deliverable at the commit the spawn gives.
  - `### A deliverable whose base is another deliverable`: a node belongs to every deliverable it names. It may be blocked on a node of any of those deliverables or of their bases. A node that names no deliverable is still not limited by this rule.
- `expedition-cleanup`, `### A merged deliverable as the region`: the first item now needs every deliverable the node names to have merged. A node that also names an unmerged deliverable stays out of the set, and the merged deliverable keeps its entry and its local branch. That is what the passage "A deliverable that a remaining node still names" already says.
- `expedition-triage`, `## Check each open node`: a node that names deliverables is also checked against each named branch's tip, read through git without a checkout.
- The four worker contracts: after "Run the command over the working tree, and never over the effort's own record." comes a new rule. For a reported node that will name a deliverable, the command runs over that deliverable's code, at the commit the spawn gives or at the branch tip where the spawn gives none.
- The grilling, precondition and prototype contracts, `## What you read`: where the spawn gives a deliverable's branch and a commit, the worker reads those files at that commit through git without checking it out. It reads the record, the map and the contract as it would otherwise. The prototype contract adds that the worker copies the files it needs into `prototypes/NN-<name>/`. Each contract defines "deliverable" in one sentence where it first uses the word, because the contracts stand alone and have no glossary entry for it.
- `.claude/rules/expedition-triggers.md` is unchanged. No edit touches a trigger duty or the priority in `SKILL.md`.

*Manager's note:* landed as `a40f9008e8` on `master` by fast-forward, after the human's approval; the worktree and branch are removed. The worker's `NEW NODES` part is [node 12](12-re-derive-a-deliverable-nodes-scope-against-its-branch.md).

## Flags

`10.1` `ASSUMPTION` **· settled** — Amendment 1, by the manager before the claim: the re-run of the recorded `main checkout` search found one more line, in `.claude/skills/expedition-upgrade/SKILL.md`, which node 07 created. The amendment records the new result and adds no requirement.

`10.2` `ASSUMPTION` **· settled** — Edits beyond the literal clauses, all inside files the condition names:
(a) The enumerator rule in `graph-conventions.md` ("An enumerator searches the working tree and never the effort's record") now says that for a node naming a deliverable, the tree searched is that deliverable's code, at the spawn's commit or the branch tip. Without this, the standard the four contracts point to would contradict clause 9. No clause names this sentence, and none of the condition's three searches finds it.
(b) The node-file template line changed from `Deliverable: <name>` to `Deliverable: <name>, <name>`, to show the list form. The paragraph above it says an implementation node holds exactly one name.
(c) Each of the three non-implementation contracts defines "deliverable" in one sentence in `## What you read`. The implementation contract defines it in the clause-9 sentence. The contracts stand alone, and the word appeared in none of them before.

## Review

### Checker run 1 — `PASS`

The checker's entry, as it wrote it:

PASS

Standards read: only the standards in `/home/mathieu/projects/graph-agent/.scratch/rename-split-upgrade/map-implementation-rules.md`. I opened no other file in the effort's directory. These bore on the work: the glossary `_Avoid_` lines, `graph-conventions.md`, the root `CLAUDE.md` `## Rules for the files under .claude/skills/` (rules for writing), and the trigger-file rule. I held `/coding-principles`, `/naming` and `/writing-for-agents` by hand through the CLAUDE.md writing rules and invoked no skill. The work changes none of the standards' required or refused elements: graph-conventions changes only the Deliverable field rules, the enumerator scope and check 12, and the work is checked against exactly those. Method: `git diff --word-diff=plain` in the worktree, plus the searches named below.

1. graph-conventions `## The node file`: the Deliverable paragraph now has three bullets. An implementation node carries the field only where its code lands on a deliverable's branch, and then holds exactly one name. A grilling, precondition or prototype node may carry it, with one or more comma-separated names. A node serving no deliverable carries none. The phrase "carried only by" is gone (grep over `.claude` for "carried only by|implementation node only|Only `implementation` nodes" finds no matches). Met.
2. Check 12 reads "Every name in a `Deliverable:` field is the name of an entry under `## Deliverables` in `map-manager-only.md`, and an `implementation` node's field holds exactly one name." The "Only implementation nodes" sentence is removed. Met.
3. Glossary **Deliverable** now says an implementation node "belongs to at most one deliverable" and "Any other node may name, in its `Deliverable:` field, every deliverable it serves." The diff does not touch the `_Avoid_` line. Met.
4. wayfinder-divergences `## Added` reads "carried by any node and holding one name on an `implementation` node". The phrase "on an `implementation` node only" is gone. Met.
5. expedition/SKILL.md: a new block sits under `## Spawning a worker`, before `### Two things that travel in a spawn`, at about line 190. It covers each deliverable's branch with the tip commit at the time the spawn is written, reading through git without checkout, the same commit for the whole attempt with a resume included, and "Make no worktree for this reading." Met.
6. The "Every worker reads a consistent snapshot" paragraph now says: implementation worker reads its own working tree; every other worker reads the main checkout and each deliverable its node names at the spawn's commit; so no worker reads a file while it is being changed. Met.
7. `### A deliverable whose base is another deliverable` now says: "A node belongs to every deliverable its `Deliverable:` field names. It may be blocked on a node belonging to any deliverable it names, or to such a deliverable's base." It keeps "A node that names no deliverable is not limited by this rule." Met.
8. In cleanup `### A merged deliverable as the region`, the first item reads "names that deliverable, and whose every named deliverable has merged". The new paragraph says a node that also names an unmerged deliverable stays out of the set, and the merged deliverable keeps its entry and its local branch, "as the passage below beginning "A deliverable that a remaining node still names" says". That passage exists further down the same section. Met.
9. `grep -rn "Run the command over the working tree" .claude` finds 4 lines, one in each of the grilling, implementation, precondition and prototype contracts. Each is followed by the new sentences: for a node that will name a deliverable, the command runs over that deliverable's code, at the spawn's commit or else the branch tip. The "never over the effort's own record" clause is kept. Met.
10. The grilling, precondition and prototype contracts each get a new paragraph under `## What you read` (headings checked by grep of `^#`). It covers reading the deliverable's files at the given commit through git without checkout, and reading "the effort's record, the map and this contract as you would otherwise". The prototype contract adds copying the needed files from that commit into `prototypes/NN-<name>/`. Each paragraph is in its own words and points to no other skill file. Met.
11. Triage `## Check each open node` has the added paragraph: an open node naming deliverables is also checked against the tip of each named deliverable's branch, read through git without checkout. Met.
12. None of the SKILL.md edits (spawn contents, deliverable base rule, snapshot paragraph) is a governing statement of a trigger-duty or of the priority. `git diff --quiet -- .claude/rules` shows `.claude/rules/expedition-triggers.md` unchanged. Met.
- Files changed: `git status` shows exactly the 10 named paths and nothing outside the scope.

Recorded searches, run as written over the working tree:
- `grep -rn "Deliverable:" .claude`: 18 lines now, because the work added mentions. `git grep` at 7a86d138e0 and at HEAD 9c0083ffbd gives 8 lines each, which matches the recorded 8. There are no hits outside the named files.
- `grep -rn "Run the command over the working tree" .claude`: 4 lines in the 4 named contracts. Matches the record.
- `grep -rn "main checkout" .claude`: 4 lines, 3 in `expedition/SKILL.md` and 1 in `expedition-upgrade/SKILL.md`. This matches the amended record. `git grep` at HEAD also gives 4. The work did not edit the upgrade hit, which is outside the named files and is reported here, as the condition says.

Bar: the root `CLAUDE.md` `## Commands` states there is no build, no tests, no formatter and no CI. The worktree root confirms this: it holds only `.claude`, `CLAUDE.md`, `CONTEXT-MAP.md`, `CONTEXT.md`, `.gitignore` and `.scratch`, with no build or CI files. `git diff --check` printed no whitespace errors. On the standards:
- Glossary `_Avoid_`: I checked the distinctive refusals in the added text by hand and found none. "attempt", "resume" and "spawn" are used as defined terms.
- Writing rules: no bolding was added, and each pointer quotes a passage rather than giving a line number.
- The prototype contract and the other worker contracts each stand alone: "deliverable" is defined inline in each of the four.

Flags (checked after the outcome):
- 10.1: true. The re-run finds the extra line in `expedition-upgrade/SKILL.md`.
- 10.2: true.
  - The enumerator rule in graph-conventions is extended to a deliverable's code.
  - The template line reads `Deliverable: <name>, <name>`.
  - Each of the four worker contracts defines "A deliverable is a piece of the effort's work that lands on its own branch."

I wrote no temporary files.

### Gate outcome — approve

The human's words, `verbatim`:

> approve

## Annotation: node 12 extends this answer to the manager's claim-time search

As the worker of [node 12](12-re-derive-a-deliverable-nodes-scope-against-its-branch.md) reported it: This extends node 10, whose answer shipped "Triage and scoping searches read deliverable branches". The manager's re-derivation before a claim, and its search for quoted passages, now read the deliverable's branch too. Nothing node 10 or node 05 says is contradicted.

## Annotation: node 14 narrows the residual clause

As the worker of [node 14](14-ship-the-rule-for-widening-scope.md) reported it: Node 10 (resolved): its condition's residual clause "reported and not edited" is superseded for future work by the three grounds. This is a narrowing of what such a clause forbids, and it does not change what node 10 landed.
