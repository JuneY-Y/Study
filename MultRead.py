import glob
for file in glob.glob("*.txt"):
    with open(file) as f:
        text=f.read()

print(text)
