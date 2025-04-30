#!/bin/dash

found=0
prev_list=$(mktemp)

for file in "$@"
do
    while read prev
    do
        # 避免 file 和自己比（或比过了）
        [ "$file" = "$prev" ] && continue

        if cmp -s "$file" "$prev"
        then
            echo "ln -s $prev $file"
            found=1
            break
        fi
    done < "$prev_list"

    # 不论是否找到匹配，都要加入 prev_list
    echo "$file" >> "$prev_list"
done

rm -f "$prev_list"

if [ "$found" -eq 0 ]
then
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