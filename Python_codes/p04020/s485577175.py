N = int(input())
A = [int(input()) for _ in range(N)]
A.append(0)

ans = 0
for i in range(N):
    ans += A[i]//2
    if A[i]&1 and A[i+1]:
        A[i+1] -= 1
        ans += 1

print(ans)