n = int(input())
rest = 0
res = 0
for i in range(1, n + 1):
    a = int(input())
    if a == 0:
        rest = 0
    else:
        res += (rest + a) // 2
        rest = (rest + a) % 2
print(res)
