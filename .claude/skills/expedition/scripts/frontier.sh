#!/bin/sh
# Reads only the expedition's own graph files, the node files under the graph directory it is given.
# It assumes nothing about the repository the expedition is being run on.
#
# Usage: frontier.sh GRAPH_DIR [HUMAN_TARGET [IMPLEMENTATION_TARGET]]
# GRAPH_DIR holds map.md and nodes/. Each target defaults to 2.

set -eu

usage() {
	echo "usage: frontier.sh GRAPH_DIR [HUMAN_TARGET [IMPLEMENTATION_TARGET]]" >&2
	exit 2
}

require_count() {
	case $1 in
	'' | *[!0-9]*)
		echo "frontier.sh: target must be a non-negative integer, got '$1'" >&2
		usage
		;;
	esac
}

[ $# -ge 1 ] && [ $# -le 3 ] || usage
graph_dir=$1
human_target=${2:-2}
implementation_target=${3:-2}
require_count "$human_target"
require_count "$implementation_target"

if [ ! -f "$graph_dir/map.md" ] || [ ! -d "$graph_dir/nodes" ]; then
	echo "frontier.sh: '$graph_dir' holds no map.md and nodes/ directory" >&2
	exit 2
fi

set -- "$graph_dir"/nodes/[0-9]*-*.md
if [ ! -f "$1" ]; then
	echo "frontier.sh: no NN-<name>.md files under '$graph_dir/nodes'" >&2
	exit 2
fi

awk -v human_target="$human_target" -v implementation_target="$implementation_target" '
# A run of N backticks opens a code span that the next run of exactly N backticks closes.
function strip_code_spans(text,    out, run, closing, rest) {
	out = ""
	while (match(text, /`+/)) {
		out = out substr(text, 1, RSTART - 1)
		run = substr(text, RSTART, RLENGTH)
		rest = substr(text, RSTART + RLENGTH)
		closing = 0
		while (match(rest, /`+/)) {
			if (RLENGTH == length(run)) {
				closing = RSTART + RLENGTH
				break
			}
			rest = substr(rest, RSTART + RLENGTH)
		}
		if (!closing) {
			return out run rest
		}
		text = substr(rest, closing)
		out = out " "
	}
	return out text
}

function strip_strikethrough(text) {
	gsub(/~~[^~]*~~/, " ", text)
	return text
}

function strip_link_targets(text) {
	gsub(/\]\([^)]*\)/, "] ", text)
	return text
}

function blocker_numbers(field,    text, count, word, words, i) {
	text = strip_link_targets(strip_strikethrough(strip_code_spans(field)))
	gsub(/[^A-Za-z0-9]+/, " ", text)
	count = split(text, words, " ")
	blockers = ""
	for (i = 1; i <= count; i++) {
		word = words[i]
		if (word ~ /^[0-9]+$/) {
			blockers = blockers " " (word + 0)
		}
	}
	return blockers
}

function field_value(line) {
	sub(/^[^:]*:[ \t]*/, "", line)
	sub(/[ \t]+$/, "", line)
	return line
}

FNR == 1 {
	file_name = FILENAME
	sub(/.*\//, "", file_name)
	sub(/\.md$/, "", file_name)
	number = file_name
	sub(/-.*/, "", number)
	number += 0
	name = file_name
	sub(/^[0-9]+-/, "", name)
	names[number] = name
	statuses[number] = ""
	types[number] = ""
	blocked_by[number] = ""
	if (number > max_number) max_number = number
	in_header = 1
	in_fence = 0
	seen_type = seen_status = seen_blocked_by = 0
}

!in_header { next }

/^## / {
	in_header = 0
	next
}

/^(```|~~~)/ {
	in_fence = !in_fence
	next
}

in_fence { next }

/^Type:/ && !seen_type {
	types[number] = field_value($0)
	seen_type = 1
}

/^Status:/ && !seen_status {
	statuses[number] = field_value($0)
	seen_status = 1
}

/^Blocked by:/ && !seen_blocked_by {
	blocked_by[number] = field_value($0)
	seen_blocked_by = 1
}

END {
	type_order = "grilling prototype precondition implementation"
	type_count = split(type_order, ordered_types, " ")
	for (i = 1; i <= type_count; i++) known_type[ordered_types[i]] = 1
	for (n = 0; n <= max_number; n++) {
		if (!(n in names)) continue
		if (types[n] != "" && !(types[n] in known_type)) {
			known_type[types[n]] = 1
			ordered_types[++type_count] = types[n]
		}
		if (statuses[n] == "claimed") claimed[types[n]]++
		if (statuses[n] != "open") continue
		blocker_count = split(blocker_numbers(blocked_by[n]), blocker_list, " ")
		unblocked = 1
		for (b = 1; b <= blocker_count; b++) {
			if (!(blocker_list[b] in statuses) || statuses[blocker_list[b]] != "resolved") {
				unblocked = 0
				break
			}
		}
		if (unblocked) {
			startable[n] = 1
			startable_by_type[types[n]]++
			startable_total++
		}
	}

	print "Claimed nodes against their target:"
	printf "  grilling, the nodes that need the human: %d of %d\n", claimed["grilling"], human_target
	printf "  implementation, the nodes that hold a code slot: %d of %d\n", claimed["implementation"], implementation_target
	print ""
	printf "Startable nodes: %d in total\n", startable_total
	for (i = 1; i <= type_count; i++) {
		printf "  %s: %d\n", ordered_types[i], startable_by_type[ordered_types[i]]
	}
	for (i = 1; i <= type_count; i++) {
		if (!startable_by_type[ordered_types[i]]) continue
		print ""
		printf "Startable %s nodes:\n", ordered_types[i]
		for (n = 0; n <= max_number; n++) {
			if ((n in startable) && types[n] == ordered_types[i]) {
				printf "  %d %s\n", n, names[n]
			}
		}
	}
}
' "$@"
