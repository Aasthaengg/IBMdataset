n = int(input())
A = list(int(input()) for _ in range(n))
ans = 0
for i in range(n):
    tmp = A[i]
    ans += (tmp//2)
    if i < n-1 and tmp %2 and A[i+1] > 0:
        ans += 1
        A[i+1] -= 1
print(ans)