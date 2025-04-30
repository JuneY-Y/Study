#!/bin/bash

file="$1"

n=$(grep "Nobel Prize for physics" awards.psv | sort -t'|' -k2,2n | awk -F'|' '!seen[$2]++' |head -n 1 | cut -d '|' -f2,2)

m=$(grep "Nobel Prize for physics" awards.psv | sort -t'|' -k2,2n | awk -F'|' '!seen[$2]++' |tail -n 1 | cut -d '|' -f2,2)


seq "$n" "$m"