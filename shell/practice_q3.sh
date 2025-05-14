#!/bin/dash

# while [ -f "#$@" ]; do
# done < dictionary

for item in *; do
    if [ -d "$item" ]; then
        count=$(ls -A "$item"|wc -l)
        if [ "$count" -ge 2 ]; then
            echo "$item"
        fi
    fi
    # if [ "$count" -ge 2 ]; then
    #     echo "$item"
    # fi
done