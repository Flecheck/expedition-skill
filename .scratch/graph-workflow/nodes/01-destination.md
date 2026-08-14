# Destination of this effort

Type: grilling
Status: resolved

## Question

What does this charting effort deliver — a spec to hand off, a locked decision, or a working change made in place?

## Answer

**A working workflow, in place, dogfooded at least once.**

This map carries execution rather than stopping at a plan. Wayfinder is normally plan-don't-do, but its Notes block explicitly permits an effort to override that, and this effort does.

Reasoning: the deliverable is mostly prose instructions (skill files). A spec "precise enough to build from" would be nearly the same document written twice. It also matches the thesis of the workflow being designed — implementation is the better prototype — so designing it via spec-then-build would contradict the thing itself.

Done means: skill files (plus any harness they need) live in this repo, and the workflow has been run end-to-end on at least one real effort.
