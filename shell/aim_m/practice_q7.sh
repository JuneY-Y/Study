#!/bin/dash

for pathname in "$@"; do
    # case "$(head -1 "$pathname")" in
    #     *perll*
    # esac
    cat "$file_name" | head -n 1 | while read -r line; do

    if ! echo "$line" | grep -Eq "^#!"; then
        echo "$file_name doe not have a #! line"
    elif ! echo "$line" | grep -Eq "^#!.*(python|sh|perl)"; then
        echo "$file_name no extension for shebang line"
    elif echo "$line"|grep -Eq "^#!.*python"; then
        if [ -f "$file_name.py" ]; then
            echo "$file_name.py already exists"
        else
            echo "mv $file_name $file_name.py"
        fi




done