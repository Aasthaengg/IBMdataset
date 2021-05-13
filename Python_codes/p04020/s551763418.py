n = int(input())
A = [int(input()) for i in range(n)]

ans = 0
for i in range(n):
    m = A[i] // 2
    ans += m
    A[i] -= 2*m
    if i <= n-2 and min(A[i], A[i+1]) == 1:
        ans += 1
        A[i] -= 1
        A[i+1] -= 1
print(ans)