#!/usr/bin/env python3

import sys
import itertools

#Check if user gave 2 arguments: a line number n and a filename.
if len(sys.argv) !=3: # 这里的冒号是不能少的
    print("Usage: python nth_line.py <n> <filename>", file=sys.stderr)
    sys.exit(1)


# Try to convert n into an integer.
try:
    n = int(sys.argv[1])
except ValueError:
    print("Error: n must be an integer. ", file=sys.stderr)
    sys.exit(1)
filename = sys.argv[2]

#Try to open the file.
#Read it line by line.
try: 
    with open(filename, 'r') as f:
        # for idx, line in enumerate(f,start=1):
         for idx, line in enumerate(f, start=1):
            if idx == n:
                # Strip the newline before printing
                print(line.rstrip('\n'))
                break
except FileNotFoundError:
    print(f"Error: File'{filename}' not found", file=sys.stderr)
    sys.exit(1)

#When the current line number matches n, print that line and stop.

#If something goes wrong (bad input, file not found), show an error and exit.
# excepeted errorvalue



