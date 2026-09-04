# The graph's records name absolute paths on a machine that no longer exists

Type: implementation
Status: claimed

Blocked by: none

## Question

*Minted by the manager on the human's direction. The question below is the manager's own.*

Thirty-six paths across sixteen of this effort's graph files name this repository as
`/home/mathieu/projects/graph-agent/…` — the repository under a former name on a former machine. That directory does
not exist here. Six of the sixteen files are **open** implementation nodes whose acceptance condition opens by naming
where the work is, so those six state a location their worker and their checker cannot reach. Write every one of
those paths relative to the repository root instead.

**The human's direction**, `verbatim`:

> ok well obviously the project just lives at the root of the current git repository, not in
> /home/mathieu/projects/graph-agent/ - that's the writing that will work everywhere. Update all referenced places,
> then continue.

and, scoping it:

> the "Lang" project references can stay for now.

**What the direction reaches, and what it leaves.** It names the `graph-agent` prefix, and Lang is excepted by name.
Eight further occurrences name files on that machine outside any project — `~/.claude/`, `~/dotfiles/`,
`~/.nix-profile/` — inside research and grilling nodes reporting where something was found there. Those are
statements about an external machine rather than pointers into this repository, and no repo-relative form expresses
them, so this node leaves them alone. **That scoping is the manager's reading rather than the human's words**, and it
is flagged below.

**Why this is a node rather than a manager edit.** Rewriting an acceptance condition is never the manager's, and six
of the sixteen files are live conditions. The human directed the change, which settles *whether*; the change itself
is a worker's.

## Acceptance condition

***Written by the manager***, this node having been minted by the manager and having no spawning node. Read back
against the two rules binding every condition and found to meet both: it is **self-contained text** — its three
enumerators are written out, its transformation is stated with a worked example, and it sends its reader nowhere to
learn what is demanded; and it **does not quantify over the record**, every clause being answerable from the
enumerators and the diff.

The work is this repository's working tree, and the files it touches are under `.scratch/graph-workflow/`. **Editing
those files is what this node is for**: its subject is the graph's own records rather than a report of progress on
other work. The worker may edit the files the clause 1 enumerator names; it may not mark this node, resolve it, or
write a line in `.scratch/graph-workflow/decisions.md` or `.scratch/graph-workflow/flags.md`.

Done means every one of the following is true of the finished tree.

1. *Recorded enumerator:* `git grep -c -F '/home/mathieu/projects/graph-agent' -- .`, which at commit `c3d50bf`
   returned **36 occurrences across 16 files**. Re-run it; the demand is that it return nothing, whatever the count
   has become.

2. Each of those occurrences is replaced by the path it names, written relative to the repository root: the prefix
   `/home/mathieu/projects/graph-agent/` is removed and everything after it is kept exactly. So
   `/home/mathieu/projects/graph-agent/.claude/skills/expedition/graph-conventions.md` becomes
   `.claude/skills/expedition/graph-conventions.md`, and
   `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/` becomes `.scratch/graph-workflow/`. Every one of the
   36 carries a path after the prefix, so no occurrence needs a rewritten sentence in order to lose it.

3. **Nothing else in any file changes.** No sentence is reworded, no text is deleted, summarised or shortened, no
   struck-through text is unstruck, and no heading or clause is renumbered. This is a repair of pointers and not a
   change of meaning: for every line that changes, the line before and the line after it differ only by the removed
   prefix.

4. *Recorded enumerator:* `git grep -c -F '/home/mathieu/projects/Lang' -- .`, which at commit `c3d50bf` returned **4
   occurrences across 4 files**. Re-run it; the demand is that it return those same four, unchanged. They name a
   project outside this repository and are deliberately left as they are.

5. *Recorded enumerator:* `git grep -c -E '/home/mathieu/(\.claude|\.nix-profile|dotfiles)' -- .`, which at commit
   `c3d50bf` returned **8 occurrences across 6 files**. Re-run it; the demand is that it return those same eight,
   unchanged. They name files on a machine outside this repository, are reports of where something was found there,
   and have no repo-relative form.

6. No file outside `.scratch/graph-workflow/` is modified.

7. Every markdown link whose target this node rewrote resolves to a path that exists, read from the repository root.

8. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This node blocks five others.** Nodes [134](134-repair-two-context-defects-node-113-found.md),
[140](140-move-the-implementers-and-checkers-material-out-of-the-map.md),
[142](142-bring-graph-conventions-map-shape-into-line.md),
[143](143-rules-arrive-by-the-spawn-never-by-a-search.md),
[144](144-make-the-rules-file-stand-alone.md) and
[146](146-graph-conventions-map-rules-name-two-notes-sections.md) each carry a condition naming the unreachable
prefix. **No `Blocked by:` edge has been added to any of them**: the graph's own rule is that an edge is satisfied
only by a `resolved` node and no edge is inferred from anything else, and the manager has not decided that those six
must wait rather than be repaired under them. It is a sequencing matter, and with a code slot of one they serialise
regardless.

**Nothing recurs-proofs this.** What stops the next condition being written with an absolute path is unwritten; that
is a node rather than something this one carries, and it is not yet minted.

## Flags

`147.1` `ASSUMPTION` — The human's direction names the `graph-agent` prefix and excepts Lang by name. It says nothing
about the eight occurrences naming `~/.claude/`, `~/dotfiles/` and `~/.nix-profile/` on that machine. The manager
scoped those out on the ground that they report where a file was found on an external machine and have no
repo-relative form, and wrote that scoping into clauses 5 of the condition. The human has not been asked.

## Interview

### Attempt 1

*The attempt's routing key is held in the manager's session and does not survive it.*

**The worker's raise, pasted as it wrote it.** It had finished the sixteen files and verified them before
raising; the raise is about whether clause 1 reaches this node's own file.

> **ASK:** Should node 147's own file be left untouched — clause 1's demand read as reaching the sixteen files
> the enumerator named at `c3d50bf`, rather than the tree as it now stands?
>
> **RECOMMENDED:** Yes, leave it untouched, and amend clause 1 to except this node's own file. Three grounds.
> First, it is the only reading under which the condition is satisfiable at all: four of the six occurrences are
> load-bearing text of the condition itself and one is the human's verbatim words, and clause 3 forbids
> rewording while my contract forbids rewriting the condition. Second, clause 2's premise — "Every one of the 36
> carries a path after the prefix" — is true of the recorded 36 and false of the enumerator occurrence at line
> 54, which is direct evidence that the manager wrote clause 1 over the 36 and not over the node's own text.
> Third, the spawn's own orientation names "the sixteen files that the clause 1 enumerator names, and nothing
> else". The pointers in node 147's file are quotations of a string being repaired, not pointers anyone follows;
> nothing reads them as a location.
>
> **ALTERNATIVES:** Rewrite all six mechanically — leaves `git grep -c -F '' -- .` as the recorded enumerator
> and `becomes` as the worked example, destroying the condition's own record, and alters a `verbatim` human
> quote.
>
> Rewrite only the transformable ones and leave the rest — still returns non-empty, so it fails clause 1 anyway,
> and still alters the human's verbatim quote and the Question's ellipsis.
>
> Ship the sixteen with an `ASSUMPTION` flag and let it ride to the gate — the checker runs clause 1 as written,
> finds 6, and reports the condition unmet; node 110's rule that an enumerator mismatch never `FAIL`s the work
> does not cover this, because clause 1 states a demand and not only a count. That spends a checker round to
> arrive back here.

***The manager's note.*** **The defect is in the manager's own condition.** Clause 1 demands that a grep for a
string return nothing, in a tree that now contains a node file whose whole subject is that string — the condition
quotes what it is repairing, so it cannot be satisfied while it exists. The manager wrote clause 1 against a count
taken at `c3d50bf`, one commit before the node's own file existed. Amending it is not the manager's, so it is put
to the human.

**The human's answer**, `verbatim`:

> ok for resolved nodes

***The manager's note.*** **Recorded and put back rather than acted on.** The raise asked whether clause 1's demand
reaches this node's own file; the reply names a different population — the resolved nodes among the sixteen — and
does not settle which of the raise's four routes it takes. Under the convention that a terse reply whose option is
unclear is recorded and queried rather than interpreted, the manager asked which and did not resume the worker. The
worker remains stopped on its raise.

**The human's clarification**, `verbatim`, on being asked which option their reply took:

> What I meant is essentially recommended, but exclude all "resolved" "nodes" (see context.md) not just 147

***The manager's note.*** **An answer registered against the manager's question by an accidental keypress is not
recorded here and was not acted on**, the human having said so in the same breath: *"I accidentally answered
something apparently by pressing a numpad key just as you opened it?"*, and *"please re-ask your last question"*.
Nothing was written onto this node from it.

**What the clarification widens.** The worker's recommendation excepted this node's own file from clause 1. The human
takes it and widens the exception to every `resolved` node, pointing at `CONTEXT.md` for both words: a resolved node
carries its `## Answer` and is the record of what was true, so its paths are history rather than live pointers. Of the
sixteen files the enumerator named, **seven are resolved nodes carrying 14 of the 36 occurrences** — nodes 59, 64, 75,
103, 114, 116 and 139 — **eight are open nodes carrying 21**, and one is `recovered/46-scan-nodes-01-60.md` carrying
the last. The worker rewrote all sixteen before raising, so the widened exception means reverting part of finished
work rather than declining to do it.

**The human's answer**, `verbatim`, on the manager's re-asked question:

> all stay rewritten except 147

The option it takes was the third the manager offered, in the manager's words: *"All sixteen stay rewritten. Your
earlier 'update all referenced places' stands unnarrowed, and the exception covers only node 147's own file — the
worker's original recommendation. Nothing is reverted; the resolved nodes keep their new repo-relative paths."*

***The manager's note.*** **This is the worker's own recommendation, so it is not a divergence from it.** It does
supersede the human's own clarification one message earlier, which had widened the exception to every resolved node;
both stand above under the never-delete rule and the later one governs. Nothing is reverted, and the seven resolved
nodes and `recovered/46-scan-nodes-01-60.md` keep the rewrite the worker already made.

### The amendment to clause 1

**Decided by the human**, above. The manager records it rather than authoring it; the exception is quoted from the
worker that proposed it.

~~Clause 1's demand that the enumerator *"return nothing, whatever the count has become"*~~ is amended to except this
node's own file, `nodes/147-graph-records-name-absolute-paths-on-a-machine.md`. The demand is that the enumerator
return nothing **outside that file**. Within it the string stands wherever it appears — clause 1's own enumerator
command, clause 2's statement and worked example, the Question's ellipsis, and the human's `verbatim` direction —
because the condition quotes the string it repairs and cannot be satisfied while doing so.

**This amendment is part of the condition** and travels with it to the checker.

`147.2` `ASSUMPTION` — *The worker's own prose, pasted.* Clause 7 demands that every markdown link this node
rewrote resolve to an existing path. No rewritten occurrence was a markdown link — verified before editing — so the
clause is vacuously satisfied. But five of the rewritten paths do not resolve from the repository root:
`.worktrees/103-pick-report-settling-moment` and its `CONTEXT.md` in node 103,
`.worktrees/114-destination-entry/CONTEXT.md` in node 114, and `.worktrees/116-checker-enumerator-duty` in two forms
in node 116. I left all five as bare rewritten paths rather than repairing, deleting or annotating them, on the
judgement that they are historical records of gate payloads naming worktrees the landing policy removed once those
nodes landed; they did not resolve before this change either, and a record of where work once stood is not a pointer
anyone is meant to follow. Repairing them would have been a change of meaning, which clause 3 forbids. If the intent
is that every path in the record resolve, these five need a different treatment and this node did not give them one.

## Retrospective

*Filed by the manager from the worker's handover, this effort's seventh handover part. The worker's own text,
pasted.*

**What I had to hunt for.** Three things, none of which the spawn or the node file held. **(1) Whether the
repository is still named `graph-agent`.** Found in `git remote -v`, which returns
`git@github.com:Flecheck/graph-agent.git`. I looked first in `map.md` and `CONTEXT.md`, both of which use the name
`graph-agent` freely without saying whether it is still current — so they were evidence of the name's use, not of
its truth. This mattered: without the remote I would have surfaced a node to repair 25 correct references. **(2)
Whether any of the 36 sat inside a markdown link target.** Clause 7 demands that rewritten link targets resolve, but
nothing said whether any rewritten occurrence *was* a link, so I derived it with a regex before editing. Answering
clause 7 required a measurement the condition assumed had been taken. **(3) Where the shipped files license a path
in a condition.** Found by grepping `.claude/skills/` for the bullet text; five worker contracts and
`graph-conventions.md` carry it. I looked first at the manager's `SKILL.md` `## Acceptance conditions` section,
which defers with *"`graph-conventions.md` states that rule in full"* — a correct pointer that cost one read.

**What I read and did not use.** `decisions.md` in full, 95 lines. Exactly one line bore on the work — node 110's,
that a checker re-runs a condition's enumerator and reports a mismatch alongside the outcome without failing on it —
and I used it only to reason about whether the clause 1 conflict would survive to the gate. The other 94 lines were
about decisions a mechanical prefix removal cannot touch. From `map.md`: the landing policy, the worktree lifecycle,
the code-slot count, the concurrency and question-queue rules, the token-cost preference, the dogfood and
heterogeneous-worker paragraphs, the flag-settling rule, the retrospective rule. What I actually used was the bar
paragraph, the never-delete rule, and the four standing rules for writing. I never needed to open `CONTEXT.md`.

**What would have made this node easier.** **The node file could have reconciled its own enumerator with its own
existence.** The count was taken at `c3d50bf` and the node file written at `c474ad2`, and writing the node added six
occurrences of the very string being counted. Nothing reconciled the two, so the first thing I did after reading was
discover a conflict that stopped the node for a human round-trip. Any condition whose enumerator counts a string the
condition itself contains has this shape, and it is detectable at authoring time by re-running the enumerator after
the node file is written rather than before. **The spawn and the condition disagreed, and the spawn could not settle
it.** The orientation said *"the sixteen files that the clause 1 enumerator names, and nothing else"* — which was
the right answer — while clause 1 said *"return nothing, whatever the count has become."* Orientation is explicitly
*not permission*, so I could not use the correct answer sitting in front of me. Had the amendment been in the
condition, this node would have had no raise at all. **The contract's rule that a wrong condition is a raise and
never a flag has no gradation.** It is right in substance, and here it was also expensive: the defect was a boundary
case, I held a recommendation I believed and stated it, and the human agreed with it in four words. Nothing in the
contract distinguishes a condition wrong in what it demands from one wrong only in its edge, and I would not have
wanted to decide that boundary myself — but it is where the cost of this node went.

**What I read that was stale, wrong, or contradicted something else.** **Clause 2's premise is false as applied.**
*"Every one of the 36 carries a path after the prefix, so no occurrence needs a rewritten sentence in order to lose
it"* is true of the recorded 36 and false of the 42 the enumerator returned at claim time: clause 1's own enumerator
command carries no path after the prefix at all. **The filing note's count of open nodes is wrong.** It says six of
the sixteen are open implementation nodes; there are eight — nodes 60 and 61 are both `Type: implementation`,
`Status: open`, and both carried the prefix in their conditions. The spawn's manager notes repeated the six. Five
more live-condition occurrences than either believed. **`map.md` says the graph is six files and names them, but the
directory holds two more things.** `prototypes/` and `recovered/` appear in neither the map's file list nor its
`## Notes`. I had to edit a file in `recovered/` and no rule told me whether an archived record counts as inside the
graph. **Nothing in the record says the checkout moved.** The map's bar paragraph still reads *"`graph-agent` has no
build, no tests..."*, which is accurate about the repository, while the working directory is
`/home/ten/Projects/expedition` and the git author is a different person from the one every path in the record
named. That gap between the record and the machine is precisely the defect this node was minted to repair, and the
record contains no line noting it happened.

`147.3` `ASSUMPTION` — *The manager's own, about its own conduct.* A checker is given nothing from the effort's
record, so that it cannot be unblinded by what the record says. This node's **work is the record**: its diff is
sixteen files under `.scratch/graph-workflow/`, and no checker can hold the work against the condition without
opening them. The manager spawned the checker with an instruction to read those files as the work under check and
to hold the work against the acceptance condition, the bar and the ground rules alone — deriving nothing from what
their content says about this effort or this node. That instruction is the manager's own judgement about a
collision the contracts do not address, made because the alternative was a node that cannot be checked at all. The
human has not been asked. It will recur on every node whose subject is the graph's own files, node 140 next.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted. It was spawned by the manager, not by the worker, and was given the acceptance
condition as extracted text together with the amendment.*

**Standards found and used.** Per the spawn I went looking for no reviewing skill and invoked none, so no part of a
reviewing skill ran in a spawned agent; I held the work against the named standards by hand. Used:
`/coding-principles`, `/naming`, `CONTEXT.md`'s forty `_Avoid_` lines, `.claude/skills/expedition/graph-conventions.md`
(incl. its `## Mechanical checks`), and `mattpocock-skills:writing-for-agents` (loaded into my own context, no agent
spawned). None of these standards is among the paths that changed — the diff is confined to `.scratch/graph-workflow/`
— so no standard moved under the check and the `Where the work moved one of them` route did not apply.

**Preamble.** The set of files in `git diff --name-only` is byte-identically the set the clause 1 enumerator named at
`c3d50bf` (compared with `diff` over both sorted lists). `git status --porcelain -uall` lists those sixteen and nothing
else, tracked or untracked, so `decisions.md`, `flags.md` and `nodes/147-graph-records-name-absolute-paths-on-a-machine.md`
are all untouched.

**Clause 1, as amended.** Re-ran `git grep -c -F '/home/mathieu/projects/graph-agent' -- .` in the worktree. It returns
one line: `.scratch/graph-workflow/nodes/147-graph-records-name-absolute-paths-on-a-machine.md:6`. Nothing outside that
file, which is what the amendment demands. I also ran the command against `c3d50bf` and it returned 36 across 16 files,
matching the recorded return exactly.

**Clauses 2 and 3, established together by a byte-level test.** For each of the sixteen files,
`git show HEAD:<f> | sed 's|/home/mathieu/projects/graph-agent/||g'` is byte-identical to the working-tree file
(`diff -q`, all sixteen identical). That single result establishes both clauses at once and without relying on lines as
units: every occurrence lost exactly the prefix and kept everything after it (clause 2), and no other byte moved
anywhere in any file — no reword, no deletion, no unstrike, no renumbering (clause 3). I separately confirmed clause 2's
premise held over the recorded 36: the only occurrence at HEAD lacking a trailing slash is inside node 147's own file,
which the amendment excepts. I read the ellipsis-continuation sites (`nodes/61` line 31, `nodes/142` lines 44-46,
`nodes/60` line 52) to confirm the `.../` forms still resolve against their now-relative sibling; they do.

**Clause 4.** Recorded return verified true: at `c3d50bf` the command returns 4 across 4 files. The four recorded files
each still return 1 and none is in the diff. The current return also carries a fifth hit; handed back below, and never
on its own a `FAIL`.

**Clause 5.** Recorded return verified true at `c3d50bf`: 8 occurrences across 6 files. Current return is identical —
same six files, same per-file counts, summing 8. One of the six (`nodes/103-…`) is in the diff, and the byte-level test
above proves its two lines are unchanged.

**Clause 6.** `git status --porcelain -uall` lists only the sixteen, all under `.scratch/graph-workflow/`.

**Clause 7.** Vacuously satisfied: this node rewrote no markdown link target. Checked on unwrapped text
(`git show HEAD:<f> | tr '\n' ' '`, matching `](…)`), no link target in any of the sixteen files contained the prefix at
HEAD, so none could have been rewritten. Separately, every repo-root path the rewrite produced that names a live
location exists (`.claude/`, `.claude/skills/`, `.claude/skills/expedition-checker/`, `…/expedition-checker/SKILL.md`,
`…/expedition/graph-conventions.md`, `…/expedition-implementation/SKILL.md`, `…/expedition-research/SKILL.md`,
`CONTEXT.md`, `.scratch/`, `.scratch/graph-workflow/`, `…/map.md`, `…/nodes/`).

**Clause 8 — the bar.** Its command half is genuinely empty and I confirmed rather than assumed it: the repository root
holds only `.claude/`, `CONTEXT.md`, `.scratch/`, `.gitignore`, and a `find` for `package.json`, `Makefile`, `justfile`,
`Cargo.toml`, `pyproject.toml`, `*.nix`, `.pre-commit-config.yaml` returned nothing. Nothing to invoke, so nothing was
run. Non-command half:

- `/coding-principles`, `/naming` — no code and no identifier was introduced; the byte-level test proves no text was
  added anywhere.
- `CONTEXT.md`'s `_Avoid_` lines — nothing added, so no avoided term entered. The change removes occurrences of
  `graph-agent`, which line 17 avoids.
- `graph-conventions.md` — none of its ten mechanical checks is reached: no edge, label, id, status, `## Answer`, flag
  entry or `## Review` item moved.
- `/writing-for-agents` — no prose was reworded, so its levers have nothing to bite on. The change removes a
  machine-specific restatement in favour of paths the environment resolves, which is the direction that standard's
  `cache` and `single source of truth` points.
- Ground rules 1-5 and the four standing rules — nothing added. On `an in-place update never deletes`: the prefix's
  removal is what the condition dictates and what the human directed, which is that constraint's own stated exception
  (information leaves when it is clearly wrong or the human asks for it gone).

Not a finding, reported so you know I saw it: `nodes/61-collapse-onto-scribe.md` cites `graph-conventions.md` by line
number on one of the changed lines, against standing rule 4. It is present at HEAD, the work did not introduce it, and
clause 3 forbade the worker to touch it.

**FINDING, handed back alongside the `PASS` — clause 4's enumerator no longer returns the four it records.**

- **Instances.** Re-running `git grep -c -F '/home/mathieu/projects/Lang' -- .` returns 5 occurrences across 5 files,
  not the recorded 4 across 4. The four recorded files each return 1 and are byte-unchanged. The fifth is
  `.scratch/graph-workflow/nodes/147-graph-records-name-absolute-paths-on-a-machine.md` line 70, which is clause 4's own
  enumerator command quoted inside the condition. That file is tracked at HEAD (`c474ad2`), did not exist at `c3d50bf`,
  and is untouched by the work — `git status --porcelain` reports nothing for it. So the work did not cause this and,
  being outside the sixteen files it may edit, could not have repaired it. This is the same self-quotation the amendment
  excepted for clause 1, and clause 4 carries no such exception.
- **The form, as a predicate.** A file tracked in the working tree that contains the literal
  `/home/mathieu/projects/Lang`, is not one of the four the condition records, and is not one of the sixteen files the
  worker may edit.
- **The extent — an enumerator.** Over the part of the work the implementer may edit:
  `git grep -c -F '/home/mathieu/projects/Lang' -- $(git diff --name-only)` returns nothing (exit 1). Over the tree, the
  instances of the form are listed by `git grep -l -F '/home/mathieu/projects/Lang' -- . | grep -vxF -e
  .scratch/graph-workflow/decisions.md -e .scratch/graph-workflow/map-history.md -e
  .scratch/graph-workflow/map-manager-only.md -e .scratch/graph-workflow/nodes/09-dogfood-target.md`, which returns
  exactly the one file above. Both enumerators are bounded by the tracked working tree I hold; I can establish this is
  the only such file there, not that it is the only one in the effort.

***The manager's note.*** **The run covered the whole condition and named no part it could not reach**, so this entry
carries no `NOT COVERED:` label. The finding above is an enumerator return reported alongside the outcome under [node
110](110-does-the-checker-rerun-the-enumerator.md)'s rule, which is never on its own a `FAIL`; it travels into the gate
payload. **The gate is not raised yet**: a grilling question was live in front of the human when this run returned, and
nothing displaces a live question.
