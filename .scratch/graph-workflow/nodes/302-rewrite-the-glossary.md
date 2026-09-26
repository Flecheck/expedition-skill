# Rewrite the glossary in plain English

Type: implementation
Status: resolved
Blocked by: 291, 292, 293, 294, 295, 298, 300, 301

## Question

Rewrite `CONTEXT.md` in plain English and shorter, under the pass [node 289](289-a-plain-english-and-compaction-pass-over-the-shipped-files.md) settled.

> Beside the work, the handover carries three things. (1) For every open node whose `## Acceptance condition` quotes text or a heading from the before-text of what this node rewrites: either a replacement for each affected clause, quoting the after-text, or a proposal that the node be superseded as unnecessary, with the reason. Name the search you ran. (2) Every generalisation made, naming the statements it replaced. (3) Any rule judged dead or a default behaviour, reported as a new node and left in the text.

## Acceptance condition

*Authored by node 289's worker and filed by the manager. Node 289's worker's COMMON CLAUSES block, copied in full, then this node's own clauses, verbatim.*

**Terms.** *The before-text* of a file is that file as it stands at the commit this work's branch was created from, read with `git show $(git merge-base HEAD master):<path>` in the worktree. *The after-text* is the file in the worktree. *The rewritten range* is the part of the file this condition's own clauses name, or the whole file where they name no part.

1. **Nothing binding is lost.** Every binding statement in the before-text has a counterpart somewhere in the whole after-text that gives the same outcome in every case. The binding statements are: every rule, meaning every instruction, permission, prohibition or duty, and whose it is; every condition or exception attached to a rule; every fixed template; every term the text defines, and its definition; every word the text refuses; and the members and stated count of every closed list. A binding statement with no counterpart, or whose counterpart changes the outcome for any case, fails this clause.
2. **Nothing binding is added.** The after-text states no rule, permission, duty, exception, defined term or refused word that the before-text does not.
3. **Generalisation.** Several before-text statements may be replaced by one general statement only where every case each of them decided comes out the same under it, and it decides no case the before-text left undecided.
4. **Fixed text.** Everything inside code fences, and the frontmatter block at the top of the file where there is one, is byte-identical to the before-text.
5. **Headings.** A heading of the before-text whose exact text appears in any other of the following files keeps that exact text in the after-text: `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/graph-conventions.md`, `.claude/skills/expedition/wayfinder-divergences.md`, `.claude/skills/expedition-checker/SKILL.md`, `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-stop/SKILL.md`, `CONTEXT.md`, `.claude/rules/expedition-triggers.md`, `.scratch/graph-workflow/map.md`, `.scratch/graph-workflow/map-manager-only.md`, `.scratch/graph-workflow/map-implementation-rules.md`, `.gitignore`. Any other heading may be reworded, merged or removed, provided clause 1 holds.
6. **References inside the file.** Every reference the after-text makes to another part of the same file, such as "below", "above" or "under *X*", points at something the after-text holds.
7. **Terms.** Where the before-text uses a term defined in `CONTEXT.md`, the after-text spells that term as `CONTEXT.md` defines it wherever the idea recurs. The after-text uses no word that a `CONTEXT.md` `_Avoid_` line refuses, for the concept that line refuses it for, and coins no new term.
8. **Plain English.** Within the rewritten range, prose outside code fences has these six properties. The checker names each passage it judges to breach one, and which property it breaches.
   a. A rule is stated as what to do. A prohibition appears only where the rule cannot be stated as what to do, and then beside the positive statement.
   b. Bold appears only on a term at the place where it is defined. No clause or sentence is bolded for emphasis.
   c. An idea that is not a term defined in `CONTEXT.md` is said in plain words, with no figure of speech and no coined phrase. The following, from the shipped files, are the kind ruled out: "neither pen reaches", "rides a moment that already exists", "claimants", "in as many words".
   d. Statements are direct. No sentence is a slogan-shaped contrast or reversal, of the kind "the ban is about recording, not about files" or "amending is never authoring". No sentence uses "the whole of what".
   e. Every sentence is grammatical, and each "it", "this", "that", "they", "these" or "those" has one clear referent in the same sentence or the one before. The following is the kind ruled out: "Two things that is not, and neither is loosened by it."
   f. One idea per sentence. No sentence holds more than one dash-delimited aside, or more than one semicolon.
9. **Size, reported and not enforced.** The checker reports the `wc -w` count of the rewritten range in the before-text and in the after-text. The target is an after-text of at most two thirds of the before-text. Missing the target does not fail the work.
10. **Scope.** The work changes no path except those this condition's own clauses name, and within a named file, no text outside the rewritten range: that text is byte-identical to the before-text.

11. **Scope.** The work changes `CONTEXT.md` and no other path. The rewritten range is the whole file.
12. **The entries are kept.** Every term entry and every `_Avoid_` line in the before-text is present in the after-text, with the same term spelled the same way, and the same words refused for the same concept. The count of term entries and of `_Avoid_` lines is unchanged.

## Amendment by the human, 2026-09-24

*The human approved the manager's proposal, `verbatim`: "ok". The proposal and the answer to A that prompted it are recorded on [node 290](290-rewrite-the-research-contract-as-the-pilot.md). The manager drafted the wording below, and the human amended the condition with it. The original clauses above are left as they were. The clauses below take the place of clauses 1 and 2, add clause 1a, and add a sentence to clause 3.*

1. **Lost or changed statements are rule changes.** The binding statements are: every rule, meaning every instruction, permission, prohibition or duty, and whose it is; every condition or exception attached to a rule; every fixed template; every term the text defines, and its definition; every word the text refuses; and the members and stated count of every closed list. A binding statement of the before-text that has no counterpart anywhere in the whole after-text, or whose counterpart changes the outcome for any case, is a rule change. The checker lists every rule change it finds, each with the before-text statement and its after-text counterpart, or "removed". A rule change does not fail the work.
1a. **Terms `CONTEXT.md` does not define.** A term the before-text defines that `CONTEXT.md` does not define may be dropped as a term, where its meaning is still stated in plain words at the place it was defined. Dropping a term that way is not a rule change.
2. **Added statements are rule changes.** A rule, permission, duty, exception, defined term or refused word that the after-text states and the before-text does not is a rule change. The checker lists it the same way as under clause 1. It does not fail the work.
3. *(added sentence)* A generalisation that changes an outcome, or decides a case the before-text left undecided, is a rule change under clause 1 or clause 2.

## Answer

The glossary is rewritten in plain English, keeping all 51 entries and 41 `_Avoid_` lines, and five open conditions that quoted old entry wording get replacement clauses.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`, as changed by correction round 1. The checker passed it on run 2, finding two borderline rule changes, both on the worker's list. The human approved. The work landed as commit `de347dc`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-25. The worker's own text, pasted. The flags are raised under `## Flags` at the gate. The worker was sent the shared search script's path and command mid-node.*

HANDOVER:      Rewrite the glossary in plain English

ANSWER:
I rewrote `CONTEXT.md` in plain English in the worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/302-rewrite-the-glossary`. Nothing is committed. No other path changed.

- **Entries kept (clauses 11 and 12).** Base counts, confirmed: `grep -c '^\*\*'` gives 51 and `grep -c '_Avoid_'` gives 41. The after-text gives the same 51 and 41. `grep -c '^\*\*.*\*\*:$'`, node 247's baseline, also gives 51. Every headword is spelled as before and stays in the same order. Every `_Avoid_` line refuses the same words for the same concept.
- **`_Avoid_` lines.** The refused words are unchanged. Only the prose reasons inside four lines changed:
  - Checker: the dash asides became parentheses.
  - precondition: "collides with the word for a worker" became "is too close to the words used for a worker".
  - Handover: "owns that word" became "uses that word".
  - Promote: "both blur into park" became "both are too close in meaning to park".
  - Raise: the semicolon and trailing clause became one parenthesis.
- **Headings.** All eight are unchanged. Clause 5 protects two of them: `Expedition`, found in `wayfinder-divergences.md`, and `Closing an effort`, found in `expedition/SKILL.md` and `graph-conventions.md`.
- **No fenced blocks or frontmatter.** The file has none, so clause 4 has nothing to check.
- **Entries left byte-identical because open nodes own their changes:**
  - `Code slot` (nodes 81 and 92)
  - `Closed` (node 90)
  - `Closing report` (nodes 106 and 137)
  - `Node`, `Graph`, `Resolve`, `Supersede`, `Claim`, `Approval`, `Divergence`, `Manager note`, `Code commit`, and the `_Note_` line under Relay. These were already plain.
- **Words kept on purpose, because open nodes change them:**
  - "landed" in the Checker entry (node 307)
  - "written by the node that spawned it" in the Acceptance condition entry (node 318)
  - "pick report", twice (node 137)
  - "Three of the kinds name a skill the worker invokes" (node 134)
- **Figures and coined phrases removed:**
  - "charts the way … travels it", and "downstream"
  - "one-liaison-behind-a-crew"
  - "at low resolution", "reads cold" and "sibling" in Map, and "alone ever reads cold" in Checker
  - "Sharpness, not scope"
  - "graduates"
  - "A filter and never structure"
  - "every byte"
  - "inside the boundary", "laying runs end to end"
  - "outlives"
  - "characteristic case"
  - "Below that line", "pre-empts"
  - "can stand", "stay banked", "Paid for once"
  - "surfaced", "what survives", "on its way out"
  - "Uncapped"
  - "passes through no gate", "join key"
- **Refused words.** I grepped every refused word against the non-`_Avoid_` lines of the after-text. No refused word is used for the concept its line refuses it for. I also removed two uses I had introduced in drafts: "summary" for Map, since `summary` is refused for the closing report, and "plans" for the ancestor, since `plan` is refused for Graph and Map. Before-text uses that stay, and are not the refused concept:
  - "session", in "agent session" and "concurrent session"
  - "returns to open"
  - "queues"
  - "does not interrupt the human", in Cascade
  - "What done means"
  - "closes the node", which is `expedition/SKILL.md`'s own phrase
- **Size, `wc -w`.** 2,494 before and 2,721 after, which is 109%. The target was 1,663 and is missed. The before-text was mostly telegraphic fragments. Making each one a grammatical sentence and splitting dash-and-semicolon sentences (clauses 8e and 8f) added words.
- **Bar.** The repo has no build, no tests, no formatter and no CI. I found no manifest or task runner, which matches the record in `map-implementation-rules.md`. `git diff --check` is clean.
- **Method skills.** None invoked, so nothing was skipped.

RULE CHANGES:
I made no deliberate rule change. Every item below is a rewording that a strict reader could count as one. "Same outcome" is my judgement.
1. Handover `_Avoid_` reason. Before: "(the closing report owns that word)". After: "(the closing report uses that word)". The claim that the closing report owns the word exclusively is gone. The refused words are unchanged. This is the most substantive item. "Owns" was a figure (8c), and node 137 already finds the claim false. Node 137's demand for "a report goes to the human; a handover goes to the manager" is left to node 137.
2. Expedition entry. Before: "Where its ancestor charts the way, an expedition travels it — implementation lives inside the graph rather than downstream of it." After: "Its ancestor works out what the work is, and leaves the implementation to follow afterwards. An expedition also implements the work, as nodes inside its own graph." The figure became a literal statement with the same meaning. This breaks node 247's clauses (see the re-pointing search).
3. Intro. Before: "which it supersedes for efforts it is run on". After: "Expedition replaces `/wayfinder` on the efforts Expedition is run on." "Supersede" is a node term, so I used a plain verb here. Same outcome.
4. Intro. Before: "It grows only as terms are actually resolved". After: "A term is added only when the node that settles it resolves." The next sentence already tied each term to the node that settled it.
5. Map. Before: "the part every worker reads cold once per node". After: "Every worker reads one part of it once per node". "cold" is dropped. A worker is fresh on each node anyway.
6. Map. Before: "sits in a sibling of that part". After: "is kept in another file beside that part". The entry already says the map is more than one file.
7. Map. Before: "It indexes decisions and never restates one." After: "The map points to decisions and does not restate them." "Indexes" was replaced because `index` is refused for Map.
8. Fog. Before: "Sharpness, not scope, keeps something here." After: "Work stays in the fog until it can be phrased as one [a question]." The "not scope" half is carried by "In-scope" in the first sentence.
9. Out of scope. Before: "it never graduates into fog". After: "Work that is out of scope stays out of the fog." Same outcome, in positive form.
10. Labels. Before: "A filter and never structure". After: "A label only filters nodes." Both prohibitions that follow are kept word for word.
11. Manager. Before: "It never answers a question on the human's behalf." After: "A question put to the human is the human's to answer, and the manager never answers one on the human's behalf." This adds a positive form beside the prohibition (8a).
12. Manager. Before: "The record is what it alone writes — every answer, status, index line and flag — rather than every byte of the graph's files." After: "The record is every answer, status, index line and flag, and the manager alone writes it. Other text in the graph's files is not part of the record." The contrast is now stated directly.
13. Scribe. Before: "Assembling is inside the boundary — ordering pasted pieces, laying runs end to end, extracting a block of text to hand to somebody else — and rewriting them into a gloss is not." After: "The manager may assemble pasted pieces: put them in order, join them into one continuous text, and extract a block of text to hand to somebody else. It may not rewrite the pieces into a gloss." I read "laying runs end to end" as joining pieces into one text. I added "as it was handed back" to the paste sentence as the positive form of "never re-authors…".
14. Worker. Added: "Anything it has for the human goes through the manager." This is the positive form of "never addresses the human directly" (8a). It follows from the Manager entry's "the only thing the human ever talks to". Borderline addition.
15. Attempt. Before: "A node outlives its attempts: a dead worker is replaced". After: "A node lasts longer than any of its attempts: a worker that dies is replaced". Same outcome.
16. Checker. Before: "issues no verdict at all". After: "gives no outcome at all". "Outcome" is the entry's own word for `PASS` and `FAIL`.
17. Checker. Before: "its characteristic case is an acceptance condition that is incoherent or unmeasurable, which it alone ever reads cold". After: "The typical reason it raises is an acceptance condition that is incoherent or unmeasurable. The checker is the only agent that reads the condition without having read the node." I rendered "cold" with the implementation contract's own description of the checker.
18. grilling. Before: "independence being what decides which of them share one". After: "Only questions that are independent of each other share a payload."
19. research. Before: "Never involves the human." After: "It is worked without the human." Same outcome. This moves node 57's quote.
20. implementation. Before: "and is neither where the node ends nor where it resolves:". After: "The node continues after its gate:". The following clause still says "the node resolves after that".
21. precondition. Added the framing "It does only that work:" before the three prohibitions (8a). The `_Avoid_` reason was reworded, as listed under ANSWER.
22. Handover. Before: "the nodes it surfaced or invalidated". After: "the new nodes it found, and the nodes it invalidated".
23. Flag. Before: "It is settled at the first human moment its node's close reaches — an implementation node's gate where it has one, and otherwise the pick report that closes the node — and reaches the closing report only where the human never spoke again." After: "A flag is settled at the first moment, after its node's worker has handed back, at which the node is put in front of the human. That moment is an implementation node's gate where the node has one, and otherwise the pick report that closes the node. A flag goes into the closing report only where the human never spoke again." I rendered "its node's close" as the point after the worker has handed back, to avoid the refused `close`. "first" is kept.
24. Flag. Before: "usually a worker's, and the manager's where a judgement of its own reached the graph". After: "The agent is usually a worker, and it is the manager where a judgement of the manager's own went into the graph."
25. Acceptance condition. Before: "Its worker may not rewrite it, and a condition it judges wrong is a raise rather than a flag of its own". After: "Its worker leaves it as written, and may not rewrite it. Where the worker judges the condition wrong, the worker raises the matter, and does not raise a flag of its own." A positive form is added. Same outcome.
26. The bar. Before: "builds, no warnings, formatted, tests pass where relevant, plus whatever the repo itself demands. Properties rather than commands: the commands are discovered per repo." After: "it builds, it has no warnings, it is formatted, the relevant tests pass, and whatever else the repo itself demands is met. The bar is a list of properties. The commands that check them are discovered in each repo."
27. Relay. Before: "it never carries a second worker's". After: "A payload carries the questions of one worker only." Same outcome, in positive form.
28. Relay. Before: "The manager passes both along unaltered". After: "The manager passes the questions and the answers along unaltered". I read "both" as the questions and the answers. It could be read as the channel and the payload.
29. Raise. Before: "Whether it waits is a property of the channel rather than of the word". After: "Whether a raise waits depends on its channel." The "rather than of the word" contrast is dropped (8d).
30. Raise. Before: "a checker's question handed back alongside its outcome does not". After: "does not wait for the human".
31. Raise. Before: "Below that line it decides and leaves a flag instead." After: "Where none of these holds, the worker decides and leaves a flag instead." This matches the implementation contract's trigger reading.
32. Raise. Before: "it pre-empts grilling work in the manager's queue". After: "is put ahead of grilling work in the manager's queue".
33. Banked answer. Before: "Paid for once." After: "The human is not asked for it a second time." The figure became a literal statement of what it means.
34. Park. Before: "the answers it already holds stay banked". After: "it keeps the answers it already holds as banked answers".
35. Reject. Before: "Not a verdict on quality — a node whose code is merely wrong takes a correction round — so the node does not resolve, the working tree is cleaned, and what survives is the discovery." After: "A reject is not a verdict on quality: a node whose code is merely wrong takes a correction round. On a reject the node does not resolve, and the working tree is cleaned. What is kept is the discovery." This moves node 81's quotes.
36. Reject. Before: "surfaced something meaning its code should not exist". After: "revealed that its code should not exist".
37. Salvage. Before: "linked from whichever node inherits the work. Saved and never finished — nothing is tidied, made to build, or brought to the bar on its way out." After: "linked from the node that takes over the work. It is saved and never finished: nothing in it is tidied, made to build, or brought to the bar when it is saved."
38. Correction round. Before: "Uncapped, and neither a revision nor a check." After: "The number of rounds has no limit. A correction round is not a revision, and it is not a check."
39. Graph commit. Before: "It passes through no gate". After: "No gate applies to it".
40. Node trailer. Before: "the join key between git history and the graph". After: "It is the key that joins git history to the graph."
41. Plain rewordings with the same outcome:
   - Effort: "One expedition's worth of work … the human closing it" became "One expedition's work … until the human closes the effort".
   - Frontier: "takeable right now" became "the work that can be taken now".
   - Out of scope: "consciously ruled" became "deliberately ruled to lie".
   - Destination: "which is what makes … rather than fog" became "so … is not fog", and "non-empty frontier" became "a frontier that is not empty".
   - Cascade: "over edges and code, queueing … rather than interrupting" became "along edges and into code. It queues … and does not interrupt".
   - Sweep: "a cascade knows what changed, and a sweep is looking" became "a cascade starts from a known change, and a sweep searches for changes".
   - Verbatim / paraphrase: "two ways a recorded answer can stand" became "two forms a recorded answer can take".
   - Interview: "with their verbatim-or-paraphrase standing" became "each marked verbatim or paraphrase".
   - Gate: "never rendering" became "does not render".
   - Revision, Promote and AFK / HITL: grammar only.

Every closed list keeps its members and count:
- the Gate's three outcomes
- the bar's five properties
- the Raise's three cases
- the Scribe's four forbidden acts and three assembling acts
- the Handover's contents
- the Map's four contents
- the precondition's three prohibitions

RE-POINTING SEARCH:
- **Command**, run from `/home/mathieu/projects/graph-agent`:
  `python3 .scratch/graph-workflow/scripts/search-conditions.py 302 "$(git -C /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/302-rewrite-the-glossary merge-base HEAD master):CONTEXT.md" /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/302-rewrite-the-glossary/CONTEXT.md --skip .scratch/graph-workflow/nodes/302-rewrite-the-glossary.md --phrases /tmp/claude-1000/n302/phrases.txt`
  It searched 85 open or claimed nodes, excluding 302.
- **Second search.** A plain grep of those nodes' `Acceptance condition…` and `Amendment…` sections for `CONTEXT|glossary|chart`. It catches demands stated as properties, such as node 247's, which quote no span.
- **Handles searched:**
  - the path `CONTEXT.md`, and "glossary"
  - all eight headings
  - every quoted before-text span, and 6-word runs
  - these removed or replaced phrases: charts the way; travels it; downstream; lives inside the graph; one-liaison; liaison; supersedes for efforts; grows only as terms; vocabulary the skill files are written in; One expedition's worth of work; low resolution; reads cold; read cold; sibling; indexes decisions; never restates; Sharpness; graduates; never structure; A filter; every byte; inside the boundary; laying runs end to end; into a gloss; Named for its role; harness is replaceable; what stays the manager's is the recording; outlives its attempts; dead worker; never by the implementer; no verdict; characteristic case; alone ever reads; independence being; Never involves the human; lives outside the product tree; Need not be code; neither where the node ends nor where it resolves; decides nothing, probes nothing; collides with the word for a worker; surfaced or invalidated; owns that word; turning out wrong; over edges and code; queueing graph edits; a cascade knows what changed; a sweep is looking; first human moment; node's close reaches; usually a worker's; reached the graph; blur into park; a raise rather than a flag; ship it anyway; Properties rather than commands; discovered per repo; builds, no warnings, formatted; one thing in front of the human; second worker's; passes both along; property of the channel; blocking kind; Below that line; pre-empts; ordinary mode of a worker; answer can stand; stay banked; Paid for once; verbatim-or-paraphrase standing; never rendering the diff; surfaced something meaning; Not a verdict on quality; what survives is the discovery; saved off a stopped attempt; whichever node inherits; on its way out; Saved and never finished; Uncapped; neither a revision nor a check; passes through no gate; join key; landed implementation; written by the node that spawned it; three of them name a skill; reached by interviewing; the pick report; takeable; never answers a question on the human's behalf; does none of the graph's bookkeeping; chart
- **Replacement clauses:**
  - **Node 81, entry 2 (`Reject`).** Three replacements:
    - "Its clause *"so the node does not resolve, the working tree is cleaned, and what survives is the discovery"* is false." becomes "Its sentences *"On a reject the node does not resolve, and the working tree is cleaned. What is kept is the discovery."* are false."
    - "The rewritten clause says that" becomes "The rewritten sentences say that".
    - "*"Not a verdict on quality — a node whose code is merely wrong takes a correction round"*" becomes "*"A reject is not a verdict on quality: a node whose code is merely wrong takes a correction round."*"
    - The quoted *"The word is the human's alone; the checker's outcomes are `PASS` and `FAIL`"*, the `Code slot` entry, and both `_Avoid_` lines are byte-identical, so entries 1 and 3 need nothing.
    - Informational: `### What the minting worker deliberately left out` quotes the Salvage entry's old wording as that worker's words. It demands nothing, so I propose no change. The Salvage entry now reads "It is a path-limited diff that the manager writes without reading. It is kept out of the product tree, and linked from the node that takes over the work."
  - **Node 120, clause 4, as amended from node 296.** "`CONTEXT.md`: the `attempt` entry reads "A node outlives its attempts: a dead worker is replaced, and the replacement is a new attempt."" becomes "`CONTEXT.md`: the `Attempt` entry reads "A node lasts longer than any of its attempts: a worker that dies is replaced, and the replacement is a new attempt."" The rest of clause 4 is unchanged and still applies.
  - **Node 137, clause 5.** "`CONTEXT.md`'s `**Handover**:` entry ends today with `_Avoid_: report (the closing report owns that word), return, payload, deliverable`." becomes "`CONTEXT.md`'s `**Handover**:` entry ends today with `_Avoid_: report (the closing report uses that word), return, payload, deliverable`." The rest of clause 5 is unchanged. Clause 6's recorded count, "2 in `CONTEXT.md`" for `pick report`, and clause 7's `closing report` occurrences in `CONTEXT.md` (3) are the same before and after.
  - **Node 57, clause 5.** "`CONTEXT.md`'s `research` entry no longer says a research node *"never involves the human"* without qualification." becomes "`CONTEXT.md`'s `research` entry no longer says without qualification that a research node is worked without the human, which it states today as *"It is worked without the human."*" The rest of clause 5 is unchanged. Side note: the `research` entry has no `_Avoid_` line, before or after, so "Its `_Avoid_` line is unchanged" holds trivially.
  - **Node 247.** The Expedition entry no longer uses "charts", and `grep -rn -i "chart" .claude/skills/ CONTEXT.md` now returns nothing. Three replacements:
    - Scope paragraph: "`grep -rn -i "chart" .claude/skills/ CONTEXT.md` returns exactly one line, the glossary's own `Expedition` entry;" becomes "`grep -rn -i "chart" .claude/skills/ CONTEXT.md` returns nothing;"
    - Clause 4, second half: "and that the file's existing `Expedition` entry uses the word for what the workflow's ancestor does rather than for anything this workflow performs" becomes "and that the act the word names is what the file's existing `Expedition` entry says the workflow's ancestor does, *"works out what the work is"*, rather than anything this workflow performs".
    - Clause 9, second sentence: "The verb *charts* appears only in the `Expedition` entry item 8 preserves." becomes "No other form of the word *chart* appears anywhere in the file."
    - Clause 8 still holds as written, because it is measured from before 247's own work. The baselines 51 and 41 are unchanged.
- **Matches that need no change:**
  - 90: the `Closed` entry is byte-identical.
  - 92: the `Code slot` `_Avoid_` line is byte-identical.
  - 106: the `Closing report` entry is byte-identical.
  - 134: "## The five kinds of node" and "name a skill the worker invokes" are kept, and "worker may put several of its" is kept.
  - 307: "landed implementation" is kept.
  - 318: "written by the node that spawned it" is kept.
  - 258: its clauses are property-based. "a worker that dies is replaced" is the same statement for clause 3's test.
  - 61: it quotes nothing from the entries.
  - 44: "occupancy is discovered from the working tree" is kept.
  - 41, 97, 155, 220, 221, 285: they quote only kept strings.
- **Coincidental matches**, which quote other files: 111 (its clause 10 quotes `graph-conventions.md`'s Destination description), 206 (`graph-conventions.md`'s `## Labels`), 146, 156, 287, and the "sibling" hits in 44, 149, 202, 228, 232 and 233.
- **Checked, and they only mention `CONTEXT.md`:** 56, 101, 109, 124, 148, 190, 279, 284. For 109, "self-contained" still does not appear in `CONTEXT.md`.
- **Supersessions proposed:** none.

GENERALISATIONS:
None. No two before-text statements were merged into one general statement. The nearest items only restate a negative in positive form: Relay's "carries the questions of one worker only" and Out of scope's "stays out of the fog". Both are listed under RULE CHANGES.

INDEX LINE:    The glossary is rewritten in plain English, keeping all 51 entries and 41 `_Avoid_` lines, and five open conditions that quoted old entry wording get replacement clauses.

FLAGS:
ASSUMPTION: I left the Code slot, Closed and Closing report entries byte-identical, along with the words "landed" (Checker), "written by the node that spawned it" (Acceptance condition) and "pick report", even where the plain-English rule might have reworded them. Open nodes 81, 92, 90, 106, 137, 307 and 318 exist to change exactly those, and several of their conditions demand the surrounding text "left exactly as it stands". Rewording them here would only have churned those conditions. What I did: rewrote every other entry and the intro, kept every headword and `_Avoid_` line, and ran the shared search script and a grep for property demands.
Index sentence: The glossary rewrite left untouched the entries and phrases that open nodes 81, 90, 92, 106, 137, 307 and 318 are about to change, to avoid re-pointing their conditions.

ASSUMPTION: I changed the Handover `_Avoid_` reason from "the closing report owns that word" to "the closing report uses that word". "Owns" is a figure that clause 8c rules out. Every refused word is unchanged. The change drops a claim of exclusive ownership that node 137 already judges false. Node 137's own wording demand is left to it, and its clause 5 gets a replacement quote.
Index sentence: The glossary's Handover `_Avoid_` line now says the closing report "uses" the word report, not "owns" it, because "owns" is a figure the plain-English rule rules out.

NEW NODES:
- **Name:** The glossary's `Flag` entry names one case of a flag reaching the closing report, and the manager contract names two
  **Kind:** implementation
  **Question:** `CONTEXT.md`'s `Flag` entry says a flag goes into the closing report "only where the human never spoke again". `expedition/SKILL.md` says "Flags reach the closing report in two cases only": the first is a flag raised before this settling rule existed, on a node already resolved, and the second is a flag whose pick report the human never answered. Should the glossary carry both cases?
  **Blockers:** 302
  **Acceptance condition:**
  1. In `CONTEXT.md`, or at the path the glossary has moved to, the `**Flag**:` entry's sentence "A flag goes into the closing report only where the human never spoke again." is replaced by a statement that a flag goes into the closing report in two cases only. The first case is a flag on a node already resolved, raised before flags were settled at a node's gate or at the report that closes the node. The second is a flag whose closing moment the human never answered, because they never spoke again. Where the file no longer uses the term `pick report`, the statement uses the file's term for the same report.
  2. The entry's other sentences and its `_Avoid_` line are unchanged. No other entry in the file changes, and no entry is added or removed.
  3. No other path changes.
  4. The working tree meets the bar.

*The manager's note, 2026-09-26:* minted as [node 320](320-the-glossarys-flag-entry-names-one-case-of-a-flag-reaching-the-closing-report.md). The worker's acceptance condition above was first filed here as a pointer in place of the worker's text, which broke the scribe rule. It is restored here as the worker wrote it.

INVALIDATIONS: none

GATE PAYLOAD:
- **Checker findings:** none yet.
- **Paths touched:** `CONTEXT.md` (the worktree copy at `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/302-rewrite-the-glossary/CONTEXT.md`).
- **Scratch files, outside the repo:** `/tmp/claude-1000/n302/before.md`, which is the before-text, and `/tmp/claude-1000/n302/phrases.txt`, which is the search's phrase list. Both are under `$TMPDIR`.
- **Proposed commit message:**
  ```
  Rewrite the glossary in plain English

  Node: graph-workflow/302
  ```

RETROSPECTIVE:
1. **What I had to hunt for.**
   - Node 247's demand that "charts" stay in the Expedition entry. The shared script missed it, because 247 quotes no before-text span: its demand is a word-occurrence property, plus a byte-identical clause. I found it only by grepping the condition sections for `CONTEXT|glossary|chart`, after reading the manager's list. I first looked in the script's output.
   - Which open nodes demand text "left exactly as it stands": 81, 90 and 92. I read each condition, because the spawn listed the nodes but not which entries or phrases each one freezes.
   - Clause 7's refused-word check. I wrote an ad hoc script that pulls the words out of every `_Avoid_` line and greps the other lines. It caught two collisions I had introduced in drafts ("summary" and "plans").
   - The before-text. I used `git show $(git merge-base HEAD master):CONTEXT.md`, as the condition says.
2. **What arrived that this node did not need.**
   - Most of `map-implementation-rules.md`: only standing rule 5 and the bar paragraph applied.
   - Node 81's long historical subsections, which sit inside its `## Acceptance condition` section and so come with any read of the condition.
   - Node 301's full handover, which I read as a format sample. An example of the extra handover parts, embedded in the spawn or in the contract, would have avoided that.
   - The script's "sibling" hits in seven unrelated nodes. My phrase list caused them, because the phrase was too generic.
3. **What would have made this node easier.**
   - A spawn line naming the two clause-5-protected headings (`Expedition`, `Closing an effort`).
   - A table in the spawn of open nodes against the glossary entries or phrases each one quotes or freezes. The manager's list of node numbers was most of the way there.
   - A refused-word check (clause 7) and a property-demand grep (words such as "appears only in", "byte-identical", "left exactly") built into the shared search script.
   - Saying up front that the glossary's telegraphic fragments will grow when made grammatical, so the size target is out of reach.
4. **What was stale, wrong, or contradicted something else.**
   - The glossary's `Flag` entry names one case of a flag reaching the closing report. `expedition/SKILL.md` names two. This is reported as a new node.
   - Node 56's condition section says "`CONTEXT.md` today holds exactly **50** term entries", but its clause 1, and the file, say 51.
   - Node 57's clause 5 says the `research` entry's `_Avoid_` line is unchanged, but that entry has no `_Avoid_` line.
   - `CONTEXT.md`'s intro names `.scratch/graph-workflow/nodes/`, a path specific to this effort, in a shipped file. That goes against ground rule 1. I kept it, because node 56 rewrites the file's head.
   - Node 61's preamble ("`scribe` … appears nowhere in `CONTEXT.md`") is stale, as its earlier amendment already notes. Its clause 1 may already be satisfied by the existing `Scribe` entry.
   - Node 111's clause 2 names "charting" as a way to start an effort. Node 112's decision, which node 247 carries, refuses that word. This is outside my scope, and I did not verify which of the two is current.

## Review

### Checker run 1 — `FAIL`, acceptance condition

*The checker's own text, pasted, 2026-09-26. The checker was resumed from node 319's check.*

> FAIL: acceptance condition
>
> Node 302, "Rewrite the glossary in plain English", fails on one phrase under clause 8c. Everything else is met and the bar holds. The fix is a one-phrase rewording. Two statements have changed in ways I list as rule changes. Neither fails the work under the amendment.
>
> My contract is the main-tree checker contract, unchanged since my last check: its last commit is `76e66e3` and it has no uncommitted edits. The work is `CONTEXT.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/302-rewrite-the-glossary`, on branch `worktree-302-rewrite-the-glossary`, based on `02bdd3b`. I read the changed path only as the work.
>
> **The work changed one of the standards, so I checked that first.** `CONTEXT.md`'s `_Avoid_` lines are one of the standards the work is held against, and the work edits them. I compared the set of refused words, concept by concept, before and after, unwrapped. The sets are identical: 41 `_Avoid_` lines, the same words refused for the same concepts. Only the explanations in parentheses were reworded:
> - "owns that word" became "uses that word".
> - "collides with the word for a worker" became "is too close to the words used for a worker".
> - "blur into park" became "are too close in meaning to park".
> - "— reviewing is the human's; reject — that is the human's word at the gate" became "(reviewing is the human's), reject (the human's word at the gate)".
> - The Raise line's *ask* gloss moved from a trailing clause into parentheses.
>
> So the standard still stands, and I held the work against it as usual.
>
> **Finding: clause 8c, a figure of speech (1 instance)**
> - **Instance:** the **Promote** entry: "Turning a flag, or a one-line note of friction, into a node." "Friction" is a figure of speech for a difficulty met while working. `CONTEXT.md` does not define it, and no shipped file uses it as a term: `grep -rn -i friction .claude CONTEXT.md` returns only this line. The before-text has the same wording, but the rewritten range is the whole file. Plain wording, such as "a one-line note of a difficulty met while working", would meet the clause.
> - **Form:** a word or phrase outside any `CONTEXT.md` definition that carries its idea by a figure of speech where a literal wording exists.
> - **Extent (bounding set):** every sentence of the after-text, read by hand. I judged these acceptable:
>   - "a loose idea": plain idiom, used the same way in the fixed frontmatter of `.claude/skills/expedition/SKILL.md`.
>   - "steady state": the technical sense.
>   - "the code path": `CONTEXT.md`'s own Gate wording.
>   - "a crew of agents": a team, describing firstmate's own design.
>
> **RULE CHANGES**
> 1. **Scribe, the permission to assemble, reworded (borderline).**
>    - Before: "Assembling is inside the boundary — ordering pasted pieces, laying runs end to end, extracting a block of text to hand to somebody else".
>    - After: "The manager may assemble pasted pieces: put them in order, join them into one continuous text, and extract a block of text to hand to somebody else."
>    - "Laying runs end to end" (placing runs one after another) has become "join them into one continuous text". The object has also widened from runs to any pasted pieces.
>    - Read literally, "join … into one continuous text" may permit merging the pieces so their boundaries disappear. The before-text did not decide that case. The sentence that follows, "It may not rewrite the pieces into a gloss", still limits it.
> 2. **Manager, the ban on answering for the human, narrowed (borderline).**
>    - Before: "It never answers a question on the human's behalf."
>    - After: "A question put to the human is the human's to answer, and the manager never answers one on the human's behalf."
>    - The before-text covers any question. The after-text's "one" refers to "a question put to the human". Read literally, it may no longer cover a question meant for the human that is still waiting in the queue and has not yet been sent.
>
> How far the list reaches: I compared all 51 term entries, the intro and the section introductions of the before-text, word by word, against the whole after-text. I checked every definition, the rules each states and whose they are, conditions and exceptions, the refused words, and the closed lists with their counts. Those lists are the five kinds of node, the three gate outcomes, the three things that settle or place a flag, the four parts of a handover, and the three raise conditions.
>
> Beyond the two changes above, I judged every reworded statement to give the same outcome. The nearest cases:
> - **Worker's new sentence**, "Anything it has for the human goes through the manager": this restates the intro's "The human talks only to the manager" and the Manager entry's "the only thing the human ever talks to".
> - **Flag's settlement moment**, reworded: the sentence that now follows it still names the moment as "an implementation node's gate where the node has one, and otherwise the pick report".
> - **Map**: "reads cold" was dropped. It described the reading and was not a rule.
> - **Relay**: "passes both along" became "passes the questions and the answers along".
> - **grilling**: "independence being what decides which of them share one" became "Only questions that are independent of each other share a payload", together with the same permission.
> - No defined term was dropped, so clause 1a does not apply.
>
> **Clause by clause**
> 1. **Lost or changed statements: met.** The rule changes are listed above.
> 1a. **Terms `CONTEXT.md` does not define: met.** No term is dropped.
> 2. **Added statements: met.** Nothing is added beyond what is listed.
> 3. **Generalisation: met.** The Scribe permission is the one listed case.
> 4. **Fixed text: met.** The file has no code fences and no frontmatter.
> 5. **Headings: met.** All seven headings are identical to the before-text.
> 6. **References inside the file: met.** The file makes no references to other parts of itself.
> 7. **Terms: met.**
>    - Every term is spelled as defined.
>    - The Map entry now says "points to decisions" instead of "indexes decisions". "Index" is refused for the Map concept.
>    - "Session" in the Node and Claim entries is unchanged from the before-text.
>    - "`/wayfinder`" names the ancestor skill, not this workflow.
>    - No new term is coined.
> 8. **Plain English: fails on 8c**, as above. The other five properties hold:
>    - 8a: every prohibition has its positive form beside it. For example, "It never re-authors …" sits with "It pastes … as it was handed back", and "may not rewrite it" sits with "leaves it as written".
>    - 8b: bold appears only on the 51 term heads.
>    - 8d: I found no slogan-shaped sentence, and "the whole of what" does not appear.
>    - 8e: I read every it, this, that, they, these and those, and each has one clear referent. An entry's first "It" refers to the term being defined, as glossary entries do.
>    - 8f: three sentences hold one semicolon each (Node, Reject, Closed). One dash-delimited aside remains, in the Code slot `_Avoid_` line.
> 9. **Size (reported, not enforced):** the rewritten range is the whole file. `wc -w` gives 2494 before and 2721 after, which is 109% of the before-text. The target of at most 1663 is missed, which does not fail the work.
> 10. and 11. **Scope: met.** `git status --porcelain --untracked-files=all` shows only `CONTEXT.md` modified.
> 12. **The entries are kept: met.** The 51 term heads are identical, and the 41 `_Avoid_` lines are still there. Each refuses the same words for the same concept. The `_Note_` line under Relay is unchanged.
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, in the same state as at my last check: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:** standing rule 5 (plain English), `CONTEXT.md`'s `_Avoid_` lines (settled first, above), `/writing-for-agents`, and all five ground rules, which are met.
> - No reviewing skill is named, so I ran none.

*The manager's note, matching the two lists:* both of the checker's rule changes are on the worker's list: the Scribe permission is the worker's entry 13, and the Manager ban is its entry 11. The checker judges both borderline, and the worker judged both to keep their outcome. Nothing on the checker's list is missing from the worker's. What goes back is the clause 8c finding.

### Correction round 1 — the worker's changes for checker run 1

*The worker's own text, pasted, 2026-09-26.*

CORRECTION ROUND 1, node 302: Rewrite the glossary in plain English

Fixed the checker's single clause 8c finding. Only the Promote entry changed. The work is still uncommitted.

WHAT I CHANGED:
- In `CONTEXT.md`, the **Promote** entry. Before: "Turning a flag, or a one-line note of friction, into a node." After: "Turning a flag, or a one-line note of a difficulty met while working, into a node." This is the checker's suggested wording. The entry's `_Avoid_` line is unchanged.
- This touches something the acceptance condition names: clause 8c, and the rewritten range, which is the whole file. Nothing else changed.
- Checks after the edit:
  - `grep -rn -i friction .claude CONTEXT.md` returns nothing.
  - The counts are unchanged: 51 term entries (`grep -c '^\*\*'`) and 41 `_Avoid_` lines.
  - `git diff --check` is clean.
  - `wc -w` is now 2,725, up from 2,721.
  - `git status` shows only `CONTEXT.md` modified.

HANDOVER PARTS THAT DIFFER:
- **RULE CHANGES.** Add item 42. Before: "a one-line note of friction". After: "a one-line note of a difficulty met while working". The figure became a literal phrase. I judge the outcome the same, but it is borderline. The after-text is general, while node 41's planned `FRICTION` flag means a defect in the workflow itself. The before-text did not say which of the two it meant, so I kept the wider reading rather than narrow it.
- **RE-POINTING SEARCH.** I did not re-run the script. Instead I grepped the `Acceptance condition…` and `Amendment…` sections of every open and claimed node for "note of friction", "one-line note" and "Promote".
  - Node 41, "Ship the friction flag", quotes no glossary text. Its condition is about `graph-conventions.md` and the five worker contracts. The manager's note under it says `FRICTION` will be a new glossary term. The new wording keeps no part of the old phrase that 41 depends on, so no replacement clause is needed.
  - Node 208 matched only in the manager's own prose ("The manager promotes friction into a node"). That prose quotes nothing from `CONTEXT.md`, so no replacement is needed.
  - The earlier results stand: replacement clauses for nodes 81, 120, 137, 57 and 247, and no supersessions.
- **Size in the ANSWER.** The after-text is now 2,725 words, not 2,721. That is 109% of the before-text's 2,494, and the target is still missed.
- **GATE PAYLOAD.**
  - Checker finding, clause 8c on "friction" in Promote: reworded as above.
  - Paths touched: `CONTEXT.md` only (worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/302-rewrite-the-glossary`).
  - The commit message is unchanged: "Rewrite the glossary in plain English", with the trailer `Node: graph-workflow/302`.
- **Everything else is unchanged:** ANSWER apart from the word count, INDEX LINE, FLAGS, NEW NODES, INVALIDATIONS and RETROSPECTIVE.
- **The checker's two rule changes.** They are my own entries 11 (the Manager's positive-form question sentence) and 13 (the Scribe's permission wording). They were already listed, and I have not changed them.

### Checker run 2 — `PASS`, under the amended condition

*The checker's own text, pasted, 2026-09-26.*

> PASS
>
> This is check 2 of node 302, "Rewrite the glossary in plain English". The clause 8c finding from run 1 is fixed, and the correction changes nothing else. The work now meets the acceptance condition and the bar. The two rule changes from run 1 still stand, and neither fails the work under the amendment.
>
> My contract is the main-tree checker contract, unchanged since run 1: its last commit is `76e66e3` and it has no uncommitted edits. The work is `CONTEXT.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/302-rewrite-the-glossary`, based on `02bdd3b`. I read the changed path only as the work.
>
> **What changed since run 1.** I worked this out from the file itself, not from the worker's statement. It matches the statement: the **Promote** entry changed.
> - Before: "Turning a flag, or a one-line note of friction, into a node."
> - After: "Turning a flag, or a one-line note of a difficulty met while working, into a node."
> - The entry's `_Avoid_` line is unchanged.
>
> I found no other change:
> - The file still has 318 lines. The word count went from 2721 to 2725, which is exactly the four words this edit adds.
> - The sentences I cited in run 1 read as they did then: the Scribe permission, the Manager ban on answering for the human, and the Worker sentence.
> - The unwrapped `_Avoid_` and `_Note_` lines differ from the before-text in the same five reworded explanations as in run 1, and in nothing else.
> - `grep -n -i friction CONTEXT.md` now returns nothing.
>
> **The standard the work edits, settled first.** `CONTEXT.md`'s `_Avoid_` lines are one of the standards. The set of refused words per concept is identical before and after, and only the explanations in parentheses were reworded. So the standard still stands, as in run 1.
>
> **RULE CHANGES** (for the file as it now stands)
> 1. **Scribe, the permission to assemble, reworded (borderline).**
>    - Before: "Assembling is inside the boundary — ordering pasted pieces, laying runs end to end, extracting a block of text to hand to somebody else".
>    - After: "The manager may assemble pasted pieces: put them in order, join them into one continuous text, and extract a block of text to hand to somebody else."
>    - "Laying runs end to end" has become "join them into one continuous text", and the object has widened from runs to any pasted pieces. Read literally, this may permit merging the pieces so their boundaries disappear, a case the before-text did not decide. The sentence that follows, "It may not rewrite the pieces into a gloss", still limits it.
> 2. **Manager, the ban on answering for the human, narrowed (borderline).**
>    - Before: "It never answers a question on the human's behalf."
>    - After: "A question put to the human is the human's to answer, and the manager never answers one on the human's behalf."
>    - The before-text covers any question. The after-text's "one" refers to "a question put to the human". Read literally, it may no longer cover a question meant for the human that is still waiting in the queue and has not yet been sent.
>
> The Promote edit is not a rule change. It states the same idea in plain words, and the entry's refused words are unchanged.
>
> How far the list reaches: all 51 term entries, the intro and the section introductions of the before-text, compared word by word against the whole after-text. The comparison covered every definition, every rule and whose it is, every condition and exception, the refused words, and every closed list with its count. It is the full run-1 comparison, together with the one edit above. Beyond the two changes listed, I judged every reworded statement to give the same outcome, as detailed in run 1.
>
> **Clause by clause**
> 1. **Lost or changed statements: met.** The rule changes are listed above.
> 1a. **Terms `CONTEXT.md` does not define: met.** No term is dropped.
> 2. **Added statements: met.** Nothing is added beyond what is listed.
> 3. **Generalisation: met.** The Scribe permission is the one listed case.
> 4. **Fixed text: met.** The file has no code fences and no frontmatter.
> 5. **Headings: met.** Re-run: all seven headings are identical to the before-text.
> 6. **References inside the file: met.** The file makes no references to other parts of itself.
> 7. **Terms: met.** The edit introduces no refused word and no new term.
> 8. **Plain English: met.**
>    - 8c: the run-1 instance now uses plain words. The phrases I judged acceptable in run 1 stand: "a loose idea", "steady state", "the code path" and "a crew of agents".
>    - 8e: in the new Promote wording, the single sentence has no pronoun.
>    - 8a, 8b, 8d and 8f are unaffected by the edit. Re-run: bold still appears only on the 51 term heads.
> 9. **Size (reported, not enforced):** the rewritten range is the whole file. `wc -w` gives 2494 before and 2725 after, which is 109% of the before-text. The target of at most 1663 is missed, which does not fail the work.
> 10. and 11. **Scope: met.** `git status --porcelain --untracked-files=all` shows only `CONTEXT.md` modified.
> 12. **The entries are kept: met.** Re-run: the 51 term heads are identical, and there are still 41 `_Avoid_` lines, each refusing the same words for the same concept.
>
> **The bar, re-run in full**
> - The repo has no build, tests, formatter or CI, and `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, in the same state as at run 1: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:** standing rule 5 (plain English), `CONTEXT.md`'s `_Avoid_` lines (settled first, above), `/writing-for-agents`, and all five ground rules, which are met.
> - No reviewing skill is named, so I ran none.

*The manager's note, matching the two lists:* both rule changes are the worker's entries 13 and 11. The worker's entry 42 (Promote) the checker judges not a rule change. Nothing on the checker's list is missing from the worker's.


### Gate — approve, 2026-09-26

The human, `verbatim`: *"approve"*

## Flags

`302.1` **· settled** `ASSUMPTION` — I left the Code slot, Closed and Closing report entries byte-identical, along with the words "landed" (Checker), "written by the node that spawned it" (Acceptance condition) and "pick report", even where the plain-English rule might have reworded them. Open nodes 81, 92, 90, 106, 137, 307 and 318 exist to change exactly those, and several of their conditions demand the surrounding text "left exactly as it stands". Rewording them here would only have churned those conditions. What I did: rewrote every other entry and the intro, kept every headword and `_Avoid_` line, and ran the shared search script and a grep for property demands.

`302.2` **· settled** `ASSUMPTION` — I changed the Handover `_Avoid_` reason from "the closing report owns that word" to "the closing report uses that word". "Owns" is a figure that clause 8c rules out. Every refused word is unchanged. The change drops a claim of exclusive ownership that node 137 already judges false. Node 137's own wording demand is left to it, and its clause 5 gets a replacement quote.
