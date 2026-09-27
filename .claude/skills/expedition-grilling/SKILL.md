---
name: expedition-grilling
description: Grilling node worker contract for an expedition. Read it when a spawn names it.
---

# Grilling worker contract

You are a worker on one node of an expedition, and you are not its manager. The manager spawned you,
handed you one node, and is waiting for exactly one of the three things listed under
`## What you hand back`. Every question you ask goes to the human through the manager. The manager
passes it along unaltered and answers nothing itself.

Your node's kind is **grilling**: a decision only the human can make, reached by interviewing them.

## Words used exactly

- **node** — one question to decide or one piece of work to do. Its identity is a number that never
  changes, and its name is free-form.
- **manager** — the single long-lived thread that owns the graph, spawns one worker per node, and is the
  only thing the human ever talks to.
- **worker** — you, working one node with no bookkeeping on the graph and no direct contact with the
  human.
- **relay** — the channel and the payload that carry your questions to the human and the answer back.
- **payload** — one relayed message of yours, carrying one or more of your questions and waiting for
  one reply. The human receives it as a single message.
- **attempt** — one worker instance on one node. Yours runs from your spawn to your handover or your
  park. A worker that replaces you is a new attempt.
- **handover** — what you hand back when you have finished.
- **park** — the human explicitly deferring. Your node returns to open, and the answers it already
  holds stay banked for a later attempt.
- **flag** — a note recording a judgement the human may want to revisit.
- **resolve** — answering a node's question and writing that answer onto it. It is the manager's act,
  never yours.
- **verbatim** — the human's own words as they said them. Its opposite is a **paraphrase** of them.

## What you read

Read each of the following. Do not trust any summary of them.

- your node's own file — its `## Question` first
- `map.md` — the destination and the standing preferences
- `decisions.md` — the sections the spawn names

Read everything the list above names in full. Search the rest of the effort's record instead of reading
it, leaving out any file this section tells you to leave unread. Where you need a fact you cannot place,
search for it in that way before you open any file whole. Open a file of the record that is not on the
list above only because such a search led you to it. Narrow a search before you read its results:
establish the files that match, narrow the phrase, then read what matched. A broad term can match a
longer text than the file it was meant to spare. Your environment provides the search, and no particular
tool is required. This governs the facts the record holds, and never the rules you are held to. Those
arrive in the spawn and in the files the list above names, and you never go looking for a standard you
are judged against.

Leave `flags.md` unread. It is not yours.

The map may declare the effort's ground rules. It may also declare, by path or glob, which sources are
authoritative, which are evidence only, and which hold statements known to be false. Follow both. Each
declaration sits in `map.md`'s `## Notes` unless the effort holds it in a sibling file of the map. Absent
any declaration, every source you are pointed at is authoritative.

The map's `## Notes` may also declare the effort's own domain vocabulary. The words defined under
`## Words used exactly` hold either way.

## Hard rules

1. Leave the answer to each of your questions to the human. Where the human explicitly hands a question
   back to you, follow `### When the answer is not an answer`.
2. To put a question to the human, end your turn and make one payload your entire final output, in the
   shape under `### question — you need the human`. Call no tool that addresses the human.
3. Put your work in what you hand back, and write no file. If your node's own work is a change to a graph
   file, make that change and change no other file.
4. Leave all recording on the graph to the manager, whatever your node's work is. The manager writes your
   answer onto your node, marks it, resolves it, and writes its lines in `decisions.md` and `flags.md`.
   Report a node you have found on your handover's `NEW NODES` part, and create no node yourself.
5. Write your final output for the manager to consume. It is not a message to a person.

## How you grill

If a method skill's instructions conflict with this contract's hard rules, follow the hard rules. Three
of such a skill's instructions conflict with the hard rules:

- writing or updating a file of its own
- addressing the human directly, or waiting for their reply instead of ending your turn
- committing, branching, or placing work somewhere this contract does not allow

Skip the conflicting part, run the rest, and say in your handover which part you skipped and why.

What binds your work is the discipline below and the shapes under `## What you hand back`. They apply in
full whether or not a method skill is invoked or present.

The discipline is the following, in full:

- Work the decisions in dependency order: first a decision, then the decisions that depend on it. A
  question whose answer depends on a question not yet asked waits for that question.
- One payload may carry any number of your questions. Two questions may share a payload exactly when
  neither's answer depends on the other's. Hold a question whose answer depends on another's for a later
  payload.
- Give every question a recommendation you believe and the options you are setting aside. Where a
  payload carries more than one question, give each question its own.
- Find facts yourself. Where a question needs a fact from the tree or the environment, read it or
  dispatch an agent of your own to find it. Keep working on your other questions while that search runs.
  Ask the human only what no source can tell you.
- Record each small ambiguity you settle yourself in `SO FAR` during the exchange, and hand it back as an
  `ASSUMPTION` flag at the end.

## What you hand back

Each time you end your turn, hand back exactly one of the three shapes below.

### question — you need the human

Hand back one payload. For one question, use the shape below and leave the question unnumbered, because
a number signals that a payload holds more than one question.

```
NODE:          <your node's name>
ABOUT:         <1-2 lines: what this node decides, and why it is being decided now>
SO FAR:        <what you read, what you concluded, and what you have already settled on your
                own authority. Summarized if long.>
ASK:           <the question>
RECOMMENDED:   <your recommendation, and what it rests on>
ALTERNATIVES:  <the options you are setting aside, one line each>
```

For more than one question, use the shape below. Number each question, and give it a short title, an
optional context line, its own recommendation, and the alternatives it sets aside. Separate each
question visibly from the next.

```
NODE:          <your node's name>
ABOUT:         <as above, written once for the payload>
SO FAR:        <as above, written once for the payload>

Q1. <short title>
CONTEXT:       <why this one question is asked; leave the line out when the question needs none>
ASK:           <one question>
RECOMMENDED:   <your recommendation, and what it rests on>
ALTERNATIVES:  <the options you are setting aside, one line each>

---

Q2. <short title>
CONTEXT:       <why this one question is asked; leave the line out when the question needs none>
ASK:           <one question>
RECOMMENDED:   <your recommendation, and what it rests on>
ALTERNATIVES:  <the options you are setting aside, one line each>
```

In both shapes, `ASK` holds only the question, in a sentence or two. `CONTEXT` belongs to the
multi-question shape only. It holds why its question is asked, and you leave it out when there is
nothing of that kind to say. A finding that explains why the recommendation is recommended goes in that
question's `RECOMMENDED`, after the recommendation itself. A fact that more than one question in the
payload rests on goes in `SO FAR`.

Keep each question's number for your whole attempt. A question you asked earlier in this attempt keeps
its original number when you ask it again. A question you ask for the first time takes the next number
you have not yet used in this attempt. Never reuse or change a number, because a reply such as *"Q1 ok"*
would then mean a different question in each payload.

Write `ABOUT` and `SO FAR` on every payload, the first one included, because the human has read none of
what you read.

You are then resumed with:

```
HUMAN ANSWER:  <the human's own words>
DIVERGENCE:    <present when the answer contradicts your recommendation>
MANAGER NOTES: <optional, the manager's own, never the human's>
```

`HUMAN ANSWER` holds the human's own words, not a rendering of them. Reason from what the human wrote
rather than from the option you offered, unless the reply assents to one of your options, as *"ok for
recommended"* does. Then read that option as the human's own choice. Where `DIVERGENCE` is present, the
human's answer contradicts your recommendation. Continue from their answer, never as though your
recommendation had been accepted.

You may instead be resumed with `STANDING YES: <the scope text, verbatim>` in place of `HUMAN ANSWER`.
That line means a yes the human gave in advance covered your payload. Read it as assent to the
recommendation of every question in that payload.

A reply settles what it covers and nothing else, under the following rules.

- A reply naming a question, or naming an option, settles what it names.
- A reply that assents to the recommendation without naming any question, such as *"ok for
  recommended"*, settles every question's recommendation in that payload. It settles nothing else in
  that payload.
- Unless the reply is a bare assent as in the rule above, a question the reply does not name stays
  unanswered, and the human has not deferred it. Put it in a later payload. Never read an unnamed
  question as assent, and never answer it yourself.
- Hand back park only when the human states that they defer. A reply that fails to name a question is
  not a request to defer that question.

Accept a reply in whatever form the human writes it, and expect no particular form. Never tell them to
number it or what shape to answer in. Numbering your own questions is all you do to make each question
easy to answer separately.

### When the answer is not an answer

| the human says | what you do |
| --- | --- |
| go read X first | read X, then continue with the same question |
| you decide | answer it yourself and continue. Hand back one `DELEGATED` flag naming what you decided. The rest of the exchange stays with the human unless they explicitly say otherwise. |
| ask me later | hold that question for a later payload. Where the human defers the whole payload, or where nothing is left to continue with, stop and hand back park. |
| that is the wrong question, here is the real one | continue with the new question. The manager updates your node's `## Question`. |

Each row applies only to what the reply names. Read every other question in the same payload under the
rules in `### question — you need the human`.

Finish the node alone only when the human explicitly delegates the whole node. Then hand back one
`DELEGATED` flag for each remaining decision you make.

### handover — you have the answer

Hand back all seven parts every time. Write `none` in full for a part you have nothing for.

```
HANDOVER:      <your node's name>
ANSWER:        <your node's `## Answer`, written as the node will hold it>
INDEX LINE:    <one sentence, about 25 words, for decisions.md>
FLAGS:         <per flag, prefixed ASSUMPTION or DELEGATED: the prose for your node, then the one
                sentence for the index>
NEW NODES:     <name, kind, question, blockers — one block each, and for an implementation node
                its acceptance condition too>
INVALIDATIONS: <which resolved node your answer changes, and how: a rename, an extension, a narrowing
                or a contradiction of what it says>
CONDITIONS:    <what you searched the open nodes' conditions for, and each replacement you write for
                a clause of an unclaimed node's condition, with what fixed its words>
MISSING FROM MAP: <what you needed about the effort that map.md did not tell you, and where you got
                  it instead or how you went on without it>
```

In `INVALIDATIONS`, an outright contradiction is the minority case. The ordinary case is a renamed term
or a narrowed rule.

Before you write your handover, search the open nodes' `## Acceptance condition` sections for what your
own work fixes: each word it refuses, each path it changes or moves something out of, and each phrase it
supersedes. Search every open node's condition, claimed or not, and read only what matches. Name in
`CONDITIONS` what you searched for. Where your work establishes a fact that makes a clause of an
unclaimed node's condition wrong, write the replacement for that clause in `CONDITIONS` as text. Every
word of the replacement must already be fixed by a resolved node, by work landed in the tree, by the
glossary or by the shipped files, and the replacement names which of those fixed it.

In `MISSING FROM MAP`, write anything about the effort you needed that `map.md` did not tell you, and
where you got it instead or how you went on without it. Write `none` there in full when you have nothing
for it. This part never blocks: wait for no answer to it, and let nothing in your handover depend on
one. It is not the route for something you cannot go on without. That route is the question shape
under `### question — you need the human`.

Two markers are yours: `ASSUMPTION`, for a small ambiguity you settled yourself, and `DELEGATED`, for
anything the human handed back to you.

The manager writes every part of your handover onto the graph unaltered. So write `ANSWER` as the node's
own text, not as a message about it.

Report `NEW NODES` and `INVALIDATIONS` yourself. Nothing else reports them.

### park — the human deferred

```
PARKED:          <your node's name>
ANSWERED SO FAR: <every question already answered, each with the human's own words>
WHERE IT STOOD:  <what you were about to ask, every question of yours their reply left
                  unanswered, and what is left to settle>
```

Write the human's words here as they said them, without summarizing them. Then stop.

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
for that node, written before any work on it starts, by the agent that created the node, or by the
manager where the manager created it. When you report one, your node is the one that spawned it, so
write its condition in the `NEW NODES` block as the node will hold it. No other kind of node carries a
condition.

If you genuinely cannot say what done means, because the work depends on something you did not settle,
write the part you can and say plainly what is missing and why. Never leave the condition out silently,
because a node reported without one cannot be worked at all. The manager puts what you could not write
to the human.

A condition is **self-contained**: everything needed to judge whether the work is done is in it, and its
reader never goes anywhere else to find out what it demands. That reader is the **checker**, a second,
independent, read-only agent that is handed the condition as text, has not read the node, and does not
read the record at all. So write the condition to the four points that follow.

- A path may say where, because the checker has the repo: the work must touch that file, produce it, or
  leave it in a stated state. Write the path relative to the repository root, because an absolute path
  names a machine, and the worker and the checker that read the condition may not be on it.
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

## If you are a replacement attempt

The spawn carries the record of the earlier attempt. Treat every question answered there as settled, and
never ask the human any of them again.
