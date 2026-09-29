# The dogfood link in `map-manager-only.md` names a path on another machine

Type: grilling
Status: resolved

Blocked by: none

## Answer

Discharged with no edit at node 366's triage: `/home/mathieu/projects/Lang` now exists on this machine, so the link resolves.

*The manager's note:* resolved rather than superseded because no node made it moot, under the human's answer to [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q1 (`verbatim`: *"ok"*). See flag 366.1.

## Question

*Surfaced by [Move the implementer's and checker's material out of the map](140-move-the-implementers-and-checkers-material-out-of-the-map.md)'s worker, and pasted as it wrote it.*

> `map-manager-only.md` links the dogfood target as `[Lang](/home/mathieu/projects/Lang)`. That path does not exist
> on this machine, where the repository itself lives at a different root; node 147 rewrote the graph's own absolute
> paths to be repo-root-relative and left this one, a path outside the repository, untouched. It makes any *"every
> markdown link resolves"* clause — node 140's clause 14, node 144's clause 6 — unsatisfiable for that file by any
> work confined to this repository. Only the human can say what the link should be: their machine's real path, a path
> made relative to nothing this repo knows, or plain text with no link at all.

## The manager's note at filing

*Not a change to anything above.*

**It was left deliberately and the human said so**, at [node
147](147-graph-records-name-absolute-paths-on-a-machine.md): *"the 'Lang' project references can stay for now"*, and
node 147's clause 4 demanded the four occurrences come back unchanged. **What nobody decided is the consequence** —
that two written acceptance conditions now carry a clause no work in this repository can satisfy. That is what this
node asks about, rather than reopening the human's *for now*.

**It is live rather than theoretical:** node 140's worker finished with its clause 14 unmet on exactly this link, and
node 144's clause 6 will hit it next.
