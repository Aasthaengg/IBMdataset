#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys


def get_ints():
    return map(int, sys.stdin.readline().strip().split())


def _main():
    input()
    an = list(get_ints())

    t = 0
    old = 1000000000
    while 1:
        ans = sq(t, an)
        g = sq(t+1, an) - ans
        t -= g / abs(g)
        if old > ans:
            old = ans
        else:
            break
    print(int(old))


def sq(t, an):
    ans = 0
    for ai in an:
        ans += pow(ai - t, 2)
    return ans


if __name__ == "__main__":
    _main()
