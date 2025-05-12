cut -d '|' -f2,3 "enrollments.txt"|sort -f|uniq -i|sed 's/^ *//'|cut -d '|' -f2|cut -d ' ' -f2|sort


## 心得： 这里是需要一步一步的cut 
#并且用到了sed进行去掉最前面的空格 s/^ *//