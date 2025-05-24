#!/bin/dash
flag=0
processed=""
for file1 in "$@"; do
        case "$processed" in
            *" $file1 "*) continue ;;
        esac
#commands to replace some of the files with symbolic links.
    for file2 in "$@";do
        if [ "$file1" != "$file2" ]; then
            # if echo "$processed"| grep -qE "(^| )$file1( |$)"; then
            #     continue
            # fi
            # continue 
            # 这里🌟 如果processed中已经存在了file2那么跳过还是继续啊continue？需要熟悉这段代码以及if替换格式
            case "$processed" in
                *" $file2 "*) continue ;;
            esac
            if cmp -s "$file1" "$file2";then
                echo "ln -s "$file1" "$file2""
                processed="$processed $file2 "
                flag=1
            fi
        fi
        # if cmp -s "$file1" "$file2";then
        #     echo "ln -s "$file1" "$file2""
        #     continue
        # fi
    done
    processed="$processed $file1 " ##务必拼接的时候加上空格，因为🌟字符串匹配需要明确分隔边界
done
# echo "$processed"
[ $flag -eq 0 ]&& echo "No files can be replaced by symbolic links"  #重新学一遍🌟