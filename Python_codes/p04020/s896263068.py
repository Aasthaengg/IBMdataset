N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

cnt = 0
for i in range(N):
    if i > 0:
        if A[i - 1] == 1 and A[i] > 0:
            A[i] -= 1
            cnt += 1
            A[i - 1] -= 1
    cnt += A[i] // 2
    A[i] %= 2

print(cnt)
