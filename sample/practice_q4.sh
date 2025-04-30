#!/bin/dash

file="$1"

n=$(sort -n "$file" | head -n 1)
m=$(sort -n numbers_1.txt | tail -n 1)

expected=$(mktemp)
actual=$(mktemp)

seq "$n" "$m" > "$expected"
sort -n "$file" > "$actual"
