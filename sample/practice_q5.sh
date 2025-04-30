#!/bin/bash

# file="$1"
regex="$1"
file="$2"

matching_lines=$(grep -E "^$regex$" "$file")

if [ -z "$matching_lines" ]; then
        echo "No awards matched"
        exit 0
fi 

years_given=$(mktemp)   # mktemp 保证每次都是唯一安全的临时文件名
echo "$matching_lines" | cut -d '|' -f2 | sort -n | uniq > "$years_given"

n=$(head -n1 "$years_given")
m=$(tail -n1 "$years_given")

expected=$(mktemp)

# n=$(grep "Nobel Prize for physics" awards.psv | sort -t'|' -k2,2n | awk -F'|' '!seen[$2]++' |head -n 1 | cut -d '|' -f2,2)

# m=$(grep "Nobel Prize for physics" awards.psv | sort -t'|' -k2,2n | awk -F'|' '!seen[$2]++' |tail -n 1 | cut -d '|' -f2,2)

# grep "Nobel Prize for physics" awards.psv | sort -t'|' -k2,2n | awk -F'|' '!seen[$2]++' |cut -d '|' -f2,2 >  "$award"

seq "$n" "$m" > "$expected" #不变

diff "$expected" "$years_given" | grep '^>' |cut -d " " -f2 #不变

rm -f "$expected" "$years_given" # 不变
