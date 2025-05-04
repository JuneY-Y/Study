#!/usr/bin/env dash
	# 功能：找出某个奖项从第一次颁发到最后一次之间，未曾颁发的年份。
	# •	输入：
	# •	$1：奖项名称
	# •	$2：数据文件（pipe-separated）
	# •	核心逻辑：
	# •	提取该奖项出现的所有年份 → years
	# •	用 seq 生成完整年份序列
	# •	每年检查是否在 years 中 → 不在即为缺失年份
    
# Given
# 1) a 'pipe separated values' file with award winners
# in the format:
#   award name
#   award year
#   winner name
#   winner gender
#   winner country
#   winner birth year
# 2) The name of an award
#
# find all years in which the award was *not* given

years=$(grep -E "^$1\|" "$2" | sort -t'|' -k2 | cut -d'|' -f2)

if [ -z "$years" ]; then
    echo "No award matching '$1'" >&2
    exit 1
fi

start=$(echo "$years" | head -n1)
end=$(echo "$years" | tail -n1)

for year in $(seq "$start" "$end"); do
    if ! echo "$years" | grep -q "$year"; then
        echo "$year"
    fi
done