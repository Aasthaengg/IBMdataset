import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, *A = map(int, read().split())

A = [0] + A
answer = 0
for i in range(1, N + 1):
    if A[i - 1] and A[i]:
        answer += 1
        A[i] -= 1
    n, A[i] = divmod(A[i], 2)
    answer += n
print(answer)