# Ship the `/repo-docs` skill

Type: implementation
Status: resolved
Blocked by: none

## Answer

`.claude/skills/repo-docs/SKILL.md` ships: a standalone 647-word skill keeping a repo's glossary and decision records, defaulting to `GLOSSARY.md` and `docs/decisions/`, grep-searched, with a report-only check.

*The manager's note:* landed as commit `ffbd4b07b`, the gate taken under the standing yes on 2026-10-04. Flags 383.1 and 383.2 settle at the node closing report. Node 135's 383 half of its trigger is met.

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

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      Ship the `/repo-docs` skill

ANSWER:        **`.claude/skills/repo-docs/SKILL.md` is written. It is a standalone, model-invoked skill of 647 words by `wc -w` (frontmatter included), and it is the only file in its directory.** Its frontmatter is `name: repo-docs` with the description "Keep a repository's glossary and decision records true as work changes the repository. Use when a change settles what a term means or makes a hard-to-reverse decision, or to check those docs against the code." It has no `disable-model-invocation`, so an agent can reach it by itself when a change settles a term or a decision.

               Sections, in order:
               - Opening: the docs hold only what the code cannot tell a reader. There are two kinds of content and no others, and no pages describing what the code does. Search with grep before opening a file whole.
               - `## Look for existing docs first`: (1) the agent instructions files, such as `AGENTS.md` or `CLAUDE.md`; (2) a grep for an existing glossary file, with the hint that a file in this format holds `_Avoid_` lines; (3) a directory listing for an existing decision-record directory, such as `docs/adr/` or `docs/decisions/`. The defaults, used only when that search turns up none, are `GLOSSARY.md` and `docs/decisions/`, both relative to the repository root. A file or directory is created only when there is a first entry to write in it.
               - `## The glossary`: the entry shape as a code block (`**Term**:`, a meaning of one or two sentences, an `_Avoid_:` line). An entry states meaning only, with no rule, no implementation detail and no specification. Only terms specific to the repository go in. Where several words name one concept, one is chosen and the others go on its `_Avoid_` line.
               - `## Decision records`: one file of about a paragraph (context, choice, why). The name carries a sequential number and a title, e.g. `0007-store-events-not-state.md`, and the next number is the highest existing one plus one. A record is written only when the decision is hard to reverse, would surprise a reader who lacks the context, and came from a real trade-off. An accepted record is not edited to change its decision. A changed decision gets a new record that names the record it replaces, by file name.
               - `## Writing`: the entry or record goes in the same change that settles the term or decision. Every edit goes into the change the human reviews with the rest of the work, never as a separate write. No index file and no log file are created, because the directory listing and the version-control history do those jobs. An agent without permission to write files only searches and checks, and reports the entries it would write.
               - `## Check`: it reports and fixes nothing, and covers the five findings of clause 11. The `_Avoid_` finding adds that a use of the same word for another meaning is not a finding, which applies the clause's "for that term's meaning". Each finding gives the file, the line and what is wrong. The check is complete when each of the five has been searched for across the repository.
               - `## What this skill produces`: writing produces entries and records in the change under way. The check, or a run without permission to write files, produces a report returned to whoever invoked the skill.

               Calls a later reader would otherwise have to re-derive:
               - The file names no search tool but grep. The word "find" is avoided as a verb, so it cannot be read as the `find` command.
               - "index" appears only where clause 6 requires it, as the file not to create.
               - The file never says "user". "The human" appears once, as the reviewer of the change, and is not addressed.
               - Version control is named generically and git is not named, under ground rule 1.
               - The headroom is 3 words under the 650 cap. Any correction that adds text needs cuts elsewhere.
               - Observation, not a defect of this file: run on this repository, step 2's `_Avoid_` grep finds `.claude/skills/expedition/glossary.md`, and also the skill's own `SKILL.md` wherever the skill is installed in the repository it serves. An agent running `/repo-docs` here would therefore adopt Expedition's glossary as the repository's glossary. Node 130's flag 130.2 says that glossary stays outside `/repo-docs`. The skill does not and cannot encode that, so whether this repository's agent instructions should say so is the manager's call.

INDEX LINE:    `.claude/skills/repo-docs/SKILL.md` ships: a standalone 647-word skill keeping a repo's glossary and decision records, defaulting to `GLOSSARY.md` and `docs/decisions/`, grep-searched, with a report-only check.

FLAGS:         ASSUMPTION: *Node:* The condition asks for one default glossary path and one default decision directory, and leaves both open. I chose `GLOSSARY.md` and `docs/decisions/`. `GLOSSARY.md` names what it holds. `docs/decisions/` matches the skill's own term "decision records" and is the default of one common decision-record convention. I set aside `CONTEXT.md` and `docs/adr/`, the names the replaced external skill used, because `CONTEXT.md` does not say it is a glossary. `docs/adr/` still appears as an example of an existing directory to look for. *Index:* `/repo-docs` defaults to `GLOSSARY.md` and `docs/decisions/`, chosen by its worker over the `CONTEXT.md` and `docs/adr/` names of the skill it replaces.

               ASSUMPTION: *Node:* The skill is model-invoked: it has a trigger-bearing description and no `disable-model-invocation`. The condition's clause 7 needs an agent to write an entry in the same change that settles a term, so the agent must be able to reach the skill without the human typing its name. The cost is one description that is always loaded. *Index:* `/repo-docs` is model-invoked so an agent reaches it when a change settles a term or decision, at the cost of an always-loaded description.

NEW NODES:     none

INVALIDATIONS: No resolved node is contradicted.
               - Extension: node 130's answer described the skill as ~50 lines. It now exists at 647 words, within node 130's own 650-word rendering of that size (flag 130.4).
               - Unaffected: node 130's flag 130.2 (Expedition's glossary stays outside `/repo-docs`). The shipped skill neither names nor excludes any particular glossary. The observation under ANSWER says how the two meet if the skill is run on this repository.

CONDITIONS:    **What I searched.** The `## Acceptance condition`, `## Question` and `## What must be true when it is done` text of every open or claimed node (Status: open or claimed, 2026-10-04), for: `repo-docs`, `domain-modeling`, `skills/*`, `GLOSSARY`, `docs/decisions`, `decision record`, and counts or globs over the shipped skill set (`every skill`, `shipped set`, `eleven`, `twelve`, `thirteen`).
               - Nodes 380 and 382 scope their work with greps over `.claude/skills/*/SKILL.md` for the phrases "Do not trust any summary of them" and "Before you write your handover, search the open nodes'". The new file contains neither, so no clause of theirs becomes wrong.
               - Node 135 (open, precondition, `Blocked by: 126, 383`): the node's question is unchanged. Its 383 half of the trigger is met once this work lands. The shipped text replacing `/domain-modeling` is `.claude/skills/repo-docs/SKILL.md`, invoked as `/repo-docs`.
               - No clause of any unclaimed node's condition is made wrong. I write no replacement.

MISSING FROM MAP: The map does not say whether the effort's own standards (the six writing rules and the glossary's `_Avoid_` lines) bind a shipped file that must not depend on Expedition. I held the file to the writing rules and to `/writing-for-agents`. I read the `_Avoid_` lines as binding only where the file names an Expedition concept, and it names none.

GATE PAYLOAD:  No checker findings yet.
               Paths touched: `.claude/skills/repo-docs/SKILL.md` (new; the directory is new too). Nothing else changed. `git status --short` in the worktree shows only `?? .claude/skills/repo-docs/`.
               The bar: the repo states no build, test or format commands. It has no manifest, no task runner and no CI, and `.gitignore` only ignores worktree paths. This matches `map-implementation-rules.md`'s record. The bar is its non-command half.
               Condition checks run on the finished file:
               - `wc -w`: 647.
               - The clause 3 grep for `expedition|mattpocock|domain-modeling|qmd|\.scratch`: no output (exit 1).
               - `grep -rn 'repo-docs' .claude/skills/`: one match, `.claude/skills/repo-docs/SKILL.md:2`.
               Method-skill parts skipped: none. `/writing-for-agents` was read as a standard and not invoked.
               Proposed commit message:
                 Ship the /repo-docs skill

                 A standalone skill that keeps a repository's glossary and decision
                 records true as work changes it: look for existing docs first, write
                 entries in the same reviewed change, supersede decisions instead of
                 editing them, search with grep, and check without fixing.

                 Node: graph-workflow/383

RETROSPECTIVE:
1. What I had to hunt for: the `/writing-for-agents` text, which the standards name only as a skill, found under the nix store with `find`. The commit trailer's effort name, found in `git log`. How to tell open nodes from the rest: a grep over `Status:` lines.
2. What arrived that this node did not need: most of `map.md` (worktree, landing, the numbers rule, the rule for nodes grouped by file), most of `map-implementation-rules.md` (the record-as-work rule, the trigger-file rule), and `graph-conventions.md` as a listed standard, which bears on a standalone skill not at all.
3. What would have made this easier: the spawn stating the bar is empty for this repo (it is recorded, but I re-confirmed it), and a pointer to node 130's handover section for the approved option list, which is the clearest statement of intent behind the condition.
4. What was stale, wrong or contradictory: both manager's notes checked out. The human's words are "q1 ok q2 just use grep for now", and node 130's flag 130.3 kept "for now" out. One near-tension: clause 10 says the file names no "index", while clause 6 requires it to name an index file not to create. I read clause 10 as meaning search indexes, and "index" appears only in clause 6's sentence. A second near-tension: running the skill on this repository would adopt Expedition's glossary, against flag 130.2. That is described under ANSWER.
`````

## Flags

`383.1` `ASSUMPTION` **· settled** — `/repo-docs` defaults to `GLOSSARY.md` and `docs/decisions/`, chosen by its worker over the `CONTEXT.md` and `docs/adr/` names of the skill it replaces. *(The worker's full text is under its handover's `FLAGS`.)*

`383.2` `ASSUMPTION` **· settled** — `/repo-docs` is model-invoked so an agent reaches it when a change settles a term or decision, at the cost of an always-loaded description. *(The worker's full text is under its handover's `FLAGS`.)*

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-10-04. A fresh checker; the condition reached it as a verbatim copy in `$TMPDIR/c383.md`, and the node's two flags as their `flags.md` sentences with ids, under node 379's rule.*

> PASS
>
> Work under check: the untracked `.claude/skills/repo-docs/SKILL.md` in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/383-repo-docs (HEAD 3a0b93e0a). The file has 67 lines, and every paragraph is already one unbroken line, so my searches ran over unwrapped text. F below stands for `.claude/skills/repo-docs/SKILL.md`.
>
> Acceptance condition, one line per part:
> 1. Established by `ls -la .claude/skills/repo-docs/`, which lists only SKILL.md. The frontmatter holds `name: repo-docs`, and its description reads "Keep a repository's glossary and decision records true as work changes the repository. Use when ...".
> 2. Established by `wc -w F`, which prints 647. The limit is 650.
> 3. `grep -n -i -E 'expedition|mattpocock|domain-modeling|qmd|\.scratch' F` returns nothing (rc=1). `grep -rn 'repo-docs' .claude/skills/` returns only `.claude/skills/repo-docs/SKILL.md:2:name: repo-docs`. `grep -n -i skill F` hits only "this skill's format", "What this skill produces" and "invoked this skill", so the file names no other skill. The only files it tells the agent to read are "the repository's agent instructions files, such as `AGENTS.md` or `CLAUDE.md`", which are the repository's own files.
> 4. Under `## Look for existing docs first`, the file says to search before creating anything and gives three steps: the agent instructions files, grep for an existing glossary file, and a listing of directories for an existing decision-records directory. Its fallback names `GLOSSARY.md` and `docs/decisions/`, "both relative to the repository root". It adds "Create a file or a directory only when you have a first entry to write in it."
> 5. The opening paragraph says "Keep two kinds of content ... and no others. Keep no pages describing what the code does."
>    - `## The glossary` gives the shape `**Term**:`, then one or two sentences, then a `_Avoid_:` line. It says "It holds no rule, no implementation detail and no specification."
>    - `## Decision records` says each record is one file of about a paragraph, with a sequential number and a title in the file name, and lists the three conditions.
> 6. Established by `grep -n index F` (line 50): "Create no index file and no log file. The directory listing serves as the index, and the version-control history serves as the log."
> 7. `## Writing`, first bullet: "A term or a decision settled in a change gets its glossary entry or decision record in that same change."
> 8. `## Decision records`: "An accepted decision record is not edited to change the decision. When a decision changes, write a new record that names, by file name, the record it replaces."
> 9. `## Writing`, second and fourth bullets: edits go "into a change that the human reviews together with the rest of the work, never as a separate write". An agent without write permission should "only search and check, and report the entries you would write".
> 10. `grep -n -i -E 'grep|rg|ripgrep|search|index|embed|engine|find' F` hits:
>     - "Search with grep before you open a file whole" (line 10);
>     - grep again at line 17;
>     - "index" only in the clause 6 sentence.
>     No other search tool, engine, index tool or embedding tool is named.
> 11. `## Check` opens "The check reports and fixes nothing" and lists all five items. The `_Avoid_` item adds a qualifier that a use of the word for another meaning is not a finding, which narrows nothing the condition demands.
> 12. `grep -n -i -E '\b(ask|user|wait|reply|confirm|question)' F` returns nothing. `## What this skill produces` states the output as entries written, or "a report returned to whoever invoked this skill".
> 13. `git status --porcelain` shows only `?? .claude/skills/repo-docs/`, and `git diff --stat 3a0b93e0a` is empty. The ignored files outside `.scratch` show nothing new.
>
> The condition records no scope search, so I had no recorded command to re-run. I read the changed path as the work, under the record-as-work rule in map-implementation-rules.md. It is a shipped skill file and none of the effort's record files.
>
> The bar:
> - Commands: I found no agent-instruction file at the repo root, only CONTEXT.md and CONTEXT-MAP.md. map-implementation-rules.md records that this repo has no build, no tests, no formatter and no CI, so the command half of the bar is empty and I ran nothing for it. That is a complete bar for this repo.
> - Standards: I read `.scratch/graph-workflow/map-implementation-rules.md` for its standards only, under `## What the work is held against`, and opened no other file in the effort's directory. No reviewing skill is named for this repo, so I ran none.
>
> Which standards bore on this work:
> - `/coding-principles` and `/naming`: these cover code, and the work holds none, so they did not bear.
> - The `_Avoid_` lines in `.claude/skills/expedition/glossary.md`: I checked them by hand, as the rules file directs. The file uses "report", "decision", "index", "log", "complete", "review" and "specification" in their ordinary meanings. None of them stands for the expedition concept whose entry refuses the word. "Report" and "the human reviews" are the condition's own words. No breach.
> - Ground rules 1 to 5:
>   - The file assumes no repo, machine or toolchain beyond grep, which clause 10 demands.
>   - It stands alone.
>   - It tells no agent to address the human.
>   - It is short prose.
>   - I held it against `/writing-for-agents`, which I located by name in the mattpocock-skills plugin, together with its SKILL-MECHANICS.md. The description front-loads its leading words and carries two branches, writing and checking. The check has a completion criterion ("complete when each of the five has been searched for across the repository"). Every prohibition in the file is wording the condition demands, and each stands beside a positive where one exists. No breach.
> - The six writing rules: I found no breach.
>   - The file is navigable by heading.
>   - It cites no file by line number. `grep -n -E 'line [0-9]|:[0-9]+' F` returns nothing.
>   - The only bold is the `**Term**` shape inside the code block.
>   - It uses no figure of speech or slogan contrast, and every negation is wording demanded by clauses 5, 6, 8, 9 or 11. `grep -n -i -E '\b(no|not|never|nothing|none)\b' F` lists each one.
>   - It points at no other shipped file.
> - graph-conventions.md: it governs the effort's record files, not a shipped skill, so it did not bear.
>
> I wrote no temporary files.
>
> Flags, checked after the outcome. Both are true of the work, so there are no QUESTIONS:
> - 383.1 is true. The fallback paths are `GLOSSARY.md` and `docs/decisions/`. `CONTEXT.md` does not appear in F, and `docs/adr/` appears only as an example of an existing directory to look for.
> - 383.2 is true. The frontmatter carries a model-facing description, and `grep -c disable-model-invocation F` prints 0.

### The gate, 2026-10-04 — standing yes

`standing yes`. The scope, word for word: *"Approve all gates automatically"*. The checker's `PASS` is taken as the human's approval. The run covered every part, handed back no question, and found both flags true. A gate taken under a standing yes settles no flag, so flags 383.1 and 383.2 settle at the node closing report.

*The manager's note, 2026-10-04:* flags 383.1 and 383.2 settle at the node closing report that closes this node.
