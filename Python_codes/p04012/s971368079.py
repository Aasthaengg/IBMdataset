from collections import Counter
w = list(input())
c = Counter(w)
f = True
for i in list(c.values()):
    if i % 2 == 1:
        f = False
        break

if f:
    print("Yes")
else:
    print("No")
