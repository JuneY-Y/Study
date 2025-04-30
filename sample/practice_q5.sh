#!/bin/bash

# file="$1"

n=$(grep "Nobel Prize for physics" awards.psv | sort -t'|' -k2,2n | awk -F'|' '!seen[$2]++' |head -n 1 | cut -d '|' -f2,2)

m=$(grep "Nobel Prize for physics" awards.psv | sort -t'|' -k2,2n | awk -F'|' '!seen[$2]++' |tail -n 1 | cut -d '|' -f2,2)

grep "Nobel Prize for physics" awards.psv | sort -t'|' -k2,2n | awk -F'|' '!seen[$2]++' |cut -d '|' -f2,2 >  "$award"

seq "$n" "$m" > "$expected"

diff "$expected" "$award" | grep '^>' |cut -d " " -f2 

rm -f "$expected" "$award" 
