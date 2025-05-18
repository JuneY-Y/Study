#!/usr/bin/env python3
import sys

n = int(sys.argv[1])
filename = sys.argv[2]

with open(filename, 'r') as f:
    lines = f.readlines()

new_lines = []

for line in lines:
    line = line.rstrip('\n')

    flag = False  # loop control
    while not flag:
        if len(line) <= n:
            new_lines.append(line)
            flag = True
        elif ' ' not in line:
            new_lines.append(line)
            flag = True
        else:
            front = line[:n]
            if ' ' in front:
                split_index = front.rfind(' ')
                new_lines.append(line[:split_index])
                line = line[split_index + 1:]
            else:
                split_index = line.find(' ')
                new_lines.append(line[:split_index])
                line = line[split_index + 1:]
            # continue here is not needed — while loop continues automatically

with open(filename, 'w') as f:
    for l in new_lines:
        f.write(l + '\n')