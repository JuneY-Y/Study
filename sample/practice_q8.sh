#!/bin/dash

found=0
prev_list=$(mktemp)
matched_list=$(mktemp)
raw_output=$(mktemp)
final_output=$(mktemp)

for file in "$@"
do
    # 如果当前文件已经被匹配过，则跳过
    if grep -Fx "$file" "$matched_list" >/dev/null; then
        continue
    fi

    matched=0

    while read prev
    do
        # 如果前面的文件也已经被匹配过，则跳过
        if grep -Fx "$prev" "$matched_list" >/dev/null; then
            continue
        fi

        if cmp -s "$file" "$prev"; then
            echo "ln -s $prev $file" >> "$raw_output"
            echo "$file" >> "$matched_list"
            found=1
            matched=1
            break
        fi
    done < "$prev_list"

    if [ "$matched" -eq 0 ]; then
        echo "$file" >> "$prev_list"
    fi
done

# 去除重复（包括反向）
if [ "$found" -eq 1 ]; then
    sort "$raw_output" | while read -r line
    do
        set -- $line
        src=$3
        dst=$4

        # 生成规范形式（按文件名排序）
        if [ "$src" -gt "$dst" ] 2>/dev/null; then
            key="$dst $src"
        else
            key="$src $dst"
        fi

        # 如果已经输出过这个组合，跳过
        if grep -Fx "$key" "$final_output" >/dev/null; then
            continue
        fi

        echo "$key" >> "$final_output"
    done

    # 按源文件编号排序输出
    sort -k1.5n "$final_output" | while read src dst
    do
        echo "ln -s $src $dst"
    done
else
    echo "No files can be replaced by symbolic links"
fi

# 清理临时文件
rm -f "$prev_list" "$matched_list" "$raw_output" "$final_output"