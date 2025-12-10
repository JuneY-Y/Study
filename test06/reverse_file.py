#!/usr/bin/env python3
import sys

# If exactly 2 arguments (source, destination) are not provided, exit silently (or with an error code).
if len(sys.argv) != 3:
    sys.exit(1)  # No output, just exit.

source = sys.argv[1]
dest = sys.argv[2]

try:
    with open(source, 'r') as s:
        lines = s.readlines()
    # Reverse the list of lines in-place
    lines.reverse()
    with open(dest, 'w') as d:
        d.writelines(lines)
except FileNotFoundError:
    # If the source file is missing, exit silently (with non-zero status)
    sys.exit(1)