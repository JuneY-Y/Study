#!/bin/dash

prev_list=$(mktemp)
matched_list=$(mktemp)
output_list=$(mktemp)

found=0

for file in "$@"
do
    # 跳过 file 自己匹配自己
    if grep -qF "|$file|" "$matched_list"; then
        continue
    fi

    while read prev
    do
        # 跳过自引用
        [ "$prev" = "$file" ] && continue

        # 如果已经出现过这对，就跳过
        if grep -qF "|$prev|$file|" "$matched_list" || grep -qF "|$file|$prev|" "$matched_list"; then
            continue
        fi

        if cmp -s "$file" "$prev"; then
            echo "$prev|$file" >> "$matched_list"
            echo "$file|$prev" >> "$output_list"  # key 是目标文件，方便按 $@ 顺序输出
            found=1
            break
        fi
    done < "$prev_list"

    echo "$file" >> "$prev_list"
done

# ✅ 严格按 $@ 顺序输出
for file in "$@"
do
    match=$(grep "^$file|" "$output_list" | head -n1)
    if [ -n "$match" ]; then
        src=$(echo "$match" | cut -d'|' -f2)
        tgt=$(echo "$match" | cut -d'|' -f1)
        echo "ln -s $src $tgt"
    fi
done

if [ "$found" -eq 0 ]; then
    echo "No files can be replaced by symbolic links"
fi

rm -f "$prev_list" "$matched_list" "$output_list"