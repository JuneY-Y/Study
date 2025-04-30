#!/bin/dash

found=0
prev_files=
output=""

for file in "$@"
do
    for prev in $prev_files
    do
        if cmp -s "$file" "$prev"
        then
            output="$output
ln -s $prev $file"
            found=1
            break
        fi
    done
    prev_files="$prev_files $file"
done

if [ "$found" -eq 1 ]
then
    printf "%s\n" "$output" | sed '/^$/d'  # 删除空行并输出所有命令
else
    echo "No files can be replaced by symbolic links"
fi