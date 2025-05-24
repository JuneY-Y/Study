#!/bin/dash
flag=0
processed=""
for file1 in "$@"; do
#commands to replace some of the files with symbolic links.
    for file2 in "$@";do
        if [ "$file1" != "$file2" ]; then
            # continue 
            # 这里🌟 如果processed中已经存在了file2那么跳过还是继续啊continue？
            case "$processed" in
                *" $file2 "*) continue ;;
            esac
            if cmp -s "$file1" "$file2";then
                echo "ln -s "$file1" "$file2""
                processed="$processed $file2"
            fi
        fi
        # if cmp -s "$file1" "$file2";then
        #     echo "ln -s "$file1" "$file2""
        #     continue
        # fi
    done
    processed="$processed $file2"
    flag=1
done
echo "$processed"