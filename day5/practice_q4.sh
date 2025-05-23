#!/bin/dash
## 需要再做一遍，while这里有些遗忘
filename="$1"

n=$(sort -n "$filename"| head -n 1)
m=$(sort -n "$filename"| tail -n 1)
numbers=$(cat "$filename"|sort -n)
start="$n"

# echo $start
while [ $start -le $m ]; do
    if ! echo $numbers|grep -q "$start"; then
        echo "$start"
    fi
    start=$(( start+1 ))
done



