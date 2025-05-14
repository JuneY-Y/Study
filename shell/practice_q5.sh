#!/bin/dash
## Find Years an Award Was Not Given

award=$1
filename=$2
real_award=$(cut -d '|' -f1 $filename)
if [ $award -ne $real_awrd ];then
    echo "practice_q5.sh: no awards match '"$award"'"
fi

# echo "$real_award"
for awards in $real_award;do
    years=$(grep -E "$awards" "$filename"| cut -d '|' -f2,2|sort -n|uniq)
    # echo "$years"
    start=$(echo "$years"|head -n1)
    end=$(echo "$years"|tail -n1)
    # echo "$start"
    start_count=$start
    while [ $start_count -le $end ]; do
        if ! echo $start_count| grep -Eq $years ;then
            echo "$start_count"
        fi
    done
    start_count=$((start_count+1))

done