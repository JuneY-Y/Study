#!/bin/dash

found=0
prev_files=

for file in "$@"
do
    for prev in $prev_files
    do
        if cmp -s "$file" "$prev"
        then
            echo "ln -s $prev $file"
            found=1
            break
        fi
    done
    prev_files="$prev_files $file"
done

if [ "$found" -eq 0 ]
then
    echo "No files can be replaced by symbolic links"
fi