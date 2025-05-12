#!/usr/bin/env python3

'''

grep -iE ".*\|M$" | cut -d'|' -f3,3|cut -d ',' -f1|sort |uniq

'''
import sys
import re

with open ("enrollments.txt") as f:
