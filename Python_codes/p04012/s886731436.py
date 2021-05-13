from collections import Counter
w = input()
c = Counter(w)
li = set(list(w))
for i in li:
    if int(c[i]) % 2 != 0:
        print("No")
        exit()
print("Yes")