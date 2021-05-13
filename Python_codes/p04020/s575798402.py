N = int(input())
A = [int(input()) for i in range(N)]
ans = 0
for i in range(N):
    tmp = A[i]
    ans += (tmp // 2)
    if i < N -1 and tmp % 2 and A[i + 1] > 0:
        ans += 1
        A[i + 1] -= 1
print(ans)