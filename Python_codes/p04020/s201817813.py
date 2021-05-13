N = int(input())
A = [int(input()) for i in range(N)]

ans = 0
for i in range(N):
    if A[i] >= 2:
        ans += A[i]//2
        A[i] -= (A[i]//2)*2
    if i != N-1:
        if A[i] == 1 and A[i+1] >= 1:
            A[i] = 0
            A[i+1] -= 1
            ans += 1
print(ans)

