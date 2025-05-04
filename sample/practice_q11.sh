#!/bin/dash
# wc -l : 统计文本中总共有多少行（即换行符的数量）。
dir1=$1
dir2=$2

tmp1=$(mktemp)
tmp2=$(mktemp)
common=$(mktemp)
only1=$(mktemp)
only2=$(mktemp)

# ✅ 不要 cd，直接 find + 相对路径
# find "$dir1" -type f | sed "s|^$dir1/||" | sort > "$tmp1"
# find "$dir2" -type f | sed "s|^$dir2/||" | sort > "$tmp2"
# 获取两个目录树中的相对路径（不使用 sed，进入目录执行 find）
(cd "$dir1" || exit 1; find . -type f | sort) > "$tmp1"
(cd "$dir2" || exit 1; find . -type f | sort) > "$tmp2"

comm -12 "$tmp1" "$tmp2" > "$common"
comm -23 "$tmp1" "$tmp2" > "$only1"
comm -13 "$tmp1" "$tmp2" > "$only2"

same=0
diff=0

while IFS= read -r path; do
    size1=$(stat -c %s "$dir1/$path")
    size2=$(stat -c %s "$dir2/$path")
    if [ "$size1" -eq "$size2" ]; then
        same=$((same + 1))
    else
        diff=$((diff + 1))
    fi
done < "$common"

only1_count=$(wc -l < "$only1")
only2_count=$(wc -l < "$only2")

echo "$same $diff $only1_count $only2_count"

rm -f "$tmp1" "$tmp2" "$common" "$only1" "$only2"