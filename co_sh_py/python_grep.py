#!/usr/bin/env python3

# import sys, re
from sys import argv, exit
from re import search

if len(argv) !=3:
    print(f"Usage: {argv[0]} <regex> <file>")
    exit(0)

regex=argv[1]
file=argv[2]
with open(file, "r") as file:
    for line in file:
        if search(regex,line.rstrip()):
            print(line.rstrip()) ## line 自动会代空格