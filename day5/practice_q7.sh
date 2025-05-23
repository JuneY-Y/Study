#!/bin/dash

for file in "$@"; do
    if echo "$file"| grep -Eq "\."; then
        echo "# $file already has an extension"
        continue
    fi

    if head -n1 "$file"|grep -Eq "^#!"; then
        echo "# $file does not have a #! line"

done