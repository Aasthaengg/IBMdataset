N = int(input())
A = [int(input()) for _ in range(N)]

r = 0
ans = 0
for i in range(N):
    if r == 1:
        if A[i] != 0:
            A[i] += 1
        else:
            r = 0
    ans += A[i]//2
    r = A[i]%2

print(ans)