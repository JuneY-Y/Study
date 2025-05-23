#!/bin/dash
# ✅ Shell Structural Logic (Q4/Q6 style)

# Question 2:
# Print all unique years between 1970 and 1975 (inclusive) during which awards were given. Each year should be printed once and in ascending order.

grep -E '\|197[0-5]\|' |cut -d '|' -f2|sort -n|uniq