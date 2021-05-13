N = int(input())
A = [0] + [int(input()) for _ in range(N)]

ans = 0
for i in range(1,N+1):
    if A[i] != 0:
        ans += A[i-1]
        A[i] -= A[i-1]
    ans += A[i]//2
    A[i] = A[i]%2

print(ans)
