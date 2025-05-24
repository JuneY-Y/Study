#!/bin/dash

# 这道题用 flag 变量 printed 来判断是否有 ln -s 输出。
# 我们使用双重 for file1 in "$@" + for file2 in "$@" 来实现所有两两文件配对比较，
# 每次只比较不相同的文件名。为了避免重复处理同一文件（或对称反复比较），我们用 processed 记录已处理的文件名。
# 最终如果没有任何匹配的文件，
# 就用 flag printed=0 统一输出 “No files can be replaced…”。

flag=0
processed=""

for file1 in "$@"; do
    # case "$processed" in
    #     *" $file1 "*) continue;;
    # esac
    if echo "$procesed"| grep -qE "(^| )$file1( |$)"; then
        continue
    fi

    for file2 in "$@"; do
    done

done