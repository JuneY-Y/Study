#!/bin/dash

# 获取起始位置
start="$1"

# 棋盘列到数字的映射（a=1, ..., h=8）
letter_to_num() {
    ch="$1"
    ord=$(printf "%d" "'$ch")   # e.g. 'a' → 97
    echo $((ord - 96))          # 97 - 96 = 1 → 列号
}

# 数字到棋盘列的映射（1=a, ..., 8=h）
num_to_letter() {
    n="$1"
    printf "\\$(printf '%03o' "$((96 + n))")"
}

# 判断是否合法格子
is_valid() {
    [ "$1" -ge 1 ] && [ "$1" -le 8 ] && [ "$2" -ge 1 ] && [ "$2" -le 8 ]
}

# 全部已访问格子（全局变量）
visited=""

# 当前层
current="$start"
echo "$start"

# 坐标偏移（8个方向）
dxs="-2 -2 -1 -1 1 1 2 2"
dys="-1 1 -2 2 -2 2 -1 1"

# 主循环
while [ -n "$current" ]
do
    next=""
    for square in $current
    do
        x=$(letter_to_num "$(printf '%s' "$square" | cut -c1)")
        y=$(printf '%s' "$square" | cut -c2)

        i=1
        for dx in $dxs
        do
            dy=$(echo "$dys" | cut -d' ' -f $i)
            i=$((i + 1))

            nx=$((x + dx))
            ny=$((y + dy))

            if is_valid "$nx" "$ny"
            then
                letter=$(num_to_letter "$nx")
                coord="$letter$ny"

                # 没访问过就加入
                echo "$visited" | grep -w "$coord" >/dev/null 2>&1 && continue
                echo "$next" | grep -w "$coord" >/dev/null 2>&1 && continue

                next="$next $coord"
            fi
        done
    done

    # 输出下一层
    if [ -n "$next" ]
    then
        # 去重、排序
        echo "$next" | tr ' ' '\n' | sort | uniq | tr '\n' ' ' | sed 's/ *$//'
    fi

    # 累加 visited
    visited="$visited $current"
    current=$(echo "$next" | tr ' ' '\n' | sort | uniq)
done