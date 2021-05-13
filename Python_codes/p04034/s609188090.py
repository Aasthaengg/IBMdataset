# https://atcoder.jp/contests/agc002/tasks/agc002_b
import sys
input = sys.stdin.buffer.readline

n, m = [int(i) for i in input().split()]

count = [1] * (n + 1)  # 1-indexed
have_red = [0] * (n + 1)  # 1-indexed
have_red[1] = 1
for _ in range(m):
    x, y = [int(i) for i in input().split()]
    if have_red[x]:
        have_red[y] = 1
    count[x] -= 1
    count[y] += 1
    if count[x] == 0:
        have_red[x] = 0

ans = sum(have_red)

print(ans)
