import sys
def I(): return int(sys.stdin.readline().rstrip())


N = I()
A = [I() for _ in range(N)]

ans = 0
for i in range(N):
    a = A[i]
    ans += a//2
    A[i] -= 2*(a//2)
    if A[i] == 1 and i < N-1 and A[i+1] >= 1:
        ans += 1
        A[i] = 0
        A[i+1] -= 1

print(ans)
