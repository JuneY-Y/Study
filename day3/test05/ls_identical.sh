#!/bin/dash
for file in "$@":do
    # while IFS= read -r line; do ## read line by line 
    count=$(cat "$file"|wc -l)
    echo "$count"

    
done