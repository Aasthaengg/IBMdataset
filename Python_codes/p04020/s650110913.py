N = int(input())
A = [int(input()) for _ in range(N)]

n = 0
ans = 0
for i in range(N):
    if A[i]:
        n += A[i]
    else:
        ans += n//2
        n = 0
ans += n//2

print(ans)
