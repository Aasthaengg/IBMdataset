import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
red = [0] * (N + 1)
white = [1] * (N + 1)
red[1] = 1
white[1] = 0

for _ in range(M):
    x, y = map(int, input().split())
    if red[x]:
        red[y] += 1
    else:
        white[y] += 1
    if white[x]:
        white[x] -= 1
    else:
        red[x] -= 1

print(N-red[1:].count(0))