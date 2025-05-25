#!/bin/dash

for f in *.htm;do
    echo "$f"
    original=$(echo "$f" | sed "s/\.htm//")
    echo "$original"
    newfile="$original".html
    if [ -e "$newfile" ]; then
        echo ""$newfile" exists" 1>&2
        exit 1 ## 这里为什么exit1？
    else
        mv "$f" "$newfile"
    fi
    
   
    
   
done
exit 0