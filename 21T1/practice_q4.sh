#!/bin/dash

n=$(echo $1 | grep -Eo '[0-9]+')
m=$(echo $2 | grep -Eo '[0-9]+')

# echo $n
# echo $m 
current_num=$n  ##初始化

while [ "$current_num" -le "$m" ]; do
        result=$(echo $n | sed "s/$n/$current_num/")
        echo $result
        current_num=$((current_num+1))
done