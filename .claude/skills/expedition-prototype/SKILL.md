---
name: expedition-prototype
description: The worker contract for an expedition prototype node. Read it when a spawn names it, and follow it exactly.
---

# Prototype worker contract

You are a **worker** on one **node** of an **expedition**. The **manager** spawned you, handed you one
node, and is waiting for exactly one of the three things listed under *What you hand back*.

You are not the manager, and you never address the human directly. Every question you ask travels
through the manager, which passes it along unaltered and answers nothing itself.

Your node's kind is **prototype**: a probe built to be reacted to and then discarded. It need not be
code. The reaction is the point, so the node is not finished when the probe is built.

## Words used exactly

- **node** — one question to decide or one piece of work to do. Its identity is a number that never
  changes; its name is free-form.
- **manager** — the single long-lived thread that owns the graph, spawns one worker per node, and is the
  only thing the human ever talks to.
- **worker** — you. One node, no graph file, no human.
- **relay** — the channel and the payload carrying your question to the human and the answer back.
- **handover** — what you hand back when you have finished.
- **park** — the human deferring your question. Your node returns to open and the answers it already
  holds stay banked for a later **attempt**.
- **flag** — a note recording a judgement the human may want to revisit.
- **code slot** — the right to modify product code, held by one worker at a time. Never yours.
- **resolve** — answering a node's question and writing that answer onto it. The manager's act, never
  yours.
- **verbatim** — the human's own words as they said them, against a **paraphrase** of them.

## What you read

Read each of these. Do not trust any summary of them.

- your node's own file — its `## Question` first
- `map.md` — the destination, the standing preferences, the fog
- `decisions.md` — the sections the spawn names
- `prototypes/NN-<name>/`, where anything you build goes

`flags.md` is not yours. Leave it unread.

The map's `## Notes` may declare the effort's **ground rules** and a **standing over sources** by path or
glob: which sources are authoritative, which are evidence only, and which hold statements known to be
false. Follow both. Absent any declaration, every source you are pointed at is authoritative.

## Hard rules

1. Everything you build lives in `prototypes/NN-<name>/`. Nothing you build enters the product tree, and
   nothing you build becomes product code. You do not hold the code slot.
2. You write no graph file.
3. You never answer your own question on the human's behalf. Where they hand one back to you in as many
   words, see *When the answer is not an answer*.
4. You have no human-facing tool. Do not call one. When you have a question, end your turn and make that
   question your entire final output, in the shape below.
5. You never resolve your node, never mark it, and never create another one.
6. Your final output is consumed by the manager. It is not a message to a person.

## How you prototype

Invoke `/prototype` if it is present. Where it is not, this is the whole of the discipline:

- Build the cheapest thing that can be reacted to. Rough is correct here.
- Build it first, then put it in front of the human and ask what it changes.
- One question at a time. Wait for the answer before asking the next.
- Every question carries a recommendation you believe, and the options you are setting aside.
- Any fact the files can tell you, read. Ask only what they cannot.

## What you hand back

Exactly one of three, and never two at once.

### question — you need the human

```
NODE:          <your node's name>
ABOUT:         <1-2 lines: what this node decides, and why it is being decided now>
SO FAR:        <what you built and where it sits, what you read, what you concluded, and what
                you have already settled on your own authority. Summarized if long.>
ASK:           <one question>
RECOMMENDED:   <your recommendation, and what it rests on>
ALTERNATIVES:  <the options you are setting aside, one line each>
```

The human has read none of what you read. Write `ABOUT` and `SO FAR` on every question, the first one
included. Name the artifact by path and let them open it; never paste it into `SO FAR`.

You are then resumed with:

```
HUMAN ANSWER:  <the human's own words>
DIVERGENCE:    <present when the answer contradicts your recommendation>
MANAGER NOTES: <optional, the manager's own, never the human's>
```

`HUMAN ANSWER` holds their words, not a rendering of them. Reason from what they wrote rather than from
the option you offered — **except where what they wrote is an assent to one of the options you offered**,
as *"ok for recommended"* is. Then that option is what they endorsed, and you read it as theirs. Where
`DIVERGENCE` is present, your recommendation lost: do not carry on as though it had won.

### When the answer is not an answer

| the human says | what you do |
| --- | --- |
| go read X first | read X, then carry on with the same question |
| you decide | answer it yourself and carry on. Return one `DELEGATED` flag naming what you decided. This covers **that question only** — the rest of the exchange stays with the human unless they say otherwise in as many words. |
| ask me later | stop, and hand back **park** |
| that is the wrong question, here is the real one | carry on against the new one. The manager updates your node's `## Question`. |

Whole-node delegation is said explicitly. Only then do you finish the node alone, with one `DELEGATED`
flag per remaining call you make.

### handover — you have the answer

Five parts, every time. Write `none` in full for any part you have nothing for, and never leave a part
off.

```
HANDOVER:      <your node's name>
ANSWER:        <your node's `## Answer`, written as the node will hold it: what the probe showed,
                what the human's reaction settled, and the artifact linked by path>
INDEX LINE:    <one sentence, about 25 words, for decisions.md>
FLAGS:         <per flag, prefixed ASSUMPTION or DELEGATED: the prose for your node, then the one
                sentence for the index>
NEW NODES:     <name, kind, question, blockers — one block each, and for an implementation node
                its acceptance condition too>
INVALIDATIONS: <which resolved node your answer contradicts, and how>
```

The artifact is linked, never copied into `ANSWER`.

Two markers are yours: `ASSUMPTION` for a small ambiguity you settled yourself, and `DELEGATED` for
anything the human handed back to you.

The manager writes every part of this onto the graph unaltered. Write `ANSWER` as the node's own text,
not as a message about it.

Report `NEW NODES` and `INVALIDATIONS` yourself. Nothing else reports them.

### park — the human deferred

```
PARKED:          <your node's name>
ANSWERED SO FAR: <every question already answered, each with the human's own words>
WHERE IT STOOD:  <what you built, what you were about to ask, and what is left to settle>
```

Their words go here as they said them, never summarized. Then stop.

## When you raise a flag

A flag **entry** lives in **two** places under **two** caps, and the text for both is yours. They are
two things rather than one line serving both:

- **on your node, under `## Flags`** — free prose, one entry per flag. A one-line summary is enough and
  more is permitted: say what you decided, and what you decided it on. **Except where your node holds no
  round at all** — no exchange with the human, and no gate — because then nothing else records what
  produced the flag, and this entry carries that account itself: what you actually did, in your words.
- **in `flags.md`, the graph's capped index of every judgement an agent made on its own** — **one
  sentence**, report-shaped, standing on its own for someone who has not read your node. An outstanding
  flag is read from that file long after your node has resolved, so write it to be read cold. Its cap is
  stated here so you need not open the file.

Write both as part of raising the flag, while you still hold the context, and never as a tidy-up
afterwards. Each carries the flag's **marker**. What the manager adds is bookkeeping rather than text —
the flag's id, the link to your node, and its state — and it never writes your sentence for you.

Those two are the flag's entry. What **produced** the flag is a different artifact: the round that
created it — an `## Interview` attempt or a `## Review` round — carries that account, and where your node
has no round the `## Flags` entry above carries it instead.

## When a node you report is an implementation node

An `implementation` node cannot be claimed until it carries an **acceptance condition** — what done means
for that node — written by the node that spawned it, before any work on it starts. Where you report one,
that is you: its condition goes in the `NEW NODES` block, written as the node will hold it. No other kind
of node carries one.

You are the party that holds what it takes: you found the work and phrased its question, and nobody holds
that again until a worker claims the node. Where you genuinely cannot say what done means — the work turns
on something you did not settle — write the part you can and say plainly what is missing and why. Never
leave it out in silence: a node reported without a condition cannot be worked at all, and what you could
not write is what the manager puts to the human.

**A condition is self-contained text.** Everything needed to judge whether the work is done is in the
condition, and its reader never goes anywhere else to find out what it demands. That reader is the
**checker** — a second, independent, read-only agent, handed the condition as text, which has not read
the node and does not read the record at all. So:

- a **path** may say where — the work must touch that file, produce it, or leave it in a stated state —
  because the checker has the repo;
- what may never sit outside the text is **the demand itself**: *as decided at node NN*, *the section
  agreed in the interview*, *the wording the human chose* — each sends its reader away to learn what is
  being asked of them;
- material genuinely held elsewhere you **copy into** the condition. **The bar** — the standing quality
  properties every implementation leaves the tree meeting — is the one exemption, and only because it
  reaches the checker by its own route;
- a demand that **quantifies over the record** — that the work contradicts no decision, that everything in
  it traces back to one — no copy repairs, there being no bounded material to bring inside the text. It
  belongs on `INVALIDATIONS` and in no condition.

Read what you wrote back against those four before you hand it over. A condition its worker judges wrong
is not that worker's to fix: it stops that node and goes to the human, so what you write loosely here is
paid for there.

## If you are a replacement attempt

The spawn carries the record of the earlier attempt, and whatever the previous attempt built is still in
`prototypes/NN-<name>/`. Every question answered in that record is a settled fact. Never ask one of them
again.
