# Whether `decisions.md`'s size trigger is re-offered or retired, now that spawns scope the pointer

Type: grilling
Status: claimed
Blocked by: none

## Question

`map-manager-only.md`'s item "When `decisions.md` stops being small enough" tells the manager to re-offer part (ii) of node 129's package, which takes `decisions.md` off every worker's read-whole list, when the file nears ~43,847 bytes. That number is node 129's worker's, flagged at `129.4`, and not the human's. The file is now 79,139 bytes, and the offer was never made. Node 181's worker saw it at 76,348 bytes and found no sign of the offer. Since the shadow pairs began, spawns have named the entries that bear on each node instead of pointing at the whole file, which is the practice of node 185. Is the re-offer still owed? Or has scoping met the trigger, so that the line is retired, or folded into node 185's answer?

*Reported by [node 356](356-whether-node-165s-remaining-shadow-pairs-still-run.md)'s worker under its `NEW NODES`, and filed by the manager. Its words: "Related: node 185 (open), whose answer may settle it."*

## Interview

#### Question 1, relayed 2026-09-28

*Pasted as the worker handed it back.*

```
NODE:          Whether `decisions.md`'s size trigger is re-offered or retired, now that spawns scope the pointer (node 358)
ABOUT:         This node decides what happens to a manager duty that was never carried out. The duty says: once `decisions.md` grows too large, offer the human again the chance to take that file off the list of files every worker reads in full. The file is now far past the size meant to set that off, and node 356 has just retired the measurement that was supposed to inform the decision.
SO FAR:        What I read: my node file; `map.md`; the item in `map-manager-only.md` headed "When `decisions.md` stops being small enough"; the passages in node 129 about part (ii), the revert and flag `129.4`; node 185 in full; node 356's answer on this trigger; the shipped contracts' wording about `decisions.md`. I did not read `decisions.md` whole.
               Background. At node 129 I recommended part (ii): workers stop reading `decisions.md` in full and search it instead. You reverted that, verbatim: *"wait revert: leave decisions in read-whole - it's small enough"*, and *"whereas if it's fed to context, the LLM's engine will take it into account naturally - and it's small enough."* The file was 24,345 bytes then. Node 129's worker set a trigger: offer (ii) again when the file nears ~43,847 bytes, which is the size at which this effort decided `map.md` needed splitting. That number is the worker's own and was never put to you (flag `129.4`).
               Where things stand. `decisions.md` is 80,400 bytes today, about 1.8 times the trigger size. The trigger passed long ago and nothing noticed. The shipped worker contracts already tell a worker to read "the sections the spawn names". The manager's contract provides only one way to name sections: by label, and only where the effort declares labels. This effort declares none. Even so, this session every spawn has told its worker to read "only the lines about …". In practice, then, part (ii) is already in use in a form the manager chooses. Nothing in the record makes that practice a rule; turning it into one is open node 185 ("A spawn points at the decisions index without naming which sections bear on the node"). Node 185 is open, unclaimed and already raised 17 times, and its subject is exactly what part (ii) would decide. Node 356 retired the shadow pairs that were meant to inform this trigger, so no measurement is waiting on it. You have also made token-use work the priority.
               Settled on my own authority: node 358 is not the place to decide how the pointer is scoped (a label vocabulary, headings, or a list of node numbers per spawn). That is node 185's question.
ASK:           Should the size trigger be retired, with the offer it was guarding made through node 185 instead of on its own?
RECOMMENDED:   Yes. Retire the item "When `decisions.md` stops being small enough" from `map-manager-only.md`: replace it, and copy its current text verbatim into `map-history.md`. Then amend node 185's question, which is allowed because the node is open and unclaimed, so that it says three things: `decisions.md` is 80,400 bytes, past the effort's own ~43,847 anchor; the "small enough" reason for reading it in full therefore no longer holds; and node 185 is where part (ii) gets offered again, in its scoped form. Why: a scoped pointer answers the second half of your revert reason. The lines the manager names are still put in front of the worker, so the worker takes them into account on its own, and it never has to decide by itself to go searching. That was the weakness of (ii) as first worded. Keeping a separate size trigger would duplicate node 185, and a trigger that nothing watches has already been missed by 36 KB.
ALTERNATIVES:  B. Offer part (ii) again here, as first worded: workers search `decisions.md` on their own. Set aside because your reason for reverting it (search depends on the worker deciding to look) still holds against that wording.
               C. Keep the trigger with a size you choose. Set aside because the file is already past any plausible size, the old trigger was never watched, and once spawns scope the pointer the file's size stops setting what each worker pays.
               D. Retire the trigger and carry nothing into node 185. Set aside because node 185 would then decide without knowing that the ground for your revert has gone.
```
