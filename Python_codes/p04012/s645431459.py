import collections
w = list(input())

lis = collections.Counter(w)

for key, value in lis.items():
    if value % 2 != 0:
        print('No')
        exit()

print('Yes')