import collections
w = input()
cw = collections.Counter(w)
for val in cw.values():
    if val%2 == 1:
        print('No')
        exit()
print('Yes')
