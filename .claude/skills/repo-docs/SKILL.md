---
name: repo-docs
description: Keep a repository's glossary and decision records true as work changes the repository. Use when a change settles what a term means or makes a hard-to-reverse decision, or to check those docs against the code.
---

# Repo docs

These docs hold only what the code cannot tell a reader: what the repository's own terms mean, and why its hard-to-reverse decisions were made. Keep two kinds of content, a glossary and decision records, and no others. Keep no pages describing what the code does.

Search with grep before you open a file whole, and read the lines that matched.

## Look for existing docs first

Before you create anything, look for where the repository already keeps a glossary and decision records, and use those.

1. Read the repository's agent instructions files, such as `AGENTS.md` or `CLAUDE.md`, for a glossary or a directory of decision records they name.
2. Search with grep for an existing glossary file. A file in this skill's format holds lines beginning `_Avoid_`.
3. List the repository's directories for an existing directory of decision records, such as `docs/adr/` or `docs/decisions/`.

Where this search turns up none, use `GLOSSARY.md` for the glossary and `docs/decisions/` for decision records, both relative to the repository root. Create a file or a directory only when you have a first entry to write in it.

## The glossary

Each entry has this shape:

```md
**Term**:
One or two sentences saying what the term means.
_Avoid_: rejected synonym, another rejected synonym
```

A glossary entry states what a term means. It holds no rule, no implementation detail and no specification. Enter only terms specific to this repository. Where several words name one concept, choose one and list the others on its `_Avoid_` line.

## Decision records

A decision record is one file of about a paragraph: the context, the choice made, and why. Its file name carries a sequential number and a title, such as `0007-store-events-not-state.md`. Number a new record one above the highest number already in the directory.

Write a decision record only when all three of these hold:

- the decision is hard to reverse;
- it would surprise a reader who lacks the context;
- it was the result of a real trade-off between alternatives.

An accepted decision record is not edited to change the decision. When a decision changes, write a new record that names, by file name, the record it replaces.

## Writing

- A term or a decision settled in a change gets its glossary entry or decision record in that same change.
- Every edit to these docs goes into a change that the human reviews together with the rest of the work, never as a separate write.
- Create no index file and no log file. The directory listing serves as the index, and the version-control history serves as the log.
- Where you are not permitted to write files, only search and check, and report the entries you would write.

## Check

The check reports and fixes nothing. It reports each of these:

- a term used in the repository with no glossary entry;
- a word listed on an `_Avoid_` line in use for that term's meaning, where a use of the same word for another meaning is not a finding;
- a glossary entry that states a rule or an implementation detail;
- a glossary entry or decision record that the code contradicts;
- a decision overturned with no record superseding it.

For each finding, give the file, the line and what is wrong. The check is complete when each of the five has been searched for across the repository.

## What this skill produces

Writing produces glossary entries and decision records in the change under way. The check, or a run without permission to write files, produces a report returned to whoever invoked this skill.
