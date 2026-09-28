# Whether node 165's remaining shadow pairs still run

Type: grilling
Status: claimed
Blocked by: none

## Question

Node 165's parts (ii)-(iv) made three shadow pairs a standing duty on the manager. Pair 1 (node 179) returned null with a finding outside the readout's two questions (the fed arm was handed a stale premise). Pair 2 (node 176) was spawned with a scoped pointer instead of the flat file, and its readout is filed nowhere in the record. Pair 3 has not run. Node 181 has decided that the instrument is not shipped. Should the manager file pair 2's readout (if the arms' outputs still exist) and run pair 3, or should the duty be retired? Given that spawns now point at named entries of `decisions.md` and not the whole file, what would a pair measure?

*Reported by [node 181](181-whether-the-workflow-ships-the-shadow-spawn-instrument.md)'s worker under its `NEW NODES`, and filed by the manager. Its words on related nodes: "Related: node 185 (open, scoping the decisions pointer), whose practice is already in use, and node 182, which waits on the same pairs."*

## Interview

#### Question 1, relayed 2026-09-28

*Pasted as the worker handed it back.*

```
NODE:          Whether node 165's remaining shadow pairs still run

ABOUT:         Node 165 made three "shadow pairs" a standing duty on the manager. A shadow pair runs one grilling node twice, once with the `decisions.md` pointer in the spawn (the fed arm) and once without it (the unfed arm). Both arms stop at their first question, and a read-only agent compares them. You decided at node 181 not to ship this instrument ("yes, don't ship it"). This node decides whether the duty that is left over still runs. Node 182 waits on the same pairs.

SO FAR:        **Where the three pairs stand.**
               - Pair 1 (node 179) was read out and came back null on both readout questions. Under node 165's own rules, a null licenses nothing. The readout also found something neither question asked: the fed arm had been handed a stale premise from `decisions.md`.
               - Pair 2 (node 176) was spawned, and its readout was never run or filed. **Both arms' first questions still exist.** They are in this machine's session transcripts for the earlier manager session, not in the record. The fed arm is subagent `agent-a6ed2b26586ca6d17` and the unfed arm is `agent-ad2ef0a8c6df218a6`, both in session `0e2d7caf…`. A readout could therefore still be run.
               - Pair 3 was never spawned.

               **What a pair would measure now.** The protocol was built to test whether `decisions.md` should stay fed whole to every worker. Spawns no longer feed it whole: from pair 2 onwards the manager has named the few entries that bear on each node, which is node 185's practice (node 185 itself is still open). So a pair now compares "a handful of named entries" against "nothing". Nobody proposes dropping the pointer altogether. Node 185's open options are all ways to scope it (headings in the index, a list of node numbers in each spawn, or a label vocabulary). The result would therefore decide nothing that is live. That is the same ground node 165 used to close its own first candidate.

               **What a pair's result was meant to feed has already been overtaken.** Under node 165's part (iv), a divergence would have retired node 129's size trigger, and a null would have been used only as evidence beside that trigger when it fired. The trigger was "re-offer taking `decisions.md` off the read-whole list when it nears ~43,847 bytes". `decisions.md` is now 79,139 bytes, so the trigger fired some time ago and was never re-offered. Scoped pointers already do what the re-offer would have proposed. I am not deciding that trigger here. I will report it for the manager.

               **The cheaper measure is already in use.** Every worker's retrospective asks "what arrived that this node did not need". Node 345 acted on those answers and cut `map.md` from 42 KB to 22 KB without running a shadow.

               **Settled on my own authority:** I read "the duty" as node 165's parts (ii)-(iv) as a whole: running the pairs, running the fixed readout, and applying the outcomes fixed in advance.

ASK:           Should the manager's duty to run node 165's shadow pairs be retired now, leaving pair 2 unread and pair 3 unrun, or should the manager still file pair 2's readout from the transcripts and run pair 3?

RECOMMENDED:   Retire the duty now. Record on node 165 that pair 2 was left unread, name where its arms' outputs sit, and record that pair 3 was never run. Node 182 then no longer waits on the pairs.
               This rests on three points:
               - The comparison the pairs were designed for, flat feed against none, is no longer what spawns do.
               - The comparison they would make now, named entries against none, has no live decision behind it.
               - The result was meant to feed a size trigger that scoped pointers have already overtaken.
               A shadow stays available as this effort's optional practice, as node 181 left it, for any future live and reversible choice about a fed file. This fits your priority on token use and ground rule 4 (prefer the simple thing that can change later).

ALTERNATIVES:  - File pair 2's readout from the transcripts, which costs one cheap read-only agent, and then retire the duty without running pair 3. This gives two data points instead of one, but neither would decide anything, and pair 2 would carry the confound of a scoped pointer.
               - Run the protocol as written: file pair 2's readout and shadow the next grilling node as pair 3. This costs one extra worker, up to its first question, plus two readouts, and it measures a question nobody is asking.
               - Redesign the pairs to test node 185's options, for example named entries against the whole file. This is node 185's decision to make, and it can use a shadow as optional practice without this duty.
```
