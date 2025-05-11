#!/usr/bin/env python3
import sys
import re

course_code=sys.argv[1]

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <course code>")
    sys.exit(1)
