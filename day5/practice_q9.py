#!/usr/bin/env python3
'''
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
        #需要进行
        front=line[:n]
        if ' ' in front:
            split_index=front.rfind(' ') #rfind不熟悉
            new_lines.append(line[:split_index])
            line=line[split_index+1:]
        else:
            split_index=line.find(' ')
            new_lines.append(line[:split_index])
            line=line[split_index+1:]
    if len(line)<=n:
        new_lines.append(line)
with open(filename, 'w') as f:
    for l in new_lines:
        f.write(l + '\n')