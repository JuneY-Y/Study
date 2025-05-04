#!/bin/dash
# ==============================================================================
# name: practice_q12.sh
# aim: 计算国际象棋中，马（Knight）从给定位置出发所有可达的格子路径
#
# 说明：
# - 输入：一个棋盘位置（如 a1、d4 等）
# - 每一行输出：从上一轮格子可一步马走法扩展出的“新格子”，直到无法扩展
# - 每步结果按字母+数字格式升序（如 b3 c2）
# ==============================================================================

squares="$1"                     # 起始格子
squares_regex=XX                # 正则屏蔽已访问格子

# 如果还有格子可以扩展
while test -n "$squares"
do
    echo "$squares"             # 输出当前轮格子

    # 构造正则表达式，记录已访问格子
    squares_regex="$squares_regex|$(echo "$squares" | tr ' ' '|')"

    # 下一轮所有新可达格子
    squares="$(
        for square in $squares
        do
            # 提取列（a~h → 1~8）和行（数字）
            column_number=$(echo "$square" | cut -c1 | tr abcdefgh 12345678)
            row_number=$(echo "$square" | cut -c2)

            # 尝试所有马步组合（共8种）
            for column_delta in -2 -1 1 2
            do
                for row_delta in -2 -1 1 2
                do
                    # 只保留一个动两格，另一个动一格的情况（否则不是L型）
                    test "$(echo "$row_delta" | tr -d -)" = "$(echo "$column_delta" | tr -d -)" && continue

                    # 计算新位置
                    new_row=$((row_number + row_delta))
                    new_column_number=$((column_number + column_delta))
                    new_column=$(echo "$new_column_number" | tr 12345678 abcdefgh)

                    echo "$new_column$new_row"
                done
            done
        done |
        sort |                              # 排序
        uniq |                              # 去重
        grep '^[a-h][1-8]$' |               # 只保留在棋盘上的格子
        grep -Ev "$squares_regex" |         # 去掉已访问过的格子
        tr '\n' ' ' |                       # 转为单行
        sed 's/ *$//'                       # 去除末尾空格
    )"
done