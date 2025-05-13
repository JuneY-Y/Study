#!/bin/dash

string1=$1
string2=$2
# echo "$string"
n=$(echo "$string1"| grep -Eo "[0-9]+")
echo "$n"
m=$(echo "$string2"| grep -Eo "[0-9]+")
count_num=$n
while [ $n -le $m ];do
    count_num=$(( $count_num + 1 ))
done
echo $count_num