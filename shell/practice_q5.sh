#!/bin/dash
## Find Years an Award Was Not Given

award=$1
filename=$2
# real_award=$(cut -d '|' -f1 $filename)
# echo "$real_award"
for awards in $award;do
    years=$(grep -E "$awards" "$filename"| cut -d '|' -f2,2|sort -n|uniq)
    # echo "$years"
    start=$(echo "$years"|head -n1)
    end=$(echo "$years"|tail -n1)
    # echo "$start"
    start_count=$start
    while [ $start_count -le $end ]; do
        if ! echo 
    done
    start_count=$((start_count+1))

done