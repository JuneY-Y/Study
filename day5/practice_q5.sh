#!/bin/dash

award=$1
file=$2

year=$(grep -E "^$1" $2|cut -d '|' -f2|sort -n|uniq)
# echo "$year"
if [ -z "$year" ];then
    echo "No award matching '$1'"
    exit 0
fi

n=$(echo "$year"|head -n1)
m=$(echo "$year"|tail -n1)
start="$n"
while [ $start -le $m ];do
    if ! echo "$year"|grep -Eq "$start"; then
        echo "$start"
    fi
    start=$((start+1))
done
# echo "$n"
# echo "$m"
