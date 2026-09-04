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
