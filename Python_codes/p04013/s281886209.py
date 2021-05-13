from collections import defaultdict

n, a = map(int, input().split())
arr = [x-a for x in list(map(int, input().split()))]

dct = defaultdict(int)
dct[0] = 1

for x in arr:
    for k, v in list(dct.items()):
        dct[k+x] += v

print(dct[0]-1)