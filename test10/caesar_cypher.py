#!/usr/bin/env python3

import sys

# Get shift value from command line
shift = int(sys.argv[1])

# Loop over each line from standard input
for line in sys.stdin:
    result = ''
    for char in line:
        if 'a' <= char <= 'z':
            # Shift lowercase letters with wrap-around
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += shifted
        elif 'A' <= char <= 'Z':
            # Shift uppercase letters with wrap-around
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += shifted
        else:
            # Leave all other characters unchanged
            result += char
    print(result, end='')
# #!/usr/bin/env python3

# '''
# This Caesar cipher implementation builds a custom 
# translation table by rotating letters using ASCII math and applies it efficiently using str.translate() for performance and clarity.
# '''
# import sys
# from string import ascii_lowercase, ascii_uppercase  # Provides 'abcdefghijklmnopqrstuvwxyz' and 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# # Ensure the script is called with exactly one argument: the shift offset
# assert len(sys.argv) == 2, "Usage: ./caesar_cypher.py <offset>"

# # Parse the shift offset from command line argument (can be negative)
# offset = int(sys.argv[1])
# # Create translated lowercase alphabet by shifting each letter by offset
# cypher_lowercase = ''.join(map(
#     lambda c: chr((ord(c) - ord(ascii_lowercase[0]) + offset) %
#                   (ord(ascii_lowercase[-1]) - ord(ascii_lowercase[0]) + 1)
#                   + ord(ascii_lowercase[0])),
#     ascii_lowercase
# ))

# # Same logic applied to uppercase alphabet
# cypher_uppercase = ''.join(map(
#     lambda c: chr((ord(c) - ord(ascii_uppercase[0]) + offset) %
#                   (ord(ascii_uppercase[-1]) - ord(ascii_uppercase[0]) + 1)
#                   + ord(ascii_uppercase[0])),
#     ascii_uppercase
# ))

# # Create a translation table from normal letters to their shifted equivalents
# cypher = str.maketrans(
#     ascii_lowercase + ascii_uppercase,
#     cypher_lowercase + cypher_uppercase
# )

# # For each line of input, apply the translation table and print it
# for line in sys.stdin:
#     print(line.translate(cypher), end='')