#!/bin/dash
##🌟 掌握的-d 以及ls 非常不熟悉。重新写
# lists all “happy” directories in the current directory.

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