# Point `map-manager-only.md` at the admission test that already binds it

Type: implementation
Status: claimed

Blocked by: 229

## Question

*Specified by [node 225](225-whether-map-manager-only-gets-an-admission-test.md)'s worker after the human chose a
pointer over a restatement, and pasted as that worker wrote it.*

> `map-manager-only.md`'s opening declares its reader and says nothing about what it admits, while its sibling
> `map-implementation-rules.md` opens with an admission test in its own words — so a reader comparing them reads the
> silence as *this file is under no test*. It is: [node 197](197-ship-what-a-file-of-the-map-admits.md)'s shipped
> statement in `graph-conventions.md`'s `## Writing the map` is stated over the reader each file of the map
> declares and names *"the manager alone"* explicitly. The human chose a pointer over a restatement, a full local
> restatement being the duplication node 196 created and node 200 was spent collapsing.

**Blocker, in the worker's words:** *"the sweep node above. Both nodes write `map-manager-only.md`, and the sweep's
condition turns on byte-identity outside its own fourteen edits, so the two are sequenced rather than parallelised
— this map's own rule for two workers over one file."*

## Acceptance condition

*Written by node 225's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map-manager-only.md` and no other file may be edited. The worker may not mark
> this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> Done means all of the following are true of the finished tree.
>
> 1. The file's opening gains **exactly one new paragraph**, placed directly below the paragraph beginning `**The
>    manager is this file's reader** ` and above the paragraph beginning `**Nothing below was reworded on the way
>    here**`. That position is required: the second paragraph claims a property of everything after it, which a
>    paragraph inserted below it would falsify.
> 2. The new paragraph says, in its own words: that what this file admits is stated in `graph-conventions.md`'s
>    `## Writing the map` section, over the reader each file of the map declares; that this file's declared reader
>    is the manager; and that the test is **not** restated here. It cites this node by markdown link in the form the
>    file's other items use.
> 3. **It states none of the test's content.** It does not say what a line must do to earn its place, does not name
>    what is inadmissible, does not distinguish a trigger from a history, and does not state who applies the test or
>    that no sweep is owed. A paragraph containing any of those is a restatement and fails this clause.
> 4. The new paragraph is **at most 400 bytes**, including its trailing newline.
> 5. The change is a **pure insertion**: deleting the new paragraph and its blank separator line from the finished
>    file reproduces the pre-work file byte for byte. Report the md5 of both to show it.
> 6. The count of `~~` occurrences in the file is unchanged, and no existing sentence is reworded, moved or removed.
> 7. Every markdown link in the file resolves to a path that exists, except a link to a path outside this
>    repository, which is out of scope.
> 8. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**The blocking edge is the worker's own and the manager has written it as stated.** Both nodes write
`map-manager-only.md`, and node 229's condition demands byte-identity outside its fourteen spans, so a parallel run
would make node 229 unsatisfiable through no fault of its worker.

**Clause 6 will read differently after node 229 lands, and that is deliberate rather than a defect.** It says the
count of `~~` occurrences is unchanged; node 229's clause (a) drives that count to **zero** in the landing section.
So this clause binds whatever the count is when this node starts, which is what *unchanged* means, and the two
conditions do not disagree.

## Amendment, 2026-09-27 (from node 347)

*Written by [node 347](347-rename-sweep-of-a-file-to-a-word-the-glossary-does-not-own.md)'s worker under its `CONDITIONS`, and filed by the manager after that node landed as commit `4b538be`, whose `graph-conventions.md` text ("No pass over a whole file is owed under the test, and one is allowed.") fixes every word of it.*

- **Clause 3's last sentence pair.** Where it reads "...does not state who applies the test or that no sweep is owed. A paragraph containing any of those is a restatement and fails this clause.", read "...does not state who applies the test, that no pass over a whole file is owed, or that one is allowed. A paragraph containing any of those is a restatement and fails this clause."

## Flags

`230.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above.* Node 347's replacement for clause 3's last sentence pair was filed on this open, unclaimed node without asking the human first.
