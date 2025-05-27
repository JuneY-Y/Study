#!/bin/dash

# 保存 stdin 到临时文件
tmpfile=$(mktemp)
cat > "$tmpfile"

# 按行处理
lineno=0
while read -r line; do
    lineno=$((lineno + 1))
    if echo "$line" | grep -Eq '^#[0-9]+$'; then
        n=$(echo "$line" | sed 's/#//')
        sed -n "${n}p" "$tmpfile"
    else
        echo "$line"
    fi
done < "$tmpfile"

# 清理临时文件
rm "$tmpfile"