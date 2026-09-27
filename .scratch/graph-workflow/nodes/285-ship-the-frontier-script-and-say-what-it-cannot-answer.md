# Ship the frontier script and say what it cannot answer

Type: implementation
Status: resolved

Blocked by: none

## Question

*Surfaced by [node 273](273-a-script-that-answers-what-can-be-started.md)'s worker, and pasted as it wrote it.*

> Write and ship the read-only frontier script node 273 decided on, and state in the manager's contract that it
> exists and where it is partial.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 273's worker. Pasted as it wrote it, and not the manager's.*

> A script exists at `.claude/skills/expedition/scripts/frontier.sh` and is executable. It is written in POSIX shell
> and awk only: no bash-only syntax, and no dependency on python, perl, node, jq or any other interpreter.
>
> Its first argument is the path to an expedition's graph directory — the directory holding `map.md` and a `nodes/`
> subdirectory of `NN-<name>.md` files. It optionally takes two further integers: the target number of concurrently
> running nodes that need the human, and the target number of implementation nodes, each defaulting to 2 when not
> given. **It hardcodes no path; in particular the strings `.scratch` and `graph-workflow` appear nowhere in it.**
>
> It writes no file and modifies nothing. Running it leaves the tree byte-identical.
>
> From each `nodes/NN-<name>.md` it reads only the header block — every line above the first line beginning with
> `## ` — and takes three fields from it: `Type:`, `Status:` and `Blocked by:`. It reads no field from below the
> first `## ` heading, and treats no text inside a fenced code block as a field.
>
> From the `Blocked by:` field it takes a node number only where that number lies outside every backtick-delimited
> code span, outside every `~~...~~` strikethrough, and outside the parenthesised target of every markdown link.
> **Four worked examples it must satisfy**, each written as the field's literal content followed by what must be
> taken from it:
>
> ```
> `123, 120`                                                       -> 123 and 120
> `[node 269](269-ignore-the-new-worktree-path.md)`                -> 269 only
> `none — [node 139](139-move-the-managers-material.md) landed as `4e38c11`` -> 139 only
> `~~95~~ **none — node 95 resolved and landed at `b095bb6`.**`    -> nothing
> ```
>
> An empty field, and the literal `none`, mean no blocker.
>
> It reports a node as startable when its `Status:` is `open`, it is not `claimed`, and every blocker taken from its
> `Blocked by:` field names a node whose own `Status:` is `resolved`. **No other status value satisfies a blocker.**
>
> Its output carries three things, in this order, each labelled in plain words:
>
> 1. for each of `grilling` and `implementation`, how many nodes hold `Status: claimed`, shown against the
>    corresponding target passed in or defaulted;
> 2. how many nodes are startable in total, and how many of each `Type:`;
> 3. the startable nodes themselves, grouped by `Type:`, one per line, each line carrying the node's number and its
>    name.
>
> It orders the startable nodes by nothing beyond that grouping, and it performs no check of the graph's internal
> consistency — no dangling-edge, back-edge, reused-number, label, index or flag check.
>
> Its opening comment states, in two sentences, that it reads only the expedition's own graph files and assumes
> nothing about the repository the expedition is being run on.
>
> `.claude/skills/expedition/SKILL.md`, under its existing `### Picking the next node` heading, gains a short
> passage that: names the script by its path relative to the skill directory; says the manager runs it when a node
> finishes, to see what is startable and whether a slot has emptied; and states in one sentence each that **the
> script cannot tell whether two startable nodes would edit the same file**, because no field records which files a
> node touches, so the manager applies that filter itself before filling a second implementation slot — and that
> **two grilling nodes can never collide**, a grilling worker writing no file.
>
> **Verification the checker performs:** run the script against the graph directory at `.scratch/graph-workflow` in
> this repository. It exits 0, writes nothing, and prints the three labelled sections above. The checker then picks
> **ten** `nodes/NN-<name>.md` files at random, reads each one's `Status:` and `Blocked by:` fields and the
> `Status:` of each node those fields name, works out by hand whether each of the ten is startable, and confirms the
> script's output agrees on all ten. The checker also confirms the four `Blocked by:` examples above are handled as
> stated, by reading the parsing code where no node in the tree exercises a case.
>
> No file other than the two named above changes.

## The manager's note at filing

*Not a change to anything above.*

**This is the first executable this effort ships**, and every ground rule on it was written for markdown
deliverables. **The argument for why ground rule 1 does not reach it is in [node
273](273-a-script-that-answers-what-can-be-started.md)'s answer and is load-bearing** — the rule guards the *host
project's* stack, and this script reads only the expedition's own markdown in a format the workflow itself creates.
**A worker on this node should carry that argument rather than re-derive it**, and a checker should hold the script
against it.

**The condition's verification clause is unusually strong and that is deliberate.** It makes the checker compute ten
nodes' startability by hand and compare, and read the parsing code for the cases no live node exercises. **That is
the only part of this node a `PASS` cannot be reached on by inspection.**

**The manager is the party the script exists to correct**, having reported *"nothing is waiting on you"* three times
in one session with slots free and work startable. It is worth a claiming worker knowing that the failure is
measured rather than supposed.

## Interview

### Attempt 1

#### The worker's raise, 2026-09-27

*The worker's payload, pasted as handed back. It holds a question about the acceptance condition, which the standing yes never covers.*

````
NODE:          Ship the frontier script and say what it cannot answer (285)
ABOUT:         Ships `.claude/skills/expedition/scripts/frontier.sh`, a read-only POSIX sh and awk script, plus a passage under `### Picking the next node` in `.claude/skills/expedition/SKILL.md`. Both are written and tested, uncommitted, in worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/285-frontier`. The only thing still open is one example in the acceptance condition that contradicts the condition's own parsing rule.
SO FAR:        What I read: my contract; node 285; map.md (Notes: no source hierarchy); map-implementation-rules.md; the decisions.md lines on the frontier (nodes 05, 10 and 273); graph-conventions.md `## Reading the graph` (node 339's rule 3 with its four examples); node 339's file, searched for its examples.
               What I built:
               - The script takes GRAPH_DIR [HUMAN_TARGET [IMPLEMENTATION_TARGET]], each target defaulting to 2. A bad argument exits 2 with a message.
               - It reads Type:, Status: and Blocked by: only from the header block. It skips fenced blocks.
               - It takes numbers from Blocked by: outside code spans (a run of N backticks is closed by a run of N backticks), outside ~~...~~ and outside link targets. A number counts only as a whole token, and leading zeros are ignored ("07" means node 7).
               - A node is startable when it is open and every blocker it names is resolved.
               - It prints three labelled sections: claimed grilling and implementation counts against their targets, startable totals per type, and the startable nodes grouped by type.
               - Its opening comment is the two sentences the condition asks for. The strings `.scratch` and `graph-workflow` appear nowhere in it. It is executable.
               - The SKILL.md passage is 7 lines at the file's wrap width. It names `scripts/frontier.sh`, says to run it when a node finishes, and says how to call it. It gives the same-file limit and the grilling-cannot-collide sentence, one sentence each.
               What I tested:
               - Against the main checkout's live graph `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/`: exit 0, 71 startable nodes (31 grilling, 2 research, 1 precondition, 37 implementation), claimed 1 grilling and 1 implementation. The sha256 of every record file was the same before and after the run.
               - An independent grep and sed computation agrees on all 75 open-status files. It differed on one node, 13, but that was my cross-check's bug: it matched `Status: open` in a body line, and 13 is resolved.
               - Only one open node uses a non-plain form live: 271, `[node 269](...)`, which the script lists as startable, correctly.
               - Fixture graph in $TMPDIR: every form from the condition and from graph-conventions, plus double-backtick spans, a fenced `Blocked by:`, leading zeros, a claimed blocker, a dangling blocker, and empty and `none` fields. All behave as the rule states.
               - The bar: the repo states no build, test, format or shell-check command, which matches the record. I ran shellcheck -s sh (clean). Output is byte-identical under dash with gawk, dash with mawk, busybox sh with busybox awk, and gawk in POSIX mode.
               Settled on my own authority (these will be ASSUMPTION flags):
               - The name printed is the filename's `<name>` part.
               - A missing `Blocked by:` field means no blocker, since graph-conventions says an optional field appears only when it has a value.
               - A digit run inside a word is not a node number.
               - The per-type counts list all five known types, zeros included.
               - Nodes inside a group are listed by ascending number.
               - The first `## ` line ends the header block even inside a fence, which is the condition's literal wording.
ASK:           Example 4 of the condition says `~~95~~ **none — node 95 resolved and landed at `b095bb6`.**` -> nothing. The condition's own rule (numbers outside code spans, strikethrough and link targets) takes 95 from the prose "node 95", and so does graph-conventions.md rule 3, which gives 277 for the identical node-277 form. Should the script follow the stated rule and graph-conventions, with the example amended to "-> 95, which blocks nothing because node 95 is resolved"?
RECOMMENDED:   Yes: amend example 4 to "-> 95 (node 95 is resolved, so it blocks nothing)" and keep the script as built. Three grounds:
               - The rule sentence and graph-conventions.md, which is part of this effort's bar, both demand 95.
               - Node 339's worker already found and flagged this exact gap (its flag 339.3, settled).
               - Startability is identical either way on every live node, because every such struck-then-repeated form in the graph names a resolved node.
ALTERNATIVES:  - Add a special rule so that a number already struck in the same field is not taken again. This satisfies example 4, but the script then diverges from graph-conventions.md rule 3, and that file would need the same rule. That reaches beyond this node, which is trigger 2.
               - Ship as built and leave the condition as it stands, with a flag. The checker is told to confirm example 4 "as stated", so it would FAIL on it.

RETROSPECTIVE
1. What I had to hunt for:
   - Whether example 1's backticks are literal or only mark the example. Example 3's closing ``` `4e38c11`` ``` settles it: they only mark the example.
   - Real `Blocked by:` forms in the live graph.
   - That 102 node files have no `Blocked by:` field at all, and whether that is legal (graph-conventions: optional fields appear only when they have a value).
   - That numbers are zero-padded (`06`, `07`).
   - A POSIX shell and awk to test with. None is installed, so I fetched dash, mawk, busybox and shellcheck through `nix shell`.
2. What arrived that this node did not need: the "Nothing else is running beside you on SKILL.md" note. The manager's note that the worktree's record is old mattered only for choosing which graph to test against.
3. What would have made this easier:
   - The spawn noting that example 4 conflicts with node 339's rule 3. The manager's own note tells me to follow that rule, so the conflict was knowable from the record: 339.3 records it.
   - The node file saying whether "name" means the `# ` title or the filename slug.
4. What was stale, wrong or contradictory:
   - Example 4 of node 285's condition contradicts its own rule sentence and graph-conventions.md rule 3; this is the raise above.
   - The manager's note cites `Blocked by: ~~338~~` as an example of the forms, but no open node carries a struck form. Only 271's link form is exercised live, so the struck and code-span forms can be tested only by fixture.
````

#### The human's answer, 2026-09-27

The human, `verbatim`: *"ok for recommended"*. The recommendation it takes, the worker's: "Yes: amend example 4 to "-> 95 (node 95 is resolved, so it blocks nothing)" and keep the script as built."

## Amendment by the human, 2026-09-27

*Made on the human's "ok for recommended" above, which took the worker's recommendation to amend the example. The manager writes it as a direct substitution; the original clause above is left as it was.*

- **Example 4.** Where the condition gives `~~95~~ **none — node 95 resolved and landed at `b095bb6`.**` -> nothing, read: -> 95 (node 95 is resolved, so it blocks nothing).

## Answer

The frontier script ships as a read-only POSIX sh and awk script. It reads the header fields and parses `Blocked by:` by graph-conventions rule 3. SKILL.md says the script cannot see file collisions between nodes.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `353689f`. Flags 285.1, 285.2, 285.3, 285.4 settle at the node closing report.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      Ship the frontier script and say what it cannot answer

ANSWER:        Shipped `.claude/skills/expedition/scripts/frontier.sh` and a passage under `### Picking the next node` in `.claude/skills/expedition/SKILL.md`.

               **The script.**
               - It is executable and written in POSIX sh and awk, calling no other interpreter. It writes nothing.
               - It takes `GRAPH_DIR [HUMAN_TARGET [IMPLEMENTATION_TARGET]]`, and each target defaults to 2. A wrong argument count, a target that is not a non-negative integer, a directory without `map.md` and `nodes/`, or a directory with no `NN-<name>.md` files exits 2 with a message on stderr.
               - From each `nodes/NN-<name>.md` it reads `Type:`, `Status:` and `Blocked by:`, taking the first occurrence of each. It reads only the lines above the first line beginning with `## `, and skips lines inside a fence opened by ``` or `~~~`. A `## ` line ends the header block even inside a fence, which is the condition's literal wording.
               - The node number comes from the filename prefix, compared as a number, so `07` names node 7. The printed name is the filename's `<name>` part, not the `# ` title.
               - In `Blocked by:` it removes three things, in this order: code spans (a run of N backticks is closed by the next run of exactly N), then `~~...~~`, then link targets `](...)`. It then takes every whole number token that is left.
               - A number is a whole token: a run of digits with no letter or digit next to it. So digits inside a bare hash outside a code span are not taken.
               - An empty field, the literal `none`, and a missing field (graph-conventions: an optional field appears only when it has a value) mean no blocker.
               - The human's amendment to example 4 holds: ``~~95~~ **none — node 95 resolved and landed at `b095bb6`.**`` gives 95, and 95 blocks nothing because it is resolved.
               - A node is startable when its status is `open` and every blocker names an existing node whose status is `resolved`.
               - Output has three sections, in order: claimed grilling and implementation counts shown against their targets; startable nodes in total and per type, all five known types listed with zeros included and any unknown type after them; then the startable nodes grouped by type, one `NN name` line each.
               - Within a group nodes are listed by ascending number, which is no ranking. It makes no consistency check.
               - Its opening comment states in two sentences that it reads only the expedition's own graph files and assumes nothing about the repository.

               **The SKILL.md passage.**
               - It names `scripts/frontier.sh`, beside the file.
               - It says to run the script when a node finishes, to see what is startable and whether a slot has emptied, and how to call it.
               - It says in one sentence that the script cannot tell whether two startable nodes would edit the same file, because no field records which files a node touches, so the manager applies that filter before filling a second implementation slot.
               - It says in one sentence that two grilling nodes can never collide, because a grilling worker writes no file.

               **Why ground rule 1 does not reach the script.** This is node 273's argument, carried rather than re-derived. The rule guards the host project's stack, and this script reads only the expedition's own markdown, in a format the workflow itself creates.

               **Tests.**
               - Run against the main checkout's live graph `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/`: exit 0, with 71 startable nodes (31 grilling, 2 research, 1 precondition, 37 implementation) and 1 of 2 claimed of each kind. The sha256 of every record file was the same before and after the run.
               - An independent grep and sed computation agrees on every open node.
               - Only node 271 exercises a non-plain form live: `[node 269](...)`, which gives startable. The other forms were tested with fixtures, covering every example in the condition and in graph-conventions.md.
               - The fixtures also covered double-backtick spans, a fenced `Blocked by:`, zero-padded numbers, a claimed blocker, a dangling blocker, and empty and `none` fields.
               - Output is byte-identical under dash with gawk, dash with mawk, busybox sh with busybox awk, and gawk in POSIX mode. `shellcheck -s sh` is clean.

INDEX LINE:    The frontier script ships as a read-only POSIX sh and awk script. It reads the header fields and parses `Blocked by:` by graph-conventions rule 3. SKILL.md says the script cannot see file collisions between nodes.

FLAGS:         ASSUMPTION: The printed node name is the filename's `<name>` part, not the `# ` title. The condition speaks of `nodes/NN-<name>.md` and restricts the fields read to three.
               Index: The frontier script prints each node's filename name part rather than its `# ` title line.

               ASSUMPTION: A node number in `Blocked by:` is a whole digit token not adjacent to a letter or digit. Digits inside a bare word, such as an unquoted commit hash, are not read as a node number. The condition says "number" and does not say how to handle digits inside a word.
               Index: The frontier script takes only whole digit tokens from `Blocked by:`, so an unquoted hash yields no node number.

               ASSUMPTION: A node file with no `Blocked by:` field has no blockers. Graph-conventions says an optional field appears only when it has a value, and 102 live node files omit the field.
               Index: The frontier script treats a missing `Blocked by:` field as no blocker, as graph-conventions' optional-field rule implies.

               ASSUMPTION: The per-type counts list all five known types, zeros included. Within each group, nodes are listed by ascending number, as a neutral order and not a ranking. The condition forbids ordering beyond the grouping but must print them in some order.
               Index: The frontier script lists every known type's count including zeros, and lists nodes within a type by ascending number.

NEW NODES:     none

INVALIDATIONS: Node 05 (How the graph's bookkeeping is kept straight) is extended, not contradicted. The graph stays markdown and prose rules, and the read-only frontier command it named as the first thing to extract now exists as a script. Node 273 is carried out as decided. Its condition's example 4 was amended by the human to agree with graph-conventions.md rule 3 (node 339).

CONDITIONS:    I searched every open and claimed node's `## Acceptance condition` for `frontier`, `scripts/`, `Picking the next node` and `startable`. The only matches outside node 285 were node 149's ordinary use of "startable", which my work does not affect. No replacements.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings: none yet; no checker has run.
               Paths touched, in worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/285-frontier`:
               - `.claude/skills/expedition/scripts/frontier.sh` (new, mode 755)
               - `.claude/skills/expedition/SKILL.md` (8 lines added after "sometimes more than one node." under `### Picking the next node`)
               Outside the worktree I wrote only throwaway fixtures under $TMPDIR.
               The bar: the repo states no build, test, format or shell-check command, which matches map-implementation-rules.md. I ran shellcheck and four shell and awk combinations anyway.
               Proposed commit message:
                 Ship the frontier script and say what it cannot answer

                 Add .claude/skills/expedition/scripts/frontier.sh, a read-only POSIX sh
                 and awk script that reports claimed counts against their targets and
                 the startable nodes by type, parsing Blocked by: per graph-conventions
                 rule 3. State in the manager's contract when to run it, and that it
                 cannot see file collisions between startable nodes.

                 Node: graph-workflow/285

RETROSPECTIVE
1. What I had to hunt for:
   - Whether the condition's examples used literal or delimiting backticks. Example 3's closing ``` `4e38c11`` ``` settles it: they only mark the example.
   - The real `Blocked by:` forms in the live graph.
   - That 102 node files have no `Blocked by:` field, and whether that is legal.
   - That numbers are zero-padded (`06`, `07`).
   - A POSIX shell and awk to test with. None is installed, so I fetched dash, mawk, busybox and shellcheck through `nix shell`.
2. What arrived that this node did not need: the note that nothing else was running on SKILL.md. The note that the worktree's record is old mattered only for choosing which graph to test against.
3. What would have made this easier:
   - The spawn pointing out that example 4 conflicted with graph-conventions rule 3. The conflict was on the record as flag 339.3 and cost one raise round.
   - The node file saying whether "name" means the `# ` title or the filename slug.
4. What was stale, wrong or contradictory:
   - Example 4 of the original condition contradicted its own rule sentence and graph-conventions.md; this is now amended.
   - The spawn cited `Blocked by: ~~338~~` as a form the script meets, but no open node carries a struck form. Only 271's link form is exercised live.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 109's check; the condition reached it as a verbatim copy in `$TMPDIR/c285.md`.*

> PASS
>
> Node 285, "Ship the frontier script and say what it cannot answer". The work is in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/285-frontier` on base 8c1053b: the untracked `.claude/skills/expedition/scripts/frontier.sh` and an uncommitted diff to `.claude/skills/expedition/SKILL.md`. I read the whole condition in `/tmp/claude-1000/c285.md`, taking example 4 as the human's amendment reads it (→ 95).
>
> **Parts of the condition**
>
> - **Exists, executable, POSIX shell and awk only:** met.
>   - `ls -l` shows `-rwxr-xr-x` and the shebang is `#!/bin/sh`.
>   - `shellcheck -s sh` finds nothing (exit 0). The shell uses only `set -eu`, `case`, `[`, `${n:-2}` and `set --`.
>   - The awk program uses only POSIX awk: `match`, `RSTART`/`RLENGTH`, `gsub`, `split`, `in`. It runs identically under `dash` with `mawk`, `busybox awk` and `gawk --posix`, all run through `nix shell`.
>   - It calls no other interpreter.
> - **Arguments; no hardcoded path:** met.
>   - It takes `GRAPH_DIR [HUMAN_TARGET [IMPLEMENTATION_TARGET]]`, and each target defaults to `2` (`${2:-2}`, `${3:-2}`).
>   - `grep -nE '\.scratch|graph-workflow'` over the script returns nothing.
> - **Writes nothing:** met.
>   - I took an md5 over every file, first in the worktree's `.scratch/graph-workflow` and then in the live graph at `/home/mathieu/projects/graph-agent/.scratch/graph-workflow` (excluding `worktrees/`).
>   - I ran the script under `dash` against each and took the md5 again. Both sets were unchanged, and the worktree's `git status --porcelain` was unchanged.
> - **Header block only, three fields, fences skipped:** met.
>   - It stops at the first `^## ` line, toggles on fenced lines (lines starting with a backtick or tilde fence) and skips what is inside them, and takes only the first `Type:`, `Status:` and `Blocked by:` in the header.
>   - Synthetic test: a node with `Blocked by: 7` inside a header fence and again below `## Q` is treated as unblocked. A node whose `Status:` appears only below its first heading is not treated as open.
>   - Live check: node 13 has `Status: open` inside a body fence and `Status: resolved` in its header. The script reads it as resolved, which is correct.
> - **`Blocked by:` parsing, with the four examples:** met. I read the parser and ran a synthetic graph in `$TMPDIR` under all three awks.
>   - The parser first strips backtick code spans, pairing a run of N backticks with the next run of exactly N. It then strips `~~…~~` strikethroughs, then `](…)` link targets, and takes only the words that are all digits.
>   - I read the outer backticks in the condition's example block as delimiters of each field's literal content. Example 1 only makes sense that way.
>   - `123, 120` gives 123 and 120.
>   - `[node 269](269-….md)` gives 269 only.
>   - `none — [node 139](139-….md) landed as `4e38c11`` gives 139 only.
>   - `~~95~~ **none — node 95 resolved and landed at `b095bb6`.**` gives 95, as amended.
>   - Extra cases:
>     - `landed as `4444``: the code-span digits are not taken, so the node is startable.
>     - `[node 95](7-open-target.md)`: the digits in the link target are not taken, so the node is startable.
>     - `~~7~~ 95`: startable.
>     - A double-backtick span holding `` `7` `` is stripped whole.
>     - A blocker naming an open node blocks.
>     - A blocker naming a superseded node blocks.
>     - A blocker naming a nonexistent node blocks.
> - **Empty field and `none` mean no blocker; only `resolved` satisfies a blocker:** met. There is no digit to take in either case. The code requires `statuses[b] == "resolved"` for every blocker, and only `open` nodes can be startable.
> - **Output, three labelled parts in order:** met. In the live run (exit 0), the output reads:
>   1. "Claimed nodes against their target:", then "grilling, the nodes that need the human: 0 of 2" and "implementation, the nodes that hold a code slot: 2 of 2";
>   2. "Startable nodes: 71 in total", then one count per `Type:`;
>   3. "Startable <type> nodes:" groups, one `NN name` line each.
>   - The startable nodes are grouped by type and listed within each group by node number. There is no priority or ranking.
>   - It runs no consistency check. Its only refusals are input validation: bad arguments, a missing `map.md` or `nodes/`, or no node files.
> - **Opening comment in two sentences:** met. "Reads only the expedition's own graph files, the node files under the graph directory it is given. It assumes nothing about the repository the expedition is being run on."
> - **The SKILL.md passage under `### Picking the next node`:** met. The hunk sits after the two-counts paragraph in that section.
>   - It names "`scripts/frontier.sh`, beside this file".
>   - It says "Run it when a node finishes, to see what is startable and whether a slot has emptied."
>   - One sentence says it "cannot tell whether two startable nodes would edit the same file, because no field records which files a node touches, so apply that filter yourself before you fill a second implementation slot."
>   - One sentence says "Two grilling nodes can never collide, because a grilling worker writes no file."
> - **The checker's verification:** met.
>   - Against the live graph directory, the script exits 0, writes nothing, and prints the three sections.
>   - I picked ten node files at random (`ls | shuf -n 10`) and read only each one's header `Status:` and `Blocked by:`. They were 105, 170, 47, 199, 119, 109, 213, 98, 171 and 44.
>   - By hand, only 170 (open, `none`) and 44 (open, no field) are startable, because the other eight are resolved or superseded. The script lists 170 and 44 and none of the other eight, so it agrees on all ten.
>   - Ten of the picks were not open, so I also checked five open nodes that have blockers, reading each blocker's header `Status:`:
>     - 149 (144 resolved), 256 (255 resolved) and 230 (229 resolved) are startable, and the script lists them.
>     - 135 (126 resolved, 130 open) is blocked, and the script does not list it.
>     - 13 is resolved, as above, and is not listed.
>   - The four examples are established by the synthetic runs and my reading of the parser, as above.
>   - The condition directs this verification, so I read those header fields as test data only. I took nothing else from those files.
> - **No other file changes:** met. `git status --short --untracked-files=all` shows only `M .claude/skills/expedition/SKILL.md` and `?? .claude/skills/expedition/scripts/frontier.sh`.
>
> **The bar**
>
> - The repo has no build, tests, formatter or CI. For the script, the checks that apply are:
>   - `shellcheck -s sh` is clean;
>   - it runs under `dash`, and under `mawk`, `busybox awk` and `gawk --posix`, with the same output from each.
> - `git diff --check` is clean (exit 0).
> - No added line in SKILL.md exceeds the file's wrap width.
>
> **Standards**
>
> As in my earlier checks, I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`.
>
> - These bore on the work:
>   - `/coding-principles`: the script fails loudly with a message and exit 2 on bad input rather than silently.
>   - `/naming`: the names are descriptive (`blocker_numbers`, `strip_code_spans`, `startable_by_type`).
>   - The CONTEXT.md `_Avoid_` lines: nothing refused appears in the added text.
>   - The writing rules.
>   - `/writing-for-agents`.
>   - The ground rules: the script reads only the graph directory it is given and assumes no repo or machine. POSIX sh and awk are what the condition itself demands.
> - No reviewing skill is named, so I ran none.
> - I removed the synthetic graph and outputs I made in `$TMPDIR`.
>
> NOT COVERED:
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The condition does not demand this; the rules file makes it a bookkeeping rule. The worktree shows no such change. What the main tree's record holds is outside what I was given.

### Gate — approve, `standing yes`, 2026-09-27

Taken under the standing yes recorded in `map.md`'s `## Notes` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and its one NOT COVERED item is the worker's bookkeeping. This settles none of the node's flags; they settle at the node closing report.

## Flags

`285.1` `ASSUMPTION` **· settled** — The printed node name is the filename's `<name>` part, not the `# ` title. The condition speaks of `nodes/NN-<name>.md` and restricts the fields read to three. — The frontier script prints each node's filename name part rather than its `# ` title line.

`285.2` `ASSUMPTION` **· settled** — A node number in `Blocked by:` is a whole digit token not adjacent to a letter or digit. Digits inside a bare word, such as an unquoted commit hash, are not read as a node number. The condition says "number" and does not say how to handle digits inside a word. — The frontier script takes only whole digit tokens from `Blocked by:`, so an unquoted hash yields no node number.

`285.3` `ASSUMPTION` **· settled** — A node file with no `Blocked by:` field has no blockers. Graph-conventions says an optional field appears only when it has a value, and 102 live node files omit the field. — The frontier script treats a missing `Blocked by:` field as no blocker, as graph-conventions' optional-field rule implies.

`285.4` `ASSUMPTION` **· settled** — The per-type counts list all five known types, zeros included. Within each group, nodes are listed by ascending number, as a neutral order and not a ranking. The condition forbids ordering beyond the grouping but must print them in some order. — The frontier script lists every known type's count including zeros, and lists nodes within a type by ascending number.

*The manager's note, 2026-09-27:* flags 285.1, 285.2, 285.3, 285.4 settle at the node closing report that closes this node, which names its gate as taken under the standing yes.
