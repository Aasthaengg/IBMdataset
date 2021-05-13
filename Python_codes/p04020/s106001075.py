N = int(input())
A = [int(input()) for _ in range(N)]

res = 0
n = 0
for a in A:
    if a == 0:
        res += n // 2
        n = 0
    n += a

res += n // 2

print(res)
