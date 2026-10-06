# State the prose standard's demands in the rules file, instead of locating it by plugin name

Type: implementation
Status: out-of-scope

Blocked by: 144

## Question

*Surfaced by [Whether "not depend on mattpockock" reaches this effort's own never-shipped
bar](132-does-the-plugin-direction-reach-the-efforts-own-bar.md)'s worker, and pasted as it wrote it.*

> Ground rule 5 holds every prose deliverable on this effort against a standard it locates by a plugin name that has
> a measured record of ceasing to resolve. Replace the locator with the standard's own demands, held as text in the
> file the checker and implementer read, and correct the map line that claims the human's no-plugin direction reaches
> ground rule 5 and the consult-skills line.

**Blockers, in the worker's words:** *"144. Node 144's clause 1 moves the ground-rules block byte-identical and
forbids any rule being reworded, so this change cannot be folded into it; and node 144 is where ground rule 5 arrives
in the rules file, so running this first would write the vendored text into `map.md` only to move it again."*

## Acceptance condition

*Written by node 132's worker. Pasted as it wrote it, and not the manager's.*

> The work is `/home/ten/Projects/expedition/.scratch/graph-workflow/`. The worker may edit `map.md` and the sibling
> file holding the implementer's and checker's rules, and no other file; it may not mark this node, resolve it, or
> write a line in `decisions.md` or `flags.md`.
>
> **Which file is the rules file:** the one file directly in that directory that is not `map.md`, `map-history.md`,
> `map-manager-only.md`, `decisions.md` or `flags.md`, and that contains a block beginning with the line `**Ground
> rules for this effort.**`. If no such file exists, this node is not yet startable: the worker stops and says so,
> and changes nothing.
>
> Done means every one of the following is true of the finished tree.
>
> 1. The rules file contains a section, under a heading of its own, stating the demands that prose written on this
>    effort is held to. The section is self-contained: a reader with no access to any plugin, skill, or network can
>    apply every demand in it from that section's text alone, and it contains no instruction to read another document
>    in order to learn what is being demanded.
> 2. That section is at most 2,500 bytes. It states demands rather than reproducing a source document.
> 3. Each demand in that section carries, in one short phrase, where it came from: the skill
>    `mattpocock-skills:writing-for-agents` where that is its source, or this repository's own record where it is.
>    Where that skill did not resolve when the worker looked for it, the section says so in one sentence and states
>    which demands were recovered from this repository's record instead.
> 4. The numbered rule in the rules file which before this work reads `Prose deliverables are held against the
>    /writing-for-agents standard, which is specific to this repo, is never shipped, and is located by name in the
>    mattpocock-skills plugin rather than by path.` no longer stands as that file's live statement of the prose
>    standard. Its replacement names the section from clause 1 as the standard, keeps the rule's number and its
>    position in the numbered block, and locates the standard by no plugin name.
> 5. The replacement may name `mattpocock-skills:writing-for-agents` as one route to the same material. Where it
>    does, the same sentence states that the standard holds whether or not that name resolves. Nowhere in the rules
>    file is the prose standard's applicability made conditional on a skill being invocable or on a name resolving.
> 6. Wherever the rules file's list of standards that work is held against names `/writing-for-agents` or
>    `writing-for-agents`, that entry instead names the section from clause 1. No entry in that list locates a
>    standard by a plugin name.
> 7. The superseded text of the rule in clause 4 is left in the file, marked as superseded, rather than removed. No
>    other numbered rule in that block is reworded, renumbered or reordered.
> 8. In `map.md`, the bullet beginning `**The shipped files should not depend on the` no longer asserts that the
>    direction reaches the `Skills every session should consult` line or the ground rule about prose deliverables. In
>    its place it states that the direction binds what the workflow ships and binds neither of those two, and that
>    the prose standard is now stated in the rules file rather than located by plugin name. The superseded sentence
>    is marked as superseded and left in place rather than removed. If that bullet already says this when the worker
>    starts, this clause is already met and the worker changes nothing for it.
> 9. `map.md`'s line beginning `**Skills every session should consult:**` is byte-identical to what it was before
>    this work.
> 10. No file under `/home/ten/Projects/expedition/.claude/skills/` is modified, and no file outside
>     `/home/ten/Projects/expedition/.scratch/graph-workflow/` is modified.
> 11. Every markdown link in `map.md` and in the rules file resolves to a path that exists.
> 12. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**The condition names its paths absolutely**, three times — `/home/ten/Projects/expedition/…`. That is the defect
[node 147](147-graph-records-name-absolute-paths-on-a-machine.md) has just finished repairing across sixteen files
and that [node 148](148-nothing-stops-a-condition-being-written-with-an-absolute-path.md) exists to stop recurring,
and it recurred in the first condition written after node 147 landed. **The manager has not rewritten it** — a
condition is handed over as written — and files it with the flag below. Node 148 is unblocked and, landing first,
would give the rule this condition was written before.

**It corrects a `map.md` bullet the manager wrote.** Clause 8 carries out the correction rather than leaving it to
the manager, which is why no map change was made when node 132 resolved.

## Flags

`149.1` `ASSUMPTION` **· settled** — *The manager's own.* This node's acceptance condition names three absolute paths beginning
`/home/ten/Projects/expedition/`, which is the machine-specific form node 147 removed from every other live condition
and node 148 is minted to prevent. The manager filed the condition unaltered rather than repairing it, on the rule
that rewriting an acceptance condition is never the manager's. The consequence is that this node's worker and its
checker are handed a path that names this machine, and the node is startable only on a machine where that path
resolves. Sequencing node 148 before it would fix the class rather than this instance; the manager has not made that
an edge.

## Ruled out of scope, 2026-10-06

Dropped at the triage the human invoked on 2026-10-06: the plugin standard still resolves, and the map's six standing rules for writing already state the prose demands as text; its condition is stale three ways (a rules-file block that no longer exists, a rule that now lives in `map.md`, and `/home/ten/...` paths). A read-only agent checked the node against the current files.

*The human's answer to the triage proposal, `verbatim`, 2026-10-06:* *"ok"*. The manager's proposal ended "Please answer Q1 to Q4. \"ok for all\" approves each as proposed."

*The manager's note, 2026-10-06:* flag 149.1 settled in the triage flag batch the human approved.

