# What the token findings change in the workflow and its skills

Type: grilling
Status: resolved

Blocked by: 52, 54

## Question

Take what [How an agent workflow and its skills reduce their own token
cost](52-token-cost-of-a-workflow.md) found and what [Re-review the shipped files against
`/writing-for-agents`](54-review-against-writing-for-agents.md) found, and decide what this workflow does about
it: which rules for writing a skill become standing rules of the effort, what changes in the workflow's own
shape, and which shipped files are edited.

The human's instruction that this node exists to serve, `verbatim`: *"And then follow it up with a grilling node.
We can then add new rules for writing skills , updates to the workflow and update to the skills."*

**Three kinds of output, and they land in three different places.** Worth separating before the interview
starts, because they have different costs and different reversibility:

- **Rules for writing a skill** — standing preferences in `map.md`'s `## Notes`, or a clause in the bar. Cheap,
  reversible, and reaches every later implementation node for free.
- **Changes to the workflow's shape** — what a spawn carries, what a handover returns, how many checkers run,
  what the manager holds. These touch decisions already resolved, so each one is an invalidation to record, not
  an edit to make quietly.
- **Edits to the shipped files** — reported as implementation nodes with conditions, not done here.

**Why it is blocked on two nodes rather than one.** Node 52 supplies the external facts. Node 54 supplies the
standard this effort is held to, freshly re-sited — and the two overlap: the new standard's `## Pruning` section
is itself token-optimisation advice, so deciding rules from node 52 alone would risk adopting a rule the
standard already states differently, or contradicting it.

**One tension this node should expect to meet head-on**, because it is already written into the map and the
whole effort leans on it: *"the node files are written for agents… so completeness for an agent beats brevity
for a human, and the density of these files is correct rather than a failure of editing."* That preference was
settled by the human at node 26's gate and has been used to **discard** at least two findings — a code-review
skill's duplication smell at node 22, and a checker's brevity finding at node 31. A token-optimisation pass runs
straight into it. It is not obviously wrong: [Friction from running this map by hand](24-self-hosted-friction.md)
found agent context to be the binding constraint, which is an argument *for* pruning what agents read, and the
density preference was priced against human patience. Whether the preference survives, narrows, or splits by
reader is this node's, and it is the human's to settle rather than a worker's.

## Interview

### Attempt 1 — routing key `graph-workflow/53/a1`

**Q1, from the worker**, pasted as it wrote it.

```
NODE:          What the token findings change in the workflow and its skills

ABOUT:         Two research nodes just landed. One measured what this workflow's own files cost
               in tokens; the other re-held the shipped files against `/writing-for-agents`, the
               standard you asked this effort to be judged by, after it was rewritten upstream.
               This node decides what actually changes as a result — which rules become standing
               preferences, what changes in the workflow's shape, and which shipped files get
               edited. It is being decided now because both inputs are resolved and every
               candidate change is blocked behind one thing only you can settle: whether a
               preference you fixed at node 26's gate still holds, and over which files.

SO FAR:        Read both research nodes in full, `map.md`, `decisions.md`, and the new standard
               on disk (both its files). Then verified the load-bearing facts myself rather than
               trusting the summaries.

               THE MEASUREMENTS THAT MATTER. `map.md` is ~19,840 tokens. Every worker reads all
               of it, and — this is the part nobody had priced — a subagent never reads its
               parent's prompt cache, so each worker pays that whole read at full uncached rate,
               once per node. At the dogfood target's 179 nodes that is ~4M tokens of re-reading
               one file. It is 4.4x the largest shipped contract and 81% of the entire shipped
               corpus, and it grows monotonically. Against that, two things turn out to be
               non-issues by measurement: struck-through text is 2.1% of the map (so never-delete
               is not what makes it expensive — live append-in-place prose is; one single fog
               paragraph is 5,147 tokens, 26% of the file, larger than any contract we ship), and
               the 700 duplicated words per contract that node 50 is deciding are ~5% of one
               worker's opening read, so that argument has to stand on maintenance rather than
               tokens. Two more things the research settled by measurement and asked me not to
               spend your time on: the always-loaded skill descriptions total ~180 tokens across
               all six contracts, and tool-schema deferral is already on by default.

               THE COLLISION. Your preference at `map.md:39`, verbatim: "A node's reader is the
               next agent, so completeness for an agent beats brevity for a human, and the density
               of these files is correct rather than a failure of editing." The new standard names
               a failure mode called SPRAWL — "a document simply too long, even when every line is
               live and unique. Attention thins across the excess" — whose entire content is that
               completeness is no defence, because the cost is attention rather than staleness or
               repetition. That is head-on. It also widened its own scope to "any document an agent
               consumes", which puts node files, `map.md` and `decisions.md` inside it for the
               first time.

               WHAT I VERIFIED MYSELF, and it changes the shape of the question. The preference as
               written names NODE FILES only. But it has already been stretched twice beyond them,
               both times to discard a finding: at node 31 a checker found the word `unwrap`
               spelled out as a sentence at four sites in one contract and the finding was
               discarded because "the map endorses completeness for an agent reader over brevity"
               — that is a SHIPPED CONTRACT, not a node file; and the map's own fog item at line 84
               applies the preference to `map.md` itself. So the preference is currently governing
               three different document classes while being stated over one. I also re-ran the
               standard's leading-word hunt: `scribe` — one pretrained word for the manager's whole
               discipline — appears exactly ONCE in the shipped tree, in the one file no worker
               reads and nothing points at, and appears nowhere in `CONTEXT.md` at all, while the
               concept is spelled out as a sentence at ten sites across the five contracts. That
               refactor is blocked by nothing except this preference.

               SETTLED ON MY OWN AUTHORITY, and it will come back as a flag: I am treating the
               shipped contracts as a third document class distinct from node files, because they
               are the only ones that leave this repo.

ASK:           Does "completeness for an agent beats brevity for a human" still hold — and over
               which of the three document classes? My reading is that it was decided about node
               files, against a human reader as the alternative, and has since been applied to two
               other classes whose readers are different: a node file has one reader who needs all
               of it, a shipped contract has one reader per spawn and travels to other repos, and
               `map.md` has every reader on every node, each needing a different fraction of it.

RECOMMENDED:   Narrow it by document class, on the preference's own premise rather than against it.
               Three rulings, and only the third changes anything:

               1. NODE FILES — stands verbatim. The premise "a node's reader is the next agent"
                  is exactly true here: one worker, claiming that node, needing that node whole.
                  Sprawl does not bite where every line bears on the one task the reader has.
                  Nothing to edit, and the two findings already discarded under it stay discarded.

               2. SHIPPED CONTRACTS — stands, but on a better ground than completeness. The
                  research found the compression literature's penalty concentrates on
                  format-bearing instruction text, the class our contracts mostly are (a five-part
                  handover with named parts, a required `## Review` shape, a flag marker fixed as
                  a literal string): one measured study found compression past 30% failed every
                  task in an agent scenario, attributed to loss of format. So contracts stay
                  complete, with a stated boundary — compress the prose that explains WHY, never
                  the shapes. That boundary is what makes the `scribe` refactor admissible, since
                  a leading word replaces adjectives and sentences, never a shape.

               3. `map.md` — the preference does NOT reach it, and this is the one thing I am
                  asking you to change. Its reader is not "the next agent" in the singular; it is
                  every worker on every node, and each needs a different ~5% of it. That is sprawl
                  in the standard's exact sense, it is the largest measured recurring token cost
                  in the whole design, and the standard's own cure applies: disclose behind
                  pointers rather than hold everything inline. Ruling this now does not commit you
                  to any particular mechanism — that is my next question — it only removes the
                  preference as the reason not to look.

               What this rests on: the preference's own words. It defends density by saying the
               reader needs it. That is a claim about a reader who needs the material, and it is
               true of a node file and false of a shared file each of whose readers needs a
               different fraction. So this is the preference applied consistently rather than
               overturned — which also means it keeps doing the work you fixed it to do, including
               keeping the density of the record safe from every future pruning pass.

ALTERNATIVES:  - Survives unchanged over all three classes. Cheapest to decide, and it is a real
                 option: you settled it deliberately and it has been load-bearing twice. The cost
                 is that it forecloses the single biggest lever the research found (~4M tokens),
                 and leaves this effort's product failing the standard it declares itself held to
                 on the one charge that standard says completeness cannot answer.
               - Reverses outright: adopt sprawl wholesale and prune node files too. Costs the
                 record, contradicts two discards already made, and runs into the measured finding
                 that compressing format-bearing text is the fragile class.
               - Splits by reader as human-versus-agent: two renderings of each file, one dense for
                 agents and one brief for you. Costs a rendering step per file and makes the
                 manager an author of text it currently only transcribes, which the scribe rule
                 forbids.
               - Leave the preference untouched and just cap the map mechanically (the fog item
                 already lists "cap an item's updates" as a candidate). Gets the saving without
                 the ruling — but the preference then still stands over a file it demonstrably
                 should not govern, so the next worker re-argues this from scratch.
```

**The manager's notes on Q1, to travel with it.**

1. **The human's steering to bump token-use priority arrived after this question was written and before it was
   put to them**, and it is now a standing preference in `map.md`. It does not answer Q1 and should not be read
   as doing so: the instruction ranks token-reducing work up the frontier, and Q1 asks whether the biggest such
   reduction is *permitted* at all. Worth naming so the two are not conflated.
2. **The worker's central factual claim is verified**, and by the manager rather than taken on trust: the
   preference's text names node files, and it has been applied twice beyond them. `map.md` is currently **83,473
   characters** — it grew by ~4,100 today, in the course of recording the finding that it is too big, which is
   the practice indicting itself.
3. **One thing the manager adds against the recommendation's item 1.** *Node files stand verbatim* rests on
   *"one worker, claiming that node, needing that node whole"* — and that is now false for a class of node file
   this effort keeps producing. Nodes 47, 52 and 54 each carry a research answer several thousand words long
   that **no future worker claims**, because those nodes are resolved; their readers are the next worker on
   *some other* node, following a link for one fact. The premise holds for an **open** node and not for a
   **resolved** one. Not an objection to item 1's ruling on the files a worker actually claims; a reason the
   class may need splitting again, and cheaply, since the map already distinguishes the two by `Status:`.

**A1, from the human**, `verbatim`: *"for 53 q1 ok for recommanded."*

The option it points at, quoted from Q1's `RECOMMENDED` and attributed to the worker that wrote it: *"Narrow it
by document class, on the preference's own premise rather than against it."* All three rulings as offered —
**node files**, the preference stands verbatim and the two findings already discarded under it stay discarded;
**shipped contracts**, it stands but on the fragility ground rather than on completeness, with the boundary
*compress the prose that explains why, never the shapes*; and **`map.md`**, the preference does not reach it.

**No divergence.** The reply takes the recommendation whole and names no alternative, so nothing here is
`paraphrase`. Recorded under [What is recorded when the human takes an option as offered](25-recording-an-option-taken.md).

**What this does and does not commit.** Ruling `map.md` outside the preference *"does not commit you to any
particular mechanism… it only removes the preference as the reason not to look"*, in the worker's own words. So
the largest measured recurring cost in the design — every worker reading ~19,840 tokens of this map cold and
uncached, once per node — is now open to being reduced, and by what means is the next question.

**The manager's note 3 was not reached by this reply and is therefore still the worker's.** It observed that
item 1's premise — *"one worker, claiming that node, needing that node whole"* — is false for a **resolved**
node file carrying a research answer nobody will claim, and that `Status:` already distinguishes the two
classes cheaply. The ruling on node files stands as assented to; whether the class wants splitting again is
undecided and unasked.

**Q2, from the worker**, pasted as it wrote it.

```
NODE:          What the token findings change in the workflow and its skills

ABOUT:         A1 settled that the density preference does not reach `map.md`. This is the
               follow-up it exists to enable: by what mechanism does a worker stop reading ~22,300
               tokens of that file once per node. It is the single largest recurring token cost the
               research found, and you have just prioritised token-use improvement above the rest
               of the frontier.

SO FAR:        I re-measured the file rather than reusing the research node's numbers, because it
               grew ~9,700 characters while my first question was with you. It is now 89,214
               characters, ~22,300 tokens, and every worker reads all of it cold and uncached, once
               per node — a subagent never reads its parent's cache.

               WHERE THE BYTES ARE, measured by section:
                 `## Not yet specified` (the fog)      51,866 chars   58% of the file
                 `## Notes`                            33,210 chars   37%
                 `## Out of scope`                      2,330 chars
                 `## Destination` + decisions pointer   1,018 chars
               One single fog item is 20,589 characters — 23% of the whole file in one paragraph,
               larger than any file we ship.

               WHAT THAT MATERIAL ACTUALLY IS, and this is the finding that decides the mechanism.
               I read it looking for what a worker could act on. Almost none of it is standing
               state; it is append history, and most of the appends restate what a resolved node
               already holds. Two clean examples I can quantify. Lines 19–31, 7,154 characters, are
               the entire saga of one preference being recorded, found obstructed twice, dissolved,
               then renamed upstream, then landing — whose live residue is now one 202-character
               ground rule at line 74, and the saga sits above it in full. Line 78, 6,414
               characters, is the nine-deltas paragraph, every delta discharged into
               `graph-conventions.md`, and it says so itself. Adding the fog, the material a worker
               cannot act on comes to roughly 65,500 characters — about 74% of what every worker
               reads.

               THE RULE THIS EFFORT ALREADY HAS, applied to every graph file except this one.
               `decisions.md` opens with it: "A decision lives in exactly one place, its node; this
               file never restates one." That is why `decisions.md` is 608 characters in the map's
               place and one capped line per node in its own. `map.md` is the one graph file that
               restates its nodes rather than citing them — its fog items say "node 31 added
               requirement X, node 35 bounded it, node 19 widened it" at length, while nodes 31, 35
               and 19 each hold their own account in full.

               WHICH REFRAMES NEVER-DELETE, and I think dissolves the objection rather than
               fighting it. The research already measured that struck-through text is 2.1% of this
               file, so never-delete is not what makes it expensive. What makes it expensive is
               LIVE restatement of what a resolved node holds — and never-delete was written to
               stop information being lost, which restatement's removal does not do.

               ONE CORRECTNESS FINDING I FOUND WHILE MEASURING, reported because you ruled that a
               saving may not be ranked above one. Citations into this map by line number are
               already stale: the research node published four days ago cites `map.md:75` for the
               large fog paragraph (now line 88) and `map.md:51` for a standing preference (now line
               54). Append-in-place shifts every line below the append, so any line-number citation
               into this file decays on its own. That is true today, before anything I propose.

               CONSTRAINTS I CHECKED MY ANSWER AGAINST. Node 29's new rule — a shipped file may
               require only what travels with it, or what the effort must declare in the form the
               requirement needs — and the mechanism below survives it, because a file for
               accumulated history is a convention every effort's map needs, not a fact about this
               one. Node 29's new five-item ground-rules block, 2,423 characters, is the one thing
               in this file with a named consumer and a stated reason to be inline: a checker reads
               no map and receives it only as copied text. That block is live state and stays.
               `provenance` is refused by name in the glossary, so it is out as a name.

               STILL OPEN AND MINE TO DISPOSE OF: your note that item 1's premise is false for a
               resolved research node, whose readers are workers on other nodes following a link
               for one fact. I am holding it rather than dropping it, because the mechanism below is
               the same move and may answer it without a separate ruling. I will dispose of it
               before handover either way.

ASK:           Which mechanism stops a worker reading this file whole? My recommendation is one
               rule plus one bulk, verbatim move, described below.

RECOMMENDED:   Extend `decisions.md`'s own rule to `map.md`: an item states its CURRENT form and
               cites the nodes that shaped it; it does not restate what they hold. Carry that out
               by moving, not by editing — every append the items currently carry goes verbatim
               into a sibling file the map points at, and what stays in `map.md` is each item's
               current statement.

               So `map.md` becomes: the destination, the standing preferences, the ground-rules
               block, the operational notes, the out-of-scope list, and each fog item as one or two
               live lines naming the nodes that shaped it. Everything else moves out intact.

               Measured, on today's file: a worker's map read goes from ~22,300 tokens to ~6,200.
               About a 72% cut, on the largest recurring cost in the design, and it holds rather
               than eroding because the growth from here lands in the sibling.

               Four things it rests on:
                 - It is not a new idea, it is this effort's own founding rule for an index file,
                   applied to the one graph file that never got it. `decisions.md` was split out on
                   a growth-rate argument that the map's own fog item records as FALSIFIED — the
                   other sections grew too, in words per item rather than item count. This is that
                   argument made correctly, on measured numbers.
                 - Nothing is deleted, so it needs no exception to never-delete and no per-append
                   judgement about what is safe to lose. A bulk verbatim move is the same move
                   `decisions.md` was created by — "moved, not shortened, per the standing rule."
                 - It is the new standard's own prescription. Its cure for sprawl is the ladder:
                   disclose reference behind pointers, inline what every branch needs and push
                   behind a pointer what only some branches reach. A fog item's provenance is
                   reached by some nodes; its current statement is needed by all.
                 - It fixes the cause rather than relocating the symptom. Any mechanism that only
                   moves today's bulk leaves the practice that produced it running.

               The cost, stated plainly: it is an implementation node with real authoring in it —
               writing each item's current statement is a judgement, and a careless one loses a
               load-bearing fact. The mitigation is that the appends survive verbatim in the
               sibling, so what is at risk is the index, not the information.

ALTERNATIVES:  - Drop the duplicated appends instead of moving them, since the citing node already
                 holds each one. Smaller result, no fifth file — but it needs your explicit licence
                 against never-delete, and it needs a judgement per append about whether the node
                 really does hold it. The map itself warns this is not always true: line 78 says it
                 "remains the only place the reasoning behind each delta is written down."
               - Consolidate in place with a cap: when an item exceeds N appends, the next node to
                 touch it rewrites it as one current statement. The remedy the map's own fog item
                 already lists. Keeps one file, but spreads the authoring risk across every future
                 node instead of doing it once, and rewrites the record repeatedly rather than
                 moving it once.
               - Change nothing in the map; narrow only what the five contracts tell a worker to
                 read — read `## Notes` and `## Out of scope` always, a fog item only where the
                 spawn names it. By far the cheapest: five one-line edits, no record risk at all.
                 Measured at a 56% cut rather than 72%, and it leaves ~3,400 tokens of discharged
                 history inside the section it keeps, in a file that keeps growing. Worth taking as
                 a first step if you want the saving before the authoring work, and it composes
                 with the recommendation rather than competing with it.
               - Have the manager render a per-node digest of the map into each spawn. Kills the
                 read entirely, and I am setting it aside rather than offering it seriously: the map
                 already reasons that the manager carrying a standard makes the manager its author,
                 and it contradicts "most of the context lives in the workers."
```

**The manager's notes on Q2.**

1. **Every measurement was re-run by the manager and every one holds.** `map.md` is 89,214 characters. By
   section: fog **51,887**, `## Notes` **33,219**, `## Out of scope` **2,346** — the worker's figures to within
   the boundary line of each heading. The largest single line is **20,589** characters, at line 88, exactly as
   claimed. `decisions.md` opens verbatim with *"A decision lives in exactly one place, its node; this file never
   restates one."*
2. **The correctness finding is confirmed and is worse than stated.** Node 52's citations are stale: `map.md:75`
   and `map.md:51` now land on a blank line and on the wrong preference respectively; the paragraph it meant is
   at 88 and the preference at 54. **So a resolved research node's citations into the map decayed within four
   days, and the manager filed more of them today.** Every `map.md:NN` in this graph is suspect, which is a
   defect of the append-in-place practice rather than of any node.
3. **One thing the worker could not know, and it cuts toward its third alternative.** The manager has been the
   principal author of the growth it measured: ~9,700 characters today, of which a large share is the record of
   node 52's finding that the file is too expensive. **The practice indicting itself is not a coincidence — it is
   the mechanism.** Every resolution the manager files appends here, so the file grows fastest exactly when the
   effort is working well.
4. **The manager's own view, since it is asked for as standing practice.** The recommendation is right and the
   third alternative is the one to take **first**, not instead. Five one-line edits buy 56% with **zero** record
   risk and no authoring, and the worker says plainly they compose. Under the human's own limit — *a saving may
   not be ranked above a correctness finding, and not by predicted size* — taking the measured, risk-free 56%
   before the authoring work is the ordering that limit implies. The manager notes against its own convenience
   that the recommendation's authoring risk falls on **the manager**, since writing each item's current statement
   is a scribe act it would be doing.

**Not an answer to Q2 — a fifth mechanism from the human, put to the worker to weigh.** Their words,
`verbatim`: *"I am not sure what the manager is saying with 'third alternative'. For the map, could we keep only
what is stricly nessesary for all agents and then have the subagents ask the manager that should already have
all the information loaded so it can answer question about the effort ? I am not sure it is a good idea since it
is using the manager more but can you look into it ?"*

So: `map.md` holds only the minimum every agent needs, and anything else a worker wants it **asks the manager
for**. They named their own doubt. **Q2 stands unanswered**; the worker was asked to weigh this and return
either with it as its recommendation or with its reasons against.

**The first sentence was a failure of the manager's relay, not a doubt about the option.** The manager wrote
*"third alternative"* without naming it. It means editing the single line `- `map.md` — the destination, the
standing preferences, the fog` that appears in each of the five worker contracts, and nothing else. Clarified to
the human in the same message.

**Five facts the manager gathered and verified, sent to the worker as evidence rather than as a conclusion.**

1. **The premise is partly true, and it is the strongest thing the proposal has.** The manager's window is
   billed at the cached-read rate, ~10% of standard input, while every worker pays its opening payload uncached.
   On token price alone, asking a warm manager beats a cold read.
2. **The premise is also partly false, and this is the manager disclosing about itself.** `map.md` records that
   the manager is *"compacted between nodes as standing procedure"*. After a compaction it holds a summary, not
   the map — attested directly: this session compacted, and the manager has re-read `map.md` and multiple node
   files many times since. So *"should already have all the information loaded"* does not hold in general, and
   the manager would often re-read the map to answer, paying that read in the resource node 24 found fails first.
3. **A worker that pauses to ask is exposed to a cold restart.** *"Subagents use the five-minute TTL even on a
   subscription."* So the cost of a question is the risk of re-paying the worker's whole conversation so far at
   full uncached rate — a cost that **scales with how much work it has already done, making late questions the
   expensive ones.** The manager's own turnaround this session has repeatedly exceeded five minutes.
4. **There is no existing channel for this, so it is new machinery.** A grilling worker's question and an
   implementation worker's raise both **relay to the human**; neither queries the manager's own knowledge. This
   would make the manager a **source** rather than a conduit, which is what [Subagent context
   contract](12-subagent-context-contract.md)'s scribe rule was written to prevent. Beside it: a `research` node
   has **no raise channel at all**, and workers are fully parallel today, so every worker waiting on a manager
   answer queues behind one single-threaded manager.
5. **The effort has already decided this exact fork once**, for the blind checker, which reads no map. The two
   candidates were *the manager decides per spawn what to hand over* and *the effort declares a block and the
   manager copies it verbatim, adding nothing*. The human chose the second at [What keeps the shipped files
   consistent when a decision changes a term](29-shipped-file-consistency.md) today, and struck the manager's
   proposed sixth ground rule **precisely because it was the manager authoring rather than copying.** Whether
   that precedent governs a worker's general access to the map, or is specific to a blind checker and a standard,
   was left to the worker to judge.

**One distinction the manager drew for the worker rather than deciding.** The worker had already set aside *"have
the manager render a per-node digest"* as not seriously offered. The human's proposal is adjacent and not
identical: a digest is manager-**pushed** per spawn; theirs is worker-**pulled** on demand. Those differ in who
decides what is needed and in when the cost is paid, so the worker was asked to say explicitly whether its
reasons against the digest reach the pull version too.

**Q3, from the worker** — still Q2's subject, re-asked after the human's fifth mechanism changed its
recommendation. Pasted as it wrote it, abridged to its `ASK`, `RECOMMENDED` and `ALTERNATIVES` plus the two
findings that changed the answer; its full text is in the relay transcript and its reasoning is reproduced
below in its own words.

**Half one of the human's proposal, adopted outright and credited:** *"'keep only what is strictly necessary for
all agents' — I am adopting outright, and your wording is better than mine. 'Strictly necessary for ALL agents'
is exactly the test the standard states and I had stated it loosely."*

**Half two, where it breaks — the manager has no privileged copy.** *"After a compaction it holds a summary, not
the map… So 'should already have all the information loaded' holds within one node's life and not across nodes.
Where it fails, the manager answers by re-reading the file. Which means the material has to be on disk for the
manager to answer from AT ALL — the manager cannot be the store, only a reader of it. And once it is on disk and
pointed at, a worker reading it directly is strictly cheaper than a worker asking the manager to read it and
relay it: one read, versus a read plus a relay plus a pause."*

**The resource distinction, sharpened.** *"The manager's window is billed at the cached rate (~10%) but is a
CAPACITY, and node 24 measured it as the thing that broke every single session at ~200k per node… Your proposal
is a good trade on money and moves load onto the capacity that has already broken, repeatedly."*

**The number that settled it, measured on itself.** *"I have read 207,843 characters, about 52,000 tokens. A
question I asked at this point that outlived the cache would re-pay ~52,000 tokens — more than TWICE the entire
22,300-token map read the proposal exists to avoid. And the exposure grows with how much work the worker has
already done, which is exactly when it knows enough to ask something worth asking. **Late questions, the good
ones, are the expensive ones.**"*

**On the node 29 precedent, judged rather than applied.** *"I judge it governs here, but only partly: the
objection was never 'the checker is blind', it was that the manager selecting is the manager authoring the
standard the work is judged against. A worker asking 'what does this effort require of me' gets the manager's
selection. That is the same defect at a different party. It does NOT govern plain facts — which node is open,
what node 31 decided — where relaying is conduit work. But the map's contents are overwhelmingly normative, so
the part of the precedent that governs is the part that matters."*

**Answering the push-versus-pull question explicitly, as asked.** *"'the manager becomes the author' DOES reach
it, but only where the manager answers by SUMMARISING — a manager answering with a pointer stays a conduit, so
that objection shapes the fix rather than killing the idea. 'It contradicts context-in-workers' does NOT reach
it, so long as the pull ends with the worker doing the reading. And three objections hit pull and not push: the
cache expiry, the serialisation, and the silent trigger. Pull is worse than push on availability and better on
authorship. **Neither is fatal in the way I implied last turn, and I was wrong to set the digest aside as not
seriously offered.**"*

**What the human's question found that the worker had missed**, in its words: *"My split has a real weakness:
the partition has to be RIGHT, and a bad one strands material a worker needed, silently, with no correction
mechanism. Your instinct went straight at that. The effort already has the pattern that fixes it — the
checker's `QUESTIONS:` part is explicitly NON-BLOCKING: 'You do not wait for an answer, and your outcome never
depends on one.'"*

```
ASK:           Do you take the synthesis below — your partition, the residual on disk rather than in
               the manager's head, and your pull idea in its non-blocking form?

RECOMMENDED:   Three parts.

               1. YOUR PARTITION, adopted as you stated it. `map.md` holds only what is strictly
                  necessary for all agents: the destination, the standing preferences, the
                  ground-rules block, the operational notes, the out-of-scope list, and each fog
                  item as its current statement naming the nodes that shaped it.

               2. THE RESIDUAL GOES TO A FILE, not to the manager. Every append the items currently
                  carry moves verbatim into a sibling file the map points at. Not because a file is
                  more elegant, but because the manager cannot be the store — it compacts between
                  nodes, so it would answer by reading this file anyway, and a worker reading it
                  directly skips the relay, the pause and the cache risk. Measured: a worker's map
                  read goes from ~22,300 tokens to ~6,200, about 72%, and it holds rather than
                  eroding because growth from here lands in the sibling.

               3. YOUR PULL IDEA, IN ITS NON-BLOCKING FORM — and this is the part I would not have
                  proposed without your question. A worker that needed something the map no longer
                  holds says so ON ITS HANDOVER, the way the checker's `QUESTIONS:` already works:
                  it never waits, its work never depends on an answer, and the manager promotes that
                  material back into the live section. So the partition does not have to be right on
                  day one. It becomes right by MEASURED DEMAND rather than by my guess — which is
                  the weakness you spotted, fixed with a pattern the effort already ships instead of
                  new machinery.

               Why this shape rather than yours as stated: it keeps every advantage you were reaching
               for — a minimal map, no need to partition perfectly in advance, the manager's
               knowledge put to use — and pays none of the four costs, because nothing blocks,
               nothing pauses, nothing queues behind you, and the manager relays a location rather
               than authoring a summary. Your stated doubt was right, and it was right for a sharper
               reason than "it uses the manager more": it uses the manager's CONTEXT, which is the
               one resource this effort has measured failing every session.

ALTERNATIVES:  - Your proposal as stated, blocking. I am setting it aside on the numbers above, not
                 on taste: the manager has no privileged copy after compaction, and one expired
                 question can cost more than twice the read it saves.
               - A blocking pull that the manager may only answer WITH A POINTER, never a summary.
                 This survives the authorship objection cleanly and is the strongest version of your
                 idea. I set it aside only because part 3 gets the same benefit with no pause at all
                 — but if you want a worker to be able to get unstuck mid-run rather than reporting
                 it afterwards, this is the one to take.
               - The narrow first step from last turn, still available and still cheap: change only
                 the one `map.md` line in each of the five contracts, so a worker reads `## Notes`
                 and `## Out of scope` always and a fog item only where its spawn names it. Five
                 one-line edits, no record risk, measured 56% rather than 72%, and it composes with
                 all of the above rather than competing.
               - Consolidate in place under a cap instead of moving to a sibling. Keeps the graph at
                 four files, but spreads the authoring risk across every future node rather than
                 doing it once.
```

**Disposed of by the worker rather than asked, and returning as a flag** — the manager's note that item 1's
premise fails for a resolved research node. Its ruling: *"the class does not want splitting. 'Cite, don't
restate' cannot apply — a research answer is original facts with sources, not a restatement of another node.
What applies is navigability, and it is already satisfied."* Verified by the manager: node 52's answer carries
**18** headings and node 54's **13**. The standing rule it takes instead: **a long answer is navigable by
heading.**

### The manager's notes on Q3, and the first is a structural problem the worker did not name

1. **Parts 1 and 2 cannot be an implementation node, and the worker calls them one.** Verified in the contracts
   it has read: the implementation contract's hard rule 1 is *"You write product code. You write no graph
   file."* and `graph-conventions.md` line 10 is *"The manager is the graph's only writer, and it writes as a
   scribe."* So **no worker may restructure `map.md`**, and the work falls to the manager — which has **no
   checker and no gate**, those being implementation-only, and which is **forbidden to author**, the scribe rule
   saying it pastes and never re-authors. So parts 1 and 2 as described sit in a hole: the party permitted to
   write the file may not write the text, and the party that could write the text may not touch the file.
   **There is a shape that fits and the effort already uses it**: a worker returns the restructured items as
   **text in a handover** and the manager pastes them — which is what every other node does, and what a
   `precondition` node is for, [What the manager reports to the human, in one
   place](46-what-the-manager-reports.md) being the standing example of one that *"decides nothing and writes no
   product code"*. Named as a fact rather than decided; how these parts land is the worker's to report.
2. **The non-blocking pattern part 3 leans on is verified and is the only one of its kind.** `QUESTIONS` appears
   in `expedition-checker/SKILL.md` **once** and in the five worker contracts **zero** times, and its
   non-blocking sentence is verbatim as quoted, at line 224. So part 3 is **new machinery in five contracts**,
   modelled on a shipped pattern rather than invented — a materially smaller claim than the *"new machinery in
   all six contracts"* the worker rightly charged against the **blocking** version.
3. **The manager's own view, since it is asked for as standing practice.** The synthesis is right and the
   manager was wrong to press its own ordering as *"first"* — the worker's part 3 answers the objection the
   narrow step was standing in for. What remains genuinely open is whether this lands as **one** piece of work
   or two, and the manager notes that all four candidate edits — the reading-list line, the new handover part,
   and both map changes — fall on the same five contracts plus one graph file, where flag `47.2` already priced
   contention for the exclusive code slot.

**A3, from the human**, `verbatim`: *"I think a research node should be able to raise when it can do nothing. Ok
for the recommandation. For the implementation spawn a implementation node to modify the files. The graph file
ban is because the manager should handle progress but here it is a work on the map itself, not just an update on
the map. The rule is more about only doing it's work and not updating when finished as it's the manager job."*

The option it points at, quoted from Q3's `RECOMMENDED`: the three-part synthesis — the human's own partition,
the residual moved verbatim to a sibling file rather than into the manager's head, and their pull idea in its
**non-blocking** form on the handover. **No divergence on the synthesis**; it is taken whole.

**And a ruling on the manager's structural objection, which overrules it.** The manager reported that parts 1
and 2 could not be an implementation node, the implementation contract's hard rule 1 being *"You write product
code. You write no graph file."* The human's reading: **the ban exists so that a worker does not do the
manager's progress bookkeeping, and it does not reach work whose subject *is* the map.** In their words: *"The
rule is more about only doing it's work and not updating when finished as it's the manager job."* So parts 1 and
2 **are** an implementation node, and the human asked for one to be spawned.

**That is a raise answered, so it yields two outputs and not one**, under [Whether a spawn may override a shipped
worker contract](28-spawn-overriding-a-contract.md)'s rule that the human's answer to a blocking raise gives a
licence for the one attempt, flagged, **and** a node for the permanent fix. The licence travels into the map
node's spawn as **the human's own words**, marked as theirs rather than as the manager's, per that node's fourth
spawn element. The permanent fix is [Qualify the graph-file ban in the worker
contracts](58-qualify-the-graph-file-ban.md) — because as written the rule is unqualified in five contracts, so
every future worker reads it broadly and this reading reaches nobody.

**The third sentence is a separate decision and not part of the synthesis.** *"I think a research node should be
able to raise when it can do nothing"* **reverses the human's own decision at [When an AFK worker cannot
proceed](23-worker-cannot-proceed.md)'s gate**, where they said *"I guess precondition could raise, as it is more
reseach that is supposed to be fully autonomous"* — extending the channel to `precondition` and naming
`research` as the kind meant to need nobody. That node records the exclusion as resting *"on the human's own
reasoning rather than on the glossary's"*. It is recorded as [Give a research node the cannot-proceed
raise](57-research-can-raise.md), and the reversal is annotated there and on node 23.

## Answer

Three questions, three answers, all taken as recommended with no divergence. Measurements were re-taken on this
node rather than carried over from [How an agent workflow and its skills reduce their own token
cost](52-token-cost-of-a-workflow.md), because `map.md` grew ~9,700 characters while the first question was with
the human — **the practice indicting itself inside one session.**

### A1. The density preference narrows by document class

The preference was settled at [Carry the recorded deltas into the shipped skill
files](26-carry-deltas-into-shipped-files.md)'s gate over **node files**, and has since been applied to two
other classes to discard findings — at [What the checker contract owes to having been
run](31-checker-contract-owes.md) a checker's finding that `unwrap` is spelled out at four sites was discarded
because *"the map endorses completeness for an agent reader over brevity"*, and that is a **shipped contract**;
and the fog item on never-delete applies it to `map.md`. **One preference stated over one class was governing
three.**

1. **Node files — stands verbatim.** *A node's reader is the next agent* is exactly true: one worker, claiming
   that node, needing it whole. Nothing is edited, and the two findings already discarded stay discarded.
2. **Shipped contracts — stands, on a different ground.** Not completeness but **fragility**: the compression
   penalty concentrates on **format-bearing instruction text**, which these contracts mostly are, and one
   measured study found compression past 30% failed **every** task in an agent scenario. So the boundary is
   **compress the prose that explains why, never the shapes** — under which leading-word refactoring is
   admissible where wholesale compression is not, a leading word replacing adjectives and sentences and never a
   shape.
3. **`map.md` — the preference does not reach it.** Its reader is not *the next agent* in the singular; it is
   every worker on every node, each needing a different fraction. That is sprawl in the standard's exact sense.

*"This is the preference applied consistently rather than overturned: it defends density by saying the reader
needs the material, which is true of a node file and false of a shared file each of whose readers needs a
different part."*

### A2. What a worker reads of `map.md`, and how the residual is reached

**Measured.** 89,214 characters, ~22,300 tokens, read in full by every worker, cold and uncached, once per node.
By section: fog **51,866** (58%), `## Notes` **33,210** (37%), out-of-scope 2,330, destination plus pointer
1,018. One fog item is **20,589 characters** — 23% of the file in one paragraph, larger than any file this
effort ships.

**What that material is.** Append history, most of it restating what a resolved node already holds. ~7,150
characters are the whole saga of one preference being recorded, obstructed twice, dissolved, renamed and landed,
whose live residue is a **202-character** ground rule sitting below it; 6,414 are the nine-deltas paragraph,
every delta discharged and saying so itself. **~65,500 characters — about 74% of what every worker reads — is
material a worker cannot act on.**

**The rule this effort already had.** `decisions.md` opens with *"A decision lives in exactly one place, its
node; this file never restates one."* `map.md` is the one graph file that restates its nodes rather than citing
them. And struck-through text is 2.1%, so **never-delete is not the cost** — live restatement is, and
never-delete exists to stop information being *lost*, which removing a restatement does not do.

**The human's own fifth mechanism, tested.** Their doubt was right and for a sharper reason than they gave.
**The manager has no privileged copy** — it is compacted between nodes, so the material must be on disk for it
to answer from **at all**: *"the manager can be a reader of the store, never the store."* **It spends the
resource that actually fails** — the manager's window is billed at ~10% but is a **capacity**, measured at ~200k
per node and named the thing that broke every session, while a worker's uncached read is **money**. **The pause
is the cost, not the question**: measured on this worker, which read **207,843 characters, ~52,000 tokens**, so a
question outliving the five-minute subagent TTL re-pays *"more than twice the entire 22,300-token map read the
proposal exists to avoid"* — and the exposure grows with work done, so **the late, well-informed questions are
the expensive ones.** Three smaller costs: it routes machine traffic into the one queue reserved for the scarce
human; it is new machinery, no such channel existing; and **the failure mode is silent** — a worker must know
that it does not know in order to ask.

**On node 29's precedent, judged rather than applied:** *"the objection there was never the checker is blind, it
was that the manager selecting is the manager authoring the standard the work is judged against. A worker asking
what does this effort require of me gets the manager's selection — the same defect at a different party."* It
does not govern plain facts, *"but the map's contents are overwhelmingly normative, so the governing part is the
part that matters."*

**Pull against push, stated explicitly, correcting its own earlier dismissal.** *The manager becomes the author*
reaches pull **only where the manager summarises**; answering with a pointer keeps it a conduit. *Contradicts
context-in-workers* does **not** reach pull, so long as the pull ends with the worker reading. Three objections
hit pull and not push: cache expiry, serialisation, silent trigger. *"Pull is worse than push on availability and
better on authorship; neither is fatal in the way the digest's dismissal implied."*

**What the human's question found that the recommendation had missed:** *"a partition has to be **right**, and a
bad one strands material a worker needed, silently, with no correction mechanism."* The effort already ships the
fix — `expedition-checker/SKILL.md`'s `QUESTIONS:` part is explicitly non-blocking, *"You do not wait for an
answer, and your outcome never depends on one"* — the one existing worker-to-manager channel that is not a relay
to the human. Verified: `QUESTIONS` appears **once** in the checker contract and **zero** times in the five
worker contracts.

**The decision, in three parts, taken whole.**

1. **`map.md` holds only what is strictly necessary for all agents** — the human's own wording, *"and sharper
   than the recommendation's"*: destination, standing preferences, ground-rules block, operational notes,
   out-of-scope list, and each fog item as its current statement naming the nodes that shaped it.
2. **The residual goes to a file, not to the manager.** Every append moves **verbatim** into a sibling
   `map.md` points at. Nothing is deleted, so no exception to never-delete and no per-append judgement — *"the
   same bulk verbatim move `decisions.md` was created by."*
3. **The pull idea, in its non-blocking form.** A worker that needed something the map no longer holds says so
   **on its handover**: never waiting, nothing depending on an answer, and the manager promotes that material
   back. **So the partition does not have to be right on day one — it becomes right by measured demand.**

**Expected: a worker's map read falls from ~22,300 tokens to at most ~8,000, a cut of at least 64% and likely
nearer 72%**, holding rather than eroding because growth lands in the sibling.

### A3. The graph-file ban does not reach work whose subject is the map

The human's ruling, `verbatim`: *"The graph file ban is because the manager should handle progress but here it is
a work on the map itself, not just an update on the map. The rule is more about only doing it's work and not
updating when finished as it's the manager job."* So the ban stops a worker doing the manager's **progress
bookkeeping** and does not reach work whose **subject** is a graph file. It is a departure from a shipped
contract, so it yields node 28's two outputs and always both: a **licence** travelling into the spawn as the
human's own words, and [Qualify the graph-file ban in the worker
contracts](58-qualify-the-graph-file-ban.md) for the permanent fix.

### Four standing rules of this effort

1. **Compress the prose that explains why; never compress the shapes.** Over every prose deliverable.
2. **An item states its current form and cites the nodes that shaped it; it does not restate what they hold.**
   `decisions.md`'s founding rule, now `map.md`'s too.
3. **A long answer is navigable by heading**, so a reader following a link for one fact reads one section.
4. **Cite a file by heading or by a quoted phrase, never by line number.** Append-in-place shifts every line
   below the append. Measured: node 52, four days old, cites `map.md:75` (now 88) and `map.md:51` (now 54) —
   *"both were already wrong before anything here was proposed."* A **correctness** finding, not a saving.

### What the manager's own skill inherits, from primary harness documentation

*Facts, not judgements.* **Compacting between nodes is cheap only inside the cache TTL** — one hour on a
subscription, five minutes once drawing on credits, `ENABLE_PROMPT_CACHING_1H=1` holding the hour — so the
standing practice is cheap **conditionally**. **`/rewind` is strictly cheaper than `/compact`** for abandoning a
path, and `/clear` costs nothing. **Cache scope is per machine and per directory, worktrees included**, so
`isolation: worktree` forfeits prefix sharing — *"a cost this effort has never priced and the one item here that
is actionable today."*

### What node 50 inherits, reported rather than decided

The 700 byte-identical words are ~1,015 tokens per spawn, paid once then cached, against ~19,840 tokens of map
— **~5% of one worker's opening read.** *"On token cost alone the duplication does not clear the bar for a remedy
that costs exact agreement, so the argument for changing it has to stand on maintenance rather than on tokens."*

### What this node did not decide, and where each went

- **Fork versus cheap model** is a **confirmation, not a decision**: you cannot have a cheap model and a warm
  cache on the same worker, and both the context-in-workers preference and the credit constraint point at the
  named subagent, *"which is what every worker already is — so the existing choice is now justified rather than
  assumed."* Mints nothing.
- **Homogenising a checker fan-out's prefix conditions** folded into the runtime node, not dropped.
- **The contracts' prohibition density** — 14.8 to 19.0 per 1,000 words against the standard's 6.2 — set aside
  with a reason: the standard exempts *"a hard guardrail you cannot phrase positively"*, which is what a hard
  rule is, and the **unpaired** cases already have owners in nodes 48 and 58. *"So the measurement is evidence
  those two workers should hold, and a systemic pass is warranted only if they find the pattern recurs."*
- **The always-loaded surface and tool-schema deferral** were settled by measurement upstream and absorbed none
  of the human's budget, as node 52 asked.
- **A research node's raise channel** is node 57's, *"though it is the same hole the non-blocking part above
  works around rather than closes."*

### Method skills, and what was left unrun

*"`/grilling` was run whole. `/domain-modeling` was run in part: its instructions to update `CONTEXT.md` inline
and to create ADR files were left unrun, against this contract's 'You write no file'. Its consumable half was
used, and earned its keep once — it is why the sibling file's name is barred from the word `provenance`, which
this effort's glossary refuses by name."*

## Flags

`53.1` `ASSUMPTION` — **It treated the shipped worker contracts as a third document class on its own
authority**, the preference naming node files only. Ground: the contracts are the only files that leave this
repo, and node 31's discard shows the preference was already being applied to them. *"Had the human read the
preference as covering exactly two classes, ruling 2 above would have no subject."*

`53.2` `ASSUMPTION` — **It settled the resolved-research-node case itself** rather than spending a question.
*"cite, don't restate cannot apply, a research answer being original facts with sources rather than a
restatement of another node, and what does apply — navigability — is already satisfied."* Turned into standing
rule 3.

`53.3` `ASSUMPTION` — **It made *cite by heading, never by line number* a standing rule without asking.**
Ground: *"this is a correctness finding rather than a saving… and the effort's own new instruction forbids
ranking a saving above a correctness finding, which would be an odd basis for leaving one unrecorded."*

`53.4` `ASSUMPTION` — **It folded the checker-fan-out prefix candidate into another node instead of minting
one**, the mechanism being documented for the dynamic-workflow runtime and *"documented neither way"* for the
`Agent`-tool spawns this effort uses, with the saving unmeasured.

`53.5` `ASSUMPTION` — **It read ruling 1's *the two discards stay discarded* as not barring the leading-word
work on the contracts**, one of those discards having been a leading-word finding against a **shipped contract**
whose governing ground ruling 2 changed in the same answer. *"Acting conservatively on that reading, it scoped
the refactor node to `scribe` alone and reported the `unwrap` half on `INVALIDATIONS` for the human to see."*

`53.6` `ASSUMPTION` — **It left part of `/domain-modeling` unrun** — the instructions to update `CONTEXT.md`
inline and create ADR files — against its contract's no-file rule. Recorded *"because that carve-out names
`/research`, `/grilling` and `/prototype` and the collision here was with a fourth skill."*

### Manager's note: six flags outstanding, on the ordering node 39 exposed

A grilling node's flags arrive **after** the last answer, so no answer here reached them. All six presented.
`53.1` and `53.5` are the load-bearing pair: `53.1` because ruling 2 has no subject if the human read the
preference as two classes, and `53.5` because it turns on how the human's *"discards stay discarded"* reads
against a discard that was itself about a contract.
