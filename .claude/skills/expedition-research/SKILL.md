---
name: expedition-research
description: Research node worker contract for an expedition. Read it when a spawn names it.
---

# Research worker contract

You are a worker on one node of an expedition, and you are not its manager. The manager spawned you and
is waiting for one handover.

Your node's kind is **research**: a fact from outside the working directory, read and reported. A
research node never involves the human.

## Words used exactly

- **node** — one question to decide or one piece of work to do. Its identity is a number that never
  changes, and its name is free-form.
- **manager** — the single long-lived thread that owns the graph, spawns one worker per node, and is the
  only thing the human ever talks to.
- **worker** — you, working one node with no bookkeeping on the graph and no contact with the human.
- **handover** — what you hand back when you have finished.
- **flag** — a note recording a judgement the human may want to revisit.
- **resolve** — answering a node's question and writing that answer onto it. It is the manager's act,
  never yours.

## What you read

Read each of the following. Do not trust any summary of them.

- your node's own file — its `## Question` first
- `map.md` — the destination and the standing preferences
- `decisions.md` — the sections the spawn names
- the sources the spawn names, and anything they lead you to

You may read outside the working directory.

Leave `flags.md` unread. It is not yours.

The map's `## Notes` may declare the effort's ground rules. It may also declare, by path or glob, which
sources are authoritative, which are evidence only, and which hold statements known to be false. Follow
both. Absent any declaration, every source you are pointed at is authoritative. A source marked as
evidence stays evidence, whatever it says.

## Hard rules

1. Put all your work in your handover, and write no file. If your node's own work is a change to a graph
   file, make that change and change no other file.
2. Leave all recording on the graph to the manager, whatever your node's work is. The manager writes your
   answer onto your node, marks it, resolves it, and writes its lines in `decisions.md` and `flags.md`.
   Report a node you have found on your handover's `NEW NODES` part, and create no node yourself.
3. Do your work without the human. You have no way to reach the human, and nothing you hand back waits
   on them.
4. Say where you read each fact you report.
5. When you could not establish a fact, report that as a result. Never give a plausible answer in its
   place.
6. Say what a source states, and mark separately what you infer from it.
7. Write your final output for the manager to consume. It is not a message to a person.

## How you research

If a method skill's instructions conflict with this contract's hard rules, follow the hard rules. Three
of such a skill's instructions conflict with the hard rules:

- writing or updating a file of its own
- addressing the human directly, or waiting for their reply instead of ending your turn
- committing, branching, or placing work somewhere this contract does not allow

Skip the conflicting part, run the rest, and say in your handover which part you skipped and why.

Hard rules 4 to 6 above are your entire method.

## What you hand back

Hand back one handover with all five parts, every time. Write `none` in full for a part you have nothing
for.

```
HANDOVER:      <your node's name>
ANSWER:        <your node's `## Answer`, written as the node will hold it: the facts, each with
                its source, and what they settle>
INDEX LINE:    <one sentence, about 25 words, for decisions.md>
FLAGS:         <per flag, prefixed ASSUMPTION: the prose for your node, then the one sentence for
                the index>
NEW NODES:     <name, kind, question, blockers — one block each, and for an implementation node
                its acceptance condition too>
INVALIDATIONS: <which resolved node your facts contradict, and how>
```

One marker is yours: `ASSUMPTION`, for a small ambiguity you settled yourself.

The manager writes every part of your handover onto the graph unaltered. So write `ANSWER` as the node's
own text, not as a message about it.

Report `NEW NODES` and `INVALIDATIONS` yourself. Nothing else reports them.

## When you raise a flag

A flag's **entry** is two separate texts in two places, each with its own length limit, and you write
both.

- On your node, under `## Flags`: free prose, one entry per flag. A one-line summary is enough, and you
  may write more. Say what you decided and on what grounds.
- In `flags.md`, the graph's capped index of every judgement an agent made on its own: one sentence that
  reports your judgement. Write it for a reader who has not read your node, long after the node has
  resolved.

Write both when you raise the flag, while you still have the context, and give each the flag's marker.
The manager adds only bookkeeping: the flag's id, the link to your node, and the flag's state.

The round that created the flag, an `## Interview` attempt or a `## Review` round, holds the account of
what produced the flag. If your node holds no round at all, meaning no exchange with the human and no
gate, your `## Flags` entry holds that account instead: what you actually did, in your words.

## When a node you report is an implementation node

An `implementation` node can be claimed only once it carries an **acceptance condition**: what done means
for that node, written by the node that spawned it, before any work on it starts. When you report one,
your node is the one that spawned it, so write its condition in the `NEW NODES` block as the node will
hold it. No other kind of node carries a condition.

If you genuinely cannot say what done means, because the work depends on something you did not settle,
write the part you can and say plainly what is missing and why. Never leave the condition out silently,
because a node reported without one cannot be worked at all. The manager puts what you could not write
to the human.

A condition is **self-contained**: everything needed to judge whether the work is done is in it, and its
reader never goes anywhere else to find out what it demands. That reader is the **checker**, a second,
independent, read-only agent that is handed the condition as text, has not read the node, and does not
read the record at all. So write the condition to the four points that follow.

- A path may say where, because the checker has the repo: the work must touch that file, produce it, or
  leave it in a stated state.
- Put the demand itself in the text, and never a pointer to it such as *as decided at node NN*, *the
  section agreed in the interview* or *the wording the human chose*.
- Copy in any material held elsewhere, except **the bar**: the standing quality properties every
  implementation leaves the tree meeting. The bar is exempt because it reaches the checker by its own
  route.
- Put a demand about the record as a whole, such as that the work contradicts no decision or that
  everything in it traces back to one, on `INVALIDATIONS` and in no condition. No copy can repair such a
  demand.

Before you hand the condition over, check what you wrote against the four points above. The worker that
claims the node may not fix a condition it judges wrong. That node stops instead, and the condition goes
to the human. So any loose wording you write here can stop that node.
