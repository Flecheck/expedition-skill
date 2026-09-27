# Adoption

This file tells the manager how to start an effort from a directory of work that already exists. Read
`## Starting an effort` in `SKILL.md` and `### Start an effort` in `graph-conventions.md` first. This
file holds only the steps adoption adds to them. Terms are used exactly as the glossary (`glossary.md`)
defines them.

Adoption is a way of starting an effort, and not a kind of node. You perform it, before the graph
exists. It produces the same files as starting from a conversation, and its input is a directory of
work that already exists. This file calls that directory's existing files the foreign record.

Your own part is bounded. You read the foreign record only as far as your steps need, and you
transcribe none of its entries. Your part ends when you mint the bulk import as the graph's first
nodes. Their kind is `precondition`. Workers write the imported node files, and you write none of them
yourself.

## Your steps, in order

1. **Take the effort's name from the directory.** The effort's name is the name of the directory that
   already exists. Write the graph's files into that directory, and not into a new one beside it.
2. **Resolve each reserved name the directory already uses for something else.** The graph reserves
   `map.md`, `map-history.md`, `map-manager-only.md`, `map-implementation-rules.md`, `decisions.md`,
   `flags.md` and `nodes/`. Rename each foreign file or directory on one of these names to a name the
   graph does not use, and follow the rule under `## A reserved name already in use`.
3. **Write `map.md`** with the three sections `## The seven files` in `graph-conventions.md` gives it.
   Take its content from what the effort already wrote, and invent none of it:
   - the destination, and whether the effort is expected to reach it;
   - the notes and the standing preferences;
   - the effort's ground rules, copied verbatim;
   - its declaration of which sources are authoritative, which are evidence only, and which hold
     statements known to be false, built from the foreign record's own statements about its sources
     and put in those three terms.

   Where the foreign record states nothing for one of these, ask the human rather than write it
   yourself.
4. **Declare the label vocabulary from the foreign label families.** A family is the shared part of
   the foreign identifiers, such as `AUTH` for `AUTH-1` and `AUTH-2`. Declare the families, and not the
   identifiers, in `map-manager-only.md`, where `### Start an effort` puts the vocabulary. Where the
   foreign record has no identifiers, write the line saying the effort declares no vocabulary.
5. **Append the expedition section to the target repository's tracker doc, where it has one.** Where
   that doc describes the `/wayfinder` local-markdown scheme, append the block under `## Changed` in
   `wayfinder-divergences.md`. Add one line after it saying that the effort was adopted and where its
   nodes are. A tracker doc of any other scheme gets that one line only.
6. **Create the remaining graph files empty**, as `### Start an effort` lists them.
7. **Mint the import nodes.**
   1. Sort the foreign files by the rule under `## Which foreign files import`. Link each file of
      research output from `map.md`'s `## Notes`.
   2. Build the lookup table under `## Citations inside imported material`.
   3. Mint the pass-one nodes and the pass-two node, as `## The bulk import` describes them. Mint a
      node of its own for each file the sorting left undecided.
   4. Run checks 1, 3 and 4 under `## Mechanical checks` in `graph-conventions.md`, as step 9 of
      `### Start an effort` requires.

   Your part ends here.

## A reserved name already in use

The existing file's content moves verbatim into the node files that now hold it. The reserved name is
then rewritten to its expedition meaning. Nothing is summarised, shortened or discarded on the way.

The file you renamed in step 2 is where pass one reads that content from. Pass two removes the renamed
file, because by then every entry of it is in a node file. For example, a foreign `decisions.md` whose
entries are decisions ends with each entry in a node of its own. The reserved `decisions.md` then holds
one line per such node, each line linking the node that now holds the entry.

## The bulk import

The import transcribes the foreign record as it stands. It reconciles nothing. A question the foreign
record has already answered elsewhere is imported as an ordinary node, like any other question. It is
resolved afterwards by ordinary graph work, which is where reconciling the foreign record happens.

The import runs in two passes, each on `precondition` nodes.

- **Pass one mints every node file.** It can be split, for example by foreign file or by label family,
  into several nodes that run in parallel. Give each of them a range of node numbers that no other
  range overlaps, larger than its share. A node added after the import takes a number above the
  highest range.
- **Pass two wires the edges.** It writes every `Blocked by:`, `Supersedes:` and `Superseded by:` edge
  that the foreign prose states. It is one node, blocked by every pass-one node, because inverting an
  edge needs the whole mapping from foreign identifier to node number at once. It builds that mapping
  from the node filenames.

Start no imported node until the pass-two node resolves, because until then the imported nodes carry
no edges and the frontier is wrong.

Each import node's `## Question` names the foreign files or entries it transcribes, its number range,
and the lookup table it applies. The node files it writes are its node's own work, and not nodes it
found, so its worker writes them under its contract's rule for a graph file that is its own node's
work. The recording of the import node itself stays yours.

### What an imported node looks like

- **Its name.** The foreign identifier survives in the node's free-form filename, such as
  `nodes/24-auth-2-token-refresh.md` for `AUTH-2`. It is never written as a field. Its label is its
  identifier's family.
- **Its kind.** It takes the kind the foreign record gives it where that kind is one of the five. It is
  a `grilling` node otherwise, because a question the foreign record holds open is one the human
  decides.
- **Its words.** Foreign prose moved into a node keeps its own words, including words the glossary
  refuses. Prose newly written in the graph uses the glossary's words and does not adopt the foreign
  ones.
- **Its status.** A foreign status maps onto an expedition status:
  - decided: `resolved`, with the entry's full text as the node's `## Answer`, and its line in
    `decisions.md`;
  - replaced by another entry: `open` in pass one, and `superseded` once pass two writes its edges;
  - ruled beyond the effort: `out-of-scope`, with its line in `map-manager-only.md`'s
    `## Out of scope`;
  - set aside to return to: `open`, with the foreign conversation under `## Interview`;
  - anything else, or no status: `open`.

Where the foreign record already names one entry as superseding another, pass two writes both
directions of the edge, `Supersedes:` on the replacement and `Superseded by:` on the old node, so the
pair has both of its halves. Pass two also sets that old node's `Status: superseded`. The import
records a supersession the foreign record already made. It performs none of its own.

## Which foreign files import

- A file holding questions or decisions imports, each entry becoming a node.
- A file holding research output is linked from `map.md`, and not imported.
- A file that is genuinely either gets a `grilling` node of its own, whose question is whether it
  imports or is linked. The import does not decide it.

## Citations inside imported material

Imported prose cites paths, and some of those paths may have moved since they were written. Before the
import, build a lookup table. It maps each cited path that no longer exists onto the path that now
holds the cited file. Building the table is part of your own act, because it takes judgement. The
import applies the table mechanically to every citation it moves.

## Git history

Adoption changes nothing about the target repository's git history. It creates no branch, pushes
nothing and rewrites no commit. No existing commit is attributed to an imported node, so each imported
node's landed-code history starts empty. The commit trailer `Node: <effort>/<NN>` carries the effort's
name, so a later effort in the same repository cannot be confused with this one.
