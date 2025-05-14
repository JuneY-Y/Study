#!/bin/dash
## Find Years an Award Was Not Given

award=$1
filename=$2

real_award=$(cut -d '|' -f1 $filename)
# echo "$real_award"
for awards in $award;do
    years=$(grep -E "$awards" "$filename"| )

done