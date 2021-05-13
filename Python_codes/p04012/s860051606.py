w = input()
chars = []
for c in w:
    chars.append(c)

cset = set(chars)

beautiful = True
for c in cset:
    if chars.count(c) % 2 != 0:
        beautiful = False
        break

if beautiful:
    print('Yes')
else:
    print('No')