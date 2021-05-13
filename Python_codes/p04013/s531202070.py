import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, a = list(map(int, readline().split()))
    x = list(map(int, readline().split()))
    for i in range(n):
        x[i] -= a
    ls = [0] * 5010
    ls[2500] = 1
    for v in x:
        if v == 0:
            for i in range(5010):
                ls[i+v] += ls[i]
        elif v > 0:
            for i in range(5009 - v, -1, -1):
                ls[i+v] += ls[i]
        elif v < 0:
            for i in range(5009 + v):
                ls[i+v] += ls[i]
    print(ls[2500] - 1)


if __name__ == '__main__':
    solve()
