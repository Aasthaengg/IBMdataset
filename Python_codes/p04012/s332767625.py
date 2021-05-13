import collections

w = input()
flag = True
for i in collections.Counter(w).values():
    if i % 2 != 0:
        print('No')
        flag = False
        break
if flag:
    print('Yes')