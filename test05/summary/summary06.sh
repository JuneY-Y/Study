#!/bin/dash

#for any condition to if fi , fi is the end of this result judgment
if [ condition ];then

fi

#for loop下面的代码遍历当前目录下所有以 .txt 结尾的文件，对每个文件执行相应的操作。

for file in *.txt; do

done

#while loop 在循环的时候不固定的时候，进行使用
while [ condition ]; do

done

##example
count=1
while [ $count -le 5 ]; do
    echo "Count is $count"
    count=$((count+1))
done

# Count is 1
# Count is 2
# Count is 3
# Count is 4
# Count is 5