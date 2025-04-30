# ✅ 1. *args — Variable-length positional arguments

# 🗣️ English explanation:

# *args allows you to pass any number of positional arguments (those without keyword names) to a function.

# 📦 It collects them into a tuple.

def add_all(*args):
    total = 0
    for number in args:
        total += number
    return total

print(add_all(1, 2, 3))      # 6
print(add_all(10, 20, 30, 40))  # 100