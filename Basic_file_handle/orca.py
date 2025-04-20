import sys, re

with open(sys.argv[1:], "r") as f:
    for line in line:
        words=line.strip().split() ##这里我需要提取第三行，动物名称。不会写了
        animal_name=" ".join(words[2:])
        if animal_name=="Orca":
            count=int(words[1])
            count=+ count
            
        
