#!/usr/bin/env python3
import re

text= "COMP9044"
words= re.split(r"comp+", text)
print(words)

text1 = "Hello, world!"
words = [word for word in re.split(r"\W+", text1) if word] ##\D+
print(words)