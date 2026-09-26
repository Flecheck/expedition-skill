# Land the open repairs to the checker contract in one change

Type: implementation
Status: open
Supersedes: 151, 173, 164
Blocked by: none

## Question

Open nodes 151, 173 and 164 each change `.claude/skills/expedition-checker/SKILL.md` and each forbids other changes to it. Make all their live changes in one node.

*Proposed by [node 329](329-group-the-open-nodes-against-the-worker-contracts.md)'s worker and filed by the manager, on the human's "ok" to node 329's merge and its conflicts' recommendations.*

## Acceptance condition

*Written by node 329's worker.*

The work is `.claude/skills/expedition-checker/SKILL.md`, path relative to the repository root. The worker may edit that file and no other, and writes no file under `.scratch/`. Done means every one of the following is true of the finished tree.

**A. A method section** *(node 151)*
A1. The file contains a section headed exactly `## How you check`, placed after the section headed `## Hard rules` and before the section headed `## What you hand back`.
A2. That section's body, from its heading to the next line beginning `## `, is at most 2,000 bytes.
A3. It states that the checker splits the acceptance condition into its parts before it reads the work, because its `PASS` owes one line per part.
A4. It states that three things are kept separate and are never merged with or ranked against one another: the acceptance condition, the bar, and the standards the checker reads for itself from `map-implementation-rules.md`. Passing on one of the three never excuses or masks failing on another.
A5. It states that the standards report under the bar, so work that breaches a standard is `FAIL: the bar` and never `FAIL: acceptance condition`.
A6. It states that the checker establishes each part of the condition by a search it can name, and hands that search back, rather than by reading the work through.
A7. It states that the checker says plainly what it did not check.
A8. It states that an effort's own rules may add method specific to that effort on top of this section, and that this section's demands still hold where they do.
A9. The section contains no instruction to search for, look for, discover or otherwise go and find the standards the checker holds work against.
A10. Where the section refers to a shape the file defines elsewhere, it uses the file's own name for it (`PASS`, `FAIL: acceptance condition`, `FAIL: the bar`, `NOT COVERED`) and defines no second version of any of them.
A11. Nothing added to the file names a skill or a plugin, requires anything to be invocable, or assumes a particular repository, machine or toolchain.

**B. The bar's commands** *(node 173)*
B1. The file nowhere states or implies that the checker's spawn may carry the bar's commands. The item in the list of givens that begins `The bar:` today reads "The bar: either its commands for this repo, or the properties alone." and contains "Where you are given the properties and no commands, discover the commands from the repo." After the work it offers no choice between being given commands and being given the properties, and the file holds no sentence conditioned on the checker having been given properties and no commands.
B2. That item states the bar's properties in full: the work builds, it warns about nothing, it is formatted, the tests relevant to it pass, and whatever else the repo itself demands is satisfied. It also states that the checker discovers the commands from the repo itself.
B3. The item says that a repo which states its own commands to an agent typically states them in its own agent-instruction file. That file is named by role and position only, and no particular filename for it appears anywhere in the finished file.
B4. The item keeps its statement that a repo with no build, no tests and no formatter meets the bar on its remaining half, which is "the complete bar for such a repo".
B5. The sentence introducing the givens today reads "You are given six things. The spawn carries the first five, and you read the sixth for yourself from one file this contract names." After the work, the count it states is arithmetically correct for the items the list holds, and it splits them correctly between those that arrive in the spawn and those the checker reads for itself.
B6. The sentence "The implementer works from the same file, so the two of you hold the work to one set of standards." is unchanged. No other sentence claims that the checker and the implementer take the bar's commands from the same place.

**C. Record material in the standards file** *(node 164)*
C1. Under `## The standards you hold the work against`, the file keeps its statement "The file is in the same directory as the record you are blind to, and it may itself hold record material, such as how the work lands, what the effort has decided, or links onward to the rest of the record. Read only the standards in it, and open no other file in the effort's directory." It also states, under the same heading, that the checker says in its outcome that it read only the standards in that file.
C2. The statement beginning "A ground rule is a standing constraint on the effort that is true of any node's work" is unchanged in what it requires.
C3. The statement "Leave the record unread, and do not go looking for it.", with its one exception for `map-implementation-rules.md`, is unchanged in what it requires.

**D. What else may change** *(the union of the fences of 151, 173 and 164)*
D1. Nothing outside the following is deleted or reworded: the new `## How you check` section; the given-list item beginning `The bar:`; the sentence introducing the givens; the sentence C1 adds; and any one sentence elsewhere stating A5's routing, which may be removed as a duplicate of the new section.
D2. No other file is modified.
D3. The working tree meets the bar.
