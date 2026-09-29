# Re-review the shipped files against `/writing-for-agents`

Type: research
Status: resolved

## Question

The standard the shipped files were just reviewed against was renamed and rewritten upstream on the same day.
Hold the shipped files against the **new** text, and report what the previous review's findings gain, lose, or
keep.

The human's instruction, `verbatim`: *"Also, I did an update, /writing-great-skills was renamed/changed to
/writing-for-agents. We might want to spawn research node for the new one. (I don't know if you see the new
skill, maybe you need to reload skills ?)"*

### What the manager measured before minting this, so the worker does not re-derive it

*Facts, not findings. Verify any you rely on.*

- **The new skill is not on this machine.** Both `mattpocock-skills` copies in the nix store still hold
  `skills/productivity/writing-great-skills/`; nothing named `writing-for-agents` exists under the nix store
  paths, `~/.claude/`, `~/dotfiles/` or this repo. The flake input `github:mattpocock/skills` is pinned in
  `~/dotfiles/flake.lock` at rev `2ab9580`; upstream `HEAD` is `5b15a47`. **No skill reload changes that** — the
  file is not on disk.
- **Read it from upstream at a pinned rev** unless it has landed locally by the time you run. Path in the repo:
  `skills/productivity/writing-for-agents/`, holding `SKILL.md` (81 lines) and `SKILL-MECHANICS.md` (22 lines).
  If a local copy exists by then, **prefer it and say which you read**, since that is the text an installed
  worker would get.
- **It is not a rename.** `disable-model-invocation` is **gone**, so the new skill is model-invoked and will
  appear in a worker's skill list once installed. `GLOSSARY.md` (201 lines) is gone, replaced by
  `SKILL-MECHANICS.md` (22 lines) holding only frontmatter, the invocation choice and router skills; the
  definitions folded into `SKILL.md`. Scope widened from skills to *"any document an agent consumes"*.
- **The previous review is [Review every shipped file against
  `/writing-great-skills`](47-review-shipped-skills.md)**, resolved, with six findings against the standard and
  six places the files already met it, plus an annotation recording exactly this supersession. Its measurements
  of *this effort's files* — line counts, byte-identical section ranges, the four method-skill pointers, the
  absent scan rules, the `graph-conventions.md:5` pointer — were verified and stand; what needs re-siting is the
  half of each finding that cites the standard.

### Standing instructions for this node's worker

- **This is a delta review, not a review from scratch.** For each of node 47's twelve items say which of:
  *stands as written*, *stands on different grounds in the new text* (give them), *weakened or reversed*, or
  *superseded outright*. Then report what the new text finds that the old one could not.
- **Four places the new text is known to bite, and they are the manager's pointers rather than findings.**
  **Negation** is now a named failure mode with a mechanism — *"steering by prohibition drags the forbidden
  behaviour into context and makes it more available, not less"* — against measured `never` densities of 24/2469
  words in the implementation contract, 20/1989 in prototype, 14/1324 in research. **Sprawl** is a charge
  distinct from duplication. **Leading words** are named a compression lever with an instruction to go hunting:
  *"Assume every document is carrying restatements that leading words retire."* And `SKILL-MECHANICS.md` offers
  an option the old text did not: *"A model-invoked skill whose content is all reference is also one home for
  shared reference: another skill can invoke it."*
- **Two of this effort's own facts make that last one live**: `.claude/skills/expedition/graph-conventions.md`
  is a shipped file that is **not** a skill and is reached by **no pointer from anywhere** — verified, `grep -rn
  "graph-conventions\|CONTEXT\.md\|wayfinder-divergences" .claude/skills/*/SKILL.md` returns nothing — and the
  five worker contracts hold 216 lines of byte-identical duplication that a shared-reference home would absorb.
  Report what the new text implies here; **do not decide it**, it is [Whether the five contracts' shared blocks
  stay duplicated](50-shared-blocks-stay-duplicated.md)'s, which is blocked on you.
- **You write no file.** A finding needing a shipped-file change is a `NEW NODES` entry, with an acceptance
  condition where it is an implementation node. A finding turning on a judgement only the human can make is a
  `grilling` node.
- **Say where the effort's standing preferences conflict with the new text rather than ranking them silently.**
  `map.md`'s *"completeness for an agent beats brevity for a human"* is the one that collides hardest, and under
  the new text it collides with **sprawl** rather than with duplication. That collision is a finding, and its
  resolution is [What the token findings change in the workflow and its
  skills](53-what-token-findings-change.md)'s.

**Blockers: none.** It reads an outside source and writes nothing.

## Answer

Read from **upstream** at rev `5b15a47f2d7150f545fbcacbfe381787fc0230dc` — `SKILL.md` (81 lines, 1,777 words)
and `SKILL-MECHANICS.md` (22 lines, 414 words). **No local copy exists**, confirmed from both ends. The old text
is still on disk at the `8xxmsy1r…` store path — `SKILL.md` (83 lines, 1,526 words), `GLOSSARY.md` (201 lines,
2,939 words) — **and reading both is what makes this a delta review rather than a fresh one.**

### The finding that reshapes the rest: the four places the new text was expected to bite were all in the old text

*Facts. Each is a line-for-line comparison of the two files named. All four were the manager's pointers, and all
four were wrong.*

- **Negation.** New `SKILL.md:74`. Old `SKILL.md:83` **and** old `GLOSSARY.md:161`, a full entry with the same
  elephant mechanism and the same closing rule. The new text **compresses** it: old `GLOSSARY.md:161`'s *"Its
  leading word is the elephant: whatever a prohibition names into the frame"* is gone.
- **Sprawl distinct from duplication.** New `SKILL.md:43`. Old `SKILL.md:81` as a bullet and old
  `GLOSSARY.md:113` as a full entry already stating the distinction outright — *"Distinct from **sediment**
  (length from stale accumulation) and **duplication** (length from repeated meaning) — sprawl is length itself,
  whatever its cause."*
- **The leading-word hunting instruction.** New `SKILL.md:72` against old `SKILL.md:72`. **One word changed**,
  `skill` → `document`.
- **A model-invoked all-reference skill as a home for shared reference.** New `SKILL-MECHANICS.md:9`. Old
  `GLOSSARY.md:21`, **verbatim**.

**The worker's inference, marked as such:** *"the rewrite is a repackaging plus a scope widening, not a new set
of levers. Almost every lever node 47 used survives; what moved is where each sits on the hierarchy — the old
text disclosed its definitions to a 201-line glossary and kept `SKILL.md` to 83 lines, and the new text folds
the definitions into an 81-line body and discloses only the skill-specific mechanics to 22 lines."*

### What is genuinely new, and it is short

1. **Scope.** New `SKILL.md:6`: *"Reference for writing any document an agent consumes: a skill, an `AGENTS.md` /
   `CLAUDE.md`, a doc reached by a pointer."* Consequence: `graph-conventions.md`, `wayfinder-divergences.md`
   and `CONTEXT.md` were in node 47's scope only *"where a finding about the skill files reaches it"*. They are
   now first-class subjects — **and so are `map.md`, `decisions.md` and every node file.**
2. **The no-pointer accounting sentence.** New `SKILL.md:27`: *"Material reached only through a pointer escapes
   context load at the price of the pointer's own line; material with no pointer at all rides entirely on
   cognitive load."* Nothing equivalent in the old text, whose two load entries define the budgets and never
   state the accounting between them. **The sharpest new sentence for this effort.**
3. **The environment as a source of truth, and a restating document as a cache.** New `SKILL.md:79`. Zero
   occurrences of `cache`, `environment`, `package.json` or `--help` anywhere in the old text.
4. **The pointer rules now bind any always-loaded pointer**, not just a skill description — new `SKILL.md:12`,
   where the old rules lived under `## Writing the description`.

**What is lost.** `Predictability` as the named root virtue (5 hits in old `GLOSSARY.md`, 3 in old `SKILL.md`;
the new text says *"predictable"* once). `Granularity` as a term, with its window-crowding clause.
`External Reference` as a named term. `Legwork`, `Post-completion steps` and `Premature completion` as separate
entries. And **the whole `_Avoid_` apparatus — 28 `_Avoid_` lines in old `GLOSSARY.md`, zero in the new text.**

### Verdict on node 47's twelve

**Ten stand, one narrows, one sub-claim loses its citation.** The six it found already met:

| # | item | verdict |
| --- | --- | --- |
| A1 | model-invocation chosen correctly | **stands as written.** Re-sited to `SKILL-MECHANICS.md:10`, `:12`. |
| A2 | all-reference with no steps is blessed | **stands on different grounds.** Blessing survives at `SKILL.md:34`, but `:39` attaches a clause the old blessing lacked — *"When a document has steps, in-file reference that should be disclosed buries them and turns attending to them into a coin-flip: a variance lever, not just a legibility one."* **The contracts are mixed, not all-reference** — `## How you grill`, `## How you implement`, `## After the code is written` and the checker's re-check procedure are steps. So the clause is live where the old blessing covered the files whole. |
| A3 | the exhaustiveness demand is present and strong | **stands as written.** Re-sited to `SKILL.md:50`, `:52`. *"Five parts, every time"* is both checkable and exhaustive, which `:52` names the strongest form. |
| A4 | the leading-word discipline was arrived at independently | **stands as a claim about the vocabulary, and is overtaken by a finding it missed.** Node 47 credited the practice and never ran `:72`'s instruction. Running it finds the effort's best leading word **unused** — below. Two supports also weaken: the `_Avoid_` device it cited as the same lever is no longer modelled at all, and `:63`'s *"a made-up word recruits no priors"* is a test it did not apply. Of `CONTEXT.md`'s 50 terms most are pretrained (`fog`, `frontier`, `gate`, `bar`, `sweep`, `cascade`, `salvage`, `park`, `raise`, `scribe`); `code slot` and `banked answer` are the coined ones. |
| A5 | no sediment | **stands as written.** Re-measured: zero `~~` in all eight files. |
| A6 | no drift in the duplicated vocabulary yet | **stands on narrower grounds.** Re-measured: 17 distinct terms, **53 definition instances** (checker 6, grilling 9, implementation 13, precondition 9, prototype 10, research 6). Still no divergence beyond the deliberate checker ones. But `:78`'s new parenthesis — *"(The accidental inverse of a leading word, which repeats a token on purpose, never the meaning.)"* — makes repeating the **meaning** the failure, and 53 instances for 17 meanings is that. So *"the cost flag `22.5` predicted has not been paid"* is true of drift and **false of the two costs `:78` names**, maintenance and inflated prominence, which are being paid now. |

The six it found they did not meet:

| # | item | verdict |
| --- | --- | --- |
| B1 | four method-skill pointers contradict the pointing contract's hard rules | **stands, strengthened.** New `SKILL.md:12` carries the **remedy order** the old pointer entry lacked — *"sharpen the wording first, and inline the material only if sharpening fails"* — and `:6`/`:12` widen the pointer concept past descriptions, so the rule binds a pointer whatever it names. Re-verified on disk. **Demonstrated on this worker for the second consecutive time.** Node 48's. |
| B2 | the scan rules are scattered and three absent | **stands, strengthened, and its measurement has moved.** Co-location survives near-verbatim at `SKILL.md:41`. Second lever the old text did not supply: `:63`'s *"Repeated as a token, never as a sentence"* makes the inversion a **leading-word** failure too — `unwrap` is stated as a sentence at four sites in the checker contract and appears in no other shipped file. **And `graph-conventions.md` is now 402 lines with nine checks, not 384 with eight.** The ninth ships **with** its anchoring rules inline, *"so prose that mentions the words names no part at all"* — so the file's newest check carries exactly the discipline the older eight lack, which is evidence the gap is known locally and unrepaired globally. Node 49's, **whose condition cites the eight.** |
| B3 | two bare prohibitions have no positive beside them | **stands, widened.** Re-sited to `SKILL.md:74` and **promoted on the hierarchy** — body, where the old text had a bullet plus a disclosed entry. Widened because node 47 calibrated on the bare word `never`, which made the checker contract look clean at 9/3,253. Measuring **prohibitions** (`never`, `do not`, `does not`, `may not`, `cannot`, `must not`) per 1,000 words: implementation **19.0**, prototype **17.6**, research **17.4**, checker **15.7**, grilling **15.4**, precondition **14.8**, `graph-conventions.md` **11.5** — against the new standard's own **6.2** and `/wayfinder`'s **4.4**. **Every contract runs 2.4× to 4.3× the standard it is held against, and the checker contract is not the outlier the `never` count implied.** |
| B4 | the six descriptions spend context load on non-invocation text | **stands on its three main grounds; one sub-claim superseded outright.** Re-verified: all six 18–19 words against the plugin's 9–69 range over 41 skills; the discriminating word at position 6 in every one; `:18`'s *"Cut identity the body already carries"* bites exactly, each description opening *"The worker contract for an expedition `<kind>` node"* against a body whose H1 is `# Research worker contract`. *"and follow it exactly"* also falls to `:81`'s no-op test. **Superseded:** node 47's window-crowding claim cited `GLOSSARY.md:63` = `Granularity`, **gone from the new text entirely**, and the new `## When to split` keeps only the two cuts with no such clause. That sub-claim now has no citation. |
| B5 | the density collision | **stands, the charge sheet grows by one, and the reversal node 47's annotation announced was never a change.** Re-measured for node 50: byte-identical by md5 across all five contracts, **216 lines and 2,800 words** in four redundant copies; corpus now **8 files, 1,804 lines, 17,067 words**, so **12.0% by line and 16.4% by word**. Sizing against the new standard: `expedition-checker/SKILL.md` 3.9× its `SKILL.md` by line and 1.8× by word; `graph-conventions.md` **5.0× and 2.1×**, and 1.9× / 3.0× the plugin's largest disclosed reference. |
| B6 | `graph-conventions.md:5` points at a glossary by bare filename | **stands, and gains a citation it did not have.** Under the old text pointers were a description concept and this rested on inference; new `:12` makes the bare `CONTEXT.md` a **context pointer** by the standard's own definition. Node 29's. |

### What the new text finds that the old could not

**A. A quarter of the shipped corpus is read by nobody, and the standard now prices it.** Re-verified: no
shipped skill points at any of the three non-skill files, **and `.claude/skills/expedition/` holds no `SKILL.md`
at all** — so it is a skill directory containing no skill, and neither file in it can be invoked or reached.
New `SKILL.md:27` prices that exactly: *material with no pointer at all rides entirely on cognitive load.*
**454 lines and 4,057 words — 25% by line, 24% by word — ride entirely on the human remembering the files
exist.** The worker's inference, marked as such: `map.md:37` has already settled that the human's two interfaces
are the manager's chat and the diff, so **the human is not the index for a file inside the skill tree**, and
`:25`'s *"the human is the index"* has no holder here. The old text could not make this argument.

**B. The leading-word hunt, run — and the effort's best token is unused.** `scribe` **appears exactly once** in
the shipped tree, at `graph-conventions.md:10`, which is the file no worker reads and nothing points at. The
concept is then spelled out **as a sentence at ten sites** across the five contracts — the opener in each
(*"the manager, which passes it along unaltered and answers nothing itself"*, at `:12` in four of them) and the
handover paragraph in each (*"The manager writes every part of this onto the graph unaltered"*) — plus twice in
`CONTEXT.md`. **A pretrained one-word token for the manager's entire discipline exists, is correct, and reaches
no worker.** Two more of the same shape: `unwrap` restated four times in the checker contract, and the
four-clause self-contained-condition test spelled out at **six** sites — 33 identical lines in each of five
contracts plus `graph-conventions.md:117-150` — against `:67`'s worked example, *"A triad spelled out at three
sites… begging to collapse into a single token."*

**C. The cache lever, and it cuts both ways.** Where the files **meet** it, deliberately: the bar is written as
properties with commands discovered per repo, which is `:79`'s *"Leave the one-file, one-command lookups to the
environment, where they cannot go stale"* exactly, and `map.md` reached that independently. Where it
**collides**: the 53 definition instances are a cache of a one-file lookup, `CONTEXT.md`, which `:79` says does
not earn its load — against `map.md:51`'s *"a worker contract that stands alone as a file"*, hardened by node
22's condition 9. Stated as a collision, not ranked.

### For node 50, not decided here

The new text names **two** homes for the 216 duplicated lines, **and neither is new** — both were in the old
text, one verbatim. A model-invoked all-reference skill another skill invokes (`SKILL-MECHANICS.md:9`, costing
one always-loaded description), or a plain file outside the skill system any document points at
(`SKILL-MECHANICS.md:14`, `SKILL.md:35`). The worker's inference: *"`graph-conventions.md` is already the second
shape and is missing only the pointer, so that route costs one line per contract and no context load. The first
route makes the material firable but reachable only by invocation, which is what `map.md:51` insures against."*
Also relevant: `:43`'s cure for sprawl is *"the ladder"* rather than deduplication.

### The standing-preference collision, for node 53

`map.md:37`'s *"completeness for an agent beats brevity for a human"* collides with **sprawl** rather than with
duplication, **head-on**: *"the preference concedes length and defends it by completeness, while sprawl's whole
content is that completeness is no defence, because the cost is **attention** rather than staleness or
repetition."* Two things sharpen it past node 47's version. `:6`'s scope widening **puts the preference's own
subject inside the standard** — the preference is about node files, which the old standard did not reach.
And **on the two unreachable files the preference and the standard agree**: `map.md:37` says the human works
from the chat and the diff, `:27` says unpointed material rides on cognitive load, `:25` says the human is the
index — so nobody is reading `graph-conventions.md`, and that is an argument the old text could not make.

## Flags

`54.1` `ASSUMPTION` **· settled** — **It read the upstream standard by downloading it into `$TMPDIR`**, outside the repo and
outside the graph, judging that hard rule 1's *"no other file"* governs artifacts rather than the mechanics of
reading a remote source. In its words: *"rule 1's neighbours — no graph file, the manager as the graph's only
writer — are all about what a worker produces, and the alternative reading forbids a research node from reading
any remote source at all, which is the one thing this node kind exists for."* **And it is a finding about the
contract, not only about its own conduct:** `You write no file — no graph file, and no other file.` is itself a
bare prohibition with no positive beside it, the positive sitting ~30 lines away in the handover mechanism —
the same defect node 48's clause 2 repairs for two other sentences, **and that clause names exactly two, not
this one.**

`54.2` `ASSUMPTION` **· settled** — **It declined to mint nodes for the two shipped-file findings with no existing home**,
routing the leading-word refactor to node 53 and the bare-prohibition finding to node 48's clause 2. Its
reasons: whether to spend edits on a leading-word refactor is exactly node 53's judgement; its largest instance
sits inside the blocks node 50 is deciding; flag `47.2` already priced multiple nodes contending for the same
five files; and *"widening an open unclaimed node's condition is not mine, so I state it rather than do it."*

## Manager's note on flag 54.2, filed against the manager's own interest

*Not a change to the answer.* **One of that flag's four reasons is factually wrong, and it matters for node 53.**
`scribe`'s ten sites are the contracts' **openers** and **handover paragraphs** — not `## When you raise a flag`
and not `## When a node you report is an implementation node`, which are the two byte-identical blocks node 50 is
deciding the fate of. So the `scribe` refactor is **not** blocked by node 50; only the six-site condition test
partly overlaps. The routing to node 53 still stands on its other three reasons.

The bare-prohibition finding on hard rule 1 is **currently owned by nobody**: node 48's condition names two
sentences, node 32 owns the third, and this is a fourth. The manager is **not** widening node 48's condition —
that is the act node 33 forbids and node 39 is deciding — so it is recorded here and named in the report as one
line for the human rather than repaired silently.

## Annotation: the skill landed locally while this node was being filed, and the review needs no re-run

*Filed by the manager, verified rather than assumed.* The human rebuilt: `/writing-for-agents` is now on disk at
a **third** store path, `w0svxj9j…`, and `writing-great-skills` is **gone** from that path. `~/dotfiles/flake.lock`
now pins `github:mattpocock/skills` at **`5b15a47f2d7150f545fbcacbfe381787fc0230dc`** — the exact rev this
node's worker read from upstream.

**`diff` against upstream at that rev returns `IDENTICAL` for both `SKILL.md` and `SKILL-MECHANICS.md`.** So the
worker's flag-free choice to read upstream was sound, every citation in the answer above resolves against the
local file, and **nothing in this node needs re-running.** The one thing its answer said it could not settle —
whether to prefer a local copy — is settled by the copies being the same bytes.

**Three consequences that outlive this node.**

1. **`disable-model-invocation` is genuinely gone**, confirmed on the local file's frontmatter. So the skill is
   **model-invoked** and will appear in a worker's and a checker's skill list — which retires, in fact rather
   than in prospect, the invocation obstruction `map.md` recorded and both of the workarounds it reasoned
   through. An agent can now **fire** it rather than being handed it as text or a path.
2. **A session already running does not see it.** The skill registry is loaded per process against a store path
   that changed, so this manager thread and any worker spawned from it still hold the pre-rebuild registry. Any
   worker that must *invoke* rather than *read* the new standard has to be spawned from a session started after
   the rebuild. Recorded because it is exactly the class of stale-mid-session fact [What the checker contract
   owes to having been run](31-checker-contract-owes.md) was written about, arriving from the other direction:
   there a mid-session **file** edit did reach a freshly-spawned worker, and here a mid-session **plugin** change
   does not.
3. **The store path is machine-specific and changed twice today**, which is the map's own *prefer properties
   that are discovered over commands that are declared* earning its keep for the third time on this one skill.
   Nothing should ever carry that path.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
