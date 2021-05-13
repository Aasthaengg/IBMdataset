n = int(input())
A = [int(input()) for _ in range(n)]
ans = 0
for i in range(n-1):
    p,r = divmod(A[i], 2)
    A[i] = r
    ans += p
    if A[i]*A[i+1]:
        A[i+1] -= 1
        ans += 1
print(ans+A[-1]//2)