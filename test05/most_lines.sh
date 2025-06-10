#!/bin/dash

max=0
result=""
#$@ 是全局变量的索引
for inputs in "$@"
do
    cur_line=$( wc -l < "$inputs" )
    if [ "$cur_line" -gt "$max" ]
    then
     max=$cur_line
     result=$inputs
    fi
done

echo "$result"