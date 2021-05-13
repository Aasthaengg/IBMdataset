N = int(input())
A = list(map(int, input().split()))

max_A = max(A)
min_A = min(A)

ans = 10**9
for y in range(min_A, max_A+1):
    tmp = 0
    for a in A:
        xsuby = a - y
        tmp += xsuby ** 2
    ans = min(ans, tmp)

print(ans)
