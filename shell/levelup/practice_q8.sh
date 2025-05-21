#!/bin/dash
# ==============================================================================
# name: practice_q8.sh (if/elif version)
# aim: Find all pairs of identical files and suggest symbolic links
# ==============================================================================

printed=0
processed=""

for file1 in "$@"; do
    # 如果 file1 已处理，跳过
    if echo "$processed" | grep -q " $file1 "; then
        continue
    fi

    for file2 in "$@"; do
        # 不和自己比较
        if [ "$file1" = "$file2" ]; then
            continue
        fi

        # 如果 file2 已处理，跳过
        if echo "$processed" | grep -q " $file2 "; then
            continue
        fi

        # 比较内容是否相同
        if cmp -s "$file1" "$file2"; then
            echo "ln -s $file1 $file2"
            printed=1
            processed="$processed $file2 "
        fi
    done

    processed="$processed $file1 "
done

if [ "$printed" -eq 0 ]; then
    echo "No files can be replaced by symbolic links"
fi