#!/bin/dash
# ==============================================================================
# name: script.sh
# aim: Validate the course code format (4 uppercase letters + 4 digits) and check
#      if a file with the course code name exists (optional).
#
# Written by: JiamingYang (see my website niyoumengma.cn) z5452842 
## detail
## any involved bug and modified:
# - Fixed the file check logic to correctly use the variable $course_code.
# - Improved error messages for better clarity.
# ==============================================================================
course_code=$1

## 检测是否存在名为coursecode的文件
## $course_code 才是shell里变量的正确写法
if [ ! -f "$course_code" ]; then :
    echo "File <$course_code> does not exist."
fi


if [ "$#" -ne 1 ]; then  ## 🌟 参数无效如何判断: 如果参数个数不为1，则输出
    echo "Usage: $0 <course code>"
    exit 1
fi

if echo "$course_code" | grep -E "^[A-Z]{4}[0-9]{4}$" > /dev/null; then :
else
    echo "Invalid course code: $course_code"
    exit 1
fi

echo "Valid course code: $course_code"