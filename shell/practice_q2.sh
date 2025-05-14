#!/bin/dash
filename=$1
echo $filename
count_man=$(grep -E "\|M$" "$filename")
echo "$count_man"
count_woman=$(grep -E "\|F$" "$filename")
echo "$count_woman"
# while read -r "$filename"; do
for line1 in "$count_man"; do
    for line2 in "$count_woman"; do
        if grep -qE "$line1"
    done
done

# done