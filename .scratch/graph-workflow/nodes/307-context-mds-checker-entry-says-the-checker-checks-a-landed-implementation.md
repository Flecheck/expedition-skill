# `CONTEXT.md`'s checker entry says the checker checks a landed implementation

Type: implementation
Status: open
Blocked by: 302

## Question

`CONTEXT.md`'s `**Checker**:` entry says the checker "checks a landed implementation … before the human sees it". The checker runs before the gate, and landing comes after approval. The manager contract now takes its definition from this entry. Correct the word.

*Reported by [node 296](296-rewrite-the-manager-contract-part-1.md)'s worker, which gave it no blockers and left its sequencing with node 302, the glossary rewrite, to the manager. The manager has blocked it on node 302 under node 289's freeze on a file being rewritten.*

## Acceptance condition

*Authored by node 296's worker and filed by the manager.*

1. In `CONTEXT.md`, the `**Checker**:` entry no longer says the checker checks a *landed* implementation. It says the checker checks a finished implementation, before the human sees it.
2. No other entry in `CONTEXT.md` changes.
3. No other path changes.
4. The working tree meets the bar.
