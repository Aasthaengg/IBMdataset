import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M = map(int, readline().split())
m = map(int, read().split())

count = [1] * (N+1)
red = [0] * (N+1)
red[1] = True
for x, y in zip(m, m):
    count[x] -= 1
    count[y] += 1
    if red[x]:
        red[y] = 1
    if not count[x]:
        red[x] = 0

print(sum(red))