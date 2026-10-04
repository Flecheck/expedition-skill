# Derivations about the record

This file holds no numbers. It holds the means of obtaining them. A value about the record is obtained by running
the derivation for it at the moment the value is wanted, against the tree as it stands then. A number found
written anywhere else in the record is a historical statement of what was true when it was written, and not the
current state.

Run every block from the directory `.scratch/graph-workflow/` of the tree being measured, under `sh`. Each block
uses only `sh`, `awk`, `find`, `wc`, `sort`, `grep` and `git`. Byte sizes are bytes and not characters: the blocks
set `LC_ALL=C` wherever `awk` measures a length, because in a UTF-8 locale `awk` counts characters.

The directory `worktrees/` holds one full checkout of the repository per claimed implementation node. It is not
part of the record, and every derivation that walks the directory leaves it out.

## (a) Size of a file at a past date

What was the byte size of a named file in this directory at the end of a given day?

The answer is the file as committed in the last commit on the current branch up to the end of that day. A file that
has since been renamed is named as it was then: the node files sat under `issues/` before they sat under `nodes/`.
The command fails, and prints nothing on its standard output, where no commit precedes the date or the file did not
exist in that commit.

```sh
file=map.md day=2026-09-01
rev=$(git rev-list -1 --before="$day 23:59:59" HEAD) && [ -n "$rev" ] && git cat-file -s "$rev:./$file"
```

## (b) Node file count over time

How many node files did the directory hold at the end of each day on which the node files changed?

The node files are the files named `NN-<name>.md` directly under `nodes/`, or under `issues/` before that directory
was renamed. Each output line is a day and the count in the last commit of that day, newest day first.

```sh
git log --format='%H %cs' -- nodes issues | awk '!seen[$2]++' | while read -r rev day; do
	count=$(git ls-tree -r --name-only "$rev" -- nodes issues | grep -cE '^(nodes|issues)/[0-9]+-[^/]*\.md$')
	echo "$day $count"
done
```

## (c) Node files by status

How many node files are there now for each value of `Status:`?

A node file's fields are read only from its header block, the lines above its first `##` heading, and fenced code
blocks are skipped. A `Status:` line in a node's prose body, or in a code block quoting the file format, is not a
field and is not counted. Where the header holds the field twice, the first occurrence counts. A file whose header
holds no `Status:` line is counted under `(none)`, so the counts always add up to the number of node files.

```sh
LC_ALL=C awk -v field=Status '
FNR == 1 { in_header = 1; in_fence = 0; value[FILENAME] = "(none)"; seen = 0 }
!in_header { next }
/^## / { in_header = 0; next }
/^(```|~~~)/ { in_fence = !in_fence; next }
in_fence || seen { next }
index($0, field ":") == 1 {
	line = substr($0, length(field) + 2)
	sub(/^[ \t]+/, "", line)
	sub(/[ \t]+$/, "", line)
	value[FILENAME] = line
	seen = 1
}
END { for (file in value) count[value[file]]++; for (v in count) print count[v], v }
' nodes/[0-9]*-*.md | sort -rn
```

## (d) Node files by type

How many node files are there now for each value of `Type:`?

A node file's fields are read only from its header block, the lines above its first `##` heading, and fenced code
blocks are skipped. A `Type:` line in a node's prose body, or in a code block quoting the file format, is not a
field and is not counted. Where the header holds the field twice, the first occurrence counts. A file whose header
holds no `Type:` line is counted under `(none)`, so the counts always add up to the number of node files.

```sh
LC_ALL=C awk -v field=Type '
FNR == 1 { in_header = 1; in_fence = 0; value[FILENAME] = "(none)"; seen = 0 }
!in_header { next }
/^## / { in_header = 0; next }
/^(```|~~~)/ { in_fence = !in_fence; next }
in_fence || seen { next }
index($0, field ":") == 1 {
	line = substr($0, length(field) + 2)
	sub(/^[ \t]+/, "", line)
	sub(/[ \t]+$/, "", line)
	value[FILENAME] = line
	seen = 1
}
END { for (file in value) count[value[file]]++; for (v in count) print count[v], v }
' nodes/[0-9]*-*.md | sort -rn
```

## (e) Open and claimed nodes

Which node files have the status `open` or `claimed` now?

The status is read the same way as in (c): from the header block above the first `##` heading only, with fenced
code blocks skipped and the first `Status:` line counting. Each output line is a status and a file name, ordered by
node number.

```sh
awk '
FNR == 1 { in_header = 1; in_fence = 0; seen = 0 }
!in_header { next }
/^## / { in_header = 0; next }
/^(```|~~~)/ { in_fence = !in_fence; next }
in_fence || seen { next }
/^Status:/ {
	seen = 1
	status = $0
	sub(/^Status:[ \t]*/, "", status)
	sub(/[ \t]+$/, "", status)
	name = FILENAME
	sub(/.*\//, "", name)
	if (status == "open" || status == "claimed") print status, name
}
' nodes/[0-9]*-*.md | sort -k2 -n
```

## (f) Flags by state

How many entries does `flags.md` hold in each state, checked and unchecked?

An entry is a line that begins with `- [ ] ` (unchecked) or `- [x] ` (checked). Fenced code blocks are skipped,
because the file's `Format:` block shows an unchecked entry as an example. The legend line writes its boxes inside
backticks and so does not begin with either form.

```sh
awk '
/^(```|~~~)/ { in_fence = !in_fence; next }
in_fence { next }
/^- \[ \] / { unchecked++ }
/^- \[x\] / { checked++ }
END { print checked + 0, "checked"; print unchecked + 0, "unchecked" }
' flags.md
```

## (g) Struck-through text

What is the total byte size of struck-through text across the directory, and its share of the directory's bytes?

Struck-through text is the text between an opening `~~` and the next `~~` within one block: a strike spans line
breaks inside a paragraph or a list item, and never crosses a blank line, a heading or the start of a new list
item. A heading is a block of its own. The two `~~` markers are not counted, and the line breaks inside a strike
are. Fenced code blocks are skipped, and a `~` inside a code span is not a marker. An opening `~~` that no closing
`~~` follows in its block strikes nothing. The directory is every file under `.scratch/graph-workflow/` except
`worktrees/`. The share is the struck bytes divided by the byte size of those same files.

```sh
files=$(find . -path ./worktrees -prune -o -type f -print)
total=$(cat $files | wc -c)
LC_ALL=C awk -v total="$total" '
function mask_code_spans(text,    out, run, rest, closing, span) {
	out = ""
	while (match(text, /`+/)) {
		out = out substr(text, 1, RSTART - 1)
		run = substr(text, RSTART, RLENGTH)
		rest = substr(text, RSTART + RLENGTH)
		closing = 0
		span = ""
		while (match(rest, /`+/)) {
			if (RLENGTH == length(run)) {
				closing = RSTART
				break
			}
			span = span substr(rest, 1, RSTART + RLENGTH - 1)
			rest = substr(rest, RSTART + RLENGTH)
		}
		if (!closing) return out run span rest
		span = span substr(rest, 1, closing - 1)
		gsub(/~/, "-", span)
		out = out run span run
		text = substr(rest, closing + length(run))
	}
	return out text
}
function end_block(    text, opening, closing) {
	text = mask_code_spans(block)
	while ((opening = index(text, "~~")) > 0) {
		text = substr(text, opening + 2)
		closing = index(text, "~~")
		if (!closing) break
		struck += closing - 1
		text = substr(text, closing + 2)
	}
	block = ""
}
FNR == 1 { end_block(); in_fence = 0 }
/^(```|~~~)/ { end_block(); in_fence = !in_fence; next }
in_fence { next }
/^[ \t]*$/ { end_block(); next }
/^#/ { end_block(); block = $0; end_block(); next }
/^[ \t]*([-*+]|[0-9]+\.)[ \t]/ { end_block() }
{ block = (block == "" ? $0 : block "\n" $0) }
END {
	end_block()
	printf "%d struck bytes of %d bytes, a share of %.2f%%\n", struck, total, 100 * struck / total
}
' $files
```

## (h) Size of each item under `## Notes` in `map.md`

How many bytes of its own prose does each item under `## Notes` in `map.md` hold, and which items exceed 500 bytes?

This derivation reads `map.md` and no node file. Where any derivation in this file reads a node file's fields, it
reads them only from the header block above the first `##` heading and skips fenced code blocks, and this one
likewise skips fenced code blocks. An item is a paragraph or a list item between the `## Notes` heading and the next
`##` heading: it ends at a blank line and at the start of the next list item. An item's own prose is its text with
every quotation of the human's own words removed. In `map.md` the human's words are quoted as an italic quotation,
an asterisk and a double quote opening it and a double quote and an asterisk closing it, and the whole quotation,
its markers included, is removed. The line breaks inside an item are counted and its final line break is not. Each
output line is an item's byte size, the line of `map.md` it starts on, and its first words. The items over 500 bytes
are then listed again.

```sh
LC_ALL=C awk '
function strip_human_quotations(text,    out, opening, closing) {
	out = ""
	while ((opening = index(text, "*\"")) > 0) {
		closing = index(substr(text, opening + 2), "\"*")
		if (!closing) break
		out = out substr(text, 1, opening - 1)
		text = substr(text, opening + 2 + closing + 1)
	}
	return out text
}
function end_item(    size) {
	if (item == "") return
	size = length(strip_human_quotations(item))
	items++
	sizes[items] = size
	starts[items] = start
	openings[items] = substr(item, 1, 60)
	item = ""
}
/^## / { end_item(); in_notes = ($0 == "## Notes"); next }
!in_notes { next }
/^(```|~~~)/ { end_item(); in_fence = !in_fence; next }
in_fence { next }
/^[ \t]*$/ { end_item(); next }
/^[ \t]*([-*+]|[0-9]+\.)[ \t]/ { end_item() }
{ if (item == "") { item = $0; start = NR } else item = item "\n" $0 }
END {
	end_item()
	for (i = 1; i <= items; i++) printf "%d bytes, line %d: %s\n", sizes[i], starts[i], openings[i]
	print ""
	print "Over 500 bytes:"
	for (i = 1; i <= items; i++) if (sizes[i] > 500) printf "%d bytes, line %d: %s\n", sizes[i], starts[i], openings[i]
}
' map.md
```

## (i) Size of the node files

What are the total and the mean byte size of the node files now?

The node files are the files named `NN-<name>.md` directly under `nodes/`.

```sh
set -- nodes/[0-9]*-*.md
total=$(cat "$@" | wc -c)
awk -v total="$total" -v files="$#" 'BEGIN { printf "%d files, %d bytes in total, a mean of %.1f bytes\n", files, total, total / files }'
```

## (j) Item names carried by the retrospectives

For each standing item named in a retrospective, how many retrospectives carry that name, and in which node files?

A retrospective is written into a node file in one of two ways: as a section under a heading of its own, or as the
`RETROSPECTIVE` part of a worker's handover pasted into the file. The block reads every form of both.

The headings under which a retrospective section sits are `## Retrospective`, `### Retrospective`,
`## RETROSPECTIVE`, `## Retrospective — attempt 1`, `## Retrospective — what the two correction rounds added`,
`## Annotation: the retrospective`, `## Annotation: the retrospective, and the manager's note on filing this node`,
and `### The retrospective`. The block matches a heading of any level whose text is `Retrospective`,
`RETROSPECTIVE` or `The retrospective`, or begins with `Retrospective — ` or `Annotation: the retrospective`. A
retrospective section's body ends at the next heading of the same or higher level. A retrospective heading inside a
section that is already open starts no second section. Some headings name a retrospective without holding one, and
the block does not read them: a node file's title,
`## The manager's disposal of the retrospective's record items`, and
`## Annotation: this node's retrospective claim is refined, and its own number has moved`, which is a later node's
note about one retrospective's claim.

A handover's `RETROSPECTIVE` part starts at a line that begins with the word `RETROSPECTIVE`. The word stands alone,
or is followed by a colon, by a suffix in parentheses such as `RETROSPECTIVE (this round)`, or by `ADDITION:`. Where
that line is inside a fenced code block, the part ends where its fenced block ends. Where it is outside every fenced
block, the part ends at the next heading. Outside a fenced block, the line may also open with `*` or `_` emphasis
markers, as in `**RETROSPECTIVE**` and `*RETROSPECTIVE, addition to …:*`, and the word may be written
`Retrospective`, as in the correction-round paragraphs `**Retrospective, added:**` and
`**Retrospective, changed:**`. Where the line opens with a blockquote marker, as in `> RETROSPECTIVE`, the part ends
at the first line that does not begin with `>`. A part that starts inside a retrospective section belongs to that
section. A line that starts a part while another part is open ends that part and starts a new one.

A fenced code block opens at a run of three or more backticks or tildes, indented by at most three spaces. It closes
at a line holding only a run of the same character at least as long as the opening run. A pasted handover may be
fenced with a long run and hold shorter fences of its own, and a closing run shorter than the opening one closes
nothing. A heading inside a fenced code block is skipped, and it neither opens nor ends a section.

An item name is recognised in one written form: a numbered or bulleted list item inside a retrospective, whose text
opens with a code span. The list item may sit inside a blockquote, behind one or more `>` markers. The code span
holds two or more words of lowercase letters and digits joined by hyphens. The name is the text of that code span. A
name written in any other form, in bold or in running prose, is not recognised, because no other form can be told
apart from ordinary emphasis and code spans.

Each retrospective section, and each handover part outside a section, is one retrospective. Each output line is a
count, a name, and the node files whose retrospectives carry that name. The count is the number of retrospectives
that carry the name. A node file holding several of them, such as a first attempt and a correction round, adds one
to the count for each, and is listed once. A name carried by only one retrospective is reported too, so that a
name minted once is visible to the next worker looking for an existing name to reuse.

A heading that names a retrospective, and that the block neither reads nor excludes as above, is a form this entry
does not yet cover. The block prints each such heading on its standard error, and prints none while the forms above
are complete.

```sh
LC_ALL=C awk '
function is_retrospective_heading(text) {
	return text == "Retrospective" || text == "RETROSPECTIVE" || text == "The retrospective" ||
		index(text, "Retrospective — ") == 1 || index(text, "Annotation: the retrospective") == 1
}
function is_excluded_heading(level, text) {
	return level == 1 || index(text, "disposal of the retrospective") || index(text, "retrospective claim is refined")
}
function read_name(    name, file) {
	if (!match($0, /^([ \t]*>)*[ \t]*([0-9]+\.|[-*+])[ \t]+`[a-z0-9]+(-[a-z0-9]+)+`/)) return
	name = substr($0, RSTART, RLENGTH)
	sub(/^[^`]*`/, "", name)
	sub(/`$/, "", name)
	if ((name, retrospective) in carried) return
	carried[name, retrospective] = 1
	count[name]++
	file = FILENAME
	sub(/.*\//, "", file)
	if ((name, file) in listed) return
	listed[name, file] = 1
	files[name] = files[name] " " file
}
FNR == 1 { fence = ""; section = 0; part = "" }
fence != "" {
	run = $0
	sub(/^ +/, "", run)
	sub(/[ \t]+$/, "", run)
	if (run ~ /^(`+|~+)$/ && substr(run, 1, 1) == substr(fence, 1, 1) && length(run) >= length(fence)) {
		fence = ""
		if (part == "fenced") part = ""
		next
	}
	if (!section && /^RETROSPECTIVE/) { part = "fenced"; retrospective++ }
	if (section || part != "") read_name()
	next
}
/^ ? ? ?(```|~~~)/ {
	match($0, /`+|~+/)
	fence = substr($0, RSTART, RLENGTH)
	if (part == "quoted") part = ""
	next
}
/^#+ / {
	level = index($0, " ") - 1
	text = substr($0, level + 2)
	if (section && level <= section) section = 0
	part = ""
	if (section) next
	if (is_retrospective_heading(text)) { section = level; retrospective++ }
	else if (tolower(text) ~ /retrospective/ && !is_excluded_heading(level, text))
		print "heading not covered: " FILENAME ": " $0 > "/dev/stderr"
	next
}
part == "quoted" && !/^>/ { part = "" }
!section && /^(> ?)?[*_]*(RETROSPECTIVE|Retrospective)/ { part = /^>/ ? "quoted" : "plain"; retrospective++ }
section || part != "" { read_name() }
END { for (name in count) print count[name], name ":" files[name] }
' nodes/[0-9]*-*.md | sort -k1,1rn -k2,2
```
