N,*A = map(int, open(0).read().split())
ans = 0
cum = 0
for i in range(N):
    if A[i] > 0:
        cum += A[i]
    else:
        ans += cum // 2
        cum = 0
print(ans+cum//2)