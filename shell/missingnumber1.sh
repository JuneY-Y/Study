#!/bin/dash

## 用flag判断 missing number
## 读取文件

# bolloon flag="flase"
filename=$1

numbers=$(cat $filename| sort|uniq|sed 's/ /\\n/g')
echo $numbers