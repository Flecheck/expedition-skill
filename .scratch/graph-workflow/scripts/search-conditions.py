#!/usr/bin/env python3
"""Search the open and claimed nodes' conditions for what a change to one file makes wrong.

Usage:
    python3 .scratch/graph-workflow/scripts/search-conditions.py NODE BEFORE AFTER \\
        [--path PATH] [--phrases FILE] [--skip FILE] [--ngram N]

    NODE      your node's number; its own file is left out of the search.
    BEFORE    the before-text: a file, or REV:PATH, read with `git show REV:PATH` in the repo.
    AFTER     the after-text: a file, usually the one in your worktree, or REV:PATH.
    --path    the rewritten file's repo-relative path. Needed only when neither argument is
              REV:PATH and AFTER sits in no git tree.
    --phrases a file of phrases, one per line, reported wherever a condition holds one.
    --skip    a file whose lines are dropped from every condition before searching. On a
              rewrite node, pass your own node file: that drops the common clauses every
              rewrite node carries, whose ruled-out examples otherwise match in every search.
    --ngram   the word n-gram length, 6 by default.

Example, from the repo root:
    python3 .scratch/graph-workflow/scripts/search-conditions.py 302 \\
        "$(git -C WORKTREE merge-base HEAD master):CONTEXT.md" WORKTREE/CONTEXT.md \\
        --skip .scratch/graph-workflow/nodes/302-rewrite-the-glossary.md

It collects each `Acceptance condition...` and `Amendment...` section, at any heading level and
wherever it sits, of every node whose status is `open` or `claimed`, and prints four reports:
quoted spans of the before-text that the after-text no longer holds, shared word n-grams, phrase
hits, and which files of the rewrite nodes' clause 5 list hold each before-text heading. The
clause-5 files are read as they stand in the main tree, not at a revision.

Reading the output: every gone item is one line that starts, after its indent, with `GONE |`, so
`grep '^ *GONE |'` on the output lists exactly them; no header uses the word in capitals, so a
plain `grep GONE` lists them too, plus any quoted text that itself holds the word. A gone line
reads `GONE | quote | NN | span` or `GONE | n-gram run | NN | run`, NN being the number of the
node whose condition holds it, or `GONE | protected heading | text`, a before-text heading that
another clause-5 file cites and the after-text lacks. The last line counts them, `# Gone items: N (...)`, and reads
0 when nothing is gone. The rest of the output, the KEPT lines and the free headings, is context.
Comparing a file with itself reports nothing gone.
Text is compared after lower-casing and dropping markdown and punctuation, so line wrapping and
emphasis do not matter. It prints to stdout, writes no file, and needs no environment variable.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

RECORD = Path(__file__).resolve().parents[1]
REPO = RECORD.parents[1]

# Clause 5 of the plain-English rewrite nodes' conditions: a heading whose exact text appears in
# any of these files other than the rewritten one keeps that exact text.
HEADING_CITING_FILES = [
    '.claude/skills/expedition/SKILL.md',
    '.claude/skills/expedition/graph-conventions.md',
    '.claude/skills/expedition/wayfinder-divergences.md',
    '.claude/skills/expedition-checker/SKILL.md',
    '.claude/skills/expedition-grilling/SKILL.md',
    '.claude/skills/expedition-implementation/SKILL.md',
    '.claude/skills/expedition-precondition/SKILL.md',
    '.claude/skills/expedition-prototype/SKILL.md',
    '.claude/skills/expedition-research/SKILL.md',
    '.claude/skills/expedition-stop/SKILL.md',
    'CONTEXT.md',
    '.claude/rules/expedition-triggers.md',
    '.scratch/graph-workflow/map.md',
    '.scratch/graph-workflow/map-manager-only.md',
    '.scratch/graph-workflow/map-implementation-rules.md',
    '.gitignore',
]


def main():
    args = parse_args()
    before_text, before_path = read_text_arg(args.before)
    after_text, after_path = read_text_arg(args.after)
    rewritten_path = args.path or before_path or after_path or repo_relative_path(Path(args.after))
    if rewritten_path is None:
        sys.exit('cannot tell which file is rewritten: pass --path')

    skipped_lines = set()
    if args.skip:
        skipped_lines = {norm(l) for l in Path(args.skip).read_text().split('\n') if norm(l)}
    conditions = list(open_conditions(args.node, skipped_lines))
    print(f'# Conditions searched: {len(conditions)}, excluding node {args.node}')
    print('   ', ', '.join(name.split('-')[0] for name, _ in conditions))
    if args.skip:
        print(f'    lines of {args.skip} dropped from them first')

    before, after = norm(before_text), norm(after_text)
    gone_quotes = report_quotes(conditions, before, after)
    gone_runs = report_ngrams(conditions, before, after, args.ngram)
    if args.phrases:
        report_phrases(conditions, args.phrases)
    gone_headings = report_headings(before_text, after_text, rewritten_path)
    print(f'\n# Gone items: {gone_quotes + gone_runs + gone_headings} (quotes {gone_quotes}, '
          f'n-gram runs {gone_runs}, protected headings {gone_headings})')


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('node', type=int)
    parser.add_argument('before')
    parser.add_argument('after')
    parser.add_argument('--path')
    parser.add_argument('--phrases')
    parser.add_argument('--skip')
    parser.add_argument('--ngram', type=int, default=6)
    return parser.parse_args()


def read_text_arg(arg):
    """Return the text, and the repo-relative path when the argument is REV:PATH."""
    if Path(arg).is_file():
        return Path(arg).read_text(), None
    if ':' not in arg:
        sys.exit(f'{arg!r} is neither a file nor REV:PATH')
    rev, path = arg.split(':', 1)
    shown = subprocess.run(['git', '-C', str(REPO), 'show', f'{rev}:{path}'], capture_output=True, text=True)
    if shown.returncode != 0:
        sys.exit(f'git show {arg} failed: {shown.stderr.strip()}')
    return shown.stdout, path


def repo_relative_path(file):
    top = subprocess.run(['git', '-C', str(file.resolve().parent), 'rev-parse', '--show-toplevel'],
                         capture_output=True, text=True)
    if top.returncode != 0:
        return None
    return str(file.resolve().relative_to(Path(top.stdout.strip()).resolve()))


# ---- reports -----------------------------------------------------------------------------------

# Backticks, single-asterisk italics, straight and curly double quotes. Bold (`**`) marks no quote.
QUOTE = re.compile(r'`([^`]{12,})`|(?<!\*)\*(?!\*)"?([^*]{12,}?)"?(?<!\*)\*(?!\*)|"([^"]{12,}?)"|“([^”]{12,}?)”')


def report_quotes(conditions, before, after):
    """Print the quoted spans and return how many are gone."""
    print('\n# Quoted spans of the before-text that a condition quotes, each KEPT or gone from the after-text')
    gone_count = 0
    for name, text in conditions:
        hits = []
        for match in QUOTE.finditer(' '.join(text.split())):
            span = next(g for g in match.groups() if g)
            if len(norm(span)) >= 12 and holds(before, span):
                hits.append(('KEPT' if holds(after, span) else 'GONE', span))
        if hits:
            print('==', name)
            for state, span in sorted(hits):
                if state == 'GONE':
                    gone_count += 1
                    print('    GONE | quote |', node_number_of(name), '|', span)
                else:
                    print('    KEPT |', span)
    return gone_count


def report_ngrams(conditions, before, after, n):
    """Print the shared runs and return how many are gone."""
    print(f'\n# Word {n}-grams a condition shares with the before-text, merged into runs the '
          'before-text holds in one piece, each KEPT or gone from the after-text')
    before_words = before.split()
    before_ngrams = {' '.join(before_words[i:i + n]) for i in range(len(before_words) - n + 1)}
    gone_count = 0
    for name, text in conditions:
        words = norm(text).split()
        starts = [i for i in range(len(words) - n + 1) if ' '.join(words[i:i + n]) in before_ngrams]
        runs = [' '.join(words[first:last + n]) for first, last in runs_held_by(before, words, starts, n)]
        if runs:
            gone = [r for r in runs if not holds(after, r)]
            gone_count += len(gone)
            print('==', name, f'{len(runs)} runs')
            for run in gone:
                print('    GONE | n-gram run |', node_number_of(name), '|', run)
            for run in runs:
                if run not in gone:
                    print('    KEPT |', run)
    return gone_count


def report_phrases(conditions, phrases_file):
    print(f'\n# Phrases of {phrases_file} a condition holds')
    phrases = [l.strip() for l in Path(phrases_file).read_text().split('\n') if l.strip()]
    for name, text in conditions:
        normalized = norm(text)
        hits = [p for p in phrases if holds(normalized, p)]
        if hits:
            print('==', name, '|', ' ; '.join(hits))


def report_headings(before_text, after_text, rewritten_path):
    """Print the before-text headings and return how many protected ones are gone."""
    print(f'\n# Headings of the before-text, and the other clause-5 files holding their exact text '
          f'(rewritten file: {rewritten_path})')
    others = {}
    for path in HEADING_CITING_FILES:
        if path == rewritten_path:
            continue
        file = REPO / path
        if not file.is_file():
            print('    MISSING FILE |', path)
            continue
        others[path] = file.read_text()
    after_headings = {text for _, text, _ in headings(after_text.split('\n'))}
    gone_count = 0
    for _, text, _ in headings(before_text.split('\n')):
        citing = [path for path, content in others.items() if text in content]
        if not citing:
            state = 'free'
        elif text in after_headings:
            state = 'PROTECTED, kept'
        else:
            state = 'GONE | protected heading'
            gone_count += 1
        print(f'    {state} | {text}')
        for path in citing:
            print('        ', path)
    return gone_count


# ---- reading the nodes -------------------------------------------------------------------------

SECTION_PREFIXES = ('Acceptance condition', 'Amendment')


def open_conditions(own_node, skipped_lines):
    """Yield (node file stem, text of its condition and amendment sections) per open or claimed node."""
    for path in sorted((RECORD / 'nodes').glob('*.md'), key=lambda p: node_number(p) or 0):
        number = node_number(path)
        if number is None or number == own_node:
            continue
        lines = path.read_text().split('\n')
        if node_status(lines, path) not in ('open', 'claimed'):
            continue
        kept = [l for l in condition_lines(lines) if norm(l) not in skipped_lines]
        if kept:
            yield path.stem, '\n'.join(kept)


def node_number(path):
    match = re.match(r'(\d+)-', path.name)
    return int(match.group(1)) if match else None


def node_number_of(stem):
    return stem.split('-')[0]


def node_status(lines, path):
    for line in lines:
        if line.startswith('## '):
            break
        match = re.match(r'Status:\s*(\S+)', line)
        if match:
            return match.group(1)
    sys.exit(f'{path}: no Status line before the first section')


def condition_lines(lines):
    """The lines of every condition or amendment section; a section runs to the next heading at
    its level or above, and a section nested in another is taken once."""
    taken = set()
    found = headings(lines)
    for k, (level, text, start) in enumerate(found):
        if not text.startswith(SECTION_PREFIXES):
            continue
        end = next((s for lv, _, s in found[k + 1:] if lv <= level), len(lines))
        taken.update(range(start, end))
    return [lines[i] for i in sorted(taken)]


def headings(lines):
    """(level, text, line index) of every markdown heading outside code fences."""
    found, fenced = [], False
    for i, line in enumerate(lines):
        if line.lstrip().startswith(('```', '~~~')):
            fenced = not fenced
            continue
        match = re.match(r'(#{1,6})\s+(.*?)\s*$', line)
        if match and not fenced:
            found.append((len(match.group(1)), match.group(2), i))
    return found


# ---- text comparison ---------------------------------------------------------------------------

def norm(s):
    s = s.lower()
    s = re.sub(r'[*_`>"“”‘’\']', ' ', s)
    s = re.sub(r'[—–;:,.()\[\]!?|-]', ' ', s)
    return ' '.join(s.split())


def holds(normalized_text, fragment):
    """Whether the normalized text holds the fragment as whole words."""
    return f' {norm(fragment)} ' in f' {normalized_text} '


def runs_held_by(before, words, sorted_starts, n):
    """[first, last] n-gram starts of each run: consecutive starts, cut wherever the joined words
    are no longer one piece of the before-text.

    Two n-grams that overlap in a condition can sit in different places of the before-text, and
    their merged run is then in neither text, so it would read as gone even when both texts are
    the same file."""
    ranges = []
    for i in sorted_starts:
        if ranges and i == ranges[-1][1] + 1 and holds(before, ' '.join(words[ranges[-1][0]:i + n])):
            ranges[-1][1] = i
        else:
            ranges.append([i, i])
    return ranges


main()
