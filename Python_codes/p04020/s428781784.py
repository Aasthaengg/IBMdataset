N = int(input())
A = [int(input()) for i in range(N)]
count = A[0]//2
A[0] %= 2
for i in range(1,N):
    if A[i] == 0:
        continue
    if A[i-1] != 0:
        count += 1
        A[i] -= 1
    count += A[i]//2
    A[i] %= 2
print(count)
