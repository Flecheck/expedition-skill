# Whether a checker may write scratch files outside the work

Type: grilling
Status: resolved

## Answer

Checker, grilling, research and cascade contracts each gain one sentence: temporary files may go in a new directory under the system's temporary directory, removed before handback.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The human took the recommendation. The node it surfaced is [node 376](376-permit-a-removed-temporary-directory.md). Flags 67.1, 67.2, 67.3 settle at the node closing report.

## Question

The checker contract's hard rule 1 is *"write no file"*. A checker on [Restructure `map.md` to what every worker
needs](59-restructure-the-map.md) had to establish that **nothing was deleted** across ~40,000 characters of prose
on both sides of a diff — a set operation. It wrote five scratch files outside the work to do it, and removed them.

In its own words:

> Hard rule 1 says *"write no file"*. Establishing clause 4 meant set operations over ~40,000 characters of prose on
> both sides of a diff. I did most of it with process substitution but wrote five files under `/tmp` for the
> comparison and removed them afterwards. Saying whether scratch outside the work is permitted would settle it,
> because **the honest alternative is to establish clause 4 by eye, which on 35 lines averaging 1,500 characters is
> not establishing it.**

**That last sentence is the whole node.** The rule as written does not merely inconvenience the checker; on any
clause requiring an exact comparison over more text than fits in a judgement, it makes the difference between
**establishing** a clause and **asserting** it. A checker that obeys the rule literally and reports `PASS` on clause
4 has done the thing the mechanical checks exist to prevent.

**Why the rule exists, so the decision does not undo it by accident.** The prohibition keeps the checker from
writing the graph, from writing the product, and from leaving anything behind that a later reader mistakes for the
work. None of those reasons reaches a temporary file outside the tree that is removed before the handover. But the
rule is stated absolutely, and a hard rule read down by an agent on its own authority is precisely what [Reconcile a
method skill's instructions with the contract's hard rules](48-method-skill-conflicts-hard-rules.md) was opened to
stop — so the reading has to be **granted**, not inferred.

## What has to be decided

1. **Whether scratch outside the work is permitted at all**, or whether the checker's route is instead to be given
   a mechanism that needs no files.
2. **Where.** The machine-local temporary directory is the obvious answer and the wrong shape for a shipped file —
   ground rule 1 forbids assuming this machine, and the human's own standing instruction refuses a bare `/tmp`.
   Stating the **property** (a location outside the work, discovered rather than declared) is the likely form.
3. **Whether it must be cleaned up, and whether an uncleaned file is a finding against the checker.** The checker
   here removed its own without being asked.
4. **Whether the same permission is owed to the other five contracts.** A worker under a no-file rule establishing
   its own work faces the identical wall, and node 59's worker reported keeping *"the scratch build scripts and the
   before-state copy"* outside the repo — so **it took the same licence, unasked, and disclosed it.** Two agents,
   two contracts, the same unstated permission exercised.

## Where it came from

Reported by node 59's checker in its retrospective, under the human's standing instruction. The manager records one
thing beyond what the checker said: **this is the second agent on the same node to write scratch outside the tree
under a no-file rule**, and neither was faulted for it, so the practice already exists and only the permission is
missing. That is the [What keeps the shipped files consistent when a decision changes a
term](29-shipped-file-consistency.md) problem in its purest form — a rule the shipped files state absolutely and
that every agent quietly reads down.

## Interview

#### Question 1, relayed 2026-10-02

*Pasted as the worker handed it back.*

```
NODE:          Whether a checker may write scratch files outside the work (node 67)
ABOUT:         Four shipped contracts forbid writing any file outright. A checker or worker that has to compare large texts exactly can only do it with temporary files. So every agent that needed such a comparison this session wrote them anyway and said so afterwards. The decision is whether the shipped rule grants this, where the files go, and what the agent owes afterwards.
SO FAR:        I read the node, map.md, the decisions.md lines for nodes 59 and 334, and every shipped contract's hard rules.
               - Contracts that ban files outright: checker rule 1 ("write no file, fix nothing, and commit nothing"), grilling rule 3, research rule 1, and cascade rule 2. Cascade's two role sections also each say "write no file".
               - Contracts that do not ban them: implementation, precondition and prototype forbid product code or graph files outside the node's own work, but nothing outside the repository. So node 59's implementer, who kept its build scripts outside the repo, broke no written rule. Only the four contracts above need a change.
               - What the ban protects: the graph, the product, and a later reader who might mistake a leftover file for the work. A temporary file outside the repository, removed before the handover, touches none of these.
               - Practice so far: the checkers on nodes 59, 367, 369 and 372, among others, wrote temporary files and disclosed them ("My only writes were scratch files in $TMPDIR").
               - Place: ground rule 1 forbids naming this machine's $TMPDIR. Your own instruction refuses a bare /tmp. The property that holds on any platform is "a new directory under the system's temporary directory". A new directory per agent also means two agents running in parallel cannot collide on a file name. That keeps true the manager contract's claim that two grilling nodes can never collide.
               - Settled by me: the shipped text says "temporary file" and not "scratch", because `.scratch/<effort>/` is already the name of the record's directory.
               - Settled by me: the files-free route is not workable. The node-59 checker already used process substitution as far as it would go, and says it still needed files. The alternative is checking by eye, which asserts a clause instead of establishing it.
ASK:           Should the four contracts that ban files (checker, grilling, research, cascade) each gain the one sentence below, and nothing more? "A temporary file is not a file in this contract's sense: you may write one in a new directory under the system's temporary directory, and you remove that directory before you hand back."
RECOMMENDED:   Yes, that one sentence in each of the four, about 190 bytes each and about 760 bytes in all. It grants the permission. It states where the files go as a property, which works on any machine and is never a bare /tmp. It requires cleanup, which removes the only remaining reason for the ban, a leftover file someone mistakes for the work. A file left behind is a defect the agent reports, not a FAIL: no other agent checks the checker, so making it a finding would need checking machinery nobody has asked for. The implementation, precondition and prototype contracts stay as they are, because they never banned such files. If you agree, I will report an implementation node to make the change, with its acceptance condition.
ALTERNATIVES:  - Same sentence, plus "and say in your handover that you used one". This adds about 40 bytes per contract and one clause to every such handover. It makes cleanup visible to the manager, but nobody checks it.
               - Grant it to the checker only. That leaves grilling, research and cascade workers facing the same problem without permission, which is the pattern of reading a rule down unasked that this node exists to stop.
               - Grant it in all seven contracts so they are uniform. This adds about 570 bytes to the three contracts that never needed it.
               - Put the permission in this effort's map only. Every future effort would then hit the same problem, since the obstacle is in the shipped text.
               - Keep the ban and use no files. Exact comparison over large texts then becomes checking by eye, so a PASS on such a clause would assert it without establishing it.

RETROSPECTIVE
1. What I had to hunt for: which contracts actually ban files outright. The node says "the other five contracts". There are six other worker contracts, and only three of them have an absolute ban. I had to grep all the hard rules to find this out.
2. What arrived that this node did not need: the decisions.md lines for nodes 59 and 334. Neither bore on the question beyond what the node file already says. Most of map.md was also unneeded; only ground rule 1 and the never-delete scope applied.
3. What would have made this easier: a list in the node of which contracts carry an absolute no-file rule, with their rule numbers.
4. What was stale, wrong or contradictory: the node's decision 4 implies node 59's implementer took a licence its rule denied. The implementation contract has no such ban, so that worker broke no written rule. The node also quotes "/tmp", while the checkers' later reports say $TMPDIR; I treated both as the same thing.
```

#### The human's answer to question 1, 2026-10-02

`verbatim`: *"ok"*

The manager had put the question with the line "Please answer: "ok for recommended", or name an alternative." So the reply takes the worker's `RECOMMENDED`: the checker, grilling, research and cascade contracts each gain the one sentence "A temporary file is not a file in this contract's sense: you may write one in a new directory under the system's temporary directory, and you remove that directory before you hand back.", and nothing more.

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      Whether a checker may write scratch files outside the work

ANSWER:        A checker or worker may write temporary files outside the repository. The four shipped contracts that ban writing any file outright are the checker, grilling, research and cascade contracts. Each gains one sentence and nothing more: "A temporary file is not a file in this contract's sense: you may write one in a new directory under the system's temporary directory, and you remove that directory before you hand back."

               Why. The ban exists to protect the graph and the product, and to keep a later reader from mistaking a leftover file for the work. A temporary file outside the repository that is removed before the handover touches none of these. Without the permission, an exact comparison over more text than fits in a judgement can only be done by eye, and a PASS on that clause asserts it rather than establishes it. The checkers on nodes 59, 367, 369 and 372, among others, had already done this and disclosed it. The permission is granted here rather than read into the rule by each agent.

               Where. The location is stated as a property ("a new directory under the system's temporary directory"), not as a path. That keeps ground rule 1, never names this machine's `$TMPDIR`, and is never a bare `/tmp`. Because each agent makes its own directory, two agents running in parallel cannot collide on a file name. So the manager contract's statement that "a grilling worker writes no file", given there as the reason two grilling nodes can never collide, still holds in its sense and stays as it is.

               Cleanup. The agent removes its directory before it hands back. It owes no disclosure in the handover. A directory left behind is a defect the agent reports, not a FAIL, because no agent checks the checker.

               Scope. The implementation, precondition and prototype contracts are unchanged. They forbid product code or graph files outside the node's own work, and nothing outside the repository, so they never banned such files. Node 59's implementer, which kept build scripts outside the repo, broke no written rule.

               Words. The shipped text says "temporary file" and not "scratch", because `.scratch/<effort>/` already names the record's directory.

               The human's reply, verbatim: "ok", given to a payload that closed with "Please answer: "ok for recommended", or name an alternative."

INDEX LINE:    Checker, grilling, research and cascade contracts each gain one sentence: temporary files may go in a new directory under the system's temporary directory, removed before handback.

FLAGS:         ASSUMPTION: the shipped sentence says "temporary file" rather than "scratch", because `.scratch/<effort>/` is already the name of the record's directory. Index sentence: Node 67's permission is worded "temporary file" so it cannot be read as the `.scratch/` record directory.
               ASSUMPTION: I set aside a files-free route as unworkable. Node 59's checker had already used process substitution as far as it would go and still needed files. Index sentence: Node 67 judged a files-free comparison route unworkable, on node 59's checker's report that process substitution was not enough.
               ASSUMPTION: the manager contract's "a grilling worker writes no file" (`.claude/skills/expedition/SKILL.md`, the paragraph on `scripts/frontier.sh`) is left unedited. Its point is that grilling nodes cannot collide, and a per-agent directory outside the repository keeps that true. Index sentence: Node 67 left the manager contract's "a grilling worker writes no file" as it is, the collision it rules out still being impossible.

NEW NODES:     Name: Let the four no-file contracts permit a removed temporary directory
               Kind: implementation
               Question: Carry node 67's answer into the checker, grilling, research and cascade contracts.
               Blockers: none. It shares `.claude/skills/expedition-checker/SKILL.md` with node 214 (claimed), and the grilling and research contracts with node 41 (open). Those nodes' conditions concern other sentences, so this is a code-slot collision for the manager to schedule, not a defect to join.
               Acceptance condition:
               1. Each of the four files below gains the following sentence, word for word, read with line breaks unwrapped into spaces: "A temporary file is not a file in this contract's sense: you may write one in a new directory under the system's temporary directory, and you remove that directory before you hand back." In each file it appears exactly once, as the last sentence of the numbered item under `## Hard rules` named here:
                  - `.claude/skills/expedition-checker/SKILL.md`, item 1, which begins "Leave everything as you found it"
                  - `.claude/skills/expedition-grilling/SKILL.md`, item 3, which begins "Put your work in what you hand back"
                  - `.claude/skills/expedition-research/SKILL.md`, item 1, which begins "Put all your work in your handover"
                  - `.claude/skills/expedition-cascade/SKILL.md`, item 2, which begins "Write no file, in either role"
               2. In those four files, no other text changes except the rewrapping of the item that receives the sentence. Every other line keeps the width the file already uses. In particular, the sentences in the cascade contract that say "write no file" under its two `### What you do` sections stay as they are.
               3. No other file in the repository changes.
               4. Scope search: the command `grep -rn -i 'write no file' .claude/skills/`, run over the working tree, returned six lines in four files. Those are the checker contract's hard rule 1, the grilling contract's hard rule 3, the research contract's hard rule 1, and three lines of the cascade contract (hard rule 2 and one sentence in each of its two `### What you do` sections). The four files in clause 1 are the whole scope. If the same search, run while doing the work, finds the phrase in any file outside these four, report it and do not edit it.

INVALIDATIONS: Extension, not contradiction, of the four contracts' absolute no-file rules: a temporary directory outside the repository, removed before handback, is now permitted. Narrowing of node 48's ground, as it applies to this rule: an agent reading the no-file rule down on its own authority stops being the issue, because the reading is now granted in the rule's text. No resolved node's answer is contradicted.

CONDITIONS:    I searched the conditions and questions of every open and claimed node for "write no file", "temporar", "scratch file", "TMPDIR", and the paths of the four contracts.
               - Node 214 (claimed), clause 3: "No other sentence of `.claude/skills/expedition-checker/SKILL.md` changes to carry clauses 1 and 2". It is limited to that node's own clauses, so the new node does not break it. No replacement is written.
               - Node 41 (open), clause 8, and node 375 (claimed), clause 7, each say the checker contract "is not changed by this work". Each binds only its own work. No replacement is written.
               - Node 41 also edits the grilling and research contracts, at sentences other than the hard rules. No clause needs changing.
               - No open node's question changes.

MISSING FROM MAP: The map does not say which shipped contracts carry an absolute no-file rule. I found that by grepping the hard rules of all seven worker contracts.

How I grilled: no method skill was invoked, so no part of one was skipped.

RETROSPECTIVE
1. What I had to hunt for: at the resume, whether any node landed since the question had touched the four contracts. The manager said none had, and I confirmed it with the scope search. I also had to check the open nodes' conditions on the same files (214, 41, 375) for clauses the new node could break.
2. What arrived that this node did not need: the list of landed nodes 370, 371, 373 and 374. None of them touches the four files.
3. What would have made this easier: if each open node's file showed which files its work touches, the collision check would not need a search.
4. What was stale, wrong or contradictory: nothing new since the first payload. The earlier point stands: the node's decision 4 says node 59's implementer took a licence it was denied, but the implementation contract has no such ban.
`````

## Flags

`67.1` `ASSUMPTION` **· settled** — Node 67's permission is worded "temporary file" so it cannot be read as the `.scratch/` record directory. *(The worker's full text is under its handover's `FLAGS`.)*

`67.2` `ASSUMPTION` **· settled** — Node 67 judged a files-free comparison route unworkable, on node 59's checker's report that process substitution was not enough. *(The worker's full text is under its handover's `FLAGS`.)*

`67.3` `ASSUMPTION` **· settled** — Node 67 left the manager contract's "a grilling worker writes no file" as it is, the collision it rules out still being impossible. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-10-02:* flags 67.1, 67.2, 67.3 settle at the node closing report that closes this node.
