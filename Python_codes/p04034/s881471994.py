import sys


def input():
    return sys.stdin.readline()[:-1]


N, M = map(int, input().split())

red = [0]*N
red[0] = 1
box = [1]*N
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    if red[x] == 1 and box[x] == 1:
        # 箱Xには赤玉がある可能性があって、全ボール数が1個のみがある場合
        red[x] -= 1
        red[y] = 1
    elif red[x] == 1 and box[x] >= 2:
        # 箱Xには赤玉がある可能性があって、全ボール数が2個以上ある場合
        red[y] = 1
    box[x] -= 1
    box[y] += 1

print(red.count(1))
