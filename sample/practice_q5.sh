#!/bin/bash

# file="$1"
regex="$1"
file="$2"

matching_lines=$(grep -E "^$regex$" "$file")

if [ -z "$matching_lines" ]; then
        echo "No awards matched"
        exit 0
fi 

years_given=$(mktemp)
n=$(grep "Nobel Prize for physics" awards.psv | sort -t'|' -k2,2n | awk -F'|' '!seen[$2]++' |head -n 1 | cut -d '|' -f2,2)

m=$(grep "Nobel Prize for physics" awards.psv | sort -t'|' -k2,2n | awk -F'|' '!seen[$2]++' |tail -n 1 | cut -d '|' -f2,2)

grep "Nobel Prize for physics" awards.psv | sort -t'|' -k2,2n | awk -F'|' '!seen[$2]++' |cut -d '|' -f2,2 >  "$award"

seq "$n" "$m" > "$expected"

diff "$expected" "$award" | grep '^>' |cut -d " " -f2 

rm -f "$expected" "$award" 
