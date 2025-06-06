#!/bin/dash
# ==============================================================================
# name: practice_q8.sh
# aim: Find all pairs of identical files and suggest symbolic links
# #题目目的：
# - 找出所有内容完全相同的文件对，并推荐用 ln -s 建立符号链接

# 关键技术：
# - cmp 比较文件内容
# - case 语句判断文件是否已处理
# - 参数顺序控制输出顺序
# - 防止重复、反向或自我链接
# This script compares the contents of all input files.
# For each pair of files with identical content, it prints:
#   ln -s source target
# Ensures:
#   - Each file is only used once as target
#   - Output follows input order
#   - No duplicate or reversed links are printed
# If no matches found, prints:
#   No files can be replaced by symbolic links
#
# Written in POSIX-compliant shell for COMP2041/9044
# ==============================================================================
printed=0
processed=""

for file1 in "$@"; do
    # file1 如果被处理过就跳过（避免成为 file2）
    case "$processed" in
        *" $file1 "*) continue ;;
    esac

    for file2 in "$@"; do
        # file1 不和自己比
        [ "$file1" = "$file2" ] && continue

        # file2 处理过就跳过
        case "$processed" in
            *" $file2 "*) continue ;;
        esac

        if cmp -s "$file1" "$file2"; then
            echo "ln -s $file1 $file2"
            printed=1
            processed="$processed $file2 "
        fi
    done

    processed="$processed $file1 "
done

test "$printed" -eq 0 && echo "No files can be replaced by symbolic links"