# The manager contract forbids rendering a reply while graph-conventions.md permits a paraphrase

Type: grilling
Status: resolved
Blocked by: none

## Question

*Surfaced by [node 312](312-cut-the-rules-both-the-manager-contract-and-graph-conventions-state.md)'s worker, and filed by the manager as it wrote it.*

SKILL.md's `### The human's words` says "You never render a reply, so its mark never depends on your judgement." graph-conventions.md's `### Recording the human's words` says "The manager marks an answer `paraphrase` only where it could not avoid rendering the answer in its own words." Both were already in the before-texts at 9d8044c. Is the manager ever allowed to render a reply, and if so, which file states when?

## Answer

The manager renders a reply only when the human's words are no longer in its context to copy, marking it `paraphrase` with a note of why; SKILL.md states when.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The human's `"ok"` is under `## Interview`. The implementation is [node 319](319-carry-the-one-case-the-manager-renders-a-reply-into-the-manager-contract.md).

## Interview

### Attempt 1

**Q1, from the worker**, pasted as it wrote it, 2026-09-25. Put to the human in the same turn.

```
NODE:          The manager contract forbids rendering a reply while graph-conventions.md permits a paraphrase
ABOUT:         This node decides whether the manager may ever write the human's answer in its own words, marked `paraphrase`, and which file says when. The two shipped manager files disagree today, and node 312's worker surfaced the disagreement while it was splitting rules between them.
SO FAR:        The two files on master:
                - `expedition/SKILL.md` `### The human's words` says: "Paste the reply as the human wrote it, however terse… You never render a reply, so its mark never depends on your judgement."
                - `expedition/graph-conventions.md` `### Recording the human's words` says: "The manager marks an answer `paraphrase` only where it could not avoid rendering the answer in its own words."
               Where they came from. Node 25 ("What is recorded when the human takes an option as offered") decided that the manager pastes whatever you wrote, marked `verbatim`. It kept `paraphrase` on purpose, defined as "a rendering the manager could not avoid", which "after this decision is rare and always deliberate". Node 26 shipped that as "nothing is `paraphrase` unless the manager genuinely could not avoid rendering it". Later, the manager contract shortened this to a flat "you never render one" and lost the "unless". So this is drift from node 25, not two decisions that disagree.
               Where `paraphrase` still matters:
                - The only live `paraphrase` marks on this map are on old entries: node 12's three and node 17's three. In those, your actual words were never kept.
                - The glossary and all three worker contracts define `verbatim` and `paraphrase` as a pair.
                - The manager reports that on this effort it has marked every reply `verbatim`, down to one-word replies, and has never used `paraphrase`.
               When a rendering could not be avoided: only when your words are no longer there to copy. That happens if the manager's context is compacted, or its session ends, before it writes them down. The contract already requires writing your words down in the same turn they arrive, so this case only follows a failure. Whether the words are still there is a fact, not a judgement. By contrast, "could not avoid" as graph-conventions.md words it is a judgement, and node 25 found that a marker which depends on a judgement gets got wrong.
               Settled on my own authority (will be an ASSUMPTION flag): if rendering is allowed, the rule for *when* goes in SKILL.md, and graph-conventions.md keeps only what the mark means, plus a pointer. That follows the split you approved at node 312: file format and procedures in graph-conventions.md, the manager's own choices in SKILL.md.
ASK:           Should the manager ever record your answer in its own words? If yes, is this the case: your words are no longer there to copy?
RECOMMENDED:   Yes, in that one case only. Where your words are no longer in the manager's context, because a compaction or a session ending lost them before they were written down, the manager records what it still holds. It marks that `paraphrase`, adds a note of its own saying why, and never marks it `verbatim`. In every other case it pastes. SKILL.md states this in place of "You never render a reply". graph-conventions.md's "could not avoid" sentence is replaced by a pointer to SKILL.md. This rests on three things:
                - it is node 25's decision, restored;
                - it turns the trigger into a fact, so the mark still never depends on the manager's judgement;
                - it leaves an honest mark for the one failure that really happens. Without it, a manager that lost your words must either claim `verbatim` for its own text or leave the answer out. Node 25 named the first of those as the unsafe direction.
ALTERNATIVES:  - Never render, and retire `paraphrase` as a live mark, keeping it only to read the old entries on nodes 12 and 17. The rule is simpler, but a manager that has lost your words has no honest mark to use, and the pair defined in the glossary and the three worker contracts goes one-sided.
               - Keep graph-conventions.md's "could not avoid" wording and only soften SKILL.md's "never". This leaves the trigger as a judgement.
               - Also allow rendering a long reply that covers several things. Rejected: taking out the part that answers one question is already scribe work, so the manager can quote that part as you wrote it.
```

**A1, the human**, `verbatim`, 2026-09-25: *"ok"*

This takes the option the worker offered as `RECOMMENDED`, in the worker's words: *"Yes, in that one case only. Where your words are no longer in the manager's context, because a compaction or a session ending lost them before they were written down, the manager records what it still holds. It marks that `paraphrase`, adds a note of its own saying why, and never marks it `verbatim`. In every other case it pastes. SKILL.md states this in place of "You never render a reply". graph-conventions.md's "could not avoid" sentence is replaced by a pointer to SKILL.md."*

**The worker's retrospective**, handed back with Q1, pasted:

1. Hunted for: the origin of each sentence. `git log -S` found "never render a reply" at 6745f37, and before that "You never render one" in the earlier text. The "could not avoid" clause traced to 0cec4e7, which is node 26. The intent behind both is in node 25's `## Answer`, which I reached through decisions.md line 44. I searched decisions.md for "paraphrase" first, and it hit only unrelated lines. The useful decision line uses the word "verbatim", so it would have been missed without that extra term in the spawn.
2. Not needed:
   - Nearly all of map.md: the worktree, token, resume and retrospective items, about 39 KB against one relevant fact (compaction, in the node-24 line).
   - The first decisions.md grep printed a 43 KB result, because an unbounded match on "render"/"verbatim"/"marker" hits long lines. Cutting lines short (`cut -c`) fixed it.
   - A spawn pointer straight to node 25, with "check whether the shipped wording dropped node 25's exception", would have avoided the search.
3. Easier: the node file could name node 25 as the origin of `paraphrase`'s meaning. The index line for node 25 could say it keeps `paraphrase` for renderings that could not be avoided. As it stands, it only says "marked `verbatim`".
4. Stale or contradictory:
   - SKILL.md's absolute "never" contradicts node 25 and node 26, which is this node.
   - The glossary still defines `paraphrase` as "the manager's rendering", with no rule for when that happens.
   - Node 312's decisions index line reads "file format and procedures there, manager choices here". "There" and "here" do not say which file is which to someone reading it later.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-25. The worker's own text, pasted. Its retrospective, unchanged from the one handed back with Q1, is under `## Interview`; the worker's own item 4 notes "Nothing new since the first payload".*

HANDOVER:      The manager contract forbids rendering a reply while graph-conventions.md permits a paraphrase

ANSWER:        **The manager records a reply in its own words in one case only: when the human's words are no longer in its context to copy.** That happens when a compaction or the end of a session lost the words before they were written onto the node. The entry then holds what the manager still has. It is marked `paraphrase`, never `verbatim`, and it carries a note of the manager's own saying why it could not paste. In every other case the manager pastes the reply as the human wrote it.

The trigger is a fact: are the words still there to copy or not. It is not a judgement of the manager's, so the mark still never depends on the manager's judgement. Node 25 ([What is recorded when the human takes an option as offered](25-recording-an-option-taken.md)) found that a mark which depends on a judgement gets got wrong. This is also why graph-conventions.md's "could not avoid rendering" does not stay as the trigger: it asks the manager for a judgement.

This restores node 25's decision rather than making a new one. Node 25 kept `paraphrase` for "a rendering the manager could not avoid", which it called rare and always deliberate. Node 26 shipped that as an "unless" clause. The manager contract's wording later became a flat "You never render a reply", which dropped the exception. So the two files disagreed because the wording drifted, not because two decisions disagreed. Retiring `paraphrase` was considered and set aside. It would have left a manager that lost the human's words with two bad choices: claim `verbatim` for its own text, which is the unsafe direction node 25 named, or leave the answer off the record.

**Where it is stated:**
- The rule for *when* goes in `expedition/SKILL.md` `### The human's words`, in place of "You never render a reply".
- `expedition/graph-conventions.md` `### Recording the human's words` keeps both marks and what each one means. Its "could not avoid" sentence is replaced by a pointer to SKILL.md.
- This follows the split the human approved at [node 312](312-cut-the-rules-both-the-manager-contract-and-graph-conventions-state.md): file format and procedures in graph-conventions.md, the manager's own choices in SKILL.md.

Carrying this into the shipped files is the implementation node reported by this node.

INDEX LINE:    The manager renders a reply only when the human's words are no longer in its context to copy, marking it `paraphrase` with a note of why; SKILL.md states when.

FLAGS:
ASSUMPTION — Prose for the node: I decided on my own which file states when a reply may be rendered: `expedition/SKILL.md` `### The human's words`, with graph-conventions.md keeping only the marks' meaning and a pointer. The ground is the split the human approved at node 312: file format and procedures in graph-conventions.md, the manager's own choices in SKILL.md. When to render is the manager's conduct, not the form of an entry. I stated this placement in the payload's SO FAR, and it was also written into the recommendation the human assented to with "ok". Even so, the human was never asked about placement as a question of its own.
Index sentence: The rule for when the manager may mark an answer `paraphrase` was placed in SKILL.md rather than graph-conventions.md, on node 312's split, without a question of its own.

NEW NODES:
- Name: Carry the one case the manager renders a reply into the manager contract
  Kind: implementation
  Question: State in the shipped manager files the only case where the manager records a reply in its own words, and remove the contradiction between them.
  Blockers: none
  Acceptance condition:
    1. In `.claude/skills/expedition/SKILL.md`, section `### The human's words`, the sentence "You never render a reply, so its mark never depends on your judgement." no longer appears. In its place, that section states all four of the following, in wording of the worker's choosing:
       (a) The manager records a reply in its own words only when the human's words are no longer in its context to copy, because a compaction or the end of a session lost them before they were written onto the node.
       (b) Such an entry holds what the manager still has. It is marked `paraphrase`, never `verbatim`, and it carries a note of the manager's own saying why it could not paste.
       (c) In every other case the manager pastes the reply as the human wrote it. The existing sentence "Paste the reply as the human wrote it, however terse." may stand as this statement.
       (d) Whether the words are still present to copy is a fact, not a judgement of the manager's, so the mark does not depend on the manager's judgement.
    2. In `.claude/skills/expedition/graph-conventions.md`, section `### Recording the human's words`:
       - the sentence "The manager marks an answer `paraphrase` only where it could not avoid rendering the answer in its own words." no longer appears;
       - the section says that SKILL.md's `### The human's words` states when an answer is marked `paraphrase`;
       - the section still names both marks, `verbatim` and `paraphrase`, and still says what `verbatim` means;
       - the section states no condition of its own for when `paraphrase` is used.
    3. No sentence in either file still says or implies that the manager never renders a reply, or that it may render one for any reason other than the one in 1(a).
    4. The work changes no file other than these two.

*The manager's note, 2026-09-26:* this node is minted as [node 319](319-carry-the-one-case-the-manager-renders-a-reply-into-the-manager-contract.md). The worker's acceptance condition above was first filed here as a pointer to node 319 in place of the worker's text, which broke the scribe rule. It is restored here as the worker wrote it.

INVALIDATIONS: none. The answer restores the decisions of node 25 and node 26. The answers of node 296 (manager contract rewrite, part 1) and node 312 describe SKILL.md's text as it read then, including "You never render a reply". Once the implementation node lands, those descriptions are out of date. That is a later edit to a file, not a contradicted decision.

## Flags

`315.1` **· settled** `ASSUMPTION` — Prose for the node: I decided on my own which file states when a reply may be rendered: `expedition/SKILL.md` `### The human's words`, with graph-conventions.md keeping only the marks' meaning and a pointer. The ground is the split the human approved at node 312: file format and procedures in graph-conventions.md, the manager's own choices in SKILL.md. When to render is the manager's conduct, not the form of an entry. I stated this placement in the payload's SO FAR, and it was also written into the recommendation the human assented to with "ok". Even so, the human was never asked about placement as a question of its own.
