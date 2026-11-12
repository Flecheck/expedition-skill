# GitHub issue 1, saved verbatim

Fetched on 2026-11-11 from https://github.com/Flecheck/expedition-skill/issues/1, at repository `HEAD` `d49b11e`. The title, body and one comment are below as the API returned them. The only change is that each heading of the comment is one level deeper, so it nests under this file's own heading.

## Title

Trips on self-written nodes

## Body, by Ten0, 2026-11-04

It writes the nodes with its own conditions, then they fail the check, it realizes the conditions were actually slightly wrong, but still waits on the user to validate:
<img width="1258" height="200" alt="Image" src="https://github.com/user-attachments/assets/09fa011e-63c4-4a93-9e24-e09130d052de" />
(for the second one it asks whether it should fix something it decided itself too)

Basically it sometimes trips on its own inconsistencies and asks things it should take responsibility for.
This pauses the implementation process and costs time.

## Comment, by Ten0, 2026-11-11

### Handoff: field notes and proposed fixes

These notes come from one long effort run under the skill at `d49b11e`. It had about 40 nodes, several deliverables, a deliverable split by the human midway, and a rollout across two services and a data pipeline. During the effort, the human gave the manager a standing instruction:
- settle flags on the manager's own choices;
- still bring every item with a product effect to the human;
- log each self-settled decision in a file next to the map, as source material for this issue.

What follows is that log in anonymised form, then the proposed changes. Section and clause references are to `d49b11e`, which is still `HEAD`.

#### Root cause

Every clause that sends a judgement to the human says *when* it settles: at the gate, or at the node closing report. None says *whose* choice it records. So a choice the manager authored is routed to the human as though the human owned it: a condition it wrote, a node split, an edge, a scope re-derived by re-running a recorded command.

When a worker or the checker then shows that the manager's own condition was slightly wrong, two clauses combine to make the manager wait:

- **The condition freezes once claimed.** SKILL.md § Changing one after it is written: "Where a worker already holds the node, its condition is handed over as written. A worker that judges the condition wrong raises it, and the human answers."
- **No flag is settled on judgement.** SKILL.md § Flags: "Settle a flag only at the moments this section names, never on your own judgement."

#### Examples (anonymised)

1. **Scope re-derivation.** Twice, the manager re-ran a condition's recorded search before the claim, as § Changing one after it is written requires ("Re-derive an enumerated scope before the node is claimed"). Each time the search returned one more call site than the worker's list, so the manager widened the list. Under the contract, that amendment became a flag "which settles at that node's gate". The human was asked to approve the output of a command the condition itself had fixed.
2. **A worker's raise on a manager-written clause.**
   - One clause asked a comment to state an invariant that the code contradicts: a helper is called with the very thing the comment says no function takes.
   - Another clause named a test command for a package that has no test target.
   - Both were wordings the manager had written, with no product effect, yet both raises went to the human.
3. **A checker's finding that a manager-written condition cannot hold in production.** A clause asked for a non-null column to be added to a large live table, but the setup tooling refuses that on a non-empty table. The fix was to make the column nullable, which changes nothing a user sees. It still went to the human.
4. **A rollout decision made after the conditions were written.** The human split one deliverable into two plus a cleanup, ordered by deploy. Several clauses could only land after another deliverable's deploy, and one clause became impossible under the new order. The manager moved clauses between nodes and suspended one. Under the contract, each move was an amendment for the human to settle at a gate.
5. **A checker question the manager had already answered.**
   - The checker asked whether a comment held on a path it could not read. It did not know where the sibling repository holding that path lives: the only pointer was in a scoped instruction file that never loaded (example 8). It could have found the repository by looking, and did not say what it had tried. The manager knew the location from its own notes.
   - The manager read that path, established the answer, and still put the question to the human at the gate, because `expedition-standing-yes` § What a standing yes never covers lists "a checker's raise, which includes a question a checker hands back" with no exception.
   - The human: "so basically you're asking me to answer a question you have already answered yourself?"
6. **"Decide yourself" on a flag at the gate.** The human answered a gate flag with "decide yourself". § Two things the human can say that are not answers sends a "you decide" back to the worker, but at the gate the worker had already decided and was waiting. Sending it back would have re-asked the worker its own question.
7. **The manager's own inference in a relay.** The human asked the manager to explain a worker's question, and the manager's explanation added a claim the worker had not made. The claim was false and cost three rounds. The glossary's "drawn only from context it already holds" and "answers nothing itself" leave open which side of that line an explanation falls on.
8. **Scoped instruction files never loaded.**
   - Every worker and checker was spawned from the main checkout and worked in a sibling worktree. The harness loads a subdirectory's `AGENTS.md`, and path-scoped rules, only for files under the session's own directory, so none of the scoped files governing the edited code ever loaded.
   - In one case, a checker reported a sibling repository as unreadable, though the scoped `AGENTS.md` said where it lives.
   - In another, a scoped `AGENTS.md` asked for the changed endpoint to be called against a locally running service before shipping. The workers never saw that step, and a type-binding bug reached a staging environment that the call would have caught.
   - The human asked: "it's unclear to me why when working on the code they don't load these files automatically: the separate worktree has the CLAUDE.md copy too no?" The worktree does hold its own copy; what is missing is that the agent's working directory is not inside it.

#### Proposed changes, smallest first

1. **Define the author of a choice** (glossary).
   - Name a choice by who made it: the human, a worker, or the manager.
   - Add a test of *product effect*: would the finished product behave or read differently for its user?
   - These have none: a node split, an edge, a sequencing, a scope re-derived by re-running a recorded command, or the wording of a clause that only restates what is already fixed.
2. **Settle own-authored flags at filing** (§ Flags). Add a third settling moment: a flag on a manager-authored choice with no product effect is settled by the manager when it is filed.
   - It is marked `**· settled**` with the reason `own choice, no product effect`.
   - It is left out of gate payloads and node closing reports (examples 1, 2).
3. **Let the manager amend its own condition after the claim** (§ Changing one after it is written).
   - When the condition is the manager's own and a worker or the checker shows a clause wrong, the manager amends it without the human.
   - The existing provisos still apply: every word already fixed, source named. The amendment must also change no product behaviour the human decided.
   - The amended text goes to the worker, and to the checker on the re-check.
   - This covers a condition the human's later decision made out of date, such as a split deliverable or a reordered rollout (example 4).
   - A correction that does change the product still goes to the human (examples 2, 3).
4. **What the manager does with a raise or a question from a worker or the checker** (§ The checker, § The gate, § A paused implementation node). Before passing it to the human:
   - If it concerns a choice the manager made and the fix has no product effect, the manager settles it under items 2 and 3, and re-runs the check (example 3).
   - If the agent is blocked by missing information the manager already holds, such as where a file lives or a decision recorded in the map, the manager hands that information back and lets the agent finish. It settles nothing and decides nothing for the agent. It also does not go looking: it hands back only what it already has, and never investigates a raise itself (example 5).
   - Everything else goes to the human.

   An agent that reports it cannot read or do something states what it tried (the path, the command, the error), so that a missing tool or permission can be told apart from not having looked.
5. **"You decide" on a gate flag** (§ Two things the human can say that are not answers). At a gate, the flag's worker has already decided, so a "you decide" settles the flag as delegated, on the worker's existing choice, with no round trip (example 6).
6. **No explanation of the manager's own in a relay** (§ What is in front of the human, and when; glossary). When the human asks the manager to explain a worker's question, the manager quotes the worker's own words or sends the request back to the worker. It writes no explanation that adds claims the worker did not make (example 7).

#### Status of the scoped-instruction-files gap (example 8): on trial outside the skill

The human's sharper wording of what is missing: "properly collect the agents.md of parent directories of the files it edits, which wasn't done automatically because the workspace is not a subdir".

To keep the skill lean, the human chose to try this first as a rule in the host project's own always-loaded agent instructions, not in the skill. The rule is roughly:

> When a file you read or edit lies outside the directory the session started in (a sibling worktree), read every `AGENTS.md` from that file's directory up to the repository root before working on it: Claude Code loads a subdirectory's `AGENTS.md` only for files under the session's directory.

An always-loaded rule reaches subagents too, so it needs no line in each spawn brief.

If the trial shows a project rule is not enough, or not every host project will carry one, there are two options for the skill:
- the root fix: start each worker with its working directory inside its own worktree, where the harness allows it;
- the fallback: one ground rule in § Spawning a worker and § The checker, saying to walk up from every file read or edited to the repository root and read each `AGENTS.md` / `CLAUDE.md` on the way. A scoped file governs its whole subtree, not only its own directory.

#### Out of scope

Two other lessons from the same effort were judged project-specific by the human, and stay out of the skill.

#### A note from the human on how to write the fix (paraphrased)

Keep it to the principle, the author of a choice and its product effect, and let the manager handle the cases nobody specified on its own. Don't list the steps for each scenario: a list risks the agent forgetting a scenario it leaves out. For the same reason, there's no need for a log or report line of self-settled choices: they are items the human would never have seen had they not gone wrong, so settling them costs no human time.

#### Suggested first steps for a worker on this issue

1. Re-read SKILL.md, the glossary and `expedition-standing-yes` at the current `HEAD`, and check that each quoted clause still reads as above.
2. Weigh each proposal against § What is never yours, and against keeping the skill lean. Items 1–4 share one principle and probably carry most of the gain: before anything reaches the human, the manager handles what is its own choice, and passes back what it already holds. Items 5 and 6 are independent.
3. Example 8 waits on the trial above.

