#!/bin/dash

# 第一个参数：要创建的文件数量（正整数）
# 第二个参数：要写入的名字（字符串）
integer="$1"
name="$2"

count=1
while [ "$count" -le "$integer" ]
do
    # 注意这里使用 $count
    echo "hello $name" > "hello$count.txt"
    count=$((count + 1))
done

# #!/bin/dash

# integer=$1
# name=$2

# count=1

# while [ $count -le $integer ]
# do 
#     echo "hello $name" > "hello$number.txt"
#     count=$((count+1))

# done