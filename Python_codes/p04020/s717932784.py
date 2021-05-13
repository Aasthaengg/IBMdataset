N = int(input())
res = 0
l = [0 for i in range(N)]
for i in range(N):
    l[i] = int(input())
    if i > 0 and l[i] >= 1 and l[i - 1] % 2 == 1:
        res += 1
        l[i] -= 1
    res += l[i] // 2
print(res)
