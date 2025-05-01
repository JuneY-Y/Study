#!/bin/dash
## 11先不写，这个代码是完全错的。
dir1=$1
dir2=$2

# 临时文件
tmp1=$(mktemp)
tmp2=$(mktemp)
common=$(mktemp)
only1=$(mktemp)
only2=$(mktemp)

# 获取两个目录树中的所有相对路径文件（按字典序排序）
cd "$dir1" || exit 1
find . -type f | sort > "$tmp1"

cd "$dir2" || exit 1
find . -type f | sort > "$tmp2"

# 交集和差集：相同路径、仅在dir1、仅在dir2
comm -12 "$tmp1" "$tmp2" > "$common"
comm -23 "$tmp1" "$tmp2" > "$only1"
comm -13 "$tmp1" "$tmp2" > "$only2"

# 初始化计数器
same=0
diff=0

# 对所有在两个目录中相同路径的文件，比较大小
while IFS= read -r path
do
    size1=$(stat -c %s "$dir1/$path")
    size2=$(stat -c %s "$dir2/$path")
    if [ "$size1" -eq "$size2" ]; then
        same=$((same + 1))
    else
        diff=$((diff + 1))
    fi
done < "$common"

# 差集文件数量统计
only1_count=$(wc -l < "$only1")
only2_count=$(wc -l < "$only2")

# 输出最终结果（按顺序）
echo "$same $diff $only1_count $only2_count"

# 清理临时文件
rm -f "$tmp1" "$tmp2" "$common" "$only1" "$only2"