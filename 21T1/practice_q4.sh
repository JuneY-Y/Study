#!/bin/dash

n=$1
m=$2

n=$(echo $n | grep -Eo '[0-9]+')
m=$(echo $m | grep -Eo '[0-9]+')

echo $n
echo $m

while [ '$current_num' -le '$m' ]; do
        result=$(echo $n | sed "s/n/$current_num/")
        echo $result
        current_num=$((current_num+1))
done