#!/bin/dash

# 检查文件是否存在
if [ ! -f "diff_1.txt" ] || [ ! -f "diff_2.txt" ]; then
    echo "no file exit"
    exit 1
fi

# 使用diff -q检查文件是否相同
if diff -q diff_1.txt diff_2.txt > /dev/null; then
    echo "the same file"
else
    echo "not similar"
fi

