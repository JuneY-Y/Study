#!/bin/dash

dir1="$1"
dir2="$2"

for file in "$dir1"/*; do
    filename=$(basename "$file")

    if [ -f "$dir2/$filename" ]; then

        if cmp -s "$file" "$dir2/$filename"; then
            echo "$filename"
        fi
    fi
    
done | sort