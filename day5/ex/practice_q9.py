#!/usr/bin/env python3
'''
✅ 对文件按行处理、按长度拆分、优先按空格断行，最后把结果写回文件。
	•	特殊条件：比如“不超过 n 不用改”“无空格不改”
	•	优先级：比如先按前 n 个找空格，找不到再全行找

'''
import sys
#which takes two command line argument, n and name of a file
n=int(sys.argv[1])
filename=sys.argv[2]
# in question: should change the file
#sample: script m file.txt 因此需要open file,要全部读取每个line。记录为readlines()
with open(filename, 'r') as f:
    lines=f.readlines()
#a maximum desired line length,这里为什么用list而不是set呢？
new_lines=[]
#for loop 处理line结尾的'\n' 防止分割时候的干扰
for line in lines:
    line=line.rstrip('\n')
#当len(line)的长度是>n的时候，就是符合题意的处理
    while len(line)>n:
        if ' ' not in line: # lines not containing a space character ' ' should not be changed
            new_lines.append(line) #直接在new_lines里添加整个line即可
            break
        #这里需要进行的是把处理好的line的前n行放入一个front的容器里
        front=line[:n]

        if ' ' in front:
            split_index=front.rfind(' ') #rfind不熟悉，用rfind实现按单词换行的环节
            new_lines.append(line[:split_index])
            line=line[split_index+1:]
#left_part = line[:index]        # 前半段，不包含 index 本身
#right_part = line[index + 1:]   # 后半段，跳过 index 自身的字符
        else:
            split_index=line.find(' ')
            new_lines.append(line[:split_index])
            line=line[split_index+1:]
    if len(line)<=n:
        new_lines.append(line)
        #因为去创建，因此还需要再次写回这个文件里才可以
with open(filename, 'w') as f:
    for l in new_lines:
        f.write(l + '\n')