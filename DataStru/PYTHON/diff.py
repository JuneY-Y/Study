import os
import sys
# import filecmp
'''
调用了.exists库进行查看
用line进行查看是否相同
'''
file1="diff_1.txt"
file2="diff_2.txt"

if not (os.path.exists(file1) and os.path.exists(file2)):
    print("no file exit")
    sys.exit(1)

#method1 : readlines()函数进行比较
# with open(file1, 'r') as f1, open(file2, 'r') as f2:
#     lines1=f1.readlines()
#     lines2=f2.readlines()

##method 2: 逐行比较
def compare():
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line_num, (line1, line2) in enumerate(zip(f1, f2), 1):
            if line1 != line2:
                print(f"Files differ at line {line_num}")
                sys.exit(0)

    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        if sum(1 for _ in f1) != sum(1 for _ in f2):
            print("Files differ in Length")
            sys.exit(0)

    print("same file")

compare()


