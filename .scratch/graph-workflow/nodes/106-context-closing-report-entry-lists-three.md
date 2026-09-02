# `CONTEXT.md`'s `Closing report` entry lists three contents where the settled report has six

Type: implementation
Status: open

## Question

*Surfaced by [What the manager reports to the human, in one place](46-what-the-manager-reports.md)'s worker, and
pasted as it wrote it.*

> `CONTEXT.md`'s **Closing report** entry says the manager hands over *"what was decided, what landed, and every flag
> still outstanding"*. Node 10 and `.claude/skills/expedition/SKILL.md` fix six items and make the report a delta
> scoped to what the human has not already seen. `CONTEXT.md` is declared authoritative and ships with the skill set,
> so a reader taking it at its word writes a report short by half. Node 103's condition reaches `CONTEXT.md`'s
> **Flag** entry and not this one; node 90's reaches the **Closed** entry and not this one.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 46's worker. Pasted as it wrote it, and not the manager's.*

> `CONTEXT.md`'s **Closing report** entry states that the report is a delta scoped to what the human has not already
> seen, and that it carries what landed, the supersession chains, the state of the bar, every outstanding flag, what
> the sweep found, and every sweep round. Its `_Avoid_` line is unchanged. No other entry in `CONTEXT.md` changes —
> in particular the **Closed**, **Flag** and **Handover** entries are untouched, those being other nodes' work. No
> file under `.claude/skills/` changes and no file under `.scratch/` changes. The working tree meets the bar.
