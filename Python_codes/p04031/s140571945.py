n = int(input())
a = list(map(int, input().split()))
cmin = ((max(a) - min(a)) ** 2) * n
for x in range(min(a), max(a) + 1):
    c = 0
    for i in a:
        c += (i - x) ** 2
    cmin = min(c, cmin)
print(cmin)
