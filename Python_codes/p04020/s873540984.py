import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = []
    for _ in range(N):
        a = int(input())
        A.append(a)

    B = []
    C = []
    for a in A:
        if a != 0:
            C.append(a)
        else:
            B.append(C)
            C = []
    if len(C) > 0:
        B.append(C)

    res = 0
    for b in B:
        res += sum(b) // 2
    print(res)


if __name__ == '__main__':
    main()
