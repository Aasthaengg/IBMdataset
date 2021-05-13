w = input()
d = {}
for s in w:
    if d.get(s, -1) == -1:
        d[s] = 1
    else:
        d[s] += 1
good = True
for key in d:
    if d[key] % 2 != 0:
        good = False
        break
print('Yes' if good else 'No')

