# Whether the effort's index of flags, `flags.md`, is dropped

Type: grilling
Status: resolved

## Question

*Written by the manager.* This decides whether every effort keeps a separate index of its flags. The human said, `verbatim`: *"I think we might want to just remove the flags.md file, I don't feel like it is useful ?"* Today `flags.md` is one of an effort's seven files: one line per flag with its state, which the shipped files make the source for the effort closing report's outstanding flags and for the sweep, and which wins where it and a node's `## Flags` entry disagree. Should `flags.md` be removed, and if so, what takes over each job it does today?

## Answer

`flags.md` is dropped from every effort. The `## Flags` section of each node is the only record of that node's flags. The human decided this over three payloads, and their replies, `verbatim`, were "ok, for the flags in the closing report, I feel like it is a bit late anyway", "ok, its a good idea a FRICTION can start a discution about possible refactor or similar", and "ok". Each job the index did today is handed over as follows.

- **The flag's text.** A flag is one entry on its node. The entry starts with its id `NN.k` and its marker. Its first sentence is the raising agent's one-sentence report of the judgement, written for a reader who has not read the node. The full account of what produced the flag follows that sentence. The manager adds only the id and the state.
- **State.** A flag is outstanding until its entry carries the marker `**· settled**`. The rules under `### How a check reads the files` say where that marker counts. No checkbox exists anywhere.
- **Finding the outstanding flags.** Search the node files for `## Flags` entries that are not marked settled. Triage, the session closing report of `expedition-stop`, and the effort closing report all use this search.
- **Effort closing report.** It no longer lists every outstanding flag, because by then that list comes too late to be useful. It lists only each outstanding `FRICTION` flag on an effort whose product is not the expedition skill files, with its id and first sentence. Such a flag records a defect that can only be fixed in another repository, and it can start a discussion of a refactor there.
- **Region cleanup.** It follows the same rule. Each outstanding `FRICTION` flag of that kind held by a node in the set is listed, with its id and first sentence, in the set put to the human for confirmation. The removal proceeds on that confirmation. No other outstanding flag stops the removal. The ids of all outstanding flags removed with their nodes are listed in the cleanup's report to the human.
- **The checker.** It receives, for each flag of the node under check, the first sentence of the flag's entry with its id.
- **Gone.** The rule that `flags.md` wins a disagreement, the agreement check (check 6), and the flag cleanup operation of `expedition-cleanup` are all removed.
- **Check 6.** It is replaced in place by a check that every `## Flags` entry begins at the start of a line with an id `NN.k`, whose `NN` is its node's number, and that no two entries on one node share an id. The outstanding-flags search finds an entry only by its id. The other checks keep their numbers, because checks 7 to 12 are cited by number.
- **An old entry with no id.** It is given the next unused id on its node when it is settled.
- **The heading.** `## The seven files` in `graph-conventions.md` is renamed `## The graph's files`. Every citation of it is updated in the same change.
- **This effort's own `flags.md`.** Once the change lands, the manager confirms one last time that every line in it agrees with its node's entry, then deletes the file. This effort's record directory is not tracked by git, so that deletion cannot be recovered from version control. The closed `graph-workflow` record is left as it is.

**MISSING FROM MAP, as the worker wrote it:** This effort's record directory, `.scratch/rename-split-upgrade/`, is not tracked by git (the `git status` in the spawn context shows it as `??`). So deleting this effort's `flags.md` cannot be recovered from version control. I learned this from that git status, and I wrote it into the answer for the manager to weigh.

## Flags

`15.1` `ASSUMPTION` **· settled** — Check 6 is replaced in place rather than removed. The human accepted removing the agreement check. Deleting check 6 outright would renumber checks 7 to 12, and the shipped files cite those by number: "check 7", "check 8", "check 9", "checks 4, 10, 11 and 12", "checks 1, 3, 4 and 12" and "check 10". The search for outstanding flags also finds an entry only by its line-anchored id, so an entry with no id would be missed without anything reporting it. So I proposed, as the new check 6, an id check on `## Flags` entries. The human was not asked about this replacement.

`15.2` `ASSUMPTION` **· settled** — I chose `## The graph's files` as the new name for `## The seven files`, because the opening paragraph of `graph-conventions.md` already says "the graph's files". The human was not asked.

`15.3` `ASSUMPTION` **· settled** — I read the human's first reply, "ok, for the flags in the closing report, I feel like it is a bit late anyway", as assent to the whole recommended package. I read its second half as raising a separate question about the effort closing report, and I put that question to the human in the next payload. I read their question about cleanup, "The FRICTION flags for nodes that are removed are given ?", as asking whether such flags are shown to the human. I put it as a question, and the human answered "ok" to showing them in the confirmation without letting them stop the removal.

## Interview

### Attempt 1 — agent `a2c3370897b5e4626`

**Relayed question, payload 1, as the worker wrote it:**

NODE:          Whether the effort's index of flags, `flags.md`, is dropped
ABOUT:         Decides whether every effort keeps `flags.md`, a separate one-line-per-flag index of its flags, or whether each node's own `## Flags` section becomes the only record of its flags. It is being decided now because the human said they do not find the file useful, and nodes 12 to 14 are editing the files that rely on it.
SO FAR:        I read the node, the map, the grilling contract, and every passage in the shipped files that mentions `flags.md`. I did not open any effort's `flags.md`, because the contract tells me to leave it unread. Today `flags.md` does seven jobs:
               (a) It is the source of "every outstanding flag" in the effort closing report (SKILL.md `## Closing an effort`).
               (b) Where it and a node's `## Flags` entry disagree, it wins (graph-conventions `## The seven files`).
               (c) Check 6 of the sweep checks that it and the nodes agree on which flags exist and which are settled.
               (d) It holds the one-sentence report that the checker is handed for each of a node's flags (SKILL.md, on the checker's spawn).
               (e) Raising, settling and amending a flag each write to it, so every flag is written twice (`### Raise a flag`, `### Settle a flag`, `### Amend an acceptance condition`).
               (f) `expedition-cleanup` has a whole operation, flag cleanup, that only removes settled lines from it.
               (g) Triage, and the stop skill's "every unsettled flag", read their outstanding flags from it. Triage also falls back to it for an old flag entry that has no id.
               Each node's `## Flags` entry already holds the flag's id, its kind, its full account and its settled state, written as `**· settled**`. `### How a check reads the files` already makes "is this entry settled?" decidable from the node file alone. So a search over `nodes/` for entries that lack that marker gives the outstanding flags without the index.
               What the index adds is one file to read instead of searching every node, plus a one-sentence version of each flag. For scale only, not authoritative, counted on 2026-10-12: the closed `graph-workflow` effort's `flags.md` has 869 lines. Across this effort's 15 nodes, 10 node files have a `## Flags` section.
               The human's plan for deliverables is one effort that runs indefinitely, cleaned up as pieces merge. In that kind of effort the index keeps growing, and flag cleanup exists only to trim it.
               The change would touch graph-conventions (`## The seven files`, which is cited about 8 times across `.claude/skills/`, `### Raise a flag`, `### Settle a flag`, `### Amend an acceptance condition`, check 6, `### How a check reads the files`). It would also touch SKILL.md (`## Flags`, the checker's spawn, `## Closing an effort`), the flag-raising sections and "Leave `flags.md` unread" in all four worker contracts, `expedition-cleanup`, `expedition-triage`, `expedition-stop` and `adoption.md`. `.claude/rules/expedition-triggers.md` and the glossary do not mention `flags.md`. Open nodes 12 to 14 do not mention `flags.md` or `## The seven files` in their conditions or questions.

ASK:           Should `flags.md` be dropped, so that each node's `## Flags` section is the only record of its flags?
RECOMMENDED:   Yes, drop it, and hand each job over as follows:
               (a) The effort closing report, triage and stop find outstanding flags by searching `nodes/` for `## Flags` entries that have no `**· settled**` marker.
               (b) and (c) Both go: once the flags are recorded in one place, there is nothing to disagree with and nothing to check.
               (d) The worker's one-sentence report becomes the first sentence of the flag's entry on its node, written for a reader who has not read the node. The full account follows it. The checker and the closing report take that first sentence.
               (e) Raising, settling and amending a flag each write only to the node file.
               (f) Flag cleanup is removed, and `expedition-cleanup` keeps only region cleanup.
               (g) An old entry with no id is given one when it is settled.
               `## The seven files` gets a new name that does not count the files, and every place that cites it is updated in the same change.
               The manager deletes this effort's own `flags.md` once the change lands, after one last check-6 comparison. The closed `graph-workflow` record is left as it is.
               This rests on three points. Every flag is written twice today, which is what makes check 6 and the "index wins" rule necessary. The node already holds everything except the one-sentence report. And an effort that runs indefinitely would otherwise need flag cleanup again and again. The cost is that finding outstanding flags means searching the node files instead of reading one file. That is the same kind of search workers already do over the record.
ALTERNATIVES:  - Keep `flags.md` as it is. Nothing to rewrite, but flags stay written twice, with check 6 and flag cleanup to maintain.
               - Keep `flags.md` for outstanding flags only, removing each line when its flag settles. The file stays short, but every flag is still written twice and the agreement check is still needed.
               - Drop it, and also drop the one-sentence report. The checker and the closing report then take each flag's full account, so their inputs get longer and have no fixed size.

**The human's answer to payload 1, `verbatim`:**

> ok, for the flags in the closing report, I feel like it is a bit late anyway

The reply takes the worker's `RECOMMENDED`: *"Yes, drop it, and hand each job over as follows"*, and adds a remark on job (a), the outstanding flags in the effort closing report: that it comes "a bit late anyway".

**Relayed question, payload 2, as the worker wrote it:**

NODE:          Whether the effort's index of flags, `flags.md`, is dropped
ABOUT:         Decides whether every effort keeps `flags.md`, and what takes over each job it does. The human's last reply settled the drop and added a remark about the effort closing report. This payload asks what that remark changes.
SO FAR:        Settled by the human's reply, verbatim: "ok, for the flags in the closing report, I feel like it is a bit late anyway". I read the "ok" as assent to the whole recommended package:
               - `flags.md` is dropped. Each node's `## Flags` section becomes the only record of its flags.
               - Outstanding flags are found by searching `nodes/` for entries that have no `**· settled**` marker.
               - The flag's one-sentence report becomes the first sentence of its entry, and the checker takes that sentence.
               - Raising, settling and amending a flag each write only to the node file.
               - Check 6, the "index wins" rule and flag cleanup are removed.
               - An old entry with no id is given one when it is settled.
               - `## The seven files` gets a name that does not count the files, and every citation of it is updated in the same change.
               - This effort's `flags.md` is deleted once the change lands.
               The second half of the reply bears on one job: today the effort closing report must carry "every outstanding flag" (SKILL.md `## Closing an effort`). I read the remark as saying that this comes too late to be useful. It does not say whether that list should go.
               What else depends on that list: flags normally settle at the node's gate or at its node closing report, so the flags still outstanding at effort close are mostly flags the human never answered. There is one exception. A `FRICTION` flag on an effort whose product is not the expedition skill files can never be settled as fixed in that effort. `### Settle a flag` in graph-conventions says "The effort closing report of that effort carries it again". That report is the last point at which such a flag is surfaced before the effort ends.
               Other places still list outstanding flags earlier, through the search above: the session closing report in `expedition-stop` and `expedition-triage`'s batch.
ASK:           Should the effort closing report stop listing outstanding flags?
RECOMMENDED:   Yes. Remove the outstanding flags from the effort closing report, with one exception: it still lists any outstanding `FRICTION` flag on an effort whose product is not the expedition skill files. This rests on two points. Every other outstanding flag has already reached the human, through its node's gate or node closing report, the session closing report, or triage. Such a `FRICTION` flag, however, records a defect that can only be fixed in another repository. The effort closing report is the last point at which it is carried out of that effort.
ALTERNATIVES:  - Remove every outstanding flag from the effort closing report, `FRICTION` flags included. This is simplest, but a defect in the skill files found on another repository is then reported only on its node.
               - Keep the list of every outstanding flag in the effort closing report, built by the search. Nothing changes except where the list comes from.

**The human's answer to payload 2, `verbatim`:**

> ok, its a good idea a FRICTION can start a discution about possible refactor or similar

The reply takes the worker's `RECOMMENDED`: *"Yes. Remove the outstanding flags from the effort closing report, with one exception: it still lists any outstanding `FRICTION` flag on an effort whose product is not the expedition skill files."*

**The human's words, `verbatim`, sent while the worker held the node after payload 2:**

> I guess that in the cleanup it should be the same ? The FRICTION flags for nodes that are removed are given ?

*Manager's note:* passed to the worker as a further question of the human's on this node.

**Relayed question, payload 3, as the worker wrote it:**

NODE:          Whether the effort's index of flags, `flags.md`, is dropped
ABOUT:         Decides whether every effort keeps `flags.md`, and what takes over each job it does. The human asked whether region cleanup should handle flags the same way as the effort closing report. That question remains before the handover.
SO FAR:        Settled so far:
               - `flags.md` is dropped. Each node's `## Flags` entry is the only record of its flag, and its first sentence is the one-sentence report the checker is handed.
               - Outstanding flags are found by searching the node files for entries without `**· settled**`.
               - Check 6, the "index wins" rule and flag cleanup go.
               - The effort closing report no longer lists outstanding flags. The one exception is any outstanding `FRICTION` flag on an effort whose product is not the expedition skill files. The human said: "ok, its a good idea a FRICTION can start a discution about possible refactor or similar".
               The human then asked, verbatim: "I guess that in the cleanup it should be the same ? The FRICTION flags for nodes that are removed are given ?"
               What `expedition-cleanup` says today, under `## Region cleanup`, step 3: "A node in the set that holds an outstanding flag also stops the removal. Put that flag to the human first, because removing its line would drop it from the effort closing report." Once the closing report carries only those `FRICTION` flags, that reason no longer holds for any other flag.
               In practice, few other flags are still outstanding by cleanup time. A node's flags settle at its gate, or on whatever the human says after its node closing report. So an outstanding flag on a resolved node is almost always one of those `FRICTION` flags, which stay outstanding until the human declines them or checks them by hand.
               With `flags.md` gone, removing a node also removes the only record of its flags. The text then survives only in version control.
               I have already searched the shipped files for the full set of places the change touches. The handover will carry it.
ASK:           Should region cleanup follow the same rule as the effort closing report, so that only outstanding `FRICTION` flags on an effort whose product is not the expedition skill files are shown to the human before their nodes are removed?
RECOMMENDED:   Yes. In the set put to the human for confirmation, list each such outstanding `FRICTION` flag held by a node in the set, with its id and the first sentence of its entry. The removal then goes ahead on the human's confirmation, as for the rest of the set. Any other outstanding flag no longer stops the removal. Its id is listed in the cleanup's report to the human, so no flag disappears without the human being told. This rests on two points. It matches the closing-report rule the human just accepted. And by cleanup time, an outstanding flag that is not one of those `FRICTION` flags is one the human has already been shown at its node's gate or node closing report.
ALTERNATIVES:  - Keep today's rule: every outstanding flag stops the removal and is put to the human first. Only the stated reason changes, to "the node holds the flag's only record".
               - The same as recommended, but such a `FRICTION` flag stops the removal until the human declines it or checks it by hand, instead of only being shown in the confirmation.
               - The same as recommended, but other outstanding flags are removed without their ids being listed in the report.

**The human's answer to payload 3, `verbatim`:**

> ok

The reply takes the worker's `RECOMMENDED`: *"Yes. In the set put to the human for confirmation, list each such outstanding `FRICTION` flag held by a node in the set, with its id and the first sentence of its entry."*
