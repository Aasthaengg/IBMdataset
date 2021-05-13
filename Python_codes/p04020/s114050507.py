N = int(input())
A = [int(input()) for _ in range(N)]

ans = 0
for i in range(N-1):
    ans += A[i]//2
    A[i] %= 2
    if A[i] <= A[i+1]:
        ans += A[i]
        A[i+1] -= A[i]
ans += A[N-1]//2

print(ans)