import os
import sys
import filecmp
'''
调用了.exists库进行查看
用line进行查看是否相同
'''
file1="diff_1.txt"
file2="diff_2.txt"

if not (os.path.exists(file1) and os.path.exists(file2)):
    print("no file exit")
    sys.exit(1)

with open(file1, 'r') as f1, open(file2, 'r') as f2:
    lines1=f1.readlines()
    lines2=f2.readlines()

if lines1==lines2:
    print("same file")
else:
    print("different file")