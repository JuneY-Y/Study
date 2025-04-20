#!/usr/bin/env python3
import sys, re
from collections import Counter 

count = Counter()
for line in sys.stdin:
    words = re.findall(r"[a-zA-Z]+", line)  # Fix regex to match words
    words = (word.lower() for word in words)  # Correct variable name
    count.update(words)

# Print the most common words from top 1 to top 3 🌟
for rank, (word, freq) in enumerate(count.most_common(3), start=1): ## copilot 写的，写的真是太好了
    print(f"Top {rank}: {word} ({freq} occurrences)")
