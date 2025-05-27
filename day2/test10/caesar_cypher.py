#! /usr/bin/env python3

import sys
from string import ascii_lowercase, ascii_uppercase

assert len(sys.argv) == 2, "Usage: ./caesar_cypher.py <offset>"

offset = int(sys.argv[1])

cypher_lowercase = ''.join(map(lambda c: chr((ord(c) - ord(ascii_lowercase[0]) + offset) % (ord(ascii_lowercase[-1]) - ord(ascii_lowercase[0]) + 1) + ord(ascii_lowercase[0])), ascii_lowercase))
cypher_uppercase = ''.join(map(lambda c: chr((ord(c) - ord(ascii_uppercase[0]) + offset) % (ord(ascii_uppercase[-1]) - ord(ascii_uppercase[0]) + 1) + ord(ascii_uppercase[0])), ascii_uppercase))

cypher = str.maketrans(ascii_lowercase + ascii_uppercase, cypher_lowercase + cypher_uppercase)

for line in sys.stdin:
    print(line.translate(cypher), end="")