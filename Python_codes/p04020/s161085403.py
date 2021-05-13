N, *A = map(int, open(0).read().split())

ans = 0
cnt = 0
for i in range(N):
    if A[i] > 0:
        cnt += A[i]
    else:
        ans += cnt // 2
        cnt = 0
else:
    ans += cnt // 2

print(ans)
