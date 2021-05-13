import collections

n, a = map(int, input().split())
ls = sorted([x - a for x in map(int, input().split())])
counter = collections.Counter()
for x in ls:
    for k, v in list(counter.items()):
        counter[k + x] = counter[k + x] + v
    counter[x] += 1
print(counter[0])