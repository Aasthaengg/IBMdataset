from collections import Counter
w = input()

c = Counter(w)

for i, v in c.items():
    if v % 2 == 0:
        continue
    else:
        print('No')
        exit()

print('Yes')
