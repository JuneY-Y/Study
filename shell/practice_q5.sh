#!/bin/dash
## Find Years an Award Was Not Given
# -ne是数字比较

award=$1
filename=$2
real_award=$(cut -d '|' -f1 $filename)

if ! echo "$real_award"|grep -qE "^$award$";then
    echo "practice_q5.sh: no awards match '"$award"'"
    exit 0
fi

# echo "$real_award"
# for awards in $award;do
years=$(grep -E "^$awards$" "$filename"| cut -d '|' -f2,2|sort -n|uniq)
# echo "$years"
start=$(echo "$years"|head -n1)
end=$(echo "$years"|tail -n1)
# echo "$start"
start_count=$start
while [ $start_count -le $end ]; do
    if ! echo "$years"| grep -qE "^$start_count$" ;then
        echo "$start_count"
    fi
    start_count=$((start_count+1))
done
# done