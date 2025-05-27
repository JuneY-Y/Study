#!/bin/dash
#1️⃣ 直接一次性读两遍 stdin
# 保存 stdin 到临时文件
tmpfile=$(mktemp)
cat > "$tmpfile"

# 按行处理
count=0
while read -r line; do
    count=$((lineno + 1))
    if echo "$line" | grep -Eq '^#[0-9]+$'; then
        n=$(echo "$line" | sed 's/#//')
        sed -n "${n}p" "$tmpfile" #sed -n '3p' file 打印文件第3行
    else
        echo "$line"
    fi
done < "$tmpfile"

# 清理临时文件
rm "$tmpfile"