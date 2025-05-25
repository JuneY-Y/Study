#!/bin/dash

for f in "$@";do
    original=$(echo "$f"|grep -oE "^[A-Za-z]+\.")
    suffix=".html"
    original_suffix=$(echo "$f"|grep -oE "\.[A-Za-z]+$")
    if echo "$original"| grep -qE "$original";then
        new_suffix=$original$suffix
        echo "$new_suffix"
        mv "$f" "$new_suffix"
    fi  
done