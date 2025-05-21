#!/bin/dash
# ==============================================================================
# name: practice_q11_v2.sh
# aim: 同路径文件的大小比较 + 独有文件统计（模仿图中结构）
# ==============================================================================

dir1=$1
dir2=$2

num_same_size=0
num_not_same_size=0
num_only_one=0
num_only_two=0

# 获取两个目录中所有文件路径（绝对路径）
files_dir1=$(find "$dir1" -type f)
files_dir2=$(find "$dir2" -type f)

# 遍历 dir1 中的每个文件，提取其相对路径
for file1 in $files_dir1; do
    # 去除 dir1 路径前缀，得到相对路径
    file_rel=$(echo "$file1" | sed "s|^$dir1/||")
    file2="$dir2/$file_rel"

    if [ -f "$file2" ]; then
        # 文件也存在于 dir2，比较大小
        size1=$(wc -c < "$file1")
        size2=$(wc -c < "$file2")

        if [ "$size1" -eq "$size2" ]; then
            num_same_size=$((num_same_size + 1))
        else
            num_not_same_size=$((num_not_same_size + 1))
        fi
    else
        # 文件只存在于 dir1
        num_only_one=$((num_only_one + 1))
    fi
done

# 再遍历 dir2，统计只在 dir2 出现的文件
for file2 in $files_dir2; do
    file_rel=$(echo "$file2" | sed "s|^$dir2/||")
    file1="$dir1/$file_rel"

    if [ ! -f "$file1" ]; then
        num_only_two=$((num_only_two + 1))
    fi
done

# 输出结果
echo "$num_same_size $num_not_same_size $num_only_one $num_only_two"