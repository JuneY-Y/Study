#!/bin/dash

max=0
result=""
#$@ 是全局变量的索引
for inputs in "$@"
do
    current_line=$( wc -l < "$inputs" )
    if [ "$current_line" -gt "$max" ]
    then
     max=$current_line
     result=$inputs
    fi
done

echo "$result"