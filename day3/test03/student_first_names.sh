#!/bin/dash
# 完全正确，考试的时候这个题是没有坑的
cut -d "|" -f2,3|sort -n|uniq|cut -d "," -f2|cut -d ' ' -f2|sort|sed "s/ //"