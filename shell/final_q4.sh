#!/bin/dash
# Missing Number Finder
# test： ./final_q4.sh numbers_1.txt
filename=$1

numbers=$(cat "$filename" | sort -n)
# echo $numbers
min=$(echo "$numbers"|head -n1)
max=$(echo "$numbers"|tail -n1)

count_num=$min

while [ $count_num -le $max ]; do

    if ! echo “$numbers”| grep -qE “$count_num”;then ##条件判断语句在dash里面没有()
        echo $count_num
    fi
    count_num=$(( count_num+1 ))
done