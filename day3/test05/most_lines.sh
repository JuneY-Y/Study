#!/bin/dash
## 忘记用-gt了。 而且赋值需要写在全局变量 检查变量是否写错
maxlines=0
max_file=""

for file in "$@"; do
    count=$(wc -l < "$file")
    if [ "$count" -gt "$maxlines" ]; then
        maxlines=$count
        max_file=$file
    fi
done
echo "$max_file"