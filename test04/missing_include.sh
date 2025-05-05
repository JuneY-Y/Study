#!/bin/dash

for file in "$@" ; do
    grep -e "#include \".*\.h\"" "$file" | \
    while read -r line; do
        head_file=$(echo "$line"| cut -d"\"" -f2)

        if [ ! -f "$head_file" ]; then
        # if [ ! -f "$head_file" ]; then
            echo "$head_file included into $file does not exist"
        fi
    done
done

