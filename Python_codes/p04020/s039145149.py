N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

ans = 0
for i in range(N):
    ans += A[i] // 2
    A[i] = A[i] % 2
    if A[i] == 1 and i + 1 < N and A[i + 1] > 0:
        ans += 1
        A[i] -= 1
        A[i + 1] -= 1

print(ans)