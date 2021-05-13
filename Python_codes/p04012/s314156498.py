from collections import Counter
w = Counter(input())
for i in w.values():
    if i&1:
        print("No")
        break
else:
    print("Yes")