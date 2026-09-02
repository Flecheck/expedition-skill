# Carry the pick-report settling moment into the shipped files and the map

Type: implementation
Status: claimed


## Question

*Surfaced by [A node's flags arrive after the human moment that was supposed to settle
them](99-flags-arrive-after-the-node-s-human-moment.md)'s worker, and pasted as it wrote it.*

> Make the shipped files and the effort's map state where a node's flags are settled, so that no file still names a
> moment at which the flags do not exist.

**Blockers, in the worker's words:** *"the grilling node above (it changes the same sentence in the same files, and
the sentence differs by whether it names grilling alone or every kind); and node 100, whose uncommitted work rewrites
one of the two sections in `SKILL.md` that this node edits."*

**The manager's note at filing:** [node 100](100-the-manager-starts-the-next-node-rather-than-proposing-it.md) has
passed its check and is at its gate; once it lands that blocker is discharged, so the header carries only
`Blocked by: 102`.

## Acceptance condition

*Written by node 99's worker. Pasted as it wrote it, and not the manager's.*

> Done when every file below states the rule below, and no file in the repository still says that a grilling node's
> flags are settled at that node's last answer.
>
> **The rule to state.** A node's flags are settled at the **pick report** — the message the manager sends when that
> node closes and it starts the next work — and not at the node's last answer. The pick report awaits no answer and
> takes no place in the human's queue; the settlement rides whatever the human says next, whatever that next thing is
> about, rather than waiting for it. Where the human never speaks again, nothing settles: the flags stay outstanding
> and reach the effort's closing report by the existing route for a flag whose moment never came. The manager never
> settles a flag on its own judgement or on the passage of time.
>
> **The duty that comes with it.** A pick report closing a node that holds flags carries every one of those flags, in
> the fuller form used when a flag reaches the human at a gate — what was decided, why, and the context needed to
> answer it, so that answering never requires opening a file — because a payload that omits a flag settles that flag
> silently.
>
> **Where each must say it.**
>
> 1. `.claude/skills/expedition/SKILL.md`, under `## Flags`: the sentence beginning *"A node's flags are settled at
>    the human moment that ends that node"* names the pick report in place of *"a grilling node's last answer"*, and
>    keeps an implementation node's gate.
> 2. `.claude/skills/expedition/SKILL.md`, in whichever section states what the manager reports when it picks and
>    starts the next node: that report's stated contents include the closing node's flags in the fuller form, with the
>    silent-settlement reason given.
> 3. `.claude/skills/expedition/graph-conventions.md`, under `### Settle a flag`: the paragraph beginning *"The norm
>    is settling a node's flags at the human moment that ends it"* says the same, and its list of what the closing
>    report carries stays consistent with it.
> 4. `CONTEXT.md`, the `Flag` entry: the sentence *"It is settled at the human moment that ends its node"* names the
>    same moment as the three above.
> 5. `.scratch/graph-workflow/map.md`, the standing preference beginning *"Approving a node's end settles that node's
>    flags"*: restated to the rule above, keeping the human's own words quoted verbatim, under the map's own change
>    procedure — the superseded text moves verbatim into `map-history.md` before the map is changed.
>
> **One naming repair, in the same work.** `map.md` calls the per-node message *"a closing report"*, and `CONTEXT.md`
> gives that name to the once-per-effort report the manager hands over when the frontier empties. Every per-node use
> in `map.md` becomes *pick report*. No use of *closing report* for the once-per-effort report changes.
>
> The standing bar applies.

### Amendment by the manager, before the claim

***This section is the manager's own and is not node 99's worker's text.*** Performed under [How a condition's scope
is amended](82-amending-a-condition-whose-scope-was-too-narrow.md)'s permission, whose test is that an amendment may
**add places and no demands**. It adds one place and one missing rung; it changes no demand.

**Guard 1 — the search, re-derived by the manager before the claim rather than taken from the annotation below.**

```
grep -rln "closing report" .claude/ CONTEXT.md
```

returns exactly four files, with zero false positives:

- `.claude/skills/expedition/graph-conventions.md` — the condition's place 3;
- `.claude/skills/expedition/SKILL.md` — its places 1 and 2;
- `CONTEXT.md` — its place 4;
- **`.claude/skills/expedition-precondition/SKILL.md` — named nowhere in the condition.**

The unnamed site, quoted so the checker need not go and look: *"passes through no gate, so a flag here waits for the
closing report. Write it short and plain enough to be settled cold."*

**6. The sixth place, added.** `.claude/skills/expedition-precondition/SKILL.md`'s sentence *"passes through no gate,
so a flag here waits for the closing report"* states the rule above on a **different false ground** from the one the
five places carry — *no gate*, rather than *no human moment*. It is repaired to the same rule as the other five. The
sentence immediately following it, *"Write it short and plain enough to be settled cold"*, is **kept**: [node
102](102-do-afk-nodes-flags-settle-at-the-pick-report.md)'s answer states that instruction gets *more* binding rather
than less, the reader now being a human meeting that node for the first time in a pick report.

**Why this adds no demand.** The rule at that place is fixed by node 102's resolved answer, which names this exact
site, quotes this exact sentence, states that *"having no gate is now irrelevant to where a flag settles"*, and
states the rule that replaces it. So the replacement text is **copied across rather than composed here** — the same
ground node 81's amendment ran on. Nothing new is demanded of the worker; one more place is named where an
already-fixed demand applies.

**7. The missing rung, supplied.** The condition's *"no file in the repository still says…"* clause is a predicate
keyed to the **wording** of one sentence, which is exactly why the sixth site slipped it. The enumerator above is the
condition's rung 1 under [node 94](94-condition-scope-as-a-predicate.md), and its domain is the working tree rather
than the effort's record, as flag `94.2` requires. **A place this work finds outside the six named is reported and
not edited**; reporting it is the whole of what the condition asks for it.

**What the manager did not do.** It did not touch the rule, the duty, the naming repair, or any of the five original
places, and it did not rewrite node 99's worker's text anywhere above. **`map.md` remains place 5 and is not in the
enumerator's domain**, being the effort's own record rather than the tree.

**Recorded as flag `103.1`**, and named in the pick report that starts this node, as node 82's guard 2 requires.
**One thing it rests on that is not settled:** node 94's flag `94.4`, which reads this particular addition as inside
node 82's permission, is outstanding. The manager applied node 82's test itself and reached the same place, but the
reading is not the human's.

## Flags

`103.1` `ASSUMPTION` **settled** — ***The manager's own flag, not a worker's, and marked as the manager's.*** The acceptance
condition above was amended before the claim: one place added — `.claude/skills/expedition-precondition/SKILL.md` —
and one enumerator supplied, under node 82's permission to add places and no demands. The full record, including the
search re-derived at guard 1 and what the manager did not touch, is in `### Amendment by the manager, before the
claim` above.

## Annotation: this condition is malformed under node 94, and its enumerator returns a site it does not name

*Filed by the manager from [Whether a condition's scope stops being a list of
files](94-condition-scope-as-a-predicate.md)'s `INVALIDATIONS`, in that node's own words. **The condition above is
not amended by this annotation**; amending it is a separate act under [How a condition's scope is
amended](82-amending-a-condition-whose-scope-was-too-narrow.md)'s guard 2, and the manager has not performed it.*

> Its scope was plainly derived from a search — five sites named across the shipped tree — and it carries no
> enumerator, no bounding set, and no statement that no search was run. It is malformed under rung 3's own terms, and
> the malformation is not theoretical: the missing rung is exactly what let the sixth site through. The enumerator is
> `grep -rln "closing report"` over `.claude/` and `CONTEXT.md`, which returns four files with zero false positives,
> three of which the condition names, the fourth being `.claude/skills/expedition-precondition/SKILL.md`. Adding that
> place is a widening node 82 licenses on my reading at flag `94.4`; the sentence that must replace the site's
> *"passes through no gate, so a flag here waits for the closing report"* is node 102's answer's own, copied rather
> than composed.

`103.2` `ASSUMPTION` — **three sites repaired that the condition's six places do not name.** The condition's places
name particular sections; its second clause is a whole-repository predicate — *"no file in the repository still says
that a grilling node's flags are settled at that node's last answer."* Three sentences fall under the second and not
the first: `CONTEXT.md`'s `Raise` entry, which says *"a grilling node's last answer, an implementation node's gate"*
in exactly the forbidden words; and two in `expedition/SKILL.md` — its `raise` glossary entry and *"settling a flag,
which rides the human moment that already ends its node"* — which state the same moment generically and so, for a
grilling node, name the last answer. I repaired all three. The competing reading is the manager's amendment clause
*"a place this work finds outside the six named is reported and not edited"*, which I read as scoped to whole
**files** outside the enumerator's four (there were none) rather than to sentences inside a named file. Under that
reading `CONTEXT.md` would have shipped asserting the old rule two entries below the entry I had just repaired, and
the file would contradict itself. Nobody was asked.

`103.3` `ASSUMPTION` — **I edited the worktree's copies of `map.md` and `map-history.md`, which are stale.** The spawn
directed me to the worktree copies and my contract confines me to that tree, so that is where I worked. But
`.scratch/` is tracked, the worktree sits on `47703bb`, and the **main checkout holds uncommitted manager edits to
both files**: `map.md` differs in four places (a `## Destination` paragraph, the one-question bullet, the never-idles
bullet, and a fog item) and `map-history.md` is 30 lines longer. The bullet I replaced is byte-identical in both, and
my `map-history.md` append lands at the end of a shorter file, so **the text transfers cleanly** — but the landing
policy's `git merge --ff-only` will refuse over a dirty tracked path, and re-saving the map from the manager's own
working copy would silently drop my edit. I judged reporting this cheaper than a raise, the spawn having already made
the placement decision and the manager holding the live file. Nobody was asked.

`103.4` `ASSUMPTION` — **I used *close* of a node about eight times.** `CONTEXT.md`'s `Resolve` entry carries
`_Avoid_: close`, and `Closed` reserves the word for an effort. I used it anyway — *"the first human moment its close
reaches"*, *"the pick report that closes it"*, *"a pick report closing a node that holds flags"* — because the
acceptance condition, node 99's answer and node 102's answer all phrase the rule that way, and because node 100 had
already shipped *"rather than at that node's close"* into the same section of the same file. The alternative was
*ends*, which is the wording the old false rule used and which would have obscured that the moment moved. Reported as
a collision, not resolved.

`103.5` `ASSUMPTION` — ***The manager's own flag, not a worker's, and marked as the manager's.*** **The map edits were
moved out of the worker's tree and applied to the live copies by the manager, and the worktree's `.scratch/` reverted,
so the node's commit will carry the four shipped files only.** This is the manager acting on flag `103.3` rather than
raising it, and the act is the manager's alone: the two files are the graph's own, the manager is their only writer,
and the landing policy already says the graph's files are not committed per node. **The worker's text was applied
verbatim** — the `map.md` bullet is its line unchanged, and the `map-history.md` block is its lines unchanged — which
is scribe work rather than authorship. What the manager accepted: **place 5 of the condition can no longer be
established in the tree the checker sees**, and the checker is blind to `.scratch/` in any case, so place 5 is a part
it cannot cover and the manager establishes it instead. Whether this is the right disposition in general is [Two
writers edit the map at once when an implementation node's work is a map
change](115-two-writers-edit-the-map-at-once.md), which the worker surfaced and which this act pre-empts for one node
only.
