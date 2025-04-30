#!/bin/dash


# 逻辑说明：
# 	1.	第一段循环：找出最小值和最大值（min, max）
# 	2.	第二段循环：从 min+1 到 max-1 逐个枚举数字
# 	3.	第三段内层循环：检查这个数字是否出现在输入参数中
# 	4.	如果没有出现，就打印出来并退出

# Initialize min and max to the first argument
min=$1
max=$2
# found=false

# 不能这么写，shell没有int类型。直接写变量名就可: int lose

for num in "$@"; do
    [ "$num" -lt "$min" ] && min=$num
    [ "$num" -gt "$max" ] && max=$num
done

# 
# Step 1: Find the actual min and max from all input numbers
for i in $(seq "$((min + 1))" "$((max - 1))"); do
    found=false
    for n in "$@"; do
        if [ "$i" -eq "$n" ]; then
            found=true
            break
        fi
    done
# for循环里进行判断，如果found是false了，那么说明没有找到。所以echo"$i" 输出i的值
    if [ "$found" = false ]; then
        echo "$i"
        exit 0
    fi

done

    # seq "$((min+1))" "$((max-1))"

    # if [ "$input" -eq "$num" ]; then
    #     found=true
    #     break
    # else
    #     lose = $num 
    #     print"lose"
    
#     fi

# done