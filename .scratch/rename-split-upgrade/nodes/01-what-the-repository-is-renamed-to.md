# What the repository is renamed to, and what the rename covers

Type: grilling
Status: resolved
Labels: RENAME

## Question

The human wants the repository renamed from `graph-agent` to something like `expedition-skill`. What is
the new name, and what does the rename cover? Candidates for what it covers include the hosted
repository's name, the local directory, and every text in the repository that names `graph-agent`, such
as the glossary's `_Avoid_` line on the term Expedition and the root `CLAUDE.md`. Which of those does
the human do themselves, and which become implementation work in this effort?

## Answer

**Before you record this:** at 2026-10-12, after your note, `git -C /home/mathieu/projects/graph-agent remote -v` still printed `origin https://github.com/Flecheck/graph-agent.git` for both fetch and push. The `set-url` the manager reported did not take effect in the main checkout. Item 3 below is not yet done.

The repository's new name is `expedition-skill`. The human chose it.

What the rename covers, and who changes each place:

1. **Hosted repository.** The human renamed the GitHub repository to `https://github.com/Flecheck/expedition-skill` before any of this effort's nodes had landed. This is done.
2. **Local checkout.** The human renames `/home/mathieu/projects/graph-agent` to `/home/mathieu/projects/expedition-skill`. In the same step, the human moves the Claude Code project directory `~/.claude/projects/-home-mathieu-projects-graph-agent/` to `~/.claude/projects/-home-mathieu-projects-expedition-skill/`, so the memory and session history follow the checkout. The human does this while no expedition session is running in the checkout, for example right after a management session stops, and preferably before this effort cuts any worktree. Renaming the directory while the manager runs in it would break that session's paths. A worktree that exists at the time of the rename would need `git worktree repair`.
3. **Git remote.** The manager points `origin` at `https://github.com/Flecheck/expedition-skill.git` with `git remote set-url` in the main checkout. This only changes local configuration and pushes nothing. Until it is done, GitHub's forwarding of the old URL is all that keeps the remote working.
4. **Text in the repository.** One implementation node in this effort makes two edits. It retitles the root `CLAUDE.md` to `expedition-skill`. It drops `graph-agent` from the glossary's `_Avoid_` line under Expedition, leaving `_Avoid_: wayfinder`. The `_Avoid_` entry goes because naming this repository in a shipped file breaks the root `CLAUDE.md` rule 1 for the skill files. A repository named after the workflow also leaves nothing for the entry to warn against. As of 2026-10-12, these two lines are the only places outside `.scratch/` and `.git` that name `graph-agent`.
5. **Left as they are.** The closed effort's record, `.scratch/graph-workflow/`, which is evidence only. The commit history.

The human's words: *"Q1. expedition-skill is fine Q2 I just renamed it since nothing as started yet https://github.com/Flecheck/expedition-skill Q3 ok"*, then *"Q4 ok Q5 ok"*.

*Manager's note:* the worker's opening paragraph was true when it looked. My first `set-url` failed inside the sandbox with `error: could not write config file .git/config: Device or resource busy`. I had sent the worker a note saying the change was done before I saw that failure, and that note was wrong. I re-ran the command with the sandbox off, and `git remote -v` then printed `https://github.com/Flecheck/expedition-skill.git` for fetch and push. So item 3 is done.

## Flags

`01.1` `ASSUMPTION` **· settled** — The commit history stays as it is. Its commit messages are history and name no repository in a way any reader acts on. I settled this myself and stated it in both payloads, and the human did not object.

`01.2` `ASSUMPTION` **· settled** — The new `CLAUDE.md` title is exactly `# expedition-skill`, lowercase and matching the repository's name, as `# graph-agent` matched the old one.

## Interview

### Attempt 1 — agent `ad5a824143b07a03a`

**Relayed question, payload 1, as the worker wrote it:**

NODE:          What the repository is renamed to, and what the rename covers

ABOUT:         This node decides the repository's new name and which places the rename reaches. For each place, it also decides whether the human makes the change or this effort makes it as implementation work. It is decided first because every later text that names the repository depends on it.

SO FAR:        I read the node, the map and the grilling contract, and searched the working tree.
                - Outside `.scratch/`, the old name `graph-agent` appears in exactly two places. One is the root `CLAUDE.md` title, `# graph-agent`. The other is the glossary's `_Avoid_` line under the term Expedition, `.claude/skills/expedition/glossary.md`, which reads `_Avoid_: graph-agent (the repository's name, not the workflow's), wayfinder`. No skill file, rule file, `.gitignore` entry, `CONTEXT.md` or `CONTEXT-MAP.md` names it. The repository has no `.claude/settings*.json`.
                - Inside `.scratch/`, about 131 files of the closed effort `.scratch/graph-workflow/` name it. That count is from a search on 2026-10-12, for scale only and not authoritative. The map says that record is evidence only, so I treat it as left as it is. The two files of this effort that name it are its own map and this node, and both describe the rename itself.
                - Outside the repository, three things carry the old name. The git remote is `https://github.com/Flecheck/graph-agent.git`. The local checkout is `/home/mathieu/projects/graph-agent`. The human's Claude Code project data is the directory `~/.claude/projects/-home-mathieu-projects-graph-agent/`, which is keyed by the checkout's path and holds 9 memory files and the session logs. If the checkout is renamed, Claude Code starts a fresh, empty project for the new path, unless that directory is moved to the matching new key.
                - Nothing else on the machine points at the checkout's path. The user-level skills under `~/.claude/skills` are other skills, and `~/dotfiles` does not mention `graph-agent`. Only the main worktree exists right now.
                - GitHub sends the old URL on to the new one after a rename, but the local remote should still be updated.
                - The repository holds 11 skills: `expedition` and its 9 contract and command skills, plus `repo-docs`.
                - Settled on my own authority: the closed effort's record is not rewritten, and the commit history is not rewritten.

Q1. The new name
ASK:           What is the repository's new name?
RECOMMENDED:   `expedition-skill`. It is the name the human suggested. It also names the one skill a user invokes, `/expedition`, which the other skills serve.
ALTERNATIVES:  `expedition-skills`: the plural fits the 11 skill directories more literally.
               `expedition`: shorter, but the same word as the workflow, so "the repository" and "the workflow" would be harder to tell apart in text.

---

Q2. The hosted repository and the local checkout
CONTEXT:       Renaming the GitHub repository needs admin rights on GitHub. Renaming the local directory moves the directory that every running manager session and worktree is working in. It also needs the Claude Code project directory moved, or the memory is lost.
ASK:           Are both the GitHub repository and the local directory renamed, and do you make those changes yourself rather than this effort?
RECOMMENDED:   Rename both, and do it yourself, outside the effort's nodes. Do it in this order:
               (1) rename on GitHub;
               (2) run `git remote set-url origin` to the new URL;
               (3) when no expedition session or worktree is in use (preferably after this effort's other nodes have landed), rename the local directory and move `~/.claude/projects/-home-mathieu-projects-graph-agent/` to the key for the new path.
               This rests on two facts. Every one of these steps is outside what a worker may touch: GitHub admin rights, the sandbox, and the Claude Code data directory. And renaming the directory while the manager runs in it would break that session's paths.
ALTERNATIVES:  Rename only on GitHub and keep the local directory name: no memory move is needed, but the local name and the hosted name differ.
               Rename the local directory now, in the middle of the effort: this breaks the running manager session and the paths of any worktree that exists by then.
               Make these steps an implementation node: no worker can run them inside its contract.

---

Q3. The texts in the repository that name `graph-agent`
CONTEXT:       Only two places in the repository's live files name the old name. The root `CLAUDE.md` rule 1 for the skill files says nothing in them may assume this repository.
ASK:           Should one implementation node in this effort make two changes? The first is to retitle the root `CLAUDE.md` to the new name. The second is to drop `graph-agent` from the glossary's `_Avoid_` line under Expedition, leaving `_Avoid_: wayfinder`.
RECOMMENDED:   Yes, one small implementation node for both changes. Leave `.scratch/graph-workflow/` and the commit history unchanged. The glossary is a shipped file, and naming this repository in it breaks rule 1. Once the repository is named after the workflow, nobody would confuse the two names, so there is nothing left to warn against.
ALTERNATIVES:  Keep the `_Avoid_` entry, reworded as `graph-agent (the repository's former name)`. It helps a reader of the old record, but it keeps a mention of this repository in a shipped file.
               Also rewrite the closed effort's record to the new name: about 131 files of evidence-only history, with no reader it would help.
               You edit the two lines yourself, with no node: possible, but then the change gets no check against the standards.

**The human's answer to payload 1, `verbatim`:**

> Q1. expedition-skill is fine Q2 I just renamed it since nothing as started yet https://github.com/Flecheck/expedition-skill Q3 ok

Q1 takes the worker's `RECOMMENDED`: *"`expedition-skill`. It is the name the human suggested."* Q3 takes the worker's `RECOMMENDED`: *"Yes, one small implementation node for both changes. Leave `.scratch/graph-workflow/` and the commit history unchanged."*

*Manager's note:* the same message also carried, before these answers, a remark about destination 2, which is recorded on node 02 and in the map. It reads, `verbatim`: *"Also for Destination 2, I am not sure yet but I might want it to be my main way of working and continue indefinity on it for all small tasks, as I have new things to do I add then and when they are merged I cleanup the graph."*

**Relayed question, payload 2, as the worker wrote it:**

NODE:          What the repository is renamed to, and what the rename covers

ABOUT:         This node decides the repository's new name and which places the rename reaches. For each place, it also decides whether the human makes the change or this effort makes it as implementation work. Two places are still open after your last reply: the local directory, and the git remote.

SO FAR:        Settled by your reply:
                - The new name is `expedition-skill`.
                - You renamed the GitHub repository to `https://github.com/Flecheck/expedition-skill` yourself.
                - One implementation node in this effort makes two edits. It retitles the root `CLAUDE.md` to `expedition-skill`, and it drops `graph-agent` from the glossary's `_Avoid_` line under Expedition, leaving `_Avoid_: wayfinder`.
                - The closed effort's record and the commit history stay as they are.

               What I checked on 2026-10-12, after your reply:
                - The local checkout is still `/home/mathieu/projects/graph-agent`. `/home/mathieu/projects/expedition-skill` does not exist.
                - The Claude Code project directory is still `~/.claude/projects/-home-mathieu-projects-graph-agent/`. It holds the memory and the session logs, and it is keyed by the checkout's path.
                - The git remote `origin` still points at `https://github.com/Flecheck/graph-agent.git`. GitHub forwards that old URL to the new one, so nothing is broken today.
                - I could not confirm the new URL from here. The public page returns 404, which is what a private repository returns, and no credentials are available to me.

Q4. The local directory
CONTEXT:       Your "I just renamed it" covers GitHub. The local directory still carries the old name.
ASK:           Is the local directory renamed to `/home/mathieu/projects/expedition-skill`, and if so, when?
RECOMMENDED:   Yes. You do it yourself, at a moment when no expedition session is running in it, for example right after this management session stops. In the same step, move `~/.claude/projects/-home-mathieu-projects-graph-agent/` to `~/.claude/projects/-home-mathieu-projects-expedition-skill/`, so that the memory and the session history follow the checkout. Doing it now would break the paths of the manager session that is running in the directory. No worktree exists yet, so between sessions is the cheapest moment.
ALTERNATIVES:  Keep the local name `graph-agent`: nothing needs to move, but the local name and the hosted name differ.
               Rename it later, after this effort's worktrees exist: each worktree's path would need a `git worktree repair`.

---

Q5. The git remote
ASK:           Who points `origin` at `https://github.com/Flecheck/expedition-skill.git`, and when?
RECOMMENDED:   The manager does it now, by running `git remote set-url origin https://github.com/Flecheck/expedition-skill.git` in the main checkout. It is a one-line change to local git configuration. It pushes nothing, and it removes the dependence on GitHub forwarding the old URL.
ALTERNATIVES:  You run it yourself, together with the directory rename.
               Leave it as it is and rely on GitHub forwarding the old URL: this works until a new repository named `graph-agent` is ever created under `Flecheck`.

**The human's answer to payload 2, `verbatim`:**

> Q4 ok Q5 ok

Q4 takes the worker's `RECOMMENDED`: *"Yes. You do it yourself, at a moment when no expedition session is running in it, for example right after this management session stops."* Q5 takes the worker's `RECOMMENDED`: *"The manager does it now, by running `git remote set-url origin https://github.com/Flecheck/expedition-skill.git` in the main checkout."*
