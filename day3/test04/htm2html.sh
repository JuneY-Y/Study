#!/bin/dash

for f in *.htm;do
    # echo "$f"
    original=$(echo "$f" | sed "s/\.htm//")
    # echo "$original"
    suffix=".html"
    if ! echo "$f"|grep -Eq "\.html";then
    # original_suffix=$(echo "$f"|grep -oE "\.[A-Za-z]+$")
    # if echo "$original"| grep -q E "$original";then
        new_suffix="$original$suffix"
        # echo "$new_suffix"
        mv "$f" "$new_suffix"
    else
        echo ""$f" exists" 1>&2
        exit 1
    fi
    # fi  
done
exit 0