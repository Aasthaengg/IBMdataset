import sys
import collections


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, l = list(map(int, readline().split()))
    a = collections.deque(list(map(int, readline().split())))
    for i in range(1, n):
        if a[i] + a[i-1] >= l:
            print("Possible")
            for j in range(1, i):
                print(j)
            for j in range(n - 1, i, -1):
                print(j)
            print(i)
            exit()
    print("Impossible")


if __name__ == '__main__':
    solve()
