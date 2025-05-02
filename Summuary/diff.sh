#!/bin/dash

for file in "$dir1"/* #这会遍历 $dir1 目录下的所有文件（包含完整路径），更可靠，支持文件名带空格
do
    echo "$file"
done

file_name='basename "$ls_file1"'
if test -e "$dir2/$file_name"
if diff -i -w "$dir1/$file_name" "$dir2/$file_name" >/dev/null
echo "$file_name" 