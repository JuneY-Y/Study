#!/bin/dash

#读取每行
while read -r line; do
    if echo "$line" | grep -q ' '; then
        left=$(echo "$line" | cut -d ' ' -f1)
        right=$(echo "$line" | cut -d ' ' -f2-)
        echo "${left},${right}"
    else
        echo "there are no space in $line"
    fi 
done 