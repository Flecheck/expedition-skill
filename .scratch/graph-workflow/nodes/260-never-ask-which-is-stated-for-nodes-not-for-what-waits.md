# The never-ask-which rule is stated for picking a node and not for what is already waiting

Type: implementation
Status: claimed

Blocked by: none

## Question

*Directed by the human. Their words, `verbatim`, on 2026-09-16:*

> It should also be added to the rule and the skill but I thought it was already present.

**What "it" is.** The steering they gave in the turn before, `verbatim`: *"Just give stuff, don't ask me too
choose"* — the manager never ends a report by listing what is waiting and inviting the human to pick one. The
manager had just written that into `map.md` as steering scoped to this effort. This node carries it into the two
shipped files, `.claude/skills/expedition/SKILL.md` and `.claude/rules/expedition-triggers.md`.

**They were substantially right that it is already present, and the node is what is missing rather than what is
absent.** Four sentences already in force say most of it:

- `SKILL.md`, `## What is in front of the human, and when`: *"Exactly one question is in front of the human at a
  time, and nothing ever displaces a live one."* — the ordering exists.
- The same section: *"Within a tier, arrival order."* — the tie-break exists.
- The same section: *"Every relayed question names in one line whatever else is waiting — by node name and kind
  only, never restating the other question or its options."* — the bound on what may be named exists.
- `expedition-triggers.md`, third bullet: *"if the human has nothing to do and there is a question/gate, give it to
  him."* — the trigger exists.

**What none of them says is the prohibition itself**, in the imperative, for a thing already waiting. The file says
it once and only for the other case — *"Never ask which node to work"* under `### Picking the next node` — and that
sentence is about work not yet started, not about two payloads both sitting in the queue. The manager read all four
sentences and then put both waiting items in front of the human and invited a pick, which is the evidence that an
ordering stated as a fact does not land as an instruction.

## Acceptance condition

***Written by the manager, and this node was minted by the manager rather than by an agent.*** The contract's
prohibition is on authoring a condition for a node **an agent** minted; there is no agent here whose condition this
would displace.

Done when all five hold.

**1.** `.claude/skills/expedition/SKILL.md`, in the section `## What is in front of the human, and when`, states in
its own words that the manager never asks the human which of the things already waiting to take next — that where
more than one is waiting the manager sends the one the ordering already in that section selects, rather than
listing them and inviting a choice. It is placed with the queue rules it follows from, not under
`### Picking the next node`.

**2.** That statement says in the same breath what it does **not** reach, both parts:

- the one-line naming of whatever else is waiting stays, since it invites nothing and another rule in that same
  section requires it; and
- a question a **worker** puts to the human that genuinely offers options is the worker's question and is relayed
  whole — the rule binds the manager's own reports, not a payload it is carrying.

**3.** `.claude/rules/expedition-triggers.md`'s third bullet carries the same prohibition in the one clause the file
has room for, in the file's own register. Nothing else in that file changes by this node's hand.

**4.** The paragraph the manager added to `.scratch/graph-workflow/map.md` beginning *"**The manager never asks the
human to choose which waiting thing to take next.**"* is **replaced** by a pointer to the shipped statement — the
steering having stopped being this effort's own once it ships — and its existing wording is appended **verbatim** to
`.scratch/graph-workflow/map-history.md` under a heading mirroring the section it came from. The human's own words
survive that replacement somewhere in the effort's record.

**5.** No other file is changed. Nothing is written in `decisions.md` or `flags.md`. Every markdown link resolves.
The bar applies.

## The manager's note at filing

*Not a change to anything above.*

**Sequencing, which is the manager's and not this node's.** [Node
255](255-ship-the-priority-list-into-the-managers-contract.md) edits **both** of the same two shipped files — a new
section in `SKILL.md` after `## What is never yours`, two clause deletions elsewhere in it, and four changes to
`expedition-triggers.md` including its title and closing section. The two nodes touch different lines and neither
condition quotes the other's target text, but **two workers must not hold either file at once**. Node 255 is the
older and already carries a condition its author wrote; it goes first. This is a sequencing constraint the manager
holds, not a `Blocked by` edge.

**This node is the same shape as [node 256](256-collapse-the-two-map-notes-the-priority-list-subsumes.md)** —
effort-scoped steering that stops being effort-scoped the moment it ships, leaving a duplicate behind in the map.
Clause 4 is what stops this one accruing that debt rather than paying it later.

**The manager is the party this rule binds and the party that broke it**, in the same session in which it wrote the
steering to disk. That is recorded here rather than as a flag because no judgement of the manager's is being banked
for review; it is the observation that motivates clause 1 being an imperative.

## What the work states

*The worker's `ANSWER`, pasted as it wrote it.*

> The prohibition now stands in the imperative in both shipped files, and the map carries a pointer in place of the
> steering.
>
> **`SKILL.md`, `## What is in front of the human, and when`** — two paragraphs inserted immediately after the
> tiers/arrival-order paragraph and before *"Every relayed question names in one line whatever else is waiting"*. The
> first is the rule: *"Never ask the human which of the waiting things to take next."* The second is the boundary:
> the one-line naming stays, and a worker's genuinely optioned question is relayed whole.
>
> **Three calls inside that, which a later reader would otherwise re-derive:**
>
> 1. **Placement is with the ordering rather than with the naming rule.** The prohibition is a consequence of the
>    tiers and arrival order — *the ordering has already chosen, so there is nothing to ask* — so it sits directly
>    under the sentence that states the ordering. Placing it after the naming rule would have made it read as a
>    qualifier on naming, which is the one thing it does not touch. It is deliberately not under `### Picking the next
>    node`, which is about work not yet started.
> 2. **It is written as an imperative with a named failure mode, not as another statement of fact.** Four sentences
>    already in force implied the rule and the manager read all four and broke it anyway; the diagnosis on the node is
>    that an ordering stated as a fact does not land as an instruction. So the sentence is a prohibition in the same
>    grammatical shape as the file's existing *"Never ask which node to work"* — the two now read as a matched pair —
>    and it names the exact act that went wrong (*listing what is waiting and inviting them to pick*) rather than only
>    the principle. The cost clause is the throughput one the section already argues in: the single channel spent
>    making a choice twice.
> 3. **The carve-out cites the naming rule by quoted phrase**, per the effort's fourth standing writing rule, rather
>    than by position.
>
> **`expedition-triggers.md`, third bullet** — one clause appended in the file's own terse, human-voiced register:
> *"Where several are waiting, pick the one the order gives you and send it — never list them and ask him which to
> take."* It leans on the `## Priority` list already in that file, so it adds no second ordering. Nothing else in that
> file changed.
>
> **`map.md`** — the steering paragraph is replaced by a pointer naming both shipped sites, shaped exactly like the
> two pointer items above it (the ground rules and the four standing writing rules). **`map-history.md`** — the
> paragraph is banked verbatim under `## Superseded from `map.md`'s `## Notes` at node 260`, diff-verified
> byte-identical to the source. The human's words *"Just give stuff, don't ask me too choose"* sit inside that banked
> paragraph and so survive the replacement.
>
> **Four files changed and no others.** Nothing was written in `decisions.md` or `flags.md`, and no node's status
> line was touched.
>
> **On the condition's quality, since the manager wrote it and invited scepticism:** it is good, and clause 2 is the
> reason — the two carve-outs are precisely the ambiguity I would otherwise have had to decide alone, and they were
> handed to me already settled. Where authorship shows is **clause 4**: it names its target paragraph by its opening
> words and assumes my tree holds it. It does not (see the flag). That is the signature of an author reading their
> own live working tree rather than the committed state a worker is given, and it is the one clause I could not
> satisfy literally.

**The index line the worker wrote**, held here until the node resolves:

> The never-ask-which prohibition ships in the imperative into `SKILL.md`'s queue section and the triggers rule's
> third bullet, with the map's steering paragraph banked and replaced by a pointer.

## Flags

`260.1` `ASSUMPTION` — *The worker's own text, pasted.*

> Clause 4 demands that a `map.md` paragraph be **replaced** by a pointer. That paragraph is **not in my worktree**:
> it is an uncommitted change in the manager's main tree, and the worktree was reset to `4598672`, which predates it.
> The only difference between the two copies of `map.md` is that one paragraph, verified by diff. I did not raise, on
> the judgement that the substance is unambiguous and the end state identical: I banked the paragraph verbatim from
> the manager's live copy and wrote the pointer at the same position, so **my `map.md` is byte-for-byte what "replace
> the paragraph with a pointer" would have produced on the manager's tree**. What it is not is a *replacement* in the
> git diff, which shows an addition. Two consequences the manager must carry, neither of which is mine: **(a)**
> landing will collide — merging this branch while the main tree holds an uncommitted `map.md` will refuse, or, if
> resolved the wrong way, will leave the steering paragraph alive and defeat clause 4's whole purpose; **(b)** the
> markdown link `nodes/260-...md` that both `map.md` and `map-history.md` now carry **dangles in this worktree** and
> resolves only in the manager's tree, the node file being untracked there. Clause 5 asks that every markdown link
> resolve; it does in the landed state and not in the tree under check. I judged citing the node correctly to
> outweigh dropping a link the effort's second standing writing rule requires.

## Retrospective

*The worker's own text, pasted.*

> 1. **What I had to hunt for.** That `map.md`'s target paragraph was absent from my tree — found by grepping the
>    worktree for the quoted phrase, getting nothing, and then grepping the main tree, which hit. I looked in the
>    worktree first, which was right; what was missing was any reason to suspect a difference. **Two minutes and
>    roughly 8k tokens went on establishing it** — `git status` on both trees, a `diff`, and a scan of `git log
>    --stat` to learn how earlier record-file nodes landed. A single line in the spawn — *the manager's tree holds
>    uncommitted record changes, including the paragraph clause 4 names* — would have removed all of it. The manager
>    knew this and could not know I needed telling.
> 2. **What arrived and this node did not need.** Judged backwards from finished work: **the review-route paragraph
>    in `map-implementation-rules.md`**, which the spawn itself warned is written for the checker — the warning was
>    accurate and I still read the paragraph to confirm it, because a warning that a passage is not mine does not let
>    me skip it safely. That is about 700 words per implementation worker. A heading such as `### For the checker
>    only` would let a worker stop at the heading instead of at the end of the paragraph. **`decisions.md` under the
>    prescribed grep** returned twelve hits and I used none of them — the prescribed grep terms were right for the
>    node's subject and the file simply holds nothing bearing on it, which is a good outcome for the instruction
>    rather than a bad one. **`CONTEXT.md`'s `_Avoid_` lines**: I went for four words and grepped out all 38 lines,
>    then read six entries; that is the arrangement working. The one place I took a whole file for one fact was
>    **`graph-conventions.md`**, where I needed `## Writing the map` and the `Change the map` procedure — I grepped
>    the headings first and read two windows of 40 and 20 lines, which the spawn's *"its `## Writing the map` section
>    only"* made possible; without it I would have read 480 lines.
> 3. **What would have made this node easier.** The spawn was unusually good — the warning about node 255, the
>    pre-scoped reads, and the note that a fifth sentence reading like the other four would fail the same way, which
>    is the sentence that shaped my draft more than anything in the condition. The gap is the one in (1). **A
>    structural suggestion beyond this node:** where a condition quotes text a worker must find, saying *which tree
>    that text is in* costs one clause and would have saved the whole investigation. The record itself has the same
>    hole from the other side — `map-manager-only.md`'s worktree route says how a tree is created and reset and says
>    nothing about the manager's own uncommitted state at the moment of the reset.
> 4. **What I read that was stale, wrong, or contradicted something else.** Nothing stale. One contradiction, and it
>    is the flag: clause 4 describes a tree state that does not hold. I will note that **the manager's framing of the
>    four already-present sentences was exactly right** and the node file's quotation of all four was the most useful
>    single thing I read — I checked each against the file as it now stands and all four were accurate after node
>    255's edits, which is not something I could have assumed.

## The manager's disposal of the retrospective's record items

*Not the worker's text.*

- **The spawn not saying the manager's tree holds uncommitted record changes** → **the manager's conduct, and it
  cost this worker ~8k tokens to discover.** It will say so in every spawn for a node whose work is the record. But
  the worker is right that it *"could not know I needed telling"*, which is why the durable half is minted rather
  than promised: **[node 266](266-a-worker-cannot-see-the-record-the-manager-has-not-committed.md)**, carrying the
  worker's own question.
- **`map-manager-only.md`'s worktree route saying nothing about the manager's uncommitted state at the moment of the
  reset** → **folded into node 266**, which is the same hole from the record's side. Not a second node.
- **`map-implementation-rules.md`'s review-route paragraph, read for nothing** → **this is the second worker in two
  nodes to report it**, and the effort's repeat threshold is met. The worker's point is sharper than the first
  report: a *warning* that a passage is not yours does not let you skip it, only a **heading** does. Still not
  minted — it is node 246's subject on a second file and widening an open node is not the manager's. **Named for
  the human**, now twice over.
- **The scoped reads working** — `decisions.md` by grep returning twelve hits used for nothing, `CONTEXT.md` by
  grep, and `graph-conventions.md` cut from 480 lines to two windows of 40 and 20 — → **carried to [node
  165](165-measure-whether-a-fed-file-earns-its-place.md)** as measurement rather than proposal. This is the second
  such measurement in two nodes.

## Review

### Run 1 — `PASS`

*The checker's own text, pasted. It was spawned by the manager, was given the acceptance condition as extracted
text, the bar as properties, the four changed paths and the tree holding them, the record-as-work rule, and this
effort's ground rules and four standing rules for writing copied as text. It was given nothing from this node or
from the effort's record. **It was told one fact about the tree and no more**: that the worktree's base predates
some of the manager's record writing, so the committed `map.md` there is not identical to the manager's working
copy — and told to establish what clause 4 demands against the tree it was given and to say precisely if the clause
could not be met there.*

> **PASS**
>
> **Route taken.** `EnterWorktree` with the given absolute path succeeded from my working directory
> (`.scratch/graph-workflow/nodes`, not the repo root). No sandbox override was needed at any point.
>
> **I read the changed paths as the work**, under the implementation-rules file's rule that an implementation node's
> work on this effort may be the effort's own record — two of the four (`map.md`, `map-history.md`) are record files,
> and I held them against the condition and the standards exactly as product code, deriving no statement of intent
> from them. No node status line, no `decisions.md`, no `flags.md` appears among the work, so the bookkeeping rule
> does not bite. `map-implementation-rules.md` states **no reviewing skill is named for this repo**, so I ran none
> and went looking for none.
>
> **1 — MET.** `SKILL.md` gains, inside `## What is in front of the human, and when`, the paragraph beginning
> *"**Never ask the human which of the waiting things to take next.** The two tiers and arrival order have already
> chosen it; send that one."* It states the prohibition in its own words (no phrase is lifted from the archived
> steering) and names the ordering that section already holds as what selects. Placement established from `grep -n
> '^## \|^### '`: the paragraph sits between the tier rules and the one-line-naming rule, and `### Picking the next
> node` begins strictly after it.
>
> **2 — MET.** The immediately following paragraph, *"**Two things that is not**, and neither is loosened by it"*,
> carries both parts: the one-line naming stays, citing *"Every relayed question names in one line whatever else is
> waiting"* — which I confirmed is the real sibling rule, standing just below — and a worker's genuinely-optioned
> question is relayed whole, *"this binds the reports you write yourself, never a payload you are carrying."*
>
> **3 — MET.** `expedition-triggers.md`'s third bullet gains one appended sentence: *"Where several are waiting, pick
> the one the order gives you and send it — never list them and ask him which to take."* It is in the bullet's own
> register (imperative, second person to the manager, *him* for the human, matching *"give it to him"* already
> there). `git diff` shows exactly one changed line in that file; nothing else in it moved.
>
> **4 — MET on what is observable in this tree; two sub-parts not covered (below).** The paragraph the clause names
> is **absent from this worktree's `map.md` at the base commit** — `git show 4598672:.scratch/graph-workflow/map.md |
> grep -c "never asks the human to choose"` returns `0` — so no replacement was possible here, and `map.md` shows
> `+2` with no deletion. What I *can* establish: `map.md` now carries a pointer paragraph in `## Notes` naming both
> shipped locations and citing node 260; `map.md` carries no copy of the steering paragraph; `map-history.md` gains a
> block under `## Superseded from `map.md`'s `## Notes` at node 260 — …`, whose shape mirrors the committed precedent
> at node 244; and the human's own words, `verbatim`: *"Just give stuff, don't ask me too choose"*, are present inside
> that block. The archived block's opening sentence matches the condition's quoted opening exactly. So the end state
> the clause aims at holds in this tree.
>
> **5 — MET, with one finding handed back below.** `git status --porcelain` returns exactly the four ` M ` lines and
> nothing else; `decisions.md`, `flags.md` and `nodes/` are untouched. I resolved every markdown link in `map.md` and
> `map-history.md` by unwrapping each file to one line, extracting every `](…)` target, and stat-ing it relative to
> the file. All resolve **except** two new pointers to `nodes/260-…-waits.md`, which resolve to nothing in this tree.
>
> **The bar — held.** Discovered from the repo rather than any account: the worktree root contains only `.claude/`,
> `CONTEXT.md`, `.gitignore`, `.scratch/`; no manifest, no task runner, no `.github/workflows`. Nothing to build, no
> tests, no formatter, no CI, so the bar here is entirely its non-command half. **Ground rules** — (1) nothing added
> to the shipped files names this repo, machine or toolchain; (3) both additions are written to the manager in its own
> contract and the triggers file it owns, and neither tells any spawned agent to address the human; (4) short prose,
> no new machinery. **Four standing rules** — rule 4 holds, the `SKILL.md` addition citing its sibling by quoted
> phrase and `map.md` citing `SKILL.md` by heading, no line numbers in the added text; rule 2 holds, the `map.md` item
> stating its current form and citing node 260 by link without restating it. **`graph-conventions.md`,
> `## Writing the map`** — the `map.md` addition is a current statement citing by markdown link, with the account
> moved out verbatim to `map-history.md` under a mirroring heading, which is the `Change the map` shape. Its item
> measures 593 bytes against the 500-byte target; the convention states in as many words that this is *"a target the
> writer aims at and never a rule that forces text out… nothing fails"*, and eleven existing `## Notes` items are
> larger, so this is not a finding. **`CONTEXT.md` `_Avoid_` lines** — checked by hand per the rules file's warning
> that a grep returns false positives; the added text uses *queue* only for the pending queue (the `_Avoid_` is on
> *queue* as a name for **Frontier**), and *payload* and *report* only in their established `SKILL.md` senses. No
> distinctive refused term appears. **`/writing-for-agents`** — the negation lever is the one that bites, and both
> additions pair the prohibition with the positive target in the same breath (*"send that one"*; *"pick the one the
> order gives you and send it"*). The `SKILL.md` statement and the triggers clause are not a duplication defect, the
> triggers file declaring itself *"the copy that survives a compaction"* whose governing statement is in the skill.
>
> ```
> NOT COVERED:
> - "is **replaced** by a pointer to the shipped statement" — the paragraph the clause names is not in
>   this worktree's `map.md` at base commit 4598672 (verified: zero matches). The replacement the clause
>   demands therefore cannot be performed here and I cannot observe whether it happened. What I can and do
>   establish is the end state: `map.md` carries the pointer and carries no copy of the paragraph.
> - "its existing wording is appended **verbatim**" — the source wording exists in no file I hold, so I
>   have nothing to compare the archived block against beyond its opening sentence, which the condition
>   quotes and which matches exactly. Verbatim-ness of the remainder is not establishable in this tree.
> ```
>
> **Consequence of the above, which the party holding the record must settle:** as written, this branch *adds* a
> pointer to `map.md` without removing anything. Merged into a `map.md` that does carry the steering paragraph, the
> paragraph would survive alongside the new pointer, and the replacement clause 4 demands would still not have
> happened. The `map-history.md` preamble already asserts that it did — *"Moved verbatim under the `Change the map`
> procedure"* and *"`map.md` now carries a pointer in its place"* — which is a claim that is false of this tree as it
> stands.
>
> **FINDING, handed back alongside the `PASS` and not a `FAIL`.** Two markdown links resolve to nothing in the files
> I hold, both new in this change — in `map.md`'s added `## Notes` item and in `map-history.md`'s added block, both
> targeting `nodes/260-never-ask-which-is-stated-for-nodes-not-for-what-waits.md`. Found by unwrapping each file to a
> single line, extracting every `](…)` target, and stat-ing it relative to the file's directory. Every other link in
> both files resolves, and every link in the base commit's versions resolves, so these two are the only ones. *Form,
> as a predicate:* a relative markdown link target added by this change that does not exist as a file relative to the
> linking file's directory. *Extent:* an enumerator over the four editable paths, unwrapping each and stat-ing every
> non-anchor target, which returns exactly the two instances. **Why this is not a `FAIL` on clause 5.** I can
> establish the target is absent from what I hold; I cannot establish it is absent from the effort. This worktree's
> `nodes/` directory tops out at node 241, so it is provably a stale snapshot for a node numbered 260, and the target
> is a node file — manager-owned bookkeeping this contract's own rules make a `FAIL` for a worker to create. Failing
> here would fail the work for the base it was given. **The party holding the record settles what it means**: if
> `nodes/260-…-waits.md` exists there under that exact filename, both links resolve and clause 5 is met outright.

**The manager's settlement of the two items the checker referred to it.** *Not the checker's text, and both are
measurements rather than readings.*

- **The two links resolve.** `nodes/260-never-ask-which-is-stated-for-nodes-not-for-what-waits.md` exists in the
  manager's tree under exactly that filename — `ls` on the full path returns it. **Clause 5 is met outright**, on
  the checker's own stated condition for it.
- **The verbatim-ness the checker could not establish, the manager can, and did.** The steering paragraph exists
  only in the manager's uncommitted `map.md`; the manager extracted it from `git diff` (937 bytes) and matched it as
  a fixed string against the worktree's `map-history.md`: **one match, byte-identical**. The banking is verbatim in
  full and not only in its opening sentence.
- **The landing collision is resolved and is smaller than it looked.** The manager's `git diff` on `map.md` is
  **exactly the two lines of the steering paragraph and nothing else**. So the replacement clause 4 demands is
  performed at landing by discarding that one uncommitted hunk — the paragraph goes, and the branch's fast-forward
  brings the pointer into the same position. **The text is banked before it is discarded**, which is the `Change the
  map` procedure's own order, and the two halves happen to sit in two trees only because of the defect [node
  266](266-a-worker-cannot-see-the-record-the-manager-has-not-committed.md) names.
- **The checker's observation that `map-history.md`'s preamble asserts something false of its own tree stands** and
  is not dismissed: it is true of the landed state and false of the branch in isolation. Nothing is changed for it.
