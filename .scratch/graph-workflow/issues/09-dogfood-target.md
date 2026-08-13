# Dogfood target

Type: grilling
Status: open

## Question

Which real effort is the workflow first run on, end to end?

The destination requires at least one dogfood run, so this needs an answer — and picking it early shapes the design, because the workflow should be built for the effort it will actually face first.

Candidates to weigh:

- **Itself** — use the workflow to finish the workflow. Maximally recursive and a genuine test of the revision loop, but a broken workflow cannot repair itself, and a failure is hard to attribute.
- **A separate real project** of the user's, chosen for having genuine fog and real code to write.
- **A deliberately small throwaway effort** built only to exercise the machinery. Fastest signal, weakest evidence that it works at real scale.

The answer should also state what would count as the run **succeeding** — otherwise "dogfooded once" is not checkable, and the destination has no test.

Independent of the other open issues: answerable now, and its answer constrains how much the rest can cost.
