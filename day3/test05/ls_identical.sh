#!/bin/dash
di1=$1
di2=$2
file=""
for file1 in "$di1"/*; do
    echo "$file1"
    for file2 in "$di2"/*;do
        echo "$file2"
        if [ "$file1" -eq "$file2" ];then
            file=$(echo "$file1"|)
        fi
    done
done
