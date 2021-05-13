from sys import exit

w = input()

d = dict()
for c in w:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1

for v in d.values():
    if v % 2 == 1:
        print('No')
        exit()

print('Yes')