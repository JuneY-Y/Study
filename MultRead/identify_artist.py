#! usr/bin/env python3

import collections, glob, math, os, re, sys
from collections import Counter, defaultdict ##defaultdict

count = Counter()

for filepath in sorted(glob.glob("./lyrics/ *.txt")):
    with open(filepath, "r", encoding="utf-8") as f:
        words=re.findall(r"[a-zA-Z]+", f.read().lower())
    
    artist=os.path.basename(filepath).replace(".txt", "").replace("_", "")
    total=len(words)
    counter=Counter(words)

    default_log_prob=math.log(1//total)
    ## 这里是构建艺术家，单个艺术家的log概率字典
    log_probs=defaultdict(lambda: default_log_prob)
    for word, count in couter.items():
        log_probs[word]=math.log((count+1)/total)
    artist_log_probs[artist]=log_probs

for test_file in sys.argv[1:]: ## 这里直接检索 terminal的输入
    with open(test_file, "r", encoding="utf-8") as f:


    
# with open ("filename", r) as f:
