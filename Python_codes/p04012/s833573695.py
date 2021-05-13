from collections import Counter
w = Counter(list(input()))
f = True
for k, v in w.items():
    if v % 2 == 1:
        f = False
print("Yes" if f else "No")
