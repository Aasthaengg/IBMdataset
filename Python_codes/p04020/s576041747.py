n = int(input())
A = [int(input()) for _ in range(n)]
ans = 0
for i in range(n-1):
    x,y = A[i], A[i+1]
    ans += x//2
    if x%2!=0 and y > 0:
        ans += 1
        A[i+1] -= 1
ans += A[-1]//2

print(ans)