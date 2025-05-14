#!/bin/dash

filename=$1
country=$(cut -d '|' -f5,5 "$filename"|sort )
echo "$country"
for countries in "$country";do
    
done
