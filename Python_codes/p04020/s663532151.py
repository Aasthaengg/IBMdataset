N = int(input())
A = [0] + [int(input()) for _ in range(N)]

ans = 0
for i in range(1, N + 1):
    cnt = A[i-1] + A[i]
    if cnt % 2 == 1 and cnt > 1:
        A[i-1],A[i] = 0,1
    elif cnt % 2 == 0:
        A[i] = 0
    ans += cnt // 2

print(ans)