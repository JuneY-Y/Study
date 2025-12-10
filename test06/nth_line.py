#!/usr/bin/env python3
import sys

# 1) Check number of arguments
if len(sys.argv) != 3:
    # print("this file has one line")
    print("Usage: python nth_line.py <n> <filename>", file=sys.stderr)
    sys.exit(1)

# 2) Parse command-line arguments
try:
    n = int(sys.argv[1])
except ValueError:
    print("Error: n must be an integer.", file=sys.stderr)
    sys.exit(1)

filename = sys.argv[2]

# 3) Open the file and read line by line
try:
    with open(filename, 'r') as f:
        for idx, line in enumerate(f, start=1):
            if idx == n:
                # Strip the newline before printing
                print(line.rstrip('\n'))
                break
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.", file=sys.stderr)
    sys.exit(1)