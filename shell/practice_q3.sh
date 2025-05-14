#!/bin/dash
##🌟 掌握的-d 以及ls 非常不熟悉。重新写
# lists all “happy” directories in the current directory.
# 可以记下模板:
# for item in *; do
#     if [ -d "$item" ]; then
#     fi
# done
# test: ./practice_q3.sh

# Loop over all items (files and directories) in the current directory
for item in *; do #for loop all✅
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