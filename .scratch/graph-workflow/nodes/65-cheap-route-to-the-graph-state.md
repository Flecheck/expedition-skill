# A worker has no cheap route to the graph's live state

Type: grilling
Status: out-of-scope

## Question

A worker that needs to know **what the graph currently holds** — which nodes exist, which are open, which
resolved, what each one is about — is offered exactly one route: `map.md`. That file is a **low-resolution index
written by the manager**, and [Restructure `map.md` to what every worker needs](59-restructure-the-map.md) has just
demonstrated it cannot be trusted for the purpose.

**The evidence, from that node's worker in its own words:**

> The current state of the graph, needed to write nine fog items truthfully. `map.md`'s own fog said the manager's
> skill was *"down to two blockers, nodes 15 and 16"* — both have since resolved, and a node for that skill still
> does not exist. I looked in the map first, because that is what the item is; the authoritative answer was one
> `ls nodes/*.md` plus a grep of `Type:`/`Status:`/first line, **which is cheap and which nothing pointed me at.**

So the expensive route is stale by construction — the map is written by hand and its statements about the graph age
the moment a node resolves — while the cheap route is exact, costs two commands, and exists in no shipped file.

**What is at stake, and why it is not merely a convenience.** Every node file's `Blocked by:` and every fog item's
node links are statements about the graph that some worker will read as current. Node 59's worker caught one stale
one because it happened to be writing that very item; a worker reading it in passing would have carried it into its
work. The manager's own errors this session were the same shape: three stale figures in one condition preamble,
because nothing re-derived them.

## What has to be decided

1. **Whether the cheap route belongs in the shipped files at all**, given ground rule 1 — *nothing in the shipped
   files may assume this repo, this machine, or a toolchain.* `ls` and `grep` are a toolchain assumption in the
   strict reading; the rule's own second sentence — *prefer properties that are discovered over commands that are
   declared* — may be the way through, by naming the **property** (each node file's first lines carry its type and
   status) and leaving the command to whoever runs it.
2. **Which files it goes in.** A worker contract reaches every worker but repeats the text six times; the
   conventions document says it once and is read by nobody who has not been sent there.
3. **Whether the map should stop making statements about the graph** that the node files already answer, which
   would be a preference rather than a mechanism, and which overlaps [Say in the conventions document how the map
   and its history are written](64-conventions-say-how-the-map-is-written.md).
4. **Whether this is instead the manager's job** — the spawn stating the graph facts the node depends on, freshly
   derived, so no worker ever reads the map for them. That is the cheapest for the worker and the most expensive
   for the manager, which is the trade this effort has now met four times.

## Where it came from

Reported by node 59's worker in the first retrospective filed under the human's standing instruction. The manager
judged the other three answers of that retrospective actionable without a node — two were the manager's own filing
discipline, one was a stale figure — and this one not: it is a gap with no owner, and deciding it means choosing
between four places to put the fix.

## Ruled out of scope, 2026-09-29

*The manager's note:* under the human's answer to [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q2 (`verbatim`: *"ok"*). Its line in `map-manager-only.md`'s `## Out of scope` is node 366's worker's text.
