import sys
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
may_contain_red = [0 for _ in range(n + 1)]
num_of_ball = [1 for _ in range(n + 1)]
may_contain_red[1] = 1
for i in range(m):
    x, y = map(int, input().split())
    num_of_ball[x] -= 1
    num_of_ball[y] += 1
    if may_contain_red[x] != 0:
        may_contain_red[y] = 1
    if num_of_ball[x] == 0:
        may_contain_red[x] = 0

print(sum(may_contain_red))
