#!/bin/dash

#所有的传参数都会涉及到test检查传惨是否报错，test主要的考点
if test "$#" -ne "1"; then ## -ne "1" 参数是否为1
        echo "Usage: $0 <course prefix>"
        exit 1
fi

# if test "$#" -ne "1"; then
#         echo "Usage: $0 <course prefix>"
#         exit 1
# fi

## 这里获取前缀 命名为prefix
prefix="$1"


if echo "$prefix" | grep -E "[A-Z]{4}" > /dev/null; then : #to send any unwanted output from program/command
else
        echo "Invalid course prefix: ${prefix}"
        exit 1
fi

#-----
# if #condition; then :
# fi

# #或者是
# if #condition; then :
# else
# fi
#-----
prefix="$1"
if echo "$prefix"|grep -E "[A-Z]{4}" >/dev/null; then :
else 
        echo "Invalid course prefix: ${prefix}"
        exit 1
fi

# grep -o 只是输出了匹配部分
curl --location --silent "http://www.timetable.unsw.edu.au/2024/${prefix}KENS.html" |
grep -oE "${prefix}[0-9]{4}\.html\">(.*)</a>" |
# 只输出这些
# VISN1101.html">VISN1101</a>
# VISN1101.html">Seeing the World: Perspectives from Vision Science</a>
# VISN1111.html">VISN1111</a>
# ...
#-v 反选 为了去掉：VISN5531.html">VISN5531
grep -vE ">${prefix}" |
# 去掉</a>
# 替换"> 为空 s/旧的/新的 /
sed 's/<\/a>//;s/.html\">/ /' |
sort |
uniq