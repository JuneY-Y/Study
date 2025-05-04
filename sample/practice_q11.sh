#!/bin/dash
# ==============================================================================
# name: practice_q11.sh
# aim: 比较两个目录树中具有相同相对路径的文件是否存在、大小是否一致
#
# 输出格式为四个整数：
#   1. 两个目录中相同路径的文件，且大小相同的数量
#   2. 两个目录中相同路径的文件，但大小不同的数量
#   3. 只出现在第一个目录中的文件数量
#   4. 只出现在第二个目录中的文件数量
# ==============================================================================

dir1=$1
dir2=$2

# 创建临时文件保存路径列表和集合运算结果
tmp1=$(mktemp)
tmp2=$(mktemp)
common=$(mktemp)
only1=$(mktemp)
only2=$(mktemp)

# ✅ 使用 subshell 进入目录，输出相对路径（省去 sed 处理）
(cd "$dir1" || exit 1; find . -type f | sort) > "$tmp1"
(cd "$dir2" || exit 1; find . -type f | sort) > "$tmp2"

# 生成集合：相同路径、只在dir1、只在dir2
comm -12 "$tmp1" "$tmp2" > "$common"
comm -23 "$tmp1" "$tmp2" > "$only1"
comm -13 "$tmp1" "$tmp2" > "$only2"

same=0       # 同路径同大小的文件数量
diff=0       # 同路径但大小不同的文件数量

# 比较所有“路径相同”的文件是否“大小一致”
while IFS= read -r path; do
    size1=$(stat -c %s "$dir1/$path")
    size2=$(stat -c %s "$dir2/$path")
    if [ "$size1" -eq "$size2" ]; then
        same=$((same + 1))
    else
        diff=$((diff + 1))
    fi
done < "$common"

# wc -l：统计行数，相当于统计 only1 和 only2 中有多少个路径
only1_count=$(wc -l < "$only1")
only2_count=$(wc -l < "$only2")

# 输出题目要求的四个数（空格分隔）
echo "$same $diff $only1_count $only2_count"

# 删除临时文件
rm -f "$tmp1" "$tmp2" "$common" "$only1" "$only2"