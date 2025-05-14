#!/bin/dash

string1=$1
string2=$2
# echo "$string"
n=$(echo "$string1"| grep -Eo "[0-9]+")
echo "$n"
m=$(echo "$string2"| grep -Eo "[0-9]+")
echo "$m"
count_num=$n
while [ $count_num -le $m ]; do
    echo "$count_num"
    count_num=$(( count_num+1 ))
    # echo $count_num
done
# echo $count_num