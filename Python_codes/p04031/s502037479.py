n = int(input())
a = list(map(int, input().split()))

res = float('inf')
for i in range(-100, 101):
    s = 0
    for v in a:
        s += (v - i) ** 2
    res = min(res, s)

print(res)