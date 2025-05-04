#!/usr/bin/env dash
	# 功能：找出某个奖项从第一次颁发到最后一次之间，未曾颁发的年份。
	# •	输入：
	# •	$1：奖项名称
	# •	$2：数据文件（pipe-separated）
	# •	核心逻辑：
	# •	提取该奖项出现的所有年份 → years
	# •	用 seq 生成完整年份序列
	# •	每年检查是否在 years 中 → 不在即为缺失年份
# ==============================================================================
# name: missing_award_years.sh
# aim: Given an award name and a data file, print all missing years in which
#      the award was not given (between its earliest and latest award year)
# ==============================================================================

# 查找所有与奖项名完全匹配的记录行（以“奖项名|”开头）
matching_lines=$(grep -E "^$1\|" "$2")

# 如果没有匹配行，则输出错误并退出
if [ -z "$matching_lines" ]; then
    echo "No award matching '$1'" >&2
    exit 1
fi

# 提取所有已颁奖年份（第二列），升序排序
years=$(echo "$matching_lines" | cut -d'|' -f2 | sort -n)

# 找到最早和最晚的年份（用于生成完整年份区间）
start=$(echo "$years" | head -n1)
end=$(echo "$years" | tail -n1)

# 输出在区间中但未颁发奖项的年份
for year in $(seq "$start" "$end"); do
    if ! echo "$years" | grep -q "$year"; then
        echo "$year"
    fi
done