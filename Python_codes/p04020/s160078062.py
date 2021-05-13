n = int(input())
cur = 0
res = 0
for _ in range(n):
    x = int(input())
    if x == 0:
        res += cur // 2
        cur = 0
    else:
        cur += x
res += cur // 2
print(res)

