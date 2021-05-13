from collections import Counter

W = input()
C = Counter(W)

for v in C.values():
    if v % 2:
        print("No")
        exit()
print("Yes")
