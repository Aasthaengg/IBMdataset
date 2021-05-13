N, *A = map(int, open(0).read().split())
ans = 0
for i in range(N):
    q, r = divmod(A[i], 2)
    ans += q
    if r == 0 or i == N - 1:
        continue
    elif A[i + 1] != 0:
        A[i + 1] += 1
print(ans)
