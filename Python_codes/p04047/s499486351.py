# -*- coding: utf-8 -*-
"""
A - BBQ Easy
https://atcoder.jp/contests/agc001/tasks/agc001_a

"""
import sys


def solve(N, L):
    ans = 0
    while L:
        a = L.pop()
        b = L.pop()
        ans += min(a, b)
    return ans


def main(args):
    N = int(input())
    L = sorted(map(int, input().split()))
    ans = solve(N, L)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])