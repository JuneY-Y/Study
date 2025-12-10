#!/usr/bin/env python3
import sys

# 1) Check number of arguments
if len(sys.argv) != 4:
    # print("Usage: python create_integers_file.py <start> <end> <filename>")
    sys.exit(1)

# 2) Parse arguments
start = int(sys.argv[1])
end = int(sys.argv[2])
filename = sys.argv[3]

# 3) Open file for writing and write the range of integers
with open(filename, 'w') as f:
    if start <= end:
        for i in range(start, end + 1):
            f.write(str(i) + "\n")
    else:
        for i in range(start, end - 1, -1):
            f.write(str(i) + "\n")