import sys
N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]
ans = 0
for i in range(1, N):
    ans += (A[i - 1] + A[i]) // 2
    if A[i]:
        A[i] = (A[i - 1] + A[i]) % 2
print(A[0] // 2 if N == 1 else ans)