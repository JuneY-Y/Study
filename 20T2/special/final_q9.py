#!/usr/bin/env python3
'''
给定一个文件目录，
用python去读取整个文件目录的结构 
生成对应的linux命令  输出到saved.sh

执行./saved.sh的时候 会生成一个跟原来一模一样的文件目录
'''

import os
import sys

# sys.argv[1] 是传入的文件夹路径
# 开始遍历目录结构
for root, dirs, files in os.walk(sys.argv[1]):

    # 处理目录
    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)
        print(f'test -d "{dir_path}" || mkdir "{dir_path}"')

    # 处理文件
    for file_name in files:
        file_path = os.path.join(root, file_name)
        with open(file_path) as file:
            print(f'test -f "{file_path}" || echo -n "{file.read()}" > "{file_path}"')