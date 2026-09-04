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
