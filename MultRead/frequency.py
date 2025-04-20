import sys, re
import glob
from collections import Counter
'''
<出现次数>/<总词数> = <频率> <歌手名>
'''
count_words=Counter()
for file in glob.glob("/lyrics *.txt"): ## 需要带“”
    with open(file,"r") as f:
        for word in sys.stdin:
            if 


    