#!/bin/dash

regex="$1"
file="$2"

matching_lines=$(grep -E "^${regex}\|" "$file")
if [ -z "$matching_lines" ]; then
    echo "No awards matched"
    exit 0
fi

years_given=$(mktemp)
expected_years=$(mktemp)

# 提取已颁奖年份，排序去重写入临时文件
printf '%s\n' "$matching_lines" | cut -d '|' -f2 | sort -n | uniq > "$years_given"

# 获取最早和最晚年份
n=$(head -n1 "$years_given")
m=$(tail -n1 "$years_given")

# 生成完整年份区间
seq "$n" "$m" > "$expected_years"

# 输出缺失年份

# 1.	两个文件都必须已经排好序（用 sort -n）
# 2.	comm 会一列一列输出，所以用 -23 是为了“去掉第2列（只在file2中）和第3列（公共行）”

comm -23 "$expected_years" "$years_given" #只输出 第一个文件中有，但第二个文件中没有 的行。

# 清理临时文件
rm -f "$years_given" "$expected_years"

# #!/bin/bash

# # file="$1"
# regex="$1"
# file="$2"

# matching_lines=$(grep -E "^${regex}\|" "$file")
# #matching_lines=$(grep -E "^$regex\|" "$file")
# # echo "$matching_lines"
# if [ -z "$matching_lines" ]; then
#         echo "No awards matched"
#         exit 0
# fi 

# years_given=$(mktemp)   # mktemp 保证每次都是唯一安全的临时文件名
# # grep -E "^$regex\|" "$file" | cut -d '|' -f2 | sort -n | uniq > "$years_given" 我会写的内容
# printf '%s\n' "$matching_lines" | cut -d '|' -f2 | sort -n | uniq > "$years_given"

# n=$(head -n1 "$years_given")
# m=$(tail -n1 "$years_given")

# # echo "First year: $n"
# # echo "Last year:  $m"

# expected=$(mktemp)

# # n=$(grep "Nobel Prize for physics" awards.psv | sort -t'|' -k2,2n | awk -F'|' '!seen[$2]++' |head -n 1 | cut -d '|' -f2,2)

# # m=$(grep "Nobel Prize for physics" awards.psv | sort -t'|' -k2,2n | awk -F'|' '!seen[$2]++' |tail -n 1 | cut -d '|' -f2,2)

# # grep "Nobel Prize for physics" awards.psv | sort -t'|' -k2,2n | awk -F'|' '!seen[$2]++' |cut -d '|' -f2,2 >  "$award"

# # 先生成 expected 内容
# seq "$n" "$m" > "$expected"

# echo "🔹 Given Years (from file: $years_given):"
# cat "$years_given"
# echo "🔹 Expected Years (from file: $expected):"
# cat "$expected"
# echo "🔹 Missing Years:"

# # diff "$expected" "$years_given" | grep '^>' |cut -d " " -f2 #不变
# diff "$expected" "$years_given" | grep '^>' | sed 's/^> *//'

# rm -f "$expected" "$years_given" # 不变
