#!/bin/dash

for cfile in "$@"; do
    while IFS= read -r line; do ## read line by line 🌟
        # 只抓 #include "xxx.h"
        include=$(echo "$line" | grep -Eo '#include "([^"]+\.h)"' | sed -E  's/#include "//; s/"$//')
        if [ -n "$include" ]; then ## 相当于 ! -z string非空
            if [ ! -r "$include" ]; then # 文件系统层面，比如目录里有没有 abc.h 这个文件
                echo "$include included into $cfile does not exist"
            fi
        fi
    done < "$cfile"
done
# #!/bin/dash
# file1=$1
# file2=$2
# ##need to for loop all of file
# #when file is checked, if include "d.h" not exist d.h in directory. then print it in standout
# for f in "$@";do
#     while IFS= read -r line;do
#         check=$(grep -Eo '"[A-Za-z]*.\.h"')
        
#         check_name=$(echo "$check"|sed 's/"//g')
#         # echo "$check_name"
#         if [ ! -r "$check_name" ];then
#             echo ""$check_name" included into a.c does not exist"
#         fi
#     done < "$file1"
    
# done
