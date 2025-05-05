#!/bin/dash

for file in *;do
    if [ -d "$file" ]; then
        #num=$(ls "$file" | wc -l)
        count=$(find "$file" -mindepth 1 -maxdepth 1 | wc -l) #直接寻找
        if [ "$count" -ge 2 ]; then
            echo "$file"
        fi
    fi
done