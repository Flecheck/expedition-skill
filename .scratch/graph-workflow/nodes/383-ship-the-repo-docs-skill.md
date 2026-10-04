# Ship the `/repo-docs` skill

Type: implementation
Status: open
Blocked by: none

## Question

Write the standalone docs skill node 130 settled, as one new file, `.claude/skills/repo-docs/SKILL.md`.

*Reported by [node 130](130-the-docs-discipline-this-workflow-ships.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none."*

## Acceptance condition

*Authored by node 130's worker and filed by the manager.*

> Done when all of the following hold.
>
> 1. The file `.claude/skills/repo-docs/SKILL.md` exists and is the only file in the directory `.claude/skills/repo-docs/`. It opens with YAML frontmatter holding `name: repo-docs` and a `description` saying the skill is for keeping a repository's glossary and decision records true as work changes the repository.
> 2. The file is at most 650 words as counted by `wc -w .claude/skills/repo-docs/SKILL.md`, frontmatter included.
> 3. The file stands alone. `grep -n -i -E 'expedition|mattpocock|domain-modeling|qmd|\.scratch' .claude/skills/repo-docs/SKILL.md` returns nothing. The file names no other skill and tells the reader to read no file outside the repository it is working in, apart from that repository's own files. `grep -rn 'repo-docs' .claude/skills/` returns matches only inside `.claude/skills/repo-docs/`.
> 4. Before anything is created, the file tells the agent to find where the repository already keeps a glossary and decision records, and to use those: its agent instructions files (such as `AGENTS.md` or `CLAUDE.md`), an existing glossary file, an existing directory of decision records. It names one default path for a glossary and one default directory for decision records, both relative to the repository root, to be used only when that search finds none. It tells the agent to create a file only when there is a first entry to write in it.
> 5. The file keeps two kinds of content and no others.
>    - A glossary. Each entry is a term in bold followed by a colon, a meaning of one or two sentences, and a line beginning `_Avoid_` listing rejected synonyms. The file says a glossary entry states what a term means and holds no rule, no implementation detail and no specification.
>    - Decision records. Each is one file, about a paragraph long, whose file name carries a sequential number and a title. The file says a decision record is written only when all three hold: the decision is hard to reverse, it would surprise a reader who lacks the context, and it was the result of a real trade-off between alternatives.
>    - The file says the skill keeps no pages describing what the code does.
> 6. The file tells the agent to create no index file and no log file, and says the directory listing and the version-control history serve those purposes.
> 7. The file tells the agent that a term or decision settled in a change gets its glossary entry or decision record in that same change.
> 8. The file says an accepted decision record is not edited to change the decision. A changed decision gets a new record that names the record it replaces.
> 9. The file says every edit to these docs goes into a change that the human reviews together with the rest of the work, never as a separate write. It says an agent not permitted to write files only searches and checks, and reports the entries it would write.
> 10. The file tells the agent to search with grep before opening a file whole. It names no other search tool, search engine, index or embedding tool.
> 11. The file gives a check operation that reports and fixes nothing. The check reports each of these five:
>     - a term used in the repository with no glossary entry;
>     - a word listed on an `_Avoid_` line in use for that term's meaning;
>     - a glossary entry that states a rule or an implementation detail;
>     - a glossary entry or decision record that the code contradicts;
>     - a decision overturned with no record superseding it.
> 12. The file contains no instruction to ask the user anything, to address the user, or to wait for a reply. What it produces is stated as entries written or a report returned to whoever invoked it.
> 13. No file outside `.claude/skills/repo-docs/` is changed.
>
> Scope: the work creates a file, and the named places are the work rather than instances of a defect. So the scope came from no search. The `grep` commands in clauses 3 and 10 are demands on the finished file, not a scope search.
