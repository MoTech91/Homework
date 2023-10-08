from collections import Counter

s = "Hello, World!"
counter = Counter(s)

for char, count in counter.items():
    print(f"'{char}': {count}")