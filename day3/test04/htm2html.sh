#!/bin/dash

for f in *.htm;do
    echo "$f"
    original=$(echo "$f" | sed "s/\.[A-Za-z]//")
    echo "$original"
    suffix=".html"
    # original_suffix=$(echo "$f"|grep -oE "\.[A-Za-z]+$")
    # if echo "$original"| grep -qE "$original";then
    new_suffix="$original$suffix"
    echo "$new_suffix"
    mv "$f" "$new_suffix"
    # fi  
done