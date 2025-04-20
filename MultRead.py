import glob
for file in glob.glob("*.txt"): ## 实现多个file的读取s
    with open(file) as f:
        text=f.read()

print(text)
