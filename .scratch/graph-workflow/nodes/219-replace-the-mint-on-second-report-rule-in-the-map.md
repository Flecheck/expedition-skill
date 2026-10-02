# Replace the mint-on-second-report rule in the map's retrospective item

Type: implementation
Status: claimed

Blocked by: none

## Question

*Surfaced by [The rule that mints a node on a repeated retrospective item has been defeated by its own
test](212-the-mint-on-second-report-rule-is-defeated.md)'s worker, and pasted as it wrote it.*

> The map's retrospective bullet carries three statements this node replaces: that the worker's
>            retrospective names no standing item, that the manager mints a node on the second report of the same
>            standing item, and that the retrospective is filed as an annotation after the node resolves. All
>            three are one bullet and one coherent statement, so they are one edit rather than three — three
>            nodes editing one bullet is node 115's two-writers collision. Nothing ships: the retrospective
>            appears in no file under `.claude/`.

**Blockers, in the worker's words:** none

## Acceptance condition

*Written by node 212's worker. Pasted as it wrote it, and not the manager's.*

> The work is edits to two files, `.scratch/graph-workflow/map.md` and `.scratch/graph-workflow/map-history.md`.
> Nothing else changes.
>
> Done means every one of the following is true of the finished tree.
>
> 1. In `.scratch/graph-workflow/map.md`, under `## Notes`, the bullet beginning **"Every worker returns a
>    retrospective as the last handover part, on this effort only"** states all four of the following, and every
>    statement that bullet previously carried which contradicts them is no longer in it:
>
>    (a) **The worker names the item.** For each standing item its retrospective reports, the worker gives that
>        item a short name; it reuses a name an earlier retrospective already carries where one fits and mints a
>        new one where none does; and it states how many earlier retrospectives carry that name, listing the node
>        ids. The bullet says the worker finds the existing names by searching the retrospective sections of the
>        files under `.scratch/graph-workflow/nodes/`, and not from memory or from any list held elsewhere.
>
>    (b) **The word is "name".** That field is called a name throughout the bullet, and the bullet does not call
>        it a label.
>
>    (c) **A count ranks and mints nothing.** The bullet states that a repeated standing item is not minted as a
>        node on reaching any count; that the count ranks that item among what the manager picks next, so
>        repetition orders work rather than triggering it; and that the manager's separate duty to dispose of each
>        item naming the record in the report closing that node — by acting on it, minting a node, or saying why
>        not — is unchanged.
>
>    (d) **Filing is part of resolving.** The bullet states that the worker hands the retrospective back as text
>        and the manager writes it into the node file in the same edit that writes that node's answer, its flags
>        and its line in `decisions.md`, rather than as a later separate act; that it is written last in the file
>        so the mandatory section order is untouched; and that it is written under the heading `## Retrospective`
>        and under no other heading.
>
> 2. Every statement clause 1 replaced is appended verbatim to `.scratch/graph-workflow/map-history.md`, under a
>    heading naming the section of `map.md` it came from, with any struck-through text left struck through.
>    Nothing already in `map-history.md` is changed, reordered or removed.
>
> 3. That bullet still carries, unchanged and character-for-character, the human's quoted instruction beginning
>    **"Could you, for this effort only, ask subagents"**, and the four retrospective questions numbered (1)
>    through (4). Clause 1(a) is stated as a duty covering all four and adds no fifth question.
>
> 4. No file under `.claude/` is modified, and no file in `.scratch/graph-workflow/` other than `map.md` and
>    `map-history.md` is modified.
>
> 5. The tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Three statements, one bullet, one node — and its author gave the reason in the effort's own vocabulary:** *"three
nodes editing one bullet is node 115's two-writers collision."*

**Its clause 3 protects the human's own words** — the quoted instruction that created the retrospective, and the
four questions — character-for-character, and forbids a fifth question. What changes is what the manager does with
the answers, not what a worker is asked.

## Amendment, 2026-09-29 (from node 366)

*Written by [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s worker under its `CONDITIONS`, and filed by the manager under the standing instruction that an unclaimed node's condition may be amended where every word of the replacement is already fixed. The worker's own text, pasted:*

"Node 219: clauses 1 and 4 name `.scratch/graph-workflow/map.md` `## Notes`, but the retrospective bullet now lives in `map-manager-only.md` `## Notes`. `map.md`'s own pointer line says node 345 moved it there. Replacement: read `.scratch/graph-workflow/map-manager-only.md`, `## Notes`, wherever those clauses say `.scratch/graph-workflow/map.md` `## Notes`."

## Handover, attempt 1

*The worker's own text, pasted, 2026-10-02.*

````
HANDOVER:      Replace the mint-on-second-report rule in the map

ANSWER:        The retrospective bullet in `.scratch/graph-workflow/map-manager-only.md` `## Notes` (beginning "Every worker returns a retrospective as the last handover part, on this effort only") now states node 212's rule. Node 345 moved the bullet there from `map.md`, and node 366's amendment points this node's condition at it. The work changes three passages and adds one sentence. The quoted instruction, the four numbered questions and the rest of the bullet are unchanged.

- **The worker names the item.** A new passage follows question (4). It is a duty that covers all four questions and is not a fifth question. For each standing item its retrospective reports, the worker gives the item a short name. It reuses a name an earlier retrospective already carries where one fits, and mints a new one where none does. It states how many earlier retrospectives carry the name and lists their node ids. It finds existing names by searching the retrospective sections of the files under `.scratch/graph-workflow/nodes/`, "whatever heading each section was filed under". It does not work from memory or from any list held elsewhere. The word used is "name" throughout, never "label".
- **A count ranks and mints nothing.** The "Two duties on the manager" sentence is rewritten. The disposal duty stays and is stated as unchanged: in the report closing a node, the manager acts on each item naming the record, mints a node for it, or says why not. The second duty is now that the manager ranks each named standing item among what it picks next by that name's count. A repeated standing item is not minted as a node on reaching any count, so repetition orders work rather than triggering it.
- **Filing is part of resolving.** The filing sentence now says the following. The worker hands the retrospective back as text. The manager writes it into the node file in the same edit that writes that node's answer, its flags and its `decisions.md` line, rather than as a later separate act. It goes last in the file, so the mandatory section order is untouched, under the heading `## Retrospective` and no other.
- **Citation.** A sentence citing node 212 as where these three changes were settled was added before "Naming the subject is not decoration".

Two statements were replaced: the old two-duties sentence, which carried "on the second report of the same standing item it mints a node", and the old filing sentence. Both are appended verbatim to the end of `.scratch/graph-workflow/map-history.md`. They sit under "## Superseded from `map-manager-only.md` at node 219 — the retrospective bullet's mint-on-second-report rule and its filing sentence", each with a "### From `map-manager-only.md`'s `## Notes` — …" subheading. Nothing already in that file changed.

The bullet never stated outright that "the worker's retrospective names no standing item", so there was no sentence to remove for that point. The new naming passage covers it. The "annotation" wording was already replaced at node 340's follow-up, and its history entry already exists.

INDEX LINE:    The map-manager-only.md retrospective bullet now has the worker name and count each standing item, ranks a repeat instead of minting a node, and files retrospectives in the resolving edit.

FLAGS:         ASSUMPTION: I rewrote the old filing sentence as well as the mint sentence, even though it did not strictly contradict clause 1(d). It said the manager "files it … placed last" but did not say when. I replaced it rather than adding a second sentence beside it, so the bullet states the filing once. Under clause 2, its old text went verbatim to map-history.md. Index: Node 219 replaced the retrospective bullet's old filing sentence, which was silent on timing, instead of adding a second filing sentence, and banked the old text in map-history.md.
ASSUMPTION: The naming passage tells the worker to search retrospective sections "whatever heading each section was filed under". Node 212 measured five heading forms, and a search for `## Retrospective` alone undercounts. This adds no new rule: it stops clause 1(a)'s search from missing sections. Index: Node 219's naming duty tells the worker to search retrospective sections under every heading form, because node 212 found five forms and miscounts from scanning only one.

NEW NODES:     none

INVALIDATIONS: Flag 141.3, and node 141 §4's "second, not fourth" trigger: the second-report threshold no longer exists in the map. This is a contradiction, and node 212 already recorded it. The map-history.md entry from node 340's follow-up, "the retrospective bullet's filing sentence", is unchanged. The sentence that replaced it is now replaced too, and its own history entry is new.

CONDITIONS:    I searched the `## Question`, `## Acceptance condition` and `## Amendment` sections of every node whose status is not resolved, dropped, moot, merged or superseded. The terms were "second report", "mints a node", "annotation", "label", "retrospective bullet", "separate act" and "map-manager-only". Nothing that matched makes a clause wrong. Node 220 (open) lists this node as a blocker ("Node A above"), and its condition still fits the bullet as written. This work unblocks it. It also fits the "whatever heading" wording, because its clause 2 already covers every heading form. Node 185's "label" matches are about the decisions index's label vocabulary, and are untouched. Node 221 is out-of-scope. I made no replacements.

MISSING FROM MAP: map.md does not hold the retrospective bullet. Its pointer line ("The standing preferences only the manager acts on are in map-manager-only.md's `## Notes`") and the spawn told me where it is. map.md also gives no format for map-history.md headings. I copied the convention from recent entries (node 367, node 80).

GATE PAYLOAD:  Checker findings: none yet.
Paths touched: .scratch/graph-workflow/map-manager-only.md and .scratch/graph-workflow/map-history.md, inside the worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/219-retrospective-names. No file under `.claude/` was touched.
Bar: the repo has no build, tests, formatter or CI. The root holds only .claude, CONTEXT-MAP.md, CONTEXT.md, .gitignore and .scratch, which matches the record in map-implementation-rules.md. `git diff --check` is clean.
Integration: node 190 also appends to the end of map-history.md, so expect a conflict at that point. Both appended blocks should be kept, one after the other.
Proposed commit message:
  Replace the mint-on-second-report rule in the retrospective bullet

  The worker names and counts each standing item it reports, a count
  ranks work rather than minting a node, and the manager files the
  retrospective in the edit that resolves the node. The replaced
  sentences are banked verbatim in map-history.md.

  Node: graph-workflow/219

RETROSPECTIVE
1. What I had to hunt for: what node 212 meant by "every statement which contradicts them". I found it in node 212's `## Answer`, "What the worker reported its work invalidates", after first checking the bullet itself. I also had to find the map-history.md heading convention, which I copied from the latest entries. I looked for it in map.md first, and it is not stated there.
2. What arrived that this node did not need: most of map.md, such as the ground rules' background, the dogfood text and the v2 harness paragraph. The decisions.md lines for 345 and 366 also added nothing beyond what the spawn's amendment note already said. map-implementation-rules.md is about 70 lines, and only the "no build, no tests" sentence and the "work may be the record" rule applied here.
3. What would have made this easier: a condition that quoted the bullet's current sentences to be replaced, rather than paraphrasing three statements of which one no longer exists. A one-line heading template for map-history.md entries would also have helped.
4. What was stale, wrong or contradictory: the node's question and clause 1 describe the bullet as saying the retrospective is "filed as an annotation after the node resolves". The bullet had already been reworded after node 340 to "a section of its own headed `## Retrospective`". It also never stated that the worker names no item. The condition's paths named map.md, which node 345 made stale; the amendment fixed that.
````

## Flags

`219.1` `ASSUMPTION` — *The worker's own text.* I rewrote the old filing sentence as well as the mint sentence, even though it did not strictly contradict clause 1(d). It said the manager "files it … placed last" but did not say when. I replaced it rather than adding a second sentence beside it, so the bullet states the filing once. Under clause 2, its old text went verbatim to map-history.md.

`219.2` `ASSUMPTION` — *The worker's own text.* The naming passage tells the worker to search retrospective sections "whatever heading each section was filed under". Node 212 measured five heading forms, and a search for `## Retrospective` alone undercounts. This adds no new rule: it stops clause 1(a)'s search from missing sections.
