# Review every shipped file against `/writing-great-skills`

Type: research
Status: resolved

## Question

Eight files have shipped across five implementation nodes, written before this effort had any standard for
what makes a skill good. Hold every one of them against `/writing-great-skills` and report what it finds.

The human's instruction, `verbatim`: *"We should also maybe do a full review of what was already done with
/writing-great-skills, you should add a node for it (research ?) and run it in the background"*.

**Why `research` and not something else.** It reads a resource outside the working directory — the skill lives
in a plugin, not in this repo — and it produces **facts with sources**, not a decision and not code. It never
involves the human, and it writes nothing. Under [Concurrency model](04-concurrency-model.md) AFK research
*"may fan out freely"*, so it costs nothing against the interview slots or the code slot and can run beside
anything.

**This is the first research node in the effort, and it discharges a coverage criterion the map has been
holding.** [map.md](../map.md)'s fog records that no research node existed *"because every open question is a
design decision rather than an external fact"*, that the premise was retired by [Dogfood
target](09-dogfood-target.md), and that *"the first genuine research node arrives with the dogfood, and the
coverage criterion requires one to be run."* It arrives here instead, from the human's own steering, before
the dogfood — so the criterion is discharged on this effort rather than on Lang.

### What the manager measured before this node was claimed

*The manager's own note, facts rather than findings, so the worker spends no effort establishing them.*

**The eight shipped files, with sizes at claim time.** Product of nodes 21, 22, 26, 31, 35, 38 and 42:

| file | lines |
| --- | --- |
| `.claude/skills/expedition/graph-conventions.md` | 384 |
| `.claude/skills/expedition/wayfinder-divergences.md` | 52 |
| `.claude/skills/expedition-checker/SKILL.md` | 318 |
| `.claude/skills/expedition-implementation/SKILL.md` | 254 |
| `.claude/skills/expedition-precondition/SKILL.md` | 221 |
| `.claude/skills/expedition-prototype/SKILL.md` | 212 |
| `.claude/skills/expedition-grilling/SKILL.md` | 208 |
| `.claude/skills/expedition-research/SKILL.md` | 137 |

Adjacent and **not** a skill file: [`CONTEXT.md`](../../../CONTEXT.md) at the repo root, 285 lines, the
glossary the shipped files declare authoritative for their terms. In scope only where a finding about the skill
files reaches it.

**Every one of the six `SKILL.md` files is model-invoked, and none sets `disable-model-invocation`.** Verified
by grep across `.claude/skills/`: the string appears nowhere. Each carries a `description` of the same shape,
differing only in the node kind — *"The worker contract for an expedition `<kind>` node. Read it when a spawn
names it, and follow it exactly."* Every one of them is in fact reached by a spawn naming it.

**Large blocks are byte-identical across the five worker contracts, by deliberate choice rather than by
accident.** Flag `35.3` records it in that worker's own words: it *"wrote the two new sections byte-identical
in all five contracts, accepting a five-way edit and one restatement, to buy exact agreement across the
five."*

~~**`graph-conventions.md` is reached by pointer from the contracts rather than inlined**, and is the only
shipped file that is not a skill.~~

**False, and found false by this node's own worker.** The second half stands: it is the only shipped file that
is not a skill. The first half is wrong — it is reached by **no pointer from anywhere**.
`grep -rn "graph-conventions\|CONTEXT\.md\|wayfinder-divergences" .claude/skills/*/SKILL.md` returns nothing at
all, re-run by the manager and confirmed; the only file under `.claude/skills/` that names it is
`wayfinder-divergences.md`, which is the other unreachable one. The record already held the correct position
twice — [Write the worker contract skills](22-worker-contract-skills.md) at line 251, *"No file points at
another, at `CONTEXT.md`, or at `graph-conventions.md` for anything binding"*, and [A worker's handover carries
no acceptance condition for the node it mints](35-handover-mints-no-condition.md) at line 108, *"A worker never
reads `graph-conventions.md`, so a rule stated only there does not reach the party"* — so **no resolved node is
wrong and only this measurement was**, written by the manager from memory rather than from the grep it claimed.
The consequence for whoever reads this node: the two files under `.claude/skills/expedition/` are reachable by
no invocation and no pointer, and the only shipped-file pointers that exist are the four method-skill lines.

**Two files moved in the last two commits**, `ea63e1c` (the checker contract) and `d6eb665`
(`graph-conventions.md`).

### Standing instructions for this node's worker

- The facts above are the **manager's** and are measurements, not findings. Verify any you rely on.
- `/writing-great-skills` is **user-invoked** (`disable-model-invocation: true`), so you cannot invoke it and
  it will not appear in your skill list. **Read it as a file.** Find it rather than being given a path — the
  two copies on this machine sit under different nix store hashes. It lives in the `mattpocock-skills` plugin
  under `skills/productivity/writing-great-skills/`, and it discloses its full definitions to a `GLOSSARY.md`
  beside it, which is part of the skill and worth reading.
- Report findings as **facts with sources**, per your contract's rules 4 to 6: say what the skill states, and
  mark separately what you infer. A finding is *this file does X, the skill says Y, here is where each is
  written* — not a rewrite.
- **You write no file.** Where a finding needs a change to a shipped file, that is a `NEW NODES` entry, and
  where you report an implementation node you write its acceptance condition.
- Where a finding turns on a judgement only the human can make, report a `grilling` node rather than deciding
  it.
- The effort's own standing preferences are in `map.md` and some may **conflict** with the skill's advice. Say
  so where they do rather than ranking them silently: the map's *"the node files are written for agents… so
  completeness for an agent beats brevity for a human"* is the one most likely to collide with the skill's
  pruning and context-load principles, and that collision is a finding rather than an error.

## Answer

Eight shipped files held against `/writing-great-skills`, read as a file at
`skills/productivity/writing-great-skills/` in the `mattpocock-skills` plugin — `SKILL.md` (83 lines) plus
`GLOSSARY.md` (201 lines). The worker's own words on provenance: *"`diff -r` against the second copy under hash
`8xxmsy1r…` returns no differences, so the two are byte-identical and nothing here turns on which was read. Its
`disable-model-invocation: true` is at `SKILL.md:4`, and it is absent from this worker's own skill listing — the
map's claim about it is confirmed from both ends."*

The manager's measurements were checked: six `SKILL.md` files, eight shipped files, line counts all exactly as
stated, zero hits for `disable-model-invocation` anywhere under `.claude/`. One measured fact was **false** and
is corrected above, in the manager's note where it was written.

### Where the shipped files already meet the standard

- **Model-invocation is the only available choice and was chosen correctly.** `SKILL.md:16` and
  `GLOSSARY.md:27`: a user-invoked skill is reachable *"only by the human typing its name… no other skill can
  fire it."* The six contracts must be reached by a spawned agent, so stripping the description would make them
  unreachable. No change.
- **All-reference with no steps is explicitly blessed**, not a smell — `SKILL.md:35`, `GLOSSARY.md:79`
  (*"often a legitimately flat peer-set… a fine arrangement"*).
- **The exhaustiveness demand the standard asks of step-less reference is present and strong.**
  `GLOSSARY.md:139` names the *demand* axis as what binds flat reference; *"Five parts, every time. Write `none`
  in full for any part you have nothing for, and never leave a part off"* is exactly that, in all six.
- **The leading-word discipline was arrived at independently.** `GLOSSARY.md:131-133`; `CONTEXT.md`'s 50 terms
  with `_Avoid_` lines and each contract's `## Words used exactly` are the same lever.
- **No sediment.** Zero `~~` in any of the eight files. The never-delete rule is scoped to graph files only
  (`map.md:38`, `graph-conventions.md:15`), so `GLOSSARY.md:191`'s failure mode does not apply and the density
  question is purely about live text.
- **No drift in the duplicated vocabulary yet.** 17 distinct terms across the six `## Words used exactly`
  blocks; six (`manager`, `worker`, `node`, `flag`, `handover`, `resolve`) appear in five contracts each. Every
  multi-contract term is byte-identical after unwrapping. `manager`, `raise`, `acceptance condition` and
  `checker` differ between the checker contract and the rest, deliberately, given its blindness. **The cost flag
  `22.5` predicted has not been paid.**

### Where they do not

**1. Four method-skill pointers name targets whose text contradicts the pointing contract's own hard rules,
and only the checker carries a precedence rule.** Pointers at `expedition-research/SKILL.md:57`,
`expedition-grilling/SKILL.md:62`, `expedition-prototype/SKILL.md:63`,
`expedition-implementation/SKILL.md:93`. Holding each target against its contract:

- `/research` instructs *"Write the findings to a single Markdown file"* and *"Save it where the repo already
  keeps such notes."* The research contract's hard rule 1 is *"You write no file — no graph file, and no other
  file."*
- `/grilling` is written in the human's first person: *"Interview me relentlessly… put each one to me and wait
  for my answer. Do not act on it until I confirm."* The grilling contract's hard rule 2 is *"You have no
  human-facing tool. Do not call one."*
- `/domain-modeling` instructs *"When a term is resolved, update `CONTEXT.md` right there"* and to create
  `docs/adr/` files. The grilling contract's hard rule 3 forbids writing any file — and the file it would edit
  is the glossary this effort declares authoritative.
- `/prototype` instructs *"Locate the prototype code close to where it will actually be used"* and *"commit it
  to a throwaway branch."* The prototype contract's hard rule 1 confines everything built to
  `prototypes/NN-<name>/` and forbids the product tree.
- `/coding-principles` and `/naming`, named by the implementation contract, are **clean**: grepping both for
  file-write and human-facing instructions returns nothing.

`expedition-checker/SKILL.md:132` is the only file that resolves this: *"Where a skill's procedure and your
blindness conflict, blindness wins."* By `GLOSSARY.md:39`, a context pointer's *"wording, not the target,
decides when the agent reaches — and how reliably"*; **the worker's inference, marked as such:** four pointers
reach material that instructs the opposite of a hard rule, with nothing stating which governs, which is a
variance bug in the standard's own terms. **Demonstrated on this worker:** it declined to invoke `/research`
for exactly this reason and had no precedence rule to lean on. Flag `47.1`.

**2. The scan rules that make `graph-conventions.md`'s eight mechanical checks runnable are scattered, and
three are absent.** Present today: header-block fields (`:83`, `:282`), skip fenced blocks (`:283`),
`flags.md`'s first-link rule (`:67`), the `**· settled**` marker form (`:165`). Absent entirely: the **unwrap
rule** (`grep -ni "unwrap\|wraps\|reflow\|line break"` over the file returns nothing), `decisions.md` entry
identity, and `## Flags` entry line-anchoring. The consequence is measured, not predicted: `map.md` records
**twelve false results across seven sessions**, and names these exact gaps. `GLOSSARY.md:109` (Co-location) is
the lever — *"reading one part brings its neighbours with it"*. **The inversion is sharp: the unwrap rule is
stated four times in the checker contract (`:63`, `:92`, `:111`, `:304`) and zero times in the file whose
checks it protects.**

**3. Two bare prohibitions have no positive target beside them.** `SKILL.md:83` / `GLOSSARY.md:163`: keep a
prohibition *"only as a hard guardrail you can't phrase positively, and even then pair it with what to do
instead."* Most of the contracts' prohibitions are paired and earn their place. Two are not: *"You never
resolve your node, never mark it, and never create another one"* (grilling:57, precondition:55, prototype:58,
research:47; implementation:83 in short form) and *"You never create the node that would replace your own, and
you never split your own node"* (implementation:88). **Inference:** the first is also ambiguous against the
same file's `NEW NODES` handover part, which requires the worker to surface nodes; "create" alone does not
separate reporting from writing the file. *"`flags.md` is not yours. Leave it unread"* is the third such
sentence — already [Narrow the flags.md clause in the worker
contracts](32-narrow-flags-file-clause.md)'s, so its positive-pairing repair belongs there.

Measured density, for calibration rather than as a verdict: `never` per word — implementation 24/2469, research
14/1324, prototype 20/1989; against the plugin's own maximum of 7/2023 (`wayfinder`) and 1/1526 in
`writing-great-skills` itself.

**4. The six descriptions spend permanent context load on non-invocation text.** `SKILL.md:24`: *"Every word
increases context load, so a description earns even harder pruning than the body"*; `:26` front-load the
leading word; `:28` cut identity already in the body. All six read *"The worker contract for an expedition
`<kind>` node. Read it when a spawn names it, and follow it exactly."* — 19-20 words, well inside the plugin's
9-69 range. The trigger clause earns its place; *"and follow it exactly"* does invocation work nowhere, and the
discriminating word sits at position six or seven behind wording all six share. **Inference:** six
near-identical descriptions competing in one window is the misfire risk `GLOSSARY.md:63` names; not observed
here, and the fix is cheap either way.

**5. The density collision, stated as a collision rather than settled.** Byte-identical across all five worker
contracts: `## When you raise a flag` (21 lines, 276 words) and `## When a node you report is an implementation
node` (33 lines, 424 words) — 54 lines and 700 words per contract, verified by hash over both section ranges.
Four redundant copies are **216 lines and 2,800 words, 12% of the shipped corpus by line and 17% by word**
(8 files, 1,786 lines, 16,869 words). 53 non-blank lines per contract appear in all five. Add the vocabulary:
7 homes for 17 terms, 6 of them in five contracts each.

`SKILL.md:55`/`GLOSSARY.md:179` name this **Duplication**; `GLOSSARY.md:97` names its remedy, **External
Reference** — *"the home for shared reference that needn't fire on its own"* — which is precisely what
`graph-conventions.md` already is. Against that: `map.md:37` (*"completeness for an agent beats brevity for a
human, and the density of these files is correct rather than a failure of editing"*), flag `35.3`
(byte-identical *"to buy exact agreement across the five"*, its cost named as *"a five-way edit… in a set of
files nothing checks for divergence"*), flag `22.5`, and node 22's report that a code-review skill's smell
baseline **already flagged this duplication and suppressed it against condition 9** (`22-worker-contract-skills.md:924-927`).
Node 31 records a checker discarding a related finding because *"the map endorses completeness for an agent
reader over brevity"* (`:450`).

The one thing the record does not settle, and why this is a question rather than an answer: **the map's stated
hazard and the condition's mechanism are not the same width.** `map.md:49` asks for *"a worker contract that
stands alone as a file rather than depending on skill invocation"*; node 22's condition 9 hardened that to
*"everything binding on the worker is in the file, so a runner with no skill-invocation mechanism gets the same
instructions by reading it."* **A plain-file pointer is not skill invocation, and a skill-less runner can follow
one.** Sizing: `expedition-checker/SKILL.md` at 318 lines / 3,253 words is 2.3× the plugin's longest `SKILL.md`
by line and 1.6× by word; `graph-conventions.md` at 384 lines / 3,529 words exceeds the plugin's largest
disclosed reference. Open node 44 will add a seventh contract in the same shape, and open nodes 32, 40 and 41
each edit the same five.

**6. `graph-conventions.md:5` points at a glossary by bare filename, outside the skill tree.** *"Terms are used
exactly as the glossary (`CONTEXT.md`) defines them."* `CONTEXT.md` lives at the repo root, not under
`.claude/skills/`, so copying the skill tree to another repository carries the pointer and not its target.
**Inference:** it does not merely dangle — `/domain-modeling`, one of the skills the grilling contract itself
points at, creates a root `CONTEXT.md` as *that* repo's own domain glossary, so the pointer resolves to the
**wrong** file rather than to nothing.

### Manager's note: finding 6 was found twice, independently, on the same day

*The manager's own note, not part of the answer.* This worker reported finding 6 as a new grilling node, adding
*"the manager may prefer to fold this into"* [What keeps the shipped files consistent when a decision changes a
term](29-shipped-file-consistency.md). It is folded, and no node was minted for it — because **that node's
worker, running concurrently and reading a different set of files, reported the same defect down to the
`/domain-modeling` collision**, and put it to the human as part 1 of its own live question. Two blind agents
converging on one defect from different evidence is the strongest signal this effort has produced about it, so
it is recorded on node 29 rather than split across two nodes. What node 47 adds that node 29 did not hold: the
pointer's exact site at `graph-conventions.md:5`, and that **no `SKILL.md` points at `graph-conventions.md` at
all**, so the file carrying that pointer is itself unreached.

### Coverage criterion discharged

This is the effort's **first research node**, and `map.md`'s fog required one to be run. It arrived from the
human's steering before the dogfood rather than with it, so the criterion is discharged on this effort.

## Flags

Two, both `ASSUMPTION`. This node holds no round, so each entry carries its own account, per
`graph-conventions.md`'s rule for an AFK node with no round.

`47.1` `ASSUMPTION` **· settled** — **The worker declined to invoke `/research`, which its own contract's `## How you
research` instructs.** In its words: *"The only `/research` on this machine is defined as writing a Markdown
file to the repo, which my hard rule 1 forbids outright. With no precedence rule in the contract I applied the
checker contract's (`blindness wins`) by analogy and let the hard rule govern, then reported the collision as
finding 1. A research node has no raise channel, so a flag was the only outlet."*

`47.2` `ASSUMPTION` **· settled** — **The worker bundled three determined wording repairs into one implementation node rather
than three.** In its words: *"All three edit the same six contract files; the code slot is exclusive and four
open nodes already contend for it, so three nodes would mean three checks and three gates for edits totalling a
few dozen lines. Weighed against the map's per-node economics and node 41's own warning about nodes editing the
same five files."*

## Annotation: the standard this node was held against was superseded upstream, the same day

*Filed by the manager immediately after this node resolved, from the human's own instruction and then verified.*
The human's words, `verbatim`: *"Also, I did an update, /writing-great-skills was renamed/changed to
/writing-for-agents. We might want to spawn research node for the new one. (I don't know if you see the new
skill, maybe you need to reload skills ?)"*

**It is not a rename, and it has not reached this machine.** Measured rather than assumed:

- Both `mattpocock-skills` copies in this machine's nix store still hold `skills/productivity/writing-great-skills/`,
  and nothing named `writing-for-agents` exists anywhere under the nix store paths, `~/.claude/`, `~/dotfiles/`
  or this repo. **No skill reload would change that** — the plugin is a nix flake input, so the file simply is
  not on disk.
- The flake input `github:mattpocock/skills` is pinned in `~/dotfiles/flake.lock` at rev `2ab9580`. Upstream
  `HEAD` is `5b15a47`, and it holds `skills/productivity/writing-for-agents/` with `SKILL.md` **and**
  `SKILL-MECHANICS.md`.
- So the review above is against a **superseded standard**, and every one of its citations names a file that no
  longer exists upstream.

**What changed in the standard, read from upstream at rev `5b15a47`.** The shape of the change matters more than
its size, because it lands on this node's findings unevenly:

- **The scope widened past skills.** It is now *"Reference for writing any document an agent consumes: a skill,
  an `AGENTS.md` / `CLAUDE.md`, a doc reached by a pointer"* — where the old one opened *"A skill exists to
  wrangle determinism out of a stochastic system."*
- **`disable-model-invocation: true` is gone.** The new standard is **model-invoked**, with the description
  *"Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md."*
  That reverses the fact this node's own standing instructions were written around, and reverses the second
  finding recorded in `map.md`'s note on the skill: once installed it **will** appear in a worker's skill list
  and can be invoked rather than read as a file.
- **`GLOSSARY.md` (201 lines) is gone**, replaced by `SKILL-MECHANICS.md` (22 lines), with the definitions
  folded into `SKILL.md` and the invocation material moved out to the mechanics file. Every `GLOSSARY.md:NN`
  citation in the answer above is now unresolvable.
- ~~**Two concepts are new and both bear directly on this effort's open questions.** *The two loads* is now its
  own section naming **context load** and **cognitive load** as two budgets every document spends. And
  **sprawl** is named as a failure mode in its own right — *"a document simply too long, even when every line is
  live and unique. Attention thins across the excess"* — which is a different charge from `Duplication`, and it
  is the charge finding 5 above would now have to answer.~~
- ~~**One sentence directly contradicts the framing of finding 5.** Progressive disclosure is now *"Not primarily
  a token optimisation: it is how the hierarchy is protected."*~~

**Both of those two bullets are false, and [Re-review the shipped files against
`/writing-for-agents`](54-review-against-writing-for-agents.md)'s worker falsified them by reading the old text
the manager never opened.** They were written from a partial diff and from the new file alone. Recorded here
rather than deleted, and the surviving claims above are unaffected.

**Neither concept is new.** Both loads were named terms in the old standard — `GLOSSARY.md:43` `### Context
Load` and `:49` `### Cognitive Load` — old `SKILL.md:11` opened on *"Two choices, trading different costs"*, and
`:48` used the phrase *"the two loads"*. **Sprawl** was a named failure mode twice over, at old `SKILL.md:81`
and old `GLOSSARY.md:113`, the latter already stating it *"Distinct from **sediment** (length from stale
accumulation) and **duplication** (length from repeated meaning) — sprawl is length itself, whatever its
cause."* What changed is **prominence** — both moved from a disclosed glossary into the main body — not
existence. The practical claim survives: finding 5 must answer sprawl. The reason given for it does not.

**The sentence said to contradict finding 5 was in the old text, in a file finding 5 cited.** Old
`GLOSSARY.md:103`: *"Not primarily a token optimisation; it is how the **information hierarchy** is protected."*
A colon for a semicolon. **So it contradicted finding 5's framing at the moment finding 5 was written, and the
rewrite changed nothing about it** — which makes it a finding against node 47's own worker rather than against
the rewrite.

**The general lesson, and it is the manager's.** All **four** places this annotation named as *"where the new
text is known to bite"* — negation, sprawl, the leading-word hunt, and the shared-reference home — were in the
old text; the leading-word instruction differs by **one word**, `skill` → `document`, and the shared-reference
sentence is **verbatim**. The manager read the new file and a partial diff and never opened the old
`GLOSSARY.md`, which was on disk the whole time. **A delta stated without reading both sides is not a delta.**
Those four claims travelled into node 54's spawn as manager pointers; that worker was told to treat manager
material as evidence rather than argument, checked all four, and returned them falsified — which is the spawn
rule working rather than failing.

**What survives and what does not.** The half of every finding that measures *this effort's files* stands
untouched — the line counts, the byte-identical sections, the four method-skill pointers and their conflicts,
the absent scan rules, the `graph-conventions.md:5` pointer. What is superseded is the half that cites the
standard. Findings 1, 2 and 6 rest on levers that survive the rewrite in substance (context pointers,
co-location, hard-rule conflict) and their citations need re-siting. Findings 3, 4 and 5 rest on text that moved
or changed, finding 5 most of all. Re-held against the new standard by [Re-review the shipped files against
`/writing-for-agents`](54-review-against-writing-for-agents.md).

## Annotation: flag `47.1`'s complaint has been answered by the human

*Filed by the manager.* Flag `47.1` recorded this node's worker declining its contract's `/research` pointer and
noting, as the reason a flag was all it could do: *"A research node has no raise channel, so a flag was the only
outlet."*

**The human has now granted the channel**, in their words: *"I think a research node should be able to raise when
it can do nothing."* That is [Give a research node the cannot-proceed raise](57-research-can-raise.md), and it
**reverses their own decision** at [When an AFK worker cannot proceed](23-worker-cannot-proceed.md)'s gate rather
than filling a gap nobody had considered.

So this worker's flag did the thing a flag is for: it recorded a constraint the worker could not act on, and the
constraint was changed. It is also the reason the change happened at all — the second research worker, at
[Re-review the shipped files against `/writing-for-agents`](54-review-against-writing-for-agents.md), hit the
identical blocker and reported it identically, and two instances in one session is what made the case.

**The conflict itself was fixed separately and first**, by [Reconcile a method skill's instructions with the
contract's hard rules](48-method-skill-conflicts-hard-rules.md), landed as commit `915d45a`. So a research
worker meeting that same collision today has an action stated in its contract — leave the conflicting part
unrun, run the rest, report which part and why — and after node 57 will also have a channel for the case where
no action is available at all. Finding 1 of this node is discharged twice over.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
