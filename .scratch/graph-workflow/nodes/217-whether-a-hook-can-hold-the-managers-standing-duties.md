# Whether a harness hook can hold the manager's standing duties across a compaction

Type: research
Status: resolved

Blocked by: none

## Question

*Asked by the human, in their own words, in the same message that answered [node
212](212-the-mint-on-second-report-rule-is-defeated.md)'s three questions.*

> It might be the compaction that is causing issues with the rules of the map (here retrospecive and the rule to
> give thing to the user and the rule to spawn tasks after one finish), is there a way of adding a hook to keep the
> map instructions ?

**The three duties they name, each of which the manager has missed:**

1. **Filing the retrospective** — missed on every one of the last eleven resolved nodes, node 212's `Q3.` having
   just settled that filing folds into resolving.
2. **Putting things in front of them** — the manager queued a node's banked questions behind a landing that asked
   nothing of them, an ordering no rule states, recorded at [node
   216](216-what-a-correction-round-after-a-rebase-conflict-owes.md).
3. **Topping up a slot when a node finishes** — their own standing instruction, and the manager waited for a whole
   round of gates before starting replacements until they corrected it.

**What this node establishes**, and it is a fact about the harness rather than a decision: **what hook events the
harness offers, which of them fire when context is rebuilt after a compaction, what each can inject into the
manager's context, and what that injection costs per occurrence.** Whether to use one, and what text it would
carry, is a decision for whoever reads this node's answer.

## The manager's note at filing

*Not a change to anything above. The manager is the party whose failures are this node's subject, so its own view
is marked and kept out of the question.*

**The diagnosis is plausible and the evidence is mixed, and the manager will not settle it for them.** Against
compaction being the cause: duty 3 was missed *before* this session's compaction, and duty 1 has been missed across
eleven nodes and several sessions, so no single context loss explains it. For compaction: duty 2 was invented in
the turn after a compaction, and the manager's own contract calls its context *"the resource that fails first"*.

**What the three have in common is a shape rather than a cause.** Each is a duty that fires at a moment nothing
marks — after a node resolves, after a payload arrives, after a slot frees. **Node 212's `Q3.` answer repairs one
of the three by removing the separate later act**, folding the filing into the edit that resolves the node, and
that repair needs no hook. Whether the other two can be repaired the same way, or need the harness, is what this
node's answer will inform.

**Ground rule 1 keeps whatever this finds out of the shipped files.** A hook is one harness's mechanism, and no
shipped contract may assume one; anything built on this answer is this effort's own practice.

## Flags

*The worker's own text, pasted. The id is the manager's bookkeeping and nothing else.*

`217.1` **· outstanding** `ASSUMPTION` — **SessionStart source field contains "compact" vs other values without further subdivision.** The matcher values `startup`, `resume`, `clear`, `compact`, `fork` are stated as mutually exclusive options, and no subdivision of "compact" into manual/auto is documented for SessionStart, though PreCompact and PostCompact matchers do support `manual`/`auto`. The SessionStart event schema input does not specify a field that would allow a hook to determine whether "compact" compaction was manual or automatic.

## Answer

*Pasted as the worker wrote it. Sources are named in its own text; the manager verified none of them and
adds its corroboration below as its own marked note.*

**What hook events the harness offers and what triggers each.**

The Claude Code harness provides 30+ hook events. The ones relevant to context rebuilds and standing duties are:

1. **`SessionStart`** (fires "when a session begins or resumes"): The matcher field accepts `startup`, `resume`, `clear`, `compact`, or `fork`. With matcher `"compact"`, the hook fires after context compaction when the session resumes.

2. **`PreCompact`** (fires "before context compaction"): Matcher values are `"manual"` or `"auto"` to distinguish user-initiated vs automatic compaction.

3. **`PostCompact`** (fires "after context compaction completes"): Same matchers as PreCompact.

4. **`InstructionsLoaded`** (fires "when a CLAUDE.md or `.claude/rules/*.md` file is loaded into context"): Matcher values include `session_start`, `nested_traversal`, `path_glob_match`, `include`, and `compact`, the last of which fires when a rules file is loaded during compaction recovery.

**Source:** hooks-guide.md (lines 313-515) and hooks.md table of event lifecycle.

---

**Which hooks fire on context rebuild and whether they distinguish compaction from cold start.**

`SessionStart` with matcher `"compact"` fires after compaction when a session resumes. The documentation states at line 313: "When Claude's context window fills up, compaction summarizes the conversation to free space. This can lose important details. Use a `SessionStart` hook with a `compact` matcher to re-inject critical context after every compaction."

`PreCompact` and `PostCompact` both support matchers `"manual"` and `"auto"` to distinguish the compaction trigger (hooks.md matcher table, line 693-697).

**What the documentation does not establish:** SessionStart with matcher `"compact"` does not subdivide into `manual` vs `auto`. A hook cannot distinguish cold startup from session resume using only the SessionStart event. **Inference:** To detect whether a context rebuild is from compaction vs another resume source, a hook would need to distinguish "compact" source from other `SessionStart` sources; the documentation provides no method to subdivide "compact" by whether it was manual or automatic compaction. The matcher values are `startup`, `resume`, `clear`, `compact`, `fork` with no further breakdown of `compact`.

**Source:** hooks-guide.md line 313-337 for the compaction-recovery example; hooks.md matcher table for all event types.

---

**What each hook can inject into the agent's context.**

**SessionStart hook with plain-text stdout:**
When a hook writes plain text to stdout on events including `SessionStart`, the hooks-guide explicitly states (line 606): "For `UserPromptSubmit`, `UserPromptExpansion`, `SessionStart`, and `PostModelSwitch` hooks, Claude Code adds stdout it treats as plain text to Claude's context."

The example at lines 322-335 shows a `SessionStart` hook with matcher `"compact"` that echoes a reminder string; that text is added to Claude's context. **The injection is into the model's input context, not merely displayed to the user.**

**PreCompact and PostCompact hooks:**
The documentation does not state what these hooks can inject. The event is used for blocking compaction (exit code 2) or async reaction, not for context injection. PreCompact can return `systemMessage` (field name in structured JSON output), but the documentation at line 15 and in the reference states `systemMessage` is "discarded on many events" without enumerating which events preserve it.

**systemMessage field:**
Available as a JSON output field on many events, but hooks-guide.md notes this field is delivered inconsistently across event types. The documentation does not specify whether PreCompact or PostCompact preserve it.

**additionalContext field:**
Available on `UserPromptSubmit` (hooks-guide.md line 647-657) and some tool-decision events, but not listed as available for SessionStart or compaction-related events.

**Source:** hooks-guide.md lines 313-337, 606, 615-660; hooks.md output schema (implied but not fully enumerated per event).

---

**What the injection costs.**

**Per-occurrence cost:** SessionStart hooks fire once per session lifecycle event that matches the trigger. A SessionStart hook with matcher `"compact"` fires once per context compaction, when the session resumes.

**No documented billing or token cost:** The documentation does not specify a token cost or billing model for hook execution or context injection. Hooks are presented as utility features without explicit token accounting.

**No documented size limits:** The documentation does not specify maximum output size for hook stdout or JSON fields. The hooks-guide discourages large text output at line 954 ("Hook timeouts vary by type...") and notes hook output is read from stdout/response, but no explicit limit is stated. Best practice implied: keep hook output minimal.

**Source:** hooks-guide.md lines 313-337 (example uses `echo` with a short reminder), 606-607 (exit code 0 behavior), 954 (limitations and timeouts, which do not mention size limits).

---

**Limits on holding standing instructions in a long-lived agent.**

1. **SessionStart "compact" matcher cannot distinguish manual from automatic compaction.** A hook cannot branch logic based on whether compaction was triggered by the user or by the harness reaching a token limit. Both fire the same matcher.

2. **SessionStart hook fires once per compaction.** Text injected by a hook reaches the model's context once and is then subject to normal compaction. On the next compaction, the hook fires again, re-injecting the text. This is not a persistent mechanism: the text does not survive compaction; it is re-injected after each one. **Implication:** If the manager's standing duty is to keep an instruction in front of it across every turn, a hook re-injecting on every compaction does not solve it; the instruction disappears between compactions.

3. **PreCompact and PostCompact hooks do not inject context.** They can block or react to compaction, but the documentation provides no mechanism for them to inject text that Claude will see during its reasoning.

4. **Hooks cannot modify the agent's own future state.** A hook fired after compaction resumes cannot write instructions to disk in a way that the manager would then read as part of its own standing knowledge; it can only inject text into the current context.

**Source:** hooks-guide.md (no method to persist across turns between compactions); hooks.md (no injection capability documented for PreCompact/PostCompact).

---

**Non-hook mechanisms that do the same job better or worse.**

**CLAUDE.md file auto-reload (better for this purpose):**
The memory.md documentation states (middle section under "Instructions seem lost after `/compact`"): "Project-root CLAUDE.md survives compaction: after `/compact`, Claude re-reads it from disk and re-injects it into the session."

This is built-in harness behavior, not a hook. When the session resumes after compaction, the harness automatically re-reads any CLAUDE.md file in the project root and re-injects it. **This applies to both manual and automatic compaction.** The mechanism requires no configuration beyond writing the CLAUDE.md file.

**Advantage over hooks:** 
- CLAUDE.md persists across all compactions automatically, without needing to fire and return output on each lifecycle event.
- No hook timeout or output-size constraints apply.
- Works on every compaction (manual or auto) without the hook being able to distinguish them.

**Disadvantage:** 
- Must be on disk and in the project root (or ancestor directory in CLAUDE.md load order).
- Content loaded at the start of every session and re-read after compaction, so large files consume context.
- Not dynamic: cannot branch based on session state.

**Source:** memory.md sections "How CLAUDE.md files load" and "Instructions seem lost after `/compact`".

**InstructionsLoaded hook (alternative for dynamic response):**
This hook fires "when a CLAUDE.md or `.claude/rules/*.md` file is loaded into context" with matcher `compact` available. Could theoretically be used to react when instructions are re-loaded after compaction, but does not provide a mechanism to inject new instructions; it only observes that loading has happened.

**Source:** hooks.md, line 503; hooks-guide.md.

---

**Summary: Whether a hook can hold the manager's standing duties.**

A `SessionStart` hook with matcher `"compact"` **can** inject instructions into the agent's context after each compaction. However:

1. **It fires once per compaction, not once per turn.** Instructions injected by a hook after compaction will disappear during the next round of compaction. They are not held continuously.

2. **The harness cannot distinguish manual from automatic compaction at the SessionStart level.** A hook cannot route different instructions based on the compaction cause.

3. **The CLAUDE.md mechanism is more suitable for this purpose.** CLAUDE.md files are automatically re-read and re-injected after compaction without needing hooks. They survive compaction by being read from disk, not by being injected once and then lost.

For the three missed duties named in this node's question:
- **Filing the retrospective:** Not addressable by a hook; this is a manager action on resolved nodes, per node 212's Q3 (which folds the filing into the resolution edit).
- **Putting things in front of the human:** A SessionStart hook with `"compact"` matcher could re-inject reminders after compaction, but would not help between compactions.
- **Topping up a slot when a node finishes:** A `Stop` hook or a custom `PostToolUse` hook could theoretically trigger this, but this is not a context-survival problem; it is a decision the manager must make on every node completion.

**The answer to the node's question is:** Hooks can help re-inject instructions after compaction, but the CLAUDE.md file mechanism is what actually holds instructions across a compaction. Ground rule 1 (nothing shipped may assume a hook mechanism) means this effort's solution must not depend on hooks; CLAUDE.md is the built-in mechanism that works.

**What the worker reported its work invalidates:** None. The effort's record in map.md and map-implementation-rules.md does not claim any specific harness hook behavior. The map-implementation-rules.md section on landing mentions worktrees and reset procedures but does not reference hooks for standing duties.

## The manager's note at resolution

*Not a change to anything above.*

~~**One of its findings the manager can corroborate from its own context, and does.** This session was compacted
mid-effort, and after the compaction the manager's context carried the project's instruction file and its memory
index again, re-read from disk — which is the behaviour the answer names as the mechanism that actually holds an
instruction across a compaction. That is direct evidence for the answer's central claim, and it is the only claim
here the manager can check without reading the documentation itself.~~

**Struck by the manager in the turn it was written, and this is the corrected version.** After the compaction the
manager's context carried **the human's own auto-memory index**, which lives outside this repository, re-read from
disk. **This repository has no instruction file at all** — its root holds only `.claude`, `CONTEXT.md`,
`.gitignore`, `.scratch` and `.worktrees`, and there is no `.claude/rules/` directory. So the mechanism the answer
names as the one that works **is not in play here today**, and what the manager observed was the memory mechanism
rather than a project instruction file. The observation still corroborates that *a file on disk is re-read after a
compaction*; it does not corroborate anything about a project file this repository does not have.

**What the answer does not decide, and what it hands to the next node.** It establishes the mechanism and refuses
the recommendation, correctly for a research node. What text would go in front of the manager, and whether the
effort adopts the mechanism at all, is [node
218](218-put-the-managers-trigger-duties-where-a-compaction-re-injects-them.md).

**Ground rule 1 is untouched by any of this.** A hook and an instruction file are both one harness's mechanisms, so
nothing here may reach a shipped file; the shipped repair for a missed duty has to be a rule that needs no harness
at all, which is what [node 212](212-the-mint-on-second-report-rule-is-defeated.md)'s `Q3.` answer is.
