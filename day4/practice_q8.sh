#!/bin/dash
flag=0
procesed=" "
for file1 in "$@"; do
#commands to replace some of the files with symbolic links.
    for file2 in "$@";do
        if [ "$file1" != "$file2" ]; then
            continue
        fi
       if cmp -s "$file1" "$file2";then
        echo "ln -s "$file1" "$file2""
        continue
       fi
    done
    flag=1
done