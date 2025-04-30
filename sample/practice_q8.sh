#!/bin/dash

found=0
prev_list=$(mktemp)
matched_list=$(mktemp)

for file in "$@"
do
    # 如果当前文件已经是一个匹配结果（被替换过），就跳过
    if grep -Fx "$file" "$matched_list" >/dev/null; then
        continue
    fi

    matched=0

    while read prev
    do
        # 如果prev是一个已被替换过的目标文件，也跳过
        if grep -Fx "$prev" "$matched_list" >/dev/null; then
            continue
        fi

        if cmp -s "$file" "$prev"; then
            echo "ln -s $prev $file"
            echo "$file" >> "$matched_list"  # 标记为被替换过
            found=1
            matched=1
            break
        fi
    done < "$prev_list"

    if [ "$matched" -eq 0 ]; then
        echo "$file" >> "$prev_list"
    fi
done

rm -f "$prev_list" "$matched_list"

if [ "$found" -eq 0 ]; then
    echo "No files can be replaced by symbolic links"
fi
# #!/bin/dash

# found=0
# # 创建临时文件保存处理过的文件列表
# prev_list=$(mktemp)

# for file in "$@"
# do
#     matched=0

#     while read prev
#     do
#         if cmp -s "$file" "$prev"
#         then
#             echo "ln -s $prev $file"
#             found=1
#             matched=1
#             break
#         fi
#     done < "$prev_list"

#     # 只有在没匹配过时才添加到列表
#     if [ "$matched" -eq 0 ]
#     then
#         echo "$file" >> "$prev_list"
#     fi
# done

# # 清理临时文件
# rm -f "$prev_list"

# if [ "$found" -eq 0 ]
# then
#     echo "No files can be replaced by symbolic links"
# fi